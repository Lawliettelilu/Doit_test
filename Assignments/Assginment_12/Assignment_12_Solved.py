
import os, sys, json

# 1. დაწერეთ პითონის ფუნქცია რომელიც კონტექსტის მენეჯერის გამოყენებით პარამეტრად მიიღებს ფაილის საქაღალდის მისამართს, 
# ფაილის სახელს და შემქნის მას.


def create_file(path, filename):
    file_path = None
    
    if len(path.split('/'))==2:
        file_path=f"{path}/{filename}.json"

        os.makedirs(path, exist_ok=True)
    
    try:
        with open(file_path, 'x'):
            pass
    except FileExistsError:
        print(f"File '{filename}.json' already exists in '{path}' directory.")
        print("keep working with existing file...\n\n")
    except TypeError:
        print("Invalid path format. Please provide a valid path.")
        sys.exit(1)
    return file_path

def write_json(file_path, data:list):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=2)

# # 2. დაწერეთ პითონის ფუნქცია რომელიც წაიკითხავს პარამეტრად მიღებული ფაილის კონტენტს.

def read_file_content(file_path):
    with open(file_path, 'r',encoding='utf-8') as file:
        return json.loads(file.read())


# # # 3. დაწერეთ პითონის ფუნქცია რომელიც პარამეტრად მიიღებს ლექსიკონს (dict) და დაამატებს ფაილის კონტენტს.

# # [
# #   {'id': 568, 'name': 'Kasparov', 'country': 'Russia', 'rating': 2705, 'age': 56},
# #   {'id': 189, 'name': 'Karpov', 'country': 'Russia', 'rating': 2698, 'age': 59},
# # ]

# # ბოლოში უნდა ჩაემატოს მხოლოდ ორი ლექსიკონი და არა სია.

def append_dicts_to_file(file_path, data:dict):

    players= read_file_content(file_path)

    if type(data['id']) !=int:
        print("id must be integer")
        return
    
    for player in players:
        if player['id']==data['id']:
            print(f"Player with id {data['id']} already exists.")
            return
    
    else:
        players.append(data)
        players.sort(key=lambda x: x['id'])

    write_json(file_path, players)

# # 4. დაწერეთ პითონის ფუნქცია, რომელიც გაანახლებს ფაილში არსებულ კონტენტს.

def update_file_content(file_path):
    players = read_file_content(file_path)
    data = {}

    data['id'] = input("\nID [Press 'Enter' to exit]: ").strip()

    if not data['id']:  # user pressed Enter
        print("Exit...\n")
        return

    if not data['id'].isdigit():
        print("ID must be an integer.\n")
        return

    data['id'] = int(data['id'])
    found = False

    for i, player in enumerate(players):
        if data['id'] == player['id']:
            found = True
            print(f"\nCurrent data: {player}\n")

            data['name'] = input("Name [Press 'Enter' to keep current]: ").strip() or player['name']
            data['country'] = input("Country [Press 'Enter' to keep current]: ").strip() or player['country']

            rating = input("Rating [Press 'Enter' to keep current]: ").strip()
            data['rating'] = int(rating) if rating.isdigit() else player['rating']

            age = input("Age [Press 'Enter' to keep current]: ").strip()
            data['age'] = int(age) if age.isdigit() else player['age']

            print(f"\nUpdated data: {data}\n")

            players[i] = data
            break

    if not found:
        print(f"\nPlayer with ID '{data['id']}' not found.\n")
        return

    question = input("\nWrite data to a file [y/n]? ").strip().lower()
    if question == 'y':
        write_json(file_path, players)
        print(" Data has been written successfully.")
    else:
        print(" Data has not been written.")
