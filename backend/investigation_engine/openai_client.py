import json

from openai import OpenAI

from backend.config import settings


class OpenAIClient:

    def __init__(self):

        self.client = OpenAI(
            api_key=settings.OPENAI_API_KEY
        )

        self.model = settings.OPENAI_MODEL

    def investigate(
        self,
        prompt: str,
    ) -> dict:

        response = self.client.responses.create(

            model=self.model,

            input=prompt,

            temperature=0,

            text={
                "format": {
                    "type": "json_object"
                }
            }
        )

        return json.loads(
            response.output_text
        )