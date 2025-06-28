# math_games.py
import matplotlib.pyplot as plt
import numpy as np
import random
from sympy import symbols, Eq, solve

# --- GAME 1: Scatter Plot Game ---
def scatter_plot_game():
    points = [(random.randint(1, 10), random.randint(1, 10)) for _ in range(5)]
    plt.figure(figsize=(6, 6))
    for x, y in points:
        plt.plot(x, y, 'ro')
    plt.title("Scatter Plot Game - Guess the Coordinates")
    plt.grid(True)
    plt.xlim(0, 12)
    plt.ylim(0, 12)
    plt.savefig("scatter_plot.png")
    plt.close()

    score = 0
    for idx, (x, y) in enumerate(points):
        guess = input(f"Enter coordinates of point #{idx + 1} (format: x y): ").split()
        if len(guess) == 2 and int(guess[0]) == x and int(guess[1]) == y:
            print("✅ Correct!")
            score += 1
        else:
            print(f"❌ Incorrect. The correct answer was ({x}, {y})")
    print(f"\nYour final score: {score}/{len(points)}")

# --- GAME 2: Algebra Practice Game ---
def algebra_game():
    def one_step():
        x = random.randint(1, 10)
        a = random.randint(1, 10)
        result = a * x
        print(f"\nSolve: {a}x = {result}")
        ans = float(input("x = "))
        return 1 if ans == x else 0

    def two_step():
        x = random.randint(-10, 10)
        a = random.randint(1, 5)
        b = random.randint(-10, 10)
        result = a * x + b
        print(f"\nSolve: {a}x + {b} = {result}")
        ans = float(input("x = "))
        return 1 if ans == x else 0

    score = 0
    for _ in range(3):
        score += one_step()
    for _ in range(2):
        score += two_step()
    print(f"\nAlgebra Game Score: {score}/5")

# --- GAME 3: Projectile Game (Hard mode) ---
def projectile_game():
    wall_x = random.uniform(3, 7)
    wall_h = random.uniform(4, 8)
    print(f"\nWALL at x = {wall_x:.2f}, height = {wall_h:.2f}")

    a = float(input("Enter coefficient a: "))
    b = float(input("Enter coefficient b: "))
    c = float(input("Enter coefficient c: "))

    x = np.linspace(0, 10, 400)
    y = a * x**2 + b * x + c

    plt.figure(figsize=(8, 6))
    plt.plot(x, y, label=f"y = {a}x² + {b}x + {c}")
    plt.axvline(x=wall_x, color='red', linestyle='--')
    plt.axhline(y=wall_h, color='red', linestyle='--')
    plt.fill_between([wall_x-0.1, wall_x+0.1], 0, wall_h, color='red', alpha=0.5, label="Wall")
    plt.title("Projectile Game")
    plt.grid(True)
    plt.legend()
    plt.savefig("projectile_plot.png")
    plt.close()
    print("Graph saved as 'projectile_plot.png'. Did you clear the wall?")

# --- MAIN MENU ---
def main():
    print("🎮 Math Games Menu 🎮")
    print("1. Scatter Plot Game")
    print("2. Algebra Game")
    print("3. Projectile Game")
    choice = input("Choose a game (1/2/3): ")

    if choice == '1':
        scatter_plot_game()
    elif choice == '2':
        algebra_game()
    elif choice == '3':
        projectile_game()
    else:
        print("Invalid choice. Bye!")

if __name__ == "__main__":
    main()
