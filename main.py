import os
import visualization as vis
from menu import show_menu


while True:
    os.system('cls')
    show_menu()
    choice = input("Enter your choice (1-7): ")
    if choice == "1":
        vis.plot_age_distribution()
    elif choice == "2":
        vis.plot_bmi_distribution()
    elif choice == "3":
        vis.plot_sleep_distribution()
    elif choice == "4":
        vis.plot_heatmap()
    elif choice == "5":
        vis.plot_bmi_by_gender()
    elif choice == "6":
        vis.plot_steps_vs_bmi()
    elif choice == "7":
       vis.plot_pairplot()
    elif choice == "8":
        vis.plot_facetgrid_steps_vs_bmi()
    elif choice == "9":
        vis.plot_bmi_vs_age()
    elif choice == "10":
        vis.plot_alcohol_vs_heart_rate()
    elif choice == "11":
        vis.plot_exercise_by_smoker()
    elif choice == "12":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")
