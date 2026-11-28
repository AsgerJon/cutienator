"""
QSvgLine binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtSvg/6.12.0/QtSvg/private/qsvggraphics_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QSvgLine to be private: it declares the class in a header it
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

  from ..QtCore import QLineF
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QLineF = WAIT['QLineF']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSvgLine(QSvgNode):
  """
  The cute side of Qt's QSvgLine: a plain Python object standing in front of
  one C++ QSvgLine.

  It is built on the cute 'QSvgNode', as Qt's QSvgLine is built on Qt's
  QSvgNode, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QSvgLine that has a ritual and that Python can call
  so far, 3 names in all: 'type', 'requiresGroupRendering', 'line'. It can be
  made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSvgLine::~QSvgLine()': the destructor: Python never removes a C++
    QSvgLine.
  - Qt's 'void QSvgLine::drawCommand(QPainter *p, QSvgExtraStates &states)':
    takes a type Python has no way to hand over yet.
  - Qt's 'QRectF QSvgLine::internalFastBounds(QPainter *p, QSvgExtraStates
    &states) const': takes a type Python has no way to hand over yet.
  - Qt's 'QRectF QSvgLine::internalBounds(QPainter *p, QSvgExtraStates
    &states) const': takes a type Python has no way to hand over yet.
  - Qt's 'QRectF QSvgLine::decoratedInternalBounds(QPainter *p,
    QSvgExtraStates &states) const': takes a type Python has no way to hand
    over yet.
  - Qt's 'QRectF QSvgLine::internalBounds(QPainter *p, QSvgExtraStates
    &states, BoundsMode mode) const': takes a type Python has no way to hand
    over yet.

  What to expect
  --------------

  - The C++ QSvgLine is created at the first use, not by 'QSvgLine(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSvgLine.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSvgLine'

  #  A C++ QSvgLine Python makes is of a C++ class of ours, in which Python
  #  can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QSvgLine'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def type(self) -> QSvgNode.Type:
    """
    Calls Qt's 'Type QSvgLine::type() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgline.html#type

    Returns
    -------

    QSvgNode.Type
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'QSvgNode.Type(number)'
      gives.
    """
    #  Type QSvgLine::type() const
    ritual = 'ritual_ZNK8QSvgLine4typeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK8QSvgLine4typeEv'
    return QSvgNode.Type(self.uglySide.call(ritual))

  def requiresGroupRendering(self) -> bool:
    """
    Calls Qt's 'bool QSvgLine::requiresGroupRendering() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsvgline.html#requiresGroupRendering
    """
    #  bool QSvgLine::requiresGroupRendering() const
    ritual = 'ritual_ZNK8QSvgLine22requiresGroupRenderingEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK8QSvgLine22requiresGroupRenderingEv'
    return self.uglySide.call(ritual)

  def line(self) -> QLineF:
    """
    Calls Qt's 'QLineF QSvgLine::line() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgline.html#line

    Returns
    -------

    QLineF
      A new cute QLineF around the copy Qt gave back. Python owns it.
    """
    #  QLineF QSvgLine::line() const
    address = self.uglySide.call('ritual_ZNK8QSvgLine4lineEv')
    from ..QtCore import QLineF
    return QLineF._cuteOwning(address)

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

  @overload(QSvgNode, QLineF)
  @overload(NoneType, QLineF)
  def __init__(self, parent: Optional[QSvgNode], line: QLineF) -> None:
    """
    Notes what was given, for Qt's 'QSvgLine::QSvgLine(QSvgNode *parent,
    const QLineF &line)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qsvgline.html#QSvgLine

    Parameters
    ----------

    parent : Optional[QSvgNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    line : QLineF
      Passed on as a value: Qt reads the C++ QLineF, which stays Python's
      own.
    """
    #  QSvgLine::QSvgLine(QSvgNode *parent, const QLineF &line)
    self._noteCreation(QSvgLine, lambda: Rituals.call(
        'ritual_ZN8QSvgLineC1EP8QSvgNodeRK6QLineF',
        self._addressOf(parent), self._valueOf(line),
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
