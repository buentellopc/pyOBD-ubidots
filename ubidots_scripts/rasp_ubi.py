# Write your code here :-)
import time
import requests
import math
import random
from var_carro import RPM
from var_carro import mph
from var_carro import thr
from var_carro import load



TOKEN = "BBFF-a7swpPFTE42z11hBbhAc6G1JXiAiQ0"  # Put your TOKEN here
DEVICE_LABEL = "rasp64"  # Put your device label here
VARIABLE_LABEL_1 = "Revoluciones por minuto"  # Put your first variable label here
VARIABLE_LABEL_2 = "Velocidad"  # Put your second variable label here
VARIABLE_LABEL_3 = "Acelerador"  # Put your second variable label here
VARIABLE_LABEL_4 = "Carga"

lst = [1,2,3,4,5,6,7,8,9,10]
indx = 0
def build_payload(variable_1, variable_2, variable_3, variable_4):
    # Creates two random values for sending data
    value_1 = RPM[indx]
    value_2 = mph[indx]
    value_3 = thr[indx]
    value_4 = load[indx]
    payload = {variable_1: value_1,
               variable_2: value_2,
               variable_3: value_3,
               variable_4: value_4}

    return payload


def post_request(payload):
    # Creates the headers for the HTTP requests
    url = "http://industrial.api.ubidots.com"
    url = "{}/api/v1.6/devices/{}".format(url, DEVICE_LABEL)
    headers = {"X-Auth-Token": TOKEN, "Content-Type": "application/json"}

    # Makes the HTTP requests
    status = 400
    attempts = 0
    while status >= 400 and attempts <= 5:
        req = requests.post(url=url, headers=headers, json=payload)
        status = req.status_code
        attempts += 1
        time.sleep(1)

    # Processes results
    if status >= 400:
        print("[ERROR] Could not send data after 5 attempts, please check \
            your token credentials and internet connection")
        return False

    print("[INFO] request made properly, your device is updated")
    return True


def main():
    payload = build_payload(
        VARIABLE_LABEL_1, VARIABLE_LABEL_2, VARIABLE_LABEL_3, VARIABLE_LABEL_4)

    print("[INFO] Attemping to send data")
    post_request(payload)
    print("[INFO] finished")


if __name__ == '__main__':
    while (True):
        main()
        indx += 1
        if indx == 50:
            break
        time.sleep(1)