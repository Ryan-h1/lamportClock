from SenderAndReceiver import SenderAndReceiver


def main()-> None:
    person_a = SenderAndReceiver("Person A")
    person_b = SenderAndReceiver("Person B")

    person_b.send_message_to_receiver("Hello", person_a)
    person_a.send_message_to_receiver("Hi", person_b)

if __name__ == "__main__":
    main()
