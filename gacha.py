import json
import random
import os

class Gacha:
    def __init__(self, json_file):
        self.json_file = json_file
        self.counts = {
            "total": 0,
            "rare": 0,
            "common": 0
        }
        self.load_counts()

    def load_counts(self):
        if os.path.exists(self.json_file):
            try:
                with open(self.json_file, 'r', encoding='utf-8') as f:
                    self.counts = json.load(f)
            except (json.JSONDecodeError, IOError):
                # 読み込みエラーの場合は初期化
                self.counts = {"total": 0, "rare": 0, "common": 0}

    def save_counts(self):
        with open(self.json_file, 'w', encoding='utf-8') as f:
            json.dump(self.counts, f, ensure_ascii=False, indent=2)

    def play(self):
        self.counts["total"] += 1
        # 例: 10%の確率でレア、それ以外はコモン
        if random.random() < 0.1:
            self.counts["rare"] += 1
            result = "レア"
        else:
            self.counts["common"] += 1
            result = "コモン"
        self.save_counts()
        return result

if __name__ == "__main__":
    json_file = "gacha_counts.json"
    gacha = Gacha(json_file)
    result = gacha.play()
    print(f"ガチャの結果: {result}")
    print("現在のカウント：", gacha.counts)
