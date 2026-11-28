"""
QSGAreaAllocator binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qsgareaallocator_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QSGAreaAllocator to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QByteArray, QRect, QSize
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QRect = WAIT['QRect']
  QSize = WAIT['QSize']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSGAreaAllocator(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QSGAreaAllocator: a plain Python object standing in
  front of one C++ QSGAreaAllocator.

  C++ hands a QSGAreaAllocator around as a copy, so every C++
  QSGAreaAllocator behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QSGAreaAllocator that has a ritual and that Python
  can call so far, 6 names in all: 'allocate', 'deallocate', 'isEmpty',
  'size', 'serialize', 'deserialize'. It can be made from Python, in 1 way;
  see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSGAreaAllocator::~QSGAreaAllocator()': the destructor: Python
    removes its C++ QSGAreaAllocator by it, and has no other use for it.
  - Qt's 'bool QSGAreaAllocator::allocateInNode(const QSize &size, QPoint
    &result, const QRect &currentRect, QSGAreaAllocatorNode *node)': takes a
    type Python has no way to hand over yet.
  - Qt's 'bool QSGAreaAllocator::deallocateInNode(const QPoint &pos,
    QSGAreaAllocatorNode *node)': names 'QSGAreaAllocatorNode', which has no
    cute class yet.
  - Qt's 'void QSGAreaAllocator::mergeNodeWithNeighbors(QSGAreaAllocatorNode
    *node)': names 'QSGAreaAllocatorNode', which has no cute class yet.

  What to expect
  --------------

  - The C++ QSGAreaAllocator is created at the first use, not by
    'QSGAreaAllocator(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QSGAreaAllocator back gives a copy the ritual made
    for Python, in a new cute QSGAreaAllocator.
  - Each name of Qt's QSGAreaAllocator that has no cute function yet,
    'allocateInNode', 'deallocateInNode', 'mergeNodeWithNeighbors', holds a
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
  __qt_class__ = 'QSGAreaAllocator'

  #  Qt's '~QSGAreaAllocator()'. Naming it makes this a value class: Python
  #  owns every C++ QSGAreaAllocator behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN16QSGAreaAllocatorD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isEmpty(self) -> bool:
    """
    Calls Qt's 'bool QSGAreaAllocator::isEmpty() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsgareaallocator.html#isEmpty
    """
    #  bool QSGAreaAllocator::isEmpty() const
    return self.uglySide.call('ritual_ZNK16QSGAreaAllocator7isEmptyEv')

  def size(self) -> QSize:
    """
    Calls Qt's 'QSize QSGAreaAllocator::size() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsgareaallocator.html#size

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QSGAreaAllocator::size() const
    address = self.uglySide.call('ritual_ZNK16QSGAreaAllocator4sizeEv')
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

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

  @overload(QSize)
  def __init__(self, size: QSize) -> None:
    """
    Notes what was given, for Qt's 'QSGAreaAllocator::QSGAreaAllocator(const
    QSize &size)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgareaallocator.html#QSGAreaAllocator

    Parameters
    ----------

    size : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.
    """
    #  QSGAreaAllocator::QSGAreaAllocator(const QSize &size)
    self._noteCreation(QSGAreaAllocator, lambda: Rituals.call(
        'ritual_ZN16QSGAreaAllocatorC1ERK5QSize', self._valueOf(size),
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

  @overload(QSize)
  def allocate(self, size: QSize) -> QRect:
    """
    Calls Qt's 'QRect QSGAreaAllocator::allocate(const QSize &size)'.

    Qt's own words: https://doc.qt.io/qt-6/qsgareaallocator.html#allocate

    Parameters
    ----------

    size : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect QSGAreaAllocator::allocate(const QSize &size)
    address = self.uglySide.call(
        'ritual_ZN16QSGAreaAllocator8allocateERK5QSize', self._valueOf(size),
    )
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

  @overload(QRect)
  def deallocate(self, rect: QRect) -> bool:
    """
    Calls Qt's 'bool QSGAreaAllocator::deallocate(const QRect &rect)'.

    Qt's own words: https://doc.qt.io/qt-6/qsgareaallocator.html#deallocate

    Parameters
    ----------

    rect : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.
    """
    #  bool QSGAreaAllocator::deallocate(const QRect &rect)
    return self.uglySide.call(
        'ritual_ZN16QSGAreaAllocator10deallocateERK5QRect',
        self._valueOf(rect),
    )

  def serialize(self) -> QByteArray:
    """
    Calls Qt's 'QByteArray QSGAreaAllocator::serialize()'.

    Qt's own words: https://doc.qt.io/qt-6/qsgareaallocator.html#serialize

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QSGAreaAllocator::serialize()
    address = self.uglySide.call('ritual_ZN16QSGAreaAllocator9serializeEv')
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  @overload(str, int)
  @overload(NoneType, int)
  def deserialize(self, data: Optional[str], size: int) -> Optional[str]:
    """
    Calls Qt's 'const char *QSGAreaAllocator::deserialize(const char *data,
    int size)'.

    Qt's own words: https://doc.qt.io/qt-6/qsgareaallocator.html#deserialize

    Parameters
    ----------

    data : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    size : int
      Passed on as it is.

    Returns
    -------

    Optional[str]
      The text Qt gave back. None when Qt gave back no text.
    """
    #  const char *QSGAreaAllocator::deserialize(const char *data, int size)
    chars = self.uglySide.call(
        'ritual_ZN16QSGAreaAllocator11deserializeEPKci',
        self._bytesOf(data), size,
    )
    return None if chars is None else chars.decode()

  @staticmethod
  def allocateInNode(*__, **_) -> Never:
    """
    Qt's 'bool QSGAreaAllocator::allocateInNode(const QSize &size, QPoint
    &result, const QRect &currentRect, QSGAreaAllocatorNode *node)': takes a
    type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QSGAreaAllocator.allocateInNode' has no cute function yet. Qt's "
        "'bool QSGAreaAllocator::allocateInNode(const QSize &size, QPoint "
        "&result, const QRect &currentRect, QSGAreaAllocatorNode *node)': "
        "takes a type Python has no way to hand over yet.")

  @staticmethod
  def deallocateInNode(*__, **_) -> Never:
    """
    Qt's 'bool QSGAreaAllocator::deallocateInNode(const QPoint &pos,
    QSGAreaAllocatorNode *node)': names 'QSGAreaAllocatorNode', which has no
    cute class yet.
    """
    raise NotImplementedError(
        "'QSGAreaAllocator.deallocateInNode' has no cute function yet. Qt's "
        "'bool QSGAreaAllocator::deallocateInNode(const QPoint &pos, "
        "QSGAreaAllocatorNode *node)': names 'QSGAreaAllocatorNode', which "
        "has no cute class yet.")

  @staticmethod
  def mergeNodeWithNeighbors(*__, **_) -> Never:
    """
    Qt's 'void QSGAreaAllocator::mergeNodeWithNeighbors(QSGAreaAllocatorNode
    *node)': names 'QSGAreaAllocatorNode', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QSGAreaAllocator.mergeNodeWithNeighbors' has no cute function "
        "yet. Qt's 'void "
        "QSGAreaAllocator::mergeNodeWithNeighbors(QSGAreaAllocatorNode "
        "*node)': names 'QSGAreaAllocatorNode', which has no cute class yet."
    )
