"""
QStyleOptionTab binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/qstyleoption.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..occult import Rituals
from . import QStyleOption, QStyleOptionTabCornerWidget
from . import QStyleOptionTabSelectedPosition, QStyleOptionTabStyleOptionType
from . import QStyleOptionTabStyleOptionVersion, QStyleOptionTabTabFeature
from . import QStyleOptionTabTabPosition


class QStyleOptionTab(QStyleOption):
  """
  The cute side of Qt's QStyleOptionTab: a plain Python object standing in
  front of one C++ QStyleOptionTab.

  It is built on the cute 'QStyleOption', as Qt's QStyleOptionTab is built on
  Qt's QStyleOption, and has everything that class has.

  C++ hands a QStyleOptionTab around as a copy, so every C++ QStyleOptionTab
  behind a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  No function of Qt's QStyleOptionTab yet. It can be made from Python, in 2
  ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QStyleOptionTab::~QStyleOptionTab()': the destructor: Python
    removes its C++ QStyleOptionTab by it, and has no other use for it.

  What has no ritual
  ------------------

  2 of the 5 functions Qt declares: 1 takes or gives a type that cannot be
  passed yet; 1 protected.

  What to expect
  --------------

  - The C++ QStyleOptionTab is created at the first use, not by
    'QStyleOptionTab(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QStyleOptionTab back gives a copy the ritual made for
    Python, in a new cute QStyleOptionTab.
  """

  #  The enums Qt writes inside QStyleOptionTab, and the names Qt has for the
  #  combinations of its flags enums.
  CornerWidget = QStyleOptionTabCornerWidget
  CornerWidgets = QStyleOptionTabCornerWidget
  SelectedPosition = QStyleOptionTabSelectedPosition
  StyleOptionType = QStyleOptionTabStyleOptionType
  StyleOptionVersion = QStyleOptionTabStyleOptionVersion
  TabFeature = QStyleOptionTabTabFeature
  TabFeatures = QStyleOptionTabTabFeature
  TabPosition = QStyleOptionTabTabPosition

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QStyleOptionTab'

  #  Qt's '~QStyleOptionTab()'. Naming it makes this a value class: Python
  #  owns every C++ QStyleOptionTab behind a cute one, and removes it by this
  #  ritual.
  __delete_ritual__ = 'ritual_ZN15QStyleOptionTabD1Ev'

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
    Notes what was given, for Qt's 'QStyleOptionTab::QStyleOptionTab()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qstyleoptiontab.html#QStyleOptionTab
    """
    #  QStyleOptionTab::QStyleOptionTab()
    self._noteCreation(QStyleOptionTab, lambda: Rituals.call(
        'ritual_ZN15QStyleOptionTabC1Ev',
    ))

  @overload(THIS)
  def __init__(self, other: QStyleOptionTab) -> None:
    """
    Notes what was given, for Qt's 'QStyleOptionTab::QStyleOptionTab(const
    QStyleOptionTab &other)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qstyleoptiontab.html#QStyleOptionTab

    Parameters
    ----------

    other : QStyleOptionTab
      Passed on as a value: Qt reads the C++ QStyleOptionTab, which stays
      Python's own.
    """
    #  QStyleOptionTab::QStyleOptionTab(const QStyleOptionTab &other)
    self._noteCreation(QStyleOptionTab, lambda: Rituals.call(
        'ritual_ZN15QStyleOptionTabC1ERKS_', self._valueOf(other),
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
