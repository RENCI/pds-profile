import os
import requests
import sys
from tx.utils import get, post
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
            }
        },
        "required": [
            "clinical_feature_variable",
            "description",
            "title"
        ]
    }
}

def profile(patient_id, model, model_plugin_id, phenotype_mapping_plugin_id, data_provider_plugin_id, timestamp):
    url = f"{pds_url_base}/{model_plugin_id}/clinical_feature_variables?model={model}"
    resp1 = get(url, schema=cfv_schema)
    if isinstance(resp1, Left):
        return resp1.value
    clinical_feature_variable_objects = resp1.value

    def cfvo_to_cfvo2(cfvo):
        cfvo2 = {
            "clinical_feature_variable": cfvo["clinical_feature_variable"]
        }
        unit = cfvo.get("unit")
        if unit is not None:
            cfvo2["unit"] = unit
        return cfvo2
    
    cfvos2 = map(cfvo_to_cfvo2, clinical_feature_variable_objects)

    url = f"{pds_url_base}/{phenotype_mapping_plugin_id}/mapping?patient_id={patient_id}&data_provider_plugin_id={data_provider_plugin_id}&timestamp={timestamp}"
    print(f"url = {url}")
    resp2 = post(url, json=url)
    if isinstance(resp2, Left):
        return resp2.value
    value_objects = resp2.value
    print(f"value_objects = {value_objects}")
    sys.stdout.flush()

    profile = [{
        "clinical_feature_variable": clinical_feature_variable_object["clinical_feature_variable"],
        "description": clinical_feature_variable_object["description"],
        "title": clinical_feature_variable_object["title"],
        "unit": clinical_feature_variable_object.get("unit"),
        "value": value_object["value"],
        "calculation": value_object["calculation"],
        "certitude": value_object["certitude"],
        "quantity": value_object.get("quantity"),
        "timestamp": value_object.get("timestamp")
    } for value_object, clinical_feature_variable_object in zip(value_objects, clinical_feature_variable_objects)]

    return profile
            
        
