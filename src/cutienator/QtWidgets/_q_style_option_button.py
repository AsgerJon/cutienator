"""
QStyleOptionButton binding of the Qt C++
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

from ..cute import CuteFlags, CuteNum
from ..occult import Rituals
from . import QStyleOption


class QStyleOptionButton(QStyleOption):
  """
  The cute side of Qt's QStyleOptionButton: a plain Python object standing in
  front of one C++ QStyleOptionButton.

  It is built on the cute 'QStyleOption', as Qt's QStyleOptionButton is built
  on Qt's QStyleOption, and has everything that class has.

  C++ hands a QStyleOptionButton around as a copy, so every C++
  QStyleOptionButton behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  No function of Qt's QStyleOptionButton yet. It can be made from Python, in
  3 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QStyleOptionButton &QStyleOptionButton::operator=(const
    QStyleOptionButton &a0)': assignment: Python binds a name and has no
    operator for it.
  - Qt's 'QStyleOptionButton::~QStyleOptionButton()': the destructor: Python
    removes its C++ QStyleOptionButton by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QStyleOptionButton is created at the first use, not by
    'QStyleOptionButton(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QStyleOptionButton back gives a copy the ritual made
    for Python, in a new cute QStyleOptionButton.
  """

  #  The enums Qt writes inside QStyleOptionButton, each a class in here as
  #  in C++, and the names Qt has for the combinations of its flags enums.

  class ButtonFeature(CuteFlags):
    """
    The flags enum 'QStyleOptionButton::ButtonFeature' of Qt, with the 6
    names Qt gives in it. Qt names the type of its combinations
    'QStyleOptionButton::ButtonFeatures'.
    """

    NULL = 0x0
    Flat = 0x1
    HasMenu = 0x2
    DefaultButton = 0x4
    AutoDefaultButton = 0x8
    CommandLinkButton = 0x10

  ButtonFeatures = ButtonFeature

  class StyleOptionType(CuteNum):
    """
    The enum 'QStyleOptionButton::StyleOptionType' of Qt, with the 1 names Qt
    gives in it.
    """

    Type = Kee[int](2)

  class StyleOptionVersion(CuteNum):
    """
    The enum 'QStyleOptionButton::StyleOptionVersion' of Qt, with the 1 names
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
  __qt_class__ = 'QStyleOptionButton'

  #  Qt's '~QStyleOptionButton()'. Naming it makes this a value class: Python
  #  owns every C++ QStyleOptionButton behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN18QStyleOptionButtonD1Ev'

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
    'QStyleOptionButton::QStyleOptionButton()', which is called at the first
    use.

    Qt's own words:
    https://doc.qt.io/qt-6/qstyleoptionbutton.html#QStyleOptionButton
    """
    #  QStyleOptionButton::QStyleOptionButton()
    self._noteCreation(QStyleOptionButton, lambda: Rituals.call(
        'ritual_ZN18QStyleOptionButtonC1Ev',
    ))

  @overload(THIS)
  def __init__(self, other: QStyleOptionButton) -> None:
    """
    Notes what was given, for Qt's
    'QStyleOptionButton::QStyleOptionButton(const QStyleOptionButton
    &other)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qstyleoptionbutton.html#QStyleOptionButton

    Parameters
    ----------

    other : QStyleOptionButton
      Passed on as a value: Qt reads the C++ QStyleOptionButton, which stays
      Python's own.
    """
    #  QStyleOptionButton::QStyleOptionButton(const QStyleOptionButton
    #      &other)
    self._noteCreation(QStyleOptionButton, lambda: Rituals.call(
        'ritual_ZN18QStyleOptionButtonC1ERKS_', self._valueOf(other),
    ))

  @overload(int)
  def __init__(self, version: int) -> None:
    """
    Notes what was given, for Qt's
    'QStyleOptionButton::QStyleOptionButton(int version)', which is called at
    the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qstyleoptionbutton.html#QStyleOptionButton

    Parameters
    ----------

    version : int
      Passed on as it is.
    """
    #  QStyleOptionButton::QStyleOptionButton(int version)
    self._noteCreation(QStyleOptionButton, lambda: Rituals.call(
        'ritual_ZN18QStyleOptionButtonC1Ei', version,
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
