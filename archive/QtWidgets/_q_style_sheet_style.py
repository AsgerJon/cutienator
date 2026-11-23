"""
QStyleSheetStyle binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/6.12.0/QtWidgets/private/qstylesheetstyle_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QStyleSheetStyle to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import Qt, QObject
from ..QtGui import QIcon, QPalette
from . import QSizePolicy, QWindowsStyle

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QEvent, QMetaObject, QRect
  from ..QtGui import QFont, QFontMetrics, QPainter, QPixmap
  from . import QApplication, QStyleOption, QWidget
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QApplication = WAIT['QApplication']
  QEvent = WAIT['QEvent']
  QFont = WAIT['QFont']
  QFontMetrics = WAIT['QFontMetrics']
  QPainter = WAIT['QPainter']
  QPixmap = WAIT['QPixmap']
  QRect = WAIT['QRect']
  QStyleOption = WAIT['QStyleOption']
  QWidget = WAIT['QWidget']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QStyleSheetStyle(QWindowsStyle):
  """
  The cute side of Qt's QStyleSheetStyle: a plain Python object standing in
  front of one C++ QStyleSheetStyle.

  It is built on the cute 'QWindowsStyle', as Qt's QStyleSheetStyle is built
  on Qt's QWindowsStyle, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QStyleSheetStyle that has a ritual and that Python
  can call so far, 16 names in all: 'metaObject', 'drawItemPixmap',
  'drawItemText', 'generatedIconPixmap', 'itemPixmapRect', 'itemTextRect',
  'polish', 'standardPalette', 'layoutSpacing', 'ref', 'deref',
  'saveWidgetFont', 'clearWidgetFont', 'event', 'resolveAlignment',
  'loadPixmap'. None can be made from Python: one comes out of a function of
  another class that gives one back.

  What has no ritual
  ------------------

  74 of the 90 functions Qt declares: 29 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file; 26 leans on
  'QStyleSheetStyle; 13 takes or gives a type that cannot be passed yet; 4
  forbidden; 1 a template; 1 declared and nowhere to be found.

  What to expect
  --------------

  - The C++ QStyleSheetStyle is created at the first use, not by
    'QStyleSheetStyle(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QStyleSheetStyle.
  - Qt tells when it has removed the C++ QStyleSheetStyle. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(Qt.LayoutDirection, Qt.Alignment)
  def resolveAlignment(
      a0: Qt.LayoutDirection,
      a1: Qt.Alignment,
  ) -> Qt.Alignment:
    """
    Calls Qt's 'Qt::Alignment
    QStyleSheetStyle::resolveAlignment(Qt::LayoutDirection a0, Qt::Alignment
    a1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qstylesheetstyle.html#resolveAlignment

    Parameters
    ----------

    a0 : Qt.LayoutDirection
      Passed on as its number.

    a1 : Qt.Alignment
      Passed on as its number.

    Returns
    -------

    Qt.Alignment
      The value standing for the combination Qt gave back.
    """
    #  Qt::Alignment QStyleSheetStyle::resolveAlignment(Qt::LayoutDirection
    #      a0, Qt::Alignment a1)
    return Qt.Alignment(Rituals.call(
        'ritual_ZN16QStyleSheetStyle16resolveAlignmentEN2Qt15LayoutDirectio'
        'nE6QFlagsINS0_13AlignmentFlagEE',
        a0.value, a1.value,
    ))

  @staticmethod
  @overload(str, QObject)
  @overload(str, NoneType)
  def loadPixmap(fileName: str, context: Optional[QObject]) -> QPixmap:
    """
    Calls Qt's 'QPixmap QStyleSheetStyle::loadPixmap(const QString &fileName,
    const QObject *context)'.

    Qt's own words: https://doc.qt.io/qt-6/qstylesheetstyle.html#loadPixmap

    Parameters
    ----------

    fileName : str
      Passed on as it is: a QString is made of it for the call.

    context : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QPixmap
      A new cute QPixmap around the copy Qt gave back. Python owns it.
    """
    #  QPixmap QStyleSheetStyle::loadPixmap(const QString &fileName, const
    #      QObject *context)
    address = Rituals.call(
        'ritual_ZN16QStyleSheetStyle10loadPixmapERK7QStringPK7QObject',
        fileName, CuteMixin._addressOf(context, 'QObject'),
    )
    from ..QtGui import QPixmap
    return QPixmap._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QStyleSheetStyle'

  #  A C++ QStyleSheetStyle Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QStyleSheetStyle'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QStyleSheetStyle::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qstylesheetstyle.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QStyleSheetStyle::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK16QStyleSheetStyle10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  @overload(QIcon.Mode, QPixmap, QStyleOption)
  @overload(QIcon.Mode, QPixmap, NoneType)
  def generatedIconPixmap(
      self,
      iconMode: QIcon.Mode,
      pixmap: QPixmap,
      option: Optional[QStyleOption],
  ) -> QPixmap:
    """
    Calls Qt's 'QPixmap QStyleSheetStyle::generatedIconPixmap(QIcon::Mode
    iconMode, const QPixmap &pixmap, const QStyleOption *option) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qstylesheetstyle.html#generatedIconPixmap

    Parameters
    ----------

    iconMode : QIcon.Mode
      Passed on as its number.

    pixmap : QPixmap
      Passed on as a value: Qt reads the C++ QPixmap, which stays Python's
      own.

    option : Optional[QStyleOption]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QPixmap
      A new cute QPixmap around the copy Qt gave back. Python owns it.
    """
    #  QPixmap QStyleSheetStyle::generatedIconPixmap(QIcon::Mode iconMode,
    #      const QPixmap &pixmap, const QStyleOption *option) const
    address = self.uglySide.call(
        'ritual_ZNK16QStyleSheetStyle19generatedIconPixmapEN5QIcon4ModeERK7'
        'QPixmapPK12QStyleOption',
        iconMode.value, self._valueOf(pixmap), self._addressOf(option),
    )
    from ..QtGui import QPixmap
    return QPixmap._cuteOwning(address)

  @overload(QRect, int, QPixmap)
  def itemPixmapRect(
      self,
      rect: QRect,
      alignment: int,
      pixmap: QPixmap,
  ) -> QRect:
    """
    Calls Qt's 'QRect QStyleSheetStyle::itemPixmapRect(const QRect &rect, int
    alignment, const QPixmap &pixmap) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qstylesheetstyle.html#itemPixmapRect

    Parameters
    ----------

    rect : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.

    alignment : int
      Passed on as it is.

    pixmap : QPixmap
      Passed on as a value: Qt reads the C++ QPixmap, which stays Python's
      own.

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect QStyleSheetStyle::itemPixmapRect(const QRect &rect, int
    #      alignment, const QPixmap &pixmap) const
    address = self.uglySide.call(
        'ritual_ZNK16QStyleSheetStyle14itemPixmapRectERK5QRectiRK7QPixmap',
        self._valueOf(rect), alignment, self._valueOf(pixmap),
    )
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

  @overload(QFontMetrics, QRect, int, bool, str)
  def itemTextRect(
      self,
      metrics: QFontMetrics,
      rect: QRect,
      alignment: int,
      enabled: bool,
      text: str,
  ) -> QRect:
    """
    Calls Qt's 'QRect QStyleSheetStyle::itemTextRect(const QFontMetrics
    &metrics, const QRect &rect, int alignment, bool enabled, const QString
    &text) const'.

    Qt's own words: https://doc.qt.io/qt-6/qstylesheetstyle.html#itemTextRect

    Parameters
    ----------

    metrics : QFontMetrics
      Passed on as a value: Qt reads the C++ QFontMetrics, which stays
      Python's own.

    rect : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.

    alignment : int
      Passed on as it is.

    enabled : bool
      Passed on as it is.

    text : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect QStyleSheetStyle::itemTextRect(const QFontMetrics &metrics,
    #      const QRect &rect, int alignment, bool enabled, const QString
    #      &text) const
    address = self.uglySide.call(
        'ritual_ZNK16QStyleSheetStyle12itemTextRectERK12QFontMetricsRK5QRec'
        'tibRK7QString',
        self._valueOf(metrics), self._valueOf(rect), alignment, enabled,
        text,
    )
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

  def standardPalette(self) -> QPalette:
    """
    Calls Qt's 'QPalette QStyleSheetStyle::standardPalette() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qstylesheetstyle.html#standardPalette

    Returns
    -------

    QPalette
      A new cute QPalette around the copy Qt gave back. Python owns it.
    """
    #  QPalette QStyleSheetStyle::standardPalette() const
    address = self.uglySide.call(
        'ritual_ZNK16QStyleSheetStyle15standardPaletteEv',
    )
    return QPalette._cuteOwning(address)

  @overload(QSizePolicy.ControlType, QSizePolicy.ControlType, Qt.Orientation)
  @overload(
      QSizePolicy.ControlType, QSizePolicy.ControlType, Qt.Orientation,
      QStyleOption,
  )
  @overload(
      QSizePolicy.ControlType, QSizePolicy.ControlType, Qt.Orientation,
      NoneType,
  )
  @overload(
      QSizePolicy.ControlType, QSizePolicy.ControlType, Qt.Orientation,
      QStyleOption, QWidget,
  )
  @overload(
      QSizePolicy.ControlType, QSizePolicy.ControlType, Qt.Orientation,
      QStyleOption, NoneType,
  )
  @overload(
      QSizePolicy.ControlType, QSizePolicy.ControlType, Qt.Orientation,
      NoneType, QWidget,
  )
  @overload(
      QSizePolicy.ControlType, QSizePolicy.ControlType, Qt.Orientation,
      NoneType, NoneType,
  )
  def layoutSpacing(
      self,
      control1: QSizePolicy.ControlType,
      control2: QSizePolicy.ControlType,
      orientation: Qt.Orientation,
      option: Optional[QStyleOption] = None,
      widget: Optional[QWidget] = None,
  ) -> int:
    """
    Calls Qt's 'int QStyleSheetStyle::layoutSpacing(QSizePolicy::ControlType
    control1, QSizePolicy::ControlType control2, Qt::Orientation orientation,
    const QStyleOption *option, const QWidget *widget) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qstylesheetstyle.html#layoutSpacing

    Parameters
    ----------

    control1 : QSizePolicy.ControlType
      Passed on as its number.

    control2 : QSizePolicy.ControlType
      Passed on as its number.

    orientation : Qt.Orientation
      Passed on as its number.

    option : Optional[QStyleOption]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  int QStyleSheetStyle::layoutSpacing(QSizePolicy::ControlType control1,
    #      QSizePolicy::ControlType control2, Qt::Orientation orientation,
    #      const QStyleOption *option, const QWidget *widget) const
    return self.uglySide.call(
        'ritual_ZNK16QStyleSheetStyle13layoutSpacingEN11QSizePolicy11Contro'
        'lTypeES1_N2Qt11OrientationEPK12QStyleOptionPK7QWidget',
        control1.value, control2.value, orientation.value,
        self._addressOf(option), self._addressOf(widget),
    )

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

  @overload(QPainter, QRect, int, QPixmap)
  @overload(NoneType, QRect, int, QPixmap)
  def drawItemPixmap(
      self,
      painter: Optional[QPainter],
      rect: QRect,
      alignment: int,
      pixmap: QPixmap,
  ) -> None:
    """
    Calls Qt's 'void QStyleSheetStyle::drawItemPixmap(QPainter *painter,
    const QRect &rect, int alignment, const QPixmap &pixmap) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qstylesheetstyle.html#drawItemPixmap

    Parameters
    ----------

    painter : Optional[QPainter]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    rect : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.

    alignment : int
      Passed on as it is.

    pixmap : QPixmap
      Passed on as a value: Qt reads the C++ QPixmap, which stays Python's
      own.
    """
    #  void QStyleSheetStyle::drawItemPixmap(QPainter *painter, const QRect
    #      &rect, int alignment, const QPixmap &pixmap) const
    self.uglySide.call(
        'ritual_ZNK16QStyleSheetStyle14drawItemPixmapEP8QPainterRK5QRectiRK'
        '7QPixmap',
        self._addressOf(painter), self._valueOf(rect), alignment,
        self._valueOf(pixmap),
    )

  @overload(QPainter, QRect, int, QPalette, bool, str)
  @overload(NoneType, QRect, int, QPalette, bool, str)
  @overload(QPainter, QRect, int, QPalette, bool, str, QPalette.ColorRole)
  @overload(NoneType, QRect, int, QPalette, bool, str, QPalette.ColorRole)
  def drawItemText(
      self,
      painter: Optional[QPainter],
      rect: QRect,
      alignment: int,
      pal: QPalette,
      enabled: bool,
      text: str,
      textRole: QPalette.ColorRole = QPalette.ColorRole.NoRole,
  ) -> None:
    """
    Calls Qt's 'void QStyleSheetStyle::drawItemText(QPainter *painter, const
    QRect &rect, int alignment, const QPalette &pal, bool enabled, const
    QString &text, QPalette::ColorRole textRole) const'.

    Qt's own words: https://doc.qt.io/qt-6/qstylesheetstyle.html#drawItemText

    Parameters
    ----------

    painter : Optional[QPainter]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    rect : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.

    alignment : int
      Passed on as it is.

    pal : QPalette
      Passed on as a value: Qt reads the C++ QPalette, which stays Python's
      own.

    enabled : bool
      Passed on as it is.

    text : str
      Passed on as it is: a QString is made of it for the call.

    textRole : QPalette.ColorRole
      Passed on as its number. May be left out, as in Qt: it is then
      QPalette.ColorRole.NoRole.
    """
    #  void QStyleSheetStyle::drawItemText(QPainter *painter, const QRect
    #      &rect, int alignment, const QPalette &pal, bool enabled, const
    #      QString &text, QPalette::ColorRole textRole) const
    self.uglySide.call(
        'ritual_ZNK16QStyleSheetStyle12drawItemTextEP8QPainterRK5QRectiRK8Q'
        'PalettebRK7QStringNS5_9ColorRoleE',
        self._addressOf(painter), self._valueOf(rect), alignment,
        self._valueOf(pal), enabled, text, textRole.value,
    )

  @overload(QApplication)
  @overload(NoneType)
  def polish(self, app: Optional[QApplication]) -> None:
    """
    Calls Qt's 'void QStyleSheetStyle::polish(QApplication *app)'.

    Qt's own words: https://doc.qt.io/qt-6/qstylesheetstyle.html#polish

    Parameters
    ----------

    app : Optional[QApplication]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QStyleSheetStyle::polish(QApplication *app)
    self.uglySide.call(
        'ritual_ZN16QStyleSheetStyle6polishEP12QApplication',
        self._addressOf(app),
    )

  def ref(self) -> None:
    """
    Calls Qt's 'void QStyleSheetStyle::ref()'.

    Qt's own words: https://doc.qt.io/qt-6/qstylesheetstyle.html#ref
    """
    #  void QStyleSheetStyle::ref()
    self.uglySide.call('ritual_ZN16QStyleSheetStyle3refEv')

  def deref(self) -> None:
    """
    Calls Qt's 'void QStyleSheetStyle::deref()'.

    Qt's own words: https://doc.qt.io/qt-6/qstylesheetstyle.html#deref
    """
    #  void QStyleSheetStyle::deref()
    self.uglySide.call('ritual_ZN16QStyleSheetStyle5derefEv')

  @overload(QWidget, QFont)
  @overload(NoneType, QFont)
  def saveWidgetFont(self, w: Optional[QWidget], font: QFont) -> None:
    """
    Calls Qt's 'void QStyleSheetStyle::saveWidgetFont(QWidget *w, const QFont
    &font) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qstylesheetstyle.html#saveWidgetFont

    Parameters
    ----------

    w : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    font : QFont
      Passed on as a value: Qt reads the C++ QFont, which stays Python's own.
    """
    #  void QStyleSheetStyle::saveWidgetFont(QWidget *w, const QFont &font)
    #      const
    self.uglySide.call(
        'ritual_ZNK16QStyleSheetStyle14saveWidgetFontEP7QWidgetRK5QFont',
        self._addressOf(w), self._valueOf(font),
    )

  @overload(QWidget)
  @overload(NoneType)
  def clearWidgetFont(self, w: Optional[QWidget]) -> None:
    """
    Calls Qt's 'void QStyleSheetStyle::clearWidgetFont(QWidget *w) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qstylesheetstyle.html#clearWidgetFont

    Parameters
    ----------

    w : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QStyleSheetStyle::clearWidgetFont(QWidget *w) const
    self.uglySide.call(
        'ritual_ZNK16QStyleSheetStyle15clearWidgetFontEP7QWidget',
        self._addressOf(w),
    )

  @overload(QEvent)
  @overload(NoneType)
  def event(self, e: Optional[QEvent]) -> bool:
    """
    Calls Qt's 'bool QStyleSheetStyle::event(QEvent *e)'.

    Qt's own words: https://doc.qt.io/qt-6/qstylesheetstyle.html#event

    Parameters
    ----------

    e : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QStyleSheetStyle::event(QEvent *e)
    return self.uglySide.call(
        'ritual_ZN16QStyleSheetStyle5eventEP6QEvent', self._addressOf(e),
    )
