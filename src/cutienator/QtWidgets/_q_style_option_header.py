"""
QStyleOptionHeader binding of the Qt C++
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


class QStyleOptionHeader(QStyleOption):
  """
  The cute side of Qt's QStyleOptionHeader: a plain Python object standing in
  front of one C++ QStyleOptionHeader.

  It is built on the cute 'QStyleOption', as Qt's QStyleOptionHeader is built
  on Qt's QStyleOption, and has everything that class has.

  C++ hands a QStyleOptionHeader around as a copy, so every C++
  QStyleOptionHeader behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  No function of Qt's QStyleOptionHeader yet. It can be made from Python, in
  3 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QStyleOptionHeader &QStyleOptionHeader::operator=(const
    QStyleOptionHeader &a0)': assignment: Python binds a name and has no
    operator for it.
  - Qt's 'QStyleOptionHeader::~QStyleOptionHeader()': the destructor: Python
    removes its C++ QStyleOptionHeader by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QStyleOptionHeader is created at the first use, not by
    'QStyleOptionHeader(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QStyleOptionHeader back gives a copy the ritual made
    for Python, in a new cute QStyleOptionHeader.
  """

  #  The enums Qt writes inside QStyleOptionHeader, each a class in here as
  #  in C++, and the names Qt has for the combinations of its flags enums.

  class SectionPosition(CuteNum):
    """
    The enum 'QStyleOptionHeader::SectionPosition' of Qt, with the 4 names Qt
    gives in it.
    """

    Beginning = Kee[int](0)
    Middle = Kee[int](1)
    End = Kee[int](2)
    OnlyOneSection = Kee[int](3)

  class SelectedPosition(CuteNum):
    """
    The enum 'QStyleOptionHeader::SelectedPosition' of Qt, with the 4 names
    Qt gives in it.
    """

    NotAdjacent = Kee[int](0)
    NextIsSelected = Kee[int](1)
    PreviousIsSelected = Kee[int](2)
    NextAndPreviousAreSelected = Kee[int](3)

  class SortIndicator(CuteNum):
    """
    The enum 'QStyleOptionHeader::SortIndicator' of Qt, with the 3 names Qt
    gives in it.
    """

    NULL = Kee[int](0)
    SortUp = Kee[int](1)
    SortDown = Kee[int](2)

  class StyleOptionType(CuteNum):
    """
    The enum 'QStyleOptionHeader::StyleOptionType' of Qt, with the 1 names Qt
    gives in it.
    """

    Type = Kee[int](8)

  class StyleOptionVersion(CuteNum):
    """
    The enum 'QStyleOptionHeader::StyleOptionVersion' of Qt, with the 1 names
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
  __qt_class__ = 'QStyleOptionHeader'

  #  Qt's '~QStyleOptionHeader()'. Naming it makes this a value class: Python
  #  owns every C++ QStyleOptionHeader behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN18QStyleOptionHeaderD1Ev'

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
    'QStyleOptionHeader::QStyleOptionHeader()', which is called at the first
    use.

    Qt's own words:
    https://doc.qt.io/qt-6/qstyleoptionheader.html#QStyleOptionHeader
    """
    #  QStyleOptionHeader::QStyleOptionHeader()
    self._noteCreation(QStyleOptionHeader, lambda: Rituals.call(
        'ritual_ZN18QStyleOptionHeaderC1Ev',
    ))

  @overload(THIS)
  def __init__(self, other: QStyleOptionHeader) -> None:
    """
    Notes what was given, for Qt's
    'QStyleOptionHeader::QStyleOptionHeader(const QStyleOptionHeader
    &other)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qstyleoptionheader.html#QStyleOptionHeader

    Parameters
    ----------

    other : QStyleOptionHeader
      Passed on as a value: Qt reads the C++ QStyleOptionHeader, which stays
      Python's own.
    """
    #  QStyleOptionHeader::QStyleOptionHeader(const QStyleOptionHeader
    #      &other)
    self._noteCreation(QStyleOptionHeader, lambda: Rituals.call(
        'ritual_ZN18QStyleOptionHeaderC1ERKS_', self._valueOf(other),
    ))

  @overload(int)
  def __init__(self, version: int) -> None:
    """
    Notes what was given, for Qt's
    'QStyleOptionHeader::QStyleOptionHeader(int version)', which is called at
    the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qstyleoptionheader.html#QStyleOptionHeader

    Parameters
    ----------

    version : int
      Passed on as it is.
    """
    #  QStyleOptionHeader::QStyleOptionHeader(int version)
    self._noteCreation(QStyleOptionHeader, lambda: Rituals.call(
        'ritual_ZN18QStyleOptionHeaderC1Ei', version,
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
