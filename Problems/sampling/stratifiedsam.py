import numpy as np
ap = [round(i) for i in np.random.normal(150, 20, 10)]
kl = [round(i) for i in np.random.normal(180, 25, 15)]
tn = [round(i) for i in np.random.normal(120, 18, 8)]
ot = [round(i) for i in np.random.normal(130, 30, 6)]

print("ap : ", ap)
print("kl : ", kl)
print("tn : ", tn)
print("ot : ", ot)

ap =  [112, 184, 130, 168, 145, 161, 142, 160, 124, 134]
kl =  [173, 204, 176, 199, 118, 149, 187, 164, 161, 200, 168, 184, 161, 189, 116]
tn =  [126, 129, 103, 95, 139, 89, 132, 148]
ot =  [132, 143, 107, 141, 158, 152]

std_ap = np.std(ap)
std_kl = np.std(kl)
std_tn = np.std(tn)
std_ot = np.std(ot)

print(std_ap, std_kl, std_tn, std_ot)
