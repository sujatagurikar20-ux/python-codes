
runs_scored = int(input("Enter runs scored: "))
balls_faced = int(input("Enter balls faced: "))
ob = int(input("Enter overs bowled: "))
rc = int(input("Enter runs conceded: "))
wt = int(input("Enter wickets taken: "))
ct = int(input("Enter catches taken: "))

bsr = (runs_scored / balls_faced) * 100
er = rc / ob

print("Batting strike rate", bsr)
print("Economy rate", er)

if runs_scored >= 50 and bsr >= 120:
    batter = "Excellent"
    print("Excellent batter")
elif runs_scored >= 30 and bsr >= 100:
    batter = "Good"
    print("Good batter")
elif runs_scored >= 20:
    batter = "Average"
    print("Average batter")
else:
    batter = "Poor"
    print("Poor batter")

if wt >= 3 and er <= 6:
    bowler = "Excellent"
    print("Excellent bowler")
elif wt >= 2 and er <= 8:
    bowler = "Good"
    print("Good bowler")
elif wt >= 1:
    bowler = "Average"
    print("Average bowler")
else:
    bowler = "Poor"
    print("Poor bowler")


if ct >= 2:
    print("Outstanding fielder")
elif ct == 1:
    print("Active fielder")
else:
    print("Needs improvement")


if batter == "Excellent" and bowler == "Excellent":
    print("Star all-rounder")
elif batter == "Good" and bowler == "Good":
    print("Strong all-rounder")
elif batter == "Good" or bowler == "Good":
    print("Supporting all-rounder")
else:
    print("Needs improvement")
