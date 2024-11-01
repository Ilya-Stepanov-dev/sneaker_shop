from pydantic import BaseModel
from pydantic_settings import BaseSettings


class MainConfig(BaseModel):
    host: str = "0.0.0.0"
    port: int = 8000
    run_reload: bool = True


class PrefixConfig(BaseModel):
    prefix: str = "/api"


class Settings(BaseSettings):
    main: MainConfig = MainConfig()
    prefix: PrefixConfig = PrefixConfig()


settings = Settings()  