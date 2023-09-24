# What the Bach-ish gibberish boils down to is this:
# Given a starting point (tonic), and a variable number of steps (intervals),
# map each position to a character in one of the scales.
# Treat the array as cyclic when the position is beyond it.
class Scale:
    SHARPS = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
    FLATS = ["C", "Db", "D", "Eb", "E", "F", "Gb", "G", "Ab", "A", "Bb", "B"]

    def __init__(self, tonic: str) -> None:
        self._tonic = tonic

    def chromatic(self) -> list[str]:
        # I've no idea how this follows from the question.
        return self.interval("m" * 11)

    def interval(self, intervals: str) -> list[str]:
        # Find the scale to use.
        match self._tonic:
            case "C" | "a" | "G" | "D" | "A" | "E" | "B" | "F#" | "e" | "b" | "f#" | "c#" | "g#" | "d#":
                chromatic_scale = Scale.SHARPS
            case "F" | "Bb" | "Eb" | "Ab" | "Db" | "Gb" | "d" | "g" | "c" | "f" | "bb" | "eb":
                chromatic_scale = Scale.FLATS
            case _:
                raise ValueError("invalid tonic")
        # Find the note corresponding to the tonic.
        pos = next(i for i, ch in enumerate(chromatic_scale) if ch.upper() == self._tonic.upper())
        notes = [chromatic_scale[pos]]
        # Translate each character in the interval to a step,
        # "half step" between two adjacent notes = 1,
        # "whole step" between two notes = 2,
        # "augmented second" is whole + half steps = 3
        for i in intervals:
            match i:
                case "m":
                    pos += 1
                case "M":
                    pos += 2
                case "A":
                    pos += 3
                case _:
                    raise ValueError("invalid interval")
            pos %= len(chromatic_scale)
            notes.append(chromatic_scale[pos])
        return notes
