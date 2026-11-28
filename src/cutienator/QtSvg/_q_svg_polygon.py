"""
QSvgPolygon binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtSvg/6.12.0/QtSvg/private/qsvggraphics_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QSvgPolygon to be private: it declares the class in a header it
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

  from ..QtGui import QPainter, QPolygonF
  from . import QSvgExtraStates
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPainter = WAIT['QPainter']
  QPolygonF = WAIT['QPolygonF']
  QSvgExtraStates = WAIT['QSvgExtraStates']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSvgPolygon(QSvgNode):
  """
  The cute side of Qt's QSvgPolygon: a plain Python object standing in front
  of one C++ QSvgPolygon.

  It is built on the cute 'QSvgNode', as Qt's QSvgPolygon is built on Qt's
  QSvgNode, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QSvgPolygon that has a ritual and that Python can
  call so far, 4 names in all: 'separateFillStroke', 'type',
  'requiresGroupRendering', 'polygon'. It can be made from Python, in 1 way;
  see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSvgPolygon::~QSvgPolygon()': the destructor: Python never removes
    a C++ QSvgPolygon.
  - Qt's 'void QSvgPolygon::drawCommand(QPainter *p, QSvgExtraStates
    &states)': takes a type Python has no way to hand over yet.
  - Qt's 'QRectF QSvgPolygon::internalFastBounds(QPainter *p, QSvgExtraStates
    &states) const': takes a type Python has no way to hand over yet.
  - Qt's 'QRectF QSvgPolygon::internalBounds(QPainter *p, QSvgExtraStates
    &states) const': takes a type Python has no way to hand over yet.
  - Qt's 'QRectF QSvgPolygon::decoratedInternalBounds(QPainter *p,
    QSvgExtraStates &states) const': takes a type Python has no way to hand
    over yet.
  - Qt's 'QRectF QSvgPolygon::internalBounds(QPainter *p, QSvgExtraStates
    &states, BoundsMode mode) const': takes a type Python has no way to hand
    over yet.

  What to expect
  --------------

  - The C++ QSvgPolygon is created at the first use, not by
    'QSvgPolygon(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSvgPolygon.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSvgPolygon'

  #  A C++ QSvgPolygon Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QSvgPolygon'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QPainter, QSvgExtraStates)
  @overload(NoneType, QSvgExtraStates)
  def separateFillStroke(
      self,
      a0: Optional[QPainter],
      a1: QSvgExtraStates,
  ) -> bool:
    """
    Calls Qt's 'bool QSvgPolygon::separateFillStroke(const QPainter *a0,
    const QSvgExtraStates &a1) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsvgpolygon.html#separateFillStroke

    Parameters
    ----------

    a0 : Optional[QPainter]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    a1 : QSvgExtraStates
      Passed on as a value: Qt reads the C++ QSvgExtraStates, which stays
      Python's own.
    """
    #  bool QSvgPolygon::separateFillStroke(const QPainter *a0, const
    #      QSvgExtraStates &a1) const
    ritual = (
        'ritual_ZNK11QSvgPolygon18separateFillStrokeEPK8QPainterRK15QSvgExt'
        'raStates')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK11QSvgPolygon18separateFillStrokeEPK8QPainterRK15Q'
          'SvgExtraStates')
    return self.uglySide.call(ritual, self._addressOf(a0), self._valueOf(a1))

  def type(self) -> QSvgNode.Type:
    """
    Calls Qt's 'Type QSvgPolygon::type() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgpolygon.html#type

    Returns
    -------

    QSvgNode.Type
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'QSvgNode.Type(number)'
      gives.
    """
    #  Type QSvgPolygon::type() const
    ritual = 'ritual_ZNK11QSvgPolygon4typeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK11QSvgPolygon4typeEv'
    return QSvgNode.Type(self.uglySide.call(ritual))

  def requiresGroupRendering(self) -> bool:
    """
    Calls Qt's 'bool QSvgPolygon::requiresGroupRendering() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsvgpolygon.html#requiresGroupRendering
    """
    #  bool QSvgPolygon::requiresGroupRendering() const
    ritual = 'ritual_ZNK11QSvgPolygon22requiresGroupRenderingEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK11QSvgPolygon22requiresGroupRenderingEv'
    return self.uglySide.call(ritual)

  def polygon(self) -> QPolygonF:
    """
    Calls Qt's 'const QPolygonF &QSvgPolygon::polygon() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgpolygon.html#polygon

    Returns
    -------

    QPolygonF
      A new cute QPolygonF around the copy Qt gave back. Python owns it.
    """
    #  const QPolygonF &QSvgPolygon::polygon() const
    address = self.uglySide.call('ritual_ZNK11QSvgPolygon7polygonEv')
    from ..QtGui import QPolygonF
    return QPolygonF._cuteOwning(address)

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

  @overload(QSvgNode, QPolygonF)
  @overload(NoneType, QPolygonF)
  def __init__(self, parent: Optional[QSvgNode], poly: QPolygonF) -> None:
    """
    Notes what was given, for Qt's 'QSvgPolygon::QSvgPolygon(QSvgNode
    *parent, const QPolygonF &poly)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qsvgpolygon.html#QSvgPolygon

    Parameters
    ----------

    parent : Optional[QSvgNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    poly : QPolygonF
      Passed on as a value: Qt reads the C++ QPolygonF, which stays Python's
      own.
    """
    #  QSvgPolygon::QSvgPolygon(QSvgNode *parent, const QPolygonF &poly)
    self._noteCreation(QSvgPolygon, lambda: Rituals.call(
        'ritual_ZN11QSvgPolygonC1EP8QSvgNodeRK9QPolygonF',
        self._addressOf(parent), self._valueOf(poly),
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
