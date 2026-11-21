"""
QStyle binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/qstyle.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import Qt, QObject
from ..QtGui import QIconMode, QPaletteColorRole
from . import QSizePolicyControlType, QStyleComplexControl
from . import QStyleContentsType, QStyleControlElement, QStylePixelMetric
from . import QStylePrimitiveElement, QStyleRequestSoftwareInputPanel
from . import QStyleStandardPixmap, QStyleStateFlag, QStyleStyleHint
from . import QStyleSubControl, QStyleSubElement

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QPoint, QRect, QSize
  from ..QtGui import QFontMetrics, QIcon, QPainter, QPalette, QPixmap
  from . import QApplication, QSizePolicy, QStyleOption, QStyleOptionComplex
  from . import QWidget
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QApplication = WAIT['QApplication']
  QFontMetrics = WAIT['QFontMetrics']
  QPainter = WAIT['QPainter']
  QPalette = WAIT['QPalette']
  QPixmap = WAIT['QPixmap']
  QPoint = WAIT['QPoint']
  QRect = WAIT['QRect']
  QSize = WAIT['QSize']
  QStyleOption = WAIT['QStyleOption']
  QStyleOptionComplex = WAIT['QStyleOptionComplex']
  QWidget = WAIT['QWidget']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QStyle(QObject):
  """
  The cute side of Qt's QStyle: a plain Python object standing in front of
  one C++ QStyle.

  It is built on the cute 'QObject', as Qt's QStyle is built on Qt's QObject,
  and has everything that class has.

  What exists
  -----------

  Every function of Qt's QStyle that has a ritual and that Python can call so
  far, 30 names in all: 'metaObject', 'tr', 'name', 'polish', 'unpolish',
  'itemTextRect', 'itemPixmapRect', 'drawItemText', 'drawItemPixmap',
  'standardPalette', 'drawPrimitive', 'drawControl', 'subElementRect',
  'drawComplexControl', 'hitTestComplexControl', 'subControlRect',
  'pixelMetric', 'sizeFromContents', 'standardPixmap', 'standardIcon',
  'generatedIconPixmap', 'visualRect', 'visualPos',
  'sliderPositionFromValue', 'sliderValueFromPosition', 'visualAlignment',
  'alignedRect', 'layoutSpacing', 'combinedLayoutSpacing', 'proxy'. None can
  be made from Python: one comes out of a function of another class that
  gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QStyle::~QStyle()': the destructor: Python never removes a C++
    QStyle.
  - Qt's 'int QStyle::styleHint(StyleHint stylehint, const QStyleOption *opt,
    const QWidget *widget, QStyleHintReturn *returnData) const': names
    'QStyleHintReturn', which has no cute class yet.

  What has no ritual
  ------------------

  13 of the 47 functions Qt declares: 5 private; 3 takes or gives a type that
  cannot be passed yet; 2 forbidden; 1 a template; 1 protected; 1 the class
  is abstract, so C++ cannot make one.

  What to expect
  --------------

  - The C++ QStyle is created at the first use, not by 'QStyle(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QStyle.
  - Qt tells when it has removed the C++ QStyle. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
  """

  #  The enums Qt writes inside QStyle, and the names Qt has for the
  #  combinations of its flags enums.
  ComplexControl = QStyleComplexControl
  ContentsType = QStyleContentsType
  ControlElement = QStyleControlElement
  PixelMetric = QStylePixelMetric
  PrimitiveElement = QStylePrimitiveElement
  RequestSoftwareInputPanel = QStyleRequestSoftwareInputPanel
  StandardPixmap = QStyleStandardPixmap
  StateFlag = QStyleStateFlag
  State = QStyleStateFlag
  StyleHint = QStyleStyleHint
  SubControl = QStyleSubControl
  SubControls = QStyleSubControl
  SubElement = QStyleSubElement

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
    Calls Qt's 'QString QStyle::tr(const char *s, const char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qstyle.html#tr

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
    #  QString QStyle::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN6QStyle2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  @overload(Qt.LayoutDirection, QRect, QRect)
  def visualRect(
      direction: Qt.LayoutDirection,
      boundingRect: QRect,
      logicalRect: QRect,
  ) -> QRect:
    """
    Calls Qt's 'QRect QStyle::visualRect(Qt::LayoutDirection direction, const
    QRect &boundingRect, const QRect &logicalRect)'.

    Qt's own words: https://doc.qt.io/qt-6/qstyle.html#visualRect

    Parameters
    ----------

    direction : Qt.LayoutDirection
      Passed on as its number.

    boundingRect : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.

    logicalRect : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect QStyle::visualRect(Qt::LayoutDirection direction, const QRect
    #      &boundingRect, const QRect &logicalRect)
    address = Rituals.call(
        'ritual_ZN6QStyle10visualRectEN2Qt15LayoutDirectionERK5QRectS4_',
        direction.value, CuteMixin._valueOf(boundingRect),
        CuteMixin._valueOf(logicalRect),
    )
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

  @staticmethod
  @overload(Qt.LayoutDirection, QRect, QPoint)
  def visualPos(
      direction: Qt.LayoutDirection,
      boundingRect: QRect,
      logicalPos: QPoint,
  ) -> QPoint:
    """
    Calls Qt's 'QPoint QStyle::visualPos(Qt::LayoutDirection direction, const
    QRect &boundingRect, const QPoint &logicalPos)'.

    Qt's own words: https://doc.qt.io/qt-6/qstyle.html#visualPos

    Parameters
    ----------

    direction : Qt.LayoutDirection
      Passed on as its number.

    boundingRect : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.

    logicalPos : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.

    Returns
    -------

    QPoint
      A new cute QPoint around the copy Qt gave back. Python owns it.
    """
    #  QPoint QStyle::visualPos(Qt::LayoutDirection direction, const QRect
    #      &boundingRect, const QPoint &logicalPos)
    address = Rituals.call(
        'ritual_ZN6QStyle9visualPosEN2Qt15LayoutDirectionERK5QRectRK6QPoint',
        direction.value, CuteMixin._valueOf(boundingRect),
        CuteMixin._valueOf(logicalPos),
    )
    from ..QtCore import QPoint
    return QPoint._cuteOwning(address)

  @staticmethod
  @overload(int, int, int, int)
  @overload(int, int, int, int, bool)
  def sliderPositionFromValue(
      min: int,
      max: int,
      val: int,
      space: int,
      upsideDown: bool = False,
  ) -> int:
    """
    Calls Qt's 'int QStyle::sliderPositionFromValue(int min, int max, int
    val, int space, bool upsideDown)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qstyle.html#sliderPositionFromValue

    Parameters
    ----------

    min : int
      Passed on as it is.

    max : int
      Passed on as it is.

    val : int
      Passed on as it is.

    space : int
      Passed on as it is.

    upsideDown : bool
      Passed on as it is. May be left out, as in Qt: it is then False.
    """
    #  int QStyle::sliderPositionFromValue(int min, int max, int val, int
    #      space, bool upsideDown)
    return Rituals.call(
        'ritual_ZN6QStyle23sliderPositionFromValueEiiiib',
        min, max, val, space, upsideDown,
    )

  @staticmethod
  @overload(int, int, int, int)
  @overload(int, int, int, int, bool)
  def sliderValueFromPosition(
      min: int,
      max: int,
      pos: int,
      space: int,
      upsideDown: bool = False,
  ) -> int:
    """
    Calls Qt's 'int QStyle::sliderValueFromPosition(int min, int max, int
    pos, int space, bool upsideDown)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qstyle.html#sliderValueFromPosition

    Parameters
    ----------

    min : int
      Passed on as it is.

    max : int
      Passed on as it is.

    pos : int
      Passed on as it is.

    space : int
      Passed on as it is.

    upsideDown : bool
      Passed on as it is. May be left out, as in Qt: it is then False.
    """
    #  int QStyle::sliderValueFromPosition(int min, int max, int pos, int
    #      space, bool upsideDown)
    return Rituals.call(
        'ritual_ZN6QStyle23sliderValueFromPositionEiiiib',
        min, max, pos, space, upsideDown,
    )

  @staticmethod
  @overload(Qt.LayoutDirection, Qt.Alignment)
  def visualAlignment(
      direction: Qt.LayoutDirection,
      alignment: Qt.Alignment,
  ) -> Qt.Alignment:
    """
    Calls Qt's 'Qt::Alignment QStyle::visualAlignment(Qt::LayoutDirection
    direction, Qt::Alignment alignment)'.

    Qt's own words: https://doc.qt.io/qt-6/qstyle.html#visualAlignment

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
    #  Qt::Alignment QStyle::visualAlignment(Qt::LayoutDirection direction,
    #      Qt::Alignment alignment)
    return Qt.Alignment(Rituals.call(
        'ritual_ZN6QStyle15visualAlignmentEN2Qt15LayoutDirectionE6QFlagsINS'
        '0_13AlignmentFlagEE',
        direction.value, alignment.value,
    ))

  @staticmethod
  @overload(Qt.LayoutDirection, Qt.Alignment, QSize, QRect)
  def alignedRect(
      direction: Qt.LayoutDirection,
      alignment: Qt.Alignment,
      size: QSize,
      rectangle: QRect,
  ) -> QRect:
    """
    Calls Qt's 'QRect QStyle::alignedRect(Qt::LayoutDirection direction,
    Qt::Alignment alignment, const QSize &size, const QRect &rectangle)'.

    Qt's own words: https://doc.qt.io/qt-6/qstyle.html#alignedRect

    Parameters
    ----------

    direction : Qt.LayoutDirection
      Passed on as its number.

    alignment : Qt.Alignment
      Passed on as its number.

    size : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.

    rectangle : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect QStyle::alignedRect(Qt::LayoutDirection direction, Qt::Alignment
    #      alignment, const QSize &size, const QRect &rectangle)
    address = Rituals.call(
        'ritual_ZN6QStyle11alignedRectEN2Qt15LayoutDirectionE6QFlagsINS0_13'
        'AlignmentFlagEERK5QSizeRK5QRect',
        direction.value, alignment.value, CuteMixin._valueOf(size),
        CuteMixin._valueOf(rectangle),
    )
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QStyle'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QStyle::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qstyle.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QStyle::metaObject() const
    address = self.uglySide.call('ritual_ZNK6QStyle10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def name(self) -> str:
    """
    Calls Qt's 'QString QStyle::name() const'.

    Qt's own words: https://doc.qt.io/qt-6/qstyle.html#name

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QStyle::name() const
    return self.uglySide.call('ritual_ZNK6QStyle4nameEv')

  @overload(QFontMetrics, QRect, int, bool, str)
  def itemTextRect(
      self,
      fm: QFontMetrics,
      r: QRect,
      flags: int,
      enabled: bool,
      text: str,
  ) -> QRect:
    """
    Calls Qt's 'QRect QStyle::itemTextRect(const QFontMetrics &fm, const
    QRect &r, int flags, bool enabled, const QString &text) const'.

    Qt's own words: https://doc.qt.io/qt-6/qstyle.html#itemTextRect

    Parameters
    ----------

    fm : QFontMetrics
      Passed on as a value: Qt reads the C++ QFontMetrics, which stays
      Python's own.

    r : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.

    flags : int
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
    #  QRect QStyle::itemTextRect(const QFontMetrics &fm, const QRect &r, int
    #      flags, bool enabled, const QString &text) const
    address = self.uglySide.call(
        'ritual_ZNK6QStyle12itemTextRectERK12QFontMetricsRK5QRectibRK7QStri'
        'ng',
        self._valueOf(fm), self._valueOf(r), flags, enabled, text,
    )
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

  @overload(QRect, int, QPixmap)
  def itemPixmapRect(self, r: QRect, flags: int, pixmap: QPixmap) -> QRect:
    """
    Calls Qt's 'QRect QStyle::itemPixmapRect(const QRect &r, int flags, const
    QPixmap &pixmap) const'.

    Qt's own words: https://doc.qt.io/qt-6/qstyle.html#itemPixmapRect

    Parameters
    ----------

    r : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.

    flags : int
      Passed on as it is.

    pixmap : QPixmap
      Passed on as a value: Qt reads the C++ QPixmap, which stays Python's
      own.

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect QStyle::itemPixmapRect(const QRect &r, int flags, const QPixmap
    #      &pixmap) const
    address = self.uglySide.call(
        'ritual_ZNK6QStyle14itemPixmapRectERK5QRectiRK7QPixmap',
        self._valueOf(r), flags, self._valueOf(pixmap),
    )
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

  def standardPalette(self) -> QPalette:
    """
    Calls Qt's 'QPalette QStyle::standardPalette() const'.

    Qt's own words: https://doc.qt.io/qt-6/qstyle.html#standardPalette

    Returns
    -------

    QPalette
      A new cute QPalette around the copy Qt gave back. Python owns it.
    """
    #  QPalette QStyle::standardPalette() const
    address = self.uglySide.call('ritual_ZNK6QStyle15standardPaletteEv')
    from ..QtGui import QPalette
    return QPalette._cuteOwning(address)

  @overload(SubElement, QStyleOption)
  @overload(SubElement, NoneType)
  @overload(SubElement, QStyleOption, QWidget)
  @overload(SubElement, QStyleOption, NoneType)
  @overload(SubElement, NoneType, QWidget)
  @overload(SubElement, NoneType, NoneType)
  def subElementRect(
      self,
      subElement: SubElement,
      option: Optional[QStyleOption],
      widget: Optional[QWidget] = None,
  ) -> QRect:
    """
    Calls Qt's 'QRect QStyle::subElementRect(SubElement subElement, const
    QStyleOption *option, const QWidget *widget) const'.

    Qt's own words: https://doc.qt.io/qt-6/qstyle.html#subElementRect

    Parameters
    ----------

    subElement : SubElement
      Passed on as its number.

    option : Optional[QStyleOption]
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
    #  QRect QStyle::subElementRect(SubElement subElement, const QStyleOption
    #      *option, const QWidget *widget) const
    address = self.uglySide.call(
        'ritual_ZNK6QStyle14subElementRectENS_10SubElementEPK12QStyleOption'
        'PK7QWidget',
        subElement.value, self._addressOf(option), self._addressOf(widget),
    )
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

  @overload(ComplexControl, QStyleOptionComplex, QPoint)
  @overload(ComplexControl, NoneType, QPoint)
  @overload(ComplexControl, QStyleOptionComplex, QPoint, QWidget)
  @overload(ComplexControl, QStyleOptionComplex, QPoint, NoneType)
  @overload(ComplexControl, NoneType, QPoint, QWidget)
  @overload(ComplexControl, NoneType, QPoint, NoneType)
  def hitTestComplexControl(
      self,
      cc: ComplexControl,
      opt: Optional[QStyleOptionComplex],
      pt: QPoint,
      widget: Optional[QWidget] = None,
  ) -> SubControl:
    """
    Calls Qt's 'SubControl QStyle::hitTestComplexControl(ComplexControl cc,
    const QStyleOptionComplex *opt, const QPoint &pt, const QWidget *widget)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qstyle.html#hitTestComplexControl

    Parameters
    ----------

    cc : ComplexControl
      Passed on as its number.

    opt : Optional[QStyleOptionComplex]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    pt : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    Returns
    -------

    SubControl
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'SubControl(number)'
      gives.
    """
    #  SubControl QStyle::hitTestComplexControl(ComplexControl cc, const
    #      QStyleOptionComplex *opt, const QPoint &pt, const QWidget *widget)
    #      const
    return QStyle.SubControl(self.uglySide.call(
        'ritual_ZNK6QStyle21hitTestComplexControlENS_14ComplexControlEPK19Q'
        'StyleOptionComplexRK6QPointPK7QWidget',
        cc.value, self._addressOf(opt), self._valueOf(pt),
        self._addressOf(widget),
    ))

  @overload(ComplexControl, QStyleOptionComplex, SubControl)
  @overload(ComplexControl, NoneType, SubControl)
  @overload(ComplexControl, QStyleOptionComplex, SubControl, QWidget)
  @overload(ComplexControl, QStyleOptionComplex, SubControl, NoneType)
  @overload(ComplexControl, NoneType, SubControl, QWidget)
  @overload(ComplexControl, NoneType, SubControl, NoneType)
  def subControlRect(
      self,
      cc: ComplexControl,
      opt: Optional[QStyleOptionComplex],
      sc: SubControl,
      widget: Optional[QWidget] = None,
  ) -> QRect:
    """
    Calls Qt's 'QRect QStyle::subControlRect(ComplexControl cc, const
    QStyleOptionComplex *opt, SubControl sc, const QWidget *widget) const'.

    Qt's own words: https://doc.qt.io/qt-6/qstyle.html#subControlRect

    Parameters
    ----------

    cc : ComplexControl
      Passed on as its number.

    opt : Optional[QStyleOptionComplex]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    sc : SubControl
      Passed on as its number.

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect QStyle::subControlRect(ComplexControl cc, const
    #      QStyleOptionComplex *opt, SubControl sc, const QWidget *widget)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK6QStyle14subControlRectENS_14ComplexControlEPK19QStyleOp'
        'tionComplexNS_10SubControlEPK7QWidget',
        cc.value, self._addressOf(opt), sc.value, self._addressOf(widget),
    )
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

  @overload(PixelMetric)
  @overload(PixelMetric, QStyleOption)
  @overload(PixelMetric, NoneType)
  @overload(PixelMetric, QStyleOption, QWidget)
  @overload(PixelMetric, QStyleOption, NoneType)
  @overload(PixelMetric, NoneType, QWidget)
  @overload(PixelMetric, NoneType, NoneType)
  def pixelMetric(
      self,
      metric: PixelMetric,
      option: Optional[QStyleOption] = None,
      widget: Optional[QWidget] = None,
  ) -> int:
    """
    Calls Qt's 'int QStyle::pixelMetric(PixelMetric metric, const
    QStyleOption *option, const QWidget *widget) const'.

    Qt's own words: https://doc.qt.io/qt-6/qstyle.html#pixelMetric

    Parameters
    ----------

    metric : PixelMetric
      Passed on as its number.

    option : Optional[QStyleOption]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  int QStyle::pixelMetric(PixelMetric metric, const QStyleOption
    #      *option, const QWidget *widget) const
    return self.uglySide.call(
        'ritual_ZNK6QStyle11pixelMetricENS_11PixelMetricEPK12QStyleOptionPK'
        '7QWidget',
        metric.value, self._addressOf(option), self._addressOf(widget),
    )

  @overload(ContentsType, QStyleOption, QSize)
  @overload(ContentsType, NoneType, QSize)
  @overload(ContentsType, QStyleOption, QSize, QWidget)
  @overload(ContentsType, QStyleOption, QSize, NoneType)
  @overload(ContentsType, NoneType, QSize, QWidget)
  @overload(ContentsType, NoneType, QSize, NoneType)
  def sizeFromContents(
      self,
      ct: ContentsType,
      opt: Optional[QStyleOption],
      contentsSize: QSize,
      w: Optional[QWidget] = None,
  ) -> QSize:
    """
    Calls Qt's 'QSize QStyle::sizeFromContents(ContentsType ct, const
    QStyleOption *opt, const QSize &contentsSize, const QWidget *w) const'.

    Qt's own words: https://doc.qt.io/qt-6/qstyle.html#sizeFromContents

    Parameters
    ----------

    ct : ContentsType
      Passed on as its number.

    opt : Optional[QStyleOption]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    contentsSize : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.

    w : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QStyle::sizeFromContents(ContentsType ct, const QStyleOption
    #      *opt, const QSize &contentsSize, const QWidget *w) const
    address = self.uglySide.call(
        'ritual_ZNK6QStyle16sizeFromContentsENS_12ContentsTypeEPK12QStyleOp'
        'tionRK5QSizePK7QWidget',
        ct.value, self._addressOf(opt), self._valueOf(contentsSize),
        self._addressOf(w),
    )
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  @overload(StandardPixmap)
  @overload(StandardPixmap, QStyleOption)
  @overload(StandardPixmap, NoneType)
  @overload(StandardPixmap, QStyleOption, QWidget)
  @overload(StandardPixmap, QStyleOption, NoneType)
  @overload(StandardPixmap, NoneType, QWidget)
  @overload(StandardPixmap, NoneType, NoneType)
  def standardPixmap(
      self,
      standardPixmap: StandardPixmap,
      opt: Optional[QStyleOption] = None,
      widget: Optional[QWidget] = None,
  ) -> QPixmap:
    """
    Calls Qt's 'QPixmap QStyle::standardPixmap(StandardPixmap standardPixmap,
    const QStyleOption *opt, const QWidget *widget) const'.

    Qt's own words: https://doc.qt.io/qt-6/qstyle.html#standardPixmap

    Parameters
    ----------

    standardPixmap : StandardPixmap
      Passed on as its number.

    opt : Optional[QStyleOption]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    Returns
    -------

    QPixmap
      A new cute QPixmap around the copy Qt gave back. Python owns it.
    """
    #  QPixmap QStyle::standardPixmap(StandardPixmap standardPixmap, const
    #      QStyleOption *opt, const QWidget *widget) const
    address = self.uglySide.call(
        'ritual_ZNK6QStyle14standardPixmapENS_14StandardPixmapEPK12QStyleOp'
        'tionPK7QWidget',
        standardPixmap.value, self._addressOf(opt), self._addressOf(widget),
    )
    from ..QtGui import QPixmap
    return QPixmap._cuteOwning(address)

  @overload(StandardPixmap)
  @overload(StandardPixmap, QStyleOption)
  @overload(StandardPixmap, NoneType)
  @overload(StandardPixmap, QStyleOption, QWidget)
  @overload(StandardPixmap, QStyleOption, NoneType)
  @overload(StandardPixmap, NoneType, QWidget)
  @overload(StandardPixmap, NoneType, NoneType)
  def standardIcon(
      self,
      standardIcon: StandardPixmap,
      option: Optional[QStyleOption] = None,
      widget: Optional[QWidget] = None,
  ) -> QIcon:
    """
    Calls Qt's 'QIcon QStyle::standardIcon(StandardPixmap standardIcon, const
    QStyleOption *option, const QWidget *widget) const'.

    Qt's own words: https://doc.qt.io/qt-6/qstyle.html#standardIcon

    Parameters
    ----------

    standardIcon : StandardPixmap
      Passed on as its number.

    option : Optional[QStyleOption]
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
    #  QIcon QStyle::standardIcon(StandardPixmap standardIcon, const
    #      QStyleOption *option, const QWidget *widget) const
    address = self.uglySide.call(
        'ritual_ZNK6QStyle12standardIconENS_14StandardPixmapEPK12QStyleOpti'
        'onPK7QWidget',
        standardIcon.value, self._addressOf(option), self._addressOf(widget),
    )
    from ..QtGui import QIcon
    return QIcon._cuteOwning(address)

  @overload(QIconMode, QPixmap, QStyleOption)
  @overload(QIconMode, QPixmap, NoneType)
  def generatedIconPixmap(
      self,
      iconMode: QIcon.Mode,
      pixmap: QPixmap,
      opt: Optional[QStyleOption],
  ) -> QPixmap:
    """
    Calls Qt's 'QPixmap QStyle::generatedIconPixmap(QIcon::Mode iconMode,
    const QPixmap &pixmap, const QStyleOption *opt) const'.

    Qt's own words: https://doc.qt.io/qt-6/qstyle.html#generatedIconPixmap

    Parameters
    ----------

    iconMode : QIcon.Mode
      Passed on as its number.

    pixmap : QPixmap
      Passed on as a value: Qt reads the C++ QPixmap, which stays Python's
      own.

    opt : Optional[QStyleOption]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QPixmap
      A new cute QPixmap around the copy Qt gave back. Python owns it.
    """
    #  QPixmap QStyle::generatedIconPixmap(QIcon::Mode iconMode, const
    #      QPixmap &pixmap, const QStyleOption *opt) const
    address = self.uglySide.call(
        'ritual_ZNK6QStyle19generatedIconPixmapEN5QIcon4ModeERK7QPixmapPK12'
        'QStyleOption',
        iconMode.value, self._valueOf(pixmap), self._addressOf(opt),
    )
    from ..QtGui import QPixmap
    return QPixmap._cuteOwning(address)

  @overload(QSizePolicyControlType, QSizePolicyControlType, Qt.Orientation)
  @overload(
      QSizePolicyControlType, QSizePolicyControlType, Qt.Orientation,
      QStyleOption,
  )
  @overload(
      QSizePolicyControlType, QSizePolicyControlType, Qt.Orientation,
      NoneType,
  )
  @overload(
      QSizePolicyControlType, QSizePolicyControlType, Qt.Orientation,
      QStyleOption, QWidget,
  )
  @overload(
      QSizePolicyControlType, QSizePolicyControlType, Qt.Orientation,
      QStyleOption, NoneType,
  )
  @overload(
      QSizePolicyControlType, QSizePolicyControlType, Qt.Orientation,
      NoneType, QWidget,
  )
  @overload(
      QSizePolicyControlType, QSizePolicyControlType, Qt.Orientation,
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
    Calls Qt's 'int QStyle::layoutSpacing(QSizePolicy::ControlType control1,
    QSizePolicy::ControlType control2, Qt::Orientation orientation, const
    QStyleOption *option, const QWidget *widget) const'.

    Qt's own words: https://doc.qt.io/qt-6/qstyle.html#layoutSpacing

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
    #  int QStyle::layoutSpacing(QSizePolicy::ControlType control1,
    #      QSizePolicy::ControlType control2, Qt::Orientation orientation,
    #      const QStyleOption *option, const QWidget *widget) const
    return self.uglySide.call(
        'ritual_ZNK6QStyle13layoutSpacingEN11QSizePolicy11ControlTypeES1_N2'
        'Qt11OrientationEPK12QStyleOptionPK7QWidget',
        control1.value, control2.value, orientation.value,
        self._addressOf(option), self._addressOf(widget),
    )

  @overload(QSizePolicyControlType, QSizePolicyControlType, Qt.Orientation)
  @overload(
      QSizePolicyControlType, QSizePolicyControlType, Qt.Orientation,
      QStyleOption,
  )
  @overload(
      QSizePolicyControlType, QSizePolicyControlType, Qt.Orientation,
      NoneType,
  )
  @overload(
      QSizePolicyControlType, QSizePolicyControlType, Qt.Orientation,
      QStyleOption, QWidget,
  )
  @overload(
      QSizePolicyControlType, QSizePolicyControlType, Qt.Orientation,
      QStyleOption, NoneType,
  )
  @overload(
      QSizePolicyControlType, QSizePolicyControlType, Qt.Orientation,
      NoneType, QWidget,
  )
  @overload(
      QSizePolicyControlType, QSizePolicyControlType, Qt.Orientation,
      NoneType, NoneType,
  )
  def combinedLayoutSpacing(
      self,
      controls1: QSizePolicy.ControlTypes,
      controls2: QSizePolicy.ControlTypes,
      orientation: Qt.Orientation,
      option: Optional[QStyleOption] = None,
      widget: Optional[QWidget] = None,
  ) -> int:
    """
    Calls Qt's 'int QStyle::combinedLayoutSpacing(QSizePolicy::ControlTypes
    controls1, QSizePolicy::ControlTypes controls2, Qt::Orientation
    orientation, QStyleOption *option, QWidget *widget) const'.

    Qt's own words: https://doc.qt.io/qt-6/qstyle.html#combinedLayoutSpacing

    Parameters
    ----------

    controls1 : QSizePolicy.ControlTypes
      Passed on as its number.

    controls2 : QSizePolicy.ControlTypes
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
    #  int QStyle::combinedLayoutSpacing(QSizePolicy::ControlTypes controls1,
    #      QSizePolicy::ControlTypes controls2, Qt::Orientation orientation,
    #      QStyleOption *option, QWidget *widget) const
    return self.uglySide.call(
        'ritual_ZNK6QStyle21combinedLayoutSpacingE6QFlagsIN11QSizePolicy11C'
        'ontrolTypeEES3_N2Qt11OrientationEP12QStyleOptionP7QWidget',
        controls1.value, controls2.value, orientation.value,
        self._addressOf(option), self._addressOf(widget),
    )

  def proxy(self) -> Optional[QStyle]:
    """
    Calls Qt's 'const QStyle *QStyle::proxy() const'.

    Qt's own words: https://doc.qt.io/qt-6/qstyle.html#proxy

    Returns
    -------

    Optional[QStyle]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QStyle *QStyle::proxy() const
    address = self.uglySide.call('ritual_ZNK6QStyle5proxyEv')
    return QStyle._cuteAt(address)

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

  @overload(QWidget)
  @overload(NoneType)
  def polish(self, widget: Optional[QWidget]) -> None:
    """
    Calls Qt's 'void QStyle::polish(QWidget *widget)'.

    Qt's own words: https://doc.qt.io/qt-6/qstyle.html#polish

    Parameters
    ----------

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QStyle::polish(QWidget *widget)
    self.uglySide.call(
        'ritual_ZN6QStyle6polishEP7QWidget', self._addressOf(widget),
    )

  @overload(QApplication)
  def polish(self, application: Optional[QApplication]) -> None:
    """
    Calls Qt's 'void QStyle::polish(QApplication *application)'.

    Qt's own words: https://doc.qt.io/qt-6/qstyle.html#polish

    Parameters
    ----------

    application : Optional[QApplication]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QStyle::polish(QApplication *application)
    self.uglySide.call(
        'ritual_ZN6QStyle6polishEP12QApplication',
        self._addressOf(application),
    )

  @overload(QWidget)
  @overload(NoneType)
  def unpolish(self, widget: Optional[QWidget]) -> None:
    """
    Calls Qt's 'void QStyle::unpolish(QWidget *widget)'.

    Qt's own words: https://doc.qt.io/qt-6/qstyle.html#unpolish

    Parameters
    ----------

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QStyle::unpolish(QWidget *widget)
    self.uglySide.call(
        'ritual_ZN6QStyle8unpolishEP7QWidget', self._addressOf(widget),
    )

  @overload(QApplication)
  def unpolish(self, application: Optional[QApplication]) -> None:
    """
    Calls Qt's 'void QStyle::unpolish(QApplication *application)'.

    Qt's own words: https://doc.qt.io/qt-6/qstyle.html#unpolish

    Parameters
    ----------

    application : Optional[QApplication]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QStyle::unpolish(QApplication *application)
    self.uglySide.call(
        'ritual_ZN6QStyle8unpolishEP12QApplication',
        self._addressOf(application),
    )

  @overload(QPainter, QRect, int, QPalette, bool, str)
  @overload(NoneType, QRect, int, QPalette, bool, str)
  @overload(QPainter, QRect, int, QPalette, bool, str, QPaletteColorRole)
  @overload(NoneType, QRect, int, QPalette, bool, str, QPaletteColorRole)
  def drawItemText(
      self,
      painter: Optional[QPainter],
      rect: QRect,
      flags: int,
      pal: QPalette,
      enabled: bool,
      text: str,
      textRole: QPalette.ColorRole = QPaletteColorRole.NoRole,
  ) -> None:
    """
    Calls Qt's 'void QStyle::drawItemText(QPainter *painter, const QRect
    &rect, int flags, const QPalette &pal, bool enabled, const QString &text,
    QPalette::ColorRole textRole) const'.

    Qt's own words: https://doc.qt.io/qt-6/qstyle.html#drawItemText

    Parameters
    ----------

    painter : Optional[QPainter]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    rect : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.

    flags : int
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
      QPaletteColorRole.NoRole.
    """
    #  void QStyle::drawItemText(QPainter *painter, const QRect &rect, int
    #      flags, const QPalette &pal, bool enabled, const QString &text,
    #      QPalette::ColorRole textRole) const
    self.uglySide.call(
        'ritual_ZNK6QStyle12drawItemTextEP8QPainterRK5QRectiRK8QPalettebRK7'
        'QStringNS5_9ColorRoleE',
        self._addressOf(painter), self._valueOf(rect), flags,
        self._valueOf(pal), enabled, text, textRole.value,
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
    Calls Qt's 'void QStyle::drawItemPixmap(QPainter *painter, const QRect
    &rect, int alignment, const QPixmap &pixmap) const'.

    Qt's own words: https://doc.qt.io/qt-6/qstyle.html#drawItemPixmap

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
    #  void QStyle::drawItemPixmap(QPainter *painter, const QRect &rect, int
    #      alignment, const QPixmap &pixmap) const
    self.uglySide.call(
        'ritual_ZNK6QStyle14drawItemPixmapEP8QPainterRK5QRectiRK7QPixmap',
        self._addressOf(painter), self._valueOf(rect), alignment,
        self._valueOf(pixmap),
    )

  @overload(PrimitiveElement, QStyleOption, QPainter)
  @overload(PrimitiveElement, QStyleOption, NoneType)
  @overload(PrimitiveElement, NoneType, QPainter)
  @overload(PrimitiveElement, NoneType, NoneType)
  @overload(PrimitiveElement, QStyleOption, QPainter, QWidget)
  @overload(PrimitiveElement, QStyleOption, QPainter, NoneType)
  @overload(PrimitiveElement, QStyleOption, NoneType, QWidget)
  @overload(PrimitiveElement, QStyleOption, NoneType, NoneType)
  @overload(PrimitiveElement, NoneType, QPainter, QWidget)
  @overload(PrimitiveElement, NoneType, QPainter, NoneType)
  @overload(PrimitiveElement, NoneType, NoneType, QWidget)
  @overload(PrimitiveElement, NoneType, NoneType, NoneType)
  def drawPrimitive(
      self,
      pe: PrimitiveElement,
      opt: Optional[QStyleOption],
      p: Optional[QPainter],
      w: Optional[QWidget] = None,
  ) -> None:
    """
    Calls Qt's 'void QStyle::drawPrimitive(PrimitiveElement pe, const
    QStyleOption *opt, QPainter *p, const QWidget *w) const'.

    Qt's own words: https://doc.qt.io/qt-6/qstyle.html#drawPrimitive

    Parameters
    ----------

    pe : PrimitiveElement
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
    #  void QStyle::drawPrimitive(PrimitiveElement pe, const QStyleOption
    #      *opt, QPainter *p, const QWidget *w) const
    self.uglySide.call(
        'ritual_ZNK6QStyle13drawPrimitiveENS_16PrimitiveElementEPK12QStyleO'
        'ptionP8QPainterPK7QWidget',
        pe.value, self._addressOf(opt), self._addressOf(p),
        self._addressOf(w),
    )

  @overload(ControlElement, QStyleOption, QPainter)
  @overload(ControlElement, QStyleOption, NoneType)
  @overload(ControlElement, NoneType, QPainter)
  @overload(ControlElement, NoneType, NoneType)
  @overload(ControlElement, QStyleOption, QPainter, QWidget)
  @overload(ControlElement, QStyleOption, QPainter, NoneType)
  @overload(ControlElement, QStyleOption, NoneType, QWidget)
  @overload(ControlElement, QStyleOption, NoneType, NoneType)
  @overload(ControlElement, NoneType, QPainter, QWidget)
  @overload(ControlElement, NoneType, QPainter, NoneType)
  @overload(ControlElement, NoneType, NoneType, QWidget)
  @overload(ControlElement, NoneType, NoneType, NoneType)
  def drawControl(
      self,
      element: ControlElement,
      opt: Optional[QStyleOption],
      p: Optional[QPainter],
      w: Optional[QWidget] = None,
  ) -> None:
    """
    Calls Qt's 'void QStyle::drawControl(ControlElement element, const
    QStyleOption *opt, QPainter *p, const QWidget *w) const'.

    Qt's own words: https://doc.qt.io/qt-6/qstyle.html#drawControl

    Parameters
    ----------

    element : ControlElement
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
    #  void QStyle::drawControl(ControlElement element, const QStyleOption
    #      *opt, QPainter *p, const QWidget *w) const
    self.uglySide.call(
        'ritual_ZNK6QStyle11drawControlENS_14ControlElementEPK12QStyleOptio'
        'nP8QPainterPK7QWidget',
        element.value, self._addressOf(opt), self._addressOf(p),
        self._addressOf(w),
    )

  @overload(ComplexControl, QStyleOptionComplex, QPainter)
  @overload(ComplexControl, QStyleOptionComplex, NoneType)
  @overload(ComplexControl, NoneType, QPainter)
  @overload(ComplexControl, NoneType, NoneType)
  @overload(ComplexControl, QStyleOptionComplex, QPainter, QWidget)
  @overload(ComplexControl, QStyleOptionComplex, QPainter, NoneType)
  @overload(ComplexControl, QStyleOptionComplex, NoneType, QWidget)
  @overload(ComplexControl, QStyleOptionComplex, NoneType, NoneType)
  @overload(ComplexControl, NoneType, QPainter, QWidget)
  @overload(ComplexControl, NoneType, QPainter, NoneType)
  @overload(ComplexControl, NoneType, NoneType, QWidget)
  @overload(ComplexControl, NoneType, NoneType, NoneType)
  def drawComplexControl(
      self,
      cc: ComplexControl,
      opt: Optional[QStyleOptionComplex],
      p: Optional[QPainter],
      widget: Optional[QWidget] = None,
  ) -> None:
    """
    Calls Qt's 'void QStyle::drawComplexControl(ComplexControl cc, const
    QStyleOptionComplex *opt, QPainter *p, const QWidget *widget) const'.

    Qt's own words: https://doc.qt.io/qt-6/qstyle.html#drawComplexControl

    Parameters
    ----------

    cc : ComplexControl
      Passed on as its number.

    opt : Optional[QStyleOptionComplex]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    p : Optional[QPainter]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  void QStyle::drawComplexControl(ComplexControl cc, const
    #      QStyleOptionComplex *opt, QPainter *p, const QWidget *widget)
    #      const
    self.uglySide.call(
        'ritual_ZNK6QStyle18drawComplexControlENS_14ComplexControlEPK19QSty'
        'leOptionComplexP8QPainterPK7QWidget',
        cc.value, self._addressOf(opt), self._addressOf(p),
        self._addressOf(widget),
    )
