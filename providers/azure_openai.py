import os
from openai import AzureOpenAI
from . import conversation


class AzureOpenAIProvider:
    def __init__(
        self
    ) -> None:
        self.client = AzureOpenAI(
            api_key=os.getenv("AZURE_OPENAI_API_KEY"),
            api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
            azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
        )
        # For Azure cloud, model = "deployment_name"
        self.default_model = os.getenv("AZURE_OPENAI_DEFAULT_MODEL")

    @staticmethod
    def name():
        return "AzureOpenAIProvider"

    # Will maintain 'msgs' outside of provider.
    # TODO: pass through User related informations.
    def ask(self, conversation: conversation.Conversation):
        if conversation.validate() == False:
            return "invalid empty input"

        system_message = [
            {"role": "system", "content": "You are binacs's AI bot."}]

        messages = system_message + conversation.get()

        # ATTENTION: for gpt-4 model, we need 'chat' work model
        response = self.client.chat.completions.create(
            model=self.default_model,
            messages=messages,
        )

        # TODO: error handling
        content = response.choices[0].message.content
        conversation.add({"role": "assistant", "content": content})
        return content

    def contruct_prompt(self, msg: str):
        return {"role": "user", "content": msg}
