clinical_feature_variables = [
    {
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
    }
]

phenotypes = {
    "1000": [{
        "value": "a0",
        "unit": "u0",
        "certitude": 0,
        "calculation": "c0",
    }, {
        "value": "a1",
        "unit": "u1",
        "certitude": 1,
        "calculation": "c1",
    }, {
        "value": "a2",
        "unit": "u2",
        "certitude": 2,
        "calculation": "c2",
    }]
}

def get_clinical_feature_variables():
    return clinical_feature_variables

def get_phenotype(patient_id, data_provider_plugin_id, timestamp, body):
    ps = phenotypes.get(patient_id)
    if ps is None:
        return (404, "Not Found")
    else:
        for p, cfv in zip(ps, clinical_feature_variables):
            cus = [a for a in body if a["clinical_feature_variable"] == cfv["clinical_feature_variable"]]
            if len(cus) > 0:
                q = cus[0]
                if "unit" in q:
                    p["unit"] = q["unit"]
        return ps






