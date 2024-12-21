import subprocess

# Function to update crontab by modifying the schedule for a specific command
def update_crontab(new_timing, command_to_match):
    """
    Updates the schedule for a specific command in the system's crontab.

    Parameters:
        new_timing (str): The new cron timing to set (e.g., "0 5 * * *").
        command_to_match (str): The command to search for in the existing crontab.
    """
    try:
        # Step 1: Read the current crontab
        # Fetches the current crontab using the 'crontab -l' command.
        result = subprocess.run(['crontab', '-l'], stdout=subprocess.PIPE, text=True, check=True)
        current_crontab = result.stdout.splitlines()

        # Step 2: Prepare to update crontab
        updated_crontab = []
        found = False

        for line in current_crontab:
            # Preserve comments and blank lines
            if line.strip().startswith('#') or not line.strip():
                updated_crontab.append(line)
                continue

            # Check if the line contains the target command
            if command_to_match in line:
                # Split the line into timing and command parts
                parts = line.split(maxsplit=5)
                if len(parts) >= 6:
                    # Update the cron timing for the matched command
                    updated_line = f"{new_timing} {parts[5]}"
                    updated_crontab.append(updated_line)
                    found = True
                    print(f"Updated crontab line: {updated_line}")
                else:
                    # Append the line as-is if it doesn't match the expected format
                    updated_crontab.append(line)
            else:
                # Append other non-matching lines as-is
                updated_crontab.append(line)

        # Step 3: Handle case where command was not found
        if not found:
            # Raise an error if the command was not found in the crontab
            raise ValueError(f"Command '{command_to_match}' not found in crontab.")

        # Step 4: Write the updated crontab back
        # Combine updated lines into a single string and write it back to crontab
        updated_crontab_text = "\n".join(updated_crontab) + "\n"
        subprocess.run(['crontab', '-'], input=updated_crontab_text, text=True, check=True)
        print("Crontab updated successfully.")

    except Exception as e:
        # Handle and print any errors that occur during the process
        print(f"Error updating crontab: {e}")
        raise

def main():
    """
    Updates the timing for a specific command in the system's crontab.

    Example Usage:
        update_crontab("0 5 * * *", "/usr/bin/python3 /path/to/script.py")
    """
    try:
        # Step 1: Define the new cron timing
        cron_value = "0 5 * * *"  # Example: 5 AM daily

        # Step 2: Specify the command to match in the crontab
        command_to_match = "/usr/bin/python3 /path/to/script.py"

        # Step 3: Call the function to update the crontab
        update_crontab(cron_value, command_to_match)

    except Exception as e:
        # Print the error traceback for debugging
        print(f"An error occurred: {e}")
        import traceback
        print(traceback.format_exc())


if __name__ == "__main__":
    # Entry point of the script
    main()
