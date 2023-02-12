import json
import os

CONST_NEW_ACCOUNT_NAME = 'rexto_account-'
CONST_NEW_ACCOUNT_STARTING_NUMBER = 1
CONST_NEW_FOLDER_NAME = 'json_accounts'
# FINAL RESULT WILL LOOK LIKE 'rexto_account-1.json' inside 'json_accounts' folder

if __name__=='__main__':
    file1 = open('accs.txt', 'r')
    Lines = file1.readlines()

    new_account_json_file = open('example.json', 'r')
    new_account_json = json.load(new_account_json_file)
    new_account_json_file.close()

    if not os.path.exists(CONST_NEW_FOLDER_NAME):
        os.makedirs(CONST_NEW_FOLDER_NAME)

    count = 0
    for line in Lines:
        count += 1
        parse_array = line.strip().split(':')
        new_account_data = json.dumps(new_account_json)
        data = json.loads(new_account_data)
        data['SteamLogin'] = parse_array[0]
        data['SteamPassword'] = parse_array[1]
        new_account_data = json.dumps(data)
        print(new_account_data)

        with open(os.path.join(CONST_NEW_FOLDER_NAME, f"{CONST_NEW_ACCOUNT_NAME}{CONST_NEW_ACCOUNT_STARTING_NUMBER + count - 1}.json"), "w") as file:
            file.write(new_account_data)

    new_account_json_file.close()