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
from . import QSizePolicy, QStyle, QWindowsStyle

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QEvent, QMetaObject, QPoint, QRect, QSize
  from ..QtGui import QFont, QFontMetrics, QPainter, QPixmap
  from . import QApplication, QStyleHintReturn, QStyleOption
  from . import QStyleOptionComplex, QWidget
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
  QPoint = WAIT['QPoint']
  QRect = WAIT['QRect']
  QSize = WAIT['QSize']
  QStyleHintReturn = WAIT['QStyleHintReturn']
  QStyleOption = WAIT['QStyleOption']
  QStyleOptionComplex = WAIT['QStyleOptionComplex']
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
  can call so far, 29 names in all: 'metaObject', 'drawComplexControl',
  'drawControl', 'drawItemPixmap', 'drawItemText', 'drawPrimitive',
  'generatedIconPixmap', 'hitTestComplexControl', 'itemPixmapRect',
  'itemTextRect', 'pixelMetric', 'polish', 'sizeFromContents',
  'standardPalette', 'standardIcon', 'standardPixmap', 'layoutSpacing',
  'styleHint', 'subElementRect', 'subControlRect', 'unpolish', 'ref',
  'deref', 'saveWidgetFont', 'clearWidgetFont', 'event', 'resolveAlignment',
  'isNaturalChild', 'loadPixmap'. None can be made from Python: one comes out
  of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QStyleSheetStyle::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QStyleSheetStyle::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'void QStyleSheetStyle::polish(QPalette &pal)': takes a type Python
    has no way to hand over yet.
  - Qt's 'QStyleSheetStylePrivate *QStyleSheetStyle::d_func()': gives
    'QStyleSheetStylePrivate', which has no cute class yet.
  - Qt's 'const QStyleSheetStylePrivate *QStyleSheetStyle::d_func() const':
    gives 'QStyleSheetStylePrivate', which has no cute class yet.

  What has no ritual
  ------------------

  31 of the 67 functions Qt declares: 19 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file; 4 forbidden;
  4 leans on 'QStyleSheetStyle; 2 not a gap; 2 the compiler refuses its
  ritual as it would be written here.

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
  - Each name of Qt's QStyleSheetStyle that has no cute function yet,
    '__init__', 'baseStyle', 'defaultSize', 'getDefaultStyleSheet',
    'hasStyleRule', 'initWidget', 'nativeFrameWidth', 'positionRect',
    'renderMenuItemIcon', 'renderRule', 'repolish', 'setGeometry',
    'setPalette', 'setProperties', 'styleRules', 'styleSheetPalette',
    'titleBarLayout', 'unsetPalette', 'unsetStyleSheetFont',
    'updateStyleSheetFont', holds a function that raises
    'NotImplementedError', and its docstring says why.
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
  @overload(QObject)
  @overload(NoneType)
  def isNaturalChild(obj: Optional[QObject]) -> bool:
    """
    Calls Qt's 'bool QStyleSheetStyle::isNaturalChild(const QObject *obj)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qstylesheetstyle.html#isNaturalChild

    Parameters
    ----------

    obj : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QStyleSheetStyle::isNaturalChild(const QObject *obj)
    return Rituals.call(
        'ritual_ZN16QStyleSheetStyle14isNaturalChildEPK7QObject',
        CuteMixin._addressOf(obj, 'QObject'),
    )

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

  @overload(QStyle.ComplexControl, QStyleOptionComplex, QPoint)
  @overload(QStyle.ComplexControl, NoneType, QPoint)
  @overload(QStyle.ComplexControl, QStyleOptionComplex, QPoint, QWidget)
  @overload(QStyle.ComplexControl, QStyleOptionComplex, QPoint, NoneType)
  @overload(QStyle.ComplexControl, NoneType, QPoint, QWidget)
  @overload(QStyle.ComplexControl, NoneType, QPoint, NoneType)
  def hitTestComplexControl(
      self,
      cc: QStyle.ComplexControl,
      opt: Optional[QStyleOptionComplex],
      pt: QPoint,
      w: Optional[QWidget] = None,
  ) -> QStyle.SubControl:
    """
    Calls Qt's 'SubControl
    QStyleSheetStyle::hitTestComplexControl(ComplexControl cc, const
    QStyleOptionComplex *opt, const QPoint &pt, const QWidget *w) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qstylesheetstyle.html#hitTestComplexControl

    Parameters
    ----------

    cc : QStyle.ComplexControl
      Passed on as its number.

    opt : Optional[QStyleOptionComplex]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    pt : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.

    w : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    Returns
    -------

    QStyle.SubControl
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QStyle.SubControl(number)' gives.
    """
    #  SubControl QStyleSheetStyle::hitTestComplexControl(ComplexControl cc,
    #      const QStyleOptionComplex *opt, const QPoint &pt, const QWidget
    #      *w) const
    return QStyle.SubControl(self.uglySide.call(
        'ritual_ZNK16QStyleSheetStyle21hitTestComplexControlEN6QStyle14Comp'
        'lexControlEPK19QStyleOptionComplexRK6QPointPK7QWidget',
        cc.value, self._addressOf(opt), self._valueOf(pt),
        self._addressOf(w),
    ))

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

  @overload(QStyle.PixelMetric)
  @overload(QStyle.PixelMetric, QStyleOption)
  @overload(QStyle.PixelMetric, NoneType)
  @overload(QStyle.PixelMetric, QStyleOption, QWidget)
  @overload(QStyle.PixelMetric, QStyleOption, NoneType)
  @overload(QStyle.PixelMetric, NoneType, QWidget)
  @overload(QStyle.PixelMetric, NoneType, NoneType)
  def pixelMetric(
      self,
      metric: QStyle.PixelMetric,
      option: Optional[QStyleOption] = None,
      widget: Optional[QWidget] = None,
  ) -> int:
    """
    Calls Qt's 'int QStyleSheetStyle::pixelMetric(PixelMetric metric, const
    QStyleOption *option, const QWidget *widget) const'.

    Qt's own words: https://doc.qt.io/qt-6/qstylesheetstyle.html#pixelMetric

    Parameters
    ----------

    metric : QStyle.PixelMetric
      Passed on as its number.

    option : Optional[QStyleOption]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  int QStyleSheetStyle::pixelMetric(PixelMetric metric, const
    #      QStyleOption *option, const QWidget *widget) const
    return self.uglySide.call(
        'ritual_ZNK16QStyleSheetStyle11pixelMetricEN6QStyle11PixelMetricEPK'
        '12QStyleOptionPK7QWidget',
        metric.value, self._addressOf(option), self._addressOf(widget),
    )

  @overload(QStyle.ContentsType, QStyleOption, QSize)
  @overload(QStyle.ContentsType, NoneType, QSize)
  @overload(QStyle.ContentsType, QStyleOption, QSize, QWidget)
  @overload(QStyle.ContentsType, QStyleOption, QSize, NoneType)
  @overload(QStyle.ContentsType, NoneType, QSize, QWidget)
  @overload(QStyle.ContentsType, NoneType, QSize, NoneType)
  def sizeFromContents(
      self,
      ct: QStyle.ContentsType,
      opt: Optional[QStyleOption],
      contentsSize: QSize,
      widget: Optional[QWidget] = None,
  ) -> QSize:
    """
    Calls Qt's 'QSize QStyleSheetStyle::sizeFromContents(ContentsType ct,
    const QStyleOption *opt, const QSize &contentsSize, const QWidget
    *widget) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qstylesheetstyle.html#sizeFromContents

    Parameters
    ----------

    ct : QStyle.ContentsType
      Passed on as its number.

    opt : Optional[QStyleOption]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    contentsSize : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QStyleSheetStyle::sizeFromContents(ContentsType ct, const
    #      QStyleOption *opt, const QSize &contentsSize, const QWidget
    #      *widget) const
    address = self.uglySide.call(
        'ritual_ZNK16QStyleSheetStyle16sizeFromContentsEN6QStyle12ContentsT'
        'ypeEPK12QStyleOptionRK5QSizePK7QWidget',
        ct.value, self._addressOf(opt), self._valueOf(contentsSize),
        self._addressOf(widget),
    )
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

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

  @overload(QStyle.StandardPixmap)
  @overload(QStyle.StandardPixmap, QStyleOption)
  @overload(QStyle.StandardPixmap, NoneType)
  @overload(QStyle.StandardPixmap, QStyleOption, QWidget)
  @overload(QStyle.StandardPixmap, QStyleOption, NoneType)
  @overload(QStyle.StandardPixmap, NoneType, QWidget)
  @overload(QStyle.StandardPixmap, NoneType, NoneType)
  def standardIcon(
      self,
      standardIcon: QStyle.StandardPixmap,
      opt: Optional[QStyleOption] = None,
      widget: Optional[QWidget] = None,
  ) -> QIcon:
    """
    Calls Qt's 'QIcon QStyleSheetStyle::standardIcon(StandardPixmap
    standardIcon, const QStyleOption *opt, const QWidget *widget) const'.

    Qt's own words: https://doc.qt.io/qt-6/qstylesheetstyle.html#standardIcon

    Parameters
    ----------

    standardIcon : QStyle.StandardPixmap
      Passed on as its number.

    opt : Optional[QStyleOption]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    Returns
    -------

    QIcon
      A new cute QIcon around the copy Qt gave back. Python owns it.
    """
    #  QIcon QStyleSheetStyle::standardIcon(StandardPixmap standardIcon,
    #      const QStyleOption *opt, const QWidget *widget) const
    address = self.uglySide.call(
        'ritual_ZNK16QStyleSheetStyle12standardIconEN6QStyle14StandardPixma'
        'pEPK12QStyleOptionPK7QWidget',
        standardIcon.value, self._addressOf(opt), self._addressOf(widget),
    )
    return QIcon._cuteOwning(address)

  @overload(QStyle.StandardPixmap)
  @overload(QStyle.StandardPixmap, QStyleOption)
  @overload(QStyle.StandardPixmap, NoneType)
  @overload(QStyle.StandardPixmap, QStyleOption, QWidget)
  @overload(QStyle.StandardPixmap, QStyleOption, NoneType)
  @overload(QStyle.StandardPixmap, NoneType, QWidget)
  @overload(QStyle.StandardPixmap, NoneType, NoneType)
  def standardPixmap(
      self,
      standardPixmap: QStyle.StandardPixmap,
      option: Optional[QStyleOption] = None,
      w: Optional[QWidget] = None,
  ) -> QPixmap:
    """
    Calls Qt's 'QPixmap QStyleSheetStyle::standardPixmap(StandardPixmap
    standardPixmap, const QStyleOption *option, const QWidget *w) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qstylesheetstyle.html#standardPixmap

    Parameters
    ----------

    standardPixmap : QStyle.StandardPixmap
      Passed on as its number.

    option : Optional[QStyleOption]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    w : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    Returns
    -------

    QPixmap
      A new cute QPixmap around the copy Qt gave back. Python owns it.
    """
    #  QPixmap QStyleSheetStyle::standardPixmap(StandardPixmap
    #      standardPixmap, const QStyleOption *option, const QWidget *w)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK16QStyleSheetStyle14standardPixmapEN6QStyle14StandardPix'
        'mapEPK12QStyleOptionPK7QWidget',
        standardPixmap.value, self._addressOf(option), self._addressOf(w),
    )
    from ..QtGui import QPixmap
    return QPixmap._cuteOwning(address)

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

  @overload(QStyle.StyleHint)
  @overload(QStyle.StyleHint, QStyleOption)
  @overload(QStyle.StyleHint, NoneType)
  @overload(QStyle.StyleHint, QStyleOption, QWidget)
  @overload(QStyle.StyleHint, QStyleOption, NoneType)
  @overload(QStyle.StyleHint, NoneType, QWidget)
  @overload(QStyle.StyleHint, NoneType, NoneType)
  @overload(QStyle.StyleHint, QStyleOption, QWidget, QStyleHintReturn)
  @overload(QStyle.StyleHint, QStyleOption, QWidget, NoneType)
  @overload(QStyle.StyleHint, QStyleOption, NoneType, QStyleHintReturn)
  @overload(QStyle.StyleHint, QStyleOption, NoneType, NoneType)
  @overload(QStyle.StyleHint, NoneType, QWidget, QStyleHintReturn)
  @overload(QStyle.StyleHint, NoneType, QWidget, NoneType)
  @overload(QStyle.StyleHint, NoneType, NoneType, QStyleHintReturn)
  @overload(QStyle.StyleHint, NoneType, NoneType, NoneType)
  def styleHint(
      self,
      sh: QStyle.StyleHint,
      opt: Optional[QStyleOption] = None,
      w: Optional[QWidget] = None,
      shret: Optional[QStyleHintReturn] = None,
  ) -> int:
    """
    Calls Qt's 'int QStyleSheetStyle::styleHint(StyleHint sh, const
    QStyleOption *opt, const QWidget *w, QStyleHintReturn *shret) const'.

    Qt's own words: https://doc.qt.io/qt-6/qstylesheetstyle.html#styleHint

    Parameters
    ----------

    sh : QStyle.StyleHint
      Passed on as its number.

    opt : Optional[QStyleOption]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    w : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    shret : Optional[QStyleHintReturn]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  int QStyleSheetStyle::styleHint(StyleHint sh, const QStyleOption *opt,
    #      const QWidget *w, QStyleHintReturn *shret) const
    return self.uglySide.call(
        'ritual_ZNK16QStyleSheetStyle9styleHintEN6QStyle9StyleHintEPK12QSty'
        'leOptionPK7QWidgetP16QStyleHintReturn',
        sh.value, self._addressOf(opt), self._addressOf(w),
        self._addressOf(shret),
    )

  @overload(QStyle.SubElement, QStyleOption)
  @overload(QStyle.SubElement, NoneType)
  @overload(QStyle.SubElement, QStyleOption, QWidget)
  @overload(QStyle.SubElement, QStyleOption, NoneType)
  @overload(QStyle.SubElement, NoneType, QWidget)
  @overload(QStyle.SubElement, NoneType, NoneType)
  def subElementRect(
      self,
      r: QStyle.SubElement,
      opt: Optional[QStyleOption],
      widget: Optional[QWidget] = None,
  ) -> QRect:
    """
    Calls Qt's 'QRect QStyleSheetStyle::subElementRect(SubElement r, const
    QStyleOption *opt, const QWidget *widget) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qstylesheetstyle.html#subElementRect

    Parameters
    ----------

    r : QStyle.SubElement
      Passed on as its number.

    opt : Optional[QStyleOption]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect QStyleSheetStyle::subElementRect(SubElement r, const
    #      QStyleOption *opt, const QWidget *widget) const
    address = self.uglySide.call(
        'ritual_ZNK16QStyleSheetStyle14subElementRectEN6QStyle10SubElementE'
        'PK12QStyleOptionPK7QWidget',
        r.value, self._addressOf(opt), self._addressOf(widget),
    )
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

  @overload(QStyle.ComplexControl, QStyleOptionComplex, QStyle.SubControl)
  @overload(QStyle.ComplexControl, NoneType, QStyle.SubControl)
  @overload(
      QStyle.ComplexControl, QStyleOptionComplex, QStyle.SubControl, QWidget,
  )
  @overload(
      QStyle.ComplexControl, QStyleOptionComplex, QStyle.SubControl,
      NoneType,
  )
  @overload(QStyle.ComplexControl, NoneType, QStyle.SubControl, QWidget)
  @overload(QStyle.ComplexControl, NoneType, QStyle.SubControl, NoneType)
  def subControlRect(
      self,
      cc: QStyle.ComplexControl,
      opt: Optional[QStyleOptionComplex],
      sc: QStyle.SubControl,
      w: Optional[QWidget] = None,
  ) -> QRect:
    """
    Calls Qt's 'QRect QStyleSheetStyle::subControlRect(ComplexControl cc,
    const QStyleOptionComplex *opt, SubControl sc, const QWidget *w) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qstylesheetstyle.html#subControlRect

    Parameters
    ----------

    cc : QStyle.ComplexControl
      Passed on as its number.

    opt : Optional[QStyleOptionComplex]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    sc : QStyle.SubControl
      Passed on as its number.

    w : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect QStyleSheetStyle::subControlRect(ComplexControl cc, const
    #      QStyleOptionComplex *opt, SubControl sc, const QWidget *w) const
    address = self.uglySide.call(
        'ritual_ZNK16QStyleSheetStyle14subControlRectEN6QStyle14ComplexCont'
        'rolEPK19QStyleOptionComplexNS0_10SubControlEPK7QWidget',
        cc.value, self._addressOf(opt), sc.value, self._addressOf(w),
    )
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'QStyleSheetStyle::QStyleSheetStyle(QStyle *baseStyle)': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: use of undeclared identifier 'styleSheetCaches'.
    """
    raise NotImplementedError(
        "'QStyleSheetStyle.__init__' has no cute function yet. Qt's "
        "'QStyleSheetStyle::QStyleSheetStyle(QStyle *baseStyle)': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: use of undeclared identifier "
        "'styleSheetCaches'.")

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

  @overload(QStyle.ComplexControl, QStyleOptionComplex, QPainter)
  @overload(QStyle.ComplexControl, QStyleOptionComplex, NoneType)
  @overload(QStyle.ComplexControl, NoneType, QPainter)
  @overload(QStyle.ComplexControl, NoneType, NoneType)
  @overload(QStyle.ComplexControl, QStyleOptionComplex, QPainter, QWidget)
  @overload(QStyle.ComplexControl, QStyleOptionComplex, QPainter, NoneType)
  @overload(QStyle.ComplexControl, QStyleOptionComplex, NoneType, QWidget)
  @overload(QStyle.ComplexControl, QStyleOptionComplex, NoneType, NoneType)
  @overload(QStyle.ComplexControl, NoneType, QPainter, QWidget)
  @overload(QStyle.ComplexControl, NoneType, QPainter, NoneType)
  @overload(QStyle.ComplexControl, NoneType, NoneType, QWidget)
  @overload(QStyle.ComplexControl, NoneType, NoneType, NoneType)
  def drawComplexControl(
      self,
      cc: QStyle.ComplexControl,
      opt: Optional[QStyleOptionComplex],
      p: Optional[QPainter],
      w: Optional[QWidget] = None,
  ) -> None:
    """
    Calls Qt's 'void QStyleSheetStyle::drawComplexControl(ComplexControl cc,
    const QStyleOptionComplex *opt, QPainter *p, const QWidget *w) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qstylesheetstyle.html#drawComplexControl

    Parameters
    ----------

    cc : QStyle.ComplexControl
      Passed on as its number.

    opt : Optional[QStyleOptionComplex]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    p : Optional[QPainter]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    w : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  void QStyleSheetStyle::drawComplexControl(ComplexControl cc, const
    #      QStyleOptionComplex *opt, QPainter *p, const QWidget *w) const
    self.uglySide.call(
        'ritual_ZNK16QStyleSheetStyle18drawComplexControlEN6QStyle14Complex'
        'ControlEPK19QStyleOptionComplexP8QPainterPK7QWidget',
        cc.value, self._addressOf(opt), self._addressOf(p),
        self._addressOf(w),
    )

  @overload(QStyle.ControlElement, QStyleOption, QPainter)
  @overload(QStyle.ControlElement, QStyleOption, NoneType)
  @overload(QStyle.ControlElement, NoneType, QPainter)
  @overload(QStyle.ControlElement, NoneType, NoneType)
  @overload(QStyle.ControlElement, QStyleOption, QPainter, QWidget)
  @overload(QStyle.ControlElement, QStyleOption, QPainter, NoneType)
  @overload(QStyle.ControlElement, QStyleOption, NoneType, QWidget)
  @overload(QStyle.ControlElement, QStyleOption, NoneType, NoneType)
  @overload(QStyle.ControlElement, NoneType, QPainter, QWidget)
  @overload(QStyle.ControlElement, NoneType, QPainter, NoneType)
  @overload(QStyle.ControlElement, NoneType, NoneType, QWidget)
  @overload(QStyle.ControlElement, NoneType, NoneType, NoneType)
  def drawControl(
      self,
      element: QStyle.ControlElement,
      opt: Optional[QStyleOption],
      p: Optional[QPainter],
      w: Optional[QWidget] = None,
  ) -> None:
    """
    Calls Qt's 'void QStyleSheetStyle::drawControl(ControlElement element,
    const QStyleOption *opt, QPainter *p, const QWidget *w) const'.

    Qt's own words: https://doc.qt.io/qt-6/qstylesheetstyle.html#drawControl

    Parameters
    ----------

    element : QStyle.ControlElement
      Passed on as its number.

    opt : Optional[QStyleOption]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    p : Optional[QPainter]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    w : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  void QStyleSheetStyle::drawControl(ControlElement element, const
    #      QStyleOption *opt, QPainter *p, const QWidget *w) const
    self.uglySide.call(
        'ritual_ZNK16QStyleSheetStyle11drawControlEN6QStyle14ControlElement'
        'EPK12QStyleOptionP8QPainterPK7QWidget',
        element.value, self._addressOf(opt), self._addressOf(p),
        self._addressOf(w),
    )

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

  @overload(QStyle.PrimitiveElement, QStyleOption, QPainter)
  @overload(QStyle.PrimitiveElement, QStyleOption, NoneType)
  @overload(QStyle.PrimitiveElement, NoneType, QPainter)
  @overload(QStyle.PrimitiveElement, NoneType, NoneType)
  @overload(QStyle.PrimitiveElement, QStyleOption, QPainter, QWidget)
  @overload(QStyle.PrimitiveElement, QStyleOption, QPainter, NoneType)
  @overload(QStyle.PrimitiveElement, QStyleOption, NoneType, QWidget)
  @overload(QStyle.PrimitiveElement, QStyleOption, NoneType, NoneType)
  @overload(QStyle.PrimitiveElement, NoneType, QPainter, QWidget)
  @overload(QStyle.PrimitiveElement, NoneType, QPainter, NoneType)
  @overload(QStyle.PrimitiveElement, NoneType, NoneType, QWidget)
  @overload(QStyle.PrimitiveElement, NoneType, NoneType, NoneType)
  def drawPrimitive(
      self,
      pe: QStyle.PrimitiveElement,
      opt: Optional[QStyleOption],
      p: Optional[QPainter],
      w: Optional[QWidget] = None,
  ) -> None:
    """
    Calls Qt's 'void QStyleSheetStyle::drawPrimitive(PrimitiveElement pe,
    const QStyleOption *opt, QPainter *p, const QWidget *w) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qstylesheetstyle.html#drawPrimitive

    Parameters
    ----------

    pe : QStyle.PrimitiveElement
      Passed on as its number.

    opt : Optional[QStyleOption]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    p : Optional[QPainter]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    w : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  void QStyleSheetStyle::drawPrimitive(PrimitiveElement pe, const
    #      QStyleOption *opt, QPainter *p, const QWidget *w) const
    self.uglySide.call(
        'ritual_ZNK16QStyleSheetStyle13drawPrimitiveEN6QStyle16PrimitiveEle'
        'mentEPK12QStyleOptionP8QPainterPK7QWidget',
        pe.value, self._addressOf(opt), self._addressOf(p),
        self._addressOf(w),
    )

  @overload(QWidget)
  @overload(NoneType)
  def polish(self, widget: Optional[QWidget]) -> None:
    """
    Calls Qt's 'void QStyleSheetStyle::polish(QWidget *widget)'.

    Qt's own words: https://doc.qt.io/qt-6/qstylesheetstyle.html#polish

    Parameters
    ----------

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QStyleSheetStyle::polish(QWidget *widget)
    self.uglySide.call(
        'ritual_ZN16QStyleSheetStyle6polishEP7QWidget',
        self._addressOf(widget),
    )

  @overload(QApplication)
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

  @overload(QWidget)
  @overload(NoneType)
  def unpolish(self, widget: Optional[QWidget]) -> None:
    """
    Calls Qt's 'void QStyleSheetStyle::unpolish(QWidget *widget)'.

    Qt's own words: https://doc.qt.io/qt-6/qstylesheetstyle.html#unpolish

    Parameters
    ----------

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QStyleSheetStyle::unpolish(QWidget *widget)
    self.uglySide.call(
        'ritual_ZN16QStyleSheetStyle8unpolishEP7QWidget',
        self._addressOf(widget),
    )

  @overload(QApplication)
  def unpolish(self, app: Optional[QApplication]) -> None:
    """
    Calls Qt's 'void QStyleSheetStyle::unpolish(QApplication *app)'.

    Qt's own words: https://doc.qt.io/qt-6/qstylesheetstyle.html#unpolish

    Parameters
    ----------

    app : Optional[QApplication]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QStyleSheetStyle::unpolish(QApplication *app)
    self.uglySide.call(
        'ritual_ZN16QStyleSheetStyle8unpolishEP12QApplication',
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

  @staticmethod
  def baseStyle(*__, **_) -> Never:
    """
    Qt's 'QStyle *QStyleSheetStyle::baseStyle() const': leans on
    'QStyleSheetStyle::staticMetaObject', which Qt's source does not mark for
    use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QStyleSheetStyle.baseStyle' has no cute function yet. Qt's "
        "'QStyle *QStyleSheetStyle::baseStyle() const': leans on "
        "'QStyleSheetStyle::staticMetaObject', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def defaultSize(*__, **_) -> Never:
    """
    Qt's 'QSize QStyleSheetStyle::defaultSize(const QWidget *a0, QSize a1,
    const QRect &a2, int a3) const': leans on
    'QStyleSheetStyle::staticMetaObject', which Qt's source does not mark for
    use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QStyleSheetStyle.defaultSize' has no cute function yet. Qt's "
        "'QSize QStyleSheetStyle::defaultSize(const QWidget *a0, QSize a1, "
        "const QRect &a2, int a3) const': leans on "
        "'QStyleSheetStyle::staticMetaObject', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def getDefaultStyleSheet(*__, **_) -> Never:
    """
    Qt's 'QCss::StyleSheet QStyleSheetStyle::getDefaultStyleSheet() const':
    Qt's library has no name for it, and its code in Qt's source does not
    compile apart from its file: unknown type name 'StyleSheet'.
    """
    raise NotImplementedError(
        "'QStyleSheetStyle.getDefaultStyleSheet' has no cute function yet. "
        "Qt's 'QCss::StyleSheet QStyleSheetStyle::getDefaultStyleSheet() "
        "const': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: unknown type name "
        "'StyleSheet'.")

  @staticmethod
  def hasStyleRule(*__, **_) -> Never:
    """
    Qt's 'bool QStyleSheetStyle::hasStyleRule(const QWidget *w, int part)
    const': Qt's library has no name for it, and its code in Qt's source does
    not compile apart from its file: use of undeclared identifier
    'styleSheetCaches'.
    """
    raise NotImplementedError(
        "'QStyleSheetStyle.hasStyleRule' has no cute function yet. Qt's "
        "'bool QStyleSheetStyle::hasStyleRule(const QWidget *w, int part) "
        "const': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: use of undeclared "
        "identifier 'styleSheetCaches'.")

  @staticmethod
  def initWidget(*__, **_) -> Never:
    """
    Qt's 'bool QStyleSheetStyle::initWidget(const QWidget *w) const': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: use of undeclared identifier 'styleSheetCaches'.
    """
    raise NotImplementedError(
        "'QStyleSheetStyle.initWidget' has no cute function yet. Qt's 'bool "
        "QStyleSheetStyle::initWidget(const QWidget *w) const': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: use of undeclared identifier "
        "'styleSheetCaches'.")

  @staticmethod
  def nativeFrameWidth(*__, **_) -> Never:
    """
    Qt's 'int QStyleSheetStyle::nativeFrameWidth(const QWidget *a0)': leans
    on 'QStyleSheetStyle::staticMetaObject', which Qt's source does not mark
    for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QStyleSheetStyle.nativeFrameWidth' has no cute function yet. Qt's "
        "'int QStyleSheetStyle::nativeFrameWidth(const QWidget *a0)': leans "
        "on 'QStyleSheetStyle::staticMetaObject', which Qt's source does "
        "not mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def positionRect(*__, **_) -> Never:
    """
    - Qt's 'QRect QStyleSheetStyle::positionRect(const QWidget *a0, const
      QRenderRule &a1, const QRenderRule &a2, int a3, const QRect &a4,
      Qt::LayoutDirection a5) const': Qt's library has no name for it, and
      its code in Qt's source does not compile apart from its file: unknown
      type name 'Origin'; did you mean 'QCss::Origin'?.
    - Qt's 'QRect QStyleSheetStyle::positionRect(const QWidget *w, const
      QRenderRule &rule2, int pe, const QRect &originRect,
      Qt::LayoutDirection dir) const': Qt's library has no name for it, and
      its code in Qt's source does not compile apart from its file: unknown
      type name 'QStyleSheetPositionData'.
    """
    raise NotImplementedError(
        "'QStyleSheetStyle.positionRect' has no cute function yet. Qt's "
        "'QRect QStyleSheetStyle::positionRect(const QWidget *a0, const "
        "QRenderRule &a1, const QRenderRule &a2, int a3, const QRect &a4, "
        "Qt::LayoutDirection a5) const': Qt's library has no name for it, "
        "and its code in Qt's source does not compile apart from its file: "
        "unknown type name 'Origin'; did you mean 'QCss::Origin'?. Qt's "
        "'QRect QStyleSheetStyle::positionRect(const QWidget *w, const "
        "QRenderRule &rule2, int pe, const QRect &originRect, "
        "Qt::LayoutDirection dir) const': Qt's library has no name for it, "
        "and its code in Qt's source does not compile apart from its file: "
        "unknown type name 'QStyleSheetPositionData'.")

  @staticmethod
  def renderMenuItemIcon(*__, **_) -> Never:
    """
    Qt's 'void QStyleSheetStyle::renderMenuItemIcon(const
    QStyleOptionMenuItem *mi, QPainter *p, const QWidget *w, const QRect
    &rect, QRenderRule &subRule) const': Qt's library has no name for it, and
    its code in Qt's source does not compile apart from its file: use of
    undeclared identifier 'PseudoElement_MenuIcon'.
    """
    raise NotImplementedError(
        "'QStyleSheetStyle.renderMenuItemIcon' has no cute function yet. "
        "Qt's 'void QStyleSheetStyle::renderMenuItemIcon(const "
        "QStyleOptionMenuItem *mi, QPainter *p, const QWidget *w, const "
        "QRect &rect, QRenderRule &subRule) const': Qt's library has no "
        "name for it, and its code in Qt's source does not compile apart "
        "from its file: use of undeclared identifier "
        "'PseudoElement_MenuIcon'.")

  @staticmethod
  def renderRule(*__, **_) -> Never:
    """
    - Qt's 'QRenderRule QStyleSheetStyle::renderRule(const QWidget *a0, int
      a1, quint64 a2) const': the compiler refuses its ritual as it would be
      written here: calling 'renderRule' with incomplete return type
      'QRenderRule'.
    - Qt's 'QRenderRule QStyleSheetStyle::renderRule(const QWidget *a0, const
      QStyleOption *a1, int a2) const': the compiler refuses its ritual as it
      would be written here: calling 'renderRule' with incomplete return type
      'QRenderRule'.
    """
    raise NotImplementedError(
        "'QStyleSheetStyle.renderRule' has no cute function yet. Qt's "
        "'QRenderRule QStyleSheetStyle::renderRule(const QWidget *a0, int "
        "a1, quint64 a2) const': the compiler refuses its ritual as it "
        "would be written here: calling 'renderRule' with incomplete return "
        "type 'QRenderRule'. Qt's 'QRenderRule "
        "QStyleSheetStyle::renderRule(const QWidget *a0, const QStyleOption "
        "*a1, int a2) const': the compiler refuses its ritual as it would "
        "be written here: calling 'renderRule' with incomplete return type "
        "'QRenderRule'.")

  @staticmethod
  def repolish(*__, **_) -> Never:
    """
    - Qt's 'void QStyleSheetStyle::repolish(QWidget *widget)': Qt's library
      has no name for it, and its code in Qt's source does not compile apart
      from its file: use of undeclared identifier 'styleSheetCaches'.
    - Qt's 'void QStyleSheetStyle::repolish(QApplication *app)': Qt's library
      has no name for it, and its code in Qt's source does not compile apart
      from its file: use of undeclared identifier 'styleSheetCaches'; did you
      mean 'QStyleSheetStyleCaches::styleSheetCache'?.
    """
    raise NotImplementedError(
        "'QStyleSheetStyle.repolish' has no cute function yet. Qt's 'void "
        "QStyleSheetStyle::repolish(QWidget *widget)': Qt's library has no "
        "name for it, and its code in Qt's source does not compile apart "
        "from its file: use of undeclared identifier 'styleSheetCaches'. "
        "Qt's 'void QStyleSheetStyle::repolish(QApplication *app)': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: use of undeclared identifier "
        "'styleSheetCaches'; did you mean "
        "'QStyleSheetStyleCaches::styleSheetCache'?.")

  @staticmethod
  def setGeometry(*__, **_) -> Never:
    """
    Qt's 'void QStyleSheetStyle::setGeometry(QWidget *a0)': Qt's library has
    no name for it, and its code in Qt's source does not compile apart from
    its file: use of undeclared identifier 'PseudoElement_None'.
    """
    raise NotImplementedError(
        "'QStyleSheetStyle.setGeometry' has no cute function yet. Qt's "
        "'void QStyleSheetStyle::setGeometry(QWidget *a0)': Qt's library "
        "has no name for it, and its code in Qt's source does not compile "
        "apart from its file: use of undeclared identifier "
        "'PseudoElement_None'.")

  @staticmethod
  def setPalette(*__, **_) -> Never:
    """
    Qt's 'void QStyleSheetStyle::setPalette(QWidget *a0)': Qt's library has
    no name for it, and its code in Qt's source does not compile apart from
    its file: use of undeclared identifier 'PseudoClass_Active'.
    """
    raise NotImplementedError(
        "'QStyleSheetStyle.setPalette' has no cute function yet. Qt's 'void "
        "QStyleSheetStyle::setPalette(QWidget *a0)': Qt's library has no "
        "name for it, and its code in Qt's source does not compile apart "
        "from its file: use of undeclared identifier 'PseudoClass_Active'.")

  @staticmethod
  def setProperties(*__, **_) -> Never:
    """
    Qt's 'void QStyleSheetStyle::setProperties(QWidget *a0)': Qt's library
    has no name for it, and its code in Qt's source does not compile apart
    from its file: use of undeclared identifier 'Declaration'.
    """
    raise NotImplementedError(
        "'QStyleSheetStyle.setProperties' has no cute function yet. Qt's "
        "'void QStyleSheetStyle::setProperties(QWidget *a0)': Qt's library "
        "has no name for it, and its code in Qt's source does not compile "
        "apart from its file: use of undeclared identifier 'Declaration'.")

  @staticmethod
  def styleRules(*__, **_) -> Never:
    """
    Qt's 'QList<QCss::StyleRule> QStyleSheetStyle::styleRules(const QWidget
    *w) const': Qt's library has no name for it, and its code in Qt's source
    does not compile apart from its file: use of undeclared identifier
    'StyleRule'.
    """
    raise NotImplementedError(
        "'QStyleSheetStyle.styleRules' has no cute function yet. Qt's "
        "'QList<QCss::StyleRule> QStyleSheetStyle::styleRules(const QWidget "
        "*w) const': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: use of undeclared "
        "identifier 'StyleRule'.")

  @staticmethod
  def styleSheetPalette(*__, **_) -> Never:
    """
    Qt's 'bool QStyleSheetStyle::styleSheetPalette(const QWidget *w, const
    QStyleOption *opt, QPalette *pal)': Qt's library has no name for it, and
    its code in Qt's source does not compile apart from its file: expected
    expression.
    """
    raise NotImplementedError(
        "'QStyleSheetStyle.styleSheetPalette' has no cute function yet. "
        "Qt's 'bool QStyleSheetStyle::styleSheetPalette(const QWidget *w, "
        "const QStyleOption *opt, QPalette *pal)': Qt's library has no name "
        "for it, and its code in Qt's source does not compile apart from "
        "its file: expected expression.")

  @staticmethod
  def titleBarLayout(*__, **_) -> Never:
    """
    Qt's 'QHash<QStyle::SubControl, QRect>
    QStyleSheetStyle::titleBarLayout(const QWidget *w, const
    QStyleOptionTitleBar *tb) const': Qt's library has no name for it, and
    its code in Qt's source does not compile apart from its file: calling
    'renderRule' with incomplete return type 'QRenderRule'.
    """
    raise NotImplementedError(
        "'QStyleSheetStyle.titleBarLayout' has no cute function yet. Qt's "
        "'QHash<QStyle::SubControl, QRect> "
        "QStyleSheetStyle::titleBarLayout(const QWidget *w, const "
        "QStyleOptionTitleBar *tb) const': Qt's library has no name for it, "
        "and its code in Qt's source does not compile apart from its file: "
        "calling 'renderRule' with incomplete return type 'QRenderRule'.")

  @staticmethod
  def unsetPalette(*__, **_) -> Never:
    """
    Qt's 'void QStyleSheetStyle::unsetPalette(QWidget *a0)': Qt's library has
    no name for it, and its code in Qt's source does not compile apart from
    its file: use of undeclared identifier 'styleSheetCaches'.
    """
    raise NotImplementedError(
        "'QStyleSheetStyle.unsetPalette' has no cute function yet. Qt's "
        "'void QStyleSheetStyle::unsetPalette(QWidget *a0)': Qt's library "
        "has no name for it, and its code in Qt's source does not compile "
        "apart from its file: use of undeclared identifier "
        "'styleSheetCaches'.")

  @staticmethod
  def unsetStyleSheetFont(*__, **_) -> Never:
    """
    Qt's 'void QStyleSheetStyle::unsetStyleSheetFont(QWidget *a0) const':
    Qt's library has no name for it, and its code in Qt's source does not
    compile apart from its file: use of undeclared identifier
    'styleSheetCaches'.
    """
    raise NotImplementedError(
        "'QStyleSheetStyle.unsetStyleSheetFont' has no cute function yet. "
        "Qt's 'void QStyleSheetStyle::unsetStyleSheetFont(QWidget *a0) "
        "const': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: use of undeclared "
        "identifier 'styleSheetCaches'.")

  @staticmethod
  def updateStyleSheetFont(*__, **_) -> Never:
    """
    Qt's 'void QStyleSheetStyle::updateStyleSheetFont(QWidget *w) const':
    Qt's library has no name for it, and its code in Qt's source does not
    compile apart from its file: use of undeclared identifier
    'PseudoClass_Active'; did you mean 'QCss::PseudoClass_Active'?.
    """
    raise NotImplementedError(
        "'QStyleSheetStyle.updateStyleSheetFont' has no cute function yet. "
        "Qt's 'void QStyleSheetStyle::updateStyleSheetFont(QWidget *w) "
        "const': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: use of undeclared "
        "identifier 'PseudoClass_Active'; did you mean "
        "'QCss::PseudoClass_Active'?.")
