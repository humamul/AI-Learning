name = "Humam Ul Islam"
experience = 2
skills = ["java","python","sql", "django"]

print(f"Name: {name}")
def funA(skill_list):
    for skill in skill_list:
        if(len(skill)>5): print(f"Big Skill: {skill}")
        else : print(f"Small List: {skill}")

funA(skills)
bigSkill_list = [skill for skill in skills if len(skill)> 5];
print(bigSkill_list);

firm_profile = {
    "name": "Digital Engravers",
    "GST": "ajrpi1992l",
    "city": "moradabad",
    "is_active": True
}
print(f"Firm Name: {firm_profile["name"]}")
def check(firm_dict):
    if firm_dict["is_active"] : print(firm_dict["name"])
    else: print(f"{firm_dict["name"]} doesn't Exist");

check(firm_profile)