def hot_cold(emotion):

# count how many love between calm and passion
    cnt = 0
    for i in range(len(emotion)):
        if emotion[i] == 'calm':
            for i in range(i, len(emotion)):
                if emotion[i] == 'love':
                    cnt = cnt+1
                elif emotion[i] == 'passion':
                    break
            return cnt
        elif emotion[i] == 'passion':
            for i in range(i, len(emotion)):
                if emotion[i] == 'love':
                    cnt = cnt+1
                elif emotion[i] == 'calm':
                    break
            return cnt  

print(hot_cold(['calm', 'love', 'love', 'love', 'passion', 'love', 'love']))
print(hot_cold(['passion', 'love', 'love', 'love', 'calm', 'love', 'love']))
