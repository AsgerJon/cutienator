"""
QRingBuffer binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/6.12.0/QtCore/private/qringbuffer_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QRingBuffer to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QByteArray
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QRingBuffer(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QRingBuffer: a plain Python object standing in front
  of one C++ QRingBuffer.

  What exists
  -----------

  Every function of Qt's QRingBuffer that has a ritual and that Python can
  call so far, 15 names in all: 'setChunkSize', 'chunkSize',
  'nextDataBlockSize', 'readPointer', 'free', 'truncate', 'chop', 'isEmpty',
  'getChar', 'size', 'clear', 'read', 'append', 'skip', 'canReadLine'. It can
  be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QRingBuffer::QRingBuffer(QRingBuffer &&a0)': takes a type Python
    has no way to hand over yet.
  - Qt's 'QRingBuffer &QRingBuffer::operator=(QRingBuffer &&a0)': assignment:
    Python binds a name and has no operator for it.
  - Qt's 'const char *QRingBuffer::readPointerAtPosition(qint64 pos, qint64
    &length) const': takes a number to change where it is.
  - Qt's 'char *QRingBuffer::reserve(qint64 bytes)': gives 'char', which has
    no cute class yet.
  - Qt's 'char *QRingBuffer::reserveFront(qint64 bytes)': gives 'char', which
    has no cute class yet.
  - Qt's 'void QRingBuffer::putChar(char c)': takes a single letter as C has
    it.
  - Qt's 'void QRingBuffer::ungetChar(char c)': takes a single letter as C
    has it.
  - Qt's 'qint64 QRingBuffer::indexOf(char c) const': takes a single letter
    as C has it.
  - Qt's 'qint64 QRingBuffer::indexOf(char c, qint64 maxLength, qint64 pos)
    const': takes a single letter as C has it.
  - Qt's 'qint64 QRingBuffer::read(char *data, qint64 maxLength)': names
    'char', which has no cute class yet.
  - Qt's 'qint64 QRingBuffer::peek(char *data, qint64 maxLength, qint64 pos)
    const': names 'char', which has no cute class yet.
  - Qt's 'void QRingBuffer::append(QByteArray &&qba)': takes a type Python
    has no way to hand over yet.
  - Qt's 'qint64 QRingBuffer::readLineWithoutTerminatingNull(char *data,
    qint64 maxLength)': names 'char', which has no cute class yet.
  - Qt's 'qint64 QRingBuffer::readLine(char *data, qint64 maxLength)': names
    'char', which has no cute class yet.

  What has no ritual
  ------------------

  2 of the 33 functions Qt declares: 2 forbidden.

  What to expect
  --------------

  - The C++ QRingBuffer is created at the first use, not by
    'QRingBuffer(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QRingBuffer.
  - Each name of Qt's QRingBuffer that has no cute function yet, 'indexOf',
    'peek', 'putChar', 'readLine', 'readLineWithoutTerminatingNull',
    'readPointerAtPosition', 'reserve', 'reserveFront', 'ungetChar', holds a
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
  __qt_class__ = 'QRingBuffer'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def chunkSize(self) -> int:
    """
    Calls Qt's 'int QRingBuffer::chunkSize() const'.

    Qt's own words: https://doc.qt.io/qt-6/qringbuffer.html#chunkSize
    """
    #  int QRingBuffer::chunkSize() const
    return self.uglySide.call('ritual_ZNK11QRingBuffer9chunkSizeEv')

  def nextDataBlockSize(self) -> int:
    """
    Calls Qt's 'qint64 QRingBuffer::nextDataBlockSize() const'.

    Qt's own words: https://doc.qt.io/qt-6/qringbuffer.html#nextDataBlockSize
    """
    #  qint64 QRingBuffer::nextDataBlockSize() const
    return self.uglySide.call('ritual_ZNK11QRingBuffer17nextDataBlockSizeEv')

  def readPointer(self) -> Optional[str]:
    """
    Calls Qt's 'const char *QRingBuffer::readPointer() const'.

    Qt's own words: https://doc.qt.io/qt-6/qringbuffer.html#readPointer

    Returns
    -------

    Optional[str]
      The text Qt gave back. None when Qt gave back no text.
    """
    #  const char *QRingBuffer::readPointer() const
    chars = self.uglySide.call('ritual_ZNK11QRingBuffer11readPointerEv')
    return None if chars is None else chars.decode()

  def isEmpty(self) -> bool:
    """
    Calls Qt's 'bool QRingBuffer::isEmpty() const'.

    Qt's own words: https://doc.qt.io/qt-6/qringbuffer.html#isEmpty
    """
    #  bool QRingBuffer::isEmpty() const
    return self.uglySide.call('ritual_ZNK11QRingBuffer7isEmptyEv')

  def size(self) -> int:
    """
    Calls Qt's 'qint64 QRingBuffer::size() const'.

    Qt's own words: https://doc.qt.io/qt-6/qringbuffer.html#size
    """
    #  qint64 QRingBuffer::size() const
    return self.uglySide.call('ritual_ZNK11QRingBuffer4sizeEv')

  def canReadLine(self) -> bool:
    """
    Calls Qt's 'bool QRingBuffer::canReadLine() const'.

    Qt's own words: https://doc.qt.io/qt-6/qringbuffer.html#canReadLine
    """
    #  bool QRingBuffer::canReadLine() const
    return self.uglySide.call('ritual_ZNK11QRingBuffer11canReadLineEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setChunkSize(self, size: int) -> None:
    """
    Calls Qt's 'void QRingBuffer::setChunkSize(int size)'.

    Qt's own words: https://doc.qt.io/qt-6/qringbuffer.html#setChunkSize

    Parameters
    ----------

    size : int
      Passed on as it is.
    """
    #  void QRingBuffer::setChunkSize(int size)
    self.uglySide.call('ritual_ZN11QRingBuffer12setChunkSizeEi', size)

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
  @overload(int)
  def __init__(self, growth: int = 4096) -> None:
    """
    Notes what was given, for Qt's 'QRingBuffer::QRingBuffer(int growth)',
    which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qringbuffer.html#QRingBuffer

    Parameters
    ----------

    growth : int
      Passed on as it is. May be left out, as in Qt: it is then 4096.
    """
    #  QRingBuffer::QRingBuffer(int growth)
    self._noteCreation(QRingBuffer, lambda: Rituals.call(
        'ritual_ZN11QRingBufferC1Ei', growth,
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

  @overload(int)
  def free(self, bytes: int) -> None:
    """
    Calls Qt's 'void QRingBuffer::free(qint64 bytes)'.

    Qt's own words: https://doc.qt.io/qt-6/qringbuffer.html#free

    Parameters
    ----------

    bytes : int
      Passed on as it is.
    """
    #  void QRingBuffer::free(qint64 bytes)
    self.uglySide.call('ritual_ZN11QRingBuffer4freeEx', bytes)

  @overload(int)
  def truncate(self, pos: int) -> None:
    """
    Calls Qt's 'void QRingBuffer::truncate(qint64 pos)'.

    Qt's own words: https://doc.qt.io/qt-6/qringbuffer.html#truncate

    Parameters
    ----------

    pos : int
      Passed on as it is.
    """
    #  void QRingBuffer::truncate(qint64 pos)
    self.uglySide.call('ritual_ZN11QRingBuffer8truncateEx', pos)

  @overload(int)
  def chop(self, bytes: int) -> None:
    """
    Calls Qt's 'void QRingBuffer::chop(qint64 bytes)'.

    Qt's own words: https://doc.qt.io/qt-6/qringbuffer.html#chop

    Parameters
    ----------

    bytes : int
      Passed on as it is.
    """
    #  void QRingBuffer::chop(qint64 bytes)
    self.uglySide.call('ritual_ZN11QRingBuffer4chopEx', bytes)

  def getChar(self) -> int:
    """
    Calls Qt's 'int QRingBuffer::getChar()'.

    Qt's own words: https://doc.qt.io/qt-6/qringbuffer.html#getChar
    """
    #  int QRingBuffer::getChar()
    return self.uglySide.call('ritual_ZN11QRingBuffer7getCharEv')

  def clear(self) -> None:
    """
    Calls Qt's 'void QRingBuffer::clear()'.

    Qt's own words: https://doc.qt.io/qt-6/qringbuffer.html#clear
    """
    #  void QRingBuffer::clear()
    self.uglySide.call('ritual_ZN11QRingBuffer5clearEv')

  def read(self) -> QByteArray:
    """
    Calls Qt's 'QByteArray QRingBuffer::read()'.

    Qt's own words: https://doc.qt.io/qt-6/qringbuffer.html#read

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QRingBuffer::read()
    address = self.uglySide.call('ritual_ZN11QRingBuffer4readEv')
    from . import QByteArray
    return QByteArray._cuteOwning(address)

  @overload(str, int)
  @overload(NoneType, int)
  def append(self, data: Optional[str], size: int) -> None:
    """
    Calls Qt's 'void QRingBuffer::append(const char *data, qint64 size)'.

    Qt's own words: https://doc.qt.io/qt-6/qringbuffer.html#append

    Parameters
    ----------

    data : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    size : int
      Passed on as it is.
    """
    #  void QRingBuffer::append(const char *data, qint64 size)
    self.uglySide.call(
        'ritual_ZN11QRingBuffer6appendEPKcx', self._bytesOf(data), size,
    )

  @overload(QByteArray)
  def append(self, qba: QByteArray) -> None:
    """
    Calls Qt's 'void QRingBuffer::append(const QByteArray &qba)'.

    Qt's own words: https://doc.qt.io/qt-6/qringbuffer.html#append

    Parameters
    ----------

    qba : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void QRingBuffer::append(const QByteArray &qba)
    self.uglySide.call(
        'ritual_ZN11QRingBuffer6appendERK10QByteArray', self._valueOf(qba),
    )

  @overload(int)
  def skip(self, length: int) -> int:
    """
    Calls Qt's 'qint64 QRingBuffer::skip(qint64 length)'.

    Qt's own words: https://doc.qt.io/qt-6/qringbuffer.html#skip

    Parameters
    ----------

    length : int
      Passed on as it is.
    """
    #  qint64 QRingBuffer::skip(qint64 length)
    return self.uglySide.call('ritual_ZN11QRingBuffer4skipEx', length)

  @staticmethod
  def indexOf(*__, **_) -> Never:
    """
    - Qt's 'qint64 QRingBuffer::indexOf(char c) const': takes a single letter
      as C has it.
    - Qt's 'qint64 QRingBuffer::indexOf(char c, qint64 maxLength, qint64 pos)
      const': takes a single letter as C has it.
    """
    raise NotImplementedError(
        "'QRingBuffer.indexOf' has no cute function yet. Qt's 'qint64 "
        "QRingBuffer::indexOf(char c) const': takes a single letter as C "
        "has it. Qt's 'qint64 QRingBuffer::indexOf(char c, qint64 "
        "maxLength, qint64 pos) const': takes a single letter as C has it.")

  @staticmethod
  def peek(*__, **_) -> Never:
    """
    Qt's 'qint64 QRingBuffer::peek(char *data, qint64 maxLength, qint64 pos)
    const': names 'char', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QRingBuffer.peek' has no cute function yet. Qt's 'qint64 "
        "QRingBuffer::peek(char *data, qint64 maxLength, qint64 pos) "
        "const': names 'char', which has no cute class yet.")

  @staticmethod
  def putChar(*__, **_) -> Never:
    """
    Qt's 'void QRingBuffer::putChar(char c)': takes a single letter as C has
    it.
    """
    raise NotImplementedError(
        "'QRingBuffer.putChar' has no cute function yet. Qt's 'void "
        "QRingBuffer::putChar(char c)': takes a single letter as C has it.")

  @staticmethod
  def readLine(*__, **_) -> Never:
    """
    Qt's 'qint64 QRingBuffer::readLine(char *data, qint64 maxLength)': names
    'char', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QRingBuffer.readLine' has no cute function yet. Qt's 'qint64 "
        "QRingBuffer::readLine(char *data, qint64 maxLength)': names "
        "'char', which has no cute class yet.")

  @staticmethod
  def readLineWithoutTerminatingNull(*__, **_) -> Never:
    """
    Qt's 'qint64 QRingBuffer::readLineWithoutTerminatingNull(char *data,
    qint64 maxLength)': names 'char', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QRingBuffer.readLineWithoutTerminatingNull' has no cute function "
        "yet. Qt's 'qint64 QRingBuffer::readLineWithoutTerminatingNull(char "
        "*data, qint64 maxLength)': names 'char', which has no cute class "
        "yet.")

  @staticmethod
  def readPointerAtPosition(*__, **_) -> Never:
    """
    Qt's 'const char *QRingBuffer::readPointerAtPosition(qint64 pos, qint64
    &length) const': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QRingBuffer.readPointerAtPosition' has no cute function yet. Qt's "
        "'const char *QRingBuffer::readPointerAtPosition(qint64 pos, qint64 "
        "&length) const': takes a number to change where it is.")

  @staticmethod
  def reserve(*__, **_) -> Never:
    """
    Qt's 'char *QRingBuffer::reserve(qint64 bytes)': gives 'char', which has
    no cute class yet.
    """
    raise NotImplementedError(
        "'QRingBuffer.reserve' has no cute function yet. Qt's 'char "
        "*QRingBuffer::reserve(qint64 bytes)': gives 'char', which has no "
        "cute class yet.")

  @staticmethod
  def reserveFront(*__, **_) -> Never:
    """
    Qt's 'char *QRingBuffer::reserveFront(qint64 bytes)': gives 'char', which
    has no cute class yet.
    """
    raise NotImplementedError(
        "'QRingBuffer.reserveFront' has no cute function yet. Qt's 'char "
        "*QRingBuffer::reserveFront(qint64 bytes)': gives 'char', which has "
        "no cute class yet.")

  @staticmethod
  def ungetChar(*__, **_) -> Never:
    """
    Qt's 'void QRingBuffer::ungetChar(char c)': takes a single letter as C
    has it.
    """
    raise NotImplementedError(
        "'QRingBuffer.ungetChar' has no cute function yet. Qt's 'void "
        "QRingBuffer::ungetChar(char c)': takes a single letter as C has it."
    )
