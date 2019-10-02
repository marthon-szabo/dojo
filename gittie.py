import time


def introduce():
    print("Hello, I'm Marci!")

    print("Heya, friend! I'm Gittie!")



def joke():
    print('Why did the chicken cross the road?')
    time.sleep(1)
    print("...")
    time.sleep(1)
    print('To get to the other side.')


def shout(something):
    print(something.upper())

shout("hello, hello, hello!")
introduce()
joke()
introduce()

def add(a,b):
    return a + b

add(2,3)

