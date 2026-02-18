# Day 14 - Async Scraper (Agent)
# Learning goal: Master asyncio.gather(), httpx, and file I/O with async
# Date: Feb 2026
# Status: Working ✅

# 1. Scope: Scrape Patient IDs 1 to 100.
# 2. Concurrency: Use a Semaphore of 10. (Don't DDOS the hospital).
# 3. Resilience:
#   - Retry on 500 Errors (Max 3 tries).
#   - Timeout if a request takes > 3 seconds (Use wait_for).
# 4. Parsing: Extract the Name and Condition from the HTML.
# 5. Output: Save the successful results to a file named patients.csv (Format: ID, Name, Condition).

# Hints:
# - Mix day11_retries.py (Retries) and day12_timeout.py (Timeouts).
# - Use BeautifulSoup inside your fetch function after getting the text.
# - Collect all results in main(), filter out the failures (None), and then write to the file.
