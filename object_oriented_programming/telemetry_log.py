class Sensor:
    def __init__(self, sensor_id, hw_revision):
        self.sensor_id = sensor_id
        self.hw_revision = hw_revision


class WiredSensor(Sensor):
    def __init__(self, sensor_id, hw_revision):
        super().__init__(sensor_id, hw_revision)
        self.error_count = 0
        self.total_count = 0
        self.step_counter = 0

    def send_data(self, data):
        self.step_counter += 1
        checksum = sum(map(ord, str(data))) % 256
        if self.step_counter % 10 == 0:
            checksum += 1
            self.error_count += 1
        self.total_count += 1
        return data, checksum

    def get_error_rate(self):
        if self.total_count == 0:
            return 0
        return 100 * self.error_count / self.total_count


class WirelessSensor(Sensor):
    def __init__(self, sensor_id, hw_revision, loss_rate_step=5):
        super().__init__(sensor_id, hw_revision)
        self.loss_rate_step = loss_rate_step
        self.step_counter = 0
        self.total_count = 0
        self.loss_count = 0

    def send_data(self, data):
        self.step_counter += 1
        self.total_count += 1
        if self.step_counter % self.loss_rate_step == 0:
            self.loss_count += 1
            return None
        return data

    def get_error_rate(self):
        if self.total_count == 0:
            return 0
        return 100 * self.loss_count / self.total_count


class GPS(WiredSensor):
    def __init__(self, sensor_id, hw_revision):
        super().__init__(sensor_id, hw_revision)
        self.x = 0.0
        self.y = 0.0

    def read_data(self):
        self.x += 0.1
        self.y += 0.05
        data = {"x": round(self.x, 2), "y": round(self.y, 2)}
        return self.send_data(data)


class Steering(WiredSensor):
    def __init__(self, sensor_id, hw_revision):
        super().__init__(sensor_id, hw_revision)
        self.angle = 0.0
        self.turn_rate = 0.0

    def read_data(self):
        self.angle += 3
        self.turn_rate = (self.turn_rate + 0.1) % 1
        data = {"angle": self.angle, "turn_rate": round(self.turn_rate, 2)}
        return self.send_data(data)


class Temperature(WirelessSensor):
    def __init__(self, sensor_id, hw_revision):
        super().__init__(sensor_id, hw_revision, loss_rate_step=6)
        self.inside = 20.0
        self.outside = 15.0

    def read_data(self):
        self.inside += 0.2
        self.outside += 0.15
        data = {"inside": round(self.inside, 1), "outside": round(self.outside, 1)}
        return self.send_data(data)


class Humidity(WirelessSensor):
    def __init__(self, sensor_id, hw_revision):
        super().__init__(sensor_id, hw_revision, loss_rate_step=4)
        for i in range(1, 11):
            self.v_table = [round(0.1 * i, 1)]
        self.voltage = 0.1

    def read_data(self):
        self.voltage += 0.1
        if self.voltage > 1.0:
            self.voltage = 0.1
        closest = min(self.v_table, key=lambda v: abs(v - self.voltage))
        index = self.v_table.index(closest)
        humidity_percent = int((index + 1) / len(self.v_table) * 100)
        data = {"humidity": f"{humidity_percent}%", "V": round(self.voltage, 2)}
        return self.send_data(data)


class BatterySensor(WirelessSensor):
    def __init__(self, sensor_id, hw_revision):
        super().__init__(sensor_id, hw_revision, loss_rate_step=8)
        self.voltage = 12.5

    def read_data(self):
        self.voltage -= 0.05
        if self.voltage < 10:
            self.voltage = 12.5
        battery_percent = int((self.voltage - 10) / 2.5 * 100)
        data = {"voltage": round(self.voltage, 2), "percent": battery_percent}
        return self.send_data(data)


class TelemetryPacket:
    def __init__(self, timestamp, packet_id):
        self.timestamp = timestamp
        self.packet_id = packet_id
        self.data = {}

    def add_data(self, sensor, data):
        self.data[f"{sensor.__class__.__name__}<{hex(sensor.sensor_id)}, {sensor.hw_revision}>"] = data

    def __repr__(self):
        return f"Packet {self.packet_id} @ {self.timestamp}:\n{self.data}\n"


class TelemetryLog:
    def __init__(self):
        self.packets = []

    def add_packet(self, packet):
        self.packets.append(packet)

    def query_interval(self, start_ts, end_ts):
        for p in self.packets:
            if start_ts <= p.timestamp <= end_ts:
                print(p)

    def error_rate_by_hw(self, hw_rev):
        found = False
        for s in all_sensors:
            if s.hw_revision == hw_rev:
                found = True
                print(f"{s.__class__.__name__}<{s.hw_revision}>: {s.get_error_rate():.2f}% грешки")
        if not found:
            print("Няма сензори с такава ревизия.")

    def point_in_polygon(self, x, y):
        gps_points = [
            (p.data[k]["x"], p.data[k]["y"])
            for p in self.packets
            for k in p.data if k.startswith("GPS")
        ]
        if len(gps_points) < 3:
            return False
        inside = False
        j = len(gps_points) - 1
        for i in range(len(gps_points)):
            xi, yi = gps_points[i]
            xj, yj = gps_points[j]
            if ((yi > y) != (yj > y)) and (x < (xj - xi) * (y - yi) / (yj - yi + 1e-9) + xi):
                inside = not inside
            j = i
        return inside


def simulate(steps):
    log = TelemetryLog()
    for step in range(steps):
        packet = TelemetryPacket(timestamp=step, packet_id=step)
        for sensor in all_sensors:
            data = sensor.read_data()
            if isinstance(sensor, WiredSensor):
                data, checksum = data
                data["checksum"] = checksum
            if data:
                packet.add_data(sensor, data)
        log.add_packet(packet)
    return log


steps = int(input("Моля въведете брой стъпки: "))

gps = GPS(0x10, "HW_1")
steering = Steering(0x11, "HW_1")
humidity = Humidity(0x12, "HW_1")
temperature = Temperature(0x13, "HW_2")
battery = BatterySensor(0x14, "HW_3")

all_sensors = [gps, steering, humidity, temperature, battery]

telemetry_log = simulate(steps)

while True:
    user_input = input().strip().split()
    if not user_input:
        continue
    if user_input[0] == "I" and len(user_input) == 3:
        telemetry_log.query_interval(int(user_input[1]), int(user_input[2]))
    elif user_input[0] == "H" and len(user_input) == 2:
        telemetry_log.error_rate_by_hw(user_input[1])
    elif user_input[0] == "P" and len(user_input) == 3:
        x, y = float(user_input[1]), float(user_input[2])
        print(telemetry_log.point_in_polygon(x, y))
    elif user_input[0] == "Q":
        break
    else:
        print("Възможни команди: I, H, P, Q")
