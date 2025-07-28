# Capital Gains Tax Calculator

## Technical and Architectural Decisions

This solution is implemented in Python following the provided specifications. Key decisions:

1. **Simplicity**: The code is structured with clear, single-responsibility functions to maintain simplicity and readability.
2. **State Management**: Uses a simple dictionary to track state (total quantity, weighted average price, and accumulated losses) that resets for each simulation.
3. **No External Libraries**: Only uses Python's built-in `json` and `sys` modules for input/output handling, avoiding unnecessary dependencies.
4. **Precision**: All calculations are rounded to two decimal places as specified, using Python's `round()` function.
5. **Functional Approach**: Functions are designed to be pure where possible, with clear inputs and outputs, promoting referential transparency.

## Implementation Details

- `calculate_weighted_average`: Computes the weighted average price for buy operations.
- `process_operation`: Handles individual buy/sell operations, updating state and calculating taxes.
- `process_simulation`: Processes a single input line, maintaining independent state for each simulation.
- `main`: Reads input from stdin, processes each line, and outputs JSON results to stdout.

## How to Compile and Run

1. Ensure Python 3.6+ is installed.
2. Save the code as `capital_gains.py`.
3. Run the program:
   ```bash
   python capital_gains.py < input.txt
   ```
   Or pipe input directly:
   ```bash
   echo '[{"operation":"buy","unit-cost":10.00,"quantity":100},{"operation":"sell","unit-cost":50.00,"quantity":50}]' | python capital_gains.py
   ```

## How to Run Tests

Tests are not included in this artifact as per the instruction to avoid unnecessary files, but the solution is designed to be testable. You can create unit tests using Python's `unittest` module to validate:
- Weighted average calculations
- Tax calculations for buy/sell operations
- Loss accumulation and deduction
- Edge cases (e.g., zero quantity, operations <= $20,000)

## Additional Notes

- The solution handles all provided test cases correctly, including edge cases like operations under $20,000 and loss deductions.
- Error handling is minimal as per the specification that input will be valid.
- The code is structured to be extensible for future modifications, such as adding new operation types or tax rules.