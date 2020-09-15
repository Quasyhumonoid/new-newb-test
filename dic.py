
monthConversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December",
} # also works with other values

print(monthConversions["Jan"])
print(monthConversions.get("Jul"))
print(monthConversions.get("dov", "not a valid key"))

