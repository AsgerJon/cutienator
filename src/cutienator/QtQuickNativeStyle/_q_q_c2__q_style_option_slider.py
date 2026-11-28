"""
QQC2::QStyleOptionSlider binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickNativeStyle/6.12.0/QtQuickNativeStyle/private/qqc2qstyleoption_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQC2::QStyleOptionSlider to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute
from ..occult import Rituals


class QStyleOptionSlider(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQC2::QStyleOptionSlider: a plain Python object
  standing in front of one C++ QQC2::QStyleOptionSlider.

  C++ hands a QQC2::QStyleOptionSlider around as a copy, so every C++
  QQC2::QStyleOptionSlider behind a cute one is Python's own: it is removed,
  by the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  No function of Qt's QQC2::QStyleOptionSlider yet. It can be made from
  Python, in 3 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QStyleOptionSlider &QQC2::QStyleOptionSlider::operator=(const
    QStyleOptionSlider &a0)': assignment: Python binds a name and has no
    operator for it.
  - Qt's 'QQC2::QStyleOptionSlider::~QStyleOptionSlider()': the destructor:
    Python removes its C++ QQC2::QStyleOptionSlider by it, and has no other
    use for it.

  What to expect
  --------------

  - The C++ QQC2::QStyleOptionSlider is created at the first use, not by
    'QQC2::QStyleOptionSlider(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QQC2::QStyleOptionSlider back gives a copy the ritual
    made for Python, in a new cute QQC2::QStyleOptionSlider.
  """

  #  The enums Qt writes inside QQC2::QStyleOptionSlider, each a class in
  #  here as in C++, and the names Qt has for the combinations of its flags
  #  enums.

  class StyleOptionType(CuteNum):
    """
    The enum 'QQC2::QStyleOptionSlider::StyleOptionType' of Qt, with the 1
    names Qt gives in it.
    """

    Type = Kee[int](983041)

  class StyleOptionVersion(CuteNum):
    """
    The enum 'QQC2::QStyleOptionSlider::StyleOptionVersion' of Qt, with the 1
    names Qt gives in it.
    """

    Version = Kee[int](1)

  class TickPosition(CuteNum):
    """
    The enum 'QQC2::QStyleOptionSlider::TickPosition' of Qt, with the 6 names
    Qt gives in it.
    """

    NoTicks = Kee[int](0)
    TicksAbove = Kee[int](1)
    TicksLeft = Kee[int](1)
    TicksBelow = Kee[int](2)
    TicksRight = Kee[int](2)
    TicksBothSides = Kee[int](3)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQC2::QStyleOptionSlider'

  #  Qt's '~QQC2::QStyleOptionSlider()'. Naming it makes this a value class:
  #  Python owns every C++ QQC2::QStyleOptionSlider behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN4QQC218QStyleOptionSliderD1Ev'

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
    'QQC2::QStyleOptionSlider::QStyleOptionSlider()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqc2-qstyleoptionslider.html#QStyleOptionSlider
    """
    #  QQC2::QStyleOptionSlider::QStyleOptionSlider()
    self._noteCreation(QStyleOptionSlider, lambda: Rituals.call(
        'ritual_ZN4QQC218QStyleOptionSliderC1Ev',
    ))

  @overload(THIS)
  def __init__(self, other: QStyleOptionSlider) -> None:
    """
    Notes what was given, for Qt's
    'QQC2::QStyleOptionSlider::QStyleOptionSlider(const QStyleOptionSlider
    &other)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqc2-qstyleoptionslider.html#QStyleOptionSlider

    Parameters
    ----------

    other : QStyleOptionSlider
      Passed on as a value: Qt reads the C++ QQC2::QStyleOptionSlider, which
      stays Python's own.
    """
    #  QQC2::QStyleOptionSlider::QStyleOptionSlider(const QStyleOptionSlider
    #      &other)
    self._noteCreation(QStyleOptionSlider, lambda: Rituals.call(
        'ritual_ZN4QQC218QStyleOptionSliderC1ERKS0_', self._valueOf(other),
    ))

  @overload(int)
  def __init__(self, version: int) -> None:
    """
    Notes what was given, for Qt's
    'QQC2::QStyleOptionSlider::QStyleOptionSlider(int version)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqc2-qstyleoptionslider.html#QStyleOptionSlider

    Parameters
    ----------

    version : int
      Passed on as it is.
    """
    #  QQC2::QStyleOptionSlider::QStyleOptionSlider(int version)
    self._noteCreation(QStyleOptionSlider, lambda: Rituals.call(
        'ritual_ZN4QQC218QStyleOptionSliderC1Ei', version,
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
