class Frame(list[int]):
    def score(self) -> int:
        return sum(self)

    def is_complete(self) -> bool:
        return len(self) == 2 or self.score() == 10


class BowlingGame:
    def __init__(self) -> None:
        self.frames: list[Frame] = []

    def roll(self, pins: int) -> None:
        if self.__is_complete():
            raise ValueError("game is complete")
        if pins < 0:
            raise ValueError("invalid pins")

        if not self.frames or self.frames[-1].is_complete():
            frame = Frame()
        else:
            frame = self.frames.pop()

        if frame.score() + pins > 10:
            raise ValueError("not enough pins left")

        frame.append(pins)
        self.frames.append(frame)

    def score(self) -> int:
        if not self.__is_complete():
            raise ValueError("game is not complete")

        score = 0
        for i, f in enumerate(self.frames[:10]):
            if f.score() == 10 and len(f) == 1:
                s = sum([t for fr in self.frames[i + 1 :] for t in fr][:2])
            elif f.score() == 10:
                s = self.frames[i + 1][0]
            else:
                s = 0

            score += f.score() + s

        return score

    def __is_complete(self) -> bool:
        num_frames = len(self.frames)
        if num_frames < 10:
            return False
        tenth_frame_throws = len(self.frames[9])
        tenth_frame_score = self.frames[9].score()
        if num_frames == 10:
            return tenth_frame_throws == 2 and tenth_frame_score < 10
        if num_frames == 11:
            return tenth_frame_throws + len(self.frames[10]) == 3
        return True
