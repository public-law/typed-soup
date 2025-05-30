"""
This type stub file was generated by pyright.
"""

from typing import Generator, Tuple
from urllib.parse import urljoin
from scrapy.exceptions import NotSupported
from scrapy.http.common import obsolete_setter
from scrapy.http.headers import Headers
from scrapy.http.request import Request
from scrapy.link import Link
from scrapy.utils.trackref import object_ref

"""
This module implements the Response class which is used to represent HTTP
responses in Scrapy.

See documentation in docs/topics/request-response.rst
"""
class Response(object_ref):
    """An object that represents an HTTP response, which is usually
    downloaded (by the Downloader) and fed to the Spiders for processing.
    """
    attributes: Tuple[str, ...] = ...
    def __init__(self, url: str, status=..., headers=..., body=..., flags=..., request=..., certificate=..., ip_address=..., protocol=...) -> None:
        ...
    
    @property
    def cb_kwargs(self):
        ...
    
    @property
    def meta(self):
        ...
    
    url = ...
    body = ...
    def __repr__(self): # -> str:
        ...
    
    def copy(self):
        """Return a copy of this Response"""
        ...
    
    def replace(self, *args, **kwargs):
        """Create a new Response with the same attributes except for those given new values"""
        ...
    
    def urljoin(self, url): # -> Any:
        """Join this Response's url with a possible relative url to form an
        absolute interpretation of the latter."""
        ...
    
    @property
    def text(self):
        """For subclasses of TextResponse, this will return the body
        as str
        """
        ...
    
    def css(self, *a, **kw):
        """Shortcut method implemented only by responses whose content
        is text (subclasses of TextResponse).
        """
        ...
    
    def jmespath(self, *a, **kw):
        """Shortcut method implemented only by responses whose content
        is text (subclasses of TextResponse).
        """
        ...
    
    def xpath(self, *a, **kw):
        """Shortcut method implemented only by responses whose content
        is text (subclasses of TextResponse).
        """
        ...
    
    def follow(self, url, callback=..., method=..., headers=..., body=..., cookies=..., meta=..., encoding=..., priority=..., dont_filter=..., errback=..., cb_kwargs=..., flags=...) -> Request:
        """
        Return a :class:`~.Request` instance to follow a link ``url``.
        It accepts the same arguments as ``Request.__init__`` method,
        but ``url`` can be a relative URL or a ``scrapy.link.Link`` object,
        not only an absolute URL.

        :class:`~.TextResponse` provides a :meth:`~.TextResponse.follow`
        method which supports selectors in addition to absolute/relative URLs
        and Link objects.

        .. versionadded:: 2.0
           The *flags* parameter.
        """
        ...
    
    def follow_all(self, urls, callback=..., method=..., headers=..., body=..., cookies=..., meta=..., encoding=..., priority=..., dont_filter=..., errback=..., cb_kwargs=..., flags=...) -> Generator[Request, None, None]:
        """
        .. versionadded:: 2.0

        Return an iterable of :class:`~.Request` instances to follow all links
        in ``urls``. It accepts the same arguments as ``Request.__init__`` method,
        but elements of ``urls`` can be relative URLs or :class:`~scrapy.link.Link` objects,
        not only absolute URLs.

        :class:`~.TextResponse` provides a :meth:`~.TextResponse.follow_all`
        method which supports selectors in addition to absolute/relative URLs
        and Link objects.
        """
        ...
    


