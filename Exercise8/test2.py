

def step(x, y):
    l = list(range(1, 6))

    def index_generator():
        while True:
            yield 0
            yield -1

    index = index_generator()
    result = []
    while l:
        result.append(l.pop(next(index)))


def bouncing_ball(h, bounce, window):

    if h <= 0 or bounce <= 0 or bounce >= 1 or window >= h:

        return -1

    count = 1

    while h * bounce > window:

        h = h * bounce

        count += 2

    return count

print(bouncing_ball(3, 0.66, 1.5))

def rental_car(days):

    if days < 3:

        return days * 40

    elif days >= 3 and days < 7:

        return (days * 40) - 20

    else:

        return (days * 40) - 50
    
    def duplicate_count(text):

        return len([x for x in set(text) if text.count(x) > 1])
    
    def maskify(cc):
        return '#' * (len(cc) - 4) + cc[-4:]



def banana_count(string):
    count = 0
    x = string.find('banana')
    if x >= 0:
        count += 1
        return count + banana_count(string[x + len('banana'):])
    return count

string = 'banbababananbanbnabnba'
print(banana_count(string))











