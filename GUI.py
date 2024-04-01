import tkinter as tk
from tkinter import messagebox

class EducationalObjective:
    def __init__(self, name, domain, complexity_level, lessons=None):
        self.name = name
        self.domain = domain
        self.complexity_level = complexity_level
        self.children = []
        self.lessons = lessons if lessons is not None else []

    def add_sub_objective(self, sub_objective):
        self.children.append(sub_objective)

    def add_lesson(self, lesson):
        self.lessons.append(lesson)

    def find_objective(self, name):
        if self.name == name:
            return self
        for child in self.children:
            found = child.find_objective(name)
            if found:
                return found
        return None

    def __repr__(self):
        lessons_repr = ', '.join(self.lessons)
        return f"{self.name} ({self.domain}, Level {self.complexity_level}) - Lessons: {lessons_repr}"

class RewardSystem:
    def __init__(self):
        self.rewards = {
            "verbal_praise": ["Great job!", "Well done!", "You're amazing!"],
            "stickers": ["star", "smiley face", "heart"],
            "playtime": ["5 minutes extra screenstime", "10 minutes extra physical games", "15 minutes extra at Ninja U"]
        }

    def get_reward(self, reward_type):
        if reward_type in self.rewards:
            return self.rewards[reward_type]
        return []

    def display_rewards(self):
        print("Available Rewards:")
        for reward_type, reward_options in self.rewards.items():
            print(f"{reward_type.title()}:")
            for option in reward_options:
                print(f"  - {option}")

class WeeklySchedule:
    def __init__(self):
        self.schedule = {day: [] for day in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]}

    def add_activity(self, day, objective, activity):
        self.schedule[day].append((objective, activity))

    def get_activities_for_day(self, day):
        return self.schedule[day]

    def display_weekly_schedule(self):
        for day, activities in self.schedule.items():
            print(f"{day}:")
            for objective, activity in activities:
                print(f"  - {objective.name}: {activity}")
                for lesson in objective.lessons:
                    print(f"    - Lesson: {lesson}")
            print()

def build_educational_tree():
    root = EducationalObjective("Preschool Curriculum", "General", 0)
    cognitive = EducationalObjective("Cognitive Development", "Cognitive", 1)
    motor_skills = EducationalObjective("Motor Skills", "Physical", 1)
    language_literacy = EducationalObjective("Language and Literacy", "Cognitive", 1)
    mathematical_understanding = EducationalObjective("Mathematical Understanding", "Cognitive", 1)
    science_awareness = EducationalObjective("Science and Environmental Awareness", "Cognitive", 1)
    creative_arts = EducationalObjective("Creative Arts and Expression", "Cognitive", 1)
    social_emotional = EducationalObjective("Social and Emotional Development", "Cognitive", 1)


    language_literacy.add_sub_objective(EducationalObjective("Alphabet Recognition", "Cognitive", 2, ["Recognize letters", "Write letters"]))
    language_literacy.add_sub_objective(EducationalObjective("Phonics and Reading", "Cognitive", 2, ["Sound out letters", "Read simple words"]))
    mathematical_understanding.add_sub_objective(EducationalObjective("Basic Operations", "Cognitive", 2, ["Introduction to addition", "Introduction to subtraction"]))
    mathematical_understanding.add_sub_objective(EducationalObjective("Patterns and Sequences", "Cognitive", 2, ["Recognize patterns", "Create sequences"]))
    science_awareness.add_sub_objective(EducationalObjective("Weather and Seasons", "Cognitive", 2, ["Identify weather types", "Seasonal changes"]))
    creative_arts.add_sub_objective(EducationalObjective("Drawing and Painting", "Cognitive", 2, ["Use of colors", "Expressing ideas through art"]))
    social_emotional.add_sub_objective(EducationalObjective("Understanding Emotions", "Cognitive", 2, ["Recognize emotions", "Empathy towards friends"]))


    cognitive.add_sub_objective(EducationalObjective("Numbers and Counting", "Cognitive", 2, ["Count objects", "Number recognition"]))
    cognitive.add_sub_objective(EducationalObjective("Shapes and Colors", "Cognitive", 2, ["Identify shapes", "Color matching"]))
    motor_skills.add_sub_objective(EducationalObjective("Fine Motor Skills", "Physical", 2, ["Pincer grasp activities", "Using scissors"]))
    motor_skills.add_sub_objective(EducationalObjective("Gross Motor Skills", "Physical", 2, ["Jumping over obstacles", "Balancing"]))


    root.add_sub_objective(cognitive)
    root.add_sub_objective(motor_skills)
    root.add_sub_objective(language_literacy)
    root.add_sub_objective(mathematical_understanding)
    root.add_sub_objective(science_awareness)
    root.add_sub_objective(creative_arts)
    root.add_sub_objective(social_emotional)

    return root

def populate_schedule(schedule):
    schedule.add_activity("Monday", root.find_objective("Numbers and Counting"), "Count to 10 with blocks.")
    schedule.add_activity("Tuesday", root.find_objective("Shapes and Colors"), "Find and name circles around the room.")
    schedule.add_activity("Wednesday", root.find_objective("Physical Education"), "Jumping over obstacles or Balancing")
    schedule.add_activity("Thursday", root.find_objective("Fine Motor Skills"), "Pincer grasp activities (picking up loose change")
    schedule.add_activity("Friday", root.find_objective("Cognitive Development"),"Spend 20 mins reading a book together and 10 mins working on Phonics")
   # NEED TO POPULATE WITH CONTINUED DATA FOR CLASS STRUCTURE

def gui_display_activities_for_day():
    clear_activity_widgets()
    selected_day = day_var.get()
    activities = schedule.get_activities_for_day(selected_day)
    for i, (objective, activity) in enumerate(activities):
        frame = tk.Frame(activity_frame)
        frame.grid(row=i, column=0, sticky='w', pady=2)


        chk_var = tk.BooleanVar(value=False)
        chk = tk.Checkbutton(frame, variable=chk_var)
        chk.grid(row=0, column=0, sticky='w')
        checkboxes.append((chk, chk_var))


        label = tk.Label(frame, text=f"{objective.name}: {activity}")
        label.grid(row=0, column=1, sticky='w')


        chk_var.trace("w", lambda name, index, mode, var=chk_var, obj=objective: checkbox_callback(var, obj))

def checkbox_callback(var, objective):
    if var.get():
        reward_message = f"Well done! Here's a reward for completing '{objective.name}': {reward_system.get_reward('verbal_praise')[0]}"
        messagebox.showinfo("Reward", reward_message)
        # ADD MORE SOPHISTICATED REWARD LOGIC.

def clear_activity_widgets():
    for chk, var in checkboxes:
        chk.destroy()
    checkboxes.clear()


root = build_educational_tree()
schedule = WeeklySchedule()
populate_schedule(schedule)

app = tk.Tk()
app.title("Preschool Curriculum Planner")


app.minsize(800, 600)

reward_system = RewardSystem()


day_var = tk.StringVar(app)
day_var.set("Monday")
day_dropdown = tk.OptionMenu(app, day_var, *schedule.schedule.keys())
day_dropdown.pack()


activity_frame = tk.Frame(app)
activity_frame.pack(pady=(30, 75))

checkboxes = []

button_show_activities = tk.Button(app, text="Show Activities", command=gui_display_activities_for_day)
button_show_activities.pack(pady=(50, 75))

app.mainloop()
