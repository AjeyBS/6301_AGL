
import requests
import pprint

ip = input("Enter AGL ip: ")
headers = {"Content-type": "application/json"}
pp = pprint.PrettyPrinter(indent=4)
while True:
    sel1 = input("""
                     RADIO CONTROLS

                ----- Select options -----
                1 - Start radio
                2 - Stop radio
                3 - Seek radio forward
                4 - Seek radio backward 
                0 - Exit from option
                """)

    if sel1 == "1":
                link = "http://" + ip + ":30039/api/radio/start"
                data = '{}'
                response = requests.post(link, headers=headers, data=data)

                pp.pprint(response.json())

    elif sel1 == "2":
                link = "http://" + ip + ":30039/api/radio/stop"
                data = '{}'
                response = requests.post(link, headers=headers, data=data)

                pp.pprint(response.json())

    elif sel1 == "3":
                link = "http://" + ip + ":30039/api/radio/scan_start"
                data = '{"direction":"forward"}'
                response = requests.post(link, headers=headers, data=data)

                pp.pprint(response.json())

    elif sel1 == "4":
                link = "http://" + ip + ":30039/api/radio/scan_start"
                data = '{"direction":"backward"}'
                response = requests.post(link, headers=headers, data=data)

                pp.pprint(response.json())

    elif sel1 == "0":
                break

    else:
        print("Wrong option")
print('Exiting radio controls')
