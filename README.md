📌 Description

This project is a simple animated simulation of a solar system, built with Python and the turtle graphics module.
Each planet orbits around the Sun using trigonometric functions (cos() and sin()) to compute circular motion.
- The project is built using a clean object-oriented architecture (OOP):
- A Soleil (Sun) class
- A Planete (Planet) class
- An animation loop that updates all objects in real time

This project is an excellent way to learn:
➡️ Animation with the Turtle module
➡️ Geometric transformations
➡️ Time-based object updates
➡️ Modular Python architecture

✨ How It Works
- The Sun remains fixed at the center of the screen.
- Each planet orbits around the Sun with:
- A specific orbital radius
- A unique rotation speed
- A distinct color
- A different initial angle

Smooth animation is achieved with:
 screen.tracer(0)
 screen.update()

🧱 Project Structure
📁 solar-system
│── main.py         # Animation loop
│── soleil.py       # Sun class
│── planete.py      # Planet class
│── README.md

🌞 Soleil (Sun) Class

📄 soleil.py

class Soleil(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('yellow')
        self.shapesize(10, 10)
        self.penup()

The Sun is simply a large yellow turtle positioned at the center.

🪐 Planete (Planet) Class

📄 planete.py

Each planet has:
- angle → its current angle around the Sun
- thespeed → its rotation speed
- rayon → orbital radius
- color → planet color

The orbital movement is computed using:
  x = rayon * cos(angle)
  y = rayon * sin(angle)

The angle increases continuously to simulate motion along the orbit.

🚀 Run the Project
1️⃣ Install Python 3
Make sure Python 3.10+ is installed on your system.

2️⃣ Run the project
python3 main.py


A Turtle graphics window will open and the planets will begin orbiting the Sun.
🧩 Sample Animation Loop
while True:
    time.sleep(0.02)
    screen.update()
    for planet in liste_planetes:
        planet.move()

🌟 Included Improvements
This README includes enhancements already integrated or recommended for future versions:
✔️ Clearer radius computation
  A fixed radius can be defined directly for each planet.
✔️ Smoother animation
  Using time.sleep(0.02) for natural movement.
✔️ Clean code separation
  Sun, Planet, and main animation loop are fully modular.
✔️ Optional “no-trail” mode
  Using penup() to avoid drawing orbital paths.
✔️ Support for satellites (moons)
  A future class Lune can orbit around a planet.

🗺️ Roadmap – Future Enhancements
 - Add a Moon class orbiting around a planet
 - Simplify and improve the radius management
 - Add Sun rotation animation
 - Add user controls (speed, toggle trails, etc.)
 - Add a starry background
 - Add zoom or camera effects
 - Add elliptical orbits
 - Add UI elements (buttons, keyboard shortcuts)

🧑‍💻 Skills Developed
- By building this project, you practice:
- Object-oriented programming (OOP)
- Real-time animation with Turtle
- Applied trigonometry (cosine & sine)
- Event-based graphics programming
- Modular Python architecture
- Simulation of physical systems

📝 Author
Developed by Francis SOP SOP, as part of a series of advanced Python Turtle graphics and animation exercises.
