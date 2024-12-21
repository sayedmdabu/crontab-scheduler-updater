# Crontab Scheduler Updater

A Python script to automate the updating of crontab schedules for specific commands. This tool is designed to make it easier to manage scheduled tasks in Linux systems by programmatically modifying the crontab entries.

## Features

- Fetches the current crontab entries.
- Updates the schedule for a specific command without affecting other entries.
- Preserves comments and blank lines in the crontab.
- Provides detailed error handling for common issues (e.g., command not found, invalid syntax).

## Requirements

- Python 3.6+
- Linux system with `crontab` command available

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/crontab-scheduler-updater.git
   ```

2. Navigate to the project directory:
   ```bash
   cd crontab-scheduler-updater
   ```

3. Ensure Python 3 is installed on your system.

## Usage

### Example Script

The script updates the crontab entry for a specific command.

1. Open the script and modify the `cron_value` and `command_to_match` variables in the `main()` function:
   ```python
   cron_value = "0 5 * * *"  # New schedule (e.g., 5 AM daily)
   command_to_match = "/usr/bin/python3 /path/to/script.py"  # Command to update
   ```

2. Run the script:
   ```bash
   python3 crontab_updater.py
   ```

3. If the command is found, the script updates its schedule. Otherwise, it raises an error.

### Sample Crontab Update

#### Before:
```bash
# Backup script
0 2 * * * /usr/bin/python3 /path/to/script.py
```

#### After:
```bash
# Backup script
0 5 * * * /usr/bin/python3 /path/to/script.py
```

## Notes

- The script only updates existing crontab entries. It does not add new entries.
- Ensure that the `command_to_match` is unique to avoid unintended modifications.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request with your improvements or suggestions.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.


