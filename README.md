Headless Minecraft Python Script

This project allows you to run a headless instance of Minecraft, connect it to a server, and interact with it through a Python script. The project uses HeadlessMC and a custom Python script to automate tasks within Minecraft.
Contents

    HeadlessMC: Directory containing HeadlessMC resources.
    headlessmc-launcher-1.9.5.jar: The HeadlessMC launcher JAR file.
    main.py: The main Python script to start the headless Minecraft instance and interact with it.
    readme: Existing readme file.

Setup

    Install Java: Ensure that you have Java installed on your machine. You can download it from here.

    Download HeadlessMC: The HeadlessMC launcher JAR file is already included in this project. No further action is needed.

    Install Python: Ensure that you have Python installed on your machine. You can download it from here.

    Install Python dependencies:

    sh

    pip install -r requirements.txt

Running the Project

    Start HeadlessMC:

    sh

java -jar headlessmc-launcher-1.9.5.jar

Run the Python Script:

sh

    python main.py

Project Structure

    HeadlessMC: Contains the configuration and additional resources for HeadlessMC.
    headlessmc-launcher-1.9.5.jar: The HeadlessMC launcher used to run Minecraft in a headless mode.
    main.py: Python script to start and control the Minecraft instance.

Usage

    Configuration: Ensure that the configuration in main.py is set according to your requirements, including the server address and any commands you wish to send to the Minecraft instance.

    Running the Script: Follow the steps in the "Running the Project" section to start HeadlessMC and run the Python script.

Contributing

Feel free to submit issues and pull requests for any improvements or bug fixes.
License

This project is licensed under the MIT License.
