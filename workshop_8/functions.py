"""
expceted number format:
\d+ (11111, 1212312312, 134571639847189342)
\d+. (1., 1231241., 123121666.)
\d+.\d+ (1.1, 1.111111, 1.765756765, 14321432124.324523452345)
.\d+ (.78878978978, .1, .32432334234)
- in front of all of the above
+ in front of all of the above
"""

text = "..1"

def is_correct_number(text):
    dot_found = False
    # if text[0] == "+" or text[0] == "-"
    parsed_number = text
    if text[0] in "-+":
        # string contains sign
        if len(text) == 1 or (len(text) == 2 and "." in text):
            return False
        parsed_number = text[1:]


    for ch in parsed_number: # ვიღებთ თითოეულ სიმბოლოს parsed_number -ში
        if ch == ".": # ვამოწმებთ სიბომოლო არის თუ არა "."
            if dot_found: # თუ უკვე ნაპოვნია აქამდე წერტილი 
                # we found second dot
                return False # დაბრუნდეს False ანუ არასწორი. რიცხვია!

            dot_found = True # მოვნიშნოთ რომ წერტილი ერთხელ მაინც ვიპოვეთ უკვე!
            continue # გადავიდეს შემდეგ იტერაციაზე (ანუ სიმბოლოზე)

        if not ch.isdigit(): # თუ სიმბოლო რიცხვი არ არის
            return False # არასწორი რიცხვია!

    return not (dot_found and len(text) == 1) # თუ წერტილი ნაპოვნია და 1 ცალი სიმბოლოსგან შედგება, არასწორი რიცხვია თუ არადა ყველაფერი სწორია!


text = "-17.9"
if is_correct_number(text):
    print(float(text))
else:
    print("Not correct")



"""
გვაქვს
"..7"

1. შევამოწმეთ ნიშანზე (+-) და ოქეია
2. ავიღეთ პირველი სიმბოლო (.) შემოწმდა წერტილი არის თუ არა და არის მოვნიშნოთ რომ ნაპოვნია
3. გადავედით შემდეგ სიმბოლოზე (.) შემოწმდა არის თუ არა წერტილი და არის, ასევე უკვე ნაპოვნია სხვა წერტილი, ამიტომაც მორჩა ფუნქცია!

"""