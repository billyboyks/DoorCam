# movement_tracking_module.py

from collections import defaultdict

class MovementTrackingModule:
    def __init__(self, zone_a_coords, zone_b_coords):
        self.zone_a_coords = zone_a_coords
        self.zone_b_coords = zone_b_coords
        self.previous_positions = defaultdict(lambda: None)

    def update_positions(self, face_locations, face_names):
        events = []
        for (top, right, bottom, left), name in zip(face_locations, face_names):
            center_x = (left + right) // 2
            center_y = (top + bottom) // 2
            current_position = (center_x, center_y)

            previous_position = self.previous_positions[name]
            if previous_position:
                movement_event = self.check_movement(name, previous_position, current_position)
                if movement_event:
                    events.append(movement_event)

            self.previous_positions[name] = current_position
        return events

    def check_movement(self, name, prev_pos, curr_pos):
        prev_zone = self.get_zone(prev_pos)
        curr_zone = self.get_zone(curr_pos)

        if prev_zone == 'Zone A' and curr_zone == 'Zone B':
            return {'name': name, 'event': 'entered'}
        elif prev_zone == 'Zone B' and curr_zone == 'Zone A':
            return {'name': name, 'event': 'exited'}
        else:
            return None

    def get_zone(self, position):
        x, y = position
        if self.is_in_zone(position, self.zone_a_coords):
            return 'Zone A'
        elif self.is_in_zone(position, self.zone_b_coords):
            return 'Zone B'
        else:
            return 'Unknown'

    def is_in_zone(self, position, zone_coords):
        x, y = position
        (x1, y1), (x2, y2) = zone_coords
        return x1 <= x <= x2 and y1 <= y <= y2
