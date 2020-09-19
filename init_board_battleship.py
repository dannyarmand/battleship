while turns > 0:
    if turn == 1:
            while loopx == False:
                    try:
                            move = raw_input("Do you want to attack or gegenerate health? Press 1 to ATTACK and 2 to REGEN. ")
                            print ""
                            move = int(move)
                            if move == 1:
                                    health1 = health1 - damage
                                    print "You attacked!"
                                    loopx = True                        # fix1
                            elif move == 2:
                                    health = health+regen
                                    print "You regenerated health!"
                                    loopx = True
                            else:
                                    print "Invalid number, try again"
                                    continue
                    except:
                                    print "Invalid number, try again"
                                    continue
            turn = 2                                                    # fix 2

    if turn == 2:
            AImove = r.randint(1,2)
            if AImove == 1:
                    print "AI attacked!"
                    health = health - damage1
            else:
                    print "AI regenerated!"
                    health1 = health1+regen1
            turn = 1                                                    # fix 3
            continue

print "game over!"