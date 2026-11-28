"""
QQuickColorAnimation binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquickanimation_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QQuickColorAnimation to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject
from . import QQuickPropertyAnimation

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from ..QtGui import QColor
  from . import QQuickPropertyAnimationPrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QColor = WAIT['QColor']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickColorAnimation(QQuickPropertyAnimation):
  """
  The cute side of Qt's QQuickColorAnimation: a plain Python object standing
  in front of one C++ QQuickColorAnimation.

  It is built on the cute 'QQuickPropertyAnimation', as Qt's
  QQuickColorAnimation is built on Qt's QQuickPropertyAnimation, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickColorAnimation that has a ritual and that
  Python can call so far, 7 names in all: 'metaObject', 'tr', 'd_func',
  'from_', 'setFrom', 'to', 'setTo'. It can be made from Python, in 1 way;
  see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickColorAnimation::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QQuickColorAnimation::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'const QQuickPropertyAnimationPrivate
    *QQuickColorAnimation::d_func() const': takes in Python what
    'QQuickPropertyAnimationPrivate *QQuickColorAnimation::d_func()' takes.
  - Qt's 'QQuickColorAnimation::~QQuickColorAnimation()': the destructor:
    Python never removes a C++ QQuickColorAnimation.

  What has no ritual
  ------------------

  2 of the 14 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuickColorAnimation is created at the first use, not by
    'QQuickColorAnimation(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickColorAnimation.
  - Qt tells when it has removed the C++ QQuickColorAnimation. Every call on
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
    Calls Qt's 'QString QQuickColorAnimation::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcoloranimation.html#tr

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
    #  QString QQuickColorAnimation::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN20QQuickColorAnimation2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickColorAnimation'

  #  A C++ QQuickColorAnimation Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickColorAnimation'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickColorAnimation::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcoloranimation.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickColorAnimation::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK20QQuickColorAnimation10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def from_(self) -> QColor:
    """
    Calls Qt's 'QColor QQuickColorAnimation::from() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcoloranimation.html#from

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QQuickColorAnimation::from() const
    address = self.uglySide.call('ritual_ZNK20QQuickColorAnimation4fromEv')
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def to(self) -> QColor:
    """
    Calls Qt's 'QColor QQuickColorAnimation::to() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcoloranimation.html#to

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QQuickColorAnimation::to() const
    address = self.uglySide.call('ritual_ZNK20QQuickColorAnimation2toEv')
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QColor)
  def setFrom(self, a0: QColor) -> None:
    """
    Calls Qt's 'void QQuickColorAnimation::setFrom(const QColor &a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcoloranimation.html#setFrom

    Parameters
    ----------

    a0 : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QQuickColorAnimation::setFrom(const QColor &a0)
    self.uglySide.call(
        'ritual_ZN20QQuickColorAnimation7setFromERK6QColor',
        self._valueOf(a0),
    )

  @overload(QColor)
  def setTo(self, a0: QColor) -> None:
    """
    Calls Qt's 'void QQuickColorAnimation::setTo(const QColor &a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcoloranimation.html#setTo

    Parameters
    ----------

    a0 : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QQuickColorAnimation::setTo(const QColor &a0)
    self.uglySide.call(
        'ritual_ZN20QQuickColorAnimation5setToERK6QColor', self._valueOf(a0),
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
    'QQuickColorAnimation::QQuickColorAnimation(QObject *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcoloranimation.html#QQuickColorAnimation

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickColorAnimation::QQuickColorAnimation(QObject *parent)
    self._noteCreation(QQuickColorAnimation, lambda: Rituals.call(
        'ritual_ZN20QQuickColorAnimationC1EP7QObject',
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
    *QQuickColorAnimation::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcoloranimation.html#d_func

    Returns
    -------

    Optional[QQuickPropertyAnimationPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickPropertyAnimationPrivate *QQuickColorAnimation::d_func()
    address = self.uglySide.call('ritual_ZN20QQuickColorAnimation6d_funcEv')
    from . import QQuickPropertyAnimationPrivate
    return QQuickPropertyAnimationPrivate._cuteAt(address)
