#!/bin/bash

sam build --use-container --template sam.yml
sam deploy --config-file samconfig.toml