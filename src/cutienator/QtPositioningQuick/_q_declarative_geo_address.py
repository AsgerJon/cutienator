"""
QDeclarativeGeoAddress binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtPositioningQuick/6.12.0/QtPositioningQuick/private/qdeclarativegeoaddress_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QDeclarativeGeoAddress to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from ..QtPositioning import QGeoAddress
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QGeoAddress = WAIT['QGeoAddress']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QDeclarativeGeoAddress(QObject):
  """
  The cute side of Qt's QDeclarativeGeoAddress: a plain Python object
  standing in front of one C++ QDeclarativeGeoAddress.

  It is built on the cute 'QObject', as Qt's QDeclarativeGeoAddress is built
  on Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QDeclarativeGeoAddress that has a ritual and that
  Python can call so far, 36 names in all: 'metaObject', 'tr', 'address',
  'setAddress', 'text', 'setText', 'country', 'setCountry', 'countryCode',
  'setCountryCode', 'state', 'setState', 'county', 'setCounty', 'city',
  'setCity', 'district', 'setDistrict', 'street', 'setStreet',
  'streetNumber', 'setStreetNumber', 'postalCode', 'setPostalCode',
  'isTextGenerated', 'textChanged', 'countryChanged', 'countryCodeChanged',
  'stateChanged', 'countyChanged', 'cityChanged', 'districtChanged',
  'streetChanged', 'streetNumberChanged', 'postalCodeChanged',
  'isTextGeneratedChanged'. It can be made from Python, in 2 ways; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QDeclarativeGeoAddress::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QDeclarativeGeoAddress::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.

  What has no ritual
  ------------------

  2 of the 42 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QDeclarativeGeoAddress is created at the first use, not by
    'QDeclarativeGeoAddress(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QDeclarativeGeoAddress.
  - Qt tells when it has removed the C++ QDeclarativeGeoAddress. Every call
    on the cute object, and every use of it as an argument, then raises
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
    Calls Qt's 'QString QDeclarativeGeoAddress::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qdeclarativegeoaddress.html#tr

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
    #  QString QDeclarativeGeoAddress::tr(const char *s, const char *c, int
    #      n)
    return Rituals.call(
        'ritual_ZN22QDeclarativeGeoAddress2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QDeclarativeGeoAddress'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QDeclarativeGeoAddress::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeoaddress.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QDeclarativeGeoAddress::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK22QDeclarativeGeoAddress10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def address(self) -> QGeoAddress:
    """
    Calls Qt's 'QGeoAddress QDeclarativeGeoAddress::address() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeoaddress.html#address

    Returns
    -------

    QGeoAddress
      A new cute QGeoAddress around the copy Qt gave back. Python owns it.
    """
    #  QGeoAddress QDeclarativeGeoAddress::address() const
    address = self.uglySide.call(
        'ritual_ZNK22QDeclarativeGeoAddress7addressEv',
    )
    from ..QtPositioning import QGeoAddress
    return QGeoAddress._cuteOwning(address)

  def text(self) -> str:
    """
    Calls Qt's 'QString QDeclarativeGeoAddress::text() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdeclarativegeoaddress.html#text

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QDeclarativeGeoAddress::text() const
    return self.uglySide.call('ritual_ZNK22QDeclarativeGeoAddress4textEv')

  def country(self) -> str:
    """
    Calls Qt's 'QString QDeclarativeGeoAddress::country() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeoaddress.html#country

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QDeclarativeGeoAddress::country() const
    return self.uglySide.call('ritual_ZNK22QDeclarativeGeoAddress7countryEv')

  def countryCode(self) -> str:
    """
    Calls Qt's 'QString QDeclarativeGeoAddress::countryCode() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeoaddress.html#countryCode

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QDeclarativeGeoAddress::countryCode() const
    return self.uglySide.call(
        'ritual_ZNK22QDeclarativeGeoAddress11countryCodeEv',
    )

  def state(self) -> str:
    """
    Calls Qt's 'QString QDeclarativeGeoAddress::state() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdeclarativegeoaddress.html#state

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QDeclarativeGeoAddress::state() const
    return self.uglySide.call('ritual_ZNK22QDeclarativeGeoAddress5stateEv')

  def county(self) -> str:
    """
    Calls Qt's 'QString QDeclarativeGeoAddress::county() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdeclarativegeoaddress.html#county

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QDeclarativeGeoAddress::county() const
    return self.uglySide.call('ritual_ZNK22QDeclarativeGeoAddress6countyEv')

  def city(self) -> str:
    """
    Calls Qt's 'QString QDeclarativeGeoAddress::city() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdeclarativegeoaddress.html#city

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QDeclarativeGeoAddress::city() const
    return self.uglySide.call('ritual_ZNK22QDeclarativeGeoAddress4cityEv')

  def district(self) -> str:
    """
    Calls Qt's 'QString QDeclarativeGeoAddress::district() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeoaddress.html#district

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QDeclarativeGeoAddress::district() const
    return self.uglySide.call(
        'ritual_ZNK22QDeclarativeGeoAddress8districtEv',
    )

  def street(self) -> str:
    """
    Calls Qt's 'QString QDeclarativeGeoAddress::street() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdeclarativegeoaddress.html#street

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QDeclarativeGeoAddress::street() const
    return self.uglySide.call('ritual_ZNK22QDeclarativeGeoAddress6streetEv')

  def streetNumber(self) -> str:
    """
    Calls Qt's 'QString QDeclarativeGeoAddress::streetNumber() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeoaddress.html#streetNumber

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QDeclarativeGeoAddress::streetNumber() const
    return self.uglySide.call(
        'ritual_ZNK22QDeclarativeGeoAddress12streetNumberEv',
    )

  def postalCode(self) -> str:
    """
    Calls Qt's 'QString QDeclarativeGeoAddress::postalCode() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeoaddress.html#postalCode

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QDeclarativeGeoAddress::postalCode() const
    return self.uglySide.call(
        'ritual_ZNK22QDeclarativeGeoAddress10postalCodeEv',
    )

  def isTextGenerated(self) -> bool:
    """
    Calls Qt's 'bool QDeclarativeGeoAddress::isTextGenerated() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeoaddress.html#isTextGenerated
    """
    #  bool QDeclarativeGeoAddress::isTextGenerated() const
    return self.uglySide.call(
        'ritual_ZNK22QDeclarativeGeoAddress15isTextGeneratedEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QGeoAddress)
  def setAddress(self, address: QGeoAddress) -> None:
    """
    Calls Qt's 'void QDeclarativeGeoAddress::setAddress(const QGeoAddress
    &address)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeoaddress.html#setAddress

    Parameters
    ----------

    address : QGeoAddress
      Passed on as a value: Qt reads the C++ QGeoAddress, which stays
      Python's own.
    """
    #  void QDeclarativeGeoAddress::setAddress(const QGeoAddress &address)
    self.uglySide.call(
        'ritual_ZN22QDeclarativeGeoAddress10setAddressERK11QGeoAddress',
        self._valueOf(address),
    )

  @overload(str)
  def setText(self, address: str) -> None:
    """
    Calls Qt's 'void QDeclarativeGeoAddress::setText(const QString
    &address)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeoaddress.html#setText

    Parameters
    ----------

    address : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QDeclarativeGeoAddress::setText(const QString &address)
    self.uglySide.call(
        'ritual_ZN22QDeclarativeGeoAddress7setTextERK7QString', address,
    )

  @overload(str)
  def setCountry(self, country: str) -> None:
    """
    Calls Qt's 'void QDeclarativeGeoAddress::setCountry(const QString
    &country)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeoaddress.html#setCountry

    Parameters
    ----------

    country : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QDeclarativeGeoAddress::setCountry(const QString &country)
    self.uglySide.call(
        'ritual_ZN22QDeclarativeGeoAddress10setCountryERK7QString', country,
    )

  @overload(str)
  def setCountryCode(self, countryCode: str) -> None:
    """
    Calls Qt's 'void QDeclarativeGeoAddress::setCountryCode(const QString
    &countryCode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeoaddress.html#setCountryCode

    Parameters
    ----------

    countryCode : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QDeclarativeGeoAddress::setCountryCode(const QString
    #      &countryCode)
    self.uglySide.call(
        'ritual_ZN22QDeclarativeGeoAddress14setCountryCodeERK7QString',
        countryCode,
    )

  @overload(str)
  def setState(self, state: str) -> None:
    """
    Calls Qt's 'void QDeclarativeGeoAddress::setState(const QString &state)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeoaddress.html#setState

    Parameters
    ----------

    state : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QDeclarativeGeoAddress::setState(const QString &state)
    self.uglySide.call(
        'ritual_ZN22QDeclarativeGeoAddress8setStateERK7QString', state,
    )

  @overload(str)
  def setCounty(self, county: str) -> None:
    """
    Calls Qt's 'void QDeclarativeGeoAddress::setCounty(const QString
    &county)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeoaddress.html#setCounty

    Parameters
    ----------

    county : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QDeclarativeGeoAddress::setCounty(const QString &county)
    self.uglySide.call(
        'ritual_ZN22QDeclarativeGeoAddress9setCountyERK7QString', county,
    )

  @overload(str)
  def setCity(self, city: str) -> None:
    """
    Calls Qt's 'void QDeclarativeGeoAddress::setCity(const QString &city)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeoaddress.html#setCity

    Parameters
    ----------

    city : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QDeclarativeGeoAddress::setCity(const QString &city)
    self.uglySide.call(
        'ritual_ZN22QDeclarativeGeoAddress7setCityERK7QString', city,
    )

  @overload(str)
  def setDistrict(self, district: str) -> None:
    """
    Calls Qt's 'void QDeclarativeGeoAddress::setDistrict(const QString
    &district)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeoaddress.html#setDistrict

    Parameters
    ----------

    district : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QDeclarativeGeoAddress::setDistrict(const QString &district)
    self.uglySide.call(
        'ritual_ZN22QDeclarativeGeoAddress11setDistrictERK7QString',
        district,
    )

  @overload(str)
  def setStreet(self, street: str) -> None:
    """
    Calls Qt's 'void QDeclarativeGeoAddress::setStreet(const QString
    &street)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeoaddress.html#setStreet

    Parameters
    ----------

    street : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QDeclarativeGeoAddress::setStreet(const QString &street)
    self.uglySide.call(
        'ritual_ZN22QDeclarativeGeoAddress9setStreetERK7QString', street,
    )

  @overload(str)
  def setStreetNumber(self, streetNumber: str) -> None:
    """
    Calls Qt's 'void QDeclarativeGeoAddress::setStreetNumber(const QString
    &streetNumber)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeoaddress.html#setStreetNumber

    Parameters
    ----------

    streetNumber : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QDeclarativeGeoAddress::setStreetNumber(const QString
    #      &streetNumber)
    self.uglySide.call(
        'ritual_ZN22QDeclarativeGeoAddress15setStreetNumberERK7QString',
        streetNumber,
    )

  @overload(str)
  def setPostalCode(self, postalCode: str) -> None:
    """
    Calls Qt's 'void QDeclarativeGeoAddress::setPostalCode(const QString
    &postalCode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeoaddress.html#setPostalCode

    Parameters
    ----------

    postalCode : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QDeclarativeGeoAddress::setPostalCode(const QString &postalCode)
    self.uglySide.call(
        'ritual_ZN22QDeclarativeGeoAddress13setPostalCodeERK7QString',
        postalCode,
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
    'QDeclarativeGeoAddress::QDeclarativeGeoAddress(QObject *parent)', which
    is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeoaddress.html#QDeclarativeGeoAddress

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QDeclarativeGeoAddress::QDeclarativeGeoAddress(QObject *parent)
    self._noteCreation(QDeclarativeGeoAddress, lambda: Rituals.call(
        'ritual_ZN22QDeclarativeGeoAddressC1EP7QObject',
        self._addressOf(parent, 'QObject'),
    ))

  @overload(QGeoAddress)
  @overload(QGeoAddress, QObject)
  @overload(QGeoAddress, NoneType)
  def __init__(
      self,
      address: QGeoAddress,
      parent: Optional[QObject] = None,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QDeclarativeGeoAddress::QDeclarativeGeoAddress(const QGeoAddress
    &address, QObject *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeoaddress.html#QDeclarativeGeoAddress

    Parameters
    ----------

    address : QGeoAddress
      Passed on as a value: Qt reads the C++ QGeoAddress, which stays
      Python's own.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QDeclarativeGeoAddress::QDeclarativeGeoAddress(const QGeoAddress
    #      &address, QObject *parent)
    self._noteCreation(QDeclarativeGeoAddress, lambda: Rituals.call(
        'ritual_ZN22QDeclarativeGeoAddressC1ERK11QGeoAddressP7QObject',
        self._valueOf(address), self._addressOf(parent, 'QObject'),
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

  def textChanged(self) -> None:
    """
    Calls Qt's 'void QDeclarativeGeoAddress::textChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeoaddress.html#textChanged
    """
    #  void QDeclarativeGeoAddress::textChanged()
    self.uglySide.call('ritual_ZN22QDeclarativeGeoAddress11textChangedEv')

  def countryChanged(self) -> None:
    """
    Calls Qt's 'void QDeclarativeGeoAddress::countryChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeoaddress.html#countryChanged
    """
    #  void QDeclarativeGeoAddress::countryChanged()
    self.uglySide.call('ritual_ZN22QDeclarativeGeoAddress14countryChangedEv')

  def countryCodeChanged(self) -> None:
    """
    Calls Qt's 'void QDeclarativeGeoAddress::countryCodeChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeoaddress.html#countryCodeChanged
    """
    #  void QDeclarativeGeoAddress::countryCodeChanged()
    self.uglySide.call(
        'ritual_ZN22QDeclarativeGeoAddress18countryCodeChangedEv',
    )

  def stateChanged(self) -> None:
    """
    Calls Qt's 'void QDeclarativeGeoAddress::stateChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeoaddress.html#stateChanged
    """
    #  void QDeclarativeGeoAddress::stateChanged()
    self.uglySide.call('ritual_ZN22QDeclarativeGeoAddress12stateChangedEv')

  def countyChanged(self) -> None:
    """
    Calls Qt's 'void QDeclarativeGeoAddress::countyChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeoaddress.html#countyChanged
    """
    #  void QDeclarativeGeoAddress::countyChanged()
    self.uglySide.call('ritual_ZN22QDeclarativeGeoAddress13countyChangedEv')

  def cityChanged(self) -> None:
    """
    Calls Qt's 'void QDeclarativeGeoAddress::cityChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeoaddress.html#cityChanged
    """
    #  void QDeclarativeGeoAddress::cityChanged()
    self.uglySide.call('ritual_ZN22QDeclarativeGeoAddress11cityChangedEv')

  def districtChanged(self) -> None:
    """
    Calls Qt's 'void QDeclarativeGeoAddress::districtChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeoaddress.html#districtChanged
    """
    #  void QDeclarativeGeoAddress::districtChanged()
    self.uglySide.call(
        'ritual_ZN22QDeclarativeGeoAddress15districtChangedEv',
    )

  def streetChanged(self) -> None:
    """
    Calls Qt's 'void QDeclarativeGeoAddress::streetChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeoaddress.html#streetChanged
    """
    #  void QDeclarativeGeoAddress::streetChanged()
    self.uglySide.call('ritual_ZN22QDeclarativeGeoAddress13streetChangedEv')

  def streetNumberChanged(self) -> None:
    """
    Calls Qt's 'void QDeclarativeGeoAddress::streetNumberChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeoaddress.html#streetNumberChanged
    """
    #  void QDeclarativeGeoAddress::streetNumberChanged()
    self.uglySide.call(
        'ritual_ZN22QDeclarativeGeoAddress19streetNumberChangedEv',
    )

  def postalCodeChanged(self) -> None:
    """
    Calls Qt's 'void QDeclarativeGeoAddress::postalCodeChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeoaddress.html#postalCodeChanged
    """
    #  void QDeclarativeGeoAddress::postalCodeChanged()
    self.uglySide.call(
        'ritual_ZN22QDeclarativeGeoAddress17postalCodeChangedEv',
    )

  def isTextGeneratedChanged(self) -> None:
    """
    Calls Qt's 'void QDeclarativeGeoAddress::isTextGeneratedChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeoaddress.html#isTextGeneratedChanged
    """
    #  void QDeclarativeGeoAddress::isTextGeneratedChanged()
    self.uglySide.call(
        'ritual_ZN22QDeclarativeGeoAddress22isTextGeneratedChangedEv',
    )
