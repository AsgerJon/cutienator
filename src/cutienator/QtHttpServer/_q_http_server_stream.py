"""
QHttpServerStream binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtHttpServer/6.12.0/QtHttpServer/private/qhttpserverstream_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QHttpServerStream to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..QtCore import QObject
from . import QHttpServerResponder

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QByteArray, QIODevice, QMetaObject
  from ..QtNetwork import QHttpHeaders
  from . import QHttpServerResponderPrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']
  QHttpHeaders = WAIT['QHttpHeaders']
  QHttpServerResponderPrivate = WAIT['QHttpServerResponderPrivate']
  QIODevice = WAIT['QIODevice']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QHttpServerStream(QObject):
  """
  The cute side of Qt's QHttpServerStream: a plain Python object standing in
  front of one C++ QHttpServerStream.

  It is built on the cute 'QObject', as Qt's QHttpServerStream is built on
  Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QHttpServerStream that has a ritual and that Python
  can call so far, 10 names in all: 'metaObject', 'responderDestroyed',
  'startHandlingRequest', 'socketDisconnected', 'write', 'writeBeginChunked',
  'writeChunk', 'writeEndChunked', 'connectResponder', 'disconnectResponder'.
  None can be made from Python: one comes out of a function of another class
  that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QHttpServerStream::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QHttpServerStream::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.

  What has no ritual
  ------------------

  4 of the 18 functions Qt declares: 2 not a gap; 2 leans on
  'QHttpServerStream.

  What to expect
  --------------

  - The C++ QHttpServerStream is created at the first use, not by
    'QHttpServerStream(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QHttpServerStream.
  - Qt tells when it has removed the C++ QHttpServerStream. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QHttpServerStream that has no cute function yet,
    '__init__', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QHttpServerStream'

  #  A C++ QHttpServerStream Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QHttpServerStream'

  #  The functions Qt calls itself that QHttpServerStream is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'responderDestroyed': (
          ('_ZN17QHttpServerStream18responderDestroyedEj',
           ('nothing', 'nothing', ''),
           (
               ('unsigned int', 'number', ''),
           )),
      ),
      'startHandlingRequest': (
          ('_ZN17QHttpServerStream20startHandlingRequestEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'socketDisconnected': (
          ('_ZN17QHttpServerStream18socketDisconnectedEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'write': (
          ('_ZN17QHttpServerStream5writeERK10QByteArrayRK12QHttpHeadersN20Q'
           'HttpServerResponder10StatusCodeEj',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtCore:QByteArray'),
               ('address', 'value', 'QtNetwork:QHttpHeaders'),
               ('int', 'enum',
                'QtHttpServer:QHttpServerResponder.StatusCode'),
               ('unsigned int', 'number', ''),
           )),
          ('_ZN17QHttpServerStream5writeEN20QHttpServerResponder10StatusCod'
           'eEj',
           ('nothing', 'nothing', ''),
           (
               ('int', 'enum',
                'QtHttpServer:QHttpServerResponder.StatusCode'),
               ('unsigned int', 'number', ''),
           )),
          ('_ZN17QHttpServerStream5writeEP9QIODeviceRK12QHttpHeadersN20QHtt'
           'pServerResponder10StatusCodeEj',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtCore:QIODevice'),
               ('address', 'value', 'QtNetwork:QHttpHeaders'),
               ('int', 'enum',
                'QtHttpServer:QHttpServerResponder.StatusCode'),
               ('unsigned int', 'number', ''),
           )),
      ),
      'writeBeginChunked': (
          ('_ZN17QHttpServerStream17writeBeginChunkedERK12QHttpHeadersN20QH'
           'ttpServerResponder10StatusCodeEj',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtNetwork:QHttpHeaders'),
               ('int', 'enum',
                'QtHttpServer:QHttpServerResponder.StatusCode'),
               ('unsigned int', 'number', ''),
           )),
      ),
      'writeChunk': (
          ('_ZN17QHttpServerStream10writeChunkERK10QByteArrayj',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtCore:QByteArray'),
               ('unsigned int', 'number', ''),
           )),
      ),
      'writeEndChunked': (
          ('_ZN17QHttpServerStream15writeEndChunkedERK10QByteArrayRK12QHttp'
           'Headersj',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtCore:QByteArray'),
               ('address', 'value', 'QtNetwork:QHttpHeaders'),
               ('unsigned int', 'number', ''),
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
    Calls Qt's 'const QMetaObject *QHttpServerStream::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qhttpserverstream.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QHttpServerStream::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK17QHttpServerStream10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

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
    Qt's 'QHttpServerStream::QHttpServerStream(QIODevice *socket,
    QHttpServerRequestFilter *filter, QObject *parent)': leans on
    'QHttpServerStream::qt_metacall(QMetaObject::Call, int, void**)', which
    Qt's source does not mark for use from outside Qt and has no code for
    that could be taken.
    """
    raise NotImplementedError(
        "'QHttpServerStream.__init__' has no cute function yet. Qt's "
        "'QHttpServerStream::QHttpServerStream(QIODevice *socket, "
        "QHttpServerRequestFilter *filter, QObject *parent)': leans on "
        "'QHttpServerStream::qt_metacall(QMetaObject::Call, int, void**)', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")

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

  @overload(int)
  def responderDestroyed(self, streamId: int) -> None:
    """
    Calls Qt's 'void QHttpServerStream::responderDestroyed(quint32
    streamId)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpserverstream.html#responderDestroyed

    Parameters
    ----------

    streamId : int
      Passed on as it is.
    """
    #  void QHttpServerStream::responderDestroyed(quint32 streamId)
    self.uglySide.call(
        'ritual_ZN17QHttpServerStream18responderDestroyedEj', streamId,
    )

  def startHandlingRequest(self) -> None:
    """
    Calls Qt's 'void QHttpServerStream::startHandlingRequest()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpserverstream.html#startHandlingRequest
    """
    #  void QHttpServerStream::startHandlingRequest()
    self.uglySide.call(
        'ritual_ZN17QHttpServerStream20startHandlingRequestEv',
    )

  def socketDisconnected(self) -> None:
    """
    Calls Qt's 'void QHttpServerStream::socketDisconnected()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpserverstream.html#socketDisconnected
    """
    #  void QHttpServerStream::socketDisconnected()
    self.uglySide.call('ritual_ZN17QHttpServerStream18socketDisconnectedEv')

  @overload(QByteArray, QHttpHeaders, QHttpServerResponder.StatusCode, int)
  def write(
      self,
      body: QByteArray,
      headers: QHttpHeaders,
      status: QHttpServerResponder.StatusCode,
      streamId: int,
  ) -> None:
    """
    Calls Qt's 'void QHttpServerStream::write(const QByteArray &body, const
    QHttpHeaders &headers, QHttpServerResponder::StatusCode status, quint32
    streamId)'.

    Qt's own words: https://doc.qt.io/qt-6/qhttpserverstream.html#write

    Parameters
    ----------

    body : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    headers : QHttpHeaders
      Passed on as a value: Qt reads the C++ QHttpHeaders, which stays
      Python's own.

    status : QHttpServerResponder.StatusCode
      Passed on as its number.

    streamId : int
      Passed on as it is.
    """
    #  void QHttpServerStream::write(const QByteArray &body, const
    #      QHttpHeaders &headers, QHttpServerResponder::StatusCode status,
    #      quint32 streamId)
    self.uglySide.call(
        'ritual_ZN17QHttpServerStream5writeERK10QByteArrayRK12QHttpHeadersN'
        '20QHttpServerResponder10StatusCodeEj',
        self._valueOf(body), self._valueOf(headers), status.value, streamId,
    )

  @overload(QHttpServerResponder.StatusCode, int)
  def write(
      self,
      status: QHttpServerResponder.StatusCode,
      streamId: int,
  ) -> None:
    """
    Calls Qt's 'void
    QHttpServerStream::write(QHttpServerResponder::StatusCode status, quint32
    streamId)'.

    Qt's own words: https://doc.qt.io/qt-6/qhttpserverstream.html#write

    Parameters
    ----------

    status : QHttpServerResponder.StatusCode
      Passed on as its number.

    streamId : int
      Passed on as it is.
    """
    #  void QHttpServerStream::write(QHttpServerResponder::StatusCode status,
    #      quint32 streamId)
    self.uglySide.call(
        'ritual_ZN17QHttpServerStream5writeEN20QHttpServerResponder10Status'
        'CodeEj',
        status.value, streamId,
    )

  @overload(QIODevice, QHttpHeaders, QHttpServerResponder.StatusCode, int)
  @overload(NoneType, QHttpHeaders, QHttpServerResponder.StatusCode, int)
  def write(
      self,
      data: Optional[QIODevice],
      headers: QHttpHeaders,
      status: QHttpServerResponder.StatusCode,
      streamId: int,
  ) -> None:
    """
    Calls Qt's 'void QHttpServerStream::write(QIODevice *data, const
    QHttpHeaders &headers, QHttpServerResponder::StatusCode status, quint32
    streamId)'.

    Qt's own words: https://doc.qt.io/qt-6/qhttpserverstream.html#write

    Parameters
    ----------

    data : Optional[QIODevice]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    headers : QHttpHeaders
      Passed on as a value: Qt reads the C++ QHttpHeaders, which stays
      Python's own.

    status : QHttpServerResponder.StatusCode
      Passed on as its number.

    streamId : int
      Passed on as it is.
    """
    #  void QHttpServerStream::write(QIODevice *data, const QHttpHeaders
    #      &headers, QHttpServerResponder::StatusCode status, quint32
    #      streamId)
    self.uglySide.call(
        'ritual_ZN17QHttpServerStream5writeEP9QIODeviceRK12QHttpHeadersN20Q'
        'HttpServerResponder10StatusCodeEj',
        self._addressOf(data), self._valueOf(headers), status.value,
        streamId,
    )

  @overload(QHttpHeaders, QHttpServerResponder.StatusCode, int)
  def writeBeginChunked(
      self,
      headers: QHttpHeaders,
      status: QHttpServerResponder.StatusCode,
      streamId: int,
  ) -> None:
    """
    Calls Qt's 'void QHttpServerStream::writeBeginChunked(const QHttpHeaders
    &headers, QHttpServerResponder::StatusCode status, quint32 streamId)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpserverstream.html#writeBeginChunked

    Parameters
    ----------

    headers : QHttpHeaders
      Passed on as a value: Qt reads the C++ QHttpHeaders, which stays
      Python's own.

    status : QHttpServerResponder.StatusCode
      Passed on as its number.

    streamId : int
      Passed on as it is.
    """
    #  void QHttpServerStream::writeBeginChunked(const QHttpHeaders &headers,
    #      QHttpServerResponder::StatusCode status, quint32 streamId)
    self.uglySide.call(
        'ritual_ZN17QHttpServerStream17writeBeginChunkedERK12QHttpHeadersN2'
        '0QHttpServerResponder10StatusCodeEj',
        self._valueOf(headers), status.value, streamId,
    )

  @overload(QByteArray, int)
  def writeChunk(self, body: QByteArray, streamId: int) -> None:
    """
    Calls Qt's 'void QHttpServerStream::writeChunk(const QByteArray &body,
    quint32 streamId)'.

    Qt's own words: https://doc.qt.io/qt-6/qhttpserverstream.html#writeChunk

    Parameters
    ----------

    body : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    streamId : int
      Passed on as it is.
    """
    #  void QHttpServerStream::writeChunk(const QByteArray &body, quint32
    #      streamId)
    self.uglySide.call(
        'ritual_ZN17QHttpServerStream10writeChunkERK10QByteArrayj',
        self._valueOf(body), streamId,
    )

  @overload(QByteArray, QHttpHeaders, int)
  def writeEndChunked(
      self,
      data: QByteArray,
      trailers: QHttpHeaders,
      streamId: int,
  ) -> None:
    """
    Calls Qt's 'void QHttpServerStream::writeEndChunked(const QByteArray
    &data, const QHttpHeaders &trailers, quint32 streamId)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpserverstream.html#writeEndChunked

    Parameters
    ----------

    data : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    trailers : QHttpHeaders
      Passed on as a value: Qt reads the C++ QHttpHeaders, which stays
      Python's own.

    streamId : int
      Passed on as it is.
    """
    #  void QHttpServerStream::writeEndChunked(const QByteArray &data, const
    #      QHttpHeaders &trailers, quint32 streamId)
    self.uglySide.call(
        'ritual_ZN17QHttpServerStream15writeEndChunkedERK10QByteArrayRK12QH'
        'ttpHeadersj',
        self._valueOf(data), self._valueOf(trailers), streamId,
    )

  @overload(QHttpServerResponderPrivate)
  @overload(NoneType)
  def connectResponder(
      self,
      responder: Optional[QHttpServerResponderPrivate],
  ) -> None:
    """
    Calls Qt's 'void
    QHttpServerStream::connectResponder(QHttpServerResponderPrivate
    *responder)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpserverstream.html#connectResponder

    Parameters
    ----------

    responder : Optional[QHttpServerResponderPrivate]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QHttpServerStream::connectResponder(QHttpServerResponderPrivate
    #      *responder)
    self.uglySide.call(
        'ritual_ZN17QHttpServerStream16connectResponderEP27QHttpServerRespo'
        'nderPrivate',
        self._addressOf(responder),
    )

  @overload(int)
  def disconnectResponder(self, streamId: int) -> None:
    """
    Calls Qt's 'void QHttpServerStream::disconnectResponder(quint32
    streamId)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpserverstream.html#disconnectResponder

    Parameters
    ----------

    streamId : int
      Passed on as it is.
    """
    #  void QHttpServerStream::disconnectResponder(quint32 streamId)
    self.uglySide.call(
        'ritual_ZN17QHttpServerStream19disconnectResponderEj', streamId,
    )
