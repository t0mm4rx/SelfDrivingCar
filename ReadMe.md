# SelfDrivingCar

This project allows you to make multiple AI controll cars and compete in a race. This can used to make AI battles, or to compare differents strategies.

## How does it work ?

First of all, you each AI, or controller, needs its own directory in the "controllers" folder. You can copy/paste the empty folder, which is an empty template.

You can launch a game with this command :
```bash
python game.py <config_file.json>
```

The config file describes the map, and the different cars that will compete.
- Multiple cars can be controlled by the same controller
- Only one car can be human-controlled (with the playable option)
- You can see what the car sees with the debug option
- Two cars can't have the same name

Here is an example of a config file :
```json
{
  "map": "road1.json",
  "players": [
    {
      "name": "IA",
      "folder": "empty",
      "playable": true,
      "debug": true
    },
    {
      "name": "IA2",
      "folder": "test",
      "playable": false,
      "debug": false
    }
  ]
}
```
Here, the map will be road1.json. The race will contain two cars.
The first one, which is called 'IA', is controlled by the keyboard, because the playable option is true. You can use this option to test the game, and get data (we will see how get that data later) to make machine learning for example. So your controller won't be able to move the car, until you don't switch the playable option. The debug flag will help you figure out how sensors work.
The second one, called 'IA2' is controlled by its AI.

The folder option is the name of the folder in the controllers directory. It's the option that choose the controller you want to use.

## Controller

A controller is a behaviour, how the car will be controlled.
To create a new controller, you can copy/paste and rename the empty folder, which is a template.
The requirements are :
- A controller is a class named 'Controller', which extends of AI
- The Controller class should be in a file named 'ai.py'
- This file is placed in a subfolder of controllers directory

AI class will provide you two function:
- start(self, road). This function is called once before the race. Road is an object representing the map. Interesting properties of this object are 'road.lines', which contains every segment of the road, and 'road.points', that contains the path of the road. You can look at the Road.py class to see what data you can use.
- play(self, sensors, speed, heading, inputs).
  Sensors is an array of every sensors of the car. The 'value' property of sensors is the more important. It gives you the distance between you and the nearest bound of the road in a specific direction. You can activate the debug option to see how it works.
  Speed is the speed vector.
  Heading is the direction vector, normalized to 1.
  Inputs is always None if the car isn't playable. If it's playable, it contains the key inputs : [ top, right, down, left ]. This is useful to train a ML model from a human behaviour.

Here is the default controller :
```python
import sys
sys.path.append('../..')
from AI import AI

class Controller(AI):

    def start(self, map):
        print("My controller !")

    def play(self, sensors, speed, heading, inputs):
        print(sensors, speed, heading, inputs)

```

## Maps

Maps are json-formatted. All maps are in the 'maps' foler.
```json
{
  "width": 120,
  "points": [
    [100, 100],
    [1100, 100],
    [1100, 900],
    [100, 900]
  ]
}
```
The width property defines the width of the road. Points is an array representing the path of the road.
Bounds of the road are automatically calculated.
