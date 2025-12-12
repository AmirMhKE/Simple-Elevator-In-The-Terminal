# Elevator Management System - Specifications

## Project Structure
We have two elevators, `A` and `B`, for the hotel. The lowest floor is `X-` and the highest floor is `Y`. We consider the finite set:
`H = {-X, -X + 1, ..., Y - 1, Y}`.

We define two sets:
- **A**: The set of floors for elevator A.
- **B**: The set of floors for elevator B.

Sets `A` and `B` form a partition of `H`, meaning they have no common elements, and their union equals `H`, representing all hotel floors.

---

## Elevator Prioritization System
1. **Initial State**: The elevator is idle and positioned at an initial floor.
2. **Direction Determination**: If a request originates from a higher floor, the elevator's direction is set to **UP**; otherwise, it is set to **DOWN**.
3. **Upward Movement**: When moving **UP**, the elevator continues upward as long as there are requests above its current floor. It stops at each requested floor (removing it from the request list), always prioritizing the **closest floor above** the current position.
4. **Direction Change (Up to Down)**: If, at a stop, there are no more requests above but there are requests below, the elevator's direction changes to **DOWN**.
5. **Downward Movement**: When moving **DOWN**, the rules defined in points 3 and 4 apply in reverse.

---

## Required Data Structures

### 1. Array
*   **Purpose**: Stores all floors in ascending order.
*   **Implementation**: Each floor is represented as an object with a state indicating whether it has been requested or not.

### 2. Doubly Linked List
*   **Purpose**: Manages the specific floor sets for each elevator.
*   **Reasoning**: Since the floor order isn't predetermined and we have two separate sets (`A` and `B`), each set is stored in its own Doubly Linked List in ascending order.
*   **Structure**: We will have two Doubly Linked Lists. The `Head` of each list points to the lowest floor in its respective set.

---

## Code Explanation

### 1. Class `Floor`
This class has four attributes:
*   The first two are self-explanatory (e.g., floor number, request status).
*   The `before` and `next` attributes store references to the previous and next floors, effectively implementing the node structure for the Doubly Linked List.

### 2. Class `Elevator`

#### **Attributes**
*   `move_direction`: Stores the current state: `IDLE`, `UP`, or `DOWN`.
*   `top_requests`: Counts the number of pending requests **above** the current floor.
*   `down_requests`: Counts the number of pending requests **below** the current floor.

#### **Methods**
*   **`go_up` / `go_down`**:
    *   `go_up`: If the elevator is `IDLE` or moving `UP`, it moves up one floor. Upon reaching a requested floor, `top_requests` is decremented. Otherwise, returns `False`.
    *   `go_down`: Functions analogously for downward movement, decrementing `down_requests`.
*   **`find_floor`**:
    *   Takes a floor number as input and returns the corresponding `Floor` object.
*   **`get_request`**:
    *   Sends a request to a specified floor.
    *   If the requested floor is above the current one, increments `top_requests`.
    *   If below, increments `down_requests`.
    *   If the request is for the current floor, no action is taken.
    *   If the elevator is `IDLE`, this method also determines the initial direction (`UP` or `DOWN`).

---

## Main Program (`main.py`)
1.  **Initialization**: `Floor` objects and their corresponding Doubly Linked Lists are created.
2.  **Elevator Creation**: Two elevator objects, `elev_A` and `elev_B`, are instantiated. Their assigned floor sets and initial positions are specified.
3.  **Terminal Simulation**: The elevators are simulated in the terminal.
4.  **Request Input**:
    *   For each elevator movement cycle, zero or more floor requests can be sent to each elevator independently.
    *   Requested floor numbers must be entered on a single line, separated by spaces.
    *   Requests are processed in left-to-right order (the leftmost request is considered the earliest).
5.  **Skipping Requests**: To send no requests for a cycle, simply press `Enter`.
