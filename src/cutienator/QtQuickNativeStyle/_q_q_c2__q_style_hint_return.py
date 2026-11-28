"""
QQC2::QStyleHintReturn binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickNativeStyle/6.12.0/QtQuickNativeStyle/private/qqc2qstyleoption_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQC2::QStyleHintReturn to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute
from ..occult import Rituals


class QStyleHintReturn(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQC2::QStyleHintReturn: a plain Python object
  standing in front of one C++ QQC2::QStyleHintReturn.

  C++ hands a QQC2::QStyleHintReturn around as a copy, so every C++
  QQC2::QStyleHintReturn behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  No function of Qt's QQC2::QStyleHintReturn yet. It can be made from Python,
  in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QQC2::QStyleHintReturn::~QStyleHintReturn()': the destructor:
    Python removes its C++ QQC2::QStyleHintReturn by it, and has no other use
    for it.

  What to expect
  --------------

  - The C++ QQC2::QStyleHintReturn is created at the first use, not by
    'QQC2::QStyleHintReturn(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QQC2::QStyleHintReturn back gives a copy the ritual
    made for Python, in a new cute QQC2::QStyleHintReturn.
  """

  #  The enums Qt writes inside QQC2::QStyleHintReturn, each a class in here
  #  as in C++, and the names Qt has for the combinations of its flags enums.

  class HintReturnType(CuteNum):
    """
    The enum 'QQC2::QStyleHintReturn::HintReturnType' of Qt, with the 3 names
    Qt gives in it.
    """

    SH_Default = Kee[int](61440)
    SH_Mask = Kee[int](61441)
    SH_Variant = Kee[int](61442)

  class StyleOptionType(CuteNum):
    """
    The enum 'QQC2::QStyleHintReturn::StyleOptionType' of Qt, with the 1
    names Qt gives in it.
    """

    Type = Kee[int](61440)

  class StyleOptionVersion(CuteNum):
    """
    The enum 'QQC2::QStyleHintReturn::StyleOptionVersion' of Qt, with the 1
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
  __qt_class__ = 'QQC2::QStyleHintReturn'

  #  Qt's '~QQC2::QStyleHintReturn()'. Naming it makes this a value class:
  #  Python owns every C++ QQC2::QStyleHintReturn behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN4QQC216QStyleHintReturnD1Ev'

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
  def __init__(self, version: int = 1, type: int = 61440) -> None:
    """
    Notes what was given, for Qt's
    'QQC2::QStyleHintReturn::QStyleHintReturn(int version, int type)', which
    is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqc2-qstylehintreturn.html#QStyleHintReturn

    Parameters
    ----------

    version : int
      Passed on as it is. May be left out, as in Qt: it is then 1.

    type : int
      Passed on as it is. May be left out, as in Qt: it is then 61440.
    """
    #  QQC2::QStyleHintReturn::QStyleHintReturn(int version, int type)
    self._noteCreation(QStyleHintReturn, lambda: Rituals.call(
        'ritual_ZN4QQC216QStyleHintReturnC1Eii', version, type,
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
