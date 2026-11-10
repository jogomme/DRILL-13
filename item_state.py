selected_ball = 1


def select_ball(selection):
    global selected_ball
    if selection not in (0, 1, 2):
        raise ValueError(f'Unsupported ball selection: {selection}')
    selected_ball = selection
