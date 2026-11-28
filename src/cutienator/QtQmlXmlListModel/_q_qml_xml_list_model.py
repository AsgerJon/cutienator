"""
QQmlXmlListModel binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQmlXmlListModel/6.12.0/QtQmlXmlListModel/private/qqmlxmllistmodel_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQmlXmlListModel to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import QAbstractListModel, QHash, QObject
from ..QtQml import QQmlParserStatus

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QByteArray, QMetaObject, QModelIndex, QUrl, QVariant
  from . import QQmlXmlListModelQueryJob, QQmlXmlListModelQueryResult
  from . import QQmlXmlListModelRole
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']
  QModelIndex = WAIT['QModelIndex']
  QQmlXmlListModelQueryResult = WAIT['QQmlXmlListModelQueryResult']
  QQmlXmlListModelRole = WAIT['QQmlXmlListModelRole']
  QUrl = WAIT['QUrl']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQmlXmlListModel(QAbstractListModel, QQmlParserStatus):
  """
  The cute side of Qt's QQmlXmlListModel: a plain Python object standing in
  front of one C++ QQmlXmlListModel.

  It is built on the cute 'QAbstractListModel', as Qt's QQmlXmlListModel is
  built on Qt's QAbstractListModel, and has everything that class has. It is
  built on the cute 'QQmlParserStatus' as well, as Qt's QQmlXmlListModel is
  built on Qt's QQmlParserStatus too, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQmlXmlListModel that has a ritual and that Python
  can call so far, 33 names in all: 'metaObject', 'tr', 'index', 'rowCount',
  'data', 'roleNames', 'count', 'source', 'setSource', 'query', 'setQuery',
  'appendRole', 'clearRole', 'status', 'progress', 'errorString',
  'classBegin', 'componentComplete', 'statusChanged', 'progressChanged',
  'countChanged', 'sourceChanged', 'queryChanged', 'reload',
  'requestFinished', 'requestProgress', 'dataCleared', 'queryCompleted',
  'notifyQueryStarted', 'tryExecuteQuery', 'createJob', 'nextQueryId',
  'deleteReply'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQmlXmlListModel::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QQmlXmlListModel::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QQmlXmlListModel::~QQmlXmlListModel()': the destructor: Python
    never removes a C++ QQmlXmlListModel.
  - Qt's 'QQmlListProperty<QQmlXmlListModelRole>
    QQmlXmlListModel::roleObjects()': gives a type Python has no way to take
    yet.
  - Qt's 'void QQmlXmlListModel::queryError(void *object, const QString
    &error)': names 'void', which has no cute class yet.
  - Qt's 'void
    QQmlXmlListModel::appendRole(QQmlListProperty<QQmlXmlListModelRole> *a0,
    QQmlXmlListModelRole *a1)': names
    'QQmlListProperty<QQmlXmlListModelRole>', which has no cute class yet.
  - Qt's 'void
    QQmlXmlListModel::clearRole(QQmlListProperty<QQmlXmlListModelRole> *a0)':
    names 'QQmlListProperty<QQmlXmlListModelRole>', which has no cute class
    yet.

  What has no ritual
  ------------------

  4 of the 45 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QQmlXmlListModel is created at the first use, not by
    'QQmlXmlListModel(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQmlXmlListModel.
  - Qt tells when it has removed the C++ QQmlXmlListModel. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQmlXmlListModel that has no cute function yet,
    'queryError', 'roleObjects', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QQmlXmlListModel, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class Status(CuteNum):
    """
    The enum 'QQmlXmlListModel::Status' of Qt, with the 4 names Qt gives in
    it.
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
    Calls Qt's 'QString QQmlXmlListModel::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlxmllistmodel.html#tr

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
    #  QString QQmlXmlListModel::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN16QQmlXmlListModel2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlXmlListModel'

  #  Qt's QQmlXmlListModel is built on more than one class. The part of a C++
  #  QQmlXmlListModel that belongs to a class after the first begins
  #  somewhere inside the object, and the ritual named for that class gives
  #  where; see 'CuteMixin._addressAs'.
  __cast_rituals__ = {
      'QQmlParserStatus': 'ritual_cast_QQmlXmlListModel_QQmlParserStatus',
  }

  #  A C++ QQmlXmlListModel Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQmlXmlListModel'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQmlXmlListModel::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlxmllistmodel.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQmlXmlListModel::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK16QQmlXmlListModel10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  @overload(int, int, QModelIndex)
  def index(self, row: int, column: int, parent: QModelIndex) -> QModelIndex:
    """
    Calls Qt's 'QModelIndex QQmlXmlListModel::index(int row, int column,
    const QModelIndex &parent) const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlxmllistmodel.html#index

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
    #  QModelIndex QQmlXmlListModel::index(int row, int column, const
    #      QModelIndex &parent) const
    ritual = 'ritual_ZNK16QQmlXmlListModel5indexEiiRK11QModelIndex'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK16QQmlXmlListModel5indexEiiRK11QModelIndex'
    address = self.uglySide.call(ritual, row, column, self._valueOf(parent))
    from ..QtCore import QModelIndex
    return QModelIndex._cuteOwning(address)

  @overload(QModelIndex)
  def rowCount(self, parent: QModelIndex) -> int:
    """
    Calls Qt's 'int QQmlXmlListModel::rowCount(const QModelIndex &parent)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlxmllistmodel.html#rowCount

    Parameters
    ----------

    parent : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.
    """
    #  int QQmlXmlListModel::rowCount(const QModelIndex &parent) const
    ritual = 'ritual_ZNK16QQmlXmlListModel8rowCountERK11QModelIndex'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK16QQmlXmlListModel8rowCountERK11QModelIndex'
    return self.uglySide.call(ritual, self._valueOf(parent))

  @overload(QModelIndex, int)
  def data(self, index: QModelIndex, role: int) -> QVariant:
    """
    Calls Qt's 'QVariant QQmlXmlListModel::data(const QModelIndex &index, int
    role) const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlxmllistmodel.html#data

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
    #  QVariant QQmlXmlListModel::data(const QModelIndex &index, int role)
    #      const
    ritual = 'ritual_ZNK16QQmlXmlListModel4dataERK11QModelIndexi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK16QQmlXmlListModel4dataERK11QModelIndexi'
    address = self.uglySide.call(ritual, self._valueOf(index), role)
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  def roleNames(self) -> QHash[int, QByteArray]:
    """
    Calls Qt's 'QHash<int, QByteArray> QQmlXmlListModel::roleNames() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlxmllistmodel.html#roleNames

    Returns
    -------

    QHash[int, QByteArray]
      A new cute map around the copy Qt gave back. Python owns it.
    """
    #  QHash<int, QByteArray> QQmlXmlListModel::roleNames() const
    address = self.uglySide.call('ritual_ZNK16QQmlXmlListModel9roleNamesEv')
    from ..QtCore import QByteArray
    return QHash[int, QByteArray]._cuteOwning(address)

  def count(self) -> int:
    """
    Calls Qt's 'int QQmlXmlListModel::count() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlxmllistmodel.html#count
    """
    #  int QQmlXmlListModel::count() const
    return self.uglySide.call('ritual_ZNK16QQmlXmlListModel5countEv')

  def source(self) -> QUrl:
    """
    Calls Qt's 'QUrl QQmlXmlListModel::source() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlxmllistmodel.html#source

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QQmlXmlListModel::source() const
    address = self.uglySide.call('ritual_ZNK16QQmlXmlListModel6sourceEv')
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  def query(self) -> str:
    """
    Calls Qt's 'QString QQmlXmlListModel::query() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlxmllistmodel.html#query

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlXmlListModel::query() const
    return self.uglySide.call('ritual_ZNK16QQmlXmlListModel5queryEv')

  def status(self) -> Status:
    """
    Calls Qt's 'Status QQmlXmlListModel::status() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlxmllistmodel.html#status

    Returns
    -------

    Status
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Status(number)' gives.
    """
    #  Status QQmlXmlListModel::status() const
    return QQmlXmlListModel.Status(self.uglySide.call(
        'ritual_ZNK16QQmlXmlListModel6statusEv',
    ))

  def progress(self) -> float:
    """
    Calls Qt's 'qreal QQmlXmlListModel::progress() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlxmllistmodel.html#progress
    """
    #  qreal QQmlXmlListModel::progress() const
    return self.uglySide.call('ritual_ZNK16QQmlXmlListModel8progressEv')

  def errorString(self) -> str:
    """
    Calls Qt's 'QString QQmlXmlListModel::errorString() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlxmllistmodel.html#errorString

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlXmlListModel::errorString() const
    return self.uglySide.call('ritual_ZNK16QQmlXmlListModel11errorStringEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QUrl)
  def setSource(self, a0: QUrl) -> None:
    """
    Calls Qt's 'void QQmlXmlListModel::setSource(const QUrl &a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlxmllistmodel.html#setSource

    Parameters
    ----------

    a0 : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  void QQmlXmlListModel::setSource(const QUrl &a0)
    self.uglySide.call(
        'ritual_ZN16QQmlXmlListModel9setSourceERK4QUrl', self._valueOf(a0),
    )

  @overload(str)
  def setQuery(self, a0: str) -> None:
    """
    Calls Qt's 'void QQmlXmlListModel::setQuery(const QString &a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlxmllistmodel.html#setQuery

    Parameters
    ----------

    a0 : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQmlXmlListModel::setQuery(const QString &a0)
    self.uglySide.call('ritual_ZN16QQmlXmlListModel8setQueryERK7QString', a0)

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
    'QQmlXmlListModel::QQmlXmlListModel(QObject *parent)', which is called at
    the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlxmllistmodel.html#QQmlXmlListModel

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQmlXmlListModel::QQmlXmlListModel(QObject *parent)
    self._noteCreation(QQmlXmlListModel, lambda: Rituals.call(
        'ritual_ZN16QQmlXmlListModelC1EP7QObject',
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

  @overload(QQmlXmlListModelRole)
  @overload(NoneType)
  def appendRole(self, a0: Optional[QQmlXmlListModelRole]) -> None:
    """
    Calls Qt's 'void QQmlXmlListModel::appendRole(QQmlXmlListModelRole *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlxmllistmodel.html#appendRole

    Parameters
    ----------

    a0 : Optional[QQmlXmlListModelRole]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlXmlListModel::appendRole(QQmlXmlListModelRole *a0)
    self.uglySide.call(
        'ritual_ZN16QQmlXmlListModel10appendRoleEP20QQmlXmlListModelRole',
        self._addressOf(a0),
    )

  def clearRole(self) -> None:
    """
    Calls Qt's 'void QQmlXmlListModel::clearRole()'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlxmllistmodel.html#clearRole
    """
    #  void QQmlXmlListModel::clearRole()
    self.uglySide.call('ritual_ZN16QQmlXmlListModel9clearRoleEv')

  def classBegin(self) -> None:
    """
    Calls Qt's 'void QQmlXmlListModel::classBegin()'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlxmllistmodel.html#classBegin
    """
    #  void QQmlXmlListModel::classBegin()
    ritual = 'ritual_ZN16QQmlXmlListModel10classBeginEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN16QQmlXmlListModel10classBeginEv'
    self.uglySide.call(ritual)

  def componentComplete(self) -> None:
    """
    Calls Qt's 'void QQmlXmlListModel::componentComplete()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlxmllistmodel.html#componentComplete
    """
    #  void QQmlXmlListModel::componentComplete()
    ritual = 'ritual_ZN16QQmlXmlListModel17componentCompleteEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN16QQmlXmlListModel17componentCompleteEv'
    self.uglySide.call(ritual)

  @overload(Status)
  def statusChanged(self, a0: Status) -> None:
    """
    Calls Qt's 'void QQmlXmlListModel::statusChanged(QQmlXmlListModel::Status
    a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlxmllistmodel.html#statusChanged

    Parameters
    ----------

    a0 : Status
      Passed on as its number.
    """
    #  void QQmlXmlListModel::statusChanged(QQmlXmlListModel::Status a0)
    self.uglySide.call(
        'ritual_ZN16QQmlXmlListModel13statusChangedENS_6StatusE', a0.value,
    )

  @overload(float)
  def progressChanged(self, progress: float) -> None:
    """
    Calls Qt's 'void QQmlXmlListModel::progressChanged(qreal progress)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlxmllistmodel.html#progressChanged

    Parameters
    ----------

    progress : float
      Passed on as it is.
    """
    #  void QQmlXmlListModel::progressChanged(qreal progress)
    self.uglySide.call(
        'ritual_ZN16QQmlXmlListModel15progressChangedEd', progress,
    )

  def countChanged(self) -> None:
    """
    Calls Qt's 'void QQmlXmlListModel::countChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlxmllistmodel.html#countChanged
    """
    #  void QQmlXmlListModel::countChanged()
    self.uglySide.call('ritual_ZN16QQmlXmlListModel12countChangedEv')

  def sourceChanged(self) -> None:
    """
    Calls Qt's 'void QQmlXmlListModel::sourceChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlxmllistmodel.html#sourceChanged
    """
    #  void QQmlXmlListModel::sourceChanged()
    self.uglySide.call('ritual_ZN16QQmlXmlListModel13sourceChangedEv')

  def queryChanged(self) -> None:
    """
    Calls Qt's 'void QQmlXmlListModel::queryChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlxmllistmodel.html#queryChanged
    """
    #  void QQmlXmlListModel::queryChanged()
    self.uglySide.call('ritual_ZN16QQmlXmlListModel12queryChangedEv')

  def reload(self) -> None:
    """
    Calls Qt's 'void QQmlXmlListModel::reload()'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlxmllistmodel.html#reload
    """
    #  void QQmlXmlListModel::reload()
    self.uglySide.call('ritual_ZN16QQmlXmlListModel6reloadEv')

  def requestFinished(self) -> None:
    """
    Calls Qt's 'void QQmlXmlListModel::requestFinished()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlxmllistmodel.html#requestFinished
    """
    #  void QQmlXmlListModel::requestFinished()
    self.uglySide.call('ritual_ZN16QQmlXmlListModel15requestFinishedEv')

  @overload(int, int)
  def requestProgress(self, a0: int, a1: int) -> None:
    """
    Calls Qt's 'void QQmlXmlListModel::requestProgress(qint64 a0, qint64
    a1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlxmllistmodel.html#requestProgress

    Parameters
    ----------

    a0 : int
      Passed on as it is.

    a1 : int
      Passed on as it is.
    """
    #  void QQmlXmlListModel::requestProgress(qint64 a0, qint64 a1)
    self.uglySide.call(
        'ritual_ZN16QQmlXmlListModel15requestProgressExx', a0, a1,
    )

  def dataCleared(self) -> None:
    """
    Calls Qt's 'void QQmlXmlListModel::dataCleared()'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlxmllistmodel.html#dataCleared
    """
    #  void QQmlXmlListModel::dataCleared()
    self.uglySide.call('ritual_ZN16QQmlXmlListModel11dataClearedEv')

  @overload(QQmlXmlListModelQueryResult)
  def queryCompleted(self, a0: QQmlXmlListModelQueryResult) -> None:
    """
    Calls Qt's 'void QQmlXmlListModel::queryCompleted(const
    QQmlXmlListModelQueryResult &a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlxmllistmodel.html#queryCompleted

    Parameters
    ----------

    a0 : QQmlXmlListModelQueryResult
      Passed on as a value: Qt reads the C++ QQmlXmlListModelQueryResult,
      which stays Python's own.
    """
    #  void QQmlXmlListModel::queryCompleted(const
    #      QQmlXmlListModelQueryResult &a0)
    self.uglySide.call(
        'ritual_ZN16QQmlXmlListModel14queryCompletedERK27QQmlXmlListModelQu'
        'eryResult',
        self._valueOf(a0),
    )

  @overload(bool)
  def notifyQueryStarted(self, remoteSource: bool) -> None:
    """
    Calls Qt's 'void QQmlXmlListModel::notifyQueryStarted(bool
    remoteSource)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlxmllistmodel.html#notifyQueryStarted

    Parameters
    ----------

    remoteSource : bool
      Passed on as it is.
    """
    #  void QQmlXmlListModel::notifyQueryStarted(bool remoteSource)
    self.uglySide.call(
        'ritual_ZN16QQmlXmlListModel18notifyQueryStartedEb', remoteSource,
    )

  @overload(QByteArray)
  def tryExecuteQuery(self, data: QByteArray) -> None:
    """
    Calls Qt's 'void QQmlXmlListModel::tryExecuteQuery(const QByteArray
    &data)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlxmllistmodel.html#tryExecuteQuery

    Parameters
    ----------

    data : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void QQmlXmlListModel::tryExecuteQuery(const QByteArray &data)
    self.uglySide.call(
        'ritual_ZN16QQmlXmlListModel15tryExecuteQueryERK10QByteArray',
        self._valueOf(data),
    )

  @overload(QByteArray)
  def createJob(self, data: QByteArray) -> QQmlXmlListModelQueryJob:
    """
    Calls Qt's 'QQmlXmlListModelQueryJob QQmlXmlListModel::createJob(const
    QByteArray &data)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlxmllistmodel.html#createJob

    Parameters
    ----------

    data : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    Returns
    -------

    QQmlXmlListModelQueryJob
      A new cute QQmlXmlListModelQueryJob around the copy Qt gave back.
      Python owns it.
    """
    #  QQmlXmlListModelQueryJob QQmlXmlListModel::createJob(const QByteArray
    #      &data)
    address = self.uglySide.call(
        'ritual_ZN16QQmlXmlListModel9createJobERK10QByteArray',
        self._valueOf(data),
    )
    from . import QQmlXmlListModelQueryJob
    return QQmlXmlListModelQueryJob._cuteOwning(address)

  def nextQueryId(self) -> int:
    """
    Calls Qt's 'int QQmlXmlListModel::nextQueryId()'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlxmllistmodel.html#nextQueryId
    """
    #  int QQmlXmlListModel::nextQueryId()
    return self.uglySide.call('ritual_ZN16QQmlXmlListModel11nextQueryIdEv')

  def deleteReply(self) -> None:
    """
    Calls Qt's 'void QQmlXmlListModel::deleteReply()'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlxmllistmodel.html#deleteReply
    """
    #  void QQmlXmlListModel::deleteReply()
    self.uglySide.call('ritual_ZN16QQmlXmlListModel11deleteReplyEv')

  @staticmethod
  def queryError(*__, **_) -> Never:
    """
    Qt's 'void QQmlXmlListModel::queryError(void *object, const QString
    &error)': names 'void', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QQmlXmlListModel.queryError' has no cute function yet. Qt's 'void "
        "QQmlXmlListModel::queryError(void *object, const QString &error)': "
        "names 'void', which has no cute class yet.")

  @staticmethod
  def roleObjects(*__, **_) -> Never:
    """
    Qt's 'QQmlListProperty<QQmlXmlListModelRole>
    QQmlXmlListModel::roleObjects()': gives a type Python has no way to take
    yet.
    """
    raise NotImplementedError(
        "'QQmlXmlListModel.roleObjects' has no cute function yet. Qt's "
        "'QQmlListProperty<QQmlXmlListModelRole> "
        "QQmlXmlListModel::roleObjects()': gives a type Python has no way "
        "to take yet.")
