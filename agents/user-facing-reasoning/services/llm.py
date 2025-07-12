from openai import OpenAI
from ..core.config import settings

llm_client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=settings.openroter_mistral_7b_key,
)

def get_simple_response(query: str):
    generation = llm_client.chat.completions.create(
        model="mistralai/mistral-7b-instruct:free",
        messages=[
            {"role": "user", "content": f"{query}"}
        ],
        # extra_body={"include_reasoning": True}, # No reason to add it because it is not supported
        # stream=True,
    )
    
    return generation.choices[0].message.content
