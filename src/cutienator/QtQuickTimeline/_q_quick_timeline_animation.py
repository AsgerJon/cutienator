"""
QQuickTimelineAnimation binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickTimeline/6.12.0/QtQuickTimeline/private/qquicktimelineanimation_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuickTimelineAnimation to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin
from ..occult import Rituals
from ..QtCore import QList, QObject
from ..QtQuick import QQuickNumberAnimation

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickTimelineAnimation(QQuickNumberAnimation):
  """
  The cute side of Qt's QQuickTimelineAnimation: a plain Python object
  standing in front of one C++ QQuickTimelineAnimation.

  It is built on the cute 'QQuickNumberAnimation', as Qt's
  QQuickTimelineAnimation is built on Qt's QQuickNumberAnimation, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickTimelineAnimation that has a ritual and that
  Python can call so far, 8 names in all: 'metaObject', 'tr', 'setPingPong',
  'pingPong', 'pingPongChanged', 'finished', 'handleStarted',
  'handleStopped'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickTimelineAnimation::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QQuickTimelineAnimation::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.

  What has no ritual
  ------------------

  2 of the 13 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuickTimelineAnimation is created at the first use, not by
    'QQuickTimelineAnimation(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickTimelineAnimation.
  - Qt tells when it has removed the C++ QQuickTimelineAnimation. Every call
    on the cute object, and every use of it as an argument, then raises
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
    Calls Qt's 'QString QQuickTimelineAnimation::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktimelineanimation.html#tr

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
    #  QString QQuickTimelineAnimation::tr(const char *s, const char *c, int
    #      n)
    return Rituals.call(
        'ritual_ZN23QQuickTimelineAnimation2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickTimelineAnimation'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickTimelineAnimation::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktimelineanimation.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickTimelineAnimation::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK23QQuickTimelineAnimation10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def pingPong(self) -> bool:
    """
    Calls Qt's 'bool QQuickTimelineAnimation::pingPong() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktimelineanimation.html#pingPong
    """
    #  bool QQuickTimelineAnimation::pingPong() const
    return self.uglySide.call(
        'ritual_ZNK23QQuickTimelineAnimation8pingPongEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  def setPingPong(self, b: bool) -> None:
    """
    Calls Qt's 'void QQuickTimelineAnimation::setPingPong(bool b)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktimelineanimation.html#setPingPong

    Parameters
    ----------

    b : bool
      Passed on as it is.
    """
    #  void QQuickTimelineAnimation::setPingPong(bool b)
    self.uglySide.call(
        'ritual_ZN23QQuickTimelineAnimation11setPingPongEb', b,
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
    'QQuickTimelineAnimation::QQuickTimelineAnimation(QObject *parent)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktimelineanimation.html

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickTimelineAnimation::QQuickTimelineAnimation(QObject *parent)
    self._noteCreation(QQuickTimelineAnimation, lambda: Rituals.call(
        'ritual_ZN23QQuickTimelineAnimationC1EP7QObject',
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

  def pingPongChanged(self) -> None:
    """
    Calls Qt's 'void QQuickTimelineAnimation::pingPongChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktimelineanimation.html#pingPongChanged
    """
    #  void QQuickTimelineAnimation::pingPongChanged()
    self.uglySide.call(
        'ritual_ZN23QQuickTimelineAnimation15pingPongChangedEv',
    )

  def finished(self) -> None:
    """
    Calls Qt's 'void QQuickTimelineAnimation::finished()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktimelineanimation.html#finished
    """
    #  void QQuickTimelineAnimation::finished()
    self.uglySide.call('ritual_ZN23QQuickTimelineAnimation8finishedEv')

  def handleStarted(self) -> None:
    """
    Calls Qt's 'void QQuickTimelineAnimation::handleStarted()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktimelineanimation.html#handleStarted
    """
    #  void QQuickTimelineAnimation::handleStarted()
    self.uglySide.call('ritual_ZN23QQuickTimelineAnimation13handleStartedEv')

  def handleStopped(self) -> None:
    """
    Calls Qt's 'void QQuickTimelineAnimation::handleStopped()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktimelineanimation.html#handleStopped
    """
    #  void QQuickTimelineAnimation::handleStopped()
    self.uglySide.call('ritual_ZN23QQuickTimelineAnimation13handleStoppedEv')


#  Qt's 'QList<QQuickTimelineAnimation *>': the list of
#  QQuickTimelineAnimation, which 'QList[QQuickTimelineAnimation]' gives. It
#  is made here, so that there is one as soon as there can be a
#  QQuickTimelineAnimation.
QList.createKind(
    QQuickTimelineAnimation, 'address',
    make='ritual_list_make_QQuickTimelineAnimation_ptr',
    add='ritual_list_add_QQuickTimelineAnimation_ptr',
    size='ritual_list_size_QQuickTimelineAnimation_ptr',
    at='ritual_list_at_QQuickTimelineAnimation_ptr',
    drop='ritual_list_drop_QQuickTimelineAnimation_ptr',
)
