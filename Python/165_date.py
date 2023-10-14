# pylint: disable=C0103, C0114, C0116,C0115, R0903, C0304
from datetime import date
import calendar
import time
from babel import dates

# ------ diff entre 2 jours
d0 = date(2014, 7, 2)
d1 = date(2018, 7, 11)
delta = d1 - d0
print(delta.days)

# ---------- année bisextime : 2 solutions
print(calendar.isleap(1900))


def is_leap_year(year):
    """Determine whether a year is a leap year."""
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


# -- ===== Mesure de performance

start = time.perf_counter()
finish = time.perf_counter()
print(f"Finished in {round(finish-start, 2)} second(s)")

# -- ========== babel pour les dates
d = date(2018, 15, 5)

x = dates.format_date(d, "e", locale="en_GB")
jour = dates.get_day_names("wide", locale="en_US")[1]

# --------- sleep
print("Printed immediately.")
time.sleep(2.4)
print("Printed after 2.4 seconds.")

#  --------- perf time
a = time.time()
_ = [i * 2 for i in range(9999999)]
print(f"Temps d'exécution: {time.time() - a}s")
