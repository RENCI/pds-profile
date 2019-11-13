clinical_feature_variables = {
    "m": [{
        "clinical_feature_variable": "v0",
        "description": "f0",
        "title": "t0"
    }, {
        "clinical_feature_variable": "v1",
        "description": "f1",
        "title": "t1"
    }, {
        "clinical_feature_variable": "v2",
        "description": "f2",
        "title": "t2"
    }]
}

phenotypes = {
    "1000": [{
        "value": "a0",
        "certitude": 0,
        "calculation": "c0",
    }, {
        "value": "a1",
        "certitude": 1,
        "calculation": "c1",
    }, {
        "value": "a2",
        "certitude": 2,
        "calculation": "c2",
    }]
}

def get_clinical_feature_variables(model):
    return clinical_feature_variables.get(model, (404, "Not Found"))

def get_phenotype(patient_id, data_provider_plugin_id, timestamp, body):
    return phenotypes.get(patient_id, (404, "Not Found"))





