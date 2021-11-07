d1= {'jack':38, 'john':33, 'michael':48, 'guido':57}
print({ k:('below_40' if v<40 else 'above_eq_40') for k,v in d1.items()})