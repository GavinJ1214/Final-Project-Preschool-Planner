class EducationalObjective:
    def __init__(self, name, domain, complexity_level):
        self.name = name
        self.domain = domain
        self.complexity_level = complexity_level
        self.children = []  # Sub-objectives

    def add_sub_objective(self, sub_objective):
        self.children.append(sub_objective)

    def find_objective(self, name):
        # Depth-first search
        if self.name == name:
            return self
        for child in self.children:
            found = child.find_objective(name)
            if found:
                return found
        return None

    def __repr__(self):
        return f"{self.name} ({self.domain}, Level {self.complexity_level})"


def build_educational_tree():
    root = EducationalObjective("Preschool Curriculum", "General", 0)

    # Sample domains
    cognitive = EducationalObjective("Cognitive Development", "Cognitive", 1)
    motor_skills = EducationalObjective("Motor Skills", "Physical", 1)

    # Adding sub-objectives
    cognitive.add_sub_objective(EducationalObjective("Numbers and Counting", "Cognitive", 2))
    cognitive.add_sub_objective(EducationalObjective("Shapes and Colors", "Cognitive", 2))

    motor_skills.add_sub_objective(EducationalObjective("Fine Motor Skills", "Physical", 2))
    motor_skills.add_sub_objective(EducationalObjective("Gross Motor Skills", "Physical", 2))

    # Add domains to root
    root.add_sub_objective(cognitive)
    root.add_sub_objective(motor_skills)

    return root


def print_tree(node, level=0):
    print(' ' * level * 2 + str(node))
    for child in node.children:
        print_tree(child, level + 1)


root = build_educational_tree()
print_tree(root)

# Example search
objective_name = "Shapes and Colors"
found_objective = root.find_objective(objective_name)
if found_objective:
    print(f"\nFound objective: {found_objective}")
else:
    print("\nObjective not found.")