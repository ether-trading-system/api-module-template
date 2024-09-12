from invoke import task, Collection


@task(
    help={
        "name": "Name of the person to greet",
        "age": "Age of the person to greet",
    }
)
def greet(c, name: str = "World", age: int = 0):
    print(f"Hello, {name}! You are {age} years old.")


namespace = Collection(greet)
