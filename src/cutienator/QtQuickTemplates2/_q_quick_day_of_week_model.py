"""
QQuickDayOfWeekModel binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickdayofweekmodel_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuickDayOfWeekModel to be private: it declares the class in a
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


class QQuickDayOfWeekModel(QAbstractListModel):
  """
  The cute side of Qt's QQuickDayOfWeekModel: a plain Python object standing
  in front of one C++ QQuickDayOfWeekModel.

  It is built on the cute 'QAbstractListModel', as Qt's QQuickDayOfWeekModel
  is built on Qt's QAbstractListModel, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickDayOfWeekModel that has a ritual and that
  Python can call so far, 5 names in all: 'metaObject', 'roleNames', 'data',
  'rowCount', 'localeChanged'. None can be made from Python: one comes out of
  a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickDayOfWeekModel::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QQuickDayOfWeekModel::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QQuickDayOfWeekModelPrivate *QQuickDayOfWeekModel::d_func()': gives
    'QQuickDayOfWeekModelPrivate', which has no cute class yet.
  - Qt's 'const QQuickDayOfWeekModelPrivate *QQuickDayOfWeekModel::d_func()
    const': gives 'QQuickDayOfWeekModelPrivate', which has no cute class yet.

  What has no ritual
  ------------------

  9 of the 18 functions Qt declares: 3 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file; 2 not a gap;
  2 forbidden; 1 leans on 'QQuickDayOfWeekModel; 1 leans on 'vtable for
  QQuickDayOfWeekModel', which Qt's source does not mark for use from outside
  Qt and has no code for that could be taken.

  What to expect
  --------------

  - The C++ QQuickDayOfWeekModel is created at the first use, not by
    'QQuickDayOfWeekModel(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickDayOfWeekModel.
  - Qt tells when it has removed the C++ QQuickDayOfWeekModel. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQuickDayOfWeekModel that has no cute function yet,
    '__init__', 'dayAt', 'locale', 'setLocale', holds a function that raises
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
  __qt_class__ = 'QQuickDayOfWeekModel'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickDayOfWeekModel::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdayofweekmodel.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickDayOfWeekModel::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK20QQuickDayOfWeekModel10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def roleNames(self) -> QHash[int, QByteArray]:
    """
    Calls Qt's 'QHash<int, QByteArray> QQuickDayOfWeekModel::roleNames()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdayofweekmodel.html#roleNames

    Returns
    -------

    QHash[int, QByteArray]
      A new cute map around the copy Qt gave back. Python owns it.
    """
    #  QHash<int, QByteArray> QQuickDayOfWeekModel::roleNames() const
    address = self.uglySide.call(
        'ritual_ZNK20QQuickDayOfWeekModel9roleNamesEv',
    )
    from ..QtCore import QByteArray
    return QHash[int, QByteArray]._cuteOwning(address)

  @overload(QModelIndex, int)
  def data(self, index: QModelIndex, role: int) -> QVariant:
    """
    Calls Qt's 'QVariant QQuickDayOfWeekModel::data(const QModelIndex &index,
    int role) const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdayofweekmodel.html#data

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
    #  QVariant QQuickDayOfWeekModel::data(const QModelIndex &index, int
    #      role) const
    ritual = 'ritual_ZNK20QQuickDayOfWeekModel4dataERK11QModelIndexi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK20QQuickDayOfWeekModel4dataERK11QModelIndexi'
    address = self.uglySide.call(ritual, self._valueOf(index), role)
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  @overload()
  @overload(QModelIndex)
  def rowCount(self, parent: Optional[QModelIndex] = None) -> int:
    """
    Calls Qt's 'int QQuickDayOfWeekModel::rowCount(const QModelIndex &parent)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdayofweekmodel.html#rowCount

    Parameters
    ----------

    parent : Optional[QModelIndex]
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own. May be left out, as in Qt: a new 'QModelIndex()' is then
      passed on.
    """
    #  int QQuickDayOfWeekModel::rowCount(const QModelIndex &parent) const
    if parent is None:
      from ..QtCore import QModelIndex
      parent = QModelIndex()
    ritual = 'ritual_ZNK20QQuickDayOfWeekModel8rowCountERK11QModelIndex'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK20QQuickDayOfWeekModel8rowCountERK11QModelIndex')
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
    Qt's 'QQuickDayOfWeekModel::QQuickDayOfWeekModel(QObject *parent)': leans
    on 'vtable for QQuickDayOfWeekModel', which Qt's source does not mark for
    use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQuickDayOfWeekModel.__init__' has no cute function yet. Qt's "
        "'QQuickDayOfWeekModel::QQuickDayOfWeekModel(QObject *parent)': "
        "leans on 'vtable for QQuickDayOfWeekModel', which Qt's source does "
        "not mark for use from outside Qt and has no code for that could be "
        "taken.")

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

  def localeChanged(self) -> None:
    """
    Calls Qt's 'void QQuickDayOfWeekModel::localeChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdayofweekmodel.html#localeChanged
    """
    #  void QQuickDayOfWeekModel::localeChanged()
    self.uglySide.call('ritual_ZN20QQuickDayOfWeekModel13localeChangedEv')

  @staticmethod
  def dayAt(*__, **_) -> Never:
    """
    Qt's 'int QQuickDayOfWeekModel::dayAt(int index) const': Qt's library has
    no name for it, and its code in Qt's source does not compile apart from
    its file: member access into incomplete type 'const
    QQuickDayOfWeekModelPrivate'.
    """
    raise NotImplementedError(
        "'QQuickDayOfWeekModel.dayAt' has no cute function yet. Qt's 'int "
        "QQuickDayOfWeekModel::dayAt(int index) const': Qt's library has no "
        "name for it, and its code in Qt's source does not compile apart "
        "from its file: member access into incomplete type 'const "
        "QQuickDayOfWeekModelPrivate'.")

  @staticmethod
  def locale(*__, **_) -> Never:
    """
    Qt's 'QLocale QQuickDayOfWeekModel::locale() const': Qt's library has no
    name for it, and its code in Qt's source does not compile apart from its
    file: member access into incomplete type 'const
    QQuickDayOfWeekModelPrivate'.
    """
    raise NotImplementedError(
        "'QQuickDayOfWeekModel.locale' has no cute function yet. Qt's "
        "'QLocale QQuickDayOfWeekModel::locale() const': Qt's library has "
        "no name for it, and its code in Qt's source does not compile apart "
        "from its file: member access into incomplete type 'const "
        "QQuickDayOfWeekModelPrivate'.")

  @staticmethod
  def setLocale(*__, **_) -> Never:
    """
    Qt's 'void QQuickDayOfWeekModel::setLocale(const QLocale &locale)': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: member access into incomplete type
    'QQuickDayOfWeekModelPrivate'.
    """
    raise NotImplementedError(
        "'QQuickDayOfWeekModel.setLocale' has no cute function yet. Qt's "
        "'void QQuickDayOfWeekModel::setLocale(const QLocale &locale)': "
        "Qt's library has no name for it, and its code in Qt's source does "
        "not compile apart from its file: member access into incomplete "
        "type 'QQuickDayOfWeekModelPrivate'.")
