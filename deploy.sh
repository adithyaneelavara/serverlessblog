#!/bin/bash
aws cloudformation deploy --template-file ./packaged.yaml --capabilities CAPABILITY_IAM --stack-name serverlessblog