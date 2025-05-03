#!/usr/bin/env python3

"""
Monitors system CPU and Memory usage and logs it to a file over time.
"""

import psutil
import time
import logging
from datetime import datetime
import sys # Import sys module for sys.exit

# --- Configuration ---
LOG_FILE = "system_monitor.log"  # Name of the log file
MONITOR_INTERVAL_SECONDS = 5     # How often to check (in seconds)
LOG_FORMAT = '%(asctime)s - %(levelname)s - %(message)s'
DATE_FORMAT = '%Y-%m-%d %H:%M:%S'
# --- End Configuration ---

def setup_logging():
    """Configures the logging."""
    logging.basicConfig(
        level=logging.INFO,
        format=LOG_FORMAT,
        datefmt=DATE_FORMAT,
        handlers=[
            logging.FileHandler(LOG_FILE),
            logging.StreamHandler() # Also print logs to console
        ]
    )
    logging.info("System monitoring started.")
    logging.info(f"Logging interval: {MONITOR_INTERVAL_SECONDS} seconds")
    logging.info(f"Log file: {LOG_FILE}")

def get_system_stats():
    """Retrieves current CPU and Memory statistics."""
    # Get CPU usage percentage.
    # interval=None makes it non-blocking and returns the CPU usage since the last call or boot.
    # Using a small interval like 0.1 or 1 can provide a more averaged reading over that period.
    cpu_usage = psutil.cpu_percent(interval=None)

    # Get memory usage details
    memory_info = psutil.virtual_memory()
    memory_percent = memory_info.percent
    memory_used_gb = memory_info.used / (1024**3)  # Convert bytes to GB
    memory_total_gb = memory_info.total / (1024**3) # Convert bytes to GB

    return cpu_usage, memory_percent, memory_used_gb, memory_total_gb

def main():
    """Main monitoring loop."""
    setup_logging()

    try:
        while True:
            # Get current stats
            cpu, mem_perc, mem_used, mem_total = get_system_stats()

            # Format the log message
            log_message = (
                f"CPU Usage: {cpu:.1f}% | "
                f"Memory Usage: {mem_perc:.1f}% "
                f"({mem_used:.2f} GB / {mem_total:.2f} GB)"
            )

            # Log the information
            logging.info(log_message)

            # Wait for the next interval
            time.sleep(MONITOR_INTERVAL_SECONDS)

    except KeyboardInterrupt:
        logging.info("Monitoring stopped by user (Ctrl+C).")
        print("\nMonitoring stopped.")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}", exc_info=True)
        print(f"An error occurred: {e}")
    finally:
        logging.info("System monitoring ended.")
        sys.exit(0) # Ensure script exits cleanly

if __name__ == "__main__":
    main()