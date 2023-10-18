import time
def loading():
    print("Loading .", end=''), time.sleep(0.5)
    print(".", end=''), time.sleep(0.5)
    print(".", end=''), time.sleep(0.5)
    print(".\n")


def intro():
    print("╔═════════════════════════════════════════════════════════════════════════════════════════╗")
    print("    PHILIPPINES. A NEWLYWED COUPLE, NAMELY JUAN DELA CRUZ AND MARIA DELA CRUZ WILL HAVE"), time.sleep(1)
    print("║   THEIR HONEYMOON.  IN A PLACE WHERE DIFFERENT UNNATURAL CREATURES EXIST. JUAN WHO IS   ║"), time.sleep(1)
    print("    AN EX-NAVY WILL TRY TO SAVE THEIR WIFE FROM THESE CREATURES. YOU WILL PLAY AS JUAN."), time.sleep(1)
    print("║   YOUR ACTIONS  WILL  HAVE  AN  EFFECT  ON  WHAT  JUAN WILL  DO  THROUGHOUT THE GAME.   ║"), time.sleep(1)
    print(""), time.sleep(1.5)
    print("║   REMEMBER!! YOUR ACTIONS HAS CONSEQUENCES. IT MAY LEAD TO SUFFERING OR VICTORY. SAVE   ║"), time.sleep(1)
    print("    MARIA AND YOU WILL WIN THE GAME. BAD CHOICES AND YOU WILL LOSE HER. FIGHT UNTIL THE"), time.sleep(1)
    print("║                                   VERY END.                                             ║"), time.sleep(1)
    print(""), time.sleep(1.5)
    print("║                                HANDA KA NA BA?                                          ║"), time.sleep(1)
    print("                          TULUNGAN KA NAWA, JUAN DELA CRUZ                                "), time.sleep(1)
    print("╚═════════════════════════════════════════════════════════════════════════════════════════╝ \n"), time.sleep(1.5)


def title():
    print("╔═════════════════════════════════════════════════════════════════════════════════════════╗")
    print("║  ╔═════╗ ╔═╗ ╔═════╗ ╔════╗ ╔═╗ ╔═╗    ╔═╗ ╔═╗ ╔═╗ ╔═╗ ╔═════╗ ╔═════╗ ╔═════╗ ╔═════╗  ║")
    print("║  ║     ║ ║ ║ ║ ╔═╗ ║ ║    ║ ║ ╚═╝ ║ ╔╗ ║ ╚═╝ ║ ║ ║ ║ ║ ║ ╔═╗ ║ ╚═╗ ╔═╝ ║     ║ ║     ║  ║")
    print("║  ║ ╔═══╝ ║ ║ ║ ║ ║ ║ ║    ║ ╚═╗ ╔═╝ ╚╝ ║ ╔═╗ ║ ║ ╚═╝ ║ ║ ║ ║ ║   ║ ║   ║ ╔═══╝ ║ ╔═══╝  ║")
    print("║  ╚═╝     ╚═╝ ╚═╝ ╚═╝ ╚════╝   ╚═╝      ╚═╝ ╚═╝ ╚═════╝ ╚═╝ ╚═╝   ╚═╝   ╚═════╝ ╚═╝ ╚═╝  ║")
    print("║     ╔══╗                                                                                ║")
    print("║    ╔╣  ╠═════════════════════════════════════════════════════════════════════════════╗  ║")
    print("║║║║║║   ╠══════════ T H E     M A L I G N O     C H R O N I C L E S ══════════════════║  ║")
    print("║    ╚╣  ╠═════════════════════════════════════════════════════════════════════════════╝  ║")
    print("║     ╚══╝                                                                                ║")
    print("╚═════════════════════════════════════════════════════════════════════════════════════════╝\n")
    print("                              [S]tart Game   [E]xit \n")
    while True:
        action = input("                                      >> ")
        if action == 'S' or action == 's':
            break
        elif action == 'E' or action == 'e':
            exit()
        else:
            print("                          [ Type S to start or E to exit. ]\n")


