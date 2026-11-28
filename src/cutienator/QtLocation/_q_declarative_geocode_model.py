"""
QDeclarativeGeocodeModel binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtLocation/6.12.0/QtLocation/private/qdeclarativegeocodemodel_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QDeclarativeGeocodeModel to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import QAbstractListModel, QHash, QList, QObject
from ..QtQml import QQmlParserStatus
from . import QGeoCodeReply

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QByteArray, QMetaObject, QModelIndex, QVariant
  from ..QtPositioning import QGeoLocation
  from ..QtPositioningQuick import QDeclarativeGeoLocation
  from . import QDeclarativeGeoServiceProvider
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDeclarativeGeoServiceProvider = WAIT['QDeclarativeGeoServiceProvider']
  QGeoLocation = WAIT['QGeoLocation']
  QModelIndex = WAIT['QModelIndex']
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QDeclarativeGeocodeModel(QAbstractListModel, QQmlParserStatus):
  """
  The cute side of Qt's QDeclarativeGeocodeModel: a plain Python object
  standing in front of one C++ QDeclarativeGeocodeModel.

  It is built on the cute 'QAbstractListModel', as Qt's
  QDeclarativeGeocodeModel is built on Qt's QAbstractListModel, and has
  everything that class has. It is built on the cute 'QQmlParserStatus' as
  well, as Qt's QDeclarativeGeocodeModel is built on Qt's QQmlParserStatus
  too, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QDeclarativeGeocodeModel that has a ritual and that
  Python can call so far, 45 names in all: 'metaObject', 'tr', 'classBegin',
  'componentComplete', 'rowCount', 'data', 'roleNames', 'setPlugin',
  'plugin', 'setBounds', 'bounds', 'status', 'errorString', 'error',
  'autoUpdate', 'setAutoUpdate', 'count', 'get', 'limit', 'setLimit',
  'offset', 'setOffset', 'query', 'setQuery', 'reset', 'cancel',
  'countChanged', 'pluginChanged', 'statusChanged', 'errorChanged',
  'locationsChanged', 'autoUpdateChanged', 'boundsChanged', 'queryChanged',
  'limitChanged', 'offsetChanged', 'update', 'queryContentChanged',
  'geocodeFinished', 'geocodeError', 'pluginReady', 'setStatus', 'setError',
  'setLocations', 'abortRequest'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QDeclarativeGeocodeModel::qt_metacast(const char *a0)': one
    of Qt's own inner workings.
  - Qt's 'int QDeclarativeGeocodeModel::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QDeclarativeGeocodeModel::~QDeclarativeGeocodeModel()': the
    destructor: Python never removes a C++ QDeclarativeGeocodeModel.

  What has no ritual
  ------------------

  3 of the 52 functions Qt declares: 2 not a gap; 1 cannot be called and
  cannot be called through the meta-object and cannot be copied.

  What to expect
  --------------

  - The C++ QDeclarativeGeocodeModel is created at the first use, not by
    'QDeclarativeGeocodeModel(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QDeclarativeGeocodeModel.
  - Qt tells when it has removed the C++ QDeclarativeGeocodeModel. Every call
    on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QDeclarativeGeocodeModel that has no cute function yet,
    'searchManager', holds a function that raises 'NotImplementedError', and
    its docstring says why.
  """

  #  The enums Qt writes inside QDeclarativeGeocodeModel, each a class in
  #  here as in C++, and the names Qt has for the combinations of its flags
  #  enums.

  class GeocodeError(CuteNum):
    """
    The enum 'QDeclarativeGeocodeModel::GeocodeError' of Qt, with the 9 names
    Qt gives in it.
    """

    NoError = Kee[int](0)
    EngineNotSetError = Kee[int](1)
    CommunicationError = Kee[int](2)
    ParseError = Kee[int](3)
    UnsupportedOptionError = Kee[int](4)
    CombinationError = Kee[int](5)
    UnknownError = Kee[int](6)
    UnknownParameterError = Kee[int](100)
    MissingRequiredParameterError = Kee[int](101)

  class Roles(CuteNum):
    """
    The enum 'QDeclarativeGeocodeModel::Roles' of Qt, with the 1 names Qt
    gives in it.
    """

    LocationRole = Kee[int](257)

  class Status(CuteNum):
    """
    The enum 'QDeclarativeGeocodeModel::Status' of Qt, with the 4 names Qt
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
    Calls Qt's 'QString QDeclarativeGeocodeModel::tr(const char *s, const
    char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qdeclarativegeocodemodel.html#tr

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
    #  QString QDeclarativeGeocodeModel::tr(const char *s, const char *c, int
    #      n)
    return Rituals.call(
        'ritual_ZN24QDeclarativeGeocodeModel2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QDeclarativeGeocodeModel'

  #  Qt's QDeclarativeGeocodeModel is built on more than one class. The part
  #  of a C++ QDeclarativeGeocodeModel that belongs to a class after the
  #  first begins somewhere inside the object, and the ritual named for that
  #  class gives where; see 'CuteMixin._addressAs'.
  __cast_rituals__ = {
      'QQmlParserStatus':
          'ritual_cast_QDeclarativeGeocodeModel_QQmlParserStatus',
  }

  #  A C++ QDeclarativeGeocodeModel Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QDeclarativeGeocodeModel'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QDeclarativeGeocodeModel::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeocodemodel.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QDeclarativeGeocodeModel::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK24QDeclarativeGeocodeModel10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  @overload(QModelIndex)
  def rowCount(self, parent: QModelIndex) -> int:
    """
    Calls Qt's 'int QDeclarativeGeocodeModel::rowCount(const QModelIndex
    &parent) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeocodemodel.html#rowCount

    Parameters
    ----------

    parent : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.
    """
    #  int QDeclarativeGeocodeModel::rowCount(const QModelIndex &parent)
    #      const
    ritual = 'ritual_ZNK24QDeclarativeGeocodeModel8rowCountERK11QModelIndex'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK24QDeclarativeGeocodeModel8rowCountERK11QModelInde'
          'x')
    return self.uglySide.call(ritual, self._valueOf(parent))

  @overload(QModelIndex, int)
  def data(self, index: QModelIndex, role: int) -> QVariant:
    """
    Calls Qt's 'QVariant QDeclarativeGeocodeModel::data(const QModelIndex
    &index, int role) const'.

    Qt's own words: https://doc.qt.io/qt-6/qdeclarativegeocodemodel.html#data

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
    #  QVariant QDeclarativeGeocodeModel::data(const QModelIndex &index, int
    #      role) const
    ritual = 'ritual_ZNK24QDeclarativeGeocodeModel4dataERK11QModelIndexi'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK24QDeclarativeGeocodeModel4dataERK11QModelIndexi')
    address = self.uglySide.call(ritual, self._valueOf(index), role)
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  def roleNames(self) -> QHash[int, QByteArray]:
    """
    Calls Qt's 'QHash<int, QByteArray> QDeclarativeGeocodeModel::roleNames()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeocodemodel.html#roleNames

    Returns
    -------

    QHash[int, QByteArray]
      A new cute map around the copy Qt gave back. Python owns it.
    """
    #  QHash<int, QByteArray> QDeclarativeGeocodeModel::roleNames() const
    address = self.uglySide.call(
        'ritual_ZNK24QDeclarativeGeocodeModel9roleNamesEv',
    )
    from ..QtCore import QByteArray
    return QHash[int, QByteArray]._cuteOwning(address)

  def plugin(self) -> Optional[QDeclarativeGeoServiceProvider]:
    """
    Calls Qt's 'QDeclarativeGeoServiceProvider
    *QDeclarativeGeocodeModel::plugin() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeocodemodel.html#plugin

    Returns
    -------

    Optional[QDeclarativeGeoServiceProvider]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QDeclarativeGeoServiceProvider *QDeclarativeGeocodeModel::plugin()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK24QDeclarativeGeocodeModel6pluginEv',
    )
    from . import QDeclarativeGeoServiceProvider
    return QDeclarativeGeoServiceProvider._cuteAt(address)

  def bounds(self) -> QVariant:
    """
    Calls Qt's 'QVariant QDeclarativeGeocodeModel::bounds() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeocodemodel.html#bounds

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QDeclarativeGeocodeModel::bounds() const
    address = self.uglySide.call(
        'ritual_ZNK24QDeclarativeGeocodeModel6boundsEv',
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  def status(self) -> Status:
    """
    Calls Qt's 'Status QDeclarativeGeocodeModel::status() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeocodemodel.html#status

    Returns
    -------

    Status
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Status(number)' gives.
    """
    #  Status QDeclarativeGeocodeModel::status() const
    return QDeclarativeGeocodeModel.Status(self.uglySide.call(
        'ritual_ZNK24QDeclarativeGeocodeModel6statusEv',
    ))

  def errorString(self) -> str:
    """
    Calls Qt's 'QString QDeclarativeGeocodeModel::errorString() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeocodemodel.html#errorString

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QDeclarativeGeocodeModel::errorString() const
    return self.uglySide.call(
        'ritual_ZNK24QDeclarativeGeocodeModel11errorStringEv',
    )

  def error(self) -> GeocodeError:
    """
    Calls Qt's 'GeocodeError QDeclarativeGeocodeModel::error() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeocodemodel.html#error

    Returns
    -------

    GeocodeError
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'GeocodeError(number)'
      gives.
    """
    #  GeocodeError QDeclarativeGeocodeModel::error() const
    return QDeclarativeGeocodeModel.GeocodeError(self.uglySide.call(
        'ritual_ZNK24QDeclarativeGeocodeModel5errorEv',
    ))

  def autoUpdate(self) -> bool:
    """
    Calls Qt's 'bool QDeclarativeGeocodeModel::autoUpdate() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeocodemodel.html#autoUpdate
    """
    #  bool QDeclarativeGeocodeModel::autoUpdate() const
    return self.uglySide.call(
        'ritual_ZNK24QDeclarativeGeocodeModel10autoUpdateEv',
    )

  def count(self) -> int:
    """
    Calls Qt's 'int QDeclarativeGeocodeModel::count() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeocodemodel.html#count
    """
    #  int QDeclarativeGeocodeModel::count() const
    return self.uglySide.call('ritual_ZNK24QDeclarativeGeocodeModel5countEv')

  def limit(self) -> int:
    """
    Calls Qt's 'int QDeclarativeGeocodeModel::limit() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeocodemodel.html#limit
    """
    #  int QDeclarativeGeocodeModel::limit() const
    return self.uglySide.call('ritual_ZNK24QDeclarativeGeocodeModel5limitEv')

  def offset(self) -> int:
    """
    Calls Qt's 'int QDeclarativeGeocodeModel::offset() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeocodemodel.html#offset
    """
    #  int QDeclarativeGeocodeModel::offset() const
    return self.uglySide.call(
        'ritual_ZNK24QDeclarativeGeocodeModel6offsetEv',
    )

  def query(self) -> QVariant:
    """
    Calls Qt's 'QVariant QDeclarativeGeocodeModel::query() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeocodemodel.html#query

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QDeclarativeGeocodeModel::query() const
    address = self.uglySide.call(
        'ritual_ZNK24QDeclarativeGeocodeModel5queryEv',
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

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
    QDeclarativeGeocodeModel::setPlugin(QDeclarativeGeoServiceProvider
    *plugin)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeocodemodel.html#setPlugin

    Parameters
    ----------

    plugin : Optional[QDeclarativeGeoServiceProvider]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void
    #      QDeclarativeGeocodeModel::setPlugin(QDeclarativeGeoServiceProvider
    #      *plugin)
    self.uglySide.call(
        'ritual_ZN24QDeclarativeGeocodeModel9setPluginEP30QDeclarativeGeoSe'
        'rviceProvider',
        self._addressOf(plugin),
    )

  @overload(QVariant)
  def setBounds(self, boundingArea: QVariant) -> None:
    """
    Calls Qt's 'void QDeclarativeGeocodeModel::setBounds(const QVariant
    &boundingArea)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeocodemodel.html#setBounds

    Parameters
    ----------

    boundingArea : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void QDeclarativeGeocodeModel::setBounds(const QVariant &boundingArea)
    self.uglySide.call(
        'ritual_ZN24QDeclarativeGeocodeModel9setBoundsERK8QVariant',
        self._valueOf(boundingArea),
    )

  @overload(bool)
  def setAutoUpdate(self, update: bool) -> None:
    """
    Calls Qt's 'void QDeclarativeGeocodeModel::setAutoUpdate(bool update)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeocodemodel.html#setAutoUpdate

    Parameters
    ----------

    update : bool
      Passed on as it is.
    """
    #  void QDeclarativeGeocodeModel::setAutoUpdate(bool update)
    self.uglySide.call(
        'ritual_ZN24QDeclarativeGeocodeModel13setAutoUpdateEb', update,
    )

  @overload(int)
  def setLimit(self, limit: int) -> None:
    """
    Calls Qt's 'void QDeclarativeGeocodeModel::setLimit(int limit)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeocodemodel.html#setLimit

    Parameters
    ----------

    limit : int
      Passed on as it is.
    """
    #  void QDeclarativeGeocodeModel::setLimit(int limit)
    self.uglySide.call(
        'ritual_ZN24QDeclarativeGeocodeModel8setLimitEi', limit,
    )

  @overload(int)
  def setOffset(self, offset: int) -> None:
    """
    Calls Qt's 'void QDeclarativeGeocodeModel::setOffset(int offset)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeocodemodel.html#setOffset

    Parameters
    ----------

    offset : int
      Passed on as it is.
    """
    #  void QDeclarativeGeocodeModel::setOffset(int offset)
    self.uglySide.call(
        'ritual_ZN24QDeclarativeGeocodeModel9setOffsetEi', offset,
    )

  @overload(QVariant)
  def setQuery(self, query: QVariant) -> None:
    """
    Calls Qt's 'void QDeclarativeGeocodeModel::setQuery(const QVariant
    &query)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeocodemodel.html#setQuery

    Parameters
    ----------

    query : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void QDeclarativeGeocodeModel::setQuery(const QVariant &query)
    self.uglySide.call(
        'ritual_ZN24QDeclarativeGeocodeModel8setQueryERK8QVariant',
        self._valueOf(query),
    )

  @overload(Status)
  def setStatus(self, status: Status) -> None:
    """
    Calls Qt's 'void QDeclarativeGeocodeModel::setStatus(Status status)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeocodemodel.html#setStatus

    Parameters
    ----------

    status : Status
      Passed on as its number.
    """
    #  void QDeclarativeGeocodeModel::setStatus(Status status)
    self.uglySide.call(
        'ritual_ZN24QDeclarativeGeocodeModel9setStatusENS_6StatusE',
        status.value,
    )

  @overload(GeocodeError, str)
  def setError(self, error: GeocodeError, errorString: str) -> None:
    """
    Calls Qt's 'void QDeclarativeGeocodeModel::setError(GeocodeError error,
    const QString &errorString)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeocodemodel.html#setError

    Parameters
    ----------

    error : GeocodeError
      Passed on as its number.

    errorString : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QDeclarativeGeocodeModel::setError(GeocodeError error, const
    #      QString &errorString)
    self.uglySide.call(
        'ritual_ZN24QDeclarativeGeocodeModel8setErrorENS_12GeocodeErrorERK7'
        'QString',
        error.value, errorString,
    )

  @overload(QList[QGeoLocation])
  def setLocations(self, locations: QList[QGeoLocation]) -> None:
    """
    Calls Qt's 'void QDeclarativeGeocodeModel::setLocations(const
    QList<QGeoLocation> &locations)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeocodemodel.html#setLocations

    Parameters
    ----------

    locations : QList[QGeoLocation]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QDeclarativeGeocodeModel::setLocations(const QList<QGeoLocation>
    #      &locations)
    self.uglySide.call(
        'ritual_ZN24QDeclarativeGeocodeModel12setLocationsERK5QListI12QGeoL'
        'ocationE',
        self._valueOf(locations),
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
    'QDeclarativeGeocodeModel::QDeclarativeGeocodeModel(QObject *parent)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeocodemodel.html

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QDeclarativeGeocodeModel::QDeclarativeGeocodeModel(QObject *parent)
    self._noteCreation(QDeclarativeGeocodeModel, lambda: Rituals.call(
        'ritual_ZN24QDeclarativeGeocodeModelC1EP7QObject',
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
    Calls Qt's 'void QDeclarativeGeocodeModel::classBegin()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeocodemodel.html#classBegin
    """
    #  void QDeclarativeGeocodeModel::classBegin()
    ritual = 'ritual_ZN24QDeclarativeGeocodeModel10classBeginEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN24QDeclarativeGeocodeModel10classBeginEv'
    self.uglySide.call(ritual)

  def componentComplete(self) -> None:
    """
    Calls Qt's 'void QDeclarativeGeocodeModel::componentComplete()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeocodemodel.html#componentComplete
    """
    #  void QDeclarativeGeocodeModel::componentComplete()
    ritual = 'ritual_ZN24QDeclarativeGeocodeModel17componentCompleteEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN24QDeclarativeGeocodeModel17componentCompleteEv'
    self.uglySide.call(ritual)

  @overload(int)
  def get(self, index: int) -> Optional[QDeclarativeGeoLocation]:
    """
    Calls Qt's 'QDeclarativeGeoLocation *QDeclarativeGeocodeModel::get(int
    index)'.

    Qt's own words: https://doc.qt.io/qt-6/qdeclarativegeocodemodel.html#get

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    Optional[QDeclarativeGeoLocation]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QDeclarativeGeoLocation *QDeclarativeGeocodeModel::get(int index)
    address = self.uglySide.call(
        'ritual_ZN24QDeclarativeGeocodeModel3getEi', index,
    )
    from ..QtPositioningQuick import QDeclarativeGeoLocation
    return QDeclarativeGeoLocation._cuteAt(address)

  def reset(self) -> None:
    """
    Calls Qt's 'void QDeclarativeGeocodeModel::reset()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeocodemodel.html#reset
    """
    #  void QDeclarativeGeocodeModel::reset()
    self.uglySide.call('ritual_ZN24QDeclarativeGeocodeModel5resetEv')

  def cancel(self) -> None:
    """
    Calls Qt's 'void QDeclarativeGeocodeModel::cancel()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeocodemodel.html#cancel
    """
    #  void QDeclarativeGeocodeModel::cancel()
    self.uglySide.call('ritual_ZN24QDeclarativeGeocodeModel6cancelEv')

  def countChanged(self) -> None:
    """
    Calls Qt's 'void QDeclarativeGeocodeModel::countChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeocodemodel.html#countChanged
    """
    #  void QDeclarativeGeocodeModel::countChanged()
    self.uglySide.call('ritual_ZN24QDeclarativeGeocodeModel12countChangedEv')

  def pluginChanged(self) -> None:
    """
    Calls Qt's 'void QDeclarativeGeocodeModel::pluginChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeocodemodel.html#pluginChanged
    """
    #  void QDeclarativeGeocodeModel::pluginChanged()
    self.uglySide.call(
        'ritual_ZN24QDeclarativeGeocodeModel13pluginChangedEv',
    )

  def statusChanged(self) -> None:
    """
    Calls Qt's 'void QDeclarativeGeocodeModel::statusChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeocodemodel.html#statusChanged
    """
    #  void QDeclarativeGeocodeModel::statusChanged()
    self.uglySide.call(
        'ritual_ZN24QDeclarativeGeocodeModel13statusChangedEv',
    )

  def errorChanged(self) -> None:
    """
    Calls Qt's 'void QDeclarativeGeocodeModel::errorChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeocodemodel.html#errorChanged
    """
    #  void QDeclarativeGeocodeModel::errorChanged()
    self.uglySide.call('ritual_ZN24QDeclarativeGeocodeModel12errorChangedEv')

  def locationsChanged(self) -> None:
    """
    Calls Qt's 'void QDeclarativeGeocodeModel::locationsChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeocodemodel.html#locationsChanged
    """
    #  void QDeclarativeGeocodeModel::locationsChanged()
    self.uglySide.call(
        'ritual_ZN24QDeclarativeGeocodeModel16locationsChangedEv',
    )

  def autoUpdateChanged(self) -> None:
    """
    Calls Qt's 'void QDeclarativeGeocodeModel::autoUpdateChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeocodemodel.html#autoUpdateChanged
    """
    #  void QDeclarativeGeocodeModel::autoUpdateChanged()
    self.uglySide.call(
        'ritual_ZN24QDeclarativeGeocodeModel17autoUpdateChangedEv',
    )

  def boundsChanged(self) -> None:
    """
    Calls Qt's 'void QDeclarativeGeocodeModel::boundsChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeocodemodel.html#boundsChanged
    """
    #  void QDeclarativeGeocodeModel::boundsChanged()
    self.uglySide.call(
        'ritual_ZN24QDeclarativeGeocodeModel13boundsChangedEv',
    )

  def queryChanged(self) -> None:
    """
    Calls Qt's 'void QDeclarativeGeocodeModel::queryChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeocodemodel.html#queryChanged
    """
    #  void QDeclarativeGeocodeModel::queryChanged()
    self.uglySide.call('ritual_ZN24QDeclarativeGeocodeModel12queryChangedEv')

  def limitChanged(self) -> None:
    """
    Calls Qt's 'void QDeclarativeGeocodeModel::limitChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeocodemodel.html#limitChanged
    """
    #  void QDeclarativeGeocodeModel::limitChanged()
    self.uglySide.call('ritual_ZN24QDeclarativeGeocodeModel12limitChangedEv')

  def offsetChanged(self) -> None:
    """
    Calls Qt's 'void QDeclarativeGeocodeModel::offsetChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeocodemodel.html#offsetChanged
    """
    #  void QDeclarativeGeocodeModel::offsetChanged()
    self.uglySide.call(
        'ritual_ZN24QDeclarativeGeocodeModel13offsetChangedEv',
    )

  def update(self) -> None:
    """
    Calls Qt's 'void QDeclarativeGeocodeModel::update()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeocodemodel.html#update
    """
    #  void QDeclarativeGeocodeModel::update()
    self.uglySide.call('ritual_ZN24QDeclarativeGeocodeModel6updateEv')

  def queryContentChanged(self) -> None:
    """
    Calls Qt's 'void QDeclarativeGeocodeModel::queryContentChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeocodemodel.html#queryContentChanged
    """
    #  void QDeclarativeGeocodeModel::queryContentChanged()
    self.uglySide.call(
        'ritual_ZN24QDeclarativeGeocodeModel19queryContentChangedEv',
    )

  @overload(QGeoCodeReply)
  @overload(NoneType)
  def geocodeFinished(self, reply: Optional[QGeoCodeReply]) -> None:
    """
    Calls Qt's 'void QDeclarativeGeocodeModel::geocodeFinished(QGeoCodeReply
    *reply)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeocodemodel.html#geocodeFinished

    Parameters
    ----------

    reply : Optional[QGeoCodeReply]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QDeclarativeGeocodeModel::geocodeFinished(QGeoCodeReply *reply)
    self.uglySide.call(
        'ritual_ZN24QDeclarativeGeocodeModel15geocodeFinishedEP13QGeoCodeRe'
        'ply',
        self._addressOf(reply),
    )

  @overload(QGeoCodeReply, QGeoCodeReply.Error, str)
  @overload(NoneType, QGeoCodeReply.Error, str)
  def geocodeError(
      self,
      reply: Optional[QGeoCodeReply],
      error: QGeoCodeReply.Error,
      errorString: str,
  ) -> None:
    """
    Calls Qt's 'void QDeclarativeGeocodeModel::geocodeError(QGeoCodeReply
    *reply, QGeoCodeReply::Error error, const QString &errorString)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeocodemodel.html#geocodeError

    Parameters
    ----------

    reply : Optional[QGeoCodeReply]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    error : QGeoCodeReply.Error
      Passed on as its number.

    errorString : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QDeclarativeGeocodeModel::geocodeError(QGeoCodeReply *reply,
    #      QGeoCodeReply::Error error, const QString &errorString)
    self.uglySide.call(
        'ritual_ZN24QDeclarativeGeocodeModel12geocodeErrorEP13QGeoCodeReply'
        'NS0_5ErrorERK7QString',
        self._addressOf(reply), error.value, errorString,
    )

  def pluginReady(self) -> None:
    """
    Calls Qt's 'void QDeclarativeGeocodeModel::pluginReady()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeocodemodel.html#pluginReady
    """
    #  void QDeclarativeGeocodeModel::pluginReady()
    self.uglySide.call('ritual_ZN24QDeclarativeGeocodeModel11pluginReadyEv')

  def abortRequest(self) -> None:
    """
    Calls Qt's 'void QDeclarativeGeocodeModel::abortRequest()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeocodemodel.html#abortRequest
    """
    #  void QDeclarativeGeocodeModel::abortRequest()
    self.uglySide.call('ritual_ZN24QDeclarativeGeocodeModel12abortRequestEv')

  @staticmethod
  def searchManager(*__, **_) -> Never:
    """
    Qt's 'QGeoCodingManager *QDeclarativeGeocodeModel::searchManager()':
    cannot be called and cannot be called through the meta-object and cannot
    be copied: no header file has its code, Qt's source does not mark it or
    its class for use from outside Qt or writes it 'inline' or nowhere, and
    it is no signal, slot or invokable function giving back nothing, of a
    class built on QObject, and Qt's source has no code for it that could be
    told from the rest.
    """
    raise NotImplementedError(
        "'QDeclarativeGeocodeModel.searchManager' has no cute function yet. "
        "Qt's 'QGeoCodingManager "
        "*QDeclarativeGeocodeModel::searchManager()': cannot be called and "
        "cannot be called through the meta-object and cannot be copied: no "
        "header file has its code, Qt's source does not mark it or its "
        "class for use from outside Qt or writes it 'inline' or nowhere, "
        "and it is no signal, slot or invokable function giving back "
        "nothing, of a class built on QObject, and Qt's source has no code "
        "for it that could be told from the rest.")
