class SenderAndReceiver:
    def __init__(self, name: str) -> None:
        self.name = name
        self._clock = 0

    def send_message_to_receiver(self, message: str, receiver: "SenderAndReceiver") -> None:
        self._increment_clock()
        receiver.receive_message_from_sender(message, self)
        print(f"{self.name} sent message to {receiver.name} at clock {self.clock}: {message}")

    def receive_message_from_sender(self, message: str, sender: "SenderAndReceiver") -> None:
        self._update_clock_on_message_reception(sender)
        print(f"{self.name} received message from {sender.name} at clock {self.clock}: {message}")

    def _update_clock_on_message_reception(self, sender: "SenderAndReceiver") -> None:
        self.clock = max(self.clock, sender.clock) + 1

    def _increment_clock(self) -> None:
        self.clock += 1

    @property
    def clock(self) -> int:
        return self._clock

    @clock.setter
    def clock(self, value) -> None:
        self._clock = value
