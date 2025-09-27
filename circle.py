M = int(input())


count1 = max(0, (M - 10) // 30 + 1) if M >= 10 else 0

count2 = max(0, (M - 30) // 30 + 1) if M >= 30 else 0

print(count1 + count2)