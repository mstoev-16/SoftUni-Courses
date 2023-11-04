class Time:
    max_hours = 23
    max_minutes = 59
    max_seconds = 59

    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def set_time(self, new_hours, new_minutes, new_seconds):
        self.hours = new_hours
        self.minutes = new_minutes
        self.seconds = new_seconds

    def get_time(self):
        return f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}"

    def next_second(self):
        total_time = 3600 * self.hours + 60 * self.minutes + self.seconds + 1
        calc_h = total_time // 3600
        total_time %= 3600
        calc_min = total_time // 60
        total_time %= 60
        calc_sec = total_time

        if calc_sec > Time.max_seconds:
            calc_sec %= Time.max_seconds
            calc_min += 1
        if calc_min > Time.max_minutes:
            calc_min %= Time.max_minutes
            calc_h += 1
        if calc_h > Time.max_hours:
            calc_h %= 24

        self.hours, self.minutes, self.seconds = calc_h, calc_min, calc_sec
        return Time.get_time(self)


time = Time(9, 30, 59)
print(time.next_second())

time = Time(10, 59, 59)
print(time.next_second())

time = Time(23, 59, 59)
print(time.next_second())