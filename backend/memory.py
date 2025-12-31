class SimpleMemory:
    """
    Simple in-memory conversation store for academic demonstration.
    """

    def __init__(self):
        self.history = []

    def add(self, user_input, assistant_response):
        self.history.append({
            "user": user_input,
            "assistant": assistant_response
        })

    def get_history(self):
        return self.history


memory = SimpleMemory()
