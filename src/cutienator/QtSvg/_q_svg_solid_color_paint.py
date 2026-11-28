"""
QSvgSolidColorPaint binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtSvg/6.12.0/QtSvg/private/qsvgpaintserver_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QSvgSolidColorPaint to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from . import QSvgPaintServer

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from ..QtGui import QColor
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QColor = WAIT['QColor']


class QSvgSolidColorPaint(QSvgPaintServer):
  """
  The cute side of Qt's QSvgSolidColorPaint: a plain Python object standing
  in front of one C++ QSvgSolidColorPaint.

  It is built on the cute 'QSvgPaintServer', as Qt's QSvgSolidColorPaint is
  built on Qt's QSvgPaintServer, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QSvgSolidColorPaint that has a ritual and that
  Python can call so far, 2 names in all: 'type', 'qcolor'. It can be made
  from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSvgSolidColorPaint::~QSvgSolidColorPaint()': the destructor:
    Python never removes a C++ QSvgSolidColorPaint.
  - Qt's 'QBrush QSvgSolidColorPaint::brush(QPainter *a0, const QSvgNode *a1,
    QSvgExtraStates &a2)': takes a type Python has no way to hand over yet.

  What to expect
  --------------

  - The C++ QSvgSolidColorPaint is created at the first use, not by
    'QSvgSolidColorPaint(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSvgSolidColorPaint.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSvgSolidColorPaint'

  #  A C++ QSvgSolidColorPaint Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QSvgSolidColorPaint'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def type(self) -> QSvgPaintServer.Type:
    """
    Calls Qt's 'Type QSvgSolidColorPaint::type() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgsolidcolorpaint.html#type

    Returns
    -------

    QSvgPaintServer.Type
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QSvgPaintServer.Type(number)' gives.
    """
    #  Type QSvgSolidColorPaint::type() const
    ritual = 'ritual_ZNK19QSvgSolidColorPaint4typeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK19QSvgSolidColorPaint4typeEv'
    return QSvgPaintServer.Type(self.uglySide.call(ritual))

  def qcolor(self) -> QColor:
    """
    Calls Qt's 'const QColor &QSvgSolidColorPaint::qcolor() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgsolidcolorpaint.html#qcolor

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  const QColor &QSvgSolidColorPaint::qcolor() const
    address = self.uglySide.call('ritual_ZNK19QSvgSolidColorPaint6qcolorEv')
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

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

  @overload(QColor)
  def __init__(self, color: QColor) -> None:
    """
    Notes what was given, for Qt's
    'QSvgSolidColorPaint::QSvgSolidColorPaint(const QColor &color)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qsvgsolidcolorpaint.html#QSvgSolidColorPaint

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  QSvgSolidColorPaint::QSvgSolidColorPaint(const QColor &color)
    self._noteCreation(QSvgSolidColorPaint, lambda: Rituals.call(
        'ritual_ZN19QSvgSolidColorPaintC1ERK6QColor', self._valueOf(color),
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
