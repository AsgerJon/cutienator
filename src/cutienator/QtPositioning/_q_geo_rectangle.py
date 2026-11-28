"""
QGeoRectangle binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtPositioning/qgeorectangle.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..QtCore import QList
from . import QGeoShape

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QGeoCoordinate, QGeoRectanglePrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QGeoCoordinate = WAIT['QGeoCoordinate']


class QGeoRectangle(QGeoShape):
  """
  The cute side of Qt's QGeoRectangle: a plain Python object standing in
  front of one C++ QGeoRectangle.

  It is built on the cute 'QGeoShape', as Qt's QGeoRectangle is built on Qt's
  QGeoShape, and has everything that class has.

  C++ hands a QGeoRectangle around as a copy, so every C++ QGeoRectangle
  behind a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QGeoRectangle that has a ritual and that Python can
  call so far, 24 names in all: 'setTopLeft', 'topLeft', 'setTopRight',
  'topRight', 'setBottomLeft', 'bottomLeft', 'setBottomRight', 'bottomRight',
  'setCenter', 'center', 'setWidth', 'width', 'setHeight', 'height',
  'contains', 'intersects', 'translate', 'translated', 'extendRectangle',
  'united', '__or__', '__ior__', 'toString', 'd_func'. It can be made from
  Python, in 6 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QGeoRectangle::~QGeoRectangle()': the destructor: Python removes
    its C++ QGeoRectangle by it, and has no other use for it.
  - Qt's 'QGeoRectangle &QGeoRectangle::operator=(const QGeoRectangle
    &other)': assignment: Python binds a name and has no operator for it.
  - Qt's 'const QGeoRectanglePrivate *QGeoRectangle::d_func() const': takes
    in Python what 'QGeoRectanglePrivate *QGeoRectangle::d_func()' takes.
  - Qt's 'QDataStream &operator<<(QDataStream &stream, const QGeoRectangle
    &rectangle)': takes a type Python has no way to hand over yet.
  - Qt's 'QDataStream &operator>>(QDataStream &stream, QGeoRectangle
    &rectangle)': an operator between other classes, written inside this one.

  What has no ritual
  ------------------

  3 of the 38 functions Qt declares: 3 not a gap.

  What to expect
  --------------

  - The C++ QGeoRectangle is created at the first use, not by
    'QGeoRectangle(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QGeoRectangle back gives a copy the ritual made for
    Python, in a new cute QGeoRectangle.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QGeoRectangle'

  #  Qt's '~QGeoRectangle()'. Naming it makes this a value class: Python owns
  #  every C++ QGeoRectangle behind a cute one, and removes it by this
  #  ritual.
  __delete_ritual__ = 'ritual_ZN13QGeoRectangleD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def topLeft(self) -> QGeoCoordinate:
    """
    Calls Qt's 'QGeoCoordinate QGeoRectangle::topLeft() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeorectangle.html#topLeft

    Returns
    -------

    QGeoCoordinate
      A new cute QGeoCoordinate around the copy Qt gave back. Python owns it.
    """
    #  QGeoCoordinate QGeoRectangle::topLeft() const
    address = self.uglySide.call('ritual_ZNK13QGeoRectangle7topLeftEv')
    from . import QGeoCoordinate
    return QGeoCoordinate._cuteOwning(address)

  def topRight(self) -> QGeoCoordinate:
    """
    Calls Qt's 'QGeoCoordinate QGeoRectangle::topRight() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeorectangle.html#topRight

    Returns
    -------

    QGeoCoordinate
      A new cute QGeoCoordinate around the copy Qt gave back. Python owns it.
    """
    #  QGeoCoordinate QGeoRectangle::topRight() const
    address = self.uglySide.call('ritual_ZNK13QGeoRectangle8topRightEv')
    from . import QGeoCoordinate
    return QGeoCoordinate._cuteOwning(address)

  def bottomLeft(self) -> QGeoCoordinate:
    """
    Calls Qt's 'QGeoCoordinate QGeoRectangle::bottomLeft() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeorectangle.html#bottomLeft

    Returns
    -------

    QGeoCoordinate
      A new cute QGeoCoordinate around the copy Qt gave back. Python owns it.
    """
    #  QGeoCoordinate QGeoRectangle::bottomLeft() const
    address = self.uglySide.call('ritual_ZNK13QGeoRectangle10bottomLeftEv')
    from . import QGeoCoordinate
    return QGeoCoordinate._cuteOwning(address)

  def bottomRight(self) -> QGeoCoordinate:
    """
    Calls Qt's 'QGeoCoordinate QGeoRectangle::bottomRight() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeorectangle.html#bottomRight

    Returns
    -------

    QGeoCoordinate
      A new cute QGeoCoordinate around the copy Qt gave back. Python owns it.
    """
    #  QGeoCoordinate QGeoRectangle::bottomRight() const
    address = self.uglySide.call('ritual_ZNK13QGeoRectangle11bottomRightEv')
    from . import QGeoCoordinate
    return QGeoCoordinate._cuteOwning(address)

  def center(self) -> QGeoCoordinate:
    """
    Calls Qt's 'QGeoCoordinate QGeoRectangle::center() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeorectangle.html#center

    Returns
    -------

    QGeoCoordinate
      A new cute QGeoCoordinate around the copy Qt gave back. Python owns it.
    """
    #  QGeoCoordinate QGeoRectangle::center() const
    address = self.uglySide.call('ritual_ZNK13QGeoRectangle6centerEv')
    from . import QGeoCoordinate
    return QGeoCoordinate._cuteOwning(address)

  def width(self) -> float:
    """
    Calls Qt's 'double QGeoRectangle::width() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeorectangle.html#width
    """
    #  double QGeoRectangle::width() const
    return self.uglySide.call('ritual_ZNK13QGeoRectangle5widthEv')

  def height(self) -> float:
    """
    Calls Qt's 'double QGeoRectangle::height() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeorectangle.html#height
    """
    #  double QGeoRectangle::height() const
    return self.uglySide.call('ritual_ZNK13QGeoRectangle6heightEv')

  @overload(THIS)
  def contains(self, rectangle: QGeoRectangle) -> bool:
    """
    Calls Qt's 'bool QGeoRectangle::contains(const QGeoRectangle &rectangle)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeorectangle.html#contains

    Parameters
    ----------

    rectangle : QGeoRectangle
      Passed on as a value: Qt reads the C++ QGeoRectangle, which stays
      Python's own.
    """
    #  bool QGeoRectangle::contains(const QGeoRectangle &rectangle) const
    return self.uglySide.call(
        'ritual_ZNK13QGeoRectangle8containsERKS_', self._valueOf(rectangle),
    )

  @overload(THIS)
  def intersects(self, rectangle: QGeoRectangle) -> bool:
    """
    Calls Qt's 'bool QGeoRectangle::intersects(const QGeoRectangle
    &rectangle) const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeorectangle.html#intersects

    Parameters
    ----------

    rectangle : QGeoRectangle
      Passed on as a value: Qt reads the C++ QGeoRectangle, which stays
      Python's own.
    """
    #  bool QGeoRectangle::intersects(const QGeoRectangle &rectangle) const
    return self.uglySide.call(
        'ritual_ZNK13QGeoRectangle10intersectsERKS_',
        self._valueOf(rectangle),
    )

  @overload(float, float)
  def translated(
      self,
      degreesLatitude: float,
      degreesLongitude: float,
  ) -> QGeoRectangle:
    """
    Calls Qt's 'QGeoRectangle QGeoRectangle::translated(double
    degreesLatitude, double degreesLongitude) const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeorectangle.html#translated

    Parameters
    ----------

    degreesLatitude : float
      Passed on as it is.

    degreesLongitude : float
      Passed on as it is.

    Returns
    -------

    QGeoRectangle
      A new cute QGeoRectangle around the copy Qt gave back. Python owns it.
    """
    #  QGeoRectangle QGeoRectangle::translated(double degreesLatitude, double
    #      degreesLongitude) const
    address = self.uglySide.call(
        'ritual_ZNK13QGeoRectangle10translatedEdd',
        degreesLatitude, degreesLongitude,
    )
    return QGeoRectangle._cuteOwning(address)

  @overload(THIS)
  def united(self, rectangle: QGeoRectangle) -> QGeoRectangle:
    """
    Calls Qt's 'QGeoRectangle QGeoRectangle::united(const QGeoRectangle
    &rectangle) const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeorectangle.html#united

    Parameters
    ----------

    rectangle : QGeoRectangle
      Passed on as a value: Qt reads the C++ QGeoRectangle, which stays
      Python's own.

    Returns
    -------

    QGeoRectangle
      A new cute QGeoRectangle around the copy Qt gave back. Python owns it.
    """
    #  QGeoRectangle QGeoRectangle::united(const QGeoRectangle &rectangle)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK13QGeoRectangle6unitedERKS_', self._valueOf(rectangle),
    )
    return QGeoRectangle._cuteOwning(address)

  def toString(self) -> str:
    """
    Calls Qt's 'QString QGeoRectangle::toString() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeorectangle.html#toString

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QGeoRectangle::toString() const
    return self.uglySide.call('ritual_ZNK13QGeoRectangle8toStringEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QGeoCoordinate)
  def setTopLeft(self, topLeft: QGeoCoordinate) -> None:
    """
    Calls Qt's 'void QGeoRectangle::setTopLeft(const QGeoCoordinate
    &topLeft)'.

    Qt's own words: https://doc.qt.io/qt-6/qgeorectangle.html#setTopLeft

    Parameters
    ----------

    topLeft : QGeoCoordinate
      Passed on as a value: Qt reads the C++ QGeoCoordinate, which stays
      Python's own.
    """
    #  void QGeoRectangle::setTopLeft(const QGeoCoordinate &topLeft)
    self.uglySide.call(
        'ritual_ZN13QGeoRectangle10setTopLeftERK14QGeoCoordinate',
        self._valueOf(topLeft),
    )

  @overload(QGeoCoordinate)
  def setTopRight(self, topRight: QGeoCoordinate) -> None:
    """
    Calls Qt's 'void QGeoRectangle::setTopRight(const QGeoCoordinate
    &topRight)'.

    Qt's own words: https://doc.qt.io/qt-6/qgeorectangle.html#setTopRight

    Parameters
    ----------

    topRight : QGeoCoordinate
      Passed on as a value: Qt reads the C++ QGeoCoordinate, which stays
      Python's own.
    """
    #  void QGeoRectangle::setTopRight(const QGeoCoordinate &topRight)
    self.uglySide.call(
        'ritual_ZN13QGeoRectangle11setTopRightERK14QGeoCoordinate',
        self._valueOf(topRight),
    )

  @overload(QGeoCoordinate)
  def setBottomLeft(self, bottomLeft: QGeoCoordinate) -> None:
    """
    Calls Qt's 'void QGeoRectangle::setBottomLeft(const QGeoCoordinate
    &bottomLeft)'.

    Qt's own words: https://doc.qt.io/qt-6/qgeorectangle.html#setBottomLeft

    Parameters
    ----------

    bottomLeft : QGeoCoordinate
      Passed on as a value: Qt reads the C++ QGeoCoordinate, which stays
      Python's own.
    """
    #  void QGeoRectangle::setBottomLeft(const QGeoCoordinate &bottomLeft)
    self.uglySide.call(
        'ritual_ZN13QGeoRectangle13setBottomLeftERK14QGeoCoordinate',
        self._valueOf(bottomLeft),
    )

  @overload(QGeoCoordinate)
  def setBottomRight(self, bottomRight: QGeoCoordinate) -> None:
    """
    Calls Qt's 'void QGeoRectangle::setBottomRight(const QGeoCoordinate
    &bottomRight)'.

    Qt's own words: https://doc.qt.io/qt-6/qgeorectangle.html#setBottomRight

    Parameters
    ----------

    bottomRight : QGeoCoordinate
      Passed on as a value: Qt reads the C++ QGeoCoordinate, which stays
      Python's own.
    """
    #  void QGeoRectangle::setBottomRight(const QGeoCoordinate &bottomRight)
    self.uglySide.call(
        'ritual_ZN13QGeoRectangle14setBottomRightERK14QGeoCoordinate',
        self._valueOf(bottomRight),
    )

  @overload(QGeoCoordinate)
  def setCenter(self, center: QGeoCoordinate) -> None:
    """
    Calls Qt's 'void QGeoRectangle::setCenter(const QGeoCoordinate &center)'.

    Qt's own words: https://doc.qt.io/qt-6/qgeorectangle.html#setCenter

    Parameters
    ----------

    center : QGeoCoordinate
      Passed on as a value: Qt reads the C++ QGeoCoordinate, which stays
      Python's own.
    """
    #  void QGeoRectangle::setCenter(const QGeoCoordinate &center)
    self.uglySide.call(
        'ritual_ZN13QGeoRectangle9setCenterERK14QGeoCoordinate',
        self._valueOf(center),
    )

  @overload(float)
  def setWidth(self, degreesWidth: float) -> None:
    """
    Calls Qt's 'void QGeoRectangle::setWidth(double degreesWidth)'.

    Qt's own words: https://doc.qt.io/qt-6/qgeorectangle.html#setWidth

    Parameters
    ----------

    degreesWidth : float
      Passed on as it is.
    """
    #  void QGeoRectangle::setWidth(double degreesWidth)
    self.uglySide.call('ritual_ZN13QGeoRectangle8setWidthEd', degreesWidth)

  @overload(float)
  def setHeight(self, degreesHeight: float) -> None:
    """
    Calls Qt's 'void QGeoRectangle::setHeight(double degreesHeight)'.

    Qt's own words: https://doc.qt.io/qt-6/qgeorectangle.html#setHeight

    Parameters
    ----------

    degreesHeight : float
      Passed on as it is.
    """
    #  void QGeoRectangle::setHeight(double degreesHeight)
    self.uglySide.call('ritual_ZN13QGeoRectangle9setHeightEd', degreesHeight)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __or__(self, rectangle: QGeoRectangle) -> QGeoRectangle:
    """
    Calls Qt's 'QGeoRectangle QGeoRectangle::operator|(const QGeoRectangle
    &rectangle) const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeorectangle.html#operator|

    Parameters
    ----------

    rectangle : QGeoRectangle
      Passed on as a value: Qt reads the C++ QGeoRectangle, which stays
      Python's own.

    Returns
    -------

    QGeoRectangle
      A new cute QGeoRectangle around the copy Qt gave back. Python owns it.
    """
    #  QGeoRectangle QGeoRectangle::operator|(const QGeoRectangle &rectangle)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK13QGeoRectangleorERKS_', self._valueOf(rectangle),
    )
    return QGeoRectangle._cuteOwning(address)

  @overload.fallback
  def __or__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(THIS)
  def __ior__(self, rectangle: QGeoRectangle) -> QGeoRectangle:
    """
    Calls Qt's 'QGeoRectangle &QGeoRectangle::operator|=(const QGeoRectangle
    &rectangle)'.

    Qt's own words: https://doc.qt.io/qt-6/qgeorectangle.html#operator|=

    Parameters
    ----------

    rectangle : QGeoRectangle
      Passed on as a value: Qt reads the C++ QGeoRectangle, which stays
      Python's own.
    """
    #  QGeoRectangle &QGeoRectangle::operator|=(const QGeoRectangle
    #      &rectangle)
    self.uglySide.call(
        'ritual_ZN13QGeoRectangleoRERKS_', self._valueOf(rectangle),
    )
    return self

  @overload.fallback
  def __ior__(self, *args: object) -> object:
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
    Notes what was given, for Qt's 'QGeoRectangle::QGeoRectangle()', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qgeorectangle.html#QGeoRectangle
    """
    #  QGeoRectangle::QGeoRectangle()
    self._noteCreation(QGeoRectangle, lambda: Rituals.call(
        'ritual_ZN13QGeoRectangleC1Ev',
    ))

  @overload(QGeoCoordinate, float, float)
  def __init__(
      self,
      center: QGeoCoordinate,
      degreesWidth: float,
      degreesHeight: float,
  ) -> None:
    """
    Notes what was given, for Qt's 'QGeoRectangle::QGeoRectangle(const
    QGeoCoordinate &center, double degreesWidth, double degreesHeight)',
    which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qgeorectangle.html#QGeoRectangle

    Parameters
    ----------

    center : QGeoCoordinate
      Passed on as a value: Qt reads the C++ QGeoCoordinate, which stays
      Python's own.

    degreesWidth : float
      Passed on as it is.

    degreesHeight : float
      Passed on as it is.
    """
    #  QGeoRectangle::QGeoRectangle(const QGeoCoordinate &center, double
    #      degreesWidth, double degreesHeight)
    self._noteCreation(QGeoRectangle, lambda: Rituals.call(
        'ritual_ZN13QGeoRectangleC1ERK14QGeoCoordinatedd',
        self._valueOf(center), degreesWidth, degreesHeight,
    ))

  @overload(QGeoCoordinate, QGeoCoordinate)
  def __init__(
      self,
      topLeft: QGeoCoordinate,
      bottomRight: QGeoCoordinate,
  ) -> None:
    """
    Notes what was given, for Qt's 'QGeoRectangle::QGeoRectangle(const
    QGeoCoordinate &topLeft, const QGeoCoordinate &bottomRight)', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qgeorectangle.html#QGeoRectangle

    Parameters
    ----------

    topLeft : QGeoCoordinate
      Passed on as a value: Qt reads the C++ QGeoCoordinate, which stays
      Python's own.

    bottomRight : QGeoCoordinate
      Passed on as a value: Qt reads the C++ QGeoCoordinate, which stays
      Python's own.
    """
    #  QGeoRectangle::QGeoRectangle(const QGeoCoordinate &topLeft, const
    #      QGeoCoordinate &bottomRight)
    self._noteCreation(QGeoRectangle, lambda: Rituals.call(
        'ritual_ZN13QGeoRectangleC1ERK14QGeoCoordinateS2_',
        self._valueOf(topLeft), self._valueOf(bottomRight),
    ))

  @overload(QList[QGeoCoordinate])
  def __init__(self, coordinates: QList[QGeoCoordinate]) -> None:
    """
    Notes what was given, for Qt's 'QGeoRectangle::QGeoRectangle(const
    QList<QGeoCoordinate> &coordinates)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qgeorectangle.html#QGeoRectangle

    Parameters
    ----------

    coordinates : QList[QGeoCoordinate]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  QGeoRectangle::QGeoRectangle(const QList<QGeoCoordinate> &coordinates)
    self._noteCreation(QGeoRectangle, lambda: Rituals.call(
        'ritual_ZN13QGeoRectangleC1ERK5QListI14QGeoCoordinateE',
        self._valueOf(coordinates),
    ))

  @overload(THIS)
  def __init__(self, other: QGeoRectangle) -> None:
    """
    Notes what was given, for Qt's 'QGeoRectangle::QGeoRectangle(const
    QGeoRectangle &other)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qgeorectangle.html#QGeoRectangle

    Parameters
    ----------

    other : QGeoRectangle
      Passed on as a value: Qt reads the C++ QGeoRectangle, which stays
      Python's own.
    """
    #  QGeoRectangle::QGeoRectangle(const QGeoRectangle &other)
    self._noteCreation(QGeoRectangle, lambda: Rituals.call(
        'ritual_ZN13QGeoRectangleC1ERKS_', self._valueOf(other),
    ))

  @overload(QGeoShape)
  def __init__(self, other: QGeoShape) -> None:
    """
    Notes what was given, for Qt's 'QGeoRectangle::QGeoRectangle(const
    QGeoShape &other)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qgeorectangle.html#QGeoRectangle

    Parameters
    ----------

    other : QGeoShape
      Passed on as a value: Qt reads the C++ QGeoShape, which stays Python's
      own.
    """
    #  QGeoRectangle::QGeoRectangle(const QGeoShape &other)
    self._noteCreation(QGeoRectangle, lambda: Rituals.call(
        'ritual_ZN13QGeoRectangleC1ERK9QGeoShape', self._valueOf(other),
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

  @overload(float, float)
  def translate(
      self,
      degreesLatitude: float,
      degreesLongitude: float,
  ) -> None:
    """
    Calls Qt's 'void QGeoRectangle::translate(double degreesLatitude, double
    degreesLongitude)'.

    Qt's own words: https://doc.qt.io/qt-6/qgeorectangle.html#translate

    Parameters
    ----------

    degreesLatitude : float
      Passed on as it is.

    degreesLongitude : float
      Passed on as it is.
    """
    #  void QGeoRectangle::translate(double degreesLatitude, double
    #      degreesLongitude)
    self.uglySide.call(
        'ritual_ZN13QGeoRectangle9translateEdd',
        degreesLatitude, degreesLongitude,
    )

  @overload(QGeoCoordinate)
  def extendRectangle(self, coordinate: QGeoCoordinate) -> None:
    """
    Calls Qt's 'void QGeoRectangle::extendRectangle(const QGeoCoordinate
    &coordinate)'.

    Qt's own words: https://doc.qt.io/qt-6/qgeorectangle.html#extendRectangle

    Parameters
    ----------

    coordinate : QGeoCoordinate
      Passed on as a value: Qt reads the C++ QGeoCoordinate, which stays
      Python's own.
    """
    #  void QGeoRectangle::extendRectangle(const QGeoCoordinate &coordinate)
    self.uglySide.call(
        'ritual_ZN13QGeoRectangle15extendRectangleERK14QGeoCoordinate',
        self._valueOf(coordinate),
    )

  def d_func(self) -> Optional[QGeoRectanglePrivate]:
    """
    Calls Qt's 'QGeoRectanglePrivate *QGeoRectangle::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qgeorectangle.html#d_func

    Returns
    -------

    Optional[QGeoRectanglePrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QGeoRectanglePrivate *QGeoRectangle::d_func()
    address = self.uglySide.call('ritual_ZN13QGeoRectangle6d_funcEv')
    from . import QGeoRectanglePrivate
    return QGeoRectanglePrivate._cuteAt(address)


#  Qt's 'QList<QGeoRectangle>': the list of QGeoRectangle, which
#  'QList[QGeoRectangle]' gives. It is made here, so that there is one as
#  soon as there can be a QGeoRectangle.
QList.createKind(
    QGeoRectangle, 'value',
    make='ritual_list_make_QGeoRectangle',
    add='ritual_list_add_QGeoRectangle',
    size='ritual_list_size_QGeoRectangle',
    at='ritual_list_at_QGeoRectangle',
    drop='ritual_list_drop_QGeoRectangle',
)
