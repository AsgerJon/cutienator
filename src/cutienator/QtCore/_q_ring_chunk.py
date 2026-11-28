"""
QRingChunk binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/6.12.0/QtCore/private/qringbuffer_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QRingChunk to be private: it declares the class in a header it
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


class QRingChunk(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QRingChunk: a plain Python object standing in front
  of one C++ QRingChunk.

  C++ hands a QRingChunk around as a copy, so every C++ QRingChunk behind a
  cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QRingChunk that has a ritual and that Python can
  call so far, 13 names in all: 'allocate', 'isShared', 'detach', 'head',
  'size', 'capacity', 'available', 'data', 'advance', 'grow', 'assign',
  'reset', 'clear'. It can be made from Python, in 3 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QRingChunk::QRingChunk(QByteArray &&qba)': takes a type Python has
    no way to hand over yet.
  - Qt's 'void QRingChunk::swap(QRingChunk &other)': takes a type Python has
    no way to hand over yet.
  - Qt's 'char *QRingChunk::data()': gives 'char', which has no cute class
    yet.
  - Qt's 'void QRingChunk::assign(QByteArray &&qba)': takes a type Python has
    no way to hand over yet.
  - Qt's 'QRingChunk::~QRingChunk()': the destructor: Python removes its C++
    QRingChunk by it, and has no other use for it.

  What has no ritual
  ------------------

  1 of the 22 functions Qt declares: 1 can only be called on a value about to
  be thrown away.

  What to expect
  --------------

  - The C++ QRingChunk is created at the first use, not by 'QRingChunk(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QRingChunk back gives a copy the ritual made for
    Python, in a new cute QRingChunk.
  - Each name of Qt's QRingChunk that has no cute function yet, 'swap',
    'toByteArray', holds a function that raises 'NotImplementedError', and
    its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QRingChunk'

  #  Qt's '~QRingChunk()'. Naming it makes this a value class: Python owns
  #  every C++ QRingChunk behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN10QRingChunkD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isShared(self) -> bool:
    """
    Calls Qt's 'bool QRingChunk::isShared() const'.

    Qt's own words: https://doc.qt.io/qt-6/qringchunk.html#isShared
    """
    #  bool QRingChunk::isShared() const
    return self.uglySide.call('ritual_ZNK10QRingChunk8isSharedEv')

  def head(self) -> int:
    """
    Calls Qt's 'qsizetype QRingChunk::head() const'.

    Qt's own words: https://doc.qt.io/qt-6/qringchunk.html#head
    """
    #  qsizetype QRingChunk::head() const
    return self.uglySide.call('ritual_ZNK10QRingChunk4headEv')

  def size(self) -> int:
    """
    Calls Qt's 'qsizetype QRingChunk::size() const'.

    Qt's own words: https://doc.qt.io/qt-6/qringchunk.html#size
    """
    #  qsizetype QRingChunk::size() const
    return self.uglySide.call('ritual_ZNK10QRingChunk4sizeEv')

  def capacity(self) -> int:
    """
    Calls Qt's 'qsizetype QRingChunk::capacity() const'.

    Qt's own words: https://doc.qt.io/qt-6/qringchunk.html#capacity
    """
    #  qsizetype QRingChunk::capacity() const
    return self.uglySide.call('ritual_ZNK10QRingChunk8capacityEv')

  def available(self) -> int:
    """
    Calls Qt's 'qsizetype QRingChunk::available() const'.

    Qt's own words: https://doc.qt.io/qt-6/qringchunk.html#available
    """
    #  qsizetype QRingChunk::available() const
    return self.uglySide.call('ritual_ZNK10QRingChunk9availableEv')

  def data(self) -> Optional[str]:
    """
    Calls Qt's 'const char *QRingChunk::data() const'.

    Qt's own words: https://doc.qt.io/qt-6/qringchunk.html#data

    Returns
    -------

    Optional[str]
      The text Qt gave back. None when Qt gave back no text.
    """
    #  const char *QRingChunk::data() const
    chars = self.uglySide.call('ritual_ZNK10QRingChunk4dataEv')
    return None if chars is None else chars.decode()

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
    Notes what was given, for Qt's 'QRingChunk::QRingChunk()', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qringchunk.html#QRingChunk
    """
    #  QRingChunk::QRingChunk()
    self._noteCreation(QRingChunk, lambda: Rituals.call(
        'ritual_ZN10QRingChunkC1Ev',
    ))

  @overload(int)
  def __init__(self, alloc: int) -> None:
    """
    Notes what was given, for Qt's 'QRingChunk::QRingChunk(qsizetype alloc)',
    which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qringchunk.html#QRingChunk

    Parameters
    ----------

    alloc : int
      Passed on as it is.
    """
    #  QRingChunk::QRingChunk(qsizetype alloc)
    self._noteCreation(QRingChunk, lambda: Rituals.call(
        'ritual_ZN10QRingChunkC1Ex', alloc,
    ))

  @overload(QByteArray)
  def __init__(self, qba: QByteArray) -> None:
    """
    Notes what was given, for Qt's 'QRingChunk::QRingChunk(const QByteArray
    &qba)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qringchunk.html#QRingChunk

    Parameters
    ----------

    qba : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  QRingChunk::QRingChunk(const QByteArray &qba)
    self._noteCreation(QRingChunk, lambda: Rituals.call(
        'ritual_ZN10QRingChunkC1ERK10QByteArray', self._valueOf(qba),
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
  def allocate(self, alloc: int) -> None:
    """
    Calls Qt's 'void QRingChunk::allocate(qsizetype alloc)'.

    Qt's own words: https://doc.qt.io/qt-6/qringchunk.html#allocate

    Parameters
    ----------

    alloc : int
      Passed on as it is.
    """
    #  void QRingChunk::allocate(qsizetype alloc)
    self.uglySide.call('ritual_ZN10QRingChunk8allocateEx', alloc)

  def detach(self) -> None:
    """
    Calls Qt's 'void QRingChunk::detach()'.

    Qt's own words: https://doc.qt.io/qt-6/qringchunk.html#detach
    """
    #  void QRingChunk::detach()
    self.uglySide.call('ritual_ZN10QRingChunk6detachEv')

  @overload(int)
  def advance(self, offset: int) -> None:
    """
    Calls Qt's 'void QRingChunk::advance(qsizetype offset)'.

    Qt's own words: https://doc.qt.io/qt-6/qringchunk.html#advance

    Parameters
    ----------

    offset : int
      Passed on as it is.
    """
    #  void QRingChunk::advance(qsizetype offset)
    self.uglySide.call('ritual_ZN10QRingChunk7advanceEx', offset)

  @overload(int)
  def grow(self, offset: int) -> None:
    """
    Calls Qt's 'void QRingChunk::grow(qsizetype offset)'.

    Qt's own words: https://doc.qt.io/qt-6/qringchunk.html#grow

    Parameters
    ----------

    offset : int
      Passed on as it is.
    """
    #  void QRingChunk::grow(qsizetype offset)
    self.uglySide.call('ritual_ZN10QRingChunk4growEx', offset)

  @overload(QByteArray)
  def assign(self, qba: QByteArray) -> None:
    """
    Calls Qt's 'void QRingChunk::assign(const QByteArray &qba)'.

    Qt's own words: https://doc.qt.io/qt-6/qringchunk.html#assign

    Parameters
    ----------

    qba : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void QRingChunk::assign(const QByteArray &qba)
    self.uglySide.call(
        'ritual_ZN10QRingChunk6assignERK10QByteArray', self._valueOf(qba),
    )

  def reset(self) -> None:
    """
    Calls Qt's 'void QRingChunk::reset()'.

    Qt's own words: https://doc.qt.io/qt-6/qringchunk.html#reset
    """
    #  void QRingChunk::reset()
    self.uglySide.call('ritual_ZN10QRingChunk5resetEv')

  def clear(self) -> None:
    """
    Calls Qt's 'void QRingChunk::clear()'.

    Qt's own words: https://doc.qt.io/qt-6/qringchunk.html#clear
    """
    #  void QRingChunk::clear()
    self.uglySide.call('ritual_ZN10QRingChunk5clearEv')

  @staticmethod
  def swap(*__, **_) -> Never:
    """
    Qt's 'void QRingChunk::swap(QRingChunk &other)': takes a type Python has
    no way to hand over yet.
    """
    raise NotImplementedError(
        "'QRingChunk.swap' has no cute function yet. Qt's 'void "
        "QRingChunk::swap(QRingChunk &other)': takes a type Python has no "
        "way to hand over yet.")

  @staticmethod
  def toByteArray(*__, **_) -> Never:
    """
    Qt's 'QByteArray QRingChunk::toByteArray()': can only be called on a
    value about to be thrown away.
    """
    raise NotImplementedError(
        "'QRingChunk.toByteArray' has no cute function yet. Qt's "
        "'QByteArray QRingChunk::toByteArray()': can only be called on a "
        "value about to be thrown away.")
