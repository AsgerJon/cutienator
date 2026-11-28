"""
QPlacePrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtLocation/6.12.0/QtLocation/private/qplace_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QPlacePrivate to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..QtCore import QList, QMap, QSharedData
from . import QLocation

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

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


class QPlacePrivate(QSharedData):
  """
  The cute side of Qt's QPlacePrivate: a plain Python object standing in
  front of one C++ QPlacePrivate.

  It is built on the cute 'QSharedData', as Qt's QPlacePrivate is built on
  Qt's QSharedData, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QPlacePrivate that has a ritual and that Python can
  call so far, 24 names in all: 'clone', 'isEmpty', 'categories',
  'setCategories', 'location', 'setLocation', 'ratings', 'setRatings',
  'supplier', 'setSupplier', 'name', 'setName', 'placeId', 'setPlaceId',
  'attribution', 'setAttribution', 'visibility', 'setVisibility', 'icon',
  'setIcon', 'detailsFetched', 'setDetailsFetched', 'extendedAttributes',
  'extendedAttribute'. None can be made from Python: one comes out of a
  function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QPlacePrivate::~QPlacePrivate()': the destructor: Python never
    removes a C++ QPlacePrivate.
  - Qt's 'bool QPlacePrivate::operator==(const QPlacePrivate &other) const':
    takes a type Python has no way to hand over yet.
  - Qt's 'QMap<QString, QPlaceAttribute>
    &QPlacePrivate::extendedAttributes()': gives a type Python has no way to
    take yet.
  - Qt's 'QMap<QString, QList<QPlaceContactDetail>> QPlacePrivate::contacts()
    const': gives a type Python has no way to take yet.
  - Qt's 'QMap<QString, QList<QPlaceContactDetail>>
    &QPlacePrivate::contacts()': gives a type Python has no way to take yet.

  What has no ritual
  ------------------

  2 of the 31 functions Qt declares: 2 the class is abstract, so C++ cannot
  make one, and the C++ class of ours does not fill in every function it
  leaves open.

  What to expect
  --------------

  - The C++ QPlacePrivate is created at the first use, not by
    'QPlacePrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QPlacePrivate.
  - Each name of Qt's QPlacePrivate that has no cute function yet,
    '__init__', 'contacts', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QPlacePrivate'

  #  A C++ QPlacePrivate Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QPlacePrivate'

  #  The functions Qt calls itself that QPlacePrivate is the first to declare
  #  and that cannot be handed to Python yet, each as Qt declares it. A class
  #  of a program that writes one of them anew is refused, since Qt would
  #  never call what it wrote; see 'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'categories': (
          'QList<QPlaceCategory> QPlacePrivate::categories() const',
      ),
      'setCategories': (
          'void QPlacePrivate::setCategories(const QList<QPlaceCategory> &)',
      ),
      'extendedAttributes': (
          'QMap<QString, QPlaceAttribute> '
          'QPlacePrivate::extendedAttributes() const',
          'QMap<QString, QPlaceAttribute> '
          '&QPlacePrivate::extendedAttributes()',
      ),
      'contacts': (
          'QMap<QString, QList<QPlaceContactDetail>> '
          'QPlacePrivate::contacts() const',
          'QMap<QString, QList<QPlaceContactDetail>> '
          '&QPlacePrivate::contacts()',
      ),
  }

  #  The functions Qt calls itself that QPlacePrivate is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'clone': (
          ('_ZN13QPlacePrivate5cloneEv',
           ('address', 'address', 'QtLocation:QPlacePrivate'),
           ()),
      ),
      'isEmpty': (
          ('_ZNK13QPlacePrivate7isEmptyEv',
           ('bool', 'number', ''),
           ()),
      ),
      'location': (
          ('_ZNK13QPlacePrivate8locationEv',
           ('address', 'value', 'QtPositioning:QGeoLocation'),
           ()),
      ),
      'setLocation': (
          ('_ZN13QPlacePrivate11setLocationERK12QGeoLocation',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtPositioning:QGeoLocation'),
           )),
      ),
      'ratings': (
          ('_ZNK13QPlacePrivate7ratingsEv',
           ('address', 'value', 'QtLocation:QPlaceRatings'),
           ()),
      ),
      'setRatings': (
          ('_ZN13QPlacePrivate10setRatingsERK13QPlaceRatings',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtLocation:QPlaceRatings'),
           )),
      ),
      'supplier': (
          ('_ZNK13QPlacePrivate8supplierEv',
           ('address', 'value', 'QtLocation:QPlaceSupplier'),
           ()),
      ),
      'setSupplier': (
          ('_ZN13QPlacePrivate11setSupplierERK14QPlaceSupplier',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtLocation:QPlaceSupplier'),
           )),
      ),
      'name': (
          ('_ZNK13QPlacePrivate4nameEv',
           ('address', 'text', ''),
           ()),
      ),
      'setName': (
          ('_ZN13QPlacePrivate7setNameERK7QString',
           ('nothing', 'nothing', ''),
           (
               ('address', 'text', ''),
           )),
      ),
      'placeId': (
          ('_ZNK13QPlacePrivate7placeIdEv',
           ('address', 'text', ''),
           ()),
      ),
      'setPlaceId': (
          ('_ZN13QPlacePrivate10setPlaceIdERK7QString',
           ('nothing', 'nothing', ''),
           (
               ('address', 'text', ''),
           )),
      ),
      'attribution': (
          ('_ZNK13QPlacePrivate11attributionEv',
           ('address', 'text', ''),
           ()),
      ),
      'setAttribution': (
          ('_ZN13QPlacePrivate14setAttributionERK7QString',
           ('nothing', 'nothing', ''),
           (
               ('address', 'text', ''),
           )),
      ),
      'visibility': (
          ('_ZNK13QPlacePrivate10visibilityEv',
           ('int', 'enum', 'QtLocation:QLocation.Visibility'),
           ()),
      ),
      'setVisibility': (
          ('_ZN13QPlacePrivate13setVisibilityEN9QLocation10VisibilityE',
           ('nothing', 'nothing', ''),
           (
               ('int', 'enum', 'QtLocation:QLocation.Visibility'),
           )),
      ),
      'icon': (
          ('_ZNK13QPlacePrivate4iconEv',
           ('address', 'value', 'QtLocation:QPlaceIcon'),
           ()),
      ),
      'setIcon': (
          ('_ZN13QPlacePrivate7setIconERK10QPlaceIcon',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtLocation:QPlaceIcon'),
           )),
      ),
      'detailsFetched': (
          ('_ZNK13QPlacePrivate14detailsFetchedEv',
           ('bool', 'number', ''),
           ()),
      ),
      'setDetailsFetched': (
          ('_ZN13QPlacePrivate17setDetailsFetchedEb',
           ('nothing', 'nothing', ''),
           (
               ('bool', 'number', ''),
           )),
      ),
      'extendedAttribute': (
          ('_ZNK13QPlacePrivate17extendedAttributeERK7QString',
           ('address', 'value', 'QtLocation:QPlaceAttribute'),
           (
               ('address', 'text', ''),
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

  def isEmpty(self) -> bool:
    """
    Calls Qt's 'bool QPlacePrivate::isEmpty() const'.

    Qt's own words: https://doc.qt.io/qt-6/qplaceprivate.html#isEmpty
    """
    #  bool QPlacePrivate::isEmpty() const
    ritual = 'ritual_ZNK13QPlacePrivate7isEmptyEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK13QPlacePrivate7isEmptyEv'
    return self.uglySide.call(ritual)

  def categories(self) -> QList[QPlaceCategory]:
    """
    Calls Qt's 'QList<QPlaceCategory> QPlacePrivate::categories() const'.

    Qt's own words: https://doc.qt.io/qt-6/qplaceprivate.html#categories

    Returns
    -------

    QList[QPlaceCategory]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QPlaceCategory> QPlacePrivate::categories() const
    address = self.uglySide.call('ritual_ZNK13QPlacePrivate10categoriesEv')
    from . import QPlaceCategory
    return QList[QPlaceCategory]._cuteOwning(address)

  def location(self) -> QGeoLocation:
    """
    Calls Qt's 'QGeoLocation QPlacePrivate::location() const'.

    Qt's own words: https://doc.qt.io/qt-6/qplaceprivate.html#location

    Returns
    -------

    QGeoLocation
      A new cute QGeoLocation around the copy Qt gave back. Python owns it.
    """
    #  QGeoLocation QPlacePrivate::location() const
    address = self.uglySide.call('ritual_ZNK13QPlacePrivate8locationEv')
    from ..QtPositioning import QGeoLocation
    return QGeoLocation._cuteOwning(address)

  def ratings(self) -> QPlaceRatings:
    """
    Calls Qt's 'QPlaceRatings QPlacePrivate::ratings() const'.

    Qt's own words: https://doc.qt.io/qt-6/qplaceprivate.html#ratings

    Returns
    -------

    QPlaceRatings
      A new cute QPlaceRatings around the copy Qt gave back. Python owns it.
    """
    #  QPlaceRatings QPlacePrivate::ratings() const
    address = self.uglySide.call('ritual_ZNK13QPlacePrivate7ratingsEv')
    from . import QPlaceRatings
    return QPlaceRatings._cuteOwning(address)

  def supplier(self) -> QPlaceSupplier:
    """
    Calls Qt's 'QPlaceSupplier QPlacePrivate::supplier() const'.

    Qt's own words: https://doc.qt.io/qt-6/qplaceprivate.html#supplier

    Returns
    -------

    QPlaceSupplier
      A new cute QPlaceSupplier around the copy Qt gave back. Python owns it.
    """
    #  QPlaceSupplier QPlacePrivate::supplier() const
    address = self.uglySide.call('ritual_ZNK13QPlacePrivate8supplierEv')
    from . import QPlaceSupplier
    return QPlaceSupplier._cuteOwning(address)

  def name(self) -> str:
    """
    Calls Qt's 'QString QPlacePrivate::name() const'.

    Qt's own words: https://doc.qt.io/qt-6/qplaceprivate.html#name

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QPlacePrivate::name() const
    return self.uglySide.call('ritual_ZNK13QPlacePrivate4nameEv')

  def placeId(self) -> str:
    """
    Calls Qt's 'QString QPlacePrivate::placeId() const'.

    Qt's own words: https://doc.qt.io/qt-6/qplaceprivate.html#placeId

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QPlacePrivate::placeId() const
    return self.uglySide.call('ritual_ZNK13QPlacePrivate7placeIdEv')

  def attribution(self) -> str:
    """
    Calls Qt's 'QString QPlacePrivate::attribution() const'.

    Qt's own words: https://doc.qt.io/qt-6/qplaceprivate.html#attribution

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QPlacePrivate::attribution() const
    return self.uglySide.call('ritual_ZNK13QPlacePrivate11attributionEv')

  def visibility(self) -> QLocation.Visibility:
    """
    Calls Qt's 'QLocation::Visibility QPlacePrivate::visibility() const'.

    Qt's own words: https://doc.qt.io/qt-6/qplaceprivate.html#visibility

    Returns
    -------

    QLocation.Visibility
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QLocation.Visibility(number)' gives.
    """
    #  QLocation::Visibility QPlacePrivate::visibility() const
    return QLocation.Visibility(self.uglySide.call(
        'ritual_ZNK13QPlacePrivate10visibilityEv',
    ))

  def icon(self) -> QPlaceIcon:
    """
    Calls Qt's 'QPlaceIcon QPlacePrivate::icon() const'.

    Qt's own words: https://doc.qt.io/qt-6/qplaceprivate.html#icon

    Returns
    -------

    QPlaceIcon
      A new cute QPlaceIcon around the copy Qt gave back. Python owns it.
    """
    #  QPlaceIcon QPlacePrivate::icon() const
    address = self.uglySide.call('ritual_ZNK13QPlacePrivate4iconEv')
    from . import QPlaceIcon
    return QPlaceIcon._cuteOwning(address)

  def detailsFetched(self) -> bool:
    """
    Calls Qt's 'bool QPlacePrivate::detailsFetched() const'.

    Qt's own words: https://doc.qt.io/qt-6/qplaceprivate.html#detailsFetched
    """
    #  bool QPlacePrivate::detailsFetched() const
    return self.uglySide.call('ritual_ZNK13QPlacePrivate14detailsFetchedEv')

  def extendedAttributes(self) -> QMap[str, QPlaceAttribute]:
    """
    Calls Qt's 'QMap<QString, QPlaceAttribute>
    QPlacePrivate::extendedAttributes() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplaceprivate.html#extendedAttributes

    Returns
    -------

    QMap[str, QPlaceAttribute]
      A new cute map around the copy Qt gave back. Python owns it.
    """
    #  QMap<QString, QPlaceAttribute> QPlacePrivate::extendedAttributes()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK13QPlacePrivate18extendedAttributesEv',
    )
    from . import QPlaceAttribute
    return QMap[str, QPlaceAttribute]._cuteOwning(address)

  @overload(str)
  def extendedAttribute(self, attributeType: str) -> QPlaceAttribute:
    """
    Calls Qt's 'QPlaceAttribute QPlacePrivate::extendedAttribute(const
    QString &attributeType) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplaceprivate.html#extendedAttribute

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
    #  QPlaceAttribute QPlacePrivate::extendedAttribute(const QString
    #      &attributeType) const
    ritual = 'ritual_ZNK13QPlacePrivate17extendedAttributeERK7QString'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK13QPlacePrivate17extendedAttributeERK7QString'
    address = self.uglySide.call(ritual, attributeType)
    from . import QPlaceAttribute
    return QPlaceAttribute._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QList[QPlaceCategory])
  def setCategories(self, categories: QList[QPlaceCategory]) -> None:
    """
    Calls Qt's 'void QPlacePrivate::setCategories(const QList<QPlaceCategory>
    &categories)'.

    Qt's own words: https://doc.qt.io/qt-6/qplaceprivate.html#setCategories

    Parameters
    ----------

    categories : QList[QPlaceCategory]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QPlacePrivate::setCategories(const QList<QPlaceCategory>
    #      &categories)
    self.uglySide.call(
        'ritual_ZN13QPlacePrivate13setCategoriesERK5QListI14QPlaceCategoryE',
        self._valueOf(categories),
    )

  @overload(QGeoLocation)
  def setLocation(self, location: QGeoLocation) -> None:
    """
    Calls Qt's 'void QPlacePrivate::setLocation(const QGeoLocation
    &location)'.

    Qt's own words: https://doc.qt.io/qt-6/qplaceprivate.html#setLocation

    Parameters
    ----------

    location : QGeoLocation
      Passed on as a value: Qt reads the C++ QGeoLocation, which stays
      Python's own.
    """
    #  void QPlacePrivate::setLocation(const QGeoLocation &location)
    self.uglySide.call(
        'ritual_ZN13QPlacePrivate11setLocationERK12QGeoLocation',
        self._valueOf(location),
    )

  @overload(QPlaceRatings)
  def setRatings(self, ratings: QPlaceRatings) -> None:
    """
    Calls Qt's 'void QPlacePrivate::setRatings(const QPlaceRatings
    &ratings)'.

    Qt's own words: https://doc.qt.io/qt-6/qplaceprivate.html#setRatings

    Parameters
    ----------

    ratings : QPlaceRatings
      Passed on as a value: Qt reads the C++ QPlaceRatings, which stays
      Python's own.
    """
    #  void QPlacePrivate::setRatings(const QPlaceRatings &ratings)
    self.uglySide.call(
        'ritual_ZN13QPlacePrivate10setRatingsERK13QPlaceRatings',
        self._valueOf(ratings),
    )

  @overload(QPlaceSupplier)
  def setSupplier(self, supplier: QPlaceSupplier) -> None:
    """
    Calls Qt's 'void QPlacePrivate::setSupplier(const QPlaceSupplier
    &supplier)'.

    Qt's own words: https://doc.qt.io/qt-6/qplaceprivate.html#setSupplier

    Parameters
    ----------

    supplier : QPlaceSupplier
      Passed on as a value: Qt reads the C++ QPlaceSupplier, which stays
      Python's own.
    """
    #  void QPlacePrivate::setSupplier(const QPlaceSupplier &supplier)
    self.uglySide.call(
        'ritual_ZN13QPlacePrivate11setSupplierERK14QPlaceSupplier',
        self._valueOf(supplier),
    )

  @overload(str)
  def setName(self, name: str) -> None:
    """
    Calls Qt's 'void QPlacePrivate::setName(const QString &name)'.

    Qt's own words: https://doc.qt.io/qt-6/qplaceprivate.html#setName

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QPlacePrivate::setName(const QString &name)
    self.uglySide.call('ritual_ZN13QPlacePrivate7setNameERK7QString', name)

  @overload(str)
  def setPlaceId(self, placeIdentifier: str) -> None:
    """
    Calls Qt's 'void QPlacePrivate::setPlaceId(const QString
    &placeIdentifier)'.

    Qt's own words: https://doc.qt.io/qt-6/qplaceprivate.html#setPlaceId

    Parameters
    ----------

    placeIdentifier : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QPlacePrivate::setPlaceId(const QString &placeIdentifier)
    self.uglySide.call(
        'ritual_ZN13QPlacePrivate10setPlaceIdERK7QString', placeIdentifier,
    )

  @overload(str)
  def setAttribution(self, attribution: str) -> None:
    """
    Calls Qt's 'void QPlacePrivate::setAttribution(const QString
    &attribution)'.

    Qt's own words: https://doc.qt.io/qt-6/qplaceprivate.html#setAttribution

    Parameters
    ----------

    attribution : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QPlacePrivate::setAttribution(const QString &attribution)
    self.uglySide.call(
        'ritual_ZN13QPlacePrivate14setAttributionERK7QString', attribution,
    )

  @overload(QLocation.Visibility)
  def setVisibility(self, visibility: QLocation.Visibility) -> None:
    """
    Calls Qt's 'void QPlacePrivate::setVisibility(QLocation::Visibility
    visibility)'.

    Qt's own words: https://doc.qt.io/qt-6/qplaceprivate.html#setVisibility

    Parameters
    ----------

    visibility : QLocation.Visibility
      Passed on as its number.
    """
    #  void QPlacePrivate::setVisibility(QLocation::Visibility visibility)
    self.uglySide.call(
        'ritual_ZN13QPlacePrivate13setVisibilityEN9QLocation10VisibilityE',
        visibility.value,
    )

  @overload(QPlaceIcon)
  def setIcon(self, icon: QPlaceIcon) -> None:
    """
    Calls Qt's 'void QPlacePrivate::setIcon(const QPlaceIcon &icon)'.

    Qt's own words: https://doc.qt.io/qt-6/qplaceprivate.html#setIcon

    Parameters
    ----------

    icon : QPlaceIcon
      Passed on as a value: Qt reads the C++ QPlaceIcon, which stays Python's
      own.
    """
    #  void QPlacePrivate::setIcon(const QPlaceIcon &icon)
    self.uglySide.call(
        'ritual_ZN13QPlacePrivate7setIconERK10QPlaceIcon',
        self._valueOf(icon),
    )

  @overload(bool)
  def setDetailsFetched(self, fetched: bool) -> None:
    """
    Calls Qt's 'void QPlacePrivate::setDetailsFetched(bool fetched)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplaceprivate.html#setDetailsFetched

    Parameters
    ----------

    fetched : bool
      Passed on as it is.
    """
    #  void QPlacePrivate::setDetailsFetched(bool fetched)
    self.uglySide.call(
        'ritual_ZN13QPlacePrivate17setDetailsFetchedEb', fetched,
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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    - Qt's 'QPlacePrivate::QPlacePrivate()': the class is abstract, so C++
      cannot make one, and the C++ class of ours does not fill in every
      function it leaves open.
    - Qt's 'QPlacePrivate::QPlacePrivate(const QPlacePrivate &other)': the
      class is abstract, so C++ cannot make one, and the C++ class of ours
      does not fill in every function it leaves open.
    """
    raise NotImplementedError(
        "'QPlacePrivate.__init__' has no cute function yet. Qt's "
        "'QPlacePrivate::QPlacePrivate()': the class is abstract, so C++ "
        "cannot make one, and the C++ class of ours does not fill in every "
        "function it leaves open. Qt's 'QPlacePrivate::QPlacePrivate(const "
        "QPlacePrivate &other)': the class is abstract, so C++ cannot make "
        "one, and the C++ class of ours does not fill in every function it "
        "leaves open.")

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
    Calls Qt's 'QPlacePrivate *QPlacePrivate::clone()'.

    Qt's own words: https://doc.qt.io/qt-6/qplaceprivate.html#clone

    Returns
    -------

    Optional[QPlacePrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPlacePrivate *QPlacePrivate::clone()
    address = self.uglySide.call('ritual_ZN13QPlacePrivate5cloneEv')
    return QPlacePrivate._cuteAt(address)

  @staticmethod
  def contacts(*__, **_) -> Never:
    """
    - Qt's 'QMap<QString, QList<QPlaceContactDetail>>
      QPlacePrivate::contacts() const': gives a type Python has no way to
      take yet.
    - Qt's 'QMap<QString, QList<QPlaceContactDetail>>
      &QPlacePrivate::contacts()': gives a type Python has no way to take
      yet.
    """
    raise NotImplementedError(
        "'QPlacePrivate.contacts' has no cute function yet. Qt's "
        "'QMap<QString, QList<QPlaceContactDetail>> "
        "QPlacePrivate::contacts() const': gives a type Python has no way "
        "to take yet. Qt's 'QMap<QString, QList<QPlaceContactDetail>> "
        "&QPlacePrivate::contacts()': gives a type Python has no way to "
        "take yet.")
