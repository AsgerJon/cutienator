"""
QQC2::QStyleOption binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickNativeStyle/6.12.0/QtQuickNativeStyle/private/qqc2qstyleoption_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQC2::QStyleOption to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute
from ..occult import Rituals


class QStyleOption(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQC2::QStyleOption: a plain Python object standing in
  front of one C++ QQC2::QStyleOption.

  C++ hands a QQC2::QStyleOption around as a copy, so every C++
  QQC2::QStyleOption behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  No function of Qt's QQC2::QStyleOption yet. It can be made from Python, in
  2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QQC2::QStyleOption::~QStyleOption()': the destructor: Python
    removes its C++ QQC2::QStyleOption by it, and has no other use for it.
  - Qt's 'QStyleOption &QQC2::QStyleOption::operator=(const QStyleOption
    &other)': assignment: Python binds a name and has no operator for it.

  What to expect
  --------------

  - The C++ QQC2::QStyleOption is created at the first use, not by
    'QQC2::QStyleOption(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QQC2::QStyleOption back gives a copy the ritual made
    for Python, in a new cute QQC2::QStyleOption.
  """

  #  The enums Qt writes inside QQC2::QStyleOption, each a class in here as
  #  in C++, and the names Qt has for the combinations of its flags enums.

  class OptionType(CuteNum):
    """
    The enum 'QQC2::QStyleOption::OptionType' of Qt, with the 27 names Qt
    gives in it.
    """

    SO_Default = Kee[int](0)
    SO_FocusRect = Kee[int](1)
    SO_Button = Kee[int](2)
    SO_Tab = Kee[int](3)
    SO_MenuItem = Kee[int](4)
    SO_Frame = Kee[int](5)
    SO_ProgressBar = Kee[int](6)
    SO_ToolBox = Kee[int](7)
    SO_Header = Kee[int](8)
    SO_DockWidget = Kee[int](9)
    SO_ViewItem = Kee[int](10)
    SO_TabWidgetFrame = Kee[int](11)
    SO_TabBarBase = Kee[int](12)
    SO_RubberBand = Kee[int](13)
    SO_ToolBar = Kee[int](14)
    SO_GraphicsItem = Kee[int](15)
    SO_Complex = Kee[int](983040)
    SO_Slider = Kee[int](983041)
    SO_SpinBox = Kee[int](983042)
    SO_ToolButton = Kee[int](983043)
    SO_ComboBox = Kee[int](983044)
    SO_TitleBar = Kee[int](983045)
    SO_GroupBox = Kee[int](983046)
    SO_SizeGrip = Kee[int](983047)
    SO_SearchField = Kee[int](983048)
    SO_CustomBase = Kee[int](3840)
    SO_ComplexCustomBase = Kee[int](251658240)

  class StyleOptionType(CuteNum):
    """
    The enum 'QQC2::QStyleOption::StyleOptionType' of Qt, with the 1 names Qt
    gives in it.
    """

    Type = Kee[int](0)

  class StyleOptionVersion(CuteNum):
    """
    The enum 'QQC2::QStyleOption::StyleOptionVersion' of Qt, with the 1 names
    Qt gives in it.
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
  __qt_class__ = 'QQC2::QStyleOption'

  #  Qt's '~QQC2::QStyleOption()'. Naming it makes this a value class: Python
  #  owns every C++ QQC2::QStyleOption behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN4QQC212QStyleOptionD1Ev'

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
  @overload(int)
  @overload(int, int)
  def __init__(self, version: int = 1, type: int = 0) -> None:
    """
    Notes what was given, for Qt's 'QQC2::QStyleOption::QStyleOption(int
    version, int type)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqc2-qstyleoption.html#QStyleOption

    Parameters
    ----------

    version : int
      Passed on as it is. May be left out, as in Qt: it is then 1.

    type : int
      Passed on as it is. May be left out, as in Qt: it is then 0.
    """
    #  QQC2::QStyleOption::QStyleOption(int version, int type)
    self._noteCreation(QStyleOption, lambda: Rituals.call(
        'ritual_ZN4QQC212QStyleOptionC1Eii', version, type,
    ))

  @overload(THIS)
  def __init__(self, other: QStyleOption) -> None:
    """
    Notes what was given, for Qt's 'QQC2::QStyleOption::QStyleOption(const
    QStyleOption &other)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqc2-qstyleoption.html#QStyleOption

    Parameters
    ----------

    other : QStyleOption
      Passed on as a value: Qt reads the C++ QQC2::QStyleOption, which stays
      Python's own.
    """
    #  QQC2::QStyleOption::QStyleOption(const QStyleOption &other)
    self._noteCreation(QStyleOption, lambda: Rituals.call(
        'ritual_ZN4QQC212QStyleOptionC1ERKS0_', self._valueOf(other),
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
