#French 9.21.22
list_scores = []
num_scores = 0
avg_scores = 0
counter = 0

print('How many test scores would you like to average?')
num_scores = int(input(''))
while counter < num_scores:
    list_scores.append(int(input('Enter test score: ')))
    counter += 1
avg_scores = sum(list_scores) / num_scores 
print('The average for the test scores you entered is:', avg_scores)
