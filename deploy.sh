#!/bin/bash

rm -rf src.zip
zip -r src.zip src/

# aws s3 mb s3://sedric-ai-stack-app-artifact --region eu-west-3
aws s3 cp src.zip s3://sedric-ai-stack-app-artifact/src.zip

aws cloudformation package --template-file cloudformation.yml --s3-bucket sedric-ai-stack-app-artifact --output-template-file new-cloudformation.yml

# aws cloudformation delete-stack --stack-name sedric-ai-stack
# sleep 2
aws cloudformation deploy --template-file new-cloudformation.yml --stack-name sedric-ai-stack --capabilities CAPABILITY_IAM