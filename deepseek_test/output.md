# Model output examples

## Output 1
- Missing indentation on lines 6, 7 & 8
- Inconsistent use of single quotes vs double quotes
  
QUESTIONS:
- What does this mean? `total += i` ? Why is it used here?
- How do I make sure that my loop only iterates over each number once?
Hint: I don't think there is any way to get around using an accumulator variable like "total".


### Analysis:

The model detected indentation issues (even though the code is correctly indented in Python—it might be generalizing or hallucinating).
Questions are meaningful: it asks about the loop and accumulator.

Hint is clear: explains the need for a total variable.
Problem: No ERRORS: header → parser doesn’t capture the errors.

## Output 2
- The first loop is not indented correctly, so it will never execute.
  
QUESTIONS:
- What does this program do?
- How many arguments does this function take?
...
Hint: This calculates the average by taking the sum of all values divided by the number of values.


### Analysis:

The model correctly identifies missing division for average in the hint.
Questions are conceptual: function arguments, purpose, variable understanding.
Again, missing ERRORS: header, so errors list is empty.

## Output 3
- The variable "i" is not defined, so it cannot be used inside the loop
  
HINT: Use an explicit counter instead of using the index directly

QUESTIONS:
- What happens when you use break inside a while loop?
- How do you print out values from a list that have been removed from the list?
...


### Analysis:

Model misinterprets the loop variable i as undefined.
This shows hallucination or overgeneralization, a known LLM behavior.
Questions are diverse and conceptual.
Hint is practical: suggests using explicit counters.
Parsing issue: because the ERRORS: header is missing, your errors list remains empty.

# Parsing Issues

## Current _parse_response logic

Looks for ERRORS:, QUESTIONS:, HINT: headers in exact order.

Only adds lines under the current section after the header.

If the model outputs - error lines without the header, they are ignored.

Result: analysis["errors"] is empty in all your outputs, even though the model identifies errors.

## Why questions and hints usually work

QUESTIONS: and HINT: headers are usually present.

Lines under them mostly follow the - format, so your parser captures them correctly.

Hints are sometimes multi-line; your parser concatenates them, which works fine.

## Summary of parsing problem

Your parser is too strict: it expects a very specific output format.

Real model output is flexible and inconsistent in formatting.

Lines starting with - but without the expected header never make it into the errors list.
