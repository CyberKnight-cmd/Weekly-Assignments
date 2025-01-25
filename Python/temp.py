with open('binaryfile.bin', 'rb') as file:
    data = file.read()  # Reads the entire file content
    decoded_text = data.decode('utf-8')
    print("Decoded Text from Binary File:")
    print(decoded_text)
    print(data)         # Outputs the raw binary data
