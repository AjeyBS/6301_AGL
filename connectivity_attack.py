
import requests
import pprint

ip = input("Enter AGL ip: ")
headers = {"Content-type": "application/json"}
pp = pprint.PrettyPrinter(indent=4)

while True:
            sel1 = input("""
                     CONNECTIVITY

                ----- Select options -----
                1 - Turn off wifi
                2 - Turn off bluetooth 
                3 - Turn on bluetooth
                0 - Exit from option
                """)

            if sel1 == "1":
                vol = input("Enter volume to set(0-100): ")
                vol = int(vol) / 100

                link = "http://" + ip + "30030/api/network-manager/disable_technology"
                data = '{"technology":"wifi"}'
                response = requests.post(link, headers=headers, data=data)

                pp.pprint(response.json())

            elif sel1 == "2":
                link = "http://" + ip + "30030/api/network-manager/disable_technology"
                data = '{"technology":"bluetooth"}'
                response = requests.post(link, headers=headers, data=data)

                pp.pprint(response.json())

            elif sel1 == "3":
                link = "http://" + ip + "30030/api/network-manager/enable_technology"
                data = '{"technology":"bluetooth"}'
                response = requests.post(link, headers=headers, data=data)

                pp.pprint(response.json())


            elif sel1 == "0":
                break

            else:
                print("Wrong option")

print('Exiting connectivity controls')
