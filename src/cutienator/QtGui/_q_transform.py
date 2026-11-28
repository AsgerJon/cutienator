"""
QTransform binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/qtransform.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import Qt

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from ..QtCore import QLine, QLineF, QPoint, QPointF, QRect, QRectF
  from . import QPainterPath, QPolygon, QPolygonF, QRegion
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QLine = WAIT['QLine']
  QLineF = WAIT['QLineF']
  QPainterPath = WAIT['QPainterPath']
  QPoint = WAIT['QPoint']
  QPointF = WAIT['QPointF']
  QPolygon = WAIT['QPolygon']
  QPolygonF = WAIT['QPolygonF']
  QRect = WAIT['QRect']
  QRectF = WAIT['QRectF']
  QRegion = WAIT['QRegion']


class QTransform(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QTransform: a plain Python object standing in front
  of one C++ QTransform.

  C++ hands a QTransform around as a copy, so every C++ QTransform behind a
  cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QTransform that has a ritual and that Python can
  call so far, 36 names in all: 'isAffine', 'isIdentity', 'isInvertible',
  'isScaling', 'isRotating', 'isTranslating', 'type', 'determinant', 'm11',
  'm12', 'm13', 'm21', 'm22', 'm23', 'm31', 'm32', 'm33', 'dx', 'dy',
  'setMatrix', 'adjoint', 'transposed', '__eq__', '__ne__', '__imul__',
  '__mul__', 'reset', 'map', 'mapToPolygon', 'mapRect', '__itruediv__',
  '__iadd__', '__isub__', 'fromTranslate', 'fromScale', 'inline_type'. It can
  be made from Python, in 5 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QTransform &QTransform::operator=(QTransform &&other)': assignment:
    Python binds a name and has no operator for it.
  - Qt's 'QTransform &QTransform::operator=(const QTransform &a0)':
    assignment: Python binds a name and has no operator for it.
  - Qt's 'QTransform::QTransform(QTransform &&other)': takes a type Python
    has no way to hand over yet.
  - Qt's 'QTransform QTransform::inverted(bool *invertible) const': takes a
    number to change where it is.
  - Qt's 'QTransform &QTransform::translate(qreal dx, qreal dy)': gives a
    type Python has no way to take yet.
  - Qt's 'QTransform &QTransform::scale(qreal sx, qreal sy)': gives a type
    Python has no way to take yet.
  - Qt's 'QTransform &QTransform::shear(qreal sh, qreal sv)': gives a type
    Python has no way to take yet.
  - Qt's 'QTransform &QTransform::rotate(qreal a, Qt::Axis axis, qreal
    distanceToPlane)': gives a type Python has no way to take yet.
  - Qt's 'QTransform &QTransform::rotate(qreal a, Qt::Axis axis)': gives a
    type Python has no way to take yet.
  - Qt's 'QTransform &QTransform::rotateRadians(qreal a, Qt::Axis axis, qreal
    distanceToPlane)': gives a type Python has no way to take yet.
  - Qt's 'QTransform &QTransform::rotateRadians(qreal a, Qt::Axis axis)':
    gives a type Python has no way to take yet.
  - Qt's 'bool QTransform::squareToQuad(const QPolygonF &square, QTransform
    &result)': takes a type Python has no way to hand over yet.
  - Qt's 'bool QTransform::quadToSquare(const QPolygonF &quad, QTransform
    &result)': takes a type Python has no way to hand over yet.
  - Qt's 'bool QTransform::quadToQuad(const QPolygonF &one, const QPolygonF
    &two, QTransform &result)': takes a type Python has no way to hand over
    yet.
  - Qt's 'QVariant QTransform::operator QVariant() const': an operator Python
    has no name for.
  - Qt's 'void QTransform::map(int x, int y, int *tx, int *ty) const': takes
    a number to change where it is.
  - Qt's 'void QTransform::map(qreal x, qreal y, qreal *tx, qreal *ty)
    const': takes a number to change where it is.
  - Qt's 'Affine QTransform::asAffineMatrix()': gives a type Python has no
    way to take yet.
  - Qt's 'QDataStream &operator>>(QDataStream &s, Affine &m)': an operator
    between other classes, written inside this one.
  - Qt's 'QDataStream &operator<<(QDataStream &s, const Affine &m)': an
    operator between other classes, written inside this one.
  - Qt's 'void QTransform::do_map(qreal x, qreal y, qreal &nx, qreal &ny)
    const': takes a number to change where it is.
  - Qt's 'QTransform::~QTransform()': the destructor: Python removes its C++
    QTransform by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QTransform is created at the first use, not by 'QTransform(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QTransform back gives a copy the ritual made for
    Python, in a new cute QTransform.
  - Each name of Qt's QTransform that has no cute function yet,
    'asAffineMatrix', 'do_map', 'inverted', 'quadToQuad', 'quadToSquare',
    'rotate', 'rotateRadians', 'scale', 'shear', 'squareToQuad', 'translate',
    holds a function that raises 'NotImplementedError', and its docstring
    says why.
  """

  #  The enums Qt writes inside QTransform, each a class in here as in C++,
  #  and the names Qt has for the combinations of its flags enums.

  class TransformationType(CuteNum):
    """
    The enum 'QTransform::TransformationType' of Qt, with the 6 names Qt
    gives in it.
    """

    TxNone = Kee[int](0)
    TxTranslate = Kee[int](1)
    TxScale = Kee[int](2)
    TxRotate = Kee[int](4)
    TxShear = Kee[int](8)
    TxProject = Kee[int](16)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(float, float)
  def fromTranslate(dx: float, dy: float) -> QTransform:
    """
    Calls Qt's 'QTransform QTransform::fromTranslate(qreal dx, qreal dy)'.

    Qt's own words: https://doc.qt.io/qt-6/qtransform.html#fromTranslate

    Parameters
    ----------

    dx : float
      Passed on as it is.

    dy : float
      Passed on as it is.

    Returns
    -------

    QTransform
      A new cute QTransform around the copy Qt gave back. Python owns it.
    """
    #  QTransform QTransform::fromTranslate(qreal dx, qreal dy)
    address = Rituals.call('ritual_ZN10QTransform13fromTranslateEdd', dx, dy)
    return QTransform._cuteOwning(address)

  @staticmethod
  @overload(float, float)
  def fromScale(dx: float, dy: float) -> QTransform:
    """
    Calls Qt's 'QTransform QTransform::fromScale(qreal dx, qreal dy)'.

    Qt's own words: https://doc.qt.io/qt-6/qtransform.html#fromScale

    Parameters
    ----------

    dx : float
      Passed on as it is.

    dy : float
      Passed on as it is.

    Returns
    -------

    QTransform
      A new cute QTransform around the copy Qt gave back. Python owns it.
    """
    #  QTransform QTransform::fromScale(qreal dx, qreal dy)
    address = Rituals.call('ritual_ZN10QTransform9fromScaleEdd', dx, dy)
    return QTransform._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QTransform'

  #  Qt's '~QTransform()'. Naming it makes this a value class: Python owns
  #  every C++ QTransform behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN10QTransformD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isAffine(self) -> bool:
    """
    Calls Qt's 'bool QTransform::isAffine() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtransform.html#isAffine
    """
    #  bool QTransform::isAffine() const
    return self.uglySide.call('ritual_ZNK10QTransform8isAffineEv')

  def isIdentity(self) -> bool:
    """
    Calls Qt's 'bool QTransform::isIdentity() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtransform.html#isIdentity
    """
    #  bool QTransform::isIdentity() const
    return self.uglySide.call('ritual_ZNK10QTransform10isIdentityEv')

  def isInvertible(self) -> bool:
    """
    Calls Qt's 'bool QTransform::isInvertible() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtransform.html#isInvertible
    """
    #  bool QTransform::isInvertible() const
    return self.uglySide.call('ritual_ZNK10QTransform12isInvertibleEv')

  def isScaling(self) -> bool:
    """
    Calls Qt's 'bool QTransform::isScaling() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtransform.html#isScaling
    """
    #  bool QTransform::isScaling() const
    return self.uglySide.call('ritual_ZNK10QTransform9isScalingEv')

  def isRotating(self) -> bool:
    """
    Calls Qt's 'bool QTransform::isRotating() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtransform.html#isRotating
    """
    #  bool QTransform::isRotating() const
    return self.uglySide.call('ritual_ZNK10QTransform10isRotatingEv')

  def isTranslating(self) -> bool:
    """
    Calls Qt's 'bool QTransform::isTranslating() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtransform.html#isTranslating
    """
    #  bool QTransform::isTranslating() const
    return self.uglySide.call('ritual_ZNK10QTransform13isTranslatingEv')

  def type(self) -> TransformationType:
    """
    Calls Qt's 'TransformationType QTransform::type() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtransform.html#type

    Returns
    -------

    TransformationType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'TransformationType(number)' gives.
    """
    #  TransformationType QTransform::type() const
    return QTransform.TransformationType(self.uglySide.call(
        'ritual_ZNK10QTransform4typeEv',
    ))

  def determinant(self) -> float:
    """
    Calls Qt's 'qreal QTransform::determinant() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtransform.html#determinant
    """
    #  qreal QTransform::determinant() const
    return self.uglySide.call('ritual_ZNK10QTransform11determinantEv')

  def m11(self) -> float:
    """
    Calls Qt's 'qreal QTransform::m11() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtransform.html#m11
    """
    #  qreal QTransform::m11() const
    return self.uglySide.call('ritual_ZNK10QTransform3m11Ev')

  def m12(self) -> float:
    """
    Calls Qt's 'qreal QTransform::m12() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtransform.html#m12
    """
    #  qreal QTransform::m12() const
    return self.uglySide.call('ritual_ZNK10QTransform3m12Ev')

  def m13(self) -> float:
    """
    Calls Qt's 'qreal QTransform::m13() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtransform.html#m13
    """
    #  qreal QTransform::m13() const
    return self.uglySide.call('ritual_ZNK10QTransform3m13Ev')

  def m21(self) -> float:
    """
    Calls Qt's 'qreal QTransform::m21() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtransform.html#m21
    """
    #  qreal QTransform::m21() const
    return self.uglySide.call('ritual_ZNK10QTransform3m21Ev')

  def m22(self) -> float:
    """
    Calls Qt's 'qreal QTransform::m22() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtransform.html#m22
    """
    #  qreal QTransform::m22() const
    return self.uglySide.call('ritual_ZNK10QTransform3m22Ev')

  def m23(self) -> float:
    """
    Calls Qt's 'qreal QTransform::m23() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtransform.html#m23
    """
    #  qreal QTransform::m23() const
    return self.uglySide.call('ritual_ZNK10QTransform3m23Ev')

  def m31(self) -> float:
    """
    Calls Qt's 'qreal QTransform::m31() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtransform.html#m31
    """
    #  qreal QTransform::m31() const
    return self.uglySide.call('ritual_ZNK10QTransform3m31Ev')

  def m32(self) -> float:
    """
    Calls Qt's 'qreal QTransform::m32() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtransform.html#m32
    """
    #  qreal QTransform::m32() const
    return self.uglySide.call('ritual_ZNK10QTransform3m32Ev')

  def m33(self) -> float:
    """
    Calls Qt's 'qreal QTransform::m33() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtransform.html#m33
    """
    #  qreal QTransform::m33() const
    return self.uglySide.call('ritual_ZNK10QTransform3m33Ev')

  def dx(self) -> float:
    """
    Calls Qt's 'qreal QTransform::dx() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtransform.html#dx
    """
    #  qreal QTransform::dx() const
    return self.uglySide.call('ritual_ZNK10QTransform2dxEv')

  def dy(self) -> float:
    """
    Calls Qt's 'qreal QTransform::dy() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtransform.html#dy
    """
    #  qreal QTransform::dy() const
    return self.uglySide.call('ritual_ZNK10QTransform2dyEv')

  def adjoint(self) -> QTransform:
    """
    Calls Qt's 'QTransform QTransform::adjoint() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtransform.html#adjoint

    Returns
    -------

    QTransform
      A new cute QTransform around the copy Qt gave back. Python owns it.
    """
    #  QTransform QTransform::adjoint() const
    address = self.uglySide.call('ritual_ZNK10QTransform7adjointEv')
    return QTransform._cuteOwning(address)

  def transposed(self) -> QTransform:
    """
    Calls Qt's 'QTransform QTransform::transposed() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtransform.html#transposed

    Returns
    -------

    QTransform
      A new cute QTransform around the copy Qt gave back. Python owns it.
    """
    #  QTransform QTransform::transposed() const
    address = self.uglySide.call('ritual_ZNK10QTransform10transposedEv')
    return QTransform._cuteOwning(address)

  @overload(QPoint)
  def map(self, p: QPoint) -> QPoint:
    """
    Calls Qt's 'QPoint QTransform::map(const QPoint &p) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtransform.html#map

    Parameters
    ----------

    p : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.

    Returns
    -------

    QPoint
      A new cute QPoint around the copy Qt gave back. Python owns it.
    """
    #  QPoint QTransform::map(const QPoint &p) const
    address = self.uglySide.call(
        'ritual_ZNK10QTransform3mapERK6QPoint', self._valueOf(p),
    )
    from ..QtCore import QPoint
    return QPoint._cuteOwning(address)

  @overload(QPointF)
  def map(self, p: QPointF) -> QPointF:
    """
    Calls Qt's 'QPointF QTransform::map(const QPointF &p) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtransform.html#map

    Parameters
    ----------

    p : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QTransform::map(const QPointF &p) const
    address = self.uglySide.call(
        'ritual_ZNK10QTransform3mapERK7QPointF', self._valueOf(p, 'QPointF'),
    )
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  @overload(QLine)
  def map(self, l: QLine) -> QLine:
    """
    Calls Qt's 'QLine QTransform::map(const QLine &l) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtransform.html#map

    Parameters
    ----------

    l : QLine
      Passed on as a value: Qt reads the C++ QLine, which stays Python's own.

    Returns
    -------

    QLine
      A new cute QLine around the copy Qt gave back. Python owns it.
    """
    #  QLine QTransform::map(const QLine &l) const
    address = self.uglySide.call(
        'ritual_ZNK10QTransform3mapERK5QLine', self._valueOf(l),
    )
    from ..QtCore import QLine
    return QLine._cuteOwning(address)

  @overload(QLineF)
  def map(self, l: QLineF) -> QLineF:
    """
    Calls Qt's 'QLineF QTransform::map(const QLineF &l) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtransform.html#map

    Parameters
    ----------

    l : QLineF
      Passed on as a value: Qt reads the C++ QLineF, which stays Python's
      own.

    Returns
    -------

    QLineF
      A new cute QLineF around the copy Qt gave back. Python owns it.
    """
    #  QLineF QTransform::map(const QLineF &l) const
    address = self.uglySide.call(
        'ritual_ZNK10QTransform3mapERK6QLineF', self._valueOf(l),
    )
    from ..QtCore import QLineF
    return QLineF._cuteOwning(address)

  @overload(QPolygonF)
  def map(self, a: QPolygonF) -> QPolygonF:
    """
    Calls Qt's 'QPolygonF QTransform::map(const QPolygonF &a) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtransform.html#map

    Parameters
    ----------

    a : QPolygonF
      Passed on as a value: Qt reads the C++ QPolygonF, which stays Python's
      own.

    Returns
    -------

    QPolygonF
      A new cute QPolygonF around the copy Qt gave back. Python owns it.
    """
    #  QPolygonF QTransform::map(const QPolygonF &a) const
    address = self.uglySide.call(
        'ritual_ZNK10QTransform3mapERK9QPolygonF', self._valueOf(a),
    )
    from . import QPolygonF
    return QPolygonF._cuteOwning(address)

  @overload(QPolygon)
  def map(self, a: QPolygon) -> QPolygon:
    """
    Calls Qt's 'QPolygon QTransform::map(const QPolygon &a) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtransform.html#map

    Parameters
    ----------

    a : QPolygon
      Passed on as a value: Qt reads the C++ QPolygon, which stays Python's
      own.

    Returns
    -------

    QPolygon
      A new cute QPolygon around the copy Qt gave back. Python owns it.
    """
    #  QPolygon QTransform::map(const QPolygon &a) const
    address = self.uglySide.call(
        'ritual_ZNK10QTransform3mapERK8QPolygon', self._valueOf(a),
    )
    from . import QPolygon
    return QPolygon._cuteOwning(address)

  @overload(QRegion)
  def map(self, r: QRegion) -> QRegion:
    """
    Calls Qt's 'QRegion QTransform::map(const QRegion &r) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtransform.html#map

    Parameters
    ----------

    r : QRegion
      Passed on as a value: Qt reads the C++ QRegion, which stays Python's
      own.

    Returns
    -------

    QRegion
      A new cute QRegion around the copy Qt gave back. Python owns it.
    """
    #  QRegion QTransform::map(const QRegion &r) const
    address = self.uglySide.call(
        'ritual_ZNK10QTransform3mapERK7QRegion', self._valueOf(r),
    )
    from . import QRegion
    return QRegion._cuteOwning(address)

  @overload(QPainterPath)
  def map(self, p: QPainterPath) -> QPainterPath:
    """
    Calls Qt's 'QPainterPath QTransform::map(const QPainterPath &p) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtransform.html#map

    Parameters
    ----------

    p : QPainterPath
      Passed on as a value: Qt reads the C++ QPainterPath, which stays
      Python's own.

    Returns
    -------

    QPainterPath
      A new cute QPainterPath around the copy Qt gave back. Python owns it.
    """
    #  QPainterPath QTransform::map(const QPainterPath &p) const
    address = self.uglySide.call(
        'ritual_ZNK10QTransform3mapERK12QPainterPath', self._valueOf(p),
    )
    from . import QPainterPath
    return QPainterPath._cuteOwning(address)

  @overload(QRect)
  def mapToPolygon(self, r: QRect) -> QPolygon:
    """
    Calls Qt's 'QPolygon QTransform::mapToPolygon(const QRect &r) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtransform.html#mapToPolygon

    Parameters
    ----------

    r : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.

    Returns
    -------

    QPolygon
      A new cute QPolygon around the copy Qt gave back. Python owns it.
    """
    #  QPolygon QTransform::mapToPolygon(const QRect &r) const
    address = self.uglySide.call(
        'ritual_ZNK10QTransform12mapToPolygonERK5QRect', self._valueOf(r),
    )
    from . import QPolygon
    return QPolygon._cuteOwning(address)

  @overload(QRect)
  def mapRect(self, a0: QRect) -> QRect:
    """
    Calls Qt's 'QRect QTransform::mapRect(const QRect &a0) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtransform.html#mapRect

    Parameters
    ----------

    a0 : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect QTransform::mapRect(const QRect &a0) const
    address = self.uglySide.call(
        'ritual_ZNK10QTransform7mapRectERK5QRect', self._valueOf(a0),
    )
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

  @overload(QRectF)
  def mapRect(self, a0: QRectF) -> QRectF:
    """
    Calls Qt's 'QRectF QTransform::mapRect(const QRectF &a0) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtransform.html#mapRect

    Parameters
    ----------

    a0 : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QTransform::mapRect(const QRectF &a0) const
    address = self.uglySide.call(
        'ritual_ZNK10QTransform7mapRectERK6QRectF', self._valueOf(a0),
    )
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  def inline_type(self) -> TransformationType:
    """
    Calls Qt's 'TransformationType QTransform::inline_type() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtransform.html#inline_type

    Returns
    -------

    TransformationType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'TransformationType(number)' gives.
    """
    #  TransformationType QTransform::inline_type() const
    return QTransform.TransformationType(self.uglySide.call(
        'ritual_ZNK10QTransform11inline_typeEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float, float, float, float, float, float, float, float, float)
  def setMatrix(
      self,
      m11: float,
      m12: float,
      m13: float,
      m21: float,
      m22: float,
      m23: float,
      m31: float,
      m32: float,
      m33: float,
  ) -> None:
    """
    Calls Qt's 'void QTransform::setMatrix(qreal m11, qreal m12, qreal m13,
    qreal m21, qreal m22, qreal m23, qreal m31, qreal m32, qreal m33)'.

    Qt's own words: https://doc.qt.io/qt-6/qtransform.html#setMatrix

    Parameters
    ----------

    m11 : float
      Passed on as it is.

    m12 : float
      Passed on as it is.

    m13 : float
      Passed on as it is.

    m21 : float
      Passed on as it is.

    m22 : float
      Passed on as it is.

    m23 : float
      Passed on as it is.

    m31 : float
      Passed on as it is.

    m32 : float
      Passed on as it is.

    m33 : float
      Passed on as it is.
    """
    #  void QTransform::setMatrix(qreal m11, qreal m12, qreal m13, qreal m21,
    #      qreal m22, qreal m23, qreal m31, qreal m32, qreal m33)
    self.uglySide.call(
        'ritual_ZN10QTransform9setMatrixEddddddddd',
        m11, m12, m13, m21, m22, m23, m31, m32, m33,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __eq__(self, a0: QTransform) -> bool:
    """
    Calls Qt's 'bool QTransform::operator==(const QTransform &a0) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtransform.html#operator==

    Parameters
    ----------

    a0 : QTransform
      Passed on as a value: Qt reads the C++ QTransform, which stays Python's
      own.
    """
    #  bool QTransform::operator==(const QTransform &a0) const
    return self.uglySide.call(
        'ritual_ZNK10QTransformeqERKS_', self._valueOf(a0),
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
  def __ne__(self, a0: QTransform) -> bool:
    """
    Calls Qt's 'bool QTransform::operator!=(const QTransform &a0) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtransform.html#operator!=

    Parameters
    ----------

    a0 : QTransform
      Passed on as a value: Qt reads the C++ QTransform, which stays Python's
      own.
    """
    #  bool QTransform::operator!=(const QTransform &a0) const
    return self.uglySide.call(
        'ritual_ZNK10QTransformneERKS_', self._valueOf(a0),
    )

  @overload.fallback
  def __ne__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(THIS)
  def __imul__(self, a0: QTransform) -> QTransform:
    """
    Calls Qt's 'QTransform &QTransform::operator*=(const QTransform &a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qtransform.html#operator*=

    Parameters
    ----------

    a0 : QTransform
      Passed on as a value: Qt reads the C++ QTransform, which stays Python's
      own.
    """
    #  QTransform &QTransform::operator*=(const QTransform &a0)
    self.uglySide.call('ritual_ZN10QTransformmLERKS_', self._valueOf(a0))
    return self

  @overload(float)
  def __imul__(self, div: float) -> QTransform:
    """
    Calls Qt's 'QTransform &QTransform::operator*=(qreal div)'.

    Qt's own words: https://doc.qt.io/qt-6/qtransform.html#operator*=

    Parameters
    ----------

    div : float
      Passed on as it is.
    """
    #  QTransform &QTransform::operator*=(qreal div)
    self.uglySide.call('ritual_ZN10QTransformmLEd', div)
    return self

  @overload.fallback
  def __imul__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(THIS)
  def __mul__(self, o: QTransform) -> QTransform:
    """
    Calls Qt's 'QTransform QTransform::operator*(const QTransform &o) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtransform.html#operator*

    Parameters
    ----------

    o : QTransform
      Passed on as a value: Qt reads the C++ QTransform, which stays Python's
      own.

    Returns
    -------

    QTransform
      A new cute QTransform around the copy Qt gave back. Python owns it.
    """
    #  QTransform QTransform::operator*(const QTransform &o) const
    address = self.uglySide.call(
        'ritual_ZNK10QTransformmlERKS_', self._valueOf(o),
    )
    return QTransform._cuteOwning(address)

  @overload.fallback
  def __mul__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(float)
  def __itruediv__(self, div: float) -> QTransform:
    """
    Calls Qt's 'QTransform &QTransform::operator/=(qreal div)'.

    Qt's own words: https://doc.qt.io/qt-6/qtransform.html#operator/=

    Parameters
    ----------

    div : float
      Passed on as it is.
    """
    #  QTransform &QTransform::operator/=(qreal div)
    self.uglySide.call('ritual_ZN10QTransformdVEd', div)
    return self

  @overload.fallback
  def __itruediv__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(float)
  def __iadd__(self, div: float) -> QTransform:
    """
    Calls Qt's 'QTransform &QTransform::operator+=(qreal div)'.

    Qt's own words: https://doc.qt.io/qt-6/qtransform.html#operator+=

    Parameters
    ----------

    div : float
      Passed on as it is.
    """
    #  QTransform &QTransform::operator+=(qreal div)
    self.uglySide.call('ritual_ZN10QTransformpLEd', div)
    return self

  @overload.fallback
  def __iadd__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(float)
  def __isub__(self, div: float) -> QTransform:
    """
    Calls Qt's 'QTransform &QTransform::operator-=(qreal div)'.

    Qt's own words: https://doc.qt.io/qt-6/qtransform.html#operator-=

    Parameters
    ----------

    div : float
      Passed on as it is.
    """
    #  QTransform &QTransform::operator-=(qreal div)
    self.uglySide.call('ritual_ZN10QTransformmIEd', div)
    return self

  @overload.fallback
  def __isub__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(Qt.Initialization)
  def __init__(self, a0: Qt.Initialization) -> None:
    """
    Notes what was given, for Qt's 'QTransform::QTransform(Qt::Initialization
    a0)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qtransform.html#QTransform

    Parameters
    ----------

    a0 : Qt.Initialization
      Passed on as its number.
    """
    #  QTransform::QTransform(Qt::Initialization a0)
    self._noteCreation(QTransform, lambda: Rituals.call(
        'ritual_ZN10QTransformC1EN2Qt14InitializationE', a0.value,
    ))

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'QTransform::QTransform()', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qtransform.html#QTransform
    """
    #  QTransform::QTransform()
    self._noteCreation(QTransform, lambda: Rituals.call(
        'ritual_ZN10QTransformC1Ev',
    ))

  @overload(float, float, float, float, float, float, float, float, float)
  def __init__(
      self,
      h11: float,
      h12: float,
      h13: float,
      h21: float,
      h22: float,
      h23: float,
      h31: float,
      h32: float,
      h33: float,
  ) -> None:
    """
    Notes what was given, for Qt's 'QTransform::QTransform(qreal h11, qreal
    h12, qreal h13, qreal h21, qreal h22, qreal h23, qreal h31, qreal h32,
    qreal h33)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qtransform.html#QTransform

    Parameters
    ----------

    h11 : float
      Passed on as it is.

    h12 : float
      Passed on as it is.

    h13 : float
      Passed on as it is.

    h21 : float
      Passed on as it is.

    h22 : float
      Passed on as it is.

    h23 : float
      Passed on as it is.

    h31 : float
      Passed on as it is.

    h32 : float
      Passed on as it is.

    h33 : float
      Passed on as it is.
    """
    #  QTransform::QTransform(qreal h11, qreal h12, qreal h13, qreal h21,
    #      qreal h22, qreal h23, qreal h31, qreal h32, qreal h33)
    self._noteCreation(QTransform, lambda: Rituals.call(
        'ritual_ZN10QTransformC1Eddddddddd',
        h11, h12, h13, h21, h22, h23, h31, h32, h33,
    ))

  @overload(float, float, float, float, float, float)
  def __init__(
      self,
      h11: float,
      h12: float,
      h21: float,
      h22: float,
      dx: float,
      dy: float,
  ) -> None:
    """
    Notes what was given, for Qt's 'QTransform::QTransform(qreal h11, qreal
    h12, qreal h21, qreal h22, qreal dx, qreal dy)', which is called at the
    first use.

    Qt's own words: https://doc.qt.io/qt-6/qtransform.html#QTransform

    Parameters
    ----------

    h11 : float
      Passed on as it is.

    h12 : float
      Passed on as it is.

    h21 : float
      Passed on as it is.

    h22 : float
      Passed on as it is.

    dx : float
      Passed on as it is.

    dy : float
      Passed on as it is.
    """
    #  QTransform::QTransform(qreal h11, qreal h12, qreal h21, qreal h22,
    #      qreal dx, qreal dy)
    self._noteCreation(QTransform, lambda: Rituals.call(
        'ritual_ZN10QTransformC1Edddddd', h11, h12, h21, h22, dx, dy,
    ))

  @overload(THIS)
  def __init__(self, other: QTransform) -> None:
    """
    Notes what was given, for Qt's 'QTransform::QTransform(const QTransform
    &other)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qtransform.html#QTransform

    Parameters
    ----------

    other : QTransform
      Passed on as a value: Qt reads the C++ QTransform, which stays Python's
      own.
    """
    #  QTransform::QTransform(const QTransform &other)
    self._noteCreation(QTransform, lambda: Rituals.call(
        'ritual_ZN10QTransformC1ERKS_', self._valueOf(other),
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

  def reset(self) -> None:
    """
    Calls Qt's 'void QTransform::reset()'.

    Qt's own words: https://doc.qt.io/qt-6/qtransform.html#reset
    """
    #  void QTransform::reset()
    self.uglySide.call('ritual_ZN10QTransform5resetEv')

  @staticmethod
  def asAffineMatrix(*__, **_) -> Never:
    """
    Qt's 'Affine QTransform::asAffineMatrix()': gives a type Python has no
    way to take yet.
    """
    raise NotImplementedError(
        "'QTransform.asAffineMatrix' has no cute function yet. Qt's 'Affine "
        "QTransform::asAffineMatrix()': gives a type Python has no way to "
        "take yet.")

  @staticmethod
  def do_map(*__, **_) -> Never:
    """
    Qt's 'void QTransform::do_map(qreal x, qreal y, qreal &nx, qreal &ny)
    const': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QTransform.do_map' has no cute function yet. Qt's 'void "
        "QTransform::do_map(qreal x, qreal y, qreal &nx, qreal &ny) const': "
        "takes a number to change where it is.")

  @staticmethod
  def inverted(*__, **_) -> Never:
    """
    Qt's 'QTransform QTransform::inverted(bool *invertible) const': takes a
    number to change where it is.
    """
    raise NotImplementedError(
        "'QTransform.inverted' has no cute function yet. Qt's 'QTransform "
        "QTransform::inverted(bool *invertible) const': takes a number to "
        "change where it is.")

  @staticmethod
  def quadToQuad(*__, **_) -> Never:
    """
    Qt's 'bool QTransform::quadToQuad(const QPolygonF &one, const QPolygonF
    &two, QTransform &result)': takes a type Python has no way to hand over
    yet.
    """
    raise NotImplementedError(
        "'QTransform.quadToQuad' has no cute function yet. Qt's 'bool "
        "QTransform::quadToQuad(const QPolygonF &one, const QPolygonF &two, "
        "QTransform &result)': takes a type Python has no way to hand over "
        "yet.")

  @staticmethod
  def quadToSquare(*__, **_) -> Never:
    """
    Qt's 'bool QTransform::quadToSquare(const QPolygonF &quad, QTransform
    &result)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QTransform.quadToSquare' has no cute function yet. Qt's 'bool "
        "QTransform::quadToSquare(const QPolygonF &quad, QTransform "
        "&result)': takes a type Python has no way to hand over yet.")

  @staticmethod
  def rotate(*__, **_) -> Never:
    """
    - Qt's 'QTransform &QTransform::rotate(qreal a, Qt::Axis axis, qreal
      distanceToPlane)': gives a type Python has no way to take yet.
    - Qt's 'QTransform &QTransform::rotate(qreal a, Qt::Axis axis)': gives a
      type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QTransform.rotate' has no cute function yet. Qt's 'QTransform "
        "&QTransform::rotate(qreal a, Qt::Axis axis, qreal "
        "distanceToPlane)': gives a type Python has no way to take yet. "
        "Qt's 'QTransform &QTransform::rotate(qreal a, Qt::Axis axis)': "
        "gives a type Python has no way to take yet.")

  @staticmethod
  def rotateRadians(*__, **_) -> Never:
    """
    - Qt's 'QTransform &QTransform::rotateRadians(qreal a, Qt::Axis axis,
      qreal distanceToPlane)': gives a type Python has no way to take yet.
    - Qt's 'QTransform &QTransform::rotateRadians(qreal a, Qt::Axis axis)':
      gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QTransform.rotateRadians' has no cute function yet. Qt's "
        "'QTransform &QTransform::rotateRadians(qreal a, Qt::Axis axis, "
        "qreal distanceToPlane)': gives a type Python has no way to take "
        "yet. Qt's 'QTransform &QTransform::rotateRadians(qreal a, Qt::Axis "
        "axis)': gives a type Python has no way to take yet.")

  @staticmethod
  def scale(*__, **_) -> Never:
    """
    Qt's 'QTransform &QTransform::scale(qreal sx, qreal sy)': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QTransform.scale' has no cute function yet. Qt's 'QTransform "
        "&QTransform::scale(qreal sx, qreal sy)': gives a type Python has "
        "no way to take yet.")

  @staticmethod
  def shear(*__, **_) -> Never:
    """
    Qt's 'QTransform &QTransform::shear(qreal sh, qreal sv)': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QTransform.shear' has no cute function yet. Qt's 'QTransform "
        "&QTransform::shear(qreal sh, qreal sv)': gives a type Python has "
        "no way to take yet.")

  @staticmethod
  def squareToQuad(*__, **_) -> Never:
    """
    Qt's 'bool QTransform::squareToQuad(const QPolygonF &square, QTransform
    &result)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QTransform.squareToQuad' has no cute function yet. Qt's 'bool "
        "QTransform::squareToQuad(const QPolygonF &square, QTransform "
        "&result)': takes a type Python has no way to hand over yet.")

  @staticmethod
  def translate(*__, **_) -> Never:
    """
    Qt's 'QTransform &QTransform::translate(qreal dx, qreal dy)': gives a
    type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QTransform.translate' has no cute function yet. Qt's 'QTransform "
        "&QTransform::translate(qreal dx, qreal dy)': gives a type Python "
        "has no way to take yet.")
