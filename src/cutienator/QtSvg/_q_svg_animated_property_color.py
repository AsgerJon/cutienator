"""
QSvgAnimatedPropertyColor binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtSvg/6.12.0/QtSvg/private/qsvganimatedproperty_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QSvgAnimatedPropertyColor to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..QtCore import QList
from . import QSvgAbstractAnimatedProperty

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from ..QtGui import QColor
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QColor = WAIT['QColor']


class QSvgAnimatedPropertyColor(QSvgAbstractAnimatedProperty):
  """
  The cute side of Qt's QSvgAnimatedPropertyColor: a plain Python object
  standing in front of one C++ QSvgAnimatedPropertyColor.

  It is built on the cute 'QSvgAbstractAnimatedProperty', as Qt's
  QSvgAnimatedPropertyColor is built on Qt's QSvgAbstractAnimatedProperty,
  and has everything that class has.

  What exists
  -----------

  Every function of Qt's QSvgAnimatedPropertyColor that has a ritual and that
  Python can call so far, 4 names in all: 'setColors', 'appendColor',
  'colors', 'interpolate'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSvgAnimatedPropertyColor::~QSvgAnimatedPropertyColor()': the
    destructor: Python never removes a C++ QSvgAnimatedPropertyColor.

  What to expect
  --------------

  - The C++ QSvgAnimatedPropertyColor is created at the first use, not by
    'QSvgAnimatedPropertyColor(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSvgAnimatedPropertyColor.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSvgAnimatedPropertyColor'

  #  A C++ QSvgAnimatedPropertyColor Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QSvgAnimatedPropertyColor'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def colors(self) -> QList[QColor]:
    """
    Calls Qt's 'QList<QColor> QSvgAnimatedPropertyColor::colors() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsvganimatedpropertycolor.html#colors

    Returns
    -------

    QList[QColor]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QColor> QSvgAnimatedPropertyColor::colors() const
    address = self.uglySide.call(
        'ritual_ZNK25QSvgAnimatedPropertyColor6colorsEv',
    )
    from ..QtGui import QColor
    return QList[QColor]._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QList[QColor])
  def setColors(self, colors: QList[QColor]) -> None:
    """
    Calls Qt's 'void QSvgAnimatedPropertyColor::setColors(const QList<QColor>
    &colors)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsvganimatedpropertycolor.html#setColors

    Parameters
    ----------

    colors : QList[QColor]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QSvgAnimatedPropertyColor::setColors(const QList<QColor> &colors)
    self.uglySide.call(
        'ritual_ZN25QSvgAnimatedPropertyColor9setColorsERK5QListI6QColorE',
        self._valueOf(colors),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def __init__(self, name: str) -> None:
    """
    Notes what was given, for Qt's
    'QSvgAnimatedPropertyColor::QSvgAnimatedPropertyColor(const QString
    &name)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qsvganimatedpropertycolor.html

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  QSvgAnimatedPropertyColor::QSvgAnimatedPropertyColor(const QString
    #      &name)
    self._noteCreation(QSvgAnimatedPropertyColor, lambda: Rituals.call(
        'ritual_ZN25QSvgAnimatedPropertyColorC1ERK7QString', name,
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

  @overload(QColor)
  def appendColor(self, color: QColor) -> None:
    """
    Calls Qt's 'void QSvgAnimatedPropertyColor::appendColor(const QColor
    &color)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsvganimatedpropertycolor.html#appendColor

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QSvgAnimatedPropertyColor::appendColor(const QColor &color)
    self.uglySide.call(
        'ritual_ZN25QSvgAnimatedPropertyColor11appendColorERK6QColor',
        self._valueOf(color),
    )

  @overload(int, float)
  def interpolate(self, index: int, t: float) -> None:
    """
    Calls Qt's 'void QSvgAnimatedPropertyColor::interpolate(uint index, qreal
    t) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsvganimatedpropertycolor.html#interpolate

    Parameters
    ----------

    index : int
      Passed on as it is.

    t : float
      Passed on as it is.
    """
    #  void QSvgAnimatedPropertyColor::interpolate(uint index, qreal t) const
    ritual = 'ritual_ZNK25QSvgAnimatedPropertyColor11interpolateEjd'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK25QSvgAnimatedPropertyColor11interpolateEjd'
    self.uglySide.call(ritual, index, t)
