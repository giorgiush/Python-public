letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

session = True
while session == True:

    action = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    if action != "encode" and action != "decode":
        print("Try again")
        break
    msg = list(input("Type your message:\n").lower())
    if not msg:
        print("Empty message")
        break
    shift = int(input("Type the shift number:\n"))
    

    def encode(msg, shift):
        encoded_msg = []
        for i in msg:
            i = letters[(letters.index(i)+shift)%26]
            encoded_msg.append(i)
        print(f"Encoded message: {''.join(encoded_msg)}")


    def decode(msg, shift):
        decoded_msg = []
        for i in msg:
            i = letters[(letters.index(i)-shift)%26]
            decoded_msg.append(i)
        print(f"Decoded message: {''.join(decoded_msg)}")


    if action == "encode":
        encode(msg, shift)
        session = False
    elif action == "decode":
        decode(msg, shift)
        session = False