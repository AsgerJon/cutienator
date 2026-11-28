"""
QQuickNumberAnimation binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquickanimation_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QQuickNumberAnimation to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin
from ..occult import Rituals
from ..QtCore import QObject
from . import QQuickPropertyAnimation

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from . import QQuickPropertyAnimationPrivate

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickNumberAnimation(QQuickPropertyAnimation):
  """
  The cute side of Qt's QQuickNumberAnimation: a plain Python object standing
  in front of one C++ QQuickNumberAnimation.

  It is built on the cute 'QQuickPropertyAnimation', as Qt's
  QQuickNumberAnimation is built on Qt's QQuickPropertyAnimation, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickNumberAnimation that has a ritual and that
  Python can call so far, 8 names in all: 'metaObject', 'tr', 'd_func',
  'from_', 'setFrom', 'to', 'setTo', 'init'. It can be made from Python, in 1
  way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickNumberAnimation::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QQuickNumberAnimation::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'const QQuickPropertyAnimationPrivate
    *QQuickNumberAnimation::d_func() const': takes in Python what
    'QQuickPropertyAnimationPrivate *QQuickNumberAnimation::d_func()' takes.
  - Qt's 'QQuickNumberAnimation::~QQuickNumberAnimation()': the destructor:
    Python never removes a C++ QQuickNumberAnimation.
  - Qt's 'QQuickNumberAnimation::QQuickNumberAnimation(
    QQuickPropertyAnimationPrivate &dd, QObject *parent)': takes a type
    Python has no way to hand over yet.

  What has no ritual
  ------------------

  2 of the 16 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuickNumberAnimation is created at the first use, not by
    'QQuickNumberAnimation(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickNumberAnimation.
  - Qt tells when it has removed the C++ QQuickNumberAnimation. Every call on
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
    Calls Qt's 'QString QQuickNumberAnimation::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicknumberanimation.html#tr

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
    #  QString QQuickNumberAnimation::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN21QQuickNumberAnimation2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickNumberAnimation'

  #  A C++ QQuickNumberAnimation Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickNumberAnimation'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickNumberAnimation::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicknumberanimation.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickNumberAnimation::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK21QQuickNumberAnimation10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def from_(self) -> float:
    """
    Calls Qt's 'qreal QQuickNumberAnimation::from() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicknumberanimation.html#from
    """
    #  qreal QQuickNumberAnimation::from() const
    return self.uglySide.call('ritual_ZNK21QQuickNumberAnimation4fromEv')

  def to(self) -> float:
    """
    Calls Qt's 'qreal QQuickNumberAnimation::to() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicknumberanimation.html#to
    """
    #  qreal QQuickNumberAnimation::to() const
    return self.uglySide.call('ritual_ZNK21QQuickNumberAnimation2toEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float)
  def setFrom(self, a0: float) -> None:
    """
    Calls Qt's 'void QQuickNumberAnimation::setFrom(qreal a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicknumberanimation.html#setFrom

    Parameters
    ----------

    a0 : float
      Passed on as it is.
    """
    #  void QQuickNumberAnimation::setFrom(qreal a0)
    self.uglySide.call('ritual_ZN21QQuickNumberAnimation7setFromEd', a0)

  @overload(float)
  def setTo(self, a0: float) -> None:
    """
    Calls Qt's 'void QQuickNumberAnimation::setTo(qreal a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicknumberanimation.html#setTo

    Parameters
    ----------

    a0 : float
      Passed on as it is.
    """
    #  void QQuickNumberAnimation::setTo(qreal a0)
    self.uglySide.call('ritual_ZN21QQuickNumberAnimation5setToEd', a0)

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
    'QQuickNumberAnimation::QQuickNumberAnimation(QObject *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicknumberanimation.html#QQuickNumberAnimation

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickNumberAnimation::QQuickNumberAnimation(QObject *parent)
    self._noteCreation(QQuickNumberAnimation, lambda: Rituals.call(
        'ritual_ZN21QQuickNumberAnimationC1EP7QObject',
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

  def d_func(self) -> Optional[QQuickPropertyAnimationPrivate]:
    """
    Calls Qt's 'QQuickPropertyAnimationPrivate
    *QQuickNumberAnimation::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qquicknumberanimation.html#d_func

    Returns
    -------

    Optional[QQuickPropertyAnimationPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickPropertyAnimationPrivate *QQuickNumberAnimation::d_func()
    address = self.uglySide.call('ritual_ZN21QQuickNumberAnimation6d_funcEv')
    from . import QQuickPropertyAnimationPrivate
    return QQuickPropertyAnimationPrivate._cuteAt(address)

  def init(self) -> None:
    """
    Calls Qt's 'void QQuickNumberAnimation::init()'.

    Qt's own words: https://doc.qt.io/qt-6/qquicknumberanimation.html#init
    """
    #  void QQuickNumberAnimation::init()
    self.uglySide.call('ritual_ZN21QQuickNumberAnimation4initEv')
