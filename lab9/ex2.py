import pygame
import os
pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
FPS = 60
WHITE = (255, 255, 255)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Music Player")

music_directory = "music"
music_files = [f for f in os.listdir(music_directory) if f.endswith((".mp3", ".wav"))]
current_track_index = 0

clock = pygame.time.Clock()

font = pygame.font.Font(None, 36)

pygame.mixer.init()
pygame.mixer.music.load(os.path.join(music_directory, music_files[current_track_index]))

def play_next_track():
    global current_track_index
    current_track_index = (current_track_index + 1) % len(music_files)
    pygame.mixer.music.load(os.path.join(music_directory, music_files[current_track_index]))
    pygame.mixer.music.play()

def play_previous_track():
    global current_track_index
    current_track_index = (current_track_index - 1) % len(music_files)
    pygame.mixer.music.load(os.path.join(music_directory, music_files[current_track_index]))
    pygame.mixer.music.play()

running = True
music_playing = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if music_playing:
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()
                music_playing = not music_playing
            elif event.key == pygame.K_RIGHT:
                play_next_track()
            elif event.key == pygame.K_LEFT:
                play_previous_track()

    screen.fill(WHITE)

    current_track_text = font.render(f"Current Track: {music_files[current_track_index]}", True, (0, 0, 0))
    screen.blit(current_track_text, (10, 10))

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
