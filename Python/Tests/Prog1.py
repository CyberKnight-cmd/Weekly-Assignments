def count(n:str) -> int:
    for character in n:
        count += 1


words = list(input().split())
max, i = 0, ""
for index, word in enumerate(words):
    if(len(word)>max):
        max = len(word)
        i = words[index]
print(i, " : ", max)        

# max=0
# for ele in words:
#     if(len(ele)>max):
#         max=len(ele)
    
        
# print(max)
# print(words)