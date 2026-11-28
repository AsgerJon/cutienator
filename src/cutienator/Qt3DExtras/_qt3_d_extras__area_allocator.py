"""
Qt3DExtras::AreaAllocator binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DExtras/6.12.0/Qt3DExtras/private/areaallocator_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means Qt3DExtras::AreaAllocator to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
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


class AreaAllocator(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's Qt3DExtras::AreaAllocator: a plain Python object
  standing in front of one C++ Qt3DExtras::AreaAllocator.

  C++ hands a Qt3DExtras::AreaAllocator around as a copy, so every C++
  Qt3DExtras::AreaAllocator behind a cute one is Python's own: it is removed,
  by the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's Qt3DExtras::AreaAllocator that has a ritual and that
  Python can call so far, 4 names in all: 'allocate', 'deallocate',
  'isEmpty', 'size'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'Qt3DExtras::AreaAllocator::~AreaAllocator()': the destructor:
    Python removes its C++ Qt3DExtras::AreaAllocator by it, and has no other
    use for it.

  What has no ritual
  ------------------

  3 of the 9 functions Qt declares: 3 the compiler refuses its ritual as it
  would be written here.

  What to expect
  --------------

  - The C++ Qt3DExtras::AreaAllocator is created at the first use, not by
    'Qt3DExtras::AreaAllocator(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a Qt3DExtras::AreaAllocator back gives a copy the
    ritual made for Python, in a new cute Qt3DExtras::AreaAllocator.
  - Each name of Qt's Qt3DExtras::AreaAllocator that has no cute function
    yet, 'allocateInNode', 'deallocateInNode', 'mergeNodeWithNeighbors',
    holds a function that raises 'NotImplementedError', and its docstring
    says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DExtras::AreaAllocator'

  #  Qt's '~Qt3DExtras::AreaAllocator()'. Naming it makes this a value class:
  #  Python owns every C++ Qt3DExtras::AreaAllocator behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN10Qt3DExtras13AreaAllocatorD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isEmpty(self) -> bool:
    """
    Calls Qt's 'bool Qt3DExtras::AreaAllocator::isEmpty() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-areaallocator.html#isEmpty
    """
    #  bool Qt3DExtras::AreaAllocator::isEmpty() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DExtras13AreaAllocator7isEmptyEv',
    )

  def size(self) -> QSize:
    """
    Calls Qt's 'QSize Qt3DExtras::AreaAllocator::size() const'.

    Qt's own words: https://doc.qt.io/qt-6/qt3dextras-areaallocator.html#size

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize Qt3DExtras::AreaAllocator::size() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DExtras13AreaAllocator4sizeEv',
    )
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
    Notes what was given, for Qt's
    'Qt3DExtras::AreaAllocator::AreaAllocator(const QSize &size)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-areaallocator.html#AreaAllocator

    Parameters
    ----------

    size : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.
    """
    #  Qt3DExtras::AreaAllocator::AreaAllocator(const QSize &size)
    self._noteCreation(AreaAllocator, lambda: Rituals.call(
        'ritual_ZN10Qt3DExtras13AreaAllocatorC1ERK5QSize',
        self._valueOf(size),
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
    Calls Qt's 'QRect Qt3DExtras::AreaAllocator::allocate(const QSize
    &size)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-areaallocator.html#allocate

    Parameters
    ----------

    size : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect Qt3DExtras::AreaAllocator::allocate(const QSize &size)
    address = self.uglySide.call(
        'ritual_ZN10Qt3DExtras13AreaAllocator8allocateERK5QSize',
        self._valueOf(size),
    )
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

  @overload(QRect)
  def deallocate(self, rect: QRect) -> bool:
    """
    Calls Qt's 'bool Qt3DExtras::AreaAllocator::deallocate(const QRect
    &rect)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-areaallocator.html#deallocate

    Parameters
    ----------

    rect : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.
    """
    #  bool Qt3DExtras::AreaAllocator::deallocate(const QRect &rect)
    return self.uglySide.call(
        'ritual_ZN10Qt3DExtras13AreaAllocator10deallocateERK5QRect',
        self._valueOf(rect),
    )

  @staticmethod
  def allocateInNode(*__, **_) -> Never:
    """
    Qt's 'bool Qt3DExtras::AreaAllocator::allocateInNode(const QSize &size,
    QPoint &result, const QRect &currentRect, AreaAllocatorNode *node)': the
    compiler refuses its ritual as it would be written here: unknown type
    name 'AreaAllocatorNode'; did you mean 'Qt3DExtras::AreaAllocatorNode'?.
    """
    raise NotImplementedError(
        "'Qt3DExtras.AreaAllocator.allocateInNode' has no cute function "
        "yet. Qt's 'bool Qt3DExtras::AreaAllocator::allocateInNode(const "
        "QSize &size, QPoint &result, const QRect &currentRect, "
        "AreaAllocatorNode *node)': the compiler refuses its ritual as it "
        "would be written here: unknown type name 'AreaAllocatorNode'; did "
        "you mean 'Qt3DExtras::AreaAllocatorNode'?.")

  @staticmethod
  def deallocateInNode(*__, **_) -> Never:
    """
    Qt's 'bool Qt3DExtras::AreaAllocator::deallocateInNode(const QPoint &pos,
    AreaAllocatorNode *node)': the compiler refuses its ritual as it would be
    written here: unknown type name 'AreaAllocatorNode'; did you mean
    'Qt3DExtras::AreaAllocatorNode'?.
    """
    raise NotImplementedError(
        "'Qt3DExtras.AreaAllocator.deallocateInNode' has no cute function "
        "yet. Qt's 'bool Qt3DExtras::AreaAllocator::deallocateInNode(const "
        "QPoint &pos, AreaAllocatorNode *node)': the compiler refuses its "
        "ritual as it would be written here: unknown type name "
        "'AreaAllocatorNode'; did you mean 'Qt3DExtras::AreaAllocatorNode'?."
    )

  @staticmethod
  def mergeNodeWithNeighbors(*__, **_) -> Never:
    """
    Qt's 'void
    Qt3DExtras::AreaAllocator::mergeNodeWithNeighbors(AreaAllocatorNode
    *node)': the compiler refuses its ritual as it would be written here:
    unknown type name 'AreaAllocatorNode'; did you mean
    'Qt3DExtras::AreaAllocatorNode'?.
    """
    raise NotImplementedError(
        "'Qt3DExtras.AreaAllocator.mergeNodeWithNeighbors' has no cute "
        "function yet. Qt's 'void "
        "Qt3DExtras::AreaAllocator::mergeNodeWithNeighbors(AreaAllocatorNode"
        " *node)': the compiler refuses its ritual as it would be written "
        "here: unknown type name 'AreaAllocatorNode'; did you mean "
        "'Qt3DExtras::AreaAllocatorNode'?.")
