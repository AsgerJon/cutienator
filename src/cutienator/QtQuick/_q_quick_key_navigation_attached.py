"""
QQuickKeyNavigationAttached binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquickitem_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QQuickKeyNavigationAttached to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import Qt, QObject
from . import QQuickItemKeyFilter

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from ..QtGui import QKeyEvent
  from . import QQuickItem, QQuickKeyNavigationAttachedPrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QKeyEvent = WAIT['QKeyEvent']
  QQuickItem = WAIT['QQuickItem']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickKeyNavigationAttached(QObject, QQuickItemKeyFilter):
  """
  The cute side of Qt's QQuickKeyNavigationAttached: a plain Python object
  standing in front of one C++ QQuickKeyNavigationAttached.

  It is built on the cute 'QObject', as Qt's QQuickKeyNavigationAttached is
  built on Qt's QObject, and has everything that class has. It is built on
  the cute 'QQuickItemKeyFilter' as well, as Qt's QQuickKeyNavigationAttached
  is built on Qt's QQuickItemKeyFilter too, and has everything that class
  has.

  What exists
  -----------

  Every function of Qt's QQuickKeyNavigationAttached that has a ritual and
  that Python can call so far, 28 names in all: 'metaObject', 'tr', 'd_func',
  'left', 'setLeft', 'right', 'setRight', 'up', 'setUp', 'down', 'setDown',
  'tab', 'setTab', 'backtab', 'setBacktab', 'priority', 'setPriority',
  'qmlAttachedProperties', 'leftChanged', 'rightChanged', 'upChanged',
  'downChanged', 'tabChanged', 'backtabChanged', 'priorityChanged',
  'keyPressed', 'keyReleased', 'setFocusNavigation'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickKeyNavigationAttached::qt_metacast(const char *a0)':
    one of Qt's own inner workings.
  - Qt's 'int QQuickKeyNavigationAttached::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'const QQuickKeyNavigationAttachedPrivate
    *QQuickKeyNavigationAttached::d_func() const': takes in Python what
    'QQuickKeyNavigationAttachedPrivate
    *QQuickKeyNavigationAttached::d_func()' takes.
  - Qt's 'void QQuickKeyNavigationAttached::qt_qmlMarker_uncreatable()': one
    of Qt's own inner workings.
  - Qt's 'void QQuickKeyNavigationAttached::qt_qmlMarker_attached()': one of
    Qt's own inner workings.

  What has no ritual
  ------------------

  2 of the 36 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuickKeyNavigationAttached is created at the first use, not by
    'QQuickKeyNavigationAttached(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickKeyNavigationAttached.
  - Qt tells when it has removed the C++ QQuickKeyNavigationAttached. Every
    call on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  #  The enums Qt writes inside QQuickKeyNavigationAttached, each a class in
  #  here as in C++, and the names Qt has for the combinations of its flags
  #  enums.

  class Priority(CuteNum):
    """
    The enum 'QQuickKeyNavigationAttached::Priority' of Qt, with the 2 names
    Qt gives in it.
    """

    BeforeItem = Kee[int](0)
    AfterItem = Kee[int](1)

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
    Calls Qt's 'QString QQuickKeyNavigationAttached::tr(const char *s, const
    char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickkeynavigationattached.html#tr

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
    #  QString QQuickKeyNavigationAttached::tr(const char *s, const char *c,
    #      int n)
    return Rituals.call(
        'ritual_ZN27QQuickKeyNavigationAttached2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  @overload(QObject)
  @overload(NoneType)
  def qmlAttachedProperties(
      a0: Optional[QObject],
  ) -> Optional[QQuickKeyNavigationAttached]:
    """
    Calls Qt's 'QQuickKeyNavigationAttached
    *QQuickKeyNavigationAttached::qmlAttachedProperties(QObject *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickkeynavigationattached.html

    Parameters
    ----------

    a0 : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QQuickKeyNavigationAttached]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickKeyNavigationAttached
    #      *QQuickKeyNavigationAttached::qmlAttachedProperties(QObject *a0)
    address = Rituals.call(
        'ritual_ZN27QQuickKeyNavigationAttached21qmlAttachedPropertiesEP7QO'
        'bject',
        CuteMixin._addressOf(a0, 'QObject'),
    )
    return QQuickKeyNavigationAttached._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickKeyNavigationAttached'

  #  Qt's QQuickKeyNavigationAttached is built on more than one class. The
  #  part of a C++ QQuickKeyNavigationAttached that belongs to a class after
  #  the first begins somewhere inside the object, and the ritual named for
  #  that class gives where; see 'CuteMixin._addressAs'.
  __cast_rituals__ = {
      'QQuickItemKeyFilter':
          'ritual_cast_QQuickKeyNavigationAttached_QQuickItemKeyFilter',
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickKeyNavigationAttached::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickkeynavigationattached.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickKeyNavigationAttached::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK27QQuickKeyNavigationAttached10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def left(self) -> Optional[QQuickItem]:
    """
    Calls Qt's 'QQuickItem *QQuickKeyNavigationAttached::left() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickkeynavigationattached.html#left

    Returns
    -------

    Optional[QQuickItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickItem *QQuickKeyNavigationAttached::left() const
    address = self.uglySide.call(
        'ritual_ZNK27QQuickKeyNavigationAttached4leftEv',
    )
    from . import QQuickItem
    return QQuickItem._cuteAt(address)

  def right(self) -> Optional[QQuickItem]:
    """
    Calls Qt's 'QQuickItem *QQuickKeyNavigationAttached::right() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickkeynavigationattached.html#right

    Returns
    -------

    Optional[QQuickItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickItem *QQuickKeyNavigationAttached::right() const
    address = self.uglySide.call(
        'ritual_ZNK27QQuickKeyNavigationAttached5rightEv',
    )
    from . import QQuickItem
    return QQuickItem._cuteAt(address)

  def up(self) -> Optional[QQuickItem]:
    """
    Calls Qt's 'QQuickItem *QQuickKeyNavigationAttached::up() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickkeynavigationattached.html#up

    Returns
    -------

    Optional[QQuickItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickItem *QQuickKeyNavigationAttached::up() const
    address = self.uglySide.call(
        'ritual_ZNK27QQuickKeyNavigationAttached2upEv',
    )
    from . import QQuickItem
    return QQuickItem._cuteAt(address)

  def down(self) -> Optional[QQuickItem]:
    """
    Calls Qt's 'QQuickItem *QQuickKeyNavigationAttached::down() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickkeynavigationattached.html#down

    Returns
    -------

    Optional[QQuickItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickItem *QQuickKeyNavigationAttached::down() const
    address = self.uglySide.call(
        'ritual_ZNK27QQuickKeyNavigationAttached4downEv',
    )
    from . import QQuickItem
    return QQuickItem._cuteAt(address)

  def tab(self) -> Optional[QQuickItem]:
    """
    Calls Qt's 'QQuickItem *QQuickKeyNavigationAttached::tab() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickkeynavigationattached.html#tab

    Returns
    -------

    Optional[QQuickItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickItem *QQuickKeyNavigationAttached::tab() const
    address = self.uglySide.call(
        'ritual_ZNK27QQuickKeyNavigationAttached3tabEv',
    )
    from . import QQuickItem
    return QQuickItem._cuteAt(address)

  def backtab(self) -> Optional[QQuickItem]:
    """
    Calls Qt's 'QQuickItem *QQuickKeyNavigationAttached::backtab() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickkeynavigationattached.html#backtab

    Returns
    -------

    Optional[QQuickItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickItem *QQuickKeyNavigationAttached::backtab() const
    address = self.uglySide.call(
        'ritual_ZNK27QQuickKeyNavigationAttached7backtabEv',
    )
    from . import QQuickItem
    return QQuickItem._cuteAt(address)

  def priority(self) -> Priority:
    """
    Calls Qt's 'Priority QQuickKeyNavigationAttached::priority() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickkeynavigationattached.html#priority

    Returns
    -------

    Priority
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Priority(number)' gives.
    """
    #  Priority QQuickKeyNavigationAttached::priority() const
    return QQuickKeyNavigationAttached.Priority(self.uglySide.call(
        'ritual_ZNK27QQuickKeyNavigationAttached8priorityEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QQuickItem)
  @overload(NoneType)
  def setLeft(self, a0: Optional[QQuickItem]) -> None:
    """
    Calls Qt's 'void QQuickKeyNavigationAttached::setLeft(QQuickItem *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickkeynavigationattached.html#setLeft

    Parameters
    ----------

    a0 : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickKeyNavigationAttached::setLeft(QQuickItem *a0)
    self.uglySide.call(
        'ritual_ZN27QQuickKeyNavigationAttached7setLeftEP10QQuickItem',
        self._addressOf(a0),
    )

  @overload(QQuickItem)
  @overload(NoneType)
  def setRight(self, a0: Optional[QQuickItem]) -> None:
    """
    Calls Qt's 'void QQuickKeyNavigationAttached::setRight(QQuickItem *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickkeynavigationattached.html#setRight

    Parameters
    ----------

    a0 : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickKeyNavigationAttached::setRight(QQuickItem *a0)
    self.uglySide.call(
        'ritual_ZN27QQuickKeyNavigationAttached8setRightEP10QQuickItem',
        self._addressOf(a0),
    )

  @overload(QQuickItem)
  @overload(NoneType)
  def setUp(self, a0: Optional[QQuickItem]) -> None:
    """
    Calls Qt's 'void QQuickKeyNavigationAttached::setUp(QQuickItem *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickkeynavigationattached.html#setUp

    Parameters
    ----------

    a0 : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickKeyNavigationAttached::setUp(QQuickItem *a0)
    self.uglySide.call(
        'ritual_ZN27QQuickKeyNavigationAttached5setUpEP10QQuickItem',
        self._addressOf(a0),
    )

  @overload(QQuickItem)
  @overload(NoneType)
  def setDown(self, a0: Optional[QQuickItem]) -> None:
    """
    Calls Qt's 'void QQuickKeyNavigationAttached::setDown(QQuickItem *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickkeynavigationattached.html#setDown

    Parameters
    ----------

    a0 : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickKeyNavigationAttached::setDown(QQuickItem *a0)
    self.uglySide.call(
        'ritual_ZN27QQuickKeyNavigationAttached7setDownEP10QQuickItem',
        self._addressOf(a0),
    )

  @overload(QQuickItem)
  @overload(NoneType)
  def setTab(self, a0: Optional[QQuickItem]) -> None:
    """
    Calls Qt's 'void QQuickKeyNavigationAttached::setTab(QQuickItem *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickkeynavigationattached.html#setTab

    Parameters
    ----------

    a0 : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickKeyNavigationAttached::setTab(QQuickItem *a0)
    self.uglySide.call(
        'ritual_ZN27QQuickKeyNavigationAttached6setTabEP10QQuickItem',
        self._addressOf(a0),
    )

  @overload(QQuickItem)
  @overload(NoneType)
  def setBacktab(self, a0: Optional[QQuickItem]) -> None:
    """
    Calls Qt's 'void QQuickKeyNavigationAttached::setBacktab(QQuickItem
    *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickkeynavigationattached.html#setBacktab

    Parameters
    ----------

    a0 : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickKeyNavigationAttached::setBacktab(QQuickItem *a0)
    self.uglySide.call(
        'ritual_ZN27QQuickKeyNavigationAttached10setBacktabEP10QQuickItem',
        self._addressOf(a0),
    )

  @overload(Priority)
  def setPriority(self, a0: Priority) -> None:
    """
    Calls Qt's 'void QQuickKeyNavigationAttached::setPriority(Priority a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickkeynavigationattached.html#setPriority

    Parameters
    ----------

    a0 : Priority
      Passed on as its number.
    """
    #  void QQuickKeyNavigationAttached::setPriority(Priority a0)
    self.uglySide.call(
        'ritual_ZN27QQuickKeyNavigationAttached11setPriorityENS_8PriorityE',
        a0.value,
    )

  @overload(QQuickItem, str)
  @overload(QQuickItem, NoneType)
  @overload(NoneType, str)
  @overload(NoneType, NoneType)
  @overload(QQuickItem, str, Qt.FocusReason)
  @overload(QQuickItem, NoneType, Qt.FocusReason)
  @overload(NoneType, str, Qt.FocusReason)
  @overload(NoneType, NoneType, Qt.FocusReason)
  def setFocusNavigation(
      self,
      currentItem: Optional[QQuickItem],
      dir: Optional[str],
      reason: Qt.FocusReason = Qt.FocusReason.OtherFocusReason,
  ) -> None:
    """
    Calls Qt's 'void
    QQuickKeyNavigationAttached::setFocusNavigation(QQuickItem *currentItem,
    const char *dir, Qt::FocusReason reason)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickkeynavigationattached.html

    Parameters
    ----------

    currentItem : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    dir : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    reason : Qt.FocusReason
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.FocusReason.OtherFocusReason.
    """
    #  void QQuickKeyNavigationAttached::setFocusNavigation(QQuickItem
    #      *currentItem, const char *dir, Qt::FocusReason reason)
    self.uglySide.call(
        'ritual_ZN27QQuickKeyNavigationAttached18setFocusNavigationEP10QQui'
        'ckItemPKcN2Qt11FocusReasonE',
        self._addressOf(currentItem), self._bytesOf(dir), reason.value,
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
  def __init__(self, a0: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's
    'QQuickKeyNavigationAttached::QQuickKeyNavigationAttached(QObject *a0)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickkeynavigationattached.html

    Parameters
    ----------

    a0 : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickKeyNavigationAttached::QQuickKeyNavigationAttached(QObject *a0)
    self._noteCreation(QQuickKeyNavigationAttached, lambda: Rituals.call(
        'ritual_ZN27QQuickKeyNavigationAttachedC1EP7QObject',
        self._addressOf(a0, 'QObject'),
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

  def d_func(self) -> Optional[QQuickKeyNavigationAttachedPrivate]:
    """
    Calls Qt's 'QQuickKeyNavigationAttachedPrivate
    *QQuickKeyNavigationAttached::d_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickkeynavigationattached.html#d_func

    Returns
    -------

    Optional[QQuickKeyNavigationAttachedPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickKeyNavigationAttachedPrivate
    #      *QQuickKeyNavigationAttached::d_func()
    address = self.uglySide.call(
        'ritual_ZN27QQuickKeyNavigationAttached6d_funcEv',
    )
    from . import QQuickKeyNavigationAttachedPrivate
    return QQuickKeyNavigationAttachedPrivate._cuteAt(address)

  def leftChanged(self) -> None:
    """
    Calls Qt's 'void QQuickKeyNavigationAttached::leftChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickkeynavigationattached.html#leftChanged
    """
    #  void QQuickKeyNavigationAttached::leftChanged()
    self.uglySide.call(
        'ritual_ZN27QQuickKeyNavigationAttached11leftChangedEv',
    )

  def rightChanged(self) -> None:
    """
    Calls Qt's 'void QQuickKeyNavigationAttached::rightChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickkeynavigationattached.html#rightChanged
    """
    #  void QQuickKeyNavigationAttached::rightChanged()
    self.uglySide.call(
        'ritual_ZN27QQuickKeyNavigationAttached12rightChangedEv',
    )

  def upChanged(self) -> None:
    """
    Calls Qt's 'void QQuickKeyNavigationAttached::upChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickkeynavigationattached.html#upChanged
    """
    #  void QQuickKeyNavigationAttached::upChanged()
    self.uglySide.call('ritual_ZN27QQuickKeyNavigationAttached9upChangedEv')

  def downChanged(self) -> None:
    """
    Calls Qt's 'void QQuickKeyNavigationAttached::downChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickkeynavigationattached.html#downChanged
    """
    #  void QQuickKeyNavigationAttached::downChanged()
    self.uglySide.call(
        'ritual_ZN27QQuickKeyNavigationAttached11downChangedEv',
    )

  def tabChanged(self) -> None:
    """
    Calls Qt's 'void QQuickKeyNavigationAttached::tabChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickkeynavigationattached.html#tabChanged
    """
    #  void QQuickKeyNavigationAttached::tabChanged()
    self.uglySide.call(
        'ritual_ZN27QQuickKeyNavigationAttached10tabChangedEv',
    )

  def backtabChanged(self) -> None:
    """
    Calls Qt's 'void QQuickKeyNavigationAttached::backtabChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickkeynavigationattached.html#backtabChanged
    """
    #  void QQuickKeyNavigationAttached::backtabChanged()
    self.uglySide.call(
        'ritual_ZN27QQuickKeyNavigationAttached14backtabChangedEv',
    )

  def priorityChanged(self) -> None:
    """
    Calls Qt's 'void QQuickKeyNavigationAttached::priorityChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickkeynavigationattached.html#priorityChanged
    """
    #  void QQuickKeyNavigationAttached::priorityChanged()
    self.uglySide.call(
        'ritual_ZN27QQuickKeyNavigationAttached15priorityChangedEv',
    )

  @overload(QKeyEvent, bool)
  @overload(NoneType, bool)
  def keyPressed(self, event: Optional[QKeyEvent], post: bool) -> None:
    """
    Calls Qt's 'void QQuickKeyNavigationAttached::keyPressed(QKeyEvent
    *event, bool post)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickkeynavigationattached.html#keyPressed

    Parameters
    ----------

    event : Optional[QKeyEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    post : bool
      Passed on as it is.
    """
    #  void QQuickKeyNavigationAttached::keyPressed(QKeyEvent *event, bool
    #      post)
    ritual = (
        'ritual_ZN27QQuickKeyNavigationAttached10keyPressedEP9QKeyEventb')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN27QQuickKeyNavigationAttached10keyPressedEP9QKeyEve'
          'ntb')
    self.uglySide.call(ritual, self._addressOf(event), post)

  @overload(QKeyEvent, bool)
  @overload(NoneType, bool)
  def keyReleased(self, event: Optional[QKeyEvent], post: bool) -> None:
    """
    Calls Qt's 'void QQuickKeyNavigationAttached::keyReleased(QKeyEvent
    *event, bool post)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickkeynavigationattached.html#keyReleased

    Parameters
    ----------

    event : Optional[QKeyEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    post : bool
      Passed on as it is.
    """
    #  void QQuickKeyNavigationAttached::keyReleased(QKeyEvent *event, bool
    #      post)
    ritual = (
        'ritual_ZN27QQuickKeyNavigationAttached11keyReleasedEP9QKeyEventb')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN27QQuickKeyNavigationAttached11keyReleasedEP9QKeyEv'
          'entb')
    self.uglySide.call(ritual, self._addressOf(event), post)
