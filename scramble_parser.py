from typing import List, Tuple


def scramble_to_moves(scramble: str) -> List[Tuple[int, bool, bool]]:
    moves = []

    for move in scramble.split():
        is_prime = "'" in move
        is_double = "2" in move
        moves.append((move[0], is_prime, is_double))

    return moves


def moves_to_scramble(moves: List[Tuple[int, bool, bool]]) -> str:
    scramble = []

    for move in moves:
        cur_move = move[0]
        
        if move[2]:
            cur_move += "2"
        elif move[1]:
            cur_move += "'"

        scramble.append(cur_move)
    
    return " ".join(scramble)


if __name__ == "__main__":
    scramble = "L U2 D B' R2 U2 F R B2 U2 R2 U R2 U2 F2 D R2 D F2"

    print(scramble_to_moves(scramble))