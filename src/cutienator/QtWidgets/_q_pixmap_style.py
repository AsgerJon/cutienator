"""
QPixmapStyle binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/6.12.0/QtWidgets/private/qpixmapstyle_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QPixmapStyle to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import Qt, QObject
from . import QCommonStyle, QStyle

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QEvent, QMargins, QMetaObject, QPoint, QRect, QSize
  from ..QtGui import QPainter
  from . import QApplication, QPixmapStylePrivate, QStyleHintReturn
  from . import QStyleOption, QStyleOptionComplex, QTileRules, QWidget
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QApplication = WAIT['QApplication']
  QEvent = WAIT['QEvent']
  QMargins = WAIT['QMargins']
  QPainter = WAIT['QPainter']
  QPoint = WAIT['QPoint']
  QRect = WAIT['QRect']
  QSize = WAIT['QSize']
  QStyleHintReturn = WAIT['QStyleHintReturn']
  QStyleOption = WAIT['QStyleOption']
  QStyleOptionComplex = WAIT['QStyleOptionComplex']
  QTileRules = WAIT['QTileRules']
  QWidget = WAIT['QWidget']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QPixmapStyle(QCommonStyle):
  """
  The cute side of Qt's QPixmapStyle: a plain Python object standing in front
  of one C++ QPixmapStyle.

  It is built on the cute 'QCommonStyle', as Qt's QPixmapStyle is built on
  Qt's QCommonStyle, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QPixmapStyle that has a ritual and that Python can
  call so far, 38 names in all: 'metaObject', 'tr', 'polish', 'unpolish',
  'drawPrimitive', 'drawControl', 'drawComplexControl', 'sizeFromContents',
  'subElementRect', 'subControlRect', 'pixelMetric', 'styleHint',
  'hitTestComplexControl', 'eventFilter', 'addDescriptor', 'copyDescriptor',
  'drawCachedPixmap', 'addPixmap', 'copyPixmap', 'drawPushButton',
  'drawLineEdit', 'drawTextEdit', 'drawCheckBox', 'drawRadioButton',
  'drawPanelItemViewItem', 'drawProgressBarBackground',
  'drawProgressBarLabel', 'drawProgressBarFill', 'drawSlider',
  'drawComboBox', 'drawScrollBar', 'pushButtonSizeFromContents',
  'lineEditSizeFromContents', 'progressBarSizeFromContents',
  'sliderSizeFromContents', 'comboBoxSizeFromContents',
  'itemViewSizeFromContents', 'd_func'. It can be made from Python, in 1 way;
  see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QPixmapStyle::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QPixmapStyle::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QPixmapStyle::~QPixmapStyle()': the destructor: Python never
    removes a C++ QPixmapStyle.
  - Qt's 'void QPixmapStyle::polish(QPalette &palette)': takes a type Python
    has no way to hand over yet.
  - Qt's 'QRect QPixmapStyle::comboBoxSubControlRect(const
    QStyleOptionComplex *option, QPixmapStyle::SubControl sc, const QWidget
    *widget) const': takes a type Python has no way to hand over yet.
  - Qt's 'QRect QPixmapStyle::scrollBarSubControlRect(const
    QStyleOptionComplex *option, QPixmapStyle::SubControl sc, const QWidget
    *widget) const': takes a type Python has no way to hand over yet.
  - Qt's 'QPixmapStyle::QPixmapStyle(QPixmapStylePrivate &dd)': takes a type
    Python has no way to hand over yet.
  - Qt's 'const QPixmapStylePrivate *QPixmapStyle::d_func() const': takes in
    Python what 'QPixmapStylePrivate *QPixmapStyle::d_func()' takes.

  What has no ritual
  ------------------

  2 of the 51 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QPixmapStyle is created at the first use, not by
    'QPixmapStyle(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QPixmapStyle.
  - Qt tells when it has removed the C++ QPixmapStyle. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
  - Each name of Qt's QPixmapStyle that has no cute function yet,
    'comboBoxSubControlRect', 'scrollBarSubControlRect', holds a function
    that raises 'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QPixmapStyle, each a class in here as in C++,
  #  and the names Qt has for the combinations of its flags enums.

  class ControlDescriptor(CuteNum):
    """
    The enum 'QPixmapStyle::ControlDescriptor' of Qt, with the 37 names Qt
    gives in it.
    """

    BG_Background = Kee[int](0)
    LE_Enabled = Kee[int](1)
    LE_Disabled = Kee[int](2)
    LE_Focused = Kee[int](3)
    PB_Enabled = Kee[int](4)
    PB_Pressed = Kee[int](5)
    PB_PressedDisabled = Kee[int](6)
    PB_Checked = Kee[int](7)
    PB_Disabled = Kee[int](8)
    TE_Enabled = Kee[int](9)
    TE_Disabled = Kee[int](10)
    TE_Focused = Kee[int](11)
    PB_HBackground = Kee[int](12)
    PB_HContent = Kee[int](13)
    PB_HComplete = Kee[int](14)
    PB_VBackground = Kee[int](15)
    PB_VContent = Kee[int](16)
    PB_VComplete = Kee[int](17)
    SG_HEnabled = Kee[int](18)
    SG_HDisabled = Kee[int](19)
    SG_HActiveEnabled = Kee[int](20)
    SG_HActivePressed = Kee[int](21)
    SG_HActiveDisabled = Kee[int](22)
    SG_VEnabled = Kee[int](23)
    SG_VDisabled = Kee[int](24)
    SG_VActiveEnabled = Kee[int](25)
    SG_VActivePressed = Kee[int](26)
    SG_VActiveDisabled = Kee[int](27)
    DD_ButtonEnabled = Kee[int](28)
    DD_ButtonDisabled = Kee[int](29)
    DD_ButtonPressed = Kee[int](30)
    DD_PopupDown = Kee[int](31)
    DD_PopupUp = Kee[int](32)
    DD_ItemSelected = Kee[int](33)
    ID_Selected = Kee[int](34)
    SB_Horizontal = Kee[int](35)
    SB_Vertical = Kee[int](36)

  class ControlPixmap(CuteNum):
    """
    The enum 'QPixmapStyle::ControlPixmap' of Qt, with the 23 names Qt gives
    in it.
    """

    CB_Enabled = Kee[int](0)
    CB_Checked = Kee[int](1)
    CB_Pressed = Kee[int](2)
    CB_PressedChecked = Kee[int](3)
    CB_Disabled = Kee[int](4)
    CB_DisabledChecked = Kee[int](5)
    RB_Enabled = Kee[int](6)
    RB_Checked = Kee[int](7)
    RB_Pressed = Kee[int](8)
    RB_Disabled = Kee[int](9)
    RB_DisabledChecked = Kee[int](10)
    SH_HEnabled = Kee[int](11)
    SH_HDisabled = Kee[int](12)
    SH_HPressed = Kee[int](13)
    SH_VEnabled = Kee[int](14)
    SH_VDisabled = Kee[int](15)
    SH_VPressed = Kee[int](16)
    DD_ArrowEnabled = Kee[int](17)
    DD_ArrowDisabled = Kee[int](18)
    DD_ArrowPressed = Kee[int](19)
    DD_ArrowOpen = Kee[int](20)
    DD_ItemSeparator = Kee[int](21)
    ID_Separator = Kee[int](22)

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
    Calls Qt's 'QString QPixmapStyle::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qpixmapstyle.html#tr

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
    #  QString QPixmapStyle::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN12QPixmapStyle2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QPixmapStyle'

  #  A C++ QPixmapStyle Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QPixmapStyle'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QPixmapStyle::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpixmapstyle.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QPixmapStyle::metaObject() const
    address = self.uglySide.call('ritual_ZNK12QPixmapStyle10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  @overload(QStyle.ContentsType, QStyleOption, QSize)
  @overload(QStyle.ContentsType, NoneType, QSize)
  @overload(QStyle.ContentsType, QStyleOption, QSize, QWidget)
  @overload(QStyle.ContentsType, QStyleOption, QSize, NoneType)
  @overload(QStyle.ContentsType, NoneType, QSize, QWidget)
  @overload(QStyle.ContentsType, NoneType, QSize, NoneType)
  def sizeFromContents(
      self,
      type: QStyle.ContentsType,
      option: Optional[QStyleOption],
      contentsSize: QSize,
      widget: Optional[QWidget] = None,
  ) -> QSize:
    """
    Calls Qt's 'QSize QPixmapStyle::sizeFromContents(ContentsType type, const
    QStyleOption *option, const QSize &contentsSize, const QWidget *widget)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qpixmapstyle.html#sizeFromContents

    Parameters
    ----------

    type : QStyle.ContentsType
      Passed on as its number.

    option : Optional[QStyleOption]
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
    #  QSize QPixmapStyle::sizeFromContents(ContentsType type, const
    #      QStyleOption *option, const QSize &contentsSize, const QWidget
    #      *widget) const
    ritual = (
        'ritual_ZNK12QPixmapStyle16sizeFromContentsEN6QStyle12ContentsTypeE'
        'PK12QStyleOptionRK5QSizePK7QWidget')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK12QPixmapStyle16sizeFromContentsEN6QStyle12Content'
          'sTypeEPK12QStyleOptionRK5QSizePK7QWidget')
    address = self.uglySide.call(
        ritual,
        type.value, self._addressOf(option), self._valueOf(contentsSize),
        self._addressOf(widget),
    )
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  @overload(QStyle.SubElement, QStyleOption)
  @overload(QStyle.SubElement, NoneType)
  @overload(QStyle.SubElement, QStyleOption, QWidget)
  @overload(QStyle.SubElement, QStyleOption, NoneType)
  @overload(QStyle.SubElement, NoneType, QWidget)
  @overload(QStyle.SubElement, NoneType, NoneType)
  def subElementRect(
      self,
      element: QStyle.SubElement,
      option: Optional[QStyleOption],
      widget: Optional[QWidget] = None,
  ) -> QRect:
    """
    Calls Qt's 'QRect QPixmapStyle::subElementRect(SubElement element, const
    QStyleOption *option, const QWidget *widget) const'.

    Qt's own words: https://doc.qt.io/qt-6/qpixmapstyle.html#subElementRect

    Parameters
    ----------

    element : QStyle.SubElement
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
    #  QRect QPixmapStyle::subElementRect(SubElement element, const
    #      QStyleOption *option, const QWidget *widget) const
    ritual = (
        'ritual_ZNK12QPixmapStyle14subElementRectEN6QStyle10SubElementEPK12'
        'QStyleOptionPK7QWidget')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK12QPixmapStyle14subElementRectEN6QStyle10SubElemen'
          'tEPK12QStyleOptionPK7QWidget')
    address = self.uglySide.call(
        ritual,
        element.value, self._addressOf(option), self._addressOf(widget),
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
      option: Optional[QStyleOptionComplex],
      sc: QStyle.SubControl,
      widget: Optional[QWidget] = None,
  ) -> QRect:
    """
    Calls Qt's 'QRect QPixmapStyle::subControlRect(ComplexControl cc, const
    QStyleOptionComplex *option, SubControl sc, const QWidget *widget)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qpixmapstyle.html#subControlRect

    Parameters
    ----------

    cc : QStyle.ComplexControl
      Passed on as its number.

    option : Optional[QStyleOptionComplex]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    sc : QStyle.SubControl
      Passed on as its number.

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect QPixmapStyle::subControlRect(ComplexControl cc, const
    #      QStyleOptionComplex *option, SubControl sc, const QWidget *widget)
    #      const
    ritual = (
        'ritual_ZNK12QPixmapStyle14subControlRectEN6QStyle14ComplexControlE'
        'PK19QStyleOptionComplexNS0_10SubControlEPK7QWidget')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK12QPixmapStyle14subControlRectEN6QStyle14ComplexCo'
          'ntrolEPK19QStyleOptionComplexNS0_10SubControlEPK7QWidget')
    address = self.uglySide.call(
        ritual,
        cc.value, self._addressOf(option), sc.value, self._addressOf(widget),
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
    Calls Qt's 'int QPixmapStyle::pixelMetric(PixelMetric metric, const
    QStyleOption *option, const QWidget *widget) const'.

    Qt's own words: https://doc.qt.io/qt-6/qpixmapstyle.html#pixelMetric

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
    #  int QPixmapStyle::pixelMetric(PixelMetric metric, const QStyleOption
    #      *option, const QWidget *widget) const
    ritual = (
        'ritual_ZNK12QPixmapStyle11pixelMetricEN6QStyle11PixelMetricEPK12QS'
        'tyleOptionPK7QWidget')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK12QPixmapStyle11pixelMetricEN6QStyle11PixelMetricE'
          'PK12QStyleOptionPK7QWidget')
    return self.uglySide.call(
        ritual,
        metric.value, self._addressOf(option), self._addressOf(widget),
    )

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
      option: Optional[QStyleOption],
      widget: Optional[QWidget],
      returnData: Optional[QStyleHintReturn],
  ) -> int:
    """
    Calls Qt's 'int QPixmapStyle::styleHint(StyleHint hint, const
    QStyleOption *option, const QWidget *widget, QStyleHintReturn
    *returnData) const'.

    Qt's own words: https://doc.qt.io/qt-6/qpixmapstyle.html#styleHint

    Parameters
    ----------

    hint : QStyle.StyleHint
      Passed on as its number.

    option : Optional[QStyleOption]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    returnData : Optional[QStyleHintReturn]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  int QPixmapStyle::styleHint(StyleHint hint, const QStyleOption
    #      *option, const QWidget *widget, QStyleHintReturn *returnData)
    #      const
    ritual = (
        'ritual_ZNK12QPixmapStyle9styleHintEN6QStyle9StyleHintEPK12QStyleOp'
        'tionPK7QWidgetP16QStyleHintReturn')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK12QPixmapStyle9styleHintEN6QStyle9StyleHintEPK12QS'
          'tyleOptionPK7QWidgetP16QStyleHintReturn')
    return self.uglySide.call(
        ritual,
        hint.value, self._addressOf(option), self._addressOf(widget),
        self._addressOf(returnData),
    )

  @overload(QStyle.ComplexControl, QStyleOptionComplex, QPoint, QWidget)
  @overload(QStyle.ComplexControl, QStyleOptionComplex, QPoint, NoneType)
  @overload(QStyle.ComplexControl, NoneType, QPoint, QWidget)
  @overload(QStyle.ComplexControl, NoneType, QPoint, NoneType)
  def hitTestComplexControl(
      self,
      control: QStyle.ComplexControl,
      option: Optional[QStyleOptionComplex],
      pos: QPoint,
      widget: Optional[QWidget],
  ) -> QStyle.SubControl:
    """
    Calls Qt's 'SubControl QPixmapStyle::hitTestComplexControl(ComplexControl
    control, const QStyleOptionComplex *option, const QPoint &pos, const
    QWidget *widget) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpixmapstyle.html#hitTestComplexControl

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
      object.

    Returns
    -------

    QStyle.SubControl
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QStyle.SubControl(number)' gives.
    """
    #  SubControl QPixmapStyle::hitTestComplexControl(ComplexControl control,
    #      const QStyleOptionComplex *option, const QPoint &pos, const
    #      QWidget *widget) const
    ritual = (
        'ritual_ZNK12QPixmapStyle21hitTestComplexControlEN6QStyle14ComplexC'
        'ontrolEPK19QStyleOptionComplexRK6QPointPK7QWidget')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK12QPixmapStyle21hitTestComplexControlEN6QStyle14Co'
          'mplexControlEPK19QStyleOptionComplexRK6QPointPK7QWidget')
    return QStyle.SubControl(self.uglySide.call(
        ritual,
        control.value, self._addressOf(option), self._valueOf(pos),
        self._addressOf(widget),
    ))

  @overload(QStyleOption, QSize, QWidget)
  @overload(QStyleOption, QSize, NoneType)
  @overload(NoneType, QSize, QWidget)
  @overload(NoneType, QSize, NoneType)
  def pushButtonSizeFromContents(
      self,
      option: Optional[QStyleOption],
      contentsSize: QSize,
      widget: Optional[QWidget],
  ) -> QSize:
    """
    Calls Qt's 'QSize QPixmapStyle::pushButtonSizeFromContents(const
    QStyleOption *option, const QSize &contentsSize, const QWidget *widget)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpixmapstyle.html#pushButtonSizeFromContents

    Parameters
    ----------

    option : Optional[QStyleOption]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    contentsSize : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QPixmapStyle::pushButtonSizeFromContents(const QStyleOption
    #      *option, const QSize &contentsSize, const QWidget *widget) const
    address = self.uglySide.call(
        'ritual_ZNK12QPixmapStyle26pushButtonSizeFromContentsEPK12QStyleOpt'
        'ionRK5QSizePK7QWidget',
        self._addressOf(option), self._valueOf(contentsSize),
        self._addressOf(widget),
    )
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  @overload(QStyleOption, QSize, QWidget)
  @overload(QStyleOption, QSize, NoneType)
  @overload(NoneType, QSize, QWidget)
  @overload(NoneType, QSize, NoneType)
  def lineEditSizeFromContents(
      self,
      option: Optional[QStyleOption],
      contentsSize: QSize,
      widget: Optional[QWidget],
  ) -> QSize:
    """
    Calls Qt's 'QSize QPixmapStyle::lineEditSizeFromContents(const
    QStyleOption *option, const QSize &contentsSize, const QWidget *widget)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpixmapstyle.html#lineEditSizeFromContents

    Parameters
    ----------

    option : Optional[QStyleOption]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    contentsSize : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QPixmapStyle::lineEditSizeFromContents(const QStyleOption
    #      *option, const QSize &contentsSize, const QWidget *widget) const
    address = self.uglySide.call(
        'ritual_ZNK12QPixmapStyle24lineEditSizeFromContentsEPK12QStyleOptio'
        'nRK5QSizePK7QWidget',
        self._addressOf(option), self._valueOf(contentsSize),
        self._addressOf(widget),
    )
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  @overload(QStyleOption, QSize, QWidget)
  @overload(QStyleOption, QSize, NoneType)
  @overload(NoneType, QSize, QWidget)
  @overload(NoneType, QSize, NoneType)
  def progressBarSizeFromContents(
      self,
      option: Optional[QStyleOption],
      contentsSize: QSize,
      widget: Optional[QWidget],
  ) -> QSize:
    """
    Calls Qt's 'QSize QPixmapStyle::progressBarSizeFromContents(const
    QStyleOption *option, const QSize &contentsSize, const QWidget *widget)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpixmapstyle.html#progressBarSizeFromContents

    Parameters
    ----------

    option : Optional[QStyleOption]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    contentsSize : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QPixmapStyle::progressBarSizeFromContents(const QStyleOption
    #      *option, const QSize &contentsSize, const QWidget *widget) const
    address = self.uglySide.call(
        'ritual_ZNK12QPixmapStyle27progressBarSizeFromContentsEPK12QStyleOp'
        'tionRK5QSizePK7QWidget',
        self._addressOf(option), self._valueOf(contentsSize),
        self._addressOf(widget),
    )
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  @overload(QStyleOption, QSize, QWidget)
  @overload(QStyleOption, QSize, NoneType)
  @overload(NoneType, QSize, QWidget)
  @overload(NoneType, QSize, NoneType)
  def sliderSizeFromContents(
      self,
      option: Optional[QStyleOption],
      contentsSize: QSize,
      widget: Optional[QWidget],
  ) -> QSize:
    """
    Calls Qt's 'QSize QPixmapStyle::sliderSizeFromContents(const QStyleOption
    *option, const QSize &contentsSize, const QWidget *widget) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpixmapstyle.html#sliderSizeFromContents

    Parameters
    ----------

    option : Optional[QStyleOption]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    contentsSize : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QPixmapStyle::sliderSizeFromContents(const QStyleOption *option,
    #      const QSize &contentsSize, const QWidget *widget) const
    address = self.uglySide.call(
        'ritual_ZNK12QPixmapStyle22sliderSizeFromContentsEPK12QStyleOptionR'
        'K5QSizePK7QWidget',
        self._addressOf(option), self._valueOf(contentsSize),
        self._addressOf(widget),
    )
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  @overload(QStyleOption, QSize, QWidget)
  @overload(QStyleOption, QSize, NoneType)
  @overload(NoneType, QSize, QWidget)
  @overload(NoneType, QSize, NoneType)
  def comboBoxSizeFromContents(
      self,
      option: Optional[QStyleOption],
      contentsSize: QSize,
      widget: Optional[QWidget],
  ) -> QSize:
    """
    Calls Qt's 'QSize QPixmapStyle::comboBoxSizeFromContents(const
    QStyleOption *option, const QSize &contentsSize, const QWidget *widget)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpixmapstyle.html#comboBoxSizeFromContents

    Parameters
    ----------

    option : Optional[QStyleOption]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    contentsSize : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QPixmapStyle::comboBoxSizeFromContents(const QStyleOption
    #      *option, const QSize &contentsSize, const QWidget *widget) const
    address = self.uglySide.call(
        'ritual_ZNK12QPixmapStyle24comboBoxSizeFromContentsEPK12QStyleOptio'
        'nRK5QSizePK7QWidget',
        self._addressOf(option), self._valueOf(contentsSize),
        self._addressOf(widget),
    )
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  @overload(QStyleOption, QSize, QWidget)
  @overload(QStyleOption, QSize, NoneType)
  @overload(NoneType, QSize, QWidget)
  @overload(NoneType, QSize, NoneType)
  def itemViewSizeFromContents(
      self,
      option: Optional[QStyleOption],
      contentsSize: QSize,
      widget: Optional[QWidget],
  ) -> QSize:
    """
    Calls Qt's 'QSize QPixmapStyle::itemViewSizeFromContents(const
    QStyleOption *option, const QSize &contentsSize, const QWidget *widget)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpixmapstyle.html#itemViewSizeFromContents

    Parameters
    ----------

    option : Optional[QStyleOption]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    contentsSize : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QPixmapStyle::itemViewSizeFromContents(const QStyleOption
    #      *option, const QSize &contentsSize, const QWidget *widget) const
    address = self.uglySide.call(
        'ritual_ZNK12QPixmapStyle24itemViewSizeFromContentsEPK12QStyleOptio'
        'nRK5QSizePK7QWidget',
        self._addressOf(option), self._valueOf(contentsSize),
        self._addressOf(widget),
    )
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

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

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'QPixmapStyle::QPixmapStyle()', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qpixmapstyle.html#QPixmapStyle
    """
    #  QPixmapStyle::QPixmapStyle()
    self._noteCreation(QPixmapStyle, lambda: Rituals.call(
        'ritual_ZN12QPixmapStyleC1Ev',
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

  @overload(QApplication)
  @overload(NoneType)
  def polish(self, application: Optional[QApplication]) -> None:
    """
    Calls Qt's 'void QPixmapStyle::polish(QApplication *application)'.

    Qt's own words: https://doc.qt.io/qt-6/qpixmapstyle.html#polish

    Parameters
    ----------

    application : Optional[QApplication]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QPixmapStyle::polish(QApplication *application)
    ritual = 'ritual_ZN12QPixmapStyle6polishEP12QApplication'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN12QPixmapStyle6polishEP12QApplication'
    self.uglySide.call(ritual, self._addressOf(application))

  @overload(QWidget)
  def polish(self, widget: Optional[QWidget]) -> None:
    """
    Calls Qt's 'void QPixmapStyle::polish(QWidget *widget)'.

    Qt's own words: https://doc.qt.io/qt-6/qpixmapstyle.html#polish

    Parameters
    ----------

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QPixmapStyle::polish(QWidget *widget)
    ritual = 'ritual_ZN12QPixmapStyle6polishEP7QWidget'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN12QPixmapStyle6polishEP7QWidget'
    self.uglySide.call(ritual, self._addressOf(widget))

  @overload(QApplication)
  @overload(NoneType)
  def unpolish(self, application: Optional[QApplication]) -> None:
    """
    Calls Qt's 'void QPixmapStyle::unpolish(QApplication *application)'.

    Qt's own words: https://doc.qt.io/qt-6/qpixmapstyle.html#unpolish

    Parameters
    ----------

    application : Optional[QApplication]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QPixmapStyle::unpolish(QApplication *application)
    ritual = 'ritual_ZN12QPixmapStyle8unpolishEP12QApplication'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN12QPixmapStyle8unpolishEP12QApplication'
    self.uglySide.call(ritual, self._addressOf(application))

  @overload(QWidget)
  def unpolish(self, widget: Optional[QWidget]) -> None:
    """
    Calls Qt's 'void QPixmapStyle::unpolish(QWidget *widget)'.

    Qt's own words: https://doc.qt.io/qt-6/qpixmapstyle.html#unpolish

    Parameters
    ----------

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QPixmapStyle::unpolish(QWidget *widget)
    ritual = 'ritual_ZN12QPixmapStyle8unpolishEP7QWidget'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN12QPixmapStyle8unpolishEP7QWidget'
    self.uglySide.call(ritual, self._addressOf(widget))

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
    Calls Qt's 'void QPixmapStyle::drawPrimitive(PrimitiveElement element,
    const QStyleOption *option, QPainter *painter, const QWidget *widget)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qpixmapstyle.html#drawPrimitive

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
    #  void QPixmapStyle::drawPrimitive(PrimitiveElement element, const
    #      QStyleOption *option, QPainter *painter, const QWidget *widget)
    #      const
    ritual = (
        'ritual_ZNK12QPixmapStyle13drawPrimitiveEN6QStyle16PrimitiveElement'
        'EPK12QStyleOptionP8QPainterPK7QWidget')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK12QPixmapStyle13drawPrimitiveEN6QStyle16PrimitiveE'
          'lementEPK12QStyleOptionP8QPainterPK7QWidget')
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
    Calls Qt's 'void QPixmapStyle::drawControl(ControlElement element, const
    QStyleOption *option, QPainter *painter, const QWidget *widget) const'.

    Qt's own words: https://doc.qt.io/qt-6/qpixmapstyle.html#drawControl

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
    #  void QPixmapStyle::drawControl(ControlElement element, const
    #      QStyleOption *option, QPainter *painter, const QWidget *widget)
    #      const
    ritual = (
        'ritual_ZNK12QPixmapStyle11drawControlEN6QStyle14ControlElementEPK1'
        '2QStyleOptionP8QPainterPK7QWidget')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK12QPixmapStyle11drawControlEN6QStyle14ControlEleme'
          'ntEPK12QStyleOptionP8QPainterPK7QWidget')
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
      cc: QStyle.ComplexControl,
      option: Optional[QStyleOptionComplex],
      painter: Optional[QPainter],
      widget: Optional[QWidget] = None,
  ) -> None:
    """
    Calls Qt's 'void QPixmapStyle::drawComplexControl(ComplexControl cc,
    const QStyleOptionComplex *option, QPainter *painter, const QWidget
    *widget) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpixmapstyle.html#drawComplexControl

    Parameters
    ----------

    cc : QStyle.ComplexControl
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
    #  void QPixmapStyle::drawComplexControl(ComplexControl cc, const
    #      QStyleOptionComplex *option, QPainter *painter, const QWidget
    #      *widget) const
    ritual = (
        'ritual_ZNK12QPixmapStyle18drawComplexControlEN6QStyle14ComplexCont'
        'rolEPK19QStyleOptionComplexP8QPainterPK7QWidget')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK12QPixmapStyle18drawComplexControlEN6QStyle14Compl'
          'exControlEPK19QStyleOptionComplexP8QPainterPK7QWidget')
    self.uglySide.call(
        ritual,
        cc.value, self._addressOf(option), self._addressOf(painter),
        self._addressOf(widget),
    )

  @overload(QObject, QEvent)
  @overload(QObject, NoneType)
  @overload(NoneType, QEvent)
  @overload(NoneType, NoneType)
  def eventFilter(
      self,
      watched: Optional[QObject],
      event: Optional[QEvent],
  ) -> bool:
    """
    Calls Qt's 'bool QPixmapStyle::eventFilter(QObject *watched, QEvent
    *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qpixmapstyle.html#eventFilter

    Parameters
    ----------

    watched : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    event : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QPixmapStyle::eventFilter(QObject *watched, QEvent *event)
    ritual = 'ritual_ZN12QPixmapStyle11eventFilterEP7QObjectP6QEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN12QPixmapStyle11eventFilterEP7QObjectP6QEvent'
    return self.uglySide.call(
        ritual, self._addressOf(watched, 'QObject'), self._addressOf(event),
    )

  @overload(ControlDescriptor, str)
  @overload(ControlDescriptor, str, QMargins)
  @overload(ControlDescriptor, str, QMargins, QTileRules)
  def addDescriptor(
      self,
      control: ControlDescriptor,
      fileName: str,
      margins: Optional[QMargins] = None,
      tileRules: Optional[QTileRules] = None,
  ) -> None:
    """
    Calls Qt's 'void QPixmapStyle::addDescriptor(ControlDescriptor control,
    const QString &fileName, QMargins margins, QTileRules tileRules)'.

    Qt's own words: https://doc.qt.io/qt-6/qpixmapstyle.html#addDescriptor

    Parameters
    ----------

    control : ControlDescriptor
      Passed on as its number.

    fileName : str
      Passed on as it is: a QString is made of it for the call.

    margins : Optional[QMargins]
      Passed on as a value: Qt reads the C++ QMargins, which stays Python's
      own. May be left out, as in Qt: a new 'QMargins()' is then passed on.

    tileRules : Optional[QTileRules]
      Passed on as a value: Qt reads the C++ QTileRules, which stays Python's
      own. May be left out, as in Qt: a new
      'QTileRules(Qt.TileRule.RepeatTile, Qt.TileRule.RepeatTile)' is then
      passed on.
    """
    #  void QPixmapStyle::addDescriptor(ControlDescriptor control, const
    #      QString &fileName, QMargins margins, QTileRules tileRules)
    if margins is None:
      from ..QtCore import QMargins
      margins = QMargins()
    if tileRules is None:
      from . import QTileRules
      tileRules = QTileRules(Qt.TileRule.RepeatTile, Qt.TileRule.RepeatTile)
    self.uglySide.call(
        'ritual_ZN12QPixmapStyle13addDescriptorENS_17ControlDescriptorERK7Q'
        'String8QMargins10QTileRules',
        control.value, fileName, self._valueOf(margins, 'QMargins'),
        self._valueOf(tileRules),
    )

  @overload(ControlDescriptor, ControlDescriptor)
  def copyDescriptor(
      self,
      source: ControlDescriptor,
      dest: ControlDescriptor,
  ) -> None:
    """
    Calls Qt's 'void QPixmapStyle::copyDescriptor(ControlDescriptor source,
    ControlDescriptor dest)'.

    Qt's own words: https://doc.qt.io/qt-6/qpixmapstyle.html#copyDescriptor

    Parameters
    ----------

    source : ControlDescriptor
      Passed on as its number.

    dest : ControlDescriptor
      Passed on as its number.
    """
    #  void QPixmapStyle::copyDescriptor(ControlDescriptor source,
    #      ControlDescriptor dest)
    self.uglySide.call(
        'ritual_ZN12QPixmapStyle14copyDescriptorENS_17ControlDescriptorES0_',
        source.value, dest.value,
    )

  @overload(ControlDescriptor, QRect, QPainter)
  @overload(ControlDescriptor, QRect, NoneType)
  def drawCachedPixmap(
      self,
      control: ControlDescriptor,
      rect: QRect,
      p: Optional[QPainter],
  ) -> None:
    """
    Calls Qt's 'void QPixmapStyle::drawCachedPixmap(ControlDescriptor
    control, const QRect &rect, QPainter *p) const'.

    Qt's own words: https://doc.qt.io/qt-6/qpixmapstyle.html#drawCachedPixmap

    Parameters
    ----------

    control : ControlDescriptor
      Passed on as its number.

    rect : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.

    p : Optional[QPainter]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QPixmapStyle::drawCachedPixmap(ControlDescriptor control, const
    #      QRect &rect, QPainter *p) const
    self.uglySide.call(
        'ritual_ZNK12QPixmapStyle16drawCachedPixmapENS_17ControlDescriptorE'
        'RK5QRectP8QPainter',
        control.value, self._valueOf(rect), self._addressOf(p),
    )

  @overload(ControlPixmap, str)
  @overload(ControlPixmap, str, QMargins)
  def addPixmap(
      self,
      control: ControlPixmap,
      fileName: str,
      margins: Optional[QMargins] = None,
  ) -> None:
    """
    Calls Qt's 'void QPixmapStyle::addPixmap(ControlPixmap control, const
    QString &fileName, QMargins margins)'.

    Qt's own words: https://doc.qt.io/qt-6/qpixmapstyle.html#addPixmap

    Parameters
    ----------

    control : ControlPixmap
      Passed on as its number.

    fileName : str
      Passed on as it is: a QString is made of it for the call.

    margins : Optional[QMargins]
      Passed on as a value: Qt reads the C++ QMargins, which stays Python's
      own. May be left out, as in Qt: a new 'QMargins()' is then passed on.
    """
    #  void QPixmapStyle::addPixmap(ControlPixmap control, const QString
    #      &fileName, QMargins margins)
    if margins is None:
      from ..QtCore import QMargins
      margins = QMargins()
    self.uglySide.call(
        'ritual_ZN12QPixmapStyle9addPixmapENS_13ControlPixmapERK7QString8QM'
        'argins',
        control.value, fileName, self._valueOf(margins, 'QMargins'),
    )

  @overload(ControlPixmap, ControlPixmap)
  def copyPixmap(self, source: ControlPixmap, dest: ControlPixmap) -> None:
    """
    Calls Qt's 'void QPixmapStyle::copyPixmap(ControlPixmap source,
    ControlPixmap dest)'.

    Qt's own words: https://doc.qt.io/qt-6/qpixmapstyle.html#copyPixmap

    Parameters
    ----------

    source : ControlPixmap
      Passed on as its number.

    dest : ControlPixmap
      Passed on as its number.
    """
    #  void QPixmapStyle::copyPixmap(ControlPixmap source, ControlPixmap
    #      dest)
    self.uglySide.call(
        'ritual_ZN12QPixmapStyle10copyPixmapENS_13ControlPixmapES0_',
        source.value, dest.value,
    )

  @overload(QStyleOption, QPainter, QWidget)
  @overload(QStyleOption, QPainter, NoneType)
  @overload(QStyleOption, NoneType, QWidget)
  @overload(QStyleOption, NoneType, NoneType)
  @overload(NoneType, QPainter, QWidget)
  @overload(NoneType, QPainter, NoneType)
  @overload(NoneType, NoneType, QWidget)
  @overload(NoneType, NoneType, NoneType)
  def drawPushButton(
      self,
      option: Optional[QStyleOption],
      painter: Optional[QPainter],
      widget: Optional[QWidget],
  ) -> None:
    """
    Calls Qt's 'void QPixmapStyle::drawPushButton(const QStyleOption *option,
    QPainter *painter, const QWidget *widget) const'.

    Qt's own words: https://doc.qt.io/qt-6/qpixmapstyle.html#drawPushButton

    Parameters
    ----------

    option : Optional[QStyleOption]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    painter : Optional[QPainter]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QPixmapStyle::drawPushButton(const QStyleOption *option, QPainter
    #      *painter, const QWidget *widget) const
    self.uglySide.call(
        'ritual_ZNK12QPixmapStyle14drawPushButtonEPK12QStyleOptionP8QPainte'
        'rPK7QWidget',
        self._addressOf(option), self._addressOf(painter),
        self._addressOf(widget),
    )

  @overload(QStyleOption, QPainter, QWidget)
  @overload(QStyleOption, QPainter, NoneType)
  @overload(QStyleOption, NoneType, QWidget)
  @overload(QStyleOption, NoneType, NoneType)
  @overload(NoneType, QPainter, QWidget)
  @overload(NoneType, QPainter, NoneType)
  @overload(NoneType, NoneType, QWidget)
  @overload(NoneType, NoneType, NoneType)
  def drawLineEdit(
      self,
      option: Optional[QStyleOption],
      painter: Optional[QPainter],
      widget: Optional[QWidget],
  ) -> None:
    """
    Calls Qt's 'void QPixmapStyle::drawLineEdit(const QStyleOption *option,
    QPainter *painter, const QWidget *widget) const'.

    Qt's own words: https://doc.qt.io/qt-6/qpixmapstyle.html#drawLineEdit

    Parameters
    ----------

    option : Optional[QStyleOption]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    painter : Optional[QPainter]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QPixmapStyle::drawLineEdit(const QStyleOption *option, QPainter
    #      *painter, const QWidget *widget) const
    self.uglySide.call(
        'ritual_ZNK12QPixmapStyle12drawLineEditEPK12QStyleOptionP8QPainterP'
        'K7QWidget',
        self._addressOf(option), self._addressOf(painter),
        self._addressOf(widget),
    )

  @overload(QStyleOption, QPainter, QWidget)
  @overload(QStyleOption, QPainter, NoneType)
  @overload(QStyleOption, NoneType, QWidget)
  @overload(QStyleOption, NoneType, NoneType)
  @overload(NoneType, QPainter, QWidget)
  @overload(NoneType, QPainter, NoneType)
  @overload(NoneType, NoneType, QWidget)
  @overload(NoneType, NoneType, NoneType)
  def drawTextEdit(
      self,
      option: Optional[QStyleOption],
      painter: Optional[QPainter],
      widget: Optional[QWidget],
  ) -> None:
    """
    Calls Qt's 'void QPixmapStyle::drawTextEdit(const QStyleOption *option,
    QPainter *painter, const QWidget *widget) const'.

    Qt's own words: https://doc.qt.io/qt-6/qpixmapstyle.html#drawTextEdit

    Parameters
    ----------

    option : Optional[QStyleOption]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    painter : Optional[QPainter]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QPixmapStyle::drawTextEdit(const QStyleOption *option, QPainter
    #      *painter, const QWidget *widget) const
    self.uglySide.call(
        'ritual_ZNK12QPixmapStyle12drawTextEditEPK12QStyleOptionP8QPainterP'
        'K7QWidget',
        self._addressOf(option), self._addressOf(painter),
        self._addressOf(widget),
    )

  @overload(QStyleOption, QPainter, QWidget)
  @overload(QStyleOption, QPainter, NoneType)
  @overload(QStyleOption, NoneType, QWidget)
  @overload(QStyleOption, NoneType, NoneType)
  @overload(NoneType, QPainter, QWidget)
  @overload(NoneType, QPainter, NoneType)
  @overload(NoneType, NoneType, QWidget)
  @overload(NoneType, NoneType, NoneType)
  def drawCheckBox(
      self,
      option: Optional[QStyleOption],
      painter: Optional[QPainter],
      widget: Optional[QWidget],
  ) -> None:
    """
    Calls Qt's 'void QPixmapStyle::drawCheckBox(const QStyleOption *option,
    QPainter *painter, const QWidget *widget) const'.

    Qt's own words: https://doc.qt.io/qt-6/qpixmapstyle.html#drawCheckBox

    Parameters
    ----------

    option : Optional[QStyleOption]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    painter : Optional[QPainter]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QPixmapStyle::drawCheckBox(const QStyleOption *option, QPainter
    #      *painter, const QWidget *widget) const
    self.uglySide.call(
        'ritual_ZNK12QPixmapStyle12drawCheckBoxEPK12QStyleOptionP8QPainterP'
        'K7QWidget',
        self._addressOf(option), self._addressOf(painter),
        self._addressOf(widget),
    )

  @overload(QStyleOption, QPainter, QWidget)
  @overload(QStyleOption, QPainter, NoneType)
  @overload(QStyleOption, NoneType, QWidget)
  @overload(QStyleOption, NoneType, NoneType)
  @overload(NoneType, QPainter, QWidget)
  @overload(NoneType, QPainter, NoneType)
  @overload(NoneType, NoneType, QWidget)
  @overload(NoneType, NoneType, NoneType)
  def drawRadioButton(
      self,
      option: Optional[QStyleOption],
      painter: Optional[QPainter],
      widget: Optional[QWidget],
  ) -> None:
    """
    Calls Qt's 'void QPixmapStyle::drawRadioButton(const QStyleOption
    *option, QPainter *painter, const QWidget *widget) const'.

    Qt's own words: https://doc.qt.io/qt-6/qpixmapstyle.html#drawRadioButton

    Parameters
    ----------

    option : Optional[QStyleOption]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    painter : Optional[QPainter]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QPixmapStyle::drawRadioButton(const QStyleOption *option,
    #      QPainter *painter, const QWidget *widget) const
    self.uglySide.call(
        'ritual_ZNK12QPixmapStyle15drawRadioButtonEPK12QStyleOptionP8QPaint'
        'erPK7QWidget',
        self._addressOf(option), self._addressOf(painter),
        self._addressOf(widget),
    )

  @overload(QStyleOption, QPainter, QWidget)
  @overload(QStyleOption, QPainter, NoneType)
  @overload(QStyleOption, NoneType, QWidget)
  @overload(QStyleOption, NoneType, NoneType)
  @overload(NoneType, QPainter, QWidget)
  @overload(NoneType, QPainter, NoneType)
  @overload(NoneType, NoneType, QWidget)
  @overload(NoneType, NoneType, NoneType)
  def drawPanelItemViewItem(
      self,
      option: Optional[QStyleOption],
      painter: Optional[QPainter],
      widget: Optional[QWidget],
  ) -> None:
    """
    Calls Qt's 'void QPixmapStyle::drawPanelItemViewItem(const QStyleOption
    *option, QPainter *painter, const QWidget *widget) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpixmapstyle.html#drawPanelItemViewItem

    Parameters
    ----------

    option : Optional[QStyleOption]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    painter : Optional[QPainter]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QPixmapStyle::drawPanelItemViewItem(const QStyleOption *option,
    #      QPainter *painter, const QWidget *widget) const
    self.uglySide.call(
        'ritual_ZNK12QPixmapStyle21drawPanelItemViewItemEPK12QStyleOptionP8'
        'QPainterPK7QWidget',
        self._addressOf(option), self._addressOf(painter),
        self._addressOf(widget),
    )

  @overload(QStyleOption, QPainter, QWidget)
  @overload(QStyleOption, QPainter, NoneType)
  @overload(QStyleOption, NoneType, QWidget)
  @overload(QStyleOption, NoneType, NoneType)
  @overload(NoneType, QPainter, QWidget)
  @overload(NoneType, QPainter, NoneType)
  @overload(NoneType, NoneType, QWidget)
  @overload(NoneType, NoneType, NoneType)
  def drawProgressBarBackground(
      self,
      option: Optional[QStyleOption],
      painter: Optional[QPainter],
      widget: Optional[QWidget],
  ) -> None:
    """
    Calls Qt's 'void QPixmapStyle::drawProgressBarBackground(const
    QStyleOption *option, QPainter *painter, const QWidget *widget) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpixmapstyle.html#drawProgressBarBackground

    Parameters
    ----------

    option : Optional[QStyleOption]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    painter : Optional[QPainter]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QPixmapStyle::drawProgressBarBackground(const QStyleOption
    #      *option, QPainter *painter, const QWidget *widget) const
    self.uglySide.call(
        'ritual_ZNK12QPixmapStyle25drawProgressBarBackgroundEPK12QStyleOpti'
        'onP8QPainterPK7QWidget',
        self._addressOf(option), self._addressOf(painter),
        self._addressOf(widget),
    )

  @overload(QStyleOption, QPainter, QWidget)
  @overload(QStyleOption, QPainter, NoneType)
  @overload(QStyleOption, NoneType, QWidget)
  @overload(QStyleOption, NoneType, NoneType)
  @overload(NoneType, QPainter, QWidget)
  @overload(NoneType, QPainter, NoneType)
  @overload(NoneType, NoneType, QWidget)
  @overload(NoneType, NoneType, NoneType)
  def drawProgressBarLabel(
      self,
      option: Optional[QStyleOption],
      painter: Optional[QPainter],
      widget: Optional[QWidget],
  ) -> None:
    """
    Calls Qt's 'void QPixmapStyle::drawProgressBarLabel(const QStyleOption
    *option, QPainter *painter, const QWidget *widget) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpixmapstyle.html#drawProgressBarLabel

    Parameters
    ----------

    option : Optional[QStyleOption]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    painter : Optional[QPainter]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QPixmapStyle::drawProgressBarLabel(const QStyleOption *option,
    #      QPainter *painter, const QWidget *widget) const
    self.uglySide.call(
        'ritual_ZNK12QPixmapStyle20drawProgressBarLabelEPK12QStyleOptionP8Q'
        'PainterPK7QWidget',
        self._addressOf(option), self._addressOf(painter),
        self._addressOf(widget),
    )

  @overload(QStyleOption, QPainter, QWidget)
  @overload(QStyleOption, QPainter, NoneType)
  @overload(QStyleOption, NoneType, QWidget)
  @overload(QStyleOption, NoneType, NoneType)
  @overload(NoneType, QPainter, QWidget)
  @overload(NoneType, QPainter, NoneType)
  @overload(NoneType, NoneType, QWidget)
  @overload(NoneType, NoneType, NoneType)
  def drawProgressBarFill(
      self,
      option: Optional[QStyleOption],
      painter: Optional[QPainter],
      widget: Optional[QWidget],
  ) -> None:
    """
    Calls Qt's 'void QPixmapStyle::drawProgressBarFill(const QStyleOption
    *option, QPainter *painter, const QWidget *widget) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpixmapstyle.html#drawProgressBarFill

    Parameters
    ----------

    option : Optional[QStyleOption]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    painter : Optional[QPainter]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QPixmapStyle::drawProgressBarFill(const QStyleOption *option,
    #      QPainter *painter, const QWidget *widget) const
    self.uglySide.call(
        'ritual_ZNK12QPixmapStyle19drawProgressBarFillEPK12QStyleOptionP8QP'
        'ainterPK7QWidget',
        self._addressOf(option), self._addressOf(painter),
        self._addressOf(widget),
    )

  @overload(QStyleOptionComplex, QPainter, QWidget)
  @overload(QStyleOptionComplex, QPainter, NoneType)
  @overload(QStyleOptionComplex, NoneType, QWidget)
  @overload(QStyleOptionComplex, NoneType, NoneType)
  @overload(NoneType, QPainter, QWidget)
  @overload(NoneType, QPainter, NoneType)
  @overload(NoneType, NoneType, QWidget)
  @overload(NoneType, NoneType, NoneType)
  def drawSlider(
      self,
      option: Optional[QStyleOptionComplex],
      painter: Optional[QPainter],
      widget: Optional[QWidget],
  ) -> None:
    """
    Calls Qt's 'void QPixmapStyle::drawSlider(const QStyleOptionComplex
    *option, QPainter *painter, const QWidget *widget) const'.

    Qt's own words: https://doc.qt.io/qt-6/qpixmapstyle.html#drawSlider

    Parameters
    ----------

    option : Optional[QStyleOptionComplex]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    painter : Optional[QPainter]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QPixmapStyle::drawSlider(const QStyleOptionComplex *option,
    #      QPainter *painter, const QWidget *widget) const
    self.uglySide.call(
        'ritual_ZNK12QPixmapStyle10drawSliderEPK19QStyleOptionComplexP8QPai'
        'nterPK7QWidget',
        self._addressOf(option), self._addressOf(painter),
        self._addressOf(widget),
    )

  @overload(QStyleOptionComplex, QPainter, QWidget)
  @overload(QStyleOptionComplex, QPainter, NoneType)
  @overload(QStyleOptionComplex, NoneType, QWidget)
  @overload(QStyleOptionComplex, NoneType, NoneType)
  @overload(NoneType, QPainter, QWidget)
  @overload(NoneType, QPainter, NoneType)
  @overload(NoneType, NoneType, QWidget)
  @overload(NoneType, NoneType, NoneType)
  def drawComboBox(
      self,
      option: Optional[QStyleOptionComplex],
      painter: Optional[QPainter],
      widget: Optional[QWidget],
  ) -> None:
    """
    Calls Qt's 'void QPixmapStyle::drawComboBox(const QStyleOptionComplex
    *option, QPainter *painter, const QWidget *widget) const'.

    Qt's own words: https://doc.qt.io/qt-6/qpixmapstyle.html#drawComboBox

    Parameters
    ----------

    option : Optional[QStyleOptionComplex]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    painter : Optional[QPainter]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QPixmapStyle::drawComboBox(const QStyleOptionComplex *option,
    #      QPainter *painter, const QWidget *widget) const
    self.uglySide.call(
        'ritual_ZNK12QPixmapStyle12drawComboBoxEPK19QStyleOptionComplexP8QP'
        'ainterPK7QWidget',
        self._addressOf(option), self._addressOf(painter),
        self._addressOf(widget),
    )

  @overload(QStyleOptionComplex, QPainter, QWidget)
  @overload(QStyleOptionComplex, QPainter, NoneType)
  @overload(QStyleOptionComplex, NoneType, QWidget)
  @overload(QStyleOptionComplex, NoneType, NoneType)
  @overload(NoneType, QPainter, QWidget)
  @overload(NoneType, QPainter, NoneType)
  @overload(NoneType, NoneType, QWidget)
  @overload(NoneType, NoneType, NoneType)
  def drawScrollBar(
      self,
      option: Optional[QStyleOptionComplex],
      painter: Optional[QPainter],
      widget: Optional[QWidget],
  ) -> None:
    """
    Calls Qt's 'void QPixmapStyle::drawScrollBar(const QStyleOptionComplex
    *option, QPainter *painter, const QWidget *widget) const'.

    Qt's own words: https://doc.qt.io/qt-6/qpixmapstyle.html#drawScrollBar

    Parameters
    ----------

    option : Optional[QStyleOptionComplex]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    painter : Optional[QPainter]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QPixmapStyle::drawScrollBar(const QStyleOptionComplex *option,
    #      QPainter *painter, const QWidget *widget) const
    self.uglySide.call(
        'ritual_ZNK12QPixmapStyle13drawScrollBarEPK19QStyleOptionComplexP8Q'
        'PainterPK7QWidget',
        self._addressOf(option), self._addressOf(painter),
        self._addressOf(widget),
    )

  def d_func(self) -> Optional[QPixmapStylePrivate]:
    """
    Calls Qt's 'QPixmapStylePrivate *QPixmapStyle::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qpixmapstyle.html#d_func

    Returns
    -------

    Optional[QPixmapStylePrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPixmapStylePrivate *QPixmapStyle::d_func()
    address = self.uglySide.call('ritual_ZN12QPixmapStyle6d_funcEv')
    from . import QPixmapStylePrivate
    return QPixmapStylePrivate._cuteAt(address)

  @staticmethod
  def comboBoxSubControlRect(*__, **_) -> Never:
    """
    Qt's 'QRect QPixmapStyle::comboBoxSubControlRect(const
    QStyleOptionComplex *option, QPixmapStyle::SubControl sc, const QWidget
    *widget) const': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QPixmapStyle.comboBoxSubControlRect' has no cute function yet. "
        "Qt's 'QRect QPixmapStyle::comboBoxSubControlRect(const "
        "QStyleOptionComplex *option, QPixmapStyle::SubControl sc, const "
        "QWidget *widget) const': takes a type Python has no way to hand "
        "over yet.")

  @staticmethod
  def scrollBarSubControlRect(*__, **_) -> Never:
    """
    Qt's 'QRect QPixmapStyle::scrollBarSubControlRect(const
    QStyleOptionComplex *option, QPixmapStyle::SubControl sc, const QWidget
    *widget) const': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QPixmapStyle.scrollBarSubControlRect' has no cute function yet. "
        "Qt's 'QRect QPixmapStyle::scrollBarSubControlRect(const "
        "QStyleOptionComplex *option, QPixmapStyle::SubControl sc, const "
        "QWidget *widget) const': takes a type Python has no way to hand "
        "over yet.")
