# Name: Fajri Ramadhan
# NIM: 2611533006
# Question 6

full_name = "  Fajri Ramadhan  "
nim = "2611533006"
clean_name = full_name.strip()
space_index = clean_name.find(" ")
if space_index != -1:
    first_name = clean_name[:space_index].lower()
else:
    first_name = clean_name.lower()
last_three = nim[-3:]
username = first_name + last_three
print(username) 