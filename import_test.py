
def beg(target_function):
    print(1)
    def wrapper(*args, **kwargs):
        print(2)
        print('args====>', args)
        print('kwargs====>', kwargs)
        msg, say_please = target_function(*args, **kwargs)
        if say_please:
            return "{} {}".format(msg, "Please! I am poor :(")
        return msg
    print(3)
    return wrapper


@beg
def say(say_please=False):
    print(4)
    msg = "Can you buy me a beer?"
    return msg, say_please


# print(say())  # Can you buy me a beer?
print(say(say_please=True))  # Can you buy me a beer? Please! I am poor :(

# say(say_please=True) = beg(say(say_please=True))
# beg(say(say_please=True)) = wrapper(say_please=True)