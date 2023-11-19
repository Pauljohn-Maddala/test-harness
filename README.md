# Project 1: Test Harness

## Personal Information
- Name: Paul John Maddala
- Stevens Login: pmaddala@stevens.edu

## Repository URL
https://github.com/Pauljohn-Maddala/test-harness.git

## Time Spent
Approximately 16 hours spent on this project.

## Testing Approach
I have implemented a test harness in `test.py` that automates the testing process. This harness reads `.in` input files and compares the program's output to the expected `.out` files. Tests were written to cover a range of scenarios, including edge cases for error handling and standard usage.

## Known Bugs/Issues
- No issues are currently running; the utility functions as expected.

## Difficult Issues and Resolutions
- I encountered an issue where `gron.py` was incorrectly interpreting a JSON structure as a filename. After a thorough review, I resolved the problem by adjusting the test harness to distinguish when to provide the JSON data directly via STDIN and when to treat the input as a file argument.

## Implemented Extensions
- Command-Line Flags for wc.py: The utility supports flags to selectively count lines, words, or characters.
- Error Handling in gron.py: The utility handles JSON parsing errors gracefully, providing meaningful error messages.
- Pattern Matching in file_finder.py: The utility includes a feature to search files matching a specific pattern.

## How You Will Be Graded
Your grade will be based on the following criteria:
- 30% Baseline behavior of your programs.
- 30% Thoroughness and accuracy of your `README.md`.
- 30% Implementation and demonstration of the chosen extensions (10% each).
- 10% Your Continuous Integration setup running all tests and showing a green build at the time of submission.
