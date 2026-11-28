"""
QQuickTableViewDelegate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquicktableviewdelegate_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuickTableViewDelegate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtQuick import QQuickItem
from . import QQuickItemDelegate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from ..QtGui import QFont, QMouseEvent
  from ..QtQuick import QQuickTableView
  from . import QQuickTableViewDelegatePrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QMouseEvent = WAIT['QMouseEvent']
  QQuickTableView = WAIT['QQuickTableView']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickTableViewDelegate(QQuickItemDelegate):
  """
  The cute side of Qt's QQuickTableViewDelegate: a plain Python object
  standing in front of one C++ QQuickTableViewDelegate.

  It is built on the cute 'QQuickItemDelegate', as Qt's
  QQuickTableViewDelegate is built on Qt's QQuickItemDelegate, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickTableViewDelegate that has a ritual and that
  Python can call so far, 17 names in all: 'metaObject', 'tr', 'current',
  'setCurrent', 'selected', 'setSelected', 'editing', 'setEditing',
  'tableView', 'setTableView', 'tableViewChanged', 'currentChanged',
  'selectedChanged', 'editingChanged', 'defaultFont', 'mousePressEvent',
  'd_func'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickTableViewDelegate::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QQuickTableViewDelegate::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QQuickTableViewDelegate::QQuickTableViewDelegate(
    QQuickTableViewDelegatePrivate &dd, QQuickItem *parent)': takes a type
    Python has no way to hand over yet.
  - Qt's 'const QQuickTableViewDelegatePrivate
    *QQuickTableViewDelegate::d_func() const': takes in Python what
    'QQuickTableViewDelegatePrivate *QQuickTableViewDelegate::d_func()'
    takes.

  What has no ritual
  ------------------

  4 of the 26 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QQuickTableViewDelegate is created at the first use, not by
    'QQuickTableViewDelegate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickTableViewDelegate.
  - Qt tells when it has removed the C++ QQuickTableViewDelegate. Every call
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
    Calls Qt's 'QString QQuickTableViewDelegate::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktableviewdelegate.html#tr

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
    #  QString QQuickTableViewDelegate::tr(const char *s, const char *c, int
    #      n)
    return Rituals.call(
        'ritual_ZN23QQuickTableViewDelegate2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickTableViewDelegate'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickTableViewDelegate::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableviewdelegate.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickTableViewDelegate::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK23QQuickTableViewDelegate10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def current(self) -> bool:
    """
    Calls Qt's 'bool QQuickTableViewDelegate::current() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableviewdelegate.html#current
    """
    #  bool QQuickTableViewDelegate::current() const
    return self.uglySide.call(
        'ritual_ZNK23QQuickTableViewDelegate7currentEv',
    )

  def selected(self) -> bool:
    """
    Calls Qt's 'bool QQuickTableViewDelegate::selected() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableviewdelegate.html#selected
    """
    #  bool QQuickTableViewDelegate::selected() const
    return self.uglySide.call(
        'ritual_ZNK23QQuickTableViewDelegate8selectedEv',
    )

  def editing(self) -> bool:
    """
    Calls Qt's 'bool QQuickTableViewDelegate::editing() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableviewdelegate.html#editing
    """
    #  bool QQuickTableViewDelegate::editing() const
    return self.uglySide.call(
        'ritual_ZNK23QQuickTableViewDelegate7editingEv',
    )

  def tableView(self) -> Optional[QQuickTableView]:
    """
    Calls Qt's 'QQuickTableView *QQuickTableViewDelegate::tableView() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableviewdelegate.html#tableView

    Returns
    -------

    Optional[QQuickTableView]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickTableView *QQuickTableViewDelegate::tableView() const
    address = self.uglySide.call(
        'ritual_ZNK23QQuickTableViewDelegate9tableViewEv',
    )
    from ..QtQuick import QQuickTableView
    return QQuickTableView._cuteAt(address)

  def defaultFont(self) -> QFont:
    """
    Calls Qt's 'QFont QQuickTableViewDelegate::defaultFont() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableviewdelegate.html#defaultFont

    Returns
    -------

    QFont
      A new cute QFont around the copy Qt gave back. Python owns it.
    """
    #  QFont QQuickTableViewDelegate::defaultFont() const
    ritual = 'ritual_ZNK23QQuickTableViewDelegate11defaultFontEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK23QQuickTableViewDelegate11defaultFontEv'
    address = self.uglySide.call(ritual)
    from ..QtGui import QFont
    return QFont._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  def setCurrent(self, current: bool) -> None:
    """
    Calls Qt's 'void QQuickTableViewDelegate::setCurrent(bool current)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableviewdelegate.html#setCurrent

    Parameters
    ----------

    current : bool
      Passed on as it is.
    """
    #  void QQuickTableViewDelegate::setCurrent(bool current)
    self.uglySide.call(
        'ritual_ZN23QQuickTableViewDelegate10setCurrentEb', current,
    )

  @overload(bool)
  def setSelected(self, selected: bool) -> None:
    """
    Calls Qt's 'void QQuickTableViewDelegate::setSelected(bool selected)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableviewdelegate.html#setSelected

    Parameters
    ----------

    selected : bool
      Passed on as it is.
    """
    #  void QQuickTableViewDelegate::setSelected(bool selected)
    self.uglySide.call(
        'ritual_ZN23QQuickTableViewDelegate11setSelectedEb', selected,
    )

  @overload(bool)
  def setEditing(self, editing: bool) -> None:
    """
    Calls Qt's 'void QQuickTableViewDelegate::setEditing(bool editing)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableviewdelegate.html#setEditing

    Parameters
    ----------

    editing : bool
      Passed on as it is.
    """
    #  void QQuickTableViewDelegate::setEditing(bool editing)
    self.uglySide.call(
        'ritual_ZN23QQuickTableViewDelegate10setEditingEb', editing,
    )

  @overload(QQuickTableView)
  @overload(NoneType)
  def setTableView(self, tableView: Optional[QQuickTableView]) -> None:
    """
    Calls Qt's 'void QQuickTableViewDelegate::setTableView(QQuickTableView
    *tableView)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableviewdelegate.html#setTableView

    Parameters
    ----------

    tableView : Optional[QQuickTableView]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickTableViewDelegate::setTableView(QQuickTableView *tableView)
    self.uglySide.call(
        'ritual_ZN23QQuickTableViewDelegate12setTableViewEP15QQuickTableVie'
        'w',
        self._addressOf(tableView),
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
  @overload(QQuickItem)
  @overload(NoneType)
  def __init__(self, parent: Optional[QQuickItem] = None) -> None:
    """
    Notes what was given, for Qt's
    'QQuickTableViewDelegate::QQuickTableViewDelegate(QQuickItem *parent)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableviewdelegate.html

    Parameters
    ----------

    parent : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickTableViewDelegate::QQuickTableViewDelegate(QQuickItem *parent)
    self._noteCreation(QQuickTableViewDelegate, lambda: Rituals.call(
        'ritual_ZN23QQuickTableViewDelegateC1EP10QQuickItem',
        self._addressOf(parent),
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

  def tableViewChanged(self) -> None:
    """
    Calls Qt's 'void QQuickTableViewDelegate::tableViewChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableviewdelegate.html#tableViewChanged
    """
    #  void QQuickTableViewDelegate::tableViewChanged()
    self.uglySide.call(
        'ritual_ZN23QQuickTableViewDelegate16tableViewChangedEv',
    )

  def currentChanged(self) -> None:
    """
    Calls Qt's 'void QQuickTableViewDelegate::currentChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableviewdelegate.html#currentChanged
    """
    #  void QQuickTableViewDelegate::currentChanged()
    self.uglySide.call(
        'ritual_ZN23QQuickTableViewDelegate14currentChangedEv',
    )

  def selectedChanged(self) -> None:
    """
    Calls Qt's 'void QQuickTableViewDelegate::selectedChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableviewdelegate.html#selectedChanged
    """
    #  void QQuickTableViewDelegate::selectedChanged()
    self.uglySide.call(
        'ritual_ZN23QQuickTableViewDelegate15selectedChangedEv',
    )

  def editingChanged(self) -> None:
    """
    Calls Qt's 'void QQuickTableViewDelegate::editingChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableviewdelegate.html#editingChanged
    """
    #  void QQuickTableViewDelegate::editingChanged()
    self.uglySide.call(
        'ritual_ZN23QQuickTableViewDelegate14editingChangedEv',
    )

  @overload(QMouseEvent)
  @overload(NoneType)
  def mousePressEvent(self, event: Optional[QMouseEvent]) -> None:
    """
    Calls Qt's 'void QQuickTableViewDelegate::mousePressEvent(QMouseEvent
    *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableviewdelegate.html#mousePressEvent

    Parameters
    ----------

    event : Optional[QMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickTableViewDelegate::mousePressEvent(QMouseEvent *event)
    ritual = (
        'ritual_ZN23QQuickTableViewDelegate15mousePressEventEP11QMouseEvent')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN23QQuickTableViewDelegate15mousePressEventEP11QMous'
          'eEvent')
    self.uglySide.call(ritual, self._addressOf(event))

  def d_func(self) -> Optional[QQuickTableViewDelegatePrivate]:
    """
    Calls Qt's 'QQuickTableViewDelegatePrivate
    *QQuickTableViewDelegate::d_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableviewdelegate.html#d_func

    Returns
    -------

    Optional[QQuickTableViewDelegatePrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickTableViewDelegatePrivate *QQuickTableViewDelegate::d_func()
    address = self.uglySide.call(
        'ritual_ZN23QQuickTableViewDelegate6d_funcEv',
    )
    from . import QQuickTableViewDelegatePrivate
    return QQuickTableViewDelegatePrivate._cuteAt(address)
