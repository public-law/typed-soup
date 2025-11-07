from typing import TypeVar, Optional, List, Any, Dict
from bs4 import BeautifulSoup, Tag

T = TypeVar('T')


class TypedSoup:
    """A type-safe wrapper around BeautifulSoup results."""

    def __init__(self, element: Tag | BeautifulSoup) -> None:  # type: ignore
        self._element = element

    def find(self,
             name: str,
             class_: Optional[str] = None,
             attrs: Optional[Dict[str, Any]] = None) -> 'TypedSoup | None':
        """Find a single element, returning None if not found or not a Tag."""
        # Build the attrs dict from class_ parameter if provided
        search_attrs = attrs or {}
        if class_ is not None:
            search_attrs["class"] = class_

        if search_attrs:
            result = self._element.find(name, attrs=search_attrs)
        else:
            result = self._element.find(name)

        if not result or not isinstance(result, Tag):
            return None
        return TypedSoup(result)

    def find_all(self,
                 name: str,
                 class_: Optional[str] = None,
                 attrs: Optional[Dict[str, Any]] = None) -> List['TypedSoup']:
        """Find all elements, filtering out non-Tag results."""
        # Build the attrs dict from class_ parameter if provided
        search_attrs = attrs or {}
        if class_ is not None:
            search_attrs["class"] = class_

        if search_attrs:
            results = self._element.find_all(name, attrs=search_attrs)
        else:
            results = self._element.find_all(name)

        return [TypedSoup(tag) for tag in results if isinstance(tag, Tag)]

    def get_text(self, strip: bool = True) -> str:
        """Get text content, guaranteed to be a string."""
        return self._element.get_text(strip=strip)

    def __bool__(self) -> bool:
        """Allow using the wrapper in boolean contexts."""
        return bool(self._element)

    def __call__(self, name: str, class_: Optional[str] = None, attrs: Optional[Dict[str, Any]] = None) -> List['TypedSoup']:
        """Allow using the wrapper as a callable to find all elements.

        This is a shorthand for find_all(), allowing syntax like:
        elements = soup("p")  # equivalent to soup.find_all("p")
        """
        return self.find_all(name, class_=class_, attrs=attrs)

    def children(self) -> list['TypedSoup']:
        return [
            TypedSoup(child) for child in self._element.children
            if isinstance(child, Tag)
        ]

    def tag_name(self) -> str | None:
        return self._element.name

    def parent(self) -> 'TypedSoup | None':
        parent = self._element.parent
        if isinstance(parent, Tag):
            return TypedSoup(parent)
        return None

    def next_sibling(self) -> 'TypedSoup | None':
        sibling = self._element.next_sibling
        if isinstance(sibling, Tag):
            return TypedSoup(sibling)
        return None

    def get_content_after_element(self) -> str:
        """Get all content (as HTML string) after this element within its parent."""
        if not self._element.parent:
            return ""

        # Get all siblings after this element
        siblings: List[str] = []
        for sibling in self._element.next_siblings:
            siblings.append(str(sibling))

        return "".join(siblings)

    @property
    def string(self) -> str | None:
        """Get the string content of the element (similar to BeautifulSoup's .string)."""
        return self._element.string
