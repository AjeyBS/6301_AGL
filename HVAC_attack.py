
import requests
import pprint

ip = input("Enter AGL ip: ")
headers = {"Content-type": "application/json"}
pp = pprint.PrettyPrinter(indent=4)

while True:
            sel1 = input("""
                      HVAC CONTROLS

                ----- Select options -----
                1 - View current HVAC state
                2 - Set fan speed(1-100)
                3 - Set right temperature
                4 - Set left temperature 
                0 - Exit from option
                """)

            if sel1 == "1":
                link = "http://" + ip + ":30031/api/hvac/get"
                data = '{}'
                response = requests.post(link, headers=headers, data=data)

                pp.pprint(response.json())

            elif sel1 == "2":
                fanS = input("Enter fanspeed(0-255): ")

                link = "http://" + ip + ":30031/api/hvac/set"
                data = '{"FanSpeed": ' + fanS + '}'
                response = requests.post(link, headers=headers, data=data)
                link = "http://" + ip + ":30031/api/hvac/get"
                data = '{}'
                response = requests.post(link, headers=headers, data=data)

                pp.pprint(response.json())

            elif sel1 == "3":
                rightT = input("Enter right temperature: ")
                link = "http://" + ip + ":30031/api/hvac/set"
                data = '{"RightTemperature": ' + rightT + '}'
                response = requests.post(link, headers=headers, data=data)
                link = "http://" + ip + ":30031/api/hvac/get"
                data = '{}'
                response = requests.post(link, headers=headers, data=data)

                pp.pprint(response.json())

            elif sel1 == "4":
                leftT = input("Enter right temperature: ")
                link = "http://" + ip + ":30031/api/hvac/set"
                data = '{"LeftTemperature": ' + leftT + '}'
                response = requests.post(link, headers=headers, data=data)
                link = "http://" + ip + ":30031/api/hvac/get"
                data = '{}'
                response = requests.post(link, headers=headers, data=data)

                pp.pprint(response.json())

            elif sel1 == "0":
                break

            else:
                print("Wrong option")

print('Exiting HVAC controls')
