from datetime import datetime
from typing import NamedTuple

COL_WIDTHS = [10, 25, 13]
HEADERS = {"en_US": ["Date", "Description", "Change"], "nl_NL": ["Datum", "Omschrijving", "Verandering"]}
CURRENCY_SYMBOLS = {"USD": "$", "EUR": "€"}


# Subclassing NamedTuple comes with total ordering for free.
class LedgerEntry(NamedTuple):
    date: datetime
    desc: str
    change: int

    # Can't set locale because it's not recognized on Exercism.
    #   locale.setlocale(locale.LC_ALL, loc)
    #   col1 = self.date.strftime("%x")
    def _fmt_date(self, locale: str) -> str:
        fmt_str = "%m/%d/%Y" if locale == "en_US" else "%d-%m-%Y"
        return f"{self.date.strftime(fmt_str): <{COL_WIDTHS[0]}}"

    # Can't use 'textwrap.shorten' because it is aware of word-breaking,
    # but the tests aren't.
    def _fmt_desc(self) -> str:
        s = self.desc
        if len(s) > COL_WIDTHS[1]:
            s = f"{self.desc[:COL_WIDTHS[1] - 3]}..."
        return f"{s: <{COL_WIDTHS[1]}}"

    def _fmt_change(self, currency: str, locale: str) -> str:
        x = f"{abs(self.change) / 100:.2f}"
        dot_idx = len(x) - 3
        # Group the whole portion of change in chunks of 3 from the end.
        # 1234 is grouped is [1, 234].
        whole = [x[max(0, i - 3) : i] for i in range(dot_idx, 0, -3)][::-1]
        grp_sep, dec_sep = (",", ".") if locale == "en_US" else (".", ",")
        x = f"{grp_sep.join(whole)}{dec_sep}{x[-2:]}"
        symbol = CURRENCY_SYMBOLS[currency]
        match locale:
            case "en_US":
                if self.change < 0:
                    x = f"({symbol}{x})"
                else:
                    x = f"{symbol}{x} "
            case "nl_NL":
                if self.change < 0:
                    x = "-" + x
                x = f"{symbol} {x} "
        return f"{x: >{COL_WIDTHS[2]}}"

    def fmt(self, currency: str, locale: str) -> str:
        return " | ".join([self._fmt_date(locale), self._fmt_desc(), self._fmt_change(currency, locale)])


def create_entry(date: str, description: str, change: int) -> LedgerEntry:
    return LedgerEntry(datetime.strptime(date, "%Y-%m-%d"), description, change)


def format_entries(currency: str, locale: str, entries: list[LedgerEntry]) -> str:
    # The space in {0: <5} is the [fill] , the < is [align], and 5 is [width].
    header = [f"{col: <{width}}" for col, width in zip(HEADERS[locale], COL_WIDTHS)]
    table = [" | ".join(header)]
    entries.sort()
    for e in entries:
        table.append(e.fmt(currency, locale))
    return "\n".join(table)
