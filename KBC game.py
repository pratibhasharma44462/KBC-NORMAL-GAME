# KBC program 
import random

question_data = [
	["what is the capital of Italy?", "Rome", "Paris", "Berlin", "Madrid",1],
	["what is the capital of france?", "Paris", "america", "china", "india",1],
	["who is the president of the united states?", "Joe Biden", "Donald Trump", "Barack Obama", "George Bush",2],
	["what is the largest planet in our solar system?", "Jupiter", "Earth", "Mars", "Saturn",1],
	["who wrote 'Romeo and Juliet'?", "William Shakespeare", "Charles Dickens", "Mark Twain", "Ernest Hemingway",1],
	["what is the boiling point of water in Celsius?", "120", "90", "80", "100",4],
	["who painted the Mona Lisa?","Vincent van Gogh", "Michelangelo", "Raphael","Leonardo da Vinci" ,4],
	["what is the smallest country in the world?", "San marino", "Monaco", "Vatican city", "Luxembourg",3],
	["what is the chemical symbol for gold?", "Ag", "Au", "Fe", "Hg",2],
	["who discovered penicillin?", "Alexander Fleming", "Marie Curie", "Louis Pasteur", "Albert Einstein",1],
	["what is the largest mammal?", "Elephant", "Giraffe", "Blue whale", "Great White Shark",3],
	["what is the capital of Japan?", "Seoul", "Tokyo", "Beijing", "Bangkok",2],
	["who wrote '1984'?", "George Orwell", "Aldous Huxley", "Ray Bradbury", "Isaac Asimov",1],
	["what is the currency of Germany?", "Pound", "Dollar", "Yen", "Euro",4],
	["what is the main ingredient in guacamole?", "Tomato", "Avacado", "Onion", "Lime",2],
	["who was the first person to walk on the moon?", "Neil Armstrong", "Buzz Aldrin", "Yuri Gagarin", "Michael Collins",1],
	
]

levels = [1000,2000,3000,5000,10000,20000,40000,80000,160000,320000,640000,1250000,2500000,5000000,10000000,70000000]

def ask_question(question, prize, lifelines): 
    print(f"\nQuestion: {(question[0])}") 
    print(f"Question for rupees: {prize}") 
    print(f"a. {question[1]}     b. {question[2]}") 
    print(f"c. {question[3]}     d. {question[4]}") 

    lifeline_used = None  
    if lifelines:
        use_lifeline = input(f"Do you want to use a lifeline? (yes/no): ")
        if use_lifeline == "yes":
            lifeline_used = lifeline(question, lifelines)
            if lifeline_used:
                lifelines.remove(lifeline_used)
    else:
        print("No lifelines left.")

    answer = int(input("Your answer in preference to question(1-4) or press 0 to exit: "))
    
    if answer == 0:
        # If user exits, show the last won amount (previous question's prize) or 0 if first question
        take_home = levels[question_data.index(question)-1] if question_data.index(question) > 0 else 0
        print(f"You have out of the game, money you take home with you {take_home} rupees")
        return False, lifeline_used
    
    if prize == 70000000:
        print("\nCongratulations! aap yeh game jeet gaye hai ")

    if answer == question[-1]: 
        print(f"correct answer, you have won {prize} rupees")
        return True, lifeline_used
    else:
        print(f"answer is incorrect, the correct answer is {question[question[-1]]}") 
        print(f"your take home money is 0 rupees")
        return False, lifeline_used


def lifeline(question, lifelines):
    print("Lifeline options:")
    for idx, name in enumerate(lifelines, 1):
        print(f"{idx}. {name}")
    try:
        choice = int(input(f"Choose your lifeline (1-{len(lifelines)}): "))
        if 1 <= choice <= len(lifelines):
            selected = lifelines[choice-1]
            if selected == "50-50":
                options = [question[1], question[2], question[3], question[4]]
                correct_index = question[-1] - 1
                correct_option = options[correct_index]
                incorrect_indices = [i for i in range(4) if i != correct_index]
                keep_incorrect = random.choice(incorrect_indices)
                shown_options = [correct_option, options[keep_incorrect]]
                random.shuffle(shown_options)
                print(f"\nRemaining options: {shown_options[0]} and {shown_options[1]}")
                print('Remaining option numbers:', [options.index(opt)+1 for opt in shown_options])
            elif selected == "Phone a friend":
                print("You called a friend, and they think the answer is:", question[question[-1]])
            elif selected == "Ask the audience":
                print("\nThe audience thinks the answer is:", question[question[-1]]) 
                print("\nAudience poll results: 70% for option", question[question[-1]], ", 30% for others") 
            return selected
        else:
            print("Invalid lifeline choice.")
    except:
        return None  

    
def start_kbc():
    print("Welcome to the KBC Game!")
    lifelines = ["50-50", "Phone a friend", "Ask the audience"]
    for i, question in enumerate(question_data):
        prize = levels[i]
        result, _ = ask_question(question, prize, lifelines)
        if not result:
            break
        print()
if __name__ == "__main__":
    start_kbc()


