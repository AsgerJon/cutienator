"""
QOAuthUriSchemeReplyHandler binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtNetworkAuth/qoauthurischemereplyhandler.h, Qt 6.12.0. Changes made here
#  are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject
from . import QOAuthOobReplyHandler

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QUrl
  from . import QOAuthUriSchemeReplyHandlerPrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QUrl = WAIT['QUrl']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QOAuthUriSchemeReplyHandler(QOAuthOobReplyHandler):
  """
  The cute side of Qt's QOAuthUriSchemeReplyHandler: a plain Python object
  standing in front of one C++ QOAuthUriSchemeReplyHandler.

  It is built on the cute 'QOAuthOobReplyHandler', as Qt's
  QOAuthUriSchemeReplyHandler is built on Qt's QOAuthOobReplyHandler, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QOAuthUriSchemeReplyHandler that has a ritual and
  that Python can call so far, 11 names in all: 'metaObject', 'tr',
  'callback', 'setRedirectUrl', 'redirectUrl', 'handleAuthorizationRedirect',
  'listen', 'close', 'isListening', 'redirectUrlChanged', 'd_func'. It can be
  made from Python, in 3 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QOAuthUriSchemeReplyHandler::qt_metacast(const char *a0)':
    one of Qt's own inner workings.
  - Qt's 'int QOAuthUriSchemeReplyHandler::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QOAuthUriSchemeReplyHandler::~QOAuthUriSchemeReplyHandler()': the
    destructor: Python never removes a C++ QOAuthUriSchemeReplyHandler.
  - Qt's 'const QOAuthUriSchemeReplyHandlerPrivate
    *QOAuthUriSchemeReplyHandler::d_func() const': takes in Python what
    'QOAuthUriSchemeReplyHandlerPrivate
    *QOAuthUriSchemeReplyHandler::d_func()' takes.

  What has no ritual
  ------------------

  4 of the 22 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QOAuthUriSchemeReplyHandler is created at the first use, not by
    'QOAuthUriSchemeReplyHandler(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QOAuthUriSchemeReplyHandler.
  - Qt tells when it has removed the C++ QOAuthUriSchemeReplyHandler. Every
    call on the cute object, and every use of it as an argument, then raises
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
    Calls Qt's 'QString QOAuthUriSchemeReplyHandler::tr(const char *s, const
    char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qoauthurischemereplyhandler.html#tr

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
    #  QString QOAuthUriSchemeReplyHandler::tr(const char *s, const char *c,
    #      int n)
    return Rituals.call(
        'ritual_ZN27QOAuthUriSchemeReplyHandler2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QOAuthUriSchemeReplyHandler'

  #  A C++ QOAuthUriSchemeReplyHandler Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QOAuthUriSchemeReplyHandler'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QOAuthUriSchemeReplyHandler::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qoauthurischemereplyhandler.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QOAuthUriSchemeReplyHandler::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK27QOAuthUriSchemeReplyHandler10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def callback(self) -> str:
    """
    Calls Qt's 'QString QOAuthUriSchemeReplyHandler::callback() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qoauthurischemereplyhandler.html#callback

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QOAuthUriSchemeReplyHandler::callback() const
    ritual = 'ritual_ZNK27QOAuthUriSchemeReplyHandler8callbackEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK27QOAuthUriSchemeReplyHandler8callbackEv'
    return self.uglySide.call(ritual)

  def redirectUrl(self) -> QUrl:
    """
    Calls Qt's 'QUrl QOAuthUriSchemeReplyHandler::redirectUrl() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qoauthurischemereplyhandler.html#redirectUrl

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QOAuthUriSchemeReplyHandler::redirectUrl() const
    address = self.uglySide.call(
        'ritual_ZNK27QOAuthUriSchemeReplyHandler11redirectUrlEv',
    )
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  def isListening(self) -> bool:
    """
    Calls Qt's 'bool QOAuthUriSchemeReplyHandler::isListening() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qoauthurischemereplyhandler.html#isListening
    """
    #  bool QOAuthUriSchemeReplyHandler::isListening() const
    return self.uglySide.call(
        'ritual_ZNK27QOAuthUriSchemeReplyHandler11isListeningEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QUrl)
  def setRedirectUrl(self, url: QUrl) -> None:
    """
    Calls Qt's 'void QOAuthUriSchemeReplyHandler::setRedirectUrl(const QUrl
    &url)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qoauthurischemereplyhandler.html#setRedirectUrl

    Parameters
    ----------

    url : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  void QOAuthUriSchemeReplyHandler::setRedirectUrl(const QUrl &url)
    self.uglySide.call(
        'ritual_ZN27QOAuthUriSchemeReplyHandler14setRedirectUrlERK4QUrl',
        self._valueOf(url),
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
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'QOAuthUriSchemeReplyHandler::QOAuthUriSchemeReplyHandler()', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qoauthurischemereplyhandler.html
    """
    #  QOAuthUriSchemeReplyHandler::QOAuthUriSchemeReplyHandler()
    self._noteCreation(QOAuthUriSchemeReplyHandler, lambda: Rituals.call(
        'ritual_ZN27QOAuthUriSchemeReplyHandlerC1Ev',
    ))

  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject]) -> None:
    """
    Notes what was given, for Qt's
    'QOAuthUriSchemeReplyHandler::QOAuthUriSchemeReplyHandler(QObject
    *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qoauthurischemereplyhandler.html

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QOAuthUriSchemeReplyHandler::QOAuthUriSchemeReplyHandler(QObject
    #      *parent)
    self._noteCreation(QOAuthUriSchemeReplyHandler, lambda: Rituals.call(
        'ritual_ZN27QOAuthUriSchemeReplyHandlerC1EP7QObject',
        self._addressOf(parent, 'QObject'),
    ))

  @overload(QUrl)
  @overload(QUrl, QObject)
  @overload(QUrl, NoneType)
  def __init__(
      self,
      redirectUrl: QUrl,
      parent: Optional[QObject] = None,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QOAuthUriSchemeReplyHandler::QOAuthUriSchemeReplyHandler(const QUrl
    &redirectUrl, QObject *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qoauthurischemereplyhandler.html

    Parameters
    ----------

    redirectUrl : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QOAuthUriSchemeReplyHandler::QOAuthUriSchemeReplyHandler(const QUrl
    #      &redirectUrl, QObject *parent)
    self._noteCreation(QOAuthUriSchemeReplyHandler, lambda: Rituals.call(
        'ritual_ZN27QOAuthUriSchemeReplyHandlerC1ERK4QUrlP7QObject',
        self._valueOf(redirectUrl), self._addressOf(parent, 'QObject'),
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

  @overload(QUrl)
  def handleAuthorizationRedirect(self, url: QUrl) -> bool:
    """
    Calls Qt's 'bool
    QOAuthUriSchemeReplyHandler::handleAuthorizationRedirect(const QUrl
    &url)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qoauthurischemereplyhandler.html

    Parameters
    ----------

    url : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  bool QOAuthUriSchemeReplyHandler::handleAuthorizationRedirect(const
    #      QUrl &url)
    return self.uglySide.call(
        'ritual_ZN27QOAuthUriSchemeReplyHandler27handleAuthorizationRedirec'
        'tERK4QUrl',
        self._valueOf(url),
    )

  def listen(self) -> bool:
    """
    Calls Qt's 'bool QOAuthUriSchemeReplyHandler::listen()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qoauthurischemereplyhandler.html#listen
    """
    #  bool QOAuthUriSchemeReplyHandler::listen()
    return self.uglySide.call(
        'ritual_ZN27QOAuthUriSchemeReplyHandler6listenEv',
    )

  def close(self) -> None:
    """
    Calls Qt's 'void QOAuthUriSchemeReplyHandler::close()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qoauthurischemereplyhandler.html#close
    """
    #  void QOAuthUriSchemeReplyHandler::close()
    self.uglySide.call('ritual_ZN27QOAuthUriSchemeReplyHandler5closeEv')

  def redirectUrlChanged(self) -> None:
    """
    Calls Qt's 'void QOAuthUriSchemeReplyHandler::redirectUrlChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qoauthurischemereplyhandler.html
    """
    #  void QOAuthUriSchemeReplyHandler::redirectUrlChanged()
    self.uglySide.call(
        'ritual_ZN27QOAuthUriSchemeReplyHandler18redirectUrlChangedEv',
    )

  def d_func(self) -> Optional[QOAuthUriSchemeReplyHandlerPrivate]:
    """
    Calls Qt's 'QOAuthUriSchemeReplyHandlerPrivate
    *QOAuthUriSchemeReplyHandler::d_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qoauthurischemereplyhandler.html#d_func

    Returns
    -------

    Optional[QOAuthUriSchemeReplyHandlerPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QOAuthUriSchemeReplyHandlerPrivate
    #      *QOAuthUriSchemeReplyHandler::d_func()
    address = self.uglySide.call(
        'ritual_ZN27QOAuthUriSchemeReplyHandler6d_funcEv',
    )
    from . import QOAuthUriSchemeReplyHandlerPrivate
    return QOAuthUriSchemeReplyHandlerPrivate._cuteAt(address)
