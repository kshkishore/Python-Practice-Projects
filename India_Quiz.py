# Simple game in python

print('Hi, welcome to the India quiz!')
print('Try to answer as many questions correct as possible...')

totalQuestions = 5
score = 0

ans = input('1. What is the name of our country? ')

if ans == 'India':
    print('Correct!')
    score += 1
else:
    print('Incorrect')


ans = input('2. What is the capital of India? ')

if ans == "Delhi":
    print('Correct!')
    score += 1
else:
    print('Incorrect')


ans = input('3. What is the southern most point of India? ')

if ans == "Kanyakumari":
    print('Correct!')
    score += 1
else:
    print('Incorrect')


ans = input('4. What is the largest port in India? ')

if ans == "Kandla":
    print('Correct!')
    score += 1
else:
    print('Incorrect')


ans = input('5. What is the longest river in India? ')

if ans == "Ganga":
    print('Correct!')
    score += 1
else:
    print('Incorrect')


print("Thank you for playing, you got " + str(score) + ' questions correct!' )
percent = (score/totalQuestions) * 100
print("Score: " + str(int(percent)) + '%')

if percent >= 50:
    print('Great! You passed!')
else:
    print('Better luck next time')