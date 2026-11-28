"""
QQuick3DLightmapper binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3D/6.12.0/QtQuick3D/private/qquick3dlightmapper_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QQuick3DLightmapper to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QUrl
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QUrl = WAIT['QUrl']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuick3DLightmapper(QObject):
  """
  The cute side of Qt's QQuick3DLightmapper: a plain Python object standing
  in front of one C++ QQuick3DLightmapper.

  It is built on the cute 'QObject', as Qt's QQuick3DLightmapper is built on
  Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuick3DLightmapper that has a ritual and that
  Python can call so far, 36 names in all: 'metaObject', 'tr',
  'opacityThreshold', 'bias', 'isAdaptiveBiasEnabled',
  'isIndirectLightEnabled', 'samples', 'indirectLightWorkgroupSize',
  'bounces', 'indirectLightFactor', 'source', 'denoiseSigma',
  'texelsPerUnit', 'setOpacityThreshold', 'setBias',
  'setAdaptiveBiasEnabled', 'setIndirectLightEnabled', 'setSamples',
  'setIndirectLightWorkgroupSize', 'setBounces', 'setIndirectLightFactor',
  'setSource', 'setDenoiseSigma', 'setTexelsPerUnit', 'changed',
  'opacityThresholdChanged', 'biasChanged', 'adaptiveBiasEnabledChanged',
  'indirectLightEnabledChanged', 'samplesChanged',
  'indirectLightWorkgroupSizeChanged', 'bouncesChanged',
  'indirectLightFactorChanged', 'sourceChanged', 'denoiseSigmaChanged',
  'texelsPerUnitChanged'. None can be made from Python: one comes out of a
  function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuick3DLightmapper::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QQuick3DLightmapper::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.

  What has no ritual
  ------------------

  2 of the 40 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuick3DLightmapper is created at the first use, not by
    'QQuick3DLightmapper(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuick3DLightmapper.
  - Qt tells when it has removed the C++ QQuick3DLightmapper. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
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
    Calls Qt's 'QString QQuick3DLightmapper::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dlightmapper.html#tr

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
    #  QString QQuick3DLightmapper::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN19QQuick3DLightmapper2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuick3DLightmapper'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuick3DLightmapper::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dlightmapper.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuick3DLightmapper::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK19QQuick3DLightmapper10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def opacityThreshold(self) -> float:
    """
    Calls Qt's 'float QQuick3DLightmapper::opacityThreshold() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dlightmapper.html#opacityThreshold
    """
    #  float QQuick3DLightmapper::opacityThreshold() const
    return self.uglySide.call(
        'ritual_ZNK19QQuick3DLightmapper16opacityThresholdEv',
    )

  def bias(self) -> float:
    """
    Calls Qt's 'float QQuick3DLightmapper::bias() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dlightmapper.html#bias
    """
    #  float QQuick3DLightmapper::bias() const
    return self.uglySide.call('ritual_ZNK19QQuick3DLightmapper4biasEv')

  def isAdaptiveBiasEnabled(self) -> bool:
    """
    Calls Qt's 'bool QQuick3DLightmapper::isAdaptiveBiasEnabled() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dlightmapper.html#isAdaptiveBiasEnabled
    """
    #  bool QQuick3DLightmapper::isAdaptiveBiasEnabled() const
    return self.uglySide.call(
        'ritual_ZNK19QQuick3DLightmapper21isAdaptiveBiasEnabledEv',
    )

  def isIndirectLightEnabled(self) -> bool:
    """
    Calls Qt's 'bool QQuick3DLightmapper::isIndirectLightEnabled() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dlightmapper.html#isIndirectLightEnabled
    """
    #  bool QQuick3DLightmapper::isIndirectLightEnabled() const
    return self.uglySide.call(
        'ritual_ZNK19QQuick3DLightmapper22isIndirectLightEnabledEv',
    )

  def samples(self) -> int:
    """
    Calls Qt's 'int QQuick3DLightmapper::samples() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dlightmapper.html#samples
    """
    #  int QQuick3DLightmapper::samples() const
    return self.uglySide.call('ritual_ZNK19QQuick3DLightmapper7samplesEv')

  def indirectLightWorkgroupSize(self) -> int:
    """
    Calls Qt's 'int QQuick3DLightmapper::indirectLightWorkgroupSize() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dlightmapper.html
    """
    #  int QQuick3DLightmapper::indirectLightWorkgroupSize() const
    return self.uglySide.call(
        'ritual_ZNK19QQuick3DLightmapper26indirectLightWorkgroupSizeEv',
    )

  def bounces(self) -> int:
    """
    Calls Qt's 'int QQuick3DLightmapper::bounces() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dlightmapper.html#bounces
    """
    #  int QQuick3DLightmapper::bounces() const
    return self.uglySide.call('ritual_ZNK19QQuick3DLightmapper7bouncesEv')

  def indirectLightFactor(self) -> float:
    """
    Calls Qt's 'float QQuick3DLightmapper::indirectLightFactor() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dlightmapper.html#indirectLightFactor
    """
    #  float QQuick3DLightmapper::indirectLightFactor() const
    return self.uglySide.call(
        'ritual_ZNK19QQuick3DLightmapper19indirectLightFactorEv',
    )

  def source(self) -> QUrl:
    """
    Calls Qt's 'QUrl QQuick3DLightmapper::source() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dlightmapper.html#source

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QQuick3DLightmapper::source() const
    address = self.uglySide.call('ritual_ZNK19QQuick3DLightmapper6sourceEv')
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  def denoiseSigma(self) -> float:
    """
    Calls Qt's 'float QQuick3DLightmapper::denoiseSigma() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dlightmapper.html#denoiseSigma
    """
    #  float QQuick3DLightmapper::denoiseSigma() const
    return self.uglySide.call(
        'ritual_ZNK19QQuick3DLightmapper12denoiseSigmaEv',
    )

  def texelsPerUnit(self) -> float:
    """
    Calls Qt's 'float QQuick3DLightmapper::texelsPerUnit() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dlightmapper.html#texelsPerUnit
    """
    #  float QQuick3DLightmapper::texelsPerUnit() const
    return self.uglySide.call(
        'ritual_ZNK19QQuick3DLightmapper13texelsPerUnitEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float)
  def setOpacityThreshold(self, opacity: float) -> None:
    """
    Calls Qt's 'void QQuick3DLightmapper::setOpacityThreshold(float
    opacity)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dlightmapper.html#setOpacityThreshold

    Parameters
    ----------

    opacity : float
      Passed on as it is.
    """
    #  void QQuick3DLightmapper::setOpacityThreshold(float opacity)
    self.uglySide.call(
        'ritual_ZN19QQuick3DLightmapper19setOpacityThresholdEf', opacity,
    )

  @overload(float)
  def setBias(self, bias: float) -> None:
    """
    Calls Qt's 'void QQuick3DLightmapper::setBias(float bias)'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dlightmapper.html#setBias

    Parameters
    ----------

    bias : float
      Passed on as it is.
    """
    #  void QQuick3DLightmapper::setBias(float bias)
    self.uglySide.call('ritual_ZN19QQuick3DLightmapper7setBiasEf', bias)

  @overload(bool)
  def setAdaptiveBiasEnabled(self, enabled: bool) -> None:
    """
    Calls Qt's 'void QQuick3DLightmapper::setAdaptiveBiasEnabled(bool
    enabled)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dlightmapper.html#setAdaptiveBiasEnabled

    Parameters
    ----------

    enabled : bool
      Passed on as it is.
    """
    #  void QQuick3DLightmapper::setAdaptiveBiasEnabled(bool enabled)
    self.uglySide.call(
        'ritual_ZN19QQuick3DLightmapper22setAdaptiveBiasEnabledEb', enabled,
    )

  @overload(bool)
  def setIndirectLightEnabled(self, enabled: bool) -> None:
    """
    Calls Qt's 'void QQuick3DLightmapper::setIndirectLightEnabled(bool
    enabled)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dlightmapper.html#setIndirectLightEnabled

    Parameters
    ----------

    enabled : bool
      Passed on as it is.
    """
    #  void QQuick3DLightmapper::setIndirectLightEnabled(bool enabled)
    self.uglySide.call(
        'ritual_ZN19QQuick3DLightmapper23setIndirectLightEnabledEb', enabled,
    )

  @overload(int)
  def setSamples(self, count: int) -> None:
    """
    Calls Qt's 'void QQuick3DLightmapper::setSamples(int count)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dlightmapper.html#setSamples

    Parameters
    ----------

    count : int
      Passed on as it is.
    """
    #  void QQuick3DLightmapper::setSamples(int count)
    self.uglySide.call('ritual_ZN19QQuick3DLightmapper10setSamplesEi', count)

  @overload(int)
  def setIndirectLightWorkgroupSize(self, size: int) -> None:
    """
    Calls Qt's 'void QQuick3DLightmapper::setIndirectLightWorkgroupSize(int
    size)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dlightmapper.html

    Parameters
    ----------

    size : int
      Passed on as it is.
    """
    #  void QQuick3DLightmapper::setIndirectLightWorkgroupSize(int size)
    self.uglySide.call(
        'ritual_ZN19QQuick3DLightmapper29setIndirectLightWorkgroupSizeEi',
        size,
    )

  @overload(int)
  def setBounces(self, count: int) -> None:
    """
    Calls Qt's 'void QQuick3DLightmapper::setBounces(int count)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dlightmapper.html#setBounces

    Parameters
    ----------

    count : int
      Passed on as it is.
    """
    #  void QQuick3DLightmapper::setBounces(int count)
    self.uglySide.call('ritual_ZN19QQuick3DLightmapper10setBouncesEi', count)

  @overload(float)
  def setIndirectLightFactor(self, factor: float) -> None:
    """
    Calls Qt's 'void QQuick3DLightmapper::setIndirectLightFactor(float
    factor)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dlightmapper.html#setIndirectLightFactor

    Parameters
    ----------

    factor : float
      Passed on as it is.
    """
    #  void QQuick3DLightmapper::setIndirectLightFactor(float factor)
    self.uglySide.call(
        'ritual_ZN19QQuick3DLightmapper22setIndirectLightFactorEf', factor,
    )

  @overload(QUrl)
  def setSource(self, source: QUrl) -> None:
    """
    Calls Qt's 'void QQuick3DLightmapper::setSource(const QUrl &source)'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dlightmapper.html#setSource

    Parameters
    ----------

    source : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  void QQuick3DLightmapper::setSource(const QUrl &source)
    self.uglySide.call(
        'ritual_ZN19QQuick3DLightmapper9setSourceERK4QUrl',
        self._valueOf(source),
    )

  @overload(float)
  def setDenoiseSigma(self, newDenoiseSigma: float) -> None:
    """
    Calls Qt's 'void QQuick3DLightmapper::setDenoiseSigma(float
    newDenoiseSigma)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dlightmapper.html#setDenoiseSigma

    Parameters
    ----------

    newDenoiseSigma : float
      Passed on as it is.
    """
    #  void QQuick3DLightmapper::setDenoiseSigma(float newDenoiseSigma)
    self.uglySide.call(
        'ritual_ZN19QQuick3DLightmapper15setDenoiseSigmaEf', newDenoiseSigma,
    )

  @overload(float)
  def setTexelsPerUnit(self, newTexelsPerUnit: float) -> None:
    """
    Calls Qt's 'void QQuick3DLightmapper::setTexelsPerUnit(float
    newTexelsPerUnit)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dlightmapper.html#setTexelsPerUnit

    Parameters
    ----------

    newTexelsPerUnit : float
      Passed on as it is.
    """
    #  void QQuick3DLightmapper::setTexelsPerUnit(float newTexelsPerUnit)
    self.uglySide.call(
        'ritual_ZN19QQuick3DLightmapper16setTexelsPerUnitEf',
        newTexelsPerUnit,
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
    Calls Qt's 'void QQuick3DLightmapper::changed()'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dlightmapper.html#changed
    """
    #  void QQuick3DLightmapper::changed()
    self.uglySide.call('ritual_ZN19QQuick3DLightmapper7changedEv')

  def opacityThresholdChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DLightmapper::opacityThresholdChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dlightmapper.html#opacityThresholdChanged
    """
    #  void QQuick3DLightmapper::opacityThresholdChanged()
    self.uglySide.call(
        'ritual_ZN19QQuick3DLightmapper23opacityThresholdChangedEv',
    )

  def biasChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DLightmapper::biasChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dlightmapper.html#biasChanged
    """
    #  void QQuick3DLightmapper::biasChanged()
    self.uglySide.call('ritual_ZN19QQuick3DLightmapper11biasChangedEv')

  def adaptiveBiasEnabledChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DLightmapper::adaptiveBiasEnabledChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dlightmapper.html
    """
    #  void QQuick3DLightmapper::adaptiveBiasEnabledChanged()
    self.uglySide.call(
        'ritual_ZN19QQuick3DLightmapper26adaptiveBiasEnabledChangedEv',
    )

  def indirectLightEnabledChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DLightmapper::indirectLightEnabledChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dlightmapper.html
    """
    #  void QQuick3DLightmapper::indirectLightEnabledChanged()
    self.uglySide.call(
        'ritual_ZN19QQuick3DLightmapper27indirectLightEnabledChangedEv',
    )

  def samplesChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DLightmapper::samplesChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dlightmapper.html#samplesChanged
    """
    #  void QQuick3DLightmapper::samplesChanged()
    self.uglySide.call('ritual_ZN19QQuick3DLightmapper14samplesChangedEv')

  def indirectLightWorkgroupSizeChanged(self) -> None:
    """
    Calls Qt's 'void
    QQuick3DLightmapper::indirectLightWorkgroupSizeChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dlightmapper.html
    """
    #  void QQuick3DLightmapper::indirectLightWorkgroupSizeChanged()
    self.uglySide.call(
        'ritual_ZN19QQuick3DLightmapper33indirectLightWorkgroupSizeChangedE'
        'v',
    )

  def bouncesChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DLightmapper::bouncesChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dlightmapper.html#bouncesChanged
    """
    #  void QQuick3DLightmapper::bouncesChanged()
    self.uglySide.call('ritual_ZN19QQuick3DLightmapper14bouncesChangedEv')

  def indirectLightFactorChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DLightmapper::indirectLightFactorChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dlightmapper.html
    """
    #  void QQuick3DLightmapper::indirectLightFactorChanged()
    self.uglySide.call(
        'ritual_ZN19QQuick3DLightmapper26indirectLightFactorChangedEv',
    )

  def sourceChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DLightmapper::sourceChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dlightmapper.html#sourceChanged
    """
    #  void QQuick3DLightmapper::sourceChanged()
    self.uglySide.call('ritual_ZN19QQuick3DLightmapper13sourceChangedEv')

  def denoiseSigmaChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DLightmapper::denoiseSigmaChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dlightmapper.html#denoiseSigmaChanged
    """
    #  void QQuick3DLightmapper::denoiseSigmaChanged()
    self.uglySide.call(
        'ritual_ZN19QQuick3DLightmapper19denoiseSigmaChangedEv',
    )

  def texelsPerUnitChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DLightmapper::texelsPerUnitChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dlightmapper.html#texelsPerUnitChanged
    """
    #  void QQuick3DLightmapper::texelsPerUnitChanged()
    self.uglySide.call(
        'ritual_ZN19QQuick3DLightmapper20texelsPerUnitChangedEv',
    )
