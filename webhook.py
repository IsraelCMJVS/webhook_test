import logging
import requests
import json
from requests.exceptions import HTTPError
from requests.exceptions import Timeout
from requests.exceptions import MissingSchema





class CustomFormatter(logging.Formatter):               #Define colors for outputs in terminal or logs using logging function

    green = "\x1b[32;21m"
    grey = "\x1b[38;21m"
    yellow = "\x1b[33;21m"
    red = "\x1b[31;21m"
    bold_red = "\x1b[31;1m"
    reset = "\x1b[0m"
    format = "%(message)s"

    FORMATS = {
        logging.DEBUG: grey + format + reset,
        logging.INFO: green + format + reset,
        logging.WARNING: yellow + format + reset,
        logging.ERROR: red + format + reset,
        logging.CRITICAL: bold_red + format + reset
    }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt)
        return formatter.format(record)

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
ch.setFormatter(CustomFormatter())
logger.addHandler(ch)


def get_vars():
    global listhook_api, edithook_api, gitlab_token, hook_url, addhook_url
    with open('vars.json','r') as json_file:
        data = json.load(json_file)
       

    listhook_api = data['listhook_api']
    edithook_api = data['edithook_api']
    gitlab_token = data['gitlab_token']
    hook_url = data['hook_url']
    addhook_url = data['addhook_url']
get_vars()



def gitlab_req():
    headers = {
        "Content-Type": "application/json",
        "Private-Token": gitlab_token
        }
    payload={}

    try:

                                                 #Request from Gitlab API to List Hooks (optional to know HOOKID`s)

        # response_1 = requests.get(listhook_api, verify=False, headers = headers, data=payload, timeout=60)
        # if response_1.status_code == 200:
        #     projects_dict = json.loads(response_1.content)
        #     project_info = json.dumps(projects_dict, indent=4)
        #     logging.debug(project_info)
        #     #logging.debug(projects_dict)
        #     logging.info ("Request was succesfull \n \n")
        # elif response_1.status_code == 401:
        #     logging.error("Unauthorized request. Veify your Auth or Token")
        #     logging.error("Response Code:")
        #     logging.error (response_1.status_code)
        # else:
        #     logging.error("Error getting API Response \n \n")
        #     logging.error ("Response Status Code: ")
        #     logging.error (response_1.status_code)

                                                #Request API to add new hook
                                                
        # data_add = {'url': addhook_url}
        # req_2 = requests.post(listhook_api, verify=False, headers = headers, json=data_add, timeout=60)
        # if req_2.status_code == 200 or 201:
        #     addhok_dict = json.loads(req_2.content)
        #     logging.debug(addhook_dict)
        #     logging.info ("Request was succesfull. Webhook added.")
        # elif req_2.status_code == 401:
        #     logging.error("Unauthorized request. Veify your Auth or Token")
        #     logging.error("Response Code:")
        #     logging.error (req_2.status_code)
        # else:
        #     logging.error("Error getting API Response \n \n")
        #     logging.error ("Response Status Code: ")
        #     logging.error (req_2.status_code)

                                        #Request API to edit hook
        data = {'url': hook_url}
        logging.warning("STARTING API REQUEST TO UPDATE WEBHOOK...")
        req_3 = requests.put(edithook_api, verify=False, headers = headers, json=data, timeout=60)
        if req_3.status_code == 200:
            edithook_dict = json.loads(req_3.content)
            edithook_info = json.dumps(edithook_dict, indent=4)
            logging.info("\n \n UPDATED WEBHOOK INFO: ")
            logging.debug(edithook_info)
            logging.info ("Request was succesfull. Webhook updated")
        elif req_3.status_code == 401:
            logging.error("Unauthorized request. Veify your Auth or Token")
            logging.error("Response Code:")
            logging.error (req_3.status_code)
        else:
            logging.error("Error getting API Response \n \n")
            logging.error ("Response Status Code: ")
            logging.error (req_3.status_code)


    except Timeout:
        logging.error("Time for request has expired. Please try again.")
        raise Exception("Time for request has expired. Please try again.")
    except HTTPError as http_err:
        logging.error("HTTP Error", http_err)
        raise Exception("HTTP Error", http_err)
    except MissingSchema:
        logging.error("URL is not valid, please check it")
        raise Exception("Invalid API URL", )
gitlab_req()


