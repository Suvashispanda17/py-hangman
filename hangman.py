import random as rn
stage = [
    """
   ------
   |    |
   |    
   |    
   |    
   |    
=========
""",
    """
   ------
   |    |
   |    O
   |    
   |    
   |    
=========
""",
    """
   ------
   |    |
   |    O
   |    |
   |    
   |    
=========
""",
    """
   ------
   |    |
   |    O
   |   /|
   |    
   |    
=========
""",
    """
   ------
   |    |
   |    O
   |   /|\\
   |    
   |    
=========
""",
    """
   ------
   |    |
   |    O
   |   /|\\
   |   / 
   |    
=========
""",
    """
   ------
   |    |
   |    O
   |   /|\\
   |   / \\
   |    
=========
"""
]
words= [
    {"word": "Python", "hint": "A popular programming language."},
    {"word": "Matrix", "hint": "Used in linear algebra and mathematics."},
    {"word": "Algorithm", "hint": "Step-by-step solution for solving problems."},
    {"word": "Eclipse", "hint": "An astronomical event when the sun or moon is obscured."},
    {"word": "Cricket", "hint": "A sport played with a bat and ball."},
    {"word": "Pacemaker", "hint": "A device that regulates heartbeats."},
    {"word": "Podcast", "hint": "Digital audio episodes available online."},
    {"word": "Cursor", "hint": "A movable pointer on a computer screen."},
    {"word": "Galaxy", "hint": "A vast collection of stars and planets."},
    {"word": "Cryptography", "hint": "The art of writing or solving codes."},
    {"word": "Compiler", "hint": "Translates code into executable programs."},
    {"word": "Tornado", "hint": "A rotating column of air touching the ground."},
    {"word": "Neuron", "hint": "A basic unit of the nervous system."},
    {"word": "Velocity", "hint": "Speed with direction."},
    {"word": "Symmetry", "hint": "Balanced proportions on both sides."},
    {"word": "Pendulum", "hint": "A swinging object in clocks or science experiments."},
    {"word": "Binary", "hint": "A number system with only 0s and 1s."},
    {"word": "Photosynthesis", "hint": "Plants use this process to make food."},
    {"word": "Satellite", "hint": "Orbits around planets or stars."},
    {"word": "Robot", "hint": "A machine capable of carrying out tasks automatically."}
]

chosen= rn.choice(words)
wrd=chosen["word"].lower()

hnt=chosen["hint"]

display= ["_" for _ in wrd]

attempts= 6

print('                        ---Welcome To Hangman---        ')

print("\n")

print(f"Hint:   {hnt}")

if __name__ ==  "__main__":
    while attempts > 0 and '_' in display:
        print(stage[6 - attempts])
        print("\n" + " ".join(display))
        guess= input("Guess The Words-> ").lower()

        if guess in wrd:
            for index, letter in enumerate(wrd):   
                if letter == guess:
                    display[index]=guess
        else:
            print("The Letter Dosen't Appear")
            attempts -= 1
            print(f"Attempts: {attempts}")

if '_' not in display:
    print("YOU SURVIVED ")
    print("\n")
    print(" ".join(display))
    
                  
else:
    print(stage[6])
    print("YOU RAN OUT OF ATTEMPtS",wrd)
    print("IDIOT!!!!")
