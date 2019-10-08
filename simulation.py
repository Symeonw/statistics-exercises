import numpy as np
import random
import pandas as pd

out = np.random.randint(1,7,(10_000,2))
(out[:,0]==out[:, 1]).mean() #check if all from first column == all from second column

flip = 10_000
coins = 8
out_coin = np.random.choice([True, False], (flip,coins))
out_1 =  (out_coin.sum(axis=1) == 3).astype(int).mean()
out_2 = (out_coin.sum(axis=1) > 3).astype(int).mean()

times = 10_000
boards = 2
out_face = np.random.choice([True, False, False],(times, boards))
out_3 = (out_face.sum(axis=1) == 2).astype(int).mean()
out_3

#options = ["Web Dev"] * 3 + ["Data Science"]
#out_17 = ((np.random.choice(options, (10_000,2)) == "Data Science").sum(axis=1)==2).mean()
#out_17



men_mean = 178
f_mean = 170
men_std = 8
f_std = 6
out_height_men = list(np.random.normal(men_mean, men_std,(times)))
out_height_f = list(np.random.normal(f_mean, f_std, (times)))
df = pd.DataFrame({"M" : out_height_men, "F" : out_height_f})
df.reset_index
df["F_Tall"] = df.M < df.F
out_final = df.F_Tall.mean()
out_final
#n = 10_000
#male_heights = np.random.normal(178,8,n)
#female_heights = np.random.normal(170, 6, n)
#(female_heights > male_heights).mkiol,an()

stu = 50
chance = 1/250
out_stu = ((np.random.random((10_000,stu)) < chance).sum(axis=1) > 0).mean()
out_stu

downloads = np.random.choice(["Completed", "Failed"], (10_000, 450), p=[249/250, 1/250])
(downloads == "Failed").all(axis=1).mean()


n = 10_000
p_food = .7
p_no_food = 1 - p_food
out_food = np.random.choice(["Food", "No food"], (n,3), p=[p_food, p_no_food])
(out_food == "No food").all(axis=1).mean()

birthdays = np.random.choice(range(365), (10_000, 23))
unq_birth = np.array([np.unique(row).size for row in birthdays])
(unq_birth < 23).mean()



