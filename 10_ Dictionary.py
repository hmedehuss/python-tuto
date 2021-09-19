monthconversion = {
    "Jan":"January",
    "Feb": "February",
    3:"March"
}

print(monthconversion.get("Jan", "Not a valid Key"))

print(monthconversion.get("Mar", "Not a valid Key"))


print(monthconversion.get(3, "Not a valid Key"))