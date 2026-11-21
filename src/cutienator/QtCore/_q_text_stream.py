"""
QTextStream binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/qtextstream.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from . import QIODeviceBase, QTextStreamFieldAlignment, QTextStreamNumberFlag
from . import QTextStreamRealNumberNotation, QTextStreamStatus

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QByteArray, QChar, QIODevice, QLocale
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']
  QChar = WAIT['QChar']
  QIODevice = WAIT['QIODevice']
  QLocale = WAIT['QLocale']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QTextStream(QIODeviceBase):
  """
  The cute side of Qt's QTextStream: a plain Python object standing in front
  of one C++ QTextStream.

  It is built on the cute 'QIODeviceBase', as Qt's QTextStream is built on
  Qt's QIODeviceBase, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QTextStream that has a ritual and that Python can
  call so far, 34 names in all: 'setAutoDetectUnicode', 'autoDetectUnicode',
  'setGenerateByteOrderMark', 'generateByteOrderMark', 'setLocale', 'locale',
  'setDevice', 'device', 'status', 'setStatus', 'resetStatus', 'atEnd',
  'reset', 'flush', 'seek', 'pos', 'skipWhiteSpace', 'readLine', 'readAll',
  'read', 'setFieldAlignment', 'fieldAlignment', 'setPadChar', 'padChar',
  'setFieldWidth', 'fieldWidth', 'setNumberFlags', 'numberFlags',
  'setIntegerBase', 'integerBase', 'setRealNumberNotation',
  'realNumberNotation', 'setRealNumberPrecision', 'realNumberPrecision'. It
  can be made from Python, in 3 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QTextStream::QTextStream(QString *string, OpenMode openMode)':
    names 'QString', which has no cute class yet.
  - Qt's 'QTextStream::QTextStream(const QByteArray &array, OpenMode
    openMode)': takes in Python what 'QTextStream::QTextStream(QByteArray
    *array, OpenMode openMode)' takes.
  - Qt's 'QTextStream::~QTextStream()': the destructor: Python never removes
    a C++ QTextStream.
  - Qt's 'void QTextStream::setEncoding(QStringConverter::Encoding
    encoding)': names the enum 'QStringConverter::Encoding', whose class
    cannot be named here.
  - Qt's 'QStringConverter::Encoding QTextStream::encoding() const': gives
    the enum 'QStringConverter::Encoding', whose class cannot be named here.
  - Qt's 'void QTextStream::setString(QString *string, OpenMode openMode)':
    names 'QString', which has no cute class yet.
  - Qt's 'QString *QTextStream::string() const': gives 'QString', which has
    no cute class yet.
  - Qt's 'bool QTextStream::readLineInto(QString *line, qint64 maxlen)':
    names 'QString', which has no cute class yet.
  - Qt's 'bool QTextStream::operator bool() const': an operator, which is not
    reflected yet.

  What has no ritual
  ------------------

  40 of the 86 functions Qt declares: 36 takes or gives a type that cannot be
  passed yet; 2 private; 2 forbidden.

  What to expect
  --------------

  - The C++ QTextStream is created at the first use, not by
    'QTextStream(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QTextStream.
  """

  #  The enums Qt writes inside QTextStream, and the names Qt has for the
  #  combinations of its flags enums.
  FieldAlignment = QTextStreamFieldAlignment
  NumberFlag = QTextStreamNumberFlag
  NumberFlags = QTextStreamNumberFlag
  RealNumberNotation = QTextStreamRealNumberNotation
  Status = QTextStreamStatus

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QTextStream'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def autoDetectUnicode(self) -> bool:
    """
    Calls Qt's 'bool QTextStream::autoDetectUnicode() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextstream.html#autoDetectUnicode
    """
    #  bool QTextStream::autoDetectUnicode() const
    return self.uglySide.call('ritual_ZNK11QTextStream17autoDetectUnicodeEv')

  def generateByteOrderMark(self) -> bool:
    """
    Calls Qt's 'bool QTextStream::generateByteOrderMark() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextstream.html#generateByteOrderMark
    """
    #  bool QTextStream::generateByteOrderMark() const
    return self.uglySide.call(
        'ritual_ZNK11QTextStream21generateByteOrderMarkEv',
    )

  def locale(self) -> QLocale:
    """
    Calls Qt's 'QLocale QTextStream::locale() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextstream.html#locale

    Returns
    -------

    QLocale
      A new cute QLocale around the copy Qt gave back. Python owns it.
    """
    #  QLocale QTextStream::locale() const
    address = self.uglySide.call('ritual_ZNK11QTextStream6localeEv')
    from . import QLocale
    return QLocale._cuteOwning(address)

  def device(self) -> Optional[QIODevice]:
    """
    Calls Qt's 'QIODevice *QTextStream::device() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextstream.html#device

    Returns
    -------

    Optional[QIODevice]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QIODevice *QTextStream::device() const
    address = self.uglySide.call('ritual_ZNK11QTextStream6deviceEv')
    from . import QIODevice
    return QIODevice._cuteAt(address)

  def status(self) -> Status:
    """
    Calls Qt's 'Status QTextStream::status() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextstream.html#status

    Returns
    -------

    Status
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Status(number)' gives.
    """
    #  Status QTextStream::status() const
    return QTextStream.Status(self.uglySide.call(
        'ritual_ZNK11QTextStream6statusEv',
    ))

  def atEnd(self) -> bool:
    """
    Calls Qt's 'bool QTextStream::atEnd() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextstream.html#atEnd
    """
    #  bool QTextStream::atEnd() const
    return self.uglySide.call('ritual_ZNK11QTextStream5atEndEv')

  def pos(self) -> int:
    """
    Calls Qt's 'qint64 QTextStream::pos() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextstream.html#pos
    """
    #  qint64 QTextStream::pos() const
    return self.uglySide.call('ritual_ZNK11QTextStream3posEv')

  def fieldAlignment(self) -> FieldAlignment:
    """
    Calls Qt's 'FieldAlignment QTextStream::fieldAlignment() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextstream.html#fieldAlignment

    Returns
    -------

    FieldAlignment
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'FieldAlignment(number)'
      gives.
    """
    #  FieldAlignment QTextStream::fieldAlignment() const
    return QTextStream.FieldAlignment(self.uglySide.call(
        'ritual_ZNK11QTextStream14fieldAlignmentEv',
    ))

  def padChar(self) -> QChar:
    """
    Calls Qt's 'QChar QTextStream::padChar() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextstream.html#padChar

    Returns
    -------

    QChar
      A new cute QChar around the copy Qt gave back. Python owns it.
    """
    #  QChar QTextStream::padChar() const
    address = self.uglySide.call('ritual_ZNK11QTextStream7padCharEv')
    from . import QChar
    return QChar._cuteOwning(address)

  def fieldWidth(self) -> int:
    """
    Calls Qt's 'int QTextStream::fieldWidth() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextstream.html#fieldWidth
    """
    #  int QTextStream::fieldWidth() const
    return self.uglySide.call('ritual_ZNK11QTextStream10fieldWidthEv')

  def numberFlags(self) -> NumberFlags:
    """
    Calls Qt's 'NumberFlags QTextStream::numberFlags() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextstream.html#numberFlags

    Returns
    -------

    NumberFlags
      The value standing for the combination Qt gave back.
    """
    #  NumberFlags QTextStream::numberFlags() const
    return QTextStream.NumberFlags(self.uglySide.call(
        'ritual_ZNK11QTextStream11numberFlagsEv',
    ))

  def integerBase(self) -> int:
    """
    Calls Qt's 'int QTextStream::integerBase() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextstream.html#integerBase
    """
    #  int QTextStream::integerBase() const
    return self.uglySide.call('ritual_ZNK11QTextStream11integerBaseEv')

  def realNumberNotation(self) -> RealNumberNotation:
    """
    Calls Qt's 'RealNumberNotation QTextStream::realNumberNotation() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextstream.html#realNumberNotation

    Returns
    -------

    RealNumberNotation
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'RealNumberNotation(number)' gives.
    """
    #  RealNumberNotation QTextStream::realNumberNotation() const
    return QTextStream.RealNumberNotation(self.uglySide.call(
        'ritual_ZNK11QTextStream18realNumberNotationEv',
    ))

  def realNumberPrecision(self) -> int:
    """
    Calls Qt's 'int QTextStream::realNumberPrecision() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextstream.html#realNumberPrecision
    """
    #  int QTextStream::realNumberPrecision() const
    return self.uglySide.call(
        'ritual_ZNK11QTextStream19realNumberPrecisionEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  def setAutoDetectUnicode(self, enabled: bool) -> None:
    """
    Calls Qt's 'void QTextStream::setAutoDetectUnicode(bool enabled)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextstream.html#setAutoDetectUnicode

    Parameters
    ----------

    enabled : bool
      Passed on as it is.
    """
    #  void QTextStream::setAutoDetectUnicode(bool enabled)
    self.uglySide.call(
        'ritual_ZN11QTextStream20setAutoDetectUnicodeEb', enabled,
    )

  @overload(bool)
  def setGenerateByteOrderMark(self, generate: bool) -> None:
    """
    Calls Qt's 'void QTextStream::setGenerateByteOrderMark(bool generate)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextstream.html#setGenerateByteOrderMark

    Parameters
    ----------

    generate : bool
      Passed on as it is.
    """
    #  void QTextStream::setGenerateByteOrderMark(bool generate)
    self.uglySide.call(
        'ritual_ZN11QTextStream24setGenerateByteOrderMarkEb', generate,
    )

  @overload(QLocale)
  def setLocale(self, locale: QLocale) -> None:
    """
    Calls Qt's 'void QTextStream::setLocale(const QLocale &locale)'.

    Qt's own words: https://doc.qt.io/qt-6/qtextstream.html#setLocale

    Parameters
    ----------

    locale : QLocale
      Passed on as a value: Qt reads the C++ QLocale, which stays Python's
      own.
    """
    #  void QTextStream::setLocale(const QLocale &locale)
    self.uglySide.call(
        'ritual_ZN11QTextStream9setLocaleERK7QLocale', self._valueOf(locale),
    )

  @overload(QIODevice)
  @overload(NoneType)
  def setDevice(self, device: Optional[QIODevice]) -> None:
    """
    Calls Qt's 'void QTextStream::setDevice(QIODevice *device)'.

    Qt's own words: https://doc.qt.io/qt-6/qtextstream.html#setDevice

    Parameters
    ----------

    device : Optional[QIODevice]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QTextStream::setDevice(QIODevice *device)
    self.uglySide.call(
        'ritual_ZN11QTextStream9setDeviceEP9QIODevice',
        self._addressOf(device),
    )

  @overload(Status)
  def setStatus(self, status: Status) -> None:
    """
    Calls Qt's 'void QTextStream::setStatus(Status status)'.

    Qt's own words: https://doc.qt.io/qt-6/qtextstream.html#setStatus

    Parameters
    ----------

    status : Status
      Passed on as its number.
    """
    #  void QTextStream::setStatus(Status status)
    self.uglySide.call(
        'ritual_ZN11QTextStream9setStatusENS_6StatusE', status.value,
    )

  @overload(FieldAlignment)
  def setFieldAlignment(self, alignment: FieldAlignment) -> None:
    """
    Calls Qt's 'void QTextStream::setFieldAlignment(FieldAlignment
    alignment)'.

    Qt's own words: https://doc.qt.io/qt-6/qtextstream.html#setFieldAlignment

    Parameters
    ----------

    alignment : FieldAlignment
      Passed on as its number.
    """
    #  void QTextStream::setFieldAlignment(FieldAlignment alignment)
    self.uglySide.call(
        'ritual_ZN11QTextStream17setFieldAlignmentENS_14FieldAlignmentE',
        alignment.value,
    )

  @overload(QChar)
  def setPadChar(self, ch: QChar) -> None:
    """
    Calls Qt's 'void QTextStream::setPadChar(QChar ch)'.

    Qt's own words: https://doc.qt.io/qt-6/qtextstream.html#setPadChar

    Parameters
    ----------

    ch : QChar
      Passed on as a value: Qt reads the C++ QChar, which stays Python's own.
    """
    #  void QTextStream::setPadChar(QChar ch)
    self.uglySide.call(
        'ritual_ZN11QTextStream10setPadCharE5QChar', self._valueOf(ch),
    )

  @overload(int)
  def setFieldWidth(self, width: int) -> None:
    """
    Calls Qt's 'void QTextStream::setFieldWidth(int width)'.

    Qt's own words: https://doc.qt.io/qt-6/qtextstream.html#setFieldWidth

    Parameters
    ----------

    width : int
      Passed on as it is.
    """
    #  void QTextStream::setFieldWidth(int width)
    self.uglySide.call('ritual_ZN11QTextStream13setFieldWidthEi', width)

  @overload(NumberFlags)
  def setNumberFlags(self, flags: NumberFlags) -> None:
    """
    Calls Qt's 'void QTextStream::setNumberFlags(NumberFlags flags)'.

    Qt's own words: https://doc.qt.io/qt-6/qtextstream.html#setNumberFlags

    Parameters
    ----------

    flags : NumberFlags
      Passed on as its number.
    """
    #  void QTextStream::setNumberFlags(NumberFlags flags)
    self.uglySide.call(
        'ritual_ZN11QTextStream14setNumberFlagsE6QFlagsINS_10NumberFlagEE',
        flags.value,
    )

  @overload(int)
  def setIntegerBase(self, base: int) -> None:
    """
    Calls Qt's 'void QTextStream::setIntegerBase(int base)'.

    Qt's own words: https://doc.qt.io/qt-6/qtextstream.html#setIntegerBase

    Parameters
    ----------

    base : int
      Passed on as it is.
    """
    #  void QTextStream::setIntegerBase(int base)
    self.uglySide.call('ritual_ZN11QTextStream14setIntegerBaseEi', base)

  @overload(RealNumberNotation)
  def setRealNumberNotation(self, notation: RealNumberNotation) -> None:
    """
    Calls Qt's 'void QTextStream::setRealNumberNotation(RealNumberNotation
    notation)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextstream.html#setRealNumberNotation

    Parameters
    ----------

    notation : RealNumberNotation
      Passed on as its number.
    """
    #  void QTextStream::setRealNumberNotation(RealNumberNotation notation)
    self.uglySide.call(
        'ritual_ZN11QTextStream21setRealNumberNotationENS_18RealNumberNotat'
        'ionE',
        notation.value,
    )

  @overload(int)
  def setRealNumberPrecision(self, precision: int) -> None:
    """
    Calls Qt's 'void QTextStream::setRealNumberPrecision(int precision)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextstream.html#setRealNumberPrecision

    Parameters
    ----------

    precision : int
      Passed on as it is.
    """
    #  void QTextStream::setRealNumberPrecision(int precision)
    self.uglySide.call(
        'ritual_ZN11QTextStream22setRealNumberPrecisionEi', precision,
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
    Notes what was given, for Qt's 'QTextStream::QTextStream()', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qtextstream.html#QTextStream
    """
    #  QTextStream::QTextStream()
    self._noteCreation(QTextStream, lambda: Rituals.call(
        'ritual_ZN11QTextStreamC1Ev',
    ))

  @overload(QIODevice)
  @overload(NoneType)
  def __init__(self, device: Optional[QIODevice]) -> None:
    """
    Notes what was given, for Qt's 'QTextStream::QTextStream(QIODevice
    *device)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qtextstream.html#QTextStream

    Parameters
    ----------

    device : Optional[QIODevice]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QTextStream::QTextStream(QIODevice *device)
    self._noteCreation(QTextStream, lambda: Rituals.call(
        'ritual_ZN11QTextStreamC1EP9QIODevice', self._addressOf(device),
    ))

  @overload(QByteArray)
  @overload(QByteArray, QIODeviceBase.OpenMode)
  @overload(NoneType, QIODeviceBase.OpenMode)
  def __init__(
      self,
      array: Optional[QByteArray],
      openMode: QIODeviceBase.OpenMode = QIODeviceBase.OpenMode.ReadWrite,
  ) -> None:
    """
    Notes what was given, for Qt's 'QTextStream::QTextStream(QByteArray
    *array, OpenMode openMode)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qtextstream.html#QTextStream

    Parameters
    ----------

    array : Optional[QByteArray]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    openMode : QIODeviceBase.OpenMode
      Passed on as its number. May be left out, as in Qt: it is then
      QIODeviceBase.OpenMode.ReadWrite.
    """
    #  QTextStream::QTextStream(QByteArray *array, OpenMode openMode)
    self._noteCreation(QTextStream, lambda: Rituals.call(
        'ritual_ZN11QTextStreamC1EP10QByteArray6QFlagsIN13QIODeviceBase12Op'
        'enModeFlagEE',
        self._addressOf(array), openMode.value,
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

  def resetStatus(self) -> None:
    """
    Calls Qt's 'void QTextStream::resetStatus()'.

    Qt's own words: https://doc.qt.io/qt-6/qtextstream.html#resetStatus
    """
    #  void QTextStream::resetStatus()
    self.uglySide.call('ritual_ZN11QTextStream11resetStatusEv')

  def reset(self) -> None:
    """
    Calls Qt's 'void QTextStream::reset()'.

    Qt's own words: https://doc.qt.io/qt-6/qtextstream.html#reset
    """
    #  void QTextStream::reset()
    self.uglySide.call('ritual_ZN11QTextStream5resetEv')

  def flush(self) -> None:
    """
    Calls Qt's 'void QTextStream::flush()'.

    Qt's own words: https://doc.qt.io/qt-6/qtextstream.html#flush
    """
    #  void QTextStream::flush()
    self.uglySide.call('ritual_ZN11QTextStream5flushEv')

  @overload(int)
  def seek(self, pos: int) -> bool:
    """
    Calls Qt's 'bool QTextStream::seek(qint64 pos)'.

    Qt's own words: https://doc.qt.io/qt-6/qtextstream.html#seek

    Parameters
    ----------

    pos : int
      Passed on as it is.
    """
    #  bool QTextStream::seek(qint64 pos)
    return self.uglySide.call('ritual_ZN11QTextStream4seekEx', pos)

  def skipWhiteSpace(self) -> None:
    """
    Calls Qt's 'void QTextStream::skipWhiteSpace()'.

    Qt's own words: https://doc.qt.io/qt-6/qtextstream.html#skipWhiteSpace
    """
    #  void QTextStream::skipWhiteSpace()
    self.uglySide.call('ritual_ZN11QTextStream14skipWhiteSpaceEv')

  @overload()
  @overload(int)
  def readLine(self, maxlen: int = 0) -> str:
    """
    Calls Qt's 'QString QTextStream::readLine(qint64 maxlen)'.

    Qt's own words: https://doc.qt.io/qt-6/qtextstream.html#readLine

    Parameters
    ----------

    maxlen : int
      Passed on as it is. May be left out, as in Qt: it is then 0.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QTextStream::readLine(qint64 maxlen)
    return self.uglySide.call('ritual_ZN11QTextStream8readLineEx', maxlen)

  def readAll(self) -> str:
    """
    Calls Qt's 'QString QTextStream::readAll()'.

    Qt's own words: https://doc.qt.io/qt-6/qtextstream.html#readAll

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QTextStream::readAll()
    return self.uglySide.call('ritual_ZN11QTextStream7readAllEv')

  @overload(int)
  def read(self, maxlen: int) -> str:
    """
    Calls Qt's 'QString QTextStream::read(qint64 maxlen)'.

    Qt's own words: https://doc.qt.io/qt-6/qtextstream.html#read

    Parameters
    ----------

    maxlen : int
      Passed on as it is.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QTextStream::read(qint64 maxlen)
    return self.uglySide.call('ritual_ZN11QTextStream4readEx', maxlen)
