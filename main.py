import json
import os


CONST_NEW_FOLDER_NAME = 'json_accounts'


if __name__=='__main__':

    CONST_ACCOUNT_JSON_TYPE_NAME = input \
        ('Do you want to save account by login or every account will have the same name but different number?(Press 1 or 2)\n')
    if (CONST_ACCOUNT_JSON_TYPE_NAME == '2'):
        CONST_NEW_ACCOUNT_NAME = input("Print new account's name for example 'rexto_account-'\n")
        CONST_NEW_ACCOUNT_STARTING_NUMBER = int(input("Print new account's starting number\n"))



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

        if(CONST_ACCOUNT_JSON_TYPE_NAME == '1'):
            with open(os.path.join(CONST_NEW_FOLDER_NAME, f"{parse_array[0]}.json"), "w") as file:
                file.write(new_account_data)
        elif(CONST_ACCOUNT_JSON_TYPE_NAME == '2'):
            with open(os.path.join(CONST_NEW_FOLDER_NAME,
                                   f"{CONST_NEW_ACCOUNT_NAME}{CONST_NEW_ACCOUNT_STARTING_NUMBER + count - 1}.json"),
                      "w") as file:
                file.write(new_account_data)
        else:(print('ERROR! Restart and choose "1" or "2" option'))

    new_account_json_file.close()