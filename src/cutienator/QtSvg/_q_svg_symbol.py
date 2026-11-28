"""
QSvgSymbol binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtSvg/6.12.0/QtSvg/private/qsvgstructure_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QSvgSymbol to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from . import QSvgNode, QSvgSymbolLike

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QPointF, QRectF
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPointF = WAIT['QPointF']
  QRectF = WAIT['QRectF']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSvgSymbol(QSvgSymbolLike):
  """
  The cute side of Qt's QSvgSymbol: a plain Python object standing in front
  of one C++ QSvgSymbol.

  It is built on the cute 'QSvgSymbolLike', as Qt's QSvgSymbol is built on
  Qt's QSvgSymbolLike, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QSvgSymbol that has a ritual and that Python can
  call so far, 1 name in all: 'type'. It can be made from Python, in 1 way;
  see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSvgSymbol::~QSvgSymbol()': the destructor: Python never removes a
    C++ QSvgSymbol.
  - Qt's 'void QSvgSymbol::drawCommand(QPainter *p, QSvgExtraStates
    &states)': takes a type Python has no way to hand over yet.

  What to expect
  --------------

  - The C++ QSvgSymbol is created at the first use, not by 'QSvgSymbol(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSvgSymbol.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSvgSymbol'

  #  A C++ QSvgSymbol Python makes is of a C++ class of ours, in which Python
  #  can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QSvgSymbol'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def type(self) -> QSvgNode.Type:
    """
    Calls Qt's 'Type QSvgSymbol::type() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgsymbol.html#type

    Returns
    -------

    QSvgNode.Type
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'QSvgNode.Type(number)'
      gives.
    """
    #  Type QSvgSymbol::type() const
    ritual = 'ritual_ZNK10QSvgSymbol4typeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK10QSvgSymbol4typeEv'
    return QSvgNode.Type(self.uglySide.call(ritual))

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

  @overload(
      QSvgNode, QRectF, QRectF, QPointF, QSvgSymbolLike.PreserveAspectRatios,
      QSvgSymbolLike.Overflow,
  )
  @overload(
      NoneType, QRectF, QRectF, QPointF, QSvgSymbolLike.PreserveAspectRatios,
      QSvgSymbolLike.Overflow,
  )
  def __init__(
      self,
      parent: Optional[QSvgNode],
      bounds: QRectF,
      viewBox: QRectF,
      refP: QPointF,
      pAspectRatios: QSvgSymbolLike.PreserveAspectRatios,
      overflow: QSvgSymbolLike.Overflow,
  ) -> None:
    """
    Notes what was given, for Qt's 'QSvgSymbol::QSvgSymbol(QSvgNode *parent,
    QRectF bounds, QRectF viewBox, QPointF refP,
    QSvgSymbolLike::PreserveAspectRatios pAspectRatios,
    QSvgSymbolLike::Overflow overflow)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qsvgsymbol.html#QSvgSymbol

    Parameters
    ----------

    parent : Optional[QSvgNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    bounds : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    viewBox : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    refP : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    pAspectRatios : QSvgSymbolLike.PreserveAspectRatios
      Passed on as its number.

    overflow : QSvgSymbolLike.Overflow
      Passed on as its number.
    """
    #  QSvgSymbol::QSvgSymbol(QSvgNode *parent, QRectF bounds, QRectF
    #      viewBox, QPointF refP, QSvgSymbolLike::PreserveAspectRatios
    #      pAspectRatios, QSvgSymbolLike::Overflow overflow)
    self._noteCreation(QSvgSymbol, lambda: Rituals.call(
        'ritual_ZN10QSvgSymbolC1EP8QSvgNode6QRectFS2_7QPointF6QFlagsIN14QSv'
        'gSymbolLike19PreserveAspectRatioEENS5_8OverflowE',
        self._addressOf(parent), self._valueOf(bounds),
        self._valueOf(viewBox), self._valueOf(refP, 'QPointF'),
        pAspectRatios.value, overflow.value,
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
