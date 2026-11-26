schedule = {
    "Monday": ["Algorithms", "Calculus"],
    "Tuesday": ["English"],
    "Wednesday": ["Algorithms", "Physics", "Discrete Math"],
    "Thursday": ["Physics", "Calculus"],
    "Friday": ["Discrete Math"],
}

busiest_day = ""
max_courses = 0

for day, courses in schedule.items():
    if len(courses) > max_courses:
        busiest_day = day
        max_courses = len(courses)

print(f"Busiest day: {busiest_day} ({max_courses} courses)")


target_course = input()
day_count = 0

for courses in schedule.values():
    if target_course in courses:
        day_count += 1

print(f"{target_course}: {day_count} days")