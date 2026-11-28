"""
QQuickParentAnimationPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquickitemanimation_p_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QQuickParentAnimationPrivate to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from . import QQuickAnimationGroupPrivate, QQuickItem

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QPointF
  from . import QQuickParentAnimation


class QQuickParentAnimationPrivate(QQuickAnimationGroupPrivate):
  """
  The cute side of Qt's QQuickParentAnimationPrivate: a plain Python object
  standing in front of one C++ QQuickParentAnimationPrivate.

  It is built on the cute 'QQuickAnimationGroupPrivate', as Qt's
  QQuickParentAnimationPrivate is built on Qt's QQuickAnimationGroupPrivate,
  and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickParentAnimationPrivate that has a ritual and
  that Python can call so far, 2 names in all: 'q_func',
  'computeTransformOrigin'. None can be made from Python: one comes out of a
  function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QQuickParentAnimation *QQuickParentAnimationPrivate::q_func()
    const': takes in Python what 'QQuickParentAnimation
    *QQuickParentAnimationPrivate::q_func()' takes.

  What has no ritual
  ------------------

  1 of the 4 functions Qt declares: 1 leans on 'non-virtual thunk to
  QQuickAnimationGroupPrivate.

  What to expect
  --------------

  - The C++ QQuickParentAnimationPrivate is created at the first use, not by
    'QQuickParentAnimationPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickParentAnimationPrivate.
  - Each name of Qt's QQuickParentAnimationPrivate that has no cute function
    yet, '__init__', holds a function that raises 'NotImplementedError', and
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
  __qt_class__ = 'QQuickParentAnimationPrivate'

  #  A C++ QQuickParentAnimationPrivate Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickParentAnimationPrivate'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QQuickItem.TransformOrigin, float, float)
  def computeTransformOrigin(
      self,
      origin: QQuickItem.TransformOrigin,
      width: float,
      height: float,
  ) -> QPointF:
    """
    Calls Qt's 'QPointF
    QQuickParentAnimationPrivate::computeTransformOrigin(QQuickItem::
    TransformOrigin origin, qreal width, qreal height) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickparentanimationprivate.html

    Parameters
    ----------

    origin : QQuickItem.TransformOrigin
      Passed on as its number.

    width : float
      Passed on as it is.

    height : float
      Passed on as it is.

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF
    #      QQuickParentAnimationPrivate::computeTransformOrigin(QQuickItem::
    #      TransformOrigin origin, qreal width, qreal height) const
    address = self.uglySide.call(
        'ritual_ZNK28QQuickParentAnimationPrivate22computeTransformOriginEN'
        '10QQuickItem15TransformOriginEdd',
        origin.value, width, height,
    )
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'QQuickParentAnimationPrivate::QQuickParentAnimationPrivate()':
    leans on 'non-virtual thunk to
    QQuickAnimationGroupPrivate::animationCurrentLoopChanged(
    QAbstractAnimationJob*)', which Qt's source does not mark for use from
    outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQuickParentAnimationPrivate.__init__' has no cute function yet. "
        "Qt's "
        "'QQuickParentAnimationPrivate::QQuickParentAnimationPrivate()': "
        "leans on 'non-virtual thunk to "
        "QQuickAnimationGroupPrivate::animationCurrentLoopChanged(QAbstractA"
        "nimationJob*)', which Qt's source does not mark for use from "
        "outside Qt and has no code for that could be taken.")

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

  def q_func(self) -> Optional[QQuickParentAnimation]:
    """
    Calls Qt's 'QQuickParentAnimation
    *QQuickParentAnimationPrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickparentanimationprivate.html#q_func

    Returns
    -------

    Optional[QQuickParentAnimation]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickParentAnimation *QQuickParentAnimationPrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN28QQuickParentAnimationPrivate6q_funcEv',
    )
    from . import QQuickParentAnimation
    return QQuickParentAnimation._cuteAt(address)
