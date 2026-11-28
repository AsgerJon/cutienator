"""
QGuiApplicationPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qguiapplication_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QGuiApplicationPrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import Qt, QCoreApplicationPrivate, QEvent
from . import QIcon, QWindowSystemInterfacePrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMimeData, QObject, QPoint, QPointF, QThreadPool
  from . import QActionPrivate, QColorTrcLut, QDrag, QGuiApplication
  from . import QInputDeviceManager, QPalette, QPixmap
  from . import QPlatformDragQtResponse, QPlatformDropQtResponse
  from . import QPlatformIntegration, QPlatformTheme, QShortcutPrivate
  from . import QWindow
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDrag = WAIT['QDrag']
  QMimeData = WAIT['QMimeData']
  QObject = WAIT['QObject']
  QPalette = WAIT['QPalette']
  QPixmap = WAIT['QPixmap']
  QPoint = WAIT['QPoint']
  QWindow = WAIT['QWindow']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QGuiApplicationPrivate(QCoreApplicationPrivate):
  """
  The cute side of Qt's QGuiApplicationPrivate: a plain Python object
  standing in front of one C++ QGuiApplicationPrivate.

  It is built on the cute 'QCoreApplicationPrivate', as Qt's
  QGuiApplicationPrivate is built on Qt's QCoreApplicationPrivate, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QGuiApplicationPrivate that has a ritual and that
  Python can call so far, 84 names in all: 'q_func', 'init',
  'createPlatformIntegration', 'createEventDispatcher',
  'eventDispatcherReady', 'notifyLayoutDirectionChange',
  'notifyActiveWindowChange', 'canQuitAutomatically', 'quit',
  'maybeLastWindowClosed', 'lastWindowClosed', 'captureGlobalModifierState',
  'platformIntegration', 'platformTheme', 'processMouseEvent',
  'processKeyEvent', 'processWheelEvent', 'processTouchEvent',
  'processCloseEvent', 'processGeometryChangeEvent', 'processEnterEvent',
  'processLeaveEvent', 'processFocusWindowEvent',
  'processWindowStateChangedEvent', 'processWindowScreenChangedEvent',
  'processWindowDevicePixelRatioChangedEvent',
  'processSafeAreaMarginsChangedEvent', 'processWindowSystemEvent',
  'processApplicationTermination', 'processScreenOrientationChange',
  'processScreenGeometryChange', 'processScreenLogicalDotsPerInchChange',
  'processScreenRefreshRateChange', 'processThemeChanged',
  'processExposeEvent', 'processPaintEvent', 'processFileOpenEvent',
  'processTabletEvent', 'processTabletEnterProximityEvent',
  'processTabletLeaveProximityEvent', 'processGestureEvent',
  'processPlatformPanelEvent', 'processContextMenuEvent', 'processDrag',
  'processDrop', 'sendQWindowEventToQPlatformWindow',
  'maybeForwardEventToVirtualKeyboard', 'isUsingVirtualKeyboard',
  'visualAlignment', 'getPixmapCursor', '_q_updateFocusObject', 'instance',
  'showModalWindow', 'hideModalWindow', 'updateBlockedStatus',
  'defaultModality', 'windowNeverBlocked', 'popupCount', 'activePopupWindow',
  'activatePopup', 'closePopup', 'closeAllPopups', 'commitData', 'saveState',
  'inputDeviceManager', 'colorProfileForA8Text', 'colorProfileForA32Text',
  'applyQIconStyleHelper', 'notifyWindowIconChanged',
  'applyWindowGeometrySpecificationTo', 'setApplicationState',
  'resetCachedDevicePixelRatio', 'createActionPrivate',
  'createShortcutPrivate', 'updatePalette', 'contextMenuEventType',
  'qtGuiThreadPool', '_q_updatePrimaryScreenDpis', 'handleThemeChanged',
  'setPalette', 'basePalette', 'handlePaletteChanged', 'notifyDragStarted',
  'clearPalette'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QGuiApplication *QGuiApplicationPrivate::q_func() const':
    takes in Python what 'QGuiApplication *QGuiApplicationPrivate::q_func()'
    takes.
  - Qt's 'QGuiApplicationPrivate::~QGuiApplicationPrivate()': the destructor:
    Python never removes a C++ QGuiApplicationPrivate.
  - Qt's 'void QGuiApplicationPrivate::addQtOptions(QList<QCommandLineOption>
    *options)': names 'QList<QCommandLineOption>', which has no cute class
    yet.
  - Qt's 'QAbstractEventDispatcher
    *QGuiApplicationPrivate::qt_qpa_core_dispatcher()': one of Qt's own inner
    workings.
  - Qt's 'bool QGuiApplicationPrivate::processNativeEvent(QWindow *window,
    const QByteArray &eventType, void *message, qintptr *result)': names
    'void', which has no cute class yet.
  - Qt's 'bool QGuiApplicationPrivate::isWindowBlocked(QWindow *window,
    QWindow **blockingWindow) const': takes a type Python has no way to hand
    over yet.
  - Qt's 'TabletPointData &QGuiApplicationPrivate::tabletDevicePoint(qint64
    deviceId)': gives a type Python has no way to take yet.

  What has no ritual
  ------------------

  1 of the 93 functions Qt declares: 1 cannot be called and cannot be called
  through the meta-object and cannot be copied.

  What to expect
  --------------

  - The C++ QGuiApplicationPrivate is created at the first use, not by
    'QGuiApplicationPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QGuiApplicationPrivate.
  - Each name of Qt's QGuiApplicationPrivate that has no cute function yet,
    'isWindowBlocked', 'processNativeEvent', 'tabletDevicePoint',
    'updateFilteredScreenOrientation', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The classes Qt writes inside QGuiApplicationPrivate, each a class in
  #  here as in C++.

  class QLastCursorPosition(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QGuiApplicationPrivate::QLastCursorPosition: a
    plain Python object standing in front of one C++
    QGuiApplicationPrivate::QLastCursorPosition.

    C++ hands a QGuiApplicationPrivate::QLastCursorPosition around as a copy,
    so every C++ QGuiApplicationPrivate::QLastCursorPosition behind a cute
    one is Python's own: it is removed, by the ritual named in
    '__delete_ritual__', when the cute object goes.

    What exists
    -----------

    Every function of Qt's QGuiApplicationPrivate::QLastCursorPosition that
    has a ritual and that Python can call so far, 6 names in all: 'x', 'y',
    'toPoint', 'reset', '__eq__', '__ne__'. It can be made from Python, in 2
    ways; see '__init__'.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QPointF QGuiApplicationPrivate::QLastCursorPosition::operator
      QPointF() const': an operator Python has no name for.
    - Qt's 'bool operator==(const QPointF &p1, const QLastCursorPosition
      &p2)': takes in Python what 'bool operator==(const QLastCursorPosition
      &p1, const QPointF &p2)' takes.
    - Qt's 'bool operator!=(const QPointF &p1, const QLastCursorPosition
      &p2)': takes in Python what 'bool operator!=(const QLastCursorPosition
      &p1, const QPointF &p2)' takes.
    - Qt's
      'QGuiApplicationPrivate::QLastCursorPosition::~QLastCursorPosition()':
      the destructor: Python removes its C++
      QGuiApplicationPrivate::QLastCursorPosition by it, and has no other use
      for it.

    What to expect
    --------------

    - The C++ QGuiApplicationPrivate::QLastCursorPosition is created at the
      first use, not by 'QGuiApplicationPrivate::QLastCursorPosition(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QGuiApplicationPrivate::QLastCursorPosition back
      gives a copy the ritual made for Python, in a new cute
      QGuiApplicationPrivate::QLastCursorPosition.
    """

    #  The cute classes this class names and is not built on. Each waits
    #  until it is made; see 'WAIT'. A type checker reads the imports at the
    #  top of the file instead.
    if not TYPE_CHECKING:
      QPointF = WAIT['QPointF']

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QGuiApplicationPrivate::QLastCursorPosition'

    #  Qt's '~QGuiApplicationPrivate::QLastCursorPosition()'. Naming it makes
    #  this a value class: Python owns every C++
    #  QGuiApplicationPrivate::QLastCursorPosition behind a cute one, and
    #  removes it by this ritual.
    __delete_ritual__ = (
        'ritual_ZN22QGuiApplicationPrivate19QLastCursorPositionD1Ev')

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    def x(self) -> float:
      """
      Calls Qt's 'qreal QGuiApplicationPrivate::QLastCursorPosition::x()
      const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qguiapplicationprivate-qlastcursorposition.html
      """
      #  qreal QGuiApplicationPrivate::QLastCursorPosition::x() const
      return self.uglySide.call(
          'ritual_ZNK22QGuiApplicationPrivate19QLastCursorPosition1xEv',
      )

    def y(self) -> float:
      """
      Calls Qt's 'qreal QGuiApplicationPrivate::QLastCursorPosition::y()
      const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qguiapplicationprivate-qlastcursorposition.html
      """
      #  qreal QGuiApplicationPrivate::QLastCursorPosition::y() const
      return self.uglySide.call(
          'ritual_ZNK22QGuiApplicationPrivate19QLastCursorPosition1yEv',
      )

    def toPoint(self) -> QPoint:
      """
      Calls Qt's 'QPoint
      QGuiApplicationPrivate::QLastCursorPosition::toPoint() const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qguiapplicationprivate-qlastcursorposition.html

      Returns
      -------

      QPoint
        A new cute QPoint around the copy Qt gave back. Python owns it.
      """
      #  QPoint QGuiApplicationPrivate::QLastCursorPosition::toPoint() const
      address = self.uglySide.call(
          'ritual_ZNK22QGuiApplicationPrivate19QLastCursorPosition7toPointE'
          'v',
      )
      from ..QtCore import QPoint
      return QPoint._cuteOwning(address)

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @overload(QPointF)
    def __eq__(self, p2: QPointF) -> bool:
      """
      Calls Qt's 'bool operator==(const QLastCursorPosition &p1, const
      QPointF &p2)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qguiapplicationprivate-qlastcursorposition.html

      Parameters
      ----------

      p2 : QPointF
        Passed on as a value: Qt reads the C++ QPointF, which stays Python's
        own.
      """
      #  bool operator==(const QLastCursorPosition &p1, const QPointF &p2)
      return Rituals.call(
          'ritual_ZeqRKN22QGuiApplicationPrivate19QLastCursorPositionERK7QP'
          'ointF',
          CuteMixin._valueOf(self), CuteMixin._valueOf(p2, 'QPointF'),
      )

    @overload.fallback
    def __eq__(self, *args: object) -> object:
      """
      Tells Python that no function of this name takes what it was
      handed, with Python's own word for it. Python then asks the
      other side of the operator.
      """
      return NotImplemented

    @overload(QPointF)
    def __ne__(self, p2: QPointF) -> bool:
      """
      Calls Qt's 'bool operator!=(const QLastCursorPosition &p1, const
      QPointF &p2)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qguiapplicationprivate-qlastcursorposition.html

      Parameters
      ----------

      p2 : QPointF
        Passed on as a value: Qt reads the C++ QPointF, which stays Python's
        own.
      """
      #  bool operator!=(const QLastCursorPosition &p1, const QPointF &p2)
      return Rituals.call(
          'ritual_ZneRKN22QGuiApplicationPrivate19QLastCursorPositionERK7QP'
          'ointF',
          CuteMixin._valueOf(self), CuteMixin._valueOf(p2, 'QPointF'),
      )

    @overload.fallback
    def __ne__(self, *args: object) -> object:
      """
      Tells Python that no function of this name takes what it was
      handed, with Python's own word for it. Python then asks the
      other side of the operator.
      """
      return NotImplemented

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @overload()
    def __init__(self) -> None:
      """
      Notes what was given, for Qt's
      'QGuiApplicationPrivate::QLastCursorPosition::QLastCursorPosition()',
      which is called at the first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qguiapplicationprivate-qlastcursorposition.html
      """
      #  QGuiApplicationPrivate::QLastCursorPosition::QLastCursorPosition()
      self._noteCreation(
          QGuiApplicationPrivate.QLastCursorPosition, lambda: Rituals.call(
              'ritual_ZN22QGuiApplicationPrivate19QLastCursorPositionC1Ev',
          ))

    @overload(QPointF)
    def __init__(self, p: QPointF) -> None:
      """
      Notes what was given, for Qt's
      'QGuiApplicationPrivate::QLastCursorPosition::QLastCursorPosition(
      QPointF p)', which is called at the first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qguiapplicationprivate-qlastcursorposition.html

      Parameters
      ----------

      p : QPointF
        Passed on as a value: Qt reads the C++ QPointF, which stays Python's
        own.
      """
      #  QGuiApplicationPrivate::QLastCursorPosition::
      #      QLastCursorPosition(QPointF p)
      self._noteCreation(
          QGuiApplicationPrivate.QLastCursorPosition, lambda: Rituals.call(
              'ritual_ZN22QGuiApplicationPrivate19QLastCursorPositionC1E7QP'
              'ointF',
              self._valueOf(p, 'QPointF'),
          ))

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    def reset(self) -> None:
      """
      Calls Qt's 'void QGuiApplicationPrivate::QLastCursorPosition::reset()'.

      Qt's own words:
      https://doc.qt.io/qt-6/qguiapplicationprivate-qlastcursorposition.html
      """
      #  void QGuiApplicationPrivate::QLastCursorPosition::reset()
      self.uglySide.call(
          'ritual_ZN22QGuiApplicationPrivate19QLastCursorPosition5resetEv',
      )

  class SynthesizedMouseData(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QGuiApplicationPrivate::SynthesizedMouseData: a
    plain Python object standing in front of one C++
    QGuiApplicationPrivate::SynthesizedMouseData.

    C++ hands a QGuiApplicationPrivate::SynthesizedMouseData around as a
    copy, so every C++ QGuiApplicationPrivate::SynthesizedMouseData behind a
    cute one is Python's own: it is removed, by the ritual named in
    '__delete_ritual__', when the cute object goes.

    What exists
    -----------

    No function of Qt's QGuiApplicationPrivate::SynthesizedMouseData yet. It
    can be made from Python, in 1 way; see '__init__'.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's
      'QGuiApplicationPrivate::SynthesizedMouseData::~SynthesizedMouseData(
      )': the destructor: Python removes its C++
      QGuiApplicationPrivate::SynthesizedMouseData by it, and has no other
      use for it.

    What to expect
    --------------

    - The C++ QGuiApplicationPrivate::SynthesizedMouseData is created at the
      first use, not by 'QGuiApplicationPrivate::SynthesizedMouseData(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QGuiApplicationPrivate::SynthesizedMouseData back
      gives a copy the ritual made for Python, in a new cute
      QGuiApplicationPrivate::SynthesizedMouseData.
    """

    #  The cute classes this class names and is not built on. Each waits
    #  until it is made; see 'WAIT'. A type checker reads the imports at the
    #  top of the file instead.
    if not TYPE_CHECKING:
      QPointF = WAIT['QPointF']
      QWindow = WAIT['QWindow']

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QGuiApplicationPrivate::SynthesizedMouseData'

    #  Qt's '~QGuiApplicationPrivate::SynthesizedMouseData()'. Naming it
    #  makes this a value class: Python owns every C++
    #  QGuiApplicationPrivate::SynthesizedMouseData behind a cute one, and
    #  removes it by this ritual.
    __delete_ritual__ = (
        'ritual_ZN22QGuiApplicationPrivate20SynthesizedMouseDataD1Ev')

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @overload(QPointF, QPointF, QWindow)
    @overload(QPointF, QPointF, NoneType)
    def __init__(
        self,
        p: QPointF,
        sp: QPointF,
        w: Optional[QWindow],
    ) -> None:
      """
      Notes what was given, for Qt's
      'QGuiApplicationPrivate::SynthesizedMouseData::SynthesizedMouseData(
      const QPointF &p, const QPointF &sp, QWindow *w)', which is called at
      the first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qguiapplicationprivate-synthesizedmousedata.html

      Parameters
      ----------

      p : QPointF
        Passed on as a value: Qt reads the C++ QPointF, which stays Python's
        own.

      sp : QPointF
        Passed on as a value: Qt reads the C++ QPointF, which stays Python's
        own.

      w : Optional[QWindow]
        Passed on as the address of its C++ object. None is passed on as no
        object.
      """
      #  QGuiApplicationPrivate::SynthesizedMouseData::
      #      SynthesizedMouseData(const QPointF &p, const QPointF &sp,
      #      QWindow *w)
      self._noteCreation(
          QGuiApplicationPrivate.SynthesizedMouseData, lambda: Rituals.call(
              'ritual_ZN22QGuiApplicationPrivate20SynthesizedMouseDataC1ERK'
              '7QPointFS3_P7QWindow',
              self._valueOf(p, 'QPointF'), self._valueOf(sp, 'QPointF'),
              self._addressOf(w),
          ))

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  class TabletPointData(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QGuiApplicationPrivate::TabletPointData: a plain
    Python object standing in front of one C++
    QGuiApplicationPrivate::TabletPointData.

    C++ hands a QGuiApplicationPrivate::TabletPointData around as a copy, so
    every C++ QGuiApplicationPrivate::TabletPointData behind a cute one is
    Python's own: it is removed, by the ritual named in '__delete_ritual__',
    when the cute object goes.

    What exists
    -----------

    No function of Qt's QGuiApplicationPrivate::TabletPointData yet. It can
    be made from Python, in 1 way; see '__init__'.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QGuiApplicationPrivate::TabletPointData::~TabletPointData()': the
      destructor: Python removes its C++
      QGuiApplicationPrivate::TabletPointData by it, and has no other use for
      it.

    What to expect
    --------------

    - The C++ QGuiApplicationPrivate::TabletPointData is created at the first
      use, not by 'QGuiApplicationPrivate::TabletPointData(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QGuiApplicationPrivate::TabletPointData back gives
      a copy the ritual made for Python, in a new cute
      QGuiApplicationPrivate::TabletPointData.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QGuiApplicationPrivate::TabletPointData'

    #  Qt's '~QGuiApplicationPrivate::TabletPointData()'. Naming it makes
    #  this a value class: Python owns every C++
    #  QGuiApplicationPrivate::TabletPointData behind a cute one, and removes
    #  it by this ritual.
    __delete_ritual__ = (
        'ritual_ZN22QGuiApplicationPrivate15TabletPointDataD1Ev')

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @overload()
    @overload(int)
    def __init__(self, devId: int = 0) -> None:
      """
      Notes what was given, for Qt's
      'QGuiApplicationPrivate::TabletPointData::TabletPointData(qint64
      devId)', which is called at the first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qguiapplicationprivate-tabletpointdata.html

      Parameters
      ----------

      devId : int
        Passed on as it is. May be left out, as in Qt: it is then 0.
      """
      #  QGuiApplicationPrivate::TabletPointData::TabletPointData(qint64
      #      devId)
      self._noteCreation(
          QGuiApplicationPrivate.TabletPointData, lambda: Rituals.call(
              'ritual_ZN22QGuiApplicationPrivate15TabletPointDataC1Ex',
              devId,
          ))

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QEvent)
  @overload(NoneType)
  def captureGlobalModifierState(e: Optional[QEvent]) -> None:
    """
    Calls Qt's 'void
    QGuiApplicationPrivate::captureGlobalModifierState(QEvent *e)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qguiapplicationprivate.html

    Parameters
    ----------

    e : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGuiApplicationPrivate::captureGlobalModifierState(QEvent *e)
    Rituals.call(
        'ritual_ZN22QGuiApplicationPrivate26captureGlobalModifierStateEP6QE'
        'vent',
        CuteMixin._addressOf(e),
    )

  @staticmethod
  def platformIntegration() -> Optional[QPlatformIntegration]:
    """
    Calls Qt's 'QPlatformIntegration
    *QGuiApplicationPrivate::platformIntegration()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qguiapplicationprivate.html#platformIntegration

    Returns
    -------

    Optional[QPlatformIntegration]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPlatformIntegration *QGuiApplicationPrivate::platformIntegration()
    address = Rituals.call(
        'ritual_ZN22QGuiApplicationPrivate19platformIntegrationEv',
    )
    from . import QPlatformIntegration
    return QPlatformIntegration._cuteAt(address)

  @staticmethod
  def platformTheme() -> Optional[QPlatformTheme]:
    """
    Calls Qt's 'QPlatformTheme *QGuiApplicationPrivate::platformTheme()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qguiapplicationprivate.html#platformTheme

    Returns
    -------

    Optional[QPlatformTheme]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPlatformTheme *QGuiApplicationPrivate::platformTheme()
    address = Rituals.call(
        'ritual_ZN22QGuiApplicationPrivate13platformThemeEv',
    )
    from . import QPlatformTheme
    return QPlatformTheme._cuteAt(address)

  @staticmethod
  @overload(QWindowSystemInterfacePrivate.MouseEvent)
  @overload(NoneType)
  def processMouseEvent(
      e: Optional[QWindowSystemInterfacePrivate.MouseEvent],
  ) -> None:
    """
    Calls Qt's 'void QGuiApplicationPrivate::processMouseEvent(
    QWindowSystemInterfacePrivate::MouseEvent *e)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qguiapplicationprivate.html#processMouseEvent

    Parameters
    ----------

    e : Optional[QWindowSystemInterfacePrivate.MouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGuiApplicationPrivate::processMouseEvent(
    #      QWindowSystemInterfacePrivate::MouseEvent *e)
    Rituals.call(
        'ritual_ZN22QGuiApplicationPrivate17processMouseEventEPN29QWindowSy'
        'stemInterfacePrivate10MouseEventE',
        CuteMixin._addressOf(e),
    )

  @staticmethod
  @overload(QWindowSystemInterfacePrivate.KeyEvent)
  @overload(NoneType)
  def processKeyEvent(
      e: Optional[QWindowSystemInterfacePrivate.KeyEvent],
  ) -> None:
    """
    Calls Qt's 'void
    QGuiApplicationPrivate::processKeyEvent(QWindowSystemInterfacePrivate::
    KeyEvent *e)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qguiapplicationprivate.html#processKeyEvent

    Parameters
    ----------

    e : Optional[QWindowSystemInterfacePrivate.KeyEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGuiApplicationPrivate::processKeyEvent(
    #      QWindowSystemInterfacePrivate::KeyEvent *e)
    Rituals.call(
        'ritual_ZN22QGuiApplicationPrivate15processKeyEventEPN29QWindowSyst'
        'emInterfacePrivate8KeyEventE',
        CuteMixin._addressOf(e),
    )

  @staticmethod
  @overload(QWindowSystemInterfacePrivate.WheelEvent)
  @overload(NoneType)
  def processWheelEvent(
      e: Optional[QWindowSystemInterfacePrivate.WheelEvent],
  ) -> None:
    """
    Calls Qt's 'void QGuiApplicationPrivate::processWheelEvent(
    QWindowSystemInterfacePrivate::WheelEvent *e)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qguiapplicationprivate.html#processWheelEvent

    Parameters
    ----------

    e : Optional[QWindowSystemInterfacePrivate.WheelEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGuiApplicationPrivate::processWheelEvent(
    #      QWindowSystemInterfacePrivate::WheelEvent *e)
    Rituals.call(
        'ritual_ZN22QGuiApplicationPrivate17processWheelEventEPN29QWindowSy'
        'stemInterfacePrivate10WheelEventE',
        CuteMixin._addressOf(e),
    )

  @staticmethod
  @overload(QWindowSystemInterfacePrivate.TouchEvent)
  @overload(NoneType)
  def processTouchEvent(
      e: Optional[QWindowSystemInterfacePrivate.TouchEvent],
  ) -> None:
    """
    Calls Qt's 'void QGuiApplicationPrivate::processTouchEvent(
    QWindowSystemInterfacePrivate::TouchEvent *e)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qguiapplicationprivate.html#processTouchEvent

    Parameters
    ----------

    e : Optional[QWindowSystemInterfacePrivate.TouchEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGuiApplicationPrivate::processTouchEvent(
    #      QWindowSystemInterfacePrivate::TouchEvent *e)
    Rituals.call(
        'ritual_ZN22QGuiApplicationPrivate17processTouchEventEPN29QWindowSy'
        'stemInterfacePrivate10TouchEventE',
        CuteMixin._addressOf(e),
    )

  @staticmethod
  @overload(QWindowSystemInterfacePrivate.CloseEvent)
  @overload(NoneType)
  def processCloseEvent(
      e: Optional[QWindowSystemInterfacePrivate.CloseEvent],
  ) -> None:
    """
    Calls Qt's 'void QGuiApplicationPrivate::processCloseEvent(
    QWindowSystemInterfacePrivate::CloseEvent *e)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qguiapplicationprivate.html#processCloseEvent

    Parameters
    ----------

    e : Optional[QWindowSystemInterfacePrivate.CloseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGuiApplicationPrivate::processCloseEvent(
    #      QWindowSystemInterfacePrivate::CloseEvent *e)
    Rituals.call(
        'ritual_ZN22QGuiApplicationPrivate17processCloseEventEPN29QWindowSy'
        'stemInterfacePrivate10CloseEventE',
        CuteMixin._addressOf(e),
    )

  @staticmethod
  @overload(QWindowSystemInterfacePrivate.GeometryChangeEvent)
  @overload(NoneType)
  def processGeometryChangeEvent(
      e: Optional[QWindowSystemInterfacePrivate.GeometryChangeEvent],
  ) -> None:
    """
    Calls Qt's 'void QGuiApplicationPrivate::processGeometryChangeEvent(
    QWindowSystemInterfacePrivate::GeometryChangeEvent *e)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qguiapplicationprivate.html

    Parameters
    ----------

    e : Optional[QWindowSystemInterfacePrivate.GeometryChangeEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGuiApplicationPrivate::processGeometryChangeEvent(
    #      QWindowSystemInterfacePrivate::GeometryChangeEvent *e)
    Rituals.call(
        'ritual_ZN22QGuiApplicationPrivate26processGeometryChangeEventEPN29'
        'QWindowSystemInterfacePrivate19GeometryChangeEventE',
        CuteMixin._addressOf(e),
    )

  @staticmethod
  @overload(QWindowSystemInterfacePrivate.EnterEvent)
  @overload(NoneType)
  def processEnterEvent(
      e: Optional[QWindowSystemInterfacePrivate.EnterEvent],
  ) -> None:
    """
    Calls Qt's 'void QGuiApplicationPrivate::processEnterEvent(
    QWindowSystemInterfacePrivate::EnterEvent *e)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qguiapplicationprivate.html#processEnterEvent

    Parameters
    ----------

    e : Optional[QWindowSystemInterfacePrivate.EnterEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGuiApplicationPrivate::processEnterEvent(
    #      QWindowSystemInterfacePrivate::EnterEvent *e)
    Rituals.call(
        'ritual_ZN22QGuiApplicationPrivate17processEnterEventEPN29QWindowSy'
        'stemInterfacePrivate10EnterEventE',
        CuteMixin._addressOf(e),
    )

  @staticmethod
  @overload(QWindowSystemInterfacePrivate.LeaveEvent)
  @overload(NoneType)
  def processLeaveEvent(
      e: Optional[QWindowSystemInterfacePrivate.LeaveEvent],
  ) -> None:
    """
    Calls Qt's 'void QGuiApplicationPrivate::processLeaveEvent(
    QWindowSystemInterfacePrivate::LeaveEvent *e)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qguiapplicationprivate.html#processLeaveEvent

    Parameters
    ----------

    e : Optional[QWindowSystemInterfacePrivate.LeaveEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGuiApplicationPrivate::processLeaveEvent(
    #      QWindowSystemInterfacePrivate::LeaveEvent *e)
    Rituals.call(
        'ritual_ZN22QGuiApplicationPrivate17processLeaveEventEPN29QWindowSy'
        'stemInterfacePrivate10LeaveEventE',
        CuteMixin._addressOf(e),
    )

  @staticmethod
  @overload(QWindowSystemInterfacePrivate.FocusWindowEvent)
  @overload(NoneType)
  def processFocusWindowEvent(
      e: Optional[QWindowSystemInterfacePrivate.FocusWindowEvent],
  ) -> None:
    """
    Calls Qt's 'void QGuiApplicationPrivate::processFocusWindowEvent(
    QWindowSystemInterfacePrivate::FocusWindowEvent *e)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qguiapplicationprivate.html

    Parameters
    ----------

    e : Optional[QWindowSystemInterfacePrivate.FocusWindowEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGuiApplicationPrivate::processFocusWindowEvent(
    #      QWindowSystemInterfacePrivate::FocusWindowEvent *e)
    Rituals.call(
        'ritual_ZN22QGuiApplicationPrivate23processFocusWindowEventEPN29QWi'
        'ndowSystemInterfacePrivate16FocusWindowEventE',
        CuteMixin._addressOf(e),
    )

  @staticmethod
  @overload(QWindowSystemInterfacePrivate.WindowStateChangedEvent)
  @overload(NoneType)
  def processWindowStateChangedEvent(
      e: Optional[QWindowSystemInterfacePrivate.WindowStateChangedEvent],
  ) -> None:
    """
    Calls Qt's 'void QGuiApplicationPrivate::processWindowStateChangedEvent(
    QWindowSystemInterfacePrivate::WindowStateChangedEvent *e)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qguiapplicationprivate.html

    Parameters
    ----------

    e : Optional[QWindowSystemInterfacePrivate.WindowStateChangedEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGuiApplicationPrivate::processWindowStateChangedEvent(
    #      QWindowSystemInterfacePrivate::WindowStateChangedEvent *e)
    Rituals.call(
        'ritual_ZN22QGuiApplicationPrivate30processWindowStateChangedEventE'
        'PN29QWindowSystemInterfacePrivate23WindowStateChangedEventE',
        CuteMixin._addressOf(e),
    )

  @staticmethod
  @overload(QWindowSystemInterfacePrivate.WindowScreenChangedEvent)
  @overload(NoneType)
  def processWindowScreenChangedEvent(
      e: Optional[QWindowSystemInterfacePrivate.WindowScreenChangedEvent],
  ) -> None:
    """
    Calls Qt's 'void QGuiApplicationPrivate::processWindowScreenChangedEvent(
    QWindowSystemInterfacePrivate::WindowScreenChangedEvent *e)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qguiapplicationprivate.html

    Parameters
    ----------

    e : Optional[QWindowSystemInterfacePrivate.WindowScreenChangedEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGuiApplicationPrivate::processWindowScreenChangedEvent(
    #      QWindowSystemInterfacePrivate::WindowScreenChangedEvent *e)
    Rituals.call(
        'ritual_ZN22QGuiApplicationPrivate31processWindowScreenChangedEvent'
        'EPN29QWindowSystemInterfacePrivate24WindowScreenChangedEventE',
        CuteMixin._addressOf(e),
    )

  @staticmethod
  @overload(QWindowSystemInterfacePrivate.WindowDevicePixelRatioChangedEvent)
  @overload(NoneType)
  def processWindowDevicePixelRatioChangedEvent(
      e: Optional[QWindowSystemInterfacePrivate.WindowDevicePixelRatioChangedEvent],
  ) -> None:
    """
    Calls Qt's 'void
    QGuiApplicationPrivate::processWindowDevicePixelRatioChangedEvent(
    QWindowSystemInterfacePrivate::WindowDevicePixelRatioChangedEvent *e)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qguiapplicationprivate.html

    Parameters
    ----------

    e : Optional[QWindowSystemInterfacePrivate.WindowDevicePixelRatioChangedEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void
    #      QGuiApplicationPrivate::processWindowDevicePixelRatioChangedEvent(
    #      QWindowSystemInterfacePrivate::WindowDevicePixelRatioChangedEvent
    #      *e)
    Rituals.call(
        'ritual_ZN22QGuiApplicationPrivate41processWindowDevicePixelRatioCh'
        'angedEventEPN29QWindowSystemInterfacePrivate34WindowDevicePixelRat'
        'ioChangedEventE',
        CuteMixin._addressOf(e),
    )

  @staticmethod
  @overload(QWindowSystemInterfacePrivate.SafeAreaMarginsChangedEvent)
  @overload(NoneType)
  def processSafeAreaMarginsChangedEvent(
      e: Optional[QWindowSystemInterfacePrivate.SafeAreaMarginsChangedEvent],
  ) -> None:
    """
    Calls Qt's 'void
    QGuiApplicationPrivate::processSafeAreaMarginsChangedEvent(
    QWindowSystemInterfacePrivate::SafeAreaMarginsChangedEvent *e)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qguiapplicationprivate.html

    Parameters
    ----------

    e : Optional[QWindowSystemInterfacePrivate.SafeAreaMarginsChangedEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGuiApplicationPrivate::processSafeAreaMarginsChangedEvent(
    #      QWindowSystemInterfacePrivate::SafeAreaMarginsChangedEvent *e)
    Rituals.call(
        'ritual_ZN22QGuiApplicationPrivate34processSafeAreaMarginsChangedEv'
        'entEPN29QWindowSystemInterfacePrivate27SafeAreaMarginsChangedEvent'
        'E',
        CuteMixin._addressOf(e),
    )

  @staticmethod
  @overload(QWindowSystemInterfacePrivate.WindowSystemEvent)
  @overload(NoneType)
  def processWindowSystemEvent(
      e: Optional[QWindowSystemInterfacePrivate.WindowSystemEvent],
  ) -> None:
    """
    Calls Qt's 'void QGuiApplicationPrivate::processWindowSystemEvent(
    QWindowSystemInterfacePrivate::WindowSystemEvent *e)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qguiapplicationprivate.html

    Parameters
    ----------

    e : Optional[QWindowSystemInterfacePrivate.WindowSystemEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGuiApplicationPrivate::processWindowSystemEvent(
    #      QWindowSystemInterfacePrivate::WindowSystemEvent *e)
    Rituals.call(
        'ritual_ZN22QGuiApplicationPrivate24processWindowSystemEventEPN29QW'
        'indowSystemInterfacePrivate17WindowSystemEventE',
        CuteMixin._addressOf(e),
    )

  @staticmethod
  @overload(QWindowSystemInterfacePrivate.WindowSystemEvent)
  @overload(NoneType)
  def processApplicationTermination(
      e: Optional[QWindowSystemInterfacePrivate.WindowSystemEvent],
  ) -> None:
    """
    Calls Qt's 'void QGuiApplicationPrivate::processApplicationTermination(
    QWindowSystemInterfacePrivate::WindowSystemEvent *e)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qguiapplicationprivate.html

    Parameters
    ----------

    e : Optional[QWindowSystemInterfacePrivate.WindowSystemEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGuiApplicationPrivate::processApplicationTermination(
    #      QWindowSystemInterfacePrivate::WindowSystemEvent *e)
    Rituals.call(
        'ritual_ZN22QGuiApplicationPrivate29processApplicationTerminationEP'
        'N29QWindowSystemInterfacePrivate17WindowSystemEventE',
        CuteMixin._addressOf(e),
    )

  @staticmethod
  @overload(QWindowSystemInterfacePrivate.ScreenOrientationEvent)
  @overload(NoneType)
  def processScreenOrientationChange(
      e: Optional[QWindowSystemInterfacePrivate.ScreenOrientationEvent],
  ) -> None:
    """
    Calls Qt's 'void QGuiApplicationPrivate::processScreenOrientationChange(
    QWindowSystemInterfacePrivate::ScreenOrientationEvent *e)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qguiapplicationprivate.html

    Parameters
    ----------

    e : Optional[QWindowSystemInterfacePrivate.ScreenOrientationEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGuiApplicationPrivate::processScreenOrientationChange(
    #      QWindowSystemInterfacePrivate::ScreenOrientationEvent *e)
    Rituals.call(
        'ritual_ZN22QGuiApplicationPrivate30processScreenOrientationChangeE'
        'PN29QWindowSystemInterfacePrivate22ScreenOrientationEventE',
        CuteMixin._addressOf(e),
    )

  @staticmethod
  @overload(QWindowSystemInterfacePrivate.ScreenGeometryEvent)
  @overload(NoneType)
  def processScreenGeometryChange(
      e: Optional[QWindowSystemInterfacePrivate.ScreenGeometryEvent],
  ) -> None:
    """
    Calls Qt's 'void QGuiApplicationPrivate::processScreenGeometryChange(
    QWindowSystemInterfacePrivate::ScreenGeometryEvent *e)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qguiapplicationprivate.html

    Parameters
    ----------

    e : Optional[QWindowSystemInterfacePrivate.ScreenGeometryEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGuiApplicationPrivate::processScreenGeometryChange(
    #      QWindowSystemInterfacePrivate::ScreenGeometryEvent *e)
    Rituals.call(
        'ritual_ZN22QGuiApplicationPrivate27processScreenGeometryChangeEPN2'
        '9QWindowSystemInterfacePrivate19ScreenGeometryEventE',
        CuteMixin._addressOf(e),
    )

  @staticmethod
  @overload(QWindowSystemInterfacePrivate.ScreenLogicalDotsPerInchEvent)
  @overload(NoneType)
  def processScreenLogicalDotsPerInchChange(
      e: Optional[QWindowSystemInterfacePrivate.ScreenLogicalDotsPerInchEvent],
  ) -> None:
    """
    Calls Qt's 'void
    QGuiApplicationPrivate::processScreenLogicalDotsPerInchChange(
    QWindowSystemInterfacePrivate::ScreenLogicalDotsPerInchEvent *e)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qguiapplicationprivate.html

    Parameters
    ----------

    e : Optional[QWindowSystemInterfacePrivate.ScreenLogicalDotsPerInchEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGuiApplicationPrivate::processScreenLogicalDotsPerInchChange(
    #      QWindowSystemInterfacePrivate::ScreenLogicalDotsPerInchEvent *e)
    Rituals.call(
        'ritual_ZN22QGuiApplicationPrivate37processScreenLogicalDotsPerInch'
        'ChangeEPN29QWindowSystemInterfacePrivate29ScreenLogicalDotsPerInch'
        'EventE',
        CuteMixin._addressOf(e),
    )

  @staticmethod
  @overload(QWindowSystemInterfacePrivate.ScreenRefreshRateEvent)
  @overload(NoneType)
  def processScreenRefreshRateChange(
      e: Optional[QWindowSystemInterfacePrivate.ScreenRefreshRateEvent],
  ) -> None:
    """
    Calls Qt's 'void QGuiApplicationPrivate::processScreenRefreshRateChange(
    QWindowSystemInterfacePrivate::ScreenRefreshRateEvent *e)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qguiapplicationprivate.html

    Parameters
    ----------

    e : Optional[QWindowSystemInterfacePrivate.ScreenRefreshRateEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGuiApplicationPrivate::processScreenRefreshRateChange(
    #      QWindowSystemInterfacePrivate::ScreenRefreshRateEvent *e)
    Rituals.call(
        'ritual_ZN22QGuiApplicationPrivate30processScreenRefreshRateChangeE'
        'PN29QWindowSystemInterfacePrivate22ScreenRefreshRateEventE',
        CuteMixin._addressOf(e),
    )

  @staticmethod
  @overload(QWindowSystemInterfacePrivate.ThemeChangeEvent)
  @overload(NoneType)
  def processThemeChanged(
      tce: Optional[QWindowSystemInterfacePrivate.ThemeChangeEvent],
  ) -> None:
    """
    Calls Qt's 'void QGuiApplicationPrivate::processThemeChanged(
    QWindowSystemInterfacePrivate::ThemeChangeEvent *tce)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qguiapplicationprivate.html#processThemeChanged

    Parameters
    ----------

    tce : Optional[QWindowSystemInterfacePrivate.ThemeChangeEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGuiApplicationPrivate::processThemeChanged(
    #      QWindowSystemInterfacePrivate::ThemeChangeEvent *tce)
    Rituals.call(
        'ritual_ZN22QGuiApplicationPrivate19processThemeChangedEPN29QWindow'
        'SystemInterfacePrivate16ThemeChangeEventE',
        CuteMixin._addressOf(tce),
    )

  @staticmethod
  @overload(QWindowSystemInterfacePrivate.ExposeEvent)
  @overload(NoneType)
  def processExposeEvent(
      e: Optional[QWindowSystemInterfacePrivate.ExposeEvent],
  ) -> None:
    """
    Calls Qt's 'void QGuiApplicationPrivate::processExposeEvent(
    QWindowSystemInterfacePrivate::ExposeEvent *e)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qguiapplicationprivate.html#processExposeEvent

    Parameters
    ----------

    e : Optional[QWindowSystemInterfacePrivate.ExposeEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGuiApplicationPrivate::processExposeEvent(
    #      QWindowSystemInterfacePrivate::ExposeEvent *e)
    Rituals.call(
        'ritual_ZN22QGuiApplicationPrivate18processExposeEventEPN29QWindowS'
        'ystemInterfacePrivate11ExposeEventE',
        CuteMixin._addressOf(e),
    )

  @staticmethod
  @overload(QWindowSystemInterfacePrivate.PaintEvent)
  @overload(NoneType)
  def processPaintEvent(
      e: Optional[QWindowSystemInterfacePrivate.PaintEvent],
  ) -> None:
    """
    Calls Qt's 'void QGuiApplicationPrivate::processPaintEvent(
    QWindowSystemInterfacePrivate::PaintEvent *e)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qguiapplicationprivate.html#processPaintEvent

    Parameters
    ----------

    e : Optional[QWindowSystemInterfacePrivate.PaintEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGuiApplicationPrivate::processPaintEvent(
    #      QWindowSystemInterfacePrivate::PaintEvent *e)
    Rituals.call(
        'ritual_ZN22QGuiApplicationPrivate17processPaintEventEPN29QWindowSy'
        'stemInterfacePrivate10PaintEventE',
        CuteMixin._addressOf(e),
    )

  @staticmethod
  @overload(QWindowSystemInterfacePrivate.FileOpenEvent)
  @overload(NoneType)
  def processFileOpenEvent(
      e: Optional[QWindowSystemInterfacePrivate.FileOpenEvent],
  ) -> None:
    """
    Calls Qt's 'void QGuiApplicationPrivate::processFileOpenEvent(
    QWindowSystemInterfacePrivate::FileOpenEvent *e)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qguiapplicationprivate.html#processFileOpenEvent

    Parameters
    ----------

    e : Optional[QWindowSystemInterfacePrivate.FileOpenEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGuiApplicationPrivate::processFileOpenEvent(
    #      QWindowSystemInterfacePrivate::FileOpenEvent *e)
    Rituals.call(
        'ritual_ZN22QGuiApplicationPrivate20processFileOpenEventEPN29QWindo'
        'wSystemInterfacePrivate13FileOpenEventE',
        CuteMixin._addressOf(e),
    )

  @staticmethod
  @overload(QWindowSystemInterfacePrivate.TabletEvent)
  @overload(NoneType)
  def processTabletEvent(
      e: Optional[QWindowSystemInterfacePrivate.TabletEvent],
  ) -> None:
    """
    Calls Qt's 'void QGuiApplicationPrivate::processTabletEvent(
    QWindowSystemInterfacePrivate::TabletEvent *e)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qguiapplicationprivate.html#processTabletEvent

    Parameters
    ----------

    e : Optional[QWindowSystemInterfacePrivate.TabletEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGuiApplicationPrivate::processTabletEvent(
    #      QWindowSystemInterfacePrivate::TabletEvent *e)
    Rituals.call(
        'ritual_ZN22QGuiApplicationPrivate18processTabletEventEPN29QWindowS'
        'ystemInterfacePrivate11TabletEventE',
        CuteMixin._addressOf(e),
    )

  @staticmethod
  @overload(QWindowSystemInterfacePrivate.TabletEnterProximityEvent)
  @overload(NoneType)
  def processTabletEnterProximityEvent(
      e: Optional[QWindowSystemInterfacePrivate.TabletEnterProximityEvent],
  ) -> None:
    """
    Calls Qt's 'void
    QGuiApplicationPrivate::processTabletEnterProximityEvent(
    QWindowSystemInterfacePrivate::TabletEnterProximityEvent *e)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qguiapplicationprivate.html

    Parameters
    ----------

    e : Optional[QWindowSystemInterfacePrivate.TabletEnterProximityEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGuiApplicationPrivate::processTabletEnterProximityEvent(
    #      QWindowSystemInterfacePrivate::TabletEnterProximityEvent *e)
    Rituals.call(
        'ritual_ZN22QGuiApplicationPrivate32processTabletEnterProximityEven'
        'tEPN29QWindowSystemInterfacePrivate25TabletEnterProximityEventE',
        CuteMixin._addressOf(e),
    )

  @staticmethod
  @overload(QWindowSystemInterfacePrivate.TabletLeaveProximityEvent)
  @overload(NoneType)
  def processTabletLeaveProximityEvent(
      e: Optional[QWindowSystemInterfacePrivate.TabletLeaveProximityEvent],
  ) -> None:
    """
    Calls Qt's 'void
    QGuiApplicationPrivate::processTabletLeaveProximityEvent(
    QWindowSystemInterfacePrivate::TabletLeaveProximityEvent *e)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qguiapplicationprivate.html

    Parameters
    ----------

    e : Optional[QWindowSystemInterfacePrivate.TabletLeaveProximityEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGuiApplicationPrivate::processTabletLeaveProximityEvent(
    #      QWindowSystemInterfacePrivate::TabletLeaveProximityEvent *e)
    Rituals.call(
        'ritual_ZN22QGuiApplicationPrivate32processTabletLeaveProximityEven'
        'tEPN29QWindowSystemInterfacePrivate25TabletLeaveProximityEventE',
        CuteMixin._addressOf(e),
    )

  @staticmethod
  @overload(QWindowSystemInterfacePrivate.GestureEvent)
  @overload(NoneType)
  def processGestureEvent(
      e: Optional[QWindowSystemInterfacePrivate.GestureEvent],
  ) -> None:
    """
    Calls Qt's 'void QGuiApplicationPrivate::processGestureEvent(
    QWindowSystemInterfacePrivate::GestureEvent *e)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qguiapplicationprivate.html#processGestureEvent

    Parameters
    ----------

    e : Optional[QWindowSystemInterfacePrivate.GestureEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGuiApplicationPrivate::processGestureEvent(
    #      QWindowSystemInterfacePrivate::GestureEvent *e)
    Rituals.call(
        'ritual_ZN22QGuiApplicationPrivate19processGestureEventEPN29QWindow'
        'SystemInterfacePrivate12GestureEventE',
        CuteMixin._addressOf(e),
    )

  @staticmethod
  @overload(QWindowSystemInterfacePrivate.PlatformPanelEvent)
  @overload(NoneType)
  def processPlatformPanelEvent(
      e: Optional[QWindowSystemInterfacePrivate.PlatformPanelEvent],
  ) -> None:
    """
    Calls Qt's 'void QGuiApplicationPrivate::processPlatformPanelEvent(
    QWindowSystemInterfacePrivate::PlatformPanelEvent *e)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qguiapplicationprivate.html

    Parameters
    ----------

    e : Optional[QWindowSystemInterfacePrivate.PlatformPanelEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGuiApplicationPrivate::processPlatformPanelEvent(
    #      QWindowSystemInterfacePrivate::PlatformPanelEvent *e)
    Rituals.call(
        'ritual_ZN22QGuiApplicationPrivate25processPlatformPanelEventEPN29Q'
        'WindowSystemInterfacePrivate18PlatformPanelEventE',
        CuteMixin._addressOf(e),
    )

  @staticmethod
  @overload(QWindowSystemInterfacePrivate.ContextMenuEvent)
  @overload(NoneType)
  def processContextMenuEvent(
      e: Optional[QWindowSystemInterfacePrivate.ContextMenuEvent],
  ) -> None:
    """
    Calls Qt's 'void QGuiApplicationPrivate::processContextMenuEvent(
    QWindowSystemInterfacePrivate::ContextMenuEvent *e)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qguiapplicationprivate.html

    Parameters
    ----------

    e : Optional[QWindowSystemInterfacePrivate.ContextMenuEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGuiApplicationPrivate::processContextMenuEvent(
    #      QWindowSystemInterfacePrivate::ContextMenuEvent *e)
    Rituals.call(
        'ritual_ZN22QGuiApplicationPrivate23processContextMenuEventEPN29QWi'
        'ndowSystemInterfacePrivate16ContextMenuEventE',
        CuteMixin._addressOf(e),
    )

  @staticmethod
  @overload(
      QWindow, QMimeData, QPoint, Qt.DropActions, Qt.MouseButtons,
      Qt.KeyboardModifiers,
  )
  @overload(
      QWindow, NoneType, QPoint, Qt.DropActions, Qt.MouseButtons,
      Qt.KeyboardModifiers,
  )
  @overload(
      NoneType, QMimeData, QPoint, Qt.DropActions, Qt.MouseButtons,
      Qt.KeyboardModifiers,
  )
  @overload(
      NoneType, NoneType, QPoint, Qt.DropActions, Qt.MouseButtons,
      Qt.KeyboardModifiers,
  )
  def processDrag(
      w: Optional[QWindow],
      dropData: Optional[QMimeData],
      p: QPoint,
      supportedActions: Qt.DropActions,
      buttons: Qt.MouseButtons,
      modifiers: Qt.KeyboardModifiers,
  ) -> QPlatformDragQtResponse:
    """
    Calls Qt's 'QPlatformDragQtResponse
    QGuiApplicationPrivate::processDrag(QWindow *w, const QMimeData
    *dropData, const QPoint &p, Qt::DropActions supportedActions,
    Qt::MouseButtons buttons, Qt::KeyboardModifiers modifiers)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qguiapplicationprivate.html#processDrag

    Parameters
    ----------

    w : Optional[QWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    dropData : Optional[QMimeData]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    p : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.

    supportedActions : Qt.DropActions
      Passed on as its number.

    buttons : Qt.MouseButtons
      Passed on as its number.

    modifiers : Qt.KeyboardModifiers
      Passed on as its number.

    Returns
    -------

    QPlatformDragQtResponse
      A new cute QPlatformDragQtResponse around the copy Qt gave back. Python
      owns it.
    """
    #  QPlatformDragQtResponse QGuiApplicationPrivate::processDrag(QWindow
    #      *w, const QMimeData *dropData, const QPoint &p, Qt::DropActions
    #      supportedActions, Qt::MouseButtons buttons, Qt::KeyboardModifiers
    #      modifiers)
    address = Rituals.call(
        'ritual_ZN22QGuiApplicationPrivate11processDragEP7QWindowPK9QMimeDa'
        'taRK6QPoint6QFlagsIN2Qt10DropActionEES8_INS9_11MouseButtonEES8_INS'
        '9_16KeyboardModifierEE',
        CuteMixin._addressOf(w), CuteMixin._addressOf(dropData),
        CuteMixin._valueOf(p), supportedActions.value, buttons.value,
        modifiers.value,
    )
    from . import QPlatformDragQtResponse
    return QPlatformDragQtResponse._cuteOwning(address)

  @staticmethod
  @overload(
      QWindow, QMimeData, QPoint, Qt.DropActions, Qt.MouseButtons,
      Qt.KeyboardModifiers,
  )
  @overload(
      QWindow, NoneType, QPoint, Qt.DropActions, Qt.MouseButtons,
      Qt.KeyboardModifiers,
  )
  @overload(
      NoneType, QMimeData, QPoint, Qt.DropActions, Qt.MouseButtons,
      Qt.KeyboardModifiers,
  )
  @overload(
      NoneType, NoneType, QPoint, Qt.DropActions, Qt.MouseButtons,
      Qt.KeyboardModifiers,
  )
  def processDrop(
      w: Optional[QWindow],
      dropData: Optional[QMimeData],
      p: QPoint,
      supportedActions: Qt.DropActions,
      buttons: Qt.MouseButtons,
      modifiers: Qt.KeyboardModifiers,
  ) -> QPlatformDropQtResponse:
    """
    Calls Qt's 'QPlatformDropQtResponse
    QGuiApplicationPrivate::processDrop(QWindow *w, const QMimeData
    *dropData, const QPoint &p, Qt::DropActions supportedActions,
    Qt::MouseButtons buttons, Qt::KeyboardModifiers modifiers)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qguiapplicationprivate.html#processDrop

    Parameters
    ----------

    w : Optional[QWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    dropData : Optional[QMimeData]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    p : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.

    supportedActions : Qt.DropActions
      Passed on as its number.

    buttons : Qt.MouseButtons
      Passed on as its number.

    modifiers : Qt.KeyboardModifiers
      Passed on as its number.

    Returns
    -------

    QPlatformDropQtResponse
      A new cute QPlatformDropQtResponse around the copy Qt gave back. Python
      owns it.
    """
    #  QPlatformDropQtResponse QGuiApplicationPrivate::processDrop(QWindow
    #      *w, const QMimeData *dropData, const QPoint &p, Qt::DropActions
    #      supportedActions, Qt::MouseButtons buttons, Qt::KeyboardModifiers
    #      modifiers)
    address = Rituals.call(
        'ritual_ZN22QGuiApplicationPrivate11processDropEP7QWindowPK9QMimeDa'
        'taRK6QPoint6QFlagsIN2Qt10DropActionEES8_INS9_11MouseButtonEES8_INS'
        '9_16KeyboardModifierEE',
        CuteMixin._addressOf(w), CuteMixin._addressOf(dropData),
        CuteMixin._valueOf(p), supportedActions.value, buttons.value,
        modifiers.value,
    )
    from . import QPlatformDropQtResponse
    return QPlatformDropQtResponse._cuteOwning(address)

  @staticmethod
  @overload(QWindow, QEvent)
  @overload(QWindow, NoneType)
  @overload(NoneType, QEvent)
  @overload(NoneType, NoneType)
  def sendQWindowEventToQPlatformWindow(
      window: Optional[QWindow],
      event: Optional[QEvent],
  ) -> bool:
    """
    Calls Qt's 'bool
    QGuiApplicationPrivate::sendQWindowEventToQPlatformWindow(QWindow
    *window, QEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qguiapplicationprivate.html

    Parameters
    ----------

    window : Optional[QWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    event : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QGuiApplicationPrivate::sendQWindowEventToQPlatformWindow(QWindow
    #      *window, QEvent *event)
    return Rituals.call(
        'ritual_ZN22QGuiApplicationPrivate33sendQWindowEventToQPlatformWind'
        'owEP7QWindowP6QEvent',
        CuteMixin._addressOf(window), CuteMixin._addressOf(event),
    )

  @staticmethod
  @overload(QEvent)
  @overload(NoneType)
  def maybeForwardEventToVirtualKeyboard(e: Optional[QEvent]) -> bool:
    """
    Calls Qt's 'bool
    QGuiApplicationPrivate::maybeForwardEventToVirtualKeyboard(QEvent *e)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qguiapplicationprivate.html

    Parameters
    ----------

    e : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QGuiApplicationPrivate::maybeForwardEventToVirtualKeyboard(QEvent
    #      *e)
    return Rituals.call(
        'ritual_ZN22QGuiApplicationPrivate34maybeForwardEventToVirtualKeybo'
        'ardEP6QEvent',
        CuteMixin._addressOf(e),
    )

  @staticmethod
  def isUsingVirtualKeyboard() -> bool:
    """
    Calls Qt's 'bool QGuiApplicationPrivate::isUsingVirtualKeyboard()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qguiapplicationprivate.html#isUsingVirtualKeyboard
    """
    #  bool QGuiApplicationPrivate::isUsingVirtualKeyboard()
    return Rituals.call(
        'ritual_ZN22QGuiApplicationPrivate22isUsingVirtualKeyboardEv',
    )

  @staticmethod
  @overload(Qt.LayoutDirection, Qt.Alignment)
  def visualAlignment(
      direction: Qt.LayoutDirection,
      alignment: Qt.Alignment,
  ) -> Qt.Alignment:
    """
    Calls Qt's 'Qt::Alignment
    QGuiApplicationPrivate::visualAlignment(Qt::LayoutDirection direction,
    Qt::Alignment alignment)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qguiapplicationprivate.html#visualAlignment

    Parameters
    ----------

    direction : Qt.LayoutDirection
      Passed on as its number.

    alignment : Qt.Alignment
      Passed on as its number.

    Returns
    -------

    Qt.Alignment
      The value standing for the combination Qt gave back.
    """
    #  Qt::Alignment
    #      QGuiApplicationPrivate::visualAlignment(Qt::LayoutDirection
    #      direction, Qt::Alignment alignment)
    return Qt.Alignment(Rituals.call(
        'ritual_ZN22QGuiApplicationPrivate15visualAlignmentEN2Qt15LayoutDir'
        'ectionE6QFlagsINS0_13AlignmentFlagEE',
        direction.value, alignment.value,
    ))

  @staticmethod
  def instance() -> Optional[QGuiApplicationPrivate]:
    """
    Calls Qt's 'QGuiApplicationPrivate *QGuiApplicationPrivate::instance()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qguiapplicationprivate.html#instance

    Returns
    -------

    Optional[QGuiApplicationPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QGuiApplicationPrivate *QGuiApplicationPrivate::instance()
    address = Rituals.call('ritual_ZN22QGuiApplicationPrivate8instanceEv')
    return QGuiApplicationPrivate._cuteAt(address)

  @staticmethod
  @overload(QWindow)
  @overload(NoneType)
  def showModalWindow(window: Optional[QWindow]) -> None:
    """
    Calls Qt's 'void QGuiApplicationPrivate::showModalWindow(QWindow
    *window)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qguiapplicationprivate.html#showModalWindow

    Parameters
    ----------

    window : Optional[QWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGuiApplicationPrivate::showModalWindow(QWindow *window)
    Rituals.call(
        'ritual_ZN22QGuiApplicationPrivate15showModalWindowEP7QWindow',
        CuteMixin._addressOf(window),
    )

  @staticmethod
  @overload(QWindow)
  @overload(NoneType)
  def hideModalWindow(window: Optional[QWindow]) -> None:
    """
    Calls Qt's 'void QGuiApplicationPrivate::hideModalWindow(QWindow
    *window)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qguiapplicationprivate.html#hideModalWindow

    Parameters
    ----------

    window : Optional[QWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGuiApplicationPrivate::hideModalWindow(QWindow *window)
    Rituals.call(
        'ritual_ZN22QGuiApplicationPrivate15hideModalWindowEP7QWindow',
        CuteMixin._addressOf(window),
    )

  @staticmethod
  @overload(QWindow)
  @overload(NoneType)
  def updateBlockedStatus(window: Optional[QWindow]) -> None:
    """
    Calls Qt's 'void QGuiApplicationPrivate::updateBlockedStatus(QWindow
    *window)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qguiapplicationprivate.html#updateBlockedStatus

    Parameters
    ----------

    window : Optional[QWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGuiApplicationPrivate::updateBlockedStatus(QWindow *window)
    Rituals.call(
        'ritual_ZN22QGuiApplicationPrivate19updateBlockedStatusEP7QWindow',
        CuteMixin._addressOf(window),
    )

  @staticmethod
  def popupCount() -> int:
    """
    Calls Qt's 'qsizetype QGuiApplicationPrivate::popupCount()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qguiapplicationprivate.html#popupCount
    """
    #  qsizetype QGuiApplicationPrivate::popupCount()
    return Rituals.call('ritual_ZN22QGuiApplicationPrivate10popupCountEv')

  @staticmethod
  def activePopupWindow() -> Optional[QWindow]:
    """
    Calls Qt's 'QWindow *QGuiApplicationPrivate::activePopupWindow()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qguiapplicationprivate.html#activePopupWindow

    Returns
    -------

    Optional[QWindow]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWindow *QGuiApplicationPrivate::activePopupWindow()
    address = Rituals.call(
        'ritual_ZN22QGuiApplicationPrivate17activePopupWindowEv',
    )
    from . import QWindow
    return QWindow._cuteAt(address)

  @staticmethod
  @overload(QWindow)
  @overload(NoneType)
  def activatePopup(popup: Optional[QWindow]) -> None:
    """
    Calls Qt's 'void QGuiApplicationPrivate::activatePopup(QWindow *popup)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qguiapplicationprivate.html#activatePopup

    Parameters
    ----------

    popup : Optional[QWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGuiApplicationPrivate::activatePopup(QWindow *popup)
    Rituals.call(
        'ritual_ZN22QGuiApplicationPrivate13activatePopupEP7QWindow',
        CuteMixin._addressOf(popup),
    )

  @staticmethod
  @overload(QWindow)
  @overload(NoneType)
  def closePopup(popup: Optional[QWindow]) -> bool:
    """
    Calls Qt's 'bool QGuiApplicationPrivate::closePopup(QWindow *popup)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qguiapplicationprivate.html#closePopup

    Parameters
    ----------

    popup : Optional[QWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QGuiApplicationPrivate::closePopup(QWindow *popup)
    return Rituals.call(
        'ritual_ZN22QGuiApplicationPrivate10closePopupEP7QWindow',
        CuteMixin._addressOf(popup),
    )

  @staticmethod
  def closeAllPopups() -> bool:
    """
    Calls Qt's 'bool QGuiApplicationPrivate::closeAllPopups()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qguiapplicationprivate.html#closeAllPopups
    """
    #  bool QGuiApplicationPrivate::closeAllPopups()
    return Rituals.call(
        'ritual_ZN22QGuiApplicationPrivate14closeAllPopupsEv',
    )

  @staticmethod
  def inputDeviceManager() -> Optional[QInputDeviceManager]:
    """
    Calls Qt's 'QInputDeviceManager
    *QGuiApplicationPrivate::inputDeviceManager()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qguiapplicationprivate.html#inputDeviceManager

    Returns
    -------

    Optional[QInputDeviceManager]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QInputDeviceManager *QGuiApplicationPrivate::inputDeviceManager()
    address = Rituals.call(
        'ritual_ZN22QGuiApplicationPrivate18inputDeviceManagerEv',
    )
    from . import QInputDeviceManager
    return QInputDeviceManager._cuteAt(address)

  @staticmethod
  @overload(QWindow)
  @overload(NoneType)
  def applyWindowGeometrySpecificationTo(window: Optional[QWindow]) -> None:
    """
    Calls Qt's 'void
    QGuiApplicationPrivate::applyWindowGeometrySpecificationTo(QWindow
    *window)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qguiapplicationprivate.html

    Parameters
    ----------

    window : Optional[QWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void
    #      QGuiApplicationPrivate::applyWindowGeometrySpecificationTo(QWindow
    #      *window)
    Rituals.call(
        'ritual_ZN22QGuiApplicationPrivate34applyWindowGeometrySpecificatio'
        'nToEP7QWindow',
        CuteMixin._addressOf(window),
    )

  @staticmethod
  @overload(Qt.ApplicationState)
  @overload(Qt.ApplicationState, bool)
  def setApplicationState(
      state: Qt.ApplicationState,
      forcePropagate: bool = False,
  ) -> None:
    """
    Calls Qt's 'void
    QGuiApplicationPrivate::setApplicationState(Qt::ApplicationState state,
    bool forcePropagate)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qguiapplicationprivate.html#setApplicationState

    Parameters
    ----------

    state : Qt.ApplicationState
      Passed on as its number.

    forcePropagate : bool
      Passed on as it is. May be left out, as in Qt: it is then False.
    """
    #  void QGuiApplicationPrivate::setApplicationState(Qt::ApplicationState
    #      state, bool forcePropagate)
    Rituals.call(
        'ritual_ZN22QGuiApplicationPrivate19setApplicationStateEN2Qt16Appli'
        'cationStateEb',
        state.value, forcePropagate,
    )

  @staticmethod
  def resetCachedDevicePixelRatio() -> None:
    """
    Calls Qt's 'void QGuiApplicationPrivate::resetCachedDevicePixelRatio()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qguiapplicationprivate.html
    """
    #  void QGuiApplicationPrivate::resetCachedDevicePixelRatio()
    Rituals.call(
        'ritual_ZN22QGuiApplicationPrivate27resetCachedDevicePixelRatioEv',
    )

  @staticmethod
  def updatePalette() -> None:
    """
    Calls Qt's 'void QGuiApplicationPrivate::updatePalette()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qguiapplicationprivate.html#updatePalette
    """
    #  void QGuiApplicationPrivate::updatePalette()
    Rituals.call('ritual_ZN22QGuiApplicationPrivate13updatePaletteEv')

  @staticmethod
  def contextMenuEventType() -> QEvent.Type:
    """
    Calls Qt's 'QEvent::Type QGuiApplicationPrivate::contextMenuEventType()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qguiapplicationprivate.html#contextMenuEventType

    Returns
    -------

    QEvent.Type
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'QEvent.Type(number)'
      gives.
    """
    #  QEvent::Type QGuiApplicationPrivate::contextMenuEventType()
    return QEvent.Type(Rituals.call(
        'ritual_ZN22QGuiApplicationPrivate20contextMenuEventTypeEv',
    ))

  @staticmethod
  def qtGuiThreadPool() -> Optional[QThreadPool]:
    """
    Calls Qt's 'QThreadPool *QGuiApplicationPrivate::qtGuiThreadPool()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qguiapplicationprivate.html#qtGuiThreadPool

    Returns
    -------

    Optional[QThreadPool]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QThreadPool *QGuiApplicationPrivate::qtGuiThreadPool()
    address = Rituals.call(
        'ritual_ZN22QGuiApplicationPrivate15qtGuiThreadPoolEv',
    )
    from ..QtCore import QThreadPool
    return QThreadPool._cuteAt(address)

  @staticmethod
  @overload(QPalette)
  def setPalette(palette: QPalette) -> bool:
    """
    Calls Qt's 'bool QGuiApplicationPrivate::setPalette(const QPalette
    &palette)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qguiapplicationprivate.html#setPalette

    Parameters
    ----------

    palette : QPalette
      Passed on as a value: Qt reads the C++ QPalette, which stays Python's
      own.
    """
    #  bool QGuiApplicationPrivate::setPalette(const QPalette &palette)
    return Rituals.call(
        'ritual_ZN22QGuiApplicationPrivate10setPaletteERK8QPalette',
        CuteMixin._valueOf(palette),
    )

  @staticmethod
  def clearPalette() -> None:
    """
    Calls Qt's 'void QGuiApplicationPrivate::clearPalette()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qguiapplicationprivate.html#clearPalette
    """
    #  void QGuiApplicationPrivate::clearPalette()
    Rituals.call('ritual_ZN22QGuiApplicationPrivate12clearPaletteEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QGuiApplicationPrivate'

  #  A C++ QGuiApplicationPrivate Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QGuiApplicationPrivate'

  #  The functions Qt calls itself that QGuiApplicationPrivate is the first
  #  to declare and that cannot be handed to Python yet, each as Qt declares
  #  it. A class of a program that writes one of them anew is refused, since
  #  Qt would never call what it wrote; see 'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'handlePaletteChanged': (
          'void QGuiApplicationPrivate::handlePaletteChanged(const char *)',
      ),
  }

  #  The functions Qt calls itself that QGuiApplicationPrivate is the first
  #  to declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'notifyLayoutDirectionChange': (
          ('_ZN22QGuiApplicationPrivate27notifyLayoutDirectionChangeEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'notifyActiveWindowChange': (
          ('_ZN22QGuiApplicationPrivate24notifyActiveWindowChangeEP7QWindow',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtGui:QWindow'),
           )),
      ),
      'defaultModality': (
          ('_ZNK22QGuiApplicationPrivate15defaultModalityEv',
           ('int', 'enum', 'QtCore:Qt.WindowModality'),
           ()),
      ),
      'windowNeverBlocked': (
          ('_ZNK22QGuiApplicationPrivate18windowNeverBlockedEP7QWindow',
           ('bool', 'number', ''),
           (
               ('address', 'address', 'QtGui:QWindow'),
           )),
      ),
      'applyQIconStyleHelper': (
          ('_ZNK22QGuiApplicationPrivate21applyQIconStyleHelperEN5QIcon4Mod'
           'eERK7QPixmap',
           ('address', 'value', 'QtGui:QPixmap'),
           (
               ('int', 'enum', 'QtGui:QIcon.Mode'),
               ('address', 'value', 'QtGui:QPixmap'),
           )),
      ),
      'notifyWindowIconChanged': (
          ('_ZN22QGuiApplicationPrivate23notifyWindowIconChangedEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'createActionPrivate': (
          ('_ZNK22QGuiApplicationPrivate19createActionPrivateEv',
           ('address', 'address', 'QtGui:QActionPrivate'),
           ()),
      ),
      'createShortcutPrivate': (
          ('_ZNK22QGuiApplicationPrivate21createShortcutPrivateEv',
           ('address', 'address', 'QtGui:QShortcutPrivate'),
           ()),
      ),
      'handleThemeChanged': (
          ('_ZN22QGuiApplicationPrivate18handleThemeChangedEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'basePalette': (
          ('_ZNK22QGuiApplicationPrivate11basePaletteEv',
           ('address', 'value', 'QtGui:QPalette'),
           ()),
      ),
      'notifyDragStarted': (
          ('_ZN22QGuiApplicationPrivate17notifyDragStartedEPK5QDrag',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtGui:QDrag'),
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

  def lastWindowClosed(self) -> bool:
    """
    Calls Qt's 'bool QGuiApplicationPrivate::lastWindowClosed() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qguiapplicationprivate.html#lastWindowClosed
    """
    #  bool QGuiApplicationPrivate::lastWindowClosed() const
    return self.uglySide.call(
        'ritual_ZNK22QGuiApplicationPrivate16lastWindowClosedEv',
    )

  def defaultModality(self) -> Qt.WindowModality:
    """
    Calls Qt's 'Qt::WindowModality QGuiApplicationPrivate::defaultModality()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qguiapplicationprivate.html#defaultModality

    Returns
    -------

    Qt.WindowModality
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'Qt.WindowModality(number)' gives.
    """
    #  Qt::WindowModality QGuiApplicationPrivate::defaultModality() const
    ritual = 'ritual_ZNK22QGuiApplicationPrivate15defaultModalityEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK22QGuiApplicationPrivate15defaultModalityEv'
    return Qt.WindowModality(self.uglySide.call(ritual))

  @overload(QWindow)
  @overload(NoneType)
  def windowNeverBlocked(self, window: Optional[QWindow]) -> bool:
    """
    Calls Qt's 'bool QGuiApplicationPrivate::windowNeverBlocked(QWindow
    *window) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qguiapplicationprivate.html#windowNeverBlocked

    Parameters
    ----------

    window : Optional[QWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QGuiApplicationPrivate::windowNeverBlocked(QWindow *window) const
    ritual = (
        'ritual_ZNK22QGuiApplicationPrivate18windowNeverBlockedEP7QWindow')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK22QGuiApplicationPrivate18windowNeverBlockedEP7QWi'
          'ndow')
    return self.uglySide.call(ritual, self._addressOf(window))

  @overload(QIcon.Mode, QPixmap)
  def applyQIconStyleHelper(
      self,
      a0: QIcon.Mode,
      basePixmap: QPixmap,
  ) -> QPixmap:
    """
    Calls Qt's 'QPixmap
    QGuiApplicationPrivate::applyQIconStyleHelper(QIcon::Mode a0, const
    QPixmap &basePixmap) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qguiapplicationprivate.html#applyQIconStyleHelper

    Parameters
    ----------

    a0 : QIcon.Mode
      Passed on as its number.

    basePixmap : QPixmap
      Passed on as a value: Qt reads the C++ QPixmap, which stays Python's
      own.

    Returns
    -------

    QPixmap
      A new cute QPixmap around the copy Qt gave back. Python owns it.
    """
    #  QPixmap QGuiApplicationPrivate::applyQIconStyleHelper(QIcon::Mode a0,
    #      const QPixmap &basePixmap) const
    ritual = (
        'ritual_ZNK22QGuiApplicationPrivate21applyQIconStyleHelperEN5QIcon4'
        'ModeERK7QPixmap')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK22QGuiApplicationPrivate21applyQIconStyleHelperEN5'
          'QIcon4ModeERK7QPixmap')
    address = self.uglySide.call(ritual, a0.value, self._valueOf(basePixmap))
    from . import QPixmap
    return QPixmap._cuteOwning(address)

  def createActionPrivate(self) -> Optional[QActionPrivate]:
    """
    Calls Qt's 'QActionPrivate *QGuiApplicationPrivate::createActionPrivate()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qguiapplicationprivate.html#createActionPrivate

    Returns
    -------

    Optional[QActionPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QActionPrivate *QGuiApplicationPrivate::createActionPrivate() const
    ritual = 'ritual_ZNK22QGuiApplicationPrivate19createActionPrivateEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK22QGuiApplicationPrivate19createActionPrivateEv')
    address = self.uglySide.call(ritual)
    from . import QActionPrivate
    return QActionPrivate._cuteAt(address)

  def createShortcutPrivate(self) -> Optional[QShortcutPrivate]:
    """
    Calls Qt's 'QShortcutPrivate
    *QGuiApplicationPrivate::createShortcutPrivate() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qguiapplicationprivate.html#createShortcutPrivate

    Returns
    -------

    Optional[QShortcutPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QShortcutPrivate *QGuiApplicationPrivate::createShortcutPrivate()
    #      const
    ritual = 'ritual_ZNK22QGuiApplicationPrivate21createShortcutPrivateEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK22QGuiApplicationPrivate21createShortcutPrivateEv')
    address = self.uglySide.call(ritual)
    from . import QShortcutPrivate
    return QShortcutPrivate._cuteAt(address)

  def basePalette(self) -> QPalette:
    """
    Calls Qt's 'QPalette QGuiApplicationPrivate::basePalette() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qguiapplicationprivate.html#basePalette

    Returns
    -------

    QPalette
      A new cute QPalette around the copy Qt gave back. Python owns it.
    """
    #  QPalette QGuiApplicationPrivate::basePalette() const
    ritual = 'ritual_ZNK22QGuiApplicationPrivate11basePaletteEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK22QGuiApplicationPrivate11basePaletteEv'
    address = self.uglySide.call(ritual)
    from . import QPalette
    return QPalette._cuteOwning(address)

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
    'QGuiApplicationPrivate::QGuiApplicationPrivate(int &argc, char **argv)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qguiapplicationprivate.html#QGuiApplicationPrivate

    Parameters
    ----------

    argv : list
      The texts the program was started with, as 'sys.argv'. Passed on as Qt
      takes them: how many they are, and where the first one is.
    """
    #  QGuiApplicationPrivate::QGuiApplicationPrivate(int &argc, char **argv)
    self._noteCreation(QGuiApplicationPrivate, lambda: Rituals.call(
        'ritual_ZN22QGuiApplicationPrivateC1ERiPPc',
        *self._startTextsOf(argv),
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

  def q_func(self) -> Optional[QGuiApplication]:
    """
    Calls Qt's 'QGuiApplication *QGuiApplicationPrivate::q_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qguiapplicationprivate.html#q_func

    Returns
    -------

    Optional[QGuiApplication]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QGuiApplication *QGuiApplicationPrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN22QGuiApplicationPrivate6q_funcEv',
    )
    from . import QGuiApplication
    return QGuiApplication._cuteAt(address)

  def init(self) -> None:
    """
    Calls Qt's 'void QGuiApplicationPrivate::init()'.

    Qt's own words: https://doc.qt.io/qt-6/qguiapplicationprivate.html#init
    """
    #  void QGuiApplicationPrivate::init()
    self.uglySide.call('ritual_ZN22QGuiApplicationPrivate4initEv')

  def createPlatformIntegration(self) -> None:
    """
    Calls Qt's 'void QGuiApplicationPrivate::createPlatformIntegration()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qguiapplicationprivate.html
    """
    #  void QGuiApplicationPrivate::createPlatformIntegration()
    self.uglySide.call(
        'ritual_ZN22QGuiApplicationPrivate25createPlatformIntegrationEv',
    )

  def createEventDispatcher(self) -> None:
    """
    Calls Qt's 'void QGuiApplicationPrivate::createEventDispatcher()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qguiapplicationprivate.html#createEventDispatcher
    """
    #  void QGuiApplicationPrivate::createEventDispatcher()
    ritual = 'ritual_ZN22QGuiApplicationPrivate21createEventDispatcherEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN22QGuiApplicationPrivate21createEventDispatcherEv')
    self.uglySide.call(ritual)

  def eventDispatcherReady(self) -> None:
    """
    Calls Qt's 'void QGuiApplicationPrivate::eventDispatcherReady()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qguiapplicationprivate.html#eventDispatcherReady
    """
    #  void QGuiApplicationPrivate::eventDispatcherReady()
    ritual = 'ritual_ZN22QGuiApplicationPrivate20eventDispatcherReadyEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN22QGuiApplicationPrivate20eventDispatcherReadyEv')
    self.uglySide.call(ritual)

  def notifyLayoutDirectionChange(self) -> None:
    """
    Calls Qt's 'void QGuiApplicationPrivate::notifyLayoutDirectionChange()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qguiapplicationprivate.html
    """
    #  void QGuiApplicationPrivate::notifyLayoutDirectionChange()
    ritual = (
        'ritual_ZN22QGuiApplicationPrivate27notifyLayoutDirectionChangeEv')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN22QGuiApplicationPrivate27notifyLayoutDirectionChan'
          'geEv')
    self.uglySide.call(ritual)

  @overload(QWindow)
  @overload(NoneType)
  def notifyActiveWindowChange(self, previous: Optional[QWindow]) -> None:
    """
    Calls Qt's 'void QGuiApplicationPrivate::notifyActiveWindowChange(QWindow
    *previous)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qguiapplicationprivate.html

    Parameters
    ----------

    previous : Optional[QWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGuiApplicationPrivate::notifyActiveWindowChange(QWindow
    #      *previous)
    ritual = (
        'ritual_ZN22QGuiApplicationPrivate24notifyActiveWindowChangeEP7QWin'
        'dow')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN22QGuiApplicationPrivate24notifyActiveWindowChangeE'
          'P7QWindow')
    self.uglySide.call(ritual, self._addressOf(previous))

  def canQuitAutomatically(self) -> bool:
    """
    Calls Qt's 'bool QGuiApplicationPrivate::canQuitAutomatically()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qguiapplicationprivate.html#canQuitAutomatically
    """
    #  bool QGuiApplicationPrivate::canQuitAutomatically()
    ritual = 'ritual_ZN22QGuiApplicationPrivate20canQuitAutomaticallyEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN22QGuiApplicationPrivate20canQuitAutomaticallyEv')
    return self.uglySide.call(ritual)

  def quit(self) -> None:
    """
    Calls Qt's 'void QGuiApplicationPrivate::quit()'.

    Qt's own words: https://doc.qt.io/qt-6/qguiapplicationprivate.html#quit
    """
    #  void QGuiApplicationPrivate::quit()
    ritual = 'ritual_ZN22QGuiApplicationPrivate4quitEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN22QGuiApplicationPrivate4quitEv'
    self.uglySide.call(ritual)

  def maybeLastWindowClosed(self) -> None:
    """
    Calls Qt's 'void QGuiApplicationPrivate::maybeLastWindowClosed()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qguiapplicationprivate.html#maybeLastWindowClosed
    """
    #  void QGuiApplicationPrivate::maybeLastWindowClosed()
    self.uglySide.call(
        'ritual_ZN22QGuiApplicationPrivate21maybeLastWindowClosedEv',
    )

  @overload(Qt.CursorShape)
  def getPixmapCursor(self, cshape: Qt.CursorShape) -> QPixmap:
    """
    Calls Qt's 'QPixmap
    QGuiApplicationPrivate::getPixmapCursor(Qt::CursorShape cshape)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qguiapplicationprivate.html#getPixmapCursor

    Parameters
    ----------

    cshape : Qt.CursorShape
      Passed on as its number.

    Returns
    -------

    QPixmap
      A new cute QPixmap around the copy Qt gave back. Python owns it.
    """
    #  QPixmap QGuiApplicationPrivate::getPixmapCursor(Qt::CursorShape
    #      cshape)
    address = self.uglySide.call(
        'ritual_ZN22QGuiApplicationPrivate15getPixmapCursorEN2Qt11CursorSha'
        'peE',
        cshape.value,
    )
    from . import QPixmap
    return QPixmap._cuteOwning(address)

  @overload(QObject)
  @overload(NoneType)
  def _q_updateFocusObject(self, object: Optional[QObject]) -> None:
    """
    Calls Qt's 'void QGuiApplicationPrivate::_q_updateFocusObject(QObject
    *object)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qguiapplicationprivate.html#_q_updateFocusObject

    Parameters
    ----------

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGuiApplicationPrivate::_q_updateFocusObject(QObject *object)
    self.uglySide.call(
        'ritual_ZN22QGuiApplicationPrivate20_q_updateFocusObjectEP7QObject',
        self._addressOf(object, 'QObject'),
    )

  def commitData(self) -> None:
    """
    Calls Qt's 'void QGuiApplicationPrivate::commitData()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qguiapplicationprivate.html#commitData
    """
    #  void QGuiApplicationPrivate::commitData()
    self.uglySide.call('ritual_ZN22QGuiApplicationPrivate10commitDataEv')

  def saveState(self) -> None:
    """
    Calls Qt's 'void QGuiApplicationPrivate::saveState()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qguiapplicationprivate.html#saveState
    """
    #  void QGuiApplicationPrivate::saveState()
    self.uglySide.call('ritual_ZN22QGuiApplicationPrivate9saveStateEv')

  def colorProfileForA8Text(self) -> Optional[QColorTrcLut]:
    """
    Calls Qt's 'const QColorTrcLut
    *QGuiApplicationPrivate::colorProfileForA8Text()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qguiapplicationprivate.html#colorProfileForA8Text

    Returns
    -------

    Optional[QColorTrcLut]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QColorTrcLut *QGuiApplicationPrivate::colorProfileForA8Text()
    address = self.uglySide.call(
        'ritual_ZN22QGuiApplicationPrivate21colorProfileForA8TextEv',
    )
    from . import QColorTrcLut
    return QColorTrcLut._cuteAt(address)

  def colorProfileForA32Text(self) -> Optional[QColorTrcLut]:
    """
    Calls Qt's 'const QColorTrcLut
    *QGuiApplicationPrivate::colorProfileForA32Text()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qguiapplicationprivate.html#colorProfileForA32Text

    Returns
    -------

    Optional[QColorTrcLut]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QColorTrcLut *QGuiApplicationPrivate::colorProfileForA32Text()
    address = self.uglySide.call(
        'ritual_ZN22QGuiApplicationPrivate22colorProfileForA32TextEv',
    )
    from . import QColorTrcLut
    return QColorTrcLut._cuteAt(address)

  def notifyWindowIconChanged(self) -> None:
    """
    Calls Qt's 'void QGuiApplicationPrivate::notifyWindowIconChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qguiapplicationprivate.html
    """
    #  void QGuiApplicationPrivate::notifyWindowIconChanged()
    ritual = 'ritual_ZN22QGuiApplicationPrivate23notifyWindowIconChangedEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN22QGuiApplicationPrivate23notifyWindowIconChangedEv')
    self.uglySide.call(ritual)

  def _q_updatePrimaryScreenDpis(self) -> None:
    """
    Calls Qt's 'void QGuiApplicationPrivate::_q_updatePrimaryScreenDpis()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qguiapplicationprivate.html
    """
    #  void QGuiApplicationPrivate::_q_updatePrimaryScreenDpis()
    self.uglySide.call(
        'ritual_ZN22QGuiApplicationPrivate26_q_updatePrimaryScreenDpisEv',
    )

  def handleThemeChanged(self) -> None:
    """
    Calls Qt's 'void QGuiApplicationPrivate::handleThemeChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qguiapplicationprivate.html#handleThemeChanged
    """
    #  void QGuiApplicationPrivate::handleThemeChanged()
    ritual = 'ritual_ZN22QGuiApplicationPrivate18handleThemeChangedEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN22QGuiApplicationPrivate18handleThemeChangedEv'
    self.uglySide.call(ritual)

  @overload()
  @overload(str)
  @overload(NoneType)
  def handlePaletteChanged(self, className: Optional[str] = None) -> None:
    """
    Calls Qt's 'void QGuiApplicationPrivate::handlePaletteChanged(const char
    *className)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qguiapplicationprivate.html#handlePaletteChanged

    Parameters
    ----------

    className : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text. May
      be left out, as in Qt: it is then None.
    """
    #  void QGuiApplicationPrivate::handlePaletteChanged(const char
    #      *className)
    self.uglySide.call(
        'ritual_ZN22QGuiApplicationPrivate20handlePaletteChangedEPKc',
        self._bytesOf(className),
    )

  @overload(QDrag)
  @overload(NoneType)
  def notifyDragStarted(self, a0: Optional[QDrag]) -> None:
    """
    Calls Qt's 'void QGuiApplicationPrivate::notifyDragStarted(const QDrag
    *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qguiapplicationprivate.html#notifyDragStarted

    Parameters
    ----------

    a0 : Optional[QDrag]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGuiApplicationPrivate::notifyDragStarted(const QDrag *a0)
    ritual = 'ritual_ZN22QGuiApplicationPrivate17notifyDragStartedEPK5QDrag'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN22QGuiApplicationPrivate17notifyDragStartedEPK5QDra'
          'g')
    self.uglySide.call(ritual, self._addressOf(a0))

  @staticmethod
  def isWindowBlocked(*__, **_) -> Never:
    """
    Qt's 'bool QGuiApplicationPrivate::isWindowBlocked(QWindow *window,
    QWindow **blockingWindow) const': takes a type Python has no way to hand
    over yet.
    """
    raise NotImplementedError(
        "'QGuiApplicationPrivate.isWindowBlocked' has no cute function yet. "
        "Qt's 'bool QGuiApplicationPrivate::isWindowBlocked(QWindow "
        "*window, QWindow **blockingWindow) const': takes a type Python has "
        "no way to hand over yet.")

  @staticmethod
  def processNativeEvent(*__, **_) -> Never:
    """
    Qt's 'bool QGuiApplicationPrivate::processNativeEvent(QWindow *window,
    const QByteArray &eventType, void *message, qintptr *result)': names
    'void', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QGuiApplicationPrivate.processNativeEvent' has no cute function "
        "yet. Qt's 'bool QGuiApplicationPrivate::processNativeEvent(QWindow "
        "*window, const QByteArray &eventType, void *message, qintptr "
        "*result)': names 'void', which has no cute class yet.")

  @staticmethod
  def tabletDevicePoint(*__, **_) -> Never:
    """
    Qt's 'TabletPointData &QGuiApplicationPrivate::tabletDevicePoint(qint64
    deviceId)': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QGuiApplicationPrivate.tabletDevicePoint' has no cute function "
        "yet. Qt's 'TabletPointData "
        "&QGuiApplicationPrivate::tabletDevicePoint(qint64 deviceId)': "
        "gives a type Python has no way to take yet.")

  @staticmethod
  def updateFilteredScreenOrientation(*__, **_) -> Never:
    """
    Qt's 'void
    QGuiApplicationPrivate::updateFilteredScreenOrientation(QScreen
    *screen)': cannot be called and cannot be called through the meta-object
    and cannot be copied: no header file has its code, Qt's source does not
    mark it or its class for use from outside Qt or writes it 'inline' or
    nowhere, and it is no signal, slot or invokable function giving back
    nothing, of a class built on QObject, and Qt's source has no code for it
    that could be told from the rest.
    """
    raise NotImplementedError(
        "'QGuiApplicationPrivate.updateFilteredScreenOrientation' has no "
        "cute function yet. Qt's 'void "
        "QGuiApplicationPrivate::updateFilteredScreenOrientation(QScreen "
        "*screen)': cannot be called and cannot be called through the "
        "meta-object and cannot be copied: no header file has its code, "
        "Qt's source does not mark it or its class for use from outside Qt "
        "or writes it 'inline' or nowhere, and it is no signal, slot or "
        "invokable function giving back nothing, of a class built on "
        "QObject, and Qt's source has no code for it that could be told "
        "from the rest.")
