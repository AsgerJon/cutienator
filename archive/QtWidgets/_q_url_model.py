"""
QUrlModel binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/6.12.0/QtWidgets/private/qsidebar_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QUrlModel to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteNum, WAIT
from ..QtCore import Qt, QList
from ..QtGui import QStandardItemModel

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QMimeData, QModelIndex, QUrl, QVariant
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QModelIndex = WAIT['QModelIndex']
  QUrl = WAIT['QUrl']
  QVariant = WAIT['QVariant']


class QUrlModel(QStandardItemModel):
  """
  The cute side of Qt's QUrlModel: a plain Python object standing in front of
  one C++ QUrlModel.

  It is built on the cute 'QStandardItemModel', as Qt's QUrlModel is built on
  Qt's QStandardItemModel, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QUrlModel that has a ritual and that Python can call
  so far, 9 names in all: 'metaObject', 'mimeData', 'flags', 'setData',
  'urls', 'dataChanged', 'layoutChanged', 'setUrl', 'changed'. None can be
  made from Python: one comes out of a function of another class that gives
  one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QUrlModel::~QUrlModel()': the destructor: Python never removes a
    C++ QUrlModel.

  What has no ritual
  ------------------

  14 of the 24 functions Qt declares: 5 leans on 'QUrlModel; 4 Qt's library
  has no name for it, and its code in Qt's source does not compile apart from
  its file; 2 takes or gives a type that cannot be passed yet; 2 declared and
  nowhere to be found; 1 a template.

  What to expect
  --------------

  - The C++ QUrlModel is created at the first use, not by 'QUrlModel(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QUrlModel.
  - Qt tells when it has removed the C++ QUrlModel. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
  """

  #  The enums Qt writes inside QUrlModel, each a class in here as in C++,
  #  and the names Qt has for the combinations of its flags enums.

  class Roles(CuteNum):
    """The enum 'QUrlModel::Roles' of Qt, with the 2 names Qt gives in it."""

    UrlRole = Kee[int](257)
    EnabledRole = Kee[int](258)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QUrlModel'

  #  A C++ QUrlModel Python makes is of a C++ class of ours, in which Python
  #  can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QUrlModel'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QUrlModel::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qurlmodel.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QUrlModel::metaObject() const
    address = self.uglySide.call('ritual_ZNK9QUrlModel10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  @overload(QList[QModelIndex])
  def mimeData(self, indexes: QList[QModelIndex]) -> Optional[QMimeData]:
    """
    Calls Qt's 'QMimeData *QUrlModel::mimeData(const QModelIndexList
    &indexes) const'.

    Qt's own words: https://doc.qt.io/qt-6/qurlmodel.html#mimeData

    Parameters
    ----------

    indexes : QList[QModelIndex]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    Returns
    -------

    Optional[QMimeData]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QMimeData *QUrlModel::mimeData(const QModelIndexList &indexes) const
    address = self.uglySide.call(
        'ritual_ZNK9QUrlModel8mimeDataERK5QListI11QModelIndexE',
        self._valueOf(indexes),
    )
    from ..QtCore import QMimeData
    return QMimeData._cuteAt(address)

  @overload(QModelIndex)
  def flags(self, index: QModelIndex) -> Qt.ItemFlags:
    """
    Calls Qt's 'Qt::ItemFlags QUrlModel::flags(const QModelIndex &index)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qurlmodel.html#flags

    Parameters
    ----------

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    Returns
    -------

    Qt.ItemFlags
      The value standing for the combination Qt gave back.
    """
    #  Qt::ItemFlags QUrlModel::flags(const QModelIndex &index) const
    ritual = 'ritual_ZNK9QUrlModel5flagsERK11QModelIndex'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK9QUrlModel5flagsERK11QModelIndex'
    return Qt.ItemFlags(self.uglySide.call(ritual, self._valueOf(index)))

  def urls(self) -> QList[QUrl]:
    """
    Calls Qt's 'QList<QUrl> QUrlModel::urls() const'.

    Qt's own words: https://doc.qt.io/qt-6/qurlmodel.html#urls

    Returns
    -------

    QList[QUrl]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QUrl> QUrlModel::urls() const
    address = self.uglySide.call('ritual_ZNK9QUrlModel4urlsEv')
    from ..QtCore import QUrl
    return QList[QUrl]._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QModelIndex, QVariant)
  @overload(QModelIndex, QVariant, int)
  def setData(
      self,
      index: QModelIndex,
      value: QVariant,
      role: int = 2,
  ) -> bool:
    """
    Calls Qt's 'bool QUrlModel::setData(const QModelIndex &index, const
    QVariant &value, int role)'.

    Qt's own words: https://doc.qt.io/qt-6/qurlmodel.html#setData

    Parameters
    ----------

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    value : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.

    role : int
      Passed on as it is. May be left out, as in Qt: it is then 2.
    """
    #  bool QUrlModel::setData(const QModelIndex &index, const QVariant
    #      &value, int role)
    ritual = 'ritual_ZN9QUrlModel7setDataERK11QModelIndexRK8QVarianti'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN9QUrlModel7setDataERK11QModelIndexRK8QVarianti'
    return self.uglySide.call(
        ritual, self._valueOf(index), self._valueOf(value), role,
    )

  @overload(QModelIndex, QUrl, QModelIndex)
  def setUrl(
      self,
      index: QModelIndex,
      url: QUrl,
      dirIndex: QModelIndex,
  ) -> None:
    """
    Calls Qt's 'void QUrlModel::setUrl(const QModelIndex &index, const QUrl
    &url, const QModelIndex &dirIndex)'.

    Qt's own words: https://doc.qt.io/qt-6/qurlmodel.html#setUrl

    Parameters
    ----------

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    url : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.

    dirIndex : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.
    """
    #  void QUrlModel::setUrl(const QModelIndex &index, const QUrl &url,
    #      const QModelIndex &dirIndex)
    self.uglySide.call(
        'ritual_ZN9QUrlModel6setUrlERK11QModelIndexRK4QUrlS2_',
        self._valueOf(index), self._valueOf(url), self._valueOf(dirIndex),
    )

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

  @overload(QModelIndex, QModelIndex)
  def dataChanged(
      self,
      topLeft: QModelIndex,
      bottomRight: QModelIndex,
  ) -> None:
    """
    Calls Qt's 'void QUrlModel::dataChanged(const QModelIndex &topLeft, const
    QModelIndex &bottomRight)'.

    Qt's own words: https://doc.qt.io/qt-6/qurlmodel.html#dataChanged

    Parameters
    ----------

    topLeft : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    bottomRight : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.
    """
    #  void QUrlModel::dataChanged(const QModelIndex &topLeft, const
    #      QModelIndex &bottomRight)
    self.uglySide.call(
        'ritual_ZN9QUrlModel11dataChangedERK11QModelIndexS2_',
        self._valueOf(topLeft), self._valueOf(bottomRight),
    )

  def layoutChanged(self) -> None:
    """
    Calls Qt's 'void QUrlModel::layoutChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qurlmodel.html#layoutChanged
    """
    #  void QUrlModel::layoutChanged()
    self.uglySide.call('ritual_ZN9QUrlModel13layoutChangedEv')

  @overload(str)
  def changed(self, path: str) -> None:
    """
    Calls Qt's 'void QUrlModel::changed(const QString &path)'.

    Qt's own words: https://doc.qt.io/qt-6/qurlmodel.html#changed

    Parameters
    ----------

    path : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QUrlModel::changed(const QString &path)
    self.uglySide.call('ritual_ZN9QUrlModel7changedERK7QString', path)
