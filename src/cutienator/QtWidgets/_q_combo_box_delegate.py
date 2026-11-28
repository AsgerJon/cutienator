"""
QComboBoxDelegate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/6.12.0/QtWidgets/private/qcombobox_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QComboBoxDelegate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from . import QStyledItemDelegate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QAbstractItemModel, QMetaObject, QModelIndex, QSize
  from ..QtGui import QPainter
  from . import QStyleOptionViewItem
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QAbstractItemModel = WAIT['QAbstractItemModel']
  QModelIndex = WAIT['QModelIndex']
  QPainter = WAIT['QPainter']
  QStyleOptionViewItem = WAIT['QStyleOptionViewItem']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QComboBoxDelegate(QStyledItemDelegate):
  """
  The cute side of Qt's QComboBoxDelegate: a plain Python object standing in
  front of one C++ QComboBoxDelegate.

  It is built on the cute 'QStyledItemDelegate', as Qt's QComboBoxDelegate is
  built on Qt's QStyledItemDelegate, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QComboBoxDelegate that has a ritual and that Python
  can call so far, 5 names in all: 'metaObject', 'isSeparator',
  'setSeparator', 'paint', 'sizeHint'. None can be made from Python: one
  comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QComboBoxDelegate::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QComboBoxDelegate::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QComboBoxDelegate::~QComboBoxDelegate()': the destructor: Python
    never removes a C++ QComboBoxDelegate.

  What has no ritual
  ------------------

  4 of the 12 functions Qt declares: 2 not a gap; 2 leans on
  'QComboBoxDelegate.

  What to expect
  --------------

  - The C++ QComboBoxDelegate is created at the first use, not by
    'QComboBoxDelegate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QComboBoxDelegate.
  - Qt tells when it has removed the C++ QComboBoxDelegate. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QComboBoxDelegate that has no cute function yet,
    '__init__', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QModelIndex)
  def isSeparator(index: QModelIndex) -> bool:
    """
    Calls Qt's 'bool QComboBoxDelegate::isSeparator(const QModelIndex
    &index)'.

    Qt's own words: https://doc.qt.io/qt-6/qcomboboxdelegate.html#isSeparator

    Parameters
    ----------

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.
    """
    #  bool QComboBoxDelegate::isSeparator(const QModelIndex &index)
    return Rituals.call(
        'ritual_ZN17QComboBoxDelegate11isSeparatorERK11QModelIndex',
        CuteMixin._valueOf(index),
    )

  @staticmethod
  @overload(QAbstractItemModel, QModelIndex)
  @overload(NoneType, QModelIndex)
  def setSeparator(
      model: Optional[QAbstractItemModel],
      index: QModelIndex,
  ) -> None:
    """
    Calls Qt's 'void QComboBoxDelegate::setSeparator(QAbstractItemModel
    *model, const QModelIndex &index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcomboboxdelegate.html#setSeparator

    Parameters
    ----------

    model : Optional[QAbstractItemModel]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.
    """
    #  void QComboBoxDelegate::setSeparator(QAbstractItemModel *model, const
    #      QModelIndex &index)
    Rituals.call(
        'ritual_ZN17QComboBoxDelegate12setSeparatorEP18QAbstractItemModelRK'
        '11QModelIndex',
        CuteMixin._addressOf(model), CuteMixin._valueOf(index),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QComboBoxDelegate'

  #  A C++ QComboBoxDelegate Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QComboBoxDelegate'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QComboBoxDelegate::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcomboboxdelegate.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QComboBoxDelegate::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK17QComboBoxDelegate10metaObjectEv',
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
    Calls Qt's 'QSize QComboBoxDelegate::sizeHint(const QStyleOptionViewItem
    &option, const QModelIndex &index) const'.

    Qt's own words: https://doc.qt.io/qt-6/qcomboboxdelegate.html#sizeHint

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
    #  QSize QComboBoxDelegate::sizeHint(const QStyleOptionViewItem &option,
    #      const QModelIndex &index) const
    ritual = (
        'ritual_ZNK17QComboBoxDelegate8sizeHintERK20QStyleOptionViewItemRK1'
        '1QModelIndex')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK17QComboBoxDelegate8sizeHintERK20QStyleOptionViewI'
          'temRK11QModelIndex')
    address = self.uglySide.call(
        ritual, self._valueOf(option), self._valueOf(index),
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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'QComboBoxDelegate::QComboBoxDelegate(QObject *parent, QComboBox
    *cmb)': leans on 'QComboBoxDelegate::qt_metacall(QMetaObject::Call, int,
    void**)', which Qt's source does not mark for use from outside Qt and has
    no code for that could be taken.
    """
    raise NotImplementedError(
        "'QComboBoxDelegate.__init__' has no cute function yet. Qt's "
        "'QComboBoxDelegate::QComboBoxDelegate(QObject *parent, QComboBox "
        "*cmb)': leans on "
        "'QComboBoxDelegate::qt_metacall(QMetaObject::Call, int, void**)', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")

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
    Calls Qt's 'void QComboBoxDelegate::paint(QPainter *painter, const
    QStyleOptionViewItem &option, const QModelIndex &index) const'.

    Qt's own words: https://doc.qt.io/qt-6/qcomboboxdelegate.html#paint

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
    #  void QComboBoxDelegate::paint(QPainter *painter, const
    #      QStyleOptionViewItem &option, const QModelIndex &index) const
    ritual = (
        'ritual_ZNK17QComboBoxDelegate5paintEP8QPainterRK20QStyleOptionView'
        'ItemRK11QModelIndex')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK17QComboBoxDelegate5paintEP8QPainterRK20QStyleOpti'
          'onViewItemRK11QModelIndex')
    self.uglySide.call(
        ritual,
        self._addressOf(painter), self._valueOf(option),
        self._valueOf(index),
    )
