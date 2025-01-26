
# Pong Game 🎮

This is a classic Pong game developed in Python using the `turtle` module for graphics and `pygame` for sound effects. It's a two-player game where players control paddles to bounce the ball and score points.

## Features ✨
- Smooth animations with the `turtle` module.
- Sound effects using the `pygame` library:
  - Ball bounce sound.
  - Point scored sound.
- A dashed line dividing the screen for better gameplay visibility.
- Custom background image support.

## Gameplay Instructions 🕹️
1. Player 1 (Left Paddle):
   - **Move Up**: Press `W`
   - **Move Down**: Press `S`
2. Player 2 (Right Paddle):
   - **Move Up**: Press `Up Arrow`
   - **Move Down**: Press `Down Arrow`

The objective is to score points by making the ball pass the opponent’s paddle. The first player to score the most points wins.

## How to Run the Game 🛠️
1. **Install Python**: Ensure Python 3.x is installed on your system.  
   You can download it from [python.org](https://www.python.org/).
2. **Install Pygame**: Install the `pygame` library for sound effects.
   ```bash
   pip install pygame
   ```
3. **Clone the Repository**: Clone or download the source code.
   ```bash
   git clone https://github.com/username/pong-game.git
   ```
4. **Organize the Files**: Ensure the following directory structure:
   ```
   Pong/
   ├── main.py
   ├── paddle.py
   ├── ball.py
   ├── scoreboard.py
   ├── bg_resized.png         # Custom background image
   ├── bounce.mp3             # Ball bounce sound
   ├── point_scored.mp3       # Point scored sound
   ```
5. **Run the Game**: Navigate to the project directory and execute the game.
   ```bash
   python main.py
   ```

## Requirements 📋
- Python 3.x
- Pygame library

## File Structure 📁
- `main.py`: Main game loop and logic.
- `paddle.py`: Paddle class for controlling the paddles.
- `ball.py`: Ball class for movement and collision logic.
- `scoreboard.py`: Scoreboard class for managing and displaying scores.
- `bg_resized.png`: Background image for the game.
- `bounce.mp3`: Sound effect for ball bounces.
- `point_scored.mp3`: Sound effect for scoring points.

## Customization 🖌️
- **Background Image**: Replace `bg_resized.png` with your own image.
- **Sound Effects**: Replace `bounce.mp3` and `point_scored.mp3` with your preferred sounds.
- **Paddle and Ball Colors**: Modify the `color()` method in `paddle.py` and `ball.py`.

## Future Improvements 🛠️
- Add difficulty levels (e.g., increasing ball speed as the game progresses).
- Introduce a single-player mode with AI.
- Add a start menu and game-over screen.

## Acknowledgments ❤️
This project was built as part of a personal Python learning journey. Thanks to the Python and Pygame communities for their amazing resources!

## License 📜
This project is open-source and available under the MIT License.
```

Feel free to modify it according to your preferences or additional details you’d like to include!
