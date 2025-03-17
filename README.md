## SiteBlocker

#### SiteBlocker is a simple Python-based application that helps you block specific websites by modifying your system's hosts file. The project is designed to help you block distracting websites (such as social media) to improve productivity or to enforce time-based restrictions.

## Features:
- Website Blocking: Block specific websites (e.g., Facebook, Instagram, etc.) by redirecting them to 127.0.0.1 (localhost).
- Time-Based Blocking: Configure the script to block websites only during a specific time period (e.g., work hours) or continuously.
- Easy Setup: Modify your system's hosts file without manually editing it.

## How It Works:
- The script checks the current time and compares it with a predefined end_time.
- If the current time exceeds the end_time, the script starts blocking the specified websites by adding entries in the hosts file.
- If the time is not within the blocking range, the script removes those entries from the hosts file to unblock the websites.
- The hosts file is modified to redirect unwanted sites (like social media) to 127.0.0.1, effectively blocking access.
