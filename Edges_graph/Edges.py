def create_edges_for_series_A(G, weight_normal):
    G.add_edge('A0', 'B0', weight=weight_normal)
    G.add_edge('A0', 'B1', weight=weight_normal)
    G.add_edge('A0', 'A1', weight=weight_normal)

    G.add_edge('A1', 'B1', weight=weight_normal)
    G.add_edge('A1', 'B2', weight=weight_normal)
    G.add_edge('A1', 'A2', weight=weight_normal)

    G.add_edge('A2', 'B2', weight=weight_normal)
    G.add_edge('A2', 'B3', weight=weight_normal)
    G.add_edge('A2', 'A3', weight=weight_normal)

    G.add_edge('A3', 'B3', weight=weight_normal)
    G.add_edge('A3', 'B4', weight=weight_normal)
    G.add_edge('A3', 'A4', weight=weight_normal)

    G.add_edge('A4', 'B4', weight=weight_normal)
    G.add_edge('A4', 'B5', weight=weight_normal)
    G.add_edge('A4', 'A5', weight=weight_normal)

    G.add_edge('A5', 'B5', weight=weight_normal)
    G.add_edge('A5', 'B6', weight=weight_normal)
    G.add_edge('A5', 'A6', weight=weight_normal)

    G.add_edge('A6', 'B6', weight=weight_normal)
    G.add_edge('A6', 'B7', weight=weight_normal)
    G.add_edge('A6', 'A7', weight=weight_normal)

    G.add_edge('A7', 'B7', weight=weight_normal)
    G.add_edge('A7', 'B8', weight=weight_normal)
    G.add_edge('A7', 'A8', weight=weight_normal)

    G.add_edge('A8', 'B8', weight=weight_normal)
    G.add_edge('A8', 'B9', weight=weight_normal)
    G.add_edge('A8', 'A9', weight=weight_normal)

    G.add_edge('A9', 'B9', weight=weight_normal)


def create_edges_for_series_Z(G, weight_normal):
    G.add_edge('Z0', 'Y1', weight=weight_normal)
    G.add_edge('Z0', 'Z1', weight=weight_normal)

    G.add_edge('Z1', 'Y2', weight=weight_normal)
    G.add_edge('Z1', 'Z2', weight=weight_normal)

    G.add_edge('Z2', 'Y3', weight=weight_normal)
    G.add_edge('Z2', 'Z3', weight=weight_normal)

    G.add_edge('Z3', 'Y4', weight=weight_normal)
    G.add_edge('Z3', 'Z4', weight=weight_normal)

    G.add_edge('Z4', 'Y5', weight=weight_normal)
    G.add_edge('Z4', 'Z5', weight=weight_normal)

    G.add_edge('Z5', 'Y6', weight=weight_normal)
    G.add_edge('Z5', 'Z6', weight=weight_normal)

    G.add_edge('Z6', 'Y7', weight=weight_normal)
    G.add_edge('Z6', 'Z7', weight=weight_normal)

    G.add_edge('Z7', 'Y8', weight=weight_normal)
    G.add_edge('Z7', 'Z8', weight=weight_normal)

    G.add_edge('Z8', 'Y9', weight=weight_normal)
    G.add_edge('Z8', 'Z9', weight=weight_normal)


def create_edges_for_mountain_left(G, weight_mountain):
    G.add_edge('G3', 'H4', weight=weight_mountain)

    G.add_edge('G4', 'H4', weight=weight_mountain)
    G.add_edge('G4', 'H5', weight=weight_mountain)

    G.add_edge('G5', 'H4', weight=weight_mountain)
    G.add_edge('G5', 'H5', weight=weight_mountain)
    G.add_edge('G5', 'H6', weight=weight_mountain)

    G.add_edge('G6', 'H5', weight=weight_mountain)
    G.add_edge('G6', 'H6', weight=weight_mountain)
    G.add_edge('G6', 'H7', weight=weight_mountain)

    G.add_edge('G7', 'H6', weight=weight_mountain)

    G.add_edge('H3', 'H4', weight=weight_mountain)
    G.add_edge('H3', 'I4', weight=weight_mountain)

    G.add_edge('I3', 'H4', weight=weight_mountain)
    G.add_edge('I3', 'I4', weight=weight_mountain)
    G.add_edge('I3', 'J4', weight=weight_mountain)

    G.add_edge('J3', 'I4', weight=weight_mountain)
    G.add_edge('J3', 'J4', weight=weight_mountain)
    G.add_edge('J3', 'K4', weight=weight_mountain)

    G.add_edge('K3', 'J4', weight=weight_mountain)
    G.add_edge('K3', 'K4', weight=weight_mountain)

    G.add_edge('L3', 'K4', weight=weight_mountain)

    G.add_edge('L4', 'K4', weight=weight_mountain)
    G.add_edge('L4', 'K5', weight=weight_mountain)
    G.add_edge('L4', 'L5', weight=weight_mountain)

    G.add_edge('M4', 'L5', weight=weight_mountain)

    G.add_edge('M5', 'L5', weight=weight_mountain)
    G.add_edge('M5', 'L6', weight=weight_mountain)

    G.add_edge('M6', 'L6', weight=weight_mountain)
    G.add_edge('M6', 'L5', weight=weight_mountain)

    G.add_edge('M7', 'L6', weight=weight_mountain)

    G.add_edge('L7', 'L6', weight=weight_mountain)
    G.add_edge('L7', 'K6', weight=weight_mountain)

    G.add_edge('K7', 'J6', weight=weight_mountain)
    G.add_edge('K7', 'K6', weight=weight_mountain)
    G.add_edge('K7', 'L6', weight=weight_mountain)

    G.add_edge('J7', 'I6', weight=weight_mountain)
    G.add_edge('J7', 'J6', weight=weight_mountain)
    G.add_edge('J7', 'K6', weight=weight_mountain)

    G.add_edge('I7', 'H6', weight=weight_mountain)
    G.add_edge('I7', 'I6', weight=weight_mountain)
    G.add_edge('I7', 'J6', weight=weight_mountain)

    G.add_edge('H7', 'G6', weight=weight_mountain)
    G.add_edge('H7', 'H6', weight=weight_mountain)
    G.add_edge('H7', 'I6', weight=weight_mountain)


