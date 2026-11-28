"""
QQuickSwipeDelegateAttached binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickswipedelegate_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuickSwipeDelegateAttached to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin
from ..occult import Rituals
from ..QtCore import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickSwipeDelegateAttached(QObject):
  """
  The cute side of Qt's QQuickSwipeDelegateAttached: a plain Python object
  standing in front of one C++ QQuickSwipeDelegateAttached.

  It is built on the cute 'QObject', as Qt's QQuickSwipeDelegateAttached is
  built on Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickSwipeDelegateAttached that has a ritual and
  that Python can call so far, 6 names in all: 'metaObject', 'tr',
  'isPressed', 'setPressed', 'pressedChanged', 'clicked'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickSwipeDelegateAttached::qt_metacast(const char *a0)':
    one of Qt's own inner workings.
  - Qt's 'int QQuickSwipeDelegateAttached::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QQuickSwipeDelegateAttachedPrivate
    *QQuickSwipeDelegateAttached::d_func()': gives
    'QQuickSwipeDelegateAttachedPrivate', which has no cute class yet.
  - Qt's 'const QQuickSwipeDelegateAttachedPrivate
    *QQuickSwipeDelegateAttached::d_func() const': gives
    'QQuickSwipeDelegateAttachedPrivate', which has no cute class yet.

  What has no ritual
  ------------------

  4 of the 15 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QQuickSwipeDelegateAttached is created at the first use, not by
    'QQuickSwipeDelegateAttached(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickSwipeDelegateAttached.
  - Qt tells when it has removed the C++ QQuickSwipeDelegateAttached. Every
    call on the cute object, and every use of it as an argument, then raises
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
    Calls Qt's 'QString QQuickSwipeDelegateAttached::tr(const char *s, const
    char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickswipedelegateattached.html#tr

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
    #  QString QQuickSwipeDelegateAttached::tr(const char *s, const char *c,
    #      int n)
    return Rituals.call(
        'ritual_ZN27QQuickSwipeDelegateAttached2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickSwipeDelegateAttached'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickSwipeDelegateAttached::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickswipedelegateattached.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickSwipeDelegateAttached::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK27QQuickSwipeDelegateAttached10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def isPressed(self) -> bool:
    """
    Calls Qt's 'bool QQuickSwipeDelegateAttached::isPressed() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickswipedelegateattached.html#isPressed
    """
    #  bool QQuickSwipeDelegateAttached::isPressed() const
    return self.uglySide.call(
        'ritual_ZNK27QQuickSwipeDelegateAttached9isPressedEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  def setPressed(self, pressed: bool) -> None:
    """
    Calls Qt's 'void QQuickSwipeDelegateAttached::setPressed(bool pressed)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickswipedelegateattached.html#setPressed

    Parameters
    ----------

    pressed : bool
      Passed on as it is.
    """
    #  void QQuickSwipeDelegateAttached::setPressed(bool pressed)
    self.uglySide.call(
        'ritual_ZN27QQuickSwipeDelegateAttached10setPressedEb', pressed,
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
  def __init__(self, object: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's
    'QQuickSwipeDelegateAttached::QQuickSwipeDelegateAttached(QObject
    *object)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickswipedelegateattached.html

    Parameters
    ----------

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickSwipeDelegateAttached::QQuickSwipeDelegateAttached(QObject
    #      *object)
    self._noteCreation(QQuickSwipeDelegateAttached, lambda: Rituals.call(
        'ritual_ZN27QQuickSwipeDelegateAttachedC1EP7QObject',
        self._addressOf(object, 'QObject'),
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

  def pressedChanged(self) -> None:
    """
    Calls Qt's 'void QQuickSwipeDelegateAttached::pressedChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickswipedelegateattached.html#pressedChanged
    """
    #  void QQuickSwipeDelegateAttached::pressedChanged()
    self.uglySide.call(
        'ritual_ZN27QQuickSwipeDelegateAttached14pressedChangedEv',
    )

  def clicked(self) -> None:
    """
    Calls Qt's 'void QQuickSwipeDelegateAttached::clicked()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickswipedelegateattached.html#clicked
    """
    #  void QQuickSwipeDelegateAttached::clicked()
    self.uglySide.call('ritual_ZN27QQuickSwipeDelegateAttached7clickedEv')
