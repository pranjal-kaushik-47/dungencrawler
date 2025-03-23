import heapq
import random
from collections import deque

from ..database.items import spawn_items  # type: ignore


class Cell:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.walls = {'N': True, 'E': True, 'S': True, 'W': True}
        self.visited = False
        self.properties = {}
        self.symbol = ' '  # Default symbol
        
    def __lt__(self, other):
        # For priority queue comparisons
        return False
        
    def set_symbol(self, symbol):
        self.symbol = symbol
        
    def is_perimeter(self, width, height):
        return self.x == 0 or self.x == width - 1 or self.y == 0 or self.y == height - 1
        
    def get_perimeter_wall(self, width, height):
        if self.x == 0:
            return 'W'
        if self.x == width - 1:
            return 'E'
        if self.y == 0:
            return 'N'
        if self.y == height - 1:
            return 'S'
        return None

class Maze:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        level_spawned_items = spawn_items(random.randint(3, 15))

        # TODO: Distribute all the spawned items across the maze .. update the properties accordingly of the Cell 
        self.grid = [[Cell(x, y) for y in range(height)] for x in range(width)]
        self.start = None
        self.end = None
        
    def get_cell(self, x, y):
        if 0 <= x < self.width and 0 <= y < self.height:
            return self.grid[x][y]
        return None
        
    def get_neighbors(self, cell):
        neighbors = []
        directions = {'N': (0, -1), 'E': (1, 0), 'S': (0, 1), 'W': (-1, 0)}
        
        for direction, (dx, dy) in directions.items():
            nx, ny = cell.x + dx, cell.y + dy
            neighbor = self.get_cell(nx, ny)
            if neighbor:
                neighbors.append((direction, neighbor))
                
        return neighbors
        
    def remove_wall(self, cell1, cell2):
        # Determine direction from cell1 to cell2
        dx = cell2.x - cell1.x
        dy = cell2.y - cell1.y
        
        if dx == 1:  # cell2 is to the east of cell1
            cell1.walls['E'] = False
            cell2.walls['W'] = False
        elif dx == -1:  # cell2 is to the west of cell1
            cell1.walls['W'] = False
            cell2.walls['E'] = False
        elif dy == 1:  # cell2 is to the south of cell1
            cell1.walls['S'] = False
            cell2.walls['N'] = False
        elif dy == -1:  # cell2 is to the north of cell1
            cell1.walls['N'] = False
            cell2.walls['S'] = False
    
    def generate_maze(self):
        # Reset all cells
        for x in range(self.width):
            for y in range(self.height):
                self.grid[x][y] = Cell(x, y)
                
        # Pick a random starting cell
        start_cell = self.grid[random.randint(0, self.width - 1)][random.randint(0, self.height - 1)]
        start_cell.visited = True
        
        # Stack for backtracking
        stack = [start_cell]
        
        while stack:
            current = stack[-1]
            
            # Get unvisited neighbors
            unvisited_neighbors = []
            for direction, neighbor in self.get_neighbors(current):
                if not neighbor.visited:
                    unvisited_neighbors.append((direction, neighbor))
            
            if unvisited_neighbors:
                # Choose a random neighbor
                direction, next_cell = random.choice(unvisited_neighbors)
                
                # Remove the wall between current and next
                self.remove_wall(current, next_cell)
                
                # Mark the next cell as visited and add it to the stack
                next_cell.visited = True
                stack.append(next_cell)
            else:
                # Backtrack
                stack.pop()
                
        # Create start and end points on the perimeter
        self.create_start_end_points()
        
    def create_start_end_points(self):
        # Get all perimeter cells
        perimeter_cells = []
        for x in range(self.width):
            for y in range(self.height):
                cell = self.grid[x][y]
                if cell.is_perimeter(self.width, self.height):
                    perimeter_cells.append(cell)
        
        # Ensure we have at least two perimeter cells
        if len(perimeter_cells) < 2:
            raise ValueError("Maze is too small to create start and end points on perimeter")
            
        # Shuffle to randomize
        random.shuffle(perimeter_cells)
        
        # Create potential start points and verify they have a path out
        valid_start_points = []
        for cell in perimeter_cells:
            # Check if there's an internal path from this cell
            wall_to_remove = cell.get_perimeter_wall(self.width, self.height)
            
            # Get the neighbor in the direction opposite to the wall
            opposite_directions = {'N': 'S', 'E': 'W', 'S': 'N', 'W': 'E'}
            opposite_dir = opposite_directions[wall_to_remove]
            directions = {'N': (0, -1), 'E': (1, 0), 'S': (0, 1), 'W': (-1, 0)}
            dx, dy = directions[opposite_dir]
            
            neighbor_x, neighbor_y = cell.x + dx, cell.y + dy
            neighbor = self.get_cell(neighbor_x, neighbor_y)
            
            # Check if the neighbor exists and if there's no wall between them
            if neighbor and not cell.walls[opposite_dir]:
                valid_start_points.append(cell)
        
        # If no valid start points found, we need to modify the maze
        if not valid_start_points:
            # Pick a random perimeter cell and ensure it has a path out
            start_cell = random.choice(perimeter_cells)
            wall_to_remove = start_cell.get_perimeter_wall(self.width, self.height)
            opposite_dir = opposite_directions[wall_to_remove]
            dx, dy = directions[opposite_dir]
            
            neighbor_x, neighbor_y = start_cell.x + dx, start_cell.y + dy
            neighbor = self.get_cell(neighbor_x, neighbor_y)
            
            if neighbor:
                start_cell.walls[opposite_dir] = False
                neighbor.walls[wall_to_remove] = False
                valid_start_points.append(start_cell)
        
        # Set start cell
        self.start = random.choice(valid_start_points)
        self.start.set_symbol('S')
        
        # Remove the start from consideration for end point
        if self.start in perimeter_cells:
            perimeter_cells.remove(self.start)
        
        # Find valid end points that are solvable from the start
        valid_end_points = []
        for end_cell in perimeter_cells:
            # Test if there's a path from start to this end
            if self.is_solvable(self.start, end_cell):
                valid_end_points.append(end_cell)
        
        # If no valid end points, modify the maze to create one
        if not valid_end_points:
            # Pick a cell far from start
            perimeter_cells.sort(key=lambda c: abs(c.x - self.start.x) + abs(c.y - self.start.y), reverse=True)
            
            for potential_end in perimeter_cells:
                # Modify the maze to ensure a path
                if self.create_path_to(self.start, potential_end):
                    valid_end_points.append(potential_end)
                    break
        
        # Set end cell
        if valid_end_points:
            self.end = random.choice(valid_end_points)
        else:
            # If we still can't find a valid end, just pick a perimeter cell
            self.end = random.choice(perimeter_cells)
            # And ensure there's a path to it
            self.create_path_to(self.start, self.end)
        
        self.end.set_symbol('E')
        
        # Open the exterior walls for start and end
        start_wall = self.start.get_perimeter_wall(self.width, self.height)
        end_wall = self.end.get_perimeter_wall(self.width, self.height)
        
        if start_wall:
            self.start.walls[start_wall] = False
        if end_wall:
            self.end.walls[end_wall] = False
    
    def is_solvable(self, start_cell, end_cell):
        # Use BFS to check if there's a path from start to end
        queue = deque([start_cell])
        visited = set([(start_cell.x, start_cell.y)])
        
        while queue:
            current = queue.popleft()
            
            if current == end_cell:
                return True
                
            for direction, neighbor in self.get_valid_moves(current):
                if (neighbor.x, neighbor.y) not in visited:
                    visited.add((neighbor.x, neighbor.y))
                    queue.append(neighbor)
        
        return False
    
    def get_valid_moves(self, cell):
        valid_moves = []
        directions = {'N': (0, -1), 'E': (1, 0), 'S': (0, 1), 'W': (-1, 0)}
        
        for direction, (dx, dy) in directions.items():
            if not cell.walls[direction]:  # If there's no wall in this direction
                nx, ny = cell.x + dx, cell.y + dy
                neighbor = self.get_cell(nx, ny)
                if neighbor:
                    valid_moves.append((direction, neighbor))
        
        return valid_moves

    
    def heuristic(self, cell1, cell2):
        # Manhattan distance heuristic
        return abs(cell1.x - cell2.x) + abs(cell1.y - cell2.y)
    
    def reconstruct_path(self, came_from, current):
        total_path = [current]
        while (current.x, current.y) in came_from:
            current, _ = came_from[(current.x, current.y)]
            total_path.append(current)
        
        return list(reversed(total_path))
    
    def break_walls_along_path(self, path):
        for i in range(len(path) - 1):
            current = path[i]
            next_cell = path[i + 1]
            self.remove_wall(current, next_cell)
    
    
    def print_maze_with_symbols(self):
        # Print top border
        print(' ' + '_' * (self.width * 2 - 1))
        
        for y in range(self.height):
            print('|', end='')
            
            # Print the cells in this row
            for x in range(self.width):
                cell = self.grid[x][y]
                
                # Print cell symbol or south wall (floor)
                if cell.symbol != ' ':
                    print(cell.symbol, end='')
                elif cell.walls['S']:
                    print('_', end='')
                else:
                    print(' ', end='')
                
                # Print east wall
                if x == self.width - 1:
                    print('|', end='')
                elif cell.walls['E']:
                    print('|', end='')
                else:
                    print(' ', end='')
            
            print()  # New line
    
    
    def print_solution(self):
        path = self.solve_maze()
        if not path:
            return
            
        # Set path cells to '.'
        for cell in path:
            if cell != self.start and cell != self.end:
                cell.set_symbol('.')
                
        self.print_maze_with_symbols()
        
        # Reset path cells
        for cell in path:
            if cell != self.start and cell != self.end:
                cell.set_symbol(' ')

# Example usage
def main():
    # Create a maze with dimensions 10x10
    maze = Maze(15, 15)
    
    # Generate the maze
    maze.generate_maze()
    
    # Print the maze
    print("Generated Maze:")
    maze.print_maze_with_symbols()    

if __name__ == "__main__":
    main()