class Provider:
    @abstractmethod
    def name():
        pass

    @abstractmethod
    def ask(Conversation):
        pass

    @abstractmethod
    def contruct_prompt(str):
        pass
