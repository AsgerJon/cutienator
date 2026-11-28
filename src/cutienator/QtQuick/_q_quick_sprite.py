"""
QQuickSprite binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquicksprite_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QQuickSprite to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QList, QObject
from . import QQuickStochasticState

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


class QQuickSprite(QQuickStochasticState):
  """
  The cute side of Qt's QQuickSprite: a plain Python object standing in front
  of one C++ QQuickSprite.

  It is built on the cute 'QQuickStochasticState', as Qt's QQuickSprite is
  built on Qt's QQuickStochasticState, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickSprite that has a ritual and that Python can
  call so far, 46 names in all: 'metaObject', 'tr', 'source', 'frameHeight',
  'frameWidth', 'reverse', 'frames', 'frameCount', 'frameX', 'frameY',
  'resetFrameRate', 'frameRate', 'frameRateVariation', 'resetFrameDuration',
  'frameDuration', 'frameDurationVariation', 'variedDuration', 'frameSync',
  'setDevicePixelRatio', 'devicePixelRatio', 'sourceChanged',
  'frameHeightChanged', 'frameWidthChanged', 'reverseChanged',
  'frameCountChanged', 'frameXChanged', 'frameYChanged', 'frameRateChanged',
  'frameRateVariationChanged', 'frameDurationChanged',
  'frameDurationVariationChanged', 'frameSyncChanged', 'setSource',
  'setFrameHeight', 'setFrameWidth', 'setReverse', 'setFrames',
  'setFrameCount', 'setFrameX', 'setFrameY', 'setFrameRate',
  'setFrameRateVariation', 'setFrameDuration', 'setFrameDurationVariation',
  'setFrameSync', 'startImageLoading'. It can be made from Python, in 1 way;
  see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickSprite::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QQuickSprite::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QQuickSprite::~QQuickSprite()': the destructor: Python never
    removes a C++ QQuickSprite.

  What has no ritual
  ------------------

  2 of the 52 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuickSprite is created at the first use, not by
    'QQuickSprite(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickSprite.
  - Qt tells when it has removed the C++ QQuickSprite. Every call on the cute
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
    Calls Qt's 'QString QQuickSprite::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicksprite.html#tr

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
    #  QString QQuickSprite::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN12QQuickSprite2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickSprite'

  #  A C++ QQuickSprite Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickSprite'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickSprite::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicksprite.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickSprite::metaObject() const
    address = self.uglySide.call('ritual_ZNK12QQuickSprite10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def source(self) -> QUrl:
    """
    Calls Qt's 'QUrl QQuickSprite::source() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicksprite.html#source

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QQuickSprite::source() const
    address = self.uglySide.call('ritual_ZNK12QQuickSprite6sourceEv')
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  def frameHeight(self) -> int:
    """
    Calls Qt's 'int QQuickSprite::frameHeight() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicksprite.html#frameHeight
    """
    #  int QQuickSprite::frameHeight() const
    return self.uglySide.call('ritual_ZNK12QQuickSprite11frameHeightEv')

  def frameWidth(self) -> int:
    """
    Calls Qt's 'int QQuickSprite::frameWidth() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicksprite.html#frameWidth
    """
    #  int QQuickSprite::frameWidth() const
    return self.uglySide.call('ritual_ZNK12QQuickSprite10frameWidthEv')

  def reverse(self) -> bool:
    """
    Calls Qt's 'bool QQuickSprite::reverse() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicksprite.html#reverse
    """
    #  bool QQuickSprite::reverse() const
    return self.uglySide.call('ritual_ZNK12QQuickSprite7reverseEv')

  def frames(self) -> int:
    """
    Calls Qt's 'int QQuickSprite::frames() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicksprite.html#frames
    """
    #  int QQuickSprite::frames() const
    return self.uglySide.call('ritual_ZNK12QQuickSprite6framesEv')

  def frameCount(self) -> int:
    """
    Calls Qt's 'int QQuickSprite::frameCount() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicksprite.html#frameCount
    """
    #  int QQuickSprite::frameCount() const
    return self.uglySide.call('ritual_ZNK12QQuickSprite10frameCountEv')

  def frameX(self) -> int:
    """
    Calls Qt's 'int QQuickSprite::frameX() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicksprite.html#frameX
    """
    #  int QQuickSprite::frameX() const
    return self.uglySide.call('ritual_ZNK12QQuickSprite6frameXEv')

  def frameY(self) -> int:
    """
    Calls Qt's 'int QQuickSprite::frameY() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicksprite.html#frameY
    """
    #  int QQuickSprite::frameY() const
    return self.uglySide.call('ritual_ZNK12QQuickSprite6frameYEv')

  def frameRate(self) -> float:
    """
    Calls Qt's 'qreal QQuickSprite::frameRate() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicksprite.html#frameRate
    """
    #  qreal QQuickSprite::frameRate() const
    return self.uglySide.call('ritual_ZNK12QQuickSprite9frameRateEv')

  def frameRateVariation(self) -> float:
    """
    Calls Qt's 'qreal QQuickSprite::frameRateVariation() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicksprite.html#frameRateVariation
    """
    #  qreal QQuickSprite::frameRateVariation() const
    return self.uglySide.call(
        'ritual_ZNK12QQuickSprite18frameRateVariationEv',
    )

  def frameDuration(self) -> int:
    """
    Calls Qt's 'int QQuickSprite::frameDuration() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicksprite.html#frameDuration
    """
    #  int QQuickSprite::frameDuration() const
    return self.uglySide.call('ritual_ZNK12QQuickSprite13frameDurationEv')

  def frameDurationVariation(self) -> int:
    """
    Calls Qt's 'int QQuickSprite::frameDurationVariation() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicksprite.html#frameDurationVariation
    """
    #  int QQuickSprite::frameDurationVariation() const
    return self.uglySide.call(
        'ritual_ZNK12QQuickSprite22frameDurationVariationEv',
    )

  def variedDuration(self) -> int:
    """
    Calls Qt's 'int QQuickSprite::variedDuration() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicksprite.html#variedDuration
    """
    #  int QQuickSprite::variedDuration() const
    ritual = 'ritual_ZNK12QQuickSprite14variedDurationEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK12QQuickSprite14variedDurationEv'
    return self.uglySide.call(ritual)

  def frameSync(self) -> bool:
    """
    Calls Qt's 'bool QQuickSprite::frameSync() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicksprite.html#frameSync
    """
    #  bool QQuickSprite::frameSync() const
    return self.uglySide.call('ritual_ZNK12QQuickSprite9frameSyncEv')

  def devicePixelRatio(self) -> float:
    """
    Calls Qt's 'qreal QQuickSprite::devicePixelRatio() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicksprite.html#devicePixelRatio
    """
    #  qreal QQuickSprite::devicePixelRatio() const
    return self.uglySide.call('ritual_ZNK12QQuickSprite16devicePixelRatioEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float)
  def setDevicePixelRatio(self, dpr: float) -> None:
    """
    Calls Qt's 'void QQuickSprite::setDevicePixelRatio(qreal dpr)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicksprite.html#setDevicePixelRatio

    Parameters
    ----------

    dpr : float
      Passed on as it is.
    """
    #  void QQuickSprite::setDevicePixelRatio(qreal dpr)
    self.uglySide.call('ritual_ZN12QQuickSprite19setDevicePixelRatioEd', dpr)

  @overload(QUrl)
  def setSource(self, arg: QUrl) -> None:
    """
    Calls Qt's 'void QQuickSprite::setSource(QUrl arg)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicksprite.html#setSource

    Parameters
    ----------

    arg : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  void QQuickSprite::setSource(QUrl arg)
    self.uglySide.call(
        'ritual_ZN12QQuickSprite9setSourceE4QUrl', self._valueOf(arg),
    )

  @overload(int)
  def setFrameHeight(self, arg: int) -> None:
    """
    Calls Qt's 'void QQuickSprite::setFrameHeight(int arg)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicksprite.html#setFrameHeight

    Parameters
    ----------

    arg : int
      Passed on as it is.
    """
    #  void QQuickSprite::setFrameHeight(int arg)
    self.uglySide.call('ritual_ZN12QQuickSprite14setFrameHeightEi', arg)

  @overload(int)
  def setFrameWidth(self, arg: int) -> None:
    """
    Calls Qt's 'void QQuickSprite::setFrameWidth(int arg)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicksprite.html#setFrameWidth

    Parameters
    ----------

    arg : int
      Passed on as it is.
    """
    #  void QQuickSprite::setFrameWidth(int arg)
    self.uglySide.call('ritual_ZN12QQuickSprite13setFrameWidthEi', arg)

  @overload(bool)
  def setReverse(self, arg: bool) -> None:
    """
    Calls Qt's 'void QQuickSprite::setReverse(bool arg)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicksprite.html#setReverse

    Parameters
    ----------

    arg : bool
      Passed on as it is.
    """
    #  void QQuickSprite::setReverse(bool arg)
    self.uglySide.call('ritual_ZN12QQuickSprite10setReverseEb', arg)

  @overload(int)
  def setFrames(self, arg: int) -> None:
    """
    Calls Qt's 'void QQuickSprite::setFrames(int arg)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicksprite.html#setFrames

    Parameters
    ----------

    arg : int
      Passed on as it is.
    """
    #  void QQuickSprite::setFrames(int arg)
    self.uglySide.call('ritual_ZN12QQuickSprite9setFramesEi', arg)

  @overload(int)
  def setFrameCount(self, arg: int) -> None:
    """
    Calls Qt's 'void QQuickSprite::setFrameCount(int arg)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicksprite.html#setFrameCount

    Parameters
    ----------

    arg : int
      Passed on as it is.
    """
    #  void QQuickSprite::setFrameCount(int arg)
    self.uglySide.call('ritual_ZN12QQuickSprite13setFrameCountEi', arg)

  @overload(int)
  def setFrameX(self, arg: int) -> None:
    """
    Calls Qt's 'void QQuickSprite::setFrameX(int arg)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicksprite.html#setFrameX

    Parameters
    ----------

    arg : int
      Passed on as it is.
    """
    #  void QQuickSprite::setFrameX(int arg)
    self.uglySide.call('ritual_ZN12QQuickSprite9setFrameXEi', arg)

  @overload(int)
  def setFrameY(self, arg: int) -> None:
    """
    Calls Qt's 'void QQuickSprite::setFrameY(int arg)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicksprite.html#setFrameY

    Parameters
    ----------

    arg : int
      Passed on as it is.
    """
    #  void QQuickSprite::setFrameY(int arg)
    self.uglySide.call('ritual_ZN12QQuickSprite9setFrameYEi', arg)

  @overload(float)
  def setFrameRate(self, arg: float) -> None:
    """
    Calls Qt's 'void QQuickSprite::setFrameRate(qreal arg)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicksprite.html#setFrameRate

    Parameters
    ----------

    arg : float
      Passed on as it is.
    """
    #  void QQuickSprite::setFrameRate(qreal arg)
    self.uglySide.call('ritual_ZN12QQuickSprite12setFrameRateEd', arg)

  @overload(float)
  def setFrameRateVariation(self, arg: float) -> None:
    """
    Calls Qt's 'void QQuickSprite::setFrameRateVariation(qreal arg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicksprite.html#setFrameRateVariation

    Parameters
    ----------

    arg : float
      Passed on as it is.
    """
    #  void QQuickSprite::setFrameRateVariation(qreal arg)
    self.uglySide.call(
        'ritual_ZN12QQuickSprite21setFrameRateVariationEd', arg,
    )

  @overload(int)
  def setFrameDuration(self, arg: int) -> None:
    """
    Calls Qt's 'void QQuickSprite::setFrameDuration(int arg)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicksprite.html#setFrameDuration

    Parameters
    ----------

    arg : int
      Passed on as it is.
    """
    #  void QQuickSprite::setFrameDuration(int arg)
    self.uglySide.call('ritual_ZN12QQuickSprite16setFrameDurationEi', arg)

  @overload(int)
  def setFrameDurationVariation(self, arg: int) -> None:
    """
    Calls Qt's 'void QQuickSprite::setFrameDurationVariation(int arg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicksprite.html#setFrameDurationVariation

    Parameters
    ----------

    arg : int
      Passed on as it is.
    """
    #  void QQuickSprite::setFrameDurationVariation(int arg)
    self.uglySide.call(
        'ritual_ZN12QQuickSprite25setFrameDurationVariationEi', arg,
    )

  @overload(bool)
  def setFrameSync(self, arg: bool) -> None:
    """
    Calls Qt's 'void QQuickSprite::setFrameSync(bool arg)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicksprite.html#setFrameSync

    Parameters
    ----------

    arg : bool
      Passed on as it is.
    """
    #  void QQuickSprite::setFrameSync(bool arg)
    self.uglySide.call('ritual_ZN12QQuickSprite12setFrameSyncEb', arg)

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
    Notes what was given, for Qt's 'QQuickSprite::QQuickSprite(QObject
    *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qquicksprite.html#QQuickSprite

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickSprite::QQuickSprite(QObject *parent)
    self._noteCreation(QQuickSprite, lambda: Rituals.call(
        'ritual_ZN12QQuickSpriteC1EP7QObject',
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

  def resetFrameRate(self) -> None:
    """
    Calls Qt's 'void QQuickSprite::resetFrameRate()'.

    Qt's own words: https://doc.qt.io/qt-6/qquicksprite.html#resetFrameRate
    """
    #  void QQuickSprite::resetFrameRate()
    self.uglySide.call('ritual_ZN12QQuickSprite14resetFrameRateEv')

  def resetFrameDuration(self) -> None:
    """
    Calls Qt's 'void QQuickSprite::resetFrameDuration()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicksprite.html#resetFrameDuration
    """
    #  void QQuickSprite::resetFrameDuration()
    self.uglySide.call('ritual_ZN12QQuickSprite18resetFrameDurationEv')

  @overload(QUrl)
  def sourceChanged(self, arg: QUrl) -> None:
    """
    Calls Qt's 'void QQuickSprite::sourceChanged(QUrl arg)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicksprite.html#sourceChanged

    Parameters
    ----------

    arg : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  void QQuickSprite::sourceChanged(QUrl arg)
    self.uglySide.call(
        'ritual_ZN12QQuickSprite13sourceChangedE4QUrl', self._valueOf(arg),
    )

  @overload(int)
  def frameHeightChanged(self, arg: int) -> None:
    """
    Calls Qt's 'void QQuickSprite::frameHeightChanged(int arg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicksprite.html#frameHeightChanged

    Parameters
    ----------

    arg : int
      Passed on as it is.
    """
    #  void QQuickSprite::frameHeightChanged(int arg)
    self.uglySide.call('ritual_ZN12QQuickSprite18frameHeightChangedEi', arg)

  @overload(int)
  def frameWidthChanged(self, arg: int) -> None:
    """
    Calls Qt's 'void QQuickSprite::frameWidthChanged(int arg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicksprite.html#frameWidthChanged

    Parameters
    ----------

    arg : int
      Passed on as it is.
    """
    #  void QQuickSprite::frameWidthChanged(int arg)
    self.uglySide.call('ritual_ZN12QQuickSprite17frameWidthChangedEi', arg)

  @overload(bool)
  def reverseChanged(self, arg: bool) -> None:
    """
    Calls Qt's 'void QQuickSprite::reverseChanged(bool arg)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicksprite.html#reverseChanged

    Parameters
    ----------

    arg : bool
      Passed on as it is.
    """
    #  void QQuickSprite::reverseChanged(bool arg)
    self.uglySide.call('ritual_ZN12QQuickSprite14reverseChangedEb', arg)

  @overload(int)
  def frameCountChanged(self, arg: int) -> None:
    """
    Calls Qt's 'void QQuickSprite::frameCountChanged(int arg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicksprite.html#frameCountChanged

    Parameters
    ----------

    arg : int
      Passed on as it is.
    """
    #  void QQuickSprite::frameCountChanged(int arg)
    self.uglySide.call('ritual_ZN12QQuickSprite17frameCountChangedEi', arg)

  @overload(int)
  def frameXChanged(self, arg: int) -> None:
    """
    Calls Qt's 'void QQuickSprite::frameXChanged(int arg)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicksprite.html#frameXChanged

    Parameters
    ----------

    arg : int
      Passed on as it is.
    """
    #  void QQuickSprite::frameXChanged(int arg)
    self.uglySide.call('ritual_ZN12QQuickSprite13frameXChangedEi', arg)

  @overload(int)
  def frameYChanged(self, arg: int) -> None:
    """
    Calls Qt's 'void QQuickSprite::frameYChanged(int arg)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicksprite.html#frameYChanged

    Parameters
    ----------

    arg : int
      Passed on as it is.
    """
    #  void QQuickSprite::frameYChanged(int arg)
    self.uglySide.call('ritual_ZN12QQuickSprite13frameYChangedEi', arg)

  @overload(float)
  def frameRateChanged(self, arg: float) -> None:
    """
    Calls Qt's 'void QQuickSprite::frameRateChanged(qreal arg)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicksprite.html#frameRateChanged

    Parameters
    ----------

    arg : float
      Passed on as it is.
    """
    #  void QQuickSprite::frameRateChanged(qreal arg)
    self.uglySide.call('ritual_ZN12QQuickSprite16frameRateChangedEd', arg)

  @overload(float)
  def frameRateVariationChanged(self, arg: float) -> None:
    """
    Calls Qt's 'void QQuickSprite::frameRateVariationChanged(qreal arg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicksprite.html#frameRateVariationChanged

    Parameters
    ----------

    arg : float
      Passed on as it is.
    """
    #  void QQuickSprite::frameRateVariationChanged(qreal arg)
    self.uglySide.call(
        'ritual_ZN12QQuickSprite25frameRateVariationChangedEd', arg,
    )

  @overload(int)
  def frameDurationChanged(self, arg: int) -> None:
    """
    Calls Qt's 'void QQuickSprite::frameDurationChanged(int arg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicksprite.html#frameDurationChanged

    Parameters
    ----------

    arg : int
      Passed on as it is.
    """
    #  void QQuickSprite::frameDurationChanged(int arg)
    self.uglySide.call(
        'ritual_ZN12QQuickSprite20frameDurationChangedEi', arg,
    )

  @overload(int)
  def frameDurationVariationChanged(self, arg: int) -> None:
    """
    Calls Qt's 'void QQuickSprite::frameDurationVariationChanged(int arg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicksprite.html#frameDurationVariationChanged

    Parameters
    ----------

    arg : int
      Passed on as it is.
    """
    #  void QQuickSprite::frameDurationVariationChanged(int arg)
    self.uglySide.call(
        'ritual_ZN12QQuickSprite29frameDurationVariationChangedEi', arg,
    )

  @overload(bool)
  def frameSyncChanged(self, arg: bool) -> None:
    """
    Calls Qt's 'void QQuickSprite::frameSyncChanged(bool arg)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicksprite.html#frameSyncChanged

    Parameters
    ----------

    arg : bool
      Passed on as it is.
    """
    #  void QQuickSprite::frameSyncChanged(bool arg)
    self.uglySide.call('ritual_ZN12QQuickSprite16frameSyncChangedEb', arg)

  def startImageLoading(self) -> None:
    """
    Calls Qt's 'void QQuickSprite::startImageLoading()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicksprite.html#startImageLoading
    """
    #  void QQuickSprite::startImageLoading()
    self.uglySide.call('ritual_ZN12QQuickSprite17startImageLoadingEv')


#  Qt's 'QList<QQuickSprite *>': the list of QQuickSprite, which
#  'QList[QQuickSprite]' gives. It is made here, so that there is one as soon
#  as there can be a QQuickSprite.
QList.createKind(
    QQuickSprite, 'address',
    make='ritual_list_make_QQuickSprite_ptr',
    add='ritual_list_add_QQuickSprite_ptr',
    size='ritual_list_size_QQuickSprite_ptr',
    at='ritual_list_at_QQuickSprite_ptr',
    drop='ritual_list_drop_QQuickSprite_ptr',
)
