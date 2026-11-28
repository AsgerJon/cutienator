"""
QWebEngineCookieStore binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWebEngineCore/qwebenginecookiestore.h, Qt 6.12.0. Changes made here are
#  lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QUrl
  from ..QtNetwork import QNetworkCookie
  from . import QWebEngineCookieStorePrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QNetworkCookie = WAIT['QNetworkCookie']
  QUrl = WAIT['QUrl']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QWebEngineCookieStore(QObject):
  """
  The cute side of Qt's QWebEngineCookieStore: a plain Python object standing
  in front of one C++ QWebEngineCookieStore.

  It is built on the cute 'QObject', as Qt's QWebEngineCookieStore is built
  on Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QWebEngineCookieStore that has a ritual and that
  Python can call so far, 10 names in all: 'metaObject', 'tr', 'setCookie',
  'deleteCookie', 'deleteSessionCookies', 'deleteAllCookies',
  'loadAllCookies', 'cookieAdded', 'cookieRemoved', 'd_func'. It can be made
  from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QWebEngineCookieStore::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QWebEngineCookieStore::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QWebEngineCookieStore::~QWebEngineCookieStore()': the destructor:
    Python never removes a C++ QWebEngineCookieStore.
  - Qt's 'void QWebEngineCookieStore::setCookieFilter(const
    std::function<bool (const FilterRequest &)> &filterCallback)': takes a
    type Python has no way to hand over yet.
  - Qt's 'void QWebEngineCookieStore::setCookieFilter(std::function<bool
    (const FilterRequest &)> &&filterCallback)': takes a type Python has no
    way to hand over yet.
  - Qt's 'const QWebEngineCookieStorePrivate *QWebEngineCookieStore::d_func()
    const': takes in Python what 'QWebEngineCookieStorePrivate
    *QWebEngineCookieStore::d_func()' takes.

  What has no ritual
  ------------------

  4 of the 21 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QWebEngineCookieStore is created at the first use, not by
    'QWebEngineCookieStore(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QWebEngineCookieStore.
  - Qt tells when it has removed the C++ QWebEngineCookieStore. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QWebEngineCookieStore that has no cute function yet,
    'setCookieFilter', holds a function that raises 'NotImplementedError',
    and its docstring says why.
  """

  #  The classes Qt writes inside QWebEngineCookieStore, each a class in here
  #  as in C++.

  class FilterRequest(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QWebEngineCookieStore::FilterRequest: a plain
    Python object standing in front of one C++
    QWebEngineCookieStore::FilterRequest.

    C++ hands a QWebEngineCookieStore::FilterRequest around as a copy, so
    every C++ QWebEngineCookieStore::FilterRequest behind a cute one is
    Python's own: it is removed, by the ritual named in '__delete_ritual__',
    when the cute object goes.

    What exists
    -----------

    No function of Qt's QWebEngineCookieStore::FilterRequest yet. None can be
    made from Python: one comes out of a function of another class that gives
    one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QWebEngineCookieStore::FilterRequest::~FilterRequest()': the
      destructor: Python removes its C++ QWebEngineCookieStore::FilterRequest
      by it, and has no other use for it.

    What to expect
    --------------

    - The C++ QWebEngineCookieStore::FilterRequest is created at the first
      use, not by 'QWebEngineCookieStore::FilterRequest(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QWebEngineCookieStore::FilterRequest back gives a
      copy the ritual made for Python, in a new cute
      QWebEngineCookieStore::FilterRequest.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QWebEngineCookieStore::FilterRequest'

    #  Qt's '~QWebEngineCookieStore::FilterRequest()'. Naming it makes this a
    #  value class: Python owns every C++
    #  QWebEngineCookieStore::FilterRequest behind a cute one, and removes it
    #  by this ritual.
    __delete_ritual__ = 'ritual_ZN21QWebEngineCookieStore13FilterRequestD1Ev'

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(str)
  @overload(NoneType)
  @overload(str, str)
  @overload(str, NoneType)
  @overload(NoneType, str)
  @overload(NoneType, NoneType)
  @overload(str, str, int)
  @overload(str, NoneType, int)
  @overload(NoneType, str, int)
  @overload(NoneType, NoneType, int)
  def tr(s: Optional[str], c: Optional[str] = None, n: int = -1) -> str:
    """
    Calls Qt's 'QString QWebEngineCookieStore::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qwebenginecookiestore.html#tr

    Parameters
    ----------

    s : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    c : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text. May
      be left out, as in Qt: it is then None.

    n : int
      Passed on as it is. May be left out, as in Qt: it is then -1.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QWebEngineCookieStore::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN21QWebEngineCookieStore2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QWebEngineCookieStore'

  #  A C++ QWebEngineCookieStore Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QWebEngineCookieStore'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QWebEngineCookieStore::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginecookiestore.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QWebEngineCookieStore::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK21QWebEngineCookieStore10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QNetworkCookie)
  @overload(QNetworkCookie, QUrl)
  def setCookie(
      self,
      cookie: QNetworkCookie,
      origin: Optional[QUrl] = None,
  ) -> None:
    """
    Calls Qt's 'void QWebEngineCookieStore::setCookie(const QNetworkCookie
    &cookie, const QUrl &origin)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginecookiestore.html#setCookie

    Parameters
    ----------

    cookie : QNetworkCookie
      Passed on as a value: Qt reads the C++ QNetworkCookie, which stays
      Python's own.

    origin : Optional[QUrl]
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
      May be left out, as in Qt: a new 'QUrl()' is then passed on.
    """
    #  void QWebEngineCookieStore::setCookie(const QNetworkCookie &cookie,
    #      const QUrl &origin)
    if origin is None:
      from ..QtCore import QUrl
      origin = QUrl()
    self.uglySide.call(
        'ritual_ZN21QWebEngineCookieStore9setCookieERK14QNetworkCookieRK4QU'
        'rl',
        self._valueOf(cookie), self._valueOf(origin),
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

  @overload()
  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's
    'QWebEngineCookieStore::QWebEngineCookieStore(QObject *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginecookiestore.html#QWebEngineCookieStore

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QWebEngineCookieStore::QWebEngineCookieStore(QObject *parent)
    self._noteCreation(QWebEngineCookieStore, lambda: Rituals.call(
        'ritual_ZN21QWebEngineCookieStoreC1EP7QObject',
        self._addressOf(parent, 'QObject'),
    ))

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

  @overload(QNetworkCookie)
  @overload(QNetworkCookie, QUrl)
  def deleteCookie(
      self,
      cookie: QNetworkCookie,
      origin: Optional[QUrl] = None,
  ) -> None:
    """
    Calls Qt's 'void QWebEngineCookieStore::deleteCookie(const QNetworkCookie
    &cookie, const QUrl &origin)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginecookiestore.html#deleteCookie

    Parameters
    ----------

    cookie : QNetworkCookie
      Passed on as a value: Qt reads the C++ QNetworkCookie, which stays
      Python's own.

    origin : Optional[QUrl]
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
      May be left out, as in Qt: a new 'QUrl()' is then passed on.
    """
    #  void QWebEngineCookieStore::deleteCookie(const QNetworkCookie &cookie,
    #      const QUrl &origin)
    if origin is None:
      from ..QtCore import QUrl
      origin = QUrl()
    self.uglySide.call(
        'ritual_ZN21QWebEngineCookieStore12deleteCookieERK14QNetworkCookieR'
        'K4QUrl',
        self._valueOf(cookie), self._valueOf(origin),
    )

  def deleteSessionCookies(self) -> None:
    """
    Calls Qt's 'void QWebEngineCookieStore::deleteSessionCookies()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginecookiestore.html#deleteSessionCookies
    """
    #  void QWebEngineCookieStore::deleteSessionCookies()
    self.uglySide.call(
        'ritual_ZN21QWebEngineCookieStore20deleteSessionCookiesEv',
    )

  def deleteAllCookies(self) -> None:
    """
    Calls Qt's 'void QWebEngineCookieStore::deleteAllCookies()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginecookiestore.html#deleteAllCookies
    """
    #  void QWebEngineCookieStore::deleteAllCookies()
    self.uglySide.call(
        'ritual_ZN21QWebEngineCookieStore16deleteAllCookiesEv',
    )

  def loadAllCookies(self) -> None:
    """
    Calls Qt's 'void QWebEngineCookieStore::loadAllCookies()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginecookiestore.html#loadAllCookies
    """
    #  void QWebEngineCookieStore::loadAllCookies()
    self.uglySide.call('ritual_ZN21QWebEngineCookieStore14loadAllCookiesEv')

  @overload(QNetworkCookie)
  def cookieAdded(self, cookie: QNetworkCookie) -> None:
    """
    Calls Qt's 'void QWebEngineCookieStore::cookieAdded(const QNetworkCookie
    &cookie)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginecookiestore.html#cookieAdded

    Parameters
    ----------

    cookie : QNetworkCookie
      Passed on as a value: Qt reads the C++ QNetworkCookie, which stays
      Python's own.
    """
    #  void QWebEngineCookieStore::cookieAdded(const QNetworkCookie &cookie)
    self.uglySide.call(
        'ritual_ZN21QWebEngineCookieStore11cookieAddedERK14QNetworkCookie',
        self._valueOf(cookie),
    )

  @overload(QNetworkCookie)
  def cookieRemoved(self, cookie: QNetworkCookie) -> None:
    """
    Calls Qt's 'void QWebEngineCookieStore::cookieRemoved(const
    QNetworkCookie &cookie)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginecookiestore.html#cookieRemoved

    Parameters
    ----------

    cookie : QNetworkCookie
      Passed on as a value: Qt reads the C++ QNetworkCookie, which stays
      Python's own.
    """
    #  void QWebEngineCookieStore::cookieRemoved(const QNetworkCookie
    #      &cookie)
    self.uglySide.call(
        'ritual_ZN21QWebEngineCookieStore13cookieRemovedERK14QNetworkCookie',
        self._valueOf(cookie),
    )

  def d_func(self) -> Optional[QWebEngineCookieStorePrivate]:
    """
    Calls Qt's 'QWebEngineCookieStorePrivate
    *QWebEngineCookieStore::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qwebenginecookiestore.html#d_func

    Returns
    -------

    Optional[QWebEngineCookieStorePrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWebEngineCookieStorePrivate *QWebEngineCookieStore::d_func()
    address = self.uglySide.call('ritual_ZN21QWebEngineCookieStore6d_funcEv')
    from . import QWebEngineCookieStorePrivate
    return QWebEngineCookieStorePrivate._cuteAt(address)

  @staticmethod
  def setCookieFilter(*__, **_) -> Never:
    """
    - Qt's 'void QWebEngineCookieStore::setCookieFilter(const
      std::function<bool (const FilterRequest &)> &filterCallback)': takes a
      type Python has no way to hand over yet.
    - Qt's 'void QWebEngineCookieStore::setCookieFilter(std::function<bool
      (const FilterRequest &)> &&filterCallback)': takes a type Python has no
      way to hand over yet.
    """
    raise NotImplementedError(
        "'QWebEngineCookieStore.setCookieFilter' has no cute function yet. "
        "Qt's 'void QWebEngineCookieStore::setCookieFilter(const "
        "std::function<bool (const FilterRequest &)> &filterCallback)': "
        "takes a type Python has no way to hand over yet. Qt's 'void "
        "QWebEngineCookieStore::setCookieFilter(std::function<bool (const "
        "FilterRequest &)> &&filterCallback)': takes a type Python has no "
        "way to hand over yet.")
