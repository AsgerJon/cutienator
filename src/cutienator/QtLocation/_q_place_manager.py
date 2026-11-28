"""
QPlaceManager binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtLocation/qplacemanager.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QList, QObject, QStringList
from . import QPlaceReply

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QLocale, QMetaObject
  from . import QPlace, QPlaceCategory, QPlaceContentReply
  from . import QPlaceContentRequest, QPlaceDetailsReply, QPlaceIdReply
  from . import QPlaceManagerEngine, QPlaceMatchReply, QPlaceMatchRequest
  from . import QPlaceSearchReply, QPlaceSearchRequest
  from . import QPlaceSearchSuggestionReply
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QLocale = WAIT['QLocale']
  QPlace = WAIT['QPlace']
  QPlaceCategory = WAIT['QPlaceCategory']
  QPlaceContentRequest = WAIT['QPlaceContentRequest']
  QPlaceManagerEngine = WAIT['QPlaceManagerEngine']
  QPlaceMatchRequest = WAIT['QPlaceMatchRequest']
  QPlaceSearchRequest = WAIT['QPlaceSearchRequest']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QPlaceManager(QObject):
  """
  The cute side of Qt's QPlaceManager: a plain Python object standing in
  front of one C++ QPlaceManager.

  It is built on the cute 'QObject', as Qt's QPlaceManager is built on Qt's
  QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QPlaceManager that has a ritual and that Python can
  call so far, 31 names in all: 'metaObject', 'tr', 'managerName',
  'managerVersion', 'getPlaceDetails', 'getPlaceContent', 'search',
  'searchSuggestions', 'savePlace', 'removePlace', 'saveCategory',
  'removeCategory', 'initializeCategories', 'parentCategoryId',
  'childCategoryIds', 'category', 'childCategories', 'locales', 'setLocale',
  'setLocales', 'compatiblePlace', 'matchingPlaces', 'finished',
  'errorOccurred', 'placeAdded', 'placeUpdated', 'placeRemoved',
  'categoryAdded', 'categoryUpdated', 'categoryRemoved', 'dataChanged'. It
  can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QPlaceManager::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QPlaceManager::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QPlaceManager::~QPlaceManager()': the destructor: Python never
    removes a C++ QPlaceManager.

  What has no ritual
  ------------------

  4 of the 39 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QPlaceManager is created at the first use, not by
    'QPlaceManager(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QPlaceManager.
  - Qt tells when it has removed the C++ QPlaceManager. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

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
    Calls Qt's 'QString QPlaceManager::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qplacemanager.html#tr

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
    #  QString QPlaceManager::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN13QPlaceManager2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QPlaceManager'

  #  A C++ QPlaceManager Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QPlaceManager'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QPlaceManager::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qplacemanager.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QPlaceManager::metaObject() const
    address = self.uglySide.call('ritual_ZNK13QPlaceManager10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def managerName(self) -> str:
    """
    Calls Qt's 'QString QPlaceManager::managerName() const'.

    Qt's own words: https://doc.qt.io/qt-6/qplacemanager.html#managerName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QPlaceManager::managerName() const
    return self.uglySide.call('ritual_ZNK13QPlaceManager11managerNameEv')

  def managerVersion(self) -> int:
    """
    Calls Qt's 'int QPlaceManager::managerVersion() const'.

    Qt's own words: https://doc.qt.io/qt-6/qplacemanager.html#managerVersion
    """
    #  int QPlaceManager::managerVersion() const
    return self.uglySide.call('ritual_ZNK13QPlaceManager14managerVersionEv')

  @overload(str)
  def getPlaceDetails(self, placeId: str) -> Optional[QPlaceDetailsReply]:
    """
    Calls Qt's 'QPlaceDetailsReply *QPlaceManager::getPlaceDetails(const
    QString &placeId) const'.

    Qt's own words: https://doc.qt.io/qt-6/qplacemanager.html#getPlaceDetails

    Parameters
    ----------

    placeId : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    Optional[QPlaceDetailsReply]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPlaceDetailsReply *QPlaceManager::getPlaceDetails(const QString
    #      &placeId) const
    address = self.uglySide.call(
        'ritual_ZNK13QPlaceManager15getPlaceDetailsERK7QString', placeId,
    )
    from . import QPlaceDetailsReply
    return QPlaceDetailsReply._cuteAt(address)

  @overload(QPlaceContentRequest)
  def getPlaceContent(
      self,
      request: QPlaceContentRequest,
  ) -> Optional[QPlaceContentReply]:
    """
    Calls Qt's 'QPlaceContentReply *QPlaceManager::getPlaceContent(const
    QPlaceContentRequest &request) const'.

    Qt's own words: https://doc.qt.io/qt-6/qplacemanager.html#getPlaceContent

    Parameters
    ----------

    request : QPlaceContentRequest
      Passed on as a value: Qt reads the C++ QPlaceContentRequest, which
      stays Python's own.

    Returns
    -------

    Optional[QPlaceContentReply]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPlaceContentReply *QPlaceManager::getPlaceContent(const
    #      QPlaceContentRequest &request) const
    address = self.uglySide.call(
        'ritual_ZNK13QPlaceManager15getPlaceContentERK20QPlaceContentReques'
        't',
        self._valueOf(request),
    )
    from . import QPlaceContentReply
    return QPlaceContentReply._cuteAt(address)

  @overload(QPlaceSearchRequest)
  def search(
      self,
      query: QPlaceSearchRequest,
  ) -> Optional[QPlaceSearchReply]:
    """
    Calls Qt's 'QPlaceSearchReply *QPlaceManager::search(const
    QPlaceSearchRequest &query) const'.

    Qt's own words: https://doc.qt.io/qt-6/qplacemanager.html#search

    Parameters
    ----------

    query : QPlaceSearchRequest
      Passed on as a value: Qt reads the C++ QPlaceSearchRequest, which stays
      Python's own.

    Returns
    -------

    Optional[QPlaceSearchReply]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPlaceSearchReply *QPlaceManager::search(const QPlaceSearchRequest
    #      &query) const
    address = self.uglySide.call(
        'ritual_ZNK13QPlaceManager6searchERK19QPlaceSearchRequest',
        self._valueOf(query),
    )
    from . import QPlaceSearchReply
    return QPlaceSearchReply._cuteAt(address)

  @overload(QPlaceSearchRequest)
  def searchSuggestions(
      self,
      request: QPlaceSearchRequest,
  ) -> Optional[QPlaceSearchSuggestionReply]:
    """
    Calls Qt's 'QPlaceSearchSuggestionReply
    *QPlaceManager::searchSuggestions(const QPlaceSearchRequest &request)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplacemanager.html#searchSuggestions

    Parameters
    ----------

    request : QPlaceSearchRequest
      Passed on as a value: Qt reads the C++ QPlaceSearchRequest, which stays
      Python's own.

    Returns
    -------

    Optional[QPlaceSearchSuggestionReply]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPlaceSearchSuggestionReply *QPlaceManager::searchSuggestions(const
    #      QPlaceSearchRequest &request) const
    address = self.uglySide.call(
        'ritual_ZNK13QPlaceManager17searchSuggestionsERK19QPlaceSearchReque'
        'st',
        self._valueOf(request),
    )
    from . import QPlaceSearchSuggestionReply
    return QPlaceSearchSuggestionReply._cuteAt(address)

  @overload(str)
  def parentCategoryId(self, categoryId: str) -> str:
    """
    Calls Qt's 'QString QPlaceManager::parentCategoryId(const QString
    &categoryId) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplacemanager.html#parentCategoryId

    Parameters
    ----------

    categoryId : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QPlaceManager::parentCategoryId(const QString &categoryId)
    #      const
    return self.uglySide.call(
        'ritual_ZNK13QPlaceManager16parentCategoryIdERK7QString', categoryId,
    )

  @overload()
  @overload(str)
  def childCategoryIds(self, parentId: str = '') -> QStringList:
    """
    Calls Qt's 'QStringList QPlaceManager::childCategoryIds(const QString
    &parentId) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplacemanager.html#childCategoryIds

    Parameters
    ----------

    parentId : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QPlaceManager::childCategoryIds(const QString &parentId)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK13QPlaceManager16childCategoryIdsERK7QString', parentId,
    )
    return QStringList._cuteOwning(address)

  @overload(str)
  def category(self, categoryId: str) -> QPlaceCategory:
    """
    Calls Qt's 'QPlaceCategory QPlaceManager::category(const QString
    &categoryId) const'.

    Qt's own words: https://doc.qt.io/qt-6/qplacemanager.html#category

    Parameters
    ----------

    categoryId : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QPlaceCategory
      A new cute QPlaceCategory around the copy Qt gave back. Python owns it.
    """
    #  QPlaceCategory QPlaceManager::category(const QString &categoryId)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK13QPlaceManager8categoryERK7QString', categoryId,
    )
    from . import QPlaceCategory
    return QPlaceCategory._cuteOwning(address)

  @overload()
  @overload(str)
  def childCategories(self, parentId: str = '') -> QList[QPlaceCategory]:
    """
    Calls Qt's 'QList<QPlaceCategory> QPlaceManager::childCategories(const
    QString &parentId) const'.

    Qt's own words: https://doc.qt.io/qt-6/qplacemanager.html#childCategories

    Parameters
    ----------

    parentId : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.

    Returns
    -------

    QList[QPlaceCategory]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QPlaceCategory> QPlaceManager::childCategories(const QString
    #      &parentId) const
    address = self.uglySide.call(
        'ritual_ZNK13QPlaceManager15childCategoriesERK7QString', parentId,
    )
    from . import QPlaceCategory
    return QList[QPlaceCategory]._cuteOwning(address)

  def locales(self) -> QList[QLocale]:
    """
    Calls Qt's 'QList<QLocale> QPlaceManager::locales() const'.

    Qt's own words: https://doc.qt.io/qt-6/qplacemanager.html#locales

    Returns
    -------

    QList[QLocale]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QLocale> QPlaceManager::locales() const
    address = self.uglySide.call('ritual_ZNK13QPlaceManager7localesEv')
    from ..QtCore import QLocale
    return QList[QLocale]._cuteOwning(address)

  @overload(QPlace)
  def compatiblePlace(self, place: QPlace) -> QPlace:
    """
    Calls Qt's 'QPlace QPlaceManager::compatiblePlace(const QPlace &place)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qplacemanager.html#compatiblePlace

    Parameters
    ----------

    place : QPlace
      Passed on as a value: Qt reads the C++ QPlace, which stays Python's
      own.

    Returns
    -------

    QPlace
      A new cute QPlace around the copy Qt gave back. Python owns it.
    """
    #  QPlace QPlaceManager::compatiblePlace(const QPlace &place) const
    address = self.uglySide.call(
        'ritual_ZNK13QPlaceManager15compatiblePlaceERK6QPlace',
        self._valueOf(place),
    )
    from . import QPlace
    return QPlace._cuteOwning(address)

  @overload(QPlaceMatchRequest)
  def matchingPlaces(
      self,
      request: QPlaceMatchRequest,
  ) -> Optional[QPlaceMatchReply]:
    """
    Calls Qt's 'QPlaceMatchReply *QPlaceManager::matchingPlaces(const
    QPlaceMatchRequest &request) const'.

    Qt's own words: https://doc.qt.io/qt-6/qplacemanager.html#matchingPlaces

    Parameters
    ----------

    request : QPlaceMatchRequest
      Passed on as a value: Qt reads the C++ QPlaceMatchRequest, which stays
      Python's own.

    Returns
    -------

    Optional[QPlaceMatchReply]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPlaceMatchReply *QPlaceManager::matchingPlaces(const
    #      QPlaceMatchRequest &request) const
    address = self.uglySide.call(
        'ritual_ZNK13QPlaceManager14matchingPlacesERK18QPlaceMatchRequest',
        self._valueOf(request),
    )
    from . import QPlaceMatchReply
    return QPlaceMatchReply._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QLocale)
  def setLocale(self, locale: QLocale) -> None:
    """
    Calls Qt's 'void QPlaceManager::setLocale(const QLocale &locale)'.

    Qt's own words: https://doc.qt.io/qt-6/qplacemanager.html#setLocale

    Parameters
    ----------

    locale : QLocale
      Passed on as a value: Qt reads the C++ QLocale, which stays Python's
      own.
    """
    #  void QPlaceManager::setLocale(const QLocale &locale)
    self.uglySide.call(
        'ritual_ZN13QPlaceManager9setLocaleERK7QLocale',
        self._valueOf(locale),
    )

  @overload(QList[QLocale])
  def setLocales(self, locale: QList[QLocale]) -> None:
    """
    Calls Qt's 'void QPlaceManager::setLocales(const QList<QLocale>
    &locale)'.

    Qt's own words: https://doc.qt.io/qt-6/qplacemanager.html#setLocales

    Parameters
    ----------

    locale : QList[QLocale]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QPlaceManager::setLocales(const QList<QLocale> &locale)
    self.uglySide.call(
        'ritual_ZN13QPlaceManager10setLocalesERK5QListI7QLocaleE',
        self._valueOf(locale),
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

  @overload(QPlaceManagerEngine)
  @overload(NoneType)
  @overload(QPlaceManagerEngine, QObject)
  @overload(QPlaceManagerEngine, NoneType)
  @overload(NoneType, QObject)
  @overload(NoneType, NoneType)
  def __init__(
      self,
      engine: Optional[QPlaceManagerEngine],
      parent: Optional[QObject] = None,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QPlaceManager::QPlaceManager(QPlaceManagerEngine *engine, QObject
    *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qplacemanager.html#QPlaceManager

    Parameters
    ----------

    engine : Optional[QPlaceManagerEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QPlaceManager::QPlaceManager(QPlaceManagerEngine *engine, QObject
    #      *parent)
    self._noteCreation(QPlaceManager, lambda: Rituals.call(
        'ritual_ZN13QPlaceManagerC1EP19QPlaceManagerEngineP7QObject',
        self._addressOf(engine), self._addressOf(parent, 'QObject'),
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

  @overload(QPlace)
  def savePlace(self, place: QPlace) -> Optional[QPlaceIdReply]:
    """
    Calls Qt's 'QPlaceIdReply *QPlaceManager::savePlace(const QPlace
    &place)'.

    Qt's own words: https://doc.qt.io/qt-6/qplacemanager.html#savePlace

    Parameters
    ----------

    place : QPlace
      Passed on as a value: Qt reads the C++ QPlace, which stays Python's
      own.

    Returns
    -------

    Optional[QPlaceIdReply]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPlaceIdReply *QPlaceManager::savePlace(const QPlace &place)
    address = self.uglySide.call(
        'ritual_ZN13QPlaceManager9savePlaceERK6QPlace', self._valueOf(place),
    )
    from . import QPlaceIdReply
    return QPlaceIdReply._cuteAt(address)

  @overload(str)
  def removePlace(self, placeId: str) -> Optional[QPlaceIdReply]:
    """
    Calls Qt's 'QPlaceIdReply *QPlaceManager::removePlace(const QString
    &placeId)'.

    Qt's own words: https://doc.qt.io/qt-6/qplacemanager.html#removePlace

    Parameters
    ----------

    placeId : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    Optional[QPlaceIdReply]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPlaceIdReply *QPlaceManager::removePlace(const QString &placeId)
    address = self.uglySide.call(
        'ritual_ZN13QPlaceManager11removePlaceERK7QString', placeId,
    )
    from . import QPlaceIdReply
    return QPlaceIdReply._cuteAt(address)

  @overload(QPlaceCategory)
  @overload(QPlaceCategory, str)
  def saveCategory(
      self,
      category: QPlaceCategory,
      parentId: str = '',
  ) -> Optional[QPlaceIdReply]:
    """
    Calls Qt's 'QPlaceIdReply *QPlaceManager::saveCategory(const
    QPlaceCategory &category, const QString &parentId)'.

    Qt's own words: https://doc.qt.io/qt-6/qplacemanager.html#saveCategory

    Parameters
    ----------

    category : QPlaceCategory
      Passed on as a value: Qt reads the C++ QPlaceCategory, which stays
      Python's own.

    parentId : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.

    Returns
    -------

    Optional[QPlaceIdReply]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPlaceIdReply *QPlaceManager::saveCategory(const QPlaceCategory
    #      &category, const QString &parentId)
    address = self.uglySide.call(
        'ritual_ZN13QPlaceManager12saveCategoryERK14QPlaceCategoryRK7QStrin'
        'g',
        self._valueOf(category), parentId,
    )
    from . import QPlaceIdReply
    return QPlaceIdReply._cuteAt(address)

  @overload(str)
  def removeCategory(self, categoryId: str) -> Optional[QPlaceIdReply]:
    """
    Calls Qt's 'QPlaceIdReply *QPlaceManager::removeCategory(const QString
    &categoryId)'.

    Qt's own words: https://doc.qt.io/qt-6/qplacemanager.html#removeCategory

    Parameters
    ----------

    categoryId : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    Optional[QPlaceIdReply]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPlaceIdReply *QPlaceManager::removeCategory(const QString
    #      &categoryId)
    address = self.uglySide.call(
        'ritual_ZN13QPlaceManager14removeCategoryERK7QString', categoryId,
    )
    from . import QPlaceIdReply
    return QPlaceIdReply._cuteAt(address)

  def initializeCategories(self) -> Optional[QPlaceReply]:
    """
    Calls Qt's 'QPlaceReply *QPlaceManager::initializeCategories()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplacemanager.html#initializeCategories

    Returns
    -------

    Optional[QPlaceReply]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPlaceReply *QPlaceManager::initializeCategories()
    address = self.uglySide.call(
        'ritual_ZN13QPlaceManager20initializeCategoriesEv',
    )
    return QPlaceReply._cuteAt(address)

  @overload(QPlaceReply)
  @overload(NoneType)
  def finished(self, reply: Optional[QPlaceReply]) -> None:
    """
    Calls Qt's 'void QPlaceManager::finished(QPlaceReply *reply)'.

    Qt's own words: https://doc.qt.io/qt-6/qplacemanager.html#finished

    Parameters
    ----------

    reply : Optional[QPlaceReply]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QPlaceManager::finished(QPlaceReply *reply)
    self.uglySide.call(
        'ritual_ZN13QPlaceManager8finishedEP11QPlaceReply',
        self._addressOf(reply),
    )

  @overload(QPlaceReply, QPlaceReply.Error)
  @overload(NoneType, QPlaceReply.Error)
  @overload(QPlaceReply, QPlaceReply.Error, str)
  @overload(NoneType, QPlaceReply.Error, str)
  def errorOccurred(
      self,
      a0: Optional[QPlaceReply],
      error: QPlaceReply.Error,
      errorString: str = '',
  ) -> None:
    """
    Calls Qt's 'void QPlaceManager::errorOccurred(QPlaceReply *a0,
    QPlaceReply::Error error, const QString &errorString)'.

    Qt's own words: https://doc.qt.io/qt-6/qplacemanager.html#errorOccurred

    Parameters
    ----------

    a0 : Optional[QPlaceReply]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    error : QPlaceReply.Error
      Passed on as its number.

    errorString : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.
    """
    #  void QPlaceManager::errorOccurred(QPlaceReply *a0, QPlaceReply::Error
    #      error, const QString &errorString)
    self.uglySide.call(
        'ritual_ZN13QPlaceManager13errorOccurredEP11QPlaceReplyNS0_5ErrorER'
        'K7QString',
        self._addressOf(a0), error.value, errorString,
    )

  @overload(str)
  def placeAdded(self, placeId: str) -> None:
    """
    Calls Qt's 'void QPlaceManager::placeAdded(const QString &placeId)'.

    Qt's own words: https://doc.qt.io/qt-6/qplacemanager.html#placeAdded

    Parameters
    ----------

    placeId : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QPlaceManager::placeAdded(const QString &placeId)
    self.uglySide.call(
        'ritual_ZN13QPlaceManager10placeAddedERK7QString', placeId,
    )

  @overload(str)
  def placeUpdated(self, placeId: str) -> None:
    """
    Calls Qt's 'void QPlaceManager::placeUpdated(const QString &placeId)'.

    Qt's own words: https://doc.qt.io/qt-6/qplacemanager.html#placeUpdated

    Parameters
    ----------

    placeId : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QPlaceManager::placeUpdated(const QString &placeId)
    self.uglySide.call(
        'ritual_ZN13QPlaceManager12placeUpdatedERK7QString', placeId,
    )

  @overload(str)
  def placeRemoved(self, placeId: str) -> None:
    """
    Calls Qt's 'void QPlaceManager::placeRemoved(const QString &placeId)'.

    Qt's own words: https://doc.qt.io/qt-6/qplacemanager.html#placeRemoved

    Parameters
    ----------

    placeId : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QPlaceManager::placeRemoved(const QString &placeId)
    self.uglySide.call(
        'ritual_ZN13QPlaceManager12placeRemovedERK7QString', placeId,
    )

  @overload(QPlaceCategory, str)
  def categoryAdded(self, category: QPlaceCategory, parentId: str) -> None:
    """
    Calls Qt's 'void QPlaceManager::categoryAdded(const QPlaceCategory
    &category, const QString &parentId)'.

    Qt's own words: https://doc.qt.io/qt-6/qplacemanager.html#categoryAdded

    Parameters
    ----------

    category : QPlaceCategory
      Passed on as a value: Qt reads the C++ QPlaceCategory, which stays
      Python's own.

    parentId : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QPlaceManager::categoryAdded(const QPlaceCategory &category,
    #      const QString &parentId)
    self.uglySide.call(
        'ritual_ZN13QPlaceManager13categoryAddedERK14QPlaceCategoryRK7QStri'
        'ng',
        self._valueOf(category), parentId,
    )

  @overload(QPlaceCategory, str)
  def categoryUpdated(self, category: QPlaceCategory, parentId: str) -> None:
    """
    Calls Qt's 'void QPlaceManager::categoryUpdated(const QPlaceCategory
    &category, const QString &parentId)'.

    Qt's own words: https://doc.qt.io/qt-6/qplacemanager.html#categoryUpdated

    Parameters
    ----------

    category : QPlaceCategory
      Passed on as a value: Qt reads the C++ QPlaceCategory, which stays
      Python's own.

    parentId : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QPlaceManager::categoryUpdated(const QPlaceCategory &category,
    #      const QString &parentId)
    self.uglySide.call(
        'ritual_ZN13QPlaceManager15categoryUpdatedERK14QPlaceCategoryRK7QSt'
        'ring',
        self._valueOf(category), parentId,
    )

  @overload(str, str)
  def categoryRemoved(self, categoryId: str, parentId: str) -> None:
    """
    Calls Qt's 'void QPlaceManager::categoryRemoved(const QString
    &categoryId, const QString &parentId)'.

    Qt's own words: https://doc.qt.io/qt-6/qplacemanager.html#categoryRemoved

    Parameters
    ----------

    categoryId : str
      Passed on as it is: a QString is made of it for the call.

    parentId : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QPlaceManager::categoryRemoved(const QString &categoryId, const
    #      QString &parentId)
    self.uglySide.call(
        'ritual_ZN13QPlaceManager15categoryRemovedERK7QStringS2_',
        categoryId, parentId,
    )

  def dataChanged(self) -> None:
    """
    Calls Qt's 'void QPlaceManager::dataChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qplacemanager.html#dataChanged
    """
    #  void QPlaceManager::dataChanged()
    self.uglySide.call('ritual_ZN13QPlaceManager11dataChangedEv')
