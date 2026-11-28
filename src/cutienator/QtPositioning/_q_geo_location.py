"""
QGeoLocation binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtPositioning/qgeolocation.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QList, QMap

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from ..QtCore import QVariant
  from . import QGeoAddress, QGeoCoordinate, QGeoShape
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QGeoAddress = WAIT['QGeoAddress']
  QGeoCoordinate = WAIT['QGeoCoordinate']
  QGeoShape = WAIT['QGeoShape']
  QVariant = WAIT['QVariant']


class QGeoLocation(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QGeoLocation: a plain Python object standing in front
  of one C++ QGeoLocation.

  C++ hands a QGeoLocation around as a copy, so every C++ QGeoLocation behind
  a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QGeoLocation that has a ritual and that Python can
  call so far, 12 names in all: '__eq__', '__ne__', 'address', 'setAddress',
  'coordinate', 'setCoordinate', 'boundingShape', 'setBoundingShape',
  'extendedAttributes', 'setExtendedAttributes', 'isEmpty', 'equals'. It can
  be made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QGeoLocation::QGeoLocation(QGeoLocation &&other)': takes a type
    Python has no way to hand over yet.
  - Qt's 'QGeoLocation::~QGeoLocation()': the destructor: Python removes its
    C++ QGeoLocation by it, and has no other use for it.
  - Qt's 'QGeoLocation &QGeoLocation::operator=(const QGeoLocation &other)':
    assignment: Python binds a name and has no operator for it.
  - Qt's 'QGeoLocation &QGeoLocation::operator=(QGeoLocation &&other)':
    assignment: Python binds a name and has no operator for it.
  - Qt's 'void QGeoLocation::swap(QGeoLocation &other)': takes a type Python
    has no way to hand over yet.

  What to expect
  --------------

  - The C++ QGeoLocation is created at the first use, not by
    'QGeoLocation(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QGeoLocation back gives a copy the ritual made for
    Python, in a new cute QGeoLocation.
  - Each name of Qt's QGeoLocation that has no cute function yet, 'swap',
    holds a function that raises 'NotImplementedError', and its docstring
    says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(THIS, THIS)
  def equals(lhs: QGeoLocation, rhs: QGeoLocation) -> bool:
    """
    Calls Qt's 'bool QGeoLocation::equals(const QGeoLocation &lhs, const
    QGeoLocation &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qgeolocation.html#equals

    Parameters
    ----------

    lhs : QGeoLocation
      Passed on as a value: Qt reads the C++ QGeoLocation, which stays
      Python's own.

    rhs : QGeoLocation
      Passed on as a value: Qt reads the C++ QGeoLocation, which stays
      Python's own.
    """
    #  bool QGeoLocation::equals(const QGeoLocation &lhs, const QGeoLocation
    #      &rhs)
    return Rituals.call(
        'ritual_ZN12QGeoLocation6equalsERKS_S1_',
        CuteMixin._valueOf(lhs), CuteMixin._valueOf(rhs),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QGeoLocation'

  #  Qt's '~QGeoLocation()'. Naming it makes this a value class: Python owns
  #  every C++ QGeoLocation behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN12QGeoLocationD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def address(self) -> QGeoAddress:
    """
    Calls Qt's 'QGeoAddress QGeoLocation::address() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeolocation.html#address

    Returns
    -------

    QGeoAddress
      A new cute QGeoAddress around the copy Qt gave back. Python owns it.
    """
    #  QGeoAddress QGeoLocation::address() const
    address = self.uglySide.call('ritual_ZNK12QGeoLocation7addressEv')
    from . import QGeoAddress
    return QGeoAddress._cuteOwning(address)

  def coordinate(self) -> QGeoCoordinate:
    """
    Calls Qt's 'QGeoCoordinate QGeoLocation::coordinate() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeolocation.html#coordinate

    Returns
    -------

    QGeoCoordinate
      A new cute QGeoCoordinate around the copy Qt gave back. Python owns it.
    """
    #  QGeoCoordinate QGeoLocation::coordinate() const
    address = self.uglySide.call('ritual_ZNK12QGeoLocation10coordinateEv')
    from . import QGeoCoordinate
    return QGeoCoordinate._cuteOwning(address)

  def boundingShape(self) -> QGeoShape:
    """
    Calls Qt's 'QGeoShape QGeoLocation::boundingShape() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeolocation.html#boundingShape

    Returns
    -------

    QGeoShape
      A new cute QGeoShape around the copy Qt gave back. Python owns it.
    """
    #  QGeoShape QGeoLocation::boundingShape() const
    address = self.uglySide.call('ritual_ZNK12QGeoLocation13boundingShapeEv')
    from . import QGeoShape
    return QGeoShape._cuteOwning(address)

  def extendedAttributes(self) -> QMap[str, QVariant]:
    """
    Calls Qt's 'QVariantMap QGeoLocation::extendedAttributes() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeolocation.html#extendedAttributes

    Returns
    -------

    QMap[str, QVariant]
      A new cute map around the copy Qt gave back. Python owns it.
    """
    #  QVariantMap QGeoLocation::extendedAttributes() const
    address = self.uglySide.call(
        'ritual_ZNK12QGeoLocation18extendedAttributesEv',
    )
    from ..QtCore import QVariant
    return QMap[str, QVariant]._cuteOwning(address)

  def isEmpty(self) -> bool:
    """
    Calls Qt's 'bool QGeoLocation::isEmpty() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeolocation.html#isEmpty
    """
    #  bool QGeoLocation::isEmpty() const
    return self.uglySide.call('ritual_ZNK12QGeoLocation7isEmptyEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QGeoAddress)
  def setAddress(self, address: QGeoAddress) -> None:
    """
    Calls Qt's 'void QGeoLocation::setAddress(const QGeoAddress &address)'.

    Qt's own words: https://doc.qt.io/qt-6/qgeolocation.html#setAddress

    Parameters
    ----------

    address : QGeoAddress
      Passed on as a value: Qt reads the C++ QGeoAddress, which stays
      Python's own.
    """
    #  void QGeoLocation::setAddress(const QGeoAddress &address)
    self.uglySide.call(
        'ritual_ZN12QGeoLocation10setAddressERK11QGeoAddress',
        self._valueOf(address),
    )

  @overload(QGeoCoordinate)
  def setCoordinate(self, position: QGeoCoordinate) -> None:
    """
    Calls Qt's 'void QGeoLocation::setCoordinate(const QGeoCoordinate
    &position)'.

    Qt's own words: https://doc.qt.io/qt-6/qgeolocation.html#setCoordinate

    Parameters
    ----------

    position : QGeoCoordinate
      Passed on as a value: Qt reads the C++ QGeoCoordinate, which stays
      Python's own.
    """
    #  void QGeoLocation::setCoordinate(const QGeoCoordinate &position)
    self.uglySide.call(
        'ritual_ZN12QGeoLocation13setCoordinateERK14QGeoCoordinate',
        self._valueOf(position),
    )

  @overload(QGeoShape)
  def setBoundingShape(self, shape: QGeoShape) -> None:
    """
    Calls Qt's 'void QGeoLocation::setBoundingShape(const QGeoShape &shape)'.

    Qt's own words: https://doc.qt.io/qt-6/qgeolocation.html#setBoundingShape

    Parameters
    ----------

    shape : QGeoShape
      Passed on as a value: Qt reads the C++ QGeoShape, which stays Python's
      own.
    """
    #  void QGeoLocation::setBoundingShape(const QGeoShape &shape)
    self.uglySide.call(
        'ritual_ZN12QGeoLocation16setBoundingShapeERK9QGeoShape',
        self._valueOf(shape),
    )

  @overload(QMap[str, QVariant])
  def setExtendedAttributes(self, data: QMap[str, QVariant]) -> None:
    """
    Calls Qt's 'void QGeoLocation::setExtendedAttributes(const QVariantMap
    &data)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeolocation.html#setExtendedAttributes

    Parameters
    ----------

    data : QMap[str, QVariant]
      Passed on as a map of Qt: Qt reads the C++ map, which stays Python's
      own. A dict of Python is made into one first, and refused when a key or
      a value does not fit.
    """
    #  void QGeoLocation::setExtendedAttributes(const QVariantMap &data)
    self.uglySide.call(
        'ritual_ZN12QGeoLocation21setExtendedAttributesERK4QMapI7QString8QV'
        'ariantE',
        self._valueOf(data),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __eq__(self, rhs: QGeoLocation) -> bool:
    """
    Calls Qt's 'bool operator==(const QGeoLocation &lhs, const QGeoLocation
    &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qgeolocation.html#operator==

    Parameters
    ----------

    rhs : QGeoLocation
      Passed on as a value: Qt reads the C++ QGeoLocation, which stays
      Python's own.
    """
    #  bool operator==(const QGeoLocation &lhs, const QGeoLocation &rhs)
    return Rituals.call(
        'ritual_ZeqRK12QGeoLocationS1_',
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
  def __ne__(self, rhs: QGeoLocation) -> bool:
    """
    Calls Qt's 'bool operator!=(const QGeoLocation &lhs, const QGeoLocation
    &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qgeolocation.html#operator!=

    Parameters
    ----------

    rhs : QGeoLocation
      Passed on as a value: Qt reads the C++ QGeoLocation, which stays
      Python's own.
    """
    #  bool operator!=(const QGeoLocation &lhs, const QGeoLocation &rhs)
    return Rituals.call(
        'ritual_ZneRK12QGeoLocationS1_',
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
    Notes what was given, for Qt's 'QGeoLocation::QGeoLocation()', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qgeolocation.html#QGeoLocation
    """
    #  QGeoLocation::QGeoLocation()
    self._noteCreation(QGeoLocation, lambda: Rituals.call(
        'ritual_ZN12QGeoLocationC1Ev',
    ))

  @overload(THIS)
  def __init__(self, other: QGeoLocation) -> None:
    """
    Notes what was given, for Qt's 'QGeoLocation::QGeoLocation(const
    QGeoLocation &other)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qgeolocation.html#QGeoLocation

    Parameters
    ----------

    other : QGeoLocation
      Passed on as a value: Qt reads the C++ QGeoLocation, which stays
      Python's own.
    """
    #  QGeoLocation::QGeoLocation(const QGeoLocation &other)
    self._noteCreation(QGeoLocation, lambda: Rituals.call(
        'ritual_ZN12QGeoLocationC1ERKS_', self._valueOf(other),
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

  @staticmethod
  def swap(*__, **_) -> Never:
    """
    Qt's 'void QGeoLocation::swap(QGeoLocation &other)': takes a type Python
    has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QGeoLocation.swap' has no cute function yet. Qt's 'void "
        "QGeoLocation::swap(QGeoLocation &other)': takes a type Python has "
        "no way to hand over yet.")


#  Qt's 'QList<QGeoLocation>': the list of QGeoLocation, which
#  'QList[QGeoLocation]' gives. It is made here, so that there is one as soon
#  as there can be a QGeoLocation.
QList.createKind(
    QGeoLocation, 'value',
    make='ritual_list_make_QGeoLocation',
    add='ritual_list_add_QGeoLocation',
    size='ritual_list_size_QGeoLocation',
    at='ritual_list_at_QGeoLocation',
    drop='ritual_list_drop_QGeoLocation',
)
