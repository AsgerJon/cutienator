"""
QSvgCompOpStyle binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtSvg/6.12.0/QtSvg/private/qsvgstyle_p.h, Qt 6.12.0. Changes made here are
#  lost.
#
#  Qt means QSvgCompOpStyle to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..occult import Rituals
from ..QtGui import QPainter
from . import QSvgStyleProperty

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class QSvgCompOpStyle(QSvgStyleProperty):
  """
  The cute side of Qt's QSvgCompOpStyle: a plain Python object standing in
  front of one C++ QSvgCompOpStyle.

  It is built on the cute 'QSvgStyleProperty', as Qt's QSvgCompOpStyle is
  built on Qt's QSvgStyleProperty, and has everything that class has.

  C++ hands a QSvgCompOpStyle around as a copy, so every C++ QSvgCompOpStyle
  behind a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QSvgCompOpStyle that has a ritual and that Python
  can call so far, 1 name in all: 'type'. It can be made from Python, in 1
  way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSvgCompOpStyle::~QSvgCompOpStyle()': the destructor: Python
    removes its C++ QSvgCompOpStyle by it, and has no other use for it.
  - Qt's 'void QSvgCompOpStyle::apply(QPainter *p, const QSvgNode *node,
    QSvgExtraStates &states)': takes a type Python has no way to hand over
    yet.
  - Qt's 'void QSvgCompOpStyle::revert(QPainter *p, QSvgExtraStates
    &states)': takes a type Python has no way to hand over yet.
  - Qt's 'const QPainter::CompositionMode &QSvgCompOpStyle::compOp() const':
    gives a type Python has no way to take yet.

  What to expect
  --------------

  - The C++ QSvgCompOpStyle is created at the first use, not by
    'QSvgCompOpStyle(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QSvgCompOpStyle back gives a copy the ritual made for
    Python, in a new cute QSvgCompOpStyle.
  - Each name of Qt's QSvgCompOpStyle that has no cute function yet,
    'compOp', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSvgCompOpStyle'

  #  A C++ QSvgCompOpStyle Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QSvgCompOpStyle'

  #  Qt's '~QSvgCompOpStyle()'. Naming it makes this a value class: Python
  #  owns every C++ QSvgCompOpStyle behind a cute one, and removes it by this
  #  ritual.
  __delete_ritual__ = 'ritual_ZN15QSvgCompOpStyleD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def type(self) -> QSvgStyleProperty.Type:
    """
    Calls Qt's 'Type QSvgCompOpStyle::type() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgcompopstyle.html#type

    Returns
    -------

    QSvgStyleProperty.Type
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QSvgStyleProperty.Type(number)' gives.
    """
    #  Type QSvgCompOpStyle::type() const
    ritual = 'ritual_ZNK15QSvgCompOpStyle4typeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK15QSvgCompOpStyle4typeEv'
    return QSvgStyleProperty.Type(self.uglySide.call(ritual))

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

  @overload(QPainter.CompositionMode)
  def __init__(self, mode: QPainter.CompositionMode) -> None:
    """
    Notes what was given, for Qt's
    'QSvgCompOpStyle::QSvgCompOpStyle(QPainter::CompositionMode mode)', which
    is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qsvgcompopstyle.html#QSvgCompOpStyle

    Parameters
    ----------

    mode : QPainter.CompositionMode
      Passed on as its number.
    """
    #  QSvgCompOpStyle::QSvgCompOpStyle(QPainter::CompositionMode mode)
    self._noteCreation(QSvgCompOpStyle, lambda: Rituals.call(
        'ritual_ZN15QSvgCompOpStyleC1EN8QPainter15CompositionModeE',
        mode.value,
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
  def compOp(*__, **_) -> Never:
    """
    Qt's 'const QPainter::CompositionMode &QSvgCompOpStyle::compOp() const':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QSvgCompOpStyle.compOp' has no cute function yet. Qt's 'const "
        "QPainter::CompositionMode &QSvgCompOpStyle::compOp() const': gives "
        "a type Python has no way to take yet.")
