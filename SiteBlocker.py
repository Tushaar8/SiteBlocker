import datetime
import time
import os

end_time = datetime.datetime(2025, 10, 31)
site_block = ["www.facebook.com", "www.instagram.com"]
host_path = "C:/Windows/System32/drivers/etc/hosts"
redirect = "127.0.0.1"

def block_websites():
    with open(host_path, "r+") as host_file:
        content = host_file.read()
        for website in site_block:
            if website not in content:
                host_file.write(redirect + " " + website + "\n")
                print(f"Blocking {website}")

def unblock_websites():
    with open(host_path, "r+") as host_file:
        content = host_file.readlines()
        host_file.seek(0)
        for line in content:
            if not any(website in line for website in site_block):
                host_file.write(line)
        host_file.truncate()
        print("Websites unblocked")

def main():
    while True:
        if datetime.datetime.now() > end_time:
            print("Start Blocking Websites")
            block_websites()
        else:
            print("Time is up, unblock websites")
            unblock_websites()
        time.sleep(300)

if __name__ == "__main__":
    try:
        main()
    except PermissionError:
        print("Error: Script requires administrative privileges to modify the hosts file.")
    except Exception as e:
        print(f"An error occurred: {e}")
