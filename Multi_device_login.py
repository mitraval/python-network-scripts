import paramiko
import time
import getpass
import os


def send_and_wait(channel, command, wait_for_text, timeout=20):
    channel.send(command + '\n')
    output = ""
    start_time = time.time()

    while (time.time() - start_time) < timeout:
        if channel.recv_ready():
            output += channel.recv(65535).decode('utf-8', errors='ignore')
            if wait_for_text in output:
                return output
        time.sleep(0.5)

    print(f"\n[!] Timeout waiting for '{wait_for_text}'")
    return output


# ==============================================================================
# GATHERING TARGET DEVICES FROM FILE
# ==============================================================================

# We use a try/except here just in case the file is missing or named incorrectly!
try:
    with open('devices.txt', 'r') as file:
        # This loops through every line in the text file.
        # .strip() removes hidden newlines and accidental spaces.
        # 'if line.strip()' ensures we completely ignore any blank lines.
        host = [line.strip() for line in file if line.strip()]
        print(f"[+] Successfully loaded {len(host)} devices from devices.txt")

except FileNotFoundError:
    print("\n[X] Error: Could not find 'devices.txt'. Please ensure the file is in the same folder as this script.")
    exit()  # Stop the script so it doesn't crash later

linux = {'hostname': 'JumpserverIP', 'port': '22', 'username': 'JUMPSERVERUSERNAME', 'password': 'JUMPSERVERPASS'}
ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(**linux, look_for_keys=False, allow_agent=False)
remote_connection = ssh_client.invoke_shell()
time.sleep(3)

with open('ports.txt', 'w') as f:
    for device in host:
        try:
            print(f"Pinging {device}...")
            # Send a Linux ping command:
            # -c 2 means send exactly 2 pings.
            # -W 2 means timeout after 2 seconds if no reply.
            # We wait for the "$" or "#" prompt to return, meaning the ping finished.
            ping_output = send_and_wait(remote_connection, f"ping -c 2 -W 4 {device}", "$", timeout=20)
            # Check the text output to see if the ping failed
            if "100% packet loss" in ping_output or "Unreachable" in ping_output:
                print(f"[!] {device} is DEAD (Ping Failed). Skipping SSH attempt...")
                f.write(f"--- {device} OFFLINE (PING FAILED) ---\n")

                continue  # Instantly skip to the next device!

            print(f"[+] Ping successful! Initiating SSH...")

            print(f'connecting to {device} \n')
            send_and_wait(remote_connection, f'ssh -o StrictHostKeyChecking=no -l USERNAME {device}', "assword",
                          timeout=15)
            # output = remote_connection.recv(10240).decode()
            # remote_connection.send('yes\n')

            send_and_wait(remote_connection, "Password", "#", timeout=10)
            send_and_wait(remote_connection, "ter len 0", "#, timeout=5")
            final_output = send_and_wait(remote_connection, "sh int desc", "#", timeout=5)

            # output = remote_connection.recv(9999).decode()
            print(final_output)
            f.write(f' \n------{device}------\n')
            f.write(final_output)
            f.flush()
            send_and_wait(remote_connection, "exit", "$", timeout=5)



        except Exception as e:
            print(f'[!] critical error occured on {device}:{repr(e)}')
            f.write(f'---{device} Script Error ---\n')

            break
ssh_client.close()
print('Script Complete !!')