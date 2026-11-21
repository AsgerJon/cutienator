"""
QStyleOptionFrame binding of the Qt C++
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


class QStyleOptionFrame(QStyleOption):
  """
  The cute side of Qt's QStyleOptionFrame: a plain Python object standing in
  front of one C++ QStyleOptionFrame.

  It is built on the cute 'QStyleOption', as Qt's QStyleOptionFrame is built
  on Qt's QStyleOption, and has everything that class has.

  C++ hands a QStyleOptionFrame around as a copy, so every C++
  QStyleOptionFrame behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  No function of Qt's QStyleOptionFrame yet. It can be made from Python, in 2
  ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QStyleOptionFrame::~QStyleOptionFrame()': the destructor: Python
    removes its C++ QStyleOptionFrame by it, and has no other use for it.

  What has no ritual
  ------------------

  2 of the 5 functions Qt declares: 1 takes or gives a type that cannot be
  passed yet; 1 protected.

  What to expect
  --------------

  - The C++ QStyleOptionFrame is created at the first use, not by
    'QStyleOptionFrame(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QStyleOptionFrame back gives a copy the ritual made
    for Python, in a new cute QStyleOptionFrame.
  """

  #  The enums Qt writes inside QStyleOptionFrame, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class FrameFeature(CuteFlags):
    """
    The flags enum 'QStyleOptionFrame::FrameFeature' of Qt, with the 3 names
    Qt gives in it. Qt names the type of its combinations
    'QStyleOptionFrame::FrameFeatures'.
    """

    NULL = 0x0
    Flat = 0x1
    Rounded = 0x2

  FrameFeatures = FrameFeature

  class StyleOptionType(CuteNum):
    """
    The enum 'QStyleOptionFrame::StyleOptionType' of Qt, with the 1 names Qt
    gives in it.
    """

    Type = Kee[int](5)

  class StyleOptionVersion(CuteNum):
    """
    The enum 'QStyleOptionFrame::StyleOptionVersion' of Qt, with the 1 names
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
  __qt_class__ = 'QStyleOptionFrame'

  #  Qt's '~QStyleOptionFrame()'. Naming it makes this a value class: Python
  #  owns every C++ QStyleOptionFrame behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN17QStyleOptionFrameD1Ev'

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
    Notes what was given, for Qt's 'QStyleOptionFrame::QStyleOptionFrame()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qstyleoptionframe.html#QStyleOptionFrame
    """
    #  QStyleOptionFrame::QStyleOptionFrame()
    self._noteCreation(QStyleOptionFrame, lambda: Rituals.call(
        'ritual_ZN17QStyleOptionFrameC1Ev',
    ))

  @overload(THIS)
  def __init__(self, other: QStyleOptionFrame) -> None:
    """
    Notes what was given, for Qt's
    'QStyleOptionFrame::QStyleOptionFrame(const QStyleOptionFrame &other)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qstyleoptionframe.html#QStyleOptionFrame

    Parameters
    ----------

    other : QStyleOptionFrame
      Passed on as a value: Qt reads the C++ QStyleOptionFrame, which stays
      Python's own.
    """
    #  QStyleOptionFrame::QStyleOptionFrame(const QStyleOptionFrame &other)
    self._noteCreation(QStyleOptionFrame, lambda: Rituals.call(
        'ritual_ZN17QStyleOptionFrameC1ERKS_', self._valueOf(other),
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
