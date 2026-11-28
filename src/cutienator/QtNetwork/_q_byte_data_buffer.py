"""
QByteDataBuffer binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtNetwork/6.12.0/QtNetwork/private/qbytedatabuffer_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QByteDataBuffer to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from ..QtCore import QByteArray, QByteArrayView
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']


class QByteDataBuffer(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QByteDataBuffer: a plain Python object standing in
  front of one C++ QByteDataBuffer.

  C++ hands a QByteDataBuffer around as a copy, so every C++ QByteDataBuffer
  behind a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QByteDataBuffer that has a ritual and that Python
  can call so far, 14 names in all: 'squeezeFirst', 'append', 'prepend',
  'read', 'readAll', 'readPointer', 'advanceReadPointer', 'clear',
  'byteAmount', 'bufferCount', 'isEmpty', 'sizeNextBlock', 'canReadLine',
  'last'. None can be made from Python: one comes out of a function of
  another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void QByteDataBuffer::popFront(QByteArray &ba, qint64 n)': takes a
    type Python has no way to hand over yet.
  - Qt's 'void QByteDataBuffer::append(QByteDataBuffer &&other)': takes a
    type Python has no way to hand over yet.
  - Qt's 'void QByteDataBuffer::append(QByteArray &&bd)': takes a type Python
    has no way to hand over yet.
  - Qt's 'void QByteDataBuffer::prepend(QByteArray &&bd)': takes a type
    Python has no way to hand over yet.
  - Qt's 'qint64 QByteDataBuffer::read(char *dst, qint64 amount)': names
    'char', which has no cute class yet.
  - Qt's 'char QByteDataBuffer::getChar()': gives a single letter as C has
    it.
  - Qt's 'QByteArray &QByteDataBuffer::operator[](qsizetype i)': gives a type
    Python has no way to take yet.
  - Qt's 'QByteDataBuffer::~QByteDataBuffer()': the destructor: Python
    removes its C++ QByteDataBuffer by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QByteDataBuffer is created at the first use, not by
    'QByteDataBuffer(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QByteDataBuffer back gives a copy the ritual made for
    Python, in a new cute QByteDataBuffer.
  - Each name of Qt's QByteDataBuffer that has no cute function yet,
    'getChar', 'popFront', holds a function that raises
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
  __qt_class__ = 'QByteDataBuffer'

  #  Qt's '~QByteDataBuffer()'. Naming it makes this a value class: Python
  #  owns every C++ QByteDataBuffer behind a cute one, and removes it by this
  #  ritual.
  __delete_ritual__ = 'ritual_ZN15QByteDataBufferD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def readPointer(self) -> QByteArrayView:
    """
    Calls Qt's 'QByteArrayView QByteDataBuffer::readPointer() const'.

    Qt's own words: https://doc.qt.io/qt-6/qbytedatabuffer.html#readPointer

    Returns
    -------

    QByteArrayView
      A new cute QByteArrayView around the copy Qt gave back. Python owns it.
    """
    #  QByteArrayView QByteDataBuffer::readPointer() const
    address = self.uglySide.call(
        'ritual_ZNK15QByteDataBuffer11readPointerEv',
    )
    from ..QtCore import QByteArrayView
    return QByteArrayView._cuteOwning(address)

  def byteAmount(self) -> int:
    """
    Calls Qt's 'qint64 QByteDataBuffer::byteAmount() const'.

    Qt's own words: https://doc.qt.io/qt-6/qbytedatabuffer.html#byteAmount
    """
    #  qint64 QByteDataBuffer::byteAmount() const
    return self.uglySide.call('ritual_ZNK15QByteDataBuffer10byteAmountEv')

  def bufferCount(self) -> int:
    """
    Calls Qt's 'qsizetype QByteDataBuffer::bufferCount() const'.

    Qt's own words: https://doc.qt.io/qt-6/qbytedatabuffer.html#bufferCount
    """
    #  qsizetype QByteDataBuffer::bufferCount() const
    return self.uglySide.call('ritual_ZNK15QByteDataBuffer11bufferCountEv')

  def isEmpty(self) -> bool:
    """
    Calls Qt's 'bool QByteDataBuffer::isEmpty() const'.

    Qt's own words: https://doc.qt.io/qt-6/qbytedatabuffer.html#isEmpty
    """
    #  bool QByteDataBuffer::isEmpty() const
    return self.uglySide.call('ritual_ZNK15QByteDataBuffer7isEmptyEv')

  def sizeNextBlock(self) -> int:
    """
    Calls Qt's 'qint64 QByteDataBuffer::sizeNextBlock() const'.

    Qt's own words: https://doc.qt.io/qt-6/qbytedatabuffer.html#sizeNextBlock
    """
    #  qint64 QByteDataBuffer::sizeNextBlock() const
    return self.uglySide.call('ritual_ZNK15QByteDataBuffer13sizeNextBlockEv')

  def canReadLine(self) -> bool:
    """
    Calls Qt's 'bool QByteDataBuffer::canReadLine() const'.

    Qt's own words: https://doc.qt.io/qt-6/qbytedatabuffer.html#canReadLine
    """
    #  bool QByteDataBuffer::canReadLine() const
    return self.uglySide.call('ritual_ZNK15QByteDataBuffer11canReadLineEv')

  def last(self) -> QByteArray:
    """
    Calls Qt's 'const QByteArray &QByteDataBuffer::last() const'.

    Qt's own words: https://doc.qt.io/qt-6/qbytedatabuffer.html#last

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  const QByteArray &QByteDataBuffer::last() const
    address = self.uglySide.call('ritual_ZNK15QByteDataBuffer4lastEv')
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

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

  def squeezeFirst(self) -> None:
    """
    Calls Qt's 'void QByteDataBuffer::squeezeFirst()'.

    Qt's own words: https://doc.qt.io/qt-6/qbytedatabuffer.html#squeezeFirst
    """
    #  void QByteDataBuffer::squeezeFirst()
    self.uglySide.call('ritual_ZN15QByteDataBuffer12squeezeFirstEv')

  @overload(THIS)
  def append(self, other: QByteDataBuffer) -> None:
    """
    Calls Qt's 'void QByteDataBuffer::append(const QByteDataBuffer &other)'.

    Qt's own words: https://doc.qt.io/qt-6/qbytedatabuffer.html#append

    Parameters
    ----------

    other : QByteDataBuffer
      Passed on as a value: Qt reads the C++ QByteDataBuffer, which stays
      Python's own.
    """
    #  void QByteDataBuffer::append(const QByteDataBuffer &other)
    self.uglySide.call(
        'ritual_ZN15QByteDataBuffer6appendERKS_', self._valueOf(other),
    )

  @overload(QByteArray)
  def append(self, bd: QByteArray) -> None:
    """
    Calls Qt's 'void QByteDataBuffer::append(const QByteArray &bd)'.

    Qt's own words: https://doc.qt.io/qt-6/qbytedatabuffer.html#append

    Parameters
    ----------

    bd : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void QByteDataBuffer::append(const QByteArray &bd)
    self.uglySide.call(
        'ritual_ZN15QByteDataBuffer6appendERK10QByteArray',
        self._valueOf(bd),
    )

  @overload(QByteArray)
  def prepend(self, bd: QByteArray) -> None:
    """
    Calls Qt's 'void QByteDataBuffer::prepend(const QByteArray &bd)'.

    Qt's own words: https://doc.qt.io/qt-6/qbytedatabuffer.html#prepend

    Parameters
    ----------

    bd : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void QByteDataBuffer::prepend(const QByteArray &bd)
    self.uglySide.call(
        'ritual_ZN15QByteDataBuffer7prependERK10QByteArray',
        self._valueOf(bd),
    )

  @overload()
  def read(self) -> QByteArray:
    """
    Calls Qt's 'QByteArray QByteDataBuffer::read()'.

    Qt's own words: https://doc.qt.io/qt-6/qbytedatabuffer.html#read

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QByteDataBuffer::read()
    address = self.uglySide.call('ritual_ZN15QByteDataBuffer4readEv')
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  @overload(int)
  def read(self, amount: int) -> QByteArray:
    """
    Calls Qt's 'QByteArray QByteDataBuffer::read(qint64 amount)'.

    Qt's own words: https://doc.qt.io/qt-6/qbytedatabuffer.html#read

    Parameters
    ----------

    amount : int
      Passed on as it is.

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QByteDataBuffer::read(qint64 amount)
    address = self.uglySide.call('ritual_ZN15QByteDataBuffer4readEx', amount)
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  def readAll(self) -> QByteArray:
    """
    Calls Qt's 'QByteArray QByteDataBuffer::readAll()'.

    Qt's own words: https://doc.qt.io/qt-6/qbytedatabuffer.html#readAll

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QByteDataBuffer::readAll()
    address = self.uglySide.call('ritual_ZN15QByteDataBuffer7readAllEv')
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  @overload(int)
  def advanceReadPointer(self, distance: int) -> None:
    """
    Calls Qt's 'void QByteDataBuffer::advanceReadPointer(qint64 distance)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbytedatabuffer.html#advanceReadPointer

    Parameters
    ----------

    distance : int
      Passed on as it is.
    """
    #  void QByteDataBuffer::advanceReadPointer(qint64 distance)
    self.uglySide.call(
        'ritual_ZN15QByteDataBuffer18advanceReadPointerEx', distance,
    )

  def clear(self) -> None:
    """
    Calls Qt's 'void QByteDataBuffer::clear()'.

    Qt's own words: https://doc.qt.io/qt-6/qbytedatabuffer.html#clear
    """
    #  void QByteDataBuffer::clear()
    self.uglySide.call('ritual_ZN15QByteDataBuffer5clearEv')

  @staticmethod
  def getChar(*__, **_) -> Never:
    """
    Qt's 'char QByteDataBuffer::getChar()': gives a single letter as C has
    it.
    """
    raise NotImplementedError(
        "'QByteDataBuffer.getChar' has no cute function yet. Qt's 'char "
        "QByteDataBuffer::getChar()': gives a single letter as C has it.")

  @staticmethod
  def popFront(*__, **_) -> Never:
    """
    Qt's 'void QByteDataBuffer::popFront(QByteArray &ba, qint64 n)': takes a
    type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QByteDataBuffer.popFront' has no cute function yet. Qt's 'void "
        "QByteDataBuffer::popFront(QByteArray &ba, qint64 n)': takes a type "
        "Python has no way to hand over yet.")
