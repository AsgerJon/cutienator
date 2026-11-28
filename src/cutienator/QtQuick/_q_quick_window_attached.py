"""
QQuickWindowAttached binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquickwindowattached_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QQuickWindowAttached to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject
from ..QtGui import QWindow

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from . import QQuickItem, QQuickWindow
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQuickWindow = WAIT['QQuickWindow']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickWindowAttached(QObject):
  """
  The cute side of Qt's QQuickWindowAttached: a plain Python object standing
  in front of one C++ QQuickWindowAttached.

  It is built on the cute 'QObject', as Qt's QQuickWindowAttached is built on
  Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickWindowAttached that has a ritual and that
  Python can call so far, 17 names in all: 'metaObject', 'tr', 'visibility',
  'isActive', 'activeFocusItem', 'contentItem', 'width', 'height', 'window',
  'visibilityChanged', 'activeChanged', 'activeFocusItemChanged',
  'contentItemChanged', 'widthChanged', 'heightChanged', 'windowChanged',
  'windowChange'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickWindowAttached::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QQuickWindowAttached::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'void QQuickWindowAttached::qt_qmlMarker_anonymous()': one of Qt's
    own inner workings.

  What has no ritual
  ------------------

  2 of the 23 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuickWindowAttached is created at the first use, not by
    'QQuickWindowAttached(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickWindowAttached.
  - Qt tells when it has removed the C++ QQuickWindowAttached. Every call on
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
    Calls Qt's 'QString QQuickWindowAttached::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickwindowattached.html#tr

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
    #  QString QQuickWindowAttached::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN20QQuickWindowAttached2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickWindowAttached'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickWindowAttached::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwindowattached.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickWindowAttached::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK20QQuickWindowAttached10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def visibility(self) -> QWindow.Visibility:
    """
    Calls Qt's 'QWindow::Visibility QQuickWindowAttached::visibility()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwindowattached.html#visibility

    Returns
    -------

    QWindow.Visibility
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QWindow.Visibility(number)' gives.
    """
    #  QWindow::Visibility QQuickWindowAttached::visibility() const
    return QWindow.Visibility(self.uglySide.call(
        'ritual_ZNK20QQuickWindowAttached10visibilityEv',
    ))

  def isActive(self) -> bool:
    """
    Calls Qt's 'bool QQuickWindowAttached::isActive() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickwindowattached.html#isActive
    """
    #  bool QQuickWindowAttached::isActive() const
    return self.uglySide.call('ritual_ZNK20QQuickWindowAttached8isActiveEv')

  def activeFocusItem(self) -> Optional[QQuickItem]:
    """
    Calls Qt's 'QQuickItem *QQuickWindowAttached::activeFocusItem() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwindowattached.html#activeFocusItem

    Returns
    -------

    Optional[QQuickItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickItem *QQuickWindowAttached::activeFocusItem() const
    address = self.uglySide.call(
        'ritual_ZNK20QQuickWindowAttached15activeFocusItemEv',
    )
    from . import QQuickItem
    return QQuickItem._cuteAt(address)

  def contentItem(self) -> Optional[QQuickItem]:
    """
    Calls Qt's 'QQuickItem *QQuickWindowAttached::contentItem() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwindowattached.html#contentItem

    Returns
    -------

    Optional[QQuickItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickItem *QQuickWindowAttached::contentItem() const
    address = self.uglySide.call(
        'ritual_ZNK20QQuickWindowAttached11contentItemEv',
    )
    from . import QQuickItem
    return QQuickItem._cuteAt(address)

  def width(self) -> int:
    """
    Calls Qt's 'int QQuickWindowAttached::width() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickwindowattached.html#width
    """
    #  int QQuickWindowAttached::width() const
    return self.uglySide.call('ritual_ZNK20QQuickWindowAttached5widthEv')

  def height(self) -> int:
    """
    Calls Qt's 'int QQuickWindowAttached::height() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickwindowattached.html#height
    """
    #  int QQuickWindowAttached::height() const
    return self.uglySide.call('ritual_ZNK20QQuickWindowAttached6heightEv')

  def window(self) -> Optional[QQuickWindow]:
    """
    Calls Qt's 'QQuickWindow *QQuickWindowAttached::window() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickwindowattached.html#window

    Returns
    -------

    Optional[QQuickWindow]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickWindow *QQuickWindowAttached::window() const
    address = self.uglySide.call('ritual_ZNK20QQuickWindowAttached6windowEv')
    from . import QQuickWindow
    return QQuickWindow._cuteAt(address)

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

  @overload(QObject)
  @overload(NoneType)
  def __init__(self, attachee: Optional[QObject]) -> None:
    """
    Notes what was given, for Qt's
    'QQuickWindowAttached::QQuickWindowAttached(QObject *attachee)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwindowattached.html#QQuickWindowAttached

    Parameters
    ----------

    attachee : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QQuickWindowAttached::QQuickWindowAttached(QObject *attachee)
    self._noteCreation(QQuickWindowAttached, lambda: Rituals.call(
        'ritual_ZN20QQuickWindowAttachedC1EP7QObject',
        self._addressOf(attachee, 'QObject'),
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

  def visibilityChanged(self) -> None:
    """
    Calls Qt's 'void QQuickWindowAttached::visibilityChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwindowattached.html#visibilityChanged
    """
    #  void QQuickWindowAttached::visibilityChanged()
    self.uglySide.call(
        'ritual_ZN20QQuickWindowAttached17visibilityChangedEv',
    )

  def activeChanged(self) -> None:
    """
    Calls Qt's 'void QQuickWindowAttached::activeChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwindowattached.html#activeChanged
    """
    #  void QQuickWindowAttached::activeChanged()
    self.uglySide.call('ritual_ZN20QQuickWindowAttached13activeChangedEv')

  def activeFocusItemChanged(self) -> None:
    """
    Calls Qt's 'void QQuickWindowAttached::activeFocusItemChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwindowattached.html#activeFocusItemChanged
    """
    #  void QQuickWindowAttached::activeFocusItemChanged()
    self.uglySide.call(
        'ritual_ZN20QQuickWindowAttached22activeFocusItemChangedEv',
    )

  def contentItemChanged(self) -> None:
    """
    Calls Qt's 'void QQuickWindowAttached::contentItemChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwindowattached.html#contentItemChanged
    """
    #  void QQuickWindowAttached::contentItemChanged()
    self.uglySide.call(
        'ritual_ZN20QQuickWindowAttached18contentItemChangedEv',
    )

  def widthChanged(self) -> None:
    """
    Calls Qt's 'void QQuickWindowAttached::widthChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwindowattached.html#widthChanged
    """
    #  void QQuickWindowAttached::widthChanged()
    self.uglySide.call('ritual_ZN20QQuickWindowAttached12widthChangedEv')

  def heightChanged(self) -> None:
    """
    Calls Qt's 'void QQuickWindowAttached::heightChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwindowattached.html#heightChanged
    """
    #  void QQuickWindowAttached::heightChanged()
    self.uglySide.call('ritual_ZN20QQuickWindowAttached13heightChangedEv')

  def windowChanged(self) -> None:
    """
    Calls Qt's 'void QQuickWindowAttached::windowChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwindowattached.html#windowChanged
    """
    #  void QQuickWindowAttached::windowChanged()
    self.uglySide.call('ritual_ZN20QQuickWindowAttached13windowChangedEv')

  @overload(QQuickWindow)
  @overload(NoneType)
  def windowChange(self, a0: Optional[QQuickWindow]) -> None:
    """
    Calls Qt's 'void QQuickWindowAttached::windowChange(QQuickWindow *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwindowattached.html#windowChange

    Parameters
    ----------

    a0 : Optional[QQuickWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickWindowAttached::windowChange(QQuickWindow *a0)
    self.uglySide.call(
        'ritual_ZN20QQuickWindowAttached12windowChangeEP12QQuickWindow',
        self._addressOf(a0),
    )
