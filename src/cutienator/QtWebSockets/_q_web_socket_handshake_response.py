"""
QWebSocketHandshakeResponse binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWebSockets/6.12.0/QtWebSockets/private/qwebsockethandshakeresponse_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QWebSocketHandshakeResponse to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..QtCore import QObject
from . import QWebSocketProtocol

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject


class QWebSocketHandshakeResponse(QObject):
  """
  The cute side of Qt's QWebSocketHandshakeResponse: a plain Python object
  standing in front of one C++ QWebSocketHandshakeResponse.

  It is built on the cute 'QObject', as Qt's QWebSocketHandshakeResponse is
  built on Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QWebSocketHandshakeResponse that has a ritual and
  that Python can call so far, 9 names in all: 'metaObject', 'isValid',
  'canUpgrade', 'acceptedProtocol', 'acceptedExtension', 'acceptedVersion',
  'error', 'errorString', 'calculateAcceptKey'. None can be made from Python:
  one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QWebSocketHandshakeResponse::qt_metacast(const char *a0)':
    one of Qt's own inner workings.
  - Qt's 'int QWebSocketHandshakeResponse::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QWebSocketHandshakeResponse::~QWebSocketHandshakeResponse()': the
    destructor: Python never removes a C++ QWebSocketHandshakeResponse.
  - Qt's 'QTextStream &QWebSocketHandshakeResponse::writeToStream(QTextStream
    &textStream) const': takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  8 of the 21 functions Qt declares: 2 not a gap; 2 forbidden; 2 leans on
  'QWebSocketHandshakeResponse; 1 cannot be called and cannot be called
  through the meta-object and cannot be copied; 1 Qt's library has no name
  for it, and its code in Qt's source does not compile apart from its file.

  What to expect
  --------------

  - The C++ QWebSocketHandshakeResponse is created at the first use, not by
    'QWebSocketHandshakeResponse(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QWebSocketHandshakeResponse.
  - Qt tells when it has removed the C++ QWebSocketHandshakeResponse. Every
    call on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QWebSocketHandshakeResponse that has no cute function
    yet, '__init__', 'getHandshakeResponse', 'writeToStream', holds a
    function that raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QWebSocketHandshakeResponse'

  #  A C++ QWebSocketHandshakeResponse Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QWebSocketHandshakeResponse'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QWebSocketHandshakeResponse::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebsockethandshakeresponse.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QWebSocketHandshakeResponse::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK27QWebSocketHandshakeResponse10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool QWebSocketHandshakeResponse::isValid() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebsockethandshakeresponse.html#isValid
    """
    #  bool QWebSocketHandshakeResponse::isValid() const
    return self.uglySide.call(
        'ritual_ZNK27QWebSocketHandshakeResponse7isValidEv',
    )

  def canUpgrade(self) -> bool:
    """
    Calls Qt's 'bool QWebSocketHandshakeResponse::canUpgrade() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebsockethandshakeresponse.html#canUpgrade
    """
    #  bool QWebSocketHandshakeResponse::canUpgrade() const
    return self.uglySide.call(
        'ritual_ZNK27QWebSocketHandshakeResponse10canUpgradeEv',
    )

  def acceptedProtocol(self) -> str:
    """
    Calls Qt's 'QString QWebSocketHandshakeResponse::acceptedProtocol()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebsockethandshakeresponse.html#acceptedProtocol

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QWebSocketHandshakeResponse::acceptedProtocol() const
    return self.uglySide.call(
        'ritual_ZNK27QWebSocketHandshakeResponse16acceptedProtocolEv',
    )

  def acceptedExtension(self) -> str:
    """
    Calls Qt's 'QString QWebSocketHandshakeResponse::acceptedExtension()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebsockethandshakeresponse.html#acceptedExtension

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QWebSocketHandshakeResponse::acceptedExtension() const
    return self.uglySide.call(
        'ritual_ZNK27QWebSocketHandshakeResponse17acceptedExtensionEv',
    )

  def acceptedVersion(self) -> QWebSocketProtocol.Version:
    """
    Calls Qt's 'QWebSocketProtocol::Version
    QWebSocketHandshakeResponse::acceptedVersion() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebsockethandshakeresponse.html#acceptedVersion

    Returns
    -------

    QWebSocketProtocol.Version
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QWebSocketProtocol.Version(number)' gives.
    """
    #  QWebSocketProtocol::Version
    #      QWebSocketHandshakeResponse::acceptedVersion() const
    return QWebSocketProtocol.Version(self.uglySide.call(
        'ritual_ZNK27QWebSocketHandshakeResponse15acceptedVersionEv',
    ))

  def error(self) -> QWebSocketProtocol.CloseCode:
    """
    Calls Qt's 'QWebSocketProtocol::CloseCode
    QWebSocketHandshakeResponse::error() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebsockethandshakeresponse.html#error

    Returns
    -------

    QWebSocketProtocol.CloseCode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QWebSocketProtocol.CloseCode(number)' gives.
    """
    #  QWebSocketProtocol::CloseCode QWebSocketHandshakeResponse::error()
    #      const
    return QWebSocketProtocol.CloseCode(self.uglySide.call(
        'ritual_ZNK27QWebSocketHandshakeResponse5errorEv',
    ))

  def errorString(self) -> str:
    """
    Calls Qt's 'QString QWebSocketHandshakeResponse::errorString() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebsockethandshakeresponse.html#errorString

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QWebSocketHandshakeResponse::errorString() const
    return self.uglySide.call(
        'ritual_ZNK27QWebSocketHandshakeResponse11errorStringEv',
    )

  @overload(str)
  def calculateAcceptKey(self, key: str) -> str:
    """
    Calls Qt's 'QString QWebSocketHandshakeResponse::calculateAcceptKey(const
    QString &key) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebsockethandshakeresponse.html

    Parameters
    ----------

    key : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QWebSocketHandshakeResponse::calculateAcceptKey(const QString
    #      &key) const
    return self.uglySide.call(
        'ritual_ZNK27QWebSocketHandshakeResponse18calculateAcceptKeyERK7QSt'
        'ring',
        key,
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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'QWebSocketHandshakeResponse::QWebSocketHandshakeResponse(const
    QWebSocketHandshakeRequest &request, const QString &serverName, bool
    isOriginAllowed, const QList<QWebSocketProtocol::Version>
    &supportedVersions, const QList<QString> &supportedProtocols, const
    QList<QString> &supportedExtensions)': leans on
    'QWebSocketHandshakeResponse::qt_metacall(QMetaObject::Call, int,
    void**)', which Qt's source does not mark for use from outside Qt and has
    no code for that could be taken.
    """
    raise NotImplementedError(
        "'QWebSocketHandshakeResponse.__init__' has no cute function yet. "
        "Qt's "
        "'QWebSocketHandshakeResponse::QWebSocketHandshakeResponse(const "
        "QWebSocketHandshakeRequest &request, const QString &serverName, "
        "bool isOriginAllowed, const QList<QWebSocketProtocol::Version> "
        "&supportedVersions, const QList<QString> &supportedProtocols, "
        "const QList<QString> &supportedExtensions)': leans on "
        "'QWebSocketHandshakeResponse::qt_metacall(QMetaObject::Call, int, "
        "void**)', which Qt's source does not mark for use from outside Qt "
        "and has no code for that could be taken.")

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

  @staticmethod
  def getHandshakeResponse(*__, **_) -> Never:
    """
    Qt's 'QString QWebSocketHandshakeResponse::getHandshakeResponse(const
    QWebSocketHandshakeRequest &request, const QString &serverName, bool
    isOriginAllowed, const QList<QWebSocketProtocol::Version>
    &supportedVersions, const QList<QString> &supportedProtocols, const
    QList<QString> &supportedExtensions)': Qt's library has no name for it,
    and its code in Qt's source does not compile apart from its file: use of
    undeclared identifier 'listIntersection'.
    """
    raise NotImplementedError(
        "'QWebSocketHandshakeResponse.getHandshakeResponse' has no cute "
        "function yet. Qt's 'QString "
        "QWebSocketHandshakeResponse::getHandshakeResponse(const "
        "QWebSocketHandshakeRequest &request, const QString &serverName, "
        "bool isOriginAllowed, const QList<QWebSocketProtocol::Version> "
        "&supportedVersions, const QList<QString> &supportedProtocols, "
        "const QList<QString> &supportedExtensions)': Qt's library has no "
        "name for it, and its code in Qt's source does not compile apart "
        "from its file: use of undeclared identifier 'listIntersection'.")

  @staticmethod
  def writeToStream(*__, **_) -> Never:
    """
    Qt's 'QTextStream &QWebSocketHandshakeResponse::writeToStream(QTextStream
    &textStream) const': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QWebSocketHandshakeResponse.writeToStream' has no cute function "
        "yet. Qt's 'QTextStream "
        "&QWebSocketHandshakeResponse::writeToStream(QTextStream "
        "&textStream) const': takes a type Python has no way to hand over "
        "yet.")
