import os

print("\n\n====================================================")
print("Welcome to the Assignment Template Creator")
print("====================================================\n\n")
print("This code features Git Automation and will allow you to create templates for your upcoming assignments.\n As a bonus, it also provides you to push the template directly to the repository (optional)")
print("====================================================\n\n")
print("Are you planning to work on :")
print("1.A Single Assignment")
print("2.Multiple Assignments")
print("3.Exit")
while True:
    choice = int(input("Enter your choice : "))
    if choice==1:
        # Initializing the folder and the subfolder
        parent_dir = os.path.dirname(os.path.abspath(__file__))
        while True:
            assignment_no = input("Enter the assignment no. you're working on: ").strip()
            if assignment_no:
                subfolder_name = f"Assignment{assignment_no}"
                break
            print("Assignment number cannot be empty! Try again.")
        subfolder_path = os.path.join(parent_dir, subfolder_name)

        # Create the subfolder
        os.makedirs(subfolder_path, exist_ok=True)

        # Create a new file within the subfolder
        for i in range(1,6):
            file_path = os.path.join(subfolder_path, f"Prog{i}.c")
            with open(file_path, 'w') as file:
                file.write(f"\\\\ {subfolder_name}\n\\\\ Prog {i}\n\\\\ Write your question here(in shortened form)\n\n\\\\ Write your code here\n")
            print(f"File 'Prog{i}.py' was created successfully at {subfolder_path}.")
        
        # Committing the boiler plate to git
        os.system(f'git add {subfolder_name}/')
        os.system(f'git commit -a -m "Adding template for {subfolder_name} in C directory')
        

    elif choice==2:
        m = int(input("Enter the lower range of the assignment no. (inclusive of it): "))
        m_start, n = m, int(input("Enter the upper range of the assignment no. (inclusive of it) : "))
        l = []
        while(m<=n):
            # Initializing the folder and the subfolder
            parent_dir = os.path.dirname(os.path.abspath(__file__))
            subfolder_name = f"Assignment{m}"
            l.append(f"{subfolder_name}/")
            subfolder_path = os.path.join(parent_dir, subfolder_name)

            # Create the subfolder
            os.makedirs(subfolder_path, exist_ok=True)

            # Create a new file within the subfolder
            for i in range(1,6):
                file_path = os.path.join(subfolder_path, f"Prog{i}.py")
                with open(file_path, 'w') as file:
                    file.write(f"\\\\ {subfolder_name}\n\\\\ Prog {i}\n\\\\ Write your question here(in shortened form)\n\n\\\\ Write your code here\n")
                print(f"File 'Prog{i}.py' was created successfully at {subfolder_path}.")
            
            m+=1
        os.system(f'git add {" ".join(l)}')
        os.system(f'git commit -a -m "Adding template for Assignment {m_start}-{n}" in the C diretory')

    elif choice==3:
        break

    else:
        print("Wrong Choice! Try Again!!")

print("Do you want to push the changes to the repository ?")  
choice = input("Enter 'y' for Yes: ").strip().lower()
if choice or choice[0] == 'y':
    os.system('git push origin main')
