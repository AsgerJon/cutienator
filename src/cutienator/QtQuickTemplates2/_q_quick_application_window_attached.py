"""
QQuickApplicationWindowAttached binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickapplicationwindow_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuickApplicationWindowAttached to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin
from ..occult import Rituals
from ..QtCore import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from ..QtQuick import QQuickItem
  from . import QQuickApplicationWindow

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickApplicationWindowAttached(QObject):
  """
  The cute side of Qt's QQuickApplicationWindowAttached: a plain Python
  object standing in front of one C++ QQuickApplicationWindowAttached.

  It is built on the cute 'QObject', as Qt's QQuickApplicationWindowAttached
  is built on Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickApplicationWindowAttached that has a ritual
  and that Python can call so far, 14 names in all: 'metaObject', 'tr',
  'window', 'contentItem', 'activeFocusControl', 'header', 'footer',
  'menuBar', 'windowChanged', 'contentItemChanged',
  'activeFocusControlChanged', 'headerChanged', 'footerChanged',
  'menuBarChanged'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickApplicationWindowAttached::qt_metacast(const char
    *a0)': one of Qt's own inner workings.
  - Qt's 'int QQuickApplicationWindowAttached::qt_metacall(QMetaObject::Call
    a0, int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QQuickApplicationWindowAttachedPrivate
    *QQuickApplicationWindowAttached::d_func()': gives
    'QQuickApplicationWindowAttachedPrivate', which has no cute class yet.
  - Qt's 'const QQuickApplicationWindowAttachedPrivate
    *QQuickApplicationWindowAttached::d_func() const': gives
    'QQuickApplicationWindowAttachedPrivate', which has no cute class yet.

  What has no ritual
  ------------------

  4 of the 23 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QQuickApplicationWindowAttached is created at the first use, not
    by 'QQuickApplicationWindowAttached(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickApplicationWindowAttached.
  - Qt tells when it has removed the C++ QQuickApplicationWindowAttached.
    Every call on the cute object, and every use of it as an argument, then
    raises 'RuntimeError', and nothing reaches C++.
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
    Calls Qt's 'QString QQuickApplicationWindowAttached::tr(const char *s,
    const char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickapplicationwindowattached.html#tr

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
    #  QString QQuickApplicationWindowAttached::tr(const char *s, const char
    #      *c, int n)
    return Rituals.call(
        'ritual_ZN31QQuickApplicationWindowAttached2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickApplicationWindowAttached'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject
    *QQuickApplicationWindowAttached::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickapplicationwindowattached.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickApplicationWindowAttached::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK31QQuickApplicationWindowAttached10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def window(self) -> Optional[QQuickApplicationWindow]:
    """
    Calls Qt's 'QQuickApplicationWindow
    *QQuickApplicationWindowAttached::window() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickapplicationwindowattached.html#window

    Returns
    -------

    Optional[QQuickApplicationWindow]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickApplicationWindow *QQuickApplicationWindowAttached::window()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK31QQuickApplicationWindowAttached6windowEv',
    )
    from . import QQuickApplicationWindow
    return QQuickApplicationWindow._cuteAt(address)

  def contentItem(self) -> Optional[QQuickItem]:
    """
    Calls Qt's 'QQuickItem *QQuickApplicationWindowAttached::contentItem()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickapplicationwindowattached.html#contentItem

    Returns
    -------

    Optional[QQuickItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickItem *QQuickApplicationWindowAttached::contentItem() const
    address = self.uglySide.call(
        'ritual_ZNK31QQuickApplicationWindowAttached11contentItemEv',
    )
    from ..QtQuick import QQuickItem
    return QQuickItem._cuteAt(address)

  def activeFocusControl(self) -> Optional[QQuickItem]:
    """
    Calls Qt's 'QQuickItem
    *QQuickApplicationWindowAttached::activeFocusControl() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickapplicationwindowattached.html

    Returns
    -------

    Optional[QQuickItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickItem *QQuickApplicationWindowAttached::activeFocusControl()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK31QQuickApplicationWindowAttached18activeFocusControlEv',
    )
    from ..QtQuick import QQuickItem
    return QQuickItem._cuteAt(address)

  def header(self) -> Optional[QQuickItem]:
    """
    Calls Qt's 'QQuickItem *QQuickApplicationWindowAttached::header() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickapplicationwindowattached.html#header

    Returns
    -------

    Optional[QQuickItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickItem *QQuickApplicationWindowAttached::header() const
    address = self.uglySide.call(
        'ritual_ZNK31QQuickApplicationWindowAttached6headerEv',
    )
    from ..QtQuick import QQuickItem
    return QQuickItem._cuteAt(address)

  def footer(self) -> Optional[QQuickItem]:
    """
    Calls Qt's 'QQuickItem *QQuickApplicationWindowAttached::footer() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickapplicationwindowattached.html#footer

    Returns
    -------

    Optional[QQuickItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickItem *QQuickApplicationWindowAttached::footer() const
    address = self.uglySide.call(
        'ritual_ZNK31QQuickApplicationWindowAttached6footerEv',
    )
    from ..QtQuick import QQuickItem
    return QQuickItem._cuteAt(address)

  def menuBar(self) -> Optional[QQuickItem]:
    """
    Calls Qt's 'QQuickItem *QQuickApplicationWindowAttached::menuBar()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickapplicationwindowattached.html#menuBar

    Returns
    -------

    Optional[QQuickItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickItem *QQuickApplicationWindowAttached::menuBar() const
    address = self.uglySide.call(
        'ritual_ZNK31QQuickApplicationWindowAttached7menuBarEv',
    )
    from ..QtQuick import QQuickItem
    return QQuickItem._cuteAt(address)

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
    'QQuickApplicationWindowAttached::QQuickApplicationWindowAttached(QObject
    *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickapplicationwindowattached.html

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickApplicationWindowAttached::QQuickApplicationWindowAttached(
    #      QObject *parent)
    self._noteCreation(QQuickApplicationWindowAttached, lambda: Rituals.call(
        'ritual_ZN31QQuickApplicationWindowAttachedC1EP7QObject',
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

  def windowChanged(self) -> None:
    """
    Calls Qt's 'void QQuickApplicationWindowAttached::windowChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickapplicationwindowattached.html#windowChanged
    """
    #  void QQuickApplicationWindowAttached::windowChanged()
    self.uglySide.call(
        'ritual_ZN31QQuickApplicationWindowAttached13windowChangedEv',
    )

  def contentItemChanged(self) -> None:
    """
    Calls Qt's 'void QQuickApplicationWindowAttached::contentItemChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickapplicationwindowattached.html
    """
    #  void QQuickApplicationWindowAttached::contentItemChanged()
    self.uglySide.call(
        'ritual_ZN31QQuickApplicationWindowAttached18contentItemChangedEv',
    )

  def activeFocusControlChanged(self) -> None:
    """
    Calls Qt's 'void
    QQuickApplicationWindowAttached::activeFocusControlChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickapplicationwindowattached.html
    """
    #  void QQuickApplicationWindowAttached::activeFocusControlChanged()
    self.uglySide.call(
        'ritual_ZN31QQuickApplicationWindowAttached25activeFocusControlChan'
        'gedEv',
    )

  def headerChanged(self) -> None:
    """
    Calls Qt's 'void QQuickApplicationWindowAttached::headerChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickapplicationwindowattached.html#headerChanged
    """
    #  void QQuickApplicationWindowAttached::headerChanged()
    self.uglySide.call(
        'ritual_ZN31QQuickApplicationWindowAttached13headerChangedEv',
    )

  def footerChanged(self) -> None:
    """
    Calls Qt's 'void QQuickApplicationWindowAttached::footerChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickapplicationwindowattached.html#footerChanged
    """
    #  void QQuickApplicationWindowAttached::footerChanged()
    self.uglySide.call(
        'ritual_ZN31QQuickApplicationWindowAttached13footerChangedEv',
    )

  def menuBarChanged(self) -> None:
    """
    Calls Qt's 'void QQuickApplicationWindowAttached::menuBarChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickapplicationwindowattached.html
    """
    #  void QQuickApplicationWindowAttached::menuBarChanged()
    self.uglySide.call(
        'ritual_ZN31QQuickApplicationWindowAttached14menuBarChangedEv',
    )
