def determine_winner(n, user_data):
    sorted_data = sorted(user_data, key=lambda x: x[0])
    
    total = 0
    for user in user_data:
        total += user[1]
    
    winner_index = total % n
    
    winner_username = sorted_data[winner_index][0]
    
    return winner_username


n = int(input())
user_data = []
for i in range(n):
    username, rating = input().split()
    user_data.append((username, int(rating)))
print(determine_winner(n, user_data))  
