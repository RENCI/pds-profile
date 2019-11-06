import requests

json_headers = {
    "Accept": "application/json"
}

def test_api():
    result=requests.get("http://pdsprofile:8080/profile?patient_id=1000&model=m&timestamp=2019-10-19T00:00:00Z&phenotype_mapping_plugin_id=pm&model_plugin_id=mp&data_provider_plugin_id=dp", headers=json_headers, verify=False)
    print(result.content)
    assert result.status_code == 200
                
    assert result.json() == [{
        "value": "a0",
        "calculation": "c0",
        "certitude": 0,
        "description": "f0",
        "title": "t0",
        "clinical_feature_variable": "v0",
        "quantity": "q0",
        "timestamp": "ts0"
    }, {
        "value": "a1",
        "calculation": "c1",
        "certitude": 1,
        "description": "f1",
        "title": "t1",
        "clinical_feature_variable": "v1",
        "quantity": "q1",
        "timestamp": "ts1"
    }, {
        "value": "a2",
        "calculation": "c2",
        "certitude": 2,
        "description": "f2",
        "title": "t2",
        "clinical_feature_variable": "v2",
        "quantity": "q2",
        "timestamp": "ts2"
    }]
    
