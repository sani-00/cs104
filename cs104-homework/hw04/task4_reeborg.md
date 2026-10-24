# Task 4: Reeborg

## Hurdle 3

```python
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def neo():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

while not at_goal():
    if front_is_clear():
        move()
    else:
        neo()
```

## Hurdle 4

```python
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def neo():
    turn_left()
    while not right_is_clear():
        move()
    turn_right()
    move()
    turn_right()
    move()
    while front_is_clear():
      move()
    turn_left()

while not at_goal():
    if front_is_clear():
        move()
    else:
        neo()
```

## Maze

```python
while not at_goal():
    if right_is_clear():
        turn_left()
        turn_left()
        turn_left()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()
```