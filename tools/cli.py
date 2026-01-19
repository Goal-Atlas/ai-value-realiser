"""
AI Value Realiser CLI

Command-line interface for case library management and analysis.
"""

import argparse


def main() -> None:
    """Main CLI entrypoint."""
    parser = argparse.ArgumentParser(
        prog="aivr",
        description="AI Value Realiser - Evidence-based AI value identification",
    )
    
    subparsers = parser.add_subparsers(dest="command", help="Available commands")
    
    # Case commands
    case_parser = subparsers.add_parser("case", help="Case management")
    case_subparsers = case_parser.add_subparsers(dest="action")
    case_subparsers.add_parser("list", help="List all cases")
    case_subparsers.add_parser("build", help="Build a new case")
    case_subparsers.add_parser("validate", help="Validate a case")
    
    # Ontology commands
    ontology_parser = subparsers.add_parser("ontology", help="Ontology management")
    ontology_subparsers = ontology_parser.add_subparsers(dest="action")
    ontology_subparsers.add_parser("show", help="Show current ontology")
    ontology_subparsers.add_parser("stats", help="Show ontology usage statistics")
    
    args = parser.parse_args()
    
    if args.command is None:
        parser.print_help()
        return
    
    # TODO: Implement command handlers
    print(f"Command: {args.command}")
    if hasattr(args, "action") and args.action:
        print(f"Action: {args.action}")
    print("(Not yet implemented)")


if __name__ == "__main__":
    main()
