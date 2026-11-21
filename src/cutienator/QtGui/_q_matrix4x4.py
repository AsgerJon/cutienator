"""
QMatrix4x4 binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/qmatrix4x4.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import Qt
from . import QMatrix4x4Flag

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from ..QtCore import QPoint, QPointF, QRect, QRectF
  from . import QQuaternion, QTransform, QVector3D, QVector4D
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPoint = WAIT['QPoint']
  QPointF = WAIT['QPointF']
  QQuaternion = WAIT['QQuaternion']
  QRect = WAIT['QRect']
  QRectF = WAIT['QRectF']
  QTransform = WAIT['QTransform']
  QVector3D = WAIT['QVector3D']
  QVector4D = WAIT['QVector4D']


class QMatrix4x4(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QMatrix4x4: a plain Python object standing in front
  of one C++ QMatrix4x4.

  C++ hands a QMatrix4x4 around as a copy, so every C++ QMatrix4x4 behind a
  cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QMatrix4x4 that has a ritual and that Python can
  call so far, 26 names in all: 'column', 'setColumn', 'row', 'setRow',
  'isAffine', 'isIdentity', 'setToIdentity', 'fill', 'determinant',
  'transposed', 'scale', 'translate', 'rotate', 'ortho', 'frustum',
  'perspective', 'lookAt', 'viewport', 'flipCoordinates', 'toTransform',
  'map', 'mapVector', 'mapRect', 'optimize', 'projectedRotate', 'flags'. It
  can be made from Python, in 4 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const float &QMatrix4x4::operator()(int row, int column) const': an
    operator, which is not reflected yet.
  - Qt's 'QMatrix4x4 QMatrix4x4::inverted(bool *invertible) const': takes a
    number to change where it is.
  - Qt's 'bool QMatrix4x4::operator==(const QMatrix4x4 &other) const': an
    operator, which is not reflected yet.
  - Qt's 'bool QMatrix4x4::operator!=(const QMatrix4x4 &other) const': an
    operator, which is not reflected yet.
  - Qt's 'void QMatrix4x4::copyDataTo(float *values) const': takes a number
    to change where it is.
  - Qt's 'QVariant QMatrix4x4::operator QVariant() const': an operator, which
    is not reflected yet.
  - Qt's 'QMatrix4x4::~QMatrix4x4()': the destructor: Python removes its C++
    QMatrix4x4 by it, and has no other use for it.

  What has no ritual
  ------------------

  16 of the 69 functions Qt declares: 12 takes or gives a type that cannot be
  passed yet; 2 a template; 2 private.

  What to expect
  --------------

  - The C++ QMatrix4x4 is created at the first use, not by 'QMatrix4x4(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QMatrix4x4 back gives a copy the ritual made for
    Python, in a new cute QMatrix4x4.
  """

  #  The enums Qt writes inside QMatrix4x4, and the names Qt has for the
  #  combinations of its flags enums.
  Flag = QMatrix4x4Flag
  Flags = QMatrix4x4Flag

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QMatrix4x4'

  #  Qt's '~QMatrix4x4()'. Naming it makes this a value class: Python owns
  #  every C++ QMatrix4x4 behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN10QMatrix4x4D1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def column(self, index: int) -> QVector4D:
    """
    Calls Qt's 'QVector4D QMatrix4x4::column(int index) const'.

    Qt's own words: https://doc.qt.io/qt-6/qmatrix4x4.html#column

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    QVector4D
      A new cute QVector4D around the copy Qt gave back. Python owns it.
    """
    #  QVector4D QMatrix4x4::column(int index) const
    address = self.uglySide.call('ritual_ZNK10QMatrix4x46columnEi', index)
    from . import QVector4D
    return QVector4D._cuteOwning(address)

  @overload(int)
  def row(self, index: int) -> QVector4D:
    """
    Calls Qt's 'QVector4D QMatrix4x4::row(int index) const'.

    Qt's own words: https://doc.qt.io/qt-6/qmatrix4x4.html#row

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    QVector4D
      A new cute QVector4D around the copy Qt gave back. Python owns it.
    """
    #  QVector4D QMatrix4x4::row(int index) const
    address = self.uglySide.call('ritual_ZNK10QMatrix4x43rowEi', index)
    from . import QVector4D
    return QVector4D._cuteOwning(address)

  def isAffine(self) -> bool:
    """
    Calls Qt's 'bool QMatrix4x4::isAffine() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmatrix4x4.html#isAffine
    """
    #  bool QMatrix4x4::isAffine() const
    return self.uglySide.call('ritual_ZNK10QMatrix4x48isAffineEv')

  def isIdentity(self) -> bool:
    """
    Calls Qt's 'bool QMatrix4x4::isIdentity() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmatrix4x4.html#isIdentity
    """
    #  bool QMatrix4x4::isIdentity() const
    return self.uglySide.call('ritual_ZNK10QMatrix4x410isIdentityEv')

  def determinant(self) -> float:
    """
    Calls Qt's 'double QMatrix4x4::determinant() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmatrix4x4.html#determinant
    """
    #  double QMatrix4x4::determinant() const
    return self.uglySide.call('ritual_ZNK10QMatrix4x411determinantEv')

  def transposed(self) -> QMatrix4x4:
    """
    Calls Qt's 'QMatrix4x4 QMatrix4x4::transposed() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmatrix4x4.html#transposed

    Returns
    -------

    QMatrix4x4
      A new cute QMatrix4x4 around the copy Qt gave back. Python owns it.
    """
    #  QMatrix4x4 QMatrix4x4::transposed() const
    address = self.uglySide.call('ritual_ZNK10QMatrix4x410transposedEv')
    return QMatrix4x4._cuteOwning(address)

  @overload()
  def toTransform(self) -> QTransform:
    """
    Calls Qt's 'QTransform QMatrix4x4::toTransform() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmatrix4x4.html#toTransform

    Returns
    -------

    QTransform
      A new cute QTransform around the copy Qt gave back. Python owns it.
    """
    #  QTransform QMatrix4x4::toTransform() const
    address = self.uglySide.call('ritual_ZNK10QMatrix4x411toTransformEv')
    from . import QTransform
    return QTransform._cuteOwning(address)

  @overload(float)
  def toTransform(self, distanceToPlane: float) -> QTransform:
    """
    Calls Qt's 'QTransform QMatrix4x4::toTransform(float distanceToPlane)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qmatrix4x4.html#toTransform

    Parameters
    ----------

    distanceToPlane : float
      Passed on as it is.

    Returns
    -------

    QTransform
      A new cute QTransform around the copy Qt gave back. Python owns it.
    """
    #  QTransform QMatrix4x4::toTransform(float distanceToPlane) const
    address = self.uglySide.call(
        'ritual_ZNK10QMatrix4x411toTransformEf', distanceToPlane,
    )
    from . import QTransform
    return QTransform._cuteOwning(address)

  @overload(QPoint)
  def map(self, point: QPoint) -> QPoint:
    """
    Calls Qt's 'QPoint QMatrix4x4::map(const QPoint &point) const'.

    Qt's own words: https://doc.qt.io/qt-6/qmatrix4x4.html#map

    Parameters
    ----------

    point : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.

    Returns
    -------

    QPoint
      A new cute QPoint around the copy Qt gave back. Python owns it.
    """
    #  QPoint QMatrix4x4::map(const QPoint &point) const
    address = self.uglySide.call(
        'ritual_ZNK10QMatrix4x43mapERK6QPoint', self._valueOf(point),
    )
    from ..QtCore import QPoint
    return QPoint._cuteOwning(address)

  @overload(QPointF)
  def map(self, point: QPointF) -> QPointF:
    """
    Calls Qt's 'QPointF QMatrix4x4::map(const QPointF &point) const'.

    Qt's own words: https://doc.qt.io/qt-6/qmatrix4x4.html#map

    Parameters
    ----------

    point : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QMatrix4x4::map(const QPointF &point) const
    address = self.uglySide.call(
        'ritual_ZNK10QMatrix4x43mapERK7QPointF', self._valueOf(point),
    )
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  @overload(QVector3D)
  def map(self, point: QVector3D) -> QVector3D:
    """
    Calls Qt's 'QVector3D QMatrix4x4::map(const QVector3D &point) const'.

    Qt's own words: https://doc.qt.io/qt-6/qmatrix4x4.html#map

    Parameters
    ----------

    point : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  QVector3D QMatrix4x4::map(const QVector3D &point) const
    address = self.uglySide.call(
        'ritual_ZNK10QMatrix4x43mapERK9QVector3D', self._valueOf(point),
    )
    from . import QVector3D
    return QVector3D._cuteOwning(address)

  @overload(QVector4D)
  def map(self, point: QVector4D) -> QVector4D:
    """
    Calls Qt's 'QVector4D QMatrix4x4::map(const QVector4D &point) const'.

    Qt's own words: https://doc.qt.io/qt-6/qmatrix4x4.html#map

    Parameters
    ----------

    point : QVector4D
      Passed on as a value: Qt reads the C++ QVector4D, which stays Python's
      own.

    Returns
    -------

    QVector4D
      A new cute QVector4D around the copy Qt gave back. Python owns it.
    """
    #  QVector4D QMatrix4x4::map(const QVector4D &point) const
    address = self.uglySide.call(
        'ritual_ZNK10QMatrix4x43mapERK9QVector4D', self._valueOf(point),
    )
    from . import QVector4D
    return QVector4D._cuteOwning(address)

  @overload(QVector3D)
  def mapVector(self, vector: QVector3D) -> QVector3D:
    """
    Calls Qt's 'QVector3D QMatrix4x4::mapVector(const QVector3D &vector)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qmatrix4x4.html#mapVector

    Parameters
    ----------

    vector : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  QVector3D QMatrix4x4::mapVector(const QVector3D &vector) const
    address = self.uglySide.call(
        'ritual_ZNK10QMatrix4x49mapVectorERK9QVector3D',
        self._valueOf(vector),
    )
    from . import QVector3D
    return QVector3D._cuteOwning(address)

  @overload(QRect)
  def mapRect(self, rect: QRect) -> QRect:
    """
    Calls Qt's 'QRect QMatrix4x4::mapRect(const QRect &rect) const'.

    Qt's own words: https://doc.qt.io/qt-6/qmatrix4x4.html#mapRect

    Parameters
    ----------

    rect : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect QMatrix4x4::mapRect(const QRect &rect) const
    address = self.uglySide.call(
        'ritual_ZNK10QMatrix4x47mapRectERK5QRect', self._valueOf(rect),
    )
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

  @overload(QRectF)
  def mapRect(self, rect: QRectF) -> QRectF:
    """
    Calls Qt's 'QRectF QMatrix4x4::mapRect(const QRectF &rect) const'.

    Qt's own words: https://doc.qt.io/qt-6/qmatrix4x4.html#mapRect

    Parameters
    ----------

    rect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QMatrix4x4::mapRect(const QRectF &rect) const
    address = self.uglySide.call(
        'ritual_ZNK10QMatrix4x47mapRectERK6QRectF', self._valueOf(rect),
    )
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  def flags(self) -> Flags:
    """
    Calls Qt's 'Flags QMatrix4x4::flags() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmatrix4x4.html#flags

    Returns
    -------

    Flags
      The value standing for the combination Qt gave back.
    """
    #  Flags QMatrix4x4::flags() const
    return QMatrix4x4.Flags(self.uglySide.call(
        'ritual_ZNK10QMatrix4x45flagsEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int, QVector4D)
  def setColumn(self, index: int, value: QVector4D) -> None:
    """
    Calls Qt's 'void QMatrix4x4::setColumn(int index, const QVector4D
    &value)'.

    Qt's own words: https://doc.qt.io/qt-6/qmatrix4x4.html#setColumn

    Parameters
    ----------

    index : int
      Passed on as it is.

    value : QVector4D
      Passed on as a value: Qt reads the C++ QVector4D, which stays Python's
      own.
    """
    #  void QMatrix4x4::setColumn(int index, const QVector4D &value)
    self.uglySide.call(
        'ritual_ZN10QMatrix4x49setColumnEiRK9QVector4D',
        index, self._valueOf(value),
    )

  @overload(int, QVector4D)
  def setRow(self, index: int, value: QVector4D) -> None:
    """
    Calls Qt's 'void QMatrix4x4::setRow(int index, const QVector4D &value)'.

    Qt's own words: https://doc.qt.io/qt-6/qmatrix4x4.html#setRow

    Parameters
    ----------

    index : int
      Passed on as it is.

    value : QVector4D
      Passed on as a value: Qt reads the C++ QVector4D, which stays Python's
      own.
    """
    #  void QMatrix4x4::setRow(int index, const QVector4D &value)
    self.uglySide.call(
        'ritual_ZN10QMatrix4x46setRowEiRK9QVector4D',
        index, self._valueOf(value),
    )

  def setToIdentity(self) -> None:
    """
    Calls Qt's 'void QMatrix4x4::setToIdentity()'.

    Qt's own words: https://doc.qt.io/qt-6/qmatrix4x4.html#setToIdentity
    """
    #  void QMatrix4x4::setToIdentity()
    self.uglySide.call('ritual_ZN10QMatrix4x413setToIdentityEv')

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
    Notes what was given, for Qt's 'QMatrix4x4::QMatrix4x4()', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qmatrix4x4.html#QMatrix4x4
    """
    #  QMatrix4x4::QMatrix4x4()
    self._noteCreation(QMatrix4x4, lambda: Rituals.call(
        'ritual_ZN10QMatrix4x4C1Ev',
    ))

  @overload(Qt.Initialization)
  def __init__(self, a0: Qt.Initialization) -> None:
    """
    Notes what was given, for Qt's 'QMatrix4x4::QMatrix4x4(Qt::Initialization
    a0)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qmatrix4x4.html#QMatrix4x4

    Parameters
    ----------

    a0 : Qt.Initialization
      Passed on as its number.
    """
    #  QMatrix4x4::QMatrix4x4(Qt::Initialization a0)
    self._noteCreation(QMatrix4x4, lambda: Rituals.call(
        'ritual_ZN10QMatrix4x4C1EN2Qt14InitializationE', a0.value,
    ))

  @overload(
      float, float, float, float, float, float, float, float, float, float,
      float, float, float, float, float, float,
  )
  def __init__(
      self,
      m11: float,
      m12: float,
      m13: float,
      m14: float,
      m21: float,
      m22: float,
      m23: float,
      m24: float,
      m31: float,
      m32: float,
      m33: float,
      m34: float,
      m41: float,
      m42: float,
      m43: float,
      m44: float,
  ) -> None:
    """
    Notes what was given, for Qt's 'QMatrix4x4::QMatrix4x4(float m11, float
    m12, float m13, float m14, float m21, float m22, float m23, float m24,
    float m31, float m32, float m33, float m34, float m41, float m42, float
    m43, float m44)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qmatrix4x4.html#QMatrix4x4

    Parameters
    ----------

    m11 : float
      Passed on as it is.

    m12 : float
      Passed on as it is.

    m13 : float
      Passed on as it is.

    m14 : float
      Passed on as it is.

    m21 : float
      Passed on as it is.

    m22 : float
      Passed on as it is.

    m23 : float
      Passed on as it is.

    m24 : float
      Passed on as it is.

    m31 : float
      Passed on as it is.

    m32 : float
      Passed on as it is.

    m33 : float
      Passed on as it is.

    m34 : float
      Passed on as it is.

    m41 : float
      Passed on as it is.

    m42 : float
      Passed on as it is.

    m43 : float
      Passed on as it is.

    m44 : float
      Passed on as it is.
    """
    #  QMatrix4x4::QMatrix4x4(float m11, float m12, float m13, float m14,
    #      float m21, float m22, float m23, float m24, float m31, float m32,
    #      float m33, float m34, float m41, float m42, float m43, float m44)
    self._noteCreation(QMatrix4x4, lambda: Rituals.call(
        'ritual_ZN10QMatrix4x4C1Effffffffffffffff',
        m11, m12, m13, m14, m21, m22, m23, m24, m31, m32, m33, m34, m41, m42,
        m43, m44,
    ))

  @overload(QTransform)
  def __init__(self, transform: QTransform) -> None:
    """
    Notes what was given, for Qt's 'QMatrix4x4::QMatrix4x4(const QTransform
    &transform)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qmatrix4x4.html#QMatrix4x4

    Parameters
    ----------

    transform : QTransform
      Passed on as a value: Qt reads the C++ QTransform, which stays Python's
      own.
    """
    #  QMatrix4x4::QMatrix4x4(const QTransform &transform)
    self._noteCreation(QMatrix4x4, lambda: Rituals.call(
        'ritual_ZN10QMatrix4x4C1ERK10QTransform', self._valueOf(transform),
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

  @overload(float)
  def fill(self, value: float) -> None:
    """
    Calls Qt's 'void QMatrix4x4::fill(float value)'.

    Qt's own words: https://doc.qt.io/qt-6/qmatrix4x4.html#fill

    Parameters
    ----------

    value : float
      Passed on as it is.
    """
    #  void QMatrix4x4::fill(float value)
    self.uglySide.call('ritual_ZN10QMatrix4x44fillEf', value)

  @overload(QVector3D)
  def scale(self, vector: QVector3D) -> None:
    """
    Calls Qt's 'void QMatrix4x4::scale(const QVector3D &vector)'.

    Qt's own words: https://doc.qt.io/qt-6/qmatrix4x4.html#scale

    Parameters
    ----------

    vector : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.
    """
    #  void QMatrix4x4::scale(const QVector3D &vector)
    self.uglySide.call(
        'ritual_ZN10QMatrix4x45scaleERK9QVector3D', self._valueOf(vector),
    )

  @overload(float, float)
  def scale(self, x: float, y: float) -> None:
    """
    Calls Qt's 'void QMatrix4x4::scale(float x, float y)'.

    Qt's own words: https://doc.qt.io/qt-6/qmatrix4x4.html#scale

    Parameters
    ----------

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.
    """
    #  void QMatrix4x4::scale(float x, float y)
    self.uglySide.call('ritual_ZN10QMatrix4x45scaleEff', x, y)

  @overload(float, float, float)
  def scale(self, x: float, y: float, z: float) -> None:
    """
    Calls Qt's 'void QMatrix4x4::scale(float x, float y, float z)'.

    Qt's own words: https://doc.qt.io/qt-6/qmatrix4x4.html#scale

    Parameters
    ----------

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.

    z : float
      Passed on as it is.
    """
    #  void QMatrix4x4::scale(float x, float y, float z)
    self.uglySide.call('ritual_ZN10QMatrix4x45scaleEfff', x, y, z)

  @overload(float)
  def scale(self, factor: float) -> None:
    """
    Calls Qt's 'void QMatrix4x4::scale(float factor)'.

    Qt's own words: https://doc.qt.io/qt-6/qmatrix4x4.html#scale

    Parameters
    ----------

    factor : float
      Passed on as it is.
    """
    #  void QMatrix4x4::scale(float factor)
    self.uglySide.call('ritual_ZN10QMatrix4x45scaleEf', factor)

  @overload(QVector3D)
  def translate(self, vector: QVector3D) -> None:
    """
    Calls Qt's 'void QMatrix4x4::translate(const QVector3D &vector)'.

    Qt's own words: https://doc.qt.io/qt-6/qmatrix4x4.html#translate

    Parameters
    ----------

    vector : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.
    """
    #  void QMatrix4x4::translate(const QVector3D &vector)
    self.uglySide.call(
        'ritual_ZN10QMatrix4x49translateERK9QVector3D',
        self._valueOf(vector),
    )

  @overload(float, float)
  def translate(self, x: float, y: float) -> None:
    """
    Calls Qt's 'void QMatrix4x4::translate(float x, float y)'.

    Qt's own words: https://doc.qt.io/qt-6/qmatrix4x4.html#translate

    Parameters
    ----------

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.
    """
    #  void QMatrix4x4::translate(float x, float y)
    self.uglySide.call('ritual_ZN10QMatrix4x49translateEff', x, y)

  @overload(float, float, float)
  def translate(self, x: float, y: float, z: float) -> None:
    """
    Calls Qt's 'void QMatrix4x4::translate(float x, float y, float z)'.

    Qt's own words: https://doc.qt.io/qt-6/qmatrix4x4.html#translate

    Parameters
    ----------

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.

    z : float
      Passed on as it is.
    """
    #  void QMatrix4x4::translate(float x, float y, float z)
    self.uglySide.call('ritual_ZN10QMatrix4x49translateEfff', x, y, z)

  @overload(float, QVector3D)
  def rotate(self, angle: float, vector: QVector3D) -> None:
    """
    Calls Qt's 'void QMatrix4x4::rotate(float angle, const QVector3D
    &vector)'.

    Qt's own words: https://doc.qt.io/qt-6/qmatrix4x4.html#rotate

    Parameters
    ----------

    angle : float
      Passed on as it is.

    vector : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.
    """
    #  void QMatrix4x4::rotate(float angle, const QVector3D &vector)
    self.uglySide.call(
        'ritual_ZN10QMatrix4x46rotateEfRK9QVector3D',
        angle, self._valueOf(vector),
    )

  @overload(float, float, float)
  @overload(float, float, float, float)
  def rotate(self, angle: float, x: float, y: float, z: float = 0.0) -> None:
    """
    Calls Qt's 'void QMatrix4x4::rotate(float angle, float x, float y, float
    z)'.

    Qt's own words: https://doc.qt.io/qt-6/qmatrix4x4.html#rotate

    Parameters
    ----------

    angle : float
      Passed on as it is.

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.

    z : float
      Passed on as it is. May be left out, as in Qt: it is then 0.0.
    """
    #  void QMatrix4x4::rotate(float angle, float x, float y, float z)
    self.uglySide.call('ritual_ZN10QMatrix4x46rotateEffff', angle, x, y, z)

  @overload(QQuaternion)
  def rotate(self, quaternion: QQuaternion) -> None:
    """
    Calls Qt's 'void QMatrix4x4::rotate(const QQuaternion &quaternion)'.

    Qt's own words: https://doc.qt.io/qt-6/qmatrix4x4.html#rotate

    Parameters
    ----------

    quaternion : QQuaternion
      Passed on as a value: Qt reads the C++ QQuaternion, which stays
      Python's own.
    """
    #  void QMatrix4x4::rotate(const QQuaternion &quaternion)
    self.uglySide.call(
        'ritual_ZN10QMatrix4x46rotateERK11QQuaternion',
        self._valueOf(quaternion),
    )

  @overload(QRect)
  def ortho(self, rect: QRect) -> None:
    """
    Calls Qt's 'void QMatrix4x4::ortho(const QRect &rect)'.

    Qt's own words: https://doc.qt.io/qt-6/qmatrix4x4.html#ortho

    Parameters
    ----------

    rect : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.
    """
    #  void QMatrix4x4::ortho(const QRect &rect)
    self.uglySide.call(
        'ritual_ZN10QMatrix4x45orthoERK5QRect', self._valueOf(rect),
    )

  @overload(QRectF)
  def ortho(self, rect: QRectF) -> None:
    """
    Calls Qt's 'void QMatrix4x4::ortho(const QRectF &rect)'.

    Qt's own words: https://doc.qt.io/qt-6/qmatrix4x4.html#ortho

    Parameters
    ----------

    rect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void QMatrix4x4::ortho(const QRectF &rect)
    self.uglySide.call(
        'ritual_ZN10QMatrix4x45orthoERK6QRectF', self._valueOf(rect),
    )

  @overload(float, float, float, float, float, float)
  def ortho(
      self,
      left: float,
      right: float,
      bottom: float,
      top: float,
      nearPlane: float,
      farPlane: float,
  ) -> None:
    """
    Calls Qt's 'void QMatrix4x4::ortho(float left, float right, float bottom,
    float top, float nearPlane, float farPlane)'.

    Qt's own words: https://doc.qt.io/qt-6/qmatrix4x4.html#ortho

    Parameters
    ----------

    left : float
      Passed on as it is.

    right : float
      Passed on as it is.

    bottom : float
      Passed on as it is.

    top : float
      Passed on as it is.

    nearPlane : float
      Passed on as it is.

    farPlane : float
      Passed on as it is.
    """
    #  void QMatrix4x4::ortho(float left, float right, float bottom, float
    #      top, float nearPlane, float farPlane)
    self.uglySide.call(
        'ritual_ZN10QMatrix4x45orthoEffffff',
        left, right, bottom, top, nearPlane, farPlane,
    )

  @overload(float, float, float, float, float, float)
  def frustum(
      self,
      left: float,
      right: float,
      bottom: float,
      top: float,
      nearPlane: float,
      farPlane: float,
  ) -> None:
    """
    Calls Qt's 'void QMatrix4x4::frustum(float left, float right, float
    bottom, float top, float nearPlane, float farPlane)'.

    Qt's own words: https://doc.qt.io/qt-6/qmatrix4x4.html#frustum

    Parameters
    ----------

    left : float
      Passed on as it is.

    right : float
      Passed on as it is.

    bottom : float
      Passed on as it is.

    top : float
      Passed on as it is.

    nearPlane : float
      Passed on as it is.

    farPlane : float
      Passed on as it is.
    """
    #  void QMatrix4x4::frustum(float left, float right, float bottom, float
    #      top, float nearPlane, float farPlane)
    self.uglySide.call(
        'ritual_ZN10QMatrix4x47frustumEffffff',
        left, right, bottom, top, nearPlane, farPlane,
    )

  @overload(float, float, float, float)
  def perspective(
      self,
      verticalAngle: float,
      aspectRatio: float,
      nearPlane: float,
      farPlane: float,
  ) -> None:
    """
    Calls Qt's 'void QMatrix4x4::perspective(float verticalAngle, float
    aspectRatio, float nearPlane, float farPlane)'.

    Qt's own words: https://doc.qt.io/qt-6/qmatrix4x4.html#perspective

    Parameters
    ----------

    verticalAngle : float
      Passed on as it is.

    aspectRatio : float
      Passed on as it is.

    nearPlane : float
      Passed on as it is.

    farPlane : float
      Passed on as it is.
    """
    #  void QMatrix4x4::perspective(float verticalAngle, float aspectRatio,
    #      float nearPlane, float farPlane)
    self.uglySide.call(
        'ritual_ZN10QMatrix4x411perspectiveEffff',
        verticalAngle, aspectRatio, nearPlane, farPlane,
    )

  @overload(QVector3D, QVector3D, QVector3D)
  def lookAt(self, eye: QVector3D, center: QVector3D, up: QVector3D) -> None:
    """
    Calls Qt's 'void QMatrix4x4::lookAt(const QVector3D &eye, const QVector3D
    &center, const QVector3D &up)'.

    Qt's own words: https://doc.qt.io/qt-6/qmatrix4x4.html#lookAt

    Parameters
    ----------

    eye : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.

    center : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.

    up : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.
    """
    #  void QMatrix4x4::lookAt(const QVector3D &eye, const QVector3D &center,
    #      const QVector3D &up)
    self.uglySide.call(
        'ritual_ZN10QMatrix4x46lookAtERK9QVector3DS2_S2_',
        self._valueOf(eye), self._valueOf(center), self._valueOf(up),
    )

  @overload(QRectF)
  def viewport(self, rect: QRectF) -> None:
    """
    Calls Qt's 'void QMatrix4x4::viewport(const QRectF &rect)'.

    Qt's own words: https://doc.qt.io/qt-6/qmatrix4x4.html#viewport

    Parameters
    ----------

    rect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void QMatrix4x4::viewport(const QRectF &rect)
    self.uglySide.call(
        'ritual_ZN10QMatrix4x48viewportERK6QRectF', self._valueOf(rect),
    )

  @overload(float, float, float, float)
  @overload(float, float, float, float, float)
  @overload(float, float, float, float, float, float)
  def viewport(
      self,
      left: float,
      bottom: float,
      width: float,
      height: float,
      nearPlane: float = 0.0,
      farPlane: float = 1.0,
  ) -> None:
    """
    Calls Qt's 'void QMatrix4x4::viewport(float left, float bottom, float
    width, float height, float nearPlane, float farPlane)'.

    Qt's own words: https://doc.qt.io/qt-6/qmatrix4x4.html#viewport

    Parameters
    ----------

    left : float
      Passed on as it is.

    bottom : float
      Passed on as it is.

    width : float
      Passed on as it is.

    height : float
      Passed on as it is.

    nearPlane : float
      Passed on as it is. May be left out, as in Qt: it is then 0.0.

    farPlane : float
      Passed on as it is. May be left out, as in Qt: it is then 1.0.
    """
    #  void QMatrix4x4::viewport(float left, float bottom, float width, float
    #      height, float nearPlane, float farPlane)
    self.uglySide.call(
        'ritual_ZN10QMatrix4x48viewportEffffff',
        left, bottom, width, height, nearPlane, farPlane,
    )

  def flipCoordinates(self) -> None:
    """
    Calls Qt's 'void QMatrix4x4::flipCoordinates()'.

    Qt's own words: https://doc.qt.io/qt-6/qmatrix4x4.html#flipCoordinates
    """
    #  void QMatrix4x4::flipCoordinates()
    self.uglySide.call('ritual_ZN10QMatrix4x415flipCoordinatesEv')

  def optimize(self) -> None:
    """
    Calls Qt's 'void QMatrix4x4::optimize()'.

    Qt's own words: https://doc.qt.io/qt-6/qmatrix4x4.html#optimize
    """
    #  void QMatrix4x4::optimize()
    self.uglySide.call('ritual_ZN10QMatrix4x48optimizeEv')

  @overload(float, float, float, float, float)
  def projectedRotate(
      self,
      angle: float,
      x: float,
      y: float,
      z: float,
      distanceToPlane: float,
  ) -> None:
    """
    Calls Qt's 'void QMatrix4x4::projectedRotate(float angle, float x, float
    y, float z, float distanceToPlane)'.

    Qt's own words: https://doc.qt.io/qt-6/qmatrix4x4.html#projectedRotate

    Parameters
    ----------

    angle : float
      Passed on as it is.

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.

    z : float
      Passed on as it is.

    distanceToPlane : float
      Passed on as it is.
    """
    #  void QMatrix4x4::projectedRotate(float angle, float x, float y, float
    #      z, float distanceToPlane)
    self.uglySide.call(
        'ritual_ZN10QMatrix4x415projectedRotateEfffff',
        angle, x, y, z, distanceToPlane,
    )

  @overload(float, float, float, float)
  def projectedRotate(
      self,
      angle: float,
      x: float,
      y: float,
      z: float,
  ) -> None:
    """
    Calls Qt's 'void QMatrix4x4::projectedRotate(float angle, float x, float
    y, float z)'.

    Qt's own words: https://doc.qt.io/qt-6/qmatrix4x4.html#projectedRotate

    Parameters
    ----------

    angle : float
      Passed on as it is.

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.

    z : float
      Passed on as it is.
    """
    #  void QMatrix4x4::projectedRotate(float angle, float x, float y, float
    #      z)
    self.uglySide.call(
        'ritual_ZN10QMatrix4x415projectedRotateEffff', angle, x, y, z,
    )
