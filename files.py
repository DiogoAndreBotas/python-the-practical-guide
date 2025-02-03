with open('demo.txt', mode='w') as file_w:
    file_w.write('Hello from Python!')

with open('demo.txt', mode='a') as file_a:
    file_a.write('\nAnd from Portugal!')

with open('demo.txt') as file_r:
    print(file_r.read())
