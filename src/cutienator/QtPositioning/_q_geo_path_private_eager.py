"""
QGeoPathPrivateEager binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtPositioning/6.12.0/QtPositioning/private/qgeopath_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QGeoPathPrivateEager to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..QtCore import QList
from . import QGeoPathPrivate, QGeoShapePrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QGeoCoordinate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QGeoCoordinate = WAIT['QGeoCoordinate']


class QGeoPathPrivateEager(QGeoPathPrivate):
  """
  The cute side of Qt's QGeoPathPrivateEager: a plain Python object standing
  in front of one C++ QGeoPathPrivateEager.

  It is built on the cute 'QGeoPathPrivate', as Qt's QGeoPathPrivateEager is
  built on Qt's QGeoPathPrivate, and has everything that class has.

  C++ hands a QGeoPathPrivateEager around as a copy, so every C++
  QGeoPathPrivateEager behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QGeoPathPrivateEager that has a ritual and that
  Python can call so far, 4 names in all: 'clone', 'translate', 'markDirty',
  'addCoordinate'. It can be made from Python, in 3 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QGeoPathPrivateEager::~QGeoPathPrivateEager()': the destructor:
    Python removes its C++ QGeoPathPrivateEager by it, and has no other use
    for it.

  What has no ritual
  ------------------

  1 of the 9 functions Qt declares: 1 cannot be called and cannot be called
  through the meta-object and cannot be copied.

  What to expect
  --------------

  - The C++ QGeoPathPrivateEager is created at the first use, not by
    'QGeoPathPrivateEager(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QGeoPathPrivateEager back gives a copy the ritual
    made for Python, in a new cute QGeoPathPrivateEager.
  - Each name of Qt's QGeoPathPrivateEager that has no cute function yet,
    'updateBoundingBox', holds a function that raises 'NotImplementedError',
    and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QGeoPathPrivateEager'

  #  Qt's '~QGeoPathPrivateEager()'. Naming it makes this a value class:
  #  Python owns every C++ QGeoPathPrivateEager behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN20QGeoPathPrivateEagerD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def clone(self) -> Optional[QGeoShapePrivate]:
    """
    Calls Qt's 'QGeoShapePrivate *QGeoPathPrivateEager::clone() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeopathprivateeager.html#clone

    Returns
    -------

    Optional[QGeoShapePrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QGeoShapePrivate *QGeoPathPrivateEager::clone() const
    address = self.uglySide.call('ritual_ZNK20QGeoPathPrivateEager5cloneEv')
    return QGeoShapePrivate._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

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
    'QGeoPathPrivateEager::QGeoPathPrivateEager()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeopathprivateeager.html#QGeoPathPrivateEager
    """
    #  QGeoPathPrivateEager::QGeoPathPrivateEager()
    self._noteCreation(QGeoPathPrivateEager, lambda: Rituals.call(
        'ritual_ZN20QGeoPathPrivateEagerC1Ev',
    ))

  @overload(QList[QGeoCoordinate])
  @overload(QList[QGeoCoordinate], float)
  def __init__(
      self,
      path: QList[QGeoCoordinate],
      width: float = 0.0,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QGeoPathPrivateEager::QGeoPathPrivateEager(const QList<QGeoCoordinate>
    &path, const qreal width)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeopathprivateeager.html#QGeoPathPrivateEager

    Parameters
    ----------

    path : QList[QGeoCoordinate]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    width : float
      Passed on as it is. May be left out, as in Qt: it is then 0.0.
    """
    #  QGeoPathPrivateEager::QGeoPathPrivateEager(const QList<QGeoCoordinate>
    #      &path, const qreal width)
    self._noteCreation(QGeoPathPrivateEager, lambda: Rituals.call(
        'ritual_ZN20QGeoPathPrivateEagerC1ERK5QListI14QGeoCoordinateEd',
        self._valueOf(path), width,
    ))

  @overload(THIS)
  def __init__(self, other: QGeoPathPrivateEager) -> None:
    """
    Notes what was given, for Qt's
    'QGeoPathPrivateEager::QGeoPathPrivateEager(const QGeoPathPrivateEager
    &other)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeopathprivateeager.html#QGeoPathPrivateEager

    Parameters
    ----------

    other : QGeoPathPrivateEager
      Passed on as a value: Qt reads the C++ QGeoPathPrivateEager, which
      stays Python's own.
    """
    #  QGeoPathPrivateEager::QGeoPathPrivateEager(const QGeoPathPrivateEager
    #      &other)
    self._noteCreation(QGeoPathPrivateEager, lambda: Rituals.call(
        'ritual_ZN20QGeoPathPrivateEagerC1ERKS_', self._valueOf(other),
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
    Calls Qt's 'void QGeoPathPrivateEager::translate(double degreesLatitude,
    double degreesLongitude)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeopathprivateeager.html#translate

    Parameters
    ----------

    degreesLatitude : float
      Passed on as it is.

    degreesLongitude : float
      Passed on as it is.
    """
    #  void QGeoPathPrivateEager::translate(double degreesLatitude, double
    #      degreesLongitude)
    self.uglySide.call(
        'ritual_ZN20QGeoPathPrivateEager9translateEdd',
        degreesLatitude, degreesLongitude,
    )

  def markDirty(self) -> None:
    """
    Calls Qt's 'void QGeoPathPrivateEager::markDirty()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeopathprivateeager.html#markDirty
    """
    #  void QGeoPathPrivateEager::markDirty()
    self.uglySide.call('ritual_ZN20QGeoPathPrivateEager9markDirtyEv')

  @overload(QGeoCoordinate)
  def addCoordinate(self, coordinate: QGeoCoordinate) -> None:
    """
    Calls Qt's 'void QGeoPathPrivateEager::addCoordinate(const QGeoCoordinate
    &coordinate)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeopathprivateeager.html#addCoordinate

    Parameters
    ----------

    coordinate : QGeoCoordinate
      Passed on as a value: Qt reads the C++ QGeoCoordinate, which stays
      Python's own.
    """
    #  void QGeoPathPrivateEager::addCoordinate(const QGeoCoordinate
    #      &coordinate)
    self.uglySide.call(
        'ritual_ZN20QGeoPathPrivateEager13addCoordinateERK14QGeoCoordinate',
        self._valueOf(coordinate),
    )

  @staticmethod
  def updateBoundingBox(*__, **_) -> Never:
    """
    Qt's 'void QGeoPathPrivateEager::updateBoundingBox()': cannot be called
    and cannot be called through the meta-object and cannot be copied: no
    header file has its code, Qt's source does not mark it or its class for
    use from outside Qt or writes it 'inline' or nowhere, and it is no
    signal, slot or invokable function giving back nothing, of a class built
    on QObject, and Qt's source has no code for it that could be told from
    the rest.
    """
    raise NotImplementedError(
        "'QGeoPathPrivateEager.updateBoundingBox' has no cute function yet. "
        "Qt's 'void QGeoPathPrivateEager::updateBoundingBox()': cannot be "
        "called and cannot be called through the meta-object and cannot be "
        "copied: no header file has its code, Qt's source does not mark it "
        "or its class for use from outside Qt or writes it 'inline' or "
        "nowhere, and it is no signal, slot or invokable function giving "
        "back nothing, of a class built on QObject, and Qt's source has no "
        "code for it that could be told from the rest.")
