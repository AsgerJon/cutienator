"""
QHttpNetworkReplyPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtNetwork/6.12.0/QtNetwork/private/qhttpnetworkreply_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QHttpNetworkReplyPrivate to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import QObjectPrivate
from . import QHttpNetworkHeaderPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QByteArray, QByteArrayView, QIODevice, QUrl
  from . import QByteDataBuffer
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']
  QByteArrayView = WAIT['QByteArrayView']
  QByteDataBuffer = WAIT['QByteDataBuffer']
  QIODevice = WAIT['QIODevice']
  QUrl = WAIT['QUrl']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QHttpNetworkReplyPrivate(QObjectPrivate, QHttpNetworkHeaderPrivate):
  """
  The cute side of Qt's QHttpNetworkReplyPrivate: a plain Python object
  standing in front of one C++ QHttpNetworkReplyPrivate.

  It is built on the cute 'QObjectPrivate', as Qt's QHttpNetworkReplyPrivate
  is built on Qt's QObjectPrivate, and has everything that class has. It is
  built on the cute 'QHttpNetworkHeaderPrivate' as well, as Qt's
  QHttpNetworkReplyPrivate is built on Qt's QHttpNetworkHeaderPrivate too,
  and has everything that class has.

  What exists
  -----------

  Every function of Qt's QHttpNetworkReplyPrivate that has a ritual and that
  Python can call so far, 20 names in all: 'readStatus', 'parseStatus',
  'readHeader', 'parseHeader', 'appendHeaderField', 'readBody',
  'readBodyFast', 'clear', 'clearHttpLayerInformation', 'readReplyBodyRaw',
  'readReplyBodyChunked', 'isRedirecting', 'shouldEmitSignals',
  'expectContent', 'eraseData', 'bytesAvailable', 'isChunked',
  'isConnectionCloseEnabled', 'isCompressed', 'removeAutoDecompressHeader'.
  It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QHttpNetworkReplyPrivate::~QHttpNetworkReplyPrivate()': the
    destructor: Python never removes a C++ QHttpNetworkReplyPrivate.
  - Qt's 'qint64 QHttpNetworkReplyPrivate::readBodyVeryFast(QIODevice
    *socket, char *b)': names 'char', which has no cute class yet.
  - Qt's 'qint64 QHttpNetworkReplyPrivate::getChunkSize(QIODevice *in, qint64
    *chunkSize)': takes a number to change where it is.

  What to expect
  --------------

  - The C++ QHttpNetworkReplyPrivate is created at the first use, not by
    'QHttpNetworkReplyPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QHttpNetworkReplyPrivate.
  - Each name of Qt's QHttpNetworkReplyPrivate that has no cute function yet,
    'getChunkSize', 'readBodyVeryFast', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QHttpNetworkReplyPrivate, each a class in
  #  here as in C++, and the names Qt has for the combinations of its flags
  #  enums.

  class ReplyState(CuteNum):
    """
    The enum 'QHttpNetworkReplyPrivate::ReplyState' of Qt, with the 6 names
    Qt gives in it.
    """

    NothingDoneState = Kee[int](0)
    ReadingStatusState = Kee[int](1)
    ReadingHeaderState = Kee[int](2)
    ReadingDataState = Kee[int](3)
    AllDoneState = Kee[int](4)
    Aborted = Kee[int](5)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QHttpNetworkReplyPrivate'

  #  Qt's QHttpNetworkReplyPrivate is built on more than one class. The part
  #  of a C++ QHttpNetworkReplyPrivate that belongs to a class after the
  #  first begins somewhere inside the object, and the ritual named for that
  #  class gives where; see 'CuteMixin._addressAs'.
  __cast_rituals__ = {
      'QHttpNetworkHeaderPrivate':
          'ritual_cast_QHttpNetworkReplyPrivate_QHttpNetworkHeaderPrivate',
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isRedirecting(self) -> bool:
    """
    Calls Qt's 'bool QHttpNetworkReplyPrivate::isRedirecting() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpnetworkreplyprivate.html#isRedirecting
    """
    #  bool QHttpNetworkReplyPrivate::isRedirecting() const
    return self.uglySide.call(
        'ritual_ZNK24QHttpNetworkReplyPrivate13isRedirectingEv',
    )

  def bytesAvailable(self) -> int:
    """
    Calls Qt's 'qint64 QHttpNetworkReplyPrivate::bytesAvailable() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpnetworkreplyprivate.html#bytesAvailable
    """
    #  qint64 QHttpNetworkReplyPrivate::bytesAvailable() const
    return self.uglySide.call(
        'ritual_ZNK24QHttpNetworkReplyPrivate14bytesAvailableEv',
    )

  def isCompressed(self) -> bool:
    """
    Calls Qt's 'bool QHttpNetworkReplyPrivate::isCompressed() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpnetworkreplyprivate.html#isCompressed
    """
    #  bool QHttpNetworkReplyPrivate::isCompressed() const
    return self.uglySide.call(
        'ritual_ZNK24QHttpNetworkReplyPrivate12isCompressedEv',
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
  @overload(QUrl)
  def __init__(self, newUrl: Optional[QUrl] = None) -> None:
    """
    Notes what was given, for Qt's
    'QHttpNetworkReplyPrivate::QHttpNetworkReplyPrivate(const QUrl &newUrl)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpnetworkreplyprivate.html

    Parameters
    ----------

    newUrl : Optional[QUrl]
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
      May be left out, as in Qt: a new 'QUrl()' is then passed on.
    """
    #  QHttpNetworkReplyPrivate::QHttpNetworkReplyPrivate(const QUrl &newUrl)
    if newUrl is None:
      from ..QtCore import QUrl
      newUrl = QUrl()
    self._noteCreation(QHttpNetworkReplyPrivate, lambda: Rituals.call(
        'ritual_ZN24QHttpNetworkReplyPrivateC1ERK4QUrl',
        self._valueOf(newUrl),
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

  @overload(QIODevice)
  @overload(NoneType)
  def readStatus(self, socket: Optional[QIODevice]) -> int:
    """
    Calls Qt's 'qint64 QHttpNetworkReplyPrivate::readStatus(QIODevice
    *socket)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpnetworkreplyprivate.html#readStatus

    Parameters
    ----------

    socket : Optional[QIODevice]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  qint64 QHttpNetworkReplyPrivate::readStatus(QIODevice *socket)
    return self.uglySide.call(
        'ritual_ZN24QHttpNetworkReplyPrivate10readStatusEP9QIODevice',
        self._addressOf(socket),
    )

  @overload(QByteArrayView)
  def parseStatus(self, status: QByteArrayView) -> bool:
    """
    Calls Qt's 'bool QHttpNetworkReplyPrivate::parseStatus(QByteArrayView
    status)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpnetworkreplyprivate.html#parseStatus

    Parameters
    ----------

    status : QByteArrayView
      Passed on as a value: Qt reads the C++ QByteArrayView, which stays
      Python's own.
    """
    #  bool QHttpNetworkReplyPrivate::parseStatus(QByteArrayView status)
    return self.uglySide.call(
        'ritual_ZN24QHttpNetworkReplyPrivate11parseStatusE14QByteArrayView',
        self._valueOf(status),
    )

  @overload(QIODevice)
  @overload(NoneType)
  def readHeader(self, socket: Optional[QIODevice]) -> int:
    """
    Calls Qt's 'qint64 QHttpNetworkReplyPrivate::readHeader(QIODevice
    *socket)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpnetworkreplyprivate.html#readHeader

    Parameters
    ----------

    socket : Optional[QIODevice]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  qint64 QHttpNetworkReplyPrivate::readHeader(QIODevice *socket)
    return self.uglySide.call(
        'ritual_ZN24QHttpNetworkReplyPrivate10readHeaderEP9QIODevice',
        self._addressOf(socket),
    )

  @overload(QByteArrayView)
  def parseHeader(self, header: QByteArrayView) -> None:
    """
    Calls Qt's 'void QHttpNetworkReplyPrivate::parseHeader(QByteArrayView
    header)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpnetworkreplyprivate.html#parseHeader

    Parameters
    ----------

    header : QByteArrayView
      Passed on as a value: Qt reads the C++ QByteArrayView, which stays
      Python's own.
    """
    #  void QHttpNetworkReplyPrivate::parseHeader(QByteArrayView header)
    self.uglySide.call(
        'ritual_ZN24QHttpNetworkReplyPrivate11parseHeaderE14QByteArrayView',
        self._valueOf(header),
    )

  @overload(QByteArray, QByteArray)
  def appendHeaderField(self, name: QByteArray, data: QByteArray) -> None:
    """
    Calls Qt's 'void QHttpNetworkReplyPrivate::appendHeaderField(const
    QByteArray &name, const QByteArray &data)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpnetworkreplyprivate.html#appendHeaderField

    Parameters
    ----------

    name : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    data : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void QHttpNetworkReplyPrivate::appendHeaderField(const QByteArray
    #      &name, const QByteArray &data)
    self.uglySide.call(
        'ritual_ZN24QHttpNetworkReplyPrivate17appendHeaderFieldERK10QByteAr'
        'rayS2_',
        self._valueOf(name), self._valueOf(data),
    )

  @overload(QIODevice, QByteDataBuffer)
  @overload(QIODevice, NoneType)
  @overload(NoneType, QByteDataBuffer)
  @overload(NoneType, NoneType)
  def readBody(
      self,
      socket: Optional[QIODevice],
      out: Optional[QByteDataBuffer],
  ) -> int:
    """
    Calls Qt's 'qint64 QHttpNetworkReplyPrivate::readBody(QIODevice *socket,
    QByteDataBuffer *out)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpnetworkreplyprivate.html#readBody

    Parameters
    ----------

    socket : Optional[QIODevice]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    out : Optional[QByteDataBuffer]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  qint64 QHttpNetworkReplyPrivate::readBody(QIODevice *socket,
    #      QByteDataBuffer *out)
    return self.uglySide.call(
        'ritual_ZN24QHttpNetworkReplyPrivate8readBodyEP9QIODeviceP15QByteDa'
        'taBuffer',
        self._addressOf(socket), self._addressOf(out),
    )

  @overload(QIODevice, QByteDataBuffer)
  @overload(QIODevice, NoneType)
  @overload(NoneType, QByteDataBuffer)
  @overload(NoneType, NoneType)
  def readBodyFast(
      self,
      socket: Optional[QIODevice],
      rb: Optional[QByteDataBuffer],
  ) -> int:
    """
    Calls Qt's 'qint64 QHttpNetworkReplyPrivate::readBodyFast(QIODevice
    *socket, QByteDataBuffer *rb)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpnetworkreplyprivate.html#readBodyFast

    Parameters
    ----------

    socket : Optional[QIODevice]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    rb : Optional[QByteDataBuffer]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  qint64 QHttpNetworkReplyPrivate::readBodyFast(QIODevice *socket,
    #      QByteDataBuffer *rb)
    return self.uglySide.call(
        'ritual_ZN24QHttpNetworkReplyPrivate12readBodyFastEP9QIODeviceP15QB'
        'yteDataBuffer',
        self._addressOf(socket), self._addressOf(rb),
    )

  def clear(self) -> None:
    """
    Calls Qt's 'void QHttpNetworkReplyPrivate::clear()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpnetworkreplyprivate.html#clear
    """
    #  void QHttpNetworkReplyPrivate::clear()
    self.uglySide.call('ritual_ZN24QHttpNetworkReplyPrivate5clearEv')

  def clearHttpLayerInformation(self) -> None:
    """
    Calls Qt's 'void QHttpNetworkReplyPrivate::clearHttpLayerInformation()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpnetworkreplyprivate.html
    """
    #  void QHttpNetworkReplyPrivate::clearHttpLayerInformation()
    self.uglySide.call(
        'ritual_ZN24QHttpNetworkReplyPrivate25clearHttpLayerInformationEv',
    )

  @overload(QIODevice, QByteDataBuffer, int)
  @overload(QIODevice, NoneType, int)
  @overload(NoneType, QByteDataBuffer, int)
  @overload(NoneType, NoneType, int)
  def readReplyBodyRaw(
      self,
      in_: Optional[QIODevice],
      out: Optional[QByteDataBuffer],
      size: int,
  ) -> int:
    """
    Calls Qt's 'qint64 QHttpNetworkReplyPrivate::readReplyBodyRaw(QIODevice
    *in, QByteDataBuffer *out, qint64 size)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpnetworkreplyprivate.html#readReplyBodyRaw

    Parameters
    ----------

    in_ : Optional[QIODevice]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    out : Optional[QByteDataBuffer]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    size : int
      Passed on as it is.
    """
    #  qint64 QHttpNetworkReplyPrivate::readReplyBodyRaw(QIODevice *in,
    #      QByteDataBuffer *out, qint64 size)
    return self.uglySide.call(
        'ritual_ZN24QHttpNetworkReplyPrivate16readReplyBodyRawEP9QIODeviceP'
        '15QByteDataBufferx',
        self._addressOf(in_), self._addressOf(out), size,
    )

  @overload(QIODevice, QByteDataBuffer)
  @overload(QIODevice, NoneType)
  @overload(NoneType, QByteDataBuffer)
  @overload(NoneType, NoneType)
  def readReplyBodyChunked(
      self,
      in_: Optional[QIODevice],
      out: Optional[QByteDataBuffer],
  ) -> int:
    """
    Calls Qt's 'qint64
    QHttpNetworkReplyPrivate::readReplyBodyChunked(QIODevice *in,
    QByteDataBuffer *out)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpnetworkreplyprivate.html#readReplyBodyChunked

    Parameters
    ----------

    in_ : Optional[QIODevice]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    out : Optional[QByteDataBuffer]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  qint64 QHttpNetworkReplyPrivate::readReplyBodyChunked(QIODevice *in,
    #      QByteDataBuffer *out)
    return self.uglySide.call(
        'ritual_ZN24QHttpNetworkReplyPrivate20readReplyBodyChunkedEP9QIODev'
        'iceP15QByteDataBuffer',
        self._addressOf(in_), self._addressOf(out),
    )

  def shouldEmitSignals(self) -> bool:
    """
    Calls Qt's 'bool QHttpNetworkReplyPrivate::shouldEmitSignals()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpnetworkreplyprivate.html#shouldEmitSignals
    """
    #  bool QHttpNetworkReplyPrivate::shouldEmitSignals()
    return self.uglySide.call(
        'ritual_ZN24QHttpNetworkReplyPrivate17shouldEmitSignalsEv',
    )

  def expectContent(self) -> bool:
    """
    Calls Qt's 'bool QHttpNetworkReplyPrivate::expectContent()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpnetworkreplyprivate.html#expectContent
    """
    #  bool QHttpNetworkReplyPrivate::expectContent()
    return self.uglySide.call(
        'ritual_ZN24QHttpNetworkReplyPrivate13expectContentEv',
    )

  def eraseData(self) -> None:
    """
    Calls Qt's 'void QHttpNetworkReplyPrivate::eraseData()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpnetworkreplyprivate.html#eraseData
    """
    #  void QHttpNetworkReplyPrivate::eraseData()
    self.uglySide.call('ritual_ZN24QHttpNetworkReplyPrivate9eraseDataEv')

  def isChunked(self) -> bool:
    """
    Calls Qt's 'bool QHttpNetworkReplyPrivate::isChunked()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpnetworkreplyprivate.html#isChunked
    """
    #  bool QHttpNetworkReplyPrivate::isChunked()
    return self.uglySide.call(
        'ritual_ZN24QHttpNetworkReplyPrivate9isChunkedEv',
    )

  def isConnectionCloseEnabled(self) -> bool:
    """
    Calls Qt's 'bool QHttpNetworkReplyPrivate::isConnectionCloseEnabled()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpnetworkreplyprivate.html
    """
    #  bool QHttpNetworkReplyPrivate::isConnectionCloseEnabled()
    return self.uglySide.call(
        'ritual_ZN24QHttpNetworkReplyPrivate24isConnectionCloseEnabledEv',
    )

  def removeAutoDecompressHeader(self) -> None:
    """
    Calls Qt's 'void QHttpNetworkReplyPrivate::removeAutoDecompressHeader()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpnetworkreplyprivate.html
    """
    #  void QHttpNetworkReplyPrivate::removeAutoDecompressHeader()
    self.uglySide.call(
        'ritual_ZN24QHttpNetworkReplyPrivate26removeAutoDecompressHeaderEv',
    )

  @staticmethod
  def getChunkSize(*__, **_) -> Never:
    """
    Qt's 'qint64 QHttpNetworkReplyPrivate::getChunkSize(QIODevice *in, qint64
    *chunkSize)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QHttpNetworkReplyPrivate.getChunkSize' has no cute function yet. "
        "Qt's 'qint64 QHttpNetworkReplyPrivate::getChunkSize(QIODevice *in, "
        "qint64 *chunkSize)': takes a number to change where it is.")

  @staticmethod
  def readBodyVeryFast(*__, **_) -> Never:
    """
    Qt's 'qint64 QHttpNetworkReplyPrivate::readBodyVeryFast(QIODevice
    *socket, char *b)': names 'char', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QHttpNetworkReplyPrivate.readBodyVeryFast' has no cute function "
        "yet. Qt's 'qint64 "
        "QHttpNetworkReplyPrivate::readBodyVeryFast(QIODevice *socket, char "
        "*b)': names 'char', which has no cute class yet.")
