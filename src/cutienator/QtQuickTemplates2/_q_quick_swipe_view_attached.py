"""
QQuickSwipeViewAttached binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickswipeview_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QQuickSwipeViewAttached to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin
from ..occult import Rituals
from ..QtCore import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from . import QQuickSwipeView

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickSwipeViewAttached(QObject):
  """
  The cute side of Qt's QQuickSwipeViewAttached: a plain Python object
  standing in front of one C++ QQuickSwipeViewAttached.

  It is built on the cute 'QObject', as Qt's QQuickSwipeViewAttached is built
  on Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickSwipeViewAttached that has a ritual and that
  Python can call so far, 12 names in all: 'metaObject', 'tr', 'index',
  'isCurrentItem', 'view', 'isNextItem', 'isPreviousItem', 'indexChanged',
  'isCurrentItemChanged', 'viewChanged', 'isNextItemChanged',
  'isPreviousItemChanged'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickSwipeViewAttached::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QQuickSwipeViewAttached::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QQuickSwipeViewAttachedPrivate *QQuickSwipeViewAttached::d_func()':
    gives 'QQuickSwipeViewAttachedPrivate', which has no cute class yet.
  - Qt's 'const QQuickSwipeViewAttachedPrivate
    *QQuickSwipeViewAttached::d_func() const': gives
    'QQuickSwipeViewAttachedPrivate', which has no cute class yet.

  What has no ritual
  ------------------

  4 of the 21 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QQuickSwipeViewAttached is created at the first use, not by
    'QQuickSwipeViewAttached(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickSwipeViewAttached.
  - Qt tells when it has removed the C++ QQuickSwipeViewAttached. Every call
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
    Calls Qt's 'QString QQuickSwipeViewAttached::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickswipeviewattached.html#tr

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
    #  QString QQuickSwipeViewAttached::tr(const char *s, const char *c, int
    #      n)
    return Rituals.call(
        'ritual_ZN23QQuickSwipeViewAttached2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickSwipeViewAttached'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickSwipeViewAttached::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickswipeviewattached.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickSwipeViewAttached::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK23QQuickSwipeViewAttached10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def index(self) -> int:
    """
    Calls Qt's 'int QQuickSwipeViewAttached::index() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickswipeviewattached.html#index
    """
    #  int QQuickSwipeViewAttached::index() const
    return self.uglySide.call('ritual_ZNK23QQuickSwipeViewAttached5indexEv')

  def isCurrentItem(self) -> bool:
    """
    Calls Qt's 'bool QQuickSwipeViewAttached::isCurrentItem() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickswipeviewattached.html#isCurrentItem
    """
    #  bool QQuickSwipeViewAttached::isCurrentItem() const
    return self.uglySide.call(
        'ritual_ZNK23QQuickSwipeViewAttached13isCurrentItemEv',
    )

  def view(self) -> Optional[QQuickSwipeView]:
    """
    Calls Qt's 'QQuickSwipeView *QQuickSwipeViewAttached::view() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickswipeviewattached.html#view

    Returns
    -------

    Optional[QQuickSwipeView]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickSwipeView *QQuickSwipeViewAttached::view() const
    address = self.uglySide.call(
        'ritual_ZNK23QQuickSwipeViewAttached4viewEv',
    )
    from . import QQuickSwipeView
    return QQuickSwipeView._cuteAt(address)

  def isNextItem(self) -> bool:
    """
    Calls Qt's 'bool QQuickSwipeViewAttached::isNextItem() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickswipeviewattached.html#isNextItem
    """
    #  bool QQuickSwipeViewAttached::isNextItem() const
    return self.uglySide.call(
        'ritual_ZNK23QQuickSwipeViewAttached10isNextItemEv',
    )

  def isPreviousItem(self) -> bool:
    """
    Calls Qt's 'bool QQuickSwipeViewAttached::isPreviousItem() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickswipeviewattached.html#isPreviousItem
    """
    #  bool QQuickSwipeViewAttached::isPreviousItem() const
    return self.uglySide.call(
        'ritual_ZNK23QQuickSwipeViewAttached14isPreviousItemEv',
    )

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
    'QQuickSwipeViewAttached::QQuickSwipeViewAttached(QObject *parent)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickswipeviewattached.html

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickSwipeViewAttached::QQuickSwipeViewAttached(QObject *parent)
    self._noteCreation(QQuickSwipeViewAttached, lambda: Rituals.call(
        'ritual_ZN23QQuickSwipeViewAttachedC1EP7QObject',
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
    Calls Qt's 'void QQuickSwipeViewAttached::indexChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickswipeviewattached.html#indexChanged
    """
    #  void QQuickSwipeViewAttached::indexChanged()
    self.uglySide.call('ritual_ZN23QQuickSwipeViewAttached12indexChangedEv')

  def isCurrentItemChanged(self) -> None:
    """
    Calls Qt's 'void QQuickSwipeViewAttached::isCurrentItemChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickswipeviewattached.html#isCurrentItemChanged
    """
    #  void QQuickSwipeViewAttached::isCurrentItemChanged()
    self.uglySide.call(
        'ritual_ZN23QQuickSwipeViewAttached20isCurrentItemChangedEv',
    )

  def viewChanged(self) -> None:
    """
    Calls Qt's 'void QQuickSwipeViewAttached::viewChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickswipeviewattached.html#viewChanged
    """
    #  void QQuickSwipeViewAttached::viewChanged()
    self.uglySide.call('ritual_ZN23QQuickSwipeViewAttached11viewChangedEv')

  def isNextItemChanged(self) -> None:
    """
    Calls Qt's 'void QQuickSwipeViewAttached::isNextItemChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickswipeviewattached.html#isNextItemChanged
    """
    #  void QQuickSwipeViewAttached::isNextItemChanged()
    self.uglySide.call(
        'ritual_ZN23QQuickSwipeViewAttached17isNextItemChangedEv',
    )

  def isPreviousItemChanged(self) -> None:
    """
    Calls Qt's 'void QQuickSwipeViewAttached::isPreviousItemChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickswipeviewattached.html#isPreviousItemChanged
    """
    #  void QQuickSwipeViewAttached::isPreviousItemChanged()
    self.uglySide.call(
        'ritual_ZN23QQuickSwipeViewAttached21isPreviousItemChangedEv',
    )
