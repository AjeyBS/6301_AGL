
import requests
import pprint

ip = input("Enter AGL ip: ")
headers = {"Content-type": "application/json"}
pp = pprint.PrettyPrinter(indent=4)

while True:
            sel1 = input("""
                      MEDIA CONTROLS

                ----- Select options -----
                1 - Play media
                2 - Pause media
                3 - Play next in playlist
                4 - Play previous in playlist 
                0 - Exit from option
                """)

            if sel1 == "1":
                link = "http://" + ip + ":30030/api/bluetooth-manager/avrcp_controls"
                data = '{"action":"Play"}'
                response = requests.post(link, headers=headers, data=data)

                pp.pprint(response.json())

            elif sel1 == "2":
                link = "http://" + ip + ":30030/api/bluetooth-manager/avrcp_controls"
                data = '{"action":"Pause"}'
                response = requests.post(link, headers=headers, data=data)

                pp.pprint(response.json())

            elif sel1 == "3":
                link = "http://" + ip + ":30030/api/bluetooth-manager/avrcp_controls"
                data = '{"action":"Next"}'
                response = requests.post(link, headers=headers, data=data)

                pp.pprint(response.json())

            elif sel1 == "4":
                link = "http://" + ip + ":30030/api/bluetooth-manager/avrcp_controls"
                data = '{"action":"Previous"}'
                response = requests.post(link, headers=headers, data=data)

                pp.pprint(response.json())

            elif sel1 == "0":
                break

            else:
                print("Wrong option")

print('Exiting bluetooth media controls')
