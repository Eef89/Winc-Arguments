# Do not modify these lines
__winc_id__ = '7b9401ad7f544be2a23321292dd61cb6'
__human_name__ = 'arguments'

# Add your code after this line

# Part 1 Greet template

    
def greet(name, greeting = "Hello, <name>!"):
    final_greeting = greeting.replace('<name>', name)
    print (final_greeting)
    return (final_greeting)

# Part 2 Force


def force(mass, body = 'earth'):
    planets = {
    "sun": 274,
    "jupiter": 24.92,
    "neptune": 11.15,
    "saturn": 10.44,
    "earth": 9.798,
    "uranus": 8.87,
    "venus": 8.87,
    "mars": 3.71,
    "mercury": 3.7,
    "moon": 1.62,
    "pluto": 0.58
    }
    gravity = round(planets[body], 1)
    force = (mass * gravity)
    print(force)
    return(force)

# Part 3 Gravity

def pull(m1, m2, d):
    gravity_constant = 6.674*(10**-11)
    force = gravity_constant*m1*m2/(d**2)
    print(force)
    return(force)

# Testing

if __name__ == "__main__":
    greet("evert", "Jo, <name>!")
    force(2, 'jupiter')
    pull(800,1500,3)

