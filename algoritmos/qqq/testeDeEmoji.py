def num(num):
    emojis = {'0':'0️⃣','1':'1️⃣','2':'2️⃣','3':'3️⃣','4':'4️⃣','5':'5️⃣','6':'6️⃣','7':'7️⃣','8':'8️⃣','9':'9️⃣'}
    num = str(num)
    emoji_num = []
    for i in num:
        emoji_num.append(emojis[i])
    return ' '.join(emoji_num)

print(f"Número {num(1)}")