import string, random, sys

all_char, size_pass = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!\"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~", random.randint(20, 35)
def get_rand_pass(size) -> str:
    rand_pass = "".join(random.choices(all_char, k=size))
    return rand_pass

def is_num(string_num) -> bool:
    try: int(string_num); return True
    except ValueError: return False
    
def index_in_list(a_list, index): return index < len(a_list)

if index_in_list(sys.argv, 1):
    if is_num(sys.argv[1]):
        if int(sys.argv[1]) <= 0:
            sys.argv[1] = "1"
        for _ in range(int(sys.argv[1])):
            size_pass = random.randint(20, 35)
            print(f"Password Generator: {get_rand_pass(size_pass)}")
else:
    print(f"Password Generator: {get_rand_pass(size_pass)}")
