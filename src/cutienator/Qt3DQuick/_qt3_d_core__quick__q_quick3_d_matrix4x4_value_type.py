"""
Qt3DCore::Quick::QQuick3DMatrix4x4ValueType binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DQuick/6.12.0/Qt3DQuick/private/qt3dquickvaluetypes_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means Qt3DCore::Quick::QQuick3DMatrix4x4ValueType to be private: it
#  declares the class in a header it calls private. cutienator does not care.
#  Qt hands objects of the class out all the same, and a class we are handed
#  is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from ..QtCore import QVariant
  from ..QtGui import QMatrix4x4, QVector3D, QVector4D
  from ..QtQml import QJSValue
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QJSValue = WAIT['QJSValue']
  QMatrix4x4 = WAIT['QMatrix4x4']
  QVector3D = WAIT['QVector3D']
  QVector4D = WAIT['QVector4D']


class QQuick3DMatrix4x4ValueType(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's Qt3DCore::Quick::QQuick3DMatrix4x4ValueType: a plain
  Python object standing in front of one C++
  Qt3DCore::Quick::QQuick3DMatrix4x4ValueType.

  C++ hands a Qt3DCore::Quick::QQuick3DMatrix4x4ValueType around as a copy,
  so every C++ Qt3DCore::Quick::QQuick3DMatrix4x4ValueType behind a cute one
  is Python's own: it is removed, by the ritual named in '__delete_ritual__',
  when the cute object goes.

  What exists
  -----------

  Every function of Qt's Qt3DCore::Quick::QQuick3DMatrix4x4ValueType that has
  a ritual and that Python can call so far, 46 names in all: 'create', 'm11',
  'm12', 'm13', 'm14', 'm21', 'm22', 'm23', 'm24', 'm31', 'm32', 'm33',
  'm34', 'm41', 'm42', 'm43', 'm44', 'setM11', 'setM12', 'setM13', 'setM14',
  'setM21', 'setM22', 'setM23', 'setM24', 'setM31', 'setM32', 'setM33',
  'setM34', 'setM41', 'setM42', 'setM43', 'setM44', 'translate', 'rotate',
  'scale', 'lookAt', 'times', 'plus', 'minus', 'row', 'column',
  'determinant', 'inverted', 'transposed', 'fuzzyEquals'. None can be made
  from Python: one comes out of a function of another class that gives one
  back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void
    Qt3DCore::Quick::QQuick3DMatrix4x4ValueType::qt_qmlMarker_foreign()': one
    of Qt's own inner workings.
  - Qt's 'void
    Qt3DCore::Quick::QQuick3DMatrix4x4ValueType::qt_qmlMarker_extended()':
    one of Qt's own inner workings.
  - Qt's 'Qt3DCore::Quick::QQuick3DMatrix4x4ValueType::
    ~QQuick3DMatrix4x4ValueType()': the destructor: Python removes its C++
    Qt3DCore::Quick::QQuick3DMatrix4x4ValueType by it, and has no other use
    for it.

  What has no ritual
  ------------------

  3 of the 58 functions Qt declares: 3 not a gap.

  What to expect
  --------------

  - The C++ Qt3DCore::Quick::QQuick3DMatrix4x4ValueType is created at the
    first use, not by 'Qt3DCore::Quick::QQuick3DMatrix4x4ValueType(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a Qt3DCore::Quick::QQuick3DMatrix4x4ValueType back
    gives a copy the ritual made for Python, in a new cute
    Qt3DCore::Quick::QQuick3DMatrix4x4ValueType.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QJSValue)
  def create(params: QJSValue) -> QVariant:
    """
    Calls Qt's 'QVariant
    Qt3DCore::Quick::QQuick3DMatrix4x4ValueType::create(const QJSValue
    &params)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-quick-qquick3dmatrix4x4valuetype.html

    Parameters
    ----------

    params : QJSValue
      Passed on as a value: Qt reads the C++ QJSValue, which stays Python's
      own.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant Qt3DCore::Quick::QQuick3DMatrix4x4ValueType::create(const
    #      QJSValue &params)
    address = Rituals.call(
        'ritual_ZN8Qt3DCore5Quick26QQuick3DMatrix4x4ValueType6createERK8QJS'
        'Value',
        CuteMixin._valueOf(params),
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DCore::Quick::QQuick3DMatrix4x4ValueType'

  #  Qt's '~Qt3DCore::Quick::QQuick3DMatrix4x4ValueType()'. Naming it makes
  #  this a value class: Python owns every C++
  #  Qt3DCore::Quick::QQuick3DMatrix4x4ValueType behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = (
      'ritual_ZN8Qt3DCore5Quick26QQuick3DMatrix4x4ValueTypeD1Ev')

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def m11(self) -> float:
    """
    Calls Qt's 'qreal Qt3DCore::Quick::QQuick3DMatrix4x4ValueType::m11()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-quick-qquick3dmatrix4x4valuetype.html#m11
    """
    #  qreal Qt3DCore::Quick::QQuick3DMatrix4x4ValueType::m11() const
    return self.uglySide.call(
        'ritual_ZNK8Qt3DCore5Quick26QQuick3DMatrix4x4ValueType3m11Ev',
    )

  def m12(self) -> float:
    """
    Calls Qt's 'qreal Qt3DCore::Quick::QQuick3DMatrix4x4ValueType::m12()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-quick-qquick3dmatrix4x4valuetype.html#m12
    """
    #  qreal Qt3DCore::Quick::QQuick3DMatrix4x4ValueType::m12() const
    return self.uglySide.call(
        'ritual_ZNK8Qt3DCore5Quick26QQuick3DMatrix4x4ValueType3m12Ev',
    )

  def m13(self) -> float:
    """
    Calls Qt's 'qreal Qt3DCore::Quick::QQuick3DMatrix4x4ValueType::m13()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-quick-qquick3dmatrix4x4valuetype.html#m13
    """
    #  qreal Qt3DCore::Quick::QQuick3DMatrix4x4ValueType::m13() const
    return self.uglySide.call(
        'ritual_ZNK8Qt3DCore5Quick26QQuick3DMatrix4x4ValueType3m13Ev',
    )

  def m14(self) -> float:
    """
    Calls Qt's 'qreal Qt3DCore::Quick::QQuick3DMatrix4x4ValueType::m14()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-quick-qquick3dmatrix4x4valuetype.html#m14
    """
    #  qreal Qt3DCore::Quick::QQuick3DMatrix4x4ValueType::m14() const
    return self.uglySide.call(
        'ritual_ZNK8Qt3DCore5Quick26QQuick3DMatrix4x4ValueType3m14Ev',
    )

  def m21(self) -> float:
    """
    Calls Qt's 'qreal Qt3DCore::Quick::QQuick3DMatrix4x4ValueType::m21()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-quick-qquick3dmatrix4x4valuetype.html#m21
    """
    #  qreal Qt3DCore::Quick::QQuick3DMatrix4x4ValueType::m21() const
    return self.uglySide.call(
        'ritual_ZNK8Qt3DCore5Quick26QQuick3DMatrix4x4ValueType3m21Ev',
    )

  def m22(self) -> float:
    """
    Calls Qt's 'qreal Qt3DCore::Quick::QQuick3DMatrix4x4ValueType::m22()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-quick-qquick3dmatrix4x4valuetype.html#m22
    """
    #  qreal Qt3DCore::Quick::QQuick3DMatrix4x4ValueType::m22() const
    return self.uglySide.call(
        'ritual_ZNK8Qt3DCore5Quick26QQuick3DMatrix4x4ValueType3m22Ev',
    )

  def m23(self) -> float:
    """
    Calls Qt's 'qreal Qt3DCore::Quick::QQuick3DMatrix4x4ValueType::m23()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-quick-qquick3dmatrix4x4valuetype.html#m23
    """
    #  qreal Qt3DCore::Quick::QQuick3DMatrix4x4ValueType::m23() const
    return self.uglySide.call(
        'ritual_ZNK8Qt3DCore5Quick26QQuick3DMatrix4x4ValueType3m23Ev',
    )

  def m24(self) -> float:
    """
    Calls Qt's 'qreal Qt3DCore::Quick::QQuick3DMatrix4x4ValueType::m24()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-quick-qquick3dmatrix4x4valuetype.html#m24
    """
    #  qreal Qt3DCore::Quick::QQuick3DMatrix4x4ValueType::m24() const
    return self.uglySide.call(
        'ritual_ZNK8Qt3DCore5Quick26QQuick3DMatrix4x4ValueType3m24Ev',
    )

  def m31(self) -> float:
    """
    Calls Qt's 'qreal Qt3DCore::Quick::QQuick3DMatrix4x4ValueType::m31()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-quick-qquick3dmatrix4x4valuetype.html#m31
    """
    #  qreal Qt3DCore::Quick::QQuick3DMatrix4x4ValueType::m31() const
    return self.uglySide.call(
        'ritual_ZNK8Qt3DCore5Quick26QQuick3DMatrix4x4ValueType3m31Ev',
    )

  def m32(self) -> float:
    """
    Calls Qt's 'qreal Qt3DCore::Quick::QQuick3DMatrix4x4ValueType::m32()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-quick-qquick3dmatrix4x4valuetype.html#m32
    """
    #  qreal Qt3DCore::Quick::QQuick3DMatrix4x4ValueType::m32() const
    return self.uglySide.call(
        'ritual_ZNK8Qt3DCore5Quick26QQuick3DMatrix4x4ValueType3m32Ev',
    )

  def m33(self) -> float:
    """
    Calls Qt's 'qreal Qt3DCore::Quick::QQuick3DMatrix4x4ValueType::m33()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-quick-qquick3dmatrix4x4valuetype.html#m33
    """
    #  qreal Qt3DCore::Quick::QQuick3DMatrix4x4ValueType::m33() const
    return self.uglySide.call(
        'ritual_ZNK8Qt3DCore5Quick26QQuick3DMatrix4x4ValueType3m33Ev',
    )

  def m34(self) -> float:
    """
    Calls Qt's 'qreal Qt3DCore::Quick::QQuick3DMatrix4x4ValueType::m34()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-quick-qquick3dmatrix4x4valuetype.html#m34
    """
    #  qreal Qt3DCore::Quick::QQuick3DMatrix4x4ValueType::m34() const
    return self.uglySide.call(
        'ritual_ZNK8Qt3DCore5Quick26QQuick3DMatrix4x4ValueType3m34Ev',
    )

  def m41(self) -> float:
    """
    Calls Qt's 'qreal Qt3DCore::Quick::QQuick3DMatrix4x4ValueType::m41()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-quick-qquick3dmatrix4x4valuetype.html#m41
    """
    #  qreal Qt3DCore::Quick::QQuick3DMatrix4x4ValueType::m41() const
    return self.uglySide.call(
        'ritual_ZNK8Qt3DCore5Quick26QQuick3DMatrix4x4ValueType3m41Ev',
    )

  def m42(self) -> float:
    """
    Calls Qt's 'qreal Qt3DCore::Quick::QQuick3DMatrix4x4ValueType::m42()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-quick-qquick3dmatrix4x4valuetype.html#m42
    """
    #  qreal Qt3DCore::Quick::QQuick3DMatrix4x4ValueType::m42() const
    return self.uglySide.call(
        'ritual_ZNK8Qt3DCore5Quick26QQuick3DMatrix4x4ValueType3m42Ev',
    )

  def m43(self) -> float:
    """
    Calls Qt's 'qreal Qt3DCore::Quick::QQuick3DMatrix4x4ValueType::m43()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-quick-qquick3dmatrix4x4valuetype.html#m43
    """
    #  qreal Qt3DCore::Quick::QQuick3DMatrix4x4ValueType::m43() const
    return self.uglySide.call(
        'ritual_ZNK8Qt3DCore5Quick26QQuick3DMatrix4x4ValueType3m43Ev',
    )

  def m44(self) -> float:
    """
    Calls Qt's 'qreal Qt3DCore::Quick::QQuick3DMatrix4x4ValueType::m44()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-quick-qquick3dmatrix4x4valuetype.html#m44
    """
    #  qreal Qt3DCore::Quick::QQuick3DMatrix4x4ValueType::m44() const
    return self.uglySide.call(
        'ritual_ZNK8Qt3DCore5Quick26QQuick3DMatrix4x4ValueType3m44Ev',
    )

  @overload(QMatrix4x4)
  def times(self, m: QMatrix4x4) -> QMatrix4x4:
    """
    Calls Qt's 'QMatrix4x4
    Qt3DCore::Quick::QQuick3DMatrix4x4ValueType::times(const QMatrix4x4 &m)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-quick-qquick3dmatrix4x4valuetype.html

    Parameters
    ----------

    m : QMatrix4x4
      Passed on as a value: Qt reads the C++ QMatrix4x4, which stays Python's
      own.

    Returns
    -------

    QMatrix4x4
      A new cute QMatrix4x4 around the copy Qt gave back. Python owns it.
    """
    #  QMatrix4x4 Qt3DCore::Quick::QQuick3DMatrix4x4ValueType::times(const
    #      QMatrix4x4 &m) const
    address = self.uglySide.call(
        'ritual_ZNK8Qt3DCore5Quick26QQuick3DMatrix4x4ValueType5timesERK10QM'
        'atrix4x4',
        self._valueOf(m),
    )
    from ..QtGui import QMatrix4x4
    return QMatrix4x4._cuteOwning(address)

  @overload(QVector4D)
  def times(self, vec: QVector4D) -> QVector4D:
    """
    Calls Qt's 'QVector4D
    Qt3DCore::Quick::QQuick3DMatrix4x4ValueType::times(const QVector4D &vec)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-quick-qquick3dmatrix4x4valuetype.html

    Parameters
    ----------

    vec : QVector4D
      Passed on as a value: Qt reads the C++ QVector4D, which stays Python's
      own.

    Returns
    -------

    QVector4D
      A new cute QVector4D around the copy Qt gave back. Python owns it.
    """
    #  QVector4D Qt3DCore::Quick::QQuick3DMatrix4x4ValueType::times(const
    #      QVector4D &vec) const
    address = self.uglySide.call(
        'ritual_ZNK8Qt3DCore5Quick26QQuick3DMatrix4x4ValueType5timesERK9QVe'
        'ctor4D',
        self._valueOf(vec),
    )
    from ..QtGui import QVector4D
    return QVector4D._cuteOwning(address)

  @overload(QVector3D)
  def times(self, vec: QVector3D) -> QVector3D:
    """
    Calls Qt's 'QVector3D
    Qt3DCore::Quick::QQuick3DMatrix4x4ValueType::times(const QVector3D &vec)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-quick-qquick3dmatrix4x4valuetype.html

    Parameters
    ----------

    vec : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  QVector3D Qt3DCore::Quick::QQuick3DMatrix4x4ValueType::times(const
    #      QVector3D &vec) const
    address = self.uglySide.call(
        'ritual_ZNK8Qt3DCore5Quick26QQuick3DMatrix4x4ValueType5timesERK9QVe'
        'ctor3D',
        self._valueOf(vec),
    )
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  @overload(float)
  def times(self, factor: float) -> QMatrix4x4:
    """
    Calls Qt's 'QMatrix4x4
    Qt3DCore::Quick::QQuick3DMatrix4x4ValueType::times(qreal factor) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-quick-qquick3dmatrix4x4valuetype.html

    Parameters
    ----------

    factor : float
      Passed on as it is.

    Returns
    -------

    QMatrix4x4
      A new cute QMatrix4x4 around the copy Qt gave back. Python owns it.
    """
    #  QMatrix4x4 Qt3DCore::Quick::QQuick3DMatrix4x4ValueType::times(qreal
    #      factor) const
    address = self.uglySide.call(
        'ritual_ZNK8Qt3DCore5Quick26QQuick3DMatrix4x4ValueType5timesEd',
        factor,
    )
    from ..QtGui import QMatrix4x4
    return QMatrix4x4._cuteOwning(address)

  @overload(QMatrix4x4)
  def plus(self, m: QMatrix4x4) -> QMatrix4x4:
    """
    Calls Qt's 'QMatrix4x4
    Qt3DCore::Quick::QQuick3DMatrix4x4ValueType::plus(const QMatrix4x4 &m)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-quick-qquick3dmatrix4x4valuetype.html

    Parameters
    ----------

    m : QMatrix4x4
      Passed on as a value: Qt reads the C++ QMatrix4x4, which stays Python's
      own.

    Returns
    -------

    QMatrix4x4
      A new cute QMatrix4x4 around the copy Qt gave back. Python owns it.
    """
    #  QMatrix4x4 Qt3DCore::Quick::QQuick3DMatrix4x4ValueType::plus(const
    #      QMatrix4x4 &m) const
    address = self.uglySide.call(
        'ritual_ZNK8Qt3DCore5Quick26QQuick3DMatrix4x4ValueType4plusERK10QMa'
        'trix4x4',
        self._valueOf(m),
    )
    from ..QtGui import QMatrix4x4
    return QMatrix4x4._cuteOwning(address)

  @overload(QMatrix4x4)
  def minus(self, m: QMatrix4x4) -> QMatrix4x4:
    """
    Calls Qt's 'QMatrix4x4
    Qt3DCore::Quick::QQuick3DMatrix4x4ValueType::minus(const QMatrix4x4 &m)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-quick-qquick3dmatrix4x4valuetype.html

    Parameters
    ----------

    m : QMatrix4x4
      Passed on as a value: Qt reads the C++ QMatrix4x4, which stays Python's
      own.

    Returns
    -------

    QMatrix4x4
      A new cute QMatrix4x4 around the copy Qt gave back. Python owns it.
    """
    #  QMatrix4x4 Qt3DCore::Quick::QQuick3DMatrix4x4ValueType::minus(const
    #      QMatrix4x4 &m) const
    address = self.uglySide.call(
        'ritual_ZNK8Qt3DCore5Quick26QQuick3DMatrix4x4ValueType5minusERK10QM'
        'atrix4x4',
        self._valueOf(m),
    )
    from ..QtGui import QMatrix4x4
    return QMatrix4x4._cuteOwning(address)

  @overload(int)
  def row(self, n: int) -> QVector4D:
    """
    Calls Qt's 'QVector4D
    Qt3DCore::Quick::QQuick3DMatrix4x4ValueType::row(int n) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-quick-qquick3dmatrix4x4valuetype.html#row

    Parameters
    ----------

    n : int
      Passed on as it is.

    Returns
    -------

    QVector4D
      A new cute QVector4D around the copy Qt gave back. Python owns it.
    """
    #  QVector4D Qt3DCore::Quick::QQuick3DMatrix4x4ValueType::row(int n)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK8Qt3DCore5Quick26QQuick3DMatrix4x4ValueType3rowEi', n,
    )
    from ..QtGui import QVector4D
    return QVector4D._cuteOwning(address)

  @overload(int)
  def column(self, m: int) -> QVector4D:
    """
    Calls Qt's 'QVector4D
    Qt3DCore::Quick::QQuick3DMatrix4x4ValueType::column(int m) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-quick-qquick3dmatrix4x4valuetype.html

    Parameters
    ----------

    m : int
      Passed on as it is.

    Returns
    -------

    QVector4D
      A new cute QVector4D around the copy Qt gave back. Python owns it.
    """
    #  QVector4D Qt3DCore::Quick::QQuick3DMatrix4x4ValueType::column(int m)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK8Qt3DCore5Quick26QQuick3DMatrix4x4ValueType6columnEi', m,
    )
    from ..QtGui import QVector4D
    return QVector4D._cuteOwning(address)

  def determinant(self) -> float:
    """
    Calls Qt's 'qreal
    Qt3DCore::Quick::QQuick3DMatrix4x4ValueType::determinant() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-quick-qquick3dmatrix4x4valuetype.html
    """
    #  qreal Qt3DCore::Quick::QQuick3DMatrix4x4ValueType::determinant() const
    return self.uglySide.call(
        'ritual_ZNK8Qt3DCore5Quick26QQuick3DMatrix4x4ValueType11determinant'
        'Ev',
    )

  def inverted(self) -> QMatrix4x4:
    """
    Calls Qt's 'QMatrix4x4
    Qt3DCore::Quick::QQuick3DMatrix4x4ValueType::inverted() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-quick-qquick3dmatrix4x4valuetype.html

    Returns
    -------

    QMatrix4x4
      A new cute QMatrix4x4 around the copy Qt gave back. Python owns it.
    """
    #  QMatrix4x4 Qt3DCore::Quick::QQuick3DMatrix4x4ValueType::inverted()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK8Qt3DCore5Quick26QQuick3DMatrix4x4ValueType8invertedEv',
    )
    from ..QtGui import QMatrix4x4
    return QMatrix4x4._cuteOwning(address)

  def transposed(self) -> QMatrix4x4:
    """
    Calls Qt's 'QMatrix4x4
    Qt3DCore::Quick::QQuick3DMatrix4x4ValueType::transposed() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-quick-qquick3dmatrix4x4valuetype.html

    Returns
    -------

    QMatrix4x4
      A new cute QMatrix4x4 around the copy Qt gave back. Python owns it.
    """
    #  QMatrix4x4 Qt3DCore::Quick::QQuick3DMatrix4x4ValueType::transposed()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK8Qt3DCore5Quick26QQuick3DMatrix4x4ValueType10transposedE'
        'v',
    )
    from ..QtGui import QMatrix4x4
    return QMatrix4x4._cuteOwning(address)

  @overload(QMatrix4x4, float)
  def fuzzyEquals(self, m: QMatrix4x4, epsilon: float) -> bool:
    """
    Calls Qt's 'bool
    Qt3DCore::Quick::QQuick3DMatrix4x4ValueType::fuzzyEquals(const QMatrix4x4
    &m, qreal epsilon) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-quick-qquick3dmatrix4x4valuetype.html

    Parameters
    ----------

    m : QMatrix4x4
      Passed on as a value: Qt reads the C++ QMatrix4x4, which stays Python's
      own.

    epsilon : float
      Passed on as it is.
    """
    #  bool Qt3DCore::Quick::QQuick3DMatrix4x4ValueType::fuzzyEquals(const
    #      QMatrix4x4 &m, qreal epsilon) const
    return self.uglySide.call(
        'ritual_ZNK8Qt3DCore5Quick26QQuick3DMatrix4x4ValueType11fuzzyEquals'
        'ERK10QMatrix4x4d',
        self._valueOf(m), epsilon,
    )

  @overload(QMatrix4x4)
  def fuzzyEquals(self, m: QMatrix4x4) -> bool:
    """
    Calls Qt's 'bool
    Qt3DCore::Quick::QQuick3DMatrix4x4ValueType::fuzzyEquals(const QMatrix4x4
    &m) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-quick-qquick3dmatrix4x4valuetype.html

    Parameters
    ----------

    m : QMatrix4x4
      Passed on as a value: Qt reads the C++ QMatrix4x4, which stays Python's
      own.
    """
    #  bool Qt3DCore::Quick::QQuick3DMatrix4x4ValueType::fuzzyEquals(const
    #      QMatrix4x4 &m) const
    return self.uglySide.call(
        'ritual_ZNK8Qt3DCore5Quick26QQuick3DMatrix4x4ValueType11fuzzyEquals'
        'ERK10QMatrix4x4',
        self._valueOf(m),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float)
  def setM11(self, value: float) -> None:
    """
    Calls Qt's 'void
    Qt3DCore::Quick::QQuick3DMatrix4x4ValueType::setM11(qreal value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-quick-qquick3dmatrix4x4valuetype.html

    Parameters
    ----------

    value : float
      Passed on as it is.
    """
    #  void Qt3DCore::Quick::QQuick3DMatrix4x4ValueType::setM11(qreal value)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore5Quick26QQuick3DMatrix4x4ValueType6setM11Ed',
        value,
    )

  @overload(float)
  def setM12(self, value: float) -> None:
    """
    Calls Qt's 'void
    Qt3DCore::Quick::QQuick3DMatrix4x4ValueType::setM12(qreal value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-quick-qquick3dmatrix4x4valuetype.html

    Parameters
    ----------

    value : float
      Passed on as it is.
    """
    #  void Qt3DCore::Quick::QQuick3DMatrix4x4ValueType::setM12(qreal value)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore5Quick26QQuick3DMatrix4x4ValueType6setM12Ed',
        value,
    )

  @overload(float)
  def setM13(self, value: float) -> None:
    """
    Calls Qt's 'void
    Qt3DCore::Quick::QQuick3DMatrix4x4ValueType::setM13(qreal value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-quick-qquick3dmatrix4x4valuetype.html

    Parameters
    ----------

    value : float
      Passed on as it is.
    """
    #  void Qt3DCore::Quick::QQuick3DMatrix4x4ValueType::setM13(qreal value)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore5Quick26QQuick3DMatrix4x4ValueType6setM13Ed',
        value,
    )

  @overload(float)
  def setM14(self, value: float) -> None:
    """
    Calls Qt's 'void
    Qt3DCore::Quick::QQuick3DMatrix4x4ValueType::setM14(qreal value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-quick-qquick3dmatrix4x4valuetype.html

    Parameters
    ----------

    value : float
      Passed on as it is.
    """
    #  void Qt3DCore::Quick::QQuick3DMatrix4x4ValueType::setM14(qreal value)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore5Quick26QQuick3DMatrix4x4ValueType6setM14Ed',
        value,
    )

  @overload(float)
  def setM21(self, value: float) -> None:
    """
    Calls Qt's 'void
    Qt3DCore::Quick::QQuick3DMatrix4x4ValueType::setM21(qreal value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-quick-qquick3dmatrix4x4valuetype.html

    Parameters
    ----------

    value : float
      Passed on as it is.
    """
    #  void Qt3DCore::Quick::QQuick3DMatrix4x4ValueType::setM21(qreal value)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore5Quick26QQuick3DMatrix4x4ValueType6setM21Ed',
        value,
    )

  @overload(float)
  def setM22(self, value: float) -> None:
    """
    Calls Qt's 'void
    Qt3DCore::Quick::QQuick3DMatrix4x4ValueType::setM22(qreal value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-quick-qquick3dmatrix4x4valuetype.html

    Parameters
    ----------

    value : float
      Passed on as it is.
    """
    #  void Qt3DCore::Quick::QQuick3DMatrix4x4ValueType::setM22(qreal value)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore5Quick26QQuick3DMatrix4x4ValueType6setM22Ed',
        value,
    )

  @overload(float)
  def setM23(self, value: float) -> None:
    """
    Calls Qt's 'void
    Qt3DCore::Quick::QQuick3DMatrix4x4ValueType::setM23(qreal value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-quick-qquick3dmatrix4x4valuetype.html

    Parameters
    ----------

    value : float
      Passed on as it is.
    """
    #  void Qt3DCore::Quick::QQuick3DMatrix4x4ValueType::setM23(qreal value)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore5Quick26QQuick3DMatrix4x4ValueType6setM23Ed',
        value,
    )

  @overload(float)
  def setM24(self, value: float) -> None:
    """
    Calls Qt's 'void
    Qt3DCore::Quick::QQuick3DMatrix4x4ValueType::setM24(qreal value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-quick-qquick3dmatrix4x4valuetype.html

    Parameters
    ----------

    value : float
      Passed on as it is.
    """
    #  void Qt3DCore::Quick::QQuick3DMatrix4x4ValueType::setM24(qreal value)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore5Quick26QQuick3DMatrix4x4ValueType6setM24Ed',
        value,
    )

  @overload(float)
  def setM31(self, value: float) -> None:
    """
    Calls Qt's 'void
    Qt3DCore::Quick::QQuick3DMatrix4x4ValueType::setM31(qreal value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-quick-qquick3dmatrix4x4valuetype.html

    Parameters
    ----------

    value : float
      Passed on as it is.
    """
    #  void Qt3DCore::Quick::QQuick3DMatrix4x4ValueType::setM31(qreal value)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore5Quick26QQuick3DMatrix4x4ValueType6setM31Ed',
        value,
    )

  @overload(float)
  def setM32(self, value: float) -> None:
    """
    Calls Qt's 'void
    Qt3DCore::Quick::QQuick3DMatrix4x4ValueType::setM32(qreal value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-quick-qquick3dmatrix4x4valuetype.html

    Parameters
    ----------

    value : float
      Passed on as it is.
    """
    #  void Qt3DCore::Quick::QQuick3DMatrix4x4ValueType::setM32(qreal value)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore5Quick26QQuick3DMatrix4x4ValueType6setM32Ed',
        value,
    )

  @overload(float)
  def setM33(self, value: float) -> None:
    """
    Calls Qt's 'void
    Qt3DCore::Quick::QQuick3DMatrix4x4ValueType::setM33(qreal value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-quick-qquick3dmatrix4x4valuetype.html

    Parameters
    ----------

    value : float
      Passed on as it is.
    """
    #  void Qt3DCore::Quick::QQuick3DMatrix4x4ValueType::setM33(qreal value)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore5Quick26QQuick3DMatrix4x4ValueType6setM33Ed',
        value,
    )

  @overload(float)
  def setM34(self, value: float) -> None:
    """
    Calls Qt's 'void
    Qt3DCore::Quick::QQuick3DMatrix4x4ValueType::setM34(qreal value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-quick-qquick3dmatrix4x4valuetype.html

    Parameters
    ----------

    value : float
      Passed on as it is.
    """
    #  void Qt3DCore::Quick::QQuick3DMatrix4x4ValueType::setM34(qreal value)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore5Quick26QQuick3DMatrix4x4ValueType6setM34Ed',
        value,
    )

  @overload(float)
  def setM41(self, value: float) -> None:
    """
    Calls Qt's 'void
    Qt3DCore::Quick::QQuick3DMatrix4x4ValueType::setM41(qreal value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-quick-qquick3dmatrix4x4valuetype.html

    Parameters
    ----------

    value : float
      Passed on as it is.
    """
    #  void Qt3DCore::Quick::QQuick3DMatrix4x4ValueType::setM41(qreal value)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore5Quick26QQuick3DMatrix4x4ValueType6setM41Ed',
        value,
    )

  @overload(float)
  def setM42(self, value: float) -> None:
    """
    Calls Qt's 'void
    Qt3DCore::Quick::QQuick3DMatrix4x4ValueType::setM42(qreal value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-quick-qquick3dmatrix4x4valuetype.html

    Parameters
    ----------

    value : float
      Passed on as it is.
    """
    #  void Qt3DCore::Quick::QQuick3DMatrix4x4ValueType::setM42(qreal value)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore5Quick26QQuick3DMatrix4x4ValueType6setM42Ed',
        value,
    )

  @overload(float)
  def setM43(self, value: float) -> None:
    """
    Calls Qt's 'void
    Qt3DCore::Quick::QQuick3DMatrix4x4ValueType::setM43(qreal value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-quick-qquick3dmatrix4x4valuetype.html

    Parameters
    ----------

    value : float
      Passed on as it is.
    """
    #  void Qt3DCore::Quick::QQuick3DMatrix4x4ValueType::setM43(qreal value)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore5Quick26QQuick3DMatrix4x4ValueType6setM43Ed',
        value,
    )

  @overload(float)
  def setM44(self, value: float) -> None:
    """
    Calls Qt's 'void
    Qt3DCore::Quick::QQuick3DMatrix4x4ValueType::setM44(qreal value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-quick-qquick3dmatrix4x4valuetype.html

    Parameters
    ----------

    value : float
      Passed on as it is.
    """
    #  void Qt3DCore::Quick::QQuick3DMatrix4x4ValueType::setM44(qreal value)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore5Quick26QQuick3DMatrix4x4ValueType6setM44Ed',
        value,
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
  def translate(self, t: QVector3D) -> None:
    """
    Calls Qt's 'void
    Qt3DCore::Quick::QQuick3DMatrix4x4ValueType::translate(const QVector3D
    &t)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-quick-qquick3dmatrix4x4valuetype.html

    Parameters
    ----------

    t : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.
    """
    #  void Qt3DCore::Quick::QQuick3DMatrix4x4ValueType::translate(const
    #      QVector3D &t)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore5Quick26QQuick3DMatrix4x4ValueType9translateERK9'
        'QVector3D',
        self._valueOf(t),
    )

  @overload(float, QVector3D)
  def rotate(self, angle: float, axis: QVector3D) -> None:
    """
    Calls Qt's 'void
    Qt3DCore::Quick::QQuick3DMatrix4x4ValueType::rotate(float angle, const
    QVector3D &axis)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-quick-qquick3dmatrix4x4valuetype.html

    Parameters
    ----------

    angle : float
      Passed on as it is.

    axis : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.
    """
    #  void Qt3DCore::Quick::QQuick3DMatrix4x4ValueType::rotate(float angle,
    #      const QVector3D &axis)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore5Quick26QQuick3DMatrix4x4ValueType6rotateEfRK9QV'
        'ector3D',
        angle, self._valueOf(axis),
    )

  @overload(float)
  def scale(self, s: float) -> None:
    """
    Calls Qt's 'void Qt3DCore::Quick::QQuick3DMatrix4x4ValueType::scale(float
    s)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-quick-qquick3dmatrix4x4valuetype.html

    Parameters
    ----------

    s : float
      Passed on as it is.
    """
    #  void Qt3DCore::Quick::QQuick3DMatrix4x4ValueType::scale(float s)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore5Quick26QQuick3DMatrix4x4ValueType5scaleEf', s,
    )

  @overload(float, float, float)
  def scale(self, sx: float, sy: float, sz: float) -> None:
    """
    Calls Qt's 'void Qt3DCore::Quick::QQuick3DMatrix4x4ValueType::scale(float
    sx, float sy, float sz)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-quick-qquick3dmatrix4x4valuetype.html

    Parameters
    ----------

    sx : float
      Passed on as it is.

    sy : float
      Passed on as it is.

    sz : float
      Passed on as it is.
    """
    #  void Qt3DCore::Quick::QQuick3DMatrix4x4ValueType::scale(float sx,
    #      float sy, float sz)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore5Quick26QQuick3DMatrix4x4ValueType5scaleEfff',
        sx, sy, sz,
    )

  @overload(QVector3D)
  def scale(self, s: QVector3D) -> None:
    """
    Calls Qt's 'void Qt3DCore::Quick::QQuick3DMatrix4x4ValueType::scale(const
    QVector3D &s)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-quick-qquick3dmatrix4x4valuetype.html

    Parameters
    ----------

    s : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.
    """
    #  void Qt3DCore::Quick::QQuick3DMatrix4x4ValueType::scale(const
    #      QVector3D &s)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore5Quick26QQuick3DMatrix4x4ValueType5scaleERK9QVec'
        'tor3D',
        self._valueOf(s),
    )

  @overload(QVector3D, QVector3D, QVector3D)
  def lookAt(self, eye: QVector3D, center: QVector3D, up: QVector3D) -> None:
    """
    Calls Qt's 'void
    Qt3DCore::Quick::QQuick3DMatrix4x4ValueType::lookAt(const QVector3D &eye,
    const QVector3D &center, const QVector3D &up)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-quick-qquick3dmatrix4x4valuetype.html

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
    #  void Qt3DCore::Quick::QQuick3DMatrix4x4ValueType::lookAt(const
    #      QVector3D &eye, const QVector3D &center, const QVector3D &up)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore5Quick26QQuick3DMatrix4x4ValueType6lookAtERK9QVe'
        'ctor3DS4_S4_',
        self._valueOf(eye), self._valueOf(center), self._valueOf(up),
    )
