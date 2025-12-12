# Elevator Management System Project Report

## File Structure
We have two elevators, `A` and `B`, for the hotel. The lowest floor of the hotel is `X` and the highest is `Y`. We consider the following sets:

- `H = { -X, -Y+1, …, Y-1 }`
- `A` is the set of floors for elevator `A`, and `B` is the set of floors for elevator `B`.
- `A` and `B` form a partition of `H`, meaning they have no common elements, and their union equals `H`.

---

## Elevator Prioritization System
1. Initially, the elevator is in an **idle** state and positioned at an initial floor.
2. If a request is made from a higher floor, the elevator's direction becomes **upward**; otherwise, it becomes **downward**.
3. If the direction is **upward**, the elevator moves up as long as there are requests above its current floor. It stops at each requested floor, prioritizing the **closest floor above** the current position, and removes that floor from the request list.
4. If, at a stop, there are no more requests above the current floor but there are requests below, the elevator's direction changes to **downward**.
5. If the direction is **downward**, the rules defined in points 3 and 4 apply in reverse.

---

## Required Data Structures

### 1. **Array**
- Used to store all floors in ascending order.
- Each floor is represented as an object with two states: **requested** or **not requested**.

### 2. **Doubly Linked List**
- Since the order of floors is not predetermined and we have two separate sets, each set is stored in a doubly linked list in ascending order.
- As a result, we will have two doubly linked lists. The `Head` of each list holds the lowest floor of the respective set.

---

## Class Descriptions

### **Class Floor**
This class has four attributes:
- The first two attributes are self-explanatory (floor number and request status).
- The `before` and `after` attributes are used to link to the previous and next floors in the doubly linked list.

### **Class Elevator**
#### **Attributes**
- `move_direction`: The elevator's movement state (`IDLE`, `UP`, `DOWN`).
- `top_requests`: The number of requests **above** the current floor.
- `down_requests`: The number of requests **below** the current floor.

#### **Methods**
- **go_up / go_down**:
  - If the elevator is in the `IDLE` or `UP` state, it moves up one floor. Upon reaching a requested floor, the `top_requests` count decreases.
  - Otherwise, it returns a false value.
- **find_floor**:
  - Takes a floor number as input and returns the corresponding floor object.
- **get_request**:
  - Sends a request to a specified floor of the elevator.
  - If the request is for a floor above the current one, `top_requests` is incremented.
  - If it is for a floor below, `down_requests` is incremented.
  - If the request is for the current floor, no action is taken.
  - If the elevator is in the `IDLE` state, this method determines the direction of movement.

---

## Main File (`main.py`)
1. First, floor objects and doubly linked lists are created.
2. Two elevator objects (`elev_A` and `elev_B`) are created, with their respective floor sets and initial floors specified.
3. The simulation runs in the terminal.
4. At each step, zero or more floor requests can be sent to each elevator independently.
5. Requested floor numbers must be entered on a single line, separated by **spaces**.
6. Requests entered further to the left are considered to have been sent earlier.
7. To send no request, simply press the `Enter` key.

---

**End of Report**
