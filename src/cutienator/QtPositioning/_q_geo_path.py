"""
QGeoPath binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtPositioning/qgeopath.h, Qt 6.12.0. Changes made here are lost.
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
  from . import QGeoCoordinate, QGeoPathPrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QGeoCoordinate = WAIT['QGeoCoordinate']
  QVariant = WAIT['QVariant']


class QGeoPath(QGeoShape):
  """
  The cute side of Qt's QGeoPath: a plain Python object standing in front of
  one C++ QGeoPath.

  It is built on the cute 'QGeoShape', as Qt's QGeoPath is built on Qt's
  QGeoShape, and has everything that class has.

  C++ hands a QGeoPath around as a copy, so every C++ QGeoPath behind a cute
  one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QGeoPath that has a ritual and that Python can call
  so far, 19 names in all: 'setPath', 'path', 'clearPath', 'setVariantPath',
  'variantPath', 'setWidth', 'width', 'translate', 'translated', 'length',
  'size', 'addCoordinate', 'insertCoordinate', 'replaceCoordinate',
  'coordinateAt', 'containsCoordinate', 'removeCoordinate', 'toString',
  'd_func'. It can be made from Python, in 4 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QGeoPath::~QGeoPath()': the destructor: Python removes its C++
    QGeoPath by it, and has no other use for it.
  - Qt's 'QGeoPath &QGeoPath::operator=(const QGeoPath &other)': assignment:
    Python binds a name and has no operator for it.
  - Qt's 'const QGeoPathPrivate *QGeoPath::d_func() const': takes in Python
    what 'QGeoPathPrivate *QGeoPath::d_func()' takes.
  - Qt's 'QDataStream &operator<<(QDataStream &stream, const QGeoPath
    &path)': takes a type Python has no way to hand over yet.
  - Qt's 'QDataStream &operator>>(QDataStream &stream, QGeoPath &path)': an
    operator between other classes, written inside this one.

  What has no ritual
  ------------------

  3 of the 32 functions Qt declares: 3 not a gap.

  What to expect
  --------------

  - The C++ QGeoPath is created at the first use, not by 'QGeoPath(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QGeoPath back gives a copy the ritual made for
    Python, in a new cute QGeoPath.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QGeoPath'

  #  Qt's '~QGeoPath()'. Naming it makes this a value class: Python owns
  #  every C++ QGeoPath behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN8QGeoPathD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def path(self) -> QList[QGeoCoordinate]:
    """
    Calls Qt's 'const QList<QGeoCoordinate> &QGeoPath::path() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeopath.html#path

    Returns
    -------

    QList[QGeoCoordinate]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  const QList<QGeoCoordinate> &QGeoPath::path() const
    address = self.uglySide.call('ritual_ZNK8QGeoPath4pathEv')
    from . import QGeoCoordinate
    return QList[QGeoCoordinate]._cuteOwning(address)

  def variantPath(self) -> QList[QVariant]:
    """
    Calls Qt's 'QVariantList QGeoPath::variantPath() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeopath.html#variantPath

    Returns
    -------

    QList[QVariant]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QVariantList QGeoPath::variantPath() const
    address = self.uglySide.call('ritual_ZNK8QGeoPath11variantPathEv')
    from ..QtCore import QVariant
    return QList[QVariant]._cuteOwning(address)

  def width(self) -> float:
    """
    Calls Qt's 'qreal QGeoPath::width() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeopath.html#width
    """
    #  qreal QGeoPath::width() const
    return self.uglySide.call('ritual_ZNK8QGeoPath5widthEv')

  @overload(float, float)
  def translated(
      self,
      degreesLatitude: float,
      degreesLongitude: float,
  ) -> QGeoPath:
    """
    Calls Qt's 'QGeoPath QGeoPath::translated(double degreesLatitude, double
    degreesLongitude) const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeopath.html#translated

    Parameters
    ----------

    degreesLatitude : float
      Passed on as it is.

    degreesLongitude : float
      Passed on as it is.

    Returns
    -------

    QGeoPath
      A new cute QGeoPath around the copy Qt gave back. Python owns it.
    """
    #  QGeoPath QGeoPath::translated(double degreesLatitude, double
    #      degreesLongitude) const
    address = self.uglySide.call(
        'ritual_ZNK8QGeoPath10translatedEdd',
        degreesLatitude, degreesLongitude,
    )
    return QGeoPath._cuteOwning(address)

  @overload()
  @overload(int)
  @overload(int, int)
  def length(self, indexFrom: int = 0, indexTo: int = -1) -> float:
    """
    Calls Qt's 'double QGeoPath::length(qsizetype indexFrom, qsizetype
    indexTo) const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeopath.html#length

    Parameters
    ----------

    indexFrom : int
      Passed on as it is. May be left out, as in Qt: it is then 0.

    indexTo : int
      Passed on as it is. May be left out, as in Qt: it is then -1.
    """
    #  double QGeoPath::length(qsizetype indexFrom, qsizetype indexTo) const
    return self.uglySide.call(
        'ritual_ZNK8QGeoPath6lengthExx', indexFrom, indexTo,
    )

  def size(self) -> int:
    """
    Calls Qt's 'qsizetype QGeoPath::size() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeopath.html#size
    """
    #  qsizetype QGeoPath::size() const
    return self.uglySide.call('ritual_ZNK8QGeoPath4sizeEv')

  @overload(int)
  def coordinateAt(self, index: int) -> QGeoCoordinate:
    """
    Calls Qt's 'QGeoCoordinate QGeoPath::coordinateAt(qsizetype index)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeopath.html#coordinateAt

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    QGeoCoordinate
      A new cute QGeoCoordinate around the copy Qt gave back. Python owns it.
    """
    #  QGeoCoordinate QGeoPath::coordinateAt(qsizetype index) const
    address = self.uglySide.call(
        'ritual_ZNK8QGeoPath12coordinateAtEx', index,
    )
    from . import QGeoCoordinate
    return QGeoCoordinate._cuteOwning(address)

  @overload(QGeoCoordinate)
  def containsCoordinate(self, coordinate: QGeoCoordinate) -> bool:
    """
    Calls Qt's 'bool QGeoPath::containsCoordinate(const QGeoCoordinate
    &coordinate) const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeopath.html#containsCoordinate

    Parameters
    ----------

    coordinate : QGeoCoordinate
      Passed on as a value: Qt reads the C++ QGeoCoordinate, which stays
      Python's own.
    """
    #  bool QGeoPath::containsCoordinate(const QGeoCoordinate &coordinate)
    #      const
    return self.uglySide.call(
        'ritual_ZNK8QGeoPath18containsCoordinateERK14QGeoCoordinate',
        self._valueOf(coordinate),
    )

  def toString(self) -> str:
    """
    Calls Qt's 'QString QGeoPath::toString() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeopath.html#toString

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QGeoPath::toString() const
    return self.uglySide.call('ritual_ZNK8QGeoPath8toStringEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QList[QGeoCoordinate])
  def setPath(self, path: QList[QGeoCoordinate]) -> None:
    """
    Calls Qt's 'void QGeoPath::setPath(const QList<QGeoCoordinate> &path)'.

    Qt's own words: https://doc.qt.io/qt-6/qgeopath.html#setPath

    Parameters
    ----------

    path : QList[QGeoCoordinate]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QGeoPath::setPath(const QList<QGeoCoordinate> &path)
    self.uglySide.call(
        'ritual_ZN8QGeoPath7setPathERK5QListI14QGeoCoordinateE',
        self._valueOf(path),
    )

  @overload(QList[QVariant])
  def setVariantPath(self, path: QList[QVariant]) -> None:
    """
    Calls Qt's 'void QGeoPath::setVariantPath(const QVariantList &path)'.

    Qt's own words: https://doc.qt.io/qt-6/qgeopath.html#setVariantPath

    Parameters
    ----------

    path : QList[QVariant]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QGeoPath::setVariantPath(const QVariantList &path)
    self.uglySide.call(
        'ritual_ZN8QGeoPath14setVariantPathERK5QListI8QVariantE',
        self._valueOf(path),
    )

  @overload(float)
  def setWidth(self, width: float) -> None:
    """
    Calls Qt's 'void QGeoPath::setWidth(const qreal &width)'.

    Qt's own words: https://doc.qt.io/qt-6/qgeopath.html#setWidth

    Parameters
    ----------

    width : float
      Passed on as it is.
    """
    #  void QGeoPath::setWidth(const qreal &width)
    self.uglySide.call('ritual_ZN8QGeoPath8setWidthERKd', width)

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
    Notes what was given, for Qt's 'QGeoPath::QGeoPath()', which is called at
    the first use.

    Qt's own words: https://doc.qt.io/qt-6/qgeopath.html#QGeoPath
    """
    #  QGeoPath::QGeoPath()
    self._noteCreation(QGeoPath, lambda: Rituals.call(
        'ritual_ZN8QGeoPathC1Ev',
    ))

  @overload(QList[QGeoCoordinate])
  @overload(QList[QGeoCoordinate], float)
  def __init__(
      self,
      path: QList[QGeoCoordinate],
      width: float = 0.0,
  ) -> None:
    """
    Notes what was given, for Qt's 'QGeoPath::QGeoPath(const
    QList<QGeoCoordinate> &path, const qreal &width)', which is called at the
    first use.

    Qt's own words: https://doc.qt.io/qt-6/qgeopath.html#QGeoPath

    Parameters
    ----------

    path : QList[QGeoCoordinate]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    width : float
      Passed on as it is. May be left out, as in Qt: it is then 0.0.
    """
    #  QGeoPath::QGeoPath(const QList<QGeoCoordinate> &path, const qreal
    #      &width)
    self._noteCreation(QGeoPath, lambda: Rituals.call(
        'ritual_ZN8QGeoPathC1ERK5QListI14QGeoCoordinateERKd',
        self._valueOf(path), width,
    ))

  @overload(THIS)
  def __init__(self, other: QGeoPath) -> None:
    """
    Notes what was given, for Qt's 'QGeoPath::QGeoPath(const QGeoPath
    &other)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qgeopath.html#QGeoPath

    Parameters
    ----------

    other : QGeoPath
      Passed on as a value: Qt reads the C++ QGeoPath, which stays Python's
      own.
    """
    #  QGeoPath::QGeoPath(const QGeoPath &other)
    self._noteCreation(QGeoPath, lambda: Rituals.call(
        'ritual_ZN8QGeoPathC1ERKS_', self._valueOf(other),
    ))

  @overload(QGeoShape)
  def __init__(self, other: QGeoShape) -> None:
    """
    Notes what was given, for Qt's 'QGeoPath::QGeoPath(const QGeoShape
    &other)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qgeopath.html#QGeoPath

    Parameters
    ----------

    other : QGeoShape
      Passed on as a value: Qt reads the C++ QGeoShape, which stays Python's
      own.
    """
    #  QGeoPath::QGeoPath(const QGeoShape &other)
    self._noteCreation(QGeoPath, lambda: Rituals.call(
        'ritual_ZN8QGeoPathC1ERK9QGeoShape', self._valueOf(other),
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

  def clearPath(self) -> None:
    """
    Calls Qt's 'void QGeoPath::clearPath()'.

    Qt's own words: https://doc.qt.io/qt-6/qgeopath.html#clearPath
    """
    #  void QGeoPath::clearPath()
    self.uglySide.call('ritual_ZN8QGeoPath9clearPathEv')

  @overload(float, float)
  def translate(
      self,
      degreesLatitude: float,
      degreesLongitude: float,
  ) -> None:
    """
    Calls Qt's 'void QGeoPath::translate(double degreesLatitude, double
    degreesLongitude)'.

    Qt's own words: https://doc.qt.io/qt-6/qgeopath.html#translate

    Parameters
    ----------

    degreesLatitude : float
      Passed on as it is.

    degreesLongitude : float
      Passed on as it is.
    """
    #  void QGeoPath::translate(double degreesLatitude, double
    #      degreesLongitude)
    self.uglySide.call(
        'ritual_ZN8QGeoPath9translateEdd', degreesLatitude, degreesLongitude,
    )

  @overload(QGeoCoordinate)
  def addCoordinate(self, coordinate: QGeoCoordinate) -> None:
    """
    Calls Qt's 'void QGeoPath::addCoordinate(const QGeoCoordinate
    &coordinate)'.

    Qt's own words: https://doc.qt.io/qt-6/qgeopath.html#addCoordinate

    Parameters
    ----------

    coordinate : QGeoCoordinate
      Passed on as a value: Qt reads the C++ QGeoCoordinate, which stays
      Python's own.
    """
    #  void QGeoPath::addCoordinate(const QGeoCoordinate &coordinate)
    self.uglySide.call(
        'ritual_ZN8QGeoPath13addCoordinateERK14QGeoCoordinate',
        self._valueOf(coordinate),
    )

  @overload(int, QGeoCoordinate)
  def insertCoordinate(self, index: int, coordinate: QGeoCoordinate) -> None:
    """
    Calls Qt's 'void QGeoPath::insertCoordinate(qsizetype index, const
    QGeoCoordinate &coordinate)'.

    Qt's own words: https://doc.qt.io/qt-6/qgeopath.html#insertCoordinate

    Parameters
    ----------

    index : int
      Passed on as it is.

    coordinate : QGeoCoordinate
      Passed on as a value: Qt reads the C++ QGeoCoordinate, which stays
      Python's own.
    """
    #  void QGeoPath::insertCoordinate(qsizetype index, const QGeoCoordinate
    #      &coordinate)
    self.uglySide.call(
        'ritual_ZN8QGeoPath16insertCoordinateExRK14QGeoCoordinate',
        index, self._valueOf(coordinate),
    )

  @overload(int, QGeoCoordinate)
  def replaceCoordinate(
      self,
      index: int,
      coordinate: QGeoCoordinate,
  ) -> None:
    """
    Calls Qt's 'void QGeoPath::replaceCoordinate(qsizetype index, const
    QGeoCoordinate &coordinate)'.

    Qt's own words: https://doc.qt.io/qt-6/qgeopath.html#replaceCoordinate

    Parameters
    ----------

    index : int
      Passed on as it is.

    coordinate : QGeoCoordinate
      Passed on as a value: Qt reads the C++ QGeoCoordinate, which stays
      Python's own.
    """
    #  void QGeoPath::replaceCoordinate(qsizetype index, const QGeoCoordinate
    #      &coordinate)
    self.uglySide.call(
        'ritual_ZN8QGeoPath17replaceCoordinateExRK14QGeoCoordinate',
        index, self._valueOf(coordinate),
    )

  @overload(QGeoCoordinate)
  def removeCoordinate(self, coordinate: QGeoCoordinate) -> None:
    """
    Calls Qt's 'void QGeoPath::removeCoordinate(const QGeoCoordinate
    &coordinate)'.

    Qt's own words: https://doc.qt.io/qt-6/qgeopath.html#removeCoordinate

    Parameters
    ----------

    coordinate : QGeoCoordinate
      Passed on as a value: Qt reads the C++ QGeoCoordinate, which stays
      Python's own.
    """
    #  void QGeoPath::removeCoordinate(const QGeoCoordinate &coordinate)
    self.uglySide.call(
        'ritual_ZN8QGeoPath16removeCoordinateERK14QGeoCoordinate',
        self._valueOf(coordinate),
    )

  @overload(int)
  def removeCoordinate(self, index: int) -> None:
    """
    Calls Qt's 'void QGeoPath::removeCoordinate(qsizetype index)'.

    Qt's own words: https://doc.qt.io/qt-6/qgeopath.html#removeCoordinate

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  void QGeoPath::removeCoordinate(qsizetype index)
    self.uglySide.call('ritual_ZN8QGeoPath16removeCoordinateEx', index)

  def d_func(self) -> Optional[QGeoPathPrivate]:
    """
    Calls Qt's 'QGeoPathPrivate *QGeoPath::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qgeopath.html#d_func

    Returns
    -------

    Optional[QGeoPathPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QGeoPathPrivate *QGeoPath::d_func()
    address = self.uglySide.call('ritual_ZN8QGeoPath6d_funcEv')
    from . import QGeoPathPrivate
    return QGeoPathPrivate._cuteAt(address)
