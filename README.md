# snapshot-analyzer-301
AWS EBS Snapshot Analyzer

## About

This is a demo project to learn how to manage ec2 snapshots using boto3

## Configuration

snapshot uses the config file created by the AWS cli. e.g.

`aws configure --profile snapshot`

## Running

`pipenv run python .\shotty\shotty.py` <command> <--project=PROJECT>
*command* is list, stop, or start
*project* is optional
