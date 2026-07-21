# Passing functions as arguments

def greet(name):
    print(f"Hello, {name}")

def execute(function):
    function("Wasim")

execute(greet)
