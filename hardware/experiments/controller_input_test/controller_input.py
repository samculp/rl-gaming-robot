import pygame

def main():

    pygame.init()
    pygame.joystick.init()

    if pygame.joystick.get_count() == 0:
        print("No controller deteced")
        quit()
    else:
        print("Controller detected!")

    controller = pygame.joystick.Joystick(0)
    controller.init()

    print(f"Controller: {controller.get_name()}")
    print(f"Buttons: {controller.get_numbuttons()}")
    print(f"Axes: {controller.get_numaxes()}")
    print(f"Hats/D-pads: {controller.get_numhats()}")

    print("\nPress buttons. Close the window or Ctrl+C to quit.\n")

    while True:
        for event in pygame.event.get():

            if event.type == pygame.JOYBUTTONDOWN:
                print(f"BUTTON PRESSED: {event.button}")

            elif event.type == pygame.JOYBUTTONUP:
                print(f"BUTTON RELEASED: {event.button}")

            elif event.type == pygame.JOYAXISMOTION:
                print(f"AXIS {event.axis}: {event.value:.2f}")

            elif event.type == pygame.JOYHATMOTION:
                print(f"D-PAD: {event.value}")

            elif event.type == pygame.QUIT:
                pygame.quit()
                quit()


def get_button_action(button):
    actions = {
        0: "A",
        1: "B",
        2: "SELECT",
        3: "START",
    }
    return actions.get(button, "UNKNOWN")


if __name__ == "__main__":
    main()