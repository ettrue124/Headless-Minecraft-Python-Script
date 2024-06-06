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
Then Login with Microsoft Account:
    
    login <email@gmail.com>
To download minecraft/fabric/neoforge/forge run:

    download <Minecraft Version>
    fabric <Version>
    forge <Version>
    neoforge <Version>
    
    
    
Run the Python Script:

    python main.py -config <Minecraft Directory Path> -name <Minecraft Offline Username> -version <Minecraft Version> -playername <Minecraft Player Name> -ip <Minecraft Server IP Address> <Minecraft Server Port>

This project is licensed under the MIT License.
