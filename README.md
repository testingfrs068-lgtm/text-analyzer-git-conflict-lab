# Text Summarizer & Readability Analyzer

**Course:** UCS 745 Cloud and DevOps  
**Student:** Manvendra  
**GitHub:** https://github.com/testingfrs068-lgtm/text-analyzer-git-conflict-lab  

## Overview
A simple Python CLI tool that counts words/sentences, extracts top keywords, and generates short text summaries. Built for the UCS 745 Git & GitHub lab to demonstrate branching, merging, and resolving an intentional merge conflict.

## Summarization Logic
Updated in `feature/keyword-scoring`:
- Scores every sentence using the top 10 most frequent non-stopword terms.
- Picks the highest-scoring sentences and preserves their original order.

## How to Run
```bash
python3 main.py --demo
```
