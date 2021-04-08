'''
Write a program with 3 functions. Each function must call
at least one other function and use the return value to do something.

'''
import datetime

contacts = {
    "Joe Schmoe":{
        "number":2436791946,
        "email":"joe@schmoe.com",
        "last inbound":datetime.datetime(2020,12,15,14,2),
        "last outbound":datetime.datetime(2020,12,19,9,15)},
    "Jane Schmane":{
        "number":3867196092,
        "email":"janee@schmane.com",
        "last inbound":datetime.datetime(2021,2,1,18,53),
        "last outbound":datetime.datetime(2021,2,21,20,1)},
    "Kim Li":{
        "number":4589230534,
        "email":"kim@li.com",
        "last inbound":datetime.datetime(2021,3,20,16,36),
        "last outbound":datetime.datetime(2021,2,4,17,47)},
    "Robin Lin":{
        "number":6973934560,
        "email":"robin@lin.com",
        "last inbound":datetime.datetime(2021,4,7,10,21),
        "last outbound":datetime.datetime(2020,12,29,13,8)}
}

to_do = {
    1000: {
        "task":"Get Groceries",
        "done":True,
        "due":datetime.datetime(2021,4,1),
        "contact":None
    },
    1001: {
        "task":"Clean stove",
        "done":False,
        "due":datetime.datetime(2021,4,8),
        "contact":None
    }
}

# Potential functions
## contacts + all tasks --> new all tasks
## all tasks -(call contact+tasks above)-> today's tasks
## today's tasks (from above) --> new all tasks + new contacts

def update_tasks(contacts: dict,to_do: dict) -> dict:
    """Check contacts for unresponded and add to to_do

    Take contacts and to_do
    Return updated to_do
    """
    
    # Create a list of contact-linked to-dos that are open
    to_do_checker = []
    for task in to_do.values():
        if task["contact"] != None and task["done"] == False:
            to_do_checker.append(task["contact"])
    # Get the current highest task ID
    id_list = list(to_do.keys())
    id_list.sort()
    top_id = id_list[-1]
    
    for contact, info in contacts.items():
        # Check if the user has contacted the contact since last received message
        unresponded = info["last inbound"] > info["last outbound"]
        # Check the contact against list of open to-dos and add a new task if none exists
        # Futre feature: update a matching entry to have a sooner due date if needed
        if unresponded == True and contact not in to_do_checker:
            top_id += 1
            to_do[top_id] = {
                "task":f"Contact {contact}",
                "done":False,
                "due":info["last inbound"]+datetime.timedelta(days=2),
                "contact":contact
            }
    #print(to_do) #remove after debugging
    return to_do
            
def get_todays_tasks(new_to_do=to_do) -> dict:
    """Returns tasks overdue or due today as a dictionary
    
    Optionally takes a to-do list; otherwise defaults to global to_do
    """

    # Get today's date
    today = datetime.datetime.now().date()
    # Get updated tasks
    all_tasks = update_tasks(contacts,new_to_do)
    # Filter for overdue and due today
    todays_tasks = dict()
    for id,task in all_tasks.items():
        if task["due"].date() <= today and task["done"] == False:
            todays_tasks[id] = task
    # Return filtered list
    #print(todays_tasks) #remove after debugging
    return todays_tasks

def do_tasks(new_tasks=to_do) -> dict:
    """Runs user through tasks due today

    Call today's tasks and iterate through them
    Return updated task list
    """

    # Get tasks due today and full task list (note is not efficient; would just roll into getting today's tasks)
    todays_tasks = get_todays_tasks(new_tasks)
    global contacts
    all_tasks = update_tasks(contacts,new_tasks)
    if len(todays_tasks) == 0:
        print("Nothing due today!")
        return all_tasks

    # For each task, ask user if done and update today's tasks accordingly
    for id,task in todays_tasks.items():
        user_answer = input(f"Did you {task['task']}? Y/N ").upper()
        while user_answer != "Y" and user_answer != "N":
            print("Please enter 'Y' or 'N'.")
            user_answer = input(f"Did you {task['task']}? Y/N ").upper()
        if user_answer == "Y":
            task["done"] = True
            # Update last outbound time in contacts if task is linked to a contact
            if task["contact"] != None:
                contacts[task["contact"]]["last outbound"] = datetime.datetime.now()
    
    # Update full task list (could just combine with above; left this way for flexibility and readability)
    for id,task in todays_tasks.items():
        all_tasks[id] = task
    
    # Return full task list
    return all_tasks

def user_command():
    user_do_tasks = input("Get things done? Y/N ").upper()
    while user_do_tasks != "Y" and user_do_tasks != "N":
        print("Please enter 'Y' or 'N'.")
        user_do_tasks = input("Get things done? Y/N ").upper()
    return user_do_tasks

user_do_tasks = user_command()
while user_do_tasks == "Y":
    to_do = do_tasks(to_do)
    user_do_tasks = user_command()
    