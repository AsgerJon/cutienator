"""
QQC2::QStyleOptionButton binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickNativeStyle/6.12.0/QtQuickNativeStyle/private/qqc2qstyleoption_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQC2::QStyleOptionButton to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteFlags, CuteNum, MetaCute
from ..occult import Rituals


class QStyleOptionButton(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQC2::QStyleOptionButton: a plain Python object
  standing in front of one C++ QQC2::QStyleOptionButton.

  C++ hands a QQC2::QStyleOptionButton around as a copy, so every C++
  QQC2::QStyleOptionButton behind a cute one is Python's own: it is removed,
  by the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  No function of Qt's QQC2::QStyleOptionButton yet. It can be made from
  Python, in 3 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QStyleOptionButton &QQC2::QStyleOptionButton::operator=(const
    QStyleOptionButton &a0)': assignment: Python binds a name and has no
    operator for it.
  - Qt's 'QQC2::QStyleOptionButton::~QStyleOptionButton()': the destructor:
    Python removes its C++ QQC2::QStyleOptionButton by it, and has no other
    use for it.

  What to expect
  --------------

  - The C++ QQC2::QStyleOptionButton is created at the first use, not by
    'QQC2::QStyleOptionButton(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QQC2::QStyleOptionButton back gives a copy the ritual
    made for Python, in a new cute QQC2::QStyleOptionButton.
  """

  #  The enums Qt writes inside QQC2::QStyleOptionButton, each a class in
  #  here as in C++, and the names Qt has for the combinations of its flags
  #  enums.

  class ButtonFeature(CuteFlags):
    """
    The flags enum 'QQC2::QStyleOptionButton::ButtonFeature' of Qt, with the
    6 names Qt gives in it. Qt names the type of its combinations
    'QQC2::QStyleOptionButton::ButtonFeatures'.
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
    The enum 'QQC2::QStyleOptionButton::StyleOptionType' of Qt, with the 1
    names Qt gives in it.
    """

    Type = Kee[int](2)

  class StyleOptionVersion(CuteNum):
    """
    The enum 'QQC2::QStyleOptionButton::StyleOptionVersion' of Qt, with the 1
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
  __qt_class__ = 'QQC2::QStyleOptionButton'

  #  Qt's '~QQC2::QStyleOptionButton()'. Naming it makes this a value class:
  #  Python owns every C++ QQC2::QStyleOptionButton behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN4QQC218QStyleOptionButtonD1Ev'

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
    'QQC2::QStyleOptionButton::QStyleOptionButton()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqc2-qstyleoptionbutton.html#QStyleOptionButton
    """
    #  QQC2::QStyleOptionButton::QStyleOptionButton()
    self._noteCreation(QStyleOptionButton, lambda: Rituals.call(
        'ritual_ZN4QQC218QStyleOptionButtonC1Ev',
    ))

  @overload(THIS)
  def __init__(self, other: QStyleOptionButton) -> None:
    """
    Notes what was given, for Qt's
    'QQC2::QStyleOptionButton::QStyleOptionButton(const QStyleOptionButton
    &other)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqc2-qstyleoptionbutton.html#QStyleOptionButton

    Parameters
    ----------

    other : QStyleOptionButton
      Passed on as a value: Qt reads the C++ QQC2::QStyleOptionButton, which
      stays Python's own.
    """
    #  QQC2::QStyleOptionButton::QStyleOptionButton(const QStyleOptionButton
    #      &other)
    self._noteCreation(QStyleOptionButton, lambda: Rituals.call(
        'ritual_ZN4QQC218QStyleOptionButtonC1ERKS0_', self._valueOf(other),
    ))

  @overload(int)
  def __init__(self, version: int) -> None:
    """
    Notes what was given, for Qt's
    'QQC2::QStyleOptionButton::QStyleOptionButton(int version)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqc2-qstyleoptionbutton.html#QStyleOptionButton

    Parameters
    ----------

    version : int
      Passed on as it is.
    """
    #  QQC2::QStyleOptionButton::QStyleOptionButton(int version)
    self._noteCreation(QStyleOptionButton, lambda: Rituals.call(
        'ritual_ZN4QQC218QStyleOptionButtonC1Ei', version,
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
