
import base64
import csv
import json

consul_key_value = {"Key": "Value"}

#function
def load_file():
    with open('../../data.json') as file:
        data = json.load(file)
        for x in range(len(data)):
            base64_message = data[x]["Value"]
            base64_bytes = base64_message.encode('ascii')
            message_bytes = base64.b64decode(base64_bytes)
            message = message_bytes.decode('ascii')
            consul_key_value[(data[x]["Key"]).rsplit('/', 1)[1]] = message
    # print(consul_key_value)
    save_to_csv()

#function
def save_to_csv():
    with open('../../consul_file.csv', mode='w', newline='') as consul_file:
        consul_writer = csv.writer(consul_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for k, v in consul_key_value.items():
            consul_writer.writerow([k, v])
