from scipy import stats

female_doctor_bps = [128, 127, 118, 115, 144, 142, 133, 140, 132, 131,
                     111, 132, 149, 122, 139, 119, 136, 129, 126, 128]
r = stats.ttest_1samp(female_doctor_bps, 120)
print(r[1])
