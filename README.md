# Headless Minecraft Python Script

This project allows you to run a headless instance of Minecraft, connect it to a server, and interact with it through a Python script. The project uses HeadlessMC and a custom Python script to automate tasks within Minecraft.
Contents

    HeadlessMC: Directory containing HeadlessMC resources.
    headlessmc-launcher-1.9.5.jar: The HeadlessMC launcher JAR file.
    main.py: The main Python script to start the headless Minecraft instance and interact with it.

## Setup

Install Java: Ensure that you have Java installed on your machine. You can download it from here: https://www.oracle.com/java/technologies/downloads/#java21

Download HeadlessMC:

Install Python: Ensure that you have Python installed on your machine. You can download it from here: https://www.python.org/downloads/

Clone this repository:

    git clone https://github.com/ettrue124/Headless-Minecraft-Python-Script
    cd <repository_directory>

## Running Project
Launch the headless client to download versions or login:

    java -jar headlessmc-launcher-1.9.5.jar
### Then Login with Microsoft Account:
    
    login <email@gmail.com>
### To download minecraft/fabric/neoforge/forge run:

    download <Minecraft Version>
    fabric <Version>
    forge <Version>
    neoforge <Version>
    
    
    
### To run the script, use the following command:

    python main.py -config <Minecraft Directory Path> -name <Minecraft Offline Username> -version <Minecraft Version> -playername <Minecraft Player Name> -ip <Minecraft Server IP Address> <Minecraft Server Port>

Replace the placeholders with actual values:

    <Minecraft Directory Path>: Path to your Minecraft installation directory.
    <Minecraft Offline Username>: The offline username you want to use. Leave blank to use online mode.
    <Minecraft Version>: The Minecraft version you want to use (e.g., 1.19.4).
    <Minecraft Player Name>: The name of the player that can control the bot.
    <Minecraft Server IP Address>: The IP address of the Minecraft server.
    <Minecraft Server Port>: The port number of the Minecraft server.

Example:

    python main.py -config C:\Users\Name\AppData\Roaming\.minecraft -name Bot -version fabric-loader-0.15.10-1.20.4 -playername Player123 -ip mc.hypixel.net

Troubleshooting

    Ensure the Minecraft directory path is correct.
    Verify that you have the correct IP address and port number for the Minecraft server.
    Check for any errors in the script execution and refer to error messages for guidance.

This project is licensed under the MIT License.
