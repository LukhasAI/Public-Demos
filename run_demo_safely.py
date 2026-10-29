#!/usr/bin/env python3
"""Source-only research overviews for showcase entries without a verified live path.

These are explicit descriptions, NOT a fallback that pretends to run a feature.
Only standard-library code is used. The result is deliberately labelled.
"""

import sys

PREVIEWS = {
    "qrg_showcase": (
        "QRG showcase",
        "Historical QRG concepts and scannable identity demonstrations. "
        "The named source file is not a verified quantum-reasoning implementation.",
    ),
    "abstract_reasoning": (
        "Abstract reasoning",
        "Metaphor-inspired and symbolic representation experiments. "
        "No claim of a working metaphor compiler or validated reasoning benchmark.",
    ),
    "lambda_workforce": (
        "Workforce agent research",
        "Concepts for coordinating specialised agents; "
        "not a benchmarked or enterprise-deployed product.",
    ),
    "autonomous_agent_framework": (
        "Autonomous agent framework",
        "Historical agent orchestration concepts; "
        "not evidence of autonomous, safe, or production-ready deployment.",
    ),
}


def run_demo_with_fallback(name: str) -> int:
    """Display a named research overview; return nonzero for an unknown name."""
    preview = PREVIEWS.get(name)
    if preview is None:
        print(f"Unknown research overview: {name}", file=sys.stderr)
        print("Available: " + ", ".join(sorted(PREVIEWS)), file=sys.stderr)
        return 2

    title, description = preview
    print("=" * 64)
    print(f"RESEARCH OVERVIEW — {title}")
    print("Conceptual material only. No live capability has been executed.")
    print("=" * 64)
    print(description)
    return 0


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python run_demo_safely.py <overview_name>", file=sys.stderr)
        print("Available: " + ", ".join(sorted(PREVIEWS)), file=sys.stderr)
        raise SystemExit(2)
    raise SystemExit(run_demo_with_fallback(sys.argv[1]))
