class Smartphone:
    def __init__(self, memory):
        self.memory = memory
        self.apps = []
        self.is_on = False

    def power(self):
        if self.is_on:
            self.is_on = False
        else:
            self.is_on = True

    def install(self, app, app_memory):
        if self.is_on and self.memory >= app_memory:
            self.memory -= app_memory
            self.apps.append(app)
            return f"Installing {app}"
        elif self.is_on and self.memory < app_memory:
            return f"Not enough memory to install {app}"
        return f"Turn on your phone to install {app}"

    def status(self):
        return f"Total apps: {len(self.apps)}. Memory left: {self.memory}"

