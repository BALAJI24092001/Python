import pandas as pd
import scipy.stats as stats
data = pd.read_csv("./book_reviews.csv")

def bootstrap_ttest(data: pd.Series, frac = 0.1, boos = 50) -> list:
    print("BOOTSTRAPING T TEST".center(55))
    print("-"*55, "\n")
    pop_mean = data.mean()
    lst_t = list()
    lst_p = list()
    lst_r = list()
    lst_sm = list()
    lst_sd = list()
    print("No. of BootStraps : ", boos)
    print("Population size   : ", data.count())
    print("Population Mean   : ", round(pop_mean, 5))
    print("Sample Fraction   : ", int(frac*100), "%")
    print("Sample size       : ", int(data.count()*frac))
    print()
    
    for i in range(boos):
        sam = data.sample(frac=frac)
        t_stat, p_val = stats.ttest_1samp(sam, popmean=pop_mean)
        lst_sm.append(sam.mean())
        lst_sd.append(sam.std())
        lst_t.append(t_stat)
        lst_p.append(p_val)
    print("\033[1m","Sam Mean".rjust(10), "Sam Std".rjust(9), "T Val".rjust(9), "   " ,"P Value".rjust(8), "Result".rjust(9), "\033[0m")
    for i in range(boos):
        result = "Fail" if lst_p[i] <= 0.05 else "Pass"
        lst_r.append(result)
        print(str( f"{lst_sm[i]:3.4f}").rjust(10), str(f"{lst_sd[i]:3.4f}").rjust(10), str(f"{lst_t[i]:3.4f}").rjust(10), "   ", str(f"{lst_p[i]:3.4f}").rjust(6), f"{result}".rjust(8))
    print("\n", "\033[1m", "Result counts", "\033[0m")
    print(pd.value_counts(lst_r))
    return([list(lst_t), list(lst_p), list(lst_r)])

t_vals, p_vals, r_vals = bootstrap_ttest(data.price, frac=0.01, boos=50)
