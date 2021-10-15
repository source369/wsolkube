
import base64
import json

consul_key_value = {"Key": "Value"}

# function
def live_pods():
    with open('../../data.json') as file:
        data = json.load(file)
        for x in range(len(data)):
            base64_message = data[x]["Value"]
            base64_bytes = base64_message.encode('ascii')
            message_bytes = base64.b64decode(base64_bytes)
            message = message_bytes.decode('ascii')
            consul_key_value[(data[x]["Key"]).rsplit('/', 1)[1]] = message
    # print(consul_key_value)




