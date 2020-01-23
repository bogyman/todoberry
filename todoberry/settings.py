from pydantic import BaseSettings


class APISettings(BaseSettings):
    MONGO_HOST: str = ''
    MONGO_DB: str = 'todolists'
    MONGO_ITEM_COLLECTION: str = 'items'
    MONGO_LIST_COLLECTION: str = 'lists'

    class Config:
        env_prefix = "TODOBERRY_"


AppConfig = APISettings()