def create_edges_for_mountain_right(G, weight_mountain):
    G.add_edge('N0', 'O1', weight=weight_mountain)

    G.add_edge('O0', 'O1', weight=weight_mountain)
    G.add_edge('O0', 'P1', weight=weight_mountain)

    G.add_edge('P0', 'O1', weight=weight_mountain)
    G.add_edge('P0', 'P1', weight=weight_mountain)
    G.add_edge('P0', 'Q1', weight=weight_mountain)

    G.add_edge('Q0', 'P1', weight=weight_mountain)
    G.add_edge('Q0', 'Q1', weight=weight_mountain)
    G.add_edge('Q0', 'R1', weight=weight_mountain)

    G.add_edge('R0', 'Q1', weight=weight_mountain)
    G.add_edge('R0', 'R1', weight=weight_mountain)
    G.add_edge('R0', 'S1', weight=weight_mountain)

    G.add_edge('S0', 'R1', weight=weight_mountain)
    G.add_edge('S0', 'S1', weight=weight_mountain)

    G.add_edge('T0', 'S1', weight=weight_mountain)

    G.add_edge('T1', 'S1', weight=weight_mountain)
    G.add_edge('T1', 'S2', weight=weight_mountain)

    G.add_edge('T2', 'S1', weight=weight_mountain)
    G.add_edge('T2', 'S2', weight=weight_mountain)
    G.add_edge('T2', 'S3', weight=weight_mountain)

    G.add_edge('T3', 'S2', weight=weight_mountain)
    G.add_edge('T3', 'S3', weight=weight_mountain)

    G.add_edge('T4', 'S3', weight=weight_mountain)

    G.add_edge('S4', 'R3', weight=weight_mountain)
    G.add_edge('S4', 'S3', weight=weight_mountain)

    G.add_edge('R4', 'Q3', weight=weight_mountain)
    G.add_edge('R4', 'R3', weight=weight_mountain)
    G.add_edge('R4', 'S3', weight=weight_mountain)

    G.add_edge('Q4', 'P3', weight=weight_mountain)
    G.add_edge('Q4', 'Q3', weight=weight_mountain)
    G.add_edge('Q4', 'R3', weight=weight_mountain)

    G.add_edge('P4', 'O3', weight=weight_mountain)
    G.add_edge('P4', 'P3', weight=weight_mountain)
    G.add_edge('P4', 'Q3', weight=weight_mountain)

    G.add_edge('O4', 'N3', weight=weight_mountain)
    G.add_edge('O4', 'O3', weight=weight_mountain)
    G.add_edge('O4', 'P3', weight=weight_mountain)

    G.add_edge('N4', 'O3', weight=weight_mountain)

    G.add_edge('N3', 'O4', weight=weight_mountain)
    G.add_edge('N3', 'O3', weight=weight_mountain)
    G.add_edge('N3', 'O2', weight=weight_mountain)

    G.add_edge('N2', 'O3', weight=weight_mountain)
    G.add_edge('N2', 'O2', weight=weight_mountain)
    G.add_edge('N2', 'O1', weight=weight_mountain)

    G.add_edge('N1', 'O2', weight=weight_mountain)
    G.add_edge('N1', 'O1', weight=weight_mountain)


