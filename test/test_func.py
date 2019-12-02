import requests

json_headers = {
    "Accept": "application/json"
}

def test_api():
    config={
        "phenotype_mapping_plugin_id": "pm",
        "data_provider_plugin_id": "dp"
    }
    result=requests.post("http://pdsprofile:8080/profile?patient_id=1000&timestamp=2019-10-19T00:00:00Z&model_plugin_id=mp", headers=json_headers, json=config)
    print(result.content)
    assert result.status_code == 200
                
    assert result.json() == [{
        "value": "a0",
        "unit": "u0",
        "calculation": "c0",
        "certitude": 0,
        "description": "f0",
        "title": "t0",
        "clinical_feature_variable": "v0",
    }, {
        "value": "a1",
        "unit": "u1",
        "calculation": "c1",
        "certitude": 1,
        "description": "f1",
        "title": "t1",
        "clinical_feature_variable": "v1",
    }, {
        "value": "a2",
        "unit": "u2",
        "calculation": "c2",
        "certitude": 2,
        "description": "f2",
        "title": "t2",
        "clinical_feature_variable": "v2",
    }]

def test_api_custom_units():
    config={
        "phenotype_mapping_plugin_id": "pm",
        "data_provider_plugin_id": "dp",
        "custom_units": [{
            "clinical_feature_variable": "v0",
            "unit": "u0p"
        }]
    }
    result=requests.post("http://pdsprofile:8080/profile?patient_id=1000&timestamp=2019-10-19T00:00:00Z&model_plugin_id=mp", headers=json_headers, json=config)
    print(result.content)
    assert result.status_code == 200
                
    assert result.json() == [{
        "value": "a0",
        "unit": "u0p",
        "calculation": "c0",
        "certitude": 0,
        "description": "f0",
        "title": "t0",
        "clinical_feature_variable": "v0",
    }, {
        "value": "a1",
        "unit": "u1",
        "calculation": "c1",
        "certitude": 1,
        "description": "f1",
        "title": "t1",
        "clinical_feature_variable": "v1",
    }, {
        "value": "a2",
        "unit": "u2",
        "calculation": "c2",
        "certitude": 2,
        "description": "f2",
        "title": "t2",
        "clinical_feature_variable": "v2",
    }]

