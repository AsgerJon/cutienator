"""
QGeoAddress binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtPositioning/qgeoaddress.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class QGeoAddress(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QGeoAddress: a plain Python object standing in front
  of one C++ QGeoAddress.

  C++ hands a QGeoAddress around as a copy, so every C++ QGeoAddress behind a
  cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QGeoAddress that has a ritual and that Python can
  call so far, 26 names in all: '__eq__', '__ne__', 'text', 'setText',
  'country', 'setCountry', 'countryCode', 'setCountryCode', 'state',
  'setState', 'county', 'setCounty', 'city', 'setCity', 'district',
  'setDistrict', 'postalCode', 'setPostalCode', 'street', 'setStreet',
  'streetNumber', 'setStreetNumber', 'isEmpty', 'clear', 'isTextGenerated',
  'equals'. It can be made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QGeoAddress::QGeoAddress(QGeoAddress &&other)': takes a type Python
    has no way to hand over yet.
  - Qt's 'QGeoAddress::~QGeoAddress()': the destructor: Python removes its
    C++ QGeoAddress by it, and has no other use for it.
  - Qt's 'QGeoAddress &QGeoAddress::operator=(const QGeoAddress &other)':
    assignment: Python binds a name and has no operator for it.
  - Qt's 'QGeoAddress &QGeoAddress::operator=(QGeoAddress &&other)':
    assignment: Python binds a name and has no operator for it.
  - Qt's 'void QGeoAddress::swap(QGeoAddress &other)': takes a type Python
    has no way to hand over yet.

  What to expect
  --------------

  - The C++ QGeoAddress is created at the first use, not by
    'QGeoAddress(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QGeoAddress back gives a copy the ritual made for
    Python, in a new cute QGeoAddress.
  - Each name of Qt's QGeoAddress that has no cute function yet, 'swap',
    holds a function that raises 'NotImplementedError', and its docstring
    says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(THIS, THIS)
  def equals(lhs: QGeoAddress, rhs: QGeoAddress) -> bool:
    """
    Calls Qt's 'bool QGeoAddress::equals(const QGeoAddress &lhs, const
    QGeoAddress &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qgeoaddress.html#equals

    Parameters
    ----------

    lhs : QGeoAddress
      Passed on as a value: Qt reads the C++ QGeoAddress, which stays
      Python's own.

    rhs : QGeoAddress
      Passed on as a value: Qt reads the C++ QGeoAddress, which stays
      Python's own.
    """
    #  bool QGeoAddress::equals(const QGeoAddress &lhs, const QGeoAddress
    #      &rhs)
    return Rituals.call(
        'ritual_ZN11QGeoAddress6equalsERKS_S1_',
        CuteMixin._valueOf(lhs), CuteMixin._valueOf(rhs),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QGeoAddress'

  #  Qt's '~QGeoAddress()'. Naming it makes this a value class: Python owns
  #  every C++ QGeoAddress behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN11QGeoAddressD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def text(self) -> str:
    """
    Calls Qt's 'QString QGeoAddress::text() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeoaddress.html#text

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QGeoAddress::text() const
    return self.uglySide.call('ritual_ZNK11QGeoAddress4textEv')

  def country(self) -> str:
    """
    Calls Qt's 'QString QGeoAddress::country() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeoaddress.html#country

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QGeoAddress::country() const
    return self.uglySide.call('ritual_ZNK11QGeoAddress7countryEv')

  def countryCode(self) -> str:
    """
    Calls Qt's 'QString QGeoAddress::countryCode() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeoaddress.html#countryCode

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QGeoAddress::countryCode() const
    return self.uglySide.call('ritual_ZNK11QGeoAddress11countryCodeEv')

  def state(self) -> str:
    """
    Calls Qt's 'QString QGeoAddress::state() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeoaddress.html#state

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QGeoAddress::state() const
    return self.uglySide.call('ritual_ZNK11QGeoAddress5stateEv')

  def county(self) -> str:
    """
    Calls Qt's 'QString QGeoAddress::county() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeoaddress.html#county

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QGeoAddress::county() const
    return self.uglySide.call('ritual_ZNK11QGeoAddress6countyEv')

  def city(self) -> str:
    """
    Calls Qt's 'QString QGeoAddress::city() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeoaddress.html#city

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QGeoAddress::city() const
    return self.uglySide.call('ritual_ZNK11QGeoAddress4cityEv')

  def district(self) -> str:
    """
    Calls Qt's 'QString QGeoAddress::district() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeoaddress.html#district

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QGeoAddress::district() const
    return self.uglySide.call('ritual_ZNK11QGeoAddress8districtEv')

  def postalCode(self) -> str:
    """
    Calls Qt's 'QString QGeoAddress::postalCode() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeoaddress.html#postalCode

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QGeoAddress::postalCode() const
    return self.uglySide.call('ritual_ZNK11QGeoAddress10postalCodeEv')

  def street(self) -> str:
    """
    Calls Qt's 'QString QGeoAddress::street() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeoaddress.html#street

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QGeoAddress::street() const
    return self.uglySide.call('ritual_ZNK11QGeoAddress6streetEv')

  def streetNumber(self) -> str:
    """
    Calls Qt's 'QString QGeoAddress::streetNumber() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeoaddress.html#streetNumber

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QGeoAddress::streetNumber() const
    return self.uglySide.call('ritual_ZNK11QGeoAddress12streetNumberEv')

  def isEmpty(self) -> bool:
    """
    Calls Qt's 'bool QGeoAddress::isEmpty() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeoaddress.html#isEmpty
    """
    #  bool QGeoAddress::isEmpty() const
    return self.uglySide.call('ritual_ZNK11QGeoAddress7isEmptyEv')

  def isTextGenerated(self) -> bool:
    """
    Calls Qt's 'bool QGeoAddress::isTextGenerated() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeoaddress.html#isTextGenerated
    """
    #  bool QGeoAddress::isTextGenerated() const
    return self.uglySide.call('ritual_ZNK11QGeoAddress15isTextGeneratedEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setText(self, text: str) -> None:
    """
    Calls Qt's 'void QGeoAddress::setText(const QString &text)'.

    Qt's own words: https://doc.qt.io/qt-6/qgeoaddress.html#setText

    Parameters
    ----------

    text : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QGeoAddress::setText(const QString &text)
    self.uglySide.call('ritual_ZN11QGeoAddress7setTextERK7QString', text)

  @overload(str)
  def setCountry(self, country: str) -> None:
    """
    Calls Qt's 'void QGeoAddress::setCountry(const QString &country)'.

    Qt's own words: https://doc.qt.io/qt-6/qgeoaddress.html#setCountry

    Parameters
    ----------

    country : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QGeoAddress::setCountry(const QString &country)
    self.uglySide.call(
        'ritual_ZN11QGeoAddress10setCountryERK7QString', country,
    )

  @overload(str)
  def setCountryCode(self, countryCode: str) -> None:
    """
    Calls Qt's 'void QGeoAddress::setCountryCode(const QString
    &countryCode)'.

    Qt's own words: https://doc.qt.io/qt-6/qgeoaddress.html#setCountryCode

    Parameters
    ----------

    countryCode : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QGeoAddress::setCountryCode(const QString &countryCode)
    self.uglySide.call(
        'ritual_ZN11QGeoAddress14setCountryCodeERK7QString', countryCode,
    )

  @overload(str)
  def setState(self, state: str) -> None:
    """
    Calls Qt's 'void QGeoAddress::setState(const QString &state)'.

    Qt's own words: https://doc.qt.io/qt-6/qgeoaddress.html#setState

    Parameters
    ----------

    state : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QGeoAddress::setState(const QString &state)
    self.uglySide.call('ritual_ZN11QGeoAddress8setStateERK7QString', state)

  @overload(str)
  def setCounty(self, county: str) -> None:
    """
    Calls Qt's 'void QGeoAddress::setCounty(const QString &county)'.

    Qt's own words: https://doc.qt.io/qt-6/qgeoaddress.html#setCounty

    Parameters
    ----------

    county : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QGeoAddress::setCounty(const QString &county)
    self.uglySide.call('ritual_ZN11QGeoAddress9setCountyERK7QString', county)

  @overload(str)
  def setCity(self, city: str) -> None:
    """
    Calls Qt's 'void QGeoAddress::setCity(const QString &city)'.

    Qt's own words: https://doc.qt.io/qt-6/qgeoaddress.html#setCity

    Parameters
    ----------

    city : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QGeoAddress::setCity(const QString &city)
    self.uglySide.call('ritual_ZN11QGeoAddress7setCityERK7QString', city)

  @overload(str)
  def setDistrict(self, district: str) -> None:
    """
    Calls Qt's 'void QGeoAddress::setDistrict(const QString &district)'.

    Qt's own words: https://doc.qt.io/qt-6/qgeoaddress.html#setDistrict

    Parameters
    ----------

    district : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QGeoAddress::setDistrict(const QString &district)
    self.uglySide.call(
        'ritual_ZN11QGeoAddress11setDistrictERK7QString', district,
    )

  @overload(str)
  def setPostalCode(self, postalCode: str) -> None:
    """
    Calls Qt's 'void QGeoAddress::setPostalCode(const QString &postalCode)'.

    Qt's own words: https://doc.qt.io/qt-6/qgeoaddress.html#setPostalCode

    Parameters
    ----------

    postalCode : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QGeoAddress::setPostalCode(const QString &postalCode)
    self.uglySide.call(
        'ritual_ZN11QGeoAddress13setPostalCodeERK7QString', postalCode,
    )

  @overload(str)
  def setStreet(self, street: str) -> None:
    """
    Calls Qt's 'void QGeoAddress::setStreet(const QString &street)'.

    Qt's own words: https://doc.qt.io/qt-6/qgeoaddress.html#setStreet

    Parameters
    ----------

    street : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QGeoAddress::setStreet(const QString &street)
    self.uglySide.call('ritual_ZN11QGeoAddress9setStreetERK7QString', street)

  @overload(str)
  def setStreetNumber(self, streetNumber: str) -> None:
    """
    Calls Qt's 'void QGeoAddress::setStreetNumber(const QString
    &streetNumber)'.

    Qt's own words: https://doc.qt.io/qt-6/qgeoaddress.html#setStreetNumber

    Parameters
    ----------

    streetNumber : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QGeoAddress::setStreetNumber(const QString &streetNumber)
    self.uglySide.call(
        'ritual_ZN11QGeoAddress15setStreetNumberERK7QString', streetNumber,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __eq__(self, rhs: QGeoAddress) -> bool:
    """
    Calls Qt's 'bool operator==(const QGeoAddress &lhs, const QGeoAddress
    &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qgeoaddress.html#operator==

    Parameters
    ----------

    rhs : QGeoAddress
      Passed on as a value: Qt reads the C++ QGeoAddress, which stays
      Python's own.
    """
    #  bool operator==(const QGeoAddress &lhs, const QGeoAddress &rhs)
    return Rituals.call(
        'ritual_ZeqRK11QGeoAddressS1_',
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
  def __ne__(self, rhs: QGeoAddress) -> bool:
    """
    Calls Qt's 'bool operator!=(const QGeoAddress &lhs, const QGeoAddress
    &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qgeoaddress.html#operator!=

    Parameters
    ----------

    rhs : QGeoAddress
      Passed on as a value: Qt reads the C++ QGeoAddress, which stays
      Python's own.
    """
    #  bool operator!=(const QGeoAddress &lhs, const QGeoAddress &rhs)
    return Rituals.call(
        'ritual_ZneRK11QGeoAddressS1_',
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
    Notes what was given, for Qt's 'QGeoAddress::QGeoAddress()', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qgeoaddress.html#QGeoAddress
    """
    #  QGeoAddress::QGeoAddress()
    self._noteCreation(QGeoAddress, lambda: Rituals.call(
        'ritual_ZN11QGeoAddressC1Ev',
    ))

  @overload(THIS)
  def __init__(self, other: QGeoAddress) -> None:
    """
    Notes what was given, for Qt's 'QGeoAddress::QGeoAddress(const
    QGeoAddress &other)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qgeoaddress.html#QGeoAddress

    Parameters
    ----------

    other : QGeoAddress
      Passed on as a value: Qt reads the C++ QGeoAddress, which stays
      Python's own.
    """
    #  QGeoAddress::QGeoAddress(const QGeoAddress &other)
    self._noteCreation(QGeoAddress, lambda: Rituals.call(
        'ritual_ZN11QGeoAddressC1ERKS_', self._valueOf(other),
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

  def clear(self) -> None:
    """
    Calls Qt's 'void QGeoAddress::clear()'.

    Qt's own words: https://doc.qt.io/qt-6/qgeoaddress.html#clear
    """
    #  void QGeoAddress::clear()
    self.uglySide.call('ritual_ZN11QGeoAddress5clearEv')

  @staticmethod
  def swap(*__, **_) -> Never:
    """
    Qt's 'void QGeoAddress::swap(QGeoAddress &other)': takes a type Python
    has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QGeoAddress.swap' has no cute function yet. Qt's 'void "
        "QGeoAddress::swap(QGeoAddress &other)': takes a type Python has no "
        "way to hand over yet.")
