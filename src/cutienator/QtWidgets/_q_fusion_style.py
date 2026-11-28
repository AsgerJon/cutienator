"""
QFusionStyle binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/6.12.0/QtWidgets/private/qfusionstyle_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QFusionStyle to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import Qt
from ..QtGui import QIcon, QPalette
from . import QCommonStyle, QStyle

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QPoint, QRect, QSize
  from ..QtGui import QPainter, QPixmap
  from . import QApplication, QFusionStylePrivate, QStyleHintReturn
  from . import QStyleOption, QStyleOptionComplex, QWidget
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QApplication = WAIT['QApplication']
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


class QFusionStyle(QCommonStyle):
  """
  The cute side of Qt's QFusionStyle: a plain Python object standing in front
  of one C++ QFusionStyle.

  It is built on the cute 'QCommonStyle', as Qt's QFusionStyle is built on
  Qt's QCommonStyle, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QFusionStyle that has a ritual and that Python can
  call so far, 24 names in all: 'metaObject', 'tr', 'd_func',
  'standardPalette', 'drawPrimitive', 'drawControl', 'pixelMetric',
  'drawComplexControl', 'subElementRect', 'sizeFromContents',
  'hitTestComplexControl', 'subControlRect', 'generatedIconPixmap',
  'styleHint', 'itemPixmapRect', 'iconFromTheme', 'standardIcon',
  'standardPixmap', 'drawItemPixmap', 'drawItemText', 'polish', 'unpolish',
  'isHighContrast', 'colorScheme'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QFusionStyle::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QFusionStyle::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'const QFusionStylePrivate *QFusionStyle::d_func() const': takes in
    Python what 'QFusionStylePrivate *QFusionStyle::d_func()' takes.
  - Qt's 'QFusionStyle::~QFusionStyle()': the destructor: Python never
    removes a C++ QFusionStyle.
  - Qt's 'void QFusionStyle::polish(QPalette &pal)': takes a type Python has
    no way to hand over yet.
  - Qt's 'QFusionStyle::QFusionStyle(QFusionStylePrivate &dd)': takes a type
    Python has no way to hand over yet.

  What has no ritual
  ------------------

  2 of the 35 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QFusionStyle is created at the first use, not by
    'QFusionStyle(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QFusionStyle.
  - Qt tells when it has removed the C++ QFusionStyle. Every call on the cute
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
    Calls Qt's 'QString QFusionStyle::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qfusionstyle.html#tr

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
    #  QString QFusionStyle::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN12QFusionStyle2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QFusionStyle'

  #  A C++ QFusionStyle Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QFusionStyle'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QFusionStyle::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfusionstyle.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QFusionStyle::metaObject() const
    address = self.uglySide.call('ritual_ZNK12QFusionStyle10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def standardPalette(self) -> QPalette:
    """
    Calls Qt's 'QPalette QFusionStyle::standardPalette() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfusionstyle.html#standardPalette

    Returns
    -------

    QPalette
      A new cute QPalette around the copy Qt gave back. Python owns it.
    """
    #  QPalette QFusionStyle::standardPalette() const
    ritual = 'ritual_ZNK12QFusionStyle15standardPaletteEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK12QFusionStyle15standardPaletteEv'
    address = self.uglySide.call(ritual)
    return QPalette._cuteOwning(address)

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
    Calls Qt's 'int QFusionStyle::pixelMetric(PixelMetric metric, const
    QStyleOption *option, const QWidget *widget) const'.

    Qt's own words: https://doc.qt.io/qt-6/qfusionstyle.html#pixelMetric

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
    #  int QFusionStyle::pixelMetric(PixelMetric metric, const QStyleOption
    #      *option, const QWidget *widget) const
    ritual = (
        'ritual_ZNK12QFusionStyle11pixelMetricEN6QStyle11PixelMetricEPK12QS'
        'tyleOptionPK7QWidget')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK12QFusionStyle11pixelMetricEN6QStyle11PixelMetricE'
          'PK12QStyleOptionPK7QWidget')
    return self.uglySide.call(
        ritual,
        metric.value, self._addressOf(option), self._addressOf(widget),
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
    Calls Qt's 'QRect QFusionStyle::subElementRect(SubElement r, const
    QStyleOption *opt, const QWidget *widget) const'.

    Qt's own words: https://doc.qt.io/qt-6/qfusionstyle.html#subElementRect

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
    #  QRect QFusionStyle::subElementRect(SubElement r, const QStyleOption
    #      *opt, const QWidget *widget) const
    ritual = (
        'ritual_ZNK12QFusionStyle14subElementRectEN6QStyle10SubElementEPK12'
        'QStyleOptionPK7QWidget')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK12QFusionStyle14subElementRectEN6QStyle10SubElemen'
          'tEPK12QStyleOptionPK7QWidget')
    address = self.uglySide.call(
        ritual, r.value, self._addressOf(opt), self._addressOf(widget),
    )
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

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
    Calls Qt's 'QSize QFusionStyle::sizeFromContents(ContentsType type, const
    QStyleOption *option, const QSize &size, const QWidget *widget) const'.

    Qt's own words: https://doc.qt.io/qt-6/qfusionstyle.html#sizeFromContents

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
    #  QSize QFusionStyle::sizeFromContents(ContentsType type, const
    #      QStyleOption *option, const QSize &size, const QWidget *widget)
    #      const
    ritual = (
        'ritual_ZNK12QFusionStyle16sizeFromContentsEN6QStyle12ContentsTypeE'
        'PK12QStyleOptionRK5QSizePK7QWidget')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK12QFusionStyle16sizeFromContentsEN6QStyle12Content'
          'sTypeEPK12QStyleOptionRK5QSizePK7QWidget')
    address = self.uglySide.call(
        ritual,
        type.value, self._addressOf(option), self._valueOf(size),
        self._addressOf(widget),
    )
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

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
    Calls Qt's 'SubControl QFusionStyle::hitTestComplexControl(ComplexControl
    cc, const QStyleOptionComplex *opt, const QPoint &pt, const QWidget *w)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfusionstyle.html#hitTestComplexControl

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
    #  SubControl QFusionStyle::hitTestComplexControl(ComplexControl cc,
    #      const QStyleOptionComplex *opt, const QPoint &pt, const QWidget
    #      *w) const
    ritual = (
        'ritual_ZNK12QFusionStyle21hitTestComplexControlEN6QStyle14ComplexC'
        'ontrolEPK19QStyleOptionComplexRK6QPointPK7QWidget')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK12QFusionStyle21hitTestComplexControlEN6QStyle14Co'
          'mplexControlEPK19QStyleOptionComplexRK6QPointPK7QWidget')
    return QStyle.SubControl(self.uglySide.call(
        ritual,
        cc.value, self._addressOf(opt), self._valueOf(pt),
        self._addressOf(w),
    ))

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
    Calls Qt's 'QRect QFusionStyle::subControlRect(ComplexControl cc, const
    QStyleOptionComplex *opt, SubControl sc, const QWidget *widget) const'.

    Qt's own words: https://doc.qt.io/qt-6/qfusionstyle.html#subControlRect

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
    #  QRect QFusionStyle::subControlRect(ComplexControl cc, const
    #      QStyleOptionComplex *opt, SubControl sc, const QWidget *widget)
    #      const
    ritual = (
        'ritual_ZNK12QFusionStyle14subControlRectEN6QStyle14ComplexControlE'
        'PK19QStyleOptionComplexNS0_10SubControlEPK7QWidget')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK12QFusionStyle14subControlRectEN6QStyle14ComplexCo'
          'ntrolEPK19QStyleOptionComplexNS0_10SubControlEPK7QWidget')
    address = self.uglySide.call(
        ritual,
        cc.value, self._addressOf(opt), sc.value, self._addressOf(widget),
    )
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

  @overload(QIcon.Mode, QPixmap, QStyleOption)
  @overload(QIcon.Mode, QPixmap, NoneType)
  def generatedIconPixmap(
      self,
      iconMode: QIcon.Mode,
      pixmap: QPixmap,
      opt: Optional[QStyleOption],
  ) -> QPixmap:
    """
    Calls Qt's 'QPixmap QFusionStyle::generatedIconPixmap(QIcon::Mode
    iconMode, const QPixmap &pixmap, const QStyleOption *opt) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfusionstyle.html#generatedIconPixmap

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
    #  QPixmap QFusionStyle::generatedIconPixmap(QIcon::Mode iconMode, const
    #      QPixmap &pixmap, const QStyleOption *opt) const
    ritual = (
        'ritual_ZNK12QFusionStyle19generatedIconPixmapEN5QIcon4ModeERK7QPix'
        'mapPK12QStyleOption')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK12QFusionStyle19generatedIconPixmapEN5QIcon4ModeER'
          'K7QPixmapPK12QStyleOption')
    address = self.uglySide.call(
        ritual, iconMode.value, self._valueOf(pixmap), self._addressOf(opt),
    )
    from ..QtGui import QPixmap
    return QPixmap._cuteOwning(address)

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
    Calls Qt's 'int QFusionStyle::styleHint(StyleHint hint, const
    QStyleOption *option, const QWidget *widget, QStyleHintReturn
    *returnData) const'.

    Qt's own words: https://doc.qt.io/qt-6/qfusionstyle.html#styleHint

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
    #  int QFusionStyle::styleHint(StyleHint hint, const QStyleOption
    #      *option, const QWidget *widget, QStyleHintReturn *returnData)
    #      const
    ritual = (
        'ritual_ZNK12QFusionStyle9styleHintEN6QStyle9StyleHintEPK12QStyleOp'
        'tionPK7QWidgetP16QStyleHintReturn')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK12QFusionStyle9styleHintEN6QStyle9StyleHintEPK12QS'
          'tyleOptionPK7QWidgetP16QStyleHintReturn')
    return self.uglySide.call(
        ritual,
        hint.value, self._addressOf(option), self._addressOf(widget),
        self._addressOf(returnData),
    )

  @overload(QRect, int, QPixmap)
  def itemPixmapRect(self, r: QRect, flags: int, pixmap: QPixmap) -> QRect:
    """
    Calls Qt's 'QRect QFusionStyle::itemPixmapRect(const QRect &r, int flags,
    const QPixmap &pixmap) const'.

    Qt's own words: https://doc.qt.io/qt-6/qfusionstyle.html#itemPixmapRect

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
    #  QRect QFusionStyle::itemPixmapRect(const QRect &r, int flags, const
    #      QPixmap &pixmap) const
    ritual = 'ritual_ZNK12QFusionStyle14itemPixmapRectERK5QRectiRK7QPixmap'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK12QFusionStyle14itemPixmapRectERK5QRectiRK7QPixmap')
    address = self.uglySide.call(
        ritual, self._valueOf(r), flags, self._valueOf(pixmap),
    )
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

  @overload(QStyle.StandardPixmap)
  def iconFromTheme(self, standardIcon: QStyle.StandardPixmap) -> QIcon:
    """
    Calls Qt's 'QIcon QFusionStyle::iconFromTheme(StandardPixmap
    standardIcon) const'.

    Qt's own words: https://doc.qt.io/qt-6/qfusionstyle.html#iconFromTheme

    Parameters
    ----------

    standardIcon : QStyle.StandardPixmap
      Passed on as its number.

    Returns
    -------

    QIcon
      A new cute QIcon around the copy Qt gave back. Python owns it.
    """
    #  QIcon QFusionStyle::iconFromTheme(StandardPixmap standardIcon) const
    address = self.uglySide.call(
        'ritual_ZNK12QFusionStyle13iconFromThemeEN6QStyle14StandardPixmapE',
        standardIcon.value,
    )
    return QIcon._cuteOwning(address)

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
    Calls Qt's 'QIcon QFusionStyle::standardIcon(StandardPixmap standardIcon,
    const QStyleOption *option, const QWidget *widget) const'.

    Qt's own words: https://doc.qt.io/qt-6/qfusionstyle.html#standardIcon

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
    #  QIcon QFusionStyle::standardIcon(StandardPixmap standardIcon, const
    #      QStyleOption *option, const QWidget *widget) const
    ritual = (
        'ritual_ZNK12QFusionStyle12standardIconEN6QStyle14StandardPixmapEPK'
        '12QStyleOptionPK7QWidget')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK12QFusionStyle12standardIconEN6QStyle14StandardPix'
          'mapEPK12QStyleOptionPK7QWidget')
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
    Calls Qt's 'QPixmap QFusionStyle::standardPixmap(StandardPixmap
    standardPixmap, const QStyleOption *opt, const QWidget *widget) const'.

    Qt's own words: https://doc.qt.io/qt-6/qfusionstyle.html#standardPixmap

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
    #  QPixmap QFusionStyle::standardPixmap(StandardPixmap standardPixmap,
    #      const QStyleOption *opt, const QWidget *widget) const
    ritual = (
        'ritual_ZNK12QFusionStyle14standardPixmapEN6QStyle14StandardPixmapE'
        'PK12QStyleOptionPK7QWidget')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK12QFusionStyle14standardPixmapEN6QStyle14StandardP'
          'ixmapEPK12QStyleOptionPK7QWidget')
    address = self.uglySide.call(
        ritual,
        standardPixmap.value, self._addressOf(opt), self._addressOf(widget),
    )
    from ..QtGui import QPixmap
    return QPixmap._cuteOwning(address)

  def isHighContrast(self) -> bool:
    """
    Calls Qt's 'bool QFusionStyle::isHighContrast() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfusionstyle.html#isHighContrast
    """
    #  bool QFusionStyle::isHighContrast() const
    return self.uglySide.call('ritual_ZNK12QFusionStyle14isHighContrastEv')

  def colorScheme(self) -> Qt.ColorScheme:
    """
    Calls Qt's 'Qt::ColorScheme QFusionStyle::colorScheme() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfusionstyle.html#colorScheme

    Returns
    -------

    Qt.ColorScheme
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Qt.ColorScheme(number)'
      gives.
    """
    #  Qt::ColorScheme QFusionStyle::colorScheme() const
    return Qt.ColorScheme(self.uglySide.call(
        'ritual_ZNK12QFusionStyle11colorSchemeEv',
    ))

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
    Notes what was given, for Qt's 'QFusionStyle::QFusionStyle()', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qfusionstyle.html#QFusionStyle
    """
    #  QFusionStyle::QFusionStyle()
    self._noteCreation(QFusionStyle, lambda: Rituals.call(
        'ritual_ZN12QFusionStyleC1Ev',
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

  def d_func(self) -> Optional[QFusionStylePrivate]:
    """
    Calls Qt's 'QFusionStylePrivate *QFusionStyle::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qfusionstyle.html#d_func

    Returns
    -------

    Optional[QFusionStylePrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QFusionStylePrivate *QFusionStyle::d_func()
    address = self.uglySide.call('ritual_ZN12QFusionStyle6d_funcEv')
    from . import QFusionStylePrivate
    return QFusionStylePrivate._cuteAt(address)

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
      elem: QStyle.PrimitiveElement,
      option: Optional[QStyleOption],
      painter: Optional[QPainter],
      widget: Optional[QWidget] = None,
  ) -> None:
    """
    Calls Qt's 'void QFusionStyle::drawPrimitive(PrimitiveElement elem, const
    QStyleOption *option, QPainter *painter, const QWidget *widget) const'.

    Qt's own words: https://doc.qt.io/qt-6/qfusionstyle.html#drawPrimitive

    Parameters
    ----------

    elem : QStyle.PrimitiveElement
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
    #  void QFusionStyle::drawPrimitive(PrimitiveElement elem, const
    #      QStyleOption *option, QPainter *painter, const QWidget *widget)
    #      const
    ritual = (
        'ritual_ZNK12QFusionStyle13drawPrimitiveEN6QStyle16PrimitiveElement'
        'EPK12QStyleOptionP8QPainterPK7QWidget')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK12QFusionStyle13drawPrimitiveEN6QStyle16PrimitiveE'
          'lementEPK12QStyleOptionP8QPainterPK7QWidget')
    self.uglySide.call(
        ritual,
        elem.value, self._addressOf(option), self._addressOf(painter),
        self._addressOf(widget),
    )

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
      ce: QStyle.ControlElement,
      option: Optional[QStyleOption],
      painter: Optional[QPainter],
      widget: Optional[QWidget],
  ) -> None:
    """
    Calls Qt's 'void QFusionStyle::drawControl(ControlElement ce, const
    QStyleOption *option, QPainter *painter, const QWidget *widget) const'.

    Qt's own words: https://doc.qt.io/qt-6/qfusionstyle.html#drawControl

    Parameters
    ----------

    ce : QStyle.ControlElement
      Passed on as its number.

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
    #  void QFusionStyle::drawControl(ControlElement ce, const QStyleOption
    #      *option, QPainter *painter, const QWidget *widget) const
    ritual = (
        'ritual_ZNK12QFusionStyle11drawControlEN6QStyle14ControlElementEPK1'
        '2QStyleOptionP8QPainterPK7QWidget')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK12QFusionStyle11drawControlEN6QStyle14ControlEleme'
          'ntEPK12QStyleOptionP8QPainterPK7QWidget')
    self.uglySide.call(
        ritual,
        ce.value, self._addressOf(option), self._addressOf(painter),
        self._addressOf(widget),
    )

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
      widget: Optional[QWidget],
  ) -> None:
    """
    Calls Qt's 'void QFusionStyle::drawComplexControl(ComplexControl control,
    const QStyleOptionComplex *option, QPainter *painter, const QWidget
    *widget) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfusionstyle.html#drawComplexControl

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
      object.
    """
    #  void QFusionStyle::drawComplexControl(ComplexControl control, const
    #      QStyleOptionComplex *option, QPainter *painter, const QWidget
    #      *widget) const
    ritual = (
        'ritual_ZNK12QFusionStyle18drawComplexControlEN6QStyle14ComplexCont'
        'rolEPK19QStyleOptionComplexP8QPainterPK7QWidget')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK12QFusionStyle18drawComplexControlEN6QStyle14Compl'
          'exControlEPK19QStyleOptionComplexP8QPainterPK7QWidget')
    self.uglySide.call(
        ritual,
        control.value, self._addressOf(option), self._addressOf(painter),
        self._addressOf(widget),
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
    Calls Qt's 'void QFusionStyle::drawItemPixmap(QPainter *painter, const
    QRect &rect, int alignment, const QPixmap &pixmap) const'.

    Qt's own words: https://doc.qt.io/qt-6/qfusionstyle.html#drawItemPixmap

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
    #  void QFusionStyle::drawItemPixmap(QPainter *painter, const QRect
    #      &rect, int alignment, const QPixmap &pixmap) const
    ritual = (
        'ritual_ZNK12QFusionStyle14drawItemPixmapEP8QPainterRK5QRectiRK7QPi'
        'xmap')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK12QFusionStyle14drawItemPixmapEP8QPainterRK5QRecti'
          'RK7QPixmap')
    self.uglySide.call(
        ritual,
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
      flags: int,
      pal: QPalette,
      enabled: bool,
      text: str,
      textRole: QPalette.ColorRole = QPalette.ColorRole.NoRole,
  ) -> None:
    """
    Calls Qt's 'void QFusionStyle::drawItemText(QPainter *painter, const
    QRect &rect, int flags, const QPalette &pal, bool enabled, const QString
    &text, QPalette::ColorRole textRole) const'.

    Qt's own words: https://doc.qt.io/qt-6/qfusionstyle.html#drawItemText

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
    #  void QFusionStyle::drawItemText(QPainter *painter, const QRect &rect,
    #      int flags, const QPalette &pal, bool enabled, const QString &text,
    #      QPalette::ColorRole textRole) const
    ritual = (
        'ritual_ZNK12QFusionStyle12drawItemTextEP8QPainterRK5QRectiRK8QPale'
        'ttebRK7QStringNS5_9ColorRoleE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK12QFusionStyle12drawItemTextEP8QPainterRK5QRectiRK'
          '8QPalettebRK7QStringNS5_9ColorRoleE')
    self.uglySide.call(
        ritual,
        self._addressOf(painter), self._valueOf(rect), flags,
        self._valueOf(pal), enabled, text, textRole.value,
    )

  @overload(QWidget)
  @overload(NoneType)
  def polish(self, widget: Optional[QWidget]) -> None:
    """
    Calls Qt's 'void QFusionStyle::polish(QWidget *widget)'.

    Qt's own words: https://doc.qt.io/qt-6/qfusionstyle.html#polish

    Parameters
    ----------

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QFusionStyle::polish(QWidget *widget)
    ritual = 'ritual_ZN12QFusionStyle6polishEP7QWidget'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN12QFusionStyle6polishEP7QWidget'
    self.uglySide.call(ritual, self._addressOf(widget))

  @overload(QApplication)
  def polish(self, app: Optional[QApplication]) -> None:
    """
    Calls Qt's 'void QFusionStyle::polish(QApplication *app)'.

    Qt's own words: https://doc.qt.io/qt-6/qfusionstyle.html#polish

    Parameters
    ----------

    app : Optional[QApplication]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QFusionStyle::polish(QApplication *app)
    ritual = 'ritual_ZN12QFusionStyle6polishEP12QApplication'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN12QFusionStyle6polishEP12QApplication'
    self.uglySide.call(ritual, self._addressOf(app))

  @overload(QWidget)
  @overload(NoneType)
  def unpolish(self, widget: Optional[QWidget]) -> None:
    """
    Calls Qt's 'void QFusionStyle::unpolish(QWidget *widget)'.

    Qt's own words: https://doc.qt.io/qt-6/qfusionstyle.html#unpolish

    Parameters
    ----------

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QFusionStyle::unpolish(QWidget *widget)
    ritual = 'ritual_ZN12QFusionStyle8unpolishEP7QWidget'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN12QFusionStyle8unpolishEP7QWidget'
    self.uglySide.call(ritual, self._addressOf(widget))

  @overload(QApplication)
  def unpolish(self, app: Optional[QApplication]) -> None:
    """
    Calls Qt's 'void QFusionStyle::unpolish(QApplication *app)'.

    Qt's own words: https://doc.qt.io/qt-6/qfusionstyle.html#unpolish

    Parameters
    ----------

    app : Optional[QApplication]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QFusionStyle::unpolish(QApplication *app)
    ritual = 'ritual_ZN12QFusionStyle8unpolishEP12QApplication'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN12QFusionStyle8unpolishEP12QApplication'
    self.uglySide.call(ritual, self._addressOf(app))
