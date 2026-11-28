"""
QCss::ColorData binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qcssparser_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QCss::ColorData to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from . import QPalette

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from . import QColor
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QColor = WAIT['QColor']


class ColorData(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QCss::ColorData: a plain Python object standing in
  front of one C++ QCss::ColorData.

  C++ hands a QCss::ColorData around as a copy, so every C++ QCss::ColorData
  behind a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  No function of Qt's QCss::ColorData yet. It can be made from Python, in 3
  ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QCss::ColorData::~ColorData()': the destructor: Python removes its
    C++ QCss::ColorData by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QCss::ColorData is created at the first use, not by
    'QCss::ColorData(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QCss::ColorData back gives a copy the ritual made for
    Python, in a new cute QCss::ColorData.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QCss::ColorData'

  #  Qt's '~QCss::ColorData()'. Naming it makes this a value class: Python
  #  owns every C++ QCss::ColorData behind a cute one, and removes it by this
  #  ritual.
  __delete_ritual__ = 'ritual_ZN4QCss9ColorDataD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

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

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'QCss::ColorData::ColorData()', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qcss-colordata.html#ColorData
    """
    #  QCss::ColorData::ColorData()
    self._noteCreation(ColorData, lambda: Rituals.call(
        'ritual_ZN4QCss9ColorDataC1Ev',
    ))

  @overload(QColor)
  def __init__(self, col: QColor) -> None:
    """
    Notes what was given, for Qt's 'QCss::ColorData::ColorData(const QColor
    &col)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qcss-colordata.html#ColorData

    Parameters
    ----------

    col : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  QCss::ColorData::ColorData(const QColor &col)
    self._noteCreation(ColorData, lambda: Rituals.call(
        'ritual_ZN4QCss9ColorDataC1ERK6QColor', self._valueOf(col),
    ))

  @overload(QPalette.ColorRole)
  def __init__(self, r: QPalette.ColorRole) -> None:
    """
    Notes what was given, for Qt's
    'QCss::ColorData::ColorData(QPalette::ColorRole r)', which is called at
    the first use.

    Qt's own words: https://doc.qt.io/qt-6/qcss-colordata.html#ColorData

    Parameters
    ----------

    r : QPalette.ColorRole
      Passed on as its number.
    """
    #  QCss::ColorData::ColorData(QPalette::ColorRole r)
    self._noteCreation(ColorData, lambda: Rituals.call(
        'ritual_ZN4QCss9ColorDataC1EN8QPalette9ColorRoleE', r.value,
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
