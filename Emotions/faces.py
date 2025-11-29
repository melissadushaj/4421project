from Config.settings import FACE_COLS, FACE_ROWS

def _blank_face():
    return [[0 for _ in range(FACE_COLS)] for _ in range(FACE_ROWS)]


def _center():
    mid_y = FACE_ROWS // 2
    mid_x = FACE_COLS // 2
    return mid_x, mid_y


def happy_face():
    face = _blank_face()
    mid_x, mid_y = _center()

    # Eyes
    face[mid_y - 3][mid_x - 5] = 1
    face[mid_y - 3][mid_x + 5] = 1
    face[mid_y - 2][mid_x - 5] = 1
    face[mid_y - 2][mid_x + 5] = 1

    # Smile
    for dx in range(-4, 5):
        face[mid_y + 3][mid_x + dx] = 1
    face[mid_y + 2][mid_x - 3] = 1
    face[mid_y + 2][mid_x + 3] = 1

    return face


def sad_face():
    face = _blank_face()
    mid_x, mid_y = _center()

    # Eyes
    face[mid_y - 3][mid_x - 5] = 1
    face[mid_y - 3][mid_x + 5] = 1

    # Sad mouth (curving down)
    for dx in range(-4, 5):
        face[mid_y + 4][mid_x + dx] = 1
    face[mid_y + 5][mid_x - 3] = 1
    face[mid_y + 5][mid_x + 3] = 1

    return face


def surprised_face():
    face = _blank_face()
    mid_x, mid_y = _center()

    # Big round eyes
    for dy in (-3, -2):
        face[mid_y + dy][mid_x - 5] = 1
        face[mid_y + dy][mid_x + 5] = 1

    # "O" mouth
    mouth_y = mid_y + 2
    face[mouth_y][mid_x] = 1
    face[mouth_y - 1][mid_x] = 1
    face[mouth_y][mid_x - 1] = 1
    face[mouth_y][mid_x + 1] = 1
    face[mouth_y + 1][mid_x] = 1

    return face


def empathetic_face():
    face = _blank_face()
    mid_x, mid_y = _center()

    # Soft eyes (slightly tilted)
    face[mid_y - 3][mid_x - 5] = 1
    face[mid_y - 2][mid_x - 4] = 1
    face[mid_y - 3][mid_x + 5] = 1
    face[mid_y - 2][mid_x + 4] = 1

    # Gentle smile
    for dx in range(-3, 4):
        face[mid_y + 3][mid_x + dx] = 1
    face[mid_y + 2][mid_x - 2] = 1
    face[mid_y + 2][mid_x + 2] = 1

    return face


def confused_face():
    face = _blank_face()
    mid_x, mid_y = _center()

    # One raised eyebrow
    face[mid_y - 4][mid_x - 6] = 1
    face[mid_y - 4][mid_x - 5] = 1
    face[mid_y - 4][mid_x - 4] = 1

    # Eyes
    face[mid_y - 3][mid_x - 5] = 1
    face[mid_y - 3][mid_x + 5] = 1

    # Tilted mouth
    for dx in range(-3, 4):
        face[mid_y + 3][mid_x + dx + (dx // 3)] = 1

    return face


EMOTION_FACES = {
    "happy": happy_face,
    "sad": sad_face,
    "surprised": surprised_face,
    "empathetic": empathetic_face,
    "confused": confused_face,
}
