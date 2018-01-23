import base64
import json
import os
import ssl

import certifi
import paho.mqtt.client as paho

# Set up AWS variables
awshost = os.getenv("AWS_HOST", "data.iot.us-west-2.amazonaws.com")
awsport = os.getenv("AWS_PORT", 8883)
thing_name = os.getenv("UUID")

def on_connect(client, userdata, flags, rc):
    """Send data once when connected connection
    """
    print("Connection returned result: " + str(rc) )
    value = 42
    data = {"state": {"reported": {"reading": value}}}
    mqttc.publish("$aws/things/{}/shadow/update".format(thing_name), json.dumps(data), qos=1)
    mqttc.publish("cats", json.dumps(data), qos=1)
    print("msg sent: temperature " + "%.2f")

def set_cred(env_name, file_name):
    """Turn base64 encoded environmental variable into a certificate file
    """
    env = os.getenv(env_name)
    with open(file_name, "wb") as output_file:
        output_file.write(base64.b64decode(env))

# Set up key files
key_filename = "aws_private_key.key"
set_cred("AWS_PRIVATE_KEY", key_filename)
cert_filename = "aws_certificate.crt"
set_cred("AWS_CERTIFICATE", cert_filename)

mqttc = paho.Client()
mqttc.on_connect = on_connect

mqttc.tls_set(certifi.where(),
              certfile=cert_filename,
              keyfile=key_filename,
              cert_reqs=ssl.CERT_REQUIRED,
              tls_version=ssl.PROTOCOL_TLSv1_2,
              ciphers=None)

mqttc.connect(awshost, awsport, keepalive=60)
mqttc.loop_forever()
