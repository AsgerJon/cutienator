"""
QSvgEllipse binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtSvg/6.12.0/QtSvg/private/qsvggraphics_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QSvgEllipse to be private: it declares the class in a header it
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

  from ..QtCore import QRectF
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


class QSvgEllipse(QSvgNode):
  """
  The cute side of Qt's QSvgEllipse: a plain Python object standing in front
  of one C++ QSvgEllipse.

  It is built on the cute 'QSvgNode', as Qt's QSvgEllipse is built on Qt's
  QSvgNode, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QSvgEllipse that has a ritual and that Python can
  call so far, 3 names in all: 'separateFillStroke', 'type', 'rect'. It can
  be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSvgEllipse::~QSvgEllipse()': the destructor: Python never removes
    a C++ QSvgEllipse.
  - Qt's 'void QSvgEllipse::drawCommand(QPainter *p, QSvgExtraStates
    &states)': takes a type Python has no way to hand over yet.
  - Qt's 'QRectF QSvgEllipse::internalFastBounds(QPainter *p, QSvgExtraStates
    &states) const': takes a type Python has no way to hand over yet.
  - Qt's 'QRectF QSvgEllipse::internalBounds(QPainter *p, QSvgExtraStates
    &states) const': takes a type Python has no way to hand over yet.
  - Qt's 'QRectF QSvgEllipse::decoratedInternalBounds(QPainter *p,
    QSvgExtraStates &states) const': takes a type Python has no way to hand
    over yet.

  What to expect
  --------------

  - The C++ QSvgEllipse is created at the first use, not by
    'QSvgEllipse(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSvgEllipse.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSvgEllipse'

  #  A C++ QSvgEllipse Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QSvgEllipse'

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
    Calls Qt's 'bool QSvgEllipse::separateFillStroke(const QPainter *a0,
    const QSvgExtraStates &a1) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsvgellipse.html#separateFillStroke

    Parameters
    ----------

    a0 : Optional[QPainter]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    a1 : QSvgExtraStates
      Passed on as a value: Qt reads the C++ QSvgExtraStates, which stays
      Python's own.
    """
    #  bool QSvgEllipse::separateFillStroke(const QPainter *a0, const
    #      QSvgExtraStates &a1) const
    ritual = (
        'ritual_ZNK11QSvgEllipse18separateFillStrokeEPK8QPainterRK15QSvgExt'
        'raStates')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK11QSvgEllipse18separateFillStrokeEPK8QPainterRK15Q'
          'SvgExtraStates')
    return self.uglySide.call(ritual, self._addressOf(a0), self._valueOf(a1))

  def type(self) -> QSvgNode.Type:
    """
    Calls Qt's 'Type QSvgEllipse::type() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgellipse.html#type

    Returns
    -------

    QSvgNode.Type
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'QSvgNode.Type(number)'
      gives.
    """
    #  Type QSvgEllipse::type() const
    ritual = 'ritual_ZNK11QSvgEllipse4typeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK11QSvgEllipse4typeEv'
    return QSvgNode.Type(self.uglySide.call(ritual))

  def rect(self) -> QRectF:
    """
    Calls Qt's 'QRectF QSvgEllipse::rect() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgellipse.html#rect

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QSvgEllipse::rect() const
    address = self.uglySide.call('ritual_ZNK11QSvgEllipse4rectEv')
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

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
  def __init__(self, parent: Optional[QSvgNode], rect: QRectF) -> None:
    """
    Notes what was given, for Qt's 'QSvgEllipse::QSvgEllipse(QSvgNode
    *parent, const QRectF &rect)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qsvgellipse.html#QSvgEllipse

    Parameters
    ----------

    parent : Optional[QSvgNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    rect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  QSvgEllipse::QSvgEllipse(QSvgNode *parent, const QRectF &rect)
    self._noteCreation(QSvgEllipse, lambda: Rituals.call(
        'ritual_ZN11QSvgEllipseC1EP8QSvgNodeRK6QRectF',
        self._addressOf(parent), self._valueOf(rect),
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
