#!/bin/bash
aws cloudformation deploy --template-file /Users/neurons/workspace/serverless/code/serverlessblog/serverlessblog/packaged.yaml --capabilities CAPABILITY_IAM --stack-name MySample