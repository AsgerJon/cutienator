"""
QWebSocketHandshakeRequest binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWebSockets/6.12.0/QtWebSockets/private/qwebsockethandshakerequest_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QWebSocketHandshakeRequest to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QStringList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from ..QtCore import QByteArray, QUrl
  from ..QtNetwork import QHttpHeaders
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']


class QWebSocketHandshakeRequest(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QWebSocketHandshakeRequest: a plain Python object
  standing in front of one C++ QWebSocketHandshakeRequest.

  What exists
  -----------

  Every function of Qt's QWebSocketHandshakeRequest that has a ritual and
  that Python can call so far, 13 names in all: 'clear', 'port', 'isSecure',
  'isValid', 'headers', 'hasHeader', 'key', 'origin', 'protocols',
  'extensions', 'requestUrl', 'resourceName', 'host'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QWebSocketHandshakeRequest::~QWebSocketHandshakeRequest()': the
    destructor: Python never removes a C++ QWebSocketHandshakeRequest.
  - Qt's 'QList<QWebSocketProtocol::Version>
    QWebSocketHandshakeRequest::versions() const': gives a type Python has no
    way to take yet.

  What has no ritual
  ------------------

  3 of the 19 functions Qt declares: 2 forbidden; 1 Qt's library has no name
  for it, and its code in Qt's source does not compile apart from its file.

  What to expect
  --------------

  - The C++ QWebSocketHandshakeRequest is created at the first use, not by
    'QWebSocketHandshakeRequest(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QWebSocketHandshakeRequest.
  - Each name of Qt's QWebSocketHandshakeRequest that has no cute function
    yet, 'readHandshake', 'versions', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QWebSocketHandshakeRequest'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def port(self) -> int:
    """
    Calls Qt's 'int QWebSocketHandshakeRequest::port() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebsockethandshakerequest.html#port
    """
    #  int QWebSocketHandshakeRequest::port() const
    return self.uglySide.call(
        'ritual_ZNK26QWebSocketHandshakeRequest4portEv',
    )

  def isSecure(self) -> bool:
    """
    Calls Qt's 'bool QWebSocketHandshakeRequest::isSecure() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebsockethandshakerequest.html#isSecure
    """
    #  bool QWebSocketHandshakeRequest::isSecure() const
    return self.uglySide.call(
        'ritual_ZNK26QWebSocketHandshakeRequest8isSecureEv',
    )

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool QWebSocketHandshakeRequest::isValid() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebsockethandshakerequest.html#isValid
    """
    #  bool QWebSocketHandshakeRequest::isValid() const
    return self.uglySide.call(
        'ritual_ZNK26QWebSocketHandshakeRequest7isValidEv',
    )

  def headers(self) -> QHttpHeaders:
    """
    Calls Qt's 'QHttpHeaders QWebSocketHandshakeRequest::headers() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebsockethandshakerequest.html#headers

    Returns
    -------

    QHttpHeaders
      A new cute QHttpHeaders around the copy Qt gave back. Python owns it.
    """
    #  QHttpHeaders QWebSocketHandshakeRequest::headers() const
    address = self.uglySide.call(
        'ritual_ZNK26QWebSocketHandshakeRequest7headersEv',
    )
    from ..QtNetwork import QHttpHeaders
    return QHttpHeaders._cuteOwning(address)

  @overload(QByteArray)
  def hasHeader(self, name: QByteArray) -> bool:
    """
    Calls Qt's 'bool QWebSocketHandshakeRequest::hasHeader(const QByteArray
    &name) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebsockethandshakerequest.html#hasHeader

    Parameters
    ----------

    name : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  bool QWebSocketHandshakeRequest::hasHeader(const QByteArray &name)
    #      const
    return self.uglySide.call(
        'ritual_ZNK26QWebSocketHandshakeRequest9hasHeaderERK10QByteArray',
        self._valueOf(name),
    )

  def key(self) -> str:
    """
    Calls Qt's 'QString QWebSocketHandshakeRequest::key() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebsockethandshakerequest.html#key

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QWebSocketHandshakeRequest::key() const
    return self.uglySide.call('ritual_ZNK26QWebSocketHandshakeRequest3keyEv')

  def origin(self) -> str:
    """
    Calls Qt's 'QString QWebSocketHandshakeRequest::origin() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebsockethandshakerequest.html#origin

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QWebSocketHandshakeRequest::origin() const
    return self.uglySide.call(
        'ritual_ZNK26QWebSocketHandshakeRequest6originEv',
    )

  def protocols(self) -> QStringList:
    """
    Calls Qt's 'QList<QString> QWebSocketHandshakeRequest::protocols()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebsockethandshakerequest.html#protocols

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QString> QWebSocketHandshakeRequest::protocols() const
    address = self.uglySide.call(
        'ritual_ZNK26QWebSocketHandshakeRequest9protocolsEv',
    )
    return QStringList._cuteOwning(address)

  def extensions(self) -> QStringList:
    """
    Calls Qt's 'QList<QString> QWebSocketHandshakeRequest::extensions()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebsockethandshakerequest.html#extensions

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QString> QWebSocketHandshakeRequest::extensions() const
    address = self.uglySide.call(
        'ritual_ZNK26QWebSocketHandshakeRequest10extensionsEv',
    )
    return QStringList._cuteOwning(address)

  def requestUrl(self) -> QUrl:
    """
    Calls Qt's 'QUrl QWebSocketHandshakeRequest::requestUrl() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebsockethandshakerequest.html#requestUrl

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QWebSocketHandshakeRequest::requestUrl() const
    address = self.uglySide.call(
        'ritual_ZNK26QWebSocketHandshakeRequest10requestUrlEv',
    )
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  def resourceName(self) -> str:
    """
    Calls Qt's 'QString QWebSocketHandshakeRequest::resourceName() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebsockethandshakerequest.html#resourceName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QWebSocketHandshakeRequest::resourceName() const
    return self.uglySide.call(
        'ritual_ZNK26QWebSocketHandshakeRequest12resourceNameEv',
    )

  def host(self) -> str:
    """
    Calls Qt's 'QString QWebSocketHandshakeRequest::host() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebsockethandshakerequest.html#host

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QWebSocketHandshakeRequest::host() const
    return self.uglySide.call(
        'ritual_ZNK26QWebSocketHandshakeRequest4hostEv',
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

  @overload(int, bool)
  def __init__(self, port: int, isSecure: bool) -> None:
    """
    Notes what was given, for Qt's
    'QWebSocketHandshakeRequest::QWebSocketHandshakeRequest(int port, bool
    isSecure)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebsockethandshakerequest.html

    Parameters
    ----------

    port : int
      Passed on as it is.

    isSecure : bool
      Passed on as it is.
    """
    #  QWebSocketHandshakeRequest::QWebSocketHandshakeRequest(int port, bool
    #      isSecure)
    self._noteCreation(QWebSocketHandshakeRequest, lambda: Rituals.call(
        'ritual_ZN26QWebSocketHandshakeRequestC1Eib', port, isSecure,
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

  def clear(self) -> None:
    """
    Calls Qt's 'void QWebSocketHandshakeRequest::clear()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebsockethandshakerequest.html#clear
    """
    #  void QWebSocketHandshakeRequest::clear()
    self.uglySide.call('ritual_ZN26QWebSocketHandshakeRequest5clearEv')

  @staticmethod
  def readHandshake(*__, **_) -> Never:
    """
    Qt's 'void QWebSocketHandshakeRequest::readHandshake(QByteArrayView
    header, int maxHeaderLineLength)': Qt's library has no name for it, and
    its code in Qt's source does not compile apart from its file: use of
    undeclared identifier 'appendCommmaSeparatedLineToList'.
    """
    raise NotImplementedError(
        "'QWebSocketHandshakeRequest.readHandshake' has no cute function "
        "yet. Qt's 'void "
        "QWebSocketHandshakeRequest::readHandshake(QByteArrayView header, "
        "int maxHeaderLineLength)': Qt's library has no name for it, and "
        "its code in Qt's source does not compile apart from its file: use "
        "of undeclared identifier 'appendCommmaSeparatedLineToList'.")

  @staticmethod
  def versions(*__, **_) -> Never:
    """
    Qt's 'QList<QWebSocketProtocol::Version>
    QWebSocketHandshakeRequest::versions() const': gives a type Python has no
    way to take yet.
    """
    raise NotImplementedError(
        "'QWebSocketHandshakeRequest.versions' has no cute function yet. "
        "Qt's 'QList<QWebSocketProtocol::Version> "
        "QWebSocketHandshakeRequest::versions() const': gives a type Python "
        "has no way to take yet.")
