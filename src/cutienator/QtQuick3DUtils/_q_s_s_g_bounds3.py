"""
QSSGBounds3 binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3DUtils/6.12.0/QtQuick3DUtils/private/qssgbounds3_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QSSGBounds3 to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import Qt

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from ..QtGui import QMatrix4x4, QVector3D
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QMatrix4x4 = WAIT['QMatrix4x4']
  QVector3D = WAIT['QVector3D']


class QSSGBounds3(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QSSGBounds3: a plain Python object standing in front
  of one C++ QSSGBounds3.

  C++ hands a QSSGBounds3 around as a copy, so every C++ QSSGBounds3 behind a
  cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QSSGBounds3 that has a ritual and that Python can
  call so far, 18 names in all: 'boundsOfPoints', 'centerExtents',
  'setEmpty', 'setInfinite', 'include', 'isEmpty', 'intersects',
  'intersects1D', 'contains', 'isInside', 'center', 'extents', 'dimensions',
  'scale', 'fatten', 'isFinite', 'transform', 'getSupport'. It can be made
  from Python, in 3 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSSGBounds3::QSSGBounds3(const QSSGBoxPoints &points)': takes a
    type Python has no way to hand over yet.
  - Qt's 'QSSGBounds3 QSSGBounds3::basisExtent(const QVector3D &center, const
    QMatrix3x3 &basis, const QVector3D &extent)': takes a type Python has no
    way to hand over yet.
  - Qt's 'QSSGBounds3 QSSGBounds3::transform(const QMatrix3x3 &matrix, const
    QSSGBounds3 &bounds)': takes a type Python has no way to hand over yet.
  - Qt's 'QSSGBoxPoints QSSGBounds3::toQSSGBoxPointsNoEmptyCheck() const':
    gives a type Python has no way to take yet.
  - Qt's 'QSSGBoxPoints QSSGBounds3::toQSSGBoxPoints() const': gives a type
    Python has no way to take yet.
  - Qt's 'QSSGBounds3::~QSSGBounds3()': the destructor: Python removes its
    C++ QSSGBounds3 by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QSSGBounds3 is created at the first use, not by
    'QSSGBounds3(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QSSGBounds3 back gives a copy the ritual made for
    Python, in a new cute QSSGBounds3.
  - Each name of Qt's QSSGBounds3 that has no cute function yet,
    'basisExtent', 'toQSSGBoxPoints', 'toQSSGBoxPointsNoEmptyCheck', holds a
    function that raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QVector3D, QVector3D)
  def boundsOfPoints(v0: QVector3D, v1: QVector3D) -> QSSGBounds3:
    """
    Calls Qt's 'QSSGBounds3 QSSGBounds3::boundsOfPoints(const QVector3D &v0,
    const QVector3D &v1)'.

    Qt's own words: https://doc.qt.io/qt-6/qssgbounds3.html#boundsOfPoints

    Parameters
    ----------

    v0 : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.

    v1 : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.

    Returns
    -------

    QSSGBounds3
      A new cute QSSGBounds3 around the copy Qt gave back. Python owns it.
    """
    #  QSSGBounds3 QSSGBounds3::boundsOfPoints(const QVector3D &v0, const
    #      QVector3D &v1)
    address = Rituals.call(
        'ritual_ZN11QSSGBounds314boundsOfPointsERK9QVector3DS2_',
        CuteMixin._valueOf(v0), CuteMixin._valueOf(v1),
    )
    return QSSGBounds3._cuteOwning(address)

  @staticmethod
  @overload(QVector3D, QVector3D)
  def centerExtents(center: QVector3D, extent: QVector3D) -> QSSGBounds3:
    """
    Calls Qt's 'QSSGBounds3 QSSGBounds3::centerExtents(const QVector3D
    &center, const QVector3D &extent)'.

    Qt's own words: https://doc.qt.io/qt-6/qssgbounds3.html#centerExtents

    Parameters
    ----------

    center : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.

    extent : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.

    Returns
    -------

    QSSGBounds3
      A new cute QSSGBounds3 around the copy Qt gave back. Python owns it.
    """
    #  QSSGBounds3 QSSGBounds3::centerExtents(const QVector3D &center, const
    #      QVector3D &extent)
    address = Rituals.call(
        'ritual_ZN11QSSGBounds313centerExtentsERK9QVector3DS2_',
        CuteMixin._valueOf(center), CuteMixin._valueOf(extent),
    )
    return QSSGBounds3._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSSGBounds3'

  #  Qt's '~QSSGBounds3()'. Naming it makes this a value class: Python owns
  #  every C++ QSSGBounds3 behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN11QSSGBounds3D1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isEmpty(self) -> bool:
    """
    Calls Qt's 'bool QSSGBounds3::isEmpty() const'.

    Qt's own words: https://doc.qt.io/qt-6/qssgbounds3.html#isEmpty
    """
    #  bool QSSGBounds3::isEmpty() const
    return self.uglySide.call('ritual_ZNK11QSSGBounds37isEmptyEv')

  @overload(THIS)
  def intersects(self, b: QSSGBounds3) -> bool:
    """
    Calls Qt's 'bool QSSGBounds3::intersects(const QSSGBounds3 &b) const'.

    Qt's own words: https://doc.qt.io/qt-6/qssgbounds3.html#intersects

    Parameters
    ----------

    b : QSSGBounds3
      Passed on as a value: Qt reads the C++ QSSGBounds3, which stays
      Python's own.
    """
    #  bool QSSGBounds3::intersects(const QSSGBounds3 &b) const
    return self.uglySide.call(
        'ritual_ZNK11QSSGBounds310intersectsERKS_', self._valueOf(b),
    )

  @overload(THIS, int)
  def intersects1D(self, a: QSSGBounds3, axis: int) -> bool:
    """
    Calls Qt's 'bool QSSGBounds3::intersects1D(const QSSGBounds3 &a, quint32
    axis) const'.

    Qt's own words: https://doc.qt.io/qt-6/qssgbounds3.html#intersects1D

    Parameters
    ----------

    a : QSSGBounds3
      Passed on as a value: Qt reads the C++ QSSGBounds3, which stays
      Python's own.

    axis : int
      Passed on as it is.
    """
    #  bool QSSGBounds3::intersects1D(const QSSGBounds3 &a, quint32 axis)
    #      const
    return self.uglySide.call(
        'ritual_ZNK11QSSGBounds312intersects1DERKS_j',
        self._valueOf(a), axis,
    )

  @overload(QVector3D)
  def contains(self, v: QVector3D) -> bool:
    """
    Calls Qt's 'bool QSSGBounds3::contains(const QVector3D &v) const'.

    Qt's own words: https://doc.qt.io/qt-6/qssgbounds3.html#contains

    Parameters
    ----------

    v : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.
    """
    #  bool QSSGBounds3::contains(const QVector3D &v) const
    return self.uglySide.call(
        'ritual_ZNK11QSSGBounds38containsERK9QVector3D', self._valueOf(v),
    )

  @overload(THIS)
  def isInside(self, box: QSSGBounds3) -> bool:
    """
    Calls Qt's 'bool QSSGBounds3::isInside(const QSSGBounds3 &box) const'.

    Qt's own words: https://doc.qt.io/qt-6/qssgbounds3.html#isInside

    Parameters
    ----------

    box : QSSGBounds3
      Passed on as a value: Qt reads the C++ QSSGBounds3, which stays
      Python's own.
    """
    #  bool QSSGBounds3::isInside(const QSSGBounds3 &box) const
    return self.uglySide.call(
        'ritual_ZNK11QSSGBounds38isInsideERKS_', self._valueOf(box),
    )

  @overload()
  def center(self) -> QVector3D:
    """
    Calls Qt's 'QVector3D QSSGBounds3::center() const'.

    Qt's own words: https://doc.qt.io/qt-6/qssgbounds3.html#center

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  QVector3D QSSGBounds3::center() const
    address = self.uglySide.call('ritual_ZNK11QSSGBounds36centerEv')
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  @overload(int)
  def center(self, axis: int) -> float:
    """
    Calls Qt's 'float QSSGBounds3::center(quint32 axis) const'.

    Qt's own words: https://doc.qt.io/qt-6/qssgbounds3.html#center

    Parameters
    ----------

    axis : int
      Passed on as it is.
    """
    #  float QSSGBounds3::center(quint32 axis) const
    return self.uglySide.call('ritual_ZNK11QSSGBounds36centerEj', axis)

  @overload(int)
  def extents(self, axis: int) -> float:
    """
    Calls Qt's 'float QSSGBounds3::extents(quint32 axis) const'.

    Qt's own words: https://doc.qt.io/qt-6/qssgbounds3.html#extents

    Parameters
    ----------

    axis : int
      Passed on as it is.
    """
    #  float QSSGBounds3::extents(quint32 axis) const
    return self.uglySide.call('ritual_ZNK11QSSGBounds37extentsEj', axis)

  @overload()
  def extents(self) -> QVector3D:
    """
    Calls Qt's 'QVector3D QSSGBounds3::extents() const'.

    Qt's own words: https://doc.qt.io/qt-6/qssgbounds3.html#extents

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  QVector3D QSSGBounds3::extents() const
    address = self.uglySide.call('ritual_ZNK11QSSGBounds37extentsEv')
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  def dimensions(self) -> QVector3D:
    """
    Calls Qt's 'QVector3D QSSGBounds3::dimensions() const'.

    Qt's own words: https://doc.qt.io/qt-6/qssgbounds3.html#dimensions

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  QVector3D QSSGBounds3::dimensions() const
    address = self.uglySide.call('ritual_ZNK11QSSGBounds310dimensionsEv')
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  def isFinite(self) -> bool:
    """
    Calls Qt's 'bool QSSGBounds3::isFinite() const'.

    Qt's own words: https://doc.qt.io/qt-6/qssgbounds3.html#isFinite
    """
    #  bool QSSGBounds3::isFinite() const
    return self.uglySide.call('ritual_ZNK11QSSGBounds38isFiniteEv')

  @overload(QVector3D)
  def getSupport(self, direction: QVector3D) -> QVector3D:
    """
    Calls Qt's 'QVector3D QSSGBounds3::getSupport(const QVector3D &direction)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qssgbounds3.html#getSupport

    Parameters
    ----------

    direction : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  QVector3D QSSGBounds3::getSupport(const QVector3D &direction) const
    address = self.uglySide.call(
        'ritual_ZNK11QSSGBounds310getSupportERK9QVector3D',
        self._valueOf(direction),
    )
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def setEmpty(self) -> None:
    """
    Calls Qt's 'void QSSGBounds3::setEmpty()'.

    Qt's own words: https://doc.qt.io/qt-6/qssgbounds3.html#setEmpty
    """
    #  void QSSGBounds3::setEmpty()
    self.uglySide.call('ritual_ZN11QSSGBounds38setEmptyEv')

  def setInfinite(self) -> None:
    """
    Calls Qt's 'void QSSGBounds3::setInfinite()'.

    Qt's own words: https://doc.qt.io/qt-6/qssgbounds3.html#setInfinite
    """
    #  void QSSGBounds3::setInfinite()
    self.uglySide.call('ritual_ZN11QSSGBounds311setInfiniteEv')

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
    Notes what was given, for Qt's 'QSSGBounds3::QSSGBounds3()', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qssgbounds3.html#QSSGBounds3
    """
    #  QSSGBounds3::QSSGBounds3()
    self._noteCreation(QSSGBounds3, lambda: Rituals.call(
        'ritual_ZN11QSSGBounds3C1Ev',
    ))

  @overload(Qt.Initialization)
  def __init__(self, a0: Qt.Initialization) -> None:
    """
    Notes what was given, for Qt's
    'QSSGBounds3::QSSGBounds3(Qt::Initialization a0)', which is called at the
    first use.

    Qt's own words: https://doc.qt.io/qt-6/qssgbounds3.html#QSSGBounds3

    Parameters
    ----------

    a0 : Qt.Initialization
      Passed on as its number.
    """
    #  QSSGBounds3::QSSGBounds3(Qt::Initialization a0)
    self._noteCreation(QSSGBounds3, lambda: Rituals.call(
        'ritual_ZN11QSSGBounds3C1EN2Qt14InitializationE', a0.value,
    ))

  @overload(QVector3D, QVector3D)
  def __init__(self, minimum: QVector3D, maximum: QVector3D) -> None:
    """
    Notes what was given, for Qt's 'QSSGBounds3::QSSGBounds3(const QVector3D
    &minimum, const QVector3D &maximum)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qssgbounds3.html#QSSGBounds3

    Parameters
    ----------

    minimum : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.

    maximum : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.
    """
    #  QSSGBounds3::QSSGBounds3(const QVector3D &minimum, const QVector3D
    #      &maximum)
    self._noteCreation(QSSGBounds3, lambda: Rituals.call(
        'ritual_ZN11QSSGBounds3C1ERK9QVector3DS2_',
        self._valueOf(minimum), self._valueOf(maximum),
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

  @overload(QVector3D)
  def include(self, v: QVector3D) -> None:
    """
    Calls Qt's 'void QSSGBounds3::include(const QVector3D &v)'.

    Qt's own words: https://doc.qt.io/qt-6/qssgbounds3.html#include

    Parameters
    ----------

    v : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.
    """
    #  void QSSGBounds3::include(const QVector3D &v)
    self.uglySide.call(
        'ritual_ZN11QSSGBounds37includeERK9QVector3D', self._valueOf(v),
    )

  @overload(THIS)
  def include(self, b: QSSGBounds3) -> None:
    """
    Calls Qt's 'void QSSGBounds3::include(const QSSGBounds3 &b)'.

    Qt's own words: https://doc.qt.io/qt-6/qssgbounds3.html#include

    Parameters
    ----------

    b : QSSGBounds3
      Passed on as a value: Qt reads the C++ QSSGBounds3, which stays
      Python's own.
    """
    #  void QSSGBounds3::include(const QSSGBounds3 &b)
    self.uglySide.call(
        'ritual_ZN11QSSGBounds37includeERKS_', self._valueOf(b),
    )

  @overload(float)
  def scale(self, scale: float) -> None:
    """
    Calls Qt's 'void QSSGBounds3::scale(float scale)'.

    Qt's own words: https://doc.qt.io/qt-6/qssgbounds3.html#scale

    Parameters
    ----------

    scale : float
      Passed on as it is.
    """
    #  void QSSGBounds3::scale(float scale)
    self.uglySide.call('ritual_ZN11QSSGBounds35scaleEf', scale)

  @overload(float)
  def fatten(self, distance: float) -> None:
    """
    Calls Qt's 'void QSSGBounds3::fatten(double distance)'.

    Qt's own words: https://doc.qt.io/qt-6/qssgbounds3.html#fatten

    Parameters
    ----------

    distance : float
      Passed on as it is.
    """
    #  void QSSGBounds3::fatten(double distance)
    self.uglySide.call('ritual_ZN11QSSGBounds36fattenEd', distance)

  @overload(QMatrix4x4)
  def transform(self, inMatrix: QMatrix4x4) -> None:
    """
    Calls Qt's 'void QSSGBounds3::transform(const QMatrix4x4 &inMatrix)'.

    Qt's own words: https://doc.qt.io/qt-6/qssgbounds3.html#transform

    Parameters
    ----------

    inMatrix : QMatrix4x4
      Passed on as a value: Qt reads the C++ QMatrix4x4, which stays Python's
      own.
    """
    #  void QSSGBounds3::transform(const QMatrix4x4 &inMatrix)
    self.uglySide.call(
        'ritual_ZN11QSSGBounds39transformERK10QMatrix4x4',
        self._valueOf(inMatrix),
    )

  @staticmethod
  def basisExtent(*__, **_) -> Never:
    """
    Qt's 'QSSGBounds3 QSSGBounds3::basisExtent(const QVector3D &center, const
    QMatrix3x3 &basis, const QVector3D &extent)': takes a type Python has no
    way to hand over yet.
    """
    raise NotImplementedError(
        "'QSSGBounds3.basisExtent' has no cute function yet. Qt's "
        "'QSSGBounds3 QSSGBounds3::basisExtent(const QVector3D &center, "
        "const QMatrix3x3 &basis, const QVector3D &extent)': takes a type "
        "Python has no way to hand over yet.")

  @staticmethod
  def toQSSGBoxPoints(*__, **_) -> Never:
    """
    Qt's 'QSSGBoxPoints QSSGBounds3::toQSSGBoxPoints() const': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QSSGBounds3.toQSSGBoxPoints' has no cute function yet. Qt's "
        "'QSSGBoxPoints QSSGBounds3::toQSSGBoxPoints() const': gives a type "
        "Python has no way to take yet.")

  @staticmethod
  def toQSSGBoxPointsNoEmptyCheck(*__, **_) -> Never:
    """
    Qt's 'QSSGBoxPoints QSSGBounds3::toQSSGBoxPointsNoEmptyCheck() const':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QSSGBounds3.toQSSGBoxPointsNoEmptyCheck' has no cute function "
        "yet. Qt's 'QSSGBoxPoints "
        "QSSGBounds3::toQSSGBoxPointsNoEmptyCheck() const': gives a type "
        "Python has no way to take yet.")
