from typing import Final

# Constants
GRAVITATIONAL_ACCELERATION: Final[float] = 9.81

accuracy = input("---How accurate do you want the integration to be---\n" +
                "1) Less accurate but quick calculation speed\n" + 
                "2) Accurate and normal calculation speed\n" + 
                "3) Very Accurate and slow calculation speed\n" + "Choose 1, 2, or 3: ")

while accuracy not in ['1', '2', '3']:
    print("\n###That is not a valid choice!###")
    accuracy = input("---How accurate do you want the integration to be---\n" +
                    "1) Less accurate but quick calculation speed\n" + 
                    "2) Accurate and normal calculation speed\n" + 
                    "3) Very Accurate and slow calculation speed\n" + "Choose 1, 2, or 3: ")

if accuracy == '1':
    h = 0.001
elif accuracy == '2':
    h = 0.0001
elif accuracy == '3':
    h = 0.00001
    

nsteps = int(float(input("How many seconds would you like to simulate?: ")) / h)