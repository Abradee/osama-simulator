import pgzrun
import time

print("====DEBUG====\nYour game is in a different window.")

TITLE = "Osama Simulator"
WIDTH = 600
HEIGHT = 600
FPS = 1

# Game state
IsPlaying = False
GameOver = False
score = 0
score_timer = 0  # counts seconds

# Important stuff
PlayButton = Actor("playbutton")
PlayButton.pos = WIDTH / 2, HEIGHT / 2 + 60
Background2 = Actor("backdrop2")
Plane = Actor("plane")
Plane.pos = (50, HEIGHT // 2)

# Physics
plane_vel = 0
gravity = 0.5
plane_jump_strength = -8


# Draw everything
def draw():
    screen.fill((0, 0, 0))

    if not IsPlaying and not GameOver:
        # Title screen
        PlayButton.draw()
        screen.draw.text("Osama Simulator", pos=(175, 100), color="red", fontsize=36)
        screen.draw.text("Destroy the towers!", pos=(200, 80), color="red", fontsize=20)

    elif IsPlaying and not GameOver:
        # Game running
        Background2.draw()
        Plane.draw()
        screen.draw.text(f"Score: {score}", topleft=(10, 10), color="white", fontsize=30)

    elif GameOver:
        # Game over screen
        screen.draw.text("GAME OVER!", center=(WIDTH / 2, HEIGHT / 2 - 30), color="red", fontsize=60)
        screen.draw.text(f"Final Score: {score}", center=(WIDTH / 2, HEIGHT / 2 + 20), color="white", fontsize=40)
        screen.draw.text("Click to Restart", center=(WIDTH / 2, HEIGHT / 2 + 70), color="yellow", fontsize=30)


# Mouse click handler
def on_mouse_down(pos):
    global IsPlaying, GameOver, plane_vel, Plane, score, score_timer
    if not IsPlaying and not GameOver:
        # Start game
        if PlayButton.collidepoint(pos):
            print("[INFO] The game is started")
            IsPlaying = True
            score = 0
            score_timer = 0
            plane_vel = 0
            Plane.pos = (50, HEIGHT // 2)
    elif GameOver:
        # Restart game
        GameOver = False
        IsPlaying = True
        score = 0
        score_timer = 0
        plane_vel = 0
        Plane.pos = (50, HEIGHT // 2)


# Game loop
def update(dt):
    global plane_vel, GameOver, IsPlaying, score, score_timer

    if IsPlaying and not GameOver:
        # Gravity
        plane_vel += gravity
        Plane.y += plane_vel

        # Jump
        if keyboard.w:
            plane_vel = plane_jump_strength

        # Score system (increase 1 every second)
        score_timer += dt
        if score_timer >= 1.0:
            score += 1
            score_timer = 0

        # Death check (off screen)
        if Plane.y > HEIGHT or Plane.y < 0:
            GameOver = True
            IsPlaying = False
        
        

    if keyboard.escape:
        print("Quitting game. Goodbye!")
        quit()
    


pgzrun.go()
