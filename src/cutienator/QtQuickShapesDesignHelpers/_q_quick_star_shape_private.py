"""
QQuickStarShapePrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickShapesDesignHelpers/6.12.0/QtQuickShapesDesignHelpers/private/qquickstarshape_p_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuickStarShapePrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QQuickStarShape


class QQuickStarShapePrivate(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQuickStarShapePrivate: a plain Python object
  standing in front of one C++ QQuickStarShapePrivate.

  What exists
  -----------

  Every function of Qt's QQuickStarShapePrivate that has a ritual and that
  Python can call so far, 5 names in all: 'q_func', 'updatePath',
  'updatePoints', 'constructPolygonPath', 'constructRoundedPolygonPath'. It
  can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QQuickStarShape *QQuickStarShapePrivate::q_func() const':
    takes in Python what 'QQuickStarShape *QQuickStarShapePrivate::q_func()'
    takes.
  - Qt's 'QQuickStarShapePrivate::~QQuickStarShapePrivate()': the destructor:
    Python never removes a C++ QQuickStarShapePrivate.

  What to expect
  --------------

  - The C++ QQuickStarShapePrivate is created at the first use, not by
    'QQuickStarShapePrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickStarShapePrivate.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickStarShapePrivate'

  #  A C++ QQuickStarShapePrivate Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickStarShapePrivate'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

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
    Notes what was given, for Qt's
    'QQuickStarShapePrivate::QQuickStarShapePrivate()', which is called at
    the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickstarshapeprivate.html#QQuickStarShapePrivate
    """
    #  QQuickStarShapePrivate::QQuickStarShapePrivate()
    self._noteCreation(QQuickStarShapePrivate, lambda: Rituals.call(
        'ritual_ZN22QQuickStarShapePrivateC1Ev',
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

  def q_func(self) -> Optional[QQuickStarShape]:
    """
    Calls Qt's 'QQuickStarShape *QQuickStarShapePrivate::q_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickstarshapeprivate.html#q_func

    Returns
    -------

    Optional[QQuickStarShape]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickStarShape *QQuickStarShapePrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN22QQuickStarShapePrivate6q_funcEv',
    )
    from . import QQuickStarShape
    return QQuickStarShape._cuteAt(address)

  def updatePath(self) -> None:
    """
    Calls Qt's 'void QQuickStarShapePrivate::updatePath()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickstarshapeprivate.html#updatePath
    """
    #  void QQuickStarShapePrivate::updatePath()
    self.uglySide.call('ritual_ZN22QQuickStarShapePrivate10updatePathEv')

  def updatePoints(self) -> None:
    """
    Calls Qt's 'void QQuickStarShapePrivate::updatePoints()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickstarshapeprivate.html#updatePoints
    """
    #  void QQuickStarShapePrivate::updatePoints()
    self.uglySide.call('ritual_ZN22QQuickStarShapePrivate12updatePointsEv')

  def constructPolygonPath(self) -> None:
    """
    Calls Qt's 'void QQuickStarShapePrivate::constructPolygonPath()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickstarshapeprivate.html#constructPolygonPath
    """
    #  void QQuickStarShapePrivate::constructPolygonPath()
    self.uglySide.call(
        'ritual_ZN22QQuickStarShapePrivate20constructPolygonPathEv',
    )

  def constructRoundedPolygonPath(self) -> None:
    """
    Calls Qt's 'void QQuickStarShapePrivate::constructRoundedPolygonPath()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickstarshapeprivate.html
    """
    #  void QQuickStarShapePrivate::constructRoundedPolygonPath()
    self.uglySide.call(
        'ritual_ZN22QQuickStarShapePrivate27constructRoundedPolygonPathEv',
    )
