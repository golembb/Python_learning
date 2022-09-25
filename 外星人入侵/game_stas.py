import pickle


class GameStats:  # 跟踪游戏的统计信息
    def __init__(self, ai_settings):
        self.ai_settings = ai_settings
        self.reset_stats()
        self.game_active = False

    def reset_stats(self):
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0  # 不在init中是因为每次重新开始游戏需要重置得分
        self.level = 1
        self.load_high_score()  # 退出游戏初始化后从本地读取最高得分

    def save_high_score(self):  # 保存最高得分到本地
        f = open('high_score.pkl', 'wb')
        pickle.dump(str(self.high_score), f, 0)
        f.close()

    def load_high_score(self):
        f = open('high_score.pkl', 'rb')
        try:
            str_high_score = pickle.load(f)
            self.high_score = int(str_high_score)
        except EOFError:
            self.high_score = 0
        finally:
            f.close()











