"""
QPlaceManagerEngine binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtLocation/qplacemanagerengine.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QList, QMap, QObject, QStringList
from . import QPlaceReply

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QLocale, QMetaObject, QSize, QUrl, QVariant
  from . import QPlace, QPlaceCategory, QPlaceContentReply
  from . import QPlaceContentRequest, QPlaceDetailsReply, QPlaceIcon
  from . import QPlaceIdReply, QPlaceManager, QPlaceMatchReply
  from . import QPlaceMatchRequest, QPlaceSearchReply, QPlaceSearchRequest
  from . import QPlaceSearchSuggestionReply
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QLocale = WAIT['QLocale']
  QPlace = WAIT['QPlace']
  QPlaceCategory = WAIT['QPlaceCategory']
  QPlaceContentRequest = WAIT['QPlaceContentRequest']
  QPlaceIcon = WAIT['QPlaceIcon']
  QPlaceMatchRequest = WAIT['QPlaceMatchRequest']
  QPlaceSearchRequest = WAIT['QPlaceSearchRequest']
  QSize = WAIT['QSize']
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QPlaceManagerEngine(QObject):
  """
  The cute side of Qt's QPlaceManagerEngine: a plain Python object standing
  in front of one C++ QPlaceManagerEngine.

  It is built on the cute 'QObject', as Qt's QPlaceManagerEngine is built on
  Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QPlaceManagerEngine that has a ritual and that
  Python can call so far, 34 names in all: 'metaObject', 'tr', 'managerName',
  'managerVersion', 'getPlaceDetails', 'getPlaceContent', 'search',
  'searchSuggestions', 'savePlace', 'removePlace', 'saveCategory',
  'removeCategory', 'initializeCategories', 'parentCategoryId',
  'childCategoryIds', 'category', 'childCategories', 'locales', 'setLocales',
  'constructIconUrl', 'compatiblePlace', 'matchingPlaces', 'finished',
  'errorOccurred', 'placeAdded', 'placeUpdated', 'placeRemoved',
  'categoryAdded', 'categoryUpdated', 'categoryRemoved', 'dataChanged',
  'manager', 'setManagerName', 'setManagerVersion'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QPlaceManagerEngine::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QPlaceManagerEngine::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QPlaceManagerEngine::~QPlaceManagerEngine()': the destructor:
    Python never removes a C++ QPlaceManagerEngine.

  What has no ritual
  ------------------

  4 of the 42 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QPlaceManagerEngine is created at the first use, not by
    'QPlaceManagerEngine(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QPlaceManagerEngine.
  - Qt tells when it has removed the C++ QPlaceManagerEngine. Every call on
    the cute object, and every use of it as an argument, then raises
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
    Calls Qt's 'QString QPlaceManagerEngine::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qplacemanagerengine.html#tr

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
    #  QString QPlaceManagerEngine::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN19QPlaceManagerEngine2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QPlaceManagerEngine'

  #  A C++ QPlaceManagerEngine Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QPlaceManagerEngine'

  #  The functions Qt calls itself that QPlaceManagerEngine is the first to
  #  declare and that cannot be handed to Python yet, each as Qt declares it.
  #  A class of a program that writes one of them anew is refused, since Qt
  #  would never call what it wrote; see 'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'childCategoryIds': (
          'QStringList QPlaceManagerEngine::childCategoryIds(const QString '
          '&) const',
      ),
      'childCategories': (
          'QList<QPlaceCategory> '
          'QPlaceManagerEngine::childCategories(const QString &) const',
      ),
      'locales': (
          'QList<QLocale> QPlaceManagerEngine::locales() const',
      ),
      'setLocales': (
          'void QPlaceManagerEngine::setLocales(const QList<QLocale> &)',
      ),
  }

  #  The functions Qt calls itself that QPlaceManagerEngine is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'getPlaceDetails': (
          ('_ZN19QPlaceManagerEngine15getPlaceDetailsERK7QString',
           ('address', 'address', 'QtLocation:QPlaceDetailsReply'),
           (
               ('address', 'text', ''),
           )),
      ),
      'getPlaceContent': (
          ('_ZN19QPlaceManagerEngine15getPlaceContentERK20QPlaceContentRequ'
           'est',
           ('address', 'address', 'QtLocation:QPlaceContentReply'),
           (
               ('address', 'value', 'QtLocation:QPlaceContentRequest'),
           )),
      ),
      'search': (
          ('_ZN19QPlaceManagerEngine6searchERK19QPlaceSearchRequest',
           ('address', 'address', 'QtLocation:QPlaceSearchReply'),
           (
               ('address', 'value', 'QtLocation:QPlaceSearchRequest'),
           )),
      ),
      'searchSuggestions': (
          ('_ZN19QPlaceManagerEngine17searchSuggestionsERK19QPlaceSearchReq'
           'uest',
           ('address', 'address', 'QtLocation:QPlaceSearchSuggestionReply'),
           (
               ('address', 'value', 'QtLocation:QPlaceSearchRequest'),
           )),
      ),
      'savePlace': (
          ('_ZN19QPlaceManagerEngine9savePlaceERK6QPlace',
           ('address', 'address', 'QtLocation:QPlaceIdReply'),
           (
               ('address', 'value', 'QtLocation:QPlace'),
           )),
      ),
      'removePlace': (
          ('_ZN19QPlaceManagerEngine11removePlaceERK7QString',
           ('address', 'address', 'QtLocation:QPlaceIdReply'),
           (
               ('address', 'text', ''),
           )),
      ),
      'saveCategory': (
          ('_ZN19QPlaceManagerEngine12saveCategoryERK14QPlaceCategoryRK7QSt'
           'ring',
           ('address', 'address', 'QtLocation:QPlaceIdReply'),
           (
               ('address', 'value', 'QtLocation:QPlaceCategory'),
               ('address', 'text', ''),
           )),
      ),
      'removeCategory': (
          ('_ZN19QPlaceManagerEngine14removeCategoryERK7QString',
           ('address', 'address', 'QtLocation:QPlaceIdReply'),
           (
               ('address', 'text', ''),
           )),
      ),
      'initializeCategories': (
          ('_ZN19QPlaceManagerEngine20initializeCategoriesEv',
           ('address', 'address', 'QtLocation:QPlaceReply'),
           ()),
      ),
      'parentCategoryId': (
          ('_ZNK19QPlaceManagerEngine16parentCategoryIdERK7QString',
           ('address', 'text', ''),
           (
               ('address', 'text', ''),
           )),
      ),
      'category': (
          ('_ZNK19QPlaceManagerEngine8categoryERK7QString',
           ('address', 'value', 'QtLocation:QPlaceCategory'),
           (
               ('address', 'text', ''),
           )),
      ),
      'constructIconUrl': (
          ('_ZNK19QPlaceManagerEngine16constructIconUrlERK10QPlaceIconRK5QS'
           'ize',
           ('address', 'value', 'QtCore:QUrl'),
           (
               ('address', 'value', 'QtLocation:QPlaceIcon'),
               ('address', 'value', 'QtCore:QSize'),
           )),
      ),
      'compatiblePlace': (
          ('_ZNK19QPlaceManagerEngine15compatiblePlaceERK6QPlace',
           ('address', 'value', 'QtLocation:QPlace'),
           (
               ('address', 'value', 'QtLocation:QPlace'),
           )),
      ),
      'matchingPlaces': (
          ('_ZN19QPlaceManagerEngine14matchingPlacesERK18QPlaceMatchRequest',
           ('address', 'address', 'QtLocation:QPlaceMatchReply'),
           (
               ('address', 'value', 'QtLocation:QPlaceMatchRequest'),
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
    Calls Qt's 'const QMetaObject *QPlaceManagerEngine::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplacemanagerengine.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QPlaceManagerEngine::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK19QPlaceManagerEngine10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def managerName(self) -> str:
    """
    Calls Qt's 'QString QPlaceManagerEngine::managerName() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplacemanagerengine.html#managerName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QPlaceManagerEngine::managerName() const
    return self.uglySide.call(
        'ritual_ZNK19QPlaceManagerEngine11managerNameEv',
    )

  def managerVersion(self) -> int:
    """
    Calls Qt's 'int QPlaceManagerEngine::managerVersion() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplacemanagerengine.html#managerVersion
    """
    #  int QPlaceManagerEngine::managerVersion() const
    return self.uglySide.call(
        'ritual_ZNK19QPlaceManagerEngine14managerVersionEv',
    )

  @overload(str)
  def parentCategoryId(self, categoryId: str) -> str:
    """
    Calls Qt's 'QString QPlaceManagerEngine::parentCategoryId(const QString
    &categoryId) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplacemanagerengine.html#parentCategoryId

    Parameters
    ----------

    categoryId : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QPlaceManagerEngine::parentCategoryId(const QString
    #      &categoryId) const
    ritual = 'ritual_ZNK19QPlaceManagerEngine16parentCategoryIdERK7QString'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK19QPlaceManagerEngine16parentCategoryIdERK7QString')
    return self.uglySide.call(ritual, categoryId)

  @overload(str)
  def childCategoryIds(self, categoryId: str) -> QStringList:
    """
    Calls Qt's 'QStringList QPlaceManagerEngine::childCategoryIds(const
    QString &categoryId) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplacemanagerengine.html#childCategoryIds

    Parameters
    ----------

    categoryId : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QPlaceManagerEngine::childCategoryIds(const QString
    #      &categoryId) const
    address = self.uglySide.call(
        'ritual_ZNK19QPlaceManagerEngine16childCategoryIdsERK7QString',
        categoryId,
    )
    return QStringList._cuteOwning(address)

  @overload(str)
  def category(self, categoryId: str) -> QPlaceCategory:
    """
    Calls Qt's 'QPlaceCategory QPlaceManagerEngine::category(const QString
    &categoryId) const'.

    Qt's own words: https://doc.qt.io/qt-6/qplacemanagerengine.html#category

    Parameters
    ----------

    categoryId : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QPlaceCategory
      A new cute QPlaceCategory around the copy Qt gave back. Python owns it.
    """
    #  QPlaceCategory QPlaceManagerEngine::category(const QString
    #      &categoryId) const
    ritual = 'ritual_ZNK19QPlaceManagerEngine8categoryERK7QString'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK19QPlaceManagerEngine8categoryERK7QString'
    address = self.uglySide.call(ritual, categoryId)
    from . import QPlaceCategory
    return QPlaceCategory._cuteOwning(address)

  @overload(str)
  def childCategories(self, parentId: str) -> QList[QPlaceCategory]:
    """
    Calls Qt's 'QList<QPlaceCategory>
    QPlaceManagerEngine::childCategories(const QString &parentId) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplacemanagerengine.html#childCategories

    Parameters
    ----------

    parentId : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QList[QPlaceCategory]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QPlaceCategory> QPlaceManagerEngine::childCategories(const
    #      QString &parentId) const
    address = self.uglySide.call(
        'ritual_ZNK19QPlaceManagerEngine15childCategoriesERK7QString',
        parentId,
    )
    from . import QPlaceCategory
    return QList[QPlaceCategory]._cuteOwning(address)

  def locales(self) -> QList[QLocale]:
    """
    Calls Qt's 'QList<QLocale> QPlaceManagerEngine::locales() const'.

    Qt's own words: https://doc.qt.io/qt-6/qplacemanagerengine.html#locales

    Returns
    -------

    QList[QLocale]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QLocale> QPlaceManagerEngine::locales() const
    address = self.uglySide.call('ritual_ZNK19QPlaceManagerEngine7localesEv')
    from ..QtCore import QLocale
    return QList[QLocale]._cuteOwning(address)

  @overload(QPlaceIcon, QSize)
  def constructIconUrl(self, icon: QPlaceIcon, size: QSize) -> QUrl:
    """
    Calls Qt's 'QUrl QPlaceManagerEngine::constructIconUrl(const QPlaceIcon
    &icon, const QSize &size) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplacemanagerengine.html#constructIconUrl

    Parameters
    ----------

    icon : QPlaceIcon
      Passed on as a value: Qt reads the C++ QPlaceIcon, which stays Python's
      own.

    size : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QPlaceManagerEngine::constructIconUrl(const QPlaceIcon &icon,
    #      const QSize &size) const
    ritual = (
        'ritual_ZNK19QPlaceManagerEngine16constructIconUrlERK10QPlaceIconRK'
        '5QSize')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK19QPlaceManagerEngine16constructIconUrlERK10QPlace'
          'IconRK5QSize')
    address = self.uglySide.call(
        ritual, self._valueOf(icon), self._valueOf(size),
    )
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  @overload(QPlace)
  def compatiblePlace(self, original: QPlace) -> QPlace:
    """
    Calls Qt's 'QPlace QPlaceManagerEngine::compatiblePlace(const QPlace
    &original) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplacemanagerengine.html#compatiblePlace

    Parameters
    ----------

    original : QPlace
      Passed on as a value: Qt reads the C++ QPlace, which stays Python's
      own.

    Returns
    -------

    QPlace
      A new cute QPlace around the copy Qt gave back. Python owns it.
    """
    #  QPlace QPlaceManagerEngine::compatiblePlace(const QPlace &original)
    #      const
    ritual = 'ritual_ZNK19QPlaceManagerEngine15compatiblePlaceERK6QPlace'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK19QPlaceManagerEngine15compatiblePlaceERK6QPlace')
    address = self.uglySide.call(ritual, self._valueOf(original))
    from . import QPlace
    return QPlace._cuteOwning(address)

  def manager(self) -> Optional[QPlaceManager]:
    """
    Calls Qt's 'QPlaceManager *QPlaceManagerEngine::manager() const'.

    Qt's own words: https://doc.qt.io/qt-6/qplacemanagerengine.html#manager

    Returns
    -------

    Optional[QPlaceManager]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPlaceManager *QPlaceManagerEngine::manager() const
    address = self.uglySide.call('ritual_ZNK19QPlaceManagerEngine7managerEv')
    from . import QPlaceManager
    return QPlaceManager._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QList[QLocale])
  def setLocales(self, locales: QList[QLocale]) -> None:
    """
    Calls Qt's 'void QPlaceManagerEngine::setLocales(const QList<QLocale>
    &locales)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplacemanagerengine.html#setLocales

    Parameters
    ----------

    locales : QList[QLocale]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QPlaceManagerEngine::setLocales(const QList<QLocale> &locales)
    self.uglySide.call(
        'ritual_ZN19QPlaceManagerEngine10setLocalesERK5QListI7QLocaleE',
        self._valueOf(locales),
    )

  @overload(str)
  def setManagerName(self, managerName: str) -> None:
    """
    Calls Qt's 'void QPlaceManagerEngine::setManagerName(const QString
    &managerName)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplacemanagerengine.html#setManagerName

    Parameters
    ----------

    managerName : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QPlaceManagerEngine::setManagerName(const QString &managerName)
    self.uglySide.call(
        'ritual_ZN19QPlaceManagerEngine14setManagerNameERK7QString',
        managerName,
    )

  @overload(int)
  def setManagerVersion(self, managerVersion: int) -> None:
    """
    Calls Qt's 'void QPlaceManagerEngine::setManagerVersion(int
    managerVersion)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplacemanagerengine.html#setManagerVersion

    Parameters
    ----------

    managerVersion : int
      Passed on as it is.
    """
    #  void QPlaceManagerEngine::setManagerVersion(int managerVersion)
    self.uglySide.call(
        'ritual_ZN19QPlaceManagerEngine17setManagerVersionEi',
        managerVersion,
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

  @overload(QMap[str, QVariant])
  @overload(QMap[str, QVariant], QObject)
  @overload(QMap[str, QVariant], NoneType)
  def __init__(
      self,
      parameters: QMap[str, QVariant],
      parent: Optional[QObject] = None,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QPlaceManagerEngine::QPlaceManagerEngine(const QVariantMap &parameters,
    QObject *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qplacemanagerengine.html#QPlaceManagerEngine

    Parameters
    ----------

    parameters : QMap[str, QVariant]
      Passed on as a map of Qt: Qt reads the C++ map, which stays Python's
      own. A dict of Python is made into one first, and refused when a key or
      a value does not fit.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QPlaceManagerEngine::QPlaceManagerEngine(const QVariantMap
    #      &parameters, QObject *parent)
    self._noteCreation(QPlaceManagerEngine, lambda: Rituals.call(
        'ritual_ZN19QPlaceManagerEngineC1ERK4QMapI7QString8QVariantEP7QObje'
        'ct',
        self._valueOf(parameters), self._addressOf(parent, 'QObject'),
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

  @overload(str)
  def getPlaceDetails(self, placeId: str) -> Optional[QPlaceDetailsReply]:
    """
    Calls Qt's 'QPlaceDetailsReply
    *QPlaceManagerEngine::getPlaceDetails(const QString &placeId)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplacemanagerengine.html#getPlaceDetails

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
    #  QPlaceDetailsReply *QPlaceManagerEngine::getPlaceDetails(const QString
    #      &placeId)
    ritual = 'ritual_ZN19QPlaceManagerEngine15getPlaceDetailsERK7QString'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QPlaceManagerEngine15getPlaceDetailsERK7QString')
    address = self.uglySide.call(ritual, placeId)
    from . import QPlaceDetailsReply
    return QPlaceDetailsReply._cuteAt(address)

  @overload(QPlaceContentRequest)
  def getPlaceContent(
      self,
      request: QPlaceContentRequest,
  ) -> Optional[QPlaceContentReply]:
    """
    Calls Qt's 'QPlaceContentReply
    *QPlaceManagerEngine::getPlaceContent(const QPlaceContentRequest
    &request)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplacemanagerengine.html#getPlaceContent

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
    #  QPlaceContentReply *QPlaceManagerEngine::getPlaceContent(const
    #      QPlaceContentRequest &request)
    ritual = (
        'ritual_ZN19QPlaceManagerEngine15getPlaceContentERK20QPlaceContentR'
        'equest')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QPlaceManagerEngine15getPlaceContentERK20QPlaceCo'
          'ntentRequest')
    address = self.uglySide.call(ritual, self._valueOf(request))
    from . import QPlaceContentReply
    return QPlaceContentReply._cuteAt(address)

  @overload(QPlaceSearchRequest)
  def search(
      self,
      request: QPlaceSearchRequest,
  ) -> Optional[QPlaceSearchReply]:
    """
    Calls Qt's 'QPlaceSearchReply *QPlaceManagerEngine::search(const
    QPlaceSearchRequest &request)'.

    Qt's own words: https://doc.qt.io/qt-6/qplacemanagerengine.html#search

    Parameters
    ----------

    request : QPlaceSearchRequest
      Passed on as a value: Qt reads the C++ QPlaceSearchRequest, which stays
      Python's own.

    Returns
    -------

    Optional[QPlaceSearchReply]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPlaceSearchReply *QPlaceManagerEngine::search(const
    #      QPlaceSearchRequest &request)
    ritual = 'ritual_ZN19QPlaceManagerEngine6searchERK19QPlaceSearchRequest'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QPlaceManagerEngine6searchERK19QPlaceSearchReques'
          't')
    address = self.uglySide.call(ritual, self._valueOf(request))
    from . import QPlaceSearchReply
    return QPlaceSearchReply._cuteAt(address)

  @overload(QPlaceSearchRequest)
  def searchSuggestions(
      self,
      request: QPlaceSearchRequest,
  ) -> Optional[QPlaceSearchSuggestionReply]:
    """
    Calls Qt's 'QPlaceSearchSuggestionReply
    *QPlaceManagerEngine::searchSuggestions(const QPlaceSearchRequest
    &request)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplacemanagerengine.html#searchSuggestions

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
    #  QPlaceSearchSuggestionReply
    #      *QPlaceManagerEngine::searchSuggestions(const QPlaceSearchRequest
    #      &request)
    ritual = (
        'ritual_ZN19QPlaceManagerEngine17searchSuggestionsERK19QPlaceSearch'
        'Request')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QPlaceManagerEngine17searchSuggestionsERK19QPlace'
          'SearchRequest')
    address = self.uglySide.call(ritual, self._valueOf(request))
    from . import QPlaceSearchSuggestionReply
    return QPlaceSearchSuggestionReply._cuteAt(address)

  @overload(QPlace)
  def savePlace(self, place: QPlace) -> Optional[QPlaceIdReply]:
    """
    Calls Qt's 'QPlaceIdReply *QPlaceManagerEngine::savePlace(const QPlace
    &place)'.

    Qt's own words: https://doc.qt.io/qt-6/qplacemanagerengine.html#savePlace

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
    #  QPlaceIdReply *QPlaceManagerEngine::savePlace(const QPlace &place)
    ritual = 'ritual_ZN19QPlaceManagerEngine9savePlaceERK6QPlace'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QPlaceManagerEngine9savePlaceERK6QPlace'
    address = self.uglySide.call(ritual, self._valueOf(place))
    from . import QPlaceIdReply
    return QPlaceIdReply._cuteAt(address)

  @overload(str)
  def removePlace(self, placeId: str) -> Optional[QPlaceIdReply]:
    """
    Calls Qt's 'QPlaceIdReply *QPlaceManagerEngine::removePlace(const QString
    &placeId)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplacemanagerengine.html#removePlace

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
    #  QPlaceIdReply *QPlaceManagerEngine::removePlace(const QString
    #      &placeId)
    ritual = 'ritual_ZN19QPlaceManagerEngine11removePlaceERK7QString'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QPlaceManagerEngine11removePlaceERK7QString'
    address = self.uglySide.call(ritual, placeId)
    from . import QPlaceIdReply
    return QPlaceIdReply._cuteAt(address)

  @overload(QPlaceCategory, str)
  def saveCategory(
      self,
      category: QPlaceCategory,
      parentId: str,
  ) -> Optional[QPlaceIdReply]:
    """
    Calls Qt's 'QPlaceIdReply *QPlaceManagerEngine::saveCategory(const
    QPlaceCategory &category, const QString &parentId)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplacemanagerengine.html#saveCategory

    Parameters
    ----------

    category : QPlaceCategory
      Passed on as a value: Qt reads the C++ QPlaceCategory, which stays
      Python's own.

    parentId : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    Optional[QPlaceIdReply]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPlaceIdReply *QPlaceManagerEngine::saveCategory(const QPlaceCategory
    #      &category, const QString &parentId)
    ritual = (
        'ritual_ZN19QPlaceManagerEngine12saveCategoryERK14QPlaceCategoryRK7'
        'QString')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QPlaceManagerEngine12saveCategoryERK14QPlaceCateg'
          'oryRK7QString')
    address = self.uglySide.call(ritual, self._valueOf(category), parentId)
    from . import QPlaceIdReply
    return QPlaceIdReply._cuteAt(address)

  @overload(str)
  def removeCategory(self, categoryId: str) -> Optional[QPlaceIdReply]:
    """
    Calls Qt's 'QPlaceIdReply *QPlaceManagerEngine::removeCategory(const
    QString &categoryId)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplacemanagerengine.html#removeCategory

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
    #  QPlaceIdReply *QPlaceManagerEngine::removeCategory(const QString
    #      &categoryId)
    ritual = 'ritual_ZN19QPlaceManagerEngine14removeCategoryERK7QString'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QPlaceManagerEngine14removeCategoryERK7QString')
    address = self.uglySide.call(ritual, categoryId)
    from . import QPlaceIdReply
    return QPlaceIdReply._cuteAt(address)

  def initializeCategories(self) -> Optional[QPlaceReply]:
    """
    Calls Qt's 'QPlaceReply *QPlaceManagerEngine::initializeCategories()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplacemanagerengine.html#initializeCategories

    Returns
    -------

    Optional[QPlaceReply]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPlaceReply *QPlaceManagerEngine::initializeCategories()
    ritual = 'ritual_ZN19QPlaceManagerEngine20initializeCategoriesEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QPlaceManagerEngine20initializeCategoriesEv'
    address = self.uglySide.call(ritual)
    return QPlaceReply._cuteAt(address)

  @overload(QPlaceMatchRequest)
  def matchingPlaces(
      self,
      request: QPlaceMatchRequest,
  ) -> Optional[QPlaceMatchReply]:
    """
    Calls Qt's 'QPlaceMatchReply *QPlaceManagerEngine::matchingPlaces(const
    QPlaceMatchRequest &request)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplacemanagerengine.html#matchingPlaces

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
    #  QPlaceMatchReply *QPlaceManagerEngine::matchingPlaces(const
    #      QPlaceMatchRequest &request)
    ritual = (
        'ritual_ZN19QPlaceManagerEngine14matchingPlacesERK18QPlaceMatchRequ'
        'est')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QPlaceManagerEngine14matchingPlacesERK18QPlaceMat'
          'chRequest')
    address = self.uglySide.call(ritual, self._valueOf(request))
    from . import QPlaceMatchReply
    return QPlaceMatchReply._cuteAt(address)

  @overload(QPlaceReply)
  @overload(NoneType)
  def finished(self, reply: Optional[QPlaceReply]) -> None:
    """
    Calls Qt's 'void QPlaceManagerEngine::finished(QPlaceReply *reply)'.

    Qt's own words: https://doc.qt.io/qt-6/qplacemanagerengine.html#finished

    Parameters
    ----------

    reply : Optional[QPlaceReply]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QPlaceManagerEngine::finished(QPlaceReply *reply)
    self.uglySide.call(
        'ritual_ZN19QPlaceManagerEngine8finishedEP11QPlaceReply',
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
    Calls Qt's 'void QPlaceManagerEngine::errorOccurred(QPlaceReply *a0,
    QPlaceReply::Error error, const QString &errorString)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplacemanagerengine.html#errorOccurred

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
    #  void QPlaceManagerEngine::errorOccurred(QPlaceReply *a0,
    #      QPlaceReply::Error error, const QString &errorString)
    self.uglySide.call(
        'ritual_ZN19QPlaceManagerEngine13errorOccurredEP11QPlaceReplyNS0_5E'
        'rrorERK7QString',
        self._addressOf(a0), error.value, errorString,
    )

  @overload(str)
  def placeAdded(self, placeId: str) -> None:
    """
    Calls Qt's 'void QPlaceManagerEngine::placeAdded(const QString
    &placeId)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplacemanagerengine.html#placeAdded

    Parameters
    ----------

    placeId : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QPlaceManagerEngine::placeAdded(const QString &placeId)
    self.uglySide.call(
        'ritual_ZN19QPlaceManagerEngine10placeAddedERK7QString', placeId,
    )

  @overload(str)
  def placeUpdated(self, placeId: str) -> None:
    """
    Calls Qt's 'void QPlaceManagerEngine::placeUpdated(const QString
    &placeId)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplacemanagerengine.html#placeUpdated

    Parameters
    ----------

    placeId : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QPlaceManagerEngine::placeUpdated(const QString &placeId)
    self.uglySide.call(
        'ritual_ZN19QPlaceManagerEngine12placeUpdatedERK7QString', placeId,
    )

  @overload(str)
  def placeRemoved(self, placeId: str) -> None:
    """
    Calls Qt's 'void QPlaceManagerEngine::placeRemoved(const QString
    &placeId)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplacemanagerengine.html#placeRemoved

    Parameters
    ----------

    placeId : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QPlaceManagerEngine::placeRemoved(const QString &placeId)
    self.uglySide.call(
        'ritual_ZN19QPlaceManagerEngine12placeRemovedERK7QString', placeId,
    )

  @overload(QPlaceCategory, str)
  def categoryAdded(
      self,
      category: QPlaceCategory,
      parentCategoryId: str,
  ) -> None:
    """
    Calls Qt's 'void QPlaceManagerEngine::categoryAdded(const QPlaceCategory
    &category, const QString &parentCategoryId)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplacemanagerengine.html#categoryAdded

    Parameters
    ----------

    category : QPlaceCategory
      Passed on as a value: Qt reads the C++ QPlaceCategory, which stays
      Python's own.

    parentCategoryId : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QPlaceManagerEngine::categoryAdded(const QPlaceCategory
    #      &category, const QString &parentCategoryId)
    self.uglySide.call(
        'ritual_ZN19QPlaceManagerEngine13categoryAddedERK14QPlaceCategoryRK'
        '7QString',
        self._valueOf(category), parentCategoryId,
    )

  @overload(QPlaceCategory, str)
  def categoryUpdated(
      self,
      category: QPlaceCategory,
      parentCategoryId: str,
  ) -> None:
    """
    Calls Qt's 'void QPlaceManagerEngine::categoryUpdated(const
    QPlaceCategory &category, const QString &parentCategoryId)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplacemanagerengine.html#categoryUpdated

    Parameters
    ----------

    category : QPlaceCategory
      Passed on as a value: Qt reads the C++ QPlaceCategory, which stays
      Python's own.

    parentCategoryId : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QPlaceManagerEngine::categoryUpdated(const QPlaceCategory
    #      &category, const QString &parentCategoryId)
    self.uglySide.call(
        'ritual_ZN19QPlaceManagerEngine15categoryUpdatedERK14QPlaceCategory'
        'RK7QString',
        self._valueOf(category), parentCategoryId,
    )

  @overload(str, str)
  def categoryRemoved(self, categoryId: str, parentCategoryId: str) -> None:
    """
    Calls Qt's 'void QPlaceManagerEngine::categoryRemoved(const QString
    &categoryId, const QString &parentCategoryId)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplacemanagerengine.html#categoryRemoved

    Parameters
    ----------

    categoryId : str
      Passed on as it is: a QString is made of it for the call.

    parentCategoryId : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QPlaceManagerEngine::categoryRemoved(const QString &categoryId,
    #      const QString &parentCategoryId)
    self.uglySide.call(
        'ritual_ZN19QPlaceManagerEngine15categoryRemovedERK7QStringS2_',
        categoryId, parentCategoryId,
    )

  def dataChanged(self) -> None:
    """
    Calls Qt's 'void QPlaceManagerEngine::dataChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplacemanagerengine.html#dataChanged
    """
    #  void QPlaceManagerEngine::dataChanged()
    self.uglySide.call('ritual_ZN19QPlaceManagerEngine11dataChangedEv')
