"""
QCompleterItemDelegate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/6.12.0/QtWidgets/private/qcompleter_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QCompleterItemDelegate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from . import QStyledItemDelegate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QModelIndex
  from ..QtGui import QPainter
  from . import QAbstractItemView, QStyleOptionViewItem
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QAbstractItemView = WAIT['QAbstractItemView']
  QModelIndex = WAIT['QModelIndex']
  QPainter = WAIT['QPainter']
  QStyleOptionViewItem = WAIT['QStyleOptionViewItem']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QCompleterItemDelegate(QStyledItemDelegate):
  """
  The cute side of Qt's QCompleterItemDelegate: a plain Python object
  standing in front of one C++ QCompleterItemDelegate.

  It is built on the cute 'QStyledItemDelegate', as Qt's
  QCompleterItemDelegate is built on Qt's QStyledItemDelegate, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QCompleterItemDelegate that has a ritual and that
  Python can call so far, 1 name in all: 'paint'. It can be made from Python,
  in 1 way; see '__init__'.

  What to expect
  --------------

  - The C++ QCompleterItemDelegate is created at the first use, not by
    'QCompleterItemDelegate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QCompleterItemDelegate.
  - Qt tells when it has removed the C++ QCompleterItemDelegate. Every call
    on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QCompleterItemDelegate'

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

  @overload(QAbstractItemView)
  @overload(NoneType)
  def __init__(self, view: Optional[QAbstractItemView]) -> None:
    """
    Notes what was given, for Qt's
    'QCompleterItemDelegate::QCompleterItemDelegate(QAbstractItemView
    *view)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qcompleteritemdelegate.html#QCompleterItemDelegate

    Parameters
    ----------

    view : Optional[QAbstractItemView]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QCompleterItemDelegate::QCompleterItemDelegate(QAbstractItemView
    #      *view)
    self._noteCreation(QCompleterItemDelegate, lambda: Rituals.call(
        'ritual_ZN22QCompleterItemDelegateC1EP17QAbstractItemView',
        self._addressOf(view),
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

  @overload(QPainter, QStyleOptionViewItem, QModelIndex)
  @overload(NoneType, QStyleOptionViewItem, QModelIndex)
  def paint(
      self,
      p: Optional[QPainter],
      opt: QStyleOptionViewItem,
      idx: QModelIndex,
  ) -> None:
    """
    Calls Qt's 'void QCompleterItemDelegate::paint(QPainter *p, const
    QStyleOptionViewItem &opt, const QModelIndex &idx) const'.

    Qt's own words: https://doc.qt.io/qt-6/qcompleteritemdelegate.html#paint

    Parameters
    ----------

    p : Optional[QPainter]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    opt : QStyleOptionViewItem
      Passed on as a value: Qt reads the C++ QStyleOptionViewItem, which
      stays Python's own.

    idx : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.
    """
    #  void QCompleterItemDelegate::paint(QPainter *p, const
    #      QStyleOptionViewItem &opt, const QModelIndex &idx) const
    ritual = (
        'ritual_ZNK22QCompleterItemDelegate5paintEP8QPainterRK20QStyleOptio'
        'nViewItemRK11QModelIndex')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK22QCompleterItemDelegate5paintEP8QPainterRK20QStyl'
          'eOptionViewItemRK11QModelIndex')
    self.uglySide.call(
        ritual, self._addressOf(p), self._valueOf(opt), self._valueOf(idx),
    )
