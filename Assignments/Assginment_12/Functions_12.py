from data import chess_players, new_players
from Assignment_12_Solved import create_file, write_json, read_file_content, append_dicts_to_file, update_file_content

#ფაილის შექმნა
file_path = create_file("files/chess", "data")

#ფაილში ჩაწერა
write_json(file_path, chess_players)

#ფაილში მონაცემების წაკითხვა
file_content= read_file_content(file_path)

for row in file_content:
    print(row)


#ლექსიკონის დამატება ფაილში
for player in new_players:
    append_dicts_to_file(file_path, player)

#ფაილში მონაცემების განახლება
update_file_content(file_path)

