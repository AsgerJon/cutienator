"""
QStyleOptionGroupBox binding of the Qt C++
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
from . import QStyleOptionComplex


class QStyleOptionGroupBox(QStyleOptionComplex):
  """
  The cute side of Qt's QStyleOptionGroupBox: a plain Python object standing
  in front of one C++ QStyleOptionGroupBox.

  It is built on the cute 'QStyleOptionComplex', as Qt's QStyleOptionGroupBox
  is built on Qt's QStyleOptionComplex, and has everything that class has.

  C++ hands a QStyleOptionGroupBox around as a copy, so every C++
  QStyleOptionGroupBox behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  No function of Qt's QStyleOptionGroupBox yet. It can be made from Python,
  in 3 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QStyleOptionGroupBox::~QStyleOptionGroupBox()': the destructor:
    Python removes its C++ QStyleOptionGroupBox by it, and has no other use
    for it.

  What has no ritual
  ------------------

  1 of the 5 functions Qt declares: 1 takes or gives a type that cannot be
  passed yet.

  What to expect
  --------------

  - The C++ QStyleOptionGroupBox is created at the first use, not by
    'QStyleOptionGroupBox(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QStyleOptionGroupBox back gives a copy the ritual
    made for Python, in a new cute QStyleOptionGroupBox.
  """

  #  The enums Qt writes inside QStyleOptionGroupBox, each a class in here as
  #  in C++, and the names Qt has for the combinations of its flags enums.

  class StyleOptionType(CuteNum):
    """
    The enum 'QStyleOptionGroupBox::StyleOptionType' of Qt, with the 1 names
    Qt gives in it.
    """

    Type = Kee[int](983046)

  class StyleOptionVersion(CuteNum):
    """
    The enum 'QStyleOptionGroupBox::StyleOptionVersion' of Qt, with the 1
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
  __qt_class__ = 'QStyleOptionGroupBox'

  #  Qt's '~QStyleOptionGroupBox()'. Naming it makes this a value class:
  #  Python owns every C++ QStyleOptionGroupBox behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN20QStyleOptionGroupBoxD1Ev'

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
    'QStyleOptionGroupBox::QStyleOptionGroupBox()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qstyleoptiongroupbox.html#QStyleOptionGroupBox
    """
    #  QStyleOptionGroupBox::QStyleOptionGroupBox()
    self._noteCreation(QStyleOptionGroupBox, lambda: Rituals.call(
        'ritual_ZN20QStyleOptionGroupBoxC1Ev',
    ))

  @overload(THIS)
  def __init__(self, other: QStyleOptionGroupBox) -> None:
    """
    Notes what was given, for Qt's
    'QStyleOptionGroupBox::QStyleOptionGroupBox(const QStyleOptionGroupBox
    &other)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qstyleoptiongroupbox.html#QStyleOptionGroupBox

    Parameters
    ----------

    other : QStyleOptionGroupBox
      Passed on as a value: Qt reads the C++ QStyleOptionGroupBox, which
      stays Python's own.
    """
    #  QStyleOptionGroupBox::QStyleOptionGroupBox(const QStyleOptionGroupBox
    #      &other)
    self._noteCreation(QStyleOptionGroupBox, lambda: Rituals.call(
        'ritual_ZN20QStyleOptionGroupBoxC1ERKS_', self._valueOf(other),
    ))

  @overload(int)
  def __init__(self, version: int) -> None:
    """
    Notes what was given, for Qt's
    'QStyleOptionGroupBox::QStyleOptionGroupBox(int version)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qstyleoptiongroupbox.html#QStyleOptionGroupBox

    Parameters
    ----------

    version : int
      Passed on as it is.
    """
    #  QStyleOptionGroupBox::QStyleOptionGroupBox(int version)
    self._noteCreation(QStyleOptionGroupBox, lambda: Rituals.call(
        'ritual_ZN20QStyleOptionGroupBoxC1Ei', version,
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
