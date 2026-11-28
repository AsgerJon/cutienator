"""
QQuickStackViewAttached binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickstackview_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QQuickStackViewAttached to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin
from ..occult import Rituals
from ..QtCore import QObject
from . import QQuickStackView

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from . import QQuickStackViewAttachedPrivate

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickStackViewAttached(QObject):
  """
  The cute side of Qt's QQuickStackViewAttached: a plain Python object
  standing in front of one C++ QQuickStackViewAttached.

  It is built on the cute 'QObject', as Qt's QQuickStackViewAttached is built
  on Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickStackViewAttached that has a ritual and that
  Python can call so far, 18 names in all: 'metaObject', 'tr', 'index',
  'view', 'status', 'isVisible', 'setVisible', 'resetVisible',
  'indexChanged', 'viewChanged', 'statusChanged', 'activated', 'activating',
  'deactivated', 'deactivating', 'removed', 'visibleChanged', 'd_func'. It
  can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickStackViewAttached::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QQuickStackViewAttached::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QQuickStackViewAttached::~QQuickStackViewAttached()': the
    destructor: Python never removes a C++ QQuickStackViewAttached.
  - Qt's 'const QQuickStackViewAttachedPrivate
    *QQuickStackViewAttached::d_func() const': takes in Python what
    'QQuickStackViewAttachedPrivate *QQuickStackViewAttached::d_func()'
    takes.

  What has no ritual
  ------------------

  4 of the 27 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QQuickStackViewAttached is created at the first use, not by
    'QQuickStackViewAttached(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickStackViewAttached.
  - Qt tells when it has removed the C++ QQuickStackViewAttached. Every call
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
    Calls Qt's 'QString QQuickStackViewAttached::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickstackviewattached.html#tr

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
    #  QString QQuickStackViewAttached::tr(const char *s, const char *c, int
    #      n)
    return Rituals.call(
        'ritual_ZN23QQuickStackViewAttached2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickStackViewAttached'

  #  A C++ QQuickStackViewAttached Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickStackViewAttached'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickStackViewAttached::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickstackviewattached.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickStackViewAttached::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK23QQuickStackViewAttached10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def index(self) -> int:
    """
    Calls Qt's 'int QQuickStackViewAttached::index() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickstackviewattached.html#index
    """
    #  int QQuickStackViewAttached::index() const
    return self.uglySide.call('ritual_ZNK23QQuickStackViewAttached5indexEv')

  def view(self) -> Optional[QQuickStackView]:
    """
    Calls Qt's 'QQuickStackView *QQuickStackViewAttached::view() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickstackviewattached.html#view

    Returns
    -------

    Optional[QQuickStackView]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickStackView *QQuickStackViewAttached::view() const
    address = self.uglySide.call(
        'ritual_ZNK23QQuickStackViewAttached4viewEv',
    )
    return QQuickStackView._cuteAt(address)

  def status(self) -> QQuickStackView.Status:
    """
    Calls Qt's 'QQuickStackView::Status QQuickStackViewAttached::status()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickstackviewattached.html#status

    Returns
    -------

    QQuickStackView.Status
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QQuickStackView.Status(number)' gives.
    """
    #  QQuickStackView::Status QQuickStackViewAttached::status() const
    return QQuickStackView.Status(self.uglySide.call(
        'ritual_ZNK23QQuickStackViewAttached6statusEv',
    ))

  def isVisible(self) -> bool:
    """
    Calls Qt's 'bool QQuickStackViewAttached::isVisible() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickstackviewattached.html#isVisible
    """
    #  bool QQuickStackViewAttached::isVisible() const
    return self.uglySide.call(
        'ritual_ZNK23QQuickStackViewAttached9isVisibleEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  def setVisible(self, visible: bool) -> None:
    """
    Calls Qt's 'void QQuickStackViewAttached::setVisible(bool visible)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickstackviewattached.html#setVisible

    Parameters
    ----------

    visible : bool
      Passed on as it is.
    """
    #  void QQuickStackViewAttached::setVisible(bool visible)
    self.uglySide.call(
        'ritual_ZN23QQuickStackViewAttached10setVisibleEb', visible,
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
    'QQuickStackViewAttached::QQuickStackViewAttached(QObject *parent)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickstackviewattached.html

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickStackViewAttached::QQuickStackViewAttached(QObject *parent)
    self._noteCreation(QQuickStackViewAttached, lambda: Rituals.call(
        'ritual_ZN23QQuickStackViewAttachedC1EP7QObject',
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

  def resetVisible(self) -> None:
    """
    Calls Qt's 'void QQuickStackViewAttached::resetVisible()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickstackviewattached.html#resetVisible
    """
    #  void QQuickStackViewAttached::resetVisible()
    self.uglySide.call('ritual_ZN23QQuickStackViewAttached12resetVisibleEv')

  def indexChanged(self) -> None:
    """
    Calls Qt's 'void QQuickStackViewAttached::indexChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickstackviewattached.html#indexChanged
    """
    #  void QQuickStackViewAttached::indexChanged()
    self.uglySide.call('ritual_ZN23QQuickStackViewAttached12indexChangedEv')

  def viewChanged(self) -> None:
    """
    Calls Qt's 'void QQuickStackViewAttached::viewChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickstackviewattached.html#viewChanged
    """
    #  void QQuickStackViewAttached::viewChanged()
    self.uglySide.call('ritual_ZN23QQuickStackViewAttached11viewChangedEv')

  def statusChanged(self) -> None:
    """
    Calls Qt's 'void QQuickStackViewAttached::statusChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickstackviewattached.html#statusChanged
    """
    #  void QQuickStackViewAttached::statusChanged()
    self.uglySide.call('ritual_ZN23QQuickStackViewAttached13statusChangedEv')

  def activated(self) -> None:
    """
    Calls Qt's 'void QQuickStackViewAttached::activated()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickstackviewattached.html#activated
    """
    #  void QQuickStackViewAttached::activated()
    self.uglySide.call('ritual_ZN23QQuickStackViewAttached9activatedEv')

  def activating(self) -> None:
    """
    Calls Qt's 'void QQuickStackViewAttached::activating()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickstackviewattached.html#activating
    """
    #  void QQuickStackViewAttached::activating()
    self.uglySide.call('ritual_ZN23QQuickStackViewAttached10activatingEv')

  def deactivated(self) -> None:
    """
    Calls Qt's 'void QQuickStackViewAttached::deactivated()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickstackviewattached.html#deactivated
    """
    #  void QQuickStackViewAttached::deactivated()
    self.uglySide.call('ritual_ZN23QQuickStackViewAttached11deactivatedEv')

  def deactivating(self) -> None:
    """
    Calls Qt's 'void QQuickStackViewAttached::deactivating()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickstackviewattached.html#deactivating
    """
    #  void QQuickStackViewAttached::deactivating()
    self.uglySide.call('ritual_ZN23QQuickStackViewAttached12deactivatingEv')

  def removed(self) -> None:
    """
    Calls Qt's 'void QQuickStackViewAttached::removed()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickstackviewattached.html#removed
    """
    #  void QQuickStackViewAttached::removed()
    self.uglySide.call('ritual_ZN23QQuickStackViewAttached7removedEv')

  def visibleChanged(self) -> None:
    """
    Calls Qt's 'void QQuickStackViewAttached::visibleChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickstackviewattached.html#visibleChanged
    """
    #  void QQuickStackViewAttached::visibleChanged()
    self.uglySide.call(
        'ritual_ZN23QQuickStackViewAttached14visibleChangedEv',
    )

  def d_func(self) -> Optional[QQuickStackViewAttachedPrivate]:
    """
    Calls Qt's 'QQuickStackViewAttachedPrivate
    *QQuickStackViewAttached::d_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickstackviewattached.html#d_func

    Returns
    -------

    Optional[QQuickStackViewAttachedPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickStackViewAttachedPrivate *QQuickStackViewAttached::d_func()
    address = self.uglySide.call(
        'ritual_ZN23QQuickStackViewAttached6d_funcEv',
    )
    from . import QQuickStackViewAttachedPrivate
    return QQuickStackViewAttachedPrivate._cuteAt(address)
