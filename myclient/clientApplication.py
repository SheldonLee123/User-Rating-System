import json
import prettytable as pt
import requests

api = "http://127.0.0.1:8000"
session = requests.session()


while True:
    s = input("input:")
    command = s.split()[0]
    if command == "login":
        try:
            url = "http://" + s.split()[1] + "/login/"
            user = input("username:")
            pwd = input("password:")
            params = {"username": user, "password": pwd}
            res = session.get(url=url, params=params)
            print(res.text)
        except Exception as e:
            print("Input error, please try it again!")
    elif command == "register":
        try:
            url = api + "/register/"
            user = input("username:")
            email = input("email:")
            pwd = input("password:")
            params = {"username": user, "password": pwd, "email": email}
            res = session.get(url=url, params=params)
            print(res.text)
        except Exception as e:
            print("Input error, please try it again!")
    elif command == "logout":
        session = requests.session()
        print("logout!")
    elif command == "list":
        try:
            url = api + "/list/"
            res = session.get(url=url)
            res_json = json.loads(res.text)
            table = pt.PrettyTable()
            title_list = []
            for i in res_json.get('0'):
                title_list.append(i)
            table.field_names = title_list
            for i in res_json:
                row = []
                for j in res_json[i]:
                    if j == "taught":
                        taught = []
                        for t in res_json[i].get(j):
                            taught.append(t)
                        row.append(taught)
                    else:
                        row.append(res_json[i].get(j))
                    print(res_json[i].get(j))
                table.add_row(row)
            print(table)
        except Exception as e:
            print("Input error, please try it again!")
    elif command == "view":
        try:
            url = api + "/view/"
            res = session.get(url=url)
            res_json = json.loads(res.text)
            for i in res_json:
                print("The rating of the " + i + " is " + str(res_json[i]))
        except Exception as e:
            print("Input error, please try it again!")
    elif command == "average":
        try:
            url = api + "/average/"
            pro_id = input("professor_id :")
            code = input("module_code:")
            params = {"professor_id": pro_id, "module_code": code}
            res = session.get(url=url, params=params)
            print("The rating of " + pro_id + " in module " + code +" is " + res.text)
        except Exception as e:
            print("Input error, please try it again!")
    elif command == "rate":
        try:
            url = api + "/rate/"
            pro_id = input("professor_id :")
            code = input("module_code:")
            year = input("year:")
            semester = input("semester:")
            rating = input("rating:")
            params = {"professor_id": pro_id, "module_code": code, "year": year, "semester": semester, "rating": rating}
            res = session.get(url=url, params=params)
            print(res.text)
        except Exception as e:
            print("Input error, please try it again!")