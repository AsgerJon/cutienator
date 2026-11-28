"""
QQuickTimeline binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickTimeline/6.12.0/QtQuickTimeline/private/qquicktimeline_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QQuickTimeline to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin
from ..occult import Rituals
from ..QtCore import QList, QObject
from ..QtQml import QQmlParserStatus

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
  from . import QQuickTimelineAnimation

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickTimeline(QObject, QQmlParserStatus):
  """
  The cute side of Qt's QQuickTimeline: a plain Python object standing in
  front of one C++ QQuickTimeline.

  It is built on the cute 'QObject', as Qt's QQuickTimeline is built on Qt's
  QObject, and has everything that class has. It is built on the cute
  'QQmlParserStatus' as well, as Qt's QQuickTimeline is built on Qt's
  QQmlParserStatus too, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickTimeline that has a ritual and that Python can
  call so far, 20 names in all: 'metaObject', 'tr', 'enabled', 'setEnabled',
  'startFrame', 'setStartFrame', 'endFrame', 'setEndFrame', 'currentFrame',
  'setCurrentFrame', 'reevaluate', 'init', 'reset', 'getAnimations',
  'classBegin', 'componentComplete', 'enabledChanged', 'startFrameChanged',
  'endFrameChanged', 'currentFrameChanged'. It can be made from Python, in 1
  way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickTimeline::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QQuickTimeline::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QQuickTimelinePrivate *QQuickTimeline::d_func()': gives
    'QQuickTimelinePrivate', which has no cute class yet.
  - Qt's 'const QQuickTimelinePrivate *QQuickTimeline::d_func() const': gives
    'QQuickTimelinePrivate', which has no cute class yet.
  - Qt's 'QQmlListProperty<QQuickKeyframeGroup>
    QQuickTimeline::keyframeGroups()': gives a type Python has no way to take
    yet.
  - Qt's 'QQmlListProperty<QQuickTimelineAnimation>
    QQuickTimeline::animations()': gives a type Python has no way to take
    yet.

  What has no ritual
  ------------------

  2 of the 29 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuickTimeline is created at the first use, not by
    'QQuickTimeline(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickTimeline.
  - Qt tells when it has removed the C++ QQuickTimeline. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQuickTimeline that has no cute function yet,
    'animations', 'keyframeGroups', holds a function that raises
    'NotImplementedError', and its docstring says why.
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
    Calls Qt's 'QString QQuickTimeline::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktimeline.html#tr

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
    #  QString QQuickTimeline::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN14QQuickTimeline2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickTimeline'

  #  Qt's QQuickTimeline is built on more than one class. The part of a C++
  #  QQuickTimeline that belongs to a class after the first begins somewhere
  #  inside the object, and the ritual named for that class gives where; see
  #  'CuteMixin._addressAs'.
  __cast_rituals__ = {
      'QQmlParserStatus': 'ritual_cast_QQuickTimeline_QQmlParserStatus',
  }

  #  A C++ QQuickTimeline Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickTimeline'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickTimeline::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktimeline.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickTimeline::metaObject() const
    address = self.uglySide.call('ritual_ZNK14QQuickTimeline10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def enabled(self) -> bool:
    """
    Calls Qt's 'bool QQuickTimeline::enabled() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktimeline.html#enabled
    """
    #  bool QQuickTimeline::enabled() const
    return self.uglySide.call('ritual_ZNK14QQuickTimeline7enabledEv')

  def startFrame(self) -> float:
    """
    Calls Qt's 'qreal QQuickTimeline::startFrame() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktimeline.html#startFrame
    """
    #  qreal QQuickTimeline::startFrame() const
    return self.uglySide.call('ritual_ZNK14QQuickTimeline10startFrameEv')

  def endFrame(self) -> float:
    """
    Calls Qt's 'qreal QQuickTimeline::endFrame() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktimeline.html#endFrame
    """
    #  qreal QQuickTimeline::endFrame() const
    return self.uglySide.call('ritual_ZNK14QQuickTimeline8endFrameEv')

  def currentFrame(self) -> float:
    """
    Calls Qt's 'qreal QQuickTimeline::currentFrame() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktimeline.html#currentFrame
    """
    #  qreal QQuickTimeline::currentFrame() const
    return self.uglySide.call('ritual_ZNK14QQuickTimeline12currentFrameEv')

  def getAnimations(self) -> QList[QQuickTimelineAnimation]:
    """
    Calls Qt's 'QList<QQuickTimelineAnimation *>
    QQuickTimeline::getAnimations() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktimeline.html#getAnimations

    Returns
    -------

    QList[QQuickTimelineAnimation]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QQuickTimelineAnimation *> QQuickTimeline::getAnimations() const
    address = self.uglySide.call(
        'ritual_ZNK14QQuickTimeline13getAnimationsEv',
    )
    from . import QQuickTimelineAnimation
    return QList[QQuickTimelineAnimation]._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  def setEnabled(self, enabled: bool) -> None:
    """
    Calls Qt's 'void QQuickTimeline::setEnabled(bool enabled)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktimeline.html#setEnabled

    Parameters
    ----------

    enabled : bool
      Passed on as it is.
    """
    #  void QQuickTimeline::setEnabled(bool enabled)
    self.uglySide.call('ritual_ZN14QQuickTimeline10setEnabledEb', enabled)

  @overload(float)
  def setStartFrame(self, a0: float) -> None:
    """
    Calls Qt's 'void QQuickTimeline::setStartFrame(qreal a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktimeline.html#setStartFrame

    Parameters
    ----------

    a0 : float
      Passed on as it is.
    """
    #  void QQuickTimeline::setStartFrame(qreal a0)
    self.uglySide.call('ritual_ZN14QQuickTimeline13setStartFrameEd', a0)

  @overload(float)
  def setEndFrame(self, a0: float) -> None:
    """
    Calls Qt's 'void QQuickTimeline::setEndFrame(qreal a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktimeline.html#setEndFrame

    Parameters
    ----------

    a0 : float
      Passed on as it is.
    """
    #  void QQuickTimeline::setEndFrame(qreal a0)
    self.uglySide.call('ritual_ZN14QQuickTimeline11setEndFrameEd', a0)

  @overload(float)
  def setCurrentFrame(self, a0: float) -> None:
    """
    Calls Qt's 'void QQuickTimeline::setCurrentFrame(qreal a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktimeline.html#setCurrentFrame

    Parameters
    ----------

    a0 : float
      Passed on as it is.
    """
    #  void QQuickTimeline::setCurrentFrame(qreal a0)
    self.uglySide.call('ritual_ZN14QQuickTimeline15setCurrentFrameEd', a0)

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
    Notes what was given, for Qt's 'QQuickTimeline::QQuickTimeline(QObject
    *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qquicktimeline.html#QQuickTimeline

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickTimeline::QQuickTimeline(QObject *parent)
    self._noteCreation(QQuickTimeline, lambda: Rituals.call(
        'ritual_ZN14QQuickTimelineC1EP7QObject',
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

  def reevaluate(self) -> None:
    """
    Calls Qt's 'void QQuickTimeline::reevaluate()'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktimeline.html#reevaluate
    """
    #  void QQuickTimeline::reevaluate()
    self.uglySide.call('ritual_ZN14QQuickTimeline10reevaluateEv')

  def init(self) -> None:
    """
    Calls Qt's 'void QQuickTimeline::init()'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktimeline.html#init
    """
    #  void QQuickTimeline::init()
    self.uglySide.call('ritual_ZN14QQuickTimeline4initEv')

  def reset(self) -> None:
    """
    Calls Qt's 'void QQuickTimeline::reset()'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktimeline.html#reset
    """
    #  void QQuickTimeline::reset()
    self.uglySide.call('ritual_ZN14QQuickTimeline5resetEv')

  def classBegin(self) -> None:
    """
    Calls Qt's 'void QQuickTimeline::classBegin()'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktimeline.html#classBegin
    """
    #  void QQuickTimeline::classBegin()
    ritual = 'ritual_ZN14QQuickTimeline10classBeginEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN14QQuickTimeline10classBeginEv'
    self.uglySide.call(ritual)

  def componentComplete(self) -> None:
    """
    Calls Qt's 'void QQuickTimeline::componentComplete()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktimeline.html#componentComplete
    """
    #  void QQuickTimeline::componentComplete()
    ritual = 'ritual_ZN14QQuickTimeline17componentCompleteEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN14QQuickTimeline17componentCompleteEv'
    self.uglySide.call(ritual)

  def enabledChanged(self) -> None:
    """
    Calls Qt's 'void QQuickTimeline::enabledChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktimeline.html#enabledChanged
    """
    #  void QQuickTimeline::enabledChanged()
    self.uglySide.call('ritual_ZN14QQuickTimeline14enabledChangedEv')

  def startFrameChanged(self) -> None:
    """
    Calls Qt's 'void QQuickTimeline::startFrameChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktimeline.html#startFrameChanged
    """
    #  void QQuickTimeline::startFrameChanged()
    self.uglySide.call('ritual_ZN14QQuickTimeline17startFrameChangedEv')

  def endFrameChanged(self) -> None:
    """
    Calls Qt's 'void QQuickTimeline::endFrameChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktimeline.html#endFrameChanged
    """
    #  void QQuickTimeline::endFrameChanged()
    self.uglySide.call('ritual_ZN14QQuickTimeline15endFrameChangedEv')

  def currentFrameChanged(self) -> None:
    """
    Calls Qt's 'void QQuickTimeline::currentFrameChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktimeline.html#currentFrameChanged
    """
    #  void QQuickTimeline::currentFrameChanged()
    self.uglySide.call('ritual_ZN14QQuickTimeline19currentFrameChangedEv')

  @staticmethod
  def animations(*__, **_) -> Never:
    """
    Qt's 'QQmlListProperty<QQuickTimelineAnimation>
    QQuickTimeline::animations()': gives a type Python has no way to take
    yet.
    """
    raise NotImplementedError(
        "'QQuickTimeline.animations' has no cute function yet. Qt's "
        "'QQmlListProperty<QQuickTimelineAnimation> "
        "QQuickTimeline::animations()': gives a type Python has no way to "
        "take yet.")

  @staticmethod
  def keyframeGroups(*__, **_) -> Never:
    """
    Qt's 'QQmlListProperty<QQuickKeyframeGroup>
    QQuickTimeline::keyframeGroups()': gives a type Python has no way to take
    yet.
    """
    raise NotImplementedError(
        "'QQuickTimeline.keyframeGroups' has no cute function yet. Qt's "
        "'QQmlListProperty<QQuickKeyframeGroup> "
        "QQuickTimeline::keyframeGroups()': gives a type Python has no way "
        "to take yet.")
