"""
QDeclarativeSearchSuggestionModel binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtLocation/6.12.0/QtLocation/private/qdeclarativesearchsuggestionmodel_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QDeclarativeSearchSuggestionModel to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import QHash, QObject, QStringList
from . import QDeclarativeSearchModelBase

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QByteArray, QMetaObject, QModelIndex, QVariant
  from . import QPlaceManager, QPlaceReply, QPlaceSearchRequest
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QModelIndex = WAIT['QModelIndex']
  QPlaceManager = WAIT['QPlaceManager']
  QPlaceSearchRequest = WAIT['QPlaceSearchRequest']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QDeclarativeSearchSuggestionModel(QDeclarativeSearchModelBase):
  """
  The cute side of Qt's QDeclarativeSearchSuggestionModel: a plain Python
  object standing in front of one C++ QDeclarativeSearchSuggestionModel.

  It is built on the cute 'QDeclarativeSearchModelBase', as Qt's
  QDeclarativeSearchSuggestionModel is built on Qt's
  QDeclarativeSearchModelBase, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QDeclarativeSearchSuggestionModel that has a ritual
  and that Python can call so far, 13 names in all: 'metaObject', 'tr',
  'searchTerm', 'setSearchTerm', 'suggestions', 'clearData', 'rowCount',
  'data', 'roleNames', 'queryFinished', 'searchTermChanged',
  'suggestionsChanged', 'sendQuery'. It can be made from Python, in 1 way;
  see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QDeclarativeSearchSuggestionModel::qt_metacast(const char
    *a0)': one of Qt's own inner workings.
  - Qt's 'int
    QDeclarativeSearchSuggestionModel::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's
    'QDeclarativeSearchSuggestionModel::~QDeclarativeSearchSuggestionModel(
    )': the destructor: Python never removes a C++
    QDeclarativeSearchSuggestionModel.

  What has no ritual
  ------------------

  2 of the 19 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QDeclarativeSearchSuggestionModel is created at the first use,
    not by 'QDeclarativeSearchSuggestionModel(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QDeclarativeSearchSuggestionModel.
  - Qt tells when it has removed the C++ QDeclarativeSearchSuggestionModel.
    Every call on the cute object, and every use of it as an argument, then
    raises 'RuntimeError', and nothing reaches C++.
  """

  #  The enums Qt writes inside QDeclarativeSearchSuggestionModel, each a
  #  class in here as in C++, and the names Qt has for the combinations of
  #  its flags enums.

  class Roles(CuteNum):
    """
    The enum 'QDeclarativeSearchSuggestionModel::Roles' of Qt, with the 1
    names Qt gives in it.
    """

    SearchSuggestionRole = Kee[int](256)

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
    Calls Qt's 'QString QDeclarativeSearchSuggestionModel::tr(const char *s,
    const char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativesearchsuggestionmodel.html#tr

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
    #  QString QDeclarativeSearchSuggestionModel::tr(const char *s, const
    #      char *c, int n)
    return Rituals.call(
        'ritual_ZN33QDeclarativeSearchSuggestionModel2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QDeclarativeSearchSuggestionModel'

  #  A C++ QDeclarativeSearchSuggestionModel Python makes is of a C++ class
  #  of ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QDeclarativeSearchSuggestionModel'

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
    *QDeclarativeSearchSuggestionModel::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativesearchsuggestionmodel.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QDeclarativeSearchSuggestionModel::metaObject()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK33QDeclarativeSearchSuggestionModel10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def searchTerm(self) -> str:
    """
    Calls Qt's 'QString QDeclarativeSearchSuggestionModel::searchTerm()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativesearchsuggestionmodel.html#searchTerm

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QDeclarativeSearchSuggestionModel::searchTerm() const
    return self.uglySide.call(
        'ritual_ZNK33QDeclarativeSearchSuggestionModel10searchTermEv',
    )

  def suggestions(self) -> QStringList:
    """
    Calls Qt's 'QStringList QDeclarativeSearchSuggestionModel::suggestions()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativesearchsuggestionmodel.html#suggestions

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QDeclarativeSearchSuggestionModel::suggestions() const
    address = self.uglySide.call(
        'ritual_ZNK33QDeclarativeSearchSuggestionModel11suggestionsEv',
    )
    return QStringList._cuteOwning(address)

  @overload(QModelIndex)
  def rowCount(self, parent: QModelIndex) -> int:
    """
    Calls Qt's 'int QDeclarativeSearchSuggestionModel::rowCount(const
    QModelIndex &parent) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativesearchsuggestionmodel.html#rowCount

    Parameters
    ----------

    parent : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.
    """
    #  int QDeclarativeSearchSuggestionModel::rowCount(const QModelIndex
    #      &parent) const
    ritual = (
        'ritual_ZNK33QDeclarativeSearchSuggestionModel8rowCountERK11QModelI'
        'ndex')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK33QDeclarativeSearchSuggestionModel8rowCountERK11Q'
          'ModelIndex')
    return self.uglySide.call(ritual, self._valueOf(parent))

  @overload(QModelIndex, int)
  def data(self, index: QModelIndex, role: int) -> QVariant:
    """
    Calls Qt's 'QVariant QDeclarativeSearchSuggestionModel::data(const
    QModelIndex &index, int role) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativesearchsuggestionmodel.html#data

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
    #  QVariant QDeclarativeSearchSuggestionModel::data(const QModelIndex
    #      &index, int role) const
    ritual = (
        'ritual_ZNK33QDeclarativeSearchSuggestionModel4dataERK11QModelIndex'
        'i')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK33QDeclarativeSearchSuggestionModel4dataERK11QMode'
          'lIndexi')
    address = self.uglySide.call(ritual, self._valueOf(index), role)
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  def roleNames(self) -> QHash[int, QByteArray]:
    """
    Calls Qt's 'QHash<int, QByteArray>
    QDeclarativeSearchSuggestionModel::roleNames() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativesearchsuggestionmodel.html#roleNames

    Returns
    -------

    QHash[int, QByteArray]
      A new cute map around the copy Qt gave back. Python owns it.
    """
    #  QHash<int, QByteArray> QDeclarativeSearchSuggestionModel::roleNames()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK33QDeclarativeSearchSuggestionModel9roleNamesEv',
    )
    from ..QtCore import QByteArray
    return QHash[int, QByteArray]._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setSearchTerm(self, searchTerm: str) -> None:
    """
    Calls Qt's 'void QDeclarativeSearchSuggestionModel::setSearchTerm(const
    QString &searchTerm)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativesearchsuggestionmodel.html

    Parameters
    ----------

    searchTerm : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QDeclarativeSearchSuggestionModel::setSearchTerm(const QString
    #      &searchTerm)
    self.uglySide.call(
        'ritual_ZN33QDeclarativeSearchSuggestionModel13setSearchTermERK7QSt'
        'ring',
        searchTerm,
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
    'QDeclarativeSearchSuggestionModel::QDeclarativeSearchSuggestionModel(
    QObject *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativesearchsuggestionmodel.html

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QDeclarativeSearchSuggestionModel::
    #      QDeclarativeSearchSuggestionModel(QObject *parent)
    self._noteCreation(
        QDeclarativeSearchSuggestionModel, lambda: Rituals.call(
            'ritual_ZN33QDeclarativeSearchSuggestionModelC1EP7QObject',
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

  @overload()
  @overload(bool)
  def clearData(self, suppressSignal: bool = False) -> None:
    """
    Calls Qt's 'void QDeclarativeSearchSuggestionModel::clearData(bool
    suppressSignal)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativesearchsuggestionmodel.html#clearData

    Parameters
    ----------

    suppressSignal : bool
      Passed on as it is. May be left out, as in Qt: it is then False.
    """
    #  void QDeclarativeSearchSuggestionModel::clearData(bool suppressSignal)
    ritual = 'ritual_ZN33QDeclarativeSearchSuggestionModel9clearDataEb'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN33QDeclarativeSearchSuggestionModel9clearDataEb'
    self.uglySide.call(ritual, suppressSignal)

  def queryFinished(self) -> None:
    """
    Calls Qt's 'void QDeclarativeSearchSuggestionModel::queryFinished()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativesearchsuggestionmodel.html
    """
    #  void QDeclarativeSearchSuggestionModel::queryFinished()
    ritual = 'ritual_ZN33QDeclarativeSearchSuggestionModel13queryFinishedEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN33QDeclarativeSearchSuggestionModel13queryFinishedE'
          'v')
    self.uglySide.call(ritual)

  def searchTermChanged(self) -> None:
    """
    Calls Qt's 'void QDeclarativeSearchSuggestionModel::searchTermChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativesearchsuggestionmodel.html
    """
    #  void QDeclarativeSearchSuggestionModel::searchTermChanged()
    self.uglySide.call(
        'ritual_ZN33QDeclarativeSearchSuggestionModel17searchTermChangedEv',
    )

  def suggestionsChanged(self) -> None:
    """
    Calls Qt's 'void
    QDeclarativeSearchSuggestionModel::suggestionsChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativesearchsuggestionmodel.html
    """
    #  void QDeclarativeSearchSuggestionModel::suggestionsChanged()
    self.uglySide.call(
        'ritual_ZN33QDeclarativeSearchSuggestionModel18suggestionsChangedEv',
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
    *QDeclarativeSearchSuggestionModel::sendQuery(QPlaceManager *manager,
    const QPlaceSearchRequest &request)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativesearchsuggestionmodel.html#sendQuery

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
    #  QPlaceReply
    #      *QDeclarativeSearchSuggestionModel::sendQuery(QPlaceManager
    #      *manager, const QPlaceSearchRequest &request)
    ritual = (
        'ritual_ZN33QDeclarativeSearchSuggestionModel9sendQueryEP13QPlaceMa'
        'nagerRK19QPlaceSearchRequest')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN33QDeclarativeSearchSuggestionModel9sendQueryEP13QP'
          'laceManagerRK19QPlaceSearchRequest')
    address = self.uglySide.call(
        ritual, self._addressOf(manager), self._valueOf(request),
    )
    from . import QPlaceReply
    return QPlaceReply._cuteAt(address)
