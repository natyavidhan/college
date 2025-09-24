import pygame
import sys
import time

pygame.init()

WIDTH, HEIGHT = 600, 600
BOARD_SIZE = 8
SQUARE_SIZE = WIDTH // BOARD_SIZE
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
DARK_GRAY = (100, 100, 100)
GOLD = (255, 215, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('8 Queens Visualization')
clock = pygame.time.Clock()

queen_img = pygame.transform.scale(
    pygame.image.load('queen.png') if pygame.image.get_extended() else pygame.Surface((SQUARE_SIZE - 10, SQUARE_SIZE - 10)), 
    (SQUARE_SIZE - 10, SQUARE_SIZE - 10)
)

board = [[0 for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]

delay = 0.001
paused = False
completed = False
solutions_count = 0
current_attempt = {"row": 0, "col": 0}
backtracking = False
solution_found = False

def draw_board():
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            color = WHITE if (row + col) % 2 == 0 else GRAY
            pygame.draw.rect(screen, color, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
            
            if row == current_attempt["row"] and col == current_attempt["col"]:
                pygame.draw.rect(screen, GOLD, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE), 3)
                
            if board[row][col] == 1:
                if pygame.image.get_extended():
                    screen.blit(queen_img, (col * SQUARE_SIZE + 5, row * SQUARE_SIZE + 5))
                else:
                    pygame.draw.circle(screen, BLACK, 
                                      (col * SQUARE_SIZE + SQUARE_SIZE // 2, 
                                       row * SQUARE_SIZE + SQUARE_SIZE // 2), 
                                      SQUARE_SIZE // 3)

def draw_info():
    font = pygame.font.SysFont('Arial', 20)
    status = "Paused" if paused else "Running"
    if completed:
        status = "Completed"
    elif solution_found:
        status = "Solution Found! Press SPACE to continue"
        
    pygame.draw.rect(screen, DARK_GRAY, (0, 0, WIDTH, 30))
    
    text = font.render(f"Status: {status} | Solutions: {solutions_count} | Speed: {delay:.2f}s", True, WHITE)
    screen.blit(text, (10, 5))
    
    pygame.draw.rect(screen, DARK_GRAY, (0, HEIGHT - 30, WIDTH, 30))
    instructions = font.render("Space: Pause/Resume | Up/Down: Speed | R: Reset | Q: Quit", True, WHITE)
    screen.blit(instructions, (10, HEIGHT - 25))

def is_safe(board, row, col):
    for i in range(col):
        if board[row][i] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, len(board)), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def reset():
    global board, completed, solutions_count, current_attempt, backtracking, solution_found
    board = [[0 for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
    completed = False
    solutions_count = 0
    current_attempt = {"row": 0, "col": 0}
    backtracking = False
    solution_found = False

def solve_step():
    global board, solutions_count, current_attempt, completed, backtracking, solution_found, paused
    
    if current_attempt["col"] >= BOARD_SIZE:
        solutions_count += 1
        solution_found = True
        paused = True
        backtracking = True
        current_attempt["col"] -= 1
        return
    
    if backtracking:
        queen_found = False
        for r in range(BOARD_SIZE):
            if board[r][current_attempt["col"]] == 1:
                board[r][current_attempt["col"]] = 0
                current_attempt["row"] = r + 1
                queen_found = True
                break
        
        if queen_found and current_attempt["row"] < BOARD_SIZE:
            backtracking = False
            return
        
        if current_attempt["col"] > 0:
            current_attempt["col"] -= 1
        else:
            completed = True
        return
    
    if current_attempt["row"] < BOARD_SIZE:
        if is_safe(board, current_attempt["row"], current_attempt["col"]):
            board[current_attempt["row"]][current_attempt["col"]] = 1
            current_attempt["col"] += 1
            current_attempt["row"] = 0
        else:
            current_attempt["row"] += 1
    else:
        backtracking = True
        if current_attempt["col"] > 0:
            current_attempt["col"] -= 1
        else:
            completed = True

def main():
    global delay, paused, completed, solution_found
    
    last_step_time = time.time()
    
    running = True
    while running:
        current_time = time.time()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if solution_found:
                        solution_found = False
                        paused = False
                    else:
                        paused = not paused
                elif event.key == pygame.K_UP:
                    delay = max(0.01, delay / 1.5)
                elif event.key == pygame.K_DOWN:
                    delay = min(2.0, delay * 1.5)
                elif event.key == pygame.K_r:
                    reset()
                elif event.key == pygame.K_q:
                    running = False
        
        if not paused and not completed and current_time - last_step_time > delay:
            solve_step()
            last_step_time = current_time
        
        screen.fill(WHITE)
        draw_board()
        draw_info()
        pygame.display.flip()
        
        clock.tick(60)
    
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
