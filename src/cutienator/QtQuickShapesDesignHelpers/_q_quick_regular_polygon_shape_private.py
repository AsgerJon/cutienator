"""
QQuickRegularPolygonShapePrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickShapesDesignHelpers/6.12.0/QtQuickShapesDesignHelpers/private/qquickregularpolygonshape_p_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuickRegularPolygonShapePrivate to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QQuickRegularPolygonShape


class QQuickRegularPolygonShapePrivate(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQuickRegularPolygonShapePrivate: a plain Python
  object standing in front of one C++ QQuickRegularPolygonShapePrivate.

  What exists
  -----------

  Every function of Qt's QQuickRegularPolygonShapePrivate that has a ritual
  and that Python can call so far, 6 names in all: 'q_func', 'updatePath',
  'updatePoints', 'updateBisectors', 'constructPolygonPath',
  'constructRoundedPolygonPath'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QQuickRegularPolygonShape
    *QQuickRegularPolygonShapePrivate::q_func() const': takes in Python what
    'QQuickRegularPolygonShape *QQuickRegularPolygonShapePrivate::q_func()'
    takes.
  - Qt's
    'QQuickRegularPolygonShapePrivate::~QQuickRegularPolygonShapePrivate()':
    the destructor: Python never removes a C++
    QQuickRegularPolygonShapePrivate.

  What to expect
  --------------

  - The C++ QQuickRegularPolygonShapePrivate is created at the first use, not
    by 'QQuickRegularPolygonShapePrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickRegularPolygonShapePrivate.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickRegularPolygonShapePrivate'

  #  A C++ QQuickRegularPolygonShapePrivate Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickRegularPolygonShapePrivate'

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
    'QQuickRegularPolygonShapePrivate::QQuickRegularPolygonShapePrivate()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickregularpolygonshapeprivate.html
    """
    #  QQuickRegularPolygonShapePrivate::QQuickRegularPolygonShapePrivate()
    self._noteCreation(
        QQuickRegularPolygonShapePrivate, lambda: Rituals.call(
            'ritual_ZN32QQuickRegularPolygonShapePrivateC1Ev',
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

  def q_func(self) -> Optional[QQuickRegularPolygonShape]:
    """
    Calls Qt's 'QQuickRegularPolygonShape
    *QQuickRegularPolygonShapePrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickregularpolygonshapeprivate.html#q_func

    Returns
    -------

    Optional[QQuickRegularPolygonShape]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickRegularPolygonShape *QQuickRegularPolygonShapePrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN32QQuickRegularPolygonShapePrivate6q_funcEv',
    )
    from . import QQuickRegularPolygonShape
    return QQuickRegularPolygonShape._cuteAt(address)

  def updatePath(self) -> None:
    """
    Calls Qt's 'void QQuickRegularPolygonShapePrivate::updatePath()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickregularpolygonshapeprivate.html#updatePath
    """
    #  void QQuickRegularPolygonShapePrivate::updatePath()
    self.uglySide.call(
        'ritual_ZN32QQuickRegularPolygonShapePrivate10updatePathEv',
    )

  def updatePoints(self) -> None:
    """
    Calls Qt's 'void QQuickRegularPolygonShapePrivate::updatePoints()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickregularpolygonshapeprivate.html#updatePoints
    """
    #  void QQuickRegularPolygonShapePrivate::updatePoints()
    self.uglySide.call(
        'ritual_ZN32QQuickRegularPolygonShapePrivate12updatePointsEv',
    )

  def updateBisectors(self) -> None:
    """
    Calls Qt's 'void QQuickRegularPolygonShapePrivate::updateBisectors()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickregularpolygonshapeprivate.html
    """
    #  void QQuickRegularPolygonShapePrivate::updateBisectors()
    self.uglySide.call(
        'ritual_ZN32QQuickRegularPolygonShapePrivate15updateBisectorsEv',
    )

  def constructPolygonPath(self) -> None:
    """
    Calls Qt's 'void
    QQuickRegularPolygonShapePrivate::constructPolygonPath()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickregularpolygonshapeprivate.html
    """
    #  void QQuickRegularPolygonShapePrivate::constructPolygonPath()
    self.uglySide.call(
        'ritual_ZN32QQuickRegularPolygonShapePrivate20constructPolygonPathE'
        'v',
    )

  def constructRoundedPolygonPath(self) -> None:
    """
    Calls Qt's 'void
    QQuickRegularPolygonShapePrivate::constructRoundedPolygonPath()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickregularpolygonshapeprivate.html
    """
    #  void QQuickRegularPolygonShapePrivate::constructRoundedPolygonPath()
    self.uglySide.call(
        'ritual_ZN32QQuickRegularPolygonShapePrivate27constructRoundedPolyg'
        'onPathEv',
    )
