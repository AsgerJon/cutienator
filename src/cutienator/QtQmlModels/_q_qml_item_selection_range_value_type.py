"""
QQmlItemSelectionRangeValueType binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQmlModels/6.12.0/QtQmlModels/private/qqmlmodelindexvaluetype_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QQmlItemSelectionRangeValueType to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QAbstractItemModel, QItemSelectionRange, QModelIndex
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QItemSelectionRange = WAIT['QItemSelectionRange']
  QModelIndex = WAIT['QModelIndex']


class QQmlItemSelectionRangeValueType(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQmlItemSelectionRangeValueType: a plain Python
  object standing in front of one C++ QQmlItemSelectionRangeValueType.

  C++ hands a QQmlItemSelectionRangeValueType around as a copy, so every C++
  QQmlItemSelectionRangeValueType behind a cute one is Python's own: it is
  removed, by the ritual named in '__delete_ritual__', when the cute object
  goes.

  What exists
  -----------

  Every function of Qt's QQmlItemSelectionRangeValueType that has a ritual
  and that Python can call so far, 14 names in all: 'toString', 'contains',
  'intersects', 'intersected', 'top', 'left', 'bottom', 'right', 'width',
  'height', 'parent', 'model', 'isValid', 'isEmpty'. None can be made from
  Python: one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void QQmlItemSelectionRangeValueType::qt_qmlMarker_anonymous()':
    one of Qt's own inner workings.
  - Qt's 'void QQmlItemSelectionRangeValueType::qt_qmlMarker_extended()': one
    of Qt's own inner workings.
  - Qt's 'void QQmlItemSelectionRangeValueType::qt_qmlMarker_foreign()': one
    of Qt's own inner workings.
  - Qt's 'QPersistentModelIndex &QQmlItemSelectionRangeValueType::topLeft()
    const': gives a type Python has no way to take yet.
  - Qt's 'QPersistentModelIndex
    &QQmlItemSelectionRangeValueType::bottomRight() const': gives a type
    Python has no way to take yet.
  - Qt's 'QItemSelectionRange QQmlItemSelectionRangeValueType::operator
    QItemSelectionRange() const': an operator Python has no name for.
  - Qt's
    'QQmlItemSelectionRangeValueType::~QQmlItemSelectionRangeValueType()':
    the destructor: Python removes its C++ QQmlItemSelectionRangeValueType by
    it, and has no other use for it.

  What has no ritual
  ------------------

  3 of the 25 functions Qt declares: 3 not a gap.

  What to expect
  --------------

  - The C++ QQmlItemSelectionRangeValueType is created at the first use, not
    by 'QQmlItemSelectionRangeValueType(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QQmlItemSelectionRangeValueType back gives a copy the
    ritual made for Python, in a new cute QQmlItemSelectionRangeValueType.
  - Each name of Qt's QQmlItemSelectionRangeValueType that has no cute
    function yet, 'bottomRight', 'topLeft', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlItemSelectionRangeValueType'

  #  Qt's '~QQmlItemSelectionRangeValueType()'. Naming it makes this a value
  #  class: Python owns every C++ QQmlItemSelectionRangeValueType behind a
  #  cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN31QQmlItemSelectionRangeValueTypeD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def toString(self) -> str:
    """
    Calls Qt's 'QString QQmlItemSelectionRangeValueType::toString() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlitemselectionrangevaluetype.html#toString

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlItemSelectionRangeValueType::toString() const
    return self.uglySide.call(
        'ritual_ZNK31QQmlItemSelectionRangeValueType8toStringEv',
    )

  @overload(QModelIndex)
  def contains(self, index: QModelIndex) -> bool:
    """
    Calls Qt's 'bool QQmlItemSelectionRangeValueType::contains(const
    QModelIndex &index) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlitemselectionrangevaluetype.html#contains

    Parameters
    ----------

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.
    """
    #  bool QQmlItemSelectionRangeValueType::contains(const QModelIndex
    #      &index) const
    return self.uglySide.call(
        'ritual_ZNK31QQmlItemSelectionRangeValueType8containsERK11QModelInd'
        'ex',
        self._valueOf(index),
    )

  @overload(int, int, QModelIndex)
  def contains(
      self,
      row: int,
      column: int,
      parentIndex: QModelIndex,
  ) -> bool:
    """
    Calls Qt's 'bool QQmlItemSelectionRangeValueType::contains(int row, int
    column, const QModelIndex &parentIndex) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlitemselectionrangevaluetype.html#contains

    Parameters
    ----------

    row : int
      Passed on as it is.

    column : int
      Passed on as it is.

    parentIndex : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.
    """
    #  bool QQmlItemSelectionRangeValueType::contains(int row, int column,
    #      const QModelIndex &parentIndex) const
    return self.uglySide.call(
        'ritual_ZNK31QQmlItemSelectionRangeValueType8containsEiiRK11QModelI'
        'ndex',
        row, column, self._valueOf(parentIndex),
    )

  @overload(QItemSelectionRange)
  def intersects(self, other: QItemSelectionRange) -> bool:
    """
    Calls Qt's 'bool QQmlItemSelectionRangeValueType::intersects(const
    QItemSelectionRange &other) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlitemselectionrangevaluetype.html#intersects

    Parameters
    ----------

    other : QItemSelectionRange
      Passed on as a value: Qt reads the C++ QItemSelectionRange, which stays
      Python's own.
    """
    #  bool QQmlItemSelectionRangeValueType::intersects(const
    #      QItemSelectionRange &other) const
    return self.uglySide.call(
        'ritual_ZNK31QQmlItemSelectionRangeValueType10intersectsERK19QItemS'
        'electionRange',
        self._valueOf(other),
    )

  @overload(QItemSelectionRange)
  def intersected(self, other: QItemSelectionRange) -> QItemSelectionRange:
    """
    Calls Qt's 'QItemSelectionRange
    QQmlItemSelectionRangeValueType::intersected(const QItemSelectionRange
    &other) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlitemselectionrangevaluetype.html#intersected

    Parameters
    ----------

    other : QItemSelectionRange
      Passed on as a value: Qt reads the C++ QItemSelectionRange, which stays
      Python's own.

    Returns
    -------

    QItemSelectionRange
      A new cute QItemSelectionRange around the copy Qt gave back. Python
      owns it.
    """
    #  QItemSelectionRange QQmlItemSelectionRangeValueType::intersected(const
    #      QItemSelectionRange &other) const
    address = self.uglySide.call(
        'ritual_ZNK31QQmlItemSelectionRangeValueType11intersectedERK19QItem'
        'SelectionRange',
        self._valueOf(other),
    )
    from ..QtCore import QItemSelectionRange
    return QItemSelectionRange._cuteOwning(address)

  def top(self) -> int:
    """
    Calls Qt's 'int QQmlItemSelectionRangeValueType::top() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlitemselectionrangevaluetype.html#top
    """
    #  int QQmlItemSelectionRangeValueType::top() const
    return self.uglySide.call(
        'ritual_ZNK31QQmlItemSelectionRangeValueType3topEv',
    )

  def left(self) -> int:
    """
    Calls Qt's 'int QQmlItemSelectionRangeValueType::left() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlitemselectionrangevaluetype.html#left
    """
    #  int QQmlItemSelectionRangeValueType::left() const
    return self.uglySide.call(
        'ritual_ZNK31QQmlItemSelectionRangeValueType4leftEv',
    )

  def bottom(self) -> int:
    """
    Calls Qt's 'int QQmlItemSelectionRangeValueType::bottom() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlitemselectionrangevaluetype.html#bottom
    """
    #  int QQmlItemSelectionRangeValueType::bottom() const
    return self.uglySide.call(
        'ritual_ZNK31QQmlItemSelectionRangeValueType6bottomEv',
    )

  def right(self) -> int:
    """
    Calls Qt's 'int QQmlItemSelectionRangeValueType::right() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlitemselectionrangevaluetype.html#right
    """
    #  int QQmlItemSelectionRangeValueType::right() const
    return self.uglySide.call(
        'ritual_ZNK31QQmlItemSelectionRangeValueType5rightEv',
    )

  def width(self) -> int:
    """
    Calls Qt's 'int QQmlItemSelectionRangeValueType::width() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlitemselectionrangevaluetype.html#width
    """
    #  int QQmlItemSelectionRangeValueType::width() const
    return self.uglySide.call(
        'ritual_ZNK31QQmlItemSelectionRangeValueType5widthEv',
    )

  def height(self) -> int:
    """
    Calls Qt's 'int QQmlItemSelectionRangeValueType::height() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlitemselectionrangevaluetype.html#height
    """
    #  int QQmlItemSelectionRangeValueType::height() const
    return self.uglySide.call(
        'ritual_ZNK31QQmlItemSelectionRangeValueType6heightEv',
    )

  def parent(self) -> QModelIndex:
    """
    Calls Qt's 'QModelIndex QQmlItemSelectionRangeValueType::parent() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlitemselectionrangevaluetype.html#parent

    Returns
    -------

    QModelIndex
      A new cute QModelIndex around the copy Qt gave back. Python owns it.
    """
    #  QModelIndex QQmlItemSelectionRangeValueType::parent() const
    address = self.uglySide.call(
        'ritual_ZNK31QQmlItemSelectionRangeValueType6parentEv',
    )
    from ..QtCore import QModelIndex
    return QModelIndex._cuteOwning(address)

  def model(self) -> Optional[QAbstractItemModel]:
    """
    Calls Qt's 'QAbstractItemModel *QQmlItemSelectionRangeValueType::model()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlitemselectionrangevaluetype.html#model

    Returns
    -------

    Optional[QAbstractItemModel]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractItemModel *QQmlItemSelectionRangeValueType::model() const
    address = self.uglySide.call(
        'ritual_ZNK31QQmlItemSelectionRangeValueType5modelEv',
    )
    from ..QtCore import QAbstractItemModel
    return QAbstractItemModel._cuteAt(address)

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool QQmlItemSelectionRangeValueType::isValid() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlitemselectionrangevaluetype.html#isValid
    """
    #  bool QQmlItemSelectionRangeValueType::isValid() const
    return self.uglySide.call(
        'ritual_ZNK31QQmlItemSelectionRangeValueType7isValidEv',
    )

  def isEmpty(self) -> bool:
    """
    Calls Qt's 'bool QQmlItemSelectionRangeValueType::isEmpty() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlitemselectionrangevaluetype.html#isEmpty
    """
    #  bool QQmlItemSelectionRangeValueType::isEmpty() const
    return self.uglySide.call(
        'ritual_ZNK31QQmlItemSelectionRangeValueType7isEmptyEv',
    )

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

  @staticmethod
  def bottomRight(*__, **_) -> Never:
    """
    Qt's 'QPersistentModelIndex
    &QQmlItemSelectionRangeValueType::bottomRight() const': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QQmlItemSelectionRangeValueType.bottomRight' has no cute function "
        "yet. Qt's 'QPersistentModelIndex "
        "&QQmlItemSelectionRangeValueType::bottomRight() const': gives a "
        "type Python has no way to take yet.")

  @staticmethod
  def topLeft(*__, **_) -> Never:
    """
    Qt's 'QPersistentModelIndex &QQmlItemSelectionRangeValueType::topLeft()
    const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QQmlItemSelectionRangeValueType.topLeft' has no cute function "
        "yet. Qt's 'QPersistentModelIndex "
        "&QQmlItemSelectionRangeValueType::topLeft() const': gives a type "
        "Python has no way to take yet.")
