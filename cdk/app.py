#!/usr/bin/env python3
import calendar
import os
import time

import aws_cdk as cdk

from cdk.cdk_stack import CdkStack
from decouple import config

stack_name_mono = "AspenStackMono"
stack_name_scale = "AspenStackScale"
region = config('REGION')
account = config('ACCOUNT')

app = cdk.App()
CdkStack(app, stack_name_mono,
         # Get env variables
         env=cdk.Environment(account=account, region=region),
         mono=True
         )

CdkStack(app, stack_name_scale,
         # Get env variables
         env=cdk.Environment(account=account, region=region),
         mono=False
         )

app.synth()
