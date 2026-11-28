"""
Qt3DCore::Quick::QQuick3DQuaternionValueType binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DQuick/6.12.0/Qt3DQuick/private/qt3dquickvaluetypes_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means Qt3DCore::Quick::QQuick3DQuaternionValueType to be private: it
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
  from ..QtQml import QJSValue
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QJSValue = WAIT['QJSValue']


class QQuick3DQuaternionValueType(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's Qt3DCore::Quick::QQuick3DQuaternionValueType: a plain
  Python object standing in front of one C++
  Qt3DCore::Quick::QQuick3DQuaternionValueType.

  C++ hands a Qt3DCore::Quick::QQuick3DQuaternionValueType around as a copy,
  so every C++ Qt3DCore::Quick::QQuick3DQuaternionValueType behind a cute one
  is Python's own: it is removed, by the ritual named in '__delete_ritual__',
  when the cute object goes.

  What exists
  -----------

  Every function of Qt's Qt3DCore::Quick::QQuick3DQuaternionValueType that
  has a ritual and that Python can call so far, 10 names in all: 'create',
  'toString', 'scalar', 'x', 'y', 'z', 'setScalar', 'setX', 'setY', 'setZ'.
  None can be made from Python: one comes out of a function of another class
  that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void
    Qt3DCore::Quick::QQuick3DQuaternionValueType::qt_qmlMarker_foreign()':
    one of Qt's own inner workings.
  - Qt's 'void
    Qt3DCore::Quick::QQuick3DQuaternionValueType::qt_qmlMarker_extended()':
    one of Qt's own inner workings.
  - Qt's 'Qt3DCore::Quick::QQuick3DQuaternionValueType::
    ~QQuick3DQuaternionValueType()': the destructor: Python removes its C++
    Qt3DCore::Quick::QQuick3DQuaternionValueType by it, and has no other use
    for it.

  What has no ritual
  ------------------

  3 of the 16 functions Qt declares: 3 not a gap.

  What to expect
  --------------

  - The C++ Qt3DCore::Quick::QQuick3DQuaternionValueType is created at the
    first use, not by 'Qt3DCore::Quick::QQuick3DQuaternionValueType(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a Qt3DCore::Quick::QQuick3DQuaternionValueType back
    gives a copy the ritual made for Python, in a new cute
    Qt3DCore::Quick::QQuick3DQuaternionValueType.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QJSValue)
  def create(params: QJSValue) -> QVariant:
    """
    Calls Qt's 'QVariant
    Qt3DCore::Quick::QQuick3DQuaternionValueType::create(const QJSValue
    &params)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-quick-qquick3dquaternionvaluetype.html

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
    #  QVariant Qt3DCore::Quick::QQuick3DQuaternionValueType::create(const
    #      QJSValue &params)
    address = Rituals.call(
        'ritual_ZN8Qt3DCore5Quick27QQuick3DQuaternionValueType6createERK8QJ'
        'SValue',
        CuteMixin._valueOf(params),
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DCore::Quick::QQuick3DQuaternionValueType'

  #  Qt's '~Qt3DCore::Quick::QQuick3DQuaternionValueType()'. Naming it makes
  #  this a value class: Python owns every C++
  #  Qt3DCore::Quick::QQuick3DQuaternionValueType behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = (
      'ritual_ZN8Qt3DCore5Quick27QQuick3DQuaternionValueTypeD1Ev')

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def toString(self) -> str:
    """
    Calls Qt's 'QString
    Qt3DCore::Quick::QQuick3DQuaternionValueType::toString() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-quick-qquick3dquaternionvaluetype.html

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString Qt3DCore::Quick::QQuick3DQuaternionValueType::toString() const
    return self.uglySide.call(
        'ritual_ZNK8Qt3DCore5Quick27QQuick3DQuaternionValueType8toStringEv',
    )

  def scalar(self) -> float:
    """
    Calls Qt's 'qreal Qt3DCore::Quick::QQuick3DQuaternionValueType::scalar()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-quick-qquick3dquaternionvaluetype.html
    """
    #  qreal Qt3DCore::Quick::QQuick3DQuaternionValueType::scalar() const
    return self.uglySide.call(
        'ritual_ZNK8Qt3DCore5Quick27QQuick3DQuaternionValueType6scalarEv',
    )

  def x(self) -> float:
    """
    Calls Qt's 'qreal Qt3DCore::Quick::QQuick3DQuaternionValueType::x()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-quick-qquick3dquaternionvaluetype.html#x
    """
    #  qreal Qt3DCore::Quick::QQuick3DQuaternionValueType::x() const
    return self.uglySide.call(
        'ritual_ZNK8Qt3DCore5Quick27QQuick3DQuaternionValueType1xEv',
    )

  def y(self) -> float:
    """
    Calls Qt's 'qreal Qt3DCore::Quick::QQuick3DQuaternionValueType::y()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-quick-qquick3dquaternionvaluetype.html#y
    """
    #  qreal Qt3DCore::Quick::QQuick3DQuaternionValueType::y() const
    return self.uglySide.call(
        'ritual_ZNK8Qt3DCore5Quick27QQuick3DQuaternionValueType1yEv',
    )

  def z(self) -> float:
    """
    Calls Qt's 'qreal Qt3DCore::Quick::QQuick3DQuaternionValueType::z()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-quick-qquick3dquaternionvaluetype.html#z
    """
    #  qreal Qt3DCore::Quick::QQuick3DQuaternionValueType::z() const
    return self.uglySide.call(
        'ritual_ZNK8Qt3DCore5Quick27QQuick3DQuaternionValueType1zEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float)
  def setScalar(self, a0: float) -> None:
    """
    Calls Qt's 'void
    Qt3DCore::Quick::QQuick3DQuaternionValueType::setScalar(qreal a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-quick-qquick3dquaternionvaluetype.html

    Parameters
    ----------

    a0 : float
      Passed on as it is.
    """
    #  void Qt3DCore::Quick::QQuick3DQuaternionValueType::setScalar(qreal a0)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore5Quick27QQuick3DQuaternionValueType9setScalarEd',
        a0,
    )

  @overload(float)
  def setX(self, a0: float) -> None:
    """
    Calls Qt's 'void Qt3DCore::Quick::QQuick3DQuaternionValueType::setX(qreal
    a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-quick-qquick3dquaternionvaluetype.html

    Parameters
    ----------

    a0 : float
      Passed on as it is.
    """
    #  void Qt3DCore::Quick::QQuick3DQuaternionValueType::setX(qreal a0)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore5Quick27QQuick3DQuaternionValueType4setXEd', a0,
    )

  @overload(float)
  def setY(self, a0: float) -> None:
    """
    Calls Qt's 'void Qt3DCore::Quick::QQuick3DQuaternionValueType::setY(qreal
    a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-quick-qquick3dquaternionvaluetype.html

    Parameters
    ----------

    a0 : float
      Passed on as it is.
    """
    #  void Qt3DCore::Quick::QQuick3DQuaternionValueType::setY(qreal a0)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore5Quick27QQuick3DQuaternionValueType4setYEd', a0,
    )

  @overload(float)
  def setZ(self, a0: float) -> None:
    """
    Calls Qt's 'void Qt3DCore::Quick::QQuick3DQuaternionValueType::setZ(qreal
    a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-quick-qquick3dquaternionvaluetype.html

    Parameters
    ----------

    a0 : float
      Passed on as it is.
    """
    #  void Qt3DCore::Quick::QQuick3DQuaternionValueType::setZ(qreal a0)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore5Quick27QQuick3DQuaternionValueType4setZEd', a0,
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
