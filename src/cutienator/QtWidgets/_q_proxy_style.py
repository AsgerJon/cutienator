"""
QProxyStyle binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/qproxystyle.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import Qt
from ..QtGui import QIcon, QPalette
from . import QCommonStyle, QSizePolicy, QStyle

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QEvent, QMetaObject, QPoint, QRect, QSize
  from ..QtGui import QFontMetrics, QPainter, QPixmap
  from . import QApplication, QProxyStylePrivate, QStyleHintReturn
  from . import QStyleOption, QStyleOptionComplex, QWidget
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QApplication = WAIT['QApplication']
  QEvent = WAIT['QEvent']
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


class QProxyStyle(QCommonStyle):
  """
  The cute side of Qt's QProxyStyle: a plain Python object standing in front
  of one C++ QProxyStyle.

  It is built on the cute 'QCommonStyle', as Qt's QProxyStyle is built on
  Qt's QCommonStyle, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QProxyStyle that has a ritual and that Python can
  call so far, 26 names in all: 'metaObject', 'tr', 'baseStyle',
  'setBaseStyle', 'drawPrimitive', 'drawControl', 'drawComplexControl',
  'drawItemText', 'drawItemPixmap', 'sizeFromContents', 'subElementRect',
  'subControlRect', 'itemTextRect', 'itemPixmapRect',
  'hitTestComplexControl', 'styleHint', 'pixelMetric', 'layoutSpacing',
  'standardIcon', 'standardPixmap', 'generatedIconPixmap', 'standardPalette',
  'polish', 'unpolish', 'event', 'd_func'. It can be made from Python, in 2
  ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QProxyStyle::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QProxyStyle::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QProxyStyle::~QProxyStyle()': the destructor: Python never removes
    a C++ QProxyStyle.
  - Qt's 'void QProxyStyle::polish(QPalette &pal)': takes a type Python has
    no way to hand over yet.
  - Qt's 'const QProxyStylePrivate *QProxyStyle::d_func() const': takes in
    Python what 'QProxyStylePrivate *QProxyStyle::d_func()' takes.

  What has no ritual
  ------------------

  4 of the 39 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QProxyStyle is created at the first use, not by
    'QProxyStyle(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QProxyStyle.
  - Qt tells when it has removed the C++ QProxyStyle. Every call on the cute
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
    Calls Qt's 'QString QProxyStyle::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qproxystyle.html#tr

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
    #  QString QProxyStyle::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN11QProxyStyle2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QProxyStyle'

  #  A C++ QProxyStyle Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QProxyStyle'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QProxyStyle::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qproxystyle.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QProxyStyle::metaObject() const
    address = self.uglySide.call('ritual_ZNK11QProxyStyle10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def baseStyle(self) -> Optional[QStyle]:
    """
    Calls Qt's 'QStyle *QProxyStyle::baseStyle() const'.

    Qt's own words: https://doc.qt.io/qt-6/qproxystyle.html#baseStyle

    Returns
    -------

    Optional[QStyle]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QStyle *QProxyStyle::baseStyle() const
    address = self.uglySide.call('ritual_ZNK11QProxyStyle9baseStyleEv')
    return QStyle._cuteAt(address)

  @overload(QStyle.ContentsType, QStyleOption, QSize, QWidget)
  @overload(QStyle.ContentsType, QStyleOption, QSize, NoneType)
  @overload(QStyle.ContentsType, NoneType, QSize, QWidget)
  @overload(QStyle.ContentsType, NoneType, QSize, NoneType)
  def sizeFromContents(
      self,
      type: QStyle.ContentsType,
      option: Optional[QStyleOption],
      size: QSize,
      widget: Optional[QWidget],
  ) -> QSize:
    """
    Calls Qt's 'QSize QProxyStyle::sizeFromContents(ContentsType type, const
    QStyleOption *option, const QSize &size, const QWidget *widget) const'.

    Qt's own words: https://doc.qt.io/qt-6/qproxystyle.html#sizeFromContents

    Parameters
    ----------

    type : QStyle.ContentsType
      Passed on as its number.

    option : Optional[QStyleOption]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    size : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QProxyStyle::sizeFromContents(ContentsType type, const
    #      QStyleOption *option, const QSize &size, const QWidget *widget)
    #      const
    ritual = (
        'ritual_ZNK11QProxyStyle16sizeFromContentsEN6QStyle12ContentsTypeEP'
        'K12QStyleOptionRK5QSizePK7QWidget')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK11QProxyStyle16sizeFromContentsEN6QStyle12Contents'
          'TypeEPK12QStyleOptionRK5QSizePK7QWidget')
    address = self.uglySide.call(
        ritual,
        type.value, self._addressOf(option), self._valueOf(size),
        self._addressOf(widget),
    )
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  @overload(QStyle.SubElement, QStyleOption, QWidget)
  @overload(QStyle.SubElement, QStyleOption, NoneType)
  @overload(QStyle.SubElement, NoneType, QWidget)
  @overload(QStyle.SubElement, NoneType, NoneType)
  def subElementRect(
      self,
      element: QStyle.SubElement,
      option: Optional[QStyleOption],
      widget: Optional[QWidget],
  ) -> QRect:
    """
    Calls Qt's 'QRect QProxyStyle::subElementRect(SubElement element, const
    QStyleOption *option, const QWidget *widget) const'.

    Qt's own words: https://doc.qt.io/qt-6/qproxystyle.html#subElementRect

    Parameters
    ----------

    element : QStyle.SubElement
      Passed on as its number.

    option : Optional[QStyleOption]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect QProxyStyle::subElementRect(SubElement element, const
    #      QStyleOption *option, const QWidget *widget) const
    ritual = (
        'ritual_ZNK11QProxyStyle14subElementRectEN6QStyle10SubElementEPK12Q'
        'StyleOptionPK7QWidget')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK11QProxyStyle14subElementRectEN6QStyle10SubElement'
          'EPK12QStyleOptionPK7QWidget')
    address = self.uglySide.call(
        ritual,
        element.value, self._addressOf(option), self._addressOf(widget),
    )
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

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
      widget: Optional[QWidget],
  ) -> QRect:
    """
    Calls Qt's 'QRect QProxyStyle::subControlRect(ComplexControl cc, const
    QStyleOptionComplex *opt, SubControl sc, const QWidget *widget) const'.

    Qt's own words: https://doc.qt.io/qt-6/qproxystyle.html#subControlRect

    Parameters
    ----------

    cc : QStyle.ComplexControl
      Passed on as its number.

    opt : Optional[QStyleOptionComplex]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    sc : QStyle.SubControl
      Passed on as its number.

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect QProxyStyle::subControlRect(ComplexControl cc, const
    #      QStyleOptionComplex *opt, SubControl sc, const QWidget *widget)
    #      const
    ritual = (
        'ritual_ZNK11QProxyStyle14subControlRectEN6QStyle14ComplexControlEP'
        'K19QStyleOptionComplexNS0_10SubControlEPK7QWidget')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK11QProxyStyle14subControlRectEN6QStyle14ComplexCon'
          'trolEPK19QStyleOptionComplexNS0_10SubControlEPK7QWidget')
    address = self.uglySide.call(
        ritual,
        cc.value, self._addressOf(opt), sc.value, self._addressOf(widget),
    )
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

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
    Calls Qt's 'QRect QProxyStyle::itemTextRect(const QFontMetrics &fm, const
    QRect &r, int flags, bool enabled, const QString &text) const'.

    Qt's own words: https://doc.qt.io/qt-6/qproxystyle.html#itemTextRect

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
    #  QRect QProxyStyle::itemTextRect(const QFontMetrics &fm, const QRect
    #      &r, int flags, bool enabled, const QString &text) const
    ritual = (
        'ritual_ZNK11QProxyStyle12itemTextRectERK12QFontMetricsRK5QRectibRK'
        '7QString')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK11QProxyStyle12itemTextRectERK12QFontMetricsRK5QRe'
          'ctibRK7QString')
    address = self.uglySide.call(
        ritual, self._valueOf(fm), self._valueOf(r), flags, enabled, text,
    )
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

  @overload(QRect, int, QPixmap)
  def itemPixmapRect(self, r: QRect, flags: int, pixmap: QPixmap) -> QRect:
    """
    Calls Qt's 'QRect QProxyStyle::itemPixmapRect(const QRect &r, int flags,
    const QPixmap &pixmap) const'.

    Qt's own words: https://doc.qt.io/qt-6/qproxystyle.html#itemPixmapRect

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
    #  QRect QProxyStyle::itemPixmapRect(const QRect &r, int flags, const
    #      QPixmap &pixmap) const
    ritual = 'ritual_ZNK11QProxyStyle14itemPixmapRectERK5QRectiRK7QPixmap'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK11QProxyStyle14itemPixmapRectERK5QRectiRK7QPixmap')
    address = self.uglySide.call(
        ritual, self._valueOf(r), flags, self._valueOf(pixmap),
    )
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

  @overload(QStyle.ComplexControl, QStyleOptionComplex, QPoint)
  @overload(QStyle.ComplexControl, NoneType, QPoint)
  @overload(QStyle.ComplexControl, QStyleOptionComplex, QPoint, QWidget)
  @overload(QStyle.ComplexControl, QStyleOptionComplex, QPoint, NoneType)
  @overload(QStyle.ComplexControl, NoneType, QPoint, QWidget)
  @overload(QStyle.ComplexControl, NoneType, QPoint, NoneType)
  def hitTestComplexControl(
      self,
      control: QStyle.ComplexControl,
      option: Optional[QStyleOptionComplex],
      pos: QPoint,
      widget: Optional[QWidget] = None,
  ) -> QStyle.SubControl:
    """
    Calls Qt's 'SubControl QProxyStyle::hitTestComplexControl(ComplexControl
    control, const QStyleOptionComplex *option, const QPoint &pos, const
    QWidget *widget) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qproxystyle.html#hitTestComplexControl

    Parameters
    ----------

    control : QStyle.ComplexControl
      Passed on as its number.

    option : Optional[QStyleOptionComplex]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    pos : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    Returns
    -------

    QStyle.SubControl
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QStyle.SubControl(number)' gives.
    """
    #  SubControl QProxyStyle::hitTestComplexControl(ComplexControl control,
    #      const QStyleOptionComplex *option, const QPoint &pos, const
    #      QWidget *widget) const
    ritual = (
        'ritual_ZNK11QProxyStyle21hitTestComplexControlEN6QStyle14ComplexCo'
        'ntrolEPK19QStyleOptionComplexRK6QPointPK7QWidget')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK11QProxyStyle21hitTestComplexControlEN6QStyle14Com'
          'plexControlEPK19QStyleOptionComplexRK6QPointPK7QWidget')
    return QStyle.SubControl(self.uglySide.call(
        ritual,
        control.value, self._addressOf(option), self._valueOf(pos),
        self._addressOf(widget),
    ))

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
      hint: QStyle.StyleHint,
      option: Optional[QStyleOption] = None,
      widget: Optional[QWidget] = None,
      returnData: Optional[QStyleHintReturn] = None,
  ) -> int:
    """
    Calls Qt's 'int QProxyStyle::styleHint(StyleHint hint, const QStyleOption
    *option, const QWidget *widget, QStyleHintReturn *returnData) const'.

    Qt's own words: https://doc.qt.io/qt-6/qproxystyle.html#styleHint

    Parameters
    ----------

    hint : QStyle.StyleHint
      Passed on as its number.

    option : Optional[QStyleOption]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    returnData : Optional[QStyleHintReturn]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  int QProxyStyle::styleHint(StyleHint hint, const QStyleOption *option,
    #      const QWidget *widget, QStyleHintReturn *returnData) const
    ritual = (
        'ritual_ZNK11QProxyStyle9styleHintEN6QStyle9StyleHintEPK12QStyleOpt'
        'ionPK7QWidgetP16QStyleHintReturn')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK11QProxyStyle9styleHintEN6QStyle9StyleHintEPK12QSt'
          'yleOptionPK7QWidgetP16QStyleHintReturn')
    return self.uglySide.call(
        ritual,
        hint.value, self._addressOf(option), self._addressOf(widget),
        self._addressOf(returnData),
    )

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
    Calls Qt's 'int QProxyStyle::pixelMetric(PixelMetric metric, const
    QStyleOption *option, const QWidget *widget) const'.

    Qt's own words: https://doc.qt.io/qt-6/qproxystyle.html#pixelMetric

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
    #  int QProxyStyle::pixelMetric(PixelMetric metric, const QStyleOption
    #      *option, const QWidget *widget) const
    ritual = (
        'ritual_ZNK11QProxyStyle11pixelMetricEN6QStyle11PixelMetricEPK12QSt'
        'yleOptionPK7QWidget')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK11QProxyStyle11pixelMetricEN6QStyle11PixelMetricEP'
          'K12QStyleOptionPK7QWidget')
    return self.uglySide.call(
        ritual,
        metric.value, self._addressOf(option), self._addressOf(widget),
    )

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
    Calls Qt's 'int QProxyStyle::layoutSpacing(QSizePolicy::ControlType
    control1, QSizePolicy::ControlType control2, Qt::Orientation orientation,
    const QStyleOption *option, const QWidget *widget) const'.

    Qt's own words: https://doc.qt.io/qt-6/qproxystyle.html#layoutSpacing

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
    #  int QProxyStyle::layoutSpacing(QSizePolicy::ControlType control1,
    #      QSizePolicy::ControlType control2, Qt::Orientation orientation,
    #      const QStyleOption *option, const QWidget *widget) const
    ritual = (
        'ritual_ZNK11QProxyStyle13layoutSpacingEN11QSizePolicy11ControlType'
        'ES1_N2Qt11OrientationEPK12QStyleOptionPK7QWidget')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK11QProxyStyle13layoutSpacingEN11QSizePolicy11Contr'
          'olTypeES1_N2Qt11OrientationEPK12QStyleOptionPK7QWidget')
    return self.uglySide.call(
        ritual,
        control1.value, control2.value, orientation.value,
        self._addressOf(option), self._addressOf(widget),
    )

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
      option: Optional[QStyleOption] = None,
      widget: Optional[QWidget] = None,
  ) -> QIcon:
    """
    Calls Qt's 'QIcon QProxyStyle::standardIcon(StandardPixmap standardIcon,
    const QStyleOption *option, const QWidget *widget) const'.

    Qt's own words: https://doc.qt.io/qt-6/qproxystyle.html#standardIcon

    Parameters
    ----------

    standardIcon : QStyle.StandardPixmap
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
    #  QIcon QProxyStyle::standardIcon(StandardPixmap standardIcon, const
    #      QStyleOption *option, const QWidget *widget) const
    ritual = (
        'ritual_ZNK11QProxyStyle12standardIconEN6QStyle14StandardPixmapEPK1'
        '2QStyleOptionPK7QWidget')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK11QProxyStyle12standardIconEN6QStyle14StandardPixm'
          'apEPK12QStyleOptionPK7QWidget')
    address = self.uglySide.call(
        ritual,
        standardIcon.value, self._addressOf(option), self._addressOf(widget),
    )
    return QIcon._cuteOwning(address)

  @overload(QStyle.StandardPixmap, QStyleOption)
  @overload(QStyle.StandardPixmap, NoneType)
  @overload(QStyle.StandardPixmap, QStyleOption, QWidget)
  @overload(QStyle.StandardPixmap, QStyleOption, NoneType)
  @overload(QStyle.StandardPixmap, NoneType, QWidget)
  @overload(QStyle.StandardPixmap, NoneType, NoneType)
  def standardPixmap(
      self,
      standardPixmap: QStyle.StandardPixmap,
      opt: Optional[QStyleOption],
      widget: Optional[QWidget] = None,
  ) -> QPixmap:
    """
    Calls Qt's 'QPixmap QProxyStyle::standardPixmap(StandardPixmap
    standardPixmap, const QStyleOption *opt, const QWidget *widget) const'.

    Qt's own words: https://doc.qt.io/qt-6/qproxystyle.html#standardPixmap

    Parameters
    ----------

    standardPixmap : QStyle.StandardPixmap
      Passed on as its number.

    opt : Optional[QStyleOption]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    Returns
    -------

    QPixmap
      A new cute QPixmap around the copy Qt gave back. Python owns it.
    """
    #  QPixmap QProxyStyle::standardPixmap(StandardPixmap standardPixmap,
    #      const QStyleOption *opt, const QWidget *widget) const
    ritual = (
        'ritual_ZNK11QProxyStyle14standardPixmapEN6QStyle14StandardPixmapEP'
        'K12QStyleOptionPK7QWidget')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK11QProxyStyle14standardPixmapEN6QStyle14StandardPi'
          'xmapEPK12QStyleOptionPK7QWidget')
    address = self.uglySide.call(
        ritual,
        standardPixmap.value, self._addressOf(opt), self._addressOf(widget),
    )
    from ..QtGui import QPixmap
    return QPixmap._cuteOwning(address)

  @overload(QIcon.Mode, QPixmap, QStyleOption)
  @overload(QIcon.Mode, QPixmap, NoneType)
  def generatedIconPixmap(
      self,
      iconMode: QIcon.Mode,
      pixmap: QPixmap,
      opt: Optional[QStyleOption],
  ) -> QPixmap:
    """
    Calls Qt's 'QPixmap QProxyStyle::generatedIconPixmap(QIcon::Mode
    iconMode, const QPixmap &pixmap, const QStyleOption *opt) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qproxystyle.html#generatedIconPixmap

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
    #  QPixmap QProxyStyle::generatedIconPixmap(QIcon::Mode iconMode, const
    #      QPixmap &pixmap, const QStyleOption *opt) const
    ritual = (
        'ritual_ZNK11QProxyStyle19generatedIconPixmapEN5QIcon4ModeERK7QPixm'
        'apPK12QStyleOption')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK11QProxyStyle19generatedIconPixmapEN5QIcon4ModeERK'
          '7QPixmapPK12QStyleOption')
    address = self.uglySide.call(
        ritual, iconMode.value, self._valueOf(pixmap), self._addressOf(opt),
    )
    from ..QtGui import QPixmap
    return QPixmap._cuteOwning(address)

  def standardPalette(self) -> QPalette:
    """
    Calls Qt's 'QPalette QProxyStyle::standardPalette() const'.

    Qt's own words: https://doc.qt.io/qt-6/qproxystyle.html#standardPalette

    Returns
    -------

    QPalette
      A new cute QPalette around the copy Qt gave back. Python owns it.
    """
    #  QPalette QProxyStyle::standardPalette() const
    ritual = 'ritual_ZNK11QProxyStyle15standardPaletteEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK11QProxyStyle15standardPaletteEv'
    address = self.uglySide.call(ritual)
    return QPalette._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QStyle)
  @overload(NoneType)
  def setBaseStyle(self, style: Optional[QStyle]) -> None:
    """
    Calls Qt's 'void QProxyStyle::setBaseStyle(QStyle *style)'.

    Qt's own words: https://doc.qt.io/qt-6/qproxystyle.html#setBaseStyle

    Parameters
    ----------

    style : Optional[QStyle]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QProxyStyle::setBaseStyle(QStyle *style)
    self.uglySide.call(
        'ritual_ZN11QProxyStyle12setBaseStyleEP6QStyle',
        self._addressOf(style),
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
  @overload(QStyle)
  @overload(NoneType)
  def __init__(self, style: Optional[QStyle] = None) -> None:
    """
    Notes what was given, for Qt's 'QProxyStyle::QProxyStyle(QStyle *style)',
    which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qproxystyle.html#QProxyStyle

    Parameters
    ----------

    style : Optional[QStyle]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QProxyStyle::QProxyStyle(QStyle *style)
    self._noteCreation(QProxyStyle, lambda: Rituals.call(
        'ritual_ZN11QProxyStyleC1EP6QStyle', self._addressOf(style),
    ))

  @overload(str)
  def __init__(self, key: str) -> None:
    """
    Notes what was given, for Qt's 'QProxyStyle::QProxyStyle(const QString
    &key)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qproxystyle.html#QProxyStyle

    Parameters
    ----------

    key : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  QProxyStyle::QProxyStyle(const QString &key)
    self._noteCreation(QProxyStyle, lambda: Rituals.call(
        'ritual_ZN11QProxyStyleC1ERK7QString', key,
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
      element: QStyle.PrimitiveElement,
      option: Optional[QStyleOption],
      painter: Optional[QPainter],
      widget: Optional[QWidget] = None,
  ) -> None:
    """
    Calls Qt's 'void QProxyStyle::drawPrimitive(PrimitiveElement element,
    const QStyleOption *option, QPainter *painter, const QWidget *widget)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qproxystyle.html#drawPrimitive

    Parameters
    ----------

    element : QStyle.PrimitiveElement
      Passed on as its number.

    option : Optional[QStyleOption]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    painter : Optional[QPainter]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  void QProxyStyle::drawPrimitive(PrimitiveElement element, const
    #      QStyleOption *option, QPainter *painter, const QWidget *widget)
    #      const
    ritual = (
        'ritual_ZNK11QProxyStyle13drawPrimitiveEN6QStyle16PrimitiveElementE'
        'PK12QStyleOptionP8QPainterPK7QWidget')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK11QProxyStyle13drawPrimitiveEN6QStyle16PrimitiveEl'
          'ementEPK12QStyleOptionP8QPainterPK7QWidget')
    self.uglySide.call(
        ritual,
        element.value, self._addressOf(option), self._addressOf(painter),
        self._addressOf(widget),
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
      option: Optional[QStyleOption],
      painter: Optional[QPainter],
      widget: Optional[QWidget] = None,
  ) -> None:
    """
    Calls Qt's 'void QProxyStyle::drawControl(ControlElement element, const
    QStyleOption *option, QPainter *painter, const QWidget *widget) const'.

    Qt's own words: https://doc.qt.io/qt-6/qproxystyle.html#drawControl

    Parameters
    ----------

    element : QStyle.ControlElement
      Passed on as its number.

    option : Optional[QStyleOption]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    painter : Optional[QPainter]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  void QProxyStyle::drawControl(ControlElement element, const
    #      QStyleOption *option, QPainter *painter, const QWidget *widget)
    #      const
    ritual = (
        'ritual_ZNK11QProxyStyle11drawControlEN6QStyle14ControlElementEPK12'
        'QStyleOptionP8QPainterPK7QWidget')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK11QProxyStyle11drawControlEN6QStyle14ControlElemen'
          'tEPK12QStyleOptionP8QPainterPK7QWidget')
    self.uglySide.call(
        ritual,
        element.value, self._addressOf(option), self._addressOf(painter),
        self._addressOf(widget),
    )

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
      control: QStyle.ComplexControl,
      option: Optional[QStyleOptionComplex],
      painter: Optional[QPainter],
      widget: Optional[QWidget] = None,
  ) -> None:
    """
    Calls Qt's 'void QProxyStyle::drawComplexControl(ComplexControl control,
    const QStyleOptionComplex *option, QPainter *painter, const QWidget
    *widget) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qproxystyle.html#drawComplexControl

    Parameters
    ----------

    control : QStyle.ComplexControl
      Passed on as its number.

    option : Optional[QStyleOptionComplex]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    painter : Optional[QPainter]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  void QProxyStyle::drawComplexControl(ComplexControl control, const
    #      QStyleOptionComplex *option, QPainter *painter, const QWidget
    #      *widget) const
    ritual = (
        'ritual_ZNK11QProxyStyle18drawComplexControlEN6QStyle14ComplexContr'
        'olEPK19QStyleOptionComplexP8QPainterPK7QWidget')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK11QProxyStyle18drawComplexControlEN6QStyle14Comple'
          'xControlEPK19QStyleOptionComplexP8QPainterPK7QWidget')
    self.uglySide.call(
        ritual,
        control.value, self._addressOf(option), self._addressOf(painter),
        self._addressOf(widget),
    )

  @overload(QPainter, QRect, int, QPalette, bool, str)
  @overload(NoneType, QRect, int, QPalette, bool, str)
  @overload(QPainter, QRect, int, QPalette, bool, str, QPalette.ColorRole)
  @overload(NoneType, QRect, int, QPalette, bool, str, QPalette.ColorRole)
  def drawItemText(
      self,
      painter: Optional[QPainter],
      rect: QRect,
      flags: int,
      pal: QPalette,
      enabled: bool,
      text: str,
      textRole: QPalette.ColorRole = QPalette.ColorRole.NoRole,
  ) -> None:
    """
    Calls Qt's 'void QProxyStyle::drawItemText(QPainter *painter, const QRect
    &rect, int flags, const QPalette &pal, bool enabled, const QString &text,
    QPalette::ColorRole textRole) const'.

    Qt's own words: https://doc.qt.io/qt-6/qproxystyle.html#drawItemText

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
      QPalette.ColorRole.NoRole.
    """
    #  void QProxyStyle::drawItemText(QPainter *painter, const QRect &rect,
    #      int flags, const QPalette &pal, bool enabled, const QString &text,
    #      QPalette::ColorRole textRole) const
    ritual = (
        'ritual_ZNK11QProxyStyle12drawItemTextEP8QPainterRK5QRectiRK8QPalet'
        'tebRK7QStringNS5_9ColorRoleE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK11QProxyStyle12drawItemTextEP8QPainterRK5QRectiRK8'
          'QPalettebRK7QStringNS5_9ColorRoleE')
    self.uglySide.call(
        ritual,
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
    Calls Qt's 'void QProxyStyle::drawItemPixmap(QPainter *painter, const
    QRect &rect, int alignment, const QPixmap &pixmap) const'.

    Qt's own words: https://doc.qt.io/qt-6/qproxystyle.html#drawItemPixmap

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
    #  void QProxyStyle::drawItemPixmap(QPainter *painter, const QRect &rect,
    #      int alignment, const QPixmap &pixmap) const
    ritual = (
        'ritual_ZNK11QProxyStyle14drawItemPixmapEP8QPainterRK5QRectiRK7QPix'
        'map')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK11QProxyStyle14drawItemPixmapEP8QPainterRK5QRectiR'
          'K7QPixmap')
    self.uglySide.call(
        ritual,
        self._addressOf(painter), self._valueOf(rect), alignment,
        self._valueOf(pixmap),
    )

  @overload(QWidget)
  @overload(NoneType)
  def polish(self, widget: Optional[QWidget]) -> None:
    """
    Calls Qt's 'void QProxyStyle::polish(QWidget *widget)'.

    Qt's own words: https://doc.qt.io/qt-6/qproxystyle.html#polish

    Parameters
    ----------

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QProxyStyle::polish(QWidget *widget)
    ritual = 'ritual_ZN11QProxyStyle6polishEP7QWidget'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN11QProxyStyle6polishEP7QWidget'
    self.uglySide.call(ritual, self._addressOf(widget))

  @overload(QApplication)
  def polish(self, app: Optional[QApplication]) -> None:
    """
    Calls Qt's 'void QProxyStyle::polish(QApplication *app)'.

    Qt's own words: https://doc.qt.io/qt-6/qproxystyle.html#polish

    Parameters
    ----------

    app : Optional[QApplication]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QProxyStyle::polish(QApplication *app)
    ritual = 'ritual_ZN11QProxyStyle6polishEP12QApplication'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN11QProxyStyle6polishEP12QApplication'
    self.uglySide.call(ritual, self._addressOf(app))

  @overload(QWidget)
  @overload(NoneType)
  def unpolish(self, widget: Optional[QWidget]) -> None:
    """
    Calls Qt's 'void QProxyStyle::unpolish(QWidget *widget)'.

    Qt's own words: https://doc.qt.io/qt-6/qproxystyle.html#unpolish

    Parameters
    ----------

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QProxyStyle::unpolish(QWidget *widget)
    ritual = 'ritual_ZN11QProxyStyle8unpolishEP7QWidget'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN11QProxyStyle8unpolishEP7QWidget'
    self.uglySide.call(ritual, self._addressOf(widget))

  @overload(QApplication)
  def unpolish(self, app: Optional[QApplication]) -> None:
    """
    Calls Qt's 'void QProxyStyle::unpolish(QApplication *app)'.

    Qt's own words: https://doc.qt.io/qt-6/qproxystyle.html#unpolish

    Parameters
    ----------

    app : Optional[QApplication]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QProxyStyle::unpolish(QApplication *app)
    ritual = 'ritual_ZN11QProxyStyle8unpolishEP12QApplication'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN11QProxyStyle8unpolishEP12QApplication'
    self.uglySide.call(ritual, self._addressOf(app))

  @overload(QEvent)
  @overload(NoneType)
  def event(self, e: Optional[QEvent]) -> bool:
    """
    Calls Qt's 'bool QProxyStyle::event(QEvent *e)'.

    Qt's own words: https://doc.qt.io/qt-6/qproxystyle.html#event

    Parameters
    ----------

    e : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QProxyStyle::event(QEvent *e)
    ritual = 'ritual_ZN11QProxyStyle5eventEP6QEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN11QProxyStyle5eventEP6QEvent'
    return self.uglySide.call(ritual, self._addressOf(e))

  def d_func(self) -> Optional[QProxyStylePrivate]:
    """
    Calls Qt's 'QProxyStylePrivate *QProxyStyle::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qproxystyle.html#d_func

    Returns
    -------

    Optional[QProxyStylePrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QProxyStylePrivate *QProxyStyle::d_func()
    address = self.uglySide.call('ritual_ZN11QProxyStyle6d_funcEv')
    from . import QProxyStylePrivate
    return QProxyStylePrivate._cuteAt(address)
