def go(direction):
    return "You walk %s" % direction


def look(target):
    return "You see a %s" % target


def take(target):
    return "You shove the %s in your pocket" % target


def quit(noun):
    return "game over"


def unrecognized(noun):
    return "I don't know to %s" % noun

actions = {"go": go, "look": look, "take": take, "quit": quit}

translate = {"walk": "go", "run": "go", "grab": "take"}
over = False
while not over:
    command = input(">>>")
    words = command.lower().split()
    verb = words[0]
    noun = " ".join(words[1:])  # allows for multiple words to be passed into noun
    verb = translate.get(verb, verb)
    result = actions.get(verb, unrecognized)(noun)  # if verb not in actions, returns unrecognized(noun)
    print(result)
    if "game over" in result:
        over = True




