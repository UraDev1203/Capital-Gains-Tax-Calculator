import sys
import json

def calculate_weighted_average(current_avg, current_qty, new_price, new_qty):
    """Calculate weighted average price for new stock purchase."""
    if current_qty == 0:
        return new_price
    return round((current_qty * current_avg + new_qty * new_price) / (current_qty + new_qty), 2)

def process_operation(operation, state):
    """Process a single operation and return tax amount."""
    if operation["operation"] == "buy":
        state["total_quantity"] += operation["quantity"]
        state["weighted_avg"] = calculate_weighted_average(
            state["weighted_avg"],
            state["total_quantity"] - operation["quantity"],
            operation["unit-cost"],
            operation["quantity"]
        )
        return {"tax": 0.0}
    
    # Handle sell operation
    total_amount = operation["unit-cost"] * operation["quantity"]
    profit = (operation["unit-cost"] - state["weighted_avg"]) * operation["quantity"]
    
    # Update state
    state["total_quantity"] -= operation["quantity"]
    
    # No tax if total amount <= 20000 or if there's a loss
    if total_amount <= 20000 or profit <= 0:
        state["accumulated_loss"] += max(0, -profit)
        return {"tax": 0.0}
    
    # Apply accumulated losses
    taxable_profit = max(0, profit - state["accumulated_loss"])
    state["accumulated_loss"] = max(0, state["accumulated_loss"] - profit)
    
    # Calculate tax (20% of taxable profit)
    tax = round(taxable_profit * 0.2, 2)
    return {"tax": tax}

def process_simulation(operations):
    """Process a single simulation (one line of input)."""
    state = {
        "total_quantity": 0,
        "weighted_avg": 0.0,
        "accumulated_loss": 0.0
    }
    return [process_operation(op, state) for op in operations]

def main():
    """Read input from stdin and process simulations."""
    for line in sys.stdin:
        line = line.strip()
        if not line:  # Stop at blank line
            break
        operations = json.loads(line)
        result = process_simulation(operations)
        print(json.dumps(result))

if __name__ == "__main__":
    main()