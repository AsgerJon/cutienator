"""
QGeoPolygon binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtPositioning/qgeopolygon.h, Qt 6.12.0. Changes made here are lost.
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

  from ..QtCore import QVariant
  from . import QGeoCoordinate, QGeoPolygonPrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QGeoCoordinate = WAIT['QGeoCoordinate']
  QVariant = WAIT['QVariant']


class QGeoPolygon(QGeoShape):
  """
  The cute side of Qt's QGeoPolygon: a plain Python object standing in front
  of one C++ QGeoPolygon.

  It is built on the cute 'QGeoShape', as Qt's QGeoPolygon is built on Qt's
  QGeoShape, and has everything that class has.

  C++ hands a QGeoPolygon around as a copy, so every C++ QGeoPolygon behind a
  cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QGeoPolygon that has a ritual and that Python can
  call so far, 19 names in all: 'setPerimeter', 'perimeter', 'addHole',
  'hole', 'holePath', 'removeHole', 'holesCount', 'translate', 'translated',
  'length', 'size', 'addCoordinate', 'insertCoordinate', 'replaceCoordinate',
  'coordinateAt', 'containsCoordinate', 'removeCoordinate', 'toString',
  'd_func'. It can be made from Python, in 4 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QGeoPolygon::~QGeoPolygon()': the destructor: Python removes its
    C++ QGeoPolygon by it, and has no other use for it.
  - Qt's 'QGeoPolygon &QGeoPolygon::operator=(const QGeoPolygon &other)':
    assignment: Python binds a name and has no operator for it.
  - Qt's 'const QGeoPolygonPrivate *QGeoPolygon::d_func() const': takes in
    Python what 'QGeoPolygonPrivate *QGeoPolygon::d_func()' takes.
  - Qt's 'QDataStream &operator<<(QDataStream &stream, const QGeoPolygon
    &polygon)': takes a type Python has no way to hand over yet.
  - Qt's 'QDataStream &operator>>(QDataStream &stream, QGeoPolygon
    &polygon)': an operator between other classes, written inside this one.

  What has no ritual
  ------------------

  3 of the 33 functions Qt declares: 3 not a gap.

  What to expect
  --------------

  - The C++ QGeoPolygon is created at the first use, not by
    'QGeoPolygon(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QGeoPolygon back gives a copy the ritual made for
    Python, in a new cute QGeoPolygon.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QGeoPolygon'

  #  Qt's '~QGeoPolygon()'. Naming it makes this a value class: Python owns
  #  every C++ QGeoPolygon behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN11QGeoPolygonD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def perimeter(self) -> QList[QGeoCoordinate]:
    """
    Calls Qt's 'const QList<QGeoCoordinate> &QGeoPolygon::perimeter() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeopolygon.html#perimeter

    Returns
    -------

    QList[QGeoCoordinate]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  const QList<QGeoCoordinate> &QGeoPolygon::perimeter() const
    address = self.uglySide.call('ritual_ZNK11QGeoPolygon9perimeterEv')
    from . import QGeoCoordinate
    return QList[QGeoCoordinate]._cuteOwning(address)

  @overload(int)
  def hole(self, index: int) -> QList[QVariant]:
    """
    Calls Qt's 'const QVariantList QGeoPolygon::hole(qsizetype index) const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeopolygon.html#hole

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    QList[QVariant]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  const QVariantList QGeoPolygon::hole(qsizetype index) const
    address = self.uglySide.call('ritual_ZNK11QGeoPolygon4holeEx', index)
    from ..QtCore import QVariant
    return QList[QVariant]._cuteOwning(address)

  @overload(int)
  def holePath(self, index: int) -> QList[QGeoCoordinate]:
    """
    Calls Qt's 'const QList<QGeoCoordinate> QGeoPolygon::holePath(qsizetype
    index) const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeopolygon.html#holePath

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    QList[QGeoCoordinate]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  const QList<QGeoCoordinate> QGeoPolygon::holePath(qsizetype index)
    #      const
    address = self.uglySide.call('ritual_ZNK11QGeoPolygon8holePathEx', index)
    from . import QGeoCoordinate
    return QList[QGeoCoordinate]._cuteOwning(address)

  def holesCount(self) -> int:
    """
    Calls Qt's 'qsizetype QGeoPolygon::holesCount() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeopolygon.html#holesCount
    """
    #  qsizetype QGeoPolygon::holesCount() const
    return self.uglySide.call('ritual_ZNK11QGeoPolygon10holesCountEv')

  @overload(float, float)
  def translated(
      self,
      degreesLatitude: float,
      degreesLongitude: float,
  ) -> QGeoPolygon:
    """
    Calls Qt's 'QGeoPolygon QGeoPolygon::translated(double degreesLatitude,
    double degreesLongitude) const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeopolygon.html#translated

    Parameters
    ----------

    degreesLatitude : float
      Passed on as it is.

    degreesLongitude : float
      Passed on as it is.

    Returns
    -------

    QGeoPolygon
      A new cute QGeoPolygon around the copy Qt gave back. Python owns it.
    """
    #  QGeoPolygon QGeoPolygon::translated(double degreesLatitude, double
    #      degreesLongitude) const
    address = self.uglySide.call(
        'ritual_ZNK11QGeoPolygon10translatedEdd',
        degreesLatitude, degreesLongitude,
    )
    return QGeoPolygon._cuteOwning(address)

  @overload()
  @overload(int)
  @overload(int, int)
  def length(self, indexFrom: int = 0, indexTo: int = -1) -> float:
    """
    Calls Qt's 'double QGeoPolygon::length(qsizetype indexFrom, qsizetype
    indexTo) const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeopolygon.html#length

    Parameters
    ----------

    indexFrom : int
      Passed on as it is. May be left out, as in Qt: it is then 0.

    indexTo : int
      Passed on as it is. May be left out, as in Qt: it is then -1.
    """
    #  double QGeoPolygon::length(qsizetype indexFrom, qsizetype indexTo)
    #      const
    return self.uglySide.call(
        'ritual_ZNK11QGeoPolygon6lengthExx', indexFrom, indexTo,
    )

  def size(self) -> int:
    """
    Calls Qt's 'qsizetype QGeoPolygon::size() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeopolygon.html#size
    """
    #  qsizetype QGeoPolygon::size() const
    return self.uglySide.call('ritual_ZNK11QGeoPolygon4sizeEv')

  @overload(int)
  def coordinateAt(self, index: int) -> QGeoCoordinate:
    """
    Calls Qt's 'QGeoCoordinate QGeoPolygon::coordinateAt(qsizetype index)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeopolygon.html#coordinateAt

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    QGeoCoordinate
      A new cute QGeoCoordinate around the copy Qt gave back. Python owns it.
    """
    #  QGeoCoordinate QGeoPolygon::coordinateAt(qsizetype index) const
    address = self.uglySide.call(
        'ritual_ZNK11QGeoPolygon12coordinateAtEx', index,
    )
    from . import QGeoCoordinate
    return QGeoCoordinate._cuteOwning(address)

  @overload(QGeoCoordinate)
  def containsCoordinate(self, coordinate: QGeoCoordinate) -> bool:
    """
    Calls Qt's 'bool QGeoPolygon::containsCoordinate(const QGeoCoordinate
    &coordinate) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeopolygon.html#containsCoordinate

    Parameters
    ----------

    coordinate : QGeoCoordinate
      Passed on as a value: Qt reads the C++ QGeoCoordinate, which stays
      Python's own.
    """
    #  bool QGeoPolygon::containsCoordinate(const QGeoCoordinate &coordinate)
    #      const
    return self.uglySide.call(
        'ritual_ZNK11QGeoPolygon18containsCoordinateERK14QGeoCoordinate',
        self._valueOf(coordinate),
    )

  def toString(self) -> str:
    """
    Calls Qt's 'QString QGeoPolygon::toString() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeopolygon.html#toString

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QGeoPolygon::toString() const
    return self.uglySide.call('ritual_ZNK11QGeoPolygon8toStringEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QList[QGeoCoordinate])
  def setPerimeter(self, path: QList[QGeoCoordinate]) -> None:
    """
    Calls Qt's 'void QGeoPolygon::setPerimeter(const QList<QGeoCoordinate>
    &path)'.

    Qt's own words: https://doc.qt.io/qt-6/qgeopolygon.html#setPerimeter

    Parameters
    ----------

    path : QList[QGeoCoordinate]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QGeoPolygon::setPerimeter(const QList<QGeoCoordinate> &path)
    self.uglySide.call(
        'ritual_ZN11QGeoPolygon12setPerimeterERK5QListI14QGeoCoordinateE',
        self._valueOf(path),
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
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'QGeoPolygon::QGeoPolygon()', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qgeopolygon.html#QGeoPolygon
    """
    #  QGeoPolygon::QGeoPolygon()
    self._noteCreation(QGeoPolygon, lambda: Rituals.call(
        'ritual_ZN11QGeoPolygonC1Ev',
    ))

  @overload(QList[QGeoCoordinate])
  def __init__(self, path: QList[QGeoCoordinate]) -> None:
    """
    Notes what was given, for Qt's 'QGeoPolygon::QGeoPolygon(const
    QList<QGeoCoordinate> &path)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qgeopolygon.html#QGeoPolygon

    Parameters
    ----------

    path : QList[QGeoCoordinate]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  QGeoPolygon::QGeoPolygon(const QList<QGeoCoordinate> &path)
    self._noteCreation(QGeoPolygon, lambda: Rituals.call(
        'ritual_ZN11QGeoPolygonC1ERK5QListI14QGeoCoordinateE',
        self._valueOf(path),
    ))

  @overload(THIS)
  def __init__(self, other: QGeoPolygon) -> None:
    """
    Notes what was given, for Qt's 'QGeoPolygon::QGeoPolygon(const
    QGeoPolygon &other)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qgeopolygon.html#QGeoPolygon

    Parameters
    ----------

    other : QGeoPolygon
      Passed on as a value: Qt reads the C++ QGeoPolygon, which stays
      Python's own.
    """
    #  QGeoPolygon::QGeoPolygon(const QGeoPolygon &other)
    self._noteCreation(QGeoPolygon, lambda: Rituals.call(
        'ritual_ZN11QGeoPolygonC1ERKS_', self._valueOf(other),
    ))

  @overload(QGeoShape)
  def __init__(self, other: QGeoShape) -> None:
    """
    Notes what was given, for Qt's 'QGeoPolygon::QGeoPolygon(const QGeoShape
    &other)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qgeopolygon.html#QGeoPolygon

    Parameters
    ----------

    other : QGeoShape
      Passed on as a value: Qt reads the C++ QGeoShape, which stays Python's
      own.
    """
    #  QGeoPolygon::QGeoPolygon(const QGeoShape &other)
    self._noteCreation(QGeoPolygon, lambda: Rituals.call(
        'ritual_ZN11QGeoPolygonC1ERK9QGeoShape', self._valueOf(other),
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

  @overload(QVariant)
  def addHole(self, holePath: QVariant) -> None:
    """
    Calls Qt's 'void QGeoPolygon::addHole(const QVariant &holePath)'.

    Qt's own words: https://doc.qt.io/qt-6/qgeopolygon.html#addHole

    Parameters
    ----------

    holePath : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void QGeoPolygon::addHole(const QVariant &holePath)
    self.uglySide.call(
        'ritual_ZN11QGeoPolygon7addHoleERK8QVariant',
        self._valueOf(holePath),
    )

  @overload(QList[QGeoCoordinate])
  def addHole(self, holePath: QList[QGeoCoordinate]) -> None:
    """
    Calls Qt's 'void QGeoPolygon::addHole(const QList<QGeoCoordinate>
    &holePath)'.

    Qt's own words: https://doc.qt.io/qt-6/qgeopolygon.html#addHole

    Parameters
    ----------

    holePath : QList[QGeoCoordinate]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QGeoPolygon::addHole(const QList<QGeoCoordinate> &holePath)
    self.uglySide.call(
        'ritual_ZN11QGeoPolygon7addHoleERK5QListI14QGeoCoordinateE',
        self._valueOf(holePath),
    )

  @overload(int)
  def removeHole(self, index: int) -> None:
    """
    Calls Qt's 'void QGeoPolygon::removeHole(qsizetype index)'.

    Qt's own words: https://doc.qt.io/qt-6/qgeopolygon.html#removeHole

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  void QGeoPolygon::removeHole(qsizetype index)
    self.uglySide.call('ritual_ZN11QGeoPolygon10removeHoleEx', index)

  @overload(float, float)
  def translate(
      self,
      degreesLatitude: float,
      degreesLongitude: float,
  ) -> None:
    """
    Calls Qt's 'void QGeoPolygon::translate(double degreesLatitude, double
    degreesLongitude)'.

    Qt's own words: https://doc.qt.io/qt-6/qgeopolygon.html#translate

    Parameters
    ----------

    degreesLatitude : float
      Passed on as it is.

    degreesLongitude : float
      Passed on as it is.
    """
    #  void QGeoPolygon::translate(double degreesLatitude, double
    #      degreesLongitude)
    self.uglySide.call(
        'ritual_ZN11QGeoPolygon9translateEdd',
        degreesLatitude, degreesLongitude,
    )

  @overload(QGeoCoordinate)
  def addCoordinate(self, coordinate: QGeoCoordinate) -> None:
    """
    Calls Qt's 'void QGeoPolygon::addCoordinate(const QGeoCoordinate
    &coordinate)'.

    Qt's own words: https://doc.qt.io/qt-6/qgeopolygon.html#addCoordinate

    Parameters
    ----------

    coordinate : QGeoCoordinate
      Passed on as a value: Qt reads the C++ QGeoCoordinate, which stays
      Python's own.
    """
    #  void QGeoPolygon::addCoordinate(const QGeoCoordinate &coordinate)
    self.uglySide.call(
        'ritual_ZN11QGeoPolygon13addCoordinateERK14QGeoCoordinate',
        self._valueOf(coordinate),
    )

  @overload(int, QGeoCoordinate)
  def insertCoordinate(self, index: int, coordinate: QGeoCoordinate) -> None:
    """
    Calls Qt's 'void QGeoPolygon::insertCoordinate(qsizetype index, const
    QGeoCoordinate &coordinate)'.

    Qt's own words: https://doc.qt.io/qt-6/qgeopolygon.html#insertCoordinate

    Parameters
    ----------

    index : int
      Passed on as it is.

    coordinate : QGeoCoordinate
      Passed on as a value: Qt reads the C++ QGeoCoordinate, which stays
      Python's own.
    """
    #  void QGeoPolygon::insertCoordinate(qsizetype index, const
    #      QGeoCoordinate &coordinate)
    self.uglySide.call(
        'ritual_ZN11QGeoPolygon16insertCoordinateExRK14QGeoCoordinate',
        index, self._valueOf(coordinate),
    )

  @overload(int, QGeoCoordinate)
  def replaceCoordinate(
      self,
      index: int,
      coordinate: QGeoCoordinate,
  ) -> None:
    """
    Calls Qt's 'void QGeoPolygon::replaceCoordinate(qsizetype index, const
    QGeoCoordinate &coordinate)'.

    Qt's own words: https://doc.qt.io/qt-6/qgeopolygon.html#replaceCoordinate

    Parameters
    ----------

    index : int
      Passed on as it is.

    coordinate : QGeoCoordinate
      Passed on as a value: Qt reads the C++ QGeoCoordinate, which stays
      Python's own.
    """
    #  void QGeoPolygon::replaceCoordinate(qsizetype index, const
    #      QGeoCoordinate &coordinate)
    self.uglySide.call(
        'ritual_ZN11QGeoPolygon17replaceCoordinateExRK14QGeoCoordinate',
        index, self._valueOf(coordinate),
    )

  @overload(QGeoCoordinate)
  def removeCoordinate(self, coordinate: QGeoCoordinate) -> None:
    """
    Calls Qt's 'void QGeoPolygon::removeCoordinate(const QGeoCoordinate
    &coordinate)'.

    Qt's own words: https://doc.qt.io/qt-6/qgeopolygon.html#removeCoordinate

    Parameters
    ----------

    coordinate : QGeoCoordinate
      Passed on as a value: Qt reads the C++ QGeoCoordinate, which stays
      Python's own.
    """
    #  void QGeoPolygon::removeCoordinate(const QGeoCoordinate &coordinate)
    self.uglySide.call(
        'ritual_ZN11QGeoPolygon16removeCoordinateERK14QGeoCoordinate',
        self._valueOf(coordinate),
    )

  @overload(int)
  def removeCoordinate(self, index: int) -> None:
    """
    Calls Qt's 'void QGeoPolygon::removeCoordinate(qsizetype index)'.

    Qt's own words: https://doc.qt.io/qt-6/qgeopolygon.html#removeCoordinate

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  void QGeoPolygon::removeCoordinate(qsizetype index)
    self.uglySide.call('ritual_ZN11QGeoPolygon16removeCoordinateEx', index)

  def d_func(self) -> Optional[QGeoPolygonPrivate]:
    """
    Calls Qt's 'QGeoPolygonPrivate *QGeoPolygon::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qgeopolygon.html#d_func

    Returns
    -------

    Optional[QGeoPolygonPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QGeoPolygonPrivate *QGeoPolygon::d_func()
    address = self.uglySide.call('ritual_ZN11QGeoPolygon6d_funcEv')
    from . import QGeoPolygonPrivate
    return QGeoPolygonPrivate._cuteAt(address)
