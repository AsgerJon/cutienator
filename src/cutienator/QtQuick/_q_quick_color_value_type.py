"""
QQuickColorValueType binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquickvaluetypes_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QQuickColorValueType to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtGui import QColor

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from ..QtCore import QVariant
  from ..QtQml import QJSValue
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QJSValue = WAIT['QJSValue']


class QQuickColorValueType(QColor):
  """
  The cute side of Qt's QQuickColorValueType: a plain Python object standing
  in front of one C++ QQuickColorValueType.

  It is built on the cute 'QColor', as Qt's QQuickColorValueType is built on
  Qt's QColor, and has everything that class has.

  C++ hands a QQuickColorValueType around as a copy, so every C++
  QQuickColorValueType behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QQuickColorValueType that has a ritual and that
  Python can call so far, 28 names in all: 'create', 'toString', 'alpha',
  'lighter', 'darker', 'tint', 'r', 'g', 'b', 'a', 'hsvHue', 'hsvSaturation',
  'hsvValue', 'hslHue', 'hslSaturation', 'hslLightness', 'isValid', 'rgba',
  'setR', 'setG', 'setB', 'setA', 'setHsvHue', 'setHsvSaturation',
  'setHsvValue', 'setHslHue', 'setHslSaturation', 'setHslLightness'. It can
  be made from Python, in 3 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void QQuickColorValueType::qt_qmlMarker_foreign()': one of Qt's own
    inner workings.
  - Qt's 'void QQuickColorValueType::qt_qmlMarker_extended()': one of Qt's
    own inner workings.
  - Qt's 'QQuickColorValueType::~QQuickColorValueType()': the destructor:
    Python removes its C++ QQuickColorValueType by it, and has no other use
    for it.

  What has no ritual
  ------------------

  3 of the 37 functions Qt declares: 3 not a gap.

  What to expect
  --------------

  - The C++ QQuickColorValueType is created at the first use, not by
    'QQuickColorValueType(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QQuickColorValueType back gives a copy the ritual
    made for Python, in a new cute QQuickColorValueType.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QJSValue)
  def create(params: QJSValue) -> QVariant:
    """
    Calls Qt's 'QVariant QQuickColorValueType::create(const QJSValue
    &params)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcolorvaluetype.html#create

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
    #  QVariant QQuickColorValueType::create(const QJSValue &params)
    address = Rituals.call(
        'ritual_ZN20QQuickColorValueType6createERK8QJSValue',
        CuteMixin._valueOf(params),
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickColorValueType'

  #  Qt's '~QQuickColorValueType()'. Naming it makes this a value class:
  #  Python owns every C++ QQuickColorValueType behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN20QQuickColorValueTypeD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def toString(self) -> str:
    """
    Calls Qt's 'QString QQuickColorValueType::toString() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcolorvaluetype.html#toString

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuickColorValueType::toString() const
    return self.uglySide.call('ritual_ZNK20QQuickColorValueType8toStringEv')

  @overload(float)
  def alpha(self, value: float) -> QColor:
    """
    Calls Qt's 'QColor QQuickColorValueType::alpha(qreal value) const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcolorvaluetype.html#alpha

    Parameters
    ----------

    value : float
      Passed on as it is.

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QQuickColorValueType::alpha(qreal value) const
    address = self.uglySide.call(
        'ritual_ZNK20QQuickColorValueType5alphaEd', value,
    )
    return QColor._cuteOwning(address)

  @overload()
  @overload(float)
  def lighter(self, factor: float = 1.5) -> QColor:
    """
    Calls Qt's 'QColor QQuickColorValueType::lighter(qreal factor) const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcolorvaluetype.html#lighter

    Parameters
    ----------

    factor : float
      Passed on as it is. May be left out, as in Qt: it is then 1.5.

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QQuickColorValueType::lighter(qreal factor) const
    address = self.uglySide.call(
        'ritual_ZNK20QQuickColorValueType7lighterEd', factor,
    )
    return QColor._cuteOwning(address)

  @overload()
  @overload(float)
  def darker(self, factor: float = 2.0) -> QColor:
    """
    Calls Qt's 'QColor QQuickColorValueType::darker(qreal factor) const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcolorvaluetype.html#darker

    Parameters
    ----------

    factor : float
      Passed on as it is. May be left out, as in Qt: it is then 2.0.

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QQuickColorValueType::darker(qreal factor) const
    address = self.uglySide.call(
        'ritual_ZNK20QQuickColorValueType6darkerEd', factor,
    )
    return QColor._cuteOwning(address)

  @overload(QColor)
  def tint(self, tintColor: QColor) -> QColor:
    """
    Calls Qt's 'QColor QQuickColorValueType::tint(const QColor &tintColor)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcolorvaluetype.html#tint

    Parameters
    ----------

    tintColor : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QQuickColorValueType::tint(const QColor &tintColor) const
    address = self.uglySide.call(
        'ritual_ZNK20QQuickColorValueType4tintERK6QColor',
        self._valueOf(tintColor),
    )
    return QColor._cuteOwning(address)

  def r(self) -> float:
    """
    Calls Qt's 'qreal QQuickColorValueType::r() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcolorvaluetype.html#r
    """
    #  qreal QQuickColorValueType::r() const
    return self.uglySide.call('ritual_ZNK20QQuickColorValueType1rEv')

  def g(self) -> float:
    """
    Calls Qt's 'qreal QQuickColorValueType::g() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcolorvaluetype.html#g
    """
    #  qreal QQuickColorValueType::g() const
    return self.uglySide.call('ritual_ZNK20QQuickColorValueType1gEv')

  def b(self) -> float:
    """
    Calls Qt's 'qreal QQuickColorValueType::b() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcolorvaluetype.html#b
    """
    #  qreal QQuickColorValueType::b() const
    return self.uglySide.call('ritual_ZNK20QQuickColorValueType1bEv')

  def a(self) -> float:
    """
    Calls Qt's 'qreal QQuickColorValueType::a() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcolorvaluetype.html#a
    """
    #  qreal QQuickColorValueType::a() const
    return self.uglySide.call('ritual_ZNK20QQuickColorValueType1aEv')

  def hsvHue(self) -> float:
    """
    Calls Qt's 'qreal QQuickColorValueType::hsvHue() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcolorvaluetype.html#hsvHue
    """
    #  qreal QQuickColorValueType::hsvHue() const
    return self.uglySide.call('ritual_ZNK20QQuickColorValueType6hsvHueEv')

  def hsvSaturation(self) -> float:
    """
    Calls Qt's 'qreal QQuickColorValueType::hsvSaturation() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcolorvaluetype.html#hsvSaturation
    """
    #  qreal QQuickColorValueType::hsvSaturation() const
    return self.uglySide.call(
        'ritual_ZNK20QQuickColorValueType13hsvSaturationEv',
    )

  def hsvValue(self) -> float:
    """
    Calls Qt's 'qreal QQuickColorValueType::hsvValue() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcolorvaluetype.html#hsvValue
    """
    #  qreal QQuickColorValueType::hsvValue() const
    return self.uglySide.call('ritual_ZNK20QQuickColorValueType8hsvValueEv')

  def hslHue(self) -> float:
    """
    Calls Qt's 'qreal QQuickColorValueType::hslHue() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcolorvaluetype.html#hslHue
    """
    #  qreal QQuickColorValueType::hslHue() const
    return self.uglySide.call('ritual_ZNK20QQuickColorValueType6hslHueEv')

  def hslSaturation(self) -> float:
    """
    Calls Qt's 'qreal QQuickColorValueType::hslSaturation() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcolorvaluetype.html#hslSaturation
    """
    #  qreal QQuickColorValueType::hslSaturation() const
    return self.uglySide.call(
        'ritual_ZNK20QQuickColorValueType13hslSaturationEv',
    )

  def hslLightness(self) -> float:
    """
    Calls Qt's 'qreal QQuickColorValueType::hslLightness() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcolorvaluetype.html#hslLightness
    """
    #  qreal QQuickColorValueType::hslLightness() const
    return self.uglySide.call(
        'ritual_ZNK20QQuickColorValueType12hslLightnessEv',
    )

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool QQuickColorValueType::isValid() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcolorvaluetype.html#isValid
    """
    #  bool QQuickColorValueType::isValid() const
    return self.uglySide.call('ritual_ZNK20QQuickColorValueType7isValidEv')

  def rgba(self) -> int:
    """
    Calls Qt's 'int QQuickColorValueType::rgba() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcolorvaluetype.html#rgba
    """
    #  int QQuickColorValueType::rgba() const
    return self.uglySide.call('ritual_ZNK20QQuickColorValueType4rgbaEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float)
  def setR(self, a0: float) -> None:
    """
    Calls Qt's 'void QQuickColorValueType::setR(qreal a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcolorvaluetype.html#setR

    Parameters
    ----------

    a0 : float
      Passed on as it is.
    """
    #  void QQuickColorValueType::setR(qreal a0)
    self.uglySide.call('ritual_ZN20QQuickColorValueType4setREd', a0)

  @overload(float)
  def setG(self, a0: float) -> None:
    """
    Calls Qt's 'void QQuickColorValueType::setG(qreal a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcolorvaluetype.html#setG

    Parameters
    ----------

    a0 : float
      Passed on as it is.
    """
    #  void QQuickColorValueType::setG(qreal a0)
    self.uglySide.call('ritual_ZN20QQuickColorValueType4setGEd', a0)

  @overload(float)
  def setB(self, a0: float) -> None:
    """
    Calls Qt's 'void QQuickColorValueType::setB(qreal a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcolorvaluetype.html#setB

    Parameters
    ----------

    a0 : float
      Passed on as it is.
    """
    #  void QQuickColorValueType::setB(qreal a0)
    self.uglySide.call('ritual_ZN20QQuickColorValueType4setBEd', a0)

  @overload(float)
  def setA(self, a0: float) -> None:
    """
    Calls Qt's 'void QQuickColorValueType::setA(qreal a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcolorvaluetype.html#setA

    Parameters
    ----------

    a0 : float
      Passed on as it is.
    """
    #  void QQuickColorValueType::setA(qreal a0)
    self.uglySide.call('ritual_ZN20QQuickColorValueType4setAEd', a0)

  @overload(float)
  def setHsvHue(self, a0: float) -> None:
    """
    Calls Qt's 'void QQuickColorValueType::setHsvHue(qreal a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcolorvaluetype.html#setHsvHue

    Parameters
    ----------

    a0 : float
      Passed on as it is.
    """
    #  void QQuickColorValueType::setHsvHue(qreal a0)
    self.uglySide.call('ritual_ZN20QQuickColorValueType9setHsvHueEd', a0)

  @overload(float)
  def setHsvSaturation(self, a0: float) -> None:
    """
    Calls Qt's 'void QQuickColorValueType::setHsvSaturation(qreal a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcolorvaluetype.html#setHsvSaturation

    Parameters
    ----------

    a0 : float
      Passed on as it is.
    """
    #  void QQuickColorValueType::setHsvSaturation(qreal a0)
    self.uglySide.call(
        'ritual_ZN20QQuickColorValueType16setHsvSaturationEd', a0,
    )

  @overload(float)
  def setHsvValue(self, a0: float) -> None:
    """
    Calls Qt's 'void QQuickColorValueType::setHsvValue(qreal a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcolorvaluetype.html#setHsvValue

    Parameters
    ----------

    a0 : float
      Passed on as it is.
    """
    #  void QQuickColorValueType::setHsvValue(qreal a0)
    self.uglySide.call('ritual_ZN20QQuickColorValueType11setHsvValueEd', a0)

  @overload(float)
  def setHslHue(self, a0: float) -> None:
    """
    Calls Qt's 'void QQuickColorValueType::setHslHue(qreal a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcolorvaluetype.html#setHslHue

    Parameters
    ----------

    a0 : float
      Passed on as it is.
    """
    #  void QQuickColorValueType::setHslHue(qreal a0)
    self.uglySide.call('ritual_ZN20QQuickColorValueType9setHslHueEd', a0)

  @overload(float)
  def setHslSaturation(self, a0: float) -> None:
    """
    Calls Qt's 'void QQuickColorValueType::setHslSaturation(qreal a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcolorvaluetype.html#setHslSaturation

    Parameters
    ----------

    a0 : float
      Passed on as it is.
    """
    #  void QQuickColorValueType::setHslSaturation(qreal a0)
    self.uglySide.call(
        'ritual_ZN20QQuickColorValueType16setHslSaturationEd', a0,
    )

  @overload(float)
  def setHslLightness(self, a0: float) -> None:
    """
    Calls Qt's 'void QQuickColorValueType::setHslLightness(qreal a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcolorvaluetype.html#setHslLightness

    Parameters
    ----------

    a0 : float
      Passed on as it is.
    """
    #  void QQuickColorValueType::setHslLightness(qreal a0)
    self.uglySide.call(
        'ritual_ZN20QQuickColorValueType15setHslLightnessEd', a0,
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
    'QQuickColorValueType::QQuickColorValueType()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcolorvaluetype.html#QQuickColorValueType
    """
    #  QQuickColorValueType::QQuickColorValueType()
    self._noteCreation(QQuickColorValueType, lambda: Rituals.call(
        'ritual_ZN20QQuickColorValueTypeC1Ev',
    ))

  @overload(QColor)
  def __init__(self, color: QColor) -> None:
    """
    Notes what was given, for Qt's
    'QQuickColorValueType::QQuickColorValueType(const QColor &color)', which
    is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcolorvaluetype.html#QQuickColorValueType

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  QQuickColorValueType::QQuickColorValueType(const QColor &color)
    self._noteCreation(QQuickColorValueType, lambda: Rituals.call(
        'ritual_ZN20QQuickColorValueTypeC1ERK6QColor', self._valueOf(color),
    ))

  @overload(str)
  def __init__(self, string: str) -> None:
    """
    Notes what was given, for Qt's
    'QQuickColorValueType::QQuickColorValueType(const QString &string)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcolorvaluetype.html#QQuickColorValueType

    Parameters
    ----------

    string : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  QQuickColorValueType::QQuickColorValueType(const QString &string)
    self._noteCreation(QQuickColorValueType, lambda: Rituals.call(
        'ritual_ZN20QQuickColorValueTypeC1ERK7QString', string,
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
