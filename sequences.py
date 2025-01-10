def sort_by_age(people):
    def get_age(person):
        return person[1]
    sorted_list = sorted(people, key=get_age)
    return sorted_list

people = [("Samwuel", 21), ("Andrew", 11), ("Wayne", 34)]

print(sort_by_age(people))
