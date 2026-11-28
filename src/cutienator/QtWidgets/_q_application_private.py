"""
QApplicationPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/6.12.0/QtWidgets/private/qapplication_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QApplicationPrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import Qt, QEvent
from ..QtGui import QGuiApplicationPrivate, QIcon

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QObject, QPoint, QPointF, QPostEventList
  from ..QtGui import QActionPrivate, QDrag, QEventPoint, QFont, QPalette
  from ..QtGui import QPixmap, QPointingDevice, QShortcutPrivate, QTouchEvent
  from ..QtGui import QWindow
  from . import QApplication, QWidget
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDrag = WAIT['QDrag']
  QEventPoint = WAIT['QEventPoint']
  QFont = WAIT['QFont']
  QObject = WAIT['QObject']
  QPixmap = WAIT['QPixmap']
  QPoint = WAIT['QPoint']
  QPointF = WAIT['QPointF']
  QPointingDevice = WAIT['QPointingDevice']
  QPostEventList = WAIT['QPostEventList']
  QTouchEvent = WAIT['QTouchEvent']
  QWidget = WAIT['QWidget']
  QWindow = WAIT['QWindow']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QApplicationPrivate(QGuiApplicationPrivate):
  """
  The cute side of Qt's QApplicationPrivate: a plain Python object standing
  in front of one C++ QApplicationPrivate.

  It is built on the cute 'QGuiApplicationPrivate', as Qt's
  QApplicationPrivate is built on Qt's QGuiApplicationPrivate, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QApplicationPrivate that has a ritual and that
  Python can call so far, 47 names in all: 'q_func',
  'notifyLayoutDirectionChange', 'notifyActiveWindowChange',
  'desktopStyleKey', 'createEventDispatcher', 'dispatchEnterLeave',
  'notifyWindowIconChanged', 'compressEvent', 'createActionPrivate',
  'createShortcutPrivate', 'defaultModality', 'windowNeverBlocked',
  'isBlockedByModal', 'modalState', 'notify_helper', 'init', 'initialize',
  'process_cmdline', 'setActiveWindow', 'inPopupMode', 'closePopup',
  'openPopup', 'setFocusWidget', 'handleThemeChanged', 'basePalette',
  'handlePaletteChanged', 'notifyDragStarted',
  'initializeWidgetPalettesFromTheme', 'initializeWidgetFontHash',
  'setSystemFont', 'instance', 'pickMouseReceiver',
  'sendSyntheticEnterLeave', 'windowForWidget', 'updateTouchPointsForWidget',
  'initializeMultitouch', 'initializeMultitouch_sys', 'cleanupMultitouch',
  'cleanupMultitouch_sys', 'findClosestTouchPointTarget',
  'activateImplicitTouchGrab', 'translateRawTouchEvent',
  'translateTouchCancel', 'applyQIconStyleHelper',
  'giveFocusAccordingToFocusPolicy', 'shouldSetFocus', 'isAlien'. It can be
  made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QApplication *QApplicationPrivate::q_func() const': takes in
    Python what 'QApplication *QApplicationPrivate::q_func()' takes.
  - Qt's 'QApplicationPrivate::~QApplicationPrivate()': the destructor:
    Python never removes a C++ QApplicationPrivate.
  - Qt's 'bool QApplicationPrivate::tryModalHelper(QWidget *widget, QWidget
    **rettop)': takes a type Python has no way to hand over yet.
  - Qt's 'QWidget *QApplicationPrivate::focusNextPrevChild_helper(QWidget
    *toplevel, bool next, bool *wrappingOccurred)': takes a number to change
    where it is.
  - Qt's 'bool QApplicationPrivate::sendMouseEvent(QWidget *receiver,
    QMouseEvent *event, QWidget *alienWidget, QWidget *native, QWidget
    **buttonDown, QPointer<QWidget> &lastMouseReceiver, bool spontaneous,
    bool onlyDispatchEnterLeave)': takes a type Python has no way to hand
    over yet.
  - Qt's 'bool QApplicationPrivate::tryCloseAllWidgetWindows(QWindowList
    *processedWindows)': names 'QWindowList', which has no cute class yet.

  What has no ritual
  ------------------

  3 of the 57 functions Qt declares: 3 cannot be called and cannot be called
  through the meta-object and cannot be copied.

  What to expect
  --------------

  - The C++ QApplicationPrivate is created at the first use, not by
    'QApplicationPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QApplicationPrivate.
  - Each name of Qt's QApplicationPrivate that has no cute function yet,
    'appendTouchPoint', 'desktop', 'focusNextPrevChild_helper',
    'removeTouchPoint', 'sendMouseEvent', 'tryCloseAllWidgetWindows',
    'tryModalHelper', holds a function that raises 'NotImplementedError', and
    its docstring says why.
  """

  #  The enums Qt writes inside QApplicationPrivate, each a class in here as
  #  in C++, and the names Qt has for the combinations of its flags enums.

  class ImplicitTouchGrabMode(CuteNum):
    """
    The enum 'QApplicationPrivate::ImplicitTouchGrabMode' of Qt, with the 2
    names Qt gives in it.
    """

    GrabAcceptedPoints = Kee[int](0)
    GrabAllPoints = Kee[int](1)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def desktopStyleKey() -> str:
    """
    Calls Qt's 'QString QApplicationPrivate::desktopStyleKey()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qapplicationprivate.html#desktopStyleKey

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QApplicationPrivate::desktopStyleKey()
    return Rituals.call('ritual_ZN19QApplicationPrivate15desktopStyleKeyEv')

  @staticmethod
  @overload(QWidget, QWidget, QPointF)
  @overload(QWidget, NoneType, QPointF)
  @overload(NoneType, QWidget, QPointF)
  @overload(NoneType, NoneType, QPointF)
  def dispatchEnterLeave(
      enter: Optional[QWidget],
      leave: Optional[QWidget],
      globalPosF: QPointF,
  ) -> None:
    """
    Calls Qt's 'void QApplicationPrivate::dispatchEnterLeave(QWidget *enter,
    QWidget *leave, const QPointF &globalPosF)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qapplicationprivate.html#dispatchEnterLeave

    Parameters
    ----------

    enter : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    leave : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    globalPosF : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  void QApplicationPrivate::dispatchEnterLeave(QWidget *enter, QWidget
    #      *leave, const QPointF &globalPosF)
    Rituals.call(
        'ritual_ZN19QApplicationPrivate18dispatchEnterLeaveEP7QWidgetS1_RK7'
        'QPointF',
        CuteMixin._addressOf(enter), CuteMixin._addressOf(leave),
        CuteMixin._valueOf(globalPosF, 'QPointF'),
    )

  @staticmethod
  @overload(QWidget)
  @overload(NoneType)
  def isBlockedByModal(widget: Optional[QWidget]) -> bool:
    """
    Calls Qt's 'bool QApplicationPrivate::isBlockedByModal(QWidget *widget)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qapplicationprivate.html#isBlockedByModal

    Parameters
    ----------

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QApplicationPrivate::isBlockedByModal(QWidget *widget)
    return Rituals.call(
        'ritual_ZN19QApplicationPrivate16isBlockedByModalEP7QWidget',
        CuteMixin._addressOf(widget),
    )

  @staticmethod
  def modalState() -> bool:
    """
    Calls Qt's 'bool QApplicationPrivate::modalState()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qapplicationprivate.html#modalState
    """
    #  bool QApplicationPrivate::modalState()
    return Rituals.call('ritual_ZN19QApplicationPrivate10modalStateEv')

  @staticmethod
  @overload(QWidget)
  @overload(NoneType)
  def setActiveWindow(act: Optional[QWidget]) -> None:
    """
    Calls Qt's 'void QApplicationPrivate::setActiveWindow(QWidget *act)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qapplicationprivate.html#setActiveWindow

    Parameters
    ----------

    act : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QApplicationPrivate::setActiveWindow(QWidget *act)
    Rituals.call(
        'ritual_ZN19QApplicationPrivate15setActiveWindowEP7QWidget',
        CuteMixin._addressOf(act),
    )

  @staticmethod
  def inPopupMode() -> bool:
    """
    Calls Qt's 'bool QApplicationPrivate::inPopupMode()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qapplicationprivate.html#inPopupMode
    """
    #  bool QApplicationPrivate::inPopupMode()
    return Rituals.call('ritual_ZN19QApplicationPrivate11inPopupModeEv')

  @staticmethod
  @overload(QWidget, Qt.FocusReason)
  @overload(NoneType, Qt.FocusReason)
  def setFocusWidget(
      focus: Optional[QWidget],
      reason: Qt.FocusReason,
  ) -> None:
    """
    Calls Qt's 'void QApplicationPrivate::setFocusWidget(QWidget *focus,
    Qt::FocusReason reason)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qapplicationprivate.html#setFocusWidget

    Parameters
    ----------

    focus : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    reason : Qt.FocusReason
      Passed on as its number.
    """
    #  void QApplicationPrivate::setFocusWidget(QWidget *focus,
    #      Qt::FocusReason reason)
    Rituals.call(
        'ritual_ZN19QApplicationPrivate14setFocusWidgetEP7QWidgetN2Qt11Focu'
        'sReasonE',
        CuteMixin._addressOf(focus), reason.value,
    )

  @staticmethod
  def initializeWidgetPalettesFromTheme() -> None:
    """
    Calls Qt's 'void
    QApplicationPrivate::initializeWidgetPalettesFromTheme()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qapplicationprivate.html
    """
    #  void QApplicationPrivate::initializeWidgetPalettesFromTheme()
    Rituals.call(
        'ritual_ZN19QApplicationPrivate33initializeWidgetPalettesFromThemeE'
        'v',
    )

  @staticmethod
  def initializeWidgetFontHash() -> None:
    """
    Calls Qt's 'void QApplicationPrivate::initializeWidgetFontHash()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qapplicationprivate.html#initializeWidgetFontHash
    """
    #  void QApplicationPrivate::initializeWidgetFontHash()
    Rituals.call(
        'ritual_ZN19QApplicationPrivate24initializeWidgetFontHashEv',
    )

  @staticmethod
  @overload(QFont)
  def setSystemFont(font: QFont) -> None:
    """
    Calls Qt's 'void QApplicationPrivate::setSystemFont(const QFont &font)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qapplicationprivate.html#setSystemFont

    Parameters
    ----------

    font : QFont
      Passed on as a value: Qt reads the C++ QFont, which stays Python's own.
    """
    #  void QApplicationPrivate::setSystemFont(const QFont &font)
    Rituals.call(
        'ritual_ZN19QApplicationPrivate13setSystemFontERK5QFont',
        CuteMixin._valueOf(font),
    )

  @staticmethod
  def instance() -> Optional[QApplicationPrivate]:
    """
    Calls Qt's 'QApplicationPrivate *QApplicationPrivate::instance()'.

    Qt's own words: https://doc.qt.io/qt-6/qapplicationprivate.html#instance

    Returns
    -------

    Optional[QApplicationPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QApplicationPrivate *QApplicationPrivate::instance()
    address = Rituals.call('ritual_ZN19QApplicationPrivate8instanceEv')
    return QApplicationPrivate._cuteAt(address)

  @staticmethod
  @overload(
      QWidget, QPointF, QPointF, QEvent.Type, Qt.MouseButtons, QWidget,
      QWidget,
  )
  @overload(
      QWidget, QPointF, QPointF, QEvent.Type, Qt.MouseButtons, QWidget,
      NoneType,
  )
  @overload(
      QWidget, QPointF, QPointF, QEvent.Type, Qt.MouseButtons, NoneType,
      QWidget,
  )
  @overload(
      QWidget, QPointF, QPointF, QEvent.Type, Qt.MouseButtons, NoneType,
      NoneType,
  )
  @overload(
      QWidget, QPointF, NoneType, QEvent.Type, Qt.MouseButtons, QWidget,
      QWidget,
  )
  @overload(
      QWidget, QPointF, NoneType, QEvent.Type, Qt.MouseButtons, QWidget,
      NoneType,
  )
  @overload(
      QWidget, QPointF, NoneType, QEvent.Type, Qt.MouseButtons, NoneType,
      QWidget,
  )
  @overload(
      QWidget, QPointF, NoneType, QEvent.Type, Qt.MouseButtons, NoneType,
      NoneType,
  )
  @overload(
      NoneType, QPointF, QPointF, QEvent.Type, Qt.MouseButtons, QWidget,
      QWidget,
  )
  @overload(
      NoneType, QPointF, QPointF, QEvent.Type, Qt.MouseButtons, QWidget,
      NoneType,
  )
  @overload(
      NoneType, QPointF, QPointF, QEvent.Type, Qt.MouseButtons, NoneType,
      QWidget,
  )
  @overload(
      NoneType, QPointF, QPointF, QEvent.Type, Qt.MouseButtons, NoneType,
      NoneType,
  )
  @overload(
      NoneType, QPointF, NoneType, QEvent.Type, Qt.MouseButtons, QWidget,
      QWidget,
  )
  @overload(
      NoneType, QPointF, NoneType, QEvent.Type, Qt.MouseButtons, QWidget,
      NoneType,
  )
  @overload(
      NoneType, QPointF, NoneType, QEvent.Type, Qt.MouseButtons, NoneType,
      QWidget,
  )
  @overload(
      NoneType, QPointF, NoneType, QEvent.Type, Qt.MouseButtons, NoneType,
      NoneType,
  )
  def pickMouseReceiver(
      candidate: Optional[QWidget],
      windowPos: QPointF,
      pos: Optional[QPointF],
      type: QEvent.Type,
      buttons: Qt.MouseButtons,
      buttonDown: Optional[QWidget],
      alienWidget: Optional[QWidget],
  ) -> Optional[QWidget]:
    """
    Calls Qt's 'QWidget *QApplicationPrivate::pickMouseReceiver(QWidget
    *candidate, const QPointF &windowPos, QPointF *pos, QEvent::Type type,
    Qt::MouseButtons buttons, QWidget *buttonDown, QWidget *alienWidget)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qapplicationprivate.html#pickMouseReceiver

    Parameters
    ----------

    candidate : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    windowPos : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    pos : Optional[QPointF]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    type : QEvent.Type
      Passed on as its number.

    buttons : Qt.MouseButtons
      Passed on as its number.

    buttonDown : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    alienWidget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QWidget]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWidget *QApplicationPrivate::pickMouseReceiver(QWidget *candidate,
    #      const QPointF &windowPos, QPointF *pos, QEvent::Type type,
    #      Qt::MouseButtons buttons, QWidget *buttonDown, QWidget
    #      *alienWidget)
    address = Rituals.call(
        'ritual_ZN19QApplicationPrivate17pickMouseReceiverEP7QWidgetRK7QPoi'
        'ntFPS2_N6QEvent4TypeE6QFlagsIN2Qt11MouseButtonEES1_S1_',
        CuteMixin._addressOf(candidate), CuteMixin._valueOf(windowPos,
        'QPointF'), CuteMixin._addressOf(pos, 'QPointF'), type.value,
        buttons.value, CuteMixin._addressOf(buttonDown),
        CuteMixin._addressOf(alienWidget),
    )
    from . import QWidget
    return QWidget._cuteAt(address)

  @staticmethod
  @overload(QWidget)
  @overload(NoneType)
  def windowForWidget(widget: Optional[QWidget]) -> Optional[QWindow]:
    """
    Calls Qt's 'QWindow *QApplicationPrivate::windowForWidget(const QWidget
    *widget)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qapplicationprivate.html#windowForWidget

    Parameters
    ----------

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QWindow]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWindow *QApplicationPrivate::windowForWidget(const QWidget *widget)
    address = Rituals.call(
        'ritual_ZN19QApplicationPrivate15windowForWidgetEPK7QWidget',
        CuteMixin._addressOf(widget),
    )
    from ..QtGui import QWindow
    return QWindow._cuteAt(address)

  @staticmethod
  @overload(QWidget, QTouchEvent)
  @overload(QWidget, NoneType)
  @overload(NoneType, QTouchEvent)
  @overload(NoneType, NoneType)
  def updateTouchPointsForWidget(
      widget: Optional[QWidget],
      touchEvent: Optional[QTouchEvent],
  ) -> bool:
    """
    Calls Qt's 'bool QApplicationPrivate::updateTouchPointsForWidget(QWidget
    *widget, QTouchEvent *touchEvent)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qapplicationprivate.html

    Parameters
    ----------

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    touchEvent : Optional[QTouchEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QApplicationPrivate::updateTouchPointsForWidget(QWidget *widget,
    #      QTouchEvent *touchEvent)
    return Rituals.call(
        'ritual_ZN19QApplicationPrivate26updateTouchPointsForWidgetEP7QWidg'
        'etP11QTouchEvent',
        CuteMixin._addressOf(widget), CuteMixin._addressOf(touchEvent),
    )

  @staticmethod
  @overload(QWidget, QTouchEvent)
  @overload(QWidget, NoneType)
  @overload(NoneType, QTouchEvent)
  @overload(NoneType, NoneType)
  def translateRawTouchEvent(
      widget: Optional[QWidget],
      touchEvent: Optional[QTouchEvent],
  ) -> bool:
    """
    Calls Qt's 'bool QApplicationPrivate::translateRawTouchEvent(QWidget
    *widget, const QTouchEvent *touchEvent)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qapplicationprivate.html#translateRawTouchEvent

    Parameters
    ----------

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    touchEvent : Optional[QTouchEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QApplicationPrivate::translateRawTouchEvent(QWidget *widget,
    #      const QTouchEvent *touchEvent)
    return Rituals.call(
        'ritual_ZN19QApplicationPrivate22translateRawTouchEventEP7QWidgetPK'
        '11QTouchEvent',
        CuteMixin._addressOf(widget), CuteMixin._addressOf(touchEvent),
    )

  @staticmethod
  @overload(QPointingDevice, int)
  @overload(NoneType, int)
  def translateTouchCancel(
      device: Optional[QPointingDevice],
      timestamp: int,
  ) -> None:
    """
    Calls Qt's 'void QApplicationPrivate::translateTouchCancel(const
    QPointingDevice *device, ulong timestamp)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qapplicationprivate.html#translateTouchCancel

    Parameters
    ----------

    device : Optional[QPointingDevice]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    timestamp : int
      Passed on as it is.
    """
    #  void QApplicationPrivate::translateTouchCancel(const QPointingDevice
    #      *device, ulong timestamp)
    Rituals.call(
        'ritual_ZN19QApplicationPrivate20translateTouchCancelEPK15QPointing'
        'Devicem',
        CuteMixin._addressOf(device), timestamp,
    )

  @staticmethod
  @overload(QWidget, QEvent, QPoint)
  @overload(QWidget, NoneType, QPoint)
  @overload(NoneType, QEvent, QPoint)
  @overload(NoneType, NoneType, QPoint)
  def giveFocusAccordingToFocusPolicy(
      w: Optional[QWidget],
      event: Optional[QEvent],
      localPos: QPoint,
  ) -> None:
    """
    Calls Qt's 'void
    QApplicationPrivate::giveFocusAccordingToFocusPolicy(QWidget *w, QEvent
    *event, QPoint localPos)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qapplicationprivate.html

    Parameters
    ----------

    w : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    event : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    localPos : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.
    """
    #  void QApplicationPrivate::giveFocusAccordingToFocusPolicy(QWidget *w,
    #      QEvent *event, QPoint localPos)
    Rituals.call(
        'ritual_ZN19QApplicationPrivate31giveFocusAccordingToFocusPolicyEP7'
        'QWidgetP6QEvent6QPoint',
        CuteMixin._addressOf(w), CuteMixin._addressOf(event),
        CuteMixin._valueOf(localPos),
    )

  @staticmethod
  @overload(QWidget, Qt.FocusPolicy)
  @overload(NoneType, Qt.FocusPolicy)
  def shouldSetFocus(w: Optional[QWidget], policy: Qt.FocusPolicy) -> bool:
    """
    Calls Qt's 'bool QApplicationPrivate::shouldSetFocus(QWidget *w,
    Qt::FocusPolicy policy)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qapplicationprivate.html#shouldSetFocus

    Parameters
    ----------

    w : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    policy : Qt.FocusPolicy
      Passed on as its number.
    """
    #  bool QApplicationPrivate::shouldSetFocus(QWidget *w, Qt::FocusPolicy
    #      policy)
    return Rituals.call(
        'ritual_ZN19QApplicationPrivate14shouldSetFocusEP7QWidgetN2Qt11Focu'
        'sPolicyE',
        CuteMixin._addressOf(w), policy.value,
    )

  @staticmethod
  @overload(QWidget)
  @overload(NoneType)
  def isAlien(a0: Optional[QWidget]) -> bool:
    """
    Calls Qt's 'bool QApplicationPrivate::isAlien(QWidget *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qapplicationprivate.html#isAlien

    Parameters
    ----------

    a0 : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QApplicationPrivate::isAlien(QWidget *a0)
    return Rituals.call(
        'ritual_ZN19QApplicationPrivate7isAlienEP7QWidget',
        CuteMixin._addressOf(a0),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QApplicationPrivate'

  #  A C++ QApplicationPrivate Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QApplicationPrivate'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def createActionPrivate(self) -> Optional[QActionPrivate]:
    """
    Calls Qt's 'QActionPrivate *QApplicationPrivate::createActionPrivate()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qapplicationprivate.html#createActionPrivate

    Returns
    -------

    Optional[QActionPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QActionPrivate *QApplicationPrivate::createActionPrivate() const
    ritual = 'ritual_ZNK19QApplicationPrivate19createActionPrivateEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK19QApplicationPrivate19createActionPrivateEv'
    address = self.uglySide.call(ritual)
    from ..QtGui import QActionPrivate
    return QActionPrivate._cuteAt(address)

  def createShortcutPrivate(self) -> Optional[QShortcutPrivate]:
    """
    Calls Qt's 'QShortcutPrivate
    *QApplicationPrivate::createShortcutPrivate() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qapplicationprivate.html#createShortcutPrivate

    Returns
    -------

    Optional[QShortcutPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QShortcutPrivate *QApplicationPrivate::createShortcutPrivate() const
    ritual = 'ritual_ZNK19QApplicationPrivate21createShortcutPrivateEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK19QApplicationPrivate21createShortcutPrivateEv'
    address = self.uglySide.call(ritual)
    from ..QtGui import QShortcutPrivate
    return QShortcutPrivate._cuteAt(address)

  def defaultModality(self) -> Qt.WindowModality:
    """
    Calls Qt's 'Qt::WindowModality QApplicationPrivate::defaultModality()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qapplicationprivate.html#defaultModality

    Returns
    -------

    Qt.WindowModality
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'Qt.WindowModality(number)' gives.
    """
    #  Qt::WindowModality QApplicationPrivate::defaultModality() const
    ritual = 'ritual_ZNK19QApplicationPrivate15defaultModalityEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK19QApplicationPrivate15defaultModalityEv'
    return Qt.WindowModality(self.uglySide.call(ritual))

  @overload(QWindow)
  @overload(NoneType)
  def windowNeverBlocked(self, window: Optional[QWindow]) -> bool:
    """
    Calls Qt's 'bool QApplicationPrivate::windowNeverBlocked(QWindow *window)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qapplicationprivate.html#windowNeverBlocked

    Parameters
    ----------

    window : Optional[QWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QApplicationPrivate::windowNeverBlocked(QWindow *window) const
    ritual = 'ritual_ZNK19QApplicationPrivate18windowNeverBlockedEP7QWindow'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK19QApplicationPrivate18windowNeverBlockedEP7QWindo'
          'w')
    return self.uglySide.call(ritual, self._addressOf(window))

  def basePalette(self) -> QPalette:
    """
    Calls Qt's 'QPalette QApplicationPrivate::basePalette() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qapplicationprivate.html#basePalette

    Returns
    -------

    QPalette
      A new cute QPalette around the copy Qt gave back. Python owns it.
    """
    #  QPalette QApplicationPrivate::basePalette() const
    ritual = 'ritual_ZNK19QApplicationPrivate11basePaletteEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK19QApplicationPrivate11basePaletteEv'
    address = self.uglySide.call(ritual)
    from ..QtGui import QPalette
    return QPalette._cuteOwning(address)

  @overload(QIcon.Mode, QPixmap)
  def applyQIconStyleHelper(
      self,
      mode: QIcon.Mode,
      base: QPixmap,
  ) -> QPixmap:
    """
    Calls Qt's 'QPixmap
    QApplicationPrivate::applyQIconStyleHelper(QIcon::Mode mode, const
    QPixmap &base) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qapplicationprivate.html#applyQIconStyleHelper

    Parameters
    ----------

    mode : QIcon.Mode
      Passed on as its number.

    base : QPixmap
      Passed on as a value: Qt reads the C++ QPixmap, which stays Python's
      own.

    Returns
    -------

    QPixmap
      A new cute QPixmap around the copy Qt gave back. Python owns it.
    """
    #  QPixmap QApplicationPrivate::applyQIconStyleHelper(QIcon::Mode mode,
    #      const QPixmap &base) const
    ritual = (
        'ritual_ZNK19QApplicationPrivate21applyQIconStyleHelperEN5QIcon4Mod'
        'eERK7QPixmap')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK19QApplicationPrivate21applyQIconStyleHelperEN5QIc'
          'on4ModeERK7QPixmap')
    address = self.uglySide.call(ritual, mode.value, self._valueOf(base))
    from ..QtGui import QPixmap
    return QPixmap._cuteOwning(address)

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

  @overload(list)
  def __init__(self, argv: list) -> None:
    """
    Notes what was given, for Qt's
    'QApplicationPrivate::QApplicationPrivate(int &argc, char **argv)', which
    is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qapplicationprivate.html#QApplicationPrivate

    Parameters
    ----------

    argv : list
      The texts the program was started with, as 'sys.argv'. Passed on as Qt
      takes them: how many they are, and where the first one is.
    """
    #  QApplicationPrivate::QApplicationPrivate(int &argc, char **argv)
    self._noteCreation(QApplicationPrivate, lambda: Rituals.call(
        'ritual_ZN19QApplicationPrivateC1ERiPPc', *self._startTextsOf(argv),
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

  def q_func(self) -> Optional[QApplication]:
    """
    Calls Qt's 'QApplication *QApplicationPrivate::q_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qapplicationprivate.html#q_func

    Returns
    -------

    Optional[QApplication]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QApplication *QApplicationPrivate::q_func()
    address = self.uglySide.call('ritual_ZN19QApplicationPrivate6q_funcEv')
    from . import QApplication
    return QApplication._cuteAt(address)

  def notifyLayoutDirectionChange(self) -> None:
    """
    Calls Qt's 'void QApplicationPrivate::notifyLayoutDirectionChange()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qapplicationprivate.html
    """
    #  void QApplicationPrivate::notifyLayoutDirectionChange()
    ritual = 'ritual_ZN19QApplicationPrivate27notifyLayoutDirectionChangeEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QApplicationPrivate27notifyLayoutDirectionChangeE'
          'v')
    self.uglySide.call(ritual)

  @overload(QWindow)
  @overload(NoneType)
  def notifyActiveWindowChange(self, a0: Optional[QWindow]) -> None:
    """
    Calls Qt's 'void QApplicationPrivate::notifyActiveWindowChange(QWindow
    *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qapplicationprivate.html#notifyActiveWindowChange

    Parameters
    ----------

    a0 : Optional[QWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QApplicationPrivate::notifyActiveWindowChange(QWindow *a0)
    ritual = (
        'ritual_ZN19QApplicationPrivate24notifyActiveWindowChangeEP7QWindow')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QApplicationPrivate24notifyActiveWindowChangeEP7Q'
          'Window')
    self.uglySide.call(ritual, self._addressOf(a0))

  def createEventDispatcher(self) -> None:
    """
    Calls Qt's 'void QApplicationPrivate::createEventDispatcher()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qapplicationprivate.html#createEventDispatcher
    """
    #  void QApplicationPrivate::createEventDispatcher()
    ritual = 'ritual_ZN19QApplicationPrivate21createEventDispatcherEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QApplicationPrivate21createEventDispatcherEv'
    self.uglySide.call(ritual)

  def notifyWindowIconChanged(self) -> None:
    """
    Calls Qt's 'void QApplicationPrivate::notifyWindowIconChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qapplicationprivate.html#notifyWindowIconChanged
    """
    #  void QApplicationPrivate::notifyWindowIconChanged()
    ritual = 'ritual_ZN19QApplicationPrivate23notifyWindowIconChangedEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QApplicationPrivate23notifyWindowIconChangedEv')
    self.uglySide.call(ritual)

  @overload(QEvent, QObject, QPostEventList)
  @overload(QEvent, QObject, NoneType)
  @overload(QEvent, NoneType, QPostEventList)
  @overload(QEvent, NoneType, NoneType)
  @overload(NoneType, QObject, QPostEventList)
  @overload(NoneType, QObject, NoneType)
  @overload(NoneType, NoneType, QPostEventList)
  @overload(NoneType, NoneType, NoneType)
  def compressEvent(
      self,
      event: Optional[QEvent],
      receiver: Optional[QObject],
      postedEvents: Optional[QPostEventList],
  ) -> bool:
    """
    Calls Qt's 'bool QApplicationPrivate::compressEvent(QEvent *event,
    QObject *receiver, QPostEventList *postedEvents)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qapplicationprivate.html#compressEvent

    Parameters
    ----------

    event : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    receiver : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    postedEvents : Optional[QPostEventList]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QApplicationPrivate::compressEvent(QEvent *event, QObject
    #      *receiver, QPostEventList *postedEvents)
    return self.uglySide.call(
        'ritual_ZN19QApplicationPrivate13compressEventEP6QEventP7QObjectP14'
        'QPostEventList',
        self._addressOf(event), self._addressOf(receiver, 'QObject'),
        self._addressOf(postedEvents),
    )

  @overload(QObject, QEvent)
  @overload(QObject, NoneType)
  @overload(NoneType, QEvent)
  @overload(NoneType, NoneType)
  def notify_helper(
      self,
      receiver: Optional[QObject],
      e: Optional[QEvent],
  ) -> bool:
    """
    Calls Qt's 'bool QApplicationPrivate::notify_helper(QObject *receiver,
    QEvent *e)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qapplicationprivate.html#notify_helper

    Parameters
    ----------

    receiver : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    e : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QApplicationPrivate::notify_helper(QObject *receiver, QEvent *e)
    return self.uglySide.call(
        'ritual_ZN19QApplicationPrivate13notify_helperEP7QObjectP6QEvent',
        self._addressOf(receiver, 'QObject'), self._addressOf(e),
    )

  def init(self) -> None:
    """
    Calls Qt's 'void QApplicationPrivate::init()'.

    Qt's own words: https://doc.qt.io/qt-6/qapplicationprivate.html#init
    """
    #  void QApplicationPrivate::init()
    self.uglySide.call('ritual_ZN19QApplicationPrivate4initEv')

  def initialize(self) -> None:
    """
    Calls Qt's 'void QApplicationPrivate::initialize()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qapplicationprivate.html#initialize
    """
    #  void QApplicationPrivate::initialize()
    self.uglySide.call('ritual_ZN19QApplicationPrivate10initializeEv')

  def process_cmdline(self) -> None:
    """
    Calls Qt's 'void QApplicationPrivate::process_cmdline()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qapplicationprivate.html#process_cmdline
    """
    #  void QApplicationPrivate::process_cmdline()
    self.uglySide.call('ritual_ZN19QApplicationPrivate15process_cmdlineEv')

  @overload(QWidget)
  @overload(NoneType)
  def closePopup(self, popup: Optional[QWidget]) -> None:
    """
    Calls Qt's 'void QApplicationPrivate::closePopup(QWidget *popup)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qapplicationprivate.html#closePopup

    Parameters
    ----------

    popup : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QApplicationPrivate::closePopup(QWidget *popup)
    self.uglySide.call(
        'ritual_ZN19QApplicationPrivate10closePopupEP7QWidget',
        self._addressOf(popup),
    )

  @overload(QWidget)
  @overload(NoneType)
  def openPopup(self, popup: Optional[QWidget]) -> None:
    """
    Calls Qt's 'void QApplicationPrivate::openPopup(QWidget *popup)'.

    Qt's own words: https://doc.qt.io/qt-6/qapplicationprivate.html#openPopup

    Parameters
    ----------

    popup : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QApplicationPrivate::openPopup(QWidget *popup)
    self.uglySide.call(
        'ritual_ZN19QApplicationPrivate9openPopupEP7QWidget',
        self._addressOf(popup),
    )

  def handleThemeChanged(self) -> None:
    """
    Calls Qt's 'void QApplicationPrivate::handleThemeChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qapplicationprivate.html#handleThemeChanged
    """
    #  void QApplicationPrivate::handleThemeChanged()
    ritual = 'ritual_ZN19QApplicationPrivate18handleThemeChangedEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QApplicationPrivate18handleThemeChangedEv'
    self.uglySide.call(ritual)

  @overload()
  @overload(str)
  @overload(NoneType)
  def handlePaletteChanged(self, className: Optional[str] = None) -> None:
    """
    Calls Qt's 'void QApplicationPrivate::handlePaletteChanged(const char
    *className)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qapplicationprivate.html#handlePaletteChanged

    Parameters
    ----------

    className : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text. May
      be left out, as in Qt: it is then None.
    """
    #  void QApplicationPrivate::handlePaletteChanged(const char *className)
    self.uglySide.call(
        'ritual_ZN19QApplicationPrivate20handlePaletteChangedEPKc',
        self._bytesOf(className),
    )

  @overload(QDrag)
  @overload(NoneType)
  def notifyDragStarted(self, a0: Optional[QDrag]) -> None:
    """
    Calls Qt's 'void QApplicationPrivate::notifyDragStarted(const QDrag
    *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qapplicationprivate.html#notifyDragStarted

    Parameters
    ----------

    a0 : Optional[QDrag]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QApplicationPrivate::notifyDragStarted(const QDrag *a0)
    ritual = 'ritual_ZN19QApplicationPrivate17notifyDragStartedEPK5QDrag'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QApplicationPrivate17notifyDragStartedEPK5QDrag')
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(QWidget)
  @overload(NoneType)
  def sendSyntheticEnterLeave(self, widget: Optional[QWidget]) -> None:
    """
    Calls Qt's 'void QApplicationPrivate::sendSyntheticEnterLeave(QWidget
    *widget)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qapplicationprivate.html#sendSyntheticEnterLeave

    Parameters
    ----------

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QApplicationPrivate::sendSyntheticEnterLeave(QWidget *widget)
    self.uglySide.call(
        'ritual_ZN19QApplicationPrivate23sendSyntheticEnterLeaveEP7QWidget',
        self._addressOf(widget),
    )

  def initializeMultitouch(self) -> None:
    """
    Calls Qt's 'void QApplicationPrivate::initializeMultitouch()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qapplicationprivate.html#initializeMultitouch
    """
    #  void QApplicationPrivate::initializeMultitouch()
    self.uglySide.call(
        'ritual_ZN19QApplicationPrivate20initializeMultitouchEv',
    )

  def initializeMultitouch_sys(self) -> None:
    """
    Calls Qt's 'void QApplicationPrivate::initializeMultitouch_sys()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qapplicationprivate.html#initializeMultitouch_sys
    """
    #  void QApplicationPrivate::initializeMultitouch_sys()
    self.uglySide.call(
        'ritual_ZN19QApplicationPrivate24initializeMultitouch_sysEv',
    )

  def cleanupMultitouch(self) -> None:
    """
    Calls Qt's 'void QApplicationPrivate::cleanupMultitouch()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qapplicationprivate.html#cleanupMultitouch
    """
    #  void QApplicationPrivate::cleanupMultitouch()
    self.uglySide.call('ritual_ZN19QApplicationPrivate17cleanupMultitouchEv')

  def cleanupMultitouch_sys(self) -> None:
    """
    Calls Qt's 'void QApplicationPrivate::cleanupMultitouch_sys()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qapplicationprivate.html#cleanupMultitouch_sys
    """
    #  void QApplicationPrivate::cleanupMultitouch_sys()
    self.uglySide.call(
        'ritual_ZN19QApplicationPrivate21cleanupMultitouch_sysEv',
    )

  @overload(QPointingDevice, QEventPoint)
  @overload(NoneType, QEventPoint)
  def findClosestTouchPointTarget(
      self,
      device: Optional[QPointingDevice],
      touchPoint: QEventPoint,
  ) -> Optional[QWidget]:
    """
    Calls Qt's 'QWidget
    *QApplicationPrivate::findClosestTouchPointTarget(const QPointingDevice
    *device, const QEventPoint &touchPoint)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qapplicationprivate.html

    Parameters
    ----------

    device : Optional[QPointingDevice]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    touchPoint : QEventPoint
      Passed on as a value: Qt reads the C++ QEventPoint, which stays
      Python's own.

    Returns
    -------

    Optional[QWidget]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWidget *QApplicationPrivate::findClosestTouchPointTarget(const
    #      QPointingDevice *device, const QEventPoint &touchPoint)
    address = self.uglySide.call(
        'ritual_ZN19QApplicationPrivate27findClosestTouchPointTargetEPK15QP'
        'ointingDeviceRK11QEventPoint',
        self._addressOf(device), self._valueOf(touchPoint),
    )
    from . import QWidget
    return QWidget._cuteAt(address)

  @overload(QWidget, QTouchEvent)
  @overload(QWidget, NoneType)
  @overload(NoneType, QTouchEvent)
  @overload(NoneType, NoneType)
  @overload(QWidget, QTouchEvent, ImplicitTouchGrabMode)
  @overload(QWidget, NoneType, ImplicitTouchGrabMode)
  @overload(NoneType, QTouchEvent, ImplicitTouchGrabMode)
  @overload(NoneType, NoneType, ImplicitTouchGrabMode)
  def activateImplicitTouchGrab(
      self,
      widget: Optional[QWidget],
      touchBeginEvent: Optional[QTouchEvent],
      grabMode: ImplicitTouchGrabMode = (
          ImplicitTouchGrabMode.GrabAcceptedPoints),
  ) -> None:
    """
    Calls Qt's 'void QApplicationPrivate::activateImplicitTouchGrab(QWidget
    *widget, QTouchEvent *touchBeginEvent, ImplicitTouchGrabMode grabMode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qapplicationprivate.html#activateImplicitTouchGrab

    Parameters
    ----------

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    touchBeginEvent : Optional[QTouchEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    grabMode : ImplicitTouchGrabMode
      Passed on as its number. May be left out, as in Qt: it is then
      ImplicitTouchGrabMode.GrabAcceptedPoints.
    """
    #  void QApplicationPrivate::activateImplicitTouchGrab(QWidget *widget,
    #      QTouchEvent *touchBeginEvent, ImplicitTouchGrabMode grabMode)
    self.uglySide.call(
        'ritual_ZN19QApplicationPrivate25activateImplicitTouchGrabEP7QWidge'
        'tP11QTouchEventNS_21ImplicitTouchGrabModeE',
        self._addressOf(widget), self._addressOf(touchBeginEvent),
        grabMode.value,
    )

  @staticmethod
  def appendTouchPoint(*__, **_) -> Never:
    """
    Qt's 'void QApplicationPrivate::appendTouchPoint(const QEventPoint
    &touchPoint)': cannot be called and cannot be called through the
    meta-object and cannot be copied: no header file has its code, Qt's
    source does not mark it or its class for use from outside Qt or writes it
    'inline' or nowhere, and it is no signal, slot or invokable function
    giving back nothing, of a class built on QObject, and Qt's source has no
    code for it that could be told from the rest.
    """
    raise NotImplementedError(
        "'QApplicationPrivate.appendTouchPoint' has no cute function yet. "
        "Qt's 'void QApplicationPrivate::appendTouchPoint(const QEventPoint "
        "&touchPoint)': cannot be called and cannot be called through the "
        "meta-object and cannot be copied: no header file has its code, "
        "Qt's source does not mark it or its class for use from outside Qt "
        "or writes it 'inline' or nowhere, and it is no signal, slot or "
        "invokable function giving back nothing, of a class built on "
        "QObject, and Qt's source has no code for it that could be told "
        "from the rest.")

  @staticmethod
  def desktop(*__, **_) -> Never:
    """
    Qt's 'QWidget *QApplicationPrivate::desktop()': cannot be called and
    cannot be called through the meta-object and cannot be copied: no header
    file has its code, Qt's source does not mark it or its class for use from
    outside Qt or writes it 'inline' or nowhere, and it is no signal, slot or
    invokable function giving back nothing, of a class built on QObject, and
    Qt's source has no code for it that could be told from the rest.
    """
    raise NotImplementedError(
        "'QApplicationPrivate.desktop' has no cute function yet. Qt's "
        "'QWidget *QApplicationPrivate::desktop()': cannot be called and "
        "cannot be called through the meta-object and cannot be copied: no "
        "header file has its code, Qt's source does not mark it or its "
        "class for use from outside Qt or writes it 'inline' or nowhere, "
        "and it is no signal, slot or invokable function giving back "
        "nothing, of a class built on QObject, and Qt's source has no code "
        "for it that could be told from the rest.")

  @staticmethod
  def focusNextPrevChild_helper(*__, **_) -> Never:
    """
    Qt's 'QWidget *QApplicationPrivate::focusNextPrevChild_helper(QWidget
    *toplevel, bool next, bool *wrappingOccurred)': takes a number to change
    where it is.
    """
    raise NotImplementedError(
        "'QApplicationPrivate.focusNextPrevChild_helper' has no cute "
        "function yet. Qt's 'QWidget "
        "*QApplicationPrivate::focusNextPrevChild_helper(QWidget *toplevel, "
        "bool next, bool *wrappingOccurred)': takes a number to change "
        "where it is.")

  @staticmethod
  def removeTouchPoint(*__, **_) -> Never:
    """
    Qt's 'void QApplicationPrivate::removeTouchPoint(int touchPointId)':
    cannot be called and cannot be called through the meta-object and cannot
    be copied: no header file has its code, Qt's source does not mark it or
    its class for use from outside Qt or writes it 'inline' or nowhere, and
    it is no signal, slot or invokable function giving back nothing, of a
    class built on QObject, and Qt's source has no code for it that could be
    told from the rest.
    """
    raise NotImplementedError(
        "'QApplicationPrivate.removeTouchPoint' has no cute function yet. "
        "Qt's 'void QApplicationPrivate::removeTouchPoint(int "
        "touchPointId)': cannot be called and cannot be called through the "
        "meta-object and cannot be copied: no header file has its code, "
        "Qt's source does not mark it or its class for use from outside Qt "
        "or writes it 'inline' or nowhere, and it is no signal, slot or "
        "invokable function giving back nothing, of a class built on "
        "QObject, and Qt's source has no code for it that could be told "
        "from the rest.")

  @staticmethod
  def sendMouseEvent(*__, **_) -> Never:
    """
    Qt's 'bool QApplicationPrivate::sendMouseEvent(QWidget *receiver,
    QMouseEvent *event, QWidget *alienWidget, QWidget *native, QWidget
    **buttonDown, QPointer<QWidget> &lastMouseReceiver, bool spontaneous,
    bool onlyDispatchEnterLeave)': takes a type Python has no way to hand
    over yet.
    """
    raise NotImplementedError(
        "'QApplicationPrivate.sendMouseEvent' has no cute function yet. "
        "Qt's 'bool QApplicationPrivate::sendMouseEvent(QWidget *receiver, "
        "QMouseEvent *event, QWidget *alienWidget, QWidget *native, QWidget "
        "**buttonDown, QPointer<QWidget> &lastMouseReceiver, bool "
        "spontaneous, bool onlyDispatchEnterLeave)': takes a type Python "
        "has no way to hand over yet.")

  @staticmethod
  def tryCloseAllWidgetWindows(*__, **_) -> Never:
    """
    Qt's 'bool QApplicationPrivate::tryCloseAllWidgetWindows(QWindowList
    *processedWindows)': names 'QWindowList', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QApplicationPrivate.tryCloseAllWidgetWindows' has no cute "
        "function yet. Qt's 'bool "
        "QApplicationPrivate::tryCloseAllWidgetWindows(QWindowList "
        "*processedWindows)': names 'QWindowList', which has no cute class "
        "yet.")

  @staticmethod
  def tryModalHelper(*__, **_) -> Never:
    """
    Qt's 'bool QApplicationPrivate::tryModalHelper(QWidget *widget, QWidget
    **rettop)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QApplicationPrivate.tryModalHelper' has no cute function yet. "
        "Qt's 'bool QApplicationPrivate::tryModalHelper(QWidget *widget, "
        "QWidget **rettop)': takes a type Python has no way to hand over "
        "yet.")
