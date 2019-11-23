
while True:
    Europe = {"Slovenia": "Ljubljana",
              "Hungary": "Budapest",
              "Italy": "Rome",
              "Austria": "Vienna",
              "Germany": "Berlin",
              }

    Africa = {"Algeria": "Algiers",
              "Angola": "Luanda",
              "Benin": "Portonovo",
              "Botswana": "Gaborone",
              "Egipt": "Kairo"
              }

    Asia = {"Afganistan": "Kabul",
            "Armenia": "Yerevan",
            "Azerbaijan": "Baku",
            "Bahrain": "Manama",
            "Japan": "Tokyo"
            }

    comments = {0: "That was easy.",
                1: "Not impressed yet.",
                2: "Damn you're good.",
                3: "You're on fire.",
                4: "You should teach."
                }


    def query_cities(level):
        for country, capital_city in level.items():
            question = input("What is the capital city of " + str(country) + "? ")
            correct_form_answer = question.lstrip().capitalize()
            if correct_form_answer == f"{capital_city}":
                end_list = list(level)
                for key, statement in comments.items():
                    if country == end_list[-1]:
                        return f"You have answered correctly to all the questions!!!"
                    elif key == end_list.index(country):
                        print(statement)
                continue
            return f"Wrong! The capital city of {country} is {capital_city}."


    starter = input("Hello user! Please select the continent referring to quiz: [Europe, Asia, Africa] ")
    if starter.lstrip().capitalize() == "Europe":
        print(query_cities(Europe))
    elif starter.lstrip().capitalize() == "Africa":
        print(query_cities(Africa))
    elif starter.lstrip().capitalize() == "Asia":
        print(query_cities(Asia))
    else:
        end = input("Wrong input. Would you like to continue [y/n]? ")
        if end.lstrip().lower() == "n":
            print("Bye")
            break
        elif end.lstrip().lower() == "y":
            continue
        else:
            print("You have entered an invalid symbol. You will have to restart the program. Bye.")
    break



