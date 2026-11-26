"""
Text Summarizer & Readability Analyzer
UCS 745 Cloud and DevOps Lab Project
Author: Manvendra (testingfrs068-lgtm)
"""

import re
from collections import Counter

STOP_WORDS = {
    "the", "a", "an", "and", "or", "but", "in", "on", "at", "to", "for",
    "of", "with", "by", "is", "are", "was", "were", "be", "been", "this",
    "that", "it", "as", "from", "we", "you", "they", "i",
}


def count_words_and_sentences(text: str) -> dict:
    """Return basic word, character, and sentence counts."""
    words = re.findall(r"\b\w+\b", text)
    sentences = [s.strip() for s in re.split(r"[.!?]+", text) if s.strip()]
    return {
        "characters": len(text),
        "words": len(words),
        "sentences": len(sentences),
    }


def summarize_text(text: str, max_sentences: int = 2, min_words: int = 6) -> str:
    """
    Generate a short summary after filtering out short sentences.
    Added in feature/length-filter branch.
    """
    sentences = [s.strip() for s in re.split(r"(?<=[.!?])\s+", text.strip()) if s.strip()]
    filtered = [s for s in sentences if len(re.findall(r"\b\w+\b", s)) >= min_words]
    if not filtered:
        filtered = sentences
    return " ".join(filtered[:max_sentences])


def top_keywords(text: str, n: int = 5) -> list:
    """Return the top n most frequent non-stopword terms."""
    words = [w.lower() for w in re.findall(r"\b[a-zA-Z]{3,}\b", text)]
    filtered = [w for w in words if w not in STOP_WORDS]
    return Counter(filtered).most_common(n)
