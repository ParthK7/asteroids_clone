# 🪐 Asteroids Clone – Python + Pygame

A faithful recreation of the classic **Asteroids** arcade game, built using **Python** and **Pygame** with a focus on clean **Object-Oriented Programming (OOP)** design.

In this game, you control a spaceship that can rotate, thrust, and shoot. When a large asteroid is shot, it splits into two medium asteroids; medium asteroids split into two small ones, and small asteroids disappear when shot. The game loop is driven by delta time to ensure smooth performance.

## 🚀 Features

- 🚢 Player spaceship with smooth rotation, thrust, and shooting mechanics
- 🪨 Asteroids break into progressively smaller pieces (Large → Medium → Small → Destroyed)
- 💥 Collision detection between bullets and asteroids
- 🔄 Delta time-based loop for consistent gameplay across devices
- 🧱 Modular OOP design with classes like `Player`, `Asteroid`, `Shot`, and `CircleShape`

## 🧰 Technologies Used

- **Python 3**
- **Pygame 2**
- Object-Oriented Programming (OOP)

## 🛠️ Installation & Running

1. Clone the repository:

   ```bash
   git clone <repo-link>
   cd asteroids_clone

2. Create a virtual environment(recommended)

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate

3. Install dependencies
   ```bash
   pip install pygame

5. Run the game
  ```bash
  python3 main.py
  ```

## 🧠 OOP Design Overview

- **Inheritance**: All game entities like asteroids and the player inherit from a common `CircleShape` base class for shared behavior.
- **Encapsulation**: Each game object manages its own state and behavior.
- **Modularity**: Easily extendable and maintainable due to well-separated concerns and class-based architecture.

## 🎮 Controls

- **WASD**: Move and rotate the spaceship  
- **Spacebar**: Shoot  
- **ESC**: Exit game  

