"""
QPathEdge binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qpathclipper_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QPathEdge to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute
from ..occult import Rituals


class QPathEdge(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QPathEdge: a plain Python object standing in front of
  one C++ QPathEdge.

  C++ hands a QPathEdge around as a copy, so every C++ QPathEdge behind a
  cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QPathEdge that has a ritual and that Python can call
  so far, 4 names in all: 'next', 'setNext', 'directionTo', 'vertex'. It can
  be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QPathEdge::~QPathEdge()': the destructor: Python removes its C++
    QPathEdge by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QPathEdge is created at the first use, not by 'QPathEdge(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QPathEdge back gives a copy the ritual made for
    Python, in a new cute QPathEdge.
  """

  #  The enums Qt writes inside QPathEdge, each a class in here as in C++,
  #  and the names Qt has for the combinations of its flags enums.

  class Direction(CuteNum):
    """
    The enum 'QPathEdge::Direction' of Qt, with the 2 names Qt gives in it.
    """

    Forward = Kee[int](0)
    Backward = Kee[int](1)

  class Traversal(CuteNum):
    """
    The enum 'QPathEdge::Traversal' of Qt, with the 2 names Qt gives in it.
    """

    RightTraversal = Kee[int](0)
    LeftTraversal = Kee[int](1)

  class Type(CuteNum):
    """The enum 'QPathEdge::Type' of Qt, with the 2 names Qt gives in it."""

    Line = Kee[int](0)
    Curve = Kee[int](1)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QPathEdge'

  #  Qt's '~QPathEdge()'. Naming it makes this a value class: Python owns
  #  every C++ QPathEdge behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN9QPathEdgeD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(Traversal, Direction)
  def next(self, traversal: Traversal, direction: Direction) -> int:
    """
    Calls Qt's 'int QPathEdge::next(Traversal traversal, Direction direction)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qpathedge.html#next

    Parameters
    ----------

    traversal : Traversal
      Passed on as its number.

    direction : Direction
      Passed on as its number.
    """
    #  int QPathEdge::next(Traversal traversal, Direction direction) const
    return self.uglySide.call(
        'ritual_ZNK9QPathEdge4nextENS_9TraversalENS_9DirectionE',
        traversal.value, direction.value,
    )

  @overload(int)
  def directionTo(self, vertex: int) -> Direction:
    """
    Calls Qt's 'Direction QPathEdge::directionTo(int vertex) const'.

    Qt's own words: https://doc.qt.io/qt-6/qpathedge.html#directionTo

    Parameters
    ----------

    vertex : int
      Passed on as it is.

    Returns
    -------

    Direction
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Direction(number)' gives.
    """
    #  Direction QPathEdge::directionTo(int vertex) const
    return QPathEdge.Direction(self.uglySide.call(
        'ritual_ZNK9QPathEdge11directionToEi', vertex,
    ))

  @overload(Direction)
  def vertex(self, direction: Direction) -> int:
    """
    Calls Qt's 'int QPathEdge::vertex(Direction direction) const'.

    Qt's own words: https://doc.qt.io/qt-6/qpathedge.html#vertex

    Parameters
    ----------

    direction : Direction
      Passed on as its number.
    """
    #  int QPathEdge::vertex(Direction direction) const
    return self.uglySide.call(
        'ritual_ZNK9QPathEdge6vertexENS_9DirectionE', direction.value,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(Traversal, Direction, int)
  def setNext(
      self,
      traversal: Traversal,
      direction: Direction,
      next: int,
  ) -> None:
    """
    Calls Qt's 'void QPathEdge::setNext(Traversal traversal, Direction
    direction, int next)'.

    Qt's own words: https://doc.qt.io/qt-6/qpathedge.html#setNext

    Parameters
    ----------

    traversal : Traversal
      Passed on as its number.

    direction : Direction
      Passed on as its number.

    next : int
      Passed on as it is.
    """
    #  void QPathEdge::setNext(Traversal traversal, Direction direction, int
    #      next)
    self.uglySide.call(
        'ritual_ZN9QPathEdge7setNextENS_9TraversalENS_9DirectionEi',
        traversal.value, direction.value, next,
    )

  @overload(Direction, int)
  def setNext(self, direction: Direction, next: int) -> None:
    """
    Calls Qt's 'void QPathEdge::setNext(Direction direction, int next)'.

    Qt's own words: https://doc.qt.io/qt-6/qpathedge.html#setNext

    Parameters
    ----------

    direction : Direction
      Passed on as its number.

    next : int
      Passed on as it is.
    """
    #  void QPathEdge::setNext(Direction direction, int next)
    self.uglySide.call(
        'ritual_ZN9QPathEdge7setNextENS_9DirectionEi', direction.value, next,
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
  @overload(int)
  @overload(int, int)
  def __init__(self, a: int = -1, b: int = -1) -> None:
    """
    Notes what was given, for Qt's 'QPathEdge::QPathEdge(int a, int b)',
    which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qpathedge.html#QPathEdge

    Parameters
    ----------

    a : int
      Passed on as it is. May be left out, as in Qt: it is then -1.

    b : int
      Passed on as it is. May be left out, as in Qt: it is then -1.
    """
    #  QPathEdge::QPathEdge(int a, int b)
    self._noteCreation(QPathEdge, lambda: Rituals.call(
        'ritual_ZN9QPathEdgeC1Eii', a, b,
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
