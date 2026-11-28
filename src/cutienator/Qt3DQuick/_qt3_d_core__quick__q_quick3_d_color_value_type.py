"""
Qt3DCore::Quick::QQuick3DColorValueType binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DQuick/6.12.0/Qt3DQuick/private/qt3dquickvaluetypes_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means Qt3DCore::Quick::QQuick3DColorValueType to be private: it
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
  QVariant = WAIT['QVariant']


class QQuick3DColorValueType(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's Qt3DCore::Quick::QQuick3DColorValueType: a plain
  Python object standing in front of one C++
  Qt3DCore::Quick::QQuick3DColorValueType.

  C++ hands a Qt3DCore::Quick::QQuick3DColorValueType around as a copy, so
  every C++ Qt3DCore::Quick::QQuick3DColorValueType behind a cute one is
  Python's own: it is removed, by the ritual named in '__delete_ritual__',
  when the cute object goes.

  What exists
  -----------

  Every function of Qt's Qt3DCore::Quick::QQuick3DColorValueType that has a
  ritual and that Python can call so far, 27 names in all: 'create',
  'toString', 'alpha', 'lighter', 'darker', 'tint', 'r', 'g', 'b', 'a',
  'hsvHue', 'hsvSaturation', 'hsvValue', 'hslHue', 'hslSaturation',
  'hslLightness', 'isValid', 'setR', 'setG', 'setB', 'setA', 'setHsvHue',
  'setHsvSaturation', 'setHsvValue', 'setHslHue', 'setHslSaturation',
  'setHslLightness'. None can be made from Python: one comes out of a
  function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void
    Qt3DCore::Quick::QQuick3DColorValueType::qt_qmlMarker_foreign()': one of
    Qt's own inner workings.
  - Qt's 'void
    Qt3DCore::Quick::QQuick3DColorValueType::qt_qmlMarker_extended()': one of
    Qt's own inner workings.
  - Qt's
    'Qt3DCore::Quick::QQuick3DColorValueType::~QQuick3DColorValueType()': the
    destructor: Python removes its C++
    Qt3DCore::Quick::QQuick3DColorValueType by it, and has no other use for
    it.

  What has no ritual
  ------------------

  3 of the 33 functions Qt declares: 3 not a gap.

  What to expect
  --------------

  - The C++ Qt3DCore::Quick::QQuick3DColorValueType is created at the first
    use, not by 'Qt3DCore::Quick::QQuick3DColorValueType(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a Qt3DCore::Quick::QQuick3DColorValueType back gives a
    copy the ritual made for Python, in a new cute
    Qt3DCore::Quick::QQuick3DColorValueType.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QJSValue)
  def create(params: QJSValue) -> QVariant:
    """
    Calls Qt's 'QVariant
    Qt3DCore::Quick::QQuick3DColorValueType::create(const QJSValue &params)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-quick-qquick3dcolorvaluetype.html#create

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
    #  QVariant Qt3DCore::Quick::QQuick3DColorValueType::create(const
    #      QJSValue &params)
    address = Rituals.call(
        'ritual_ZN8Qt3DCore5Quick22QQuick3DColorValueType6createERK8QJSValu'
        'e',
        CuteMixin._valueOf(params),
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DCore::Quick::QQuick3DColorValueType'

  #  Qt's '~Qt3DCore::Quick::QQuick3DColorValueType()'. Naming it makes this
  #  a value class: Python owns every C++
  #  Qt3DCore::Quick::QQuick3DColorValueType behind a cute one, and removes
  #  it by this ritual.
  __delete_ritual__ = 'ritual_ZN8Qt3DCore5Quick22QQuick3DColorValueTypeD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def toString(self) -> str:
    """
    Calls Qt's 'QString Qt3DCore::Quick::QQuick3DColorValueType::toString()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-quick-qquick3dcolorvaluetype.html

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString Qt3DCore::Quick::QQuick3DColorValueType::toString() const
    return self.uglySide.call(
        'ritual_ZNK8Qt3DCore5Quick22QQuick3DColorValueType8toStringEv',
    )

  @overload(float)
  def alpha(self, value: float) -> QVariant:
    """
    Calls Qt's 'QVariant Qt3DCore::Quick::QQuick3DColorValueType::alpha(qreal
    value) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-quick-qquick3dcolorvaluetype.html#alpha

    Parameters
    ----------

    value : float
      Passed on as it is.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant Qt3DCore::Quick::QQuick3DColorValueType::alpha(qreal value)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK8Qt3DCore5Quick22QQuick3DColorValueType5alphaEd', value,
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  @overload()
  @overload(float)
  def lighter(self, factor: float = 1.5) -> QVariant:
    """
    Calls Qt's 'QVariant
    Qt3DCore::Quick::QQuick3DColorValueType::lighter(qreal factor) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-quick-qquick3dcolorvaluetype.html#lighter

    Parameters
    ----------

    factor : float
      Passed on as it is. May be left out, as in Qt: it is then 1.5.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant Qt3DCore::Quick::QQuick3DColorValueType::lighter(qreal
    #      factor) const
    address = self.uglySide.call(
        'ritual_ZNK8Qt3DCore5Quick22QQuick3DColorValueType7lighterEd',
        factor,
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  @overload()
  @overload(float)
  def darker(self, factor: float = 2.0) -> QVariant:
    """
    Calls Qt's 'QVariant
    Qt3DCore::Quick::QQuick3DColorValueType::darker(qreal factor) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-quick-qquick3dcolorvaluetype.html#darker

    Parameters
    ----------

    factor : float
      Passed on as it is. May be left out, as in Qt: it is then 2.0.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant Qt3DCore::Quick::QQuick3DColorValueType::darker(qreal factor)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK8Qt3DCore5Quick22QQuick3DColorValueType6darkerEd', factor,
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  @overload(QVariant)
  def tint(self, factor: QVariant) -> QVariant:
    """
    Calls Qt's 'QVariant
    Qt3DCore::Quick::QQuick3DColorValueType::tint(QVariant factor) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-quick-qquick3dcolorvaluetype.html#tint

    Parameters
    ----------

    factor : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant Qt3DCore::Quick::QQuick3DColorValueType::tint(QVariant
    #      factor) const
    address = self.uglySide.call(
        'ritual_ZNK8Qt3DCore5Quick22QQuick3DColorValueType4tintE8QVariant',
        self._valueOf(factor),
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  def r(self) -> float:
    """
    Calls Qt's 'qreal Qt3DCore::Quick::QQuick3DColorValueType::r() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-quick-qquick3dcolorvaluetype.html#r
    """
    #  qreal Qt3DCore::Quick::QQuick3DColorValueType::r() const
    return self.uglySide.call(
        'ritual_ZNK8Qt3DCore5Quick22QQuick3DColorValueType1rEv',
    )

  def g(self) -> float:
    """
    Calls Qt's 'qreal Qt3DCore::Quick::QQuick3DColorValueType::g() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-quick-qquick3dcolorvaluetype.html#g
    """
    #  qreal Qt3DCore::Quick::QQuick3DColorValueType::g() const
    return self.uglySide.call(
        'ritual_ZNK8Qt3DCore5Quick22QQuick3DColorValueType1gEv',
    )

  def b(self) -> float:
    """
    Calls Qt's 'qreal Qt3DCore::Quick::QQuick3DColorValueType::b() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-quick-qquick3dcolorvaluetype.html#b
    """
    #  qreal Qt3DCore::Quick::QQuick3DColorValueType::b() const
    return self.uglySide.call(
        'ritual_ZNK8Qt3DCore5Quick22QQuick3DColorValueType1bEv',
    )

  def a(self) -> float:
    """
    Calls Qt's 'qreal Qt3DCore::Quick::QQuick3DColorValueType::a() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-quick-qquick3dcolorvaluetype.html#a
    """
    #  qreal Qt3DCore::Quick::QQuick3DColorValueType::a() const
    return self.uglySide.call(
        'ritual_ZNK8Qt3DCore5Quick22QQuick3DColorValueType1aEv',
    )

  def hsvHue(self) -> float:
    """
    Calls Qt's 'qreal Qt3DCore::Quick::QQuick3DColorValueType::hsvHue()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-quick-qquick3dcolorvaluetype.html#hsvHue
    """
    #  qreal Qt3DCore::Quick::QQuick3DColorValueType::hsvHue() const
    return self.uglySide.call(
        'ritual_ZNK8Qt3DCore5Quick22QQuick3DColorValueType6hsvHueEv',
    )

  def hsvSaturation(self) -> float:
    """
    Calls Qt's 'qreal
    Qt3DCore::Quick::QQuick3DColorValueType::hsvSaturation() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-quick-qquick3dcolorvaluetype.html
    """
    #  qreal Qt3DCore::Quick::QQuick3DColorValueType::hsvSaturation() const
    return self.uglySide.call(
        'ritual_ZNK8Qt3DCore5Quick22QQuick3DColorValueType13hsvSaturationEv',
    )

  def hsvValue(self) -> float:
    """
    Calls Qt's 'qreal Qt3DCore::Quick::QQuick3DColorValueType::hsvValue()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-quick-qquick3dcolorvaluetype.html
    """
    #  qreal Qt3DCore::Quick::QQuick3DColorValueType::hsvValue() const
    return self.uglySide.call(
        'ritual_ZNK8Qt3DCore5Quick22QQuick3DColorValueType8hsvValueEv',
    )

  def hslHue(self) -> float:
    """
    Calls Qt's 'qreal Qt3DCore::Quick::QQuick3DColorValueType::hslHue()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-quick-qquick3dcolorvaluetype.html#hslHue
    """
    #  qreal Qt3DCore::Quick::QQuick3DColorValueType::hslHue() const
    return self.uglySide.call(
        'ritual_ZNK8Qt3DCore5Quick22QQuick3DColorValueType6hslHueEv',
    )

  def hslSaturation(self) -> float:
    """
    Calls Qt's 'qreal
    Qt3DCore::Quick::QQuick3DColorValueType::hslSaturation() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-quick-qquick3dcolorvaluetype.html
    """
    #  qreal Qt3DCore::Quick::QQuick3DColorValueType::hslSaturation() const
    return self.uglySide.call(
        'ritual_ZNK8Qt3DCore5Quick22QQuick3DColorValueType13hslSaturationEv',
    )

  def hslLightness(self) -> float:
    """
    Calls Qt's 'qreal Qt3DCore::Quick::QQuick3DColorValueType::hslLightness()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-quick-qquick3dcolorvaluetype.html
    """
    #  qreal Qt3DCore::Quick::QQuick3DColorValueType::hslLightness() const
    return self.uglySide.call(
        'ritual_ZNK8Qt3DCore5Quick22QQuick3DColorValueType12hslLightnessEv',
    )

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool Qt3DCore::Quick::QQuick3DColorValueType::isValid()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-quick-qquick3dcolorvaluetype.html#isValid
    """
    #  bool Qt3DCore::Quick::QQuick3DColorValueType::isValid() const
    return self.uglySide.call(
        'ritual_ZNK8Qt3DCore5Quick22QQuick3DColorValueType7isValidEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float)
  def setR(self, a0: float) -> None:
    """
    Calls Qt's 'void Qt3DCore::Quick::QQuick3DColorValueType::setR(qreal
    a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-quick-qquick3dcolorvaluetype.html#setR

    Parameters
    ----------

    a0 : float
      Passed on as it is.
    """
    #  void Qt3DCore::Quick::QQuick3DColorValueType::setR(qreal a0)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore5Quick22QQuick3DColorValueType4setREd', a0,
    )

  @overload(float)
  def setG(self, a0: float) -> None:
    """
    Calls Qt's 'void Qt3DCore::Quick::QQuick3DColorValueType::setG(qreal
    a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-quick-qquick3dcolorvaluetype.html#setG

    Parameters
    ----------

    a0 : float
      Passed on as it is.
    """
    #  void Qt3DCore::Quick::QQuick3DColorValueType::setG(qreal a0)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore5Quick22QQuick3DColorValueType4setGEd', a0,
    )

  @overload(float)
  def setB(self, a0: float) -> None:
    """
    Calls Qt's 'void Qt3DCore::Quick::QQuick3DColorValueType::setB(qreal
    a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-quick-qquick3dcolorvaluetype.html#setB

    Parameters
    ----------

    a0 : float
      Passed on as it is.
    """
    #  void Qt3DCore::Quick::QQuick3DColorValueType::setB(qreal a0)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore5Quick22QQuick3DColorValueType4setBEd', a0,
    )

  @overload(float)
  def setA(self, a0: float) -> None:
    """
    Calls Qt's 'void Qt3DCore::Quick::QQuick3DColorValueType::setA(qreal
    a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-quick-qquick3dcolorvaluetype.html#setA

    Parameters
    ----------

    a0 : float
      Passed on as it is.
    """
    #  void Qt3DCore::Quick::QQuick3DColorValueType::setA(qreal a0)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore5Quick22QQuick3DColorValueType4setAEd', a0,
    )

  @overload(float)
  def setHsvHue(self, a0: float) -> None:
    """
    Calls Qt's 'void Qt3DCore::Quick::QQuick3DColorValueType::setHsvHue(qreal
    a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-quick-qquick3dcolorvaluetype.html

    Parameters
    ----------

    a0 : float
      Passed on as it is.
    """
    #  void Qt3DCore::Quick::QQuick3DColorValueType::setHsvHue(qreal a0)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore5Quick22QQuick3DColorValueType9setHsvHueEd', a0,
    )

  @overload(float)
  def setHsvSaturation(self, a0: float) -> None:
    """
    Calls Qt's 'void
    Qt3DCore::Quick::QQuick3DColorValueType::setHsvSaturation(qreal a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-quick-qquick3dcolorvaluetype.html

    Parameters
    ----------

    a0 : float
      Passed on as it is.
    """
    #  void Qt3DCore::Quick::QQuick3DColorValueType::setHsvSaturation(qreal
    #      a0)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore5Quick22QQuick3DColorValueType16setHsvSaturation'
        'Ed',
        a0,
    )

  @overload(float)
  def setHsvValue(self, a0: float) -> None:
    """
    Calls Qt's 'void
    Qt3DCore::Quick::QQuick3DColorValueType::setHsvValue(qreal a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-quick-qquick3dcolorvaluetype.html

    Parameters
    ----------

    a0 : float
      Passed on as it is.
    """
    #  void Qt3DCore::Quick::QQuick3DColorValueType::setHsvValue(qreal a0)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore5Quick22QQuick3DColorValueType11setHsvValueEd',
        a0,
    )

  @overload(float)
  def setHslHue(self, a0: float) -> None:
    """
    Calls Qt's 'void Qt3DCore::Quick::QQuick3DColorValueType::setHslHue(qreal
    a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-quick-qquick3dcolorvaluetype.html

    Parameters
    ----------

    a0 : float
      Passed on as it is.
    """
    #  void Qt3DCore::Quick::QQuick3DColorValueType::setHslHue(qreal a0)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore5Quick22QQuick3DColorValueType9setHslHueEd', a0,
    )

  @overload(float)
  def setHslSaturation(self, a0: float) -> None:
    """
    Calls Qt's 'void
    Qt3DCore::Quick::QQuick3DColorValueType::setHslSaturation(qreal a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-quick-qquick3dcolorvaluetype.html

    Parameters
    ----------

    a0 : float
      Passed on as it is.
    """
    #  void Qt3DCore::Quick::QQuick3DColorValueType::setHslSaturation(qreal
    #      a0)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore5Quick22QQuick3DColorValueType16setHslSaturation'
        'Ed',
        a0,
    )

  @overload(float)
  def setHslLightness(self, a0: float) -> None:
    """
    Calls Qt's 'void
    Qt3DCore::Quick::QQuick3DColorValueType::setHslLightness(qreal a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-quick-qquick3dcolorvaluetype.html

    Parameters
    ----------

    a0 : float
      Passed on as it is.
    """
    #  void Qt3DCore::Quick::QQuick3DColorValueType::setHslLightness(qreal
    #      a0)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore5Quick22QQuick3DColorValueType15setHslLightnessE'
        'd',
        a0,
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
