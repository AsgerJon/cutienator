"""
QQuickWeekNumberModel binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickweeknumbermodel_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuickWeekNumberModel to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..QtCore import QAbstractListModel, QHash

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QByteArray, QMetaObject, QModelIndex, QVariant
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QModelIndex = WAIT['QModelIndex']


class QQuickWeekNumberModel(QAbstractListModel):
  """
  The cute side of Qt's QQuickWeekNumberModel: a plain Python object standing
  in front of one C++ QQuickWeekNumberModel.

  It is built on the cute 'QAbstractListModel', as Qt's QQuickWeekNumberModel
  is built on Qt's QAbstractListModel, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickWeekNumberModel that has a ritual and that
  Python can call so far, 7 names in all: 'metaObject', 'roleNames', 'data',
  'rowCount', 'monthChanged', 'yearChanged', 'localeChanged'. None can be
  made from Python: one comes out of a function of another class that gives
  one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickWeekNumberModel::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QQuickWeekNumberModel::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QQuickWeekNumberModelPrivate *QQuickWeekNumberModel::d_func()':
    gives 'QQuickWeekNumberModelPrivate', which has no cute class yet.
  - Qt's 'const QQuickWeekNumberModelPrivate *QQuickWeekNumberModel::d_func()
    const': gives 'QQuickWeekNumberModelPrivate', which has no cute class
    yet.

  What has no ritual
  ------------------

  14 of the 25 functions Qt declares: 8 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file; 2 not a gap;
  2 forbidden; 1 leans on 'QQuickWeekNumberModel; 1 leans on 'vtable for
  QQuickWeekNumberModel', which Qt's source does not mark for use from
  outside Qt and has no code for that could be taken.

  What to expect
  --------------

  - The C++ QQuickWeekNumberModel is created at the first use, not by
    'QQuickWeekNumberModel(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickWeekNumberModel.
  - Qt tells when it has removed the C++ QQuickWeekNumberModel. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQuickWeekNumberModel that has no cute function yet,
    '__init__', 'indexOf', 'locale', 'month', 'setLocale', 'setMonth',
    'setYear', 'weekNumberAt', 'year', holds a function that raises
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
  __qt_class__ = 'QQuickWeekNumberModel'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickWeekNumberModel::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickweeknumbermodel.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickWeekNumberModel::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK21QQuickWeekNumberModel10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def roleNames(self) -> QHash[int, QByteArray]:
    """
    Calls Qt's 'QHash<int, QByteArray> QQuickWeekNumberModel::roleNames()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickweeknumbermodel.html#roleNames

    Returns
    -------

    QHash[int, QByteArray]
      A new cute map around the copy Qt gave back. Python owns it.
    """
    #  QHash<int, QByteArray> QQuickWeekNumberModel::roleNames() const
    address = self.uglySide.call(
        'ritual_ZNK21QQuickWeekNumberModel9roleNamesEv',
    )
    from ..QtCore import QByteArray
    return QHash[int, QByteArray]._cuteOwning(address)

  @overload(QModelIndex, int)
  def data(self, index: QModelIndex, role: int) -> QVariant:
    """
    Calls Qt's 'QVariant QQuickWeekNumberModel::data(const QModelIndex
    &index, int role) const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickweeknumbermodel.html#data

    Parameters
    ----------

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    role : int
      Passed on as it is.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QQuickWeekNumberModel::data(const QModelIndex &index, int
    #      role) const
    ritual = 'ritual_ZNK21QQuickWeekNumberModel4dataERK11QModelIndexi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK21QQuickWeekNumberModel4dataERK11QModelIndexi'
    address = self.uglySide.call(ritual, self._valueOf(index), role)
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  @overload()
  @overload(QModelIndex)
  def rowCount(self, parent: Optional[QModelIndex] = None) -> int:
    """
    Calls Qt's 'int QQuickWeekNumberModel::rowCount(const QModelIndex
    &parent) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickweeknumbermodel.html#rowCount

    Parameters
    ----------

    parent : Optional[QModelIndex]
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own. May be left out, as in Qt: a new 'QModelIndex()' is then
      passed on.
    """
    #  int QQuickWeekNumberModel::rowCount(const QModelIndex &parent) const
    if parent is None:
      from ..QtCore import QModelIndex
      parent = QModelIndex()
    ritual = 'ritual_ZNK21QQuickWeekNumberModel8rowCountERK11QModelIndex'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK21QQuickWeekNumberModel8rowCountERK11QModelIndex')
    return self.uglySide.call(ritual, self._valueOf(parent))

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
    Qt's 'QQuickWeekNumberModel::QQuickWeekNumberModel(QObject *parent)':
    leans on 'vtable for QQuickWeekNumberModel', which Qt's source does not
    mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQuickWeekNumberModel.__init__' has no cute function yet. Qt's "
        "'QQuickWeekNumberModel::QQuickWeekNumberModel(QObject *parent)': "
        "leans on 'vtable for QQuickWeekNumberModel', which Qt's source "
        "does not mark for use from outside Qt and has no code for that "
        "could be taken.")

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

  def monthChanged(self) -> None:
    """
    Calls Qt's 'void QQuickWeekNumberModel::monthChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickweeknumbermodel.html#monthChanged
    """
    #  void QQuickWeekNumberModel::monthChanged()
    self.uglySide.call('ritual_ZN21QQuickWeekNumberModel12monthChangedEv')

  def yearChanged(self) -> None:
    """
    Calls Qt's 'void QQuickWeekNumberModel::yearChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickweeknumbermodel.html#yearChanged
    """
    #  void QQuickWeekNumberModel::yearChanged()
    self.uglySide.call('ritual_ZN21QQuickWeekNumberModel11yearChangedEv')

  def localeChanged(self) -> None:
    """
    Calls Qt's 'void QQuickWeekNumberModel::localeChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickweeknumbermodel.html#localeChanged
    """
    #  void QQuickWeekNumberModel::localeChanged()
    self.uglySide.call('ritual_ZN21QQuickWeekNumberModel13localeChangedEv')

  @staticmethod
  def indexOf(*__, **_) -> Never:
    """
    Qt's 'int QQuickWeekNumberModel::indexOf(int weekNumber) const': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: member access into incomplete type 'const
    QQuickWeekNumberModelPrivate'.
    """
    raise NotImplementedError(
        "'QQuickWeekNumberModel.indexOf' has no cute function yet. Qt's "
        "'int QQuickWeekNumberModel::indexOf(int weekNumber) const': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: member access into incomplete type "
        "'const QQuickWeekNumberModelPrivate'.")

  @staticmethod
  def locale(*__, **_) -> Never:
    """
    Qt's 'QLocale QQuickWeekNumberModel::locale() const': Qt's library has no
    name for it, and its code in Qt's source does not compile apart from its
    file: member access into incomplete type 'const
    QQuickWeekNumberModelPrivate'.
    """
    raise NotImplementedError(
        "'QQuickWeekNumberModel.locale' has no cute function yet. Qt's "
        "'QLocale QQuickWeekNumberModel::locale() const': Qt's library has "
        "no name for it, and its code in Qt's source does not compile apart "
        "from its file: member access into incomplete type 'const "
        "QQuickWeekNumberModelPrivate'.")

  @staticmethod
  def month(*__, **_) -> Never:
    """
    Qt's 'int QQuickWeekNumberModel::month() const': Qt's library has no name
    for it, and its code in Qt's source does not compile apart from its file:
    member access into incomplete type 'const QQuickWeekNumberModelPrivate'.
    """
    raise NotImplementedError(
        "'QQuickWeekNumberModel.month' has no cute function yet. Qt's 'int "
        "QQuickWeekNumberModel::month() const': Qt's library has no name "
        "for it, and its code in Qt's source does not compile apart from "
        "its file: member access into incomplete type 'const "
        "QQuickWeekNumberModelPrivate'.")

  @staticmethod
  def setLocale(*__, **_) -> Never:
    """
    Qt's 'void QQuickWeekNumberModel::setLocale(const QLocale &locale)': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: member access into incomplete type
    'QQuickWeekNumberModelPrivate'.
    """
    raise NotImplementedError(
        "'QQuickWeekNumberModel.setLocale' has no cute function yet. Qt's "
        "'void QQuickWeekNumberModel::setLocale(const QLocale &locale)': "
        "Qt's library has no name for it, and its code in Qt's source does "
        "not compile apart from its file: member access into incomplete "
        "type 'QQuickWeekNumberModelPrivate'.")

  @staticmethod
  def setMonth(*__, **_) -> Never:
    """
    Qt's 'void QQuickWeekNumberModel::setMonth(int month)': Qt's library has
    no name for it, and its code in Qt's source does not compile apart from
    its file: member access into incomplete type
    'QQuickWeekNumberModelPrivate'.
    """
    raise NotImplementedError(
        "'QQuickWeekNumberModel.setMonth' has no cute function yet. Qt's "
        "'void QQuickWeekNumberModel::setMonth(int month)': Qt's library "
        "has no name for it, and its code in Qt's source does not compile "
        "apart from its file: member access into incomplete type "
        "'QQuickWeekNumberModelPrivate'.")

  @staticmethod
  def setYear(*__, **_) -> Never:
    """
    Qt's 'void QQuickWeekNumberModel::setYear(int year)': Qt's library has no
    name for it, and its code in Qt's source does not compile apart from its
    file: member access into incomplete type 'QQuickWeekNumberModelPrivate'.
    """
    raise NotImplementedError(
        "'QQuickWeekNumberModel.setYear' has no cute function yet. Qt's "
        "'void QQuickWeekNumberModel::setYear(int year)': Qt's library has "
        "no name for it, and its code in Qt's source does not compile apart "
        "from its file: member access into incomplete type "
        "'QQuickWeekNumberModelPrivate'.")

  @staticmethod
  def weekNumberAt(*__, **_) -> Never:
    """
    Qt's 'int QQuickWeekNumberModel::weekNumberAt(int index) const': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: member access into incomplete type 'const
    QQuickWeekNumberModelPrivate'.
    """
    raise NotImplementedError(
        "'QQuickWeekNumberModel.weekNumberAt' has no cute function yet. "
        "Qt's 'int QQuickWeekNumberModel::weekNumberAt(int index) const': "
        "Qt's library has no name for it, and its code in Qt's source does "
        "not compile apart from its file: member access into incomplete "
        "type 'const QQuickWeekNumberModelPrivate'.")

  @staticmethod
  def year(*__, **_) -> Never:
    """
    Qt's 'int QQuickWeekNumberModel::year() const': Qt's library has no name
    for it, and its code in Qt's source does not compile apart from its file:
    member access into incomplete type 'const QQuickWeekNumberModelPrivate'.
    """
    raise NotImplementedError(
        "'QQuickWeekNumberModel.year' has no cute function yet. Qt's 'int "
        "QQuickWeekNumberModel::year() const': Qt's library has no name for "
        "it, and its code in Qt's source does not compile apart from its "
        "file: member access into incomplete type 'const "
        "QQuickWeekNumberModelPrivate'.")
