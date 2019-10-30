import os
import requests
import sys
from jsonschema import validate

pds_host = os.environ["PDS_HOST"]
pds_port = os.environ["PDS_PORT"]
pds_url_base = f"http://{pds_host}:{pds_port}/plugin"
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
    resp1 = requests.get(f"{pds_url_base}/{model_plugin_id}/clinical_feature_variables?model={model}")
    status_code = resp1.status_code
    if status_code != 200:
        return resp1.text, status_code
    clinical_feature_variable_objects = resp1.json()
    validate(clinical_feature_variable_objects, cfv_schema)
    profile = []
    for clinical_feature_variable_object in clinical_feature_variable_objects:
        clinical_feature_variable = clinical_feature_variable_object["clinical_feature_variable"]
        description = clinical_feature_variable_object["description"]
        title = clinical_feature_variable_object["title"]
        url = f"{pds_url_base}/{phenotype_mapping_plugin_id}/mapping?patient_id={patient_id}&clinical_feature_variable={clinical_feature_variable}&data_provider_plugin_id={data_provider_plugin_id}&timestamp={timestamp}"
        print(f"url = {url}")
        resp2 = requests.get(url)
        value_object = resp2.json()
        print(f"value_object = {value_object}")
        sys.stdout.flush()
        profile.append({
            "clinical_feature_variable": clinical_feature_variable,
            "description": description,
            "title": title,
            "value": value_object["value"],
            "calculation": value_object["calculation"],
            "certitude": value_object["certitude"]
        })
    return profile
            
        
