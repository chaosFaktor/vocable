import modules.ANSIcolour as ansi
import modules.selUI as ui
import modules.uniKey as unikey

from itertools import count
import os
import time

score = 0
maxscore = 0

os.system("clear")
print("Was willst Du lernen?")
options = os.listdir("./vocabulary")
for i in range(0,len(options)):
    options[i] = (options[i].replace(".2voc", "<2voc>")).replace(".voc", "<voc>")


menu = ui.SelectionMenu.create(options, "Was willst Du lernen?", ["|", "O", " ", 0, "-", 48])
while True:
    os.system("clear")
    print(menu.refresh())

    inp = unikey.Get.getch()
    if inp in ["w", "W", "8", "^[[A"]:
        menu.selDown()
    elif inp in ["s", "S", "2", "^[[B"]:
        menu.selUp()
    elif inp in ["d", "D", "5", "6", "\n" "^[[C"]:
        voc_path = "vocabulary/"+menu.select()
        break


voc_path=voc_path.replace("<2voc>", ".2voc")
voc_path=voc_path.replace("<voc>", ".voc")
if ".2voc" in voc_path:
    vocabular = open(voc_path, "r").readlines()
    start_time = time.time()
    os.system("clear")

    #if "--q-a--" in voc_path:
    try:

        countA = 0
        for i in vocabular:

            i = i.replace("\n", "")
            if countA == 0:
                question = str(i)

            elif countA == 1:
                answer = str(i)


                print("Score: " + str(score))
                print(question)
                plans = input()
                maxscore += 1
                if plans == answer or plans == answer.replace(" ", ""):
                    print("Richtig!")

                    time.sleep(0.2)
                    score = score + 1
                    os.system("clear")
                else:
                    print("Falsch:")
                    print(answer)
                    time.sleep(1)
                    input()
                os.system("clear")
            if countA == 0:
                countA+=1
            else:
                countA = 0

    except KeyboardInterrupt:
        print()


elif ".voc" in voc_path:
    vocabular = open(voc_path, "r").readlines()
    start_time = time.time()
    os.system("clear")
    try:
        for i in vocabular:
            i = i.replace("\n", "")
            os.system("clear")
            print("Nächste Vocabel bitte!                                             score: " + str(score))
            inp = str(input())
            if inp == str(i):
                score = score + 1
                print("richtig!")
                time.sleep(0.2)
            else:
                print("Falsch!")
                print(i)
                time.sleep(1)
                input()
            maxscore = maxscore + 1
            if inp == "let me leave!!--":
                break
    except KeyboardInterrupt:
        print()


end_time = time.time()
os.system("clear")
print("Dein Score ist: " + str(score)+ " von: " + str(maxscore))
print("Du hast " + str(round(end_time - start_time)) + " Sekunden gebraucht")
