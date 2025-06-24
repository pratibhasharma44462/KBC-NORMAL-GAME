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

def ask_question(question, prize, lifeline_used): 
    print(f"\nQuestion: {(question[0])}") 
    print(f"Question for rupees: {prize}") 
    print(f"a. {question[1]}     b. {question[2]}") 
    print(f"c. {question[3]}     d. {question[4]}") 

    if not lifeline_used:
        use_lifeline = input("Do you want to use a lifeline? (yes/no): ").strip().lower()
        if use_lifeline == "yes":
            lifeline(question)
            lifeline_used = True

    answer = int(input("Your answer in preference to question(1-4) or press 0 to exit: "))
    

    if answer == 0:
        print(f"You have out of the game , money you take home with you {prize} rupees")
        return False, lifeline_used

    if answer == question[-1]: 
        print(f"correct answer, you have won {prize} rupees")
        return True, lifeline_used
    else:
        print(f"answer is incorrect, the correct answer is {question[question[-1]]}") 
        print(f"You have lost the game, you have won 0 rupees")
        if prize >= 1000:
            prize = 0
            if prize == 70000000:
                print("\nCongratulations, aap yeh game jeet gaye hai") 
        else:    
            print(f"your take home money is {prize}rupees")
        return False, lifeline_used
    
def lifeline(question):
    print("Lifeline options:")
    print("1. 50-50")
    print("2. Phone a friend")
    print("3. Ask the audience")
    choice = int(input("Choose your lifeline (1-3):"))
    if choice == 1:
        options = [question[1], question[2], question[3], question[4]]
        correct_index = question[-1] - 1
        correct_option = options[correct_index]
        incorrect_indices = [i for i in range(4) if i != correct_index]
        keep_incorrect = random.choice(incorrect_indices)
        shown_options = [correct_option, options[keep_incorrect]]
        random.shuffle(shown_options)
        print(f"Remaining options: {options[0]} and {options[1]}")
    elif choice == 2:
        print("You called a friend, and they think the answer is:", question[question[-1]])
    elif choice == 3:
        print("\nThe audience thinks the answer is:", question[question[-1]]) 
        print("\nAudience poll results: 70% for option", question[question[-1]], ", 30% for others")    



    
def start_kbc():
    print("Welcome to the KBC Game!")
    for i, question in enumerate(question_data):
        lifeline_used = False
        prize = levels[i]
        result, lifeline_used = ask_question(question, prize, lifeline_used)
        if not result:
            break
        print()
if __name__ == "__main__":
    start_kbc()        




