from raylib import *
class Vector2:
    def __init__(self,x,y):
        self.x = x
        self.y = y


# Define Car class
class Car:
    def __init__(self, x, y):
        self.position = Vector2(x, y)
        self.velocity = Vector2(0.0, 0.0)
        self.acceleration = 0.8
        self.friction = 0.95
        self.width = 40
        self.height = 20
        self.max_speed = 20.0

    def handle_input(self):
        """Handle arrow keys and WASD input"""
        # Arrow Keys
        if IsKeyDown(KEY_RIGHT):
            self.velocity.x += self.acceleration
        if IsKeyDown(KEY_LEFT):
            self.velocity.x -= self.acceleration
        if IsKeyDown(KEY_UP):
            self.velocity.y -= self.acceleration
        if IsKeyDown(KEY_DOWN):
            self.velocity.y += self.acceleration
        # WASD Keys
        if IsKeyDown(KEY_D):
            self.velocity.x += self.acceleration
        if IsKeyDown(KEY_A):
            self.velocity.x -= self.acceleration
        if IsKeyDown(KEY_W):
            self.velocity.y -= self.acceleration
        if IsKeyDown(KEY_S):
            self.velocity.y += self.acceleration

    def update(self):
        """Update physics"""
        # Apply friction (drag)
        self.velocity.x *= self.friction
        self.velocity.y *= self.friction
        # Update position
        self.position.x += self.velocity.x
        self.position.y += self.velocity.y
        # Screen boundaries
        if self.position.x < 0:
            self.position.x = 0
        if self.position.x > 800 - self.width:
            self.position.x = 800 - self.width
        if self.position.y < 0:
            self.position.y = 0
        if self.position.y > 450 - self.height:
            self.position.y = 450 - self.height

    def draw(self):
        """Draw the car on screen"""
        # Draw car body
        DrawRectangle(int(self.position.x), int(self.position.y), self.width, self.height, RED)
        # Draw car outline
        DrawRectangleLines(int(self.position.x), int(self.position.y), self.width, self.height, BLUE)
        # Draw direction indicator (small circle at front)
        DrawCircle(int(self.position.x + self.width), int(self.position.y + self.height // 2), 5, YELLOW)

# Initialize window
InitWindow(800, 450, b"Raylib Python Example")
SetTargetFPS(60)

# Create car
car = Car(375.0, 210.0)

# Main loop
while not WindowShouldClose():
    # Handle input
    car.handle_input()
    # Update physics
    car.update()
    # Drawing
    BeginDrawing()
    ClearBackground(DARKGRAY)
    # Draw road
    DrawRectangle(0, 200, 800, 50, LIGHTGRAY)
    # Draw road lines
    for x in range(0, 800, 50):
        DrawRectangle(x, 220, 30, 5, YELLOW)
    # Draw car
    car.draw()
    # Draw instructions - FIXED: All strings converted to bytes
    DrawText(b"Use ARROW KEYS or WASD to move", 10, 10, 20, WHITE)
    DrawText(f"Speed X: {car.velocity.x:.2f} px/s".encode(), 10, 40, 16, GREEN)
    DrawText(f"Speed Y: {car.velocity.y:.2f} px/s".encode(), 10, 65, 16, GREEN)
    DrawText(f"Position: ({car.position.x:.1f}, {car.position.y:.1f})".encode(), 10, 90, 16, YELLOW)
    EndDrawing()

CloseWindow()