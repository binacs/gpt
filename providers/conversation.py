class Conversation:
    conversation = []

    def __init__(
        self
    ) -> None:
        self.conversation = []

    def reset(self):
        self.conversation = []

    def validate(self):
        return len(self.conversation) > 0

    def get(self):
        return self.conversation

    def add(self, object):
        self.conversation.append(object)
        # TODO: more precise rules.
        if len(self.conversation) > 10:
            self.conversation = self.conversation[-10:]
