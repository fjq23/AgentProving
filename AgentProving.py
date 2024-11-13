
from gpt_text import GPT4Model
import openai
from prompt import FORMATTED_PROMPT, TASK_DESCRIPTION, parse_opr
from formula import Formula, Element
import time


def colored_print(text, color_code):
    print(f"\033[{color_code}m{text}\033[0m")
# {A, -A} => None


model = GPT4Model()
history = []
mode = input("Choose your proving mode:\n- A. Proof by Contradiction\n- B. Goal-Oriented Proof\nEnter A or B:\n")
target = None
if mode == "A":
    print("You are in the 'Proof by Contradiction' mode.")
elif mode == 'B':
    print("You are in the 'Goal-Oriented Proof' mode. Please enter your proving target (an atomic proposition):\n")
    target = input()
else:
    print("Please enter a valid option!")
    exit(0)

n = int(input("Please enter the amount of elements:\n"))
element_list = []
for i in range(0,n):
    element_str = input(f"Enter your {i + 1}th element ({i + 1} out of {n}):")
    # print(list(set(element_str.split('v'))))
    element = Element(element_str)
    element_list.append(element)

formula = Formula(element_list, target)

while(True):
    colored_print("---------------------------", "36")
    colored_print(f"CURRENT: {formula}", "33")
    print(f"HISTORY: {history}")
    prompt = FORMATTED_PROMPT % ( TASK_DESCRIPTION, "\n".join(history), formula)
    output = model.call_gpt_api(prompt)
    cmd = parse_opr(output)
    colored_print(f"AGENT OPERATION: {cmd}", "34")
    if mode == "A" and str(formula.elements[len(element_list) - 1])  == "contradiction":
        break
    elif mode == "B" and str(formula.elements[len(element_list) - 1])  == target:
        break
    if cmd == "STOP":
        break
    time.sleep(1)
    history.append(str((str(formula), output)))
    formula.merge_and_append(cmd)

colored_print("---------------------------", "36")

if mode == "A":
    if str(formula.elements[len(element_list) - 1]) != "contradiction":
        colored_print("Failed! Maybe your input is not correct!", "31")
        exit(0)
    colored_print("We got a contradiction here!\nProof:", "32")
    print()
    print(history)
    print(formula)
    print("\nQ.E.D")
elif mode == "B":
    if str(formula.elements[len(element_list) - 1]) != target:
        colored_print("Failed! Maybe your input is not correct!", "31")
        exit(0)
    colored_print(f"We got {target} here!\nProof:", "32")
    print(history)
    print(formula)
    print("\nQ.E.D")

