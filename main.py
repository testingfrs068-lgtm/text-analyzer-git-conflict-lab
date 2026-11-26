#!/usr/bin/env python3
"""
CLI Runner for Text Summarizer & Readability Analyzer
UCS 745 Cloud & DevOps Lab - Manvendra
"""

import sys
from analyzer import count_words_and_sentences, summarize_text, top_keywords

SAMPLE_TEXT = (
    "Cloud computing allows teams to provision servers and storage on demand without managing physical hardware. "
    "DevOps practices combine software development and IT operations to shorten the delivery lifecycle. "
    "Using Git branches and pull requests helps teams collaborate safely on shared codebases. "
    "Automated testing ensures that new features do not break existing functionality before deployment."
)


def main():
    print("=== Text Summarizer & Readability Analyzer ===")
    if len(sys.argv) > 1 and sys.argv[1] == "--demo":
        text = SAMPLE_TEXT
    else:
        print("Enter text to analyze (or press Enter for sample text):")
        user_input = input("> ").strip()
        text = user_input if user_input else SAMPLE_TEXT

    stats = count_words_and_sentences(text)
    summary = summarize_text(text, max_sentences=2)
    keywords = top_keywords(text, n=4)

    print(f"\nStats    : {stats}")
    print(f"Keywords : {keywords}")
    print(f"Summary  : {summary}\n")


if __name__ == "__main__":
    main()
