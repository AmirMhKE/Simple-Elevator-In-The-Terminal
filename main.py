from elevator import *

FLOORS_A = [-10, -8, -7, -6, -3, -1, 0, 2, 5, 7, 8, 11, 12, 17, 20, 22, 24, 25, 28, 29]
FLOORS_B = [-9, -5, -4, -2, 1, 3, 4, 6, 9, 10, 13, 14, 15, 16, 18, 19, 21, 26, 27, 30]
INIT_FLOOR_A = 0
INIT_FLOOR_B = 1

def init_floors():
    for fls in (FLOORS_A, FLOORS_B):
        for i in range(len(fls)):
            fls[i] = Floor(fls[i])
        for i in range(len(fls) - 1):
            fls[i].next = fls[i + 1]
            fls[i + 1].before = fls[i]

def run_elev():
    elev = None
    init_floors()
    elev_A = Elevator('A', INIT_FLOOR_A, FLOORS_A)
    elev_B = Elevator('B', INIT_FLOOR_B, FLOORS_B)

    while True:
        print("Elevator A ->", "Current Floor:", elev_A.current_floor.floor_num, "***",
              "Current Direction:", elev_A.move_direction, "***", "Request Count:", (elev_A.down_requests + elev_A.top_requests))
        print("Elevator B ->", "Current Floor:", elev_B.current_floor.floor_num, "***",
              "Current Direction:", elev_B.move_direction, "***", "Request Count:", (elev_B.down_requests + elev_B.top_requests))

        for elev in (elev_A, elev_B):
            print(f"Floors {elev.name} ->", end=" ")
            for floor in elev.floors:
                print(floor.floor_num, end=" ")
            print()
            
            requests = list(map(int, input(f"Enter your floors in elevator {elev.name}: ").split()))
            for req_num in requests:
                floor = elev.find_floor(req_num, elev.floors)
                if floor:
                    elev.get_request(floor)

            if not elev.go_up():
                elev.go_down()
        print("=====================================")

if __name__ == "__main__":
    run_elev()
