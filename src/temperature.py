"""Temperature conversion helpers and command-line entry point."""

import argparse


def celsius_to_fahrenheit(celsius: float) -> float:
    """Convert a Celsius temperature to Fahrenheit."""
    return celsius * 9 / 5 + 32


def build_parser() -> argparse.ArgumentParser:
    """Create the command-line argument parser."""
    parser = argparse.ArgumentParser(description="Convert Celsius to Fahrenheit")
    parser.add_argument("celsius", type=float, help="temperature in degrees Celsius")
    return parser


def main() -> None:
    """Run the command-line converter."""
    args = build_parser().parse_args()
    fahrenheit = celsius_to_fahrenheit(args.celsius)
    print(f"{args.celsius:g}°C = {fahrenheit:g}°F")


if __name__ == "__main__":
    main()
