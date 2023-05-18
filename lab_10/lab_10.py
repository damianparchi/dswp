#zadanie1
import os

def create_folders(paths):
    for path in paths:
        if not os.path.exists(path):
            os.makedirs(path)
            print(f"Utworzono folder: {path}")
        else:
            print(f"Folder już istnieje: {path}")

folders = ["lab_10/folder1", "lab_10/folder2/podfolder1"]
create_folders(folders)


#zadanie2
import csv

def merge_files(path):
    with open('lab_10/zad2.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=";")
        columns = ""
        for root, _, files in os.walk(path):
            for file in files:
                with open(root + "/" + file, 'r') as f:
                    if columns == "":
                        columns = f.readline().removesuffix("\n").split(",")
                        writer.writerow(columns)
                    else:
                        f.readline()
                    for line in f:
                        writer.writerow(line.removesuffix("\n").split(","))

merge_files("lab_10/text.txt")

#zadanie3

from datetime import datetime, timezone
from zoneinfo import ZoneInfo, available_timezones

def display_time_in_different_timezones(time):
    current_time = datetime.now()

    time_parts = time.split(":")
    time_obj = current_time.replace(hour=int(time_parts[0]), minute=int(time_parts[1]), second=int(time_parts[2]))

    timezones = available_timezones()

    for timezone_name in timezones:
        tz = ZoneInfo(timezone_name)
        localized_time = time_obj.replace(tzinfo=timezone.utc).astimezone(tz)
        formatted_time = localized_time.strftime("%Y-%m-%d %H:%M:%S %Z%z")
        print(f"Czas w {timezone_name}: {formatted_time}")

user_time = input("Podaj czas (HH:MM:SS): ")

display_time_in_different_timezones(user_time)


#zadanie4
from datetime import datetime

def calculate_age_and_next_birthday(date):
    today = datetime.now().date()
    birthday = datetime.strptime(date, "%Y-%m-%d").date()
    age = today.year - birthday.year

    if today.month < birthday.month or (today.month == birthday.month and today.day < birthday.day):
        age -= 1

    next_birthday = birthday.replace(year=today.year)

    if next_birthday < today:
        next_birthday = next_birthday.replace(year=today.year + 1)

    if next_birthday == today:
        days_until_next_birthday = 0
    else:
        days_until_next_birthday = (next_birthday - today).days

    month_difference = (today.month - birthday.month) % 12
    day_difference = today.day - birthday.day
    if day_difference < 0:
        month_difference -= 1
        day_difference += (next_birthday - today.replace(day=1)).days

    age_message = f"Twój wiek to: {age} lat, {month_difference} miesięcy i {day_difference} dni."
    next_birthday_message = f"Do twoich urodzin pozostało: {days_until_next_birthday} dni."
    
    return age_message, next_birthday_message

date = input("Podaj datę urodzenia (RRRR-MM-DD): ")
age, next_birthday = calculate_age_and_next_birthday(date)
print(age)
print(next_birthday)

#zadanie5
def convert_date_format(file_name, date_column_index, source_format, target_format):
    new_file_name = f"converted_{file_name}"
    
    with open(file_name, 'r') as file, open(new_file_name, 'w', newline='') as new_file:
        reader = csv.reader(file, delimiter=';')
        writer = csv.writer(new_file, delimiter=';')
        
        header = next(reader)
        writer.writerow(header)
        
        for row in reader:
            date_str = row[date_column_index]
            try:
                date = datetime.strptime(date_str, source_format).date()
                new_date_str = date.strftime(target_format)
                row[date_column_index] = new_date_str
            except ValueError:
                print(f"Nieprawidłowy format daty w wierszu: {row}")
            writer.writerow(row)
    
    print(f"Plik {new_file_name} został utworzony z zaktualizowanym formatem daty.")

file_name = "lab_10/zad2.csv"
date_column_index = 0
source_format = "%d-%m-%Y"
target_format = "%Y-%m-%d"

convert_date_format(file_name, date_column_index, source_format, target_format)
