from scramble_parser import scramble_to_moves
from cube import Cube
from cube import WHITE, YELLOW, GREEN, BLUE, ORANGE, RED



def solve_cross(cube: Cube):
    EDGES = {
        "UF": "",
        "UL": "U'",
        "UR": "U",
        "UB": "U2",
        "LB": "L U' L'",
        "LD": "L2 U'",
        "LF": "L' U' L",
        "RB": "R' U R",
        "RD": "R2 U",
        "RF": "R U R'",
        "DB": "B2 U2",
        "DF": "F2"
    }

    for colour in [BLUE, ORANGE, GREEN, RED]:
        for edge in EDGES:
            if (cube.get_edge_info(edge) == (colour, YELLOW)
                    or cube.get_edge_info(edge) == (YELLOW, colour)):
                cube._do_moves(scramble_to_moves(EDGES[edge]))

                if cube.get_edge_info("UF")[0] == YELLOW:
                    cube._do_moves(scramble_to_moves("F2"))
                else:
                    cube._do_moves(scramble_to_moves("R U' R' F"))

                cube._do_moves(scramble_to_moves("D'"))
                
                break

    cube._do_moves(scramble_to_moves("D2"))


def solve_corners(cube: Cube):
    CORNERS = {
        "UFR": "U2 U2",
        "DFR": "R U R' U'",
        "DBR": "R' U R U",
        "UBR": "R'",
        "UFL": "U'",
        "UBL": "U2",
        "DFL": "L' U' L",
        "DBL": "L U L' U" 
    }

    for colour1, colour2 in [(GREEN, RED), (BLUE, RED), (BLUE, ORANGE), (GREEN, ORANGE)]:
        for corner in CORNERS:
            cur_corner = cube.get_corner_info(corner)
            if (colour1 in cur_corner and colour2 in cur_corner and YELLOW in cur_corner):
                cube._do_moves(scramble_to_moves(CORNERS[corner]))
                cur_corner = cube.get_corner_info("UFR")
                if cur_corner[0] == YELLOW:
                    moves = scramble_to_moves("U R U2 R' U R U' R'")
                elif cur_corner[1] == YELLOW:
                    moves = scramble_to_moves("U R U' R'")
                elif cur_corner[2] == YELLOW:
                    moves = scramble_to_moves("R U R'")
                
                cube._do_moves(moves)
                cube._do_moves(scramble_to_moves("D'"))

                break

                
def solve_middle_edges(cube: Cube):
    EDGES = {
        "UF": "U2 U2",
        "UR": "U",
        "UL": "U'",
        "UB": "U2",
        "RF": "R' F R F' R U R' U'",
        "LF": "L F' L' F L' U' L U",
        "RB": "R' U R B' R B R'",
        "LB": "L U' L' B L' B' L"
    }

    for colour1, colour2 in [(GREEN, RED), (RED, BLUE), (BLUE, ORANGE), (ORANGE, GREEN)]:
        for edge in EDGES:
            cur_edge = cube.get_edge_info(edge)
            if (cur_edge == (colour1, colour2)
                    or cur_edge == (colour2, colour1)):
                cube._do_moves(scramble_to_moves(EDGES[edge]))
                cur_edge = cube.get_edge_info("UF")
                if cur_edge[1] == colour1:
                    moves = scramble_to_moves("U R U' R' F R' F' R")
                else:
                    moves = scramble_to_moves("U2 R' F R F' R U R'")
                cube._do_moves(moves)
                cube.y_rotate()

                break

def solve_oll(cube: Cube):
    for i in range(4):
        top_layer = [cube.faces["U"][0][1], cube.faces["U"][1][2], 
                     cube.faces["U"][2][1], cube.faces["U"][1][0]]
        eo_state = [face == WHITE for face in top_layer]

        if eo_state == [False, False, False, False]:
            cube._do_moves(scramble_to_moves("R U2 R2 F R F' U2 R' F R F'"))
            break
        elif eo_state == [False, False, True, True]:
            cube._do_moves(scramble_to_moves("R U2 R2 F R F' U2 R' F R F'"))
            break
        elif eo_state == [False, True, False, True]:
            cube._do_moves(scramble_to_moves("F R U R' U' F'"))
            break