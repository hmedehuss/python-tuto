is_male = True
is_tall = False

if is_male and is_tall:
    print("male and tall")
elif is_male and not (is_tall):
    print("male and short")
elif not(is_male) and is_tall:
    print("not male and tall")
else:
    print("not maleand short")