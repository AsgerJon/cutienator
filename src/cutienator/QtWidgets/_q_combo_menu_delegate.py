"""
QComboMenuDelegate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/6.12.0/QtWidgets/private/qcombobox_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QComboMenuDelegate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from . import QAbstractItemDelegate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QAbstractItemModel, QEvent, QMetaObject, QModelIndex
  from ..QtCore import QSize
  from ..QtGui import QPainter
  from . import QStyleOptionViewItem
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QAbstractItemModel = WAIT['QAbstractItemModel']
  QEvent = WAIT['QEvent']
  QModelIndex = WAIT['QModelIndex']
  QPainter = WAIT['QPainter']
  QStyleOptionViewItem = WAIT['QStyleOptionViewItem']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QComboMenuDelegate(QAbstractItemDelegate):
  """
  The cute side of Qt's QComboMenuDelegate: a plain Python object standing in
  front of one C++ QComboMenuDelegate.

  It is built on the cute 'QAbstractItemDelegate', as Qt's QComboMenuDelegate
  is built on Qt's QAbstractItemDelegate, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QComboMenuDelegate that has a ritual and that Python
  can call so far, 4 names in all: 'metaObject', 'paint', 'sizeHint',
  'editorEvent'. None can be made from Python: one comes out of a function of
  another class that gives one back.

  What has no ritual
  ------------------

  10 of the 14 functions Qt declares: 4 leans on 'QComboMenuDelegate; 2 takes
  or gives a type that cannot be passed yet; 2 declared and nowhere to be
  found; 1 a template; 1 Qt's library has no name for it, and its code in
  Qt's source does not compile apart from its file.

  What to expect
  --------------

  - The C++ QComboMenuDelegate is created at the first use, not by
    'QComboMenuDelegate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QComboMenuDelegate.
  - Qt tells when it has removed the C++ QComboMenuDelegate. Every call on
    the cute object, and every use of it as an argument, then raises
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
  __qt_class__ = 'QComboMenuDelegate'

  #  A C++ QComboMenuDelegate Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QComboMenuDelegate'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QComboMenuDelegate::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcombomenudelegate.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QComboMenuDelegate::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK18QComboMenuDelegate10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  @overload(QStyleOptionViewItem, QModelIndex)
  def sizeHint(
      self,
      option: QStyleOptionViewItem,
      index: QModelIndex,
  ) -> QSize:
    """
    Calls Qt's 'QSize QComboMenuDelegate::sizeHint(const QStyleOptionViewItem
    &option, const QModelIndex &index) const'.

    Qt's own words: https://doc.qt.io/qt-6/qcombomenudelegate.html#sizeHint

    Parameters
    ----------

    option : QStyleOptionViewItem
      Passed on as a value: Qt reads the C++ QStyleOptionViewItem, which
      stays Python's own.

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QComboMenuDelegate::sizeHint(const QStyleOptionViewItem &option,
    #      const QModelIndex &index) const
    address = self.uglySide.call(
        'ritual_ZNK18QComboMenuDelegate8sizeHintERK20QStyleOptionViewItemRK'
        '11QModelIndex',
        self._valueOf(option), self._valueOf(index),
    )
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

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
      painter: Optional[QPainter],
      option: QStyleOptionViewItem,
      index: QModelIndex,
  ) -> None:
    """
    Calls Qt's 'void QComboMenuDelegate::paint(QPainter *painter, const
    QStyleOptionViewItem &option, const QModelIndex &index) const'.

    Qt's own words: https://doc.qt.io/qt-6/qcombomenudelegate.html#paint

    Parameters
    ----------

    painter : Optional[QPainter]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    option : QStyleOptionViewItem
      Passed on as a value: Qt reads the C++ QStyleOptionViewItem, which
      stays Python's own.

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.
    """
    #  void QComboMenuDelegate::paint(QPainter *painter, const
    #      QStyleOptionViewItem &option, const QModelIndex &index) const
    self.uglySide.call(
        'ritual_ZNK18QComboMenuDelegate5paintEP8QPainterRK20QStyleOptionVie'
        'wItemRK11QModelIndex',
        self._addressOf(painter), self._valueOf(option),
        self._valueOf(index),
    )

  @overload(QEvent, QAbstractItemModel, QStyleOptionViewItem, QModelIndex)
  @overload(QEvent, NoneType, QStyleOptionViewItem, QModelIndex)
  @overload(NoneType, QAbstractItemModel, QStyleOptionViewItem, QModelIndex)
  @overload(NoneType, NoneType, QStyleOptionViewItem, QModelIndex)
  def editorEvent(
      self,
      event: Optional[QEvent],
      model: Optional[QAbstractItemModel],
      option: QStyleOptionViewItem,
      index: QModelIndex,
  ) -> bool:
    """
    Calls Qt's 'bool QComboMenuDelegate::editorEvent(QEvent *event,
    QAbstractItemModel *model, const QStyleOptionViewItem &option, const
    QModelIndex &index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcombomenudelegate.html#editorEvent

    Parameters
    ----------

    event : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    model : Optional[QAbstractItemModel]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    option : QStyleOptionViewItem
      Passed on as a value: Qt reads the C++ QStyleOptionViewItem, which
      stays Python's own.

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.
    """
    #  bool QComboMenuDelegate::editorEvent(QEvent *event, QAbstractItemModel
    #      *model, const QStyleOptionViewItem &option, const QModelIndex
    #      &index)
    ritual = (
        'ritual_ZN18QComboMenuDelegate11editorEventEP6QEventP18QAbstractIte'
        'mModelRK20QStyleOptionViewItemRK11QModelIndex')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18QComboMenuDelegate11editorEventEP6QEventP18QAbstr'
          'actItemModelRK20QStyleOptionViewItemRK11QModelIndex')
    return self.uglySide.call(
        ritual,
        self._addressOf(event), self._addressOf(model),
        self._valueOf(option), self._valueOf(index),
    )
