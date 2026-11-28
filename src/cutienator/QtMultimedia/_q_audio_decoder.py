"""
QAudioDecoder binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtMultimedia/qaudiodecoder.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QIODevice, QMetaObject, QUrl
  from . import QAudioBuffer, QAudioDecoderPrivate, QAudioFormat
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QAudioFormat = WAIT['QAudioFormat']
  QIODevice = WAIT['QIODevice']
  QUrl = WAIT['QUrl']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QAudioDecoder(QObject):
  """
  The cute side of Qt's QAudioDecoder: a plain Python object standing in
  front of one C++ QAudioDecoder.

  It is built on the cute 'QObject', as Qt's QAudioDecoder is built on Qt's
  QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QAudioDecoder that has a ritual and that Python can
  call so far, 27 names in all: 'metaObject', 'tr', 'isSupported',
  'isDecoding', 'source', 'setSource', 'sourceDevice', 'setSourceDevice',
  'audioFormat', 'setAudioFormat', 'error', 'errorString', 'read',
  'bufferAvailable', 'position', 'duration', 'start', 'stop',
  'bufferAvailableChanged', 'bufferReady', 'finished', 'isDecodingChanged',
  'formatChanged', 'sourceChanged', 'positionChanged', 'durationChanged',
  'd_func'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QAudioDecoder::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QAudioDecoder::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QAudioDecoder::~QAudioDecoder()': the destructor: Python never
    removes a C++ QAudioDecoder.
  - Qt's 'const QAudioDecoderPrivate *QAudioDecoder::d_func() const': takes
    in Python what 'QAudioDecoderPrivate *QAudioDecoder::d_func()' takes.

  What has no ritual
  ------------------

  4 of the 37 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QAudioDecoder is created at the first use, not by
    'QAudioDecoder(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QAudioDecoder.
  - Qt tells when it has removed the C++ QAudioDecoder. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  #  The enums Qt writes inside QAudioDecoder, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class Error(CuteNum):
    """
    The enum 'QAudioDecoder::Error' of Qt, with the 5 names Qt gives in it.
    """

    NoError = Kee[int](0)
    ResourceError = Kee[int](1)
    FormatError = Kee[int](2)
    AccessDeniedError = Kee[int](3)
    NotSupportedError = Kee[int](4)

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
    Calls Qt's 'QString QAudioDecoder::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qaudiodecoder.html#tr

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
    #  QString QAudioDecoder::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN13QAudioDecoder2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QAudioDecoder'

  #  A C++ QAudioDecoder Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QAudioDecoder'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QAudioDecoder::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qaudiodecoder.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QAudioDecoder::metaObject() const
    address = self.uglySide.call('ritual_ZNK13QAudioDecoder10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def isSupported(self) -> bool:
    """
    Calls Qt's 'bool QAudioDecoder::isSupported() const'.

    Qt's own words: https://doc.qt.io/qt-6/qaudiodecoder.html#isSupported
    """
    #  bool QAudioDecoder::isSupported() const
    return self.uglySide.call('ritual_ZNK13QAudioDecoder11isSupportedEv')

  def isDecoding(self) -> bool:
    """
    Calls Qt's 'bool QAudioDecoder::isDecoding() const'.

    Qt's own words: https://doc.qt.io/qt-6/qaudiodecoder.html#isDecoding
    """
    #  bool QAudioDecoder::isDecoding() const
    return self.uglySide.call('ritual_ZNK13QAudioDecoder10isDecodingEv')

  def source(self) -> QUrl:
    """
    Calls Qt's 'QUrl QAudioDecoder::source() const'.

    Qt's own words: https://doc.qt.io/qt-6/qaudiodecoder.html#source

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QAudioDecoder::source() const
    address = self.uglySide.call('ritual_ZNK13QAudioDecoder6sourceEv')
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  def sourceDevice(self) -> Optional[QIODevice]:
    """
    Calls Qt's 'QIODevice *QAudioDecoder::sourceDevice() const'.

    Qt's own words: https://doc.qt.io/qt-6/qaudiodecoder.html#sourceDevice

    Returns
    -------

    Optional[QIODevice]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QIODevice *QAudioDecoder::sourceDevice() const
    address = self.uglySide.call('ritual_ZNK13QAudioDecoder12sourceDeviceEv')
    from ..QtCore import QIODevice
    return QIODevice._cuteAt(address)

  def audioFormat(self) -> QAudioFormat:
    """
    Calls Qt's 'QAudioFormat QAudioDecoder::audioFormat() const'.

    Qt's own words: https://doc.qt.io/qt-6/qaudiodecoder.html#audioFormat

    Returns
    -------

    QAudioFormat
      A new cute QAudioFormat around the copy Qt gave back. Python owns it.
    """
    #  QAudioFormat QAudioDecoder::audioFormat() const
    address = self.uglySide.call('ritual_ZNK13QAudioDecoder11audioFormatEv')
    from . import QAudioFormat
    return QAudioFormat._cuteOwning(address)

  @overload()
  def error(self) -> Error:
    """
    Calls Qt's 'Error QAudioDecoder::error() const'.

    Qt's own words: https://doc.qt.io/qt-6/qaudiodecoder.html#error

    Returns
    -------

    Error
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Error(number)' gives.
    """
    #  Error QAudioDecoder::error() const
    return QAudioDecoder.Error(self.uglySide.call(
        'ritual_ZNK13QAudioDecoder5errorEv',
    ))

  @overload(Error)
  def error(self, error: Error) -> None:
    """
    Calls Qt's 'void QAudioDecoder::error(QAudioDecoder::Error error)'.

    Qt's own words: https://doc.qt.io/qt-6/qaudiodecoder.html#error

    Parameters
    ----------

    error : Error
      Passed on as its number.
    """
    #  void QAudioDecoder::error(QAudioDecoder::Error error)
    self.uglySide.call(
        'ritual_ZN13QAudioDecoder5errorENS_5ErrorE', error.value,
    )

  def errorString(self) -> str:
    """
    Calls Qt's 'QString QAudioDecoder::errorString() const'.

    Qt's own words: https://doc.qt.io/qt-6/qaudiodecoder.html#errorString

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QAudioDecoder::errorString() const
    return self.uglySide.call('ritual_ZNK13QAudioDecoder11errorStringEv')

  def read(self) -> QAudioBuffer:
    """
    Calls Qt's 'QAudioBuffer QAudioDecoder::read() const'.

    Qt's own words: https://doc.qt.io/qt-6/qaudiodecoder.html#read

    Returns
    -------

    QAudioBuffer
      A new cute QAudioBuffer around the copy Qt gave back. Python owns it.
    """
    #  QAudioBuffer QAudioDecoder::read() const
    address = self.uglySide.call('ritual_ZNK13QAudioDecoder4readEv')
    from . import QAudioBuffer
    return QAudioBuffer._cuteOwning(address)

  def bufferAvailable(self) -> bool:
    """
    Calls Qt's 'bool QAudioDecoder::bufferAvailable() const'.

    Qt's own words: https://doc.qt.io/qt-6/qaudiodecoder.html#bufferAvailable
    """
    #  bool QAudioDecoder::bufferAvailable() const
    return self.uglySide.call('ritual_ZNK13QAudioDecoder15bufferAvailableEv')

  def position(self) -> int:
    """
    Calls Qt's 'qint64 QAudioDecoder::position() const'.

    Qt's own words: https://doc.qt.io/qt-6/qaudiodecoder.html#position
    """
    #  qint64 QAudioDecoder::position() const
    return self.uglySide.call('ritual_ZNK13QAudioDecoder8positionEv')

  def duration(self) -> int:
    """
    Calls Qt's 'qint64 QAudioDecoder::duration() const'.

    Qt's own words: https://doc.qt.io/qt-6/qaudiodecoder.html#duration
    """
    #  qint64 QAudioDecoder::duration() const
    return self.uglySide.call('ritual_ZNK13QAudioDecoder8durationEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QUrl)
  def setSource(self, fileName: QUrl) -> None:
    """
    Calls Qt's 'void QAudioDecoder::setSource(const QUrl &fileName)'.

    Qt's own words: https://doc.qt.io/qt-6/qaudiodecoder.html#setSource

    Parameters
    ----------

    fileName : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  void QAudioDecoder::setSource(const QUrl &fileName)
    self.uglySide.call(
        'ritual_ZN13QAudioDecoder9setSourceERK4QUrl',
        self._valueOf(fileName),
    )

  @overload(QIODevice)
  @overload(NoneType)
  def setSourceDevice(self, device: Optional[QIODevice]) -> None:
    """
    Calls Qt's 'void QAudioDecoder::setSourceDevice(QIODevice *device)'.

    Qt's own words: https://doc.qt.io/qt-6/qaudiodecoder.html#setSourceDevice

    Parameters
    ----------

    device : Optional[QIODevice]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAudioDecoder::setSourceDevice(QIODevice *device)
    self.uglySide.call(
        'ritual_ZN13QAudioDecoder15setSourceDeviceEP9QIODevice',
        self._addressOf(device),
    )

  @overload(QAudioFormat)
  def setAudioFormat(self, format: QAudioFormat) -> None:
    """
    Calls Qt's 'void QAudioDecoder::setAudioFormat(const QAudioFormat
    &format)'.

    Qt's own words: https://doc.qt.io/qt-6/qaudiodecoder.html#setAudioFormat

    Parameters
    ----------

    format : QAudioFormat
      Passed on as a value: Qt reads the C++ QAudioFormat, which stays
      Python's own.
    """
    #  void QAudioDecoder::setAudioFormat(const QAudioFormat &format)
    self.uglySide.call(
        'ritual_ZN13QAudioDecoder14setAudioFormatERK12QAudioFormat',
        self._valueOf(format),
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
    Notes what was given, for Qt's 'QAudioDecoder::QAudioDecoder(QObject
    *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qaudiodecoder.html#QAudioDecoder

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QAudioDecoder::QAudioDecoder(QObject *parent)
    self._noteCreation(QAudioDecoder, lambda: Rituals.call(
        'ritual_ZN13QAudioDecoderC1EP7QObject',
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

  def start(self) -> None:
    """
    Calls Qt's 'void QAudioDecoder::start()'.

    Qt's own words: https://doc.qt.io/qt-6/qaudiodecoder.html#start
    """
    #  void QAudioDecoder::start()
    self.uglySide.call('ritual_ZN13QAudioDecoder5startEv')

  def stop(self) -> None:
    """
    Calls Qt's 'void QAudioDecoder::stop()'.

    Qt's own words: https://doc.qt.io/qt-6/qaudiodecoder.html#stop
    """
    #  void QAudioDecoder::stop()
    self.uglySide.call('ritual_ZN13QAudioDecoder4stopEv')

  @overload(bool)
  def bufferAvailableChanged(self, a0: bool) -> None:
    """
    Calls Qt's 'void QAudioDecoder::bufferAvailableChanged(bool a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaudiodecoder.html#bufferAvailableChanged

    Parameters
    ----------

    a0 : bool
      Passed on as it is.
    """
    #  void QAudioDecoder::bufferAvailableChanged(bool a0)
    self.uglySide.call(
        'ritual_ZN13QAudioDecoder22bufferAvailableChangedEb', a0,
    )

  def bufferReady(self) -> None:
    """
    Calls Qt's 'void QAudioDecoder::bufferReady()'.

    Qt's own words: https://doc.qt.io/qt-6/qaudiodecoder.html#bufferReady
    """
    #  void QAudioDecoder::bufferReady()
    self.uglySide.call('ritual_ZN13QAudioDecoder11bufferReadyEv')

  def finished(self) -> None:
    """
    Calls Qt's 'void QAudioDecoder::finished()'.

    Qt's own words: https://doc.qt.io/qt-6/qaudiodecoder.html#finished
    """
    #  void QAudioDecoder::finished()
    self.uglySide.call('ritual_ZN13QAudioDecoder8finishedEv')

  @overload(bool)
  def isDecodingChanged(self, a0: bool) -> None:
    """
    Calls Qt's 'void QAudioDecoder::isDecodingChanged(bool a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaudiodecoder.html#isDecodingChanged

    Parameters
    ----------

    a0 : bool
      Passed on as it is.
    """
    #  void QAudioDecoder::isDecodingChanged(bool a0)
    self.uglySide.call('ritual_ZN13QAudioDecoder17isDecodingChangedEb', a0)

  @overload(QAudioFormat)
  def formatChanged(self, format: QAudioFormat) -> None:
    """
    Calls Qt's 'void QAudioDecoder::formatChanged(const QAudioFormat
    &format)'.

    Qt's own words: https://doc.qt.io/qt-6/qaudiodecoder.html#formatChanged

    Parameters
    ----------

    format : QAudioFormat
      Passed on as a value: Qt reads the C++ QAudioFormat, which stays
      Python's own.
    """
    #  void QAudioDecoder::formatChanged(const QAudioFormat &format)
    self.uglySide.call(
        'ritual_ZN13QAudioDecoder13formatChangedERK12QAudioFormat',
        self._valueOf(format),
    )

  def sourceChanged(self) -> None:
    """
    Calls Qt's 'void QAudioDecoder::sourceChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qaudiodecoder.html#sourceChanged
    """
    #  void QAudioDecoder::sourceChanged()
    self.uglySide.call('ritual_ZN13QAudioDecoder13sourceChangedEv')

  @overload(int)
  def positionChanged(self, position: int) -> None:
    """
    Calls Qt's 'void QAudioDecoder::positionChanged(qint64 position)'.

    Qt's own words: https://doc.qt.io/qt-6/qaudiodecoder.html#positionChanged

    Parameters
    ----------

    position : int
      Passed on as it is.
    """
    #  void QAudioDecoder::positionChanged(qint64 position)
    self.uglySide.call(
        'ritual_ZN13QAudioDecoder15positionChangedEx', position,
    )

  @overload(int)
  def durationChanged(self, duration: int) -> None:
    """
    Calls Qt's 'void QAudioDecoder::durationChanged(qint64 duration)'.

    Qt's own words: https://doc.qt.io/qt-6/qaudiodecoder.html#durationChanged

    Parameters
    ----------

    duration : int
      Passed on as it is.
    """
    #  void QAudioDecoder::durationChanged(qint64 duration)
    self.uglySide.call(
        'ritual_ZN13QAudioDecoder15durationChangedEx', duration,
    )

  def d_func(self) -> Optional[QAudioDecoderPrivate]:
    """
    Calls Qt's 'QAudioDecoderPrivate *QAudioDecoder::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qaudiodecoder.html#d_func

    Returns
    -------

    Optional[QAudioDecoderPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAudioDecoderPrivate *QAudioDecoder::d_func()
    address = self.uglySide.call('ritual_ZN13QAudioDecoder6d_funcEv')
    from . import QAudioDecoderPrivate
    return QAudioDecoderPrivate._cuteAt(address)
