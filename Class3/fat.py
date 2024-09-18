def fatorial(num):
    ans = num
    if(num == 1 or num == 0):
        return 1
    else:
        return ans * fatorial(num-1)
    

def print_hello():
    print("Hello World!")

def count_vogal(word):
    return len(word)

def count_vogal2(word):
    count = 0
    for item in  word:
        count = count + 1
    return count



    


