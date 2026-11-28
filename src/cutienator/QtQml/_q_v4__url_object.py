"""
QV4::UrlObject binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qv4urlobject_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QV4::UrlObject to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from . import QV4

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QUrl
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QUrl = WAIT['QUrl']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class UrlObject(QV4.Object):
  """
  The cute side of Qt's QV4::UrlObject: a plain Python object standing in
  front of one C++ QV4::UrlObject.

  It is built on the cute 'QV4::Object', as Qt's QV4::UrlObject is built on
  Qt's QV4::Object, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QV4::UrlObject that has a ritual and that Python can
  call so far, 29 names in all: '__dataTest', 'd_unchecked', 'd',
  'virtualDestroy', 'defaultPrototype', 'hash', 'setHash', 'host', 'setHost',
  'hostname', 'setHostname', 'href', 'setHref', 'origin', 'password',
  'setPassword', 'pathname', 'setPathname', 'port', 'setPort', 'protocol',
  'setProtocol', 'search', 'setSearch', 'username', 'setUsername', 'toQUrl',
  'setUrl', 'constD'. None can be made from Python: one comes out of a
  function of another class that gives one back.

  What has no ritual
  ------------------

  6 of the 35 functions Qt declares: 3 forbidden; 1 not a gap; 1 a template;
  1 leans on 'QV4.

  What to expect
  --------------

  - The C++ QV4::UrlObject is created at the first use, not by
    'QV4::UrlObject(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QV4::UrlObject.
  - Each name of Qt's QV4::UrlObject that has no cute function yet,
    'updateUrl', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(WAIT['QV4.Heap.Base'])
  @overload(NoneType)
  def virtualDestroy(b: Optional[QV4.Heap.Base]) -> None:
    """
    Calls Qt's 'void QV4::UrlObject::virtualDestroy(QV4::Heap::Base *b)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-urlobject.html#virtualDestroy

    Parameters
    ----------

    b : Optional[QV4.Heap.Base]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QV4::UrlObject::virtualDestroy(QV4::Heap::Base *b)
    Rituals.call(
        'ritual_ZN3QV49UrlObject14virtualDestroyEPNS_4Heap4BaseE',
        CuteMixin._addressOf(b),
    )

  @staticmethod
  @overload(WAIT['QV4.ExecutionEngine'])
  @overload(NoneType)
  def defaultPrototype(
      e: Optional[QV4.ExecutionEngine],
  ) -> Optional[QV4.Object]:
    """
    Calls Qt's 'QV4::Object
    *QV4::UrlObject::defaultPrototype(QV4::ExecutionEngine *e)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-urlobject.html#defaultPrototype

    Parameters
    ----------

    e : Optional[QV4.ExecutionEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QV4.Object]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QV4::Object *QV4::UrlObject::defaultPrototype(QV4::ExecutionEngine *e)
    address = Rituals.call(
        'ritual_ZN3QV49UrlObject16defaultPrototypeEPNS_15ExecutionEngineE',
        CuteMixin._addressOf(e),
    )
    return QV4.Object._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QV4::UrlObject'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def d_unchecked(self) -> Optional[QV4.Heap.UrlObject]:
    """
    Calls Qt's 'QV4::Heap::UrlObject *QV4::UrlObject::d_unchecked() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-urlobject.html#d_unchecked

    Returns
    -------

    Optional[QV4.Heap.UrlObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QV4::Heap::UrlObject *QV4::UrlObject::d_unchecked() const
    address = self.uglySide.call('ritual_ZNK3QV49UrlObject11d_uncheckedEv')
    return QV4.Heap.UrlObject._cuteAt(address)

  def d(self) -> Optional[QV4.Heap.UrlObject]:
    """
    Calls Qt's 'QV4::Heap::UrlObject *QV4::UrlObject::d() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-urlobject.html#d

    Returns
    -------

    Optional[QV4.Heap.UrlObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QV4::Heap::UrlObject *QV4::UrlObject::d() const
    address = self.uglySide.call('ritual_ZNK3QV49UrlObject1dEv')
    return QV4.Heap.UrlObject._cuteAt(address)

  def hash(self) -> str:
    """
    Calls Qt's 'QString QV4::UrlObject::hash() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-urlobject.html#hash

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QV4::UrlObject::hash() const
    return self.uglySide.call('ritual_ZNK3QV49UrlObject4hashEv')

  def host(self) -> str:
    """
    Calls Qt's 'QString QV4::UrlObject::host() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-urlobject.html#host

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QV4::UrlObject::host() const
    return self.uglySide.call('ritual_ZNK3QV49UrlObject4hostEv')

  def hostname(self) -> str:
    """
    Calls Qt's 'QString QV4::UrlObject::hostname() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-urlobject.html#hostname

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QV4::UrlObject::hostname() const
    return self.uglySide.call('ritual_ZNK3QV49UrlObject8hostnameEv')

  def href(self) -> str:
    """
    Calls Qt's 'QString QV4::UrlObject::href() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-urlobject.html#href

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QV4::UrlObject::href() const
    return self.uglySide.call('ritual_ZNK3QV49UrlObject4hrefEv')

  def origin(self) -> str:
    """
    Calls Qt's 'QString QV4::UrlObject::origin() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-urlobject.html#origin

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QV4::UrlObject::origin() const
    return self.uglySide.call('ritual_ZNK3QV49UrlObject6originEv')

  def password(self) -> str:
    """
    Calls Qt's 'QString QV4::UrlObject::password() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-urlobject.html#password

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QV4::UrlObject::password() const
    return self.uglySide.call('ritual_ZNK3QV49UrlObject8passwordEv')

  def pathname(self) -> str:
    """
    Calls Qt's 'QString QV4::UrlObject::pathname() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-urlobject.html#pathname

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QV4::UrlObject::pathname() const
    return self.uglySide.call('ritual_ZNK3QV49UrlObject8pathnameEv')

  def port(self) -> str:
    """
    Calls Qt's 'QString QV4::UrlObject::port() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-urlobject.html#port

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QV4::UrlObject::port() const
    return self.uglySide.call('ritual_ZNK3QV49UrlObject4portEv')

  def protocol(self) -> str:
    """
    Calls Qt's 'QString QV4::UrlObject::protocol() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-urlobject.html#protocol

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QV4::UrlObject::protocol() const
    return self.uglySide.call('ritual_ZNK3QV49UrlObject8protocolEv')

  def search(self) -> str:
    """
    Calls Qt's 'QString QV4::UrlObject::search() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-urlobject.html#search

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QV4::UrlObject::search() const
    return self.uglySide.call('ritual_ZNK3QV49UrlObject6searchEv')

  def username(self) -> str:
    """
    Calls Qt's 'QString QV4::UrlObject::username() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-urlobject.html#username

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QV4::UrlObject::username() const
    return self.uglySide.call('ritual_ZNK3QV49UrlObject8usernameEv')

  def toQUrl(self) -> QUrl:
    """
    Calls Qt's 'QUrl QV4::UrlObject::toQUrl() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-urlobject.html#toQUrl

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QV4::UrlObject::toQUrl() const
    address = self.uglySide.call('ritual_ZNK3QV49UrlObject6toQUrlEv')
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  def constD(self) -> Optional[QV4.Heap.UrlObject]:
    """
    Calls Qt's 'const Heap::UrlObject *QV4::UrlObject::constD() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-urlobject.html#constD

    Returns
    -------

    Optional[QV4.Heap.UrlObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const Heap::UrlObject *QV4::UrlObject::constD() const
    address = self.uglySide.call('ritual_ZNK3QV49UrlObject6constDEv')
    return QV4.Heap.UrlObject._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setHash(self, hash: str) -> bool:
    """
    Calls Qt's 'bool QV4::UrlObject::setHash(const QString &hash)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-urlobject.html#setHash

    Parameters
    ----------

    hash : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QV4::UrlObject::setHash(const QString &hash)
    return self.uglySide.call(
        'ritual_ZN3QV49UrlObject7setHashERK7QString', hash,
    )

  @overload(str)
  def setHost(self, host: str) -> bool:
    """
    Calls Qt's 'bool QV4::UrlObject::setHost(const QString &host)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-urlobject.html#setHost

    Parameters
    ----------

    host : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QV4::UrlObject::setHost(const QString &host)
    return self.uglySide.call(
        'ritual_ZN3QV49UrlObject7setHostERK7QString', host,
    )

  @overload(str)
  def setHostname(self, hostname: str) -> bool:
    """
    Calls Qt's 'bool QV4::UrlObject::setHostname(const QString &hostname)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-urlobject.html#setHostname

    Parameters
    ----------

    hostname : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QV4::UrlObject::setHostname(const QString &hostname)
    return self.uglySide.call(
        'ritual_ZN3QV49UrlObject11setHostnameERK7QString', hostname,
    )

  @overload(str)
  def setHref(self, href: str) -> bool:
    """
    Calls Qt's 'bool QV4::UrlObject::setHref(const QString &href)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-urlobject.html#setHref

    Parameters
    ----------

    href : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QV4::UrlObject::setHref(const QString &href)
    return self.uglySide.call(
        'ritual_ZN3QV49UrlObject7setHrefERK7QString', href,
    )

  @overload(str)
  def setPassword(self, password: str) -> bool:
    """
    Calls Qt's 'bool QV4::UrlObject::setPassword(const QString &password)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-urlobject.html#setPassword

    Parameters
    ----------

    password : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QV4::UrlObject::setPassword(const QString &password)
    return self.uglySide.call(
        'ritual_ZN3QV49UrlObject11setPasswordERK7QString', password,
    )

  @overload(str)
  def setPathname(self, pathname: str) -> bool:
    """
    Calls Qt's 'bool QV4::UrlObject::setPathname(const QString &pathname)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-urlobject.html#setPathname

    Parameters
    ----------

    pathname : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QV4::UrlObject::setPathname(const QString &pathname)
    return self.uglySide.call(
        'ritual_ZN3QV49UrlObject11setPathnameERK7QString', pathname,
    )

  @overload(str)
  def setPort(self, port: str) -> bool:
    """
    Calls Qt's 'bool QV4::UrlObject::setPort(const QString &port)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-urlobject.html#setPort

    Parameters
    ----------

    port : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QV4::UrlObject::setPort(const QString &port)
    return self.uglySide.call(
        'ritual_ZN3QV49UrlObject7setPortERK7QString', port,
    )

  @overload(str)
  def setProtocol(self, protocol: str) -> bool:
    """
    Calls Qt's 'bool QV4::UrlObject::setProtocol(const QString &protocol)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-urlobject.html#setProtocol

    Parameters
    ----------

    protocol : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QV4::UrlObject::setProtocol(const QString &protocol)
    return self.uglySide.call(
        'ritual_ZN3QV49UrlObject11setProtocolERK7QString', protocol,
    )

  @overload(str)
  def setSearch(self, search: str) -> bool:
    """
    Calls Qt's 'bool QV4::UrlObject::setSearch(const QString &search)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-urlobject.html#setSearch

    Parameters
    ----------

    search : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QV4::UrlObject::setSearch(const QString &search)
    return self.uglySide.call(
        'ritual_ZN3QV49UrlObject9setSearchERK7QString', search,
    )

  @overload(str)
  def setUsername(self, username: str) -> bool:
    """
    Calls Qt's 'bool QV4::UrlObject::setUsername(const QString &username)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-urlobject.html#setUsername

    Parameters
    ----------

    username : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QV4::UrlObject::setUsername(const QString &username)
    return self.uglySide.call(
        'ritual_ZN3QV49UrlObject11setUsernameERK7QString', username,
    )

  @overload(QUrl)
  def setUrl(self, url: QUrl) -> None:
    """
    Calls Qt's 'void QV4::UrlObject::setUrl(const QUrl &url)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-urlobject.html#setUrl

    Parameters
    ----------

    url : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  void QV4::UrlObject::setUrl(const QUrl &url)
    self.uglySide.call(
        'ritual_ZN3QV49UrlObject6setUrlERK4QUrl', self._valueOf(url),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def __dataTest(self) -> None:
    """
    Calls Qt's 'void QV4::UrlObject::__dataTest()'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-urlobject.html#__dataTest
    """
    #  void QV4::UrlObject::__dataTest()
    self.uglySide.call('ritual_ZN3QV49UrlObject10__dataTestEv')

  @staticmethod
  def updateUrl(*__, **_) -> Never:
    """
    Qt's 'QV4::UrlObject::updateUrl': a template: a pattern and no single
    function.
    """
    raise NotImplementedError(
        "'QV4.UrlObject.updateUrl' has no cute function yet. Qt's "
        "'QV4::UrlObject::updateUrl': a template: a pattern and no single "
        "function.")
