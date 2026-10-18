nu = [1,2,3,4,5,6]

for i in range(len(nu)):
    if nu[i] == 6:
        break
    elif nu[i] > nu[i+1]:
        print(nu[i])
        
        