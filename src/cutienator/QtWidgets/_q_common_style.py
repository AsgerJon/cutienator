"""
QCommonStyle binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/qcommonstyle.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import Qt
from ..QtGui import QIcon
from . import QSizePolicy, QStyle

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QPoint, QRect, QSize
  from ..QtGui import QPainter, QPixmap
  from . import QApplication, QStyleHintReturn, QStyleOption
  from . import QStyleOptionComplex, QWidget
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QApplication = WAIT['QApplication']
  QPainter = WAIT['QPainter']
  QPixmap = WAIT['QPixmap']
  QPoint = WAIT['QPoint']
  QSize = WAIT['QSize']
  QStyleHintReturn = WAIT['QStyleHintReturn']
  QStyleOption = WAIT['QStyleOption']
  QStyleOptionComplex = WAIT['QStyleOptionComplex']
  QWidget = WAIT['QWidget']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QCommonStyle(QStyle):
  """
  The cute side of Qt's QCommonStyle: a plain Python object standing in front
  of one C++ QCommonStyle.

  It is built on the cute 'QStyle', as Qt's QCommonStyle is built on Qt's
  QStyle, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QCommonStyle that has a ritual and that Python can
  call so far, 17 names in all: 'metaObject', 'tr', 'drawPrimitive',
  'drawControl', 'subElementRect', 'drawComplexControl',
  'hitTestComplexControl', 'subControlRect', 'sizeFromContents',
  'pixelMetric', 'styleHint', 'standardIcon', 'standardPixmap',
  'generatedIconPixmap', 'layoutSpacing', 'polish', 'unpolish'. It can be
  made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QCommonStyle::~QCommonStyle()': the destructor: Python never
    removes a C++ QCommonStyle.

  What has no ritual
  ------------------

  10 of the 31 functions Qt declares: 3 takes or gives a type that cannot be
  passed yet; 3 private; 2 forbidden; 1 a template; 1 protected.

  What to expect
  --------------

  - The C++ QCommonStyle is created at the first use, not by
    'QCommonStyle(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QCommonStyle.
  - Qt tells when it has removed the C++ QCommonStyle. Every call on the cute
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
    Calls Qt's 'QString QCommonStyle::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qcommonstyle.html#tr

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
    #  QString QCommonStyle::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN12QCommonStyle2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QCommonStyle'

  #  A C++ QCommonStyle Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QCommonStyle'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QCommonStyle::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcommonstyle.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QCommonStyle::metaObject() const
    address = self.uglySide.call('ritual_ZNK12QCommonStyle10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

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
    Calls Qt's 'QRect QCommonStyle::subElementRect(SubElement r, const
    QStyleOption *opt, const QWidget *widget) const'.

    Qt's own words: https://doc.qt.io/qt-6/qcommonstyle.html#subElementRect

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
    #  QRect QCommonStyle::subElementRect(SubElement r, const QStyleOption
    #      *opt, const QWidget *widget) const
    ritual = (
        'ritual_ZNK12QCommonStyle14subElementRectEN6QStyle10SubElementEPK12'
        'QStyleOptionPK7QWidget')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK12QCommonStyle14subElementRectEN6QStyle10SubElemen'
          'tEPK12QStyleOptionPK7QWidget')
    address = self.uglySide.call(
        ritual, r.value, self._addressOf(opt), self._addressOf(widget),
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
      cc: QStyle.ComplexControl,
      opt: Optional[QStyleOptionComplex],
      pt: QPoint,
      w: Optional[QWidget] = None,
  ) -> QStyle.SubControl:
    """
    Calls Qt's 'SubControl QCommonStyle::hitTestComplexControl(ComplexControl
    cc, const QStyleOptionComplex *opt, const QPoint &pt, const QWidget *w)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcommonstyle.html#hitTestComplexControl

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
    #  SubControl QCommonStyle::hitTestComplexControl(ComplexControl cc,
    #      const QStyleOptionComplex *opt, const QPoint &pt, const QWidget
    #      *w) const
    ritual = (
        'ritual_ZNK12QCommonStyle21hitTestComplexControlEN6QStyle14ComplexC'
        'ontrolEPK19QStyleOptionComplexRK6QPointPK7QWidget')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK12QCommonStyle21hitTestComplexControlEN6QStyle14Co'
          'mplexControlEPK19QStyleOptionComplexRK6QPointPK7QWidget')
    return QStyle.SubControl(self.uglySide.call(
        ritual,
        cc.value, self._addressOf(opt), self._valueOf(pt),
        self._addressOf(w),
    ))

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
    Calls Qt's 'QRect QCommonStyle::subControlRect(ComplexControl cc, const
    QStyleOptionComplex *opt, SubControl sc, const QWidget *w) const'.

    Qt's own words: https://doc.qt.io/qt-6/qcommonstyle.html#subControlRect

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
    #  QRect QCommonStyle::subControlRect(ComplexControl cc, const
    #      QStyleOptionComplex *opt, SubControl sc, const QWidget *w) const
    ritual = (
        'ritual_ZNK12QCommonStyle14subControlRectEN6QStyle14ComplexControlE'
        'PK19QStyleOptionComplexNS0_10SubControlEPK7QWidget')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK12QCommonStyle14subControlRectEN6QStyle14ComplexCo'
          'ntrolEPK19QStyleOptionComplexNS0_10SubControlEPK7QWidget')
    address = self.uglySide.call(
        ritual, cc.value, self._addressOf(opt), sc.value, self._addressOf(w),
    )
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

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
    Calls Qt's 'QSize QCommonStyle::sizeFromContents(ContentsType ct, const
    QStyleOption *opt, const QSize &contentsSize, const QWidget *widget)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qcommonstyle.html#sizeFromContents

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
    #  QSize QCommonStyle::sizeFromContents(ContentsType ct, const
    #      QStyleOption *opt, const QSize &contentsSize, const QWidget
    #      *widget) const
    ritual = (
        'ritual_ZNK12QCommonStyle16sizeFromContentsEN6QStyle12ContentsTypeE'
        'PK12QStyleOptionRK5QSizePK7QWidget')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK12QCommonStyle16sizeFromContentsEN6QStyle12Content'
          'sTypeEPK12QStyleOptionRK5QSizePK7QWidget')
    address = self.uglySide.call(
        ritual,
        ct.value, self._addressOf(opt), self._valueOf(contentsSize),
        self._addressOf(widget),
    )
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  @overload(QStyle.PixelMetric)
  @overload(QStyle.PixelMetric, QStyleOption)
  @overload(QStyle.PixelMetric, NoneType)
  @overload(QStyle.PixelMetric, QStyleOption, QWidget)
  @overload(QStyle.PixelMetric, QStyleOption, NoneType)
  @overload(QStyle.PixelMetric, NoneType, QWidget)
  @overload(QStyle.PixelMetric, NoneType, NoneType)
  def pixelMetric(
      self,
      m: QStyle.PixelMetric,
      opt: Optional[QStyleOption] = None,
      widget: Optional[QWidget] = None,
  ) -> int:
    """
    Calls Qt's 'int QCommonStyle::pixelMetric(PixelMetric m, const
    QStyleOption *opt, const QWidget *widget) const'.

    Qt's own words: https://doc.qt.io/qt-6/qcommonstyle.html#pixelMetric

    Parameters
    ----------

    m : QStyle.PixelMetric
      Passed on as its number.

    opt : Optional[QStyleOption]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  int QCommonStyle::pixelMetric(PixelMetric m, const QStyleOption *opt,
    #      const QWidget *widget) const
    ritual = (
        'ritual_ZNK12QCommonStyle11pixelMetricEN6QStyle11PixelMetricEPK12QS'
        'tyleOptionPK7QWidget')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK12QCommonStyle11pixelMetricEN6QStyle11PixelMetricE'
          'PK12QStyleOptionPK7QWidget')
    return self.uglySide.call(
        ritual, m.value, self._addressOf(opt), self._addressOf(widget),
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
    Calls Qt's 'int QCommonStyle::styleHint(StyleHint sh, const QStyleOption
    *opt, const QWidget *w, QStyleHintReturn *shret) const'.

    Qt's own words: https://doc.qt.io/qt-6/qcommonstyle.html#styleHint

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
    #  int QCommonStyle::styleHint(StyleHint sh, const QStyleOption *opt,
    #      const QWidget *w, QStyleHintReturn *shret) const
    ritual = (
        'ritual_ZNK12QCommonStyle9styleHintEN6QStyle9StyleHintEPK12QStyleOp'
        'tionPK7QWidgetP16QStyleHintReturn')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK12QCommonStyle9styleHintEN6QStyle9StyleHintEPK12QS'
          'tyleOptionPK7QWidgetP16QStyleHintReturn')
    return self.uglySide.call(
        ritual,
        sh.value, self._addressOf(opt), self._addressOf(w),
        self._addressOf(shret),
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
      opt: Optional[QStyleOption] = None,
      widget: Optional[QWidget] = None,
  ) -> QIcon:
    """
    Calls Qt's 'QIcon QCommonStyle::standardIcon(StandardPixmap standardIcon,
    const QStyleOption *opt, const QWidget *widget) const'.

    Qt's own words: https://doc.qt.io/qt-6/qcommonstyle.html#standardIcon

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
    #  QIcon QCommonStyle::standardIcon(StandardPixmap standardIcon, const
    #      QStyleOption *opt, const QWidget *widget) const
    ritual = (
        'ritual_ZNK12QCommonStyle12standardIconEN6QStyle14StandardPixmapEPK'
        '12QStyleOptionPK7QWidget')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK12QCommonStyle12standardIconEN6QStyle14StandardPix'
          'mapEPK12QStyleOptionPK7QWidget')
    address = self.uglySide.call(
        ritual,
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
      sp: QStyle.StandardPixmap,
      opt: Optional[QStyleOption] = None,
      widget: Optional[QWidget] = None,
  ) -> QPixmap:
    """
    Calls Qt's 'QPixmap QCommonStyle::standardPixmap(StandardPixmap sp, const
    QStyleOption *opt, const QWidget *widget) const'.

    Qt's own words: https://doc.qt.io/qt-6/qcommonstyle.html#standardPixmap

    Parameters
    ----------

    sp : QStyle.StandardPixmap
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
    #  QPixmap QCommonStyle::standardPixmap(StandardPixmap sp, const
    #      QStyleOption *opt, const QWidget *widget) const
    ritual = (
        'ritual_ZNK12QCommonStyle14standardPixmapEN6QStyle14StandardPixmapE'
        'PK12QStyleOptionPK7QWidget')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK12QCommonStyle14standardPixmapEN6QStyle14StandardP'
          'ixmapEPK12QStyleOptionPK7QWidget')
    address = self.uglySide.call(
        ritual, sp.value, self._addressOf(opt), self._addressOf(widget),
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
    Calls Qt's 'QPixmap QCommonStyle::generatedIconPixmap(QIcon::Mode
    iconMode, const QPixmap &pixmap, const QStyleOption *opt) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcommonstyle.html#generatedIconPixmap

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
    #  QPixmap QCommonStyle::generatedIconPixmap(QIcon::Mode iconMode, const
    #      QPixmap &pixmap, const QStyleOption *opt) const
    ritual = (
        'ritual_ZNK12QCommonStyle19generatedIconPixmapEN5QIcon4ModeERK7QPix'
        'mapPK12QStyleOption')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK12QCommonStyle19generatedIconPixmapEN5QIcon4ModeER'
          'K7QPixmapPK12QStyleOption')
    address = self.uglySide.call(
        ritual, iconMode.value, self._valueOf(pixmap), self._addressOf(opt),
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
    Calls Qt's 'int QCommonStyle::layoutSpacing(QSizePolicy::ControlType
    control1, QSizePolicy::ControlType control2, Qt::Orientation orientation,
    const QStyleOption *option, const QWidget *widget) const'.

    Qt's own words: https://doc.qt.io/qt-6/qcommonstyle.html#layoutSpacing

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
    #  int QCommonStyle::layoutSpacing(QSizePolicy::ControlType control1,
    #      QSizePolicy::ControlType control2, Qt::Orientation orientation,
    #      const QStyleOption *option, const QWidget *widget) const
    ritual = (
        'ritual_ZNK12QCommonStyle13layoutSpacingEN11QSizePolicy11ControlTyp'
        'eES1_N2Qt11OrientationEPK12QStyleOptionPK7QWidget')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK12QCommonStyle13layoutSpacingEN11QSizePolicy11Cont'
          'rolTypeES1_N2Qt11OrientationEPK12QStyleOptionPK7QWidget')
    return self.uglySide.call(
        ritual,
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

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'QCommonStyle::QCommonStyle()', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qcommonstyle.html#QCommonStyle
    """
    #  QCommonStyle::QCommonStyle()
    self._noteCreation(QCommonStyle, lambda: Rituals.call(
        'ritual_ZN12QCommonStyleC1Ev',
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
      pe: QStyle.PrimitiveElement,
      opt: Optional[QStyleOption],
      p: Optional[QPainter],
      w: Optional[QWidget] = None,
  ) -> None:
    """
    Calls Qt's 'void QCommonStyle::drawPrimitive(PrimitiveElement pe, const
    QStyleOption *opt, QPainter *p, const QWidget *w) const'.

    Qt's own words: https://doc.qt.io/qt-6/qcommonstyle.html#drawPrimitive

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
    #  void QCommonStyle::drawPrimitive(PrimitiveElement pe, const
    #      QStyleOption *opt, QPainter *p, const QWidget *w) const
    ritual = (
        'ritual_ZNK12QCommonStyle13drawPrimitiveEN6QStyle16PrimitiveElement'
        'EPK12QStyleOptionP8QPainterPK7QWidget')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK12QCommonStyle13drawPrimitiveEN6QStyle16PrimitiveE'
          'lementEPK12QStyleOptionP8QPainterPK7QWidget')
    self.uglySide.call(
        ritual,
        pe.value, self._addressOf(opt), self._addressOf(p),
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
    Calls Qt's 'void QCommonStyle::drawControl(ControlElement element, const
    QStyleOption *opt, QPainter *p, const QWidget *w) const'.

    Qt's own words: https://doc.qt.io/qt-6/qcommonstyle.html#drawControl

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
    #  void QCommonStyle::drawControl(ControlElement element, const
    #      QStyleOption *opt, QPainter *p, const QWidget *w) const
    ritual = (
        'ritual_ZNK12QCommonStyle11drawControlEN6QStyle14ControlElementEPK1'
        '2QStyleOptionP8QPainterPK7QWidget')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK12QCommonStyle11drawControlEN6QStyle14ControlEleme'
          'ntEPK12QStyleOptionP8QPainterPK7QWidget')
    self.uglySide.call(
        ritual,
        element.value, self._addressOf(opt), self._addressOf(p),
        self._addressOf(w),
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
      opt: Optional[QStyleOptionComplex],
      p: Optional[QPainter],
      w: Optional[QWidget] = None,
  ) -> None:
    """
    Calls Qt's 'void QCommonStyle::drawComplexControl(ComplexControl cc,
    const QStyleOptionComplex *opt, QPainter *p, const QWidget *w) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcommonstyle.html#drawComplexControl

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
    #  void QCommonStyle::drawComplexControl(ComplexControl cc, const
    #      QStyleOptionComplex *opt, QPainter *p, const QWidget *w) const
    ritual = (
        'ritual_ZNK12QCommonStyle18drawComplexControlEN6QStyle14ComplexCont'
        'rolEPK19QStyleOptionComplexP8QPainterPK7QWidget')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK12QCommonStyle18drawComplexControlEN6QStyle14Compl'
          'exControlEPK19QStyleOptionComplexP8QPainterPK7QWidget')
    self.uglySide.call(
        ritual,
        cc.value, self._addressOf(opt), self._addressOf(p),
        self._addressOf(w),
    )

  @overload(QApplication)
  @overload(NoneType)
  def polish(self, app: Optional[QApplication]) -> None:
    """
    Calls Qt's 'void QCommonStyle::polish(QApplication *app)'.

    Qt's own words: https://doc.qt.io/qt-6/qcommonstyle.html#polish

    Parameters
    ----------

    app : Optional[QApplication]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QCommonStyle::polish(QApplication *app)
    ritual = 'ritual_ZN12QCommonStyle6polishEP12QApplication'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN12QCommonStyle6polishEP12QApplication'
    self.uglySide.call(ritual, self._addressOf(app))

  @overload(QWidget)
  def polish(self, widget: Optional[QWidget]) -> None:
    """
    Calls Qt's 'void QCommonStyle::polish(QWidget *widget)'.

    Qt's own words: https://doc.qt.io/qt-6/qcommonstyle.html#polish

    Parameters
    ----------

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QCommonStyle::polish(QWidget *widget)
    ritual = 'ritual_ZN12QCommonStyle6polishEP7QWidget'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN12QCommonStyle6polishEP7QWidget'
    self.uglySide.call(ritual, self._addressOf(widget))

  @overload(QWidget)
  @overload(NoneType)
  def unpolish(self, widget: Optional[QWidget]) -> None:
    """
    Calls Qt's 'void QCommonStyle::unpolish(QWidget *widget)'.

    Qt's own words: https://doc.qt.io/qt-6/qcommonstyle.html#unpolish

    Parameters
    ----------

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QCommonStyle::unpolish(QWidget *widget)
    ritual = 'ritual_ZN12QCommonStyle8unpolishEP7QWidget'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN12QCommonStyle8unpolishEP7QWidget'
    self.uglySide.call(ritual, self._addressOf(widget))

  @overload(QApplication)
  def unpolish(self, application: Optional[QApplication]) -> None:
    """
    Calls Qt's 'void QCommonStyle::unpolish(QApplication *application)'.

    Qt's own words: https://doc.qt.io/qt-6/qcommonstyle.html#unpolish

    Parameters
    ----------

    application : Optional[QApplication]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QCommonStyle::unpolish(QApplication *application)
    ritual = 'ritual_ZN12QCommonStyle8unpolishEP12QApplication'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN12QCommonStyle8unpolishEP12QApplication'
    self.uglySide.call(ritual, self._addressOf(application))
