import os
import requests
import sys

pds_host = os.environ["PDS_HOST"]
pds_port = os.environ["PDS_PORT"]
pds_url_base = f"http://{pds_host}:{pds_port}/plugin"

def profile(patient_id, model, model_plugin_interface, phenotype_mapping_plugin_interface, data_provider_plugin_interface, timestamp):
    resp1 = requests.get(f"{pds_url_base}/{model_plugin_interface}/clinical_feature_variables?model={model}")
    clinical_feature_variable_objects = resp1.json()
    profile = []
    for clinical_feature_variable_object in clinical_feature_variable_objects:
        clinical_feature_variable = clinical_feature_variable_object["clinical_feature_variable"]
        description = clinical_feature_variable_object["description"]
        url = f"{pds_url_base}/{phenotype_mapping_plugin_interface}/mapping?patient_id={patient_id}&clinical_feature_variable={clinical_feature_variable}&data_provider_plugin_interface={data_provider_plugin_interface}&timestamp={timestamp}"
        print(f"url = {url}")
        resp2 = requests.get(url)
        value_object = resp2.json()
        print(f"value_object = {value_object}")
        sys.stdout.flush()
        profile.append({
            "clinical_feature_variable": clinical_feature_variable,
            "description": description,
            "value": value_object["value"],
            "calculation": value_object["calculation"],
            "certitude": value_object["certitude"]
        })
    return profile
            
        
