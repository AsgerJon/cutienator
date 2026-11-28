"""
QQuick3DParticle binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3DParticles/6.12.0/QtQuick3DParticles/private/qquick3dparticle_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuick3DParticle to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtQuick3D import QQuick3DObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from ..QtGui import QColor, QVector3D, QVector4D
  from ..QtQuick3DRuntimeRender import QSSGRenderGraphObject
  from . import QQuick3DParticleEmitter, QQuick3DParticleSystem
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QColor = WAIT['QColor']
  QQuick3DParticleEmitter = WAIT['QQuick3DParticleEmitter']
  QQuick3DParticleSystem = WAIT['QQuick3DParticleSystem']
  QSSGRenderGraphObject = WAIT['QSSGRenderGraphObject']
  QVector3D = WAIT['QVector3D']
  QVector4D = WAIT['QVector4D']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuick3DParticle(QQuick3DObject):
  """
  The cute side of Qt's QQuick3DParticle: a plain Python object standing in
  front of one C++ QQuick3DParticle.

  It is built on the cute 'QQuick3DObject', as Qt's QQuick3DParticle is built
  on Qt's QQuick3DObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuick3DParticle that has a ritual and that Python
  can call so far, 52 names in all: 'metaObject', 'tr', 'system',
  'maxAmount', 'color', 'colorVariation', 'unifiedColorVariation',
  'fadeInEffect', 'fadeOutEffect', 'fadeInDuration', 'fadeOutDuration',
  'alignMode', 'alignTargetPosition', 'hasTransparency', 'sortMode',
  'opacity', 'resetColor', 'setSystem', 'setMaxAmount', 'setColor',
  'setColorVariation', 'setUnifiedColorVariation', 'setFadeInEffect',
  'setFadeOutEffect', 'setFadeInDuration', 'setFadeOutDuration',
  'setAlignMode', 'setAlignTargetPosition', 'setHasTransparency',
  'setSortMode', 'systemChanged', 'maxAmountChanged', 'colorChanged',
  'colorVariationChanged', 'unifiedColorVariationChanged',
  'fadeInEffectChanged', 'fadeOutEffectChanged', 'fadeInDurationChanged',
  'fadeOutDurationChanged', 'alignModeChanged', 'alignTargetPositionChanged',
  'hasTransparencyChanged', 'sortModeChanged', 'componentComplete', 'reset',
  'doSetMaxAmount', 'updateNodeLayers', 'updateBurstIndex',
  'nextCurrentIndex', 'updateSpatialNode', 'setDepthBias', 'depthBias'. It
  can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuick3DParticle::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QQuick3DParticle::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'void QQuick3DParticle::qt_qmlMarker_uncreatable()': one of Qt's own
    inner workings.
  - Qt's 'QQuick3DParticle::~QQuick3DParticle()': the destructor: Python
    never removes a C++ QQuick3DParticle.
  - Qt's 'QQuick3DParticle::QQuick3DParticle(QQuick3DObjectPrivate &dd,
    QQuick3DNode *parent)': takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  2 of the 60 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuick3DParticle is created at the first use, not by
    'QQuick3DParticle(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuick3DParticle.
  - Qt tells when it has removed the C++ QQuick3DParticle. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  #  The enums Qt writes inside QQuick3DParticle, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class AlignMode(CuteNum):
    """
    The enum 'QQuick3DParticle::AlignMode' of Qt, with the 3 names Qt gives
    in it.
    """

    AlignNone = Kee[int](0)
    AlignTowardsTarget = Kee[int](1)
    AlignTowardsStartVelocity = Kee[int](2)

  class FadeType(CuteNum):
    """
    The enum 'QQuick3DParticle::FadeType' of Qt, with the 3 names Qt gives in
    it.
    """

    FadeNone = Kee[int](0)
    FadeOpacity = Kee[int](1)
    FadeScale = Kee[int](2)

  class SortMode(CuteNum):
    """
    The enum 'QQuick3DParticle::SortMode' of Qt, with the 4 names Qt gives in
    it.
    """

    SortNone = Kee[int](0)
    SortNewest = Kee[int](1)
    SortOldest = Kee[int](2)
    SortDistance = Kee[int](3)

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
    Calls Qt's 'QString QQuick3DParticle::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dparticle.html#tr

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
    #  QString QQuick3DParticle::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN16QQuick3DParticle2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuick3DParticle'

  #  A C++ QQuick3DParticle Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuick3DParticle'

  #  The functions Qt calls itself that QQuick3DParticle is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'reset': (
          ('_ZN16QQuick3DParticle5resetEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'doSetMaxAmount': (
          ('_ZN16QQuick3DParticle14doSetMaxAmountEi',
           ('nothing', 'nothing', ''),
           (
               ('int', 'number', ''),
           )),
      ),
      'updateNodeLayers': (
          ('_ZN16QQuick3DParticle16updateNodeLayersEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'nextCurrentIndex': (
          ('_ZN16QQuick3DParticle16nextCurrentIndexEPK23QQuick3DParticleEmi'
           'tter',
           ('int', 'number', ''),
           (
               ('address', 'address',
                'QtQuick3DParticles:QQuick3DParticleEmitter'),
           )),
      ),
      'setDepthBias': (
          ('_ZN16QQuick3DParticle12setDepthBiasEf',
           ('nothing', 'nothing', ''),
           (
               ('float', 'number', ''),
           )),
      ),
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuick3DParticle::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dparticle.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuick3DParticle::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK16QQuick3DParticle10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def system(self) -> Optional[QQuick3DParticleSystem]:
    """
    Calls Qt's 'QQuick3DParticleSystem *QQuick3DParticle::system() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dparticle.html#system

    Returns
    -------

    Optional[QQuick3DParticleSystem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuick3DParticleSystem *QQuick3DParticle::system() const
    address = self.uglySide.call('ritual_ZNK16QQuick3DParticle6systemEv')
    from . import QQuick3DParticleSystem
    return QQuick3DParticleSystem._cuteAt(address)

  def maxAmount(self) -> int:
    """
    Calls Qt's 'int QQuick3DParticle::maxAmount() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dparticle.html#maxAmount
    """
    #  int QQuick3DParticle::maxAmount() const
    return self.uglySide.call('ritual_ZNK16QQuick3DParticle9maxAmountEv')

  def color(self) -> QColor:
    """
    Calls Qt's 'QColor QQuick3DParticle::color() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dparticle.html#color

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QQuick3DParticle::color() const
    address = self.uglySide.call('ritual_ZNK16QQuick3DParticle5colorEv')
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def colorVariation(self) -> QVector4D:
    """
    Calls Qt's 'QVector4D QQuick3DParticle::colorVariation() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticle.html#colorVariation

    Returns
    -------

    QVector4D
      A new cute QVector4D around the copy Qt gave back. Python owns it.
    """
    #  QVector4D QQuick3DParticle::colorVariation() const
    address = self.uglySide.call(
        'ritual_ZNK16QQuick3DParticle14colorVariationEv',
    )
    from ..QtGui import QVector4D
    return QVector4D._cuteOwning(address)

  def unifiedColorVariation(self) -> bool:
    """
    Calls Qt's 'bool QQuick3DParticle::unifiedColorVariation() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticle.html#unifiedColorVariation
    """
    #  bool QQuick3DParticle::unifiedColorVariation() const
    return self.uglySide.call(
        'ritual_ZNK16QQuick3DParticle21unifiedColorVariationEv',
    )

  def fadeInEffect(self) -> FadeType:
    """
    Calls Qt's 'FadeType QQuick3DParticle::fadeInEffect() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dparticle.html#fadeInEffect

    Returns
    -------

    FadeType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'FadeType(number)' gives.
    """
    #  FadeType QQuick3DParticle::fadeInEffect() const
    return QQuick3DParticle.FadeType(self.uglySide.call(
        'ritual_ZNK16QQuick3DParticle12fadeInEffectEv',
    ))

  def fadeOutEffect(self) -> FadeType:
    """
    Calls Qt's 'FadeType QQuick3DParticle::fadeOutEffect() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticle.html#fadeOutEffect

    Returns
    -------

    FadeType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'FadeType(number)' gives.
    """
    #  FadeType QQuick3DParticle::fadeOutEffect() const
    return QQuick3DParticle.FadeType(self.uglySide.call(
        'ritual_ZNK16QQuick3DParticle13fadeOutEffectEv',
    ))

  def fadeInDuration(self) -> int:
    """
    Calls Qt's 'int QQuick3DParticle::fadeInDuration() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticle.html#fadeInDuration
    """
    #  int QQuick3DParticle::fadeInDuration() const
    return self.uglySide.call(
        'ritual_ZNK16QQuick3DParticle14fadeInDurationEv',
    )

  def fadeOutDuration(self) -> int:
    """
    Calls Qt's 'int QQuick3DParticle::fadeOutDuration() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticle.html#fadeOutDuration
    """
    #  int QQuick3DParticle::fadeOutDuration() const
    return self.uglySide.call(
        'ritual_ZNK16QQuick3DParticle15fadeOutDurationEv',
    )

  def alignMode(self) -> AlignMode:
    """
    Calls Qt's 'AlignMode QQuick3DParticle::alignMode() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dparticle.html#alignMode

    Returns
    -------

    AlignMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'AlignMode(number)' gives.
    """
    #  AlignMode QQuick3DParticle::alignMode() const
    return QQuick3DParticle.AlignMode(self.uglySide.call(
        'ritual_ZNK16QQuick3DParticle9alignModeEv',
    ))

  def alignTargetPosition(self) -> QVector3D:
    """
    Calls Qt's 'QVector3D QQuick3DParticle::alignTargetPosition() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticle.html#alignTargetPosition

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  QVector3D QQuick3DParticle::alignTargetPosition() const
    address = self.uglySide.call(
        'ritual_ZNK16QQuick3DParticle19alignTargetPositionEv',
    )
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  def hasTransparency(self) -> bool:
    """
    Calls Qt's 'bool QQuick3DParticle::hasTransparency() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticle.html#hasTransparency
    """
    #  bool QQuick3DParticle::hasTransparency() const
    return self.uglySide.call(
        'ritual_ZNK16QQuick3DParticle15hasTransparencyEv',
    )

  def sortMode(self) -> SortMode:
    """
    Calls Qt's 'SortMode QQuick3DParticle::sortMode() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dparticle.html#sortMode

    Returns
    -------

    SortMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'SortMode(number)' gives.
    """
    #  SortMode QQuick3DParticle::sortMode() const
    return QQuick3DParticle.SortMode(self.uglySide.call(
        'ritual_ZNK16QQuick3DParticle8sortModeEv',
    ))

  def opacity(self) -> float:
    """
    Calls Qt's 'float QQuick3DParticle::opacity() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dparticle.html#opacity
    """
    #  float QQuick3DParticle::opacity() const
    return self.uglySide.call('ritual_ZNK16QQuick3DParticle7opacityEv')

  def depthBias(self) -> float:
    """
    Calls Qt's 'float QQuick3DParticle::depthBias() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dparticle.html#depthBias
    """
    #  float QQuick3DParticle::depthBias() const
    return self.uglySide.call('ritual_ZNK16QQuick3DParticle9depthBiasEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QQuick3DParticleSystem)
  @overload(NoneType)
  def setSystem(self, system: Optional[QQuick3DParticleSystem]) -> None:
    """
    Calls Qt's 'void QQuick3DParticle::setSystem(QQuick3DParticleSystem
    *system)'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dparticle.html#setSystem

    Parameters
    ----------

    system : Optional[QQuick3DParticleSystem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuick3DParticle::setSystem(QQuick3DParticleSystem *system)
    self.uglySide.call(
        'ritual_ZN16QQuick3DParticle9setSystemEP22QQuick3DParticleSystem',
        self._addressOf(system),
    )

  @overload(int)
  def setMaxAmount(self, maxAmount: int) -> None:
    """
    Calls Qt's 'void QQuick3DParticle::setMaxAmount(int maxAmount)'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dparticle.html#setMaxAmount

    Parameters
    ----------

    maxAmount : int
      Passed on as it is.
    """
    #  void QQuick3DParticle::setMaxAmount(int maxAmount)
    self.uglySide.call(
        'ritual_ZN16QQuick3DParticle12setMaxAmountEi', maxAmount,
    )

  @overload(QColor)
  def setColor(self, color: QColor) -> None:
    """
    Calls Qt's 'void QQuick3DParticle::setColor(QColor color)'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dparticle.html#setColor

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QQuick3DParticle::setColor(QColor color)
    self.uglySide.call(
        'ritual_ZN16QQuick3DParticle8setColorE6QColor', self._valueOf(color),
    )

  @overload(QVector4D)
  def setColorVariation(self, colorVariation: QVector4D) -> None:
    """
    Calls Qt's 'void QQuick3DParticle::setColorVariation(QVector4D
    colorVariation)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticle.html#setColorVariation

    Parameters
    ----------

    colorVariation : QVector4D
      Passed on as a value: Qt reads the C++ QVector4D, which stays Python's
      own.
    """
    #  void QQuick3DParticle::setColorVariation(QVector4D colorVariation)
    self.uglySide.call(
        'ritual_ZN16QQuick3DParticle17setColorVariationE9QVector4D',
        self._valueOf(colorVariation),
    )

  @overload(bool)
  def setUnifiedColorVariation(self, unified: bool) -> None:
    """
    Calls Qt's 'void QQuick3DParticle::setUnifiedColorVariation(bool
    unified)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticle.html#setUnifiedColorVariation

    Parameters
    ----------

    unified : bool
      Passed on as it is.
    """
    #  void QQuick3DParticle::setUnifiedColorVariation(bool unified)
    self.uglySide.call(
        'ritual_ZN16QQuick3DParticle24setUnifiedColorVariationEb', unified,
    )

  @overload(FadeType)
  def setFadeInEffect(self, fadeInEffect: FadeType) -> None:
    """
    Calls Qt's 'void
    QQuick3DParticle::setFadeInEffect(QQuick3DParticle::FadeType
    fadeInEffect)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticle.html#setFadeInEffect

    Parameters
    ----------

    fadeInEffect : FadeType
      Passed on as its number.
    """
    #  void QQuick3DParticle::setFadeInEffect(QQuick3DParticle::FadeType
    #      fadeInEffect)
    self.uglySide.call(
        'ritual_ZN16QQuick3DParticle15setFadeInEffectENS_8FadeTypeE',
        fadeInEffect.value,
    )

  @overload(FadeType)
  def setFadeOutEffect(self, fadeOutEffect: FadeType) -> None:
    """
    Calls Qt's 'void
    QQuick3DParticle::setFadeOutEffect(QQuick3DParticle::FadeType
    fadeOutEffect)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticle.html#setFadeOutEffect

    Parameters
    ----------

    fadeOutEffect : FadeType
      Passed on as its number.
    """
    #  void QQuick3DParticle::setFadeOutEffect(QQuick3DParticle::FadeType
    #      fadeOutEffect)
    self.uglySide.call(
        'ritual_ZN16QQuick3DParticle16setFadeOutEffectENS_8FadeTypeE',
        fadeOutEffect.value,
    )

  @overload(int)
  def setFadeInDuration(self, fadeInDuration: int) -> None:
    """
    Calls Qt's 'void QQuick3DParticle::setFadeInDuration(int
    fadeInDuration)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticle.html#setFadeInDuration

    Parameters
    ----------

    fadeInDuration : int
      Passed on as it is.
    """
    #  void QQuick3DParticle::setFadeInDuration(int fadeInDuration)
    self.uglySide.call(
        'ritual_ZN16QQuick3DParticle17setFadeInDurationEi', fadeInDuration,
    )

  @overload(int)
  def setFadeOutDuration(self, fadeOutDuration: int) -> None:
    """
    Calls Qt's 'void QQuick3DParticle::setFadeOutDuration(int
    fadeOutDuration)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticle.html#setFadeOutDuration

    Parameters
    ----------

    fadeOutDuration : int
      Passed on as it is.
    """
    #  void QQuick3DParticle::setFadeOutDuration(int fadeOutDuration)
    self.uglySide.call(
        'ritual_ZN16QQuick3DParticle18setFadeOutDurationEi', fadeOutDuration,
    )

  @overload(AlignMode)
  def setAlignMode(self, alignMode: AlignMode) -> None:
    """
    Calls Qt's 'void
    QQuick3DParticle::setAlignMode(QQuick3DParticle::AlignMode alignMode)'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dparticle.html#setAlignMode

    Parameters
    ----------

    alignMode : AlignMode
      Passed on as its number.
    """
    #  void QQuick3DParticle::setAlignMode(QQuick3DParticle::AlignMode
    #      alignMode)
    self.uglySide.call(
        'ritual_ZN16QQuick3DParticle12setAlignModeENS_9AlignModeE',
        alignMode.value,
    )

  @overload(QVector3D)
  def setAlignTargetPosition(self, alignPosition: QVector3D) -> None:
    """
    Calls Qt's 'void QQuick3DParticle::setAlignTargetPosition(const QVector3D
    &alignPosition)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticle.html#setAlignTargetPosition

    Parameters
    ----------

    alignPosition : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.
    """
    #  void QQuick3DParticle::setAlignTargetPosition(const QVector3D
    #      &alignPosition)
    self.uglySide.call(
        'ritual_ZN16QQuick3DParticle22setAlignTargetPositionERK9QVector3D',
        self._valueOf(alignPosition),
    )

  @overload(bool)
  def setHasTransparency(self, transparency: bool) -> None:
    """
    Calls Qt's 'void QQuick3DParticle::setHasTransparency(bool
    transparency)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticle.html#setHasTransparency

    Parameters
    ----------

    transparency : bool
      Passed on as it is.
    """
    #  void QQuick3DParticle::setHasTransparency(bool transparency)
    self.uglySide.call(
        'ritual_ZN16QQuick3DParticle18setHasTransparencyEb', transparency,
    )

  @overload(SortMode)
  def setSortMode(self, sortMode: SortMode) -> None:
    """
    Calls Qt's 'void QQuick3DParticle::setSortMode(QQuick3DParticle::SortMode
    sortMode)'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dparticle.html#setSortMode

    Parameters
    ----------

    sortMode : SortMode
      Passed on as its number.
    """
    #  void QQuick3DParticle::setSortMode(QQuick3DParticle::SortMode
    #      sortMode)
    self.uglySide.call(
        'ritual_ZN16QQuick3DParticle11setSortModeENS_8SortModeE',
        sortMode.value,
    )

  @overload(float)
  def setDepthBias(self, bias: float) -> None:
    """
    Calls Qt's 'void QQuick3DParticle::setDepthBias(float bias)'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dparticle.html#setDepthBias

    Parameters
    ----------

    bias : float
      Passed on as it is.
    """
    #  void QQuick3DParticle::setDepthBias(float bias)
    ritual = 'ritual_ZN16QQuick3DParticle12setDepthBiasEf'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN16QQuick3DParticle12setDepthBiasEf'
    self.uglySide.call(ritual, bias)

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
  @overload(QQuick3DObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QQuick3DObject] = None) -> None:
    """
    Notes what was given, for Qt's
    'QQuick3DParticle::QQuick3DParticle(QQuick3DObject *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticle.html#QQuick3DParticle

    Parameters
    ----------

    parent : Optional[QQuick3DObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuick3DParticle::QQuick3DParticle(QQuick3DObject *parent)
    self._noteCreation(QQuick3DParticle, lambda: Rituals.call(
        'ritual_ZN16QQuick3DParticleC1EP14QQuick3DObject',
        self._addressOf(parent),
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

  def resetColor(self) -> None:
    """
    Calls Qt's 'void QQuick3DParticle::resetColor()'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dparticle.html#resetColor
    """
    #  void QQuick3DParticle::resetColor()
    self.uglySide.call('ritual_ZN16QQuick3DParticle10resetColorEv')

  def systemChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DParticle::systemChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticle.html#systemChanged
    """
    #  void QQuick3DParticle::systemChanged()
    self.uglySide.call('ritual_ZN16QQuick3DParticle13systemChangedEv')

  def maxAmountChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DParticle::maxAmountChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticle.html#maxAmountChanged
    """
    #  void QQuick3DParticle::maxAmountChanged()
    self.uglySide.call('ritual_ZN16QQuick3DParticle16maxAmountChangedEv')

  def colorChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DParticle::colorChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dparticle.html#colorChanged
    """
    #  void QQuick3DParticle::colorChanged()
    self.uglySide.call('ritual_ZN16QQuick3DParticle12colorChangedEv')

  def colorVariationChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DParticle::colorVariationChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticle.html#colorVariationChanged
    """
    #  void QQuick3DParticle::colorVariationChanged()
    self.uglySide.call(
        'ritual_ZN16QQuick3DParticle21colorVariationChangedEv',
    )

  def unifiedColorVariationChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DParticle::unifiedColorVariationChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticle.html#unifiedColorVariationChanged
    """
    #  void QQuick3DParticle::unifiedColorVariationChanged()
    self.uglySide.call(
        'ritual_ZN16QQuick3DParticle28unifiedColorVariationChangedEv',
    )

  def fadeInEffectChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DParticle::fadeInEffectChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticle.html#fadeInEffectChanged
    """
    #  void QQuick3DParticle::fadeInEffectChanged()
    self.uglySide.call('ritual_ZN16QQuick3DParticle19fadeInEffectChangedEv')

  def fadeOutEffectChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DParticle::fadeOutEffectChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticle.html#fadeOutEffectChanged
    """
    #  void QQuick3DParticle::fadeOutEffectChanged()
    self.uglySide.call('ritual_ZN16QQuick3DParticle20fadeOutEffectChangedEv')

  def fadeInDurationChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DParticle::fadeInDurationChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticle.html#fadeInDurationChanged
    """
    #  void QQuick3DParticle::fadeInDurationChanged()
    self.uglySide.call(
        'ritual_ZN16QQuick3DParticle21fadeInDurationChangedEv',
    )

  def fadeOutDurationChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DParticle::fadeOutDurationChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticle.html#fadeOutDurationChanged
    """
    #  void QQuick3DParticle::fadeOutDurationChanged()
    self.uglySide.call(
        'ritual_ZN16QQuick3DParticle22fadeOutDurationChangedEv',
    )

  def alignModeChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DParticle::alignModeChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticle.html#alignModeChanged
    """
    #  void QQuick3DParticle::alignModeChanged()
    self.uglySide.call('ritual_ZN16QQuick3DParticle16alignModeChangedEv')

  def alignTargetPositionChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DParticle::alignTargetPositionChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticle.html#alignTargetPositionChanged
    """
    #  void QQuick3DParticle::alignTargetPositionChanged()
    self.uglySide.call(
        'ritual_ZN16QQuick3DParticle26alignTargetPositionChangedEv',
    )

  def hasTransparencyChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DParticle::hasTransparencyChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticle.html#hasTransparencyChanged
    """
    #  void QQuick3DParticle::hasTransparencyChanged()
    self.uglySide.call(
        'ritual_ZN16QQuick3DParticle22hasTransparencyChangedEv',
    )

  def sortModeChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DParticle::sortModeChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticle.html#sortModeChanged
    """
    #  void QQuick3DParticle::sortModeChanged()
    self.uglySide.call('ritual_ZN16QQuick3DParticle15sortModeChangedEv')

  def componentComplete(self) -> None:
    """
    Calls Qt's 'void QQuick3DParticle::componentComplete()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticle.html#componentComplete
    """
    #  void QQuick3DParticle::componentComplete()
    ritual = 'ritual_ZN16QQuick3DParticle17componentCompleteEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN16QQuick3DParticle17componentCompleteEv'
    self.uglySide.call(ritual)

  def reset(self) -> None:
    """
    Calls Qt's 'void QQuick3DParticle::reset()'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dparticle.html#reset
    """
    #  void QQuick3DParticle::reset()
    ritual = 'ritual_ZN16QQuick3DParticle5resetEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN16QQuick3DParticle5resetEv'
    self.uglySide.call(ritual)

  @overload(int)
  def doSetMaxAmount(self, amount: int) -> None:
    """
    Calls Qt's 'void QQuick3DParticle::doSetMaxAmount(int amount)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticle.html#doSetMaxAmount

    Parameters
    ----------

    amount : int
      Passed on as it is.
    """
    #  void QQuick3DParticle::doSetMaxAmount(int amount)
    ritual = 'ritual_ZN16QQuick3DParticle14doSetMaxAmountEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN16QQuick3DParticle14doSetMaxAmountEi'
    self.uglySide.call(ritual, amount)

  def updateNodeLayers(self) -> None:
    """
    Calls Qt's 'void QQuick3DParticle::updateNodeLayers()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticle.html#updateNodeLayers
    """
    #  void QQuick3DParticle::updateNodeLayers()
    ritual = 'ritual_ZN16QQuick3DParticle16updateNodeLayersEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN16QQuick3DParticle16updateNodeLayersEv'
    self.uglySide.call(ritual)

  @overload(int)
  def updateBurstIndex(self, amount: int) -> None:
    """
    Calls Qt's 'void QQuick3DParticle::updateBurstIndex(int amount)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticle.html#updateBurstIndex

    Parameters
    ----------

    amount : int
      Passed on as it is.
    """
    #  void QQuick3DParticle::updateBurstIndex(int amount)
    self.uglySide.call(
        'ritual_ZN16QQuick3DParticle16updateBurstIndexEi', amount,
    )

  @overload(QQuick3DParticleEmitter)
  @overload(NoneType)
  def nextCurrentIndex(
      self,
      emitter: Optional[QQuick3DParticleEmitter],
  ) -> int:
    """
    Calls Qt's 'int QQuick3DParticle::nextCurrentIndex(const
    QQuick3DParticleEmitter *emitter)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticle.html#nextCurrentIndex

    Parameters
    ----------

    emitter : Optional[QQuick3DParticleEmitter]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  int QQuick3DParticle::nextCurrentIndex(const QQuick3DParticleEmitter
    #      *emitter)
    ritual = (
        'ritual_ZN16QQuick3DParticle16nextCurrentIndexEPK23QQuick3DParticle'
        'Emitter')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN16QQuick3DParticle16nextCurrentIndexEPK23QQuick3DPa'
          'rticleEmitter')
    return self.uglySide.call(ritual, self._addressOf(emitter))

  @overload(QSSGRenderGraphObject)
  @overload(NoneType)
  def updateSpatialNode(
      self,
      node: Optional[QSSGRenderGraphObject],
  ) -> Optional[QSSGRenderGraphObject]:
    """
    Calls Qt's 'QSSGRenderGraphObject
    *QQuick3DParticle::updateSpatialNode(QSSGRenderGraphObject *node)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticle.html#updateSpatialNode

    Parameters
    ----------

    node : Optional[QSSGRenderGraphObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QSSGRenderGraphObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSSGRenderGraphObject
    #      *QQuick3DParticle::updateSpatialNode(QSSGRenderGraphObject *node)
    ritual = (
        'ritual_ZN16QQuick3DParticle17updateSpatialNodeEP21QSSGRenderGraphO'
        'bject')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN16QQuick3DParticle17updateSpatialNodeEP21QSSGRender'
          'GraphObject')
    address = self.uglySide.call(ritual, self._addressOf(node))
    from ..QtQuick3DRuntimeRender import QSSGRenderGraphObject
    return QSSGRenderGraphObject._cuteAt(address)
