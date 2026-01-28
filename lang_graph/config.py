from dotenv import load_dotenv
import os

load_dotenv(".env.dev")

class Settings:
    ENV = dict(os.environ)

    @staticmethod
    def required(key: str):
        value = os.getenv(key)
        if value is None:
            raise RuntimeError(f"Variável de ambiente obrigatória não definida: {key}")
        return value
