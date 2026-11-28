"""
QNetworkCookieJar binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtNetwork/qnetworkcookiejar.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QList, QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QUrl
  from . import QNetworkCookie, QNetworkCookieJarPrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QNetworkCookie = WAIT['QNetworkCookie']
  QUrl = WAIT['QUrl']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QNetworkCookieJar(QObject):
  """
  The cute side of Qt's QNetworkCookieJar: a plain Python object standing in
  front of one C++ QNetworkCookieJar.

  It is built on the cute 'QObject', as Qt's QNetworkCookieJar is built on
  Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QNetworkCookieJar that has a ritual and that Python
  can call so far, 11 names in all: 'metaObject', 'tr', 'cookiesForUrl',
  'setCookiesFromUrl', 'insertCookie', 'updateCookie', 'deleteCookie',
  'allCookies', 'setAllCookies', 'validateCookie', 'd_func'. It can be made
  from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QNetworkCookieJar::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QNetworkCookieJar::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QNetworkCookieJar::~QNetworkCookieJar()': the destructor: Python
    never removes a C++ QNetworkCookieJar.
  - Qt's 'const QNetworkCookieJarPrivate *QNetworkCookieJar::d_func() const':
    takes in Python what 'QNetworkCookieJarPrivate
    *QNetworkCookieJar::d_func()' takes.

  What has no ritual
  ------------------

  4 of the 20 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QNetworkCookieJar is created at the first use, not by
    'QNetworkCookieJar(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QNetworkCookieJar.
  - Qt tells when it has removed the C++ QNetworkCookieJar. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

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
    Calls Qt's 'QString QNetworkCookieJar::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qnetworkcookiejar.html#tr

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
    #  QString QNetworkCookieJar::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN17QNetworkCookieJar2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QNetworkCookieJar'

  #  A C++ QNetworkCookieJar Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QNetworkCookieJar'

  #  The functions Qt calls itself that QNetworkCookieJar is the first to
  #  declare and that cannot be handed to Python yet, each as Qt declares it.
  #  A class of a program that writes one of them anew is refused, since Qt
  #  would never call what it wrote; see 'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'cookiesForUrl': (
          'QList<QNetworkCookie> QNetworkCookieJar::cookiesForUrl(const '
          'QUrl &) const',
      ),
      'setCookiesFromUrl': (
          'bool QNetworkCookieJar::setCookiesFromUrl(const '
          'QList<QNetworkCookie> &, const QUrl &)',
      ),
  }

  #  The functions Qt calls itself that QNetworkCookieJar is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'insertCookie': (
          ('_ZN17QNetworkCookieJar12insertCookieERK14QNetworkCookie',
           ('bool', 'number', ''),
           (
               ('address', 'value', 'QtNetwork:QNetworkCookie'),
           )),
      ),
      'updateCookie': (
          ('_ZN17QNetworkCookieJar12updateCookieERK14QNetworkCookie',
           ('bool', 'number', ''),
           (
               ('address', 'value', 'QtNetwork:QNetworkCookie'),
           )),
      ),
      'deleteCookie': (
          ('_ZN17QNetworkCookieJar12deleteCookieERK14QNetworkCookie',
           ('bool', 'number', ''),
           (
               ('address', 'value', 'QtNetwork:QNetworkCookie'),
           )),
      ),
      'validateCookie': (
          ('_ZNK17QNetworkCookieJar14validateCookieERK14QNetworkCookieRK4QU'
           'rl',
           ('bool', 'number', ''),
           (
               ('address', 'value', 'QtNetwork:QNetworkCookie'),
               ('address', 'value', 'QtCore:QUrl'),
           )),
      ),
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QNetworkCookieJar::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qnetworkcookiejar.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QNetworkCookieJar::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK17QNetworkCookieJar10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  @overload(QUrl)
  def cookiesForUrl(self, url: QUrl) -> QList[QNetworkCookie]:
    """
    Calls Qt's 'QList<QNetworkCookie> QNetworkCookieJar::cookiesForUrl(const
    QUrl &url) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkcookiejar.html#cookiesForUrl

    Parameters
    ----------

    url : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.

    Returns
    -------

    QList[QNetworkCookie]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QNetworkCookie> QNetworkCookieJar::cookiesForUrl(const QUrl
    #      &url) const
    address = self.uglySide.call(
        'ritual_ZNK17QNetworkCookieJar13cookiesForUrlERK4QUrl',
        self._valueOf(url),
    )
    from . import QNetworkCookie
    return QList[QNetworkCookie]._cuteOwning(address)

  def allCookies(self) -> QList[QNetworkCookie]:
    """
    Calls Qt's 'QList<QNetworkCookie> QNetworkCookieJar::allCookies() const'.

    Qt's own words: https://doc.qt.io/qt-6/qnetworkcookiejar.html#allCookies

    Returns
    -------

    QList[QNetworkCookie]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QNetworkCookie> QNetworkCookieJar::allCookies() const
    address = self.uglySide.call(
        'ritual_ZNK17QNetworkCookieJar10allCookiesEv',
    )
    from . import QNetworkCookie
    return QList[QNetworkCookie]._cuteOwning(address)

  @overload(QNetworkCookie, QUrl)
  def validateCookie(self, cookie: QNetworkCookie, url: QUrl) -> bool:
    """
    Calls Qt's 'bool QNetworkCookieJar::validateCookie(const QNetworkCookie
    &cookie, const QUrl &url) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkcookiejar.html#validateCookie

    Parameters
    ----------

    cookie : QNetworkCookie
      Passed on as a value: Qt reads the C++ QNetworkCookie, which stays
      Python's own.

    url : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  bool QNetworkCookieJar::validateCookie(const QNetworkCookie &cookie,
    #      const QUrl &url) const
    ritual = (
        'ritual_ZNK17QNetworkCookieJar14validateCookieERK14QNetworkCookieRK'
        '4QUrl')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK17QNetworkCookieJar14validateCookieERK14QNetworkCo'
          'okieRK4QUrl')
    return self.uglySide.call(
        ritual, self._valueOf(cookie), self._valueOf(url),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QList[QNetworkCookie], QUrl)
  def setCookiesFromUrl(
      self,
      cookieList: QList[QNetworkCookie],
      url: QUrl,
  ) -> bool:
    """
    Calls Qt's 'bool QNetworkCookieJar::setCookiesFromUrl(const
    QList<QNetworkCookie> &cookieList, const QUrl &url)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkcookiejar.html#setCookiesFromUrl

    Parameters
    ----------

    cookieList : QList[QNetworkCookie]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    url : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  bool QNetworkCookieJar::setCookiesFromUrl(const QList<QNetworkCookie>
    #      &cookieList, const QUrl &url)
    return self.uglySide.call(
        'ritual_ZN17QNetworkCookieJar17setCookiesFromUrlERK5QListI14QNetwor'
        'kCookieERK4QUrl',
        self._valueOf(cookieList), self._valueOf(url),
    )

  @overload(QList[QNetworkCookie])
  def setAllCookies(self, cookieList: QList[QNetworkCookie]) -> None:
    """
    Calls Qt's 'void QNetworkCookieJar::setAllCookies(const
    QList<QNetworkCookie> &cookieList)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkcookiejar.html#setAllCookies

    Parameters
    ----------

    cookieList : QList[QNetworkCookie]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QNetworkCookieJar::setAllCookies(const QList<QNetworkCookie>
    #      &cookieList)
    self.uglySide.call(
        'ritual_ZN17QNetworkCookieJar13setAllCookiesERK5QListI14QNetworkCoo'
        'kieE',
        self._valueOf(cookieList),
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
    'QNetworkCookieJar::QNetworkCookieJar(QObject *parent)', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkcookiejar.html#QNetworkCookieJar

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QNetworkCookieJar::QNetworkCookieJar(QObject *parent)
    self._noteCreation(QNetworkCookieJar, lambda: Rituals.call(
        'ritual_ZN17QNetworkCookieJarC1EP7QObject',
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
  def insertCookie(self, cookie: QNetworkCookie) -> bool:
    """
    Calls Qt's 'bool QNetworkCookieJar::insertCookie(const QNetworkCookie
    &cookie)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkcookiejar.html#insertCookie

    Parameters
    ----------

    cookie : QNetworkCookie
      Passed on as a value: Qt reads the C++ QNetworkCookie, which stays
      Python's own.
    """
    #  bool QNetworkCookieJar::insertCookie(const QNetworkCookie &cookie)
    ritual = 'ritual_ZN17QNetworkCookieJar12insertCookieERK14QNetworkCookie'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QNetworkCookieJar12insertCookieERK14QNetworkCooki'
          'e')
    return self.uglySide.call(ritual, self._valueOf(cookie))

  @overload(QNetworkCookie)
  def updateCookie(self, cookie: QNetworkCookie) -> bool:
    """
    Calls Qt's 'bool QNetworkCookieJar::updateCookie(const QNetworkCookie
    &cookie)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkcookiejar.html#updateCookie

    Parameters
    ----------

    cookie : QNetworkCookie
      Passed on as a value: Qt reads the C++ QNetworkCookie, which stays
      Python's own.
    """
    #  bool QNetworkCookieJar::updateCookie(const QNetworkCookie &cookie)
    ritual = 'ritual_ZN17QNetworkCookieJar12updateCookieERK14QNetworkCookie'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QNetworkCookieJar12updateCookieERK14QNetworkCooki'
          'e')
    return self.uglySide.call(ritual, self._valueOf(cookie))

  @overload(QNetworkCookie)
  def deleteCookie(self, cookie: QNetworkCookie) -> bool:
    """
    Calls Qt's 'bool QNetworkCookieJar::deleteCookie(const QNetworkCookie
    &cookie)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkcookiejar.html#deleteCookie

    Parameters
    ----------

    cookie : QNetworkCookie
      Passed on as a value: Qt reads the C++ QNetworkCookie, which stays
      Python's own.
    """
    #  bool QNetworkCookieJar::deleteCookie(const QNetworkCookie &cookie)
    ritual = 'ritual_ZN17QNetworkCookieJar12deleteCookieERK14QNetworkCookie'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QNetworkCookieJar12deleteCookieERK14QNetworkCooki'
          'e')
    return self.uglySide.call(ritual, self._valueOf(cookie))

  def d_func(self) -> Optional[QNetworkCookieJarPrivate]:
    """
    Calls Qt's 'QNetworkCookieJarPrivate *QNetworkCookieJar::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qnetworkcookiejar.html#d_func

    Returns
    -------

    Optional[QNetworkCookieJarPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QNetworkCookieJarPrivate *QNetworkCookieJar::d_func()
    address = self.uglySide.call('ritual_ZN17QNetworkCookieJar6d_funcEv')
    from . import QNetworkCookieJarPrivate
    return QNetworkCookieJarPrivate._cuteAt(address)
