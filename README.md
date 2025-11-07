# typed-soup

A type-safe wrapper around BeautifulSoup and utilities for parsing HTML. Extracted from [Open-Gov Crawlers](https://github.com/public-law/open-gov-crawlers).

## Motivation

This is an example [from production code](https://github.com/public-law/open-gov-crawlers/blob/d7ad31081a88cec0e48bd51e06a4d0cc6039abec/public_law/parsers/gbr/cpr_glossary.py#L128-L143).

### Before

<p align="center">
  <img src="https://raw.githubusercontent.com/public-law/typed-soup/master/before.jpg" width="75%" alt="Before">
</p>

Here are the first five errors. There are 16 in total.

```
  error: Type of "rows" is partially unknown
    Type of "rows" is "list[PageElement | Tag | NavigableString] | Unknown" (reportUnknownVariableType)
  error: Type of "find_all" is partially unknown
    Type of "find_all" is "Unknown | ((name: str | bytes | Pattern[str] | bool | ((Tag) -> bool) | Iterable[str | bytes | Pattern[str] | bool | ((Tag) -> bool)] | ElementFilter | None = None, attrs: Dict[str, str | bytes | Pattern[str] | bool | ((str) -> bool) | Iterable[str | bytes | Pattern[str] | bool | ((str) -> bool)]] = {}, recursive: bool = True, string: str | bytes | Pattern[str] | bool | ((str) -> bool) | Iterable[str | bytes | Pattern[str] | bool | ((str) -> bool)] | None = None, limit: int | None = None, _stacklevel: int = 2, **kwargs: str | bytes | Pattern[str] | bool | ((str) -> bool) | Iterable[str | bytes | Pattern[str] | bool | ((str) -> bool)]) -> ResultSet[PageElement | Tag | NavigableString])" (reportUnknownMemberType)
  error: Cannot access attribute "find_all" for class "PageElement"
    Attribute "find_all" is unknown (reportAttributeAccessIssue)
  error: Cannot access attribute "find_all" for class "NavigableString"
    Attribute "find_all" is unknown (reportAttributeAccessIssue)
  error: Type of "row" is partially unknown
    Type of "row" is "PageElement | Tag | NavigableString | Unknown" (reportUnknownVariableType)
```

### After

Switching out `BeautifulSoup` for `TypedSoup` provides type knowledge to the checker and IDE:

<p align="center">
  <img src="https://raw.githubusercontent.com/public-law/typed-soup/refs/heads/master/after.jpg" width="75%" alt="After">
</p>

## Installation

```bash
pip install typed-soup
```

## Quick Start

```python
from typed_soup import TypedSoup
from bs4 import BeautifulSoup

# Create a type-safe soup object
soup = TypedSoup(BeautifulSoup("<div>Hello <span>World</span></div>", "html.parser"))

# Find elements with type safety
element = soup.find("span")
if element:
    print(element.get_text())  # Type-safe: IDE knows this returns str
```


## Usage

Wrap a `BeautifulSoup` object in `TypedSoup` to add type safety:

```python
from typed_soup import TypedSoup
from bs4 import BeautifulSoup

soup = TypedSoup(BeautifulSoup(html_content, "html.parser"))
```


## Supported Functions

I'm adding functions as I need them. If you have a request, please open an issue.
 These are the ones that I needed for [a dozen spiders](https://github.com/public-law/open-gov-crawlers):

- `find`
- `find_all`
- `__call__` (implicit find_all, e.g. `soup("p")` - standard BeautifulSoup API)
- `get_text`
- `children`
- `tag_name`
- `parent`
- `next_sibling`
- `get_content_after_element`
- `string`

And then these help create a `TypedSoup` object:

- `TypedSoup`

## Type Safety Benefits

- All methods return properly typed results
- No more `None` surprises - optional values are properly typed and described in the function signatures
- IDE autocomplete support for all methods
- Static type checking support with mypy/pyright
- Runtime type validation for BeautifulSoup results

## License

This project is licensed under the MIT License.
