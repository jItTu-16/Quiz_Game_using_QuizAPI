import requests
import os
import time

API_KEY = # Enter api key from quizapi
url = "https://quizapi.io/api/v1/questions"


def quiz():

    score = 0
    while True:
        os.system("cls")
        print("*" * 10 + " Welcome to The Quiz " + "*" * 10)
        print()

        Category_list = [
            "Django",
            "Linux",
            "Code",
            "NodeJs",
            "SQL",
            "Next.js",
            "DevOps",
            "Docker",
            "WordPress",
            "Laravel",
            "Postgres",
            "VueJS",
            "Apache Kafka",
            "uncategorized",
            "Exit",
        ]

        print("\nCatagories:")
        for i in range(len(Category_list)):
            print(f"\t{i+1}. {Category_list[i]}")

        close = 0

        while True:
            choice = int(input("Select category for your quiz: "))

            if choice not in list(range(1, len(Category_list) + 1)):
                print("Enter valid option.")
                continue

            for i in range(1, len(Category_list) + 1):
                if choice == 15:
                    print("Exiting the quiz...")
                    close = 1
                    break

                elif choice == i:
                    category = str(Category_list[i - 1])
                    break

            break

        if close:
            break

        num = int(input("Enter number of questions(Max = 20): "))

        print("\nLoading quiz.")
        print("Please wait...\n")

        var = {"apiKey": API_KEY, "limit": num, "category": category}

        try:
            response = requests.get(url, var)

        except requests.exceptions.ConnectionError as e:
            print("Cannot connect to the internet.")
            print("Please check your internet connection.")
            exit(1)

        except requests.exceptions.Timeout as e:
            print("Cannot fetch questions from server.")
            print("Please try again.")
            exit(2)

        quiz_data = response.json()
        os.system("cls")

        t_size = list(os.get_terminal_size())
        q_no = 1

        print("=" * t_size[0])
        for question in quiz_data:
            answers = question["answers"]
            correct_answers = question["correct_answers"]

            print(f"\nQuestion {q_no}: {question['question']}\n")
            q_no += 1
            Opt = {}
            print("Options: ")
            for key, value in answers.items():
                if value:
                    print(f"\t{key[7].capitalize()}: {value}")
                    Opt.update({key: value})

            print()
            l = list(Opt.keys())
            opt_l = []
            for i in range(len(l)):
                opt_l.append(l[i][7])

            while True:
                ans = input("Choose an option: ")

                try:
                    if ans.lower() in opt_l:
                        for key, value in correct_answers.items():
                            if value == "true":
                                if str(ans.lower()) == key[7]:
                                    print(f"\nYour answer is correct.")
                                    score += 1
                                    time.sleep(2)

                                elif str(ans.lower()) != key[7]:
                                    print("\nYour answer is incorrect")
                                    print(
                                        f"Option {key[7].capitalize()} is the correct answer."
                                    )
                                    time.sleep(2)
                        break

                    else:
                        print("Not a valid option try again.\n")
                except TypeError:
                    print("Not a valid option try again.\n")
            print("=" * t_size[0])

        print()
        print(f"Your Score is {score} out of {num}\n")
        repeat = input("Do you want to play again(Y/N): ")
        print()

        time.sleep(1)

        if repeat.lower() == "y":
            continue
        elif repeat.lower() == "n":
            print("Exiting the quiz...")
            time.sleep(1)
            break

if __name__ == "__main__":
    quiz()
