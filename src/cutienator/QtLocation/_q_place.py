"""
QPlace binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtLocation/qplace.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QList, QMap, QStringList
from . import QLocation, QPlaceContent

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QUrl
  from ..QtPositioning import QGeoLocation
  from . import QPlaceAttribute, QPlaceCategory, QPlaceContactDetail
  from . import QPlaceIcon, QPlacePrivate, QPlaceRatings, QPlaceSupplier
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QGeoLocation = WAIT['QGeoLocation']
  QPlaceAttribute = WAIT['QPlaceAttribute']
  QPlaceCategory = WAIT['QPlaceCategory']
  QPlaceContactDetail = WAIT['QPlaceContactDetail']
  QPlaceIcon = WAIT['QPlaceIcon']
  QPlaceRatings = WAIT['QPlaceRatings']
  QPlaceSupplier = WAIT['QPlaceSupplier']


class QPlace(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QPlace: a plain Python object standing in front of
  one C++ QPlace.

  C++ hands a QPlace around as a copy, so every C++ QPlace behind a cute one
  is Python's own: it is removed, by the ritual named in '__delete_ritual__',
  when the cute object goes.

  What exists
  -----------

  Every function of Qt's QPlace that has a ritual and that Python can call so
  far, 44 names in all: '__eq__', '__ne__', 'categories', 'setCategory',
  'setCategories', 'location', 'setLocation', 'ratings', 'setRatings',
  'supplier', 'setSupplier', 'attribution', 'setAttribution', 'icon',
  'setIcon', 'content', 'setContent', 'insertContent', 'totalContentCount',
  'setTotalContentCount', 'name', 'setName', 'placeId', 'setPlaceId',
  'primaryPhone', 'primaryFax', 'primaryEmail', 'primaryWebsite',
  'detailsFetched', 'setDetailsFetched', 'extendedAttributeTypes',
  'extendedAttribute', 'setExtendedAttribute', 'removeExtendedAttribute',
  'contactTypes', 'contactDetails', 'setContactDetails',
  'appendContactDetail', 'removeContactDetails', 'visibility',
  'setVisibility', 'isEmpty', 'isEqual', 'd_func'. It can be made from
  Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QPlace::QPlace(QPlace &&other)': takes a type Python has no way to
    hand over yet.
  - Qt's 'QPlace::~QPlace()': the destructor: Python removes its C++ QPlace
    by it, and has no other use for it.
  - Qt's 'QPlace &QPlace::operator=(const QPlace &other)': assignment: Python
    binds a name and has no operator for it.
  - Qt's 'QPlace &QPlace::operator=(QPlace &&other)': assignment: Python
    binds a name and has no operator for it.
  - Qt's 'void QPlace::swap(QPlace &other)': takes a type Python has no way
    to hand over yet.
  - Qt's 'QPlace::QPlace(const QSharedDataPointer<QPlacePrivate> &dd)': takes
    a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  1 of the 53 functions Qt declares: 1 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file.

  What to expect
  --------------

  - The C++ QPlace is created at the first use, not by 'QPlace(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QPlace back gives a copy the ritual made for Python,
    in a new cute QPlace.
  - Each name of Qt's QPlace that has no cute function yet, 'swap', holds a
    function that raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QPlace'

  #  Qt's '~QPlace()'. Naming it makes this a value class: Python owns every
  #  C++ QPlace behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN6QPlaceD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def categories(self) -> QList[QPlaceCategory]:
    """
    Calls Qt's 'QList<QPlaceCategory> QPlace::categories() const'.

    Qt's own words: https://doc.qt.io/qt-6/qplace.html#categories

    Returns
    -------

    QList[QPlaceCategory]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QPlaceCategory> QPlace::categories() const
    address = self.uglySide.call('ritual_ZNK6QPlace10categoriesEv')
    from . import QPlaceCategory
    return QList[QPlaceCategory]._cuteOwning(address)

  def location(self) -> QGeoLocation:
    """
    Calls Qt's 'QGeoLocation QPlace::location() const'.

    Qt's own words: https://doc.qt.io/qt-6/qplace.html#location

    Returns
    -------

    QGeoLocation
      A new cute QGeoLocation around the copy Qt gave back. Python owns it.
    """
    #  QGeoLocation QPlace::location() const
    address = self.uglySide.call('ritual_ZNK6QPlace8locationEv')
    from ..QtPositioning import QGeoLocation
    return QGeoLocation._cuteOwning(address)

  def ratings(self) -> QPlaceRatings:
    """
    Calls Qt's 'QPlaceRatings QPlace::ratings() const'.

    Qt's own words: https://doc.qt.io/qt-6/qplace.html#ratings

    Returns
    -------

    QPlaceRatings
      A new cute QPlaceRatings around the copy Qt gave back. Python owns it.
    """
    #  QPlaceRatings QPlace::ratings() const
    address = self.uglySide.call('ritual_ZNK6QPlace7ratingsEv')
    from . import QPlaceRatings
    return QPlaceRatings._cuteOwning(address)

  def supplier(self) -> QPlaceSupplier:
    """
    Calls Qt's 'QPlaceSupplier QPlace::supplier() const'.

    Qt's own words: https://doc.qt.io/qt-6/qplace.html#supplier

    Returns
    -------

    QPlaceSupplier
      A new cute QPlaceSupplier around the copy Qt gave back. Python owns it.
    """
    #  QPlaceSupplier QPlace::supplier() const
    address = self.uglySide.call('ritual_ZNK6QPlace8supplierEv')
    from . import QPlaceSupplier
    return QPlaceSupplier._cuteOwning(address)

  def attribution(self) -> str:
    """
    Calls Qt's 'QString QPlace::attribution() const'.

    Qt's own words: https://doc.qt.io/qt-6/qplace.html#attribution

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QPlace::attribution() const
    return self.uglySide.call('ritual_ZNK6QPlace11attributionEv')

  def icon(self) -> QPlaceIcon:
    """
    Calls Qt's 'QPlaceIcon QPlace::icon() const'.

    Qt's own words: https://doc.qt.io/qt-6/qplace.html#icon

    Returns
    -------

    QPlaceIcon
      A new cute QPlaceIcon around the copy Qt gave back. Python owns it.
    """
    #  QPlaceIcon QPlace::icon() const
    address = self.uglySide.call('ritual_ZNK6QPlace4iconEv')
    from . import QPlaceIcon
    return QPlaceIcon._cuteOwning(address)

  @overload(QPlaceContent.Type)
  def content(self, type: QPlaceContent.Type) -> QMap[int, QPlaceContent]:
    """
    Calls Qt's 'QPlaceContent::Collection QPlace::content(QPlaceContent::Type
    type) const'.

    Qt's own words: https://doc.qt.io/qt-6/qplace.html#content

    Parameters
    ----------

    type : QPlaceContent.Type
      Passed on as its number.

    Returns
    -------

    QMap[int, QPlaceContent]
      A new cute map around the copy Qt gave back. Python owns it.
    """
    #  QPlaceContent::Collection QPlace::content(QPlaceContent::Type type)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK6QPlace7contentEN13QPlaceContent4TypeE', type.value,
    )
    return QMap[int, QPlaceContent]._cuteOwning(address)

  @overload(QPlaceContent.Type)
  def totalContentCount(self, type: QPlaceContent.Type) -> int:
    """
    Calls Qt's 'int QPlace::totalContentCount(QPlaceContent::Type type)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qplace.html#totalContentCount

    Parameters
    ----------

    type : QPlaceContent.Type
      Passed on as its number.
    """
    #  int QPlace::totalContentCount(QPlaceContent::Type type) const
    return self.uglySide.call(
        'ritual_ZNK6QPlace17totalContentCountEN13QPlaceContent4TypeE',
        type.value,
    )

  def name(self) -> str:
    """
    Calls Qt's 'QString QPlace::name() const'.

    Qt's own words: https://doc.qt.io/qt-6/qplace.html#name

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QPlace::name() const
    return self.uglySide.call('ritual_ZNK6QPlace4nameEv')

  def placeId(self) -> str:
    """
    Calls Qt's 'QString QPlace::placeId() const'.

    Qt's own words: https://doc.qt.io/qt-6/qplace.html#placeId

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QPlace::placeId() const
    return self.uglySide.call('ritual_ZNK6QPlace7placeIdEv')

  def primaryPhone(self) -> str:
    """
    Calls Qt's 'QString QPlace::primaryPhone() const'.

    Qt's own words: https://doc.qt.io/qt-6/qplace.html#primaryPhone

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QPlace::primaryPhone() const
    return self.uglySide.call('ritual_ZNK6QPlace12primaryPhoneEv')

  def primaryFax(self) -> str:
    """
    Calls Qt's 'QString QPlace::primaryFax() const'.

    Qt's own words: https://doc.qt.io/qt-6/qplace.html#primaryFax

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QPlace::primaryFax() const
    return self.uglySide.call('ritual_ZNK6QPlace10primaryFaxEv')

  def primaryEmail(self) -> str:
    """
    Calls Qt's 'QString QPlace::primaryEmail() const'.

    Qt's own words: https://doc.qt.io/qt-6/qplace.html#primaryEmail

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QPlace::primaryEmail() const
    return self.uglySide.call('ritual_ZNK6QPlace12primaryEmailEv')

  def primaryWebsite(self) -> QUrl:
    """
    Calls Qt's 'QUrl QPlace::primaryWebsite() const'.

    Qt's own words: https://doc.qt.io/qt-6/qplace.html#primaryWebsite

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QPlace::primaryWebsite() const
    address = self.uglySide.call('ritual_ZNK6QPlace14primaryWebsiteEv')
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  def detailsFetched(self) -> bool:
    """
    Calls Qt's 'bool QPlace::detailsFetched() const'.

    Qt's own words: https://doc.qt.io/qt-6/qplace.html#detailsFetched
    """
    #  bool QPlace::detailsFetched() const
    return self.uglySide.call('ritual_ZNK6QPlace14detailsFetchedEv')

  def extendedAttributeTypes(self) -> QStringList:
    """
    Calls Qt's 'QStringList QPlace::extendedAttributeTypes() const'.

    Qt's own words: https://doc.qt.io/qt-6/qplace.html#extendedAttributeTypes

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QPlace::extendedAttributeTypes() const
    address = self.uglySide.call(
        'ritual_ZNK6QPlace22extendedAttributeTypesEv',
    )
    return QStringList._cuteOwning(address)

  @overload(str)
  def extendedAttribute(self, attributeType: str) -> QPlaceAttribute:
    """
    Calls Qt's 'QPlaceAttribute QPlace::extendedAttribute(const QString
    &attributeType) const'.

    Qt's own words: https://doc.qt.io/qt-6/qplace.html#extendedAttribute

    Parameters
    ----------

    attributeType : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QPlaceAttribute
      A new cute QPlaceAttribute around the copy Qt gave back. Python owns
      it.
    """
    #  QPlaceAttribute QPlace::extendedAttribute(const QString
    #      &attributeType) const
    address = self.uglySide.call(
        'ritual_ZNK6QPlace17extendedAttributeERK7QString', attributeType,
    )
    from . import QPlaceAttribute
    return QPlaceAttribute._cuteOwning(address)

  def contactTypes(self) -> QStringList:
    """
    Calls Qt's 'QStringList QPlace::contactTypes() const'.

    Qt's own words: https://doc.qt.io/qt-6/qplace.html#contactTypes

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QPlace::contactTypes() const
    address = self.uglySide.call('ritual_ZNK6QPlace12contactTypesEv')
    return QStringList._cuteOwning(address)

  @overload(str)
  def contactDetails(self, contactType: str) -> QList[QPlaceContactDetail]:
    """
    Calls Qt's 'QList<QPlaceContactDetail> QPlace::contactDetails(const
    QString &contactType) const'.

    Qt's own words: https://doc.qt.io/qt-6/qplace.html#contactDetails

    Parameters
    ----------

    contactType : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QList[QPlaceContactDetail]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QPlaceContactDetail> QPlace::contactDetails(const QString
    #      &contactType) const
    address = self.uglySide.call(
        'ritual_ZNK6QPlace14contactDetailsERK7QString', contactType,
    )
    from . import QPlaceContactDetail
    return QList[QPlaceContactDetail]._cuteOwning(address)

  def visibility(self) -> QLocation.Visibility:
    """
    Calls Qt's 'QLocation::Visibility QPlace::visibility() const'.

    Qt's own words: https://doc.qt.io/qt-6/qplace.html#visibility

    Returns
    -------

    QLocation.Visibility
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QLocation.Visibility(number)' gives.
    """
    #  QLocation::Visibility QPlace::visibility() const
    return QLocation.Visibility(self.uglySide.call(
        'ritual_ZNK6QPlace10visibilityEv',
    ))

  def isEmpty(self) -> bool:
    """
    Calls Qt's 'bool QPlace::isEmpty() const'.

    Qt's own words: https://doc.qt.io/qt-6/qplace.html#isEmpty
    """
    #  bool QPlace::isEmpty() const
    return self.uglySide.call('ritual_ZNK6QPlace7isEmptyEv')

  @overload(THIS)
  def isEqual(self, other: QPlace) -> bool:
    """
    Calls Qt's 'bool QPlace::isEqual(const QPlace &other) const'.

    Qt's own words: https://doc.qt.io/qt-6/qplace.html#isEqual

    Parameters
    ----------

    other : QPlace
      Passed on as a value: Qt reads the C++ QPlace, which stays Python's
      own.
    """
    #  bool QPlace::isEqual(const QPlace &other) const
    return self.uglySide.call(
        'ritual_ZNK6QPlace7isEqualERKS_', self._valueOf(other),
    )

  def d_func(self) -> Optional[QPlacePrivate]:
    """
    Calls Qt's 'const QPlacePrivate *QPlace::d_func() const'.

    Qt's own words: https://doc.qt.io/qt-6/qplace.html#d_func

    Returns
    -------

    Optional[QPlacePrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QPlacePrivate *QPlace::d_func() const
    address = self.uglySide.call('ritual_ZNK6QPlace6d_funcEv')
    from . import QPlacePrivate
    return QPlacePrivate._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QPlaceCategory)
  def setCategory(self, category: QPlaceCategory) -> None:
    """
    Calls Qt's 'void QPlace::setCategory(const QPlaceCategory &category)'.

    Qt's own words: https://doc.qt.io/qt-6/qplace.html#setCategory

    Parameters
    ----------

    category : QPlaceCategory
      Passed on as a value: Qt reads the C++ QPlaceCategory, which stays
      Python's own.
    """
    #  void QPlace::setCategory(const QPlaceCategory &category)
    self.uglySide.call(
        'ritual_ZN6QPlace11setCategoryERK14QPlaceCategory',
        self._valueOf(category),
    )

  @overload(QList[QPlaceCategory])
  def setCategories(self, categories: QList[QPlaceCategory]) -> None:
    """
    Calls Qt's 'void QPlace::setCategories(const QList<QPlaceCategory>
    &categories)'.

    Qt's own words: https://doc.qt.io/qt-6/qplace.html#setCategories

    Parameters
    ----------

    categories : QList[QPlaceCategory]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QPlace::setCategories(const QList<QPlaceCategory> &categories)
    self.uglySide.call(
        'ritual_ZN6QPlace13setCategoriesERK5QListI14QPlaceCategoryE',
        self._valueOf(categories),
    )

  @overload(QGeoLocation)
  def setLocation(self, location: QGeoLocation) -> None:
    """
    Calls Qt's 'void QPlace::setLocation(const QGeoLocation &location)'.

    Qt's own words: https://doc.qt.io/qt-6/qplace.html#setLocation

    Parameters
    ----------

    location : QGeoLocation
      Passed on as a value: Qt reads the C++ QGeoLocation, which stays
      Python's own.
    """
    #  void QPlace::setLocation(const QGeoLocation &location)
    self.uglySide.call(
        'ritual_ZN6QPlace11setLocationERK12QGeoLocation',
        self._valueOf(location),
    )

  @overload(QPlaceRatings)
  def setRatings(self, ratings: QPlaceRatings) -> None:
    """
    Calls Qt's 'void QPlace::setRatings(const QPlaceRatings &ratings)'.

    Qt's own words: https://doc.qt.io/qt-6/qplace.html#setRatings

    Parameters
    ----------

    ratings : QPlaceRatings
      Passed on as a value: Qt reads the C++ QPlaceRatings, which stays
      Python's own.
    """
    #  void QPlace::setRatings(const QPlaceRatings &ratings)
    self.uglySide.call(
        'ritual_ZN6QPlace10setRatingsERK13QPlaceRatings',
        self._valueOf(ratings),
    )

  @overload(QPlaceSupplier)
  def setSupplier(self, supplier: QPlaceSupplier) -> None:
    """
    Calls Qt's 'void QPlace::setSupplier(const QPlaceSupplier &supplier)'.

    Qt's own words: https://doc.qt.io/qt-6/qplace.html#setSupplier

    Parameters
    ----------

    supplier : QPlaceSupplier
      Passed on as a value: Qt reads the C++ QPlaceSupplier, which stays
      Python's own.
    """
    #  void QPlace::setSupplier(const QPlaceSupplier &supplier)
    self.uglySide.call(
        'ritual_ZN6QPlace11setSupplierERK14QPlaceSupplier',
        self._valueOf(supplier),
    )

  @overload(str)
  def setAttribution(self, attribution: str) -> None:
    """
    Calls Qt's 'void QPlace::setAttribution(const QString &attribution)'.

    Qt's own words: https://doc.qt.io/qt-6/qplace.html#setAttribution

    Parameters
    ----------

    attribution : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QPlace::setAttribution(const QString &attribution)
    self.uglySide.call(
        'ritual_ZN6QPlace14setAttributionERK7QString', attribution,
    )

  @overload(QPlaceIcon)
  def setIcon(self, icon: QPlaceIcon) -> None:
    """
    Calls Qt's 'void QPlace::setIcon(const QPlaceIcon &icon)'.

    Qt's own words: https://doc.qt.io/qt-6/qplace.html#setIcon

    Parameters
    ----------

    icon : QPlaceIcon
      Passed on as a value: Qt reads the C++ QPlaceIcon, which stays Python's
      own.
    """
    #  void QPlace::setIcon(const QPlaceIcon &icon)
    self.uglySide.call(
        'ritual_ZN6QPlace7setIconERK10QPlaceIcon', self._valueOf(icon),
    )

  @overload(QPlaceContent.Type, QMap[int, QPlaceContent])
  def setContent(
      self,
      type: QPlaceContent.Type,
      content: QMap[int, QPlaceContent],
  ) -> None:
    """
    Calls Qt's 'void QPlace::setContent(QPlaceContent::Type type, const
    QPlaceContent::Collection &content)'.

    Qt's own words: https://doc.qt.io/qt-6/qplace.html#setContent

    Parameters
    ----------

    type : QPlaceContent.Type
      Passed on as its number.

    content : QMap[int, QPlaceContent]
      Passed on as a map of Qt: Qt reads the C++ map, which stays Python's
      own. A dict of Python is made into one first, and refused when a key or
      a value does not fit.
    """
    #  void QPlace::setContent(QPlaceContent::Type type, const
    #      QPlaceContent::Collection &content)
    self.uglySide.call(
        'ritual_ZN6QPlace10setContentEN13QPlaceContent4TypeERK4QMapIiS0_E',
        type.value, self._valueOf(content),
    )

  @overload(QPlaceContent.Type, int)
  def setTotalContentCount(
      self,
      type: QPlaceContent.Type,
      total: int,
  ) -> None:
    """
    Calls Qt's 'void QPlace::setTotalContentCount(QPlaceContent::Type type,
    int total)'.

    Qt's own words: https://doc.qt.io/qt-6/qplace.html#setTotalContentCount

    Parameters
    ----------

    type : QPlaceContent.Type
      Passed on as its number.

    total : int
      Passed on as it is.
    """
    #  void QPlace::setTotalContentCount(QPlaceContent::Type type, int total)
    self.uglySide.call(
        'ritual_ZN6QPlace20setTotalContentCountEN13QPlaceContent4TypeEi',
        type.value, total,
    )

  @overload(str)
  def setName(self, name: str) -> None:
    """
    Calls Qt's 'void QPlace::setName(const QString &name)'.

    Qt's own words: https://doc.qt.io/qt-6/qplace.html#setName

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QPlace::setName(const QString &name)
    self.uglySide.call('ritual_ZN6QPlace7setNameERK7QString', name)

  @overload(str)
  def setPlaceId(self, identifier: str) -> None:
    """
    Calls Qt's 'void QPlace::setPlaceId(const QString &identifier)'.

    Qt's own words: https://doc.qt.io/qt-6/qplace.html#setPlaceId

    Parameters
    ----------

    identifier : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QPlace::setPlaceId(const QString &identifier)
    self.uglySide.call('ritual_ZN6QPlace10setPlaceIdERK7QString', identifier)

  @overload(bool)
  def setDetailsFetched(self, fetched: bool) -> None:
    """
    Calls Qt's 'void QPlace::setDetailsFetched(bool fetched)'.

    Qt's own words: https://doc.qt.io/qt-6/qplace.html#setDetailsFetched

    Parameters
    ----------

    fetched : bool
      Passed on as it is.
    """
    #  void QPlace::setDetailsFetched(bool fetched)
    self.uglySide.call('ritual_ZN6QPlace17setDetailsFetchedEb', fetched)

  @overload(str, QPlaceAttribute)
  def setExtendedAttribute(
      self,
      attributeType: str,
      attribute: QPlaceAttribute,
  ) -> None:
    """
    Calls Qt's 'void QPlace::setExtendedAttribute(const QString
    &attributeType, const QPlaceAttribute &attribute)'.

    Qt's own words: https://doc.qt.io/qt-6/qplace.html#setExtendedAttribute

    Parameters
    ----------

    attributeType : str
      Passed on as it is: a QString is made of it for the call.

    attribute : QPlaceAttribute
      Passed on as a value: Qt reads the C++ QPlaceAttribute, which stays
      Python's own.
    """
    #  void QPlace::setExtendedAttribute(const QString &attributeType, const
    #      QPlaceAttribute &attribute)
    self.uglySide.call(
        'ritual_ZN6QPlace20setExtendedAttributeERK7QStringRK15QPlaceAttribu'
        'te',
        attributeType, self._valueOf(attribute),
    )

  @overload(str, QList[QPlaceContactDetail])
  def setContactDetails(
      self,
      contactType: str,
      details: QList[QPlaceContactDetail],
  ) -> None:
    """
    Calls Qt's 'void QPlace::setContactDetails(const QString &contactType,
    QList<QPlaceContactDetail> details)'.

    Qt's own words: https://doc.qt.io/qt-6/qplace.html#setContactDetails

    Parameters
    ----------

    contactType : str
      Passed on as it is: a QString is made of it for the call.

    details : QList[QPlaceContactDetail]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QPlace::setContactDetails(const QString &contactType,
    #      QList<QPlaceContactDetail> details)
    self.uglySide.call(
        'ritual_ZN6QPlace17setContactDetailsERK7QString5QListI19QPlaceConta'
        'ctDetailE',
        contactType, self._valueOf(details),
    )

  @overload(QLocation.Visibility)
  def setVisibility(self, visibility: QLocation.Visibility) -> None:
    """
    Calls Qt's 'void QPlace::setVisibility(QLocation::Visibility
    visibility)'.

    Qt's own words: https://doc.qt.io/qt-6/qplace.html#setVisibility

    Parameters
    ----------

    visibility : QLocation.Visibility
      Passed on as its number.
    """
    #  void QPlace::setVisibility(QLocation::Visibility visibility)
    self.uglySide.call(
        'ritual_ZN6QPlace13setVisibilityEN9QLocation10VisibilityE',
        visibility.value,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __eq__(self, rhs: QPlace) -> bool:
    """
    Calls Qt's 'bool operator==(const QPlace &lhs, const QPlace &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qplace.html#operator==

    Parameters
    ----------

    rhs : QPlace
      Passed on as a value: Qt reads the C++ QPlace, which stays Python's
      own.
    """
    #  bool operator==(const QPlace &lhs, const QPlace &rhs)
    return Rituals.call(
        'ritual_ZeqRK6QPlaceS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload.fallback
  def __eq__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(THIS)
  def __ne__(self, rhs: QPlace) -> bool:
    """
    Calls Qt's 'bool operator!=(const QPlace &lhs, const QPlace &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qplace.html#operator!=

    Parameters
    ----------

    rhs : QPlace
      Passed on as a value: Qt reads the C++ QPlace, which stays Python's
      own.
    """
    #  bool operator!=(const QPlace &lhs, const QPlace &rhs)
    return Rituals.call(
        'ritual_ZneRK6QPlaceS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload.fallback
  def __ne__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'QPlace::QPlace()', which is called at the
    first use.

    Qt's own words: https://doc.qt.io/qt-6/qplace.html#QPlace
    """
    #  QPlace::QPlace()
    self._noteCreation(QPlace, lambda: Rituals.call('ritual_ZN6QPlaceC1Ev'))

  @overload(THIS)
  def __init__(self, other: QPlace) -> None:
    """
    Notes what was given, for Qt's 'QPlace::QPlace(const QPlace &other)',
    which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qplace.html#QPlace

    Parameters
    ----------

    other : QPlace
      Passed on as a value: Qt reads the C++ QPlace, which stays Python's
      own.
    """
    #  QPlace::QPlace(const QPlace &other)
    self._noteCreation(QPlace, lambda: Rituals.call(
        'ritual_ZN6QPlaceC1ERKS_', self._valueOf(other),
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

  @overload(QPlaceContent.Type, QMap[int, QPlaceContent])
  def insertContent(
      self,
      type: QPlaceContent.Type,
      content: QMap[int, QPlaceContent],
  ) -> None:
    """
    Calls Qt's 'void QPlace::insertContent(QPlaceContent::Type type, const
    QPlaceContent::Collection &content)'.

    Qt's own words: https://doc.qt.io/qt-6/qplace.html#insertContent

    Parameters
    ----------

    type : QPlaceContent.Type
      Passed on as its number.

    content : QMap[int, QPlaceContent]
      Passed on as a map of Qt: Qt reads the C++ map, which stays Python's
      own. A dict of Python is made into one first, and refused when a key or
      a value does not fit.
    """
    #  void QPlace::insertContent(QPlaceContent::Type type, const
    #      QPlaceContent::Collection &content)
    self.uglySide.call(
        'ritual_ZN6QPlace13insertContentEN13QPlaceContent4TypeERK4QMapIiS0_'
        'E',
        type.value, self._valueOf(content),
    )

  @overload(str)
  def removeExtendedAttribute(self, attributeType: str) -> None:
    """
    Calls Qt's 'void QPlace::removeExtendedAttribute(const QString
    &attributeType)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplace.html#removeExtendedAttribute

    Parameters
    ----------

    attributeType : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QPlace::removeExtendedAttribute(const QString &attributeType)
    self.uglySide.call(
        'ritual_ZN6QPlace23removeExtendedAttributeERK7QString',
        attributeType,
    )

  @overload(str, QPlaceContactDetail)
  def appendContactDetail(
      self,
      contactType: str,
      detail: QPlaceContactDetail,
  ) -> None:
    """
    Calls Qt's 'void QPlace::appendContactDetail(const QString &contactType,
    const QPlaceContactDetail &detail)'.

    Qt's own words: https://doc.qt.io/qt-6/qplace.html#appendContactDetail

    Parameters
    ----------

    contactType : str
      Passed on as it is: a QString is made of it for the call.

    detail : QPlaceContactDetail
      Passed on as a value: Qt reads the C++ QPlaceContactDetail, which stays
      Python's own.
    """
    #  void QPlace::appendContactDetail(const QString &contactType, const
    #      QPlaceContactDetail &detail)
    self.uglySide.call(
        'ritual_ZN6QPlace19appendContactDetailERK7QStringRK19QPlaceContactD'
        'etail',
        contactType, self._valueOf(detail),
    )

  @overload(str)
  def removeContactDetails(self, contactType: str) -> None:
    """
    Calls Qt's 'void QPlace::removeContactDetails(const QString
    &contactType)'.

    Qt's own words: https://doc.qt.io/qt-6/qplace.html#removeContactDetails

    Parameters
    ----------

    contactType : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QPlace::removeContactDetails(const QString &contactType)
    self.uglySide.call(
        'ritual_ZN6QPlace20removeContactDetailsERK7QString', contactType,
    )

  @staticmethod
  def swap(*__, **_) -> Never:
    """
    Qt's 'void QPlace::swap(QPlace &other)': takes a type Python has no way
    to hand over yet.
    """
    raise NotImplementedError(
        "'QPlace.swap' has no cute function yet. Qt's 'void "
        "QPlace::swap(QPlace &other)': takes a type Python has no way to "
        "hand over yet.")


#  Qt's 'QList<QPlace>': the list of QPlace, which 'QList[QPlace]' gives. It
#  is made here, so that there is one as soon as there can be a QPlace.
QList.createKind(
    QPlace, 'value',
    make='ritual_list_make_QPlace',
    add='ritual_list_add_QPlace',
    size='ritual_list_size_QPlace',
    at='ritual_list_at_QPlace',
    drop='ritual_list_drop_QPlace',
)
