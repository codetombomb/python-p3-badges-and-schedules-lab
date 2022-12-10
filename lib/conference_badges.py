def badge_maker(name):
    return f"Hello, my name is {name}."

def batch_badge_creator(names):
    return [badge_maker(name) for name in names] 

def assign_rooms(names):
    return [f"Hello, {name}! You'll be assigned to room {idx + 1}!" for idx, name in enumerate(names)]

def printer(names):
    for message in batch_badge_creator(names):
        print(message)
    for message in assign_rooms(names):
        print(message)
