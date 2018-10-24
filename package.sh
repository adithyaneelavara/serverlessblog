#!/bin/bash
aws cloudformation package  --template-file template.yaml --output-template-file packaged.yaml   --s3-bucket build.adithyaneelavara.info