def credits():
    print(""), time.sleep(0.7), print(""), time.sleep(0.7), print(""), time.sleep(0.7)
    print(""), time.sleep(0.7), print(""), time.sleep(0.7), print(""), time.sleep(0.7)
    print("   ╔═════╗ ╔═╗ ╔═════╗ ╔════╗ ╔═╗ ╔═╗    ╔═╗ ╔═╗ ╔═╗ ╔═╗ ╔═════╗ ╔═════╗ ╔═════╗ ╔═════╗   ")
    time.sleep(0.7)
    print("   ║     ║ ║ ║ ║ ╔═╗ ║ ║    ║ ║ ╚═╝ ║ ╔╗ ║ ╚═╝ ║ ║ ║ ║ ║ ║ ╔═╗ ║ ╚═╗ ╔═╝ ║     ║ ║     ║   ")
    time.sleep(0.7)
    print("   ║ ╔═══╝ ║ ║ ║ ║ ║ ║ ║    ║ ╚═╗ ╔═╝ ╚╝ ║ ╔═╗ ║ ║ ╚═╝ ║ ║ ║ ║ ║   ║ ║   ║ ╔═══╝ ║ ╔═══╝   ")
    time.sleep(0.7)
    print("   ╚═╝     ╚═╝ ╚═╝ ╚═╝ ╚════╝   ╚═╝      ╚═╝ ╚═╝ ╚═════╝ ╚═╝ ╚═╝   ╚═╝   ╚═════╝ ╚═╝ ╚═╝   ")
    time.sleep(0.7)
    print("   ══════════════════ T H E     M A L I G N O     C H R O N I C L E S ══════════════════ \n")
    time.sleep(0.7)

    print("   ══════════════════════════════ D E V E L O P E R S ══════════════════════════════════\n")
    time.sleep(0.7)
    print("                                 AUDRIE BRYLLE CATAPAT"), time.sleep(0.7)
    print("                                  JOHN CARLO JIMENEZ"), time.sleep(0.7)
    print("                                 LEUR JEREMY MAGTIBAY"), time.sleep(0.7)
    print("                                   JOHN MARK AFABLE"), time.sleep(0.7)
    print("                                  JEZZELA RIVADENERA\n"), time.sleep(0.7)
    print("                                     INF191 © 2019"), time.sleep(0.7)
    print("   ═════════════════════════════════════════════════════════════════════════════════════\n")


