"""
QQuick3DParticleLineParticle binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3DParticles/6.12.0/QtQuick3DParticles/private/qquick3dparticlelineparticle_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuick3DParticleLineParticle to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from . import QQuick3DParticleSpriteParticle

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
  from ..QtGui import QVector3D, QVector4D
  from ..QtQuick3DRuntimeRender import QSSGRenderGraphObject
  from ..QtQuick3D import QQuick3DNode
  from . import QQuick3DParticleEmitter, QQuick3DParticleSystem
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQuick3DNode = WAIT['QQuick3DNode']
  QQuick3DParticleEmitter = WAIT['QQuick3DParticleEmitter']
  QQuick3DParticleSystem = WAIT['QQuick3DParticleSystem']
  QSSGRenderGraphObject = WAIT['QSSGRenderGraphObject']
  QVector3D = WAIT['QVector3D']
  QVector4D = WAIT['QVector4D']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuick3DParticleLineParticle(QQuick3DParticleSpriteParticle):
  """
  The cute side of Qt's QQuick3DParticleLineParticle: a plain Python object
  standing in front of one C++ QQuick3DParticleLineParticle.

  It is built on the cute 'QQuick3DParticleSpriteParticle', as Qt's
  QQuick3DParticleLineParticle is built on Qt's
  QQuick3DParticleSpriteParticle, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuick3DParticleLineParticle that has a ritual and
  that Python can call so far, 41 names in all: 'metaObject', 'tr',
  'segmentCount', 'alphaFade', 'scaleMultiplier', 'texcoordMultiplier',
  'length', 'lengthVariation', 'lengthDeltaMin', 'eolFadeOutDuration',
  'texcoordMode', 'setSegmentCount', 'setAlphaFade', 'setScaleMultiplier',
  'setTexcoordMultiplier', 'setLength', 'setLengthVariation',
  'setLengthDeltaMin', 'setEolFadeOutDuration', 'setTexcoordMode',
  'segmentCountChanged', 'alphaFadeChanged', 'scaleMultiplierChanged',
  'texcoordMultiplierChanged', 'lengthChanged', 'lengthVariationChanged',
  'lengthDeltaMinChanged', 'eolFadeOutDurationChanged',
  'texcoordModeChanged', 'updateLineNode', 'handleSegmentCountChanged',
  'updateLineSegment', 'clearSegment', 'handleMaxAmountChanged',
  'handleSystemChanged', 'reset', 'commitParticles', 'nextCurrentIndex',
  'saveLineSegment', 'setParticleData', 'resetParticleData'. It can be made
  from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuick3DParticleLineParticle::qt_metacast(const char *a0)':
    one of Qt's own inner workings.
  - Qt's 'int QQuick3DParticleLineParticle::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QQuick3DParticleLineParticle::~QQuick3DParticleLineParticle()': the
    destructor: Python never removes a C++ QQuick3DParticleLineParticle.
  - Qt's 'void
    QQuick3DParticleLineParticle::updateLineBuffer(LineParticleUpdateNode
    *updateNode, QSSGRenderGraphObject *node)': names
    'QQuick3DParticleLineParticle::LineParticleUpdateNode', which has no cute
    class yet.

  What has no ritual
  ------------------

  2 of the 48 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuick3DParticleLineParticle is created at the first use, not by
    'QQuick3DParticleLineParticle(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuick3DParticleLineParticle.
  - Qt tells when it has removed the C++ QQuick3DParticleLineParticle. Every
    call on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQuick3DParticleLineParticle that has no cute function
    yet, 'updateLineBuffer', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QQuick3DParticleLineParticle, each a class in
  #  here as in C++, and the names Qt has for the combinations of its flags
  #  enums.

  class TexcoordMode(CuteNum):
    """
    The enum 'QQuick3DParticleLineParticle::TexcoordMode' of Qt, with the 3
    names Qt gives in it.
    """

    Absolute = Kee[int](0)
    Relative = Kee[int](1)
    Fill = Kee[int](2)

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
    Calls Qt's 'QString QQuick3DParticleLineParticle::tr(const char *s, const
    char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlelineparticle.html#tr

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
    #  QString QQuick3DParticleLineParticle::tr(const char *s, const char *c,
    #      int n)
    return Rituals.call(
        'ritual_ZN28QQuick3DParticleLineParticle2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuick3DParticleLineParticle'

  #  A C++ QQuick3DParticleLineParticle Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuick3DParticleLineParticle'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuick3DParticleLineParticle::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlelineparticle.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuick3DParticleLineParticle::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK28QQuick3DParticleLineParticle10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def segmentCount(self) -> int:
    """
    Calls Qt's 'int QQuick3DParticleLineParticle::segmentCount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlelineparticle.html#segmentCount
    """
    #  int QQuick3DParticleLineParticle::segmentCount() const
    return self.uglySide.call(
        'ritual_ZNK28QQuick3DParticleLineParticle12segmentCountEv',
    )

  def alphaFade(self) -> float:
    """
    Calls Qt's 'float QQuick3DParticleLineParticle::alphaFade() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlelineparticle.html#alphaFade
    """
    #  float QQuick3DParticleLineParticle::alphaFade() const
    return self.uglySide.call(
        'ritual_ZNK28QQuick3DParticleLineParticle9alphaFadeEv',
    )

  def scaleMultiplier(self) -> float:
    """
    Calls Qt's 'float QQuick3DParticleLineParticle::scaleMultiplier() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlelineparticle.html#scaleMultiplier
    """
    #  float QQuick3DParticleLineParticle::scaleMultiplier() const
    return self.uglySide.call(
        'ritual_ZNK28QQuick3DParticleLineParticle15scaleMultiplierEv',
    )

  def texcoordMultiplier(self) -> float:
    """
    Calls Qt's 'float QQuick3DParticleLineParticle::texcoordMultiplier()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlelineparticle.html
    """
    #  float QQuick3DParticleLineParticle::texcoordMultiplier() const
    return self.uglySide.call(
        'ritual_ZNK28QQuick3DParticleLineParticle18texcoordMultiplierEv',
    )

  def length(self) -> float:
    """
    Calls Qt's 'float QQuick3DParticleLineParticle::length() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlelineparticle.html#length
    """
    #  float QQuick3DParticleLineParticle::length() const
    return self.uglySide.call(
        'ritual_ZNK28QQuick3DParticleLineParticle6lengthEv',
    )

  def lengthVariation(self) -> float:
    """
    Calls Qt's 'float QQuick3DParticleLineParticle::lengthVariation() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlelineparticle.html#lengthVariation
    """
    #  float QQuick3DParticleLineParticle::lengthVariation() const
    return self.uglySide.call(
        'ritual_ZNK28QQuick3DParticleLineParticle15lengthVariationEv',
    )

  def lengthDeltaMin(self) -> float:
    """
    Calls Qt's 'float QQuick3DParticleLineParticle::lengthDeltaMin() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlelineparticle.html#lengthDeltaMin
    """
    #  float QQuick3DParticleLineParticle::lengthDeltaMin() const
    return self.uglySide.call(
        'ritual_ZNK28QQuick3DParticleLineParticle14lengthDeltaMinEv',
    )

  def eolFadeOutDuration(self) -> int:
    """
    Calls Qt's 'int QQuick3DParticleLineParticle::eolFadeOutDuration()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlelineparticle.html
    """
    #  int QQuick3DParticleLineParticle::eolFadeOutDuration() const
    return self.uglySide.call(
        'ritual_ZNK28QQuick3DParticleLineParticle18eolFadeOutDurationEv',
    )

  def texcoordMode(self) -> TexcoordMode:
    """
    Calls Qt's 'TexcoordMode QQuick3DParticleLineParticle::texcoordMode()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlelineparticle.html#texcoordMode

    Returns
    -------

    TexcoordMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'TexcoordMode(number)'
      gives.
    """
    #  TexcoordMode QQuick3DParticleLineParticle::texcoordMode() const
    return QQuick3DParticleLineParticle.TexcoordMode(self.uglySide.call(
        'ritual_ZNK28QQuick3DParticleLineParticle12texcoordModeEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setSegmentCount(self, count: int) -> None:
    """
    Calls Qt's 'void QQuick3DParticleLineParticle::setSegmentCount(int
    count)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlelineparticle.html#setSegmentCount

    Parameters
    ----------

    count : int
      Passed on as it is.
    """
    #  void QQuick3DParticleLineParticle::setSegmentCount(int count)
    self.uglySide.call(
        'ritual_ZN28QQuick3DParticleLineParticle15setSegmentCountEi', count,
    )

  @overload(float)
  def setAlphaFade(self, fade: float) -> None:
    """
    Calls Qt's 'void QQuick3DParticleLineParticle::setAlphaFade(float fade)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlelineparticle.html#setAlphaFade

    Parameters
    ----------

    fade : float
      Passed on as it is.
    """
    #  void QQuick3DParticleLineParticle::setAlphaFade(float fade)
    self.uglySide.call(
        'ritual_ZN28QQuick3DParticleLineParticle12setAlphaFadeEf', fade,
    )

  @overload(float)
  def setScaleMultiplier(self, multiplier: float) -> None:
    """
    Calls Qt's 'void QQuick3DParticleLineParticle::setScaleMultiplier(float
    multiplier)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlelineparticle.html

    Parameters
    ----------

    multiplier : float
      Passed on as it is.
    """
    #  void QQuick3DParticleLineParticle::setScaleMultiplier(float
    #      multiplier)
    self.uglySide.call(
        'ritual_ZN28QQuick3DParticleLineParticle18setScaleMultiplierEf',
        multiplier,
    )

  @overload(float)
  def setTexcoordMultiplier(self, multiplier: float) -> None:
    """
    Calls Qt's 'void
    QQuick3DParticleLineParticle::setTexcoordMultiplier(float multiplier)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlelineparticle.html

    Parameters
    ----------

    multiplier : float
      Passed on as it is.
    """
    #  void QQuick3DParticleLineParticle::setTexcoordMultiplier(float
    #      multiplier)
    self.uglySide.call(
        'ritual_ZN28QQuick3DParticleLineParticle21setTexcoordMultiplierEf',
        multiplier,
    )

  @overload(float)
  def setLength(self, length: float) -> None:
    """
    Calls Qt's 'void QQuick3DParticleLineParticle::setLength(float length)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlelineparticle.html#setLength

    Parameters
    ----------

    length : float
      Passed on as it is.
    """
    #  void QQuick3DParticleLineParticle::setLength(float length)
    self.uglySide.call(
        'ritual_ZN28QQuick3DParticleLineParticle9setLengthEf', length,
    )

  @overload(float)
  def setLengthVariation(self, length: float) -> None:
    """
    Calls Qt's 'void QQuick3DParticleLineParticle::setLengthVariation(float
    length)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlelineparticle.html

    Parameters
    ----------

    length : float
      Passed on as it is.
    """
    #  void QQuick3DParticleLineParticle::setLengthVariation(float length)
    self.uglySide.call(
        'ritual_ZN28QQuick3DParticleLineParticle18setLengthVariationEf',
        length,
    )

  @overload(float)
  def setLengthDeltaMin(self, min: float) -> None:
    """
    Calls Qt's 'void QQuick3DParticleLineParticle::setLengthDeltaMin(float
    min)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlelineparticle.html

    Parameters
    ----------

    min : float
      Passed on as it is.
    """
    #  void QQuick3DParticleLineParticle::setLengthDeltaMin(float min)
    self.uglySide.call(
        'ritual_ZN28QQuick3DParticleLineParticle17setLengthDeltaMinEf', min,
    )

  @overload(int)
  def setEolFadeOutDuration(self, duration: int) -> None:
    """
    Calls Qt's 'void QQuick3DParticleLineParticle::setEolFadeOutDuration(int
    duration)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlelineparticle.html

    Parameters
    ----------

    duration : int
      Passed on as it is.
    """
    #  void QQuick3DParticleLineParticle::setEolFadeOutDuration(int duration)
    self.uglySide.call(
        'ritual_ZN28QQuick3DParticleLineParticle21setEolFadeOutDurationEi',
        duration,
    )

  @overload(TexcoordMode)
  def setTexcoordMode(self, mode: TexcoordMode) -> None:
    """
    Calls Qt's 'void QQuick3DParticleLineParticle::setTexcoordMode(
    QQuick3DParticleLineParticle::TexcoordMode mode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlelineparticle.html#setTexcoordMode

    Parameters
    ----------

    mode : TexcoordMode
      Passed on as its number.
    """
    #  void QQuick3DParticleLineParticle::setTexcoordMode(
    #      QQuick3DParticleLineParticle::TexcoordMode mode)
    self.uglySide.call(
        'ritual_ZN28QQuick3DParticleLineParticle15setTexcoordModeENS_12Texc'
        'oordModeE',
        mode.value,
    )

  @overload(int, QVector3D, QVector3D, QVector4D, float, float, float)
  def setParticleData(
      self,
      particleIndex: int,
      position: QVector3D,
      rotation: QVector3D,
      color: QVector4D,
      size: float,
      age: float,
      animationFrame: float,
  ) -> None:
    """
    Calls Qt's 'void QQuick3DParticleLineParticle::setParticleData(int
    particleIndex, const QVector3D &position, const QVector3D &rotation,
    const QVector4D &color, float size, float age, float animationFrame)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlelineparticle.html#setParticleData

    Parameters
    ----------

    particleIndex : int
      Passed on as it is.

    position : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.

    rotation : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.

    color : QVector4D
      Passed on as a value: Qt reads the C++ QVector4D, which stays Python's
      own.

    size : float
      Passed on as it is.

    age : float
      Passed on as it is.

    animationFrame : float
      Passed on as it is.
    """
    #  void QQuick3DParticleLineParticle::setParticleData(int particleIndex,
    #      const QVector3D &position, const QVector3D &rotation, const
    #      QVector4D &color, float size, float age, float animationFrame)
    ritual = (
        'ritual_ZN28QQuick3DParticleLineParticle15setParticleDataEiRK9QVect'
        'or3DS2_RK9QVector4Dfff')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN28QQuick3DParticleLineParticle15setParticleDataEiRK'
          '9QVector3DS2_RK9QVector4Dfff')
    self.uglySide.call(
        ritual,
        particleIndex, self._valueOf(position), self._valueOf(rotation),
        self._valueOf(color), size, age, animationFrame,
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
  @overload(QQuick3DNode)
  @overload(NoneType)
  def __init__(self, parent: Optional[QQuick3DNode] = None) -> None:
    """
    Notes what was given, for Qt's
    'QQuick3DParticleLineParticle::QQuick3DParticleLineParticle(QQuick3DNode
    *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlelineparticle.html

    Parameters
    ----------

    parent : Optional[QQuick3DNode]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuick3DParticleLineParticle::QQuick3DParticleLineParticle(
    #      QQuick3DNode *parent)
    self._noteCreation(QQuick3DParticleLineParticle, lambda: Rituals.call(
        'ritual_ZN28QQuick3DParticleLineParticleC1EP12QQuick3DNode',
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

  def segmentCountChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DParticleLineParticle::segmentCountChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlelineparticle.html
    """
    #  void QQuick3DParticleLineParticle::segmentCountChanged()
    self.uglySide.call(
        'ritual_ZN28QQuick3DParticleLineParticle19segmentCountChangedEv',
    )

  def alphaFadeChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DParticleLineParticle::alphaFadeChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlelineparticle.html#alphaFadeChanged
    """
    #  void QQuick3DParticleLineParticle::alphaFadeChanged()
    self.uglySide.call(
        'ritual_ZN28QQuick3DParticleLineParticle16alphaFadeChangedEv',
    )

  def scaleMultiplierChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DParticleLineParticle::scaleMultiplierChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlelineparticle.html
    """
    #  void QQuick3DParticleLineParticle::scaleMultiplierChanged()
    self.uglySide.call(
        'ritual_ZN28QQuick3DParticleLineParticle22scaleMultiplierChangedEv',
    )

  def texcoordMultiplierChanged(self) -> None:
    """
    Calls Qt's 'void
    QQuick3DParticleLineParticle::texcoordMultiplierChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlelineparticle.html
    """
    #  void QQuick3DParticleLineParticle::texcoordMultiplierChanged()
    self.uglySide.call(
        'ritual_ZN28QQuick3DParticleLineParticle25texcoordMultiplierChanged'
        'Ev',
    )

  def lengthChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DParticleLineParticle::lengthChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlelineparticle.html#lengthChanged
    """
    #  void QQuick3DParticleLineParticle::lengthChanged()
    self.uglySide.call(
        'ritual_ZN28QQuick3DParticleLineParticle13lengthChangedEv',
    )

  def lengthVariationChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DParticleLineParticle::lengthVariationChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlelineparticle.html
    """
    #  void QQuick3DParticleLineParticle::lengthVariationChanged()
    self.uglySide.call(
        'ritual_ZN28QQuick3DParticleLineParticle22lengthVariationChangedEv',
    )

  def lengthDeltaMinChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DParticleLineParticle::lengthDeltaMinChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlelineparticle.html
    """
    #  void QQuick3DParticleLineParticle::lengthDeltaMinChanged()
    self.uglySide.call(
        'ritual_ZN28QQuick3DParticleLineParticle21lengthDeltaMinChangedEv',
    )

  def eolFadeOutDurationChanged(self) -> None:
    """
    Calls Qt's 'void
    QQuick3DParticleLineParticle::eolFadeOutDurationChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlelineparticle.html
    """
    #  void QQuick3DParticleLineParticle::eolFadeOutDurationChanged()
    self.uglySide.call(
        'ritual_ZN28QQuick3DParticleLineParticle25eolFadeOutDurationChanged'
        'Ev',
    )

  def texcoordModeChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DParticleLineParticle::texcoordModeChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlelineparticle.html
    """
    #  void QQuick3DParticleLineParticle::texcoordModeChanged()
    self.uglySide.call(
        'ritual_ZN28QQuick3DParticleLineParticle19texcoordModeChangedEv',
    )

  @overload(QSSGRenderGraphObject)
  @overload(NoneType)
  def updateLineNode(
      self,
      node: Optional[QSSGRenderGraphObject],
  ) -> Optional[QSSGRenderGraphObject]:
    """
    Calls Qt's 'QSSGRenderGraphObject
    *QQuick3DParticleLineParticle::updateLineNode(QSSGRenderGraphObject
    *node)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlelineparticle.html#updateLineNode

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
    #  QSSGRenderGraphObject *QQuick3DParticleLineParticle::updateLineNode(
    #      QSSGRenderGraphObject *node)
    address = self.uglySide.call(
        'ritual_ZN28QQuick3DParticleLineParticle14updateLineNodeEP21QSSGRen'
        'derGraphObject',
        self._addressOf(node),
    )
    from ..QtQuick3DRuntimeRender import QSSGRenderGraphObject
    return QSSGRenderGraphObject._cuteAt(address)

  def handleSegmentCountChanged(self) -> None:
    """
    Calls Qt's 'void
    QQuick3DParticleLineParticle::handleSegmentCountChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlelineparticle.html
    """
    #  void QQuick3DParticleLineParticle::handleSegmentCountChanged()
    self.uglySide.call(
        'ritual_ZN28QQuick3DParticleLineParticle25handleSegmentCountChanged'
        'Ev',
    )

  @overload(int)
  def updateLineSegment(self, particleIndex: int) -> None:
    """
    Calls Qt's 'void QQuick3DParticleLineParticle::updateLineSegment(int
    particleIndex)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlelineparticle.html

    Parameters
    ----------

    particleIndex : int
      Passed on as it is.
    """
    #  void QQuick3DParticleLineParticle::updateLineSegment(int
    #      particleIndex)
    self.uglySide.call(
        'ritual_ZN28QQuick3DParticleLineParticle17updateLineSegmentEi',
        particleIndex,
    )

  @overload(int)
  def clearSegment(self, particleIndex: int) -> None:
    """
    Calls Qt's 'void QQuick3DParticleLineParticle::clearSegment(int
    particleIndex)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlelineparticle.html#clearSegment

    Parameters
    ----------

    particleIndex : int
      Passed on as it is.
    """
    #  void QQuick3DParticleLineParticle::clearSegment(int particleIndex)
    self.uglySide.call(
        'ritual_ZN28QQuick3DParticleLineParticle12clearSegmentEi',
        particleIndex,
    )

  @overload(int)
  def handleMaxAmountChanged(self, amount: int) -> None:
    """
    Calls Qt's 'void QQuick3DParticleLineParticle::handleMaxAmountChanged(int
    amount)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlelineparticle.html

    Parameters
    ----------

    amount : int
      Passed on as it is.
    """
    #  void QQuick3DParticleLineParticle::handleMaxAmountChanged(int amount)
    ritual = (
        'ritual_ZN28QQuick3DParticleLineParticle22handleMaxAmountChangedEi')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN28QQuick3DParticleLineParticle22handleMaxAmountChan'
          'gedEi')
    self.uglySide.call(ritual, amount)

  @overload(QQuick3DParticleSystem)
  @overload(NoneType)
  def handleSystemChanged(
      self,
      system: Optional[QQuick3DParticleSystem],
  ) -> None:
    """
    Calls Qt's 'void
    QQuick3DParticleLineParticle::handleSystemChanged(QQuick3DParticleSystem
    *system)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlelineparticle.html

    Parameters
    ----------

    system : Optional[QQuick3DParticleSystem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuick3DParticleLineParticle::handleSystemChanged(
    #      QQuick3DParticleSystem *system)
    ritual = (
        'ritual_ZN28QQuick3DParticleLineParticle19handleSystemChangedEP22QQ'
        'uick3DParticleSystem')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN28QQuick3DParticleLineParticle19handleSystemChanged'
          'EP22QQuick3DParticleSystem')
    self.uglySide.call(ritual, self._addressOf(system))

  def reset(self) -> None:
    """
    Calls Qt's 'void QQuick3DParticleLineParticle::reset()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlelineparticle.html#reset
    """
    #  void QQuick3DParticleLineParticle::reset()
    ritual = 'ritual_ZN28QQuick3DParticleLineParticle5resetEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN28QQuick3DParticleLineParticle5resetEv'
    self.uglySide.call(ritual)

  @overload(float)
  def commitParticles(self, time: float) -> None:
    """
    Calls Qt's 'void QQuick3DParticleLineParticle::commitParticles(float
    time)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlelineparticle.html#commitParticles

    Parameters
    ----------

    time : float
      Passed on as it is.
    """
    #  void QQuick3DParticleLineParticle::commitParticles(float time)
    ritual = 'ritual_ZN28QQuick3DParticleLineParticle15commitParticlesEf'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN28QQuick3DParticleLineParticle15commitParticlesEf')
    self.uglySide.call(ritual, time)

  @overload(QQuick3DParticleEmitter)
  @overload(NoneType)
  def nextCurrentIndex(
      self,
      emitter: Optional[QQuick3DParticleEmitter],
  ) -> int:
    """
    Calls Qt's 'int QQuick3DParticleLineParticle::nextCurrentIndex(const
    QQuick3DParticleEmitter *emitter)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlelineparticle.html#nextCurrentIndex

    Parameters
    ----------

    emitter : Optional[QQuick3DParticleEmitter]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  int QQuick3DParticleLineParticle::nextCurrentIndex(const
    #      QQuick3DParticleEmitter *emitter)
    ritual = (
        'ritual_ZN28QQuick3DParticleLineParticle16nextCurrentIndexEPK23QQui'
        'ck3DParticleEmitter')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN28QQuick3DParticleLineParticle16nextCurrentIndexEPK'
          '23QQuick3DParticleEmitter')
    return self.uglySide.call(ritual, self._addressOf(emitter))

  @overload(int, float)
  def saveLineSegment(self, particleIndex: int, time: float) -> None:
    """
    Calls Qt's 'void QQuick3DParticleLineParticle::saveLineSegment(int
    particleIndex, float time)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlelineparticle.html#saveLineSegment

    Parameters
    ----------

    particleIndex : int
      Passed on as it is.

    time : float
      Passed on as it is.
    """
    #  void QQuick3DParticleLineParticle::saveLineSegment(int particleIndex,
    #      float time)
    self.uglySide.call(
        'ritual_ZN28QQuick3DParticleLineParticle15saveLineSegmentEif',
        particleIndex, time,
    )

  @overload(int)
  def resetParticleData(self, particleIndex: int) -> None:
    """
    Calls Qt's 'void QQuick3DParticleLineParticle::resetParticleData(int
    particleIndex)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlelineparticle.html

    Parameters
    ----------

    particleIndex : int
      Passed on as it is.
    """
    #  void QQuick3DParticleLineParticle::resetParticleData(int
    #      particleIndex)
    ritual = 'ritual_ZN28QQuick3DParticleLineParticle17resetParticleDataEi'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN28QQuick3DParticleLineParticle17resetParticleDataEi')
    self.uglySide.call(ritual, particleIndex)

  @staticmethod
  def updateLineBuffer(*__, **_) -> Never:
    """
    Qt's 'void
    QQuick3DParticleLineParticle::updateLineBuffer(LineParticleUpdateNode
    *updateNode, QSSGRenderGraphObject *node)': names
    'QQuick3DParticleLineParticle::LineParticleUpdateNode', which has no cute
    class yet.
    """
    raise NotImplementedError(
        "'QQuick3DParticleLineParticle.updateLineBuffer' has no cute "
        "function yet. Qt's 'void "
        "QQuick3DParticleLineParticle::updateLineBuffer(LineParticleUpdateNo"
        "de *updateNode, QSSGRenderGraphObject *node)': names "
        "'QQuick3DParticleLineParticle::LineParticleUpdateNode', which has "
        "no cute class yet.")
