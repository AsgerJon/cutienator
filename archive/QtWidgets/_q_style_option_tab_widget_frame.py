"""
QStyleOptionTabWidgetFrame binding of the Qt C++
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


class QStyleOptionTabWidgetFrame(QStyleOption):
  """
  The cute side of Qt's QStyleOptionTabWidgetFrame: a plain Python object
  standing in front of one C++ QStyleOptionTabWidgetFrame.

  It is built on the cute 'QStyleOption', as Qt's QStyleOptionTabWidgetFrame
  is built on Qt's QStyleOption, and has everything that class has.

  C++ hands a QStyleOptionTabWidgetFrame around as a copy, so every C++
  QStyleOptionTabWidgetFrame behind a cute one is Python's own: it is
  removed, by the ritual named in '__delete_ritual__', when the cute object
  goes.

  What exists
  -----------

  No function of Qt's QStyleOptionTabWidgetFrame yet. It can be made from
  Python, in 3 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QStyleOptionTabWidgetFrame::~QStyleOptionTabWidgetFrame()': the
    destructor: Python removes its C++ QStyleOptionTabWidgetFrame by it, and
    has no other use for it.

  What has no ritual
  ------------------

  1 of the 5 functions Qt declares: 1 takes or gives a type that cannot be
  passed yet.

  What to expect
  --------------

  - The C++ QStyleOptionTabWidgetFrame is created at the first use, not by
    'QStyleOptionTabWidgetFrame(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QStyleOptionTabWidgetFrame back gives a copy the
    ritual made for Python, in a new cute QStyleOptionTabWidgetFrame.
  """

  #  The enums Qt writes inside QStyleOptionTabWidgetFrame, each a class in
  #  here as in C++, and the names Qt has for the combinations of its flags
  #  enums.

  class StyleOptionType(CuteNum):
    """
    The enum 'QStyleOptionTabWidgetFrame::StyleOptionType' of Qt, with the 1
    names Qt gives in it.
    """

    Type = Kee[int](11)

  class StyleOptionVersion(CuteNum):
    """
    The enum 'QStyleOptionTabWidgetFrame::StyleOptionVersion' of Qt, with the
    1 names Qt gives in it.
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
  __qt_class__ = 'QStyleOptionTabWidgetFrame'

  #  Qt's '~QStyleOptionTabWidgetFrame()'. Naming it makes this a value
  #  class: Python owns every C++ QStyleOptionTabWidgetFrame behind a cute
  #  one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN26QStyleOptionTabWidgetFrameD1Ev'

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
    'QStyleOptionTabWidgetFrame::QStyleOptionTabWidgetFrame()', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qstyleoptiontabwidgetframe.html
    """
    #  QStyleOptionTabWidgetFrame::QStyleOptionTabWidgetFrame()
    self._noteCreation(QStyleOptionTabWidgetFrame, lambda: Rituals.call(
        'ritual_ZN26QStyleOptionTabWidgetFrameC1Ev',
    ))

  @overload(THIS)
  def __init__(self, other: QStyleOptionTabWidgetFrame) -> None:
    """
    Notes what was given, for Qt's
    'QStyleOptionTabWidgetFrame::QStyleOptionTabWidgetFrame(const
    QStyleOptionTabWidgetFrame &other)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qstyleoptiontabwidgetframe.html

    Parameters
    ----------

    other : QStyleOptionTabWidgetFrame
      Passed on as a value: Qt reads the C++ QStyleOptionTabWidgetFrame,
      which stays Python's own.
    """
    #  QStyleOptionTabWidgetFrame::QStyleOptionTabWidgetFrame(const
    #      QStyleOptionTabWidgetFrame &other)
    self._noteCreation(QStyleOptionTabWidgetFrame, lambda: Rituals.call(
        'ritual_ZN26QStyleOptionTabWidgetFrameC1ERKS_', self._valueOf(other),
    ))

  @overload(int)
  def __init__(self, version: int) -> None:
    """
    Notes what was given, for Qt's
    'QStyleOptionTabWidgetFrame::QStyleOptionTabWidgetFrame(int version)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qstyleoptiontabwidgetframe.html

    Parameters
    ----------

    version : int
      Passed on as it is.
    """
    #  QStyleOptionTabWidgetFrame::QStyleOptionTabWidgetFrame(int version)
    self._noteCreation(QStyleOptionTabWidgetFrame, lambda: Rituals.call(
        'ritual_ZN26QStyleOptionTabWidgetFrameC1Ei', version,
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
