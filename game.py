from settings import Setting

class Game:
    def __init__(self) -> None:
        super(Game, self).__init__()
    # 游戏界面尺寸
    SCREEN_SIZE = SCREEN_WIDTH, SCREEN_HEIGHT = (480,640)
    # 背景颜色
    BG_COLOR = Setting.GRAY
    # 手牌数量上限
    D_MAX = 7
    # 目标分数
    TARGET_SCORE = 100