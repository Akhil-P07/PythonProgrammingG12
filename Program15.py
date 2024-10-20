# Program to take 10 sample phishing mails
# and count the most commonly occurring word
phishingemail = [
    "jackpotwin@lottery.com",
    "claimtheprize@mymoney.com",
    "youarethewinner@lottery.com",
    "luckywinner@mymoney.com",
    "spinthewheel@flipkart.com",
    "dealwinner@snapdeal.com",
    "luckywinner@snapdeal.com",
    "luckyjackpot@americanlottery.com",
    "claimtheprize@lootolottery.com",
    "youarelucky@mymoney.com"
]

myd = {}
for e in phishingemail:
    x = e.split('@')
    for w in x:
        if w not in myd:
            myd[w] = 1
        else:
            myd[w] += 1

key_max = max(myd, key=myd.get)
print("Most Common Occurring word is:", key_max)
