import sys
import requests
import pprint

ip = input("Enter AGL ip: ")
headers = {"Content-type": "application/json"}
pp = pprint.PrettyPrinter(indent=4)

while True:
            sel1 = input("""
                      LAUNCH APP

                ----- Select options -----
                1 - Open Radio
                2 - Open Phone
                3 - Open HVAC
                4 - Open Settings 
                5 - Open Dashboard
                6 - Open Mixer
                """)

            if sel1 == "1":
                link = "http://" + ip + ":30030/api/homescreen/showWindow"
                data = '{"application_id":"radio"}'
                response = requests.post(link, headers=headers, data=data)

                pp.pprint(response.json())

            elif sel1 == "2":
                link = "http://" + ip + ":30030/api/homescreen/showWindow"
                data = '{"application_id":"phone"}'
                response = requests.post(link, headers=headers, data=data)

                pp.pprint(response.json())

            elif sel1 == "3":
                link = "http://" + ip + ":30030/api/homescreen/showWindow"
                data = '{"application_id":"hvac"}'
                response = requests.post(link, headers=headers, data=data)

                pp.pprint(response.json())

            elif sel1 == "4":
                link = "http://" + ip + ":30030/api/homescreen/showWindow"
                data = '{"application_id":"settings"}'
                response = requests.post(link, headers=headers, data=data)

                pp.pprint(response.json())

            elif sel1 == "5":
                link = "http://" + ip + ":30030/api/homescreen/showWindow"
                data = '{"application_id":"dashboard"}'
                response = requests.post(link, headers=headers, data=data)

                pp.pprint(response.json())

            elif sel1 == "6":
                link = "http://" + ip + ":30030/api/homescreen/showWindow"
                data = '{"application_id":"mixer"}'
                response = requests.post(link, headers=headers, data=data)

                pp.pprint(response.json())

            elif sel1 == "0":
                break

            else:
                print("Wrong option")

print('Exiting')

