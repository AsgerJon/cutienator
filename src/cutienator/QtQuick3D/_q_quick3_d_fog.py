"""
QQuick3DFog binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3D/6.12.0/QtQuick3D/private/qquick3dfog_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QQuick3DFog to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from ..QtGui import QColor
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QColor = WAIT['QColor']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuick3DFog(QObject):
  """
  The cute side of Qt's QQuick3DFog: a plain Python object standing in front
  of one C++ QQuick3DFog.

  It is built on the cute 'QObject', as Qt's QQuick3DFog is built on Qt's
  QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuick3DFog that has a ritual and that Python can
  call so far, 42 names in all: 'metaObject', 'tr', 'isEnabled', 'color',
  'density', 'isDepthEnabled', 'depthNear', 'depthFar', 'depthCurve',
  'isHeightEnabled', 'leastIntenseY', 'mostIntenseY', 'heightCurve',
  'isTransmitEnabled', 'transmitCurve', 'setEnabled', 'setColor',
  'setDensity', 'setDepthEnabled', 'setDepthNear', 'setDepthFar',
  'setDepthCurve', 'setHeightEnabled', 'setLeastIntenseY', 'setMostIntenseY',
  'setHeightCurve', 'setTransmitEnabled', 'setTransmitCurve', 'changed',
  'enabledChanged', 'colorChanged', 'densityChanged', 'depthEnabledChanged',
  'depthNearChanged', 'depthFarChanged', 'depthCurveChanged',
  'heightEnabledChanged', 'leastIntenseYChanged', 'mostIntenseYChanged',
  'heightCurveChanged', 'transmitEnabledChanged', 'transmitCurveChanged'.
  None can be made from Python: one comes out of a function of another class
  that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuick3DFog::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QQuick3DFog::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.

  What has no ritual
  ------------------

  2 of the 46 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuick3DFog is created at the first use, not by
    'QQuick3DFog(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuick3DFog.
  - Qt tells when it has removed the C++ QQuick3DFog. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(str)
  @overload(NoneType)
  @overload(str, str)
  @overload(str, NoneType)
  @overload(NoneType, str)
  @overload(NoneType, NoneType)
  @overload(str, str, int)
  @overload(str, NoneType, int)
  @overload(NoneType, str, int)
  @overload(NoneType, NoneType, int)
  def tr(s: Optional[str], c: Optional[str] = None, n: int = -1) -> str:
    """
    Calls Qt's 'QString QQuick3DFog::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dfog.html#tr

    Parameters
    ----------

    s : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    c : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text. May
      be left out, as in Qt: it is then None.

    n : int
      Passed on as it is. May be left out, as in Qt: it is then -1.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuick3DFog::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN11QQuick3DFog2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuick3DFog'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuick3DFog::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dfog.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuick3DFog::metaObject() const
    address = self.uglySide.call('ritual_ZNK11QQuick3DFog10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def isEnabled(self) -> bool:
    """
    Calls Qt's 'bool QQuick3DFog::isEnabled() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dfog.html#isEnabled
    """
    #  bool QQuick3DFog::isEnabled() const
    return self.uglySide.call('ritual_ZNK11QQuick3DFog9isEnabledEv')

  def color(self) -> QColor:
    """
    Calls Qt's 'QColor QQuick3DFog::color() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dfog.html#color

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QQuick3DFog::color() const
    address = self.uglySide.call('ritual_ZNK11QQuick3DFog5colorEv')
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def density(self) -> float:
    """
    Calls Qt's 'float QQuick3DFog::density() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dfog.html#density
    """
    #  float QQuick3DFog::density() const
    return self.uglySide.call('ritual_ZNK11QQuick3DFog7densityEv')

  def isDepthEnabled(self) -> bool:
    """
    Calls Qt's 'bool QQuick3DFog::isDepthEnabled() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dfog.html#isDepthEnabled
    """
    #  bool QQuick3DFog::isDepthEnabled() const
    return self.uglySide.call('ritual_ZNK11QQuick3DFog14isDepthEnabledEv')

  def depthNear(self) -> float:
    """
    Calls Qt's 'float QQuick3DFog::depthNear() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dfog.html#depthNear
    """
    #  float QQuick3DFog::depthNear() const
    return self.uglySide.call('ritual_ZNK11QQuick3DFog9depthNearEv')

  def depthFar(self) -> float:
    """
    Calls Qt's 'float QQuick3DFog::depthFar() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dfog.html#depthFar
    """
    #  float QQuick3DFog::depthFar() const
    return self.uglySide.call('ritual_ZNK11QQuick3DFog8depthFarEv')

  def depthCurve(self) -> float:
    """
    Calls Qt's 'float QQuick3DFog::depthCurve() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dfog.html#depthCurve
    """
    #  float QQuick3DFog::depthCurve() const
    return self.uglySide.call('ritual_ZNK11QQuick3DFog10depthCurveEv')

  def isHeightEnabled(self) -> bool:
    """
    Calls Qt's 'bool QQuick3DFog::isHeightEnabled() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dfog.html#isHeightEnabled
    """
    #  bool QQuick3DFog::isHeightEnabled() const
    return self.uglySide.call('ritual_ZNK11QQuick3DFog15isHeightEnabledEv')

  def leastIntenseY(self) -> float:
    """
    Calls Qt's 'float QQuick3DFog::leastIntenseY() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dfog.html#leastIntenseY
    """
    #  float QQuick3DFog::leastIntenseY() const
    return self.uglySide.call('ritual_ZNK11QQuick3DFog13leastIntenseYEv')

  def mostIntenseY(self) -> float:
    """
    Calls Qt's 'float QQuick3DFog::mostIntenseY() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dfog.html#mostIntenseY
    """
    #  float QQuick3DFog::mostIntenseY() const
    return self.uglySide.call('ritual_ZNK11QQuick3DFog12mostIntenseYEv')

  def heightCurve(self) -> float:
    """
    Calls Qt's 'float QQuick3DFog::heightCurve() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dfog.html#heightCurve
    """
    #  float QQuick3DFog::heightCurve() const
    return self.uglySide.call('ritual_ZNK11QQuick3DFog11heightCurveEv')

  def isTransmitEnabled(self) -> bool:
    """
    Calls Qt's 'bool QQuick3DFog::isTransmitEnabled() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dfog.html#isTransmitEnabled
    """
    #  bool QQuick3DFog::isTransmitEnabled() const
    return self.uglySide.call('ritual_ZNK11QQuick3DFog17isTransmitEnabledEv')

  def transmitCurve(self) -> float:
    """
    Calls Qt's 'float QQuick3DFog::transmitCurve() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dfog.html#transmitCurve
    """
    #  float QQuick3DFog::transmitCurve() const
    return self.uglySide.call('ritual_ZNK11QQuick3DFog13transmitCurveEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  def setEnabled(self, newEnabled: bool) -> None:
    """
    Calls Qt's 'void QQuick3DFog::setEnabled(bool newEnabled)'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dfog.html#setEnabled

    Parameters
    ----------

    newEnabled : bool
      Passed on as it is.
    """
    #  void QQuick3DFog::setEnabled(bool newEnabled)
    self.uglySide.call('ritual_ZN11QQuick3DFog10setEnabledEb', newEnabled)

  @overload(QColor)
  def setColor(self, newColor: QColor) -> None:
    """
    Calls Qt's 'void QQuick3DFog::setColor(const QColor &newColor)'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dfog.html#setColor

    Parameters
    ----------

    newColor : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QQuick3DFog::setColor(const QColor &newColor)
    self.uglySide.call(
        'ritual_ZN11QQuick3DFog8setColorERK6QColor', self._valueOf(newColor),
    )

  @overload(float)
  def setDensity(self, newDensity: float) -> None:
    """
    Calls Qt's 'void QQuick3DFog::setDensity(float newDensity)'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dfog.html#setDensity

    Parameters
    ----------

    newDensity : float
      Passed on as it is.
    """
    #  void QQuick3DFog::setDensity(float newDensity)
    self.uglySide.call('ritual_ZN11QQuick3DFog10setDensityEf', newDensity)

  @overload(bool)
  def setDepthEnabled(self, newDepthEnabled: bool) -> None:
    """
    Calls Qt's 'void QQuick3DFog::setDepthEnabled(bool newDepthEnabled)'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dfog.html#setDepthEnabled

    Parameters
    ----------

    newDepthEnabled : bool
      Passed on as it is.
    """
    #  void QQuick3DFog::setDepthEnabled(bool newDepthEnabled)
    self.uglySide.call(
        'ritual_ZN11QQuick3DFog15setDepthEnabledEb', newDepthEnabled,
    )

  @overload(float)
  def setDepthNear(self, newDepthNear: float) -> None:
    """
    Calls Qt's 'void QQuick3DFog::setDepthNear(float newDepthNear)'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dfog.html#setDepthNear

    Parameters
    ----------

    newDepthNear : float
      Passed on as it is.
    """
    #  void QQuick3DFog::setDepthNear(float newDepthNear)
    self.uglySide.call(
        'ritual_ZN11QQuick3DFog12setDepthNearEf', newDepthNear,
    )

  @overload(float)
  def setDepthFar(self, newDepthFar: float) -> None:
    """
    Calls Qt's 'void QQuick3DFog::setDepthFar(float newDepthFar)'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dfog.html#setDepthFar

    Parameters
    ----------

    newDepthFar : float
      Passed on as it is.
    """
    #  void QQuick3DFog::setDepthFar(float newDepthFar)
    self.uglySide.call('ritual_ZN11QQuick3DFog11setDepthFarEf', newDepthFar)

  @overload(float)
  def setDepthCurve(self, newDepthCurve: float) -> None:
    """
    Calls Qt's 'void QQuick3DFog::setDepthCurve(float newDepthCurve)'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dfog.html#setDepthCurve

    Parameters
    ----------

    newDepthCurve : float
      Passed on as it is.
    """
    #  void QQuick3DFog::setDepthCurve(float newDepthCurve)
    self.uglySide.call(
        'ritual_ZN11QQuick3DFog13setDepthCurveEf', newDepthCurve,
    )

  @overload(bool)
  def setHeightEnabled(self, newHeightEnabled: bool) -> None:
    """
    Calls Qt's 'void QQuick3DFog::setHeightEnabled(bool newHeightEnabled)'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dfog.html#setHeightEnabled

    Parameters
    ----------

    newHeightEnabled : bool
      Passed on as it is.
    """
    #  void QQuick3DFog::setHeightEnabled(bool newHeightEnabled)
    self.uglySide.call(
        'ritual_ZN11QQuick3DFog16setHeightEnabledEb', newHeightEnabled,
    )

  @overload(float)
  def setLeastIntenseY(self, newleastIntenseY: float) -> None:
    """
    Calls Qt's 'void QQuick3DFog::setLeastIntenseY(float newleastIntenseY)'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dfog.html#setLeastIntenseY

    Parameters
    ----------

    newleastIntenseY : float
      Passed on as it is.
    """
    #  void QQuick3DFog::setLeastIntenseY(float newleastIntenseY)
    self.uglySide.call(
        'ritual_ZN11QQuick3DFog16setLeastIntenseYEf', newleastIntenseY,
    )

  @overload(float)
  def setMostIntenseY(self, newmostIntenseY: float) -> None:
    """
    Calls Qt's 'void QQuick3DFog::setMostIntenseY(float newmostIntenseY)'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dfog.html#setMostIntenseY

    Parameters
    ----------

    newmostIntenseY : float
      Passed on as it is.
    """
    #  void QQuick3DFog::setMostIntenseY(float newmostIntenseY)
    self.uglySide.call(
        'ritual_ZN11QQuick3DFog15setMostIntenseYEf', newmostIntenseY,
    )

  @overload(float)
  def setHeightCurve(self, newHeightCurve: float) -> None:
    """
    Calls Qt's 'void QQuick3DFog::setHeightCurve(float newHeightCurve)'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dfog.html#setHeightCurve

    Parameters
    ----------

    newHeightCurve : float
      Passed on as it is.
    """
    #  void QQuick3DFog::setHeightCurve(float newHeightCurve)
    self.uglySide.call(
        'ritual_ZN11QQuick3DFog14setHeightCurveEf', newHeightCurve,
    )

  @overload(bool)
  def setTransmitEnabled(self, newTransmitEnabled: bool) -> None:
    """
    Calls Qt's 'void QQuick3DFog::setTransmitEnabled(bool
    newTransmitEnabled)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dfog.html#setTransmitEnabled

    Parameters
    ----------

    newTransmitEnabled : bool
      Passed on as it is.
    """
    #  void QQuick3DFog::setTransmitEnabled(bool newTransmitEnabled)
    self.uglySide.call(
        'ritual_ZN11QQuick3DFog18setTransmitEnabledEb', newTransmitEnabled,
    )

  @overload(float)
  def setTransmitCurve(self, newTransmitCurve: float) -> None:
    """
    Calls Qt's 'void QQuick3DFog::setTransmitCurve(float newTransmitCurve)'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dfog.html#setTransmitCurve

    Parameters
    ----------

    newTransmitCurve : float
      Passed on as it is.
    """
    #  void QQuick3DFog::setTransmitCurve(float newTransmitCurve)
    self.uglySide.call(
        'ritual_ZN11QQuick3DFog16setTransmitCurveEf', newTransmitCurve,
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

  def changed(self) -> None:
    """
    Calls Qt's 'void QQuick3DFog::changed()'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dfog.html#changed
    """
    #  void QQuick3DFog::changed()
    self.uglySide.call('ritual_ZN11QQuick3DFog7changedEv')

  def enabledChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DFog::enabledChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dfog.html#enabledChanged
    """
    #  void QQuick3DFog::enabledChanged()
    self.uglySide.call('ritual_ZN11QQuick3DFog14enabledChangedEv')

  def colorChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DFog::colorChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dfog.html#colorChanged
    """
    #  void QQuick3DFog::colorChanged()
    self.uglySide.call('ritual_ZN11QQuick3DFog12colorChangedEv')

  def densityChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DFog::densityChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dfog.html#densityChanged
    """
    #  void QQuick3DFog::densityChanged()
    self.uglySide.call('ritual_ZN11QQuick3DFog14densityChangedEv')

  def depthEnabledChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DFog::depthEnabledChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dfog.html#depthEnabledChanged
    """
    #  void QQuick3DFog::depthEnabledChanged()
    self.uglySide.call('ritual_ZN11QQuick3DFog19depthEnabledChangedEv')

  def depthNearChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DFog::depthNearChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dfog.html#depthNearChanged
    """
    #  void QQuick3DFog::depthNearChanged()
    self.uglySide.call('ritual_ZN11QQuick3DFog16depthNearChangedEv')

  def depthFarChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DFog::depthFarChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dfog.html#depthFarChanged
    """
    #  void QQuick3DFog::depthFarChanged()
    self.uglySide.call('ritual_ZN11QQuick3DFog15depthFarChangedEv')

  def depthCurveChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DFog::depthCurveChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dfog.html#depthCurveChanged
    """
    #  void QQuick3DFog::depthCurveChanged()
    self.uglySide.call('ritual_ZN11QQuick3DFog17depthCurveChangedEv')

  def heightEnabledChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DFog::heightEnabledChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dfog.html#heightEnabledChanged
    """
    #  void QQuick3DFog::heightEnabledChanged()
    self.uglySide.call('ritual_ZN11QQuick3DFog20heightEnabledChangedEv')

  def leastIntenseYChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DFog::leastIntenseYChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dfog.html#leastIntenseYChanged
    """
    #  void QQuick3DFog::leastIntenseYChanged()
    self.uglySide.call('ritual_ZN11QQuick3DFog20leastIntenseYChangedEv')

  def mostIntenseYChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DFog::mostIntenseYChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dfog.html#mostIntenseYChanged
    """
    #  void QQuick3DFog::mostIntenseYChanged()
    self.uglySide.call('ritual_ZN11QQuick3DFog19mostIntenseYChangedEv')

  def heightCurveChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DFog::heightCurveChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dfog.html#heightCurveChanged
    """
    #  void QQuick3DFog::heightCurveChanged()
    self.uglySide.call('ritual_ZN11QQuick3DFog18heightCurveChangedEv')

  def transmitEnabledChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DFog::transmitEnabledChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dfog.html#transmitEnabledChanged
    """
    #  void QQuick3DFog::transmitEnabledChanged()
    self.uglySide.call('ritual_ZN11QQuick3DFog22transmitEnabledChangedEv')

  def transmitCurveChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DFog::transmitCurveChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dfog.html#transmitCurveChanged
    """
    #  void QQuick3DFog::transmitCurveChanged()
    self.uglySide.call('ritual_ZN11QQuick3DFog20transmitCurveChangedEv')
