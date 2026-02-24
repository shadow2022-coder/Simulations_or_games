from raylib import *

# 1. Initialization
InitWindow(800, 450, b"Raylib Python Example")
SetTargetFPS(60)

# 2. The Main Game Loop
while not WindowShouldClose():
    # Update logic goes here (e.g., move a character)
    
    # 3. Rendering
    BeginDrawing()
    ClearBackground(RAYWHITE)
    
    DrawText(b"Congrats! You created your first window!", 190, 200, 20, LIGHTGRAY)
    
    EndDrawing()

# 4. Cleanup
CloseWindow()