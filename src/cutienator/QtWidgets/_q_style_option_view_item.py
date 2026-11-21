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

from ..occult import Rituals
from . import QStyleOption, QStyleOptionViewItemPosition
from . import QStyleOptionViewItemStyleOptionType
from . import QStyleOptionViewItemStyleOptionVersion
from . import QStyleOptionViewItemViewItemFeature
from . import QStyleOptionViewItemViewItemPosition


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
  in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QStyleOptionViewItem::~QStyleOptionViewItem()': the destructor:
    Python removes its C++ QStyleOptionViewItem by it, and has no other use
    for it.

  What has no ritual
  ------------------

  2 of the 5 functions Qt declares: 1 takes or gives a type that cannot be
  passed yet; 1 protected.

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

  #  The enums Qt writes inside QStyleOptionViewItem, and the names Qt has
  #  for the combinations of its flags enums.
  Position = QStyleOptionViewItemPosition
  StyleOptionType = QStyleOptionViewItemStyleOptionType
  StyleOptionVersion = QStyleOptionViewItemStyleOptionVersion
  ViewItemFeature = QStyleOptionViewItemViewItemFeature
  ViewItemFeatures = QStyleOptionViewItemViewItemFeature
  ViewItemPosition = QStyleOptionViewItemViewItemPosition

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
