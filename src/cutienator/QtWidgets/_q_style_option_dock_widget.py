"""
QStyleOptionDockWidget binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/qstyleoption.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteNum
from ..occult import Rituals
from . import QStyleOption


class QStyleOptionDockWidget(QStyleOption):
  """
  The cute side of Qt's QStyleOptionDockWidget: a plain Python object
  standing in front of one C++ QStyleOptionDockWidget.

  It is built on the cute 'QStyleOption', as Qt's QStyleOptionDockWidget is
  built on Qt's QStyleOption, and has everything that class has.

  C++ hands a QStyleOptionDockWidget around as a copy, so every C++
  QStyleOptionDockWidget behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  No function of Qt's QStyleOptionDockWidget yet. It can be made from Python,
  in 3 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QStyleOptionDockWidget &QStyleOptionDockWidget::operator=(const
    QStyleOptionDockWidget &a0)': assignment: Python binds a name and has no
    operator for it.
  - Qt's 'QStyleOptionDockWidget::~QStyleOptionDockWidget()': the destructor:
    Python removes its C++ QStyleOptionDockWidget by it, and has no other use
    for it.

  What to expect
  --------------

  - The C++ QStyleOptionDockWidget is created at the first use, not by
    'QStyleOptionDockWidget(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QStyleOptionDockWidget back gives a copy the ritual
    made for Python, in a new cute QStyleOptionDockWidget.
  """

  #  The enums Qt writes inside QStyleOptionDockWidget, each a class in here
  #  as in C++, and the names Qt has for the combinations of its flags enums.

  class StyleOptionType(CuteNum):
    """
    The enum 'QStyleOptionDockWidget::StyleOptionType' of Qt, with the 1
    names Qt gives in it.
    """

    Type = Kee[int](9)

  class StyleOptionVersion(CuteNum):
    """
    The enum 'QStyleOptionDockWidget::StyleOptionVersion' of Qt, with the 1
    names Qt gives in it.
    """

    Version = Kee[int](1)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QStyleOptionDockWidget'

  #  Qt's '~QStyleOptionDockWidget()'. Naming it makes this a value class:
  #  Python owns every C++ QStyleOptionDockWidget behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN22QStyleOptionDockWidgetD1Ev'

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
    Notes what was given, for Qt's
    'QStyleOptionDockWidget::QStyleOptionDockWidget()', which is called at
    the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qstyleoptiondockwidget.html#QStyleOptionDockWidget
    """
    #  QStyleOptionDockWidget::QStyleOptionDockWidget()
    self._noteCreation(QStyleOptionDockWidget, lambda: Rituals.call(
        'ritual_ZN22QStyleOptionDockWidgetC1Ev',
    ))

  @overload(THIS)
  def __init__(self, other: QStyleOptionDockWidget) -> None:
    """
    Notes what was given, for Qt's
    'QStyleOptionDockWidget::QStyleOptionDockWidget(const
    QStyleOptionDockWidget &other)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qstyleoptiondockwidget.html#QStyleOptionDockWidget

    Parameters
    ----------

    other : QStyleOptionDockWidget
      Passed on as a value: Qt reads the C++ QStyleOptionDockWidget, which
      stays Python's own.
    """
    #  QStyleOptionDockWidget::QStyleOptionDockWidget(const
    #      QStyleOptionDockWidget &other)
    self._noteCreation(QStyleOptionDockWidget, lambda: Rituals.call(
        'ritual_ZN22QStyleOptionDockWidgetC1ERKS_', self._valueOf(other),
    ))

  @overload(int)
  def __init__(self, version: int) -> None:
    """
    Notes what was given, for Qt's
    'QStyleOptionDockWidget::QStyleOptionDockWidget(int version)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qstyleoptiondockwidget.html#QStyleOptionDockWidget

    Parameters
    ----------

    version : int
      Passed on as it is.
    """
    #  QStyleOptionDockWidget::QStyleOptionDockWidget(int version)
    self._noteCreation(QStyleOptionDockWidget, lambda: Rituals.call(
        'ritual_ZN22QStyleOptionDockWidgetC1Ei', version,
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
