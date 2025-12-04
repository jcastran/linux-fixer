#!/usr/bin/env python3
"""
Linux Fixer - A tool to simulate fixing Linux problems with a progress bar.
"""
import sys
from time import sleep
from tqdm import trange
import argparse


def parse_args():
    """Parse command line arguments.

    Returns:
        argparse.Namespace: Parsed command line arguments.
    """
    parser = argparse.ArgumentParser(
        description='Simulate fixing Linux problems with a progress bar'
    )
    parser.add_argument(
        '-a', '--amount',
        type=int,
        default=42,
        help='Number of problems to fix (Default: 42)'
    )
    parser.add_argument(
        '-d', '--delay',
        type=float,
        default=0.05,
        help='Delay between each fix in seconds (Default: 0.05)'
    )
    parser.add_argument(
        '-m', '--message',
        type=str,
        default='Problems Resolved',
        help='Custom completion message (Default: "Problems Resolved")'
    )
    parser.add_argument(
        '-q', '--quiet',
        action='store_true',
        help='Suppress completion message'
    )
    return parser.parse_args()


def run_fixer(amount, delay=0.05):
    """Run the problem fixer with a progress bar.

    Args:
        amount (int): Number of problems to fix.
        delay (float): Delay between each fix in seconds.

    Raises:
        KeyboardInterrupt: If user interrupts the process.
    """
    for i in trange(amount, desc="Fixing problems"):
        sleep(delay)


def main():
    """Main function to run the Linux Fixer."""
    args = parse_args()

    # Validate arguments
    if args.amount <= 0:
        print("Error: Amount must be greater than 0", file=sys.stderr)
        sys.exit(1)

    if args.delay < 0:
        print("Error: Delay cannot be negative", file=sys.stderr)
        sys.exit(1)

    try:
        run_fixer(args.amount, args.delay)

        # Print completion message unless quiet mode
        if not args.quiet:
            print(f"\n{args.message}")

    except KeyboardInterrupt:
        print("\n\nOperation cancelled by user", file=sys.stderr)
        sys.exit(130)  # Standard exit code for SIGINT
    except Exception as e:
        print(f"\nError: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
