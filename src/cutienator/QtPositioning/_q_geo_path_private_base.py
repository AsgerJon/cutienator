"""
QGeoPathPrivateBase binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtPositioning/6.12.0/QtPositioning/private/qgeopath_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QGeoPathPrivateBase to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..QtCore import QList
from . import QGeoShapePrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from . import QGeoCoordinate, QGeoRectangle
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QGeoCoordinate = WAIT['QGeoCoordinate']


class QGeoPathPrivateBase(QGeoShapePrivate):
  """
  The cute side of Qt's QGeoPathPrivateBase: a plain Python object standing
  in front of one C++ QGeoPathPrivateBase.

  It is built on the cute 'QGeoShapePrivate', as Qt's QGeoPathPrivateBase is
  built on Qt's QGeoShapePrivate, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QGeoPathPrivateBase that has a ritual and that
  Python can call so far, 19 names in all: 'isValid', 'isEmpty', 'center',
  'boundingGeoRectangle', 'hash', 'path', 'length', 'size', 'coordinateAt',
  'containsCoordinate', 'translate', 'setPath', 'clearPath', 'addCoordinate',
  'insertCoordinate', 'replaceCoordinate', 'removeCoordinate', 'markDirty',
  'ensureBoundingBoxUpdated'. It can be made from Python, in 2 ways; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QGeoPathPrivateBase::QGeoPathPrivateBase(const QGeoPathPrivateBase
    &other)': takes a type Python has no way to hand over yet.
  - Qt's 'QGeoPathPrivateBase::~QGeoPathPrivateBase()': the destructor:
    Python never removes a C++ QGeoPathPrivateBase.
  - Qt's 'bool QGeoPathPrivateBase::operator==(const QGeoShapePrivate &other)
    const': takes a type Python has no way to hand over yet.

  What to expect
  --------------

  - The C++ QGeoPathPrivateBase is created at the first use, not by
    'QGeoPathPrivateBase(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QGeoPathPrivateBase.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QGeoPathPrivateBase'

  #  A C++ QGeoPathPrivateBase Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QGeoPathPrivateBase'

  #  The functions Qt calls itself that QGeoPathPrivateBase is the first to
  #  declare and that cannot be handed to Python yet, each as Qt declares it.
  #  A class of a program that writes one of them anew is refused, since Qt
  #  would never call what it wrote; see 'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'path': (
          'const QList<QGeoCoordinate> &QGeoPathPrivateBase::path() const',
      ),
      'setPath': (
          'void QGeoPathPrivateBase::setPath(const QList<QGeoCoordinate> &)',
      ),
  }

  #  The functions Qt calls itself that QGeoPathPrivateBase is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'length': (
          ('_ZNK19QGeoPathPrivateBase6lengthExx',
           ('double', 'number', ''),
           (
               ('long long', 'number', ''),
               ('long long', 'number', ''),
           )),
      ),
      'size': (
          ('_ZNK19QGeoPathPrivateBase4sizeEv',
           ('long long', 'number', ''),
           ()),
      ),
      'coordinateAt': (
          ('_ZNK19QGeoPathPrivateBase12coordinateAtEx',
           ('address', 'value', 'QtPositioning:QGeoCoordinate'),
           (
               ('long long', 'number', ''),
           )),
      ),
      'containsCoordinate': (
          ('_ZNK19QGeoPathPrivateBase18containsCoordinateERK14QGeoCoordinat'
           'e',
           ('bool', 'number', ''),
           (
               ('address', 'value', 'QtPositioning:QGeoCoordinate'),
           )),
      ),
      'translate': (
          ('_ZN19QGeoPathPrivateBase9translateEdd',
           ('nothing', 'nothing', ''),
           (
               ('double', 'number', ''),
               ('double', 'number', ''),
           )),
      ),
      'clearPath': (
          ('_ZN19QGeoPathPrivateBase9clearPathEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'addCoordinate': (
          ('_ZN19QGeoPathPrivateBase13addCoordinateERK14QGeoCoordinate',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtPositioning:QGeoCoordinate'),
           )),
      ),
      'insertCoordinate': (
          ('_ZN19QGeoPathPrivateBase16insertCoordinateExRK14QGeoCoordinate',
           ('nothing', 'nothing', ''),
           (
               ('long long', 'number', ''),
               ('address', 'value', 'QtPositioning:QGeoCoordinate'),
           )),
      ),
      'replaceCoordinate': (
          ('_ZN19QGeoPathPrivateBase17replaceCoordinateExRK14QGeoCoordinate',
           ('nothing', 'nothing', ''),
           (
               ('long long', 'number', ''),
               ('address', 'value', 'QtPositioning:QGeoCoordinate'),
           )),
      ),
      'removeCoordinate': (
          ('_ZN19QGeoPathPrivateBase16removeCoordinateERK14QGeoCoordinate',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtPositioning:QGeoCoordinate'),
           )),
          ('_ZN19QGeoPathPrivateBase16removeCoordinateEx',
           ('nothing', 'nothing', ''),
           (
               ('long long', 'number', ''),
           )),
      ),
      'markDirty': (
          ('_ZN19QGeoPathPrivateBase9markDirtyEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool QGeoPathPrivateBase::isValid() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeopathprivatebase.html#isValid
    """
    #  bool QGeoPathPrivateBase::isValid() const
    ritual = 'ritual_ZNK19QGeoPathPrivateBase7isValidEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK19QGeoPathPrivateBase7isValidEv'
    return self.uglySide.call(ritual)

  def isEmpty(self) -> bool:
    """
    Calls Qt's 'bool QGeoPathPrivateBase::isEmpty() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeopathprivatebase.html#isEmpty
    """
    #  bool QGeoPathPrivateBase::isEmpty() const
    ritual = 'ritual_ZNK19QGeoPathPrivateBase7isEmptyEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK19QGeoPathPrivateBase7isEmptyEv'
    return self.uglySide.call(ritual)

  def center(self) -> QGeoCoordinate:
    """
    Calls Qt's 'QGeoCoordinate QGeoPathPrivateBase::center() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeopathprivatebase.html#center

    Returns
    -------

    QGeoCoordinate
      A new cute QGeoCoordinate around the copy Qt gave back. Python owns it.
    """
    #  QGeoCoordinate QGeoPathPrivateBase::center() const
    ritual = 'ritual_ZNK19QGeoPathPrivateBase6centerEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK19QGeoPathPrivateBase6centerEv'
    address = self.uglySide.call(ritual)
    from . import QGeoCoordinate
    return QGeoCoordinate._cuteOwning(address)

  def boundingGeoRectangle(self) -> QGeoRectangle:
    """
    Calls Qt's 'QGeoRectangle QGeoPathPrivateBase::boundingGeoRectangle()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeopathprivatebase.html#boundingGeoRectangle

    Returns
    -------

    QGeoRectangle
      A new cute QGeoRectangle around the copy Qt gave back. Python owns it.
    """
    #  QGeoRectangle QGeoPathPrivateBase::boundingGeoRectangle() const
    ritual = 'ritual_ZNK19QGeoPathPrivateBase20boundingGeoRectangleEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK19QGeoPathPrivateBase20boundingGeoRectangleEv'
    address = self.uglySide.call(ritual)
    from . import QGeoRectangle
    return QGeoRectangle._cuteOwning(address)

  @overload(int)
  def hash(self, seed: int) -> int:
    """
    Calls Qt's 'size_t QGeoPathPrivateBase::hash(size_t seed) const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeopathprivatebase.html#hash

    Parameters
    ----------

    seed : int
      Passed on as it is.
    """
    #  size_t QGeoPathPrivateBase::hash(size_t seed) const
    ritual = 'ritual_ZNK19QGeoPathPrivateBase4hashEm'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK19QGeoPathPrivateBase4hashEm'
    return self.uglySide.call(ritual, seed)

  def path(self) -> QList[QGeoCoordinate]:
    """
    Calls Qt's 'const QList<QGeoCoordinate> &QGeoPathPrivateBase::path()
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeopathprivatebase.html#path

    Returns
    -------

    QList[QGeoCoordinate]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  const QList<QGeoCoordinate> &QGeoPathPrivateBase::path() const
    address = self.uglySide.call('ritual_ZNK19QGeoPathPrivateBase4pathEv')
    from . import QGeoCoordinate
    return QList[QGeoCoordinate]._cuteOwning(address)

  @overload(int, int)
  def length(self, indexFrom: int, indexTo: int) -> float:
    """
    Calls Qt's 'double QGeoPathPrivateBase::length(qsizetype indexFrom,
    qsizetype indexTo) const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeopathprivatebase.html#length

    Parameters
    ----------

    indexFrom : int
      Passed on as it is.

    indexTo : int
      Passed on as it is.
    """
    #  double QGeoPathPrivateBase::length(qsizetype indexFrom, qsizetype
    #      indexTo) const
    ritual = 'ritual_ZNK19QGeoPathPrivateBase6lengthExx'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK19QGeoPathPrivateBase6lengthExx'
    return self.uglySide.call(ritual, indexFrom, indexTo)

  def size(self) -> int:
    """
    Calls Qt's 'qsizetype QGeoPathPrivateBase::size() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeopathprivatebase.html#size
    """
    #  qsizetype QGeoPathPrivateBase::size() const
    ritual = 'ritual_ZNK19QGeoPathPrivateBase4sizeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK19QGeoPathPrivateBase4sizeEv'
    return self.uglySide.call(ritual)

  @overload(int)
  def coordinateAt(self, index: int) -> QGeoCoordinate:
    """
    Calls Qt's 'QGeoCoordinate QGeoPathPrivateBase::coordinateAt(qsizetype
    index) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeopathprivatebase.html#coordinateAt

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    QGeoCoordinate
      A new cute QGeoCoordinate around the copy Qt gave back. Python owns it.
    """
    #  QGeoCoordinate QGeoPathPrivateBase::coordinateAt(qsizetype index)
    #      const
    ritual = 'ritual_ZNK19QGeoPathPrivateBase12coordinateAtEx'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK19QGeoPathPrivateBase12coordinateAtEx'
    address = self.uglySide.call(ritual, index)
    from . import QGeoCoordinate
    return QGeoCoordinate._cuteOwning(address)

  @overload(QGeoCoordinate)
  def containsCoordinate(self, coordinate: QGeoCoordinate) -> bool:
    """
    Calls Qt's 'bool QGeoPathPrivateBase::containsCoordinate(const
    QGeoCoordinate &coordinate) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeopathprivatebase.html#containsCoordinate

    Parameters
    ----------

    coordinate : QGeoCoordinate
      Passed on as a value: Qt reads the C++ QGeoCoordinate, which stays
      Python's own.
    """
    #  bool QGeoPathPrivateBase::containsCoordinate(const QGeoCoordinate
    #      &coordinate) const
    ritual = (
        'ritual_ZNK19QGeoPathPrivateBase18containsCoordinateERK14QGeoCoordi'
        'nate')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK19QGeoPathPrivateBase18containsCoordinateERK14QGeo'
          'Coordinate')
    return self.uglySide.call(ritual, self._valueOf(coordinate))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QList[QGeoCoordinate])
  def setPath(self, path: QList[QGeoCoordinate]) -> None:
    """
    Calls Qt's 'void QGeoPathPrivateBase::setPath(const QList<QGeoCoordinate>
    &path)'.

    Qt's own words: https://doc.qt.io/qt-6/qgeopathprivatebase.html#setPath

    Parameters
    ----------

    path : QList[QGeoCoordinate]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QGeoPathPrivateBase::setPath(const QList<QGeoCoordinate> &path)
    self.uglySide.call(
        'ritual_ZN19QGeoPathPrivateBase7setPathERK5QListI14QGeoCoordinateE',
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
    Notes what was given, for Qt's
    'QGeoPathPrivateBase::QGeoPathPrivateBase()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeopathprivatebase.html#QGeoPathPrivateBase
    """
    #  QGeoPathPrivateBase::QGeoPathPrivateBase()
    self._noteCreation(QGeoPathPrivateBase, lambda: Rituals.call(
        'ritual_ZN19QGeoPathPrivateBaseC1Ev',
    ))

  @overload(QList[QGeoCoordinate])
  def __init__(self, path: QList[QGeoCoordinate]) -> None:
    """
    Notes what was given, for Qt's
    'QGeoPathPrivateBase::QGeoPathPrivateBase(const QList<QGeoCoordinate>
    &path)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeopathprivatebase.html#QGeoPathPrivateBase

    Parameters
    ----------

    path : QList[QGeoCoordinate]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  QGeoPathPrivateBase::QGeoPathPrivateBase(const QList<QGeoCoordinate>
    #      &path)
    self._noteCreation(QGeoPathPrivateBase, lambda: Rituals.call(
        'ritual_ZN19QGeoPathPrivateBaseC1ERK5QListI14QGeoCoordinateE',
        self._valueOf(path),
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
    Calls Qt's 'void QGeoPathPrivateBase::translate(double degreesLatitude,
    double degreesLongitude)'.

    Qt's own words: https://doc.qt.io/qt-6/qgeopathprivatebase.html#translate

    Parameters
    ----------

    degreesLatitude : float
      Passed on as it is.

    degreesLongitude : float
      Passed on as it is.
    """
    #  void QGeoPathPrivateBase::translate(double degreesLatitude, double
    #      degreesLongitude)
    ritual = 'ritual_ZN19QGeoPathPrivateBase9translateEdd'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QGeoPathPrivateBase9translateEdd'
    self.uglySide.call(ritual, degreesLatitude, degreesLongitude)

  def clearPath(self) -> None:
    """
    Calls Qt's 'void QGeoPathPrivateBase::clearPath()'.

    Qt's own words: https://doc.qt.io/qt-6/qgeopathprivatebase.html#clearPath
    """
    #  void QGeoPathPrivateBase::clearPath()
    ritual = 'ritual_ZN19QGeoPathPrivateBase9clearPathEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QGeoPathPrivateBase9clearPathEv'
    self.uglySide.call(ritual)

  @overload(QGeoCoordinate)
  def addCoordinate(self, coordinate: QGeoCoordinate) -> None:
    """
    Calls Qt's 'void QGeoPathPrivateBase::addCoordinate(const QGeoCoordinate
    &coordinate)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeopathprivatebase.html#addCoordinate

    Parameters
    ----------

    coordinate : QGeoCoordinate
      Passed on as a value: Qt reads the C++ QGeoCoordinate, which stays
      Python's own.
    """
    #  void QGeoPathPrivateBase::addCoordinate(const QGeoCoordinate
    #      &coordinate)
    ritual = (
        'ritual_ZN19QGeoPathPrivateBase13addCoordinateERK14QGeoCoordinate')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QGeoPathPrivateBase13addCoordinateERK14QGeoCoordi'
          'nate')
    self.uglySide.call(ritual, self._valueOf(coordinate))

  @overload(int, QGeoCoordinate)
  def insertCoordinate(self, index: int, coordinate: QGeoCoordinate) -> None:
    """
    Calls Qt's 'void QGeoPathPrivateBase::insertCoordinate(qsizetype index,
    const QGeoCoordinate &coordinate)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeopathprivatebase.html#insertCoordinate

    Parameters
    ----------

    index : int
      Passed on as it is.

    coordinate : QGeoCoordinate
      Passed on as a value: Qt reads the C++ QGeoCoordinate, which stays
      Python's own.
    """
    #  void QGeoPathPrivateBase::insertCoordinate(qsizetype index, const
    #      QGeoCoordinate &coordinate)
    ritual = (
        'ritual_ZN19QGeoPathPrivateBase16insertCoordinateExRK14QGeoCoordina'
        'te')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QGeoPathPrivateBase16insertCoordinateExRK14QGeoCo'
          'ordinate')
    self.uglySide.call(ritual, index, self._valueOf(coordinate))

  @overload(int, QGeoCoordinate)
  def replaceCoordinate(
      self,
      index: int,
      coordinate: QGeoCoordinate,
  ) -> None:
    """
    Calls Qt's 'void QGeoPathPrivateBase::replaceCoordinate(qsizetype index,
    const QGeoCoordinate &coordinate)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeopathprivatebase.html#replaceCoordinate

    Parameters
    ----------

    index : int
      Passed on as it is.

    coordinate : QGeoCoordinate
      Passed on as a value: Qt reads the C++ QGeoCoordinate, which stays
      Python's own.
    """
    #  void QGeoPathPrivateBase::replaceCoordinate(qsizetype index, const
    #      QGeoCoordinate &coordinate)
    ritual = (
        'ritual_ZN19QGeoPathPrivateBase17replaceCoordinateExRK14QGeoCoordin'
        'ate')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QGeoPathPrivateBase17replaceCoordinateExRK14QGeoC'
          'oordinate')
    self.uglySide.call(ritual, index, self._valueOf(coordinate))

  @overload(QGeoCoordinate)
  def removeCoordinate(self, coordinate: QGeoCoordinate) -> None:
    """
    Calls Qt's 'void QGeoPathPrivateBase::removeCoordinate(const
    QGeoCoordinate &coordinate)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeopathprivatebase.html#removeCoordinate

    Parameters
    ----------

    coordinate : QGeoCoordinate
      Passed on as a value: Qt reads the C++ QGeoCoordinate, which stays
      Python's own.
    """
    #  void QGeoPathPrivateBase::removeCoordinate(const QGeoCoordinate
    #      &coordinate)
    ritual = (
        'ritual_ZN19QGeoPathPrivateBase16removeCoordinateERK14QGeoCoordinat'
        'e')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QGeoPathPrivateBase16removeCoordinateERK14QGeoCoo'
          'rdinate')
    self.uglySide.call(ritual, self._valueOf(coordinate))

  @overload(int)
  def removeCoordinate(self, index: int) -> None:
    """
    Calls Qt's 'void QGeoPathPrivateBase::removeCoordinate(qsizetype index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeopathprivatebase.html#removeCoordinate

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  void QGeoPathPrivateBase::removeCoordinate(qsizetype index)
    ritual = 'ritual_ZN19QGeoPathPrivateBase16removeCoordinateEx'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QGeoPathPrivateBase16removeCoordinateEx'
    self.uglySide.call(ritual, index)

  def markDirty(self) -> None:
    """
    Calls Qt's 'void QGeoPathPrivateBase::markDirty()'.

    Qt's own words: https://doc.qt.io/qt-6/qgeopathprivatebase.html#markDirty
    """
    #  void QGeoPathPrivateBase::markDirty()
    ritual = 'ritual_ZN19QGeoPathPrivateBase9markDirtyEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QGeoPathPrivateBase9markDirtyEv'
    self.uglySide.call(ritual)

  def ensureBoundingBoxUpdated(self) -> None:
    """
    Calls Qt's 'void QGeoPathPrivateBase::ensureBoundingBoxUpdated() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeopathprivatebase.html#ensureBoundingBoxUpdated
    """
    #  void QGeoPathPrivateBase::ensureBoundingBoxUpdated() const
    self.uglySide.call(
        'ritual_ZNK19QGeoPathPrivateBase24ensureBoundingBoxUpdatedEv',
    )
