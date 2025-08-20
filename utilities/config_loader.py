import os
from pathlib import Path
import yaml
from dotenv import load_dotenv


#1. Class Initialization
# Creating a Config class to load and mange configs
#env parameter helps us to choose which section of the yaml configs to load from like common,sit,preprod etc
#ev=common -> default is common if nothing provided
class Config:
    def __init__(self, env="common"):
        #Loads secrets from .env file
#2. Load .env file
        env_path = Path(__file__).parent.parent/"Configs"/".env"
        # store the .env file path in a variable , fetch the path using Path class and __file__ function , .parent.parent is to go two levels up to the root and then get the Config folder then .env file
        load_dotenv(env_path)
        #Reads the .env file and stores its variables in the system environment.
#3. Load YAML file
        config_path = Path(__file__).parent.parent/"Configs"/"config.yaml"
        with open(config_path, "r") as f:
            self.data = yaml.safe_load(f) #DOUBT
        # Opens the config.yaml file in read mode, yaml.safeloads(f) parses the yaml content into a Python Dictionary (self.data)
        """ Sample self.data is : 
        {"common": {"env_url": "...", "headers": {...}},
         "sit" : {"env_url": "...", "headers": {...}},
         "preprod" : {"env_url": "...", "headers": {...}}}"""
        self.env = env #DOUBT
        #Saves the chosen environment name (comon, sit, preprod) for later use in property methods.

    #Property Methods
    #These make your config values accessible like attributes, not like dictionary lookups.

    @property
    def env_url(self):
        return self.data[self.env]["env_url"]

    @property
    def headers(self):
        return self.data[self.env]["headers"]

    @property
    def foodhub_api_token(self):
        return os.getenv("FOODHUB_API_TOKEN") #from .env
            # Retrieves the FOODHUB_API_TOKEN  from environment variables (loaded earlier from .env).
    @property
    def app_name(self):
        return self.data[self.env]["app_name"]

    @property
    def franchise(self):
        return self.data[self.env]["franchise"]

    @property
    def passport(self):
        return os.getenv("PASSPORT") #from .env

    @property
    def store(self):
        return self.data[self.env]["store"]


