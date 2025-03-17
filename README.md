# SiteBlocker

### SiteBlocker is a simple Python-based application that helps you block specific websites by modifying your system's hosts file. The project is designed to help you block distracting websites (such as social media) to improve productivity or to enforce time-based restrictions.

## Features:
- Website Blocking: Block selected websites (e.g., Facebook, Instagram) by redirecting them to 127.0.0.1 (localhost).
- Time-Based Blocking: Set the script to block websites during specific times (e.g., work hours) or at all times.
- Easy Setup: Automatically modify your system's hosts file without the need for manual edits.

## How It Works:
- The script compares the current time with a predefined end_time.
- If the current time surpasses the end_time, the script begins blocking the specified websites by adding them to the hosts file.
- If the time is outside the blocking period, the script removes those websites from the hosts file to unblock them.
- The hosts file is updated to redirect unwanted sites (such as social media) to 127.0.0.1, effectively blocking access.

## Conclusion:
- Hosts File Method: Ideal for a straightforward solution to block websites at the system level. You can also schedule blocking based on time.
- Proxy Server Method: A more advanced approach that offers greater control, such as request logging and dynamic blocking. 
