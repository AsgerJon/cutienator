"""
QAudioBuffer binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtMultimedia/qaudiobuffer.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from ..QtCore import QByteArray
  from . import QAudioFormat
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QAudioFormat = WAIT['QAudioFormat']
  QByteArray = WAIT['QByteArray']


class QAudioBuffer(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QAudioBuffer: a plain Python object standing in front
  of one C++ QAudioBuffer.

  C++ hands a QAudioBuffer around as a copy, so every C++ QAudioBuffer behind
  a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QAudioBuffer that has a ritual and that Python can
  call so far, 8 names in all: 'isValid', 'detach', 'format', 'frameCount',
  'sampleCount', 'byteCount', 'duration', 'startTime'. It can be made from
  Python, in 4 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QAudioBuffer::~QAudioBuffer()': the destructor: Python removes its
    C++ QAudioBuffer by it, and has no other use for it.
  - Qt's 'QAudioBuffer &QAudioBuffer::operator=(const QAudioBuffer &other)':
    assignment: Python binds a name and has no operator for it.
  - Qt's 'QAudioBuffer::QAudioBuffer(QAudioBuffer &&other)': takes a type
    Python has no way to hand over yet.
  - Qt's 'QAudioBuffer &QAudioBuffer::operator=(QAudioBuffer &&other)':
    assignment: Python binds a name and has no operator for it.
  - Qt's 'void QAudioBuffer::swap(QAudioBuffer &other)': takes a type Python
    has no way to hand over yet.
  - Qt's 'const void *QAudioBuffer::constData() const': gives 'void', which
    has no cute class yet.
  - Qt's 'const void *QAudioBuffer::data() const': gives 'void', which has no
    cute class yet.
  - Qt's 'void *QAudioBuffer::data()': gives 'void', which has no cute class
    yet.

  What has no ritual
  ------------------

  3 of the 23 functions Qt declares: 3 a template.

  What to expect
  --------------

  - The C++ QAudioBuffer is created at the first use, not by
    'QAudioBuffer(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QAudioBuffer back gives a copy the ritual made for
    Python, in a new cute QAudioBuffer.
  - Each name of Qt's QAudioBuffer that has no cute function yet,
    'constData', 'data', 'swap', holds a function that raises
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
  __qt_class__ = 'QAudioBuffer'

  #  Qt's '~QAudioBuffer()'. Naming it makes this a value class: Python owns
  #  every C++ QAudioBuffer behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN12QAudioBufferD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool QAudioBuffer::isValid() const'.

    Qt's own words: https://doc.qt.io/qt-6/qaudiobuffer.html#isValid
    """
    #  bool QAudioBuffer::isValid() const
    return self.uglySide.call('ritual_ZNK12QAudioBuffer7isValidEv')

  def format(self) -> QAudioFormat:
    """
    Calls Qt's 'QAudioFormat QAudioBuffer::format() const'.

    Qt's own words: https://doc.qt.io/qt-6/qaudiobuffer.html#format

    Returns
    -------

    QAudioFormat
      A new cute QAudioFormat around the copy Qt gave back. Python owns it.
    """
    #  QAudioFormat QAudioBuffer::format() const
    address = self.uglySide.call('ritual_ZNK12QAudioBuffer6formatEv')
    from . import QAudioFormat
    return QAudioFormat._cuteOwning(address)

  def frameCount(self) -> int:
    """
    Calls Qt's 'qsizetype QAudioBuffer::frameCount() const'.

    Qt's own words: https://doc.qt.io/qt-6/qaudiobuffer.html#frameCount
    """
    #  qsizetype QAudioBuffer::frameCount() const
    return self.uglySide.call('ritual_ZNK12QAudioBuffer10frameCountEv')

  def sampleCount(self) -> int:
    """
    Calls Qt's 'qsizetype QAudioBuffer::sampleCount() const'.

    Qt's own words: https://doc.qt.io/qt-6/qaudiobuffer.html#sampleCount
    """
    #  qsizetype QAudioBuffer::sampleCount() const
    return self.uglySide.call('ritual_ZNK12QAudioBuffer11sampleCountEv')

  def byteCount(self) -> int:
    """
    Calls Qt's 'qsizetype QAudioBuffer::byteCount() const'.

    Qt's own words: https://doc.qt.io/qt-6/qaudiobuffer.html#byteCount
    """
    #  qsizetype QAudioBuffer::byteCount() const
    return self.uglySide.call('ritual_ZNK12QAudioBuffer9byteCountEv')

  def duration(self) -> int:
    """
    Calls Qt's 'qint64 QAudioBuffer::duration() const'.

    Qt's own words: https://doc.qt.io/qt-6/qaudiobuffer.html#duration
    """
    #  qint64 QAudioBuffer::duration() const
    return self.uglySide.call('ritual_ZNK12QAudioBuffer8durationEv')

  def startTime(self) -> int:
    """
    Calls Qt's 'qint64 QAudioBuffer::startTime() const'.

    Qt's own words: https://doc.qt.io/qt-6/qaudiobuffer.html#startTime
    """
    #  qint64 QAudioBuffer::startTime() const
    return self.uglySide.call('ritual_ZNK12QAudioBuffer9startTimeEv')

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
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'QAudioBuffer::QAudioBuffer()', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qaudiobuffer.html#QAudioBuffer
    """
    #  QAudioBuffer::QAudioBuffer()
    self._noteCreation(QAudioBuffer, lambda: Rituals.call(
        'ritual_ZN12QAudioBufferC1Ev',
    ))

  @overload(THIS)
  def __init__(self, other: QAudioBuffer) -> None:
    """
    Notes what was given, for Qt's 'QAudioBuffer::QAudioBuffer(const
    QAudioBuffer &other)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qaudiobuffer.html#QAudioBuffer

    Parameters
    ----------

    other : QAudioBuffer
      Passed on as a value: Qt reads the C++ QAudioBuffer, which stays
      Python's own.
    """
    #  QAudioBuffer::QAudioBuffer(const QAudioBuffer &other)
    self._noteCreation(QAudioBuffer, lambda: Rituals.call(
        'ritual_ZN12QAudioBufferC1ERKS_', self._valueOf(other),
    ))

  @overload(QByteArray, QAudioFormat)
  @overload(QByteArray, QAudioFormat, int)
  def __init__(
      self,
      data: QByteArray,
      format: QAudioFormat,
      startTime: int = -1,
  ) -> None:
    """
    Notes what was given, for Qt's 'QAudioBuffer::QAudioBuffer(const
    QByteArray &data, const QAudioFormat &format, qint64 startTime)', which
    is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qaudiobuffer.html#QAudioBuffer

    Parameters
    ----------

    data : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    format : QAudioFormat
      Passed on as a value: Qt reads the C++ QAudioFormat, which stays
      Python's own.

    startTime : int
      Passed on as it is. May be left out, as in Qt: it is then -1.
    """
    #  QAudioBuffer::QAudioBuffer(const QByteArray &data, const QAudioFormat
    #      &format, qint64 startTime)
    self._noteCreation(QAudioBuffer, lambda: Rituals.call(
        'ritual_ZN12QAudioBufferC1ERK10QByteArrayRK12QAudioFormatx',
        self._valueOf(data), self._valueOf(format), startTime,
    ))

  @overload(int, QAudioFormat)
  @overload(int, QAudioFormat, int)
  def __init__(
      self,
      numFrames: int,
      format: QAudioFormat,
      startTime: int = -1,
  ) -> None:
    """
    Notes what was given, for Qt's 'QAudioBuffer::QAudioBuffer(int numFrames,
    const QAudioFormat &format, qint64 startTime)', which is called at the
    first use.

    Qt's own words: https://doc.qt.io/qt-6/qaudiobuffer.html#QAudioBuffer

    Parameters
    ----------

    numFrames : int
      Passed on as it is.

    format : QAudioFormat
      Passed on as a value: Qt reads the C++ QAudioFormat, which stays
      Python's own.

    startTime : int
      Passed on as it is. May be left out, as in Qt: it is then -1.
    """
    #  QAudioBuffer::QAudioBuffer(int numFrames, const QAudioFormat &format,
    #      qint64 startTime)
    self._noteCreation(QAudioBuffer, lambda: Rituals.call(
        'ritual_ZN12QAudioBufferC1EiRK12QAudioFormatx',
        numFrames, self._valueOf(format), startTime,
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

  def detach(self) -> None:
    """
    Calls Qt's 'void QAudioBuffer::detach()'.

    Qt's own words: https://doc.qt.io/qt-6/qaudiobuffer.html#detach
    """
    #  void QAudioBuffer::detach()
    self.uglySide.call('ritual_ZN12QAudioBuffer6detachEv')

  @staticmethod
  def constData(*__, **_) -> Never:
    """
    - Qt's 'const void *QAudioBuffer::constData() const': gives 'void', which
      has no cute class yet.
    - Qt's 'QAudioBuffer::constData': a template: a pattern and no single
      function.
    """
    raise NotImplementedError(
        "'QAudioBuffer.constData' has no cute function yet. Qt's 'const "
        "void *QAudioBuffer::constData() const': gives 'void', which has no "
        "cute class yet. Qt's 'QAudioBuffer::constData': a template: a "
        "pattern and no single function.")

  @staticmethod
  def data(*__, **_) -> Never:
    """
    - Qt's 'const void *QAudioBuffer::data() const': gives 'void', which has
      no cute class yet.
    - Qt's 'void *QAudioBuffer::data()': gives 'void', which has no cute
      class yet.
    - Qt's 'QAudioBuffer::data': a template: a pattern and no single
      function.
    """
    raise NotImplementedError(
        "'QAudioBuffer.data' has no cute function yet. Qt's 'const void "
        "*QAudioBuffer::data() const': gives 'void', which has no cute "
        "class yet. Qt's 'void *QAudioBuffer::data()': gives 'void', which "
        "has no cute class yet. Qt's 'QAudioBuffer::data': a template: a "
        "pattern and no single function.")

  @staticmethod
  def swap(*__, **_) -> Never:
    """
    Qt's 'void QAudioBuffer::swap(QAudioBuffer &other)': takes a type Python
    has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QAudioBuffer.swap' has no cute function yet. Qt's 'void "
        "QAudioBuffer::swap(QAudioBuffer &other)': takes a type Python has "
        "no way to hand over yet.")
