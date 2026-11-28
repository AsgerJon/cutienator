"""
QSvgMask binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtSvg/6.12.0/QtSvg/private/qsvgstructure_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QSvgMask to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from . import QtSvg, QSvgNode, QSvgStructureNode

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QSvgRectF
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QSvgRectF = WAIT['QSvgRectF']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSvgMask(QSvgStructureNode):
  """
  The cute side of Qt's QSvgMask: a plain Python object standing in front of
  one C++ QSvgMask.

  It is built on the cute 'QSvgStructureNode', as Qt's QSvgMask is built on
  Qt's QSvgStructureNode, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QSvgMask that has a ritual and that Python can call
  so far, 3 names in all: 'type', 'rect', 'contentUnits'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSvgMask::~QSvgMask()': the destructor: Python never removes a C++
    QSvgMask.
  - Qt's 'void QSvgMask::drawCommand(QPainter *a0, QSvgExtraStates &a1)':
    takes a type Python has no way to hand over yet.
  - Qt's 'bool QSvgMask::shouldDrawNode(QPainter *a0, QSvgExtraStates &a1)
    const': takes a type Python has no way to hand over yet.
  - Qt's 'QImage QSvgMask::createMask(QPainter *p, QSvgExtraStates &states,
    QSvgNode *targetNode, QRectF *globalRect) const': takes a type Python has
    no way to hand over yet.
  - Qt's 'QImage QSvgMask::createMask(QPainter *p, QSvgExtraStates &states,
    const QRectF &localRect, QRectF *globalRect) const': takes a type Python
    has no way to hand over yet.

  What to expect
  --------------

  - The C++ QSvgMask is created at the first use, not by 'QSvgMask(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSvgMask.
  - Each name of Qt's QSvgMask that has no cute function yet, 'createMask',
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
  __qt_class__ = 'QSvgMask'

  #  A C++ QSvgMask Python makes is of a C++ class of ours, in which Python
  #  can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QSvgMask'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def type(self) -> QSvgNode.Type:
    """
    Calls Qt's 'Type QSvgMask::type() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgmask.html#type

    Returns
    -------

    QSvgNode.Type
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'QSvgNode.Type(number)'
      gives.
    """
    #  Type QSvgMask::type() const
    ritual = 'ritual_ZNK8QSvgMask4typeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK8QSvgMask4typeEv'
    return QSvgNode.Type(self.uglySide.call(ritual))

  def rect(self) -> QSvgRectF:
    """
    Calls Qt's 'QSvgRectF QSvgMask::rect() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgmask.html#rect

    Returns
    -------

    QSvgRectF
      A new cute QSvgRectF around the copy Qt gave back. Python owns it.
    """
    #  QSvgRectF QSvgMask::rect() const
    address = self.uglySide.call('ritual_ZNK8QSvgMask4rectEv')
    from . import QSvgRectF
    return QSvgRectF._cuteOwning(address)

  def contentUnits(self) -> QtSvg.UnitTypes:
    """
    Calls Qt's 'QtSvg::UnitTypes QSvgMask::contentUnits() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgmask.html#contentUnits

    Returns
    -------

    QtSvg.UnitTypes
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'QtSvg.UnitTypes(number)'
      gives.
    """
    #  QtSvg::UnitTypes QSvgMask::contentUnits() const
    return QtSvg.UnitTypes(self.uglySide.call(
        'ritual_ZNK8QSvgMask12contentUnitsEv',
    ))

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

  @overload(QSvgNode, QSvgRectF, QtSvg.UnitTypes)
  @overload(NoneType, QSvgRectF, QtSvg.UnitTypes)
  def __init__(
      self,
      parent: Optional[QSvgNode],
      bounds: QSvgRectF,
      contentsUnits: QtSvg.UnitTypes,
  ) -> None:
    """
    Notes what was given, for Qt's 'QSvgMask::QSvgMask(QSvgNode *parent,
    QSvgRectF bounds, QtSvg::UnitTypes contentsUnits)', which is called at
    the first use.

    Qt's own words: https://doc.qt.io/qt-6/qsvgmask.html#QSvgMask

    Parameters
    ----------

    parent : Optional[QSvgNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    bounds : QSvgRectF
      Passed on as a value: Qt reads the C++ QSvgRectF, which stays Python's
      own.

    contentsUnits : QtSvg.UnitTypes
      Passed on as its number.
    """
    #  QSvgMask::QSvgMask(QSvgNode *parent, QSvgRectF bounds,
    #      QtSvg::UnitTypes contentsUnits)
    self._noteCreation(QSvgMask, lambda: Rituals.call(
        'ritual_ZN8QSvgMaskC1EP8QSvgNode9QSvgRectFN5QtSvg9UnitTypesE',
        self._addressOf(parent), self._valueOf(bounds), contentsUnits.value,
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

  @staticmethod
  def createMask(*__, **_) -> Never:
    """
    - Qt's 'QImage QSvgMask::createMask(QPainter *p, QSvgExtraStates &states,
      QSvgNode *targetNode, QRectF *globalRect) const': takes a type Python
      has no way to hand over yet.
    - Qt's 'QImage QSvgMask::createMask(QPainter *p, QSvgExtraStates &states,
      const QRectF &localRect, QRectF *globalRect) const': takes a type
      Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QSvgMask.createMask' has no cute function yet. Qt's 'QImage "
        "QSvgMask::createMask(QPainter *p, QSvgExtraStates &states, "
        "QSvgNode *targetNode, QRectF *globalRect) const': takes a type "
        "Python has no way to hand over yet. Qt's 'QImage "
        "QSvgMask::createMask(QPainter *p, QSvgExtraStates &states, const "
        "QRectF &localRect, QRectF *globalRect) const': takes a type Python "
        "has no way to hand over yet.")
