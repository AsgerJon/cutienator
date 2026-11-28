"""
QDeclarativeSupportedCategoriesModel binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtLocation/6.12.0/QtLocation/private/qdeclarativesupportedcategoriesmodel_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QDeclarativeSupportedCategoriesModel to be private: it declares
#  the class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import QAbstractItemModel, QHash, QObject, QStringList
from ..QtQml import QQmlParserStatus

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QByteArray, QMetaObject, QModelIndex, QVariant
  from . import QDeclarativeGeoServiceProvider, QPlaceCategory, QPlaceManager
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDeclarativeGeoServiceProvider = WAIT['QDeclarativeGeoServiceProvider']
  QModelIndex = WAIT['QModelIndex']
  QPlaceCategory = WAIT['QPlaceCategory']
  QPlaceManager = WAIT['QPlaceManager']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QDeclarativeSupportedCategoriesModel(QAbstractItemModel, QQmlParserStatus):
  """
  The cute side of Qt's QDeclarativeSupportedCategoriesModel: a plain Python
  object standing in front of one C++ QDeclarativeSupportedCategoriesModel.

  It is built on the cute 'QAbstractItemModel', as Qt's
  QDeclarativeSupportedCategoriesModel is built on Qt's QAbstractItemModel,
  and has everything that class has. It is built on the cute
  'QQmlParserStatus' as well, as Qt's QDeclarativeSupportedCategoriesModel is
  built on Qt's QQmlParserStatus too, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QDeclarativeSupportedCategoriesModel that has a
  ritual and that Python can call so far, 30 names in all: 'metaObject',
  'tr', 'classBegin', 'componentComplete', 'rowCount', 'columnCount',
  'index', 'parent', 'data', 'roleNames', 'setPlugin', 'plugin',
  'setHierarchical', 'hierarchical', 'errorString', 'status', 'setStatus',
  'pluginChanged', 'hierarchicalChanged', 'statusChanged', 'dataChanged',
  'update', 'replyFinished', 'addedCategory', 'updatedCategory',
  'removedCategory', 'connectNotificationSignals', 'populateCategories',
  'updateLayout', 'emitDataChanged'. It can be made from Python, in 1 way;
  see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QDeclarativeSupportedCategoriesModel::qt_metacast(const char
    *a0)': one of Qt's own inner workings.
  - Qt's 'int
    QDeclarativeSupportedCategoriesModel::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QDeclarativeSupportedCategoriesModel::
    ~QDeclarativeSupportedCategoriesModel()': the destructor: Python never
    removes a C++ QDeclarativeSupportedCategoriesModel.
  - Qt's 'int
    QDeclarativeSupportedCategoriesModel::rowToAddChild(PlaceCategoryNode
    *a0, const QPlaceCategory &category)': names
    'QDeclarativeSupportedCategoriesModel::PlaceCategoryNode', which has no
    cute class yet.

  What has no ritual
  ------------------

  2 of the 38 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QDeclarativeSupportedCategoriesModel is created at the first use,
    not by 'QDeclarativeSupportedCategoriesModel(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QDeclarativeSupportedCategoriesModel.
  - Qt tells when it has removed the C++
    QDeclarativeSupportedCategoriesModel. Every call on the cute object, and
    every use of it as an argument, then raises 'RuntimeError', and nothing
    reaches C++.
  - Each name of Qt's QDeclarativeSupportedCategoriesModel that has no cute
    function yet, 'rowToAddChild', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QDeclarativeSupportedCategoriesModel, each a
  #  class in here as in C++, and the names Qt has for the combinations of
  #  its flags enums.

  class Roles(CuteNum):
    """
    The enum 'QDeclarativeSupportedCategoriesModel::Roles' of Qt, with the 2
    names Qt gives in it.
    """

    CategoryRole = Kee[int](256)
    ParentCategoryRole = Kee[int](257)

  class Status(CuteNum):
    """
    The enum 'QDeclarativeSupportedCategoriesModel::Status' of Qt, with the 4
    names Qt gives in it.
    """

    Null = Kee[int](0)
    Ready = Kee[int](1)
    Loading = Kee[int](2)
    Error = Kee[int](3)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(str)
  @overload(NoneType)
  @overload(str, str)
  @overload(str, NoneType)
  @overload(NoneType, str)
  @overload(NoneType, NoneType)
  @overload(str, str, int)
  @overload(str, NoneType, int)
  @overload(NoneType, str, int)
  @overload(NoneType, NoneType, int)
  def tr(s: Optional[str], c: Optional[str] = None, n: int = -1) -> str:
    """
    Calls Qt's 'QString QDeclarativeSupportedCategoriesModel::tr(const char
    *s, const char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativesupportedcategoriesmodel.html#tr

    Parameters
    ----------

    s : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    c : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text. May
      be left out, as in Qt: it is then None.

    n : int
      Passed on as it is. May be left out, as in Qt: it is then -1.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QDeclarativeSupportedCategoriesModel::tr(const char *s, const
    #      char *c, int n)
    return Rituals.call(
        'ritual_ZN36QDeclarativeSupportedCategoriesModel2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QDeclarativeSupportedCategoriesModel'

  #  Qt's QDeclarativeSupportedCategoriesModel is built on more than one
  #  class. The part of a C++ QDeclarativeSupportedCategoriesModel that
  #  belongs to a class after the first begins somewhere inside the object,
  #  and the ritual named for that class gives where; see
  #  'CuteMixin._addressAs'.
  __cast_rituals__ = {
      'QQmlParserStatus':
          'ritual_cast_QDeclarativeSupportedCategoriesModel_QQmlParserStatus',
  }

  #  A C++ QDeclarativeSupportedCategoriesModel Python makes is of a C++
  #  class of ours, in which Python can take functions over. This ritual
  #  hands one over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QDeclarativeSupportedCategoriesModel'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject
    *QDeclarativeSupportedCategoriesModel::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativesupportedcategoriesmodel.html

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QDeclarativeSupportedCategoriesModel::metaObject()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK36QDeclarativeSupportedCategoriesModel10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  @overload(QModelIndex)
  def rowCount(self, parent: QModelIndex) -> int:
    """
    Calls Qt's 'int QDeclarativeSupportedCategoriesModel::rowCount(const
    QModelIndex &parent) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativesupportedcategoriesmodel.html#rowCount

    Parameters
    ----------

    parent : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.
    """
    #  int QDeclarativeSupportedCategoriesModel::rowCount(const QModelIndex
    #      &parent) const
    ritual = (
        'ritual_ZNK36QDeclarativeSupportedCategoriesModel8rowCountERK11QMod'
        'elIndex')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK36QDeclarativeSupportedCategoriesModel8rowCountERK'
          '11QModelIndex')
    return self.uglySide.call(ritual, self._valueOf(parent))

  @overload(QModelIndex)
  def columnCount(self, parent: QModelIndex) -> int:
    """
    Calls Qt's 'int QDeclarativeSupportedCategoriesModel::columnCount(const
    QModelIndex &parent) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativesupportedcategoriesmodel.html

    Parameters
    ----------

    parent : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.
    """
    #  int QDeclarativeSupportedCategoriesModel::columnCount(const
    #      QModelIndex &parent) const
    ritual = (
        'ritual_ZNK36QDeclarativeSupportedCategoriesModel11columnCountERK11'
        'QModelIndex')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK36QDeclarativeSupportedCategoriesModel11columnCoun'
          'tERK11QModelIndex')
    return self.uglySide.call(ritual, self._valueOf(parent))

  @overload(int, int, QModelIndex)
  def index(self, row: int, column: int, parent: QModelIndex) -> QModelIndex:
    """
    Calls Qt's 'QModelIndex QDeclarativeSupportedCategoriesModel::index(int
    row, int column, const QModelIndex &parent) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativesupportedcategoriesmodel.html#index

    Parameters
    ----------

    row : int
      Passed on as it is.

    column : int
      Passed on as it is.

    parent : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    Returns
    -------

    QModelIndex
      A new cute QModelIndex around the copy Qt gave back. Python owns it.
    """
    #  QModelIndex QDeclarativeSupportedCategoriesModel::index(int row, int
    #      column, const QModelIndex &parent) const
    ritual = (
        'ritual_ZNK36QDeclarativeSupportedCategoriesModel5indexEiiRK11QMode'
        'lIndex')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK36QDeclarativeSupportedCategoriesModel5indexEiiRK1'
          '1QModelIndex')
    address = self.uglySide.call(ritual, row, column, self._valueOf(parent))
    from ..QtCore import QModelIndex
    return QModelIndex._cuteOwning(address)

  @overload(str)
  def index(self, categoryId: str) -> QModelIndex:
    """
    Calls Qt's 'QModelIndex QDeclarativeSupportedCategoriesModel::index(const
    QString &categoryId) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativesupportedcategoriesmodel.html#index

    Parameters
    ----------

    categoryId : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QModelIndex
      A new cute QModelIndex around the copy Qt gave back. Python owns it.
    """
    #  QModelIndex QDeclarativeSupportedCategoriesModel::index(const QString
    #      &categoryId) const
    address = self.uglySide.call(
        'ritual_ZNK36QDeclarativeSupportedCategoriesModel5indexERK7QString',
        categoryId,
    )
    from ..QtCore import QModelIndex
    return QModelIndex._cuteOwning(address)

  @overload(QModelIndex)
  def parent(self, child: QModelIndex) -> QModelIndex:
    """
    Calls Qt's 'QModelIndex
    QDeclarativeSupportedCategoriesModel::parent(const QModelIndex &child)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativesupportedcategoriesmodel.html#parent

    Parameters
    ----------

    child : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    Returns
    -------

    QModelIndex
      A new cute QModelIndex around the copy Qt gave back. Python owns it.
    """
    #  QModelIndex QDeclarativeSupportedCategoriesModel::parent(const
    #      QModelIndex &child) const
    ritual = (
        'ritual_ZNK36QDeclarativeSupportedCategoriesModel6parentERK11QModel'
        'Index')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK36QDeclarativeSupportedCategoriesModel6parentERK11'
          'QModelIndex')
    address = self.uglySide.call(ritual, self._valueOf(child))
    from ..QtCore import QModelIndex
    return QModelIndex._cuteOwning(address)

  @overload(QModelIndex, int)
  def data(self, index: QModelIndex, role: int) -> QVariant:
    """
    Calls Qt's 'QVariant QDeclarativeSupportedCategoriesModel::data(const
    QModelIndex &index, int role) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativesupportedcategoriesmodel.html#data

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
    #  QVariant QDeclarativeSupportedCategoriesModel::data(const QModelIndex
    #      &index, int role) const
    ritual = (
        'ritual_ZNK36QDeclarativeSupportedCategoriesModel4dataERK11QModelIn'
        'dexi')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK36QDeclarativeSupportedCategoriesModel4dataERK11QM'
          'odelIndexi')
    address = self.uglySide.call(ritual, self._valueOf(index), role)
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  def roleNames(self) -> QHash[int, QByteArray]:
    """
    Calls Qt's 'QHash<int, QByteArray>
    QDeclarativeSupportedCategoriesModel::roleNames() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativesupportedcategoriesmodel.html

    Returns
    -------

    QHash[int, QByteArray]
      A new cute map around the copy Qt gave back. Python owns it.
    """
    #  QHash<int, QByteArray>
    #      QDeclarativeSupportedCategoriesModel::roleNames() const
    address = self.uglySide.call(
        'ritual_ZNK36QDeclarativeSupportedCategoriesModel9roleNamesEv',
    )
    from ..QtCore import QByteArray
    return QHash[int, QByteArray]._cuteOwning(address)

  def plugin(self) -> Optional[QDeclarativeGeoServiceProvider]:
    """
    Calls Qt's 'QDeclarativeGeoServiceProvider
    *QDeclarativeSupportedCategoriesModel::plugin() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativesupportedcategoriesmodel.html#plugin

    Returns
    -------

    Optional[QDeclarativeGeoServiceProvider]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QDeclarativeGeoServiceProvider
    #      *QDeclarativeSupportedCategoriesModel::plugin() const
    address = self.uglySide.call(
        'ritual_ZNK36QDeclarativeSupportedCategoriesModel6pluginEv',
    )
    from . import QDeclarativeGeoServiceProvider
    return QDeclarativeGeoServiceProvider._cuteAt(address)

  def hierarchical(self) -> bool:
    """
    Calls Qt's 'bool QDeclarativeSupportedCategoriesModel::hierarchical()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativesupportedcategoriesmodel.html
    """
    #  bool QDeclarativeSupportedCategoriesModel::hierarchical() const
    return self.uglySide.call(
        'ritual_ZNK36QDeclarativeSupportedCategoriesModel12hierarchicalEv',
    )

  def errorString(self) -> str:
    """
    Calls Qt's 'QString QDeclarativeSupportedCategoriesModel::errorString()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativesupportedcategoriesmodel.html

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QDeclarativeSupportedCategoriesModel::errorString() const
    return self.uglySide.call(
        'ritual_ZNK36QDeclarativeSupportedCategoriesModel11errorStringEv',
    )

  def status(self) -> Status:
    """
    Calls Qt's 'Status QDeclarativeSupportedCategoriesModel::status() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativesupportedcategoriesmodel.html#status

    Returns
    -------

    Status
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Status(number)' gives.
    """
    #  Status QDeclarativeSupportedCategoriesModel::status() const
    return QDeclarativeSupportedCategoriesModel.Status(self.uglySide.call(
        'ritual_ZNK36QDeclarativeSupportedCategoriesModel6statusEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QDeclarativeGeoServiceProvider)
  @overload(NoneType)
  def setPlugin(
      self,
      plugin: Optional[QDeclarativeGeoServiceProvider],
  ) -> None:
    """
    Calls Qt's 'void QDeclarativeSupportedCategoriesModel::setPlugin(
    QDeclarativeGeoServiceProvider *plugin)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativesupportedcategoriesmodel.html

    Parameters
    ----------

    plugin : Optional[QDeclarativeGeoServiceProvider]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QDeclarativeSupportedCategoriesModel::setPlugin(
    #      QDeclarativeGeoServiceProvider *plugin)
    self.uglySide.call(
        'ritual_ZN36QDeclarativeSupportedCategoriesModel9setPluginEP30QDecl'
        'arativeGeoServiceProvider',
        self._addressOf(plugin),
    )

  @overload(bool)
  def setHierarchical(self, hierarchical: bool) -> None:
    """
    Calls Qt's 'void
    QDeclarativeSupportedCategoriesModel::setHierarchical(bool
    hierarchical)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativesupportedcategoriesmodel.html

    Parameters
    ----------

    hierarchical : bool
      Passed on as it is.
    """
    #  void QDeclarativeSupportedCategoriesModel::setHierarchical(bool
    #      hierarchical)
    self.uglySide.call(
        'ritual_ZN36QDeclarativeSupportedCategoriesModel15setHierarchicalEb',
        hierarchical,
    )

  @overload(Status)
  @overload(Status, str)
  def setStatus(self, status: Status, errorString: str = '') -> None:
    """
    Calls Qt's 'void QDeclarativeSupportedCategoriesModel::setStatus(Status
    status, const QString &errorString)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativesupportedcategoriesmodel.html

    Parameters
    ----------

    status : Status
      Passed on as its number.

    errorString : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.
    """
    #  void QDeclarativeSupportedCategoriesModel::setStatus(Status status,
    #      const QString &errorString)
    self.uglySide.call(
        'ritual_ZN36QDeclarativeSupportedCategoriesModel9setStatusENS_6Stat'
        'usERK7QString',
        status.value, errorString,
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

  @overload()
  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's 'QDeclarativeSupportedCategoriesModel::
    QDeclarativeSupportedCategoriesModel(QObject *parent)', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativesupportedcategoriesmodel.html

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QDeclarativeSupportedCategoriesModel::
    #      QDeclarativeSupportedCategoriesModel(QObject *parent)
    self._noteCreation(
        QDeclarativeSupportedCategoriesModel, lambda: Rituals.call(
            'ritual_ZN36QDeclarativeSupportedCategoriesModelC1EP7QObject',
            self._addressOf(parent, 'QObject'),
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

  def classBegin(self) -> None:
    """
    Calls Qt's 'void QDeclarativeSupportedCategoriesModel::classBegin()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativesupportedcategoriesmodel.html
    """
    #  void QDeclarativeSupportedCategoriesModel::classBegin()
    ritual = 'ritual_ZN36QDeclarativeSupportedCategoriesModel10classBeginEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN36QDeclarativeSupportedCategoriesModel10classBeginE'
          'v')
    self.uglySide.call(ritual)

  def componentComplete(self) -> None:
    """
    Calls Qt's 'void
    QDeclarativeSupportedCategoriesModel::componentComplete()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativesupportedcategoriesmodel.html
    """
    #  void QDeclarativeSupportedCategoriesModel::componentComplete()
    ritual = (
        'ritual_ZN36QDeclarativeSupportedCategoriesModel17componentComplete'
        'Ev')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN36QDeclarativeSupportedCategoriesModel17componentCo'
          'mpleteEv')
    self.uglySide.call(ritual)

  def pluginChanged(self) -> None:
    """
    Calls Qt's 'void QDeclarativeSupportedCategoriesModel::pluginChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativesupportedcategoriesmodel.html
    """
    #  void QDeclarativeSupportedCategoriesModel::pluginChanged()
    self.uglySide.call(
        'ritual_ZN36QDeclarativeSupportedCategoriesModel13pluginChangedEv',
    )

  def hierarchicalChanged(self) -> None:
    """
    Calls Qt's 'void
    QDeclarativeSupportedCategoriesModel::hierarchicalChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativesupportedcategoriesmodel.html
    """
    #  void QDeclarativeSupportedCategoriesModel::hierarchicalChanged()
    self.uglySide.call(
        'ritual_ZN36QDeclarativeSupportedCategoriesModel19hierarchicalChang'
        'edEv',
    )

  def statusChanged(self) -> None:
    """
    Calls Qt's 'void QDeclarativeSupportedCategoriesModel::statusChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativesupportedcategoriesmodel.html
    """
    #  void QDeclarativeSupportedCategoriesModel::statusChanged()
    self.uglySide.call(
        'ritual_ZN36QDeclarativeSupportedCategoriesModel13statusChangedEv',
    )

  def dataChanged(self) -> None:
    """
    Calls Qt's 'void QDeclarativeSupportedCategoriesModel::dataChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativesupportedcategoriesmodel.html
    """
    #  void QDeclarativeSupportedCategoriesModel::dataChanged()
    self.uglySide.call(
        'ritual_ZN36QDeclarativeSupportedCategoriesModel11dataChangedEv',
    )

  def update(self) -> None:
    """
    Calls Qt's 'void QDeclarativeSupportedCategoriesModel::update()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativesupportedcategoriesmodel.html#update
    """
    #  void QDeclarativeSupportedCategoriesModel::update()
    self.uglySide.call(
        'ritual_ZN36QDeclarativeSupportedCategoriesModel6updateEv',
    )

  def replyFinished(self) -> None:
    """
    Calls Qt's 'void QDeclarativeSupportedCategoriesModel::replyFinished()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativesupportedcategoriesmodel.html
    """
    #  void QDeclarativeSupportedCategoriesModel::replyFinished()
    self.uglySide.call(
        'ritual_ZN36QDeclarativeSupportedCategoriesModel13replyFinishedEv',
    )

  @overload(QPlaceCategory, str)
  def addedCategory(self, category: QPlaceCategory, parentId: str) -> None:
    """
    Calls Qt's 'void
    QDeclarativeSupportedCategoriesModel::addedCategory(const QPlaceCategory
    &category, const QString &parentId)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativesupportedcategoriesmodel.html

    Parameters
    ----------

    category : QPlaceCategory
      Passed on as a value: Qt reads the C++ QPlaceCategory, which stays
      Python's own.

    parentId : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QDeclarativeSupportedCategoriesModel::addedCategory(const
    #      QPlaceCategory &category, const QString &parentId)
    self.uglySide.call(
        'ritual_ZN36QDeclarativeSupportedCategoriesModel13addedCategoryERK1'
        '4QPlaceCategoryRK7QString',
        self._valueOf(category), parentId,
    )

  @overload(QPlaceCategory, str)
  def updatedCategory(self, category: QPlaceCategory, parentId: str) -> None:
    """
    Calls Qt's 'void
    QDeclarativeSupportedCategoriesModel::updatedCategory(const
    QPlaceCategory &category, const QString &parentId)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativesupportedcategoriesmodel.html

    Parameters
    ----------

    category : QPlaceCategory
      Passed on as a value: Qt reads the C++ QPlaceCategory, which stays
      Python's own.

    parentId : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QDeclarativeSupportedCategoriesModel::updatedCategory(const
    #      QPlaceCategory &category, const QString &parentId)
    self.uglySide.call(
        'ritual_ZN36QDeclarativeSupportedCategoriesModel15updatedCategoryER'
        'K14QPlaceCategoryRK7QString',
        self._valueOf(category), parentId,
    )

  @overload(str, str)
  def removedCategory(self, categoryId: str, parentId: str) -> None:
    """
    Calls Qt's 'void
    QDeclarativeSupportedCategoriesModel::removedCategory(const QString
    &categoryId, const QString &parentId)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativesupportedcategoriesmodel.html

    Parameters
    ----------

    categoryId : str
      Passed on as it is: a QString is made of it for the call.

    parentId : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QDeclarativeSupportedCategoriesModel::removedCategory(const
    #      QString &categoryId, const QString &parentId)
    self.uglySide.call(
        'ritual_ZN36QDeclarativeSupportedCategoriesModel15removedCategoryER'
        'K7QStringS2_',
        categoryId, parentId,
    )

  def connectNotificationSignals(self) -> None:
    """
    Calls Qt's 'void
    QDeclarativeSupportedCategoriesModel::connectNotificationSignals()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativesupportedcategoriesmodel.html
    """
    #  void
    #      QDeclarativeSupportedCategoriesModel::connectNotificationSignals()
    self.uglySide.call(
        'ritual_ZN36QDeclarativeSupportedCategoriesModel26connectNotificati'
        'onSignalsEv',
    )

  @overload(QPlaceManager, QPlaceCategory)
  @overload(NoneType, QPlaceCategory)
  def populateCategories(
      self,
      a0: Optional[QPlaceManager],
      parent: QPlaceCategory,
  ) -> QStringList:
    """
    Calls Qt's 'QStringList
    QDeclarativeSupportedCategoriesModel::populateCategories(QPlaceManager
    *a0, const QPlaceCategory &parent)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativesupportedcategoriesmodel.html

    Parameters
    ----------

    a0 : Optional[QPlaceManager]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    parent : QPlaceCategory
      Passed on as a value: Qt reads the C++ QPlaceCategory, which stays
      Python's own.

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QDeclarativeSupportedCategoriesModel::populateCategories(
    #      QPlaceManager *a0, const QPlaceCategory &parent)
    address = self.uglySide.call(
        'ritual_ZN36QDeclarativeSupportedCategoriesModel18populateCategorie'
        'sEP13QPlaceManagerRK14QPlaceCategory',
        self._addressOf(a0), self._valueOf(parent),
    )
    return QStringList._cuteOwning(address)

  def updateLayout(self) -> None:
    """
    Calls Qt's 'void QDeclarativeSupportedCategoriesModel::updateLayout()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativesupportedcategoriesmodel.html
    """
    #  void QDeclarativeSupportedCategoriesModel::updateLayout()
    self.uglySide.call(
        'ritual_ZN36QDeclarativeSupportedCategoriesModel12updateLayoutEv',
    )

  def emitDataChanged(self) -> None:
    """
    Calls Qt's 'void
    QDeclarativeSupportedCategoriesModel::emitDataChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativesupportedcategoriesmodel.html
    """
    #  void QDeclarativeSupportedCategoriesModel::emitDataChanged()
    self.uglySide.call(
        'ritual_ZN36QDeclarativeSupportedCategoriesModel15emitDataChangedEv',
    )

  @staticmethod
  def rowToAddChild(*__, **_) -> Never:
    """
    Qt's 'int
    QDeclarativeSupportedCategoriesModel::rowToAddChild(PlaceCategoryNode
    *a0, const QPlaceCategory &category)': names
    'QDeclarativeSupportedCategoriesModel::PlaceCategoryNode', which has no
    cute class yet.
    """
    raise NotImplementedError(
        "'QDeclarativeSupportedCategoriesModel.rowToAddChild' has no cute "
        "function yet. Qt's 'int "
        "QDeclarativeSupportedCategoriesModel::rowToAddChild(PlaceCategoryNo"
        "de *a0, const QPlaceCategory &category)': names "
        "'QDeclarativeSupportedCategoriesModel::PlaceCategoryNode', which "
        "has no cute class yet.")
