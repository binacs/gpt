from providers import azure_openai
from providers import conversation

# TODO: Abstract provider switch.
provider_switch = {
    azure_openai.AzureOpenAIProvider.name(): azure_openai.AzureOpenAIProvider(),
    # Other providers...
}

default_provider = provider_switch[azure_openai.AzureOpenAIProvider.name()]

# Commands:
# - '/clear' -> clear all previous contextual information


def main():
    # TODO: Differentiate contextual information according to different users.
    conv = conversation.Conversation()
    while True:
        msg = input("prompt: ").strip()
        if len(msg) == 0:
            continue
        if msg.startswith("/clear"):
            conv.reset()
            continue
        else:
            conv.add(default_provider.contruct_prompt(msg))
        response = default_provider.ask(conv)

        print(response)


if __name__ == "__main__":
    main()
