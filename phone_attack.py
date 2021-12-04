import sys
import requests
import pprint

ip = input("Enter AGL ip: ")
headers = {"Content-type": "application/json"}
pp = pprint.PrettyPrinter(indent=4)

while True:
            sel1 = input("""
                          PHONE

                ----- Select options -----
                1 - Get contacts
                2 - Get phone history
                3 - Make phone call
                4 - Answer call
                5 - Hangup phone call 
                6 - Check connected device battery
                7 - Check registered network provider
                0 - Exit from option
                """)

            if sel1 == "1":
                link = "http://" + ip + ":30037/api/bluetooth-pbap/contacts"
                data = '{}'
                response = requests.post(link, headers=headers, data=data)

                pp.pprint(response.json())

            elif sel1 == "2":
                link = "http://" + ip + ":30037/api/bluetooth-pbap/history"
                data = '{"list":"cch"}'
                response = requests.post(link, headers=headers, data=data)

                pp.pprint(response.json())

            elif sel1 == "3":
                num = input("Enter phone number: ")
                link = "http://" + ip + ":30037/api/telephony/dial"
                data = '{"value":"' + num + '"}'
                response = requests.post(link, headers=headers, data=data)

                pp.pprint(response.json())

            elif sel1 == "4":
                num = input("Enter phone number: ")
                link = "http://" + ip + ":30037/api/telephony/answer"
                data = '{"value":"' + num + '"}'
                response = requests.post(link, headers=headers, data=data)

                pp.pprint(response.json())

            elif sel1 == "5":
                link = "http://" + ip + ":30037/api/telephony/hangup"
                data = '{}'
                response = requests.post(link, headers=headers, data=data)

                pp.pprint(response.json())

            elif sel1 == "6":
                link = "http://" + ip + ":30037/api/telephony/get_battery_level"
                data = '{}'
                response = requests.post(link, headers=headers, data=data)

                pp.pprint(response.json())

            elif sel1 == "7":
                link = "http://" + ip + ":30037/api/telephony/get_network_registration"
                data = '{}'
                response = requests.post(link, headers=headers, data=data)

                pp.pprint(response.json())

            elif sel1 == "0":
                break

            else:
                print("Wrong option")

print('Exiting bluetooth phone controls')
