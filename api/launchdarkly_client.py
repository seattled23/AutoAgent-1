# launchdarkly_client.py
import os
from ldclient import LDClient
from ldclient.config import Config

ld_client = LDClient(Config(sdk_key=os.getenv("LAUNCHDARKLY_SDK_KEY")))
