# exercism-python
My solutions for [Exercism Python Track](https://exercism.org/tracks/python).
Feel free to open issues for questions, comments, or suggestions.

[![](https://github.com/asarkar/exercism-python/workflows/CI/badge.svg)](https://github.com/asarkar/exercism-python/actions)

## Development

```
% $(brew --prefix python)/bin/python3 -m venv ./venv

% ./venv/bin/python -m pip install --upgrade pip '.[test]' '.[lint]'
```

To remove the local copy of the package `pydata`:
```
% ./venv/bin/python -m pip uninstall -y pydata
```

## Running tests
```
./.github/run.sh <directory>
```

## Timing code
```
palindrome_product% ../venv/bin/python -m timeit \
    -s "from palindrome_products import largest" \
    "largest(min_factor=100, max_factor=999)"   
```

## License

Released under [Apache License v2.0](LICENSE).