from typing import Optional

from pydantic import BaseSettings, Field, BaseModel
import os

CURRENT_PATH = os.path.dirname(os.path.abspath(__file__))

class AppConfig(BaseModel):
    pass
    

class GlobalConfig(BaseSettings):
    APP_CONFIG: AppConfig = AppConfig()
    
    ENV_STATE: Optional[str] = Field(None, env='ENV_STATE')
    
    SECRET_KEY: Optional[str] = Field(None, env='SECRET_KEY')
    
    DEBUG: Optional[int] = None
    POSTGRES_NAME: Optional[str] = None
    POSTGRES_USER: Optional[str] = None
    POSTGRES_PASSWORD: Optional[str] = None
    POSTGRES_HOST: Optional[str] = None
    POSTGRES_PORT: Optional[int] = None
    
    
    class Config:
        env_file: str = os.path.join(CURRENT_PATH, '.env')
        
    
class DevConfig(GlobalConfig):
    
    class Config:
        env_prefix: str = 'DEV_'
        

class ProdConfig(GlobalConfig):
    pass


class FactoryConfig:
    def __init__(self, env_state):
        self.env_state = env_state
    
    def get_config(self):
        if self.env_state == "dev":
            return DevConfig()
        # elif in production state ...
    

cnf = FactoryConfig(GlobalConfig().ENV_STATE).get_config()


