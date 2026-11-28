"""
QQuickCalendarModel binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickcalendarmodel_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuickCalendarModel to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..QtCore import QAbstractListModel, QHash
from ..QtQml import QQmlParserStatus

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QByteArray, QMetaObject, QModelIndex, QVariant
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QModelIndex = WAIT['QModelIndex']


class QQuickCalendarModel(QAbstractListModel, QQmlParserStatus):
  """
  The cute side of Qt's QQuickCalendarModel: a plain Python object standing
  in front of one C++ QQuickCalendarModel.

  It is built on the cute 'QAbstractListModel', as Qt's QQuickCalendarModel
  is built on Qt's QAbstractListModel, and has everything that class has. It
  is built on the cute 'QQmlParserStatus' as well, as Qt's
  QQuickCalendarModel is built on Qt's QQmlParserStatus too, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickCalendarModel that has a ritual and that
  Python can call so far, 10 names in all: 'metaObject', 'indexOf',
  'roleNames', 'data', 'rowCount', 'fromChanged', 'toChanged',
  'countChanged', 'classBegin', 'componentComplete'. None can be made from
  Python: one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickCalendarModel::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QQuickCalendarModel::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QQuickCalendarModelPrivate *QQuickCalendarModel::d_func()': gives
    'QQuickCalendarModelPrivate', which has no cute class yet.
  - Qt's 'const QQuickCalendarModelPrivate *QQuickCalendarModel::d_func()
    const': gives 'QQuickCalendarModelPrivate', which has no cute class yet.

  What has no ritual
  ------------------

  13 of the 27 functions Qt declares: 7 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file; 2 not a gap;
  2 forbidden; 1 leans on 'QQuickCalendarModel; 1 leans on 'vtable for
  QQuickCalendarModel', which Qt's source does not mark for use from outside
  Qt and has no code for that could be taken.

  What to expect
  --------------

  - The C++ QQuickCalendarModel is created at the first use, not by
    'QQuickCalendarModel(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickCalendarModel.
  - Qt tells when it has removed the C++ QQuickCalendarModel. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQuickCalendarModel that has no cute function yet,
    '__init__', 'from_', 'monthAt', 'setFrom', 'setTo', 'to', 'yearAt', holds
    a function that raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickCalendarModel'

  #  Qt's QQuickCalendarModel is built on more than one class. The part of a
  #  C++ QQuickCalendarModel that belongs to a class after the first begins
  #  somewhere inside the object, and the ritual named for that class gives
  #  where; see 'CuteMixin._addressAs'.
  __cast_rituals__ = {
      'QQmlParserStatus': 'ritual_cast_QQuickCalendarModel_QQmlParserStatus',
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickCalendarModel::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcalendarmodel.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickCalendarModel::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK19QQuickCalendarModel10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  @overload(int, int)
  def indexOf(self, year: int, month: int) -> int:
    """
    Calls Qt's 'int QQuickCalendarModel::indexOf(int year, int month) const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcalendarmodel.html#indexOf

    Parameters
    ----------

    year : int
      Passed on as it is.

    month : int
      Passed on as it is.
    """
    #  int QQuickCalendarModel::indexOf(int year, int month) const
    return self.uglySide.call(
        'ritual_ZNK19QQuickCalendarModel7indexOfEii', year, month,
    )

  def roleNames(self) -> QHash[int, QByteArray]:
    """
    Calls Qt's 'QHash<int, QByteArray> QQuickCalendarModel::roleNames()
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcalendarmodel.html#roleNames

    Returns
    -------

    QHash[int, QByteArray]
      A new cute map around the copy Qt gave back. Python owns it.
    """
    #  QHash<int, QByteArray> QQuickCalendarModel::roleNames() const
    address = self.uglySide.call(
        'ritual_ZNK19QQuickCalendarModel9roleNamesEv',
    )
    from ..QtCore import QByteArray
    return QHash[int, QByteArray]._cuteOwning(address)

  @overload(QModelIndex, int)
  def data(self, index: QModelIndex, role: int) -> QVariant:
    """
    Calls Qt's 'QVariant QQuickCalendarModel::data(const QModelIndex &index,
    int role) const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcalendarmodel.html#data

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
    #  QVariant QQuickCalendarModel::data(const QModelIndex &index, int role)
    #      const
    ritual = 'ritual_ZNK19QQuickCalendarModel4dataERK11QModelIndexi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK19QQuickCalendarModel4dataERK11QModelIndexi'
    address = self.uglySide.call(ritual, self._valueOf(index), role)
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  @overload()
  @overload(QModelIndex)
  def rowCount(self, parent: Optional[QModelIndex] = None) -> int:
    """
    Calls Qt's 'int QQuickCalendarModel::rowCount(const QModelIndex &parent)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcalendarmodel.html#rowCount

    Parameters
    ----------

    parent : Optional[QModelIndex]
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own. May be left out, as in Qt: a new 'QModelIndex()' is then
      passed on.
    """
    #  int QQuickCalendarModel::rowCount(const QModelIndex &parent) const
    if parent is None:
      from ..QtCore import QModelIndex
      parent = QModelIndex()
    ritual = 'ritual_ZNK19QQuickCalendarModel8rowCountERK11QModelIndex'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK19QQuickCalendarModel8rowCountERK11QModelIndex'
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
    Qt's 'QQuickCalendarModel::QQuickCalendarModel(QObject *parent)': leans
    on 'vtable for QQuickCalendarModel', which Qt's source does not mark for
    use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQuickCalendarModel.__init__' has no cute function yet. Qt's "
        "'QQuickCalendarModel::QQuickCalendarModel(QObject *parent)': leans "
        "on 'vtable for QQuickCalendarModel', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
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

  def fromChanged(self) -> None:
    """
    Calls Qt's 'void QQuickCalendarModel::fromChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcalendarmodel.html#fromChanged
    """
    #  void QQuickCalendarModel::fromChanged()
    self.uglySide.call('ritual_ZN19QQuickCalendarModel11fromChangedEv')

  def toChanged(self) -> None:
    """
    Calls Qt's 'void QQuickCalendarModel::toChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcalendarmodel.html#toChanged
    """
    #  void QQuickCalendarModel::toChanged()
    self.uglySide.call('ritual_ZN19QQuickCalendarModel9toChangedEv')

  def countChanged(self) -> None:
    """
    Calls Qt's 'void QQuickCalendarModel::countChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcalendarmodel.html#countChanged
    """
    #  void QQuickCalendarModel::countChanged()
    self.uglySide.call('ritual_ZN19QQuickCalendarModel12countChangedEv')

  def classBegin(self) -> None:
    """
    Calls Qt's 'void QQuickCalendarModel::classBegin()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcalendarmodel.html#classBegin
    """
    #  void QQuickCalendarModel::classBegin()
    ritual = 'ritual_ZN19QQuickCalendarModel10classBeginEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QQuickCalendarModel10classBeginEv'
    self.uglySide.call(ritual)

  def componentComplete(self) -> None:
    """
    Calls Qt's 'void QQuickCalendarModel::componentComplete()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcalendarmodel.html#componentComplete
    """
    #  void QQuickCalendarModel::componentComplete()
    self.uglySide.call('ritual_ZN19QQuickCalendarModel17componentCompleteEv')

  @staticmethod
  def from_(*__, **_) -> Never:
    """
    Qt's 'QDate QQuickCalendarModel::from() const': Qt's library has no name
    for it, and its code in Qt's source does not compile apart from its file:
    member access into incomplete type 'const QQuickCalendarModelPrivate'.
    """
    raise NotImplementedError(
        "'QQuickCalendarModel.from_' has no cute function yet. Qt's 'QDate "
        "QQuickCalendarModel::from() const': Qt's library has no name for "
        "it, and its code in Qt's source does not compile apart from its "
        "file: member access into incomplete type 'const "
        "QQuickCalendarModelPrivate'.")

  @staticmethod
  def monthAt(*__, **_) -> Never:
    """
    Qt's 'int QQuickCalendarModel::monthAt(int index) const': Qt's library
    has no name for it, and its code in Qt's source does not compile apart
    from its file: member access into incomplete type 'const
    QQuickCalendarModelPrivate'.
    """
    raise NotImplementedError(
        "'QQuickCalendarModel.monthAt' has no cute function yet. Qt's 'int "
        "QQuickCalendarModel::monthAt(int index) const': Qt's library has "
        "no name for it, and its code in Qt's source does not compile apart "
        "from its file: member access into incomplete type 'const "
        "QQuickCalendarModelPrivate'.")

  @staticmethod
  def setFrom(*__, **_) -> Never:
    """
    Qt's 'void QQuickCalendarModel::setFrom(QDate from)': Qt's library has no
    name for it, and its code in Qt's source does not compile apart from its
    file: member access into incomplete type 'QQuickCalendarModelPrivate'.
    """
    raise NotImplementedError(
        "'QQuickCalendarModel.setFrom' has no cute function yet. Qt's 'void "
        "QQuickCalendarModel::setFrom(QDate from)': Qt's library has no "
        "name for it, and its code in Qt's source does not compile apart "
        "from its file: member access into incomplete type "
        "'QQuickCalendarModelPrivate'.")

  @staticmethod
  def setTo(*__, **_) -> Never:
    """
    Qt's 'void QQuickCalendarModel::setTo(QDate to)': Qt's library has no
    name for it, and its code in Qt's source does not compile apart from its
    file: member access into incomplete type 'QQuickCalendarModelPrivate'.
    """
    raise NotImplementedError(
        "'QQuickCalendarModel.setTo' has no cute function yet. Qt's 'void "
        "QQuickCalendarModel::setTo(QDate to)': Qt's library has no name "
        "for it, and its code in Qt's source does not compile apart from "
        "its file: member access into incomplete type "
        "'QQuickCalendarModelPrivate'.")

  @staticmethod
  def to(*__, **_) -> Never:
    """
    Qt's 'QDate QQuickCalendarModel::to() const': Qt's library has no name
    for it, and its code in Qt's source does not compile apart from its file:
    member access into incomplete type 'const QQuickCalendarModelPrivate'.
    """
    raise NotImplementedError(
        "'QQuickCalendarModel.to' has no cute function yet. Qt's 'QDate "
        "QQuickCalendarModel::to() const': Qt's library has no name for it, "
        "and its code in Qt's source does not compile apart from its file: "
        "member access into incomplete type 'const "
        "QQuickCalendarModelPrivate'.")

  @staticmethod
  def yearAt(*__, **_) -> Never:
    """
    Qt's 'int QQuickCalendarModel::yearAt(int index) const': Qt's library has
    no name for it, and its code in Qt's source does not compile apart from
    its file: member access into incomplete type 'const
    QQuickCalendarModelPrivate'.
    """
    raise NotImplementedError(
        "'QQuickCalendarModel.yearAt' has no cute function yet. Qt's 'int "
        "QQuickCalendarModel::yearAt(int index) const': Qt's library has no "
        "name for it, and its code in Qt's source does not compile apart "
        "from its file: member access into incomplete type 'const "
        "QQuickCalendarModelPrivate'.")
