"""
QMdiSubWindow binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/qmdisubwindow.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, CuteFlags, WAIT
from ..occult import Rituals
from ..QtCore import Qt, QList, QObject
from . import QWidget

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QChildEvent, QEvent, QMetaObject, QSize, QTimerEvent
  from ..QtGui import QCloseEvent, QContextMenuEvent, QFocusEvent, QHideEvent
  from ..QtGui import QKeyEvent, QMouseEvent, QMoveEvent, QPaintEvent
  from ..QtGui import QResizeEvent, QShowEvent
  from . import QMdiArea, QMenu
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QChildEvent = WAIT['QChildEvent']
  QCloseEvent = WAIT['QCloseEvent']
  QContextMenuEvent = WAIT['QContextMenuEvent']
  QEvent = WAIT['QEvent']
  QFocusEvent = WAIT['QFocusEvent']
  QHideEvent = WAIT['QHideEvent']
  QKeyEvent = WAIT['QKeyEvent']
  QMenu = WAIT['QMenu']
  QMouseEvent = WAIT['QMouseEvent']
  QMoveEvent = WAIT['QMoveEvent']
  QPaintEvent = WAIT['QPaintEvent']
  QResizeEvent = WAIT['QResizeEvent']
  QShowEvent = WAIT['QShowEvent']
  QTimerEvent = WAIT['QTimerEvent']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QMdiSubWindow(QWidget):
  """
  The cute side of Qt's QMdiSubWindow: a plain Python object standing in
  front of one C++ QMdiSubWindow.

  It is built on the cute 'QWidget', as Qt's QMdiSubWindow is built on Qt's
  QWidget, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QMdiSubWindow that has a ritual and that Python can
  call so far, 40 names in all: 'metaObject', 'tr', 'sizeHint',
  'minimumSizeHint', 'setWidget', 'widget', 'maximizedButtonsWidget',
  'maximizedSystemMenuIconWidget', 'isShaded', 'setOption', 'testOption',
  'setKeyboardSingleStep', 'keyboardSingleStep', 'setKeyboardPageStep',
  'keyboardPageStep', 'setSystemMenu', 'systemMenu', 'mdiArea',
  'showSystemMenu', 'showShaded', 'eventFilter', 'event', 'showEvent',
  'hideEvent', 'changeEvent', 'closeEvent', 'leaveEvent', 'resizeEvent',
  'timerEvent', 'moveEvent', 'paintEvent', 'mousePressEvent',
  'mouseDoubleClickEvent', 'mouseReleaseEvent', 'mouseMoveEvent',
  'keyPressEvent', 'contextMenuEvent', 'focusInEvent', 'focusOutEvent',
  'childEvent'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QMdiSubWindow::~QMdiSubWindow()': the destructor: Python never
    removes a C++ QMdiSubWindow.
  - Qt's 'QMdiSubWindowPrivate *QMdiSubWindow::d_func()': gives
    'QMdiSubWindowPrivate', which has no cute class yet.
  - Qt's 'const QMdiSubWindowPrivate *QMdiSubWindow::d_func() const': gives
    'QMdiSubWindowPrivate', which has no cute class yet.

  What has no ritual
  ------------------

  8 of the 52 functions Qt declares: 2 takes or gives a type that cannot be
  passed yet; 2 a signal; 2 forbidden; 1 a template; 1 declared and nowhere
  to be found.

  What to expect
  --------------

  - The C++ QMdiSubWindow is created at the first use, not by
    'QMdiSubWindow(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QMdiSubWindow.
  - Qt tells when it has removed the C++ QMdiSubWindow. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  #  The enums Qt writes inside QMdiSubWindow, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class SubWindowOption(CuteFlags):
    """
    The flags enum 'QMdiSubWindow::SubWindowOption' of Qt, with the 4 names
    Qt gives in it. Qt names the type of its combinations
    'QMdiSubWindow::SubWindowOptions'.
    """

    AllowOutsideAreaHorizontally = 0x1
    AllowOutsideAreaVertically = 0x2
    RubberBandResize = 0x4
    RubberBandMove = 0x8

  SubWindowOptions = SubWindowOption

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
    Calls Qt's 'QString QMdiSubWindow::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qmdisubwindow.html#tr

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
    #  QString QMdiSubWindow::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN13QMdiSubWindow2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QMdiSubWindow'

  #  A C++ QMdiSubWindow Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QMdiSubWindow'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QMdiSubWindow::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmdisubwindow.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QMdiSubWindow::metaObject() const
    address = self.uglySide.call('ritual_ZNK13QMdiSubWindow10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def sizeHint(self) -> QSize:
    """
    Calls Qt's 'QSize QMdiSubWindow::sizeHint() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmdisubwindow.html#sizeHint

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QMdiSubWindow::sizeHint() const
    ritual = 'ritual_ZNK13QMdiSubWindow8sizeHintEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK13QMdiSubWindow8sizeHintEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  def minimumSizeHint(self) -> QSize:
    """
    Calls Qt's 'QSize QMdiSubWindow::minimumSizeHint() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmdisubwindow.html#minimumSizeHint

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QMdiSubWindow::minimumSizeHint() const
    ritual = 'ritual_ZNK13QMdiSubWindow15minimumSizeHintEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK13QMdiSubWindow15minimumSizeHintEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  def widget(self) -> Optional[QWidget]:
    """
    Calls Qt's 'QWidget *QMdiSubWindow::widget() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmdisubwindow.html#widget

    Returns
    -------

    Optional[QWidget]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWidget *QMdiSubWindow::widget() const
    address = self.uglySide.call('ritual_ZNK13QMdiSubWindow6widgetEv')
    return QWidget._cuteAt(address)

  def maximizedButtonsWidget(self) -> Optional[QWidget]:
    """
    Calls Qt's 'QWidget *QMdiSubWindow::maximizedButtonsWidget() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmdisubwindow.html#maximizedButtonsWidget

    Returns
    -------

    Optional[QWidget]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWidget *QMdiSubWindow::maximizedButtonsWidget() const
    address = self.uglySide.call(
        'ritual_ZNK13QMdiSubWindow22maximizedButtonsWidgetEv',
    )
    return QWidget._cuteAt(address)

  def maximizedSystemMenuIconWidget(self) -> Optional[QWidget]:
    """
    Calls Qt's 'QWidget *QMdiSubWindow::maximizedSystemMenuIconWidget()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmdisubwindow.html#maximizedSystemMenuIconWidget

    Returns
    -------

    Optional[QWidget]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWidget *QMdiSubWindow::maximizedSystemMenuIconWidget() const
    address = self.uglySide.call(
        'ritual_ZNK13QMdiSubWindow29maximizedSystemMenuIconWidgetEv',
    )
    return QWidget._cuteAt(address)

  def isShaded(self) -> bool:
    """
    Calls Qt's 'bool QMdiSubWindow::isShaded() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmdisubwindow.html#isShaded
    """
    #  bool QMdiSubWindow::isShaded() const
    return self.uglySide.call('ritual_ZNK13QMdiSubWindow8isShadedEv')

  @overload(SubWindowOption)
  def testOption(self, a0: SubWindowOption) -> bool:
    """
    Calls Qt's 'bool QMdiSubWindow::testOption(SubWindowOption a0) const'.

    Qt's own words: https://doc.qt.io/qt-6/qmdisubwindow.html#testOption

    Parameters
    ----------

    a0 : SubWindowOption
      Passed on as its number.
    """
    #  bool QMdiSubWindow::testOption(SubWindowOption a0) const
    return self.uglySide.call(
        'ritual_ZNK13QMdiSubWindow10testOptionENS_15SubWindowOptionE',
        a0.value,
    )

  def keyboardSingleStep(self) -> int:
    """
    Calls Qt's 'int QMdiSubWindow::keyboardSingleStep() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmdisubwindow.html#keyboardSingleStep
    """
    #  int QMdiSubWindow::keyboardSingleStep() const
    return self.uglySide.call(
        'ritual_ZNK13QMdiSubWindow18keyboardSingleStepEv',
    )

  def keyboardPageStep(self) -> int:
    """
    Calls Qt's 'int QMdiSubWindow::keyboardPageStep() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmdisubwindow.html#keyboardPageStep
    """
    #  int QMdiSubWindow::keyboardPageStep() const
    return self.uglySide.call(
        'ritual_ZNK13QMdiSubWindow16keyboardPageStepEv',
    )

  def systemMenu(self) -> Optional[QMenu]:
    """
    Calls Qt's 'QMenu *QMdiSubWindow::systemMenu() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmdisubwindow.html#systemMenu

    Returns
    -------

    Optional[QMenu]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QMenu *QMdiSubWindow::systemMenu() const
    address = self.uglySide.call('ritual_ZNK13QMdiSubWindow10systemMenuEv')
    from . import QMenu
    return QMenu._cuteAt(address)

  def mdiArea(self) -> Optional[QMdiArea]:
    """
    Calls Qt's 'QMdiArea *QMdiSubWindow::mdiArea() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmdisubwindow.html#mdiArea

    Returns
    -------

    Optional[QMdiArea]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QMdiArea *QMdiSubWindow::mdiArea() const
    address = self.uglySide.call('ritual_ZNK13QMdiSubWindow7mdiAreaEv')
    from . import QMdiArea
    return QMdiArea._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QWidget)
  @overload(NoneType)
  def setWidget(self, widget: Optional[QWidget]) -> None:
    """
    Calls Qt's 'void QMdiSubWindow::setWidget(QWidget *widget)'.

    Qt's own words: https://doc.qt.io/qt-6/qmdisubwindow.html#setWidget

    Parameters
    ----------

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QMdiSubWindow::setWidget(QWidget *widget)
    self.uglySide.call(
        'ritual_ZN13QMdiSubWindow9setWidgetEP7QWidget',
        self._addressOf(widget),
    )

  @overload(SubWindowOption)
  @overload(SubWindowOption, bool)
  def setOption(self, option: SubWindowOption, on: bool = True) -> None:
    """
    Calls Qt's 'void QMdiSubWindow::setOption(SubWindowOption option, bool
    on)'.

    Qt's own words: https://doc.qt.io/qt-6/qmdisubwindow.html#setOption

    Parameters
    ----------

    option : SubWindowOption
      Passed on as its number.

    on : bool
      Passed on as it is. May be left out, as in Qt: it is then True.
    """
    #  void QMdiSubWindow::setOption(SubWindowOption option, bool on)
    self.uglySide.call(
        'ritual_ZN13QMdiSubWindow9setOptionENS_15SubWindowOptionEb',
        option.value, on,
    )

  @overload(int)
  def setKeyboardSingleStep(self, step: int) -> None:
    """
    Calls Qt's 'void QMdiSubWindow::setKeyboardSingleStep(int step)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmdisubwindow.html#setKeyboardSingleStep

    Parameters
    ----------

    step : int
      Passed on as it is.
    """
    #  void QMdiSubWindow::setKeyboardSingleStep(int step)
    self.uglySide.call(
        'ritual_ZN13QMdiSubWindow21setKeyboardSingleStepEi', step,
    )

  @overload(int)
  def setKeyboardPageStep(self, step: int) -> None:
    """
    Calls Qt's 'void QMdiSubWindow::setKeyboardPageStep(int step)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmdisubwindow.html#setKeyboardPageStep

    Parameters
    ----------

    step : int
      Passed on as it is.
    """
    #  void QMdiSubWindow::setKeyboardPageStep(int step)
    self.uglySide.call(
        'ritual_ZN13QMdiSubWindow19setKeyboardPageStepEi', step,
    )

  @overload(QMenu)
  @overload(NoneType)
  def setSystemMenu(self, systemMenu: Optional[QMenu]) -> None:
    """
    Calls Qt's 'void QMdiSubWindow::setSystemMenu(QMenu *systemMenu)'.

    Qt's own words: https://doc.qt.io/qt-6/qmdisubwindow.html#setSystemMenu

    Parameters
    ----------

    systemMenu : Optional[QMenu]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QMdiSubWindow::setSystemMenu(QMenu *systemMenu)
    self.uglySide.call(
        'ritual_ZN13QMdiSubWindow13setSystemMenuEP5QMenu',
        self._addressOf(systemMenu),
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
      flags: Qt.WindowFlags = Qt.WindowFlags(),
  ) -> None:
    """
    Notes what was given, for Qt's 'QMdiSubWindow::QMdiSubWindow(QWidget
    *parent, Qt::WindowFlags flags)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qmdisubwindow.html#QMdiSubWindow

    Parameters
    ----------

    parent : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    flags : Qt.WindowFlags
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.WindowFlags().
    """
    #  QMdiSubWindow::QMdiSubWindow(QWidget *parent, Qt::WindowFlags flags)
    self._noteCreation(QMdiSubWindow, lambda: Rituals.call(
        'ritual_ZN13QMdiSubWindowC1EP7QWidget6QFlagsIN2Qt10WindowTypeEE',
        self._addressOf(parent), flags.value,
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

  def showSystemMenu(self) -> None:
    """
    Calls Qt's 'void QMdiSubWindow::showSystemMenu()'.

    Qt's own words: https://doc.qt.io/qt-6/qmdisubwindow.html#showSystemMenu
    """
    #  void QMdiSubWindow::showSystemMenu()
    self.uglySide.call('ritual_ZN13QMdiSubWindow14showSystemMenuEv')

  def showShaded(self) -> None:
    """
    Calls Qt's 'void QMdiSubWindow::showShaded()'.

    Qt's own words: https://doc.qt.io/qt-6/qmdisubwindow.html#showShaded
    """
    #  void QMdiSubWindow::showShaded()
    self.uglySide.call('ritual_ZN13QMdiSubWindow10showShadedEv')

  @overload(QObject, QEvent)
  @overload(QObject, NoneType)
  @overload(NoneType, QEvent)
  @overload(NoneType, NoneType)
  def eventFilter(
      self,
      object: Optional[QObject],
      event: Optional[QEvent],
  ) -> bool:
    """
    Calls Qt's 'bool QMdiSubWindow::eventFilter(QObject *object, QEvent
    *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qmdisubwindow.html#eventFilter

    Parameters
    ----------

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    event : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QMdiSubWindow::eventFilter(QObject *object, QEvent *event)
    ritual = 'ritual_ZN13QMdiSubWindow11eventFilterEP7QObjectP6QEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN13QMdiSubWindow11eventFilterEP7QObjectP6QEvent'
    return self.uglySide.call(
        ritual, self._addressOf(object), self._addressOf(event),
    )

  @overload(QEvent)
  @overload(NoneType)
  def event(self, event: Optional[QEvent]) -> bool:
    """
    Calls Qt's 'bool QMdiSubWindow::event(QEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qmdisubwindow.html#event

    Parameters
    ----------

    event : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QMdiSubWindow::event(QEvent *event)
    ritual = 'ritual_ZN13QMdiSubWindow5eventEP6QEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN13QMdiSubWindow5eventEP6QEvent'
    return self.uglySide.call(ritual, self._addressOf(event))

  @overload(QShowEvent)
  @overload(NoneType)
  def showEvent(self, showEvent: Optional[QShowEvent]) -> None:
    """
    Calls Qt's 'void QMdiSubWindow::showEvent(QShowEvent *showEvent)'.

    Qt's own words: https://doc.qt.io/qt-6/qmdisubwindow.html#showEvent

    Parameters
    ----------

    showEvent : Optional[QShowEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QMdiSubWindow::showEvent(QShowEvent *showEvent)
    ritual = 'ritual_ZN13QMdiSubWindow9showEventEP10QShowEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN13QMdiSubWindow9showEventEP10QShowEvent'
    self.uglySide.call(ritual, self._addressOf(showEvent))

  @overload(QHideEvent)
  @overload(NoneType)
  def hideEvent(self, hideEvent: Optional[QHideEvent]) -> None:
    """
    Calls Qt's 'void QMdiSubWindow::hideEvent(QHideEvent *hideEvent)'.

    Qt's own words: https://doc.qt.io/qt-6/qmdisubwindow.html#hideEvent

    Parameters
    ----------

    hideEvent : Optional[QHideEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QMdiSubWindow::hideEvent(QHideEvent *hideEvent)
    ritual = 'ritual_ZN13QMdiSubWindow9hideEventEP10QHideEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN13QMdiSubWindow9hideEventEP10QHideEvent'
    self.uglySide.call(ritual, self._addressOf(hideEvent))

  @overload(QEvent)
  @overload(NoneType)
  def changeEvent(self, changeEvent: Optional[QEvent]) -> None:
    """
    Calls Qt's 'void QMdiSubWindow::changeEvent(QEvent *changeEvent)'.

    Qt's own words: https://doc.qt.io/qt-6/qmdisubwindow.html#changeEvent

    Parameters
    ----------

    changeEvent : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QMdiSubWindow::changeEvent(QEvent *changeEvent)
    ritual = 'ritual_ZN13QMdiSubWindow11changeEventEP6QEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN13QMdiSubWindow11changeEventEP6QEvent'
    self.uglySide.call(ritual, self._addressOf(changeEvent))

  @overload(QCloseEvent)
  @overload(NoneType)
  def closeEvent(self, closeEvent: Optional[QCloseEvent]) -> None:
    """
    Calls Qt's 'void QMdiSubWindow::closeEvent(QCloseEvent *closeEvent)'.

    Qt's own words: https://doc.qt.io/qt-6/qmdisubwindow.html#closeEvent

    Parameters
    ----------

    closeEvent : Optional[QCloseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QMdiSubWindow::closeEvent(QCloseEvent *closeEvent)
    ritual = 'ritual_ZN13QMdiSubWindow10closeEventEP11QCloseEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN13QMdiSubWindow10closeEventEP11QCloseEvent'
    self.uglySide.call(ritual, self._addressOf(closeEvent))

  @overload(QEvent)
  @overload(NoneType)
  def leaveEvent(self, leaveEvent: Optional[QEvent]) -> None:
    """
    Calls Qt's 'void QMdiSubWindow::leaveEvent(QEvent *leaveEvent)'.

    Qt's own words: https://doc.qt.io/qt-6/qmdisubwindow.html#leaveEvent

    Parameters
    ----------

    leaveEvent : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QMdiSubWindow::leaveEvent(QEvent *leaveEvent)
    ritual = 'ritual_ZN13QMdiSubWindow10leaveEventEP6QEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN13QMdiSubWindow10leaveEventEP6QEvent'
    self.uglySide.call(ritual, self._addressOf(leaveEvent))

  @overload(QResizeEvent)
  @overload(NoneType)
  def resizeEvent(self, resizeEvent: Optional[QResizeEvent]) -> None:
    """
    Calls Qt's 'void QMdiSubWindow::resizeEvent(QResizeEvent *resizeEvent)'.

    Qt's own words: https://doc.qt.io/qt-6/qmdisubwindow.html#resizeEvent

    Parameters
    ----------

    resizeEvent : Optional[QResizeEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QMdiSubWindow::resizeEvent(QResizeEvent *resizeEvent)
    ritual = 'ritual_ZN13QMdiSubWindow11resizeEventEP12QResizeEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN13QMdiSubWindow11resizeEventEP12QResizeEvent'
    self.uglySide.call(ritual, self._addressOf(resizeEvent))

  @overload(QTimerEvent)
  @overload(NoneType)
  def timerEvent(self, timerEvent: Optional[QTimerEvent]) -> None:
    """
    Calls Qt's 'void QMdiSubWindow::timerEvent(QTimerEvent *timerEvent)'.

    Qt's own words: https://doc.qt.io/qt-6/qmdisubwindow.html#timerEvent

    Parameters
    ----------

    timerEvent : Optional[QTimerEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QMdiSubWindow::timerEvent(QTimerEvent *timerEvent)
    ritual = 'ritual_ZN13QMdiSubWindow10timerEventEP11QTimerEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN13QMdiSubWindow10timerEventEP11QTimerEvent'
    self.uglySide.call(ritual, self._addressOf(timerEvent))

  @overload(QMoveEvent)
  @overload(NoneType)
  def moveEvent(self, moveEvent: Optional[QMoveEvent]) -> None:
    """
    Calls Qt's 'void QMdiSubWindow::moveEvent(QMoveEvent *moveEvent)'.

    Qt's own words: https://doc.qt.io/qt-6/qmdisubwindow.html#moveEvent

    Parameters
    ----------

    moveEvent : Optional[QMoveEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QMdiSubWindow::moveEvent(QMoveEvent *moveEvent)
    ritual = 'ritual_ZN13QMdiSubWindow9moveEventEP10QMoveEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN13QMdiSubWindow9moveEventEP10QMoveEvent'
    self.uglySide.call(ritual, self._addressOf(moveEvent))

  @overload(QPaintEvent)
  @overload(NoneType)
  def paintEvent(self, paintEvent: Optional[QPaintEvent]) -> None:
    """
    Calls Qt's 'void QMdiSubWindow::paintEvent(QPaintEvent *paintEvent)'.

    Qt's own words: https://doc.qt.io/qt-6/qmdisubwindow.html#paintEvent

    Parameters
    ----------

    paintEvent : Optional[QPaintEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QMdiSubWindow::paintEvent(QPaintEvent *paintEvent)
    ritual = 'ritual_ZN13QMdiSubWindow10paintEventEP11QPaintEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN13QMdiSubWindow10paintEventEP11QPaintEvent'
    self.uglySide.call(ritual, self._addressOf(paintEvent))

  @overload(QMouseEvent)
  @overload(NoneType)
  def mousePressEvent(self, mouseEvent: Optional[QMouseEvent]) -> None:
    """
    Calls Qt's 'void QMdiSubWindow::mousePressEvent(QMouseEvent
    *mouseEvent)'.

    Qt's own words: https://doc.qt.io/qt-6/qmdisubwindow.html#mousePressEvent

    Parameters
    ----------

    mouseEvent : Optional[QMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QMdiSubWindow::mousePressEvent(QMouseEvent *mouseEvent)
    ritual = 'ritual_ZN13QMdiSubWindow15mousePressEventEP11QMouseEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN13QMdiSubWindow15mousePressEventEP11QMouseEvent'
    self.uglySide.call(ritual, self._addressOf(mouseEvent))

  @overload(QMouseEvent)
  @overload(NoneType)
  def mouseDoubleClickEvent(self, mouseEvent: Optional[QMouseEvent]) -> None:
    """
    Calls Qt's 'void QMdiSubWindow::mouseDoubleClickEvent(QMouseEvent
    *mouseEvent)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmdisubwindow.html#mouseDoubleClickEvent

    Parameters
    ----------

    mouseEvent : Optional[QMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QMdiSubWindow::mouseDoubleClickEvent(QMouseEvent *mouseEvent)
    ritual = 'ritual_ZN13QMdiSubWindow21mouseDoubleClickEventEP11QMouseEvent'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN13QMdiSubWindow21mouseDoubleClickEventEP11QMouseEve'
          'nt')
    self.uglySide.call(ritual, self._addressOf(mouseEvent))

  @overload(QMouseEvent)
  @overload(NoneType)
  def mouseReleaseEvent(self, mouseEvent: Optional[QMouseEvent]) -> None:
    """
    Calls Qt's 'void QMdiSubWindow::mouseReleaseEvent(QMouseEvent
    *mouseEvent)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmdisubwindow.html#mouseReleaseEvent

    Parameters
    ----------

    mouseEvent : Optional[QMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QMdiSubWindow::mouseReleaseEvent(QMouseEvent *mouseEvent)
    ritual = 'ritual_ZN13QMdiSubWindow17mouseReleaseEventEP11QMouseEvent'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN13QMdiSubWindow17mouseReleaseEventEP11QMouseEvent')
    self.uglySide.call(ritual, self._addressOf(mouseEvent))

  @overload(QMouseEvent)
  @overload(NoneType)
  def mouseMoveEvent(self, mouseEvent: Optional[QMouseEvent]) -> None:
    """
    Calls Qt's 'void QMdiSubWindow::mouseMoveEvent(QMouseEvent *mouseEvent)'.

    Qt's own words: https://doc.qt.io/qt-6/qmdisubwindow.html#mouseMoveEvent

    Parameters
    ----------

    mouseEvent : Optional[QMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QMdiSubWindow::mouseMoveEvent(QMouseEvent *mouseEvent)
    ritual = 'ritual_ZN13QMdiSubWindow14mouseMoveEventEP11QMouseEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN13QMdiSubWindow14mouseMoveEventEP11QMouseEvent'
    self.uglySide.call(ritual, self._addressOf(mouseEvent))

  @overload(QKeyEvent)
  @overload(NoneType)
  def keyPressEvent(self, keyEvent: Optional[QKeyEvent]) -> None:
    """
    Calls Qt's 'void QMdiSubWindow::keyPressEvent(QKeyEvent *keyEvent)'.

    Qt's own words: https://doc.qt.io/qt-6/qmdisubwindow.html#keyPressEvent

    Parameters
    ----------

    keyEvent : Optional[QKeyEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QMdiSubWindow::keyPressEvent(QKeyEvent *keyEvent)
    ritual = 'ritual_ZN13QMdiSubWindow13keyPressEventEP9QKeyEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN13QMdiSubWindow13keyPressEventEP9QKeyEvent'
    self.uglySide.call(ritual, self._addressOf(keyEvent))

  @overload(QContextMenuEvent)
  @overload(NoneType)
  def contextMenuEvent(
      self,
      contextMenuEvent: Optional[QContextMenuEvent],
  ) -> None:
    """
    Calls Qt's 'void QMdiSubWindow::contextMenuEvent(QContextMenuEvent
    *contextMenuEvent)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmdisubwindow.html#contextMenuEvent

    Parameters
    ----------

    contextMenuEvent : Optional[QContextMenuEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QMdiSubWindow::contextMenuEvent(QContextMenuEvent
    #      *contextMenuEvent)
    ritual = (
        'ritual_ZN13QMdiSubWindow16contextMenuEventEP17QContextMenuEvent')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN13QMdiSubWindow16contextMenuEventEP17QContextMenuEv'
          'ent')
    self.uglySide.call(ritual, self._addressOf(contextMenuEvent))

  @overload(QFocusEvent)
  @overload(NoneType)
  def focusInEvent(self, focusInEvent: Optional[QFocusEvent]) -> None:
    """
    Calls Qt's 'void QMdiSubWindow::focusInEvent(QFocusEvent *focusInEvent)'.

    Qt's own words: https://doc.qt.io/qt-6/qmdisubwindow.html#focusInEvent

    Parameters
    ----------

    focusInEvent : Optional[QFocusEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QMdiSubWindow::focusInEvent(QFocusEvent *focusInEvent)
    ritual = 'ritual_ZN13QMdiSubWindow12focusInEventEP11QFocusEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN13QMdiSubWindow12focusInEventEP11QFocusEvent'
    self.uglySide.call(ritual, self._addressOf(focusInEvent))

  @overload(QFocusEvent)
  @overload(NoneType)
  def focusOutEvent(self, focusOutEvent: Optional[QFocusEvent]) -> None:
    """
    Calls Qt's 'void QMdiSubWindow::focusOutEvent(QFocusEvent
    *focusOutEvent)'.

    Qt's own words: https://doc.qt.io/qt-6/qmdisubwindow.html#focusOutEvent

    Parameters
    ----------

    focusOutEvent : Optional[QFocusEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QMdiSubWindow::focusOutEvent(QFocusEvent *focusOutEvent)
    ritual = 'ritual_ZN13QMdiSubWindow13focusOutEventEP11QFocusEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN13QMdiSubWindow13focusOutEventEP11QFocusEvent'
    self.uglySide.call(ritual, self._addressOf(focusOutEvent))

  @overload(QChildEvent)
  @overload(NoneType)
  def childEvent(self, childEvent: Optional[QChildEvent]) -> None:
    """
    Calls Qt's 'void QMdiSubWindow::childEvent(QChildEvent *childEvent)'.

    Qt's own words: https://doc.qt.io/qt-6/qmdisubwindow.html#childEvent

    Parameters
    ----------

    childEvent : Optional[QChildEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QMdiSubWindow::childEvent(QChildEvent *childEvent)
    ritual = 'ritual_ZN13QMdiSubWindow10childEventEP11QChildEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN13QMdiSubWindow10childEventEP11QChildEvent'
    self.uglySide.call(ritual, self._addressOf(childEvent))


#  Qt's 'QList<QMdiSubWindow *>': the list of QMdiSubWindow, which
#  'QList[QMdiSubWindow]' gives. It is made here, so that there is one as
#  soon as there can be a QMdiSubWindow.
QList.createKind(
    QMdiSubWindow, 'address',
    make='ritual_list_make_QMdiSubWindow_ptr',
    add='ritual_list_add_QMdiSubWindow_ptr',
    size='ritual_list_size_QMdiSubWindow_ptr',
    at='ritual_list_at_QMdiSubWindow_ptr',
    drop='ritual_list_drop_QMdiSubWindow_ptr',
)
