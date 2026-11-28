"""
QQuickMonthModel binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickmonthmodel_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuickMonthModel to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
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


class QQuickMonthModel(QAbstractListModel):
  """
  The cute side of Qt's QQuickMonthModel: a plain Python object standing in
  front of one C++ QQuickMonthModel.

  It is built on the cute 'QAbstractListModel', as Qt's QQuickMonthModel is
  built on Qt's QAbstractListModel, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickMonthModel that has a ritual and that Python
  can call so far, 8 names in all: 'metaObject', 'roleNames', 'data',
  'rowCount', 'monthChanged', 'yearChanged', 'localeChanged', 'titleChanged'.
  None can be made from Python: one comes out of a function of another class
  that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickMonthModel::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QQuickMonthModel::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QQuickMonthModelPrivate *QQuickMonthModel::d_func()': gives
    'QQuickMonthModelPrivate', which has no cute class yet.
  - Qt's 'const QQuickMonthModelPrivate *QQuickMonthModel::d_func() const':
    gives 'QQuickMonthModelPrivate', which has no cute class yet.

  What has no ritual
  ------------------

  16 of the 28 functions Qt declares: 11 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file; 2 not a gap;
  2 forbidden; 1 leans on 'QQuickMonthModel.

  What to expect
  --------------

  - The C++ QQuickMonthModel is created at the first use, not by
    'QQuickMonthModel(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickMonthModel.
  - Qt tells when it has removed the C++ QQuickMonthModel. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQuickMonthModel that has no cute function yet,
    '__init__', 'dateAt', 'indexOf', 'locale', 'month', 'setLocale',
    'setMonth', 'setTitle', 'setYear', 'title', 'year', holds a function that
    raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickMonthModel'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickMonthModel::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmonthmodel.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickMonthModel::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK16QQuickMonthModel10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def roleNames(self) -> QHash[int, QByteArray]:
    """
    Calls Qt's 'QHash<int, QByteArray> QQuickMonthModel::roleNames() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmonthmodel.html#roleNames

    Returns
    -------

    QHash[int, QByteArray]
      A new cute map around the copy Qt gave back. Python owns it.
    """
    #  QHash<int, QByteArray> QQuickMonthModel::roleNames() const
    address = self.uglySide.call('ritual_ZNK16QQuickMonthModel9roleNamesEv')
    from ..QtCore import QByteArray
    return QHash[int, QByteArray]._cuteOwning(address)

  @overload(QModelIndex, int)
  def data(self, index: QModelIndex, role: int) -> QVariant:
    """
    Calls Qt's 'QVariant QQuickMonthModel::data(const QModelIndex &index, int
    role) const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmonthmodel.html#data

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
    #  QVariant QQuickMonthModel::data(const QModelIndex &index, int role)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK16QQuickMonthModel4dataERK11QModelIndexi',
        self._valueOf(index), role,
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  @overload()
  @overload(QModelIndex)
  def rowCount(self, parent: Optional[QModelIndex] = None) -> int:
    """
    Calls Qt's 'int QQuickMonthModel::rowCount(const QModelIndex &parent)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmonthmodel.html#rowCount

    Parameters
    ----------

    parent : Optional[QModelIndex]
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own. May be left out, as in Qt: a new 'QModelIndex()' is then
      passed on.
    """
    #  int QQuickMonthModel::rowCount(const QModelIndex &parent) const
    if parent is None:
      from ..QtCore import QModelIndex
      parent = QModelIndex()
    return self.uglySide.call(
        'ritual_ZNK16QQuickMonthModel8rowCountERK11QModelIndex',
        self._valueOf(parent),
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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'QQuickMonthModel::QQuickMonthModel(QObject *parent)': Qt's library
    has no name for it, and its code in Qt's source does not compile apart
    from its file: member access into incomplete type
    'QQuickMonthModelPrivate'.
    """
    raise NotImplementedError(
        "'QQuickMonthModel.__init__' has no cute function yet. Qt's "
        "'QQuickMonthModel::QQuickMonthModel(QObject *parent)': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: member access into incomplete type "
        "'QQuickMonthModelPrivate'.")

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
    Calls Qt's 'void QQuickMonthModel::monthChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmonthmodel.html#monthChanged
    """
    #  void QQuickMonthModel::monthChanged()
    self.uglySide.call('ritual_ZN16QQuickMonthModel12monthChangedEv')

  def yearChanged(self) -> None:
    """
    Calls Qt's 'void QQuickMonthModel::yearChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmonthmodel.html#yearChanged
    """
    #  void QQuickMonthModel::yearChanged()
    self.uglySide.call('ritual_ZN16QQuickMonthModel11yearChangedEv')

  def localeChanged(self) -> None:
    """
    Calls Qt's 'void QQuickMonthModel::localeChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmonthmodel.html#localeChanged
    """
    #  void QQuickMonthModel::localeChanged()
    self.uglySide.call('ritual_ZN16QQuickMonthModel13localeChangedEv')

  def titleChanged(self) -> None:
    """
    Calls Qt's 'void QQuickMonthModel::titleChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmonthmodel.html#titleChanged
    """
    #  void QQuickMonthModel::titleChanged()
    self.uglySide.call('ritual_ZN16QQuickMonthModel12titleChangedEv')

  @staticmethod
  def dateAt(*__, **_) -> Never:
    """
    Qt's 'QDateTime QQuickMonthModel::dateAt(int index) const': Qt's library
    has no name for it, and its code in Qt's source does not compile apart
    from its file: member access into incomplete type 'const
    QQuickMonthModelPrivate'.
    """
    raise NotImplementedError(
        "'QQuickMonthModel.dateAt' has no cute function yet. Qt's "
        "'QDateTime QQuickMonthModel::dateAt(int index) const': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: member access into incomplete type "
        "'const QQuickMonthModelPrivate'.")

  @staticmethod
  def indexOf(*__, **_) -> Never:
    """
    Qt's 'int QQuickMonthModel::indexOf(QDateTime date) const': Qt's library
    has no name for it, and its code in Qt's source does not compile apart
    from its file: member access into incomplete type 'const
    QQuickMonthModelPrivate'.
    """
    raise NotImplementedError(
        "'QQuickMonthModel.indexOf' has no cute function yet. Qt's 'int "
        "QQuickMonthModel::indexOf(QDateTime date) const': Qt's library has "
        "no name for it, and its code in Qt's source does not compile apart "
        "from its file: member access into incomplete type 'const "
        "QQuickMonthModelPrivate'.")

  @staticmethod
  def locale(*__, **_) -> Never:
    """
    Qt's 'QLocale QQuickMonthModel::locale() const': Qt's library has no name
    for it, and its code in Qt's source does not compile apart from its file:
    member access into incomplete type 'const QQuickMonthModelPrivate'.
    """
    raise NotImplementedError(
        "'QQuickMonthModel.locale' has no cute function yet. Qt's 'QLocale "
        "QQuickMonthModel::locale() const': Qt's library has no name for "
        "it, and its code in Qt's source does not compile apart from its "
        "file: member access into incomplete type 'const "
        "QQuickMonthModelPrivate'.")

  @staticmethod
  def month(*__, **_) -> Never:
    """
    Qt's 'int QQuickMonthModel::month() const': Qt's library has no name for
    it, and its code in Qt's source does not compile apart from its file:
    member access into incomplete type 'const QQuickMonthModelPrivate'.
    """
    raise NotImplementedError(
        "'QQuickMonthModel.month' has no cute function yet. Qt's 'int "
        "QQuickMonthModel::month() const': Qt's library has no name for it, "
        "and its code in Qt's source does not compile apart from its file: "
        "member access into incomplete type 'const QQuickMonthModelPrivate'."
    )

  @staticmethod
  def setLocale(*__, **_) -> Never:
    """
    Qt's 'void QQuickMonthModel::setLocale(const QLocale &locale)': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: member access into incomplete type
    'QQuickMonthModelPrivate'.
    """
    raise NotImplementedError(
        "'QQuickMonthModel.setLocale' has no cute function yet. Qt's 'void "
        "QQuickMonthModel::setLocale(const QLocale &locale)': Qt's library "
        "has no name for it, and its code in Qt's source does not compile "
        "apart from its file: member access into incomplete type "
        "'QQuickMonthModelPrivate'.")

  @staticmethod
  def setMonth(*__, **_) -> Never:
    """
    Qt's 'void QQuickMonthModel::setMonth(int month)': Qt's library has no
    name for it, and its code in Qt's source does not compile apart from its
    file: member access into incomplete type 'QQuickMonthModelPrivate'.
    """
    raise NotImplementedError(
        "'QQuickMonthModel.setMonth' has no cute function yet. Qt's 'void "
        "QQuickMonthModel::setMonth(int month)': Qt's library has no name "
        "for it, and its code in Qt's source does not compile apart from "
        "its file: member access into incomplete type "
        "'QQuickMonthModelPrivate'.")

  @staticmethod
  def setTitle(*__, **_) -> Never:
    """
    Qt's 'void QQuickMonthModel::setTitle(const QString &title)': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: member access into incomplete type
    'QQuickMonthModelPrivate'.
    """
    raise NotImplementedError(
        "'QQuickMonthModel.setTitle' has no cute function yet. Qt's 'void "
        "QQuickMonthModel::setTitle(const QString &title)': Qt's library "
        "has no name for it, and its code in Qt's source does not compile "
        "apart from its file: member access into incomplete type "
        "'QQuickMonthModelPrivate'.")

  @staticmethod
  def setYear(*__, **_) -> Never:
    """
    Qt's 'void QQuickMonthModel::setYear(int year)': Qt's library has no name
    for it, and its code in Qt's source does not compile apart from its file:
    member access into incomplete type 'QQuickMonthModelPrivate'.
    """
    raise NotImplementedError(
        "'QQuickMonthModel.setYear' has no cute function yet. Qt's 'void "
        "QQuickMonthModel::setYear(int year)': Qt's library has no name for "
        "it, and its code in Qt's source does not compile apart from its "
        "file: member access into incomplete type 'QQuickMonthModelPrivate'."
    )

  @staticmethod
  def title(*__, **_) -> Never:
    """
    Qt's 'QString QQuickMonthModel::title() const': Qt's library has no name
    for it, and its code in Qt's source does not compile apart from its file:
    member access into incomplete type 'const QQuickMonthModelPrivate'.
    """
    raise NotImplementedError(
        "'QQuickMonthModel.title' has no cute function yet. Qt's 'QString "
        "QQuickMonthModel::title() const': Qt's library has no name for it, "
        "and its code in Qt's source does not compile apart from its file: "
        "member access into incomplete type 'const QQuickMonthModelPrivate'."
    )

  @staticmethod
  def year(*__, **_) -> Never:
    """
    Qt's 'int QQuickMonthModel::year() const': Qt's library has no name for
    it, and its code in Qt's source does not compile apart from its file:
    member access into incomplete type 'const QQuickMonthModelPrivate'.
    """
    raise NotImplementedError(
        "'QQuickMonthModel.year' has no cute function yet. Qt's 'int "
        "QQuickMonthModel::year() const': Qt's library has no name for it, "
        "and its code in Qt's source does not compile apart from its file: "
        "member access into incomplete type 'const QQuickMonthModelPrivate'."
    )
