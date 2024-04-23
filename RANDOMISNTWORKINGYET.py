import tkinter as tk
from tkinter import messagebox
import random

class EducationalObjective:
    def __init__(self, name, domain, complexity_level, lessons=None):
        self.name = name
        self.domain = domain
        self.complexity_level = complexity_level
        self.children = []
        self.lessons = lessons if lessons is not None else []

    def add_sub_objective(self, sub_objective):
        self.children.append(sub_objective)

    def find_objective(self, name):
        if self.name == name:
            return self
        for child in self.children:
            found = child.find_objective(name)
            if found:
                return found
        return None

class RewardSystem:
    def __init__(self):
        self.rewards = {
            "verbal_praise": ["Great job!", "Well done!", "You're amazing!"],
            "stickers": ["Spidey And Friends", "Dinosaurs", "Heart, Paw Patrol"],
            "playtime": ["5 minutes extra screentime", "10 minutes extra physical games", "15 minutes extra at Ninja U"],
            "special_time": ["Read an extra bedtime story", "Visit the local park or zoo", "Family movie night", "Bake cookies together"]
        }

    def get_reward(self, reward_type):
        return self.rewards.get(reward_type, [])

class WeeklySchedule:
    def __init__(self):
        self.schedule = {day: [] for day in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]}

    def add_activity(self, day, objective, activity):
        self.schedule[day].append((objective, activity))

    def clear_schedule(self):
        for day in self.schedule:
            self.schedule[day] = []

    def get_activities_for_day(self, day):
        return self.schedule.get(day, [])

class ActivityArchive:
    def __init__(self):
        self.archive = {}

    def record_activity(self, day, objective, activity, reward):
        if day not in self.archive:
            self.archive[day] = []
        self.archive[day].append({"objective": objective.name, "activity": activity, "reward": reward})

def build_educational_tree():
    root = EducationalObjective("Preschool Curriculum", "General", 0)
    cognitive = EducationalObjective("Cognitive Development", "Cognitive", 1)
    motor_skills = EducationalObjective("Motor Skills", "Physical", 1)
    language_literacy = EducationalObjective("Language and Literacy", "Cognitive", 2)
    mathematical_understanding = EducationalObjective("Numbers and Counting", "Cognitive", 2)
    science_awareness = EducationalObjective("Science and Environmental Awareness", "Cognitive", 3)
    creative_arts = EducationalObjective("Creative Arts and Expression", "Cognitive", 1)
    social_emotional = EducationalObjective("Social and Emotional Development", "Cognitive", 2)

    root.add_sub_objective(cognitive)
    root.add_sub_objective(motor_skills)
    root.add_sub_objective(language_literacy)
    root.add_sub_objective(mathematical_understanding)
    root.add_sub_objective(science_awareness)
    root.add_sub_objective(creative_arts)
    root.add_sub_objective(social_emotional)

    return root

def randomize_schedule(schedule, root):
    schedule.clear_schedule()
    activities = [
        ("Monday", "Numbers and Counting", "Count to 10 with blocks."),
        ("Tuesday", "Social and Emotional Development", "Identify emotions with flash cards"),
        ("Monday", "Creative Arts and Expression", "Find and name circles around the room."),
        ("Tuesday", "Creative Arts and Expression", "Get a small canvas and acrylic paints, put on Bob Ross and paint"),
        ("Wednesday", "Motor Skills", "Jumping over obstacles or Balancing"),
        ("Thursday", "Social and Emotional Development", "Watch an educational video on empathy and talk about different emotions"),
        ("Thursday", "Motor Skills", "Pincer grasp activities picking up loose change"),
        ("Friday", "Language and Literacy", "Head to the Local Library and find new books to read/contribute to StoryTime"),
        ("Friday", "Science and Environmental Awareness", "Take a trip to the Botanical gardens or help the neighbors in theirs"),
        ("Tuesday", "Motor Skills", "T-Ball practice in the backyard and 3 laps"),
        ("Monday", "Numbers and Counting", "Count 15 different objects around the house."),
        ("Wednesday", "Social and Emotional Development", "Volunteer at Retirement home"),
        ("Tuesday", "Creative Arts and Expression", "Sidewalk chalk if weather permits."),
        ("Thursday", "Creative Arts and Expression", "Paint fingernails or toenails"),
        ("Wednesday", "Motor Skills", "Soccer for 20 mins, dribbling/shooting"),
        ("Wednesday", "Social and Emotional Development",
         "Sing songs/hymns of deep spiritual connection"),
        ("Thursday", "Motor Skills", "Jumping stones balance game"),
        ("Monday", "Language and Literacy",
         "Practice Duolingo for 15 mins"),
        ("Friday", "Science and Environmental Awareness",
         "Use telescope or at home experiments for some fun"),
        ("Friday", "Motor Skills", "Basketball shooting and running drills")
    ]
    random.shuffle(activities)
    for day, obj_name, activity in activities:
        objective = root.find_objective(obj_name)
        if objective:
            schedule.add_activity(day, objective, activity)
        else:
            print(f"Objective named '{obj_name}' not found.")

def gui_display_activities_for_day():
    clear_activity_widgets()
    selected_day = day_var.get()
    activities = schedule.get_activities_for_day(selected_day)
    print(f"Activities for {selected_day}: {activities}")
    if not activities:
        print(f"No activities scheduled for {selected_day}.")
        return
    for i, (objective, activity) in enumerate(activities):
        frame = tk.Frame(activity_frame)
        frame.grid(row=i, column=0, sticky='w', pady=2)
        chk_var = tk.BooleanVar(value=False)
        chk = tk.Checkbutton(frame, text=f"{objective.name}: {activity}", variable=chk_var)
        chk_var.trace_add('write', lambda *args, var=chk_var, obj=objective: checkbox_callback(var, obj))
        chk.grid(row=0, column=1, sticky='w')
        checkboxes.append((chk, chk_var))

def checkbox_callback(var, objective):
    if var.get():
        complexity_to_reward = {
            1: 'verbal_praise',
            2: 'stickers',
            3: 'playtime',
            4: 'special_time'
        }
        reward_type = complexity_to_reward.get(objective.complexity_level, 'verbal_praise')
        reward_options = reward_system.get_reward(reward_type)
        if reward_options:  # Check if there are any rewards available
            reward_choice = random.choice(reward_options)
            archive.record_activity(day_var.get(), objective, "Activity completed", reward_choice)
            reward_message = f"Well done! Here's a reward for completing '{objective.name}': {reward_choice}"
            messagebox.showinfo("Reward", reward_message)  # This should show the pop-up
        else:
            print("No reward options found for the selected reward type.")  # Debug print statement


def clear_activity_widgets():
    for chk, var in checkboxes:
        chk.destroy()
    checkboxes.clear()

root = build_educational_tree()
schedule = WeeklySchedule()
archive = ActivityArchive()
reward_system = RewardSystem()

app = tk.Tk()
app.title("Preschool Curriculum Planner")
app.minsize(800, 600)
day_var = tk.StringVar(app)
day_var.set("Monday")
day_dropdown = tk.OptionMenu(app, day_var, *schedule.schedule.keys())
day_dropdown.pack()
activity_frame = tk.Frame(app)
activity_frame.pack(pady=(30, 75))
checkboxes = []
button_show_activities = tk.Button(app, text="Show Activities", command=gui_display_activities_for_day)
button_show_activities.pack(pady=(50, 75))
button_randomize_schedule = tk.Button(app, text="Randomize Schedule", command=lambda: randomize_schedule(schedule, root))
button_randomize_schedule.pack(pady=(10, 10))

randomize_schedule(schedule, root)

app.mainloop()
