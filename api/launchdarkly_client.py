# launchdarkly_client.py
import os
from ldclient import LDClient, Config


ld_client = LDClient(Config(os.getenv("LAUNCHDARKLY_SDK_KEY")))
