"""
QPdfSearchModel binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtPdf/qpdfsearchmodel.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import QAbstractListModel, QHash, QList, QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QByteArray, QMetaObject, QModelIndex, QTimerEvent
  from ..QtCore import QVariant
  from . import QPdfDocument, QPdfLink
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QModelIndex = WAIT['QModelIndex']
  QPdfDocument = WAIT['QPdfDocument']
  QTimerEvent = WAIT['QTimerEvent']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QPdfSearchModel(QAbstractListModel):
  """
  The cute side of Qt's QPdfSearchModel: a plain Python object standing in
  front of one C++ QPdfSearchModel.

  It is built on the cute 'QAbstractListModel', as Qt's QPdfSearchModel is
  built on Qt's QAbstractListModel, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QPdfSearchModel that has a ritual and that Python
  can call so far, 19 names in all: 'metaObject', 'tr', 'resultsOnPage',
  'resultAtIndex', 'document', 'searchString', 'roleNames', 'rowCount',
  'data', 'count', 'status', 'setSearchString', 'setDocument',
  'documentChanged', 'searchStringChanged', 'countChanged', 'statusChanged',
  'updatePage', 'timerEvent'. It can be made from Python, in 2 ways; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QPdfSearchModel::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QPdfSearchModel::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QPdfSearchModel::~QPdfSearchModel()': the destructor: Python never
    removes a C++ QPdfSearchModel.
  - Qt's 'QPdfSearchModelPrivate *QPdfSearchModel::d_func()': gives
    'QPdfSearchModelPrivate', which has no cute class yet.
  - Qt's 'const QPdfSearchModelPrivate *QPdfSearchModel::d_func() const':
    gives 'QPdfSearchModelPrivate', which has no cute class yet.

  What has no ritual
  ------------------

  2 of the 28 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QPdfSearchModel is created at the first use, not by
    'QPdfSearchModel(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QPdfSearchModel.
  - Qt tells when it has removed the C++ QPdfSearchModel. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  #  The enums Qt writes inside QPdfSearchModel, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class Role(CuteNum, scoped=True):
    """
    The enum 'QPdfSearchModel::Role' of Qt, with the 6 names Qt gives in it.
    C++ keeps these names inside the enum, so the class that holds the enum
    does not have them.
    """

    Page = Kee[int](256)
    IndexOnPage = Kee[int](257)
    Location = Kee[int](258)
    ContextBefore = Kee[int](259)
    ContextAfter = Kee[int](260)
    NRoles = Kee[int](261)

  class Status(CuteNum, scoped=True):
    """
    The enum 'QPdfSearchModel::Status' of Qt, with the 3 names Qt gives in
    it. C++ keeps these names inside the enum, so the class that holds the
    enum does not have them.
    """

    Null = Kee[int](0)
    Searching = Kee[int](1)
    Finished = Kee[int](2)

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
    Calls Qt's 'QString QPdfSearchModel::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qpdfsearchmodel.html#tr

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
    #  QString QPdfSearchModel::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN15QPdfSearchModel2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QPdfSearchModel'

  #  A C++ QPdfSearchModel Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QPdfSearchModel'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QPdfSearchModel::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpdfsearchmodel.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QPdfSearchModel::metaObject() const
    address = self.uglySide.call('ritual_ZNK15QPdfSearchModel10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  @overload(int)
  def resultsOnPage(self, page: int) -> QList[QPdfLink]:
    """
    Calls Qt's 'QList<QPdfLink> QPdfSearchModel::resultsOnPage(int page)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qpdfsearchmodel.html#resultsOnPage

    Parameters
    ----------

    page : int
      Passed on as it is.

    Returns
    -------

    QList[QPdfLink]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QPdfLink> QPdfSearchModel::resultsOnPage(int page) const
    address = self.uglySide.call(
        'ritual_ZNK15QPdfSearchModel13resultsOnPageEi', page,
    )
    from . import QPdfLink
    return QList[QPdfLink]._cuteOwning(address)

  @overload(int)
  def resultAtIndex(self, index: int) -> QPdfLink:
    """
    Calls Qt's 'QPdfLink QPdfSearchModel::resultAtIndex(int index) const'.

    Qt's own words: https://doc.qt.io/qt-6/qpdfsearchmodel.html#resultAtIndex

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    QPdfLink
      A new cute QPdfLink around the copy Qt gave back. Python owns it.
    """
    #  QPdfLink QPdfSearchModel::resultAtIndex(int index) const
    address = self.uglySide.call(
        'ritual_ZNK15QPdfSearchModel13resultAtIndexEi', index,
    )
    from . import QPdfLink
    return QPdfLink._cuteOwning(address)

  def document(self) -> Optional[QPdfDocument]:
    """
    Calls Qt's 'QPdfDocument *QPdfSearchModel::document() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpdfsearchmodel.html#document

    Returns
    -------

    Optional[QPdfDocument]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPdfDocument *QPdfSearchModel::document() const
    address = self.uglySide.call('ritual_ZNK15QPdfSearchModel8documentEv')
    from . import QPdfDocument
    return QPdfDocument._cuteAt(address)

  def searchString(self) -> str:
    """
    Calls Qt's 'QString QPdfSearchModel::searchString() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpdfsearchmodel.html#searchString

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QPdfSearchModel::searchString() const
    return self.uglySide.call('ritual_ZNK15QPdfSearchModel12searchStringEv')

  def roleNames(self) -> QHash[int, QByteArray]:
    """
    Calls Qt's 'QHash<int, QByteArray> QPdfSearchModel::roleNames() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpdfsearchmodel.html#roleNames

    Returns
    -------

    QHash[int, QByteArray]
      A new cute map around the copy Qt gave back. Python owns it.
    """
    #  QHash<int, QByteArray> QPdfSearchModel::roleNames() const
    address = self.uglySide.call('ritual_ZNK15QPdfSearchModel9roleNamesEv')
    from ..QtCore import QByteArray
    return QHash[int, QByteArray]._cuteOwning(address)

  @overload(QModelIndex)
  def rowCount(self, parent: QModelIndex) -> int:
    """
    Calls Qt's 'int QPdfSearchModel::rowCount(const QModelIndex &parent)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qpdfsearchmodel.html#rowCount

    Parameters
    ----------

    parent : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.
    """
    #  int QPdfSearchModel::rowCount(const QModelIndex &parent) const
    ritual = 'ritual_ZNK15QPdfSearchModel8rowCountERK11QModelIndex'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK15QPdfSearchModel8rowCountERK11QModelIndex'
    return self.uglySide.call(ritual, self._valueOf(parent))

  @overload(QModelIndex, int)
  def data(self, index: QModelIndex, role: int) -> QVariant:
    """
    Calls Qt's 'QVariant QPdfSearchModel::data(const QModelIndex &index, int
    role) const'.

    Qt's own words: https://doc.qt.io/qt-6/qpdfsearchmodel.html#data

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
    #  QVariant QPdfSearchModel::data(const QModelIndex &index, int role)
    #      const
    ritual = 'ritual_ZNK15QPdfSearchModel4dataERK11QModelIndexi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK15QPdfSearchModel4dataERK11QModelIndexi'
    address = self.uglySide.call(ritual, self._valueOf(index), role)
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  def count(self) -> int:
    """
    Calls Qt's 'int QPdfSearchModel::count() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpdfsearchmodel.html#count
    """
    #  int QPdfSearchModel::count() const
    return self.uglySide.call('ritual_ZNK15QPdfSearchModel5countEv')

  def status(self) -> Status:
    """
    Calls Qt's 'Status QPdfSearchModel::status() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpdfsearchmodel.html#status

    Returns
    -------

    Status
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Status(number)' gives.
    """
    #  Status QPdfSearchModel::status() const
    return QPdfSearchModel.Status(self.uglySide.call(
        'ritual_ZNK15QPdfSearchModel6statusEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setSearchString(self, searchString: str) -> None:
    """
    Calls Qt's 'void QPdfSearchModel::setSearchString(const QString
    &searchString)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpdfsearchmodel.html#setSearchString

    Parameters
    ----------

    searchString : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QPdfSearchModel::setSearchString(const QString &searchString)
    self.uglySide.call(
        'ritual_ZN15QPdfSearchModel15setSearchStringERK7QString',
        searchString,
    )

  @overload(QPdfDocument)
  @overload(NoneType)
  def setDocument(self, document: Optional[QPdfDocument]) -> None:
    """
    Calls Qt's 'void QPdfSearchModel::setDocument(QPdfDocument *document)'.

    Qt's own words: https://doc.qt.io/qt-6/qpdfsearchmodel.html#setDocument

    Parameters
    ----------

    document : Optional[QPdfDocument]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QPdfSearchModel::setDocument(QPdfDocument *document)
    self.uglySide.call(
        'ritual_ZN15QPdfSearchModel11setDocumentEP12QPdfDocument',
        self._addressOf(document),
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
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'QPdfSearchModel::QPdfSearchModel()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qpdfsearchmodel.html#QPdfSearchModel
    """
    #  QPdfSearchModel::QPdfSearchModel()
    self._noteCreation(QPdfSearchModel, lambda: Rituals.call(
        'ritual_ZN15QPdfSearchModelC1Ev',
    ))

  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject]) -> None:
    """
    Notes what was given, for Qt's 'QPdfSearchModel::QPdfSearchModel(QObject
    *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qpdfsearchmodel.html#QPdfSearchModel

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QPdfSearchModel::QPdfSearchModel(QObject *parent)
    self._noteCreation(QPdfSearchModel, lambda: Rituals.call(
        'ritual_ZN15QPdfSearchModelC1EP7QObject',
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

  def documentChanged(self) -> None:
    """
    Calls Qt's 'void QPdfSearchModel::documentChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpdfsearchmodel.html#documentChanged
    """
    #  void QPdfSearchModel::documentChanged()
    self.uglySide.call('ritual_ZN15QPdfSearchModel15documentChangedEv')

  def searchStringChanged(self) -> None:
    """
    Calls Qt's 'void QPdfSearchModel::searchStringChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpdfsearchmodel.html#searchStringChanged
    """
    #  void QPdfSearchModel::searchStringChanged()
    self.uglySide.call('ritual_ZN15QPdfSearchModel19searchStringChangedEv')

  def countChanged(self) -> None:
    """
    Calls Qt's 'void QPdfSearchModel::countChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qpdfsearchmodel.html#countChanged
    """
    #  void QPdfSearchModel::countChanged()
    self.uglySide.call('ritual_ZN15QPdfSearchModel12countChangedEv')

  @overload(Status)
  def statusChanged(self, status: Status) -> None:
    """
    Calls Qt's 'void QPdfSearchModel::statusChanged(QPdfSearchModel::Status
    status)'.

    Qt's own words: https://doc.qt.io/qt-6/qpdfsearchmodel.html#statusChanged

    Parameters
    ----------

    status : Status
      Passed on as its number.
    """
    #  void QPdfSearchModel::statusChanged(QPdfSearchModel::Status status)
    self.uglySide.call(
        'ritual_ZN15QPdfSearchModel13statusChangedENS_6StatusE',
        status.value,
    )

  @overload(int)
  def updatePage(self, page: int) -> None:
    """
    Calls Qt's 'void QPdfSearchModel::updatePage(int page)'.

    Qt's own words: https://doc.qt.io/qt-6/qpdfsearchmodel.html#updatePage

    Parameters
    ----------

    page : int
      Passed on as it is.
    """
    #  void QPdfSearchModel::updatePage(int page)
    self.uglySide.call('ritual_ZN15QPdfSearchModel10updatePageEi', page)

  @overload(QTimerEvent)
  @overload(NoneType)
  def timerEvent(self, event: Optional[QTimerEvent]) -> None:
    """
    Calls Qt's 'void QPdfSearchModel::timerEvent(QTimerEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qpdfsearchmodel.html#timerEvent

    Parameters
    ----------

    event : Optional[QTimerEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QPdfSearchModel::timerEvent(QTimerEvent *event)
    ritual = 'ritual_ZN15QPdfSearchModel10timerEventEP11QTimerEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN15QPdfSearchModel10timerEventEP11QTimerEvent'
    self.uglySide.call(ritual, self._addressOf(event))
