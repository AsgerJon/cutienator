"""
QMdiArea binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/qmdiarea.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteFlags, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import Qt
from . import QAbstractScrollArea, QTabWidget, QWidget

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QSize
  from ..QtGui import QBrush
  from . import QMdiSubWindow
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QBrush = WAIT['QBrush']
  QMdiSubWindow = WAIT['QMdiSubWindow']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QMdiArea(QAbstractScrollArea):
  """
  The cute side of Qt's QMdiArea: a plain Python object standing in front of
  one C++ QMdiArea.

  It is built on the cute 'QAbstractScrollArea', as Qt's QMdiArea is built on
  Qt's QAbstractScrollArea, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QMdiArea that has a ritual and that Python can call
  so far, 33 names in all: 'metaObject', 'tr', 'sizeHint', 'minimumSizeHint',
  'currentSubWindow', 'activeSubWindow', 'addSubWindow', 'removeSubWindow',
  'background', 'setBackground', 'activationOrder', 'setActivationOrder',
  'setOption', 'testOption', 'setViewMode', 'viewMode', 'documentMode',
  'setDocumentMode', 'setTabsClosable', 'tabsClosable', 'setTabsMovable',
  'tabsMovable', 'setTabShape', 'tabShape', 'setTabPosition', 'tabPosition',
  'setActiveSubWindow', 'tileSubWindows', 'cascadeSubWindows',
  'closeActiveSubWindow', 'closeAllSubWindows', 'activateNextSubWindow',
  'activatePreviousSubWindow'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QMdiArea::~QMdiArea()': the destructor: Python never removes a C++
    QMdiArea.

  What has no ritual
  ------------------

  20 of the 55 functions Qt declares: 10 protected; 3 takes or gives a type
  that cannot be passed yet; 3 private; 2 forbidden; 1 a template; 1 a
  signal.

  What to expect
  --------------

  - The C++ QMdiArea is created at the first use, not by 'QMdiArea(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QMdiArea.
  - Qt tells when it has removed the C++ QMdiArea. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
  """

  #  The enums Qt writes inside QMdiArea, each a class in here as in C++, and
  #  the names Qt has for the combinations of its flags enums.

  class AreaOption(CuteFlags):
    """
    The flags enum 'QMdiArea::AreaOption' of Qt, with the 1 names Qt gives in
    it. Qt names the type of its combinations 'QMdiArea::AreaOptions'.
    """

    DontMaximizeSubWindowOnActivation = 0x1

  AreaOptions = AreaOption

  class ViewMode(CuteNum):
    """
    The enum 'QMdiArea::ViewMode' of Qt, with the 2 names Qt gives in it.
    """

    SubWindowView = Kee[int](0)
    TabbedView = Kee[int](1)

  class WindowOrder(CuteNum):
    """
    The enum 'QMdiArea::WindowOrder' of Qt, with the 3 names Qt gives in it.
    """

    CreationOrder = Kee[int](0)
    StackingOrder = Kee[int](1)
    ActivationHistoryOrder = Kee[int](2)

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
    Calls Qt's 'QString QMdiArea::tr(const char *s, const char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qmdiarea.html#tr

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
    #  QString QMdiArea::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN8QMdiArea2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QMdiArea'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QMdiArea::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmdiarea.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QMdiArea::metaObject() const
    address = self.uglySide.call('ritual_ZNK8QMdiArea10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def sizeHint(self) -> QSize:
    """
    Calls Qt's 'QSize QMdiArea::sizeHint() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmdiarea.html#sizeHint

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QMdiArea::sizeHint() const
    address = self.uglySide.call('ritual_ZNK8QMdiArea8sizeHintEv')
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  def minimumSizeHint(self) -> QSize:
    """
    Calls Qt's 'QSize QMdiArea::minimumSizeHint() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmdiarea.html#minimumSizeHint

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QMdiArea::minimumSizeHint() const
    address = self.uglySide.call('ritual_ZNK8QMdiArea15minimumSizeHintEv')
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  def currentSubWindow(self) -> Optional[QMdiSubWindow]:
    """
    Calls Qt's 'QMdiSubWindow *QMdiArea::currentSubWindow() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmdiarea.html#currentSubWindow

    Returns
    -------

    Optional[QMdiSubWindow]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QMdiSubWindow *QMdiArea::currentSubWindow() const
    address = self.uglySide.call('ritual_ZNK8QMdiArea16currentSubWindowEv')
    from . import QMdiSubWindow
    return QMdiSubWindow._cuteAt(address)

  def activeSubWindow(self) -> Optional[QMdiSubWindow]:
    """
    Calls Qt's 'QMdiSubWindow *QMdiArea::activeSubWindow() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmdiarea.html#activeSubWindow

    Returns
    -------

    Optional[QMdiSubWindow]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QMdiSubWindow *QMdiArea::activeSubWindow() const
    address = self.uglySide.call('ritual_ZNK8QMdiArea15activeSubWindowEv')
    from . import QMdiSubWindow
    return QMdiSubWindow._cuteAt(address)

  def background(self) -> QBrush:
    """
    Calls Qt's 'QBrush QMdiArea::background() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmdiarea.html#background

    Returns
    -------

    QBrush
      A new cute QBrush around the copy Qt gave back. Python owns it.
    """
    #  QBrush QMdiArea::background() const
    address = self.uglySide.call('ritual_ZNK8QMdiArea10backgroundEv')
    from ..QtGui import QBrush
    return QBrush._cuteOwning(address)

  def activationOrder(self) -> WindowOrder:
    """
    Calls Qt's 'WindowOrder QMdiArea::activationOrder() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmdiarea.html#activationOrder

    Returns
    -------

    WindowOrder
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'WindowOrder(number)'
      gives.
    """
    #  WindowOrder QMdiArea::activationOrder() const
    return QMdiArea.WindowOrder(self.uglySide.call(
        'ritual_ZNK8QMdiArea15activationOrderEv',
    ))

  @overload(AreaOption)
  def testOption(self, opton: AreaOption) -> bool:
    """
    Calls Qt's 'bool QMdiArea::testOption(AreaOption opton) const'.

    Qt's own words: https://doc.qt.io/qt-6/qmdiarea.html#testOption

    Parameters
    ----------

    opton : AreaOption
      Passed on as its number.
    """
    #  bool QMdiArea::testOption(AreaOption opton) const
    return self.uglySide.call(
        'ritual_ZNK8QMdiArea10testOptionENS_10AreaOptionE', opton.value,
    )

  def viewMode(self) -> ViewMode:
    """
    Calls Qt's 'ViewMode QMdiArea::viewMode() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmdiarea.html#viewMode

    Returns
    -------

    ViewMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'ViewMode(number)' gives.
    """
    #  ViewMode QMdiArea::viewMode() const
    return QMdiArea.ViewMode(self.uglySide.call(
        'ritual_ZNK8QMdiArea8viewModeEv',
    ))

  def documentMode(self) -> bool:
    """
    Calls Qt's 'bool QMdiArea::documentMode() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmdiarea.html#documentMode
    """
    #  bool QMdiArea::documentMode() const
    return self.uglySide.call('ritual_ZNK8QMdiArea12documentModeEv')

  def tabsClosable(self) -> bool:
    """
    Calls Qt's 'bool QMdiArea::tabsClosable() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmdiarea.html#tabsClosable
    """
    #  bool QMdiArea::tabsClosable() const
    return self.uglySide.call('ritual_ZNK8QMdiArea12tabsClosableEv')

  def tabsMovable(self) -> bool:
    """
    Calls Qt's 'bool QMdiArea::tabsMovable() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmdiarea.html#tabsMovable
    """
    #  bool QMdiArea::tabsMovable() const
    return self.uglySide.call('ritual_ZNK8QMdiArea11tabsMovableEv')

  def tabShape(self) -> QTabWidget.TabShape:
    """
    Calls Qt's 'QTabWidget::TabShape QMdiArea::tabShape() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmdiarea.html#tabShape

    Returns
    -------

    QTabWidget.TabShape
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QTabWidget.TabShape(number)' gives.
    """
    #  QTabWidget::TabShape QMdiArea::tabShape() const
    return QTabWidget.TabShape(self.uglySide.call(
        'ritual_ZNK8QMdiArea8tabShapeEv',
    ))

  def tabPosition(self) -> QTabWidget.TabPosition:
    """
    Calls Qt's 'QTabWidget::TabPosition QMdiArea::tabPosition() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmdiarea.html#tabPosition

    Returns
    -------

    QTabWidget.TabPosition
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QTabWidget.TabPosition(number)' gives.
    """
    #  QTabWidget::TabPosition QMdiArea::tabPosition() const
    return QTabWidget.TabPosition(self.uglySide.call(
        'ritual_ZNK8QMdiArea11tabPositionEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QBrush)
  def setBackground(self, background: QBrush) -> None:
    """
    Calls Qt's 'void QMdiArea::setBackground(const QBrush &background)'.

    Qt's own words: https://doc.qt.io/qt-6/qmdiarea.html#setBackground

    Parameters
    ----------

    background : QBrush
      Passed on as a value: Qt reads the C++ QBrush, which stays Python's
      own.
    """
    #  void QMdiArea::setBackground(const QBrush &background)
    self.uglySide.call(
        'ritual_ZN8QMdiArea13setBackgroundERK6QBrush',
        self._valueOf(background),
    )

  @overload(WindowOrder)
  def setActivationOrder(self, order: WindowOrder) -> None:
    """
    Calls Qt's 'void QMdiArea::setActivationOrder(WindowOrder order)'.

    Qt's own words: https://doc.qt.io/qt-6/qmdiarea.html#setActivationOrder

    Parameters
    ----------

    order : WindowOrder
      Passed on as its number.
    """
    #  void QMdiArea::setActivationOrder(WindowOrder order)
    self.uglySide.call(
        'ritual_ZN8QMdiArea18setActivationOrderENS_11WindowOrderE',
        order.value,
    )

  @overload(AreaOption)
  @overload(AreaOption, bool)
  def setOption(self, option: AreaOption, on: bool = True) -> None:
    """
    Calls Qt's 'void QMdiArea::setOption(AreaOption option, bool on)'.

    Qt's own words: https://doc.qt.io/qt-6/qmdiarea.html#setOption

    Parameters
    ----------

    option : AreaOption
      Passed on as its number.

    on : bool
      Passed on as it is. May be left out, as in Qt: it is then True.
    """
    #  void QMdiArea::setOption(AreaOption option, bool on)
    self.uglySide.call(
        'ritual_ZN8QMdiArea9setOptionENS_10AreaOptionEb', option.value, on,
    )

  @overload(ViewMode)
  def setViewMode(self, mode: ViewMode) -> None:
    """
    Calls Qt's 'void QMdiArea::setViewMode(ViewMode mode)'.

    Qt's own words: https://doc.qt.io/qt-6/qmdiarea.html#setViewMode

    Parameters
    ----------

    mode : ViewMode
      Passed on as its number.
    """
    #  void QMdiArea::setViewMode(ViewMode mode)
    self.uglySide.call(
        'ritual_ZN8QMdiArea11setViewModeENS_8ViewModeE', mode.value,
    )

  @overload(bool)
  def setDocumentMode(self, enabled: bool) -> None:
    """
    Calls Qt's 'void QMdiArea::setDocumentMode(bool enabled)'.

    Qt's own words: https://doc.qt.io/qt-6/qmdiarea.html#setDocumentMode

    Parameters
    ----------

    enabled : bool
      Passed on as it is.
    """
    #  void QMdiArea::setDocumentMode(bool enabled)
    self.uglySide.call('ritual_ZN8QMdiArea15setDocumentModeEb', enabled)

  @overload(bool)
  def setTabsClosable(self, closable: bool) -> None:
    """
    Calls Qt's 'void QMdiArea::setTabsClosable(bool closable)'.

    Qt's own words: https://doc.qt.io/qt-6/qmdiarea.html#setTabsClosable

    Parameters
    ----------

    closable : bool
      Passed on as it is.
    """
    #  void QMdiArea::setTabsClosable(bool closable)
    self.uglySide.call('ritual_ZN8QMdiArea15setTabsClosableEb', closable)

  @overload(bool)
  def setTabsMovable(self, movable: bool) -> None:
    """
    Calls Qt's 'void QMdiArea::setTabsMovable(bool movable)'.

    Qt's own words: https://doc.qt.io/qt-6/qmdiarea.html#setTabsMovable

    Parameters
    ----------

    movable : bool
      Passed on as it is.
    """
    #  void QMdiArea::setTabsMovable(bool movable)
    self.uglySide.call('ritual_ZN8QMdiArea14setTabsMovableEb', movable)

  @overload(QTabWidget.TabShape)
  def setTabShape(self, shape: QTabWidget.TabShape) -> None:
    """
    Calls Qt's 'void QMdiArea::setTabShape(QTabWidget::TabShape shape)'.

    Qt's own words: https://doc.qt.io/qt-6/qmdiarea.html#setTabShape

    Parameters
    ----------

    shape : QTabWidget.TabShape
      Passed on as its number.
    """
    #  void QMdiArea::setTabShape(QTabWidget::TabShape shape)
    self.uglySide.call(
        'ritual_ZN8QMdiArea11setTabShapeEN10QTabWidget8TabShapeE',
        shape.value,
    )

  @overload(QTabWidget.TabPosition)
  def setTabPosition(self, position: QTabWidget.TabPosition) -> None:
    """
    Calls Qt's 'void QMdiArea::setTabPosition(QTabWidget::TabPosition
    position)'.

    Qt's own words: https://doc.qt.io/qt-6/qmdiarea.html#setTabPosition

    Parameters
    ----------

    position : QTabWidget.TabPosition
      Passed on as its number.
    """
    #  void QMdiArea::setTabPosition(QTabWidget::TabPosition position)
    self.uglySide.call(
        'ritual_ZN8QMdiArea14setTabPositionEN10QTabWidget11TabPositionE',
        position.value,
    )

  @overload(QMdiSubWindow)
  @overload(NoneType)
  def setActiveSubWindow(self, window: Optional[QMdiSubWindow]) -> None:
    """
    Calls Qt's 'void QMdiArea::setActiveSubWindow(QMdiSubWindow *window)'.

    Qt's own words: https://doc.qt.io/qt-6/qmdiarea.html#setActiveSubWindow

    Parameters
    ----------

    window : Optional[QMdiSubWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QMdiArea::setActiveSubWindow(QMdiSubWindow *window)
    self.uglySide.call(
        'ritual_ZN8QMdiArea18setActiveSubWindowEP13QMdiSubWindow',
        self._addressOf(window),
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
  def __init__(self, parent: Optional[QWidget] = None) -> None:
    """
    Notes what was given, for Qt's 'QMdiArea::QMdiArea(QWidget *parent)',
    which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qmdiarea.html#QMdiArea

    Parameters
    ----------

    parent : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QMdiArea::QMdiArea(QWidget *parent)
    self._noteCreation(QMdiArea, lambda: Rituals.call(
        'ritual_ZN8QMdiAreaC1EP7QWidget', self._addressOf(parent),
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

  @overload(QWidget)
  @overload(NoneType)
  @overload(QWidget, Qt.WindowFlags)
  @overload(NoneType, Qt.WindowFlags)
  def addSubWindow(
      self,
      widget: Optional[QWidget],
      flags: Qt.WindowFlags = Qt.WindowFlags(),
  ) -> Optional[QMdiSubWindow]:
    """
    Calls Qt's 'QMdiSubWindow *QMdiArea::addSubWindow(QWidget *widget,
    Qt::WindowFlags flags)'.

    Qt's own words: https://doc.qt.io/qt-6/qmdiarea.html#addSubWindow

    Parameters
    ----------

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    flags : Qt.WindowFlags
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.WindowFlags().

    Returns
    -------

    Optional[QMdiSubWindow]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QMdiSubWindow *QMdiArea::addSubWindow(QWidget *widget, Qt::WindowFlags
    #      flags)
    address = self.uglySide.call(
        'ritual_ZN8QMdiArea12addSubWindowEP7QWidget6QFlagsIN2Qt10WindowType'
        'EE',
        self._addressOf(widget), flags.value,
    )
    from . import QMdiSubWindow
    return QMdiSubWindow._cuteAt(address)

  @overload(QWidget)
  @overload(NoneType)
  def removeSubWindow(self, widget: Optional[QWidget]) -> None:
    """
    Calls Qt's 'void QMdiArea::removeSubWindow(QWidget *widget)'.

    Qt's own words: https://doc.qt.io/qt-6/qmdiarea.html#removeSubWindow

    Parameters
    ----------

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QMdiArea::removeSubWindow(QWidget *widget)
    self.uglySide.call(
        'ritual_ZN8QMdiArea15removeSubWindowEP7QWidget',
        self._addressOf(widget),
    )

  def tileSubWindows(self) -> None:
    """
    Calls Qt's 'void QMdiArea::tileSubWindows()'.

    Qt's own words: https://doc.qt.io/qt-6/qmdiarea.html#tileSubWindows
    """
    #  void QMdiArea::tileSubWindows()
    self.uglySide.call('ritual_ZN8QMdiArea14tileSubWindowsEv')

  def cascadeSubWindows(self) -> None:
    """
    Calls Qt's 'void QMdiArea::cascadeSubWindows()'.

    Qt's own words: https://doc.qt.io/qt-6/qmdiarea.html#cascadeSubWindows
    """
    #  void QMdiArea::cascadeSubWindows()
    self.uglySide.call('ritual_ZN8QMdiArea17cascadeSubWindowsEv')

  def closeActiveSubWindow(self) -> None:
    """
    Calls Qt's 'void QMdiArea::closeActiveSubWindow()'.

    Qt's own words: https://doc.qt.io/qt-6/qmdiarea.html#closeActiveSubWindow
    """
    #  void QMdiArea::closeActiveSubWindow()
    self.uglySide.call('ritual_ZN8QMdiArea20closeActiveSubWindowEv')

  def closeAllSubWindows(self) -> None:
    """
    Calls Qt's 'void QMdiArea::closeAllSubWindows()'.

    Qt's own words: https://doc.qt.io/qt-6/qmdiarea.html#closeAllSubWindows
    """
    #  void QMdiArea::closeAllSubWindows()
    self.uglySide.call('ritual_ZN8QMdiArea18closeAllSubWindowsEv')

  def activateNextSubWindow(self) -> None:
    """
    Calls Qt's 'void QMdiArea::activateNextSubWindow()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmdiarea.html#activateNextSubWindow
    """
    #  void QMdiArea::activateNextSubWindow()
    self.uglySide.call('ritual_ZN8QMdiArea21activateNextSubWindowEv')

  def activatePreviousSubWindow(self) -> None:
    """
    Calls Qt's 'void QMdiArea::activatePreviousSubWindow()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmdiarea.html#activatePreviousSubWindow
    """
    #  void QMdiArea::activatePreviousSubWindow()
    self.uglySide.call('ritual_ZN8QMdiArea25activatePreviousSubWindowEv')
