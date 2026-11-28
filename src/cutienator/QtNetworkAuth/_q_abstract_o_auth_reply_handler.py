"""
QAbstractOAuthReplyHandler binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtNetworkAuth/qabstractoauthreplyhandler.h, Qt 6.12.0. Changes made here
#  are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QMap, QObject
from . import QAbstractOAuth

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QByteArray, QMetaObject, QVariant
  from ..QtNetwork import QNetworkReply
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']
  QNetworkReply = WAIT['QNetworkReply']
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QAbstractOAuthReplyHandler(QObject):
  """
  The cute side of Qt's QAbstractOAuthReplyHandler: a plain Python object
  standing in front of one C++ QAbstractOAuthReplyHandler.

  It is built on the cute 'QObject', as Qt's QAbstractOAuthReplyHandler is
  built on Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QAbstractOAuthReplyHandler that has a ritual and
  that Python can call so far, 9 names in all: 'metaObject', 'tr',
  'callback', 'networkReplyFinished', 'callbackReceived', 'tokensReceived',
  'tokenRequestErrorOccurred', 'replyDataReceived', 'callbackDataReceived'.
  It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QAbstractOAuthReplyHandler::qt_metacast(const char *a0)': one
    of Qt's own inner workings.
  - Qt's 'int QAbstractOAuthReplyHandler::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QAbstractOAuthReplyHandler::~QAbstractOAuthReplyHandler()': the
    destructor: Python never removes a C++ QAbstractOAuthReplyHandler.
  - Qt's
    'QAbstractOAuthReplyHandler::QAbstractOAuthReplyHandler(QObjectPrivate
    &d, QObject *parent)': takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  4 of the 18 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QAbstractOAuthReplyHandler is created at the first use, not by
    'QAbstractOAuthReplyHandler(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QAbstractOAuthReplyHandler.
  - Qt tells when it has removed the C++ QAbstractOAuthReplyHandler. Every
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
    Calls Qt's 'QString QAbstractOAuthReplyHandler::tr(const char *s, const
    char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractoauthreplyhandler.html#tr

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
    #  QString QAbstractOAuthReplyHandler::tr(const char *s, const char *c,
    #      int n)
    return Rituals.call(
        'ritual_ZN26QAbstractOAuthReplyHandler2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QAbstractOAuthReplyHandler'

  #  A C++ QAbstractOAuthReplyHandler Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QAbstractOAuthReplyHandler'

  #  The functions Qt calls itself that QAbstractOAuthReplyHandler is the
  #  first to declare. A class of a program built on it can write one anew,
  #  and Qt then calls that. For each name: the key C++ knows the function
  #  by, what it gives, and what it takes.
  __virtual_functions__ = {
      'callback': (
          ('_ZNK26QAbstractOAuthReplyHandler8callbackEv',
           ('address', 'text', ''),
           ()),
      ),
      'networkReplyFinished': (
          ('_ZN26QAbstractOAuthReplyHandler20networkReplyFinishedEP13QNetwo'
           'rkReply',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtNetwork:QNetworkReply'),
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
    Calls Qt's 'const QMetaObject *QAbstractOAuthReplyHandler::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractoauthreplyhandler.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QAbstractOAuthReplyHandler::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK26QAbstractOAuthReplyHandler10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def callback(self) -> str:
    """
    Calls Qt's 'QString QAbstractOAuthReplyHandler::callback() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractoauthreplyhandler.html#callback

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QAbstractOAuthReplyHandler::callback() const
    return self.uglySide.call(
        'ritual_ZNK26QAbstractOAuthReplyHandler8callbackEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

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
    'QAbstractOAuthReplyHandler::QAbstractOAuthReplyHandler(QObject
    *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractoauthreplyhandler.html

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QAbstractOAuthReplyHandler::QAbstractOAuthReplyHandler(QObject
    #      *parent)
    self._noteCreation(QAbstractOAuthReplyHandler, lambda: Rituals.call(
        'ritual_ZN26QAbstractOAuthReplyHandlerC1EP7QObject',
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

  @overload(QNetworkReply)
  @overload(NoneType)
  def networkReplyFinished(self, reply: Optional[QNetworkReply]) -> None:
    """
    Calls Qt's 'void
    QAbstractOAuthReplyHandler::networkReplyFinished(QNetworkReply *reply)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractoauthreplyhandler.html

    Parameters
    ----------

    reply : Optional[QNetworkReply]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAbstractOAuthReplyHandler::networkReplyFinished(QNetworkReply
    #      *reply)
    self.uglySide.call(
        'ritual_ZN26QAbstractOAuthReplyHandler20networkReplyFinishedEP13QNe'
        'tworkReply',
        self._addressOf(reply),
    )

  @overload(QMap[str, QVariant])
  def callbackReceived(self, values: QMap[str, QVariant]) -> None:
    """
    Calls Qt's 'void QAbstractOAuthReplyHandler::callbackReceived(const
    QVariantMap &values)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractoauthreplyhandler.html#callbackReceived

    Parameters
    ----------

    values : QMap[str, QVariant]
      Passed on as a map of Qt: Qt reads the C++ map, which stays Python's
      own. A dict of Python is made into one first, and refused when a key or
      a value does not fit.
    """
    #  void QAbstractOAuthReplyHandler::callbackReceived(const QVariantMap
    #      &values)
    self.uglySide.call(
        'ritual_ZN26QAbstractOAuthReplyHandler16callbackReceivedERK4QMapI7Q'
        'String8QVariantE',
        self._valueOf(values),
    )

  @overload(QMap[str, QVariant])
  def tokensReceived(self, tokens: QMap[str, QVariant]) -> None:
    """
    Calls Qt's 'void QAbstractOAuthReplyHandler::tokensReceived(const
    QVariantMap &tokens)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractoauthreplyhandler.html#tokensReceived

    Parameters
    ----------

    tokens : QMap[str, QVariant]
      Passed on as a map of Qt: Qt reads the C++ map, which stays Python's
      own. A dict of Python is made into one first, and refused when a key or
      a value does not fit.
    """
    #  void QAbstractOAuthReplyHandler::tokensReceived(const QVariantMap
    #      &tokens)
    self.uglySide.call(
        'ritual_ZN26QAbstractOAuthReplyHandler14tokensReceivedERK4QMapI7QSt'
        'ring8QVariantE',
        self._valueOf(tokens),
    )

  @overload(QAbstractOAuth.Error, str)
  def tokenRequestErrorOccurred(
      self,
      error: QAbstractOAuth.Error,
      errorString: str,
  ) -> None:
    """
    Calls Qt's 'void
    QAbstractOAuthReplyHandler::tokenRequestErrorOccurred(QAbstractOAuth::
    Error error, const QString &errorString)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractoauthreplyhandler.html

    Parameters
    ----------

    error : QAbstractOAuth.Error
      Passed on as its number.

    errorString : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QAbstractOAuthReplyHandler::tokenRequestErrorOccurred(
    #      QAbstractOAuth::Error error, const QString &errorString)
    self.uglySide.call(
        'ritual_ZN26QAbstractOAuthReplyHandler25tokenRequestErrorOccurredEN'
        '14QAbstractOAuth5ErrorERK7QString',
        error.value, errorString,
    )

  @overload(QByteArray)
  def replyDataReceived(self, data: QByteArray) -> None:
    """
    Calls Qt's 'void QAbstractOAuthReplyHandler::replyDataReceived(const
    QByteArray &data)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractoauthreplyhandler.html#replyDataReceived

    Parameters
    ----------

    data : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void QAbstractOAuthReplyHandler::replyDataReceived(const QByteArray
    #      &data)
    self.uglySide.call(
        'ritual_ZN26QAbstractOAuthReplyHandler17replyDataReceivedERK10QByte'
        'Array',
        self._valueOf(data),
    )

  @overload(QByteArray)
  def callbackDataReceived(self, data: QByteArray) -> None:
    """
    Calls Qt's 'void QAbstractOAuthReplyHandler::callbackDataReceived(const
    QByteArray &data)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractoauthreplyhandler.html

    Parameters
    ----------

    data : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void QAbstractOAuthReplyHandler::callbackDataReceived(const QByteArray
    #      &data)
    self.uglySide.call(
        'ritual_ZN26QAbstractOAuthReplyHandler20callbackDataReceivedERK10QB'
        'yteArray',
        self._valueOf(data),
    )
