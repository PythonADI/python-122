import string
import random

georgian_letters = "აბგდევზთიკლმნოპჟრსტუფქღყშჩჯძჭ"
def generate_random_word(letters, k):
    return "".join(random.choices(letters, k=k))

def generate_random__list_of_objects(n, generate_object, *args, **kwargs):
    list_ = []
    for _ in range(n):
        list_.append(generate_object(*args, **kwargs))
    return list_


words = generate_random__list_of_objects(
    10,
    generate_random_word,
    string.ascii_letters,
    k=random.randint(5, 10)
)

print(words)


# numbers = generate_random__list_of_objects(
#     10,
#     random.randint,
#     -100,
#     100
# )

# print(numbers)



# strings = []
# for _ in range(10):
#     strings.append(generate_random_word(string.ascii_letters, random.randint(5, 10)))
#     strings.append(generate_random_word(georgian_letters, 10))


# print(strings)