def convert(input_grid: list[str]) -> str:
    if len(input_grid) % 4 != 0:
        raise ValueError('Number of input lines is not a multiple of four')
    chunks = (__parse(input_grid[i: i + 4]) for i in range(0, len(input_grid), 4))
    return ','.join(chunks)


NUMS = [[' _ ',
         '| |',
         '|_|',
         '   '
         ],
        ['   ',
         '  |',
         '  |',
         '   '
         ],
        [' _ ',
         ' _|',
         '|_ ',
         '   '
         ],
        [' _ ',
         ' _|',
         ' _|',
         '   '
         ],
        ['   ',
         '|_|',
         '  |',
         '   '
         ],
        [' _ ',
         '|_ ',
         ' _|',
         '   '
         ],
        [' _ ',
         '|_ ',
         '|_|',
         '   '
         ],
        [' _ ',
         '  |',
         '  |',
         '   '
         ],
        [' _ ',
         '|_|',
         '|_|',
         '   '
         ],
        [' _ ',
         '|_|',
         ' _|',
         '   '
         ]
        ]


def __parse(rows: list[str]) -> str:
    if not rows:
        return ''
    nums = []
    for start in range(0, len(rows[0]), 3):
        num = [r[start:start + 3] for r in rows if len(r) % 3 == 0]
        if len(num) != len(rows):
            raise ValueError('Number of input columns is not a multiple of three')
        n = next((str(i) for i, x in enumerate(NUMS) if x == num), '?')
        nums.append(n)

    return ''.join(nums)
