import argparse
import subprocess

def Config():
    # Define the path to the pre-defined configuration file
    pre_defined_file_path = r"HeadlessMC\config.properties"

    # Create an argument parser
    parser = argparse.ArgumentParser(description="Minecraft Headless Configuration")

    # Define the command line arguments
    parser.add_argument('-config', type=str, required=True, help="Minecraft Directory Path")
    parser.add_argument('-name', type=str, required=False, help="Minecraft Offline Username enter if you want to play offline")
    parser.add_argument('-version', type=str, required=True, help="Minecraft Version")
    parser.add_argument('-playername', type=str, required=True, help="Minecraft Player that can speak with to the bot")
    parser.add_argument('-ip', type=str, default="localhost", help="Minecraft Server IP Address default is localhost")
    parser.add_argument('port', type=int, default=25565, nargs='?', help="Minecraft Server Port default is 25565")

    # Parse the command line arguments
    args = parser.parse_args()

    # Extract the values from the arguments
    minedir = args.config
    offlinevalue = False if args.name is None else True
    name = args.name if args.name is not None else ""
    version = args.version
    playername = args.playername
    ip = args.ip
    port = args.port

    # Write the configuration to the pre-defined file
    with open(pre_defined_file_path, 'w') as file:
        file.write(f"hmc.gamedir={minedir}\nhmc.mcdir={minedir}\nhmc.offline={offlinevalue}")

    # Print a message indicating the file where the configuration was written
    print(f"Message written to {pre_defined_file_path}")

    # Return the extracted values
    return name, ip, port, version, playername

def read_output(shell_process):
    # Read the output from the shell process line by line
    while True:
        output = shell_process.stdout.readline()
        if output:
            print(output.strip())
        else:
            break

def start_minecraft(username, ip, port, version, playername):
    # Define the command to start Minecraft
    command = ["java", "-jar", "headlessmc-launcher-1.9.5.jar", "-username", username]

    try:
        # Start the shell process
        shell_process = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, bufsize=1, universal_newlines=True)

        # Wait for the process to output "parent" indicating that it has started successfully
        while True:
            output = shell_process.stdout.readline()
            if output:
                print(output.strip())
                if "parent" in output:
                    break

        # Determine the value for the offline flag
        valueoffline = "-lwjgl" if username != "" else ""

        # Send the launch command to the shell process
        shell_process.stdin.write(f"launch {version} {valueoffline}\n")
        shell_process.stdin.flush()

        # Wait for the process to output an error message indicating a Realms service error
        while True:
            output = shell_process.stdout.readline()
            if output:
                print(output.strip())
                if "Realms service error (400) with no payload" in output:
                    break

        # Connect to the Minecraft server
        shell_process.stdin.write(f"connect {ip} {port}\n")
        shell_process.stdin.flush()

        # Read the output from the shell process and respond to incoming messages
        while True:
            output = shell_process.stdout.readline()
            if output:
                print(output.strip())
            if f"[CHAT] {playername} whispers to you:" in output:
                text = output.split(f"[CHAT] {playername} whispers to you:")[1].strip()
                print(f"Received message: {text}")
                shell_process.stdin.write(f'msg "{text}"\n')
                shell_process.stdin.flush()

    except Exception as e:
        # Print an error message if an exception occurs
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Call the Config function to get the configuration values
    Name, ip, port, version, playername = Config()

    # Start Minecraft with the obtained configuration values
    start_minecraft(Name, ip, port, version, playername)