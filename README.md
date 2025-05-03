# mldk-monitor
## Python script to monitor system performance and log CPU and memory usage over time.

This is a Python script using the `psutil` library to monitor CPU and memory usage and log the data to a file.

**Features:**

1.  **Cross-Platform:** Uses `psutil`, which works on Linux, Windows, macOS, and more.
2.  **Logging:** Uses Python's built-in `logging` module to save data with timestamps to a file (`system_monitor.log`).
3.  **Configurable Interval:** You can easily change how often the script checks the system performance.
4.  **Graceful Shutdown:** Stops cleanly when you press Ctrl+C.
5.  **Clear Output:** Logs CPU percentage and Memory usage (percentage, used GB, total GB).

**Prerequisites:**

You need to install the `psutil` library first. Open your terminal or command prompt and run:
```bash
pip install psutil
```

**How to Use:**

1.  **Run:** Open your terminal or command prompt, navigate to the directory where you saved the file, and run it using Python:
    ```bash
    python monitor.py
    ```
2.  **Monitor:** The script will start printing the CPU and memory usage to your console *and* logging it to the `system_monitor.log` file in the same directory.
    * Console output example:
        ```
        2025-05-01 12:40:00 - INFO - System monitoring started.
        2025-05-01 12:40:00 - INFO - Logging interval: 5 seconds
        2025-05-01 12:40:00 - INFO - Log file: system_monitor.log
        2025-05-01 12:40:00 - INFO - CPU Usage: 12.3% | Memory Usage: 45.6% (7.30 GB / 16.00 GB)
        2025-05-01 12:40:05 - INFO - CPU Usage: 15.8% | Memory Usage: 45.7% (7.31 GB / 16.00 GB)
        ...
        ```
    * `system_monitor.log` file content will look similar.
3.  **Stop:** Press `Ctrl+C` in the terminal where the script is running to stop it gracefully. A "Monitoring stopped" message will be logged and printed.

This script provides a basic but effective way to monitor your system's core performance metrics over time. You can extend it further to log disk I/O, network activity, or specific process information using other functions available in the `psutil` library.