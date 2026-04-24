
def process_voice_command(command):
    command = command.lower()

    if "low stock" in command:
        return "Showing low stock items"

    elif "supplier" in command:
        return "Opening supplier dashboard"

    elif "alerts" in command:
        return "Displaying alert dashboard"

    elif "forecast" in command:
        return "Showing demand forecast"

    else:
        return "Command not recognized"


if __name__ == "__main__":
    command = input("Enter command: ")

    result = process_voice_command(command)

    print("Response:", result)
