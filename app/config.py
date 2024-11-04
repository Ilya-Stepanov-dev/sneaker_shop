# import os
from pydantic import BaseModel, field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


# DOTENV = os.path.join(os.path.dirname(__file__), ".env")
# DOTENV_PROD = os.path.join(os.path.dirname(__file__), ".env-prod")


class UvicornConfig(BaseModel):
    host: str = 'host'
    port: int = 0000
    run_reload: bool = False


class ApiConfig(BaseModel):
    prefix: str = '/vvv'

    model_config = SettingsConfigDict(
        env_file = ".env"
    )
    

class DataBaseConfig(BaseModel):
    host: str = 'host'
    port: int = 0000
    user: str = 'db_user'
    passwd: str = 'pass'
    name_db: str = 'name'
    name: str = 'name'
    engine: str = 'engine'

    def get_url(self):
        url = f'{self.name}+{self.engine}://{self.user}:{self.passwd}@{self.host}:{self.port}/{self.name_db}'
        return url



class Settings(BaseSettings):

    model_config = SettingsConfigDict(
        env_file=("app/.env-dev", "app/.env"),
        case_sensitive=False,
        env_nested_delimiter="__",
        env_prefix="APP_CONFIG__",
        # env_file_encoding="utf-8",
        # extra='allow'
    )
    uvicorn: UvicornConfig = UvicornConfig()
    api: ApiConfig = ApiConfig()
    db: DataBaseConfig = DataBaseConfig()



# uvicorn = UvicornConfig()

# print(uvicorn)

settings = Settings()
print(settings.db.get_url())