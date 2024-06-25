import datetime


def is_user_already_says_mood():
    file_path = 'data/mood_diary.txt'
    with open(file_path, 'r') as file:
        lines = [line.rstrip() for line in file]
        if len(lines) == 0:
            return False
        date_mood = lines[-1].split(':')
        date_today = datetime.date.today() # get the date today as a date object
        date_today = str(date_today) # convert it to a string
        if date_mood[0] == date_today: # today user already says mood
            return True
        return False


def store_mood_into_diary(mood):
    file_path = 'data/mood_diary.txt'
    with open(file_path, 'a') as file:
        date_today = datetime.date.today() # get the date today as a date object
        date_today = str(date_today) # convert it to a string
        mood_record = ":".join([date_today, mood])
        file.write(mood_record + "\n")


def diagnosing_disorders():
    file_path = 'data/mood_diary.txt'
    with open(file_path, 'r') as file:
        lines = [line.rstrip() for line in file]
        happy_times = 0
        sad_times = 0
        apathetic_times = 0
        total_times = 0
        if len(lines) < 7:
            return ""
        mood_diarys = lines[-7:]
        for mood_diary in mood_diarys:
            date_mood = mood_diary.split(":")
            mood = int(date_mood[1])
            if mood == 2: # happy
                happy_times += 1
            elif mood == -1: # sad
                sad_times += 1
            elif mood == 0: # apathetic
                apathetic_times += 1
            total_times += mood
        if happy_times >= 5:
            return "manic"
        elif sad_times >= 4:
            return "depressive"
        elif apathetic_times >= 6:
            return "schizoid"
        avg_mood = round(total_times/7)
        if avg_mood == 2:
            return "happy"
        if avg_mood == 1:
            return "relaxed"
        if avg_mood == 0:
            return "apathetic"
        if avg_mood == -1:
            return "sad"
        return "angry"

        


def assess_mood():
    if is_user_already_says_mood():
        print("Sorry, you have already entered your mood today.")
        return
    usr_input = ""
    valid_input = ["happy", "relaxed", "apathetic", "sad", "angry"]
    while usr_input not in valid_input:
        usr_input = input("Please input your current mood: ").strip()
    mood = 0
    if usr_input == "happy":
        mood = 2
    elif usr_input == "relaxed":
        mood = 1
    elif usr_input == "apathetic":
        mood = 0
    elif usr_input == "sad":
        mood = -1
    else:
        mood = -2
    store_mood_into_diary(str(mood))
    result = diagnosing_disorders()
    if result != "":
        print(f"Your diagnosis: {result}!")