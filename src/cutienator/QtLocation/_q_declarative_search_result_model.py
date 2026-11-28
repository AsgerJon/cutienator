"""
QDeclarativeSearchResultModel binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtLocation/6.12.0/QtLocation/private/qdeclarativesearchresultmodel_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QDeclarativeSearchResultModel to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import QHash, QList, QMap, QObject
from . import QDeclarativePlace, QDeclarativeSearchModelBase

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QByteArray, QMetaObject, QModelIndex, QVariant
  from . import QDeclarativeGeoServiceProvider, QPlace, QPlaceManager
  from . import QPlaceReply, QPlaceSearchRequest, QPlaceSearchResult
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDeclarativeGeoServiceProvider = WAIT['QDeclarativeGeoServiceProvider']
  QModelIndex = WAIT['QModelIndex']
  QPlace = WAIT['QPlace']
  QPlaceManager = WAIT['QPlaceManager']
  QPlaceSearchRequest = WAIT['QPlaceSearchRequest']
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QDeclarativeSearchResultModel(QDeclarativeSearchModelBase):
  """
  The cute side of Qt's QDeclarativeSearchResultModel: a plain Python object
  standing in front of one C++ QDeclarativeSearchResultModel.

  It is built on the cute 'QDeclarativeSearchModelBase', as Qt's
  QDeclarativeSearchResultModel is built on Qt's QDeclarativeSearchModelBase,
  and has everything that class has.

  What exists
  -----------

  Every function of Qt's QDeclarativeSearchResultModel that has a ritual and
  that Python can call so far, 39 names in all: 'metaObject', 'tr',
  'searchTerm', 'setSearchTerm', 'recommendationId', 'setRecommendationId',
  'relevanceHint', 'setRelevanceHint', 'visibilityScope',
  'setVisibilityScope', 'favoritesPlugin', 'setFavoritesPlugin',
  'favoritesMatchParameters', 'setFavoritesMatchParameters', 'rowCount',
  'clearData', 'data', 'roleNames', 'updateWith', 'searchTermChanged',
  'categoriesChanged', 'recommendationIdChanged', 'relevanceHintChanged',
  'visibilityScopeChanged', 'rowCountChanged', 'favoritesPluginChanged',
  'favoritesMatchParametersChanged', 'dataChanged', 'incrementalChanged',
  'sendQuery', 'initializePlugin', 'queryFinished', 'onContentUpdated',
  'updateLayout', 'placeUpdated', 'placeRemoved', 'getRow',
  'resultsFromPages', 'removePageRow'. It can be made from Python, in 1 way;
  see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QDeclarativeSearchResultModel::qt_metacast(const char *a0)':
    one of Qt's own inner workings.
  - Qt's 'int QDeclarativeSearchResultModel::qt_metacall(QMetaObject::Call
    a0, int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QDeclarativeSearchResultModel::~QDeclarativeSearchResultModel()':
    the destructor: Python never removes a C++ QDeclarativeSearchResultModel.
  - Qt's 'QQmlListProperty<QDeclarativeCategory>
    QDeclarativeSearchResultModel::categories()': gives a type Python has no
    way to take yet.
  - Qt's 'void QDeclarativeSearchResultModel::categories_append(
    QQmlListProperty<QDeclarativeCategory> *list, QDeclarativeCategory
    *category)': names 'QQmlListProperty<QDeclarativeCategory>', which has no
    cute class yet.
  - Qt's 'qsizetype QDeclarativeSearchResultModel::categories_count(
    QQmlListProperty<QDeclarativeCategory> *list)': names
    'QQmlListProperty<QDeclarativeCategory>', which has no cute class yet.
  - Qt's 'QDeclarativeCategory *QDeclarativeSearchResultModel::category_at(
    QQmlListProperty<QDeclarativeCategory> *list, qsizetype index)': names
    'QQmlListProperty<QDeclarativeCategory>', which has no cute class yet.
  - Qt's 'void QDeclarativeSearchResultModel::categories_clear(
    QQmlListProperty<QDeclarativeCategory> *list)': names
    'QQmlListProperty<QDeclarativeCategory>', which has no cute class yet.

  What has no ritual
  ------------------

  3 of the 52 functions Qt declares: 2 not a gap; 1 cannot be called and
  cannot be called through the meta-object and cannot be copied.

  What to expect
  --------------

  - The C++ QDeclarativeSearchResultModel is created at the first use, not by
    'QDeclarativeSearchResultModel(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QDeclarativeSearchResultModel.
  - Qt tells when it has removed the C++ QDeclarativeSearchResultModel. Every
    call on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QDeclarativeSearchResultModel that has no cute function
    yet, 'categories', 'categories_append', 'categories_clear',
    'categories_count', 'category_at', 'updateSearchRequest', holds a
    function that raises 'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QDeclarativeSearchResultModel, each a class
  #  in here as in C++, and the names Qt has for the combinations of its
  #  flags enums.

  class RelevanceHint(CuteNum):
    """
    The enum 'QDeclarativeSearchResultModel::RelevanceHint' of Qt, with the 3
    names Qt gives in it.
    """

    UnspecifiedHint = Kee[int](0)
    DistanceHint = Kee[int](1)
    LexicalPlaceNameHint = Kee[int](2)

  class SearchResultType(CuteNum):
    """
    The enum 'QDeclarativeSearchResultModel::SearchResultType' of Qt, with
    the 3 names Qt gives in it.
    """

    UnknownSearchResult = Kee[int](0)
    PlaceResult = Kee[int](1)
    ProposedSearchResult = Kee[int](2)

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
    Calls Qt's 'QString QDeclarativeSearchResultModel::tr(const char *s,
    const char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativesearchresultmodel.html#tr

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
    #  QString QDeclarativeSearchResultModel::tr(const char *s, const char
    #      *c, int n)
    return Rituals.call(
        'ritual_ZN29QDeclarativeSearchResultModel2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QDeclarativeSearchResultModel'

  #  A C++ QDeclarativeSearchResultModel Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QDeclarativeSearchResultModel'

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
    *QDeclarativeSearchResultModel::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativesearchresultmodel.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QDeclarativeSearchResultModel::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK29QDeclarativeSearchResultModel10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def searchTerm(self) -> str:
    """
    Calls Qt's 'QString QDeclarativeSearchResultModel::searchTerm() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativesearchresultmodel.html#searchTerm

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QDeclarativeSearchResultModel::searchTerm() const
    return self.uglySide.call(
        'ritual_ZNK29QDeclarativeSearchResultModel10searchTermEv',
    )

  def recommendationId(self) -> str:
    """
    Calls Qt's 'QString QDeclarativeSearchResultModel::recommendationId()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativesearchresultmodel.html

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QDeclarativeSearchResultModel::recommendationId() const
    return self.uglySide.call(
        'ritual_ZNK29QDeclarativeSearchResultModel16recommendationIdEv',
    )

  def relevanceHint(self) -> RelevanceHint:
    """
    Calls Qt's 'QDeclarativeSearchResultModel::RelevanceHint
    QDeclarativeSearchResultModel::relevanceHint() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativesearchresultmodel.html#relevanceHint

    Returns
    -------

    RelevanceHint
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'RelevanceHint(number)'
      gives.
    """
    #  QDeclarativeSearchResultModel::RelevanceHint
    #      QDeclarativeSearchResultModel::relevanceHint() const
    return QDeclarativeSearchResultModel.RelevanceHint(self.uglySide.call(
        'ritual_ZNK29QDeclarativeSearchResultModel13relevanceHintEv',
    ))

  def visibilityScope(self) -> QDeclarativePlace.Visibility:
    """
    Calls Qt's 'QDeclarativePlace::Visibility
    QDeclarativeSearchResultModel::visibilityScope() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativesearchresultmodel.html#visibilityScope

    Returns
    -------

    QDeclarativePlace.Visibility
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QDeclarativePlace.Visibility(number)' gives.
    """
    #  QDeclarativePlace::Visibility
    #      QDeclarativeSearchResultModel::visibilityScope() const
    return QDeclarativePlace.Visibility(self.uglySide.call(
        'ritual_ZNK29QDeclarativeSearchResultModel15visibilityScopeEv',
    ))

  def favoritesPlugin(self) -> Optional[QDeclarativeGeoServiceProvider]:
    """
    Calls Qt's 'QDeclarativeGeoServiceProvider
    *QDeclarativeSearchResultModel::favoritesPlugin() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativesearchresultmodel.html#favoritesPlugin

    Returns
    -------

    Optional[QDeclarativeGeoServiceProvider]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QDeclarativeGeoServiceProvider
    #      *QDeclarativeSearchResultModel::favoritesPlugin() const
    address = self.uglySide.call(
        'ritual_ZNK29QDeclarativeSearchResultModel15favoritesPluginEv',
    )
    from . import QDeclarativeGeoServiceProvider
    return QDeclarativeGeoServiceProvider._cuteAt(address)

  def favoritesMatchParameters(self) -> QMap[str, QVariant]:
    """
    Calls Qt's 'QVariantMap
    QDeclarativeSearchResultModel::favoritesMatchParameters() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativesearchresultmodel.html

    Returns
    -------

    QMap[str, QVariant]
      A new cute map around the copy Qt gave back. Python owns it.
    """
    #  QVariantMap QDeclarativeSearchResultModel::favoritesMatchParameters()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK29QDeclarativeSearchResultModel24favoritesMatchParameter'
        'sEv',
    )
    from ..QtCore import QVariant
    return QMap[str, QVariant]._cuteOwning(address)

  @overload()
  @overload(QModelIndex)
  def rowCount(self, parent: Optional[QModelIndex] = None) -> int:
    """
    Calls Qt's 'int QDeclarativeSearchResultModel::rowCount(const QModelIndex
    &parent) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativesearchresultmodel.html#rowCount

    Parameters
    ----------

    parent : Optional[QModelIndex]
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own. May be left out, as in Qt: a new 'QModelIndex()' is then
      passed on.
    """
    #  int QDeclarativeSearchResultModel::rowCount(const QModelIndex &parent)
    #      const
    if parent is None:
      from ..QtCore import QModelIndex
      parent = QModelIndex()
    ritual = (
        'ritual_ZNK29QDeclarativeSearchResultModel8rowCountERK11QModelIndex')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK29QDeclarativeSearchResultModel8rowCountERK11QMode'
          'lIndex')
    return self.uglySide.call(ritual, self._valueOf(parent))

  @overload(QModelIndex)
  @overload(QModelIndex, int)
  def data(self, index: QModelIndex, role: int = 0) -> QVariant:
    """
    Calls Qt's 'QVariant QDeclarativeSearchResultModel::data(const
    QModelIndex &index, int role) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativesearchresultmodel.html#data

    Parameters
    ----------

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    role : int
      Passed on as it is. May be left out, as in Qt: it is then 0.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QDeclarativeSearchResultModel::data(const QModelIndex &index,
    #      int role) const
    ritual = (
        'ritual_ZNK29QDeclarativeSearchResultModel4dataERK11QModelIndexi')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK29QDeclarativeSearchResultModel4dataERK11QModelInd'
          'exi')
    address = self.uglySide.call(ritual, self._valueOf(index), role)
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  @overload(int, str)
  def data(self, index: int, roleName: str) -> QVariant:
    """
    Calls Qt's 'QVariant QDeclarativeSearchResultModel::data(int index, const
    QString &roleName) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativesearchresultmodel.html#data

    Parameters
    ----------

    index : int
      Passed on as it is.

    roleName : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QDeclarativeSearchResultModel::data(int index, const QString
    #      &roleName) const
    address = self.uglySide.call(
        'ritual_ZNK29QDeclarativeSearchResultModel4dataEiRK7QString',
        index, roleName,
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  def roleNames(self) -> QHash[int, QByteArray]:
    """
    Calls Qt's 'QHash<int, QByteArray>
    QDeclarativeSearchResultModel::roleNames() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativesearchresultmodel.html#roleNames

    Returns
    -------

    QHash[int, QByteArray]
      A new cute map around the copy Qt gave back. Python owns it.
    """
    #  QHash<int, QByteArray> QDeclarativeSearchResultModel::roleNames()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK29QDeclarativeSearchResultModel9roleNamesEv',
    )
    from ..QtCore import QByteArray
    return QHash[int, QByteArray]._cuteOwning(address)

  @overload(str)
  def getRow(self, placeId: str) -> int:
    """
    Calls Qt's 'int QDeclarativeSearchResultModel::getRow(const QString
    &placeId) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativesearchresultmodel.html#getRow

    Parameters
    ----------

    placeId : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  int QDeclarativeSearchResultModel::getRow(const QString &placeId)
    #      const
    return self.uglySide.call(
        'ritual_ZNK29QDeclarativeSearchResultModel6getRowERK7QString',
        placeId,
    )

  def resultsFromPages(self) -> QList[QPlaceSearchResult]:
    """
    Calls Qt's 'QList<QPlaceSearchResult>
    QDeclarativeSearchResultModel::resultsFromPages() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativesearchresultmodel.html

    Returns
    -------

    QList[QPlaceSearchResult]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QPlaceSearchResult>
    #      QDeclarativeSearchResultModel::resultsFromPages() const
    address = self.uglySide.call(
        'ritual_ZNK29QDeclarativeSearchResultModel16resultsFromPagesEv',
    )
    from . import QPlaceSearchResult
    return QList[QPlaceSearchResult]._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setSearchTerm(self, searchTerm: str) -> None:
    """
    Calls Qt's 'void QDeclarativeSearchResultModel::setSearchTerm(const
    QString &searchTerm)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativesearchresultmodel.html#setSearchTerm

    Parameters
    ----------

    searchTerm : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QDeclarativeSearchResultModel::setSearchTerm(const QString
    #      &searchTerm)
    self.uglySide.call(
        'ritual_ZN29QDeclarativeSearchResultModel13setSearchTermERK7QString',
        searchTerm,
    )

  @overload(str)
  def setRecommendationId(self, recommendationId: str) -> None:
    """
    Calls Qt's 'void QDeclarativeSearchResultModel::setRecommendationId(const
    QString &recommendationId)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativesearchresultmodel.html

    Parameters
    ----------

    recommendationId : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QDeclarativeSearchResultModel::setRecommendationId(const QString
    #      &recommendationId)
    self.uglySide.call(
        'ritual_ZN29QDeclarativeSearchResultModel19setRecommendationIdERK7Q'
        'String',
        recommendationId,
    )

  @overload(RelevanceHint)
  def setRelevanceHint(self, hint: RelevanceHint) -> None:
    """
    Calls Qt's 'void QDeclarativeSearchResultModel::setRelevanceHint(
    QDeclarativeSearchResultModel::RelevanceHint hint)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativesearchresultmodel.html

    Parameters
    ----------

    hint : RelevanceHint
      Passed on as its number.
    """
    #  void QDeclarativeSearchResultModel::setRelevanceHint(
    #      QDeclarativeSearchResultModel::RelevanceHint hint)
    self.uglySide.call(
        'ritual_ZN29QDeclarativeSearchResultModel16setRelevanceHintENS_13Re'
        'levanceHintE',
        hint.value,
    )

  @overload(QDeclarativePlace.Visibility)
  def setVisibilityScope(
      self,
      visibilityScope: QDeclarativePlace.Visibility,
  ) -> None:
    """
    Calls Qt's 'void
    QDeclarativeSearchResultModel::setVisibilityScope(QDeclarativePlace::
    Visibility visibilityScope)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativesearchresultmodel.html

    Parameters
    ----------

    visibilityScope : QDeclarativePlace.Visibility
      Passed on as its number.
    """
    #  void QDeclarativeSearchResultModel::setVisibilityScope(
    #      QDeclarativePlace::Visibility visibilityScope)
    self.uglySide.call(
        'ritual_ZN29QDeclarativeSearchResultModel18setVisibilityScopeEN17QD'
        'eclarativePlace10VisibilityE',
        visibilityScope.value,
    )

  @overload(QDeclarativeGeoServiceProvider)
  @overload(NoneType)
  def setFavoritesPlugin(
      self,
      plugin: Optional[QDeclarativeGeoServiceProvider],
  ) -> None:
    """
    Calls Qt's 'void QDeclarativeSearchResultModel::setFavoritesPlugin(
    QDeclarativeGeoServiceProvider *plugin)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativesearchresultmodel.html

    Parameters
    ----------

    plugin : Optional[QDeclarativeGeoServiceProvider]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QDeclarativeSearchResultModel::setFavoritesPlugin(
    #      QDeclarativeGeoServiceProvider *plugin)
    self.uglySide.call(
        'ritual_ZN29QDeclarativeSearchResultModel18setFavoritesPluginEP30QD'
        'eclarativeGeoServiceProvider',
        self._addressOf(plugin),
    )

  @overload(QMap[str, QVariant])
  def setFavoritesMatchParameters(
      self,
      parameters: QMap[str, QVariant],
  ) -> None:
    """
    Calls Qt's 'void
    QDeclarativeSearchResultModel::setFavoritesMatchParameters(const
    QVariantMap &parameters)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativesearchresultmodel.html

    Parameters
    ----------

    parameters : QMap[str, QVariant]
      Passed on as a map of Qt: Qt reads the C++ map, which stays Python's
      own. A dict of Python is made into one first, and refused when a key or
      a value does not fit.
    """
    #  void QDeclarativeSearchResultModel::setFavoritesMatchParameters(const
    #      QVariantMap &parameters)
    self.uglySide.call(
        'ritual_ZN29QDeclarativeSearchResultModel27setFavoritesMatchParamet'
        'ersERK4QMapI7QString8QVariantE',
        self._valueOf(parameters),
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
    'QDeclarativeSearchResultModel::QDeclarativeSearchResultModel(QObject
    *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativesearchresultmodel.html

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QDeclarativeSearchResultModel::QDeclarativeSearchResultModel(QObject
    #      *parent)
    self._noteCreation(QDeclarativeSearchResultModel, lambda: Rituals.call(
        'ritual_ZN29QDeclarativeSearchResultModelC1EP7QObject',
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
    Calls Qt's 'void QDeclarativeSearchResultModel::clearData(bool
    suppressSignal)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativesearchresultmodel.html#clearData

    Parameters
    ----------

    suppressSignal : bool
      Passed on as it is. May be left out, as in Qt: it is then False.
    """
    #  void QDeclarativeSearchResultModel::clearData(bool suppressSignal)
    ritual = 'ritual_ZN29QDeclarativeSearchResultModel9clearDataEb'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN29QDeclarativeSearchResultModel9clearDataEb'
    self.uglySide.call(ritual, suppressSignal)

  @overload(int)
  def updateWith(self, proposedSearchIndex: int) -> None:
    """
    Calls Qt's 'void QDeclarativeSearchResultModel::updateWith(int
    proposedSearchIndex)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativesearchresultmodel.html#updateWith

    Parameters
    ----------

    proposedSearchIndex : int
      Passed on as it is.
    """
    #  void QDeclarativeSearchResultModel::updateWith(int
    #      proposedSearchIndex)
    self.uglySide.call(
        'ritual_ZN29QDeclarativeSearchResultModel10updateWithEi',
        proposedSearchIndex,
    )

  def searchTermChanged(self) -> None:
    """
    Calls Qt's 'void QDeclarativeSearchResultModel::searchTermChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativesearchresultmodel.html
    """
    #  void QDeclarativeSearchResultModel::searchTermChanged()
    self.uglySide.call(
        'ritual_ZN29QDeclarativeSearchResultModel17searchTermChangedEv',
    )

  def categoriesChanged(self) -> None:
    """
    Calls Qt's 'void QDeclarativeSearchResultModel::categoriesChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativesearchresultmodel.html
    """
    #  void QDeclarativeSearchResultModel::categoriesChanged()
    self.uglySide.call(
        'ritual_ZN29QDeclarativeSearchResultModel17categoriesChangedEv',
    )

  def recommendationIdChanged(self) -> None:
    """
    Calls Qt's 'void
    QDeclarativeSearchResultModel::recommendationIdChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativesearchresultmodel.html
    """
    #  void QDeclarativeSearchResultModel::recommendationIdChanged()
    self.uglySide.call(
        'ritual_ZN29QDeclarativeSearchResultModel23recommendationIdChangedE'
        'v',
    )

  def relevanceHintChanged(self) -> None:
    """
    Calls Qt's 'void QDeclarativeSearchResultModel::relevanceHintChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativesearchresultmodel.html
    """
    #  void QDeclarativeSearchResultModel::relevanceHintChanged()
    self.uglySide.call(
        'ritual_ZN29QDeclarativeSearchResultModel20relevanceHintChangedEv',
    )

  def visibilityScopeChanged(self) -> None:
    """
    Calls Qt's 'void
    QDeclarativeSearchResultModel::visibilityScopeChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativesearchresultmodel.html
    """
    #  void QDeclarativeSearchResultModel::visibilityScopeChanged()
    self.uglySide.call(
        'ritual_ZN29QDeclarativeSearchResultModel22visibilityScopeChangedEv',
    )

  def rowCountChanged(self) -> None:
    """
    Calls Qt's 'void QDeclarativeSearchResultModel::rowCountChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativesearchresultmodel.html#rowCountChanged
    """
    #  void QDeclarativeSearchResultModel::rowCountChanged()
    self.uglySide.call(
        'ritual_ZN29QDeclarativeSearchResultModel15rowCountChangedEv',
    )

  def favoritesPluginChanged(self) -> None:
    """
    Calls Qt's 'void
    QDeclarativeSearchResultModel::favoritesPluginChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativesearchresultmodel.html
    """
    #  void QDeclarativeSearchResultModel::favoritesPluginChanged()
    self.uglySide.call(
        'ritual_ZN29QDeclarativeSearchResultModel22favoritesPluginChangedEv',
    )

  def favoritesMatchParametersChanged(self) -> None:
    """
    Calls Qt's 'void
    QDeclarativeSearchResultModel::favoritesMatchParametersChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativesearchresultmodel.html
    """
    #  void QDeclarativeSearchResultModel::favoritesMatchParametersChanged()
    self.uglySide.call(
        'ritual_ZN29QDeclarativeSearchResultModel31favoritesMatchParameters'
        'ChangedEv',
    )

  def dataChanged(self) -> None:
    """
    Calls Qt's 'void QDeclarativeSearchResultModel::dataChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativesearchresultmodel.html#dataChanged
    """
    #  void QDeclarativeSearchResultModel::dataChanged()
    self.uglySide.call(
        'ritual_ZN29QDeclarativeSearchResultModel11dataChangedEv',
    )

  def incrementalChanged(self) -> None:
    """
    Calls Qt's 'void QDeclarativeSearchResultModel::incrementalChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativesearchresultmodel.html
    """
    #  void QDeclarativeSearchResultModel::incrementalChanged()
    self.uglySide.call(
        'ritual_ZN29QDeclarativeSearchResultModel18incrementalChangedEv',
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
    *QDeclarativeSearchResultModel::sendQuery(QPlaceManager *manager, const
    QPlaceSearchRequest &request)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativesearchresultmodel.html#sendQuery

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
    #  QPlaceReply *QDeclarativeSearchResultModel::sendQuery(QPlaceManager
    #      *manager, const QPlaceSearchRequest &request)
    ritual = (
        'ritual_ZN29QDeclarativeSearchResultModel9sendQueryEP13QPlaceManage'
        'rRK19QPlaceSearchRequest')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN29QDeclarativeSearchResultModel9sendQueryEP13QPlace'
          'ManagerRK19QPlaceSearchRequest')
    address = self.uglySide.call(
        ritual, self._addressOf(manager), self._valueOf(request),
    )
    from . import QPlaceReply
    return QPlaceReply._cuteAt(address)

  @overload(QDeclarativeGeoServiceProvider)
  @overload(NoneType)
  def initializePlugin(
      self,
      plugin: Optional[QDeclarativeGeoServiceProvider],
  ) -> None:
    """
    Calls Qt's 'void QDeclarativeSearchResultModel::initializePlugin(
    QDeclarativeGeoServiceProvider *plugin)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativesearchresultmodel.html

    Parameters
    ----------

    plugin : Optional[QDeclarativeGeoServiceProvider]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QDeclarativeSearchResultModel::initializePlugin(
    #      QDeclarativeGeoServiceProvider *plugin)
    ritual = (
        'ritual_ZN29QDeclarativeSearchResultModel16initializePluginEP30QDec'
        'larativeGeoServiceProvider')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN29QDeclarativeSearchResultModel16initializePluginEP'
          '30QDeclarativeGeoServiceProvider')
    self.uglySide.call(ritual, self._addressOf(plugin))

  def queryFinished(self) -> None:
    """
    Calls Qt's 'void QDeclarativeSearchResultModel::queryFinished()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativesearchresultmodel.html#queryFinished
    """
    #  void QDeclarativeSearchResultModel::queryFinished()
    ritual = 'ritual_ZN29QDeclarativeSearchResultModel13queryFinishedEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN29QDeclarativeSearchResultModel13queryFinishedEv')
    self.uglySide.call(ritual)

  def onContentUpdated(self) -> None:
    """
    Calls Qt's 'void QDeclarativeSearchResultModel::onContentUpdated()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativesearchresultmodel.html
    """
    #  void QDeclarativeSearchResultModel::onContentUpdated()
    ritual = 'ritual_ZN29QDeclarativeSearchResultModel16onContentUpdatedEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN29QDeclarativeSearchResultModel16onContentUpdatedEv')
    self.uglySide.call(ritual)

  @overload(QList[QPlace])
  def updateLayout(self, favoritePlaces: QList[QPlace]) -> None:
    """
    Calls Qt's 'void QDeclarativeSearchResultModel::updateLayout(const
    QList<QPlace> &favoritePlaces)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativesearchresultmodel.html#updateLayout

    Parameters
    ----------

    favoritePlaces : QList[QPlace]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QDeclarativeSearchResultModel::updateLayout(const QList<QPlace>
    #      &favoritePlaces)
    self.uglySide.call(
        'ritual_ZN29QDeclarativeSearchResultModel12updateLayoutERK5QListI6Q'
        'PlaceE',
        self._valueOf(favoritePlaces),
    )

  @overload(str)
  def placeUpdated(self, placeId: str) -> None:
    """
    Calls Qt's 'void QDeclarativeSearchResultModel::placeUpdated(const
    QString &placeId)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativesearchresultmodel.html#placeUpdated

    Parameters
    ----------

    placeId : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QDeclarativeSearchResultModel::placeUpdated(const QString
    #      &placeId)
    self.uglySide.call(
        'ritual_ZN29QDeclarativeSearchResultModel12placeUpdatedERK7QString',
        placeId,
    )

  @overload(str)
  def placeRemoved(self, placeId: str) -> None:
    """
    Calls Qt's 'void QDeclarativeSearchResultModel::placeRemoved(const
    QString &placeId)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativesearchresultmodel.html#placeRemoved

    Parameters
    ----------

    placeId : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QDeclarativeSearchResultModel::placeRemoved(const QString
    #      &placeId)
    self.uglySide.call(
        'ritual_ZN29QDeclarativeSearchResultModel12placeRemovedERK7QString',
        placeId,
    )

  @overload(int)
  def removePageRow(self, row: int) -> None:
    """
    Calls Qt's 'void QDeclarativeSearchResultModel::removePageRow(int row)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativesearchresultmodel.html#removePageRow

    Parameters
    ----------

    row : int
      Passed on as it is.
    """
    #  void QDeclarativeSearchResultModel::removePageRow(int row)
    self.uglySide.call(
        'ritual_ZN29QDeclarativeSearchResultModel13removePageRowEi', row,
    )

  @staticmethod
  def categories(*__, **_) -> Never:
    """
    Qt's 'QQmlListProperty<QDeclarativeCategory>
    QDeclarativeSearchResultModel::categories()': gives a type Python has no
    way to take yet.
    """
    raise NotImplementedError(
        "'QDeclarativeSearchResultModel.categories' has no cute function "
        "yet. Qt's 'QQmlListProperty<QDeclarativeCategory> "
        "QDeclarativeSearchResultModel::categories()': gives a type Python "
        "has no way to take yet.")

  @staticmethod
  def categories_append(*__, **_) -> Never:
    """
    Qt's 'void QDeclarativeSearchResultModel::categories_append(
    QQmlListProperty<QDeclarativeCategory> *list, QDeclarativeCategory
    *category)': names 'QQmlListProperty<QDeclarativeCategory>', which has no
    cute class yet.
    """
    raise NotImplementedError(
        "'QDeclarativeSearchResultModel.categories_append' has no cute "
        "function yet. Qt's 'void "
        "QDeclarativeSearchResultModel::categories_append(QQmlListProperty<Q"
        "DeclarativeCategory> *list, QDeclarativeCategory *category)': "
        "names 'QQmlListProperty<QDeclarativeCategory>', which has no cute "
        "class yet.")

  @staticmethod
  def categories_clear(*__, **_) -> Never:
    """
    Qt's 'void QDeclarativeSearchResultModel::categories_clear(
    QQmlListProperty<QDeclarativeCategory> *list)': names
    'QQmlListProperty<QDeclarativeCategory>', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QDeclarativeSearchResultModel.categories_clear' has no cute "
        "function yet. Qt's 'void "
        "QDeclarativeSearchResultModel::categories_clear(QQmlListProperty<QD"
        "eclarativeCategory> *list)': names "
        "'QQmlListProperty<QDeclarativeCategory>', which has no cute class "
        "yet.")

  @staticmethod
  def categories_count(*__, **_) -> Never:
    """
    Qt's 'qsizetype QDeclarativeSearchResultModel::categories_count(
    QQmlListProperty<QDeclarativeCategory> *list)': names
    'QQmlListProperty<QDeclarativeCategory>', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QDeclarativeSearchResultModel.categories_count' has no cute "
        "function yet. Qt's 'qsizetype "
        "QDeclarativeSearchResultModel::categories_count(QQmlListProperty<QD"
        "eclarativeCategory> *list)': names "
        "'QQmlListProperty<QDeclarativeCategory>', which has no cute class "
        "yet.")

  @staticmethod
  def category_at(*__, **_) -> Never:
    """
    Qt's 'QDeclarativeCategory *QDeclarativeSearchResultModel::category_at(
    QQmlListProperty<QDeclarativeCategory> *list, qsizetype index)': names
    'QQmlListProperty<QDeclarativeCategory>', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QDeclarativeSearchResultModel.category_at' has no cute function "
        "yet. Qt's 'QDeclarativeCategory "
        "*QDeclarativeSearchResultModel::category_at(QQmlListProperty<QDecla"
        "rativeCategory> *list, qsizetype index)': names "
        "'QQmlListProperty<QDeclarativeCategory>', which has no cute class "
        "yet.")

  @staticmethod
  def updateSearchRequest(*__, **_) -> Never:
    """
    Qt's 'void QDeclarativeSearchResultModel::updateSearchRequest()': cannot
    be called and cannot be called through the meta-object and cannot be
    copied: no header file has its code, Qt's source does not mark it or its
    class for use from outside Qt or writes it 'inline' or nowhere, and it is
    no signal, slot or invokable function giving back nothing, of a class
    built on QObject, and Qt's source has no code for it that could be told
    from the rest.
    """
    raise NotImplementedError(
        "'QDeclarativeSearchResultModel.updateSearchRequest' has no cute "
        "function yet. Qt's 'void "
        "QDeclarativeSearchResultModel::updateSearchRequest()': cannot be "
        "called and cannot be called through the meta-object and cannot be "
        "copied: no header file has its code, Qt's source does not mark it "
        "or its class for use from outside Qt or writes it 'inline' or "
        "nowhere, and it is no signal, slot or invokable function giving "
        "back nothing, of a class built on QObject, and Qt's source has no "
        "code for it that could be told from the rest.")
