"""
QDeclarativeSearchModelBase binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtLocation/6.12.0/QtLocation/private/qdeclarativesearchmodelbase_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QDeclarativeSearchModelBase to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import QAbstractListModel, QObject
from ..QtQml import QQmlParserStatus

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QVariant
  from . import QDeclarativeGeoServiceProvider, QPlaceManager, QPlaceReply
  from . import QPlaceSearchRequest
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDeclarativeGeoServiceProvider = WAIT['QDeclarativeGeoServiceProvider']
  QPlaceManager = WAIT['QPlaceManager']
  QPlaceSearchRequest = WAIT['QPlaceSearchRequest']
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QDeclarativeSearchModelBase(QAbstractListModel, QQmlParserStatus):
  """
  The cute side of Qt's QDeclarativeSearchModelBase: a plain Python object
  standing in front of one C++ QDeclarativeSearchModelBase.

  It is built on the cute 'QAbstractListModel', as Qt's
  QDeclarativeSearchModelBase is built on Qt's QAbstractListModel, and has
  everything that class has. It is built on the cute 'QQmlParserStatus' as
  well, as Qt's QDeclarativeSearchModelBase is built on Qt's QQmlParserStatus
  too, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QDeclarativeSearchModelBase that has a ritual and
  that Python can call so far, 34 names in all: 'metaObject', 'tr', 'plugin',
  'setPlugin', 'searchArea', 'setSearchArea', 'limit', 'setLimit',
  'previousPagesAvailable', 'nextPagesAvailable', 'status', 'setStatus',
  'update', 'cancel', 'reset', 'errorString', 'previousPage', 'nextPage',
  'clearData', 'classBegin', 'componentComplete', 'pluginChanged',
  'searchAreaChanged', 'limitChanged', 'previousPagesAvailableChanged',
  'nextPagesAvailableChanged', 'statusChanged', 'initializePlugin',
  'queryFinished', 'onContentUpdated', 'pluginNameChanged', 'sendQuery',
  'setPreviousPageRequest', 'setNextPageRequest'. It can be made from Python,
  in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QDeclarativeSearchModelBase::qt_metacast(const char *a0)':
    one of Qt's own inner workings.
  - Qt's 'int QDeclarativeSearchModelBase::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QDeclarativeSearchModelBase::~QDeclarativeSearchModelBase()': the
    destructor: Python never removes a C++ QDeclarativeSearchModelBase.

  What has no ritual
  ------------------

  2 of the 40 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QDeclarativeSearchModelBase is created at the first use, not by
    'QDeclarativeSearchModelBase(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QDeclarativeSearchModelBase.
  - Qt tells when it has removed the C++ QDeclarativeSearchModelBase. Every
    call on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  #  The enums Qt writes inside QDeclarativeSearchModelBase, each a class in
  #  here as in C++, and the names Qt has for the combinations of its flags
  #  enums.

  class Status(CuteNum):
    """
    The enum 'QDeclarativeSearchModelBase::Status' of Qt, with the 4 names Qt
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
    Calls Qt's 'QString QDeclarativeSearchModelBase::tr(const char *s, const
    char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativesearchmodelbase.html#tr

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
    #  QString QDeclarativeSearchModelBase::tr(const char *s, const char *c,
    #      int n)
    return Rituals.call(
        'ritual_ZN27QDeclarativeSearchModelBase2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QDeclarativeSearchModelBase'

  #  Qt's QDeclarativeSearchModelBase is built on more than one class. The
  #  part of a C++ QDeclarativeSearchModelBase that belongs to a class after
  #  the first begins somewhere inside the object, and the ritual named for
  #  that class gives where; see 'CuteMixin._addressAs'.
  __cast_rituals__ = {
      'QQmlParserStatus':
          'ritual_cast_QDeclarativeSearchModelBase_QQmlParserStatus',
  }

  #  A C++ QDeclarativeSearchModelBase Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QDeclarativeSearchModelBase'

  #  The functions Qt calls itself that QDeclarativeSearchModelBase is the
  #  first to declare. A class of a program built on it can write one anew,
  #  and Qt then calls that. For each name: the key C++ knows the function
  #  by, what it gives, and what it takes.
  __virtual_functions__ = {
      'clearData': (
          ('_ZN27QDeclarativeSearchModelBase9clearDataEb',
           ('nothing', 'nothing', ''),
           (
               ('bool', 'number', ''),
           )),
      ),
      'initializePlugin': (
          ('_ZN27QDeclarativeSearchModelBase16initializePluginEP30QDeclarat'
           'iveGeoServiceProvider',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address',
                'QtLocation:QDeclarativeGeoServiceProvider'),
           )),
      ),
      'queryFinished': (
          ('_ZN27QDeclarativeSearchModelBase13queryFinishedEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'onContentUpdated': (
          ('_ZN27QDeclarativeSearchModelBase16onContentUpdatedEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'sendQuery': (
          ('_ZN27QDeclarativeSearchModelBase9sendQueryEP13QPlaceManagerRK19'
           'QPlaceSearchRequest',
           ('address', 'address', 'QtLocation:QPlaceReply'),
           (
               ('address', 'address', 'QtLocation:QPlaceManager'),
               ('address', 'value', 'QtLocation:QPlaceSearchRequest'),
           )),
      ),
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
    Calls Qt's 'const QMetaObject *QDeclarativeSearchModelBase::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativesearchmodelbase.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QDeclarativeSearchModelBase::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK27QDeclarativeSearchModelBase10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def plugin(self) -> Optional[QDeclarativeGeoServiceProvider]:
    """
    Calls Qt's 'QDeclarativeGeoServiceProvider
    *QDeclarativeSearchModelBase::plugin() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativesearchmodelbase.html#plugin

    Returns
    -------

    Optional[QDeclarativeGeoServiceProvider]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QDeclarativeGeoServiceProvider *QDeclarativeSearchModelBase::plugin()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK27QDeclarativeSearchModelBase6pluginEv',
    )
    from . import QDeclarativeGeoServiceProvider
    return QDeclarativeGeoServiceProvider._cuteAt(address)

  def searchArea(self) -> QVariant:
    """
    Calls Qt's 'QVariant QDeclarativeSearchModelBase::searchArea() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativesearchmodelbase.html#searchArea

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QDeclarativeSearchModelBase::searchArea() const
    address = self.uglySide.call(
        'ritual_ZNK27QDeclarativeSearchModelBase10searchAreaEv',
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  def limit(self) -> int:
    """
    Calls Qt's 'int QDeclarativeSearchModelBase::limit() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativesearchmodelbase.html#limit
    """
    #  int QDeclarativeSearchModelBase::limit() const
    return self.uglySide.call(
        'ritual_ZNK27QDeclarativeSearchModelBase5limitEv',
    )

  def previousPagesAvailable(self) -> bool:
    """
    Calls Qt's 'bool QDeclarativeSearchModelBase::previousPagesAvailable()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativesearchmodelbase.html
    """
    #  bool QDeclarativeSearchModelBase::previousPagesAvailable() const
    return self.uglySide.call(
        'ritual_ZNK27QDeclarativeSearchModelBase22previousPagesAvailableEv',
    )

  def nextPagesAvailable(self) -> bool:
    """
    Calls Qt's 'bool QDeclarativeSearchModelBase::nextPagesAvailable()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativesearchmodelbase.html
    """
    #  bool QDeclarativeSearchModelBase::nextPagesAvailable() const
    return self.uglySide.call(
        'ritual_ZNK27QDeclarativeSearchModelBase18nextPagesAvailableEv',
    )

  def status(self) -> Status:
    """
    Calls Qt's 'Status QDeclarativeSearchModelBase::status() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativesearchmodelbase.html#status

    Returns
    -------

    Status
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Status(number)' gives.
    """
    #  Status QDeclarativeSearchModelBase::status() const
    return QDeclarativeSearchModelBase.Status(self.uglySide.call(
        'ritual_ZNK27QDeclarativeSearchModelBase6statusEv',
    ))

  def errorString(self) -> str:
    """
    Calls Qt's 'QString QDeclarativeSearchModelBase::errorString() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativesearchmodelbase.html#errorString

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QDeclarativeSearchModelBase::errorString() const
    return self.uglySide.call(
        'ritual_ZNK27QDeclarativeSearchModelBase11errorStringEv',
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
    QDeclarativeSearchModelBase::setPlugin(QDeclarativeGeoServiceProvider
    *plugin)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativesearchmodelbase.html#setPlugin

    Parameters
    ----------

    plugin : Optional[QDeclarativeGeoServiceProvider]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QDeclarativeSearchModelBase::setPlugin(
    #      QDeclarativeGeoServiceProvider *plugin)
    self.uglySide.call(
        'ritual_ZN27QDeclarativeSearchModelBase9setPluginEP30QDeclarativeGe'
        'oServiceProvider',
        self._addressOf(plugin),
    )

  @overload(QVariant)
  def setSearchArea(self, searchArea: QVariant) -> None:
    """
    Calls Qt's 'void QDeclarativeSearchModelBase::setSearchArea(const
    QVariant &searchArea)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativesearchmodelbase.html#setSearchArea

    Parameters
    ----------

    searchArea : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void QDeclarativeSearchModelBase::setSearchArea(const QVariant
    #      &searchArea)
    self.uglySide.call(
        'ritual_ZN27QDeclarativeSearchModelBase13setSearchAreaERK8QVariant',
        self._valueOf(searchArea),
    )

  @overload(int)
  def setLimit(self, limit: int) -> None:
    """
    Calls Qt's 'void QDeclarativeSearchModelBase::setLimit(int limit)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativesearchmodelbase.html#setLimit

    Parameters
    ----------

    limit : int
      Passed on as it is.
    """
    #  void QDeclarativeSearchModelBase::setLimit(int limit)
    self.uglySide.call(
        'ritual_ZN27QDeclarativeSearchModelBase8setLimitEi', limit,
    )

  @overload(Status)
  @overload(Status, str)
  def setStatus(self, status: Status, errorString: str = '') -> None:
    """
    Calls Qt's 'void QDeclarativeSearchModelBase::setStatus(Status status,
    const QString &errorString)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativesearchmodelbase.html#setStatus

    Parameters
    ----------

    status : Status
      Passed on as its number.

    errorString : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.
    """
    #  void QDeclarativeSearchModelBase::setStatus(Status status, const
    #      QString &errorString)
    self.uglySide.call(
        'ritual_ZN27QDeclarativeSearchModelBase9setStatusENS_6StatusERK7QSt'
        'ring',
        status.value, errorString,
    )

  @overload(QPlaceSearchRequest)
  def setPreviousPageRequest(self, previous: QPlaceSearchRequest) -> None:
    """
    Calls Qt's 'void
    QDeclarativeSearchModelBase::setPreviousPageRequest(const
    QPlaceSearchRequest &previous)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativesearchmodelbase.html

    Parameters
    ----------

    previous : QPlaceSearchRequest
      Passed on as a value: Qt reads the C++ QPlaceSearchRequest, which stays
      Python's own.
    """
    #  void QDeclarativeSearchModelBase::setPreviousPageRequest(const
    #      QPlaceSearchRequest &previous)
    self.uglySide.call(
        'ritual_ZN27QDeclarativeSearchModelBase22setPreviousPageRequestERK1'
        '9QPlaceSearchRequest',
        self._valueOf(previous),
    )

  @overload(QPlaceSearchRequest)
  def setNextPageRequest(self, next: QPlaceSearchRequest) -> None:
    """
    Calls Qt's 'void QDeclarativeSearchModelBase::setNextPageRequest(const
    QPlaceSearchRequest &next)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativesearchmodelbase.html

    Parameters
    ----------

    next : QPlaceSearchRequest
      Passed on as a value: Qt reads the C++ QPlaceSearchRequest, which stays
      Python's own.
    """
    #  void QDeclarativeSearchModelBase::setNextPageRequest(const
    #      QPlaceSearchRequest &next)
    self.uglySide.call(
        'ritual_ZN27QDeclarativeSearchModelBase18setNextPageRequestERK19QPl'
        'aceSearchRequest',
        self._valueOf(next),
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
    'QDeclarativeSearchModelBase::QDeclarativeSearchModelBase(QObject
    *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativesearchmodelbase.html

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QDeclarativeSearchModelBase::QDeclarativeSearchModelBase(QObject
    #      *parent)
    self._noteCreation(QDeclarativeSearchModelBase, lambda: Rituals.call(
        'ritual_ZN27QDeclarativeSearchModelBaseC1EP7QObject',
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

  def update(self) -> None:
    """
    Calls Qt's 'void QDeclarativeSearchModelBase::update()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativesearchmodelbase.html#update
    """
    #  void QDeclarativeSearchModelBase::update()
    self.uglySide.call('ritual_ZN27QDeclarativeSearchModelBase6updateEv')

  def cancel(self) -> None:
    """
    Calls Qt's 'void QDeclarativeSearchModelBase::cancel()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativesearchmodelbase.html#cancel
    """
    #  void QDeclarativeSearchModelBase::cancel()
    self.uglySide.call('ritual_ZN27QDeclarativeSearchModelBase6cancelEv')

  def reset(self) -> None:
    """
    Calls Qt's 'void QDeclarativeSearchModelBase::reset()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativesearchmodelbase.html#reset
    """
    #  void QDeclarativeSearchModelBase::reset()
    self.uglySide.call('ritual_ZN27QDeclarativeSearchModelBase5resetEv')

  def previousPage(self) -> None:
    """
    Calls Qt's 'void QDeclarativeSearchModelBase::previousPage()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativesearchmodelbase.html#previousPage
    """
    #  void QDeclarativeSearchModelBase::previousPage()
    self.uglySide.call(
        'ritual_ZN27QDeclarativeSearchModelBase12previousPageEv',
    )

  def nextPage(self) -> None:
    """
    Calls Qt's 'void QDeclarativeSearchModelBase::nextPage()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativesearchmodelbase.html#nextPage
    """
    #  void QDeclarativeSearchModelBase::nextPage()
    self.uglySide.call('ritual_ZN27QDeclarativeSearchModelBase8nextPageEv')

  @overload()
  @overload(bool)
  def clearData(self, suppressSignal: bool = False) -> None:
    """
    Calls Qt's 'void QDeclarativeSearchModelBase::clearData(bool
    suppressSignal)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativesearchmodelbase.html#clearData

    Parameters
    ----------

    suppressSignal : bool
      Passed on as it is. May be left out, as in Qt: it is then False.
    """
    #  void QDeclarativeSearchModelBase::clearData(bool suppressSignal)
    ritual = 'ritual_ZN27QDeclarativeSearchModelBase9clearDataEb'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN27QDeclarativeSearchModelBase9clearDataEb'
    self.uglySide.call(ritual, suppressSignal)

  def classBegin(self) -> None:
    """
    Calls Qt's 'void QDeclarativeSearchModelBase::classBegin()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativesearchmodelbase.html#classBegin
    """
    #  void QDeclarativeSearchModelBase::classBegin()
    ritual = 'ritual_ZN27QDeclarativeSearchModelBase10classBeginEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN27QDeclarativeSearchModelBase10classBeginEv'
    self.uglySide.call(ritual)

  def componentComplete(self) -> None:
    """
    Calls Qt's 'void QDeclarativeSearchModelBase::componentComplete()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativesearchmodelbase.html#componentComplete
    """
    #  void QDeclarativeSearchModelBase::componentComplete()
    ritual = 'ritual_ZN27QDeclarativeSearchModelBase17componentCompleteEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN27QDeclarativeSearchModelBase17componentCompleteEv')
    self.uglySide.call(ritual)

  def pluginChanged(self) -> None:
    """
    Calls Qt's 'void QDeclarativeSearchModelBase::pluginChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativesearchmodelbase.html#pluginChanged
    """
    #  void QDeclarativeSearchModelBase::pluginChanged()
    self.uglySide.call(
        'ritual_ZN27QDeclarativeSearchModelBase13pluginChangedEv',
    )

  def searchAreaChanged(self) -> None:
    """
    Calls Qt's 'void QDeclarativeSearchModelBase::searchAreaChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativesearchmodelbase.html#searchAreaChanged
    """
    #  void QDeclarativeSearchModelBase::searchAreaChanged()
    self.uglySide.call(
        'ritual_ZN27QDeclarativeSearchModelBase17searchAreaChangedEv',
    )

  def limitChanged(self) -> None:
    """
    Calls Qt's 'void QDeclarativeSearchModelBase::limitChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativesearchmodelbase.html#limitChanged
    """
    #  void QDeclarativeSearchModelBase::limitChanged()
    self.uglySide.call(
        'ritual_ZN27QDeclarativeSearchModelBase12limitChangedEv',
    )

  def previousPagesAvailableChanged(self) -> None:
    """
    Calls Qt's 'void
    QDeclarativeSearchModelBase::previousPagesAvailableChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativesearchmodelbase.html
    """
    #  void QDeclarativeSearchModelBase::previousPagesAvailableChanged()
    self.uglySide.call(
        'ritual_ZN27QDeclarativeSearchModelBase29previousPagesAvailableChan'
        'gedEv',
    )

  def nextPagesAvailableChanged(self) -> None:
    """
    Calls Qt's 'void
    QDeclarativeSearchModelBase::nextPagesAvailableChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativesearchmodelbase.html
    """
    #  void QDeclarativeSearchModelBase::nextPagesAvailableChanged()
    self.uglySide.call(
        'ritual_ZN27QDeclarativeSearchModelBase25nextPagesAvailableChangedE'
        'v',
    )

  def statusChanged(self) -> None:
    """
    Calls Qt's 'void QDeclarativeSearchModelBase::statusChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativesearchmodelbase.html#statusChanged
    """
    #  void QDeclarativeSearchModelBase::statusChanged()
    self.uglySide.call(
        'ritual_ZN27QDeclarativeSearchModelBase13statusChangedEv',
    )

  @overload(QDeclarativeGeoServiceProvider)
  @overload(NoneType)
  def initializePlugin(
      self,
      plugin: Optional[QDeclarativeGeoServiceProvider],
  ) -> None:
    """
    Calls Qt's 'void QDeclarativeSearchModelBase::initializePlugin(
    QDeclarativeGeoServiceProvider *plugin)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativesearchmodelbase.html#initializePlugin

    Parameters
    ----------

    plugin : Optional[QDeclarativeGeoServiceProvider]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QDeclarativeSearchModelBase::initializePlugin(
    #      QDeclarativeGeoServiceProvider *plugin)
    ritual = (
        'ritual_ZN27QDeclarativeSearchModelBase16initializePluginEP30QDecla'
        'rativeGeoServiceProvider')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN27QDeclarativeSearchModelBase16initializePluginEP30'
          'QDeclarativeGeoServiceProvider')
    self.uglySide.call(ritual, self._addressOf(plugin))

  def queryFinished(self) -> None:
    """
    Calls Qt's 'void QDeclarativeSearchModelBase::queryFinished()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativesearchmodelbase.html#queryFinished
    """
    #  void QDeclarativeSearchModelBase::queryFinished()
    self.uglySide.call(
        'ritual_ZN27QDeclarativeSearchModelBase13queryFinishedEv',
    )

  def onContentUpdated(self) -> None:
    """
    Calls Qt's 'void QDeclarativeSearchModelBase::onContentUpdated()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativesearchmodelbase.html#onContentUpdated
    """
    #  void QDeclarativeSearchModelBase::onContentUpdated()
    ritual = 'ritual_ZN27QDeclarativeSearchModelBase16onContentUpdatedEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN27QDeclarativeSearchModelBase16onContentUpdatedEv')
    self.uglySide.call(ritual)

  def pluginNameChanged(self) -> None:
    """
    Calls Qt's 'void QDeclarativeSearchModelBase::pluginNameChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativesearchmodelbase.html#pluginNameChanged
    """
    #  void QDeclarativeSearchModelBase::pluginNameChanged()
    self.uglySide.call(
        'ritual_ZN27QDeclarativeSearchModelBase17pluginNameChangedEv',
    )

  @overload(QPlaceManager, QPlaceSearchRequest)
  @overload(NoneType, QPlaceSearchRequest)
  def sendQuery(
      self,
      manager: Optional[QPlaceManager],
      request: QPlaceSearchRequest,
  ) -> Optional[QPlaceReply]:
    """
    Calls Qt's 'QPlaceReply
    *QDeclarativeSearchModelBase::sendQuery(QPlaceManager *manager, const
    QPlaceSearchRequest &request)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativesearchmodelbase.html#sendQuery

    Parameters
    ----------

    manager : Optional[QPlaceManager]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    request : QPlaceSearchRequest
      Passed on as a value: Qt reads the C++ QPlaceSearchRequest, which stays
      Python's own.

    Returns
    -------

    Optional[QPlaceReply]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPlaceReply *QDeclarativeSearchModelBase::sendQuery(QPlaceManager
    #      *manager, const QPlaceSearchRequest &request)
    address = self.uglySide.call(
        'ritual_ZN27QDeclarativeSearchModelBase9sendQueryEP13QPlaceManagerR'
        'K19QPlaceSearchRequest',
        self._addressOf(manager), self._valueOf(request),
    )
    from . import QPlaceReply
    return QPlaceReply._cuteAt(address)
