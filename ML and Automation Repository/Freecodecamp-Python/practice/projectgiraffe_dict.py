#dictionaries come with key-value pairs
month_concersions = {
    "Jan" : "January",
    "Feb" : "Feburay",
    "Mar" : "March",
    "Apr": "April",
    "Dec" : "December",
    0 : "January",
    8: "August"
    }

print(month_concersions.get("crazy", "Not valid yo"))
print(month_concersions.get("Jan", "Not valid yo"))
print(month_concersions.get(8, "Not valid yo"))  