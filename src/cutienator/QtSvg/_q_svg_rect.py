"""
QSvgRect binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtSvg/6.12.0/QtSvg/private/qsvggraphics_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QSvgRect to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from . import QSvgNode

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QPointF, QRectF
  from ..QtGui import QPainter
  from . import QSvgExtraStates
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPainter = WAIT['QPainter']
  QRectF = WAIT['QRectF']
  QSvgExtraStates = WAIT['QSvgExtraStates']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSvgRect(QSvgNode):
  """
  The cute side of Qt's QSvgRect: a plain Python object standing in front of
  one C++ QSvgRect.

  It is built on the cute 'QSvgNode', as Qt's QSvgRect is built on Qt's
  QSvgNode, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QSvgRect that has a ritual and that Python can call
  so far, 4 names in all: 'type', 'separateFillStroke', 'rect', 'radius'. It
  can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSvgRect::~QSvgRect()': the destructor: Python never removes a C++
    QSvgRect.
  - Qt's 'void QSvgRect::drawCommand(QPainter *p, QSvgExtraStates &states)':
    takes a type Python has no way to hand over yet.
  - Qt's 'QRectF QSvgRect::internalFastBounds(QPainter *p, QSvgExtraStates
    &states) const': takes a type Python has no way to hand over yet.
  - Qt's 'QRectF QSvgRect::internalBounds(QPainter *p, QSvgExtraStates
    &states) const': takes a type Python has no way to hand over yet.
  - Qt's 'QRectF QSvgRect::decoratedInternalBounds(QPainter *p,
    QSvgExtraStates &states) const': takes a type Python has no way to hand
    over yet.
  - Qt's 'QRectF QSvgRect::internalBounds(QPainter *p, QSvgExtraStates
    &states, BoundsMode mode) const': takes a type Python has no way to hand
    over yet.

  What to expect
  --------------

  - The C++ QSvgRect is created at the first use, not by 'QSvgRect(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSvgRect.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSvgRect'

  #  A C++ QSvgRect Python makes is of a C++ class of ours, in which Python
  #  can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QSvgRect'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def type(self) -> QSvgNode.Type:
    """
    Calls Qt's 'Type QSvgRect::type() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgrect.html#type

    Returns
    -------

    QSvgNode.Type
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'QSvgNode.Type(number)'
      gives.
    """
    #  Type QSvgRect::type() const
    ritual = 'ritual_ZNK8QSvgRect4typeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK8QSvgRect4typeEv'
    return QSvgNode.Type(self.uglySide.call(ritual))

  @overload(QPainter, QSvgExtraStates)
  @overload(NoneType, QSvgExtraStates)
  def separateFillStroke(
      self,
      a0: Optional[QPainter],
      a1: QSvgExtraStates,
  ) -> bool:
    """
    Calls Qt's 'bool QSvgRect::separateFillStroke(const QPainter *a0, const
    QSvgExtraStates &a1) const'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgrect.html#separateFillStroke

    Parameters
    ----------

    a0 : Optional[QPainter]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    a1 : QSvgExtraStates
      Passed on as a value: Qt reads the C++ QSvgExtraStates, which stays
      Python's own.
    """
    #  bool QSvgRect::separateFillStroke(const QPainter *a0, const
    #      QSvgExtraStates &a1) const
    ritual = (
        'ritual_ZNK8QSvgRect18separateFillStrokeEPK8QPainterRK15QSvgExtraSt'
        'ates')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK8QSvgRect18separateFillStrokeEPK8QPainterRK15QSvgE'
          'xtraStates')
    return self.uglySide.call(ritual, self._addressOf(a0), self._valueOf(a1))

  def rect(self) -> QRectF:
    """
    Calls Qt's 'QRectF QSvgRect::rect() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgrect.html#rect

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QSvgRect::rect() const
    address = self.uglySide.call('ritual_ZNK8QSvgRect4rectEv')
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  def radius(self) -> QPointF:
    """
    Calls Qt's 'QPointF QSvgRect::radius() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgrect.html#radius

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QSvgRect::radius() const
    address = self.uglySide.call('ritual_ZNK8QSvgRect6radiusEv')
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

  @overload(QSvgNode, QRectF)
  @overload(NoneType, QRectF)
  @overload(QSvgNode, QRectF, float)
  @overload(NoneType, QRectF, float)
  @overload(QSvgNode, QRectF, float, float)
  @overload(NoneType, QRectF, float, float)
  def __init__(
      self,
      paren: Optional[QSvgNode],
      rect: QRectF,
      rx: float = 0.0,
      ry: float = 0.0,
  ) -> None:
    """
    Notes what was given, for Qt's 'QSvgRect::QSvgRect(QSvgNode *paren, const
    QRectF &rect, qreal rx, qreal ry)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qsvgrect.html#QSvgRect

    Parameters
    ----------

    paren : Optional[QSvgNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    rect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    rx : float
      Passed on as it is. May be left out, as in Qt: it is then 0.0.

    ry : float
      Passed on as it is. May be left out, as in Qt: it is then 0.0.
    """
    #  QSvgRect::QSvgRect(QSvgNode *paren, const QRectF &rect, qreal rx,
    #      qreal ry)
    self._noteCreation(QSvgRect, lambda: Rituals.call(
        'ritual_ZN8QSvgRectC1EP8QSvgNodeRK6QRectFdd',
        self._addressOf(paren), self._valueOf(rect), rx, ry,
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
