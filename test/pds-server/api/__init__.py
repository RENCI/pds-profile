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
    "1000": {
        "v0": {
            "value": "a0",
            "certitude": 0,
            "calculation": "c0",
            "quantity": "q0",
            "timestamp": "ts0"
        }, "v1": {
            "value": "a1",
            "certitude": 1,
            "calculation": "c1",
            "quantity": "q1",
            "timestamp": "ts1"
        }, "v2": {
            "value": "a2",
            "certitude": 2,
            "calculation": "c2",
            "quantity": "q2",
            "timestamp": "ts2"
        }
    }
}

def get_clinical_feature_variables(model):
    return clinical_feature_variables.get(model, (404, "Not Found"))

def get_phenotype(patient_id, clinical_feature_variable, data_provider_plugin_id, timestamp):
    phenotype = phenotypes.get(patient_id)
    if phenotype is None:
        return 404, "Not Found"
    else:
        return phenotype.get(clinical_feature_variable, (404, "Not Found"))





