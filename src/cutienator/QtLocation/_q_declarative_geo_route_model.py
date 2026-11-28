"""
QDeclarativeGeoRouteModel binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtLocation/6.12.0/QtLocation/private/qdeclarativegeoroutemodel_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QDeclarativeGeoRouteModel to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import QAbstractListModel, QHash, QLocale, QObject
from ..QtQml import QQmlParserStatus
from . import QGeoRouteReply

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QByteArray, QMetaObject, QModelIndex, QVariant
  from . import QDeclarativeGeoRouteQuery, QDeclarativeGeoServiceProvider
  from . import QGeoRoute
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDeclarativeGeoRouteQuery = WAIT['QDeclarativeGeoRouteQuery']
  QDeclarativeGeoServiceProvider = WAIT['QDeclarativeGeoServiceProvider']
  QModelIndex = WAIT['QModelIndex']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QDeclarativeGeoRouteModel(QAbstractListModel, QQmlParserStatus):
  """
  The cute side of Qt's QDeclarativeGeoRouteModel: a plain Python object
  standing in front of one C++ QDeclarativeGeoRouteModel.

  It is built on the cute 'QAbstractListModel', as Qt's
  QDeclarativeGeoRouteModel is built on Qt's QAbstractListModel, and has
  everything that class has. It is built on the cute 'QQmlParserStatus' as
  well, as Qt's QDeclarativeGeoRouteModel is built on Qt's QQmlParserStatus
  too, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QDeclarativeGeoRouteModel that has a ritual and that
  Python can call so far, 38 names in all: 'metaObject', 'tr', 'classBegin',
  'componentComplete', 'rowCount', 'data', 'roleNames', 'setPlugin',
  'plugin', 'setQuery', 'query', 'setAutoUpdate', 'autoUpdate',
  'setMeasurementSystem', 'measurementSystem', 'status', 'errorString',
  'error', 'count', 'get', 'reset', 'cancel', 'countChanged',
  'pluginChanged', 'queryChanged', 'autoUpdateChanged', 'statusChanged',
  'errorChanged', 'routesChanged', 'measurementSystemChanged',
  'abortRequested', 'update', 'routingFinished', 'routingError',
  'queryDetailsChanged', 'pluginReady', 'setStatus', 'setError'. It can be
  made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QDeclarativeGeoRouteModel::qt_metacast(const char *a0)': one
    of Qt's own inner workings.
  - Qt's 'int QDeclarativeGeoRouteModel::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.

  What has no ritual
  ------------------

  2 of the 43 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QDeclarativeGeoRouteModel is created at the first use, not by
    'QDeclarativeGeoRouteModel(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QDeclarativeGeoRouteModel.
  - Qt tells when it has removed the C++ QDeclarativeGeoRouteModel. Every
    call on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  #  The enums Qt writes inside QDeclarativeGeoRouteModel, each a class in
  #  here as in C++, and the names Qt has for the combinations of its flags
  #  enums.

  class Roles(CuteNum):
    """
    The enum 'QDeclarativeGeoRouteModel::Roles' of Qt, with the 1 names Qt
    gives in it.
    """

    RouteRole = Kee[int](756)

  class RouteError(CuteNum):
    """
    The enum 'QDeclarativeGeoRouteModel::RouteError' of Qt, with the 8 names
    Qt gives in it.
    """

    NoError = Kee[int](0)
    EngineNotSetError = Kee[int](1)
    CommunicationError = Kee[int](2)
    ParseError = Kee[int](3)
    UnsupportedOptionError = Kee[int](4)
    UnknownError = Kee[int](5)
    UnknownParameterError = Kee[int](100)
    MissingRequiredParameterError = Kee[int](101)

  class Status(CuteNum):
    """
    The enum 'QDeclarativeGeoRouteModel::Status' of Qt, with the 4 names Qt
    gives in it.
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
    Calls Qt's 'QString QDeclarativeGeoRouteModel::tr(const char *s, const
    char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qdeclarativegeoroutemodel.html#tr

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
    #  QString QDeclarativeGeoRouteModel::tr(const char *s, const char *c,
    #      int n)
    return Rituals.call(
        'ritual_ZN25QDeclarativeGeoRouteModel2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QDeclarativeGeoRouteModel'

  #  Qt's QDeclarativeGeoRouteModel is built on more than one class. The part
  #  of a C++ QDeclarativeGeoRouteModel that belongs to a class after the
  #  first begins somewhere inside the object, and the ritual named for that
  #  class gives where; see 'CuteMixin._addressAs'.
  __cast_rituals__ = {
      'QQmlParserStatus':
          'ritual_cast_QDeclarativeGeoRouteModel_QQmlParserStatus',
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
    Calls Qt's 'const QMetaObject *QDeclarativeGeoRouteModel::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeoroutemodel.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QDeclarativeGeoRouteModel::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK25QDeclarativeGeoRouteModel10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  @overload(QModelIndex)
  def rowCount(self, parent: QModelIndex) -> int:
    """
    Calls Qt's 'int QDeclarativeGeoRouteModel::rowCount(const QModelIndex
    &parent) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeoroutemodel.html#rowCount

    Parameters
    ----------

    parent : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.
    """
    #  int QDeclarativeGeoRouteModel::rowCount(const QModelIndex &parent)
    #      const
    ritual = 'ritual_ZNK25QDeclarativeGeoRouteModel8rowCountERK11QModelIndex'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK25QDeclarativeGeoRouteModel8rowCountERK11QModelInd'
          'ex')
    return self.uglySide.call(ritual, self._valueOf(parent))

  @overload(QModelIndex, int)
  def data(self, index: QModelIndex, role: int) -> QVariant:
    """
    Calls Qt's 'QVariant QDeclarativeGeoRouteModel::data(const QModelIndex
    &index, int role) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeoroutemodel.html#data

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
    #  QVariant QDeclarativeGeoRouteModel::data(const QModelIndex &index, int
    #      role) const
    ritual = 'ritual_ZNK25QDeclarativeGeoRouteModel4dataERK11QModelIndexi'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK25QDeclarativeGeoRouteModel4dataERK11QModelIndexi')
    address = self.uglySide.call(ritual, self._valueOf(index), role)
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  def roleNames(self) -> QHash[int, QByteArray]:
    """
    Calls Qt's 'QHash<int, QByteArray> QDeclarativeGeoRouteModel::roleNames()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeoroutemodel.html#roleNames

    Returns
    -------

    QHash[int, QByteArray]
      A new cute map around the copy Qt gave back. Python owns it.
    """
    #  QHash<int, QByteArray> QDeclarativeGeoRouteModel::roleNames() const
    address = self.uglySide.call(
        'ritual_ZNK25QDeclarativeGeoRouteModel9roleNamesEv',
    )
    from ..QtCore import QByteArray
    return QHash[int, QByteArray]._cuteOwning(address)

  def plugin(self) -> Optional[QDeclarativeGeoServiceProvider]:
    """
    Calls Qt's 'QDeclarativeGeoServiceProvider
    *QDeclarativeGeoRouteModel::plugin() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeoroutemodel.html#plugin

    Returns
    -------

    Optional[QDeclarativeGeoServiceProvider]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QDeclarativeGeoServiceProvider *QDeclarativeGeoRouteModel::plugin()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK25QDeclarativeGeoRouteModel6pluginEv',
    )
    from . import QDeclarativeGeoServiceProvider
    return QDeclarativeGeoServiceProvider._cuteAt(address)

  def query(self) -> Optional[QDeclarativeGeoRouteQuery]:
    """
    Calls Qt's 'QDeclarativeGeoRouteQuery *QDeclarativeGeoRouteModel::query()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeoroutemodel.html#query

    Returns
    -------

    Optional[QDeclarativeGeoRouteQuery]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QDeclarativeGeoRouteQuery *QDeclarativeGeoRouteModel::query() const
    address = self.uglySide.call(
        'ritual_ZNK25QDeclarativeGeoRouteModel5queryEv',
    )
    from . import QDeclarativeGeoRouteQuery
    return QDeclarativeGeoRouteQuery._cuteAt(address)

  def autoUpdate(self) -> bool:
    """
    Calls Qt's 'bool QDeclarativeGeoRouteModel::autoUpdate() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeoroutemodel.html#autoUpdate
    """
    #  bool QDeclarativeGeoRouteModel::autoUpdate() const
    return self.uglySide.call(
        'ritual_ZNK25QDeclarativeGeoRouteModel10autoUpdateEv',
    )

  def measurementSystem(self) -> QLocale.MeasurementSystem:
    """
    Calls Qt's 'QLocale::MeasurementSystem
    QDeclarativeGeoRouteModel::measurementSystem() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeoroutemodel.html#measurementSystem

    Returns
    -------

    QLocale.MeasurementSystem
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QLocale.MeasurementSystem(number)' gives.
    """
    #  QLocale::MeasurementSystem
    #      QDeclarativeGeoRouteModel::measurementSystem() const
    return QLocale.MeasurementSystem(self.uglySide.call(
        'ritual_ZNK25QDeclarativeGeoRouteModel17measurementSystemEv',
    ))

  def status(self) -> Status:
    """
    Calls Qt's 'Status QDeclarativeGeoRouteModel::status() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeoroutemodel.html#status

    Returns
    -------

    Status
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Status(number)' gives.
    """
    #  Status QDeclarativeGeoRouteModel::status() const
    return QDeclarativeGeoRouteModel.Status(self.uglySide.call(
        'ritual_ZNK25QDeclarativeGeoRouteModel6statusEv',
    ))

  def errorString(self) -> str:
    """
    Calls Qt's 'QString QDeclarativeGeoRouteModel::errorString() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeoroutemodel.html#errorString

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QDeclarativeGeoRouteModel::errorString() const
    return self.uglySide.call(
        'ritual_ZNK25QDeclarativeGeoRouteModel11errorStringEv',
    )

  def error(self) -> RouteError:
    """
    Calls Qt's 'RouteError QDeclarativeGeoRouteModel::error() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeoroutemodel.html#error

    Returns
    -------

    RouteError
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'RouteError(number)'
      gives.
    """
    #  RouteError QDeclarativeGeoRouteModel::error() const
    return QDeclarativeGeoRouteModel.RouteError(self.uglySide.call(
        'ritual_ZNK25QDeclarativeGeoRouteModel5errorEv',
    ))

  def count(self) -> int:
    """
    Calls Qt's 'int QDeclarativeGeoRouteModel::count() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeoroutemodel.html#count
    """
    #  int QDeclarativeGeoRouteModel::count() const
    return self.uglySide.call(
        'ritual_ZNK25QDeclarativeGeoRouteModel5countEv',
    )

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
    Calls Qt's 'void
    QDeclarativeGeoRouteModel::setPlugin(QDeclarativeGeoServiceProvider
    *plugin)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeoroutemodel.html#setPlugin

    Parameters
    ----------

    plugin : Optional[QDeclarativeGeoServiceProvider]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QDeclarativeGeoRouteModel::setPlugin(
    #      QDeclarativeGeoServiceProvider *plugin)
    self.uglySide.call(
        'ritual_ZN25QDeclarativeGeoRouteModel9setPluginEP30QDeclarativeGeoS'
        'erviceProvider',
        self._addressOf(plugin),
    )

  @overload(QDeclarativeGeoRouteQuery)
  @overload(NoneType)
  def setQuery(self, query: Optional[QDeclarativeGeoRouteQuery]) -> None:
    """
    Calls Qt's 'void
    QDeclarativeGeoRouteModel::setQuery(QDeclarativeGeoRouteQuery *query)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeoroutemodel.html#setQuery

    Parameters
    ----------

    query : Optional[QDeclarativeGeoRouteQuery]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QDeclarativeGeoRouteModel::setQuery(QDeclarativeGeoRouteQuery
    #      *query)
    self.uglySide.call(
        'ritual_ZN25QDeclarativeGeoRouteModel8setQueryEP25QDeclarativeGeoRo'
        'uteQuery',
        self._addressOf(query),
    )

  @overload(bool)
  def setAutoUpdate(self, autoUpdate: bool) -> None:
    """
    Calls Qt's 'void QDeclarativeGeoRouteModel::setAutoUpdate(bool
    autoUpdate)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeoroutemodel.html#setAutoUpdate

    Parameters
    ----------

    autoUpdate : bool
      Passed on as it is.
    """
    #  void QDeclarativeGeoRouteModel::setAutoUpdate(bool autoUpdate)
    self.uglySide.call(
        'ritual_ZN25QDeclarativeGeoRouteModel13setAutoUpdateEb', autoUpdate,
    )

  @overload(QLocale.MeasurementSystem)
  def setMeasurementSystem(self, ms: QLocale.MeasurementSystem) -> None:
    """
    Calls Qt's 'void
    QDeclarativeGeoRouteModel::setMeasurementSystem(QLocale::
    MeasurementSystem ms)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeoroutemodel.html

    Parameters
    ----------

    ms : QLocale.MeasurementSystem
      Passed on as its number.
    """
    #  void QDeclarativeGeoRouteModel::setMeasurementSystem(QLocale::
    #      MeasurementSystem ms)
    self.uglySide.call(
        'ritual_ZN25QDeclarativeGeoRouteModel20setMeasurementSystemEN7QLoca'
        'le17MeasurementSystemE',
        ms.value,
    )

  @overload(Status)
  def setStatus(self, status: Status) -> None:
    """
    Calls Qt's 'void QDeclarativeGeoRouteModel::setStatus(Status status)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeoroutemodel.html#setStatus

    Parameters
    ----------

    status : Status
      Passed on as its number.
    """
    #  void QDeclarativeGeoRouteModel::setStatus(Status status)
    self.uglySide.call(
        'ritual_ZN25QDeclarativeGeoRouteModel9setStatusENS_6StatusE',
        status.value,
    )

  @overload(RouteError, str)
  def setError(self, error: RouteError, errorString: str) -> None:
    """
    Calls Qt's 'void QDeclarativeGeoRouteModel::setError(RouteError error,
    const QString &errorString)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeoroutemodel.html#setError

    Parameters
    ----------

    error : RouteError
      Passed on as its number.

    errorString : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QDeclarativeGeoRouteModel::setError(RouteError error, const
    #      QString &errorString)
    self.uglySide.call(
        'ritual_ZN25QDeclarativeGeoRouteModel8setErrorENS_10RouteErrorERK7Q'
        'String',
        error.value, errorString,
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
    Notes what was given, for Qt's
    'QDeclarativeGeoRouteModel::QDeclarativeGeoRouteModel(QObject *parent)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeoroutemodel.html

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QDeclarativeGeoRouteModel::QDeclarativeGeoRouteModel(QObject *parent)
    self._noteCreation(QDeclarativeGeoRouteModel, lambda: Rituals.call(
        'ritual_ZN25QDeclarativeGeoRouteModelC1EP7QObject',
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
    Calls Qt's 'void QDeclarativeGeoRouteModel::classBegin()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeoroutemodel.html#classBegin
    """
    #  void QDeclarativeGeoRouteModel::classBegin()
    ritual = 'ritual_ZN25QDeclarativeGeoRouteModel10classBeginEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN25QDeclarativeGeoRouteModel10classBeginEv'
    self.uglySide.call(ritual)

  def componentComplete(self) -> None:
    """
    Calls Qt's 'void QDeclarativeGeoRouteModel::componentComplete()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeoroutemodel.html#componentComplete
    """
    #  void QDeclarativeGeoRouteModel::componentComplete()
    ritual = 'ritual_ZN25QDeclarativeGeoRouteModel17componentCompleteEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN25QDeclarativeGeoRouteModel17componentCompleteEv')
    self.uglySide.call(ritual)

  @overload(int)
  def get(self, index: int) -> QGeoRoute:
    """
    Calls Qt's 'QGeoRoute QDeclarativeGeoRouteModel::get(int index)'.

    Qt's own words: https://doc.qt.io/qt-6/qdeclarativegeoroutemodel.html#get

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    QGeoRoute
      A new cute QGeoRoute around the copy Qt gave back. Python owns it.
    """
    #  QGeoRoute QDeclarativeGeoRouteModel::get(int index)
    address = self.uglySide.call(
        'ritual_ZN25QDeclarativeGeoRouteModel3getEi', index,
    )
    from . import QGeoRoute
    return QGeoRoute._cuteOwning(address)

  def reset(self) -> None:
    """
    Calls Qt's 'void QDeclarativeGeoRouteModel::reset()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeoroutemodel.html#reset
    """
    #  void QDeclarativeGeoRouteModel::reset()
    self.uglySide.call('ritual_ZN25QDeclarativeGeoRouteModel5resetEv')

  def cancel(self) -> None:
    """
    Calls Qt's 'void QDeclarativeGeoRouteModel::cancel()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeoroutemodel.html#cancel
    """
    #  void QDeclarativeGeoRouteModel::cancel()
    self.uglySide.call('ritual_ZN25QDeclarativeGeoRouteModel6cancelEv')

  def countChanged(self) -> None:
    """
    Calls Qt's 'void QDeclarativeGeoRouteModel::countChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeoroutemodel.html#countChanged
    """
    #  void QDeclarativeGeoRouteModel::countChanged()
    self.uglySide.call(
        'ritual_ZN25QDeclarativeGeoRouteModel12countChangedEv',
    )

  def pluginChanged(self) -> None:
    """
    Calls Qt's 'void QDeclarativeGeoRouteModel::pluginChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeoroutemodel.html#pluginChanged
    """
    #  void QDeclarativeGeoRouteModel::pluginChanged()
    self.uglySide.call(
        'ritual_ZN25QDeclarativeGeoRouteModel13pluginChangedEv',
    )

  def queryChanged(self) -> None:
    """
    Calls Qt's 'void QDeclarativeGeoRouteModel::queryChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeoroutemodel.html#queryChanged
    """
    #  void QDeclarativeGeoRouteModel::queryChanged()
    self.uglySide.call(
        'ritual_ZN25QDeclarativeGeoRouteModel12queryChangedEv',
    )

  def autoUpdateChanged(self) -> None:
    """
    Calls Qt's 'void QDeclarativeGeoRouteModel::autoUpdateChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeoroutemodel.html#autoUpdateChanged
    """
    #  void QDeclarativeGeoRouteModel::autoUpdateChanged()
    self.uglySide.call(
        'ritual_ZN25QDeclarativeGeoRouteModel17autoUpdateChangedEv',
    )

  def statusChanged(self) -> None:
    """
    Calls Qt's 'void QDeclarativeGeoRouteModel::statusChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeoroutemodel.html#statusChanged
    """
    #  void QDeclarativeGeoRouteModel::statusChanged()
    self.uglySide.call(
        'ritual_ZN25QDeclarativeGeoRouteModel13statusChangedEv',
    )

  def errorChanged(self) -> None:
    """
    Calls Qt's 'void QDeclarativeGeoRouteModel::errorChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeoroutemodel.html#errorChanged
    """
    #  void QDeclarativeGeoRouteModel::errorChanged()
    self.uglySide.call(
        'ritual_ZN25QDeclarativeGeoRouteModel12errorChangedEv',
    )

  def routesChanged(self) -> None:
    """
    Calls Qt's 'void QDeclarativeGeoRouteModel::routesChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeoroutemodel.html#routesChanged
    """
    #  void QDeclarativeGeoRouteModel::routesChanged()
    self.uglySide.call(
        'ritual_ZN25QDeclarativeGeoRouteModel13routesChangedEv',
    )

  def measurementSystemChanged(self) -> None:
    """
    Calls Qt's 'void QDeclarativeGeoRouteModel::measurementSystemChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeoroutemodel.html
    """
    #  void QDeclarativeGeoRouteModel::measurementSystemChanged()
    self.uglySide.call(
        'ritual_ZN25QDeclarativeGeoRouteModel24measurementSystemChangedEv',
    )

  def abortRequested(self) -> None:
    """
    Calls Qt's 'void QDeclarativeGeoRouteModel::abortRequested()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeoroutemodel.html#abortRequested
    """
    #  void QDeclarativeGeoRouteModel::abortRequested()
    self.uglySide.call(
        'ritual_ZN25QDeclarativeGeoRouteModel14abortRequestedEv',
    )

  def update(self) -> None:
    """
    Calls Qt's 'void QDeclarativeGeoRouteModel::update()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeoroutemodel.html#update
    """
    #  void QDeclarativeGeoRouteModel::update()
    self.uglySide.call('ritual_ZN25QDeclarativeGeoRouteModel6updateEv')

  @overload(QGeoRouteReply)
  @overload(NoneType)
  def routingFinished(self, reply: Optional[QGeoRouteReply]) -> None:
    """
    Calls Qt's 'void
    QDeclarativeGeoRouteModel::routingFinished(QGeoRouteReply *reply)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeoroutemodel.html#routingFinished

    Parameters
    ----------

    reply : Optional[QGeoRouteReply]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QDeclarativeGeoRouteModel::routingFinished(QGeoRouteReply *reply)
    self.uglySide.call(
        'ritual_ZN25QDeclarativeGeoRouteModel15routingFinishedEP14QGeoRoute'
        'Reply',
        self._addressOf(reply),
    )

  @overload(QGeoRouteReply, QGeoRouteReply.Error, str)
  @overload(NoneType, QGeoRouteReply.Error, str)
  def routingError(
      self,
      reply: Optional[QGeoRouteReply],
      error: QGeoRouteReply.Error,
      errorString: str,
  ) -> None:
    """
    Calls Qt's 'void QDeclarativeGeoRouteModel::routingError(QGeoRouteReply
    *reply, QGeoRouteReply::Error error, const QString &errorString)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeoroutemodel.html#routingError

    Parameters
    ----------

    reply : Optional[QGeoRouteReply]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    error : QGeoRouteReply.Error
      Passed on as its number.

    errorString : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QDeclarativeGeoRouteModel::routingError(QGeoRouteReply *reply,
    #      QGeoRouteReply::Error error, const QString &errorString)
    self.uglySide.call(
        'ritual_ZN25QDeclarativeGeoRouteModel12routingErrorEP14QGeoRouteRep'
        'lyNS0_5ErrorERK7QString',
        self._addressOf(reply), error.value, errorString,
    )

  def queryDetailsChanged(self) -> None:
    """
    Calls Qt's 'void QDeclarativeGeoRouteModel::queryDetailsChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeoroutemodel.html#queryDetailsChanged
    """
    #  void QDeclarativeGeoRouteModel::queryDetailsChanged()
    self.uglySide.call(
        'ritual_ZN25QDeclarativeGeoRouteModel19queryDetailsChangedEv',
    )

  def pluginReady(self) -> None:
    """
    Calls Qt's 'void QDeclarativeGeoRouteModel::pluginReady()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeoroutemodel.html#pluginReady
    """
    #  void QDeclarativeGeoRouteModel::pluginReady()
    self.uglySide.call('ritual_ZN25QDeclarativeGeoRouteModel11pluginReadyEv')
