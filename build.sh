#!/bin/bash
docker build . -t pds-profile:0.1.0
docker tag pds-profile:0.1.0 zooh/pds-profile:0.1.0
docker push zooh/pds-profile:0.1.0
