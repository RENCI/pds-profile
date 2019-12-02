import os
import requests
import sys
from tx.requests.utils import get, post
from oslash import Left, Right

pds_host = os.environ["PDS_HOST"]
pds_port = os.environ["PDS_PORT"]
pds_url_base = f"http://{pds_host}:{pds_port}/v1/plugin"
cfv_schema = {
    "type": "array",
    "items": {
        "type": "object",
        "properties": {
            "clinical_feature_variable": {
                "type": "string"
            },
            "description": {
                "type": "string"
            },
            "title": {
                "type": "string"
            },
            "unit": {
                "type": "string"
            }
        },
        "required": [
            "clinical_feature_variable",
            "description",
            "title"
        ]
    }
}

def profile(patient_id, model_plugin_id, timestamp, body):
    phenotype_mapping_plugin_id = body["phenotype_mapping_plugin_id"]
    data_provider_plugin_id = body["data_provider_plugin_id"]
    custom_units = body.get("custom_units")
    url = f"{pds_url_base}/{model_plugin_id}/clinical_feature_variables"
    resp1 = get(url, schema=cfv_schema)
    if isinstance(resp1, Left):
        return resp1.value
    clinical_feature_variable_objects = resp1.value

    def cfvo_to_cfvo2(cfvo):
        cfv = cfvo["clinical_feature_variable"]
        cfvo2 = {
            "clinical_feature_variable": cfv
        }
        unit = cfvo.get("unit")
        if unit is not None:
            cfvo2["unit"] = unit
        elif custom_units is not None:
            cus = [a for a in custom_units if a["clinical_feature_variable"] == cfv]
            if len(cus) > 0:
                cfvo2["unit"] = cus[0]["unit"]
        return cfvo2
    
    cfvos2 = list(map(cfvo_to_cfvo2, clinical_feature_variable_objects))

    url = f"{pds_url_base}/{phenotype_mapping_plugin_id}/mapping?patient_id={patient_id}&data_provider_plugin_id={data_provider_plugin_id}&timestamp={timestamp}"
    print(f"url = {url}")
    resp2 = post(url, json=cfvos2)
    if isinstance(resp2, Left):
        return resp2.value
    value_objects = resp2.value
    print(f"value_objects = {value_objects}")
    sys.stdout.flush()

    profile = [{
        **clinical_feature_variable_object, **value_object
    } for value_object, clinical_feature_variable_object in zip(value_objects, clinical_feature_variable_objects)]

    return profile
            
        
