"""
QPlatformAudioDecoder binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtMultimedia/6.12.0/QtMultimedia/private/qplatformaudiodecoder_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QPlatformAudioDecoder to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject
from . import QAudioDecoder

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QIODevice, QMetaObject, QUrl
  from . import QAudioBuffer, QAudioFormat
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


class QPlatformAudioDecoder(QObject):
  """
  The cute side of Qt's QPlatformAudioDecoder: a plain Python object standing
  in front of one C++ QPlatformAudioDecoder.

  It is built on the cute 'QObject', as Qt's QPlatformAudioDecoder is built
  on Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QPlatformAudioDecoder that has a ritual and that
  Python can call so far, 23 names in all: 'metaObject', 'tr', 'source',
  'setSource', 'sourceDevice', 'setSourceDevice', 'start', 'stop',
  'audioFormat', 'setAudioFormat', 'read', 'bufferAvailable',
  'formatChanged', 'sourceChanged', 'error', 'clearError', 'bufferReady',
  'bufferAvailableChanged', 'setIsDecoding', 'finished', 'isDecoding',
  'errorString', 'canReadQrc'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QPlatformAudioDecoder::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QPlatformAudioDecoder::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'std::chrono::milliseconds QPlatformAudioDecoder::position() const':
    gives a type Python has no way to take yet.
  - Qt's 'std::chrono::milliseconds QPlatformAudioDecoder::duration() const':
    gives a type Python has no way to take yet.
  - Qt's 'void
    QPlatformAudioDecoder::positionChanged(std::chrono::milliseconds a0)':
    takes a type Python has no way to hand over yet.
  - Qt's 'void
    QPlatformAudioDecoder::durationChanged(std::chrono::milliseconds a0)':
    takes a type Python has no way to hand over yet.
  - Qt's 'QPlatformAudioDecoder::~QPlatformAudioDecoder()': the destructor:
    Python never removes a C++ QPlatformAudioDecoder.

  What has no ritual
  ------------------

  2 of the 34 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QPlatformAudioDecoder is created at the first use, not by
    'QPlatformAudioDecoder(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QPlatformAudioDecoder.
  - Qt tells when it has removed the C++ QPlatformAudioDecoder. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QPlatformAudioDecoder that has no cute function yet,
    'duration', 'durationChanged', 'position', 'positionChanged', holds a
    function that raises 'NotImplementedError', and its docstring says why.
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
    Calls Qt's 'QString QPlatformAudioDecoder::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformaudiodecoder.html#tr

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
    #  QString QPlatformAudioDecoder::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN21QPlatformAudioDecoder2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QPlatformAudioDecoder'

  #  A C++ QPlatformAudioDecoder Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QPlatformAudioDecoder'

  #  The functions Qt calls itself that QPlatformAudioDecoder is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'source': (
          ('_ZNK21QPlatformAudioDecoder6sourceEv',
           ('address', 'value', 'QtCore:QUrl'),
           ()),
      ),
      'setSource': (
          ('_ZN21QPlatformAudioDecoder9setSourceERK4QUrl',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtCore:QUrl'),
           )),
      ),
      'sourceDevice': (
          ('_ZNK21QPlatformAudioDecoder12sourceDeviceEv',
           ('address', 'address', 'QtCore:QIODevice'),
           ()),
      ),
      'setSourceDevice': (
          ('_ZN21QPlatformAudioDecoder15setSourceDeviceEP9QIODevice',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtCore:QIODevice'),
           )),
      ),
      'start': (
          ('_ZN21QPlatformAudioDecoder5startEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'stop': (
          ('_ZN21QPlatformAudioDecoder4stopEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'audioFormat': (
          ('_ZNK21QPlatformAudioDecoder11audioFormatEv',
           ('address', 'value', 'QtMultimedia:QAudioFormat'),
           ()),
      ),
      'setAudioFormat': (
          ('_ZN21QPlatformAudioDecoder14setAudioFormatERK12QAudioFormat',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtMultimedia:QAudioFormat'),
           )),
      ),
      'read': (
          ('_ZN21QPlatformAudioDecoder4readEv',
           ('address', 'value', 'QtMultimedia:QAudioBuffer'),
           ()),
      ),
      'bufferAvailable': (
          ('_ZNK21QPlatformAudioDecoder15bufferAvailableEv',
           ('bool', 'number', ''),
           ()),
      ),
      'canReadQrc': (
          ('_ZNK21QPlatformAudioDecoder10canReadQrcEv',
           ('bool', 'number', ''),
           ()),
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
    Calls Qt's 'const QMetaObject *QPlatformAudioDecoder::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformaudiodecoder.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QPlatformAudioDecoder::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK21QPlatformAudioDecoder10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def source(self) -> QUrl:
    """
    Calls Qt's 'QUrl QPlatformAudioDecoder::source() const'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformaudiodecoder.html#source

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QPlatformAudioDecoder::source() const
    address = self.uglySide.call(
        'ritual_ZNK21QPlatformAudioDecoder6sourceEv',
    )
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  def sourceDevice(self) -> Optional[QIODevice]:
    """
    Calls Qt's 'QIODevice *QPlatformAudioDecoder::sourceDevice() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformaudiodecoder.html#sourceDevice

    Returns
    -------

    Optional[QIODevice]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QIODevice *QPlatformAudioDecoder::sourceDevice() const
    address = self.uglySide.call(
        'ritual_ZNK21QPlatformAudioDecoder12sourceDeviceEv',
    )
    from ..QtCore import QIODevice
    return QIODevice._cuteAt(address)

  def audioFormat(self) -> QAudioFormat:
    """
    Calls Qt's 'QAudioFormat QPlatformAudioDecoder::audioFormat() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformaudiodecoder.html#audioFormat

    Returns
    -------

    QAudioFormat
      A new cute QAudioFormat around the copy Qt gave back. Python owns it.
    """
    #  QAudioFormat QPlatformAudioDecoder::audioFormat() const
    address = self.uglySide.call(
        'ritual_ZNK21QPlatformAudioDecoder11audioFormatEv',
    )
    from . import QAudioFormat
    return QAudioFormat._cuteOwning(address)

  def bufferAvailable(self) -> bool:
    """
    Calls Qt's 'bool QPlatformAudioDecoder::bufferAvailable() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformaudiodecoder.html#bufferAvailable
    """
    #  bool QPlatformAudioDecoder::bufferAvailable() const
    ritual = 'ritual_ZNK21QPlatformAudioDecoder15bufferAvailableEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK21QPlatformAudioDecoder15bufferAvailableEv'
    return self.uglySide.call(ritual)

  def isDecoding(self) -> bool:
    """
    Calls Qt's 'bool QPlatformAudioDecoder::isDecoding() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformaudiodecoder.html#isDecoding
    """
    #  bool QPlatformAudioDecoder::isDecoding() const
    return self.uglySide.call(
        'ritual_ZNK21QPlatformAudioDecoder10isDecodingEv',
    )

  def errorString(self) -> str:
    """
    Calls Qt's 'QString QPlatformAudioDecoder::errorString() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformaudiodecoder.html#errorString

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QPlatformAudioDecoder::errorString() const
    return self.uglySide.call(
        'ritual_ZNK21QPlatformAudioDecoder11errorStringEv',
    )

  def canReadQrc(self) -> bool:
    """
    Calls Qt's 'bool QPlatformAudioDecoder::canReadQrc() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformaudiodecoder.html#canReadQrc
    """
    #  bool QPlatformAudioDecoder::canReadQrc() const
    ritual = 'ritual_ZNK21QPlatformAudioDecoder10canReadQrcEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK21QPlatformAudioDecoder10canReadQrcEv'
    return self.uglySide.call(ritual)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QUrl)
  def setSource(self, fileName: QUrl) -> None:
    """
    Calls Qt's 'void QPlatformAudioDecoder::setSource(const QUrl &fileName)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformaudiodecoder.html#setSource

    Parameters
    ----------

    fileName : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  void QPlatformAudioDecoder::setSource(const QUrl &fileName)
    self.uglySide.call(
        'ritual_ZN21QPlatformAudioDecoder9setSourceERK4QUrl',
        self._valueOf(fileName),
    )

  @overload(QIODevice)
  @overload(NoneType)
  def setSourceDevice(self, device: Optional[QIODevice]) -> None:
    """
    Calls Qt's 'void QPlatformAudioDecoder::setSourceDevice(QIODevice
    *device)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformaudiodecoder.html#setSourceDevice

    Parameters
    ----------

    device : Optional[QIODevice]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QPlatformAudioDecoder::setSourceDevice(QIODevice *device)
    self.uglySide.call(
        'ritual_ZN21QPlatformAudioDecoder15setSourceDeviceEP9QIODevice',
        self._addressOf(device),
    )

  @overload(QAudioFormat)
  def setAudioFormat(self, format: QAudioFormat) -> None:
    """
    Calls Qt's 'void QPlatformAudioDecoder::setAudioFormat(const QAudioFormat
    &format)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformaudiodecoder.html#setAudioFormat

    Parameters
    ----------

    format : QAudioFormat
      Passed on as a value: Qt reads the C++ QAudioFormat, which stays
      Python's own.
    """
    #  void QPlatformAudioDecoder::setAudioFormat(const QAudioFormat &format)
    self.uglySide.call(
        'ritual_ZN21QPlatformAudioDecoder14setAudioFormatERK12QAudioFormat',
        self._valueOf(format),
    )

  @overload()
  @overload(bool)
  def setIsDecoding(self, running: bool = True) -> None:
    """
    Calls Qt's 'void QPlatformAudioDecoder::setIsDecoding(bool running)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformaudiodecoder.html#setIsDecoding

    Parameters
    ----------

    running : bool
      Passed on as it is. May be left out, as in Qt: it is then True.
    """
    #  void QPlatformAudioDecoder::setIsDecoding(bool running)
    self.uglySide.call(
        'ritual_ZN21QPlatformAudioDecoder13setIsDecodingEb', running,
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

  @overload(QAudioDecoder)
  @overload(NoneType)
  def __init__(self, parent: Optional[QAudioDecoder]) -> None:
    """
    Notes what was given, for Qt's
    'QPlatformAudioDecoder::QPlatformAudioDecoder(QAudioDecoder *parent)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformaudiodecoder.html#QPlatformAudioDecoder

    Parameters
    ----------

    parent : Optional[QAudioDecoder]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QPlatformAudioDecoder::QPlatformAudioDecoder(QAudioDecoder *parent)
    self._noteCreation(QPlatformAudioDecoder, lambda: Rituals.call(
        'ritual_ZN21QPlatformAudioDecoderC1EP13QAudioDecoder',
        self._addressOf(parent),
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
    Calls Qt's 'void QPlatformAudioDecoder::start()'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformaudiodecoder.html#start
    """
    #  void QPlatformAudioDecoder::start()
    self.uglySide.call('ritual_ZN21QPlatformAudioDecoder5startEv')

  def stop(self) -> None:
    """
    Calls Qt's 'void QPlatformAudioDecoder::stop()'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformaudiodecoder.html#stop
    """
    #  void QPlatformAudioDecoder::stop()
    self.uglySide.call('ritual_ZN21QPlatformAudioDecoder4stopEv')

  def read(self) -> QAudioBuffer:
    """
    Calls Qt's 'QAudioBuffer QPlatformAudioDecoder::read()'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformaudiodecoder.html#read

    Returns
    -------

    QAudioBuffer
      A new cute QAudioBuffer around the copy Qt gave back. Python owns it.
    """
    #  QAudioBuffer QPlatformAudioDecoder::read()
    address = self.uglySide.call('ritual_ZN21QPlatformAudioDecoder4readEv')
    from . import QAudioBuffer
    return QAudioBuffer._cuteOwning(address)

  @overload(QAudioFormat)
  def formatChanged(self, format: QAudioFormat) -> None:
    """
    Calls Qt's 'void QPlatformAudioDecoder::formatChanged(const QAudioFormat
    &format)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformaudiodecoder.html#formatChanged

    Parameters
    ----------

    format : QAudioFormat
      Passed on as a value: Qt reads the C++ QAudioFormat, which stays
      Python's own.
    """
    #  void QPlatformAudioDecoder::formatChanged(const QAudioFormat &format)
    self.uglySide.call(
        'ritual_ZN21QPlatformAudioDecoder13formatChangedERK12QAudioFormat',
        self._valueOf(format),
    )

  def sourceChanged(self) -> None:
    """
    Calls Qt's 'void QPlatformAudioDecoder::sourceChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformaudiodecoder.html#sourceChanged
    """
    #  void QPlatformAudioDecoder::sourceChanged()
    self.uglySide.call('ritual_ZN21QPlatformAudioDecoder13sourceChangedEv')

  @overload(QAudioDecoder.Error, str)
  def error(self, error: QAudioDecoder.Error, errorString: str) -> None:
    """
    Calls Qt's 'void QPlatformAudioDecoder::error(QAudioDecoder::Error error,
    const QString &errorString)'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformaudiodecoder.html#error

    Parameters
    ----------

    error : QAudioDecoder.Error
      Passed on as its number.

    errorString : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QPlatformAudioDecoder::error(QAudioDecoder::Error error, const
    #      QString &errorString)
    self.uglySide.call(
        'ritual_ZN21QPlatformAudioDecoder5errorEN13QAudioDecoder5ErrorERK7Q'
        'String',
        error.value, errorString,
    )

  @overload()
  def error(self) -> QAudioDecoder.Error:
    """
    Calls Qt's 'QAudioDecoder::Error QPlatformAudioDecoder::error() const'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformaudiodecoder.html#error

    Returns
    -------

    QAudioDecoder.Error
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QAudioDecoder.Error(number)' gives.
    """
    #  QAudioDecoder::Error QPlatformAudioDecoder::error() const
    return QAudioDecoder.Error(self.uglySide.call(
        'ritual_ZNK21QPlatformAudioDecoder5errorEv',
    ))

  def clearError(self) -> None:
    """
    Calls Qt's 'void QPlatformAudioDecoder::clearError()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformaudiodecoder.html#clearError
    """
    #  void QPlatformAudioDecoder::clearError()
    self.uglySide.call('ritual_ZN21QPlatformAudioDecoder10clearErrorEv')

  def bufferReady(self) -> None:
    """
    Calls Qt's 'void QPlatformAudioDecoder::bufferReady()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformaudiodecoder.html#bufferReady
    """
    #  void QPlatformAudioDecoder::bufferReady()
    self.uglySide.call('ritual_ZN21QPlatformAudioDecoder11bufferReadyEv')

  @overload(bool)
  def bufferAvailableChanged(self, available: bool) -> None:
    """
    Calls Qt's 'void QPlatformAudioDecoder::bufferAvailableChanged(bool
    available)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformaudiodecoder.html#bufferAvailableChanged

    Parameters
    ----------

    available : bool
      Passed on as it is.
    """
    #  void QPlatformAudioDecoder::bufferAvailableChanged(bool available)
    self.uglySide.call(
        'ritual_ZN21QPlatformAudioDecoder22bufferAvailableChangedEb',
        available,
    )

  def finished(self) -> None:
    """
    Calls Qt's 'void QPlatformAudioDecoder::finished()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformaudiodecoder.html#finished
    """
    #  void QPlatformAudioDecoder::finished()
    self.uglySide.call('ritual_ZN21QPlatformAudioDecoder8finishedEv')

  @staticmethod
  def duration(*__, **_) -> Never:
    """
    Qt's 'std::chrono::milliseconds QPlatformAudioDecoder::duration() const':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QPlatformAudioDecoder.duration' has no cute function yet. Qt's "
        "'std::chrono::milliseconds QPlatformAudioDecoder::duration() "
        "const': gives a type Python has no way to take yet.")

  @staticmethod
  def durationChanged(*__, **_) -> Never:
    """
    Qt's 'void
    QPlatformAudioDecoder::durationChanged(std::chrono::milliseconds a0)':
    takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QPlatformAudioDecoder.durationChanged' has no cute function yet. "
        "Qt's 'void "
        "QPlatformAudioDecoder::durationChanged(std::chrono::milliseconds "
        "a0)': takes a type Python has no way to hand over yet.")

  @staticmethod
  def position(*__, **_) -> Never:
    """
    Qt's 'std::chrono::milliseconds QPlatformAudioDecoder::position() const':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QPlatformAudioDecoder.position' has no cute function yet. Qt's "
        "'std::chrono::milliseconds QPlatformAudioDecoder::position() "
        "const': gives a type Python has no way to take yet.")

  @staticmethod
  def positionChanged(*__, **_) -> Never:
    """
    Qt's 'void
    QPlatformAudioDecoder::positionChanged(std::chrono::milliseconds a0)':
    takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QPlatformAudioDecoder.positionChanged' has no cute function yet. "
        "Qt's 'void "
        "QPlatformAudioDecoder::positionChanged(std::chrono::milliseconds "
        "a0)': takes a type Python has no way to hand over yet.")
