"""
QDeclarativePlace binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtLocation/6.12.0/QtLocation/private/qdeclarativeplace_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QDeclarativePlace to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import QObject
from ..QtQml import QQmlParserStatus

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QUrl, QVariant
  from ..QtQml import QQmlPropertyMap
  from ..QtPositioningQuick import QDeclarativeGeoLocation
  from . import QDeclarativeContactDetails, QDeclarativeGeoServiceProvider
  from . import QDeclarativePlaceEditorialModel, QDeclarativePlaceImageModel
  from . import QDeclarativePlaceReviewModel, QPlace, QPlaceIcon
  from . import QPlaceManager, QPlaceRatings, QPlaceSupplier
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDeclarativeGeoLocation = WAIT['QDeclarativeGeoLocation']
  QDeclarativeGeoServiceProvider = WAIT['QDeclarativeGeoServiceProvider']
  QPlace = WAIT['QPlace']
  QPlaceIcon = WAIT['QPlaceIcon']
  QPlaceRatings = WAIT['QPlaceRatings']
  QPlaceSupplier = WAIT['QPlaceSupplier']
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QDeclarativePlace(QObject, QQmlParserStatus):
  """
  The cute side of Qt's QDeclarativePlace: a plain Python object standing in
  front of one C++ QDeclarativePlace.

  It is built on the cute 'QObject', as Qt's QDeclarativePlace is built on
  Qt's QObject, and has everything that class has. It is built on the cute
  'QQmlParserStatus' as well, as Qt's QDeclarativePlace is built on Qt's
  QQmlParserStatus too, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QDeclarativePlace that has a ritual and that Python
  can call so far, 76 names in all: 'metaObject', 'tr', 'classBegin',
  'componentComplete', 'setPlugin', 'plugin', 'reviewModel', 'imageModel',
  'editorialModel', 'place', 'setPlace', 'location', 'setLocation',
  'ratings', 'setRatings', 'supplier', 'setSupplier', 'icon', 'setIcon',
  'name', 'setName', 'placeId', 'setPlaceId', 'attribution',
  'setAttribution', 'detailsFetched', 'status', 'setStatus', 'getDetails',
  'save', 'remove', 'errorString', 'primaryPhone', 'primaryFax',
  'primaryEmail', 'primaryWebsite', 'extendedAttributes', 'contactDetails',
  'visibility', 'setVisibility', 'favorite', 'setFavorite', 'copyFrom',
  'initializeFavorite', 'pluginChanged', 'categoriesChanged',
  'locationChanged', 'ratingsChanged', 'supplierChanged', 'iconChanged',
  'nameChanged', 'placeIdChanged', 'attributionChanged',
  'detailsFetchedChanged', 'reviewModelChanged', 'imageModelChanged',
  'editorialModelChanged', 'primaryPhoneChanged', 'primaryFaxChanged',
  'primaryEmailChanged', 'primaryWebsiteChanged',
  'extendedAttributesChanged', 'contactDetailsChanged', 'statusChanged',
  'visibilityChanged', 'favoriteChanged', 'finished', 'contactsModified',
  'pluginReady', 'cleanupDeletedCategories', 'synchronizeCategories',
  'pullExtendedAttributes', 'synchronizeContacts', 'primarySignalsEmission',
  'primaryValue', 'manager'. It can be made from Python, in 2 ways; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QDeclarativePlace::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QDeclarativePlace::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QDeclarativePlace::~QDeclarativePlace()': the destructor: Python
    never removes a C++ QDeclarativePlace.
  - Qt's 'QQmlListProperty<QDeclarativeCategory>
    QDeclarativePlace::categories()': gives a type Python has no way to take
    yet.
  - Qt's 'void
    QDeclarativePlace::category_append(QQmlListProperty<QDeclarativeCategory>
    *prop, QDeclarativeCategory *value)': names
    'QQmlListProperty<QDeclarativeCategory>', which has no cute class yet.
  - Qt's 'qsizetype
    QDeclarativePlace::category_count(QQmlListProperty<QDeclarativeCategory>
    *prop)': names 'QQmlListProperty<QDeclarativeCategory>', which has no
    cute class yet.
  - Qt's 'QDeclarativeCategory
    *QDeclarativePlace::category_at(QQmlListProperty<QDeclarativeCategory>
    *prop, qsizetype index)': names 'QQmlListProperty<QDeclarativeCategory>',
    which has no cute class yet.
  - Qt's 'void
    QDeclarativePlace::category_clear(QQmlListProperty<QDeclarativeCategory>
    *prop)': names 'QQmlListProperty<QDeclarativeCategory>', which has no
    cute class yet.

  What has no ritual
  ------------------

  2 of the 88 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QDeclarativePlace is created at the first use, not by
    'QDeclarativePlace(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QDeclarativePlace.
  - Qt tells when it has removed the C++ QDeclarativePlace. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QDeclarativePlace that has no cute function yet,
    'categories', 'category_append', 'category_at', 'category_clear',
    'category_count', holds a function that raises 'NotImplementedError', and
    its docstring says why.
  """

  #  The enums Qt writes inside QDeclarativePlace, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class Status(CuteNum):
    """
    The enum 'QDeclarativePlace::Status' of Qt, with the 5 names Qt gives in
    it.
    """

    Ready = Kee[int](0)
    Saving = Kee[int](1)
    Fetching = Kee[int](2)
    Removing = Kee[int](3)
    Error = Kee[int](4)

  class Visibility(CuteNum):
    """
    The enum 'QDeclarativePlace::Visibility' of Qt, with the 4 names Qt gives
    in it.
    """

    UnspecifiedVisibility = Kee[int](0)
    DeviceVisibility = Kee[int](1)
    PrivateVisibility = Kee[int](2)
    PublicVisibility = Kee[int](4)

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
    Calls Qt's 'QString QDeclarativePlace::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qdeclarativeplace.html#tr

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
    #  QString QDeclarativePlace::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN17QDeclarativePlace2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QDeclarativePlace'

  #  Qt's QDeclarativePlace is built on more than one class. The part of a
  #  C++ QDeclarativePlace that belongs to a class after the first begins
  #  somewhere inside the object, and the ritual named for that class gives
  #  where; see 'CuteMixin._addressAs'.
  __cast_rituals__ = {
      'QQmlParserStatus': 'ritual_cast_QDeclarativePlace_QQmlParserStatus',
  }

  #  A C++ QDeclarativePlace Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QDeclarativePlace'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QDeclarativePlace::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdeclarativeplace.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QDeclarativePlace::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK17QDeclarativePlace10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def plugin(self) -> Optional[QDeclarativeGeoServiceProvider]:
    """
    Calls Qt's 'QDeclarativeGeoServiceProvider *QDeclarativePlace::plugin()
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qdeclarativeplace.html#plugin

    Returns
    -------

    Optional[QDeclarativeGeoServiceProvider]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QDeclarativeGeoServiceProvider *QDeclarativePlace::plugin() const
    address = self.uglySide.call('ritual_ZNK17QDeclarativePlace6pluginEv')
    from . import QDeclarativeGeoServiceProvider
    return QDeclarativeGeoServiceProvider._cuteAt(address)

  def place(self) -> QPlace:
    """
    Calls Qt's 'QPlace QDeclarativePlace::place() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdeclarativeplace.html#place

    Returns
    -------

    QPlace
      A new cute QPlace around the copy Qt gave back. Python owns it.
    """
    #  QPlace QDeclarativePlace::place() const
    address = self.uglySide.call('ritual_ZNK17QDeclarativePlace5placeEv')
    from . import QPlace
    return QPlace._cuteOwning(address)

  def location(self) -> Optional[QDeclarativeGeoLocation]:
    """
    Calls Qt's 'QDeclarativeGeoLocation *QDeclarativePlace::location()
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qdeclarativeplace.html#location

    Returns
    -------

    Optional[QDeclarativeGeoLocation]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QDeclarativeGeoLocation *QDeclarativePlace::location() const
    address = self.uglySide.call('ritual_ZNK17QDeclarativePlace8locationEv')
    from ..QtPositioningQuick import QDeclarativeGeoLocation
    return QDeclarativeGeoLocation._cuteAt(address)

  def ratings(self) -> QPlaceRatings:
    """
    Calls Qt's 'QPlaceRatings QDeclarativePlace::ratings() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdeclarativeplace.html#ratings

    Returns
    -------

    QPlaceRatings
      A new cute QPlaceRatings around the copy Qt gave back. Python owns it.
    """
    #  QPlaceRatings QDeclarativePlace::ratings() const
    address = self.uglySide.call('ritual_ZNK17QDeclarativePlace7ratingsEv')
    from . import QPlaceRatings
    return QPlaceRatings._cuteOwning(address)

  def supplier(self) -> QPlaceSupplier:
    """
    Calls Qt's 'QPlaceSupplier QDeclarativePlace::supplier() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdeclarativeplace.html#supplier

    Returns
    -------

    QPlaceSupplier
      A new cute QPlaceSupplier around the copy Qt gave back. Python owns it.
    """
    #  QPlaceSupplier QDeclarativePlace::supplier() const
    address = self.uglySide.call('ritual_ZNK17QDeclarativePlace8supplierEv')
    from . import QPlaceSupplier
    return QPlaceSupplier._cuteOwning(address)

  def icon(self) -> QPlaceIcon:
    """
    Calls Qt's 'QPlaceIcon QDeclarativePlace::icon() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdeclarativeplace.html#icon

    Returns
    -------

    QPlaceIcon
      A new cute QPlaceIcon around the copy Qt gave back. Python owns it.
    """
    #  QPlaceIcon QDeclarativePlace::icon() const
    address = self.uglySide.call('ritual_ZNK17QDeclarativePlace4iconEv')
    from . import QPlaceIcon
    return QPlaceIcon._cuteOwning(address)

  def name(self) -> str:
    """
    Calls Qt's 'QString QDeclarativePlace::name() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdeclarativeplace.html#name

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QDeclarativePlace::name() const
    return self.uglySide.call('ritual_ZNK17QDeclarativePlace4nameEv')

  def placeId(self) -> str:
    """
    Calls Qt's 'QString QDeclarativePlace::placeId() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdeclarativeplace.html#placeId

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QDeclarativePlace::placeId() const
    return self.uglySide.call('ritual_ZNK17QDeclarativePlace7placeIdEv')

  def attribution(self) -> str:
    """
    Calls Qt's 'QString QDeclarativePlace::attribution() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdeclarativeplace.html#attribution

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QDeclarativePlace::attribution() const
    return self.uglySide.call('ritual_ZNK17QDeclarativePlace11attributionEv')

  def detailsFetched(self) -> bool:
    """
    Calls Qt's 'bool QDeclarativePlace::detailsFetched() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativeplace.html#detailsFetched
    """
    #  bool QDeclarativePlace::detailsFetched() const
    return self.uglySide.call(
        'ritual_ZNK17QDeclarativePlace14detailsFetchedEv',
    )

  def status(self) -> Status:
    """
    Calls Qt's 'Status QDeclarativePlace::status() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdeclarativeplace.html#status

    Returns
    -------

    Status
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Status(number)' gives.
    """
    #  Status QDeclarativePlace::status() const
    return QDeclarativePlace.Status(self.uglySide.call(
        'ritual_ZNK17QDeclarativePlace6statusEv',
    ))

  def errorString(self) -> str:
    """
    Calls Qt's 'QString QDeclarativePlace::errorString() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdeclarativeplace.html#errorString

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QDeclarativePlace::errorString() const
    return self.uglySide.call('ritual_ZNK17QDeclarativePlace11errorStringEv')

  def primaryPhone(self) -> str:
    """
    Calls Qt's 'QString QDeclarativePlace::primaryPhone() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativeplace.html#primaryPhone

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QDeclarativePlace::primaryPhone() const
    return self.uglySide.call(
        'ritual_ZNK17QDeclarativePlace12primaryPhoneEv',
    )

  def primaryFax(self) -> str:
    """
    Calls Qt's 'QString QDeclarativePlace::primaryFax() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdeclarativeplace.html#primaryFax

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QDeclarativePlace::primaryFax() const
    return self.uglySide.call('ritual_ZNK17QDeclarativePlace10primaryFaxEv')

  def primaryEmail(self) -> str:
    """
    Calls Qt's 'QString QDeclarativePlace::primaryEmail() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativeplace.html#primaryEmail

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QDeclarativePlace::primaryEmail() const
    return self.uglySide.call(
        'ritual_ZNK17QDeclarativePlace12primaryEmailEv',
    )

  def primaryWebsite(self) -> QUrl:
    """
    Calls Qt's 'QUrl QDeclarativePlace::primaryWebsite() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativeplace.html#primaryWebsite

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QDeclarativePlace::primaryWebsite() const
    address = self.uglySide.call(
        'ritual_ZNK17QDeclarativePlace14primaryWebsiteEv',
    )
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  def extendedAttributes(self) -> Optional[QQmlPropertyMap]:
    """
    Calls Qt's 'QQmlPropertyMap *QDeclarativePlace::extendedAttributes()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativeplace.html#extendedAttributes

    Returns
    -------

    Optional[QQmlPropertyMap]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlPropertyMap *QDeclarativePlace::extendedAttributes() const
    address = self.uglySide.call(
        'ritual_ZNK17QDeclarativePlace18extendedAttributesEv',
    )
    from ..QtQml import QQmlPropertyMap
    return QQmlPropertyMap._cuteAt(address)

  def contactDetails(self) -> Optional[QDeclarativeContactDetails]:
    """
    Calls Qt's 'QDeclarativeContactDetails
    *QDeclarativePlace::contactDetails() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativeplace.html#contactDetails

    Returns
    -------

    Optional[QDeclarativeContactDetails]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QDeclarativeContactDetails *QDeclarativePlace::contactDetails() const
    address = self.uglySide.call(
        'ritual_ZNK17QDeclarativePlace14contactDetailsEv',
    )
    from . import QDeclarativeContactDetails
    return QDeclarativeContactDetails._cuteAt(address)

  def visibility(self) -> Visibility:
    """
    Calls Qt's 'Visibility QDeclarativePlace::visibility() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdeclarativeplace.html#visibility

    Returns
    -------

    Visibility
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Visibility(number)'
      gives.
    """
    #  Visibility QDeclarativePlace::visibility() const
    return QDeclarativePlace.Visibility(self.uglySide.call(
        'ritual_ZNK17QDeclarativePlace10visibilityEv',
    ))

  def favorite(self) -> Optional[QDeclarativePlace]:
    """
    Calls Qt's 'QDeclarativePlace *QDeclarativePlace::favorite() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdeclarativeplace.html#favorite

    Returns
    -------

    Optional[QDeclarativePlace]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QDeclarativePlace *QDeclarativePlace::favorite() const
    address = self.uglySide.call('ritual_ZNK17QDeclarativePlace8favoriteEv')
    return QDeclarativePlace._cuteAt(address)

  @overload(str)
  def primaryValue(self, contactType: str) -> str:
    """
    Calls Qt's 'QString QDeclarativePlace::primaryValue(const QString
    &contactType) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativeplace.html#primaryValue

    Parameters
    ----------

    contactType : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QDeclarativePlace::primaryValue(const QString &contactType)
    #      const
    return self.uglySide.call(
        'ritual_ZNK17QDeclarativePlace12primaryValueERK7QString',
        contactType,
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
    QDeclarativePlace::setPlugin(QDeclarativeGeoServiceProvider *plugin)'.

    Qt's own words: https://doc.qt.io/qt-6/qdeclarativeplace.html#setPlugin

    Parameters
    ----------

    plugin : Optional[QDeclarativeGeoServiceProvider]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QDeclarativePlace::setPlugin(QDeclarativeGeoServiceProvider
    #      *plugin)
    self.uglySide.call(
        'ritual_ZN17QDeclarativePlace9setPluginEP30QDeclarativeGeoServicePr'
        'ovider',
        self._addressOf(plugin),
    )

  @overload(QPlace)
  def setPlace(self, src: QPlace) -> None:
    """
    Calls Qt's 'void QDeclarativePlace::setPlace(const QPlace &src)'.

    Qt's own words: https://doc.qt.io/qt-6/qdeclarativeplace.html#setPlace

    Parameters
    ----------

    src : QPlace
      Passed on as a value: Qt reads the C++ QPlace, which stays Python's
      own.
    """
    #  void QDeclarativePlace::setPlace(const QPlace &src)
    self.uglySide.call(
        'ritual_ZN17QDeclarativePlace8setPlaceERK6QPlace',
        self._valueOf(src),
    )

  @overload(QDeclarativeGeoLocation)
  @overload(NoneType)
  def setLocation(self, location: Optional[QDeclarativeGeoLocation]) -> None:
    """
    Calls Qt's 'void QDeclarativePlace::setLocation(QDeclarativeGeoLocation
    *location)'.

    Qt's own words: https://doc.qt.io/qt-6/qdeclarativeplace.html#setLocation

    Parameters
    ----------

    location : Optional[QDeclarativeGeoLocation]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QDeclarativePlace::setLocation(QDeclarativeGeoLocation *location)
    self.uglySide.call(
        'ritual_ZN17QDeclarativePlace11setLocationEP23QDeclarativeGeoLocati'
        'on',
        self._addressOf(location),
    )

  @overload(QPlaceRatings)
  def setRatings(self, ratings: QPlaceRatings) -> None:
    """
    Calls Qt's 'void QDeclarativePlace::setRatings(const QPlaceRatings
    &ratings)'.

    Qt's own words: https://doc.qt.io/qt-6/qdeclarativeplace.html#setRatings

    Parameters
    ----------

    ratings : QPlaceRatings
      Passed on as a value: Qt reads the C++ QPlaceRatings, which stays
      Python's own.
    """
    #  void QDeclarativePlace::setRatings(const QPlaceRatings &ratings)
    self.uglySide.call(
        'ritual_ZN17QDeclarativePlace10setRatingsERK13QPlaceRatings',
        self._valueOf(ratings),
    )

  @overload(QPlaceSupplier)
  def setSupplier(self, supplier: QPlaceSupplier) -> None:
    """
    Calls Qt's 'void QDeclarativePlace::setSupplier(const QPlaceSupplier
    &supplier)'.

    Qt's own words: https://doc.qt.io/qt-6/qdeclarativeplace.html#setSupplier

    Parameters
    ----------

    supplier : QPlaceSupplier
      Passed on as a value: Qt reads the C++ QPlaceSupplier, which stays
      Python's own.
    """
    #  void QDeclarativePlace::setSupplier(const QPlaceSupplier &supplier)
    self.uglySide.call(
        'ritual_ZN17QDeclarativePlace11setSupplierERK14QPlaceSupplier',
        self._valueOf(supplier),
    )

  @overload(QPlaceIcon)
  def setIcon(self, icon: QPlaceIcon) -> None:
    """
    Calls Qt's 'void QDeclarativePlace::setIcon(const QPlaceIcon &icon)'.

    Qt's own words: https://doc.qt.io/qt-6/qdeclarativeplace.html#setIcon

    Parameters
    ----------

    icon : QPlaceIcon
      Passed on as a value: Qt reads the C++ QPlaceIcon, which stays Python's
      own.
    """
    #  void QDeclarativePlace::setIcon(const QPlaceIcon &icon)
    self.uglySide.call(
        'ritual_ZN17QDeclarativePlace7setIconERK10QPlaceIcon',
        self._valueOf(icon),
    )

  @overload(str)
  def setName(self, name: str) -> None:
    """
    Calls Qt's 'void QDeclarativePlace::setName(const QString &name)'.

    Qt's own words: https://doc.qt.io/qt-6/qdeclarativeplace.html#setName

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QDeclarativePlace::setName(const QString &name)
    self.uglySide.call(
        'ritual_ZN17QDeclarativePlace7setNameERK7QString', name,
    )

  @overload(str)
  def setPlaceId(self, placeId: str) -> None:
    """
    Calls Qt's 'void QDeclarativePlace::setPlaceId(const QString &placeId)'.

    Qt's own words: https://doc.qt.io/qt-6/qdeclarativeplace.html#setPlaceId

    Parameters
    ----------

    placeId : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QDeclarativePlace::setPlaceId(const QString &placeId)
    self.uglySide.call(
        'ritual_ZN17QDeclarativePlace10setPlaceIdERK7QString', placeId,
    )

  @overload(str)
  def setAttribution(self, attribution: str) -> None:
    """
    Calls Qt's 'void QDeclarativePlace::setAttribution(const QString
    &attribution)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativeplace.html#setAttribution

    Parameters
    ----------

    attribution : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QDeclarativePlace::setAttribution(const QString &attribution)
    self.uglySide.call(
        'ritual_ZN17QDeclarativePlace14setAttributionERK7QString',
        attribution,
    )

  @overload(Status)
  @overload(Status, str)
  def setStatus(self, status: Status, errorString: str = '') -> None:
    """
    Calls Qt's 'void QDeclarativePlace::setStatus(Status status, const
    QString &errorString)'.

    Qt's own words: https://doc.qt.io/qt-6/qdeclarativeplace.html#setStatus

    Parameters
    ----------

    status : Status
      Passed on as its number.

    errorString : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.
    """
    #  void QDeclarativePlace::setStatus(Status status, const QString
    #      &errorString)
    self.uglySide.call(
        'ritual_ZN17QDeclarativePlace9setStatusENS_6StatusERK7QString',
        status.value, errorString,
    )

  @overload(Visibility)
  def setVisibility(self, visibility: Visibility) -> None:
    """
    Calls Qt's 'void QDeclarativePlace::setVisibility(Visibility
    visibility)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativeplace.html#setVisibility

    Parameters
    ----------

    visibility : Visibility
      Passed on as its number.
    """
    #  void QDeclarativePlace::setVisibility(Visibility visibility)
    self.uglySide.call(
        'ritual_ZN17QDeclarativePlace13setVisibilityENS_10VisibilityE',
        visibility.value,
    )

  @overload(THIS)
  @overload(NoneType)
  def setFavorite(self, favorite: Optional[QDeclarativePlace]) -> None:
    """
    Calls Qt's 'void QDeclarativePlace::setFavorite(QDeclarativePlace
    *favorite)'.

    Qt's own words: https://doc.qt.io/qt-6/qdeclarativeplace.html#setFavorite

    Parameters
    ----------

    favorite : Optional[QDeclarativePlace]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QDeclarativePlace::setFavorite(QDeclarativePlace *favorite)
    self.uglySide.call(
        'ritual_ZN17QDeclarativePlace11setFavoriteEPS_',
        self._addressOf(favorite),
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
    'QDeclarativePlace::QDeclarativePlace(QObject *parent)', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativeplace.html#QDeclarativePlace

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QDeclarativePlace::QDeclarativePlace(QObject *parent)
    self._noteCreation(QDeclarativePlace, lambda: Rituals.call(
        'ritual_ZN17QDeclarativePlaceC1EP7QObject',
        self._addressOf(parent, 'QObject'),
    ))

  @overload(QPlace, QDeclarativeGeoServiceProvider)
  @overload(QPlace, NoneType)
  @overload(QPlace, QDeclarativeGeoServiceProvider, QObject)
  @overload(QPlace, QDeclarativeGeoServiceProvider, NoneType)
  @overload(QPlace, NoneType, QObject)
  @overload(QPlace, NoneType, NoneType)
  def __init__(
      self,
      src: QPlace,
      plugin: Optional[QDeclarativeGeoServiceProvider],
      parent: Optional[QObject] = None,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QDeclarativePlace::QDeclarativePlace(const QPlace &src,
    QDeclarativeGeoServiceProvider *plugin, QObject *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativeplace.html#QDeclarativePlace

    Parameters
    ----------

    src : QPlace
      Passed on as a value: Qt reads the C++ QPlace, which stays Python's
      own.

    plugin : Optional[QDeclarativeGeoServiceProvider]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QDeclarativePlace::QDeclarativePlace(const QPlace &src,
    #      QDeclarativeGeoServiceProvider *plugin, QObject *parent)
    self._noteCreation(QDeclarativePlace, lambda: Rituals.call(
        'ritual_ZN17QDeclarativePlaceC1ERK6QPlaceP30QDeclarativeGeoServiceP'
        'roviderP7QObject',
        self._valueOf(src), self._addressOf(plugin), self._addressOf(parent,
        'QObject'),
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
    Calls Qt's 'void QDeclarativePlace::classBegin()'.

    Qt's own words: https://doc.qt.io/qt-6/qdeclarativeplace.html#classBegin
    """
    #  void QDeclarativePlace::classBegin()
    ritual = 'ritual_ZN17QDeclarativePlace10classBeginEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QDeclarativePlace10classBeginEv'
    self.uglySide.call(ritual)

  def componentComplete(self) -> None:
    """
    Calls Qt's 'void QDeclarativePlace::componentComplete()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativeplace.html#componentComplete
    """
    #  void QDeclarativePlace::componentComplete()
    ritual = 'ritual_ZN17QDeclarativePlace17componentCompleteEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QDeclarativePlace17componentCompleteEv'
    self.uglySide.call(ritual)

  def reviewModel(self) -> Optional[QDeclarativePlaceReviewModel]:
    """
    Calls Qt's 'QDeclarativePlaceReviewModel
    *QDeclarativePlace::reviewModel()'.

    Qt's own words: https://doc.qt.io/qt-6/qdeclarativeplace.html#reviewModel

    Returns
    -------

    Optional[QDeclarativePlaceReviewModel]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QDeclarativePlaceReviewModel *QDeclarativePlace::reviewModel()
    address = self.uglySide.call(
        'ritual_ZN17QDeclarativePlace11reviewModelEv',
    )
    from . import QDeclarativePlaceReviewModel
    return QDeclarativePlaceReviewModel._cuteAt(address)

  def imageModel(self) -> Optional[QDeclarativePlaceImageModel]:
    """
    Calls Qt's 'QDeclarativePlaceImageModel
    *QDeclarativePlace::imageModel()'.

    Qt's own words: https://doc.qt.io/qt-6/qdeclarativeplace.html#imageModel

    Returns
    -------

    Optional[QDeclarativePlaceImageModel]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QDeclarativePlaceImageModel *QDeclarativePlace::imageModel()
    address = self.uglySide.call(
        'ritual_ZN17QDeclarativePlace10imageModelEv',
    )
    from . import QDeclarativePlaceImageModel
    return QDeclarativePlaceImageModel._cuteAt(address)

  def editorialModel(self) -> Optional[QDeclarativePlaceEditorialModel]:
    """
    Calls Qt's 'QDeclarativePlaceEditorialModel
    *QDeclarativePlace::editorialModel()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativeplace.html#editorialModel

    Returns
    -------

    Optional[QDeclarativePlaceEditorialModel]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QDeclarativePlaceEditorialModel *QDeclarativePlace::editorialModel()
    address = self.uglySide.call(
        'ritual_ZN17QDeclarativePlace14editorialModelEv',
    )
    from . import QDeclarativePlaceEditorialModel
    return QDeclarativePlaceEditorialModel._cuteAt(address)

  def getDetails(self) -> None:
    """
    Calls Qt's 'void QDeclarativePlace::getDetails()'.

    Qt's own words: https://doc.qt.io/qt-6/qdeclarativeplace.html#getDetails
    """
    #  void QDeclarativePlace::getDetails()
    self.uglySide.call('ritual_ZN17QDeclarativePlace10getDetailsEv')

  def save(self) -> None:
    """
    Calls Qt's 'void QDeclarativePlace::save()'.

    Qt's own words: https://doc.qt.io/qt-6/qdeclarativeplace.html#save
    """
    #  void QDeclarativePlace::save()
    self.uglySide.call('ritual_ZN17QDeclarativePlace4saveEv')

  def remove(self) -> None:
    """
    Calls Qt's 'void QDeclarativePlace::remove()'.

    Qt's own words: https://doc.qt.io/qt-6/qdeclarativeplace.html#remove
    """
    #  void QDeclarativePlace::remove()
    self.uglySide.call('ritual_ZN17QDeclarativePlace6removeEv')

  @overload(THIS)
  @overload(NoneType)
  def copyFrom(self, original: Optional[QDeclarativePlace]) -> None:
    """
    Calls Qt's 'void QDeclarativePlace::copyFrom(QDeclarativePlace
    *original)'.

    Qt's own words: https://doc.qt.io/qt-6/qdeclarativeplace.html#copyFrom

    Parameters
    ----------

    original : Optional[QDeclarativePlace]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QDeclarativePlace::copyFrom(QDeclarativePlace *original)
    self.uglySide.call(
        'ritual_ZN17QDeclarativePlace8copyFromEPS_',
        self._addressOf(original),
    )

  @overload(QDeclarativeGeoServiceProvider)
  @overload(NoneType)
  def initializeFavorite(
      self,
      plugin: Optional[QDeclarativeGeoServiceProvider],
  ) -> None:
    """
    Calls Qt's 'void
    QDeclarativePlace::initializeFavorite(QDeclarativeGeoServiceProvider
    *plugin)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativeplace.html#initializeFavorite

    Parameters
    ----------

    plugin : Optional[QDeclarativeGeoServiceProvider]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QDeclarativePlace::initializeFavorite(
    #      QDeclarativeGeoServiceProvider *plugin)
    self.uglySide.call(
        'ritual_ZN17QDeclarativePlace18initializeFavoriteEP30QDeclarativeGe'
        'oServiceProvider',
        self._addressOf(plugin),
    )

  def pluginChanged(self) -> None:
    """
    Calls Qt's 'void QDeclarativePlace::pluginChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativeplace.html#pluginChanged
    """
    #  void QDeclarativePlace::pluginChanged()
    self.uglySide.call('ritual_ZN17QDeclarativePlace13pluginChangedEv')

  def categoriesChanged(self) -> None:
    """
    Calls Qt's 'void QDeclarativePlace::categoriesChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativeplace.html#categoriesChanged
    """
    #  void QDeclarativePlace::categoriesChanged()
    self.uglySide.call('ritual_ZN17QDeclarativePlace17categoriesChangedEv')

  def locationChanged(self) -> None:
    """
    Calls Qt's 'void QDeclarativePlace::locationChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativeplace.html#locationChanged
    """
    #  void QDeclarativePlace::locationChanged()
    self.uglySide.call('ritual_ZN17QDeclarativePlace15locationChangedEv')

  def ratingsChanged(self) -> None:
    """
    Calls Qt's 'void QDeclarativePlace::ratingsChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativeplace.html#ratingsChanged
    """
    #  void QDeclarativePlace::ratingsChanged()
    self.uglySide.call('ritual_ZN17QDeclarativePlace14ratingsChangedEv')

  def supplierChanged(self) -> None:
    """
    Calls Qt's 'void QDeclarativePlace::supplierChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativeplace.html#supplierChanged
    """
    #  void QDeclarativePlace::supplierChanged()
    self.uglySide.call('ritual_ZN17QDeclarativePlace15supplierChangedEv')

  def iconChanged(self) -> None:
    """
    Calls Qt's 'void QDeclarativePlace::iconChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qdeclarativeplace.html#iconChanged
    """
    #  void QDeclarativePlace::iconChanged()
    self.uglySide.call('ritual_ZN17QDeclarativePlace11iconChangedEv')

  def nameChanged(self) -> None:
    """
    Calls Qt's 'void QDeclarativePlace::nameChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qdeclarativeplace.html#nameChanged
    """
    #  void QDeclarativePlace::nameChanged()
    self.uglySide.call('ritual_ZN17QDeclarativePlace11nameChangedEv')

  def placeIdChanged(self) -> None:
    """
    Calls Qt's 'void QDeclarativePlace::placeIdChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativeplace.html#placeIdChanged
    """
    #  void QDeclarativePlace::placeIdChanged()
    self.uglySide.call('ritual_ZN17QDeclarativePlace14placeIdChangedEv')

  def attributionChanged(self) -> None:
    """
    Calls Qt's 'void QDeclarativePlace::attributionChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativeplace.html#attributionChanged
    """
    #  void QDeclarativePlace::attributionChanged()
    self.uglySide.call('ritual_ZN17QDeclarativePlace18attributionChangedEv')

  def detailsFetchedChanged(self) -> None:
    """
    Calls Qt's 'void QDeclarativePlace::detailsFetchedChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativeplace.html#detailsFetchedChanged
    """
    #  void QDeclarativePlace::detailsFetchedChanged()
    self.uglySide.call(
        'ritual_ZN17QDeclarativePlace21detailsFetchedChangedEv',
    )

  def reviewModelChanged(self) -> None:
    """
    Calls Qt's 'void QDeclarativePlace::reviewModelChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativeplace.html#reviewModelChanged
    """
    #  void QDeclarativePlace::reviewModelChanged()
    self.uglySide.call('ritual_ZN17QDeclarativePlace18reviewModelChangedEv')

  def imageModelChanged(self) -> None:
    """
    Calls Qt's 'void QDeclarativePlace::imageModelChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativeplace.html#imageModelChanged
    """
    #  void QDeclarativePlace::imageModelChanged()
    self.uglySide.call('ritual_ZN17QDeclarativePlace17imageModelChangedEv')

  def editorialModelChanged(self) -> None:
    """
    Calls Qt's 'void QDeclarativePlace::editorialModelChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativeplace.html#editorialModelChanged
    """
    #  void QDeclarativePlace::editorialModelChanged()
    self.uglySide.call(
        'ritual_ZN17QDeclarativePlace21editorialModelChangedEv',
    )

  def primaryPhoneChanged(self) -> None:
    """
    Calls Qt's 'void QDeclarativePlace::primaryPhoneChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativeplace.html#primaryPhoneChanged
    """
    #  void QDeclarativePlace::primaryPhoneChanged()
    self.uglySide.call('ritual_ZN17QDeclarativePlace19primaryPhoneChangedEv')

  def primaryFaxChanged(self) -> None:
    """
    Calls Qt's 'void QDeclarativePlace::primaryFaxChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativeplace.html#primaryFaxChanged
    """
    #  void QDeclarativePlace::primaryFaxChanged()
    self.uglySide.call('ritual_ZN17QDeclarativePlace17primaryFaxChangedEv')

  def primaryEmailChanged(self) -> None:
    """
    Calls Qt's 'void QDeclarativePlace::primaryEmailChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativeplace.html#primaryEmailChanged
    """
    #  void QDeclarativePlace::primaryEmailChanged()
    self.uglySide.call('ritual_ZN17QDeclarativePlace19primaryEmailChangedEv')

  def primaryWebsiteChanged(self) -> None:
    """
    Calls Qt's 'void QDeclarativePlace::primaryWebsiteChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativeplace.html#primaryWebsiteChanged
    """
    #  void QDeclarativePlace::primaryWebsiteChanged()
    self.uglySide.call(
        'ritual_ZN17QDeclarativePlace21primaryWebsiteChangedEv',
    )

  def extendedAttributesChanged(self) -> None:
    """
    Calls Qt's 'void QDeclarativePlace::extendedAttributesChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativeplace.html#extendedAttributesChanged
    """
    #  void QDeclarativePlace::extendedAttributesChanged()
    self.uglySide.call(
        'ritual_ZN17QDeclarativePlace25extendedAttributesChangedEv',
    )

  def contactDetailsChanged(self) -> None:
    """
    Calls Qt's 'void QDeclarativePlace::contactDetailsChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativeplace.html#contactDetailsChanged
    """
    #  void QDeclarativePlace::contactDetailsChanged()
    self.uglySide.call(
        'ritual_ZN17QDeclarativePlace21contactDetailsChangedEv',
    )

  def statusChanged(self) -> None:
    """
    Calls Qt's 'void QDeclarativePlace::statusChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativeplace.html#statusChanged
    """
    #  void QDeclarativePlace::statusChanged()
    self.uglySide.call('ritual_ZN17QDeclarativePlace13statusChangedEv')

  def visibilityChanged(self) -> None:
    """
    Calls Qt's 'void QDeclarativePlace::visibilityChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativeplace.html#visibilityChanged
    """
    #  void QDeclarativePlace::visibilityChanged()
    self.uglySide.call('ritual_ZN17QDeclarativePlace17visibilityChangedEv')

  def favoriteChanged(self) -> None:
    """
    Calls Qt's 'void QDeclarativePlace::favoriteChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativeplace.html#favoriteChanged
    """
    #  void QDeclarativePlace::favoriteChanged()
    self.uglySide.call('ritual_ZN17QDeclarativePlace15favoriteChangedEv')

  def finished(self) -> None:
    """
    Calls Qt's 'void QDeclarativePlace::finished()'.

    Qt's own words: https://doc.qt.io/qt-6/qdeclarativeplace.html#finished
    """
    #  void QDeclarativePlace::finished()
    self.uglySide.call('ritual_ZN17QDeclarativePlace8finishedEv')

  @overload(str, QVariant)
  def contactsModified(self, a0: str, a1: QVariant) -> None:
    """
    Calls Qt's 'void QDeclarativePlace::contactsModified(const QString &a0,
    const QVariant &a1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativeplace.html#contactsModified

    Parameters
    ----------

    a0 : str
      Passed on as it is: a QString is made of it for the call.

    a1 : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void QDeclarativePlace::contactsModified(const QString &a0, const
    #      QVariant &a1)
    self.uglySide.call(
        'ritual_ZN17QDeclarativePlace16contactsModifiedERK7QStringRK8QVaria'
        'nt',
        a0, self._valueOf(a1),
    )

  def pluginReady(self) -> None:
    """
    Calls Qt's 'void QDeclarativePlace::pluginReady()'.

    Qt's own words: https://doc.qt.io/qt-6/qdeclarativeplace.html#pluginReady
    """
    #  void QDeclarativePlace::pluginReady()
    self.uglySide.call('ritual_ZN17QDeclarativePlace11pluginReadyEv')

  def cleanupDeletedCategories(self) -> None:
    """
    Calls Qt's 'void QDeclarativePlace::cleanupDeletedCategories()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativeplace.html#cleanupDeletedCategories
    """
    #  void QDeclarativePlace::cleanupDeletedCategories()
    self.uglySide.call(
        'ritual_ZN17QDeclarativePlace24cleanupDeletedCategoriesEv',
    )

  def synchronizeCategories(self) -> None:
    """
    Calls Qt's 'void QDeclarativePlace::synchronizeCategories()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativeplace.html#synchronizeCategories
    """
    #  void QDeclarativePlace::synchronizeCategories()
    self.uglySide.call(
        'ritual_ZN17QDeclarativePlace21synchronizeCategoriesEv',
    )

  def pullExtendedAttributes(self) -> None:
    """
    Calls Qt's 'void QDeclarativePlace::pullExtendedAttributes()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativeplace.html#pullExtendedAttributes
    """
    #  void QDeclarativePlace::pullExtendedAttributes()
    self.uglySide.call(
        'ritual_ZN17QDeclarativePlace22pullExtendedAttributesEv',
    )

  def synchronizeContacts(self) -> None:
    """
    Calls Qt's 'void QDeclarativePlace::synchronizeContacts()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativeplace.html#synchronizeContacts
    """
    #  void QDeclarativePlace::synchronizeContacts()
    self.uglySide.call('ritual_ZN17QDeclarativePlace19synchronizeContactsEv')

  @overload()
  @overload(str)
  def primarySignalsEmission(self, type: str = '') -> None:
    """
    Calls Qt's 'void QDeclarativePlace::primarySignalsEmission(const QString
    &type)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativeplace.html#primarySignalsEmission

    Parameters
    ----------

    type : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.
    """
    #  void QDeclarativePlace::primarySignalsEmission(const QString &type)
    self.uglySide.call(
        'ritual_ZN17QDeclarativePlace22primarySignalsEmissionERK7QString',
        type,
    )

  def manager(self) -> Optional[QPlaceManager]:
    """
    Calls Qt's 'QPlaceManager *QDeclarativePlace::manager()'.

    Qt's own words: https://doc.qt.io/qt-6/qdeclarativeplace.html#manager

    Returns
    -------

    Optional[QPlaceManager]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPlaceManager *QDeclarativePlace::manager()
    address = self.uglySide.call('ritual_ZN17QDeclarativePlace7managerEv')
    from . import QPlaceManager
    return QPlaceManager._cuteAt(address)

  @staticmethod
  def categories(*__, **_) -> Never:
    """
    Qt's 'QQmlListProperty<QDeclarativeCategory>
    QDeclarativePlace::categories()': gives a type Python has no way to take
    yet.
    """
    raise NotImplementedError(
        "'QDeclarativePlace.categories' has no cute function yet. Qt's "
        "'QQmlListProperty<QDeclarativeCategory> "
        "QDeclarativePlace::categories()': gives a type Python has no way "
        "to take yet.")

  @staticmethod
  def category_append(*__, **_) -> Never:
    """
    Qt's 'void
    QDeclarativePlace::category_append(QQmlListProperty<QDeclarativeCategory>
    *prop, QDeclarativeCategory *value)': names
    'QQmlListProperty<QDeclarativeCategory>', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QDeclarativePlace.category_append' has no cute function yet. Qt's "
        "'void "
        "QDeclarativePlace::category_append(QQmlListProperty<QDeclarativeCat"
        "egory> *prop, QDeclarativeCategory *value)': names "
        "'QQmlListProperty<QDeclarativeCategory>', which has no cute class "
        "yet.")

  @staticmethod
  def category_at(*__, **_) -> Never:
    """
    Qt's 'QDeclarativeCategory
    *QDeclarativePlace::category_at(QQmlListProperty<QDeclarativeCategory>
    *prop, qsizetype index)': names 'QQmlListProperty<QDeclarativeCategory>',
    which has no cute class yet.
    """
    raise NotImplementedError(
        "'QDeclarativePlace.category_at' has no cute function yet. Qt's "
        "'QDeclarativeCategory "
        "*QDeclarativePlace::category_at(QQmlListProperty<QDeclarativeCatego"
        "ry> *prop, qsizetype index)': names "
        "'QQmlListProperty<QDeclarativeCategory>', which has no cute class "
        "yet.")

  @staticmethod
  def category_clear(*__, **_) -> Never:
    """
    Qt's 'void
    QDeclarativePlace::category_clear(QQmlListProperty<QDeclarativeCategory>
    *prop)': names 'QQmlListProperty<QDeclarativeCategory>', which has no
    cute class yet.
    """
    raise NotImplementedError(
        "'QDeclarativePlace.category_clear' has no cute function yet. Qt's "
        "'void "
        "QDeclarativePlace::category_clear(QQmlListProperty<QDeclarativeCate"
        "gory> *prop)': names 'QQmlListProperty<QDeclarativeCategory>', "
        "which has no cute class yet.")

  @staticmethod
  def category_count(*__, **_) -> Never:
    """
    Qt's 'qsizetype
    QDeclarativePlace::category_count(QQmlListProperty<QDeclarativeCategory>
    *prop)': names 'QQmlListProperty<QDeclarativeCategory>', which has no
    cute class yet.
    """
    raise NotImplementedError(
        "'QDeclarativePlace.category_count' has no cute function yet. Qt's "
        "'qsizetype "
        "QDeclarativePlace::category_count(QQmlListProperty<QDeclarativeCate"
        "gory> *prop)': names 'QQmlListProperty<QDeclarativeCategory>', "
        "which has no cute class yet.")
