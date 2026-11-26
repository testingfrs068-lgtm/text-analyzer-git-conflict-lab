# Text Summarizer & Readability Analyzer

**Course:** UCS 745 Cloud and DevOps  
**Student:** Manvendra  
**GitHub:** https://github.com/testingfrs068-lgtm/text-analyzer-git-conflict-lab  

## Overview
A simple Python CLI tool that counts words/sentences, extracts top keywords, and generates short text summaries. Built for the UCS 745 Git & GitHub lab to demonstrate branching, merging, and resolving an intentional merge conflict.

## Summarization Logic (Merged)
Combines both feature branches after resolving the merge conflict:
- Filters out short sentences with fewer than `min_words` (default 6 words) (`feature/length-filter`).
- Scores the remaining sentences using the top 10 most frequent keywords and preserves original order (`feature/keyword-scoring`).

## How to Run
```bash
python3 main.py --demo
```
