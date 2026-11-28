"""
QSvgViewportFillStyle binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtSvg/6.12.0/QtSvg/private/qsvgstyle_p.h, Qt 6.12.0. Changes made here are
#  lost.
#
#  Qt means QSvgViewportFillStyle to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from . import QSvgStyleProperty

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from ..QtGui import QBrush
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QBrush = WAIT['QBrush']


class QSvgViewportFillStyle(QSvgStyleProperty):
  """
  The cute side of Qt's QSvgViewportFillStyle: a plain Python object standing
  in front of one C++ QSvgViewportFillStyle.

  It is built on the cute 'QSvgStyleProperty', as Qt's QSvgViewportFillStyle
  is built on Qt's QSvgStyleProperty, and has everything that class has.

  C++ hands a QSvgViewportFillStyle around as a copy, so every C++
  QSvgViewportFillStyle behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QSvgViewportFillStyle that has a ritual and that
  Python can call so far, 2 names in all: 'type', 'qbrush'. It can be made
  from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSvgViewportFillStyle::~QSvgViewportFillStyle()': the destructor:
    Python removes its C++ QSvgViewportFillStyle by it, and has no other use
    for it.
  - Qt's 'void QSvgViewportFillStyle::apply(QPainter *p, const QSvgNode
    *node, QSvgExtraStates &states)': takes a type Python has no way to hand
    over yet.
  - Qt's 'void QSvgViewportFillStyle::revert(QPainter *p, QSvgExtraStates
    &states)': takes a type Python has no way to hand over yet.

  What to expect
  --------------

  - The C++ QSvgViewportFillStyle is created at the first use, not by
    'QSvgViewportFillStyle(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QSvgViewportFillStyle back gives a copy the ritual
    made for Python, in a new cute QSvgViewportFillStyle.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSvgViewportFillStyle'

  #  A C++ QSvgViewportFillStyle Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QSvgViewportFillStyle'

  #  Qt's '~QSvgViewportFillStyle()'. Naming it makes this a value class:
  #  Python owns every C++ QSvgViewportFillStyle behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN21QSvgViewportFillStyleD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def type(self) -> QSvgStyleProperty.Type:
    """
    Calls Qt's 'Type QSvgViewportFillStyle::type() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgviewportfillstyle.html#type

    Returns
    -------

    QSvgStyleProperty.Type
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QSvgStyleProperty.Type(number)' gives.
    """
    #  Type QSvgViewportFillStyle::type() const
    ritual = 'ritual_ZNK21QSvgViewportFillStyle4typeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK21QSvgViewportFillStyle4typeEv'
    return QSvgStyleProperty.Type(self.uglySide.call(ritual))

  def qbrush(self) -> QBrush:
    """
    Calls Qt's 'const QBrush &QSvgViewportFillStyle::qbrush() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgviewportfillstyle.html#qbrush

    Returns
    -------

    QBrush
      A new cute QBrush around the copy Qt gave back. Python owns it.
    """
    #  const QBrush &QSvgViewportFillStyle::qbrush() const
    address = self.uglySide.call(
        'ritual_ZNK21QSvgViewportFillStyle6qbrushEv',
    )
    from ..QtGui import QBrush
    return QBrush._cuteOwning(address)

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

  @overload(QBrush)
  def __init__(self, brush: QBrush) -> None:
    """
    Notes what was given, for Qt's
    'QSvgViewportFillStyle::QSvgViewportFillStyle(const QBrush &brush)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qsvgviewportfillstyle.html#QSvgViewportFillStyle

    Parameters
    ----------

    brush : QBrush
      Passed on as a value: Qt reads the C++ QBrush, which stays Python's
      own.
    """
    #  QSvgViewportFillStyle::QSvgViewportFillStyle(const QBrush &brush)
    self._noteCreation(QSvgViewportFillStyle, lambda: Rituals.call(
        'ritual_ZN21QSvgViewportFillStyleC1ERK6QBrush', self._valueOf(brush),
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
