"""
QPlacePrivateDefault binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtLocation/6.12.0/QtLocation/private/qplace_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QPlacePrivateDefault to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..QtCore import QList, QMap
from . import QLocation, QPlacePrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtPositioning import QGeoLocation
  from . import QPlaceAttribute, QPlaceCategory, QPlaceIcon, QPlaceRatings
  from . import QPlaceSupplier
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QGeoLocation = WAIT['QGeoLocation']
  QPlaceCategory = WAIT['QPlaceCategory']
  QPlaceIcon = WAIT['QPlaceIcon']
  QPlaceRatings = WAIT['QPlaceRatings']
  QPlaceSupplier = WAIT['QPlaceSupplier']


class QPlacePrivateDefault(QPlacePrivate):
  """
  The cute side of Qt's QPlacePrivateDefault: a plain Python object standing
  in front of one C++ QPlacePrivateDefault.

  It is built on the cute 'QPlacePrivate', as Qt's QPlacePrivateDefault is
  built on Qt's QPlacePrivate, and has everything that class has.

  C++ hands a QPlacePrivateDefault around as a copy, so every C++
  QPlacePrivateDefault behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QPlacePrivateDefault that has a ritual and that
  Python can call so far, 22 names in all: 'clone', 'categories',
  'setCategories', 'location', 'setLocation', 'ratings', 'setRatings',
  'supplier', 'setSupplier', 'name', 'setName', 'placeId', 'setPlaceId',
  'attribution', 'setAttribution', 'visibility', 'setVisibility', 'icon',
  'setIcon', 'detailsFetched', 'setDetailsFetched', 'extendedAttributes'. It
  can be made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QPlacePrivateDefault::~QPlacePrivateDefault()': the destructor:
    Python removes its C++ QPlacePrivateDefault by it, and has no other use
    for it.
  - Qt's 'QMap<QString, QPlaceAttribute>
    &QPlacePrivateDefault::extendedAttributes()': gives a type Python has no
    way to take yet.
  - Qt's 'QMap<QString, QList<QPlaceContactDetail>>
    QPlacePrivateDefault::contacts() const': gives a type Python has no way
    to take yet.
  - Qt's 'QMap<QString, QList<QPlaceContactDetail>>
    &QPlacePrivateDefault::contacts()': gives a type Python has no way to
    take yet.

  What to expect
  --------------

  - The C++ QPlacePrivateDefault is created at the first use, not by
    'QPlacePrivateDefault(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QPlacePrivateDefault back gives a copy the ritual
    made for Python, in a new cute QPlacePrivateDefault.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QPlacePrivateDefault'

  #  A C++ QPlacePrivateDefault Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QPlacePrivateDefault'

  #  Qt's '~QPlacePrivateDefault()'. Naming it makes this a value class:
  #  Python owns every C++ QPlacePrivateDefault behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN20QPlacePrivateDefaultD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def categories(self) -> QList[QPlaceCategory]:
    """
    Calls Qt's 'QList<QPlaceCategory> QPlacePrivateDefault::categories()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplaceprivatedefault.html#categories

    Returns
    -------

    QList[QPlaceCategory]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QPlaceCategory> QPlacePrivateDefault::categories() const
    address = self.uglySide.call(
        'ritual_ZNK20QPlacePrivateDefault10categoriesEv',
    )
    from . import QPlaceCategory
    return QList[QPlaceCategory]._cuteOwning(address)

  def location(self) -> QGeoLocation:
    """
    Calls Qt's 'QGeoLocation QPlacePrivateDefault::location() const'.

    Qt's own words: https://doc.qt.io/qt-6/qplaceprivatedefault.html#location

    Returns
    -------

    QGeoLocation
      A new cute QGeoLocation around the copy Qt gave back. Python owns it.
    """
    #  QGeoLocation QPlacePrivateDefault::location() const
    ritual = 'ritual_ZNK20QPlacePrivateDefault8locationEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK20QPlacePrivateDefault8locationEv'
    address = self.uglySide.call(ritual)
    from ..QtPositioning import QGeoLocation
    return QGeoLocation._cuteOwning(address)

  def ratings(self) -> QPlaceRatings:
    """
    Calls Qt's 'QPlaceRatings QPlacePrivateDefault::ratings() const'.

    Qt's own words: https://doc.qt.io/qt-6/qplaceprivatedefault.html#ratings

    Returns
    -------

    QPlaceRatings
      A new cute QPlaceRatings around the copy Qt gave back. Python owns it.
    """
    #  QPlaceRatings QPlacePrivateDefault::ratings() const
    ritual = 'ritual_ZNK20QPlacePrivateDefault7ratingsEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK20QPlacePrivateDefault7ratingsEv'
    address = self.uglySide.call(ritual)
    from . import QPlaceRatings
    return QPlaceRatings._cuteOwning(address)

  def supplier(self) -> QPlaceSupplier:
    """
    Calls Qt's 'QPlaceSupplier QPlacePrivateDefault::supplier() const'.

    Qt's own words: https://doc.qt.io/qt-6/qplaceprivatedefault.html#supplier

    Returns
    -------

    QPlaceSupplier
      A new cute QPlaceSupplier around the copy Qt gave back. Python owns it.
    """
    #  QPlaceSupplier QPlacePrivateDefault::supplier() const
    ritual = 'ritual_ZNK20QPlacePrivateDefault8supplierEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK20QPlacePrivateDefault8supplierEv'
    address = self.uglySide.call(ritual)
    from . import QPlaceSupplier
    return QPlaceSupplier._cuteOwning(address)

  def name(self) -> str:
    """
    Calls Qt's 'QString QPlacePrivateDefault::name() const'.

    Qt's own words: https://doc.qt.io/qt-6/qplaceprivatedefault.html#name

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QPlacePrivateDefault::name() const
    ritual = 'ritual_ZNK20QPlacePrivateDefault4nameEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK20QPlacePrivateDefault4nameEv'
    return self.uglySide.call(ritual)

  def placeId(self) -> str:
    """
    Calls Qt's 'QString QPlacePrivateDefault::placeId() const'.

    Qt's own words: https://doc.qt.io/qt-6/qplaceprivatedefault.html#placeId

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QPlacePrivateDefault::placeId() const
    ritual = 'ritual_ZNK20QPlacePrivateDefault7placeIdEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK20QPlacePrivateDefault7placeIdEv'
    return self.uglySide.call(ritual)

  def attribution(self) -> str:
    """
    Calls Qt's 'QString QPlacePrivateDefault::attribution() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplaceprivatedefault.html#attribution

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QPlacePrivateDefault::attribution() const
    ritual = 'ritual_ZNK20QPlacePrivateDefault11attributionEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK20QPlacePrivateDefault11attributionEv'
    return self.uglySide.call(ritual)

  def visibility(self) -> QLocation.Visibility:
    """
    Calls Qt's 'QLocation::Visibility QPlacePrivateDefault::visibility()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplaceprivatedefault.html#visibility

    Returns
    -------

    QLocation.Visibility
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QLocation.Visibility(number)' gives.
    """
    #  QLocation::Visibility QPlacePrivateDefault::visibility() const
    ritual = 'ritual_ZNK20QPlacePrivateDefault10visibilityEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK20QPlacePrivateDefault10visibilityEv'
    return QLocation.Visibility(self.uglySide.call(ritual))

  def icon(self) -> QPlaceIcon:
    """
    Calls Qt's 'QPlaceIcon QPlacePrivateDefault::icon() const'.

    Qt's own words: https://doc.qt.io/qt-6/qplaceprivatedefault.html#icon

    Returns
    -------

    QPlaceIcon
      A new cute QPlaceIcon around the copy Qt gave back. Python owns it.
    """
    #  QPlaceIcon QPlacePrivateDefault::icon() const
    ritual = 'ritual_ZNK20QPlacePrivateDefault4iconEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK20QPlacePrivateDefault4iconEv'
    address = self.uglySide.call(ritual)
    from . import QPlaceIcon
    return QPlaceIcon._cuteOwning(address)

  def detailsFetched(self) -> bool:
    """
    Calls Qt's 'bool QPlacePrivateDefault::detailsFetched() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplaceprivatedefault.html#detailsFetched
    """
    #  bool QPlacePrivateDefault::detailsFetched() const
    ritual = 'ritual_ZNK20QPlacePrivateDefault14detailsFetchedEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK20QPlacePrivateDefault14detailsFetchedEv'
    return self.uglySide.call(ritual)

  def extendedAttributes(self) -> QMap[str, QPlaceAttribute]:
    """
    Calls Qt's 'QMap<QString, QPlaceAttribute>
    QPlacePrivateDefault::extendedAttributes() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplaceprivatedefault.html#extendedAttributes

    Returns
    -------

    QMap[str, QPlaceAttribute]
      A new cute map around the copy Qt gave back. Python owns it.
    """
    #  QMap<QString, QPlaceAttribute>
    #      QPlacePrivateDefault::extendedAttributes() const
    address = self.uglySide.call(
        'ritual_ZNK20QPlacePrivateDefault18extendedAttributesEv',
    )
    from . import QPlaceAttribute
    return QMap[str, QPlaceAttribute]._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QList[QPlaceCategory])
  def setCategories(self, categories: QList[QPlaceCategory]) -> None:
    """
    Calls Qt's 'void QPlacePrivateDefault::setCategories(const
    QList<QPlaceCategory> &categories)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplaceprivatedefault.html#setCategories

    Parameters
    ----------

    categories : QList[QPlaceCategory]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QPlacePrivateDefault::setCategories(const QList<QPlaceCategory>
    #      &categories)
    self.uglySide.call(
        'ritual_ZN20QPlacePrivateDefault13setCategoriesERK5QListI14QPlaceCa'
        'tegoryE',
        self._valueOf(categories),
    )

  @overload(QGeoLocation)
  def setLocation(self, location: QGeoLocation) -> None:
    """
    Calls Qt's 'void QPlacePrivateDefault::setLocation(const QGeoLocation
    &location)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplaceprivatedefault.html#setLocation

    Parameters
    ----------

    location : QGeoLocation
      Passed on as a value: Qt reads the C++ QGeoLocation, which stays
      Python's own.
    """
    #  void QPlacePrivateDefault::setLocation(const QGeoLocation &location)
    ritual = 'ritual_ZN20QPlacePrivateDefault11setLocationERK12QGeoLocation'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20QPlacePrivateDefault11setLocationERK12QGeoLocatio'
          'n')
    self.uglySide.call(ritual, self._valueOf(location))

  @overload(QPlaceRatings)
  def setRatings(self, ratings: QPlaceRatings) -> None:
    """
    Calls Qt's 'void QPlacePrivateDefault::setRatings(const QPlaceRatings
    &ratings)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplaceprivatedefault.html#setRatings

    Parameters
    ----------

    ratings : QPlaceRatings
      Passed on as a value: Qt reads the C++ QPlaceRatings, which stays
      Python's own.
    """
    #  void QPlacePrivateDefault::setRatings(const QPlaceRatings &ratings)
    ritual = 'ritual_ZN20QPlacePrivateDefault10setRatingsERK13QPlaceRatings'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20QPlacePrivateDefault10setRatingsERK13QPlaceRating'
          's')
    self.uglySide.call(ritual, self._valueOf(ratings))

  @overload(QPlaceSupplier)
  def setSupplier(self, supplier: QPlaceSupplier) -> None:
    """
    Calls Qt's 'void QPlacePrivateDefault::setSupplier(const QPlaceSupplier
    &supplier)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplaceprivatedefault.html#setSupplier

    Parameters
    ----------

    supplier : QPlaceSupplier
      Passed on as a value: Qt reads the C++ QPlaceSupplier, which stays
      Python's own.
    """
    #  void QPlacePrivateDefault::setSupplier(const QPlaceSupplier &supplier)
    ritual = (
        'ritual_ZN20QPlacePrivateDefault11setSupplierERK14QPlaceSupplier')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20QPlacePrivateDefault11setSupplierERK14QPlaceSuppl'
          'ier')
    self.uglySide.call(ritual, self._valueOf(supplier))

  @overload(str)
  def setName(self, name: str) -> None:
    """
    Calls Qt's 'void QPlacePrivateDefault::setName(const QString &name)'.

    Qt's own words: https://doc.qt.io/qt-6/qplaceprivatedefault.html#setName

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QPlacePrivateDefault::setName(const QString &name)
    ritual = 'ritual_ZN20QPlacePrivateDefault7setNameERK7QString'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN20QPlacePrivateDefault7setNameERK7QString'
    self.uglySide.call(ritual, name)

  @overload(str)
  def setPlaceId(self, placeIdentifier: str) -> None:
    """
    Calls Qt's 'void QPlacePrivateDefault::setPlaceId(const QString
    &placeIdentifier)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplaceprivatedefault.html#setPlaceId

    Parameters
    ----------

    placeIdentifier : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QPlacePrivateDefault::setPlaceId(const QString &placeIdentifier)
    ritual = 'ritual_ZN20QPlacePrivateDefault10setPlaceIdERK7QString'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN20QPlacePrivateDefault10setPlaceIdERK7QString'
    self.uglySide.call(ritual, placeIdentifier)

  @overload(str)
  def setAttribution(self, attribution: str) -> None:
    """
    Calls Qt's 'void QPlacePrivateDefault::setAttribution(const QString
    &attribution)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplaceprivatedefault.html#setAttribution

    Parameters
    ----------

    attribution : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QPlacePrivateDefault::setAttribution(const QString &attribution)
    ritual = 'ritual_ZN20QPlacePrivateDefault14setAttributionERK7QString'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20QPlacePrivateDefault14setAttributionERK7QString')
    self.uglySide.call(ritual, attribution)

  @overload(QLocation.Visibility)
  def setVisibility(self, visibility: QLocation.Visibility) -> None:
    """
    Calls Qt's 'void
    QPlacePrivateDefault::setVisibility(QLocation::Visibility visibility)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplaceprivatedefault.html#setVisibility

    Parameters
    ----------

    visibility : QLocation.Visibility
      Passed on as its number.
    """
    #  void QPlacePrivateDefault::setVisibility(QLocation::Visibility
    #      visibility)
    ritual = (
        'ritual_ZN20QPlacePrivateDefault13setVisibilityEN9QLocation10Visibi'
        'lityE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20QPlacePrivateDefault13setVisibilityEN9QLocation10'
          'VisibilityE')
    self.uglySide.call(ritual, visibility.value)

  @overload(QPlaceIcon)
  def setIcon(self, icon: QPlaceIcon) -> None:
    """
    Calls Qt's 'void QPlacePrivateDefault::setIcon(const QPlaceIcon &icon)'.

    Qt's own words: https://doc.qt.io/qt-6/qplaceprivatedefault.html#setIcon

    Parameters
    ----------

    icon : QPlaceIcon
      Passed on as a value: Qt reads the C++ QPlaceIcon, which stays Python's
      own.
    """
    #  void QPlacePrivateDefault::setIcon(const QPlaceIcon &icon)
    ritual = 'ritual_ZN20QPlacePrivateDefault7setIconERK10QPlaceIcon'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN20QPlacePrivateDefault7setIconERK10QPlaceIcon'
    self.uglySide.call(ritual, self._valueOf(icon))

  @overload(bool)
  def setDetailsFetched(self, fetched: bool) -> None:
    """
    Calls Qt's 'void QPlacePrivateDefault::setDetailsFetched(bool fetched)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplaceprivatedefault.html#setDetailsFetched

    Parameters
    ----------

    fetched : bool
      Passed on as it is.
    """
    #  void QPlacePrivateDefault::setDetailsFetched(bool fetched)
    ritual = 'ritual_ZN20QPlacePrivateDefault17setDetailsFetchedEb'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN20QPlacePrivateDefault17setDetailsFetchedEb'
    self.uglySide.call(ritual, fetched)

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
    Notes what was given, for Qt's
    'QPlacePrivateDefault::QPlacePrivateDefault()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qplaceprivatedefault.html#QPlacePrivateDefault
    """
    #  QPlacePrivateDefault::QPlacePrivateDefault()
    self._noteCreation(QPlacePrivateDefault, lambda: Rituals.call(
        'ritual_ZN20QPlacePrivateDefaultC1Ev',
    ))

  @overload(THIS)
  def __init__(self, other: QPlacePrivateDefault) -> None:
    """
    Notes what was given, for Qt's
    'QPlacePrivateDefault::QPlacePrivateDefault(const QPlacePrivateDefault
    &other)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qplaceprivatedefault.html#QPlacePrivateDefault

    Parameters
    ----------

    other : QPlacePrivateDefault
      Passed on as a value: Qt reads the C++ QPlacePrivateDefault, which
      stays Python's own.
    """
    #  QPlacePrivateDefault::QPlacePrivateDefault(const QPlacePrivateDefault
    #      &other)
    self._noteCreation(QPlacePrivateDefault, lambda: Rituals.call(
        'ritual_ZN20QPlacePrivateDefaultC1ERKS_', self._valueOf(other),
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

  def clone(self) -> Optional[QPlacePrivate]:
    """
    Calls Qt's 'QPlacePrivate *QPlacePrivateDefault::clone()'.

    Qt's own words: https://doc.qt.io/qt-6/qplaceprivatedefault.html#clone

    Returns
    -------

    Optional[QPlacePrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPlacePrivate *QPlacePrivateDefault::clone()
    ritual = 'ritual_ZN20QPlacePrivateDefault5cloneEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN20QPlacePrivateDefault5cloneEv'
    address = self.uglySide.call(ritual)
    return QPlacePrivate._cuteAt(address)
