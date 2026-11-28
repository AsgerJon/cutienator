"""
QCAreaAllocator binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCanvasPainter/6.12.0/QtCanvasPainter/private/qcareaallocator_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QCAreaAllocator to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from ..QtCore import QRect, QSize
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QRect = WAIT['QRect']
  QSize = WAIT['QSize']


class QCAreaAllocator(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QCAreaAllocator: a plain Python object standing in
  front of one C++ QCAreaAllocator.

  C++ hands a QCAreaAllocator around as a copy, so every C++ QCAreaAllocator
  behind a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QCAreaAllocator that has a ritual and that Python
  can call so far, 4 names in all: 'allocate', 'deallocate', 'isEmpty',
  'size'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QCAreaAllocator::~QCAreaAllocator()': the destructor: Python
    removes its C++ QCAreaAllocator by it, and has no other use for it.

  What has no ritual
  ------------------

  3 of the 9 functions Qt declares: 3 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file.

  What to expect
  --------------

  - The C++ QCAreaAllocator is created at the first use, not by
    'QCAreaAllocator(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QCAreaAllocator back gives a copy the ritual made for
    Python, in a new cute QCAreaAllocator.
  - Each name of Qt's QCAreaAllocator that has no cute function yet,
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
  __qt_class__ = 'QCAreaAllocator'

  #  Qt's '~QCAreaAllocator()'. Naming it makes this a value class: Python
  #  owns every C++ QCAreaAllocator behind a cute one, and removes it by this
  #  ritual.
  __delete_ritual__ = 'ritual_ZN15QCAreaAllocatorD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isEmpty(self) -> bool:
    """
    Calls Qt's 'bool QCAreaAllocator::isEmpty() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcareaallocator.html#isEmpty
    """
    #  bool QCAreaAllocator::isEmpty() const
    return self.uglySide.call('ritual_ZNK15QCAreaAllocator7isEmptyEv')

  def size(self) -> QSize:
    """
    Calls Qt's 'QSize QCAreaAllocator::size() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcareaallocator.html#size

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QCAreaAllocator::size() const
    address = self.uglySide.call('ritual_ZNK15QCAreaAllocator4sizeEv')
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
    Notes what was given, for Qt's 'QCAreaAllocator::QCAreaAllocator(QSize
    size)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qcareaallocator.html#QCAreaAllocator

    Parameters
    ----------

    size : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.
    """
    #  QCAreaAllocator::QCAreaAllocator(QSize size)
    self._noteCreation(QCAreaAllocator, lambda: Rituals.call(
        'ritual_ZN15QCAreaAllocatorC1E5QSize', self._valueOf(size),
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
    Calls Qt's 'QRect QCAreaAllocator::allocate(QSize size)'.

    Qt's own words: https://doc.qt.io/qt-6/qcareaallocator.html#allocate

    Parameters
    ----------

    size : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect QCAreaAllocator::allocate(QSize size)
    address = self.uglySide.call(
        'ritual_ZN15QCAreaAllocator8allocateE5QSize', self._valueOf(size),
    )
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

  @overload(QRect)
  def deallocate(self, rect: QRect) -> bool:
    """
    Calls Qt's 'bool QCAreaAllocator::deallocate(QRect rect)'.

    Qt's own words: https://doc.qt.io/qt-6/qcareaallocator.html#deallocate

    Parameters
    ----------

    rect : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.
    """
    #  bool QCAreaAllocator::deallocate(QRect rect)
    return self.uglySide.call(
        'ritual_ZN15QCAreaAllocator10deallocateE5QRect', self._valueOf(rect),
    )

  @staticmethod
  def allocateInNode(*__, **_) -> Never:
    """
    Qt's 'bool QCAreaAllocator::allocateInNode(QSize size, QPoint &result,
    QRect currentRect, QCAreaAllocatorNode *node)': Qt's library has no name
    for it, and its code in Qt's source does not compile apart from its file:
    member access into incomplete type 'QCAreaAllocatorNode'.
    """
    raise NotImplementedError(
        "'QCAreaAllocator.allocateInNode' has no cute function yet. Qt's "
        "'bool QCAreaAllocator::allocateInNode(QSize size, QPoint &result, "
        "QRect currentRect, QCAreaAllocatorNode *node)': Qt's library has "
        "no name for it, and its code in Qt's source does not compile apart "
        "from its file: member access into incomplete type "
        "'QCAreaAllocatorNode'.")

  @staticmethod
  def deallocateInNode(*__, **_) -> Never:
    """
    Qt's 'bool QCAreaAllocator::deallocateInNode(QPoint pos,
    QCAreaAllocatorNode *node)': Qt's library has no name for it, and its
    code in Qt's source does not compile apart from its file: member access
    into incomplete type 'QCAreaAllocatorNode'.
    """
    raise NotImplementedError(
        "'QCAreaAllocator.deallocateInNode' has no cute function yet. Qt's "
        "'bool QCAreaAllocator::deallocateInNode(QPoint pos, "
        "QCAreaAllocatorNode *node)': Qt's library has no name for it, and "
        "its code in Qt's source does not compile apart from its file: "
        "member access into incomplete type 'QCAreaAllocatorNode'.")

  @staticmethod
  def mergeNodeWithNeighbors(*__, **_) -> Never:
    """
    Qt's 'void QCAreaAllocator::mergeNodeWithNeighbors(QCAreaAllocatorNode
    *node)': Qt's library has no name for it, and its code in Qt's source
    does not compile apart from its file: member access into incomplete type
    'QCAreaAllocatorNode'.
    """
    raise NotImplementedError(
        "'QCAreaAllocator.mergeNodeWithNeighbors' has no cute function yet. "
        "Qt's 'void "
        "QCAreaAllocator::mergeNodeWithNeighbors(QCAreaAllocatorNode "
        "*node)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: member access into "
        "incomplete type 'QCAreaAllocatorNode'.")
