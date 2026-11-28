"""
QQuickTabBarAttached binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquicktabbar_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QQuickTabBarAttached to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin
from ..occult import Rituals
from ..QtCore import QObject
from . import QQuickTabBar

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickTabBarAttached(QObject):
  """
  The cute side of Qt's QQuickTabBarAttached: a plain Python object standing
  in front of one C++ QQuickTabBarAttached.

  It is built on the cute 'QObject', as Qt's QQuickTabBarAttached is built on
  Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickTabBarAttached that has a ritual and that
  Python can call so far, 8 names in all: 'metaObject', 'tr', 'index',
  'tabBar', 'position', 'indexChanged', 'tabBarChanged', 'positionChanged'.
  It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickTabBarAttached::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QQuickTabBarAttached::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QQuickTabBarAttachedPrivate *QQuickTabBarAttached::d_func()': gives
    'QQuickTabBarAttachedPrivate', which has no cute class yet.
  - Qt's 'const QQuickTabBarAttachedPrivate *QQuickTabBarAttached::d_func()
    const': gives 'QQuickTabBarAttachedPrivate', which has no cute class yet.

  What has no ritual
  ------------------

  4 of the 17 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QQuickTabBarAttached is created at the first use, not by
    'QQuickTabBarAttached(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickTabBarAttached.
  - Qt tells when it has removed the C++ QQuickTabBarAttached. Every call on
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
    Calls Qt's 'QString QQuickTabBarAttached::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktabbarattached.html#tr

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
    #  QString QQuickTabBarAttached::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN20QQuickTabBarAttached2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickTabBarAttached'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickTabBarAttached::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktabbarattached.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickTabBarAttached::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK20QQuickTabBarAttached10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def index(self) -> int:
    """
    Calls Qt's 'int QQuickTabBarAttached::index() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktabbarattached.html#index
    """
    #  int QQuickTabBarAttached::index() const
    return self.uglySide.call('ritual_ZNK20QQuickTabBarAttached5indexEv')

  def tabBar(self) -> Optional[QQuickTabBar]:
    """
    Calls Qt's 'QQuickTabBar *QQuickTabBarAttached::tabBar() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktabbarattached.html#tabBar

    Returns
    -------

    Optional[QQuickTabBar]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickTabBar *QQuickTabBarAttached::tabBar() const
    address = self.uglySide.call('ritual_ZNK20QQuickTabBarAttached6tabBarEv')
    return QQuickTabBar._cuteAt(address)

  def position(self) -> QQuickTabBar.Position:
    """
    Calls Qt's 'QQuickTabBar::Position QQuickTabBarAttached::position()
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktabbarattached.html#position

    Returns
    -------

    QQuickTabBar.Position
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QQuickTabBar.Position(number)' gives.
    """
    #  QQuickTabBar::Position QQuickTabBarAttached::position() const
    return QQuickTabBar.Position(self.uglySide.call(
        'ritual_ZNK20QQuickTabBarAttached8positionEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

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
    'QQuickTabBarAttached::QQuickTabBarAttached(QObject *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktabbarattached.html#QQuickTabBarAttached

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickTabBarAttached::QQuickTabBarAttached(QObject *parent)
    self._noteCreation(QQuickTabBarAttached, lambda: Rituals.call(
        'ritual_ZN20QQuickTabBarAttachedC1EP7QObject',
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

  def indexChanged(self) -> None:
    """
    Calls Qt's 'void QQuickTabBarAttached::indexChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktabbarattached.html#indexChanged
    """
    #  void QQuickTabBarAttached::indexChanged()
    self.uglySide.call('ritual_ZN20QQuickTabBarAttached12indexChangedEv')

  def tabBarChanged(self) -> None:
    """
    Calls Qt's 'void QQuickTabBarAttached::tabBarChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktabbarattached.html#tabBarChanged
    """
    #  void QQuickTabBarAttached::tabBarChanged()
    self.uglySide.call('ritual_ZN20QQuickTabBarAttached13tabBarChangedEv')

  def positionChanged(self) -> None:
    """
    Calls Qt's 'void QQuickTabBarAttached::positionChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktabbarattached.html#positionChanged
    """
    #  void QQuickTabBarAttached::positionChanged()
    self.uglySide.call('ritual_ZN20QQuickTabBarAttached15positionChangedEv')
