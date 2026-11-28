"""
QWaveDecoder binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtMultimedia/qwavedecoder.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QIODevice, QIODeviceBase, QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from . import QAudioFormat
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QAudioFormat = WAIT['QAudioFormat']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QWaveDecoder(QIODevice):
  """
  The cute side of Qt's QWaveDecoder: a plain Python object standing in front
  of one C++ QWaveDecoder.

  It is built on the cute 'QIODevice', as Qt's QWaveDecoder is built on Qt's
  QIODevice, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QWaveDecoder that has a ritual and that Python can
  call so far, 21 names in all: 'metaObject', 'tr', 'audioFormat',
  'getDevice', 'duration', 'headerLength', 'open', 'close', 'seek', 'pos',
  'setIODevice', 'size', 'isSequential', 'bytesAvailable', 'formatKnown',
  'parsingError', 'handleData', 'writeData', 'writeHeader',
  'writeDataLength', 'parsingFailed'. It can be made from Python, in 2 ways;
  see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QWaveDecoder::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QWaveDecoder::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QWaveDecoder::~QWaveDecoder()': the destructor: Python never
    removes a C++ QWaveDecoder.
  - Qt's 'qint64 QWaveDecoder::readData(char *data, qint64 maxlen)': names
    'char', which has no cute class yet.

  What has no ritual
  ------------------

  2 of the 29 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QWaveDecoder is created at the first use, not by
    'QWaveDecoder(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QWaveDecoder.
  - Qt tells when it has removed the C++ QWaveDecoder. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
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
    Calls Qt's 'QString QWaveDecoder::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qwavedecoder.html#tr

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
    #  QString QWaveDecoder::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN12QWaveDecoder2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  def headerLength() -> int:
    """
    Calls Qt's 'qint64 QWaveDecoder::headerLength()'.

    Qt's own words: https://doc.qt.io/qt-6/qwavedecoder.html#headerLength
    """
    #  qint64 QWaveDecoder::headerLength()
    return Rituals.call('ritual_ZN12QWaveDecoder12headerLengthEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QWaveDecoder'

  #  A C++ QWaveDecoder Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QWaveDecoder'

  #  The functions Qt calls itself that QWaveDecoder is the first to declare.
  #  A class of a program built on it can write one anew, and Qt then calls
  #  that. For each name: the key C++ knows the function by, what it gives,
  #  and what it takes.
  __virtual_functions__ = {
      'open': (
          ('_ZN12QWaveDecoder4openE6QFlagsIN13QIODeviceBase12OpenModeFlagEE',
           ('bool', 'number', ''),
           (
               ('int', 'flags', 'QtCore:QIODeviceBase.OpenModeFlag'),
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
    Calls Qt's 'const QMetaObject *QWaveDecoder::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwavedecoder.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QWaveDecoder::metaObject() const
    address = self.uglySide.call('ritual_ZNK12QWaveDecoder10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def audioFormat(self) -> QAudioFormat:
    """
    Calls Qt's 'QAudioFormat QWaveDecoder::audioFormat() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwavedecoder.html#audioFormat

    Returns
    -------

    QAudioFormat
      A new cute QAudioFormat around the copy Qt gave back. Python owns it.
    """
    #  QAudioFormat QWaveDecoder::audioFormat() const
    address = self.uglySide.call('ritual_ZNK12QWaveDecoder11audioFormatEv')
    from . import QAudioFormat
    return QAudioFormat._cuteOwning(address)

  def duration(self) -> int:
    """
    Calls Qt's 'int QWaveDecoder::duration() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwavedecoder.html#duration
    """
    #  int QWaveDecoder::duration() const
    return self.uglySide.call('ritual_ZNK12QWaveDecoder8durationEv')

  def pos(self) -> int:
    """
    Calls Qt's 'qint64 QWaveDecoder::pos() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwavedecoder.html#pos
    """
    #  qint64 QWaveDecoder::pos() const
    ritual = 'ritual_ZNK12QWaveDecoder3posEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK12QWaveDecoder3posEv'
    return self.uglySide.call(ritual)

  def size(self) -> int:
    """
    Calls Qt's 'qint64 QWaveDecoder::size() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwavedecoder.html#size
    """
    #  qint64 QWaveDecoder::size() const
    ritual = 'ritual_ZNK12QWaveDecoder4sizeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK12QWaveDecoder4sizeEv'
    return self.uglySide.call(ritual)

  def isSequential(self) -> bool:
    """
    Calls Qt's 'bool QWaveDecoder::isSequential() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwavedecoder.html#isSequential
    """
    #  bool QWaveDecoder::isSequential() const
    ritual = 'ritual_ZNK12QWaveDecoder12isSequentialEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK12QWaveDecoder12isSequentialEv'
    return self.uglySide.call(ritual)

  def bytesAvailable(self) -> int:
    """
    Calls Qt's 'qint64 QWaveDecoder::bytesAvailable() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwavedecoder.html#bytesAvailable
    """
    #  qint64 QWaveDecoder::bytesAvailable() const
    ritual = 'ritual_ZNK12QWaveDecoder14bytesAvailableEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK12QWaveDecoder14bytesAvailableEv'
    return self.uglySide.call(ritual)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QIODevice)
  @overload(NoneType)
  def setIODevice(self, device: Optional[QIODevice]) -> None:
    """
    Calls Qt's 'void QWaveDecoder::setIODevice(QIODevice *device)'.

    Qt's own words: https://doc.qt.io/qt-6/qwavedecoder.html#setIODevice

    Parameters
    ----------

    device : Optional[QIODevice]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWaveDecoder::setIODevice(QIODevice *device)
    self.uglySide.call(
        'ritual_ZN12QWaveDecoder11setIODeviceEP9QIODevice',
        self._addressOf(device),
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

  @overload(QIODevice)
  @overload(NoneType)
  @overload(QIODevice, QObject)
  @overload(QIODevice, NoneType)
  @overload(NoneType, QObject)
  @overload(NoneType, NoneType)
  def __init__(
      self,
      device: Optional[QIODevice],
      parent: Optional[QObject] = None,
  ) -> None:
    """
    Notes what was given, for Qt's 'QWaveDecoder::QWaveDecoder(QIODevice
    *device, QObject *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qwavedecoder.html#QWaveDecoder

    Parameters
    ----------

    device : Optional[QIODevice]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QWaveDecoder::QWaveDecoder(QIODevice *device, QObject *parent)
    self._noteCreation(QWaveDecoder, lambda: Rituals.call(
        'ritual_ZN12QWaveDecoderC1EP9QIODeviceP7QObject',
        self._addressOf(device), self._addressOf(parent, 'QObject'),
    ))

  @overload(QIODevice, QAudioFormat)
  @overload(NoneType, QAudioFormat)
  @overload(QIODevice, QAudioFormat, QObject)
  @overload(QIODevice, QAudioFormat, NoneType)
  @overload(NoneType, QAudioFormat, QObject)
  @overload(NoneType, QAudioFormat, NoneType)
  def __init__(
      self,
      device: Optional[QIODevice],
      format: QAudioFormat,
      parent: Optional[QObject] = None,
  ) -> None:
    """
    Notes what was given, for Qt's 'QWaveDecoder::QWaveDecoder(QIODevice
    *device, const QAudioFormat &format, QObject *parent)', which is called
    at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qwavedecoder.html#QWaveDecoder

    Parameters
    ----------

    device : Optional[QIODevice]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    format : QAudioFormat
      Passed on as a value: Qt reads the C++ QAudioFormat, which stays
      Python's own.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QWaveDecoder::QWaveDecoder(QIODevice *device, const QAudioFormat
    #      &format, QObject *parent)
    self._noteCreation(QWaveDecoder, lambda: Rituals.call(
        'ritual_ZN12QWaveDecoderC1EP9QIODeviceRK12QAudioFormatP7QObject',
        self._addressOf(device), self._valueOf(format),
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

  def getDevice(self) -> Optional[QIODevice]:
    """
    Calls Qt's 'QIODevice *QWaveDecoder::getDevice()'.

    Qt's own words: https://doc.qt.io/qt-6/qwavedecoder.html#getDevice

    Returns
    -------

    Optional[QIODevice]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QIODevice *QWaveDecoder::getDevice()
    address = self.uglySide.call('ritual_ZN12QWaveDecoder9getDeviceEv')
    return QIODevice._cuteAt(address)

  @overload(QIODeviceBase.OpenMode)
  def open(self, mode: QIODeviceBase.OpenMode) -> bool:
    """
    Calls Qt's 'bool QWaveDecoder::open(QIODevice::OpenMode mode)'.

    Qt's own words: https://doc.qt.io/qt-6/qwavedecoder.html#open

    Parameters
    ----------

    mode : QIODeviceBase.OpenMode
      Passed on as its number.
    """
    #  bool QWaveDecoder::open(QIODevice::OpenMode mode)
    ritual = (
        'ritual_ZN12QWaveDecoder4openE6QFlagsIN13QIODeviceBase12OpenModeFla'
        'gEE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN12QWaveDecoder4openE6QFlagsIN13QIODeviceBase12OpenM'
          'odeFlagEE')
    return self.uglySide.call(ritual, mode.value)

  def close(self) -> None:
    """
    Calls Qt's 'void QWaveDecoder::close()'.

    Qt's own words: https://doc.qt.io/qt-6/qwavedecoder.html#close
    """
    #  void QWaveDecoder::close()
    ritual = 'ritual_ZN12QWaveDecoder5closeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN12QWaveDecoder5closeEv'
    self.uglySide.call(ritual)

  @overload(int)
  def seek(self, pos: int) -> bool:
    """
    Calls Qt's 'bool QWaveDecoder::seek(qint64 pos)'.

    Qt's own words: https://doc.qt.io/qt-6/qwavedecoder.html#seek

    Parameters
    ----------

    pos : int
      Passed on as it is.
    """
    #  bool QWaveDecoder::seek(qint64 pos)
    ritual = 'ritual_ZN12QWaveDecoder4seekEx'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN12QWaveDecoder4seekEx'
    return self.uglySide.call(ritual, pos)

  def formatKnown(self) -> None:
    """
    Calls Qt's 'void QWaveDecoder::formatKnown()'.

    Qt's own words: https://doc.qt.io/qt-6/qwavedecoder.html#formatKnown
    """
    #  void QWaveDecoder::formatKnown()
    self.uglySide.call('ritual_ZN12QWaveDecoder11formatKnownEv')

  def parsingError(self) -> None:
    """
    Calls Qt's 'void QWaveDecoder::parsingError()'.

    Qt's own words: https://doc.qt.io/qt-6/qwavedecoder.html#parsingError
    """
    #  void QWaveDecoder::parsingError()
    self.uglySide.call('ritual_ZN12QWaveDecoder12parsingErrorEv')

  def handleData(self) -> None:
    """
    Calls Qt's 'void QWaveDecoder::handleData()'.

    Qt's own words: https://doc.qt.io/qt-6/qwavedecoder.html#handleData
    """
    #  void QWaveDecoder::handleData()
    self.uglySide.call('ritual_ZN12QWaveDecoder10handleDataEv')

  @overload(str, int)
  @overload(NoneType, int)
  def writeData(self, data: Optional[str], len: int) -> int:
    """
    Calls Qt's 'qint64 QWaveDecoder::writeData(const char *data, qint64
    len)'.

    Qt's own words: https://doc.qt.io/qt-6/qwavedecoder.html#writeData

    Parameters
    ----------

    data : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    len : int
      Passed on as it is.
    """
    #  qint64 QWaveDecoder::writeData(const char *data, qint64 len)
    return self.uglySide.call(
        'ritual_ZN12QWaveDecoder9writeDataEPKcx', self._bytesOf(data), len,
    )

  def writeHeader(self) -> bool:
    """
    Calls Qt's 'bool QWaveDecoder::writeHeader()'.

    Qt's own words: https://doc.qt.io/qt-6/qwavedecoder.html#writeHeader
    """
    #  bool QWaveDecoder::writeHeader()
    return self.uglySide.call('ritual_ZN12QWaveDecoder11writeHeaderEv')

  def writeDataLength(self) -> bool:
    """
    Calls Qt's 'bool QWaveDecoder::writeDataLength()'.

    Qt's own words: https://doc.qt.io/qt-6/qwavedecoder.html#writeDataLength
    """
    #  bool QWaveDecoder::writeDataLength()
    return self.uglySide.call('ritual_ZN12QWaveDecoder15writeDataLengthEv')

  def parsingFailed(self) -> None:
    """
    Calls Qt's 'void QWaveDecoder::parsingFailed()'.

    Qt's own words: https://doc.qt.io/qt-6/qwavedecoder.html#parsingFailed
    """
    #  void QWaveDecoder::parsingFailed()
    self.uglySide.call('ritual_ZN12QWaveDecoder13parsingFailedEv')
