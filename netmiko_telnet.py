 from netmiko import ConnectHandler
from netmiko.exceptions import NetmikoTimeoutException, NetmikoAuthenticationException
import getpass
import os

def main():
    # Define the file containing your hostnames/IPs
    filename = 'hosts.txt'

    # Check if the file actually exists before doing anything
    if not os.path.exists(filename):
        print(f"Error: The file '{filename}' was not found in the current directory.")
        return

    # 1. Prompt for credentials and command ONLY ONCE
    username = input("Enter your Telnet username: ")
    password = getpass.getpass("Enter your Telnet password: ")
    command_to_run = input("Enter the command to run on all hosts: ")

    # 2. Read the list of hosts from the text file
    with open(filename, 'r') as file:
        # Read the file, remove extra whitespace/newlines, and skip empty lines
        hosts = [line.strip() for line in file if line.strip()]

    if not hosts:
        print(f"Error: '{filename}' is empty. Add some hostnames or IPs.")
        return

    print(f"\nLoaded {len(hosts)} hosts from {filename}. Starting Telnet connections...\n")

    # 3. Iterate through each host in the list

