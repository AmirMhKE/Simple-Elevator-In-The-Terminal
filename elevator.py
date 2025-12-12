MOVE_DIRECTIONS = ("IDLE", "UP", "DOWN")

class Floor:
    def __init__(self, floor_num: int):
        self.floor_num = floor_num
        self.has_request = False
        self.before: Floor = None
        self.next: Floor = None

class Elevator:
    def __init__(self, elev_name: str, current_floor: int, floors: list[Floor]):
        self.name = elev_name
        self.current_floor: Floor = self.find_floor(current_floor, floors)
        self.move_direction = MOVE_DIRECTIONS[0]
        self.floors = floors
        self.top_requests = 0
        self.down_requests = 0

    def go_up(self) -> bool:
        if self.move_direction == MOVE_DIRECTIONS[1]:
            self.current_floor = self.current_floor.next
            if self.current_floor.has_request:
                self.current_floor.has_request = False
                self.top_requests -= 1
            if self.top_requests == 0:
                if self.down_requests == 0:
                    self.move_direction = MOVE_DIRECTIONS[0]
                else:
                    self.move_direction = MOVE_DIRECTIONS[2]
            return True
        return False

    def go_down(self) -> bool:
        if self.move_direction == MOVE_DIRECTIONS[2]:
            self.current_floor = self.current_floor.before
            if self.current_floor.has_request:
                self.current_floor.has_request = False
                self.down_requests -= 1
            if self.down_requests == 0:
                if self.top_requests == 0:
                    self.move_direction = MOVE_DIRECTIONS[0]
                else:
                    self.move_direction = MOVE_DIRECTIONS[1]
            return True
        return False
    
    def find_floor(self, floor_num: int, floors: list[Floor]) -> Floor:
        for floor in floors:
            if floor.floor_num == floor_num:
                return floor

    def get_request(self, req_floor: Floor):
        if req_floor.floor_num > self.current_floor.floor_num:
            if not req_floor.has_request:
                req_floor.has_request = True
                self.top_requests += 1
            if self.move_direction == MOVE_DIRECTIONS[0]:
                self.move_direction = MOVE_DIRECTIONS[1]
        elif req_floor.floor_num < self.current_floor.floor_num:
            if not req_floor.has_request:
                req_floor.has_request = True
                self.down_requests += 1
            if self.move_direction == MOVE_DIRECTIONS[0]:
                self.move_direction = MOVE_DIRECTIONS[2]