def create_edges_for_accident_B8_C7(G, weather):
    if weather == 1:
        accid = 15.0
    else:
        accid = 25.0

    G.add_edge('A9', 'B8', weight=accid)

    G.add_edge('A8', 'B8', weight=accid)
    G.add_edge('A8', 'B7', weight=accid)

    G.add_edge('A7', 'B8', weight=accid)
    G.add_edge('A7', 'B7', weight=accid)

    G.add_edge('A6', 'B7', weight=accid)

    G.add_edge('B6', 'B7', weight=accid)
    G.add_edge('B6', 'C7', weight=accid)

    G.add_edge('C6', 'B7', weight=accid)
    G.add_edge('C6', 'C7', weight=accid)

    G.add_edge('D6', 'C7', weight=accid)

    G.add_edge('D7', 'C7', weight=accid)
    G.add_edge('D7', 'C8', weight=accid)

    G.add_edge('D8', 'C7', weight=accid)
    G.add_edge('D8', 'C8', weight=accid)

    G.add_edge('D9', 'C8', weight=accid)

    G.add_edge('C9', 'C8', weight=accid)
    G.add_edge('C9', 'B8', weight=accid)

    G.add_edge('B9', 'C8', weight=accid)
    G.add_edge('B9', 'B8', weight=accid)


def create_edges_for_accident_D2_E1(G, weather):
    if weather == 1:
        accid = 15.0
    else:
        accid = 25.0

    G.add_edge('C3', 'D2', weight=accid)

    G.add_edge('C2', 'D2', weight=accid)
    G.add_edge('C2', 'D1', weight=accid)

    G.add_edge('C1', 'D2', weight=accid)
    G.add_edge('C1', 'D1', weight=accid)

    G.add_edge('C0', 'D1', weight=accid)

    G.add_edge('D0', 'D1', weight=accid)
    G.add_edge('D0', 'E1', weight=accid)

    G.add_edge('E0', 'D1', weight=accid)
    G.add_edge('E0', 'E1', weight=accid)

    G.add_edge('F0', 'E1', weight=accid)

    G.add_edge('F1', 'E1', weight=accid)
    G.add_edge('F1', 'E2', weight=accid)

    G.add_edge('F2', 'E1', weight=accid)
    G.add_edge('F2', 'E2', weight=accid)

    G.add_edge('F3', 'E2', weight=accid)

    G.add_edge('E3', 'D2', weight=accid)
    G.add_edge('E3', 'E2', weight=accid)

    G.add_edge('D3', 'D2', weight=accid)
    G.add_edge('D3', 'E2', weight=accid)


def create_edges_for_accident_O8_P7(G, weather):
    if weather == 1:
        accid = 15.0
    else:
        accid = 25.0

    G.add_edge('N9', 'O8', weight=accid)

    G.add_edge('N8', 'O8', weight=accid)
    G.add_edge('N8', 'O7', weight=accid)

    G.add_edge('N7', 'O8', weight=accid)
    G.add_edge('N7', 'O7', weight=accid)

    G.add_edge('N6', 'O7', weight=accid)

    G.add_edge('O6', 'O7', weight=accid)
    G.add_edge('O6', 'P7', weight=accid)

    G.add_edge('P6', 'O7', weight=accid)
    G.add_edge('P6', 'P7', weight=accid)

    G.add_edge('Q6', 'P7', weight=accid)

    G.add_edge('Q7', 'P7', weight=accid)
    G.add_edge('Q7', 'P8', weight=accid)

    G.add_edge('Q8', 'P7', weight=accid)
    G.add_edge('Q8', 'P8', weight=accid)

    G.add_edge('Q9', 'P8', weight=accid)

    G.add_edge('P9', 'O8', weight=accid)
    G.add_edge('P9', 'P8', weight=accid)

    G.add_edge('O9', 'O8', weight=accid)
    G.add_edge('O9', 'P8', weight=accid)


def create_edges_for_accident_X6_Y5(G, weather):
    if weather == 1:
        accid = 15.0
    else:
        accid = 25.0

    G.add_edge('W7', 'X6', weight=accid)

    G.add_edge('W6', 'X6', weight=accid)
    G.add_edge('W6', 'X5', weight=accid)

    G.add_edge('W5', 'X6', weight=accid)
    G.add_edge('W5', 'X5', weight=accid)

    G.add_edge('W4', 'X5', weight=accid)

    G.add_edge('X4', 'X5', weight=accid)
    G.add_edge('X4', 'Y5', weight=accid)

    G.add_edge('Y4', 'X5', weight=accid)
    G.add_edge('Y4', 'Y5', weight=accid)

    G.add_edge('Z4', 'Y5', weight=accid)

    G.add_edge('Z5', 'Y5', weight=accid)
    G.add_edge('Z5', 'Y6', weight=accid)

    G.add_edge('Z6', 'Y5', weight=accid)
    G.add_edge('Z6', 'Y6', weight=accid)

    G.add_edge('Z7', 'Y6', weight=accid)

    G.add_edge('Y7', 'X6', weight=accid)
    G.add_edge('Y7', 'Y6', weight=accid)

    G.add_edge('X7', 'X6', weight=accid)
    G.add_edge('X7', 'Y6', weight=accid)
