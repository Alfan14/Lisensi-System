import json
import tabulate

with open('data.json', 'r') as file:
        hasil = json.load(file)
        item = hasil["license_data"]
        table_data = [
            [
                data['id'], data['name'], data['type_of_subscribe'] ,data['aktivasi_token'], data['activated_at'], data['expires_at'], data['active'],
            ]
            for data in item
        ]

        headers = [
            "Id", "Name", "TypeOfSubscribe", "TypeOffLicense", "AktivasiToken", 
            "ActivatedAt", "ExpiresAt", "Active", 
        ]

        table = tabulate.tabulate(table_data, headers=headers, tablefmt="grid")

        print(table)