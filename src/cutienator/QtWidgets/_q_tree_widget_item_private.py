"""
QTreeWidgetItemPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/6.12.0/QtWidgets/private/qtreewidget_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QTreeWidgetItemPrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import Qt

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QTreeWidgetItem
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QTreeWidgetItem = WAIT['QTreeWidgetItem']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QTreeWidgetItemPrivate(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QTreeWidgetItemPrivate: a plain Python object
  standing in front of one C++ QTreeWidgetItemPrivate.

  C++ hands a QTreeWidgetItemPrivate around as a copy, so every C++
  QTreeWidgetItemPrivate behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QTreeWidgetItemPrivate that has a ritual and that
  Python can call so far, 3 names in all: 'propagateDisabled',
  'updateHiddenStatus', 'sortChildren'. It can be made from Python, in 1 way;
  see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QTreeWidgetItemPrivate::~QTreeWidgetItemPrivate()': the destructor:
    Python removes its C++ QTreeWidgetItemPrivate by it, and has no other use
    for it.

  What to expect
  --------------

  - The C++ QTreeWidgetItemPrivate is created at the first use, not by
    'QTreeWidgetItemPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QTreeWidgetItemPrivate back gives a copy the ritual
    made for Python, in a new cute QTreeWidgetItemPrivate.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QTreeWidgetItemPrivate'

  #  Qt's '~QTreeWidgetItemPrivate()'. Naming it makes this a value class:
  #  Python owns every C++ QTreeWidgetItemPrivate behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN22QTreeWidgetItemPrivateD1Ev'

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

  @overload(QTreeWidgetItem)
  @overload(NoneType)
  def __init__(self, item: Optional[QTreeWidgetItem]) -> None:
    """
    Notes what was given, for Qt's
    'QTreeWidgetItemPrivate::QTreeWidgetItemPrivate(QTreeWidgetItem *item)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qtreewidgetitemprivate.html#QTreeWidgetItemPrivate

    Parameters
    ----------

    item : Optional[QTreeWidgetItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QTreeWidgetItemPrivate::QTreeWidgetItemPrivate(QTreeWidgetItem *item)
    self._noteCreation(QTreeWidgetItemPrivate, lambda: Rituals.call(
        'ritual_ZN22QTreeWidgetItemPrivateC1EP15QTreeWidgetItem',
        self._addressOf(item),
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

  @overload(QTreeWidgetItem)
  @overload(NoneType)
  def propagateDisabled(self, item: Optional[QTreeWidgetItem]) -> None:
    """
    Calls Qt's 'void
    QTreeWidgetItemPrivate::propagateDisabled(QTreeWidgetItem *item)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtreewidgetitemprivate.html#propagateDisabled

    Parameters
    ----------

    item : Optional[QTreeWidgetItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QTreeWidgetItemPrivate::propagateDisabled(QTreeWidgetItem *item)
    self.uglySide.call(
        'ritual_ZN22QTreeWidgetItemPrivate17propagateDisabledEP15QTreeWidge'
        'tItem',
        self._addressOf(item),
    )

  @overload(QTreeWidgetItem, bool)
  @overload(NoneType, bool)
  def updateHiddenStatus(
      self,
      item: Optional[QTreeWidgetItem],
      inserting: bool,
  ) -> None:
    """
    Calls Qt's 'void
    QTreeWidgetItemPrivate::updateHiddenStatus(QTreeWidgetItem *item, bool
    inserting)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtreewidgetitemprivate.html#updateHiddenStatus

    Parameters
    ----------

    item : Optional[QTreeWidgetItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    inserting : bool
      Passed on as it is.
    """
    #  void QTreeWidgetItemPrivate::updateHiddenStatus(QTreeWidgetItem *item,
    #      bool inserting)
    self.uglySide.call(
        'ritual_ZN22QTreeWidgetItemPrivate18updateHiddenStatusEP15QTreeWidg'
        'etItemb',
        self._addressOf(item), inserting,
    )

  @overload(int, Qt.SortOrder, bool)
  def sortChildren(
      self,
      column: int,
      order: Qt.SortOrder,
      climb: bool,
  ) -> None:
    """
    Calls Qt's 'void QTreeWidgetItemPrivate::sortChildren(int column,
    Qt::SortOrder order, bool climb)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtreewidgetitemprivate.html#sortChildren

    Parameters
    ----------

    column : int
      Passed on as it is.

    order : Qt.SortOrder
      Passed on as its number.

    climb : bool
      Passed on as it is.
    """
    #  void QTreeWidgetItemPrivate::sortChildren(int column, Qt::SortOrder
    #      order, bool climb)
    self.uglySide.call(
        'ritual_ZN22QTreeWidgetItemPrivate12sortChildrenEiN2Qt9SortOrderEb',
        column, order.value, climb,
    )
