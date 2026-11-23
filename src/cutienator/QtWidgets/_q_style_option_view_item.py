"""
QStyleOptionViewItem binding of the Qt C++
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


class QStyleOptionViewItem(QStyleOption):
  """
  The cute side of Qt's QStyleOptionViewItem: a plain Python object standing
  in front of one C++ QStyleOptionViewItem.

  It is built on the cute 'QStyleOption', as Qt's QStyleOptionViewItem is
  built on Qt's QStyleOption, and has everything that class has.

  C++ hands a QStyleOptionViewItem around as a copy, so every C++
  QStyleOptionViewItem behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  No function of Qt's QStyleOptionViewItem yet. It can be made from Python,
  in 3 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QStyleOptionViewItem::~QStyleOptionViewItem()': the destructor:
    Python removes its C++ QStyleOptionViewItem by it, and has no other use
    for it.

  What has no ritual
  ------------------

  1 of the 5 functions Qt declares: 1 takes or gives a type that cannot be
  passed yet.

  What to expect
  --------------

  - The C++ QStyleOptionViewItem is created at the first use, not by
    'QStyleOptionViewItem(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QStyleOptionViewItem back gives a copy the ritual
    made for Python, in a new cute QStyleOptionViewItem.
  """

  #  The enums Qt writes inside QStyleOptionViewItem, each a class in here as
  #  in C++, and the names Qt has for the combinations of its flags enums.

  class Position(CuteNum):
    """
    The enum 'QStyleOptionViewItem::Position' of Qt, with the 4 names Qt
    gives in it.
    """

    Left = Kee[int](0)
    Right = Kee[int](1)
    Top = Kee[int](2)
    Bottom = Kee[int](3)

  class StyleOptionType(CuteNum):
    """
    The enum 'QStyleOptionViewItem::StyleOptionType' of Qt, with the 1 names
    Qt gives in it.
    """

    Type = Kee[int](10)

  class StyleOptionVersion(CuteNum):
    """
    The enum 'QStyleOptionViewItem::StyleOptionVersion' of Qt, with the 1
    names Qt gives in it.
    """

    Version = Kee[int](1)

  class ViewItemFeature(CuteFlags):
    """
    The flags enum 'QStyleOptionViewItem::ViewItemFeature' of Qt, with the 8
    names Qt gives in it. Qt names the type of its combinations
    'QStyleOptionViewItem::ViewItemFeatures'.
    """

    NULL = 0x0
    WrapText = 0x1
    Alternate = 0x2
    HasCheckIndicator = 0x4
    HasDisplay = 0x8
    HasDecoration = 0x10
    IsDecoratedRootColumn = 0x20
    IsDecorationForRootColumn = 0x40

  ViewItemFeatures = ViewItemFeature

  class ViewItemPosition(CuteNum):
    """
    The enum 'QStyleOptionViewItem::ViewItemPosition' of Qt, with the 5 names
    Qt gives in it.
    """

    Invalid = Kee[int](0)
    Beginning = Kee[int](1)
    Middle = Kee[int](2)
    End = Kee[int](3)
    OnlyOne = Kee[int](4)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QStyleOptionViewItem'

  #  Qt's '~QStyleOptionViewItem()'. Naming it makes this a value class:
  #  Python owns every C++ QStyleOptionViewItem behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN20QStyleOptionViewItemD1Ev'

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
    'QStyleOptionViewItem::QStyleOptionViewItem()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qstyleoptionviewitem.html#QStyleOptionViewItem
    """
    #  QStyleOptionViewItem::QStyleOptionViewItem()
    self._noteCreation(QStyleOptionViewItem, lambda: Rituals.call(
        'ritual_ZN20QStyleOptionViewItemC1Ev',
    ))

  @overload(THIS)
  def __init__(self, other: QStyleOptionViewItem) -> None:
    """
    Notes what was given, for Qt's
    'QStyleOptionViewItem::QStyleOptionViewItem(const QStyleOptionViewItem
    &other)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qstyleoptionviewitem.html#QStyleOptionViewItem

    Parameters
    ----------

    other : QStyleOptionViewItem
      Passed on as a value: Qt reads the C++ QStyleOptionViewItem, which
      stays Python's own.
    """
    #  QStyleOptionViewItem::QStyleOptionViewItem(const QStyleOptionViewItem
    #      &other)
    self._noteCreation(QStyleOptionViewItem, lambda: Rituals.call(
        'ritual_ZN20QStyleOptionViewItemC1ERKS_', self._valueOf(other),
    ))

  @overload(int)
  def __init__(self, version: int) -> None:
    """
    Notes what was given, for Qt's
    'QStyleOptionViewItem::QStyleOptionViewItem(int version)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qstyleoptionviewitem.html#QStyleOptionViewItem

    Parameters
    ----------

    version : int
      Passed on as it is.
    """
    #  QStyleOptionViewItem::QStyleOptionViewItem(int version)
    self._noteCreation(QStyleOptionViewItem, lambda: Rituals.call(
        'ritual_ZN20QStyleOptionViewItemC1Ei', version,
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
