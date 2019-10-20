import requests

json_headers = {
    "Accept": "application/json"
}

def test_api():
    result=requests.get("http://pdsprofile:8080/profile?patient_id=1000&model=m&timestamp=2019-10-19T00:00:00Z&phenotype_mapping_plugin_interface=pm&model_plugin_interface=mp", headers=json_headers)
    print(result.content)
    assert result.status_code == 200
                
    assert result.json() == [{
        "value": "a0",
        "calculation": "c0",
        "certitude": 0,
        "for": "f0",
        "clinical_feature_variable": "v0"
    }, {
        "value": "a1",
        "calculation": "c1",
        "certitude": 1,
        "for": "f1",
        "clinical_feature_variable": "v1"
    }, {
        "value": "a2",
        "calculation": "c2",
        "certitude": 2,
        "for": "f2",
        "clinical_feature_variable": "v2"
    }]
    
