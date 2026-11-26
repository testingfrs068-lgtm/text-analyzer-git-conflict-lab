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
    Generate an extractive summary combining both branches:
    1. Filter out very short sentences (< min_words) from feature/length-filter.
    2. Score remaining sentences using keyword frequencies from feature/keyword-scoring.
    """
    sentences = [s.strip() for s in re.split(r"(?<=[.!?])\s+", text.strip()) if s.strip()]
    if not sentences:
        return ""

    # Step 1: Length filtering (from feature/length-filter)
    candidates = [s for s in sentences if len(re.findall(r"\b\w+\b", s)) >= min_words]
    if not candidates:
        candidates = sentences

    # Step 2: Keyword frequency scoring (from feature/keyword-scoring)
    freq = dict(top_keywords(text, n=10))
    scored = []
    for idx, sent in enumerate(candidates):
        score = sum(freq.get(w.lower(), 0) for w in re.findall(r"\b[a-zA-Z]{3,}\b", sent))
        scored.append((score, idx, sent))

    top = sorted(sorted(scored, key=lambda x: (-x[0], x[1]))[:max_sentences], key=lambda x: x[1])
    return " ".join(s[2] for s in top)


def top_keywords(text: str, n: int = 5) -> list:
    """Return the top n most frequent non-stopword terms."""
    words = [w.lower() for w in re.findall(r"\b[a-zA-Z]{3,}\b", text)]
    filtered = [w for w in words if w not in STOP_WORDS]
    return Counter(filtered).most_common(n)
