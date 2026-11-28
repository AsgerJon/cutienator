"""
QQuick3DParticleSpriteSequence binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3DParticles/6.12.0/QtQuick3DParticles/private/qquick3dparticlespritesequence_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuick3DParticleSpriteSequence to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum
from ..occult import Rituals
from ..QtCore import QObject
from ..QtQml import QQmlParserStatus

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuick3DParticleSpriteSequence(QObject, QQmlParserStatus):
  """
  The cute side of Qt's QQuick3DParticleSpriteSequence: a plain Python object
  standing in front of one C++ QQuick3DParticleSpriteSequence.

  It is built on the cute 'QObject', as Qt's QQuick3DParticleSpriteSequence
  is built on Qt's QObject, and has everything that class has. It is built on
  the cute 'QQmlParserStatus' as well, as Qt's QQuick3DParticleSpriteSequence
  is built on Qt's QQmlParserStatus too, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuick3DParticleSpriteSequence that has a ritual and
  that Python can call so far, 27 names in all: 'metaObject', 'tr',
  'frameCount', 'frameIndex', 'interpolate', 'duration', 'durationVariation',
  'randomStart', 'animationDirection', 'setFrameCount', 'setFrameIndex',
  'setInterpolate', 'setDuration', 'setDurationVariation', 'setRandomStart',
  'setAnimationDirection', 'frameCountChanged', 'frameIndexChanged',
  'interpolateChanged', 'durationChanged', 'durationVariationChanged',
  'randomStartChanged', 'animationDirectionChanged', 'componentComplete',
  'classBegin', 'markNodesDirty', 'firstFrame'. It can be made from Python,
  in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuick3DParticleSpriteSequence::qt_metacast(const char *a0)':
    one of Qt's own inner workings.
  - Qt's 'int QQuick3DParticleSpriteSequence::qt_metacall(QMetaObject::Call
    a0, int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QQuick3DParticleSpriteSequence::~QQuick3DParticleSpriteSequence()':
    the destructor: Python never removes a C++
    QQuick3DParticleSpriteSequence.

  What has no ritual
  ------------------

  2 of the 33 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuick3DParticleSpriteSequence is created at the first use, not
    by 'QQuick3DParticleSpriteSequence(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuick3DParticleSpriteSequence.
  - Qt tells when it has removed the C++ QQuick3DParticleSpriteSequence.
    Every call on the cute object, and every use of it as an argument, then
    raises 'RuntimeError', and nothing reaches C++.
  """

  #  The enums Qt writes inside QQuick3DParticleSpriteSequence, each a class
  #  in here as in C++, and the names Qt has for the combinations of its
  #  flags enums.

  class AnimationDirection(CuteNum):
    """
    The enum 'QQuick3DParticleSpriteSequence::AnimationDirection' of Qt, with
    the 5 names Qt gives in it.
    """

    Normal = Kee[int](0)
    Reverse = Kee[int](1)
    Alternate = Kee[int](2)
    AlternateReverse = Kee[int](3)
    SingleFrame = Kee[int](4)

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
    Calls Qt's 'QString QQuick3DParticleSpriteSequence::tr(const char *s,
    const char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlespritesequence.html#tr

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
    #  QString QQuick3DParticleSpriteSequence::tr(const char *s, const char
    #      *c, int n)
    return Rituals.call(
        'ritual_ZN30QQuick3DParticleSpriteSequence2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuick3DParticleSpriteSequence'

  #  Qt's QQuick3DParticleSpriteSequence is built on more than one class. The
  #  part of a C++ QQuick3DParticleSpriteSequence that belongs to a class
  #  after the first begins somewhere inside the object, and the ritual named
  #  for that class gives where; see 'CuteMixin._addressAs'.
  __cast_rituals__ = {
      'QQmlParserStatus':
          'ritual_cast_QQuick3DParticleSpriteSequence_QQmlParserStatus',
  }

  #  A C++ QQuick3DParticleSpriteSequence Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuick3DParticleSpriteSequence'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject
    *QQuick3DParticleSpriteSequence::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlespritesequence.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuick3DParticleSpriteSequence::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK30QQuick3DParticleSpriteSequence10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def frameCount(self) -> int:
    """
    Calls Qt's 'int QQuick3DParticleSpriteSequence::frameCount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlespritesequence.html#frameCount
    """
    #  int QQuick3DParticleSpriteSequence::frameCount() const
    return self.uglySide.call(
        'ritual_ZNK30QQuick3DParticleSpriteSequence10frameCountEv',
    )

  def frameIndex(self) -> int:
    """
    Calls Qt's 'int QQuick3DParticleSpriteSequence::frameIndex() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlespritesequence.html#frameIndex
    """
    #  int QQuick3DParticleSpriteSequence::frameIndex() const
    return self.uglySide.call(
        'ritual_ZNK30QQuick3DParticleSpriteSequence10frameIndexEv',
    )

  def interpolate(self) -> bool:
    """
    Calls Qt's 'bool QQuick3DParticleSpriteSequence::interpolate() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlespritesequence.html#interpolate
    """
    #  bool QQuick3DParticleSpriteSequence::interpolate() const
    return self.uglySide.call(
        'ritual_ZNK30QQuick3DParticleSpriteSequence11interpolateEv',
    )

  def duration(self) -> int:
    """
    Calls Qt's 'int QQuick3DParticleSpriteSequence::duration() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlespritesequence.html#duration
    """
    #  int QQuick3DParticleSpriteSequence::duration() const
    return self.uglySide.call(
        'ritual_ZNK30QQuick3DParticleSpriteSequence8durationEv',
    )

  def durationVariation(self) -> int:
    """
    Calls Qt's 'int QQuick3DParticleSpriteSequence::durationVariation()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlespritesequence.html
    """
    #  int QQuick3DParticleSpriteSequence::durationVariation() const
    return self.uglySide.call(
        'ritual_ZNK30QQuick3DParticleSpriteSequence17durationVariationEv',
    )

  def randomStart(self) -> bool:
    """
    Calls Qt's 'bool QQuick3DParticleSpriteSequence::randomStart() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlespritesequence.html#randomStart
    """
    #  bool QQuick3DParticleSpriteSequence::randomStart() const
    return self.uglySide.call(
        'ritual_ZNK30QQuick3DParticleSpriteSequence11randomStartEv',
    )

  def animationDirection(self) -> AnimationDirection:
    """
    Calls Qt's 'AnimationDirection
    QQuick3DParticleSpriteSequence::animationDirection() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlespritesequence.html

    Returns
    -------

    AnimationDirection
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'AnimationDirection(number)' gives.
    """
    #  AnimationDirection
    #      QQuick3DParticleSpriteSequence::animationDirection() const
    return QQuick3DParticleSpriteSequence.AnimationDirection(
        self.uglySide.call(
            'ritual_ZNK30QQuick3DParticleSpriteSequence18animationDirection'
            'Ev',
        ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setFrameCount(self, frameCount: int) -> None:
    """
    Calls Qt's 'void QQuick3DParticleSpriteSequence::setFrameCount(int
    frameCount)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlespritesequence.html#setFrameCount

    Parameters
    ----------

    frameCount : int
      Passed on as it is.
    """
    #  void QQuick3DParticleSpriteSequence::setFrameCount(int frameCount)
    self.uglySide.call(
        'ritual_ZN30QQuick3DParticleSpriteSequence13setFrameCountEi',
        frameCount,
    )

  @overload(int)
  def setFrameIndex(self, frameIndex: int) -> None:
    """
    Calls Qt's 'void QQuick3DParticleSpriteSequence::setFrameIndex(int
    frameIndex)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlespritesequence.html#setFrameIndex

    Parameters
    ----------

    frameIndex : int
      Passed on as it is.
    """
    #  void QQuick3DParticleSpriteSequence::setFrameIndex(int frameIndex)
    self.uglySide.call(
        'ritual_ZN30QQuick3DParticleSpriteSequence13setFrameIndexEi',
        frameIndex,
    )

  @overload(bool)
  def setInterpolate(self, interpolate: bool) -> None:
    """
    Calls Qt's 'void QQuick3DParticleSpriteSequence::setInterpolate(bool
    interpolate)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlespritesequence.html#setInterpolate

    Parameters
    ----------

    interpolate : bool
      Passed on as it is.
    """
    #  void QQuick3DParticleSpriteSequence::setInterpolate(bool interpolate)
    self.uglySide.call(
        'ritual_ZN30QQuick3DParticleSpriteSequence14setInterpolateEb',
        interpolate,
    )

  @overload(int)
  def setDuration(self, duration: int) -> None:
    """
    Calls Qt's 'void QQuick3DParticleSpriteSequence::setDuration(int
    duration)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlespritesequence.html#setDuration

    Parameters
    ----------

    duration : int
      Passed on as it is.
    """
    #  void QQuick3DParticleSpriteSequence::setDuration(int duration)
    self.uglySide.call(
        'ritual_ZN30QQuick3DParticleSpriteSequence11setDurationEi', duration,
    )

  @overload(int)
  def setDurationVariation(self, durationVariation: int) -> None:
    """
    Calls Qt's 'void QQuick3DParticleSpriteSequence::setDurationVariation(int
    durationVariation)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlespritesequence.html

    Parameters
    ----------

    durationVariation : int
      Passed on as it is.
    """
    #  void QQuick3DParticleSpriteSequence::setDurationVariation(int
    #      durationVariation)
    self.uglySide.call(
        'ritual_ZN30QQuick3DParticleSpriteSequence20setDurationVariationEi',
        durationVariation,
    )

  @overload(bool)
  def setRandomStart(self, randomStart: bool) -> None:
    """
    Calls Qt's 'void QQuick3DParticleSpriteSequence::setRandomStart(bool
    randomStart)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlespritesequence.html#setRandomStart

    Parameters
    ----------

    randomStart : bool
      Passed on as it is.
    """
    #  void QQuick3DParticleSpriteSequence::setRandomStart(bool randomStart)
    self.uglySide.call(
        'ritual_ZN30QQuick3DParticleSpriteSequence14setRandomStartEb',
        randomStart,
    )

  @overload(AnimationDirection)
  def setAnimationDirection(
      self,
      animationDirection: AnimationDirection,
  ) -> None:
    """
    Calls Qt's 'void QQuick3DParticleSpriteSequence::setAnimationDirection(
    QQuick3DParticleSpriteSequence::AnimationDirection animationDirection)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlespritesequence.html

    Parameters
    ----------

    animationDirection : AnimationDirection
      Passed on as its number.
    """
    #  void QQuick3DParticleSpriteSequence::setAnimationDirection(
    #      QQuick3DParticleSpriteSequence::AnimationDirection
    #      animationDirection)
    self.uglySide.call(
        'ritual_ZN30QQuick3DParticleSpriteSequence21setAnimationDirectionEN'
        'S_18AnimationDirectionE',
        animationDirection.value,
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
  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's
    'QQuick3DParticleSpriteSequence::QQuick3DParticleSpriteSequence(QObject
    *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlespritesequence.html

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuick3DParticleSpriteSequence::QQuick3DParticleSpriteSequence(QObject
    #      *parent)
    self._noteCreation(QQuick3DParticleSpriteSequence, lambda: Rituals.call(
        'ritual_ZN30QQuick3DParticleSpriteSequenceC1EP7QObject',
        self._addressOf(parent, 'QObject'),
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

  def frameCountChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DParticleSpriteSequence::frameCountChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlespritesequence.html
    """
    #  void QQuick3DParticleSpriteSequence::frameCountChanged()
    self.uglySide.call(
        'ritual_ZN30QQuick3DParticleSpriteSequence17frameCountChangedEv',
    )

  def frameIndexChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DParticleSpriteSequence::frameIndexChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlespritesequence.html
    """
    #  void QQuick3DParticleSpriteSequence::frameIndexChanged()
    self.uglySide.call(
        'ritual_ZN30QQuick3DParticleSpriteSequence17frameIndexChangedEv',
    )

  def interpolateChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DParticleSpriteSequence::interpolateChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlespritesequence.html
    """
    #  void QQuick3DParticleSpriteSequence::interpolateChanged()
    self.uglySide.call(
        'ritual_ZN30QQuick3DParticleSpriteSequence18interpolateChangedEv',
    )

  def durationChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DParticleSpriteSequence::durationChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlespritesequence.html
    """
    #  void QQuick3DParticleSpriteSequence::durationChanged()
    self.uglySide.call(
        'ritual_ZN30QQuick3DParticleSpriteSequence15durationChangedEv',
    )

  def durationVariationChanged(self) -> None:
    """
    Calls Qt's 'void
    QQuick3DParticleSpriteSequence::durationVariationChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlespritesequence.html
    """
    #  void QQuick3DParticleSpriteSequence::durationVariationChanged()
    self.uglySide.call(
        'ritual_ZN30QQuick3DParticleSpriteSequence24durationVariationChange'
        'dEv',
    )

  def randomStartChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DParticleSpriteSequence::randomStartChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlespritesequence.html
    """
    #  void QQuick3DParticleSpriteSequence::randomStartChanged()
    self.uglySide.call(
        'ritual_ZN30QQuick3DParticleSpriteSequence18randomStartChangedEv',
    )

  def animationDirectionChanged(self) -> None:
    """
    Calls Qt's 'void
    QQuick3DParticleSpriteSequence::animationDirectionChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlespritesequence.html
    """
    #  void QQuick3DParticleSpriteSequence::animationDirectionChanged()
    self.uglySide.call(
        'ritual_ZN30QQuick3DParticleSpriteSequence25animationDirectionChang'
        'edEv',
    )

  def componentComplete(self) -> None:
    """
    Calls Qt's 'void QQuick3DParticleSpriteSequence::componentComplete()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlespritesequence.html
    """
    #  void QQuick3DParticleSpriteSequence::componentComplete()
    ritual = 'ritual_ZN30QQuick3DParticleSpriteSequence17componentCompleteEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN30QQuick3DParticleSpriteSequence17componentComplete'
          'Ev')
    self.uglySide.call(ritual)

  def classBegin(self) -> None:
    """
    Calls Qt's 'void QQuick3DParticleSpriteSequence::classBegin()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlespritesequence.html#classBegin
    """
    #  void QQuick3DParticleSpriteSequence::classBegin()
    ritual = 'ritual_ZN30QQuick3DParticleSpriteSequence10classBeginEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN30QQuick3DParticleSpriteSequence10classBeginEv'
    self.uglySide.call(ritual)

  def markNodesDirty(self) -> None:
    """
    Calls Qt's 'void QQuick3DParticleSpriteSequence::markNodesDirty()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlespritesequence.html#markNodesDirty
    """
    #  void QQuick3DParticleSpriteSequence::markNodesDirty()
    self.uglySide.call(
        'ritual_ZN30QQuick3DParticleSpriteSequence14markNodesDirtyEv',
    )

  @overload(int, bool)
  def firstFrame(self, index: int, singleFrame: bool) -> float:
    """
    Calls Qt's 'float QQuick3DParticleSpriteSequence::firstFrame(int index,
    bool singleFrame)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlespritesequence.html#firstFrame

    Parameters
    ----------

    index : int
      Passed on as it is.

    singleFrame : bool
      Passed on as it is.
    """
    #  float QQuick3DParticleSpriteSequence::firstFrame(int index, bool
    #      singleFrame)
    return self.uglySide.call(
        'ritual_ZN30QQuick3DParticleSpriteSequence10firstFrameEib',
        index, singleFrame,
    )
