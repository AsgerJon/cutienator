"""
QToolBox binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/qtoolbox.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import Qt
from . import QFrame, QWidget

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QEvent, QMetaObject
  from ..QtGui import QIcon, QShowEvent
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QEvent = WAIT['QEvent']
  QIcon = WAIT['QIcon']
  QShowEvent = WAIT['QShowEvent']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QToolBox(QFrame):
  """
  The cute side of Qt's QToolBox: a plain Python object standing in front of
  one C++ QToolBox.

  It is built on the cute 'QFrame', as Qt's QToolBox is built on Qt's QFrame,
  and has everything that class has.

  What exists
  -----------

  Every function of Qt's QToolBox that has a ritual and that Python can call
  so far, 25 names in all: 'metaObject', 'tr', 'addItem', 'insertItem',
  'removeItem', 'setItemEnabled', 'isItemEnabled', 'setItemText', 'itemText',
  'setItemIcon', 'itemIcon', 'setItemToolTip', 'itemToolTip', 'currentIndex',
  'currentWidget', 'widget', 'indexOf', 'count', 'setCurrentIndex',
  'setCurrentWidget', 'event', 'itemInserted', 'itemRemoved', 'showEvent',
  'changeEvent'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QToolBox::~QToolBox()': the destructor: Python never removes a C++
    QToolBox.

  What has no ritual
  ------------------

  9 of the 38 functions Qt declares: 4 takes or gives a type that cannot be
  passed yet; 2 forbidden; 1 a template; 1 declared and nowhere to be found;
  1 a signal.

  What to expect
  --------------

  - The C++ QToolBox is created at the first use, not by 'QToolBox(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QToolBox.
  - Qt tells when it has removed the C++ QToolBox. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
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
    Calls Qt's 'QString QToolBox::tr(const char *s, const char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qtoolbox.html#tr

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
    #  QString QToolBox::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN8QToolBox2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QToolBox'

  #  A C++ QToolBox Python makes is of a C++ class of ours, in which Python
  #  can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QToolBox'

  #  The functions Qt calls itself that QToolBox is the first to declare. A
  #  class of a program built on it can write one anew, and Qt then calls
  #  that. For each name: the key C++ knows the function by, what it gives,
  #  and what it takes.
  __virtual_functions__ = {
      'itemInserted': (
          ('_ZN8QToolBox12itemInsertedEi',
           ('nothing', 'nothing', ''),
           (
               ('int', 'number', ''),
           )),
      ),
      'itemRemoved': (
          ('_ZN8QToolBox11itemRemovedEi',
           ('nothing', 'nothing', ''),
           (
               ('int', 'number', ''),
           )),
      ),
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
    Calls Qt's 'const QMetaObject *QToolBox::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtoolbox.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QToolBox::metaObject() const
    address = self.uglySide.call('ritual_ZNK8QToolBox10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  @overload(int)
  def isItemEnabled(self, index: int) -> bool:
    """
    Calls Qt's 'bool QToolBox::isItemEnabled(int index) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtoolbox.html#isItemEnabled

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  bool QToolBox::isItemEnabled(int index) const
    return self.uglySide.call('ritual_ZNK8QToolBox13isItemEnabledEi', index)

  @overload(int)
  def itemText(self, index: int) -> str:
    """
    Calls Qt's 'QString QToolBox::itemText(int index) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtoolbox.html#itemText

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QToolBox::itemText(int index) const
    return self.uglySide.call('ritual_ZNK8QToolBox8itemTextEi', index)

  @overload(int)
  def itemIcon(self, index: int) -> QIcon:
    """
    Calls Qt's 'QIcon QToolBox::itemIcon(int index) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtoolbox.html#itemIcon

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    QIcon
      A new cute QIcon around the copy Qt gave back. Python owns it.
    """
    #  QIcon QToolBox::itemIcon(int index) const
    address = self.uglySide.call('ritual_ZNK8QToolBox8itemIconEi', index)
    from ..QtGui import QIcon
    return QIcon._cuteOwning(address)

  @overload(int)
  def itemToolTip(self, index: int) -> str:
    """
    Calls Qt's 'QString QToolBox::itemToolTip(int index) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtoolbox.html#itemToolTip

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QToolBox::itemToolTip(int index) const
    return self.uglySide.call('ritual_ZNK8QToolBox11itemToolTipEi', index)

  def currentIndex(self) -> int:
    """
    Calls Qt's 'int QToolBox::currentIndex() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtoolbox.html#currentIndex
    """
    #  int QToolBox::currentIndex() const
    return self.uglySide.call('ritual_ZNK8QToolBox12currentIndexEv')

  def currentWidget(self) -> Optional[QWidget]:
    """
    Calls Qt's 'QWidget *QToolBox::currentWidget() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtoolbox.html#currentWidget

    Returns
    -------

    Optional[QWidget]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWidget *QToolBox::currentWidget() const
    address = self.uglySide.call('ritual_ZNK8QToolBox13currentWidgetEv')
    return QWidget._cuteAt(address)

  @overload(int)
  def widget(self, index: int) -> Optional[QWidget]:
    """
    Calls Qt's 'QWidget *QToolBox::widget(int index) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtoolbox.html#widget

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    Optional[QWidget]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWidget *QToolBox::widget(int index) const
    address = self.uglySide.call('ritual_ZNK8QToolBox6widgetEi', index)
    return QWidget._cuteAt(address)

  @overload(QWidget)
  @overload(NoneType)
  def indexOf(self, widget: Optional[QWidget]) -> int:
    """
    Calls Qt's 'int QToolBox::indexOf(const QWidget *widget) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtoolbox.html#indexOf

    Parameters
    ----------

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  int QToolBox::indexOf(const QWidget *widget) const
    return self.uglySide.call(
        'ritual_ZNK8QToolBox7indexOfEPK7QWidget', self._addressOf(widget),
    )

  def count(self) -> int:
    """
    Calls Qt's 'int QToolBox::count() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtoolbox.html#count
    """
    #  int QToolBox::count() const
    return self.uglySide.call('ritual_ZNK8QToolBox5countEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int, bool)
  def setItemEnabled(self, index: int, enabled: bool) -> None:
    """
    Calls Qt's 'void QToolBox::setItemEnabled(int index, bool enabled)'.

    Qt's own words: https://doc.qt.io/qt-6/qtoolbox.html#setItemEnabled

    Parameters
    ----------

    index : int
      Passed on as it is.

    enabled : bool
      Passed on as it is.
    """
    #  void QToolBox::setItemEnabled(int index, bool enabled)
    self.uglySide.call(
        'ritual_ZN8QToolBox14setItemEnabledEib', index, enabled,
    )

  @overload(int, str)
  def setItemText(self, index: int, text: str) -> None:
    """
    Calls Qt's 'void QToolBox::setItemText(int index, const QString &text)'.

    Qt's own words: https://doc.qt.io/qt-6/qtoolbox.html#setItemText

    Parameters
    ----------

    index : int
      Passed on as it is.

    text : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QToolBox::setItemText(int index, const QString &text)
    self.uglySide.call(
        'ritual_ZN8QToolBox11setItemTextEiRK7QString', index, text,
    )

  @overload(int, QIcon)
  def setItemIcon(self, index: int, icon: QIcon) -> None:
    """
    Calls Qt's 'void QToolBox::setItemIcon(int index, const QIcon &icon)'.

    Qt's own words: https://doc.qt.io/qt-6/qtoolbox.html#setItemIcon

    Parameters
    ----------

    index : int
      Passed on as it is.

    icon : QIcon
      Passed on as a value: Qt reads the C++ QIcon, which stays Python's own.
    """
    #  void QToolBox::setItemIcon(int index, const QIcon &icon)
    self.uglySide.call(
        'ritual_ZN8QToolBox11setItemIconEiRK5QIcon',
        index, self._valueOf(icon),
    )

  @overload(int, str)
  def setItemToolTip(self, index: int, toolTip: str) -> None:
    """
    Calls Qt's 'void QToolBox::setItemToolTip(int index, const QString
    &toolTip)'.

    Qt's own words: https://doc.qt.io/qt-6/qtoolbox.html#setItemToolTip

    Parameters
    ----------

    index : int
      Passed on as it is.

    toolTip : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QToolBox::setItemToolTip(int index, const QString &toolTip)
    self.uglySide.call(
        'ritual_ZN8QToolBox14setItemToolTipEiRK7QString', index, toolTip,
    )

  @overload(int)
  def setCurrentIndex(self, index: int) -> None:
    """
    Calls Qt's 'void QToolBox::setCurrentIndex(int index)'.

    Qt's own words: https://doc.qt.io/qt-6/qtoolbox.html#setCurrentIndex

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  void QToolBox::setCurrentIndex(int index)
    self.uglySide.call('ritual_ZN8QToolBox15setCurrentIndexEi', index)

  @overload(QWidget)
  @overload(NoneType)
  def setCurrentWidget(self, widget: Optional[QWidget]) -> None:
    """
    Calls Qt's 'void QToolBox::setCurrentWidget(QWidget *widget)'.

    Qt's own words: https://doc.qt.io/qt-6/qtoolbox.html#setCurrentWidget

    Parameters
    ----------

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QToolBox::setCurrentWidget(QWidget *widget)
    self.uglySide.call(
        'ritual_ZN8QToolBox16setCurrentWidgetEP7QWidget',
        self._addressOf(widget),
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
  @overload(QWidget)
  @overload(NoneType)
  @overload(QWidget, Qt.WindowFlags)
  @overload(NoneType, Qt.WindowFlags)
  def __init__(
      self,
      parent: Optional[QWidget] = None,
      f: Qt.WindowFlags = Qt.WindowFlags(),
  ) -> None:
    """
    Notes what was given, for Qt's 'QToolBox::QToolBox(QWidget *parent,
    Qt::WindowFlags f)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qtoolbox.html#QToolBox

    Parameters
    ----------

    parent : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    f : Qt.WindowFlags
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.WindowFlags().
    """
    #  QToolBox::QToolBox(QWidget *parent, Qt::WindowFlags f)
    self._noteCreation(QToolBox, lambda: Rituals.call(
        'ritual_ZN8QToolBoxC1EP7QWidget6QFlagsIN2Qt10WindowTypeEE',
        self._addressOf(parent), f.value,
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

  @overload(QWidget, str)
  @overload(NoneType, str)
  def addItem(self, widget: Optional[QWidget], text: str) -> int:
    """
    Calls Qt's 'int QToolBox::addItem(QWidget *widget, const QString &text)'.

    Qt's own words: https://doc.qt.io/qt-6/qtoolbox.html#addItem

    Parameters
    ----------

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    text : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  int QToolBox::addItem(QWidget *widget, const QString &text)
    return self.uglySide.call(
        'ritual_ZN8QToolBox7addItemEP7QWidgetRK7QString',
        self._addressOf(widget), text,
    )

  @overload(QWidget, QIcon, str)
  @overload(NoneType, QIcon, str)
  def addItem(
      self,
      widget: Optional[QWidget],
      icon: QIcon,
      text: str,
  ) -> int:
    """
    Calls Qt's 'int QToolBox::addItem(QWidget *widget, const QIcon &icon,
    const QString &text)'.

    Qt's own words: https://doc.qt.io/qt-6/qtoolbox.html#addItem

    Parameters
    ----------

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    icon : QIcon
      Passed on as a value: Qt reads the C++ QIcon, which stays Python's own.

    text : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  int QToolBox::addItem(QWidget *widget, const QIcon &icon, const
    #      QString &text)
    return self.uglySide.call(
        'ritual_ZN8QToolBox7addItemEP7QWidgetRK5QIconRK7QString',
        self._addressOf(widget), self._valueOf(icon), text,
    )

  @overload(int, QWidget, str)
  @overload(int, NoneType, str)
  def insertItem(
      self,
      index: int,
      widget: Optional[QWidget],
      text: str,
  ) -> int:
    """
    Calls Qt's 'int QToolBox::insertItem(int index, QWidget *widget, const
    QString &text)'.

    Qt's own words: https://doc.qt.io/qt-6/qtoolbox.html#insertItem

    Parameters
    ----------

    index : int
      Passed on as it is.

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    text : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  int QToolBox::insertItem(int index, QWidget *widget, const QString
    #      &text)
    return self.uglySide.call(
        'ritual_ZN8QToolBox10insertItemEiP7QWidgetRK7QString',
        index, self._addressOf(widget), text,
    )

  @overload(int, QWidget, QIcon, str)
  @overload(int, NoneType, QIcon, str)
  def insertItem(
      self,
      index: int,
      widget: Optional[QWidget],
      icon: QIcon,
      text: str,
  ) -> int:
    """
    Calls Qt's 'int QToolBox::insertItem(int index, QWidget *widget, const
    QIcon &icon, const QString &text)'.

    Qt's own words: https://doc.qt.io/qt-6/qtoolbox.html#insertItem

    Parameters
    ----------

    index : int
      Passed on as it is.

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    icon : QIcon
      Passed on as a value: Qt reads the C++ QIcon, which stays Python's own.

    text : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  int QToolBox::insertItem(int index, QWidget *widget, const QIcon
    #      &icon, const QString &text)
    return self.uglySide.call(
        'ritual_ZN8QToolBox10insertItemEiP7QWidgetRK5QIconRK7QString',
        index, self._addressOf(widget), self._valueOf(icon), text,
    )

  @overload(int)
  def removeItem(self, index: int) -> None:
    """
    Calls Qt's 'void QToolBox::removeItem(int index)'.

    Qt's own words: https://doc.qt.io/qt-6/qtoolbox.html#removeItem

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  void QToolBox::removeItem(int index)
    self.uglySide.call('ritual_ZN8QToolBox10removeItemEi', index)

  @overload(QEvent)
  @overload(NoneType)
  def event(self, e: Optional[QEvent]) -> bool:
    """
    Calls Qt's 'bool QToolBox::event(QEvent *e)'.

    Qt's own words: https://doc.qt.io/qt-6/qtoolbox.html#event

    Parameters
    ----------

    e : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QToolBox::event(QEvent *e)
    ritual = 'ritual_ZN8QToolBox5eventEP6QEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN8QToolBox5eventEP6QEvent'
    return self.uglySide.call(ritual, self._addressOf(e))

  @overload(int)
  def itemInserted(self, index: int) -> None:
    """
    Calls Qt's 'void QToolBox::itemInserted(int index)'.

    Qt's own words: https://doc.qt.io/qt-6/qtoolbox.html#itemInserted

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  void QToolBox::itemInserted(int index)
    ritual = 'ritual_ZN8QToolBox12itemInsertedEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN8QToolBox12itemInsertedEi'
    self.uglySide.call(ritual, index)

  @overload(int)
  def itemRemoved(self, index: int) -> None:
    """
    Calls Qt's 'void QToolBox::itemRemoved(int index)'.

    Qt's own words: https://doc.qt.io/qt-6/qtoolbox.html#itemRemoved

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  void QToolBox::itemRemoved(int index)
    ritual = 'ritual_ZN8QToolBox11itemRemovedEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN8QToolBox11itemRemovedEi'
    self.uglySide.call(ritual, index)

  @overload(QShowEvent)
  @overload(NoneType)
  def showEvent(self, e: Optional[QShowEvent]) -> None:
    """
    Calls Qt's 'void QToolBox::showEvent(QShowEvent *e)'.

    Qt's own words: https://doc.qt.io/qt-6/qtoolbox.html#showEvent

    Parameters
    ----------

    e : Optional[QShowEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QToolBox::showEvent(QShowEvent *e)
    ritual = 'ritual_ZN8QToolBox9showEventEP10QShowEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN8QToolBox9showEventEP10QShowEvent'
    self.uglySide.call(ritual, self._addressOf(e))

  @overload(QEvent)
  @overload(NoneType)
  def changeEvent(self, a0: Optional[QEvent]) -> None:
    """
    Calls Qt's 'void QToolBox::changeEvent(QEvent *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qtoolbox.html#changeEvent

    Parameters
    ----------

    a0 : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QToolBox::changeEvent(QEvent *a0)
    ritual = 'ritual_ZN8QToolBox11changeEventEP6QEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN8QToolBox11changeEventEP6QEvent'
    self.uglySide.call(ritual, self._addressOf(a0))
