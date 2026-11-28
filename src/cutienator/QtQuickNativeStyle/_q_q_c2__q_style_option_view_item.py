"""
QQC2::QStyleOptionViewItem binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickNativeStyle/6.12.0/QtQuickNativeStyle/private/qqc2qstyleoption_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQC2::QStyleOptionViewItem to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteFlags, CuteNum, MetaCute
from ..occult import Rituals


class QStyleOptionViewItem(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQC2::QStyleOptionViewItem: a plain Python object
  standing in front of one C++ QQC2::QStyleOptionViewItem.

  C++ hands a QQC2::QStyleOptionViewItem around as a copy, so every C++
  QQC2::QStyleOptionViewItem behind a cute one is Python's own: it is
  removed, by the ritual named in '__delete_ritual__', when the cute object
  goes.

  What exists
  -----------

  No function of Qt's QQC2::QStyleOptionViewItem yet. It can be made from
  Python, in 3 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QStyleOptionViewItem &QQC2::QStyleOptionViewItem::operator=(const
    QStyleOptionViewItem &a0)': assignment: Python binds a name and has no
    operator for it.
  - Qt's 'QQC2::QStyleOptionViewItem::~QStyleOptionViewItem()': the
    destructor: Python removes its C++ QQC2::QStyleOptionViewItem by it, and
    has no other use for it.

  What to expect
  --------------

  - The C++ QQC2::QStyleOptionViewItem is created at the first use, not by
    'QQC2::QStyleOptionViewItem(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QQC2::QStyleOptionViewItem back gives a copy the
    ritual made for Python, in a new cute QQC2::QStyleOptionViewItem.
  """

  #  The enums Qt writes inside QQC2::QStyleOptionViewItem, each a class in
  #  here as in C++, and the names Qt has for the combinations of its flags
  #  enums.

  class Position(CuteNum):
    """
    The enum 'QQC2::QStyleOptionViewItem::Position' of Qt, with the 4 names
    Qt gives in it.
    """

    Left = Kee[int](0)
    Right = Kee[int](1)
    Top = Kee[int](2)
    Bottom = Kee[int](3)

  class ScrollMode(CuteNum):
    """
    The enum 'QQC2::QStyleOptionViewItem::ScrollMode' of Qt, with the 2 names
    Qt gives in it.
    """

    ScrollPerItem = Kee[int](0)
    ScrollPerPixel = Kee[int](1)

  class StyleOptionType(CuteNum):
    """
    The enum 'QQC2::QStyleOptionViewItem::StyleOptionType' of Qt, with the 1
    names Qt gives in it.
    """

    Type = Kee[int](10)

  class StyleOptionVersion(CuteNum):
    """
    The enum 'QQC2::QStyleOptionViewItem::StyleOptionVersion' of Qt, with the
    1 names Qt gives in it.
    """

    Version = Kee[int](4)

  class ViewItemFeature(CuteFlags):
    """
    The flags enum 'QQC2::QStyleOptionViewItem::ViewItemFeature' of Qt, with
    the 6 names Qt gives in it. Qt names the type of its combinations
    'QQC2::QStyleOptionViewItem::ViewItemFeatures'.
    """

    NULL = 0x0
    WrapText = 0x1
    Alternate = 0x2
    HasCheckIndicator = 0x4
    HasDisplay = 0x8
    HasDecoration = 0x10

  ViewItemFeatures = ViewItemFeature

  class ViewItemPosition(CuteNum):
    """
    The enum 'QQC2::QStyleOptionViewItem::ViewItemPosition' of Qt, with the 5
    names Qt gives in it.
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
  __qt_class__ = 'QQC2::QStyleOptionViewItem'

  #  Qt's '~QQC2::QStyleOptionViewItem()'. Naming it makes this a value
  #  class: Python owns every C++ QQC2::QStyleOptionViewItem behind a cute
  #  one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN4QQC220QStyleOptionViewItemD1Ev'

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
    'QQC2::QStyleOptionViewItem::QStyleOptionViewItem()', which is called at
    the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqc2-qstyleoptionviewitem.html
    """
    #  QQC2::QStyleOptionViewItem::QStyleOptionViewItem()
    self._noteCreation(QStyleOptionViewItem, lambda: Rituals.call(
        'ritual_ZN4QQC220QStyleOptionViewItemC1Ev',
    ))

  @overload(THIS)
  def __init__(self, other: QStyleOptionViewItem) -> None:
    """
    Notes what was given, for Qt's
    'QQC2::QStyleOptionViewItem::QStyleOptionViewItem(const
    QStyleOptionViewItem &other)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqc2-qstyleoptionviewitem.html

    Parameters
    ----------

    other : QStyleOptionViewItem
      Passed on as a value: Qt reads the C++ QQC2::QStyleOptionViewItem,
      which stays Python's own.
    """
    #  QQC2::QStyleOptionViewItem::QStyleOptionViewItem(const
    #      QStyleOptionViewItem &other)
    self._noteCreation(QStyleOptionViewItem, lambda: Rituals.call(
        'ritual_ZN4QQC220QStyleOptionViewItemC1ERKS0_', self._valueOf(other),
    ))

  @overload(int)
  def __init__(self, version: int) -> None:
    """
    Notes what was given, for Qt's
    'QQC2::QStyleOptionViewItem::QStyleOptionViewItem(int version)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqc2-qstyleoptionviewitem.html

    Parameters
    ----------

    version : int
      Passed on as it is.
    """
    #  QQC2::QStyleOptionViewItem::QStyleOptionViewItem(int version)
    self._noteCreation(QStyleOptionViewItem, lambda: Rituals.call(
        'ritual_ZN4QQC220QStyleOptionViewItemC1Ei', version,
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
