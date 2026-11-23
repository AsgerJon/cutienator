"""
QApplication binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/qapplication.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import Qt, QList, QObject
from ..QtGui import QGuiApplication

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QEvent, QMetaObject, QPoint
  from ..QtGui import QFont, QFontMetrics, QPalette
  from . import QStyle, QWidget
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QEvent = WAIT['QEvent']
  QFont = WAIT['QFont']
  QPalette = WAIT['QPalette']
  QPoint = WAIT['QPoint']
  QStyle = WAIT['QStyle']
  QWidget = WAIT['QWidget']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QApplication(QGuiApplication):
  """
  The cute side of Qt's QApplication: a plain Python object standing in front
  of one C++ QApplication.

  It is built on the cute 'QGuiApplication', as Qt's QApplication is built on
  Qt's QGuiApplication, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QApplication that has a ritual and that Python can
  call so far, 43 names in all: 'metaObject', 'tr', 'style', 'setStyle',
  'palette', 'setPalette', 'font', 'setFont', 'fontMetrics', 'allWidgets',
  'topLevelWidgets', 'activePopupWidget', 'activeModalWidget', 'focusWidget',
  'activeWindow', 'setActiveWindow', 'widgetAt', 'topLevelAt', 'beep',
  'alert', 'setCursorFlashTime', 'cursorFlashTime', 'setDoubleClickInterval',
  'doubleClickInterval', 'setKeyboardInputInterval', 'keyboardInputInterval',
  'setWheelScrollLines', 'wheelScrollLines', 'setStartDragTime',
  'startDragTime', 'setStartDragDistance', 'startDragDistance',
  'isEffectEnabled', 'setEffectEnabled', 'exec', 'notify', 'styleSheet',
  'autoSipEnabled', 'setStyleSheet', 'setAutoSipEnabled', 'closeAllWindows',
  'aboutQt', 'event'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QApplication::~QApplication()': the destructor: Python never
    removes a C++ QApplication.

  What has no ritual
  ------------------

  12 of the 63 functions Qt declares: 6 takes or gives a type that cannot be
  passed yet; 2 a template; 2 forbidden; 1 declared and nowhere to be found;
  1 a signal.

  What to expect
  --------------

  - The C++ QApplication is created by 'QApplication(...)' at once, since
    nearly every other object of Qt can only be made after it.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QApplication.
  - Qt tells when it has removed the C++ QApplication. Every call on the cute
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
    Calls Qt's 'QString QApplication::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qapplication.html#tr

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
    #  QString QApplication::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN12QApplication2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  def style() -> Optional[QStyle]:
    """
    Calls Qt's 'QStyle *QApplication::style()'.

    Qt's own words: https://doc.qt.io/qt-6/qapplication.html#style

    Returns
    -------

    Optional[QStyle]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QStyle *QApplication::style()
    address = Rituals.call('ritual_ZN12QApplication5styleEv')
    from . import QStyle
    return QStyle._cuteAt(address)

  @staticmethod
  @overload(QStyle)
  @overload(NoneType)
  def setStyle(a0: Optional[QStyle]) -> None:
    """
    Calls Qt's 'void QApplication::setStyle(QStyle *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qapplication.html#setStyle

    Parameters
    ----------

    a0 : Optional[QStyle]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QApplication::setStyle(QStyle *a0)
    Rituals.call(
        'ritual_ZN12QApplication8setStyleEP6QStyle',
        CuteMixin._addressOf(a0),
    )

  @staticmethod
  @overload(str)
  def setStyle(a0: str) -> Optional[QStyle]:
    """
    Calls Qt's 'QStyle *QApplication::setStyle(const QString &a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qapplication.html#setStyle

    Parameters
    ----------

    a0 : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    Optional[QStyle]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QStyle *QApplication::setStyle(const QString &a0)
    address = Rituals.call('ritual_ZN12QApplication8setStyleERK7QString', a0)
    from . import QStyle
    return QStyle._cuteAt(address)

  @staticmethod
  @overload(QWidget)
  @overload(NoneType)
  def palette(a0: Optional[QWidget]) -> QPalette:
    """
    Calls Qt's 'QPalette QApplication::palette(const QWidget *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qapplication.html#palette

    Parameters
    ----------

    a0 : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QPalette
      A new cute QPalette around the copy Qt gave back. Python owns it.
    """
    #  QPalette QApplication::palette(const QWidget *a0)
    address = Rituals.call(
        'ritual_ZN12QApplication7paletteEPK7QWidget',
        CuteMixin._addressOf(a0),
    )
    from ..QtGui import QPalette
    return QPalette._cuteOwning(address)

  @staticmethod
  @overload(str)
  def palette(className: Optional[str]) -> QPalette:
    """
    Calls Qt's 'QPalette QApplication::palette(const char *className)'.

    Qt's own words: https://doc.qt.io/qt-6/qapplication.html#palette

    Parameters
    ----------

    className : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    Returns
    -------

    QPalette
      A new cute QPalette around the copy Qt gave back. Python owns it.
    """
    #  QPalette QApplication::palette(const char *className)
    address = Rituals.call(
        'ritual_ZN12QApplication7paletteEPKc', CuteMixin._bytesOf(className),
    )
    from ..QtGui import QPalette
    return QPalette._cuteOwning(address)

  @staticmethod
  @overload(QPalette)
  @overload(QPalette, str)
  @overload(QPalette, NoneType)
  def setPalette(a0: QPalette, className: Optional[str] = None) -> None:
    """
    Calls Qt's 'void QApplication::setPalette(const QPalette &a0, const char
    *className)'.

    Qt's own words: https://doc.qt.io/qt-6/qapplication.html#setPalette

    Parameters
    ----------

    a0 : QPalette
      Passed on as a value: Qt reads the C++ QPalette, which stays Python's
      own.

    className : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text. May
      be left out, as in Qt: it is then None.
    """
    #  void QApplication::setPalette(const QPalette &a0, const char
    #      *className)
    Rituals.call(
        'ritual_ZN12QApplication10setPaletteERK8QPalettePKc',
        CuteMixin._valueOf(a0), CuteMixin._bytesOf(className),
    )

  @staticmethod
  @overload()
  def font() -> QFont:
    """
    Calls Qt's 'QFont QApplication::font()'.

    Qt's own words: https://doc.qt.io/qt-6/qapplication.html#font

    Returns
    -------

    QFont
      A new cute QFont around the copy Qt gave back. Python owns it.
    """
    #  QFont QApplication::font()
    address = Rituals.call('ritual_ZN12QApplication4fontEv')
    from ..QtGui import QFont
    return QFont._cuteOwning(address)

  @staticmethod
  @overload(QWidget)
  @overload(NoneType)
  def font(a0: Optional[QWidget]) -> QFont:
    """
    Calls Qt's 'QFont QApplication::font(const QWidget *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qapplication.html#font

    Parameters
    ----------

    a0 : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QFont
      A new cute QFont around the copy Qt gave back. Python owns it.
    """
    #  QFont QApplication::font(const QWidget *a0)
    address = Rituals.call(
        'ritual_ZN12QApplication4fontEPK7QWidget', CuteMixin._addressOf(a0),
    )
    from ..QtGui import QFont
    return QFont._cuteOwning(address)

  @staticmethod
  @overload(str)
  def font(className: Optional[str]) -> QFont:
    """
    Calls Qt's 'QFont QApplication::font(const char *className)'.

    Qt's own words: https://doc.qt.io/qt-6/qapplication.html#font

    Parameters
    ----------

    className : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    Returns
    -------

    QFont
      A new cute QFont around the copy Qt gave back. Python owns it.
    """
    #  QFont QApplication::font(const char *className)
    address = Rituals.call(
        'ritual_ZN12QApplication4fontEPKc', CuteMixin._bytesOf(className),
    )
    from ..QtGui import QFont
    return QFont._cuteOwning(address)

  @staticmethod
  @overload(QFont)
  @overload(QFont, str)
  @overload(QFont, NoneType)
  def setFont(a0: QFont, className: Optional[str] = None) -> None:
    """
    Calls Qt's 'void QApplication::setFont(const QFont &a0, const char
    *className)'.

    Qt's own words: https://doc.qt.io/qt-6/qapplication.html#setFont

    Parameters
    ----------

    a0 : QFont
      Passed on as a value: Qt reads the C++ QFont, which stays Python's own.

    className : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text. May
      be left out, as in Qt: it is then None.
    """
    #  void QApplication::setFont(const QFont &a0, const char *className)
    Rituals.call(
        'ritual_ZN12QApplication7setFontERK5QFontPKc',
        CuteMixin._valueOf(a0), CuteMixin._bytesOf(className),
    )

  @staticmethod
  def fontMetrics() -> QFontMetrics:
    """
    Calls Qt's 'QFontMetrics QApplication::fontMetrics()'.

    Qt's own words: https://doc.qt.io/qt-6/qapplication.html#fontMetrics

    Returns
    -------

    QFontMetrics
      A new cute QFontMetrics around the copy Qt gave back. Python owns it.
    """
    #  QFontMetrics QApplication::fontMetrics()
    address = Rituals.call('ritual_ZN12QApplication11fontMetricsEv')
    from ..QtGui import QFontMetrics
    return QFontMetrics._cuteOwning(address)

  @staticmethod
  def allWidgets() -> QList[QWidget]:
    """
    Calls Qt's 'QWidgetList QApplication::allWidgets()'.

    Qt's own words: https://doc.qt.io/qt-6/qapplication.html#allWidgets

    Returns
    -------

    QList[QWidget]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QWidgetList QApplication::allWidgets()
    address = Rituals.call('ritual_ZN12QApplication10allWidgetsEv')
    from . import QWidget
    return QList[QWidget]._cuteOwning(address)

  @staticmethod
  def topLevelWidgets() -> QList[QWidget]:
    """
    Calls Qt's 'QWidgetList QApplication::topLevelWidgets()'.

    Qt's own words: https://doc.qt.io/qt-6/qapplication.html#topLevelWidgets

    Returns
    -------

    QList[QWidget]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QWidgetList QApplication::topLevelWidgets()
    address = Rituals.call('ritual_ZN12QApplication15topLevelWidgetsEv')
    from . import QWidget
    return QList[QWidget]._cuteOwning(address)

  @staticmethod
  def activePopupWidget() -> Optional[QWidget]:
    """
    Calls Qt's 'QWidget *QApplication::activePopupWidget()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qapplication.html#activePopupWidget

    Returns
    -------

    Optional[QWidget]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWidget *QApplication::activePopupWidget()
    address = Rituals.call('ritual_ZN12QApplication17activePopupWidgetEv')
    from . import QWidget
    return QWidget._cuteAt(address)

  @staticmethod
  def activeModalWidget() -> Optional[QWidget]:
    """
    Calls Qt's 'QWidget *QApplication::activeModalWidget()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qapplication.html#activeModalWidget

    Returns
    -------

    Optional[QWidget]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWidget *QApplication::activeModalWidget()
    address = Rituals.call('ritual_ZN12QApplication17activeModalWidgetEv')
    from . import QWidget
    return QWidget._cuteAt(address)

  @staticmethod
  def focusWidget() -> Optional[QWidget]:
    """
    Calls Qt's 'QWidget *QApplication::focusWidget()'.

    Qt's own words: https://doc.qt.io/qt-6/qapplication.html#focusWidget

    Returns
    -------

    Optional[QWidget]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWidget *QApplication::focusWidget()
    address = Rituals.call('ritual_ZN12QApplication11focusWidgetEv')
    from . import QWidget
    return QWidget._cuteAt(address)

  @staticmethod
  def activeWindow() -> Optional[QWidget]:
    """
    Calls Qt's 'QWidget *QApplication::activeWindow()'.

    Qt's own words: https://doc.qt.io/qt-6/qapplication.html#activeWindow

    Returns
    -------

    Optional[QWidget]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWidget *QApplication::activeWindow()
    address = Rituals.call('ritual_ZN12QApplication12activeWindowEv')
    from . import QWidget
    return QWidget._cuteAt(address)

  @staticmethod
  @overload(QWidget)
  @overload(NoneType)
  def setActiveWindow(act: Optional[QWidget]) -> None:
    """
    Calls Qt's 'void QApplication::setActiveWindow(QWidget *act)'.

    Qt's own words: https://doc.qt.io/qt-6/qapplication.html#setActiveWindow

    Parameters
    ----------

    act : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QApplication::setActiveWindow(QWidget *act)
    Rituals.call(
        'ritual_ZN12QApplication15setActiveWindowEP7QWidget',
        CuteMixin._addressOf(act),
    )

  @staticmethod
  @overload(QPoint)
  def widgetAt(p: QPoint) -> Optional[QWidget]:
    """
    Calls Qt's 'QWidget *QApplication::widgetAt(const QPoint &p)'.

    Qt's own words: https://doc.qt.io/qt-6/qapplication.html#widgetAt

    Parameters
    ----------

    p : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.

    Returns
    -------

    Optional[QWidget]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWidget *QApplication::widgetAt(const QPoint &p)
    address = Rituals.call(
        'ritual_ZN12QApplication8widgetAtERK6QPoint', CuteMixin._valueOf(p),
    )
    from . import QWidget
    return QWidget._cuteAt(address)

  @staticmethod
  @overload(int, int)
  def widgetAt(x: int, y: int) -> Optional[QWidget]:
    """
    Calls Qt's 'QWidget *QApplication::widgetAt(int x, int y)'.

    Qt's own words: https://doc.qt.io/qt-6/qapplication.html#widgetAt

    Parameters
    ----------

    x : int
      Passed on as it is.

    y : int
      Passed on as it is.

    Returns
    -------

    Optional[QWidget]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWidget *QApplication::widgetAt(int x, int y)
    address = Rituals.call('ritual_ZN12QApplication8widgetAtEii', x, y)
    from . import QWidget
    return QWidget._cuteAt(address)

  @staticmethod
  @overload(QPoint)
  def topLevelAt(p: QPoint) -> Optional[QWidget]:
    """
    Calls Qt's 'QWidget *QApplication::topLevelAt(const QPoint &p)'.

    Qt's own words: https://doc.qt.io/qt-6/qapplication.html#topLevelAt

    Parameters
    ----------

    p : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.

    Returns
    -------

    Optional[QWidget]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWidget *QApplication::topLevelAt(const QPoint &p)
    address = Rituals.call(
        'ritual_ZN12QApplication10topLevelAtERK6QPoint',
        CuteMixin._valueOf(p),
    )
    from . import QWidget
    return QWidget._cuteAt(address)

  @staticmethod
  @overload(int, int)
  def topLevelAt(x: int, y: int) -> Optional[QWidget]:
    """
    Calls Qt's 'QWidget *QApplication::topLevelAt(int x, int y)'.

    Qt's own words: https://doc.qt.io/qt-6/qapplication.html#topLevelAt

    Parameters
    ----------

    x : int
      Passed on as it is.

    y : int
      Passed on as it is.

    Returns
    -------

    Optional[QWidget]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWidget *QApplication::topLevelAt(int x, int y)
    address = Rituals.call('ritual_ZN12QApplication10topLevelAtEii', x, y)
    from . import QWidget
    return QWidget._cuteAt(address)

  @staticmethod
  def beep() -> None:
    """
    Calls Qt's 'void QApplication::beep()'.

    Qt's own words: https://doc.qt.io/qt-6/qapplication.html#beep
    """
    #  void QApplication::beep()
    Rituals.call('ritual_ZN12QApplication4beepEv')

  @staticmethod
  @overload(QWidget)
  @overload(NoneType)
  @overload(QWidget, int)
  @overload(NoneType, int)
  def alert(widget: Optional[QWidget], duration: int = 0) -> None:
    """
    Calls Qt's 'void QApplication::alert(QWidget *widget, int duration)'.

    Qt's own words: https://doc.qt.io/qt-6/qapplication.html#alert

    Parameters
    ----------

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    duration : int
      Passed on as it is. May be left out, as in Qt: it is then 0.
    """
    #  void QApplication::alert(QWidget *widget, int duration)
    Rituals.call(
        'ritual_ZN12QApplication5alertEP7QWidgeti',
        CuteMixin._addressOf(widget), duration,
    )

  @staticmethod
  @overload(int)
  def setCursorFlashTime(a0: int) -> None:
    """
    Calls Qt's 'void QApplication::setCursorFlashTime(int a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qapplication.html#setCursorFlashTime

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  void QApplication::setCursorFlashTime(int a0)
    Rituals.call('ritual_ZN12QApplication18setCursorFlashTimeEi', a0)

  @staticmethod
  def cursorFlashTime() -> int:
    """
    Calls Qt's 'int QApplication::cursorFlashTime()'.

    Qt's own words: https://doc.qt.io/qt-6/qapplication.html#cursorFlashTime
    """
    #  int QApplication::cursorFlashTime()
    return Rituals.call('ritual_ZN12QApplication15cursorFlashTimeEv')

  @staticmethod
  @overload(int)
  def setDoubleClickInterval(a0: int) -> None:
    """
    Calls Qt's 'void QApplication::setDoubleClickInterval(int a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qapplication.html#setDoubleClickInterval

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  void QApplication::setDoubleClickInterval(int a0)
    Rituals.call('ritual_ZN12QApplication22setDoubleClickIntervalEi', a0)

  @staticmethod
  def doubleClickInterval() -> int:
    """
    Calls Qt's 'int QApplication::doubleClickInterval()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qapplication.html#doubleClickInterval
    """
    #  int QApplication::doubleClickInterval()
    return Rituals.call('ritual_ZN12QApplication19doubleClickIntervalEv')

  @staticmethod
  @overload(int)
  def setKeyboardInputInterval(a0: int) -> None:
    """
    Calls Qt's 'void QApplication::setKeyboardInputInterval(int a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qapplication.html#setKeyboardInputInterval

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  void QApplication::setKeyboardInputInterval(int a0)
    Rituals.call('ritual_ZN12QApplication24setKeyboardInputIntervalEi', a0)

  @staticmethod
  def keyboardInputInterval() -> int:
    """
    Calls Qt's 'int QApplication::keyboardInputInterval()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qapplication.html#keyboardInputInterval
    """
    #  int QApplication::keyboardInputInterval()
    return Rituals.call('ritual_ZN12QApplication21keyboardInputIntervalEv')

  @staticmethod
  @overload(int)
  def setWheelScrollLines(a0: int) -> None:
    """
    Calls Qt's 'void QApplication::setWheelScrollLines(int a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qapplication.html#setWheelScrollLines

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  void QApplication::setWheelScrollLines(int a0)
    Rituals.call('ritual_ZN12QApplication19setWheelScrollLinesEi', a0)

  @staticmethod
  def wheelScrollLines() -> int:
    """
    Calls Qt's 'int QApplication::wheelScrollLines()'.

    Qt's own words: https://doc.qt.io/qt-6/qapplication.html#wheelScrollLines
    """
    #  int QApplication::wheelScrollLines()
    return Rituals.call('ritual_ZN12QApplication16wheelScrollLinesEv')

  @staticmethod
  @overload(int)
  def setStartDragTime(ms: int) -> None:
    """
    Calls Qt's 'void QApplication::setStartDragTime(int ms)'.

    Qt's own words: https://doc.qt.io/qt-6/qapplication.html#setStartDragTime

    Parameters
    ----------

    ms : int
      Passed on as it is.
    """
    #  void QApplication::setStartDragTime(int ms)
    Rituals.call('ritual_ZN12QApplication16setStartDragTimeEi', ms)

  @staticmethod
  def startDragTime() -> int:
    """
    Calls Qt's 'int QApplication::startDragTime()'.

    Qt's own words: https://doc.qt.io/qt-6/qapplication.html#startDragTime
    """
    #  int QApplication::startDragTime()
    return Rituals.call('ritual_ZN12QApplication13startDragTimeEv')

  @staticmethod
  @overload(int)
  def setStartDragDistance(l: int) -> None:
    """
    Calls Qt's 'void QApplication::setStartDragDistance(int l)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qapplication.html#setStartDragDistance

    Parameters
    ----------

    l : int
      Passed on as it is.
    """
    #  void QApplication::setStartDragDistance(int l)
    Rituals.call('ritual_ZN12QApplication20setStartDragDistanceEi', l)

  @staticmethod
  def startDragDistance() -> int:
    """
    Calls Qt's 'int QApplication::startDragDistance()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qapplication.html#startDragDistance
    """
    #  int QApplication::startDragDistance()
    return Rituals.call('ritual_ZN12QApplication17startDragDistanceEv')

  @staticmethod
  @overload(Qt.UIEffect)
  def isEffectEnabled(a0: Qt.UIEffect) -> bool:
    """
    Calls Qt's 'bool QApplication::isEffectEnabled(Qt::UIEffect a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qapplication.html#isEffectEnabled

    Parameters
    ----------

    a0 : Qt.UIEffect
      Passed on as its number.
    """
    #  bool QApplication::isEffectEnabled(Qt::UIEffect a0)
    return Rituals.call(
        'ritual_ZN12QApplication15isEffectEnabledEN2Qt8UIEffectE', a0.value,
    )

  @staticmethod
  @overload(Qt.UIEffect)
  @overload(Qt.UIEffect, bool)
  def setEffectEnabled(a0: Qt.UIEffect, enable: bool = True) -> None:
    """
    Calls Qt's 'void QApplication::setEffectEnabled(Qt::UIEffect a0, bool
    enable)'.

    Qt's own words: https://doc.qt.io/qt-6/qapplication.html#setEffectEnabled

    Parameters
    ----------

    a0 : Qt.UIEffect
      Passed on as its number.

    enable : bool
      Passed on as it is. May be left out, as in Qt: it is then True.
    """
    #  void QApplication::setEffectEnabled(Qt::UIEffect a0, bool enable)
    Rituals.call(
        'ritual_ZN12QApplication16setEffectEnabledEN2Qt8UIEffectEb',
        a0.value, enable,
    )

  @staticmethod
  def exec() -> int:
    """
    Calls Qt's 'int QApplication::exec()'.

    Qt's own words: https://doc.qt.io/qt-6/qapplication.html#exec
    """
    #  int QApplication::exec()
    return Rituals.call('ritual_ZN12QApplication4execEv')

  @staticmethod
  def closeAllWindows() -> None:
    """
    Calls Qt's 'void QApplication::closeAllWindows()'.

    Qt's own words: https://doc.qt.io/qt-6/qapplication.html#closeAllWindows
    """
    #  void QApplication::closeAllWindows()
    Rituals.call('ritual_ZN12QApplication15closeAllWindowsEv')

  @staticmethod
  def aboutQt() -> None:
    """
    Calls Qt's 'void QApplication::aboutQt()'.

    Qt's own words: https://doc.qt.io/qt-6/qapplication.html#aboutQt
    """
    #  void QApplication::aboutQt()
    Rituals.call('ritual_ZN12QApplication7aboutQtEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QApplication'

  #  A C++ QApplication Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QApplication'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QApplication::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qapplication.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QApplication::metaObject() const
    address = self.uglySide.call('ritual_ZNK12QApplication10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def styleSheet(self) -> str:
    """
    Calls Qt's 'QString QApplication::styleSheet() const'.

    Qt's own words: https://doc.qt.io/qt-6/qapplication.html#styleSheet

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QApplication::styleSheet() const
    return self.uglySide.call('ritual_ZNK12QApplication10styleSheetEv')

  def autoSipEnabled(self) -> bool:
    """
    Calls Qt's 'bool QApplication::autoSipEnabled() const'.

    Qt's own words: https://doc.qt.io/qt-6/qapplication.html#autoSipEnabled
    """
    #  bool QApplication::autoSipEnabled() const
    return self.uglySide.call('ritual_ZNK12QApplication14autoSipEnabledEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setStyleSheet(self, sheet: str) -> None:
    """
    Calls Qt's 'void QApplication::setStyleSheet(const QString &sheet)'.

    Qt's own words: https://doc.qt.io/qt-6/qapplication.html#setStyleSheet

    Parameters
    ----------

    sheet : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QApplication::setStyleSheet(const QString &sheet)
    self.uglySide.call(
        'ritual_ZN12QApplication13setStyleSheetERK7QString', sheet,
    )

  @overload(bool)
  def setAutoSipEnabled(self, enabled: bool) -> None:
    """
    Calls Qt's 'void QApplication::setAutoSipEnabled(const bool enabled)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qapplication.html#setAutoSipEnabled

    Parameters
    ----------

    enabled : bool
      Passed on as it is.
    """
    #  void QApplication::setAutoSipEnabled(const bool enabled)
    self.uglySide.call(
        'ritual_ZN12QApplication17setAutoSipEnabledEb', enabled,
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

  @overload(list)
  @overload(list, int)
  def __init__(self, argv: list, a2: int = 396288) -> None:
    """
    Calls Qt's 'QApplication::QApplication(int &argc, char **argv, int a2)'
    at once: nearly every other object of Qt can only be made after the
    application.

    Qt's own words: https://doc.qt.io/qt-6/qapplication.html#QApplication

    Parameters
    ----------

    argv : list
      The texts the program was started with, as 'sys.argv'. Passed on as Qt
      takes them: how many they are, and where the first one is.

    a2 : int
      Passed on as it is. May be left out, as in Qt: it is then 396288.
    """
    #  QApplication::QApplication(int &argc, char **argv, int a2)
    self._noteCreation(QApplication, lambda: Rituals.call(
        'ritual_ZN12QApplicationC1ERiPPci', *self._startTextsOf(argv), a2,
    ))
    self._getUglySide()

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

  @overload(QObject, QEvent)
  @overload(QObject, NoneType)
  @overload(NoneType, QEvent)
  @overload(NoneType, NoneType)
  def notify(self, a0: Optional[QObject], a1: Optional[QEvent]) -> bool:
    """
    Calls Qt's 'bool QApplication::notify(QObject *a0, QEvent *a1)'.

    Qt's own words: https://doc.qt.io/qt-6/qapplication.html#notify

    Parameters
    ----------

    a0 : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    a1 : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QApplication::notify(QObject *a0, QEvent *a1)
    ritual = 'ritual_ZN12QApplication6notifyEP7QObjectP6QEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN12QApplication6notifyEP7QObjectP6QEvent'
    return self.uglySide.call(
        ritual, self._addressOf(a0, 'QObject'), self._addressOf(a1),
    )

  @overload(QEvent)
  @overload(NoneType)
  def event(self, a0: Optional[QEvent]) -> bool:
    """
    Calls Qt's 'bool QApplication::event(QEvent *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qapplication.html#event

    Parameters
    ----------

    a0 : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QApplication::event(QEvent *a0)
    ritual = 'ritual_ZN12QApplication5eventEP6QEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN12QApplication5eventEP6QEvent'
    return self.uglySide.call(ritual, self._addressOf(a0))
