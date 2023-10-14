# ----------------- PCPP :  Certified Professional in Python Programming ----
# pylint: skip-file

#   --------------------------- ADVANCED TECHNIQUES  -----------------------------


#   --------------------------- UnicodeError -----------------------------
try:
    b"\x80".decode("utf-8")
except UnicodeError as e:
    print(e)  # 'utf-8' codec can't decode byte 0x80 in position 0: invalid start byte
    print(e.encoding)  # utf-8
    print(e.reason)  # invalid start byte
    print(e.object)  # b'\x80'
    print(e.start)  # 0
    print(e.end)  # 1


# ------------------------------------  chained exception  -----------------------------
# the __context__ attribute, for implicitly chained exceptions; -
#   implicite : qui est levée alors que le traitement d'une exception précédente était en cours
# the __cause__ attribute,  for explicitly chained exceptions.
#   explicite : translating an exception for unifying behavior of exception handling

# ------------------------------------  exception implicite  -----------------------------
a_list = ["First error", "Second error"]

try:
    print(a_list[3])
except Exception as e:
    try:
        # the following line is a developer mistake - they wanted to print progress as 1/10 but wrote 1/0
        print(1 / 0)
    except ZeroDivisionError as f:
        print("Inner exception (f):", f)
        print("Outer exception (e):", e)
        print("Outer exception referenced:", f.__context__)
        print("Is it the same object:", f.__context__ is e) # True


# ------------------------------------  exception explicite  -----------------------------
class RocketNotReadyError(Exception):
    pass


def personnel_check():
    try:
        print("\tThe captain's name is", crew[0])
        print("\tThe pilot's name is", crew[1])
        print("\tThe mechanic's name is", crew[2])
        print("\tThe navigator's name is", crew[3])
    except IndexError as e:
        raise RocketNotReadyError("Crew is incomplete") from e


def fuel_check():
    try:
        print("Fuel tank is full in {}%".format(100 / 0))
    except ZeroDivisionError as e:
        raise RocketNotReadyError("Problem with fuel gauge") from e


crew = ["John", "Mary", "Mike"]
fuel = 100
check_list = [personnel_check, fuel_check]

print("Final check procedure")

for check in check_list:
    try:
        check()
    except RocketNotReadyError as f:
        print('RocketNotReady exception: "{}", caused by "{}"'.format(f, f.__cause__))


# ------------------------------------  traceback  -----------------------------
import traceback

try:
    x = 100 / 0

except Exception as f:
    print(f.__traceback__)  #   <traceback object at 0x7f3b06928b40>
    print(type(f.__traceback__))  # <class 'traceback'>

    details = traceback.format_tb(f.__traceback__)
    print("".join(details))


# ------------------------------------  fin  -----------------------------
