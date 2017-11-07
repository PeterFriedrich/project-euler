count = 0
num = 2836960

for i in range(1,21):
        if num % i == 0:
            count += 1
            print(count)
        else:
            count = 0
            break

for i in range(1,21):
    print(i)