################
intro()
while True:
    title()

    loading()

    print("     Juan dela Cruz and his wife, Maria went to a vacation tour in the province of Siquijor")
    print(" celebrating their honeymoon. In the province, running out of options, they decided to stay ")
    print(" in a barrio named \"Sitio Kababalaghan\". Despite the name, the people there are quite nice")
    print(" and accommodating to their visitors. However, they notice something strange in the barrio,")
    print(" they see many cross planted on the ground, as if they were mourning for dead people...")

    action = input(), loading()

    print("     Tired from their travel, the couple have talked to pick a place for them to stay.")
    print(" Luckily, they were greeted by Guido, a local from the barrio, who presented as their tour")
    print(" guide. Guido helps them in finding a place for them to stay and presented two offers. He")
    print(" asked which place you would like to stay.\n")

    while True:
        print("         [A] A resort (expensive but comfortable)")
        print("         [B] A little house (cheap but strange)\n")
        action = input("         ACTION >> ")
        if action == 'A' or action == 'a':
            print("\n     Guido go to and ask the reception. He said to the couple that the rooms are ")
            print(" unavailable. Juan is somehow wondering why it is unavailable even though he don't see much")
            print(" people in the resort. Out of options, the couple has decided to stay in the little house.")
            action = input(), loading()
            break
        elif action == 'B' or action == 'b':
            print(""), loading()
            break
        else:
            print("\n     It is getting dark. Juan should pick a place to stay now.\n")

    print("     Juan and Maria now spend the night in a little house owned by Mang Leandro, a friend")
    print(" of Guido. Mang Leandro seems to be of old age and all alone in the place. For dinner, the")
    print(" served the couple an unusual food, which was immediately noticed by the couple. Maria eats")
    print(" the food even though she looks like she is about to puke. While Juan is struggling to even")
    print(" swallow his food.\n")

    while True:
        print("         [A] Juan spit the food")
        print("         [B] Juan finally eat the food with discomfort\n")
        action = input("         ACTION >> ")
        if action == 'A' or action == 'a':
            print("\n     The owner was intimidated by Juan's actions and gave him a bad look. Juan felt ashamed")
            print(" and went outside the house. He was approached by Guido and asked what's wrong. Juan said")
            print(" that he feels unease about the place, like there is something hidden. Guido agreed to him")
            print(" and share a mystery that goes around the place. That the people they're mourning for are ")
            print(" not really dead but gone missing. Guido also warned the couple to be safe and to stay away")
            print(" from danger. After the conversation, Juan went back to the house and now go to sleep with")
            print(" Maria which is already sleeping in the bedroom. ")
            action = input(), loading()
            print("     The next day, the couple will go on a tour in the barrio with Guido. Before they left,")
            print(" Mang Leandro with a suspicious and scary smile, said that he will be waiting for them when")
            print(" they get back. Maria feel terrified and asked Juan and Guido for them to leave immediately.")
            print("")
            print("     In the middle of the tour, Maria shares something to her husband. She told about what")
            print(" happened after dinner. She told Juan how Mang Leandro acts very strange and how she felt ")
            print(" scared. Upon hearing, Juan is really getting suspicious about the place and its people.")
            action = input(), loading()
            break
        elif action == 'B' or action == 'b':
            print("\n     Juan felt bad about the food and went outside to get some fresh air. Maria is now left")
            print(" behind in the house. Maria go to the living room after eating. She is joined by a fidgety")
            print(" Mang Leandro. Out of the blue, the old man asked Maria if she's still a virgin. Maria felt")
            print(" irritated about the question but she just ignored it. After a few minutes, the old man")
            print(" still go on about it, asking her if she have ever tried to eat intestines. Maria now feels")
            print(" scared so she go to the bedroom leaving the old man alone and went to sleep. After a while")
            print(" she is joined by her husband after getting some fresh air.")
            action = input(), loading()
            print("     The next day, the couple will go on a tour in the barrio with Guido. Before they left,")
            print(" Mang Leandro with a suspicious and scary smile, said that he will be waiting for them when")
            print(" they get back. Maria feel terrified and asked Juan and Guido for them to leave immediately.")
            print("")
            print("     In the middle of the tour, Juan shares something to his wife. He shares what Guido has")
            print(" said to him. That there is a mystery covering the place. He thinks that they are not safe")
            print(" here. With all the stories, the couple agreed to be more vigilant.")
            action = input(), loading()
            break
        else:
            print("\n     The old man is staring at you... \n")

    print("     After a long day, the couple decided to go back to their place. Juan had gone directly")
    print(" straight to the bedroom and went to sleep. Maria, on the other hand, went outside to use")
    print(" the restroom.")
    action = input(), loading()
    print("     While taking a bath, Maria notices and heard a rustling sound outside the bathroom as")
    print(" if there was something near. She got scared. She hastily fix herself and went back to the")
    print(" house. However, as she was opening the door, there's something that tried to knock her off.\n")

    while True:
        print("         [A] Ward off fast and escape.")
        print("         [B] Punch it\n")
        action = input("         ACTION >> ")
        if action == 'A' or action == 'a':
            print("\n    Maria had evaded it and quickly went back to the house. She entered the house nervously")
            print(" and didn't want to wake up her husband and she will told him tomorrow what happened....")
            print(" However, as she was about to enter the bedroom, it appeared again, abducts, Maria and put")
            print(" her into sleep. It carry Maria on its shoulder as if she was a bag. They went away to the")
            print(" other side of the barrio.")
            action = input(), loading()
            break
        elif action == 'B' or action == 'b':
            print("\n     It catches Maria's punch and knock off Maria. It picks up Maria on its shoulder as if")
            print(" she was a bag. Maria screams and yells for someone to help her. But it seems that no one")
            print(" even cares for her. To avoid attention, Maria is put into sleep, and they went away to the")
            print(" other side of the barrio.")
            action = input(), loading()
            break
        else:
            print("\n     You need to think and act fast...\n")

    print("     Juan wakes up. Shocked not seeing his wife beside her. He got scared. He went outside")
    print(" and asks the residents if they notice something strange happening last night. Some people")
    print(" said that they saw something, some say that they heard a woman screaming. Until he meets ")
    print(" an elder from the barrio, saying that there are other instances where people, especially")
    print(" women, had gone missing on their stay here during the night. After what he has heard from")
    print(" the elder, he frustratedly search for a solution...")
    action = input(), loading()
    print("     Meanwhile... in a cave far away from the barrio, it is covered and secluded inside a")
    print(" forest. It seems to be the hideout of these scary creatures which gathers here every night.")
    print(" This night, they are preparing for a big feast, with all of their gathered sacrifice, which")
    print(" will happen on the next day where there will be a full moon. Maria is tied up on a special")
    print(" cage as the main sacrifice. She is terrified and trembling from what she is witnessing that")
    print(" these creatures are preparing for")

    action = input(), loading()

    print("     While Juan is searching for his wife, in a dark corner, Guido appeared and called him")
    print(" to come near him. Guido said that they need to talk privately in the woods. Juan just join")
    print(" Guido on his way to the woods.")
    action = input(), loading()
    print("     In the forest, now all alone, Guido presented a way on how to find Maria. He told Juan")
    print(" the abduction was done by what they called \"Aswangs\" and they tend to make Maria as their")
    print(" sacrifice. Guido said that Maria can still be saved if they act now. They just need to pass")
    print(" through the forest and go to creatures' hideout and get Maria. Guido will help Juan if he")
    print(" considers his proposition.\n")

    while True:
        print("         [A] Feeling hopeless, don't hesitate and quickly accept Guido's proposition.")
        print("         [B] Think about the proposition. Feeling suspicious. Walked away from Guido.\n ")
        action = input("         ACTION >> ")
        if action == 'A' or action == 'a':
            print("\n    Juan told Guido that he will accept his help. Guido warned him that they will encounter")
            print(" and face different creatures until they reached Maria. Also that human beings are not")
            print(" allowed in that kind of place. ")
            action = input(), loading()
            print("     They prepared the night before. Guido gave Juan a bolo just in case bad things happen.")
            print(" They left the barrio at dawn.")
            action = input(), loading()
            break
        elif action == 'B' or action == 'b':
            print("\n     Juan said that it is not possible because Aswangs are not real. He left then went back")
            print(" home to sleep. While sleeping, Juan heard another woman screaming. He wakes up immediately")
            print(" and barely saw the incident. Juan is full of anger, thinking that it is also the reason")
            print(" why her wife is missing.")
            action = input(), loading()
            print("     Juan immediately finds Guido to tell him what happened and he will now accept his help.")
            print(" Guido gave Juan a bolo just in case bad things happen. They left the barrio at dawn.")
            action = input(), loading()
            break
        else:
            print("\n     Guido is waiting for your response...\n")

    print("     Juan and Guido's journey starts. They ride a habal-habal until they reached the forest.")
    print(" Once they reached the forest, they now go on by foot. As they are entering the forest, they")
    print(" noticed that it is too dark and scary. While walking through the deep forest, they reached")
    print(" a place where there are too many huge mushrooms which are glowing in the dark. The aura is")
    print(" so fun and lovely..")
    action = input(), loading()
    print("     In the lovely mushroom place, Juan accidentally stepped on a small mushroom. The place")
    print(" suddenly turns into a dark, rotting place of mushroom. Then small creatures called \"Dwende\"")
    print(" appeared with a scary appearance like a dirty zombie. They can't get pass the place because")
    print(" Juan destroyed one of their houses. They are now surrounded by angry Dwendes. Guido reminds")
    print(" Juan that these creatures are clever and not to be trusted.")
    action = input(), loading()
    print("     One particular Dwende is running towards Juan. Then the scene suddenly changed. Juan")
    print(" saw her wife running to him asking for help.\n")

    while True:
        print("         [A] Run to the woman and help her.")
        print("         [B] Ignore the woman and stab her with the bolo.\n")
        action = input("         ACTION >> ")
        if action == 'A' or action == 'a':
            print("\n     The scene changed again and the Dwende attacked him. Juan was shocked. The Dwende bite")
            print(" the neck of Juan. Juan get hurt and fall to the ground. The other Dwendes throw stones at")
            print(" him and other ganged up on Juan. Then suddenly, a loud scream was heard through the place,")
            print(" like a scream of an Aswang. All the Dwendes run away and hide from what they heard, which")
            print(" made them all terrified.")
            action = input(), loading()
            print("     The Dwendes left Juan full of scars and a broken leg. Juan then saw Guido hiding and")
            print(" standing behind a mushroom. Guido helped Juan to stand up and they continued the journey.")
            action = input(), loading()
            break
        elif action == 'B' or action == 'b':
            print("\n     The other dwendes get really mad and attacked Juan. Juan fight back. With his bolo, he")
            print(" killed many of the Dwendes while the other ran because they too few to fight. ")
            action = input(), loading()
            print("     Then he finds Guido hiding and standing behind a mushroom. Guido told Juan that he got")
            print(" scared. Guido also told Juan that they should move fast because it will get more and more")
            print(" dangerous at night.")
            action = input(), loading()
            break
        else:
            print("\n     Can't find Guido. You need to decide on your own...\n")

    print("     Juan is tired and hurt from all the fighting a while ago. They have arrived in a foggy")
    print(" river in the forest. The river is too wide to get to the other side, however it is near to")
    print(" swim across. Juan saw a big heavy log to cross...\n")

    while True:
        print("         [A] Move the log to use to cross the river.")
        print("         [B] Swim across the river.\n")
        action = input("         ACTION >> ")
        if action == 'A' or action == 'a':
            print("\n     It takes time, but Juan and Guido managed to move the log for them to cross the river.")
            action = input(), loading()
            print("     They cross the river using the log... Because Juan was injured and hurt, he got out of")
            print(" balance and fall to the river. Guido tried to help him but the river's flowing hard and he")
            print(" got far. Something bit Juan's thigh and pulled him deeper into the river. He is struggling")
            print(" and drank some water.... and suddenly he sees it hazily.... it is a \"Shokoy\"...")
            action = input(), loading()
            break
        elif action == 'B' or action == 'b':
            print("\n     Without hesitation, they swim in the river.")
            action = input(), loading()
            print("     They both swim through the river. First to cross was Guido and got on the other side.")
            print(" While Juan is swimming in the river, there is something that bite his thigh. It pulled him")
            print(" deeper into the river. He is struggling and drank some water.... and then suddenly he sees")
            print(" it hazily.... it is a \"Shokoy\"...")
            action = input(), loading()
            break
        else:
            print("\n     It is getting late. You should act fast...\n")

    print("     Juan notices that his bolo fall off from him and went to the river ground. He tries to")
    print(" stop and get away from the Shokoy.\n")

    while True:
        print("         [A] Break free and reach for the bolo.")
        print("         [B] Fight and try to strangle the Shokoy.\n")
        action = input("         ACTION >> ")
        if action == 'A' or action == 'a':
            print("\n     Juan get caught by the Shokoy and pulled him into the surface water. He continue on")
            print(" fighting but he is weakening because of the injuries he sustained from the last fight. He")
            print(" was about to give up. Just before he close his eyes, Juan notices a fast creature which")
            print(" quickly go to the river... Juan then lost his consciousness...")
            action = input(), loading()
            print("     Juan wake up on the other side of the river, with his bolo on his side. He first saw")
            print(" Guido, then Guido told what happened and said that Juan was unconscious for several hours.")
            print(" He told Juan that he got scared so that he didn't help but luckily the Shokoy got away. He")
            print(" helped Juan stand up and reminds him that it is nearly midnight and they should continue")
            print(" their journey.")
            action = input(), loading()
            break
        elif action == 'B' or action == 'b':
            print("\n     Juan is desperate to get away from the Shokoy. He then strangles it and beat the hell")
            print(" out of the creature. It got scared and ran away from the human. Then he go on crossing the")
            print(" river.")
            action = input(), loading()
            print("     When Juan reached the other side, Guido was impressed with him on how he handled the")
            print(" situation. Guido reminded Juan that they are nearing in saving Maria. They continue their")
            print(" journey.")
            action = input(), loading()
            break
        else:
            print("\n     The Shokoy is pulling you deeper into the river...\n")

    print("     They have arrived in a smoky, dark place. They heard huge and deep voices that utters")
    print(" scary words. A three consecutive big, dark, creature jump from the trees. They are called")
    print(" \"Kapres\" Juan and Guido saw that there are plenty of eyes that they used as necklace. The")
    print(" Kapres said that you can't go anywhere from this place and that they will be dead now.")
    action = input(), loading()
    print("     Juan feeling restless and tired from the last battles, just want to save her wife, and")
    print(" just want to finish this once and for all.\n")

    while True:
        print("         [A] Fight and kill the Kapres with your bolo.")
        print("         [B] Talk and try to convince the Kapres.\n")
        action = input("         ACTION >> ")
        if action == 'A' or action == 'a':
            print("\n     With all his strength and his bolo, Juan fights off the Kapres. He used the smoke in")
            print(" the place to his advantage. He sneaks up to the Kapres and each one was stabbed. He was")
            print(" also get beaten up by the Kapres. But by using all his strategies, he finally defeated all")
            print(" the Kapres.")
            action = input(), loading()
            print("     After defeating the creatures, Juan notices that Guido was not around, but ignores it")
            print(" and continue on because he knows that Maria is already near and he cannot waste any more")
            print(" time. While he was walking, Juan heard loud scary sounds, fast creature moving and leaping")
            print(" everywhere. he turned around and saw Guido but something is different...")
            action = input(), loading()
            print("     Guido, with a grim smile, has told the truth. He told Juan that he's the leader of the")
            print(" Aswangs and about the big feast and how his wife was included. He told him that he can't")
            print(" save Maria anymore. Guido also thanks Juan that by killing the other creatures, it makes")
            print(" them, it makes the Aswangs as the dominant creatures in the forest. Slowly reverting back")
            print(" to his creature form, he said that he will now kill Juan.")
            action = input(), loading()

            print("     Juan is now really desperate and very angry especially after he learned the truth about")
            print(" Guido and the Aswangs. Bursted in anger and hatred, he fought Guido and tried to kill him.\n")
            print("         [ Stab him and beat him ]")
            action = input()
            print("     Guido was hurt and Juan got bruises. Juan also caught the Aswang.\n")
            print("         [ Strangle him ]")
            action = input()
            print("     The Aswang was strangled tightly. Juan deeply crushes its neck. \n")
            print("         [ Stab its chest with the bolo ]")
            action = input()
            print("     The Aswang fell to the ground. While bleeding, Guido told Juan that he's too late.\n")
            print("         [ Cut his head off ]")
            action = input()
            print("     Juan cuts Guido's head off, saying that this is for his wife.")
            action = input(), loading()

            print("     After defeating Guido, he brought with him his head, and quickly runs to the cave. He")
            print(" heard noises as if they were celebrating while running inside the cave. He saw the Aswangs")
            print(" feasting on a woman eating her inside organs. Juan said \"STOP!!!\" and raise the head that")
            print(" he brought. All the Aswangs noticed and look at Juan and the head. The Aswangs was scared")
            print(" that there leader is now dead. They ran outside the cave.\n")

            while True:
                print("         [A] Chase them and kill them all.")
                print("         [B] Let them go.\n")
                action = input("         ACTION >> ")
                if action == 'A' or action == 'a':
                    print("\n     Juan killed some of the Aswangs, he managed to catch. But then he saw Maria. Juan stop")
                    print(" and quickly runs toward his wife, crying.")
                    action = input(), loading()
                    break
                elif action == 'B' or action == 'b':
                    print("\n     Juan saw Maria on the ground. He quickly runs toward his wife, crying.")
                    action = input(), loading()
                    break
                else:
                    print("\n     The Aswangs are getting away...\n")

            print("     Juan saw Maria dead on the ground without her inside organs. He cried so hard. He was")
            print(" disappointed in himself, he didn't reach on time. He lost his wife. He lost Maria.")
            action = input(), loading()
            print("  ╔══════════════════════════════════════════════════════════════════════════════════════╗")
            print("  ║ You LOSE. You didn't save Maria. As what we have mentioned your choices affect what  ║")
            print("  ║        Juan would do. Remember to think about your actions before you do it...       ║")
            print("  ╚══════════════════════════════════════════════════════════════════════════════════════╝")
            action = input(), loading()

            print("     Maria is now dead. The Aswangs are still out there. Juan has now dedicated his life to")
            print(" kill Aswangs. To prevent what happened to his wife to other people. He will try to avenge")
            print(" his late wife by slaying all creatures that are deadly and will bring harm to other people.")
            print(" He goes to everywhere to search and kill creatures that as bad intentions to humans.")
            action = input(),
            break
        elif action == 'B' or action == 'b':
            print("\n     He told the Kapres that he must save his wife and let him pass through. But the Kapres")
            print(" are still not swayed by his reason. Until Juan asked why there are eyes hanging on their")
            print(" The Kapres told Juan that people who wants to pass through needs to lose an eye. There is")
            print(" no need for violence. Juan feeling eager to save his wife, openly accept and sacrifice his")
            print(" eye to the Kapres.")
            action = input(), loading()
            print("     While one of the Kapres is about to reach for the eye of Juan, there is something that")
            print(" bit its neck and tear its head off. It turns the other Kapres angry and attacks Juan. With")
            print(" no ther choice, Juan with a single eye, fights off the Kapres. He used the smoke in the")
            print(" place to his advantage. He sneaks up to the Kapres and each one was stabbed. He was also")
            print(" get beaten up by the Kapres.")
            action = input(), loading()
            print("     Juan sustained some bruises from the fighting but he finally defeated the creatures.")
            action = input(), loading()

            print("     Juan has finally killed the Kapres. Juan also lost his eye. He still can't find Guido")
            print(" so he continue on, knowing that Maria is already near. As he was about to enter the cave,")
            print(" Juan heard voices of women screaming inside the cave. So he quickly rushes into the cave.")

            action = input(), loading()

            print("     Juan saw the Aswang celebrating and Maria is being presented as the final sacrifice.")
            print(" Maria is tied up on a table naked. Surrounded by the Aswnags, which are all chanting ritual")
            print(" words before performing the sacrifice.")

            action = input(), loading()

            print("     Juan yells \"STOP!!!\" All the Aswangs look at him. One particular Aswang approached him.")
            print(" While the Aswang is shifting back to its human form, Juan notices something strange about")
            print(" this creature, and to his big surprise... it was Guido.")

            action = input(), loading()

            print("     Guido, with a grim smile, has told the truth. He told Juan that he's the leader of the")
            print(" Aswangs and about the big feast and how his wife was included. He told him that he can't")
            print(" save Maria anymore. Guido also thanks Juan that by killing the other creatures, it makes")
            print(" them, it makes the Aswangs as the dominant creatures in the forest. Slowly reverting back")
            print(" to his creature form, he said that he will now kill Juan.")

            action = input(), loading()

            print("     Juan, with all his hatred and making a fool out of him, said that he will kill every")
            print(" single one of them. He fights all the Aswangs, one by one. The last creature standing is")
            print(" Guido. Juan vowed that he will kill him and cut his head off. Bursted in anger and hatred,")
            print(" he fought Guido and try to kill him.\n")

            print("         [ Stab him and beat him ]")
            action = input()
            print("     Guido was hurt and Juan got bruises. Juan also caught the Aswang.\n")
            print("         [ Strangle him ]")
            action = input()
            print("     The Aswang was strangled tightly. Juan deeply crushes its neck. \n")
            print("         [ Stab its chest with the bolo ]")
            action = input()
            print("     The Aswang fell to the ground. While bleeding, Guido begs Juan for his life.\n")
            print("         [ Cut his head off ]")
            action = input()
            print("     Juan cuts Guido's head off, saying that this is for his wife.")
            action = input(), loading()

            print("     Juan killed all the Aswangs. He quickly runs to Maria to untie her and dress her. She")
            print(" thanked Juan for his bravery. He promised his wife that it will never happen again.")
            action = input(), loading()
            print("  ╔══════════════════════════════════════════════════════════════════════════════════════╗")
            print("  ║     You WIN. You saved Maria. As what we have mentioned your choices affect what     ║")
            print("  ║        Juan would do. Remember to think about your actions before you do it...       ║")
            print("  ╚══════════════════════════════════════════════════════════════════════════════════════╝")
            action = input(), loading()

            print("     Juan saved Maria. But there are other evil creatures out there. Juan has now dedicated")
            print(" his life to kill Aswangs and other creatures. To prevent what happened to his wife to other")
            print(" people. Juan vowed to avenge all the victims by slaying all creatures which are deadly and")
            print(" will bring danger to other people. He goes to everywhere to search and kill creatures that")
            print(" has bad intentions to humans.")
            action = input()
            break
        else:
            print("\n     You are running out of time. You need to save Maria.\n")

    print("             Juan dela Cruz, now with his mission is now called the.", end=''), time.sleep(0.5)
    print(".", end=''), time.sleep(0.5), print(".", end=''), time.sleep(0.5), print(".",end=''), time.sleep(0.5)
    print(".\n"), time.sleep(0.5)

    print("                            P ", end=''), time.sleep(0.5), print("I ", end=''), time.sleep(0.5)
    print("N ", end=''), time.sleep(0.5), print("O ", end=''), time.sleep(0.5), print("Y     ", end=''), time.sleep(0.5)
    print("H ", end=''), time.sleep(0.5),print("U ", end=''), time.sleep(0.5),print("N ", end=''), time.sleep(0.5)
    print("T ", end=''), time.sleep(0.5),print("E ", end=''), time.sleep(0.5),print("R \n\n"), time.sleep(0.5)

    credits()
    print(" "), time.sleep(0.5), print(" "), time.sleep(0.5), print(" "), time.sleep(0.5)