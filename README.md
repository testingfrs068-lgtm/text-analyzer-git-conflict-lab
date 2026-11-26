# Text Summarizer & Readability Analyzer

**Course:** UCS 745 Cloud and DevOps  
**Student:** Manvendra  
**GitHub:** https://github.com/testingfrs068-lgtm/text-analyzer-git-conflict-lab  

## Overview
A simple Python CLI tool that counts words/sentences, extracts top keywords, and generates short text summaries. Built for the UCS 745 Git & GitHub lab to demonstrate branching, merging, and resolving an intentional merge conflict.

## Summarization Logic
Updated in `feature/length-filter`:
- Filters out short sentences with fewer than `min_words` (default 6 words).
- Falls back to all sentences if none meet the minimum length.

## How to Run
```bash
python3 main.py --demo
```
