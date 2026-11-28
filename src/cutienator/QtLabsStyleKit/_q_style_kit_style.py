"""
QStyleKitStyle binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtLabsStyleKit/qstylekitstyle.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject, QStringList
from ..QtWidgets import QCommonStyle, QStyle

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QEvent, QMetaObject, QPoint, QRect, QSize
  from ..QtGui import QPainter, QPalette
  from ..QtWidgets import QApplication, QStyleHintReturn, QStyleOption
  from ..QtWidgets import QStyleOptionComplex, QWidget
  from . import QStyleKitStylePrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QApplication = WAIT['QApplication']
  QEvent = WAIT['QEvent']
  QPainter = WAIT['QPainter']
  QPoint = WAIT['QPoint']
  QSize = WAIT['QSize']
  QStyleHintReturn = WAIT['QStyleHintReturn']
  QStyleOption = WAIT['QStyleOption']
  QStyleOptionComplex = WAIT['QStyleOptionComplex']
  QWidget = WAIT['QWidget']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QStyleKitStyle(QCommonStyle):
  """
  The cute side of Qt's QStyleKitStyle: a plain Python object standing in
  front of one C++ QStyleKitStyle.

  It is built on the cute 'QCommonStyle', as Qt's QStyleKitStyle is built on
  Qt's QCommonStyle, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QStyleKitStyle that has a ritual and that Python can
  call so far, 27 names in all: 'metaObject', 'tr', 'stylePath',
  'setStylePath', 'themeName', 'setThemeName', 'availableThemeNames',
  'customThemeNames', 'drawPrimitive', 'drawControl', 'subElementRect',
  'drawComplexControl', 'hitTestComplexControl', 'subControlRect',
  'sizeFromContents', 'pixelMetric', 'styleHint', 'standardPalette',
  'polish', 'unpolish', 'eventFilter', 'event', 'stylePathChanged',
  'themeNameChanged', 'availableThemeNamesChanged',
  'customThemeNamesChanged', 'd_func'. It can be made from Python, in 2 ways;
  see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QStyleKitStyle::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QStyleKitStyle::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QStyleKitStyle::~QStyleKitStyle()': the destructor: Python never
    removes a C++ QStyleKitStyle.
  - Qt's 'void QStyleKitStyle::polish(QPalette &palette)': takes a type
    Python has no way to hand over yet.
  - Qt's 'const QStyleKitStylePrivate *QStyleKitStyle::d_func() const': takes
    in Python what 'QStyleKitStylePrivate *QStyleKitStyle::d_func()' takes.

  What has no ritual
  ------------------

  6 of the 42 functions Qt declares: 4 forbidden; 2 not a gap.

  What to expect
  --------------

  - The C++ QStyleKitStyle is created at the first use, not by
    'QStyleKitStyle(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QStyleKitStyle.
  - Qt tells when it has removed the C++ QStyleKitStyle. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
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
    Calls Qt's 'QString QStyleKitStyle::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qstylekitstyle.html#tr

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
    #  QString QStyleKitStyle::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN14QStyleKitStyle2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QStyleKitStyle'

  #  A C++ QStyleKitStyle Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QStyleKitStyle'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QStyleKitStyle::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qstylekitstyle.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QStyleKitStyle::metaObject() const
    address = self.uglySide.call('ritual_ZNK14QStyleKitStyle10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def stylePath(self) -> str:
    """
    Calls Qt's 'QString QStyleKitStyle::stylePath() const'.

    Qt's own words: https://doc.qt.io/qt-6/qstylekitstyle.html#stylePath

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QStyleKitStyle::stylePath() const
    return self.uglySide.call('ritual_ZNK14QStyleKitStyle9stylePathEv')

  def themeName(self) -> str:
    """
    Calls Qt's 'QString QStyleKitStyle::themeName() const'.

    Qt's own words: https://doc.qt.io/qt-6/qstylekitstyle.html#themeName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QStyleKitStyle::themeName() const
    return self.uglySide.call('ritual_ZNK14QStyleKitStyle9themeNameEv')

  def availableThemeNames(self) -> QStringList:
    """
    Calls Qt's 'QStringList QStyleKitStyle::availableThemeNames() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qstylekitstyle.html#availableThemeNames

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QStyleKitStyle::availableThemeNames() const
    address = self.uglySide.call(
        'ritual_ZNK14QStyleKitStyle19availableThemeNamesEv',
    )
    return QStringList._cuteOwning(address)

  def customThemeNames(self) -> QStringList:
    """
    Calls Qt's 'QStringList QStyleKitStyle::customThemeNames() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qstylekitstyle.html#customThemeNames

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QStyleKitStyle::customThemeNames() const
    address = self.uglySide.call(
        'ritual_ZNK14QStyleKitStyle16customThemeNamesEv',
    )
    return QStringList._cuteOwning(address)

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
    Calls Qt's 'QRect QStyleKitStyle::subElementRect(SubElement r, const
    QStyleOption *opt, const QWidget *widget) const'.

    Qt's own words: https://doc.qt.io/qt-6/qstylekitstyle.html#subElementRect

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
    #  QRect QStyleKitStyle::subElementRect(SubElement r, const QStyleOption
    #      *opt, const QWidget *widget) const
    ritual = (
        'ritual_ZNK14QStyleKitStyle14subElementRectEN6QStyle10SubElementEPK'
        '12QStyleOptionPK7QWidget')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK14QStyleKitStyle14subElementRectEN6QStyle10SubElem'
          'entEPK12QStyleOptionPK7QWidget')
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
    Calls Qt's 'SubControl
    QStyleKitStyle::hitTestComplexControl(ComplexControl cc, const
    QStyleOptionComplex *opt, const QPoint &pt, const QWidget *w) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qstylekitstyle.html#hitTestComplexControl

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
    #  SubControl QStyleKitStyle::hitTestComplexControl(ComplexControl cc,
    #      const QStyleOptionComplex *opt, const QPoint &pt, const QWidget
    #      *w) const
    ritual = (
        'ritual_ZNK14QStyleKitStyle21hitTestComplexControlEN6QStyle14Comple'
        'xControlEPK19QStyleOptionComplexRK6QPointPK7QWidget')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK14QStyleKitStyle21hitTestComplexControlEN6QStyle14'
          'ComplexControlEPK19QStyleOptionComplexRK6QPointPK7QWidget')
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
    Calls Qt's 'QRect QStyleKitStyle::subControlRect(ComplexControl cc, const
    QStyleOptionComplex *opt, SubControl sc, const QWidget *w) const'.

    Qt's own words: https://doc.qt.io/qt-6/qstylekitstyle.html#subControlRect

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
    #  QRect QStyleKitStyle::subControlRect(ComplexControl cc, const
    #      QStyleOptionComplex *opt, SubControl sc, const QWidget *w) const
    ritual = (
        'ritual_ZNK14QStyleKitStyle14subControlRectEN6QStyle14ComplexContro'
        'lEPK19QStyleOptionComplexNS0_10SubControlEPK7QWidget')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK14QStyleKitStyle14subControlRectEN6QStyle14Complex'
          'ControlEPK19QStyleOptionComplexNS0_10SubControlEPK7QWidget')
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
    Calls Qt's 'QSize QStyleKitStyle::sizeFromContents(ContentsType ct, const
    QStyleOption *opt, const QSize &contentsSize, const QWidget *widget)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qstylekitstyle.html#sizeFromContents

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
    #  QSize QStyleKitStyle::sizeFromContents(ContentsType ct, const
    #      QStyleOption *opt, const QSize &contentsSize, const QWidget
    #      *widget) const
    ritual = (
        'ritual_ZNK14QStyleKitStyle16sizeFromContentsEN6QStyle12ContentsTyp'
        'eEPK12QStyleOptionRK5QSizePK7QWidget')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK14QStyleKitStyle16sizeFromContentsEN6QStyle12Conte'
          'ntsTypeEPK12QStyleOptionRK5QSizePK7QWidget')
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
    Calls Qt's 'int QStyleKitStyle::pixelMetric(PixelMetric m, const
    QStyleOption *opt, const QWidget *widget) const'.

    Qt's own words: https://doc.qt.io/qt-6/qstylekitstyle.html#pixelMetric

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
    #  int QStyleKitStyle::pixelMetric(PixelMetric m, const QStyleOption
    #      *opt, const QWidget *widget) const
    ritual = (
        'ritual_ZNK14QStyleKitStyle11pixelMetricEN6QStyle11PixelMetricEPK12'
        'QStyleOptionPK7QWidget')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK14QStyleKitStyle11pixelMetricEN6QStyle11PixelMetri'
          'cEPK12QStyleOptionPK7QWidget')
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
    Calls Qt's 'int QStyleKitStyle::styleHint(StyleHint sh, const
    QStyleOption *opt, const QWidget *w, QStyleHintReturn *shret) const'.

    Qt's own words: https://doc.qt.io/qt-6/qstylekitstyle.html#styleHint

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
    #  int QStyleKitStyle::styleHint(StyleHint sh, const QStyleOption *opt,
    #      const QWidget *w, QStyleHintReturn *shret) const
    ritual = (
        'ritual_ZNK14QStyleKitStyle9styleHintEN6QStyle9StyleHintEPK12QStyle'
        'OptionPK7QWidgetP16QStyleHintReturn')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK14QStyleKitStyle9styleHintEN6QStyle9StyleHintEPK12'
          'QStyleOptionPK7QWidgetP16QStyleHintReturn')
    return self.uglySide.call(
        ritual,
        sh.value, self._addressOf(opt), self._addressOf(w),
        self._addressOf(shret),
    )

  def standardPalette(self) -> QPalette:
    """
    Calls Qt's 'QPalette QStyleKitStyle::standardPalette() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qstylekitstyle.html#standardPalette

    Returns
    -------

    QPalette
      A new cute QPalette around the copy Qt gave back. Python owns it.
    """
    #  QPalette QStyleKitStyle::standardPalette() const
    ritual = 'ritual_ZNK14QStyleKitStyle15standardPaletteEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK14QStyleKitStyle15standardPaletteEv'
    address = self.uglySide.call(ritual)
    from ..QtGui import QPalette
    return QPalette._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setStylePath(self, filePath: str) -> None:
    """
    Calls Qt's 'void QStyleKitStyle::setStylePath(const QString &filePath)'.

    Qt's own words: https://doc.qt.io/qt-6/qstylekitstyle.html#setStylePath

    Parameters
    ----------

    filePath : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QStyleKitStyle::setStylePath(const QString &filePath)
    self.uglySide.call(
        'ritual_ZN14QStyleKitStyle12setStylePathERK7QString', filePath,
    )

  @overload(str)
  def setThemeName(self, themeName: str) -> None:
    """
    Calls Qt's 'void QStyleKitStyle::setThemeName(const QString &themeName)'.

    Qt's own words: https://doc.qt.io/qt-6/qstylekitstyle.html#setThemeName

    Parameters
    ----------

    themeName : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QStyleKitStyle::setThemeName(const QString &themeName)
    self.uglySide.call(
        'ritual_ZN14QStyleKitStyle12setThemeNameERK7QString', themeName,
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
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'QStyleKitStyle::QStyleKitStyle()', which
    is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qstylekitstyle.html#QStyleKitStyle
    """
    #  QStyleKitStyle::QStyleKitStyle()
    self._noteCreation(QStyleKitStyle, lambda: Rituals.call(
        'ritual_ZN14QStyleKitStyleC1Ev',
    ))

  @overload(str)
  def __init__(self, filePath: str) -> None:
    """
    Notes what was given, for Qt's 'QStyleKitStyle::QStyleKitStyle(const
    QString &filePath)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qstylekitstyle.html#QStyleKitStyle

    Parameters
    ----------

    filePath : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  QStyleKitStyle::QStyleKitStyle(const QString &filePath)
    self._noteCreation(QStyleKitStyle, lambda: Rituals.call(
        'ritual_ZN14QStyleKitStyleC1ERK7QString', filePath,
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
    Calls Qt's 'void QStyleKitStyle::drawPrimitive(PrimitiveElement pe, const
    QStyleOption *opt, QPainter *p, const QWidget *w) const'.

    Qt's own words: https://doc.qt.io/qt-6/qstylekitstyle.html#drawPrimitive

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
    #  void QStyleKitStyle::drawPrimitive(PrimitiveElement pe, const
    #      QStyleOption *opt, QPainter *p, const QWidget *w) const
    ritual = (
        'ritual_ZNK14QStyleKitStyle13drawPrimitiveEN6QStyle16PrimitiveEleme'
        'ntEPK12QStyleOptionP8QPainterPK7QWidget')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK14QStyleKitStyle13drawPrimitiveEN6QStyle16Primitiv'
          'eElementEPK12QStyleOptionP8QPainterPK7QWidget')
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
    Calls Qt's 'void QStyleKitStyle::drawControl(ControlElement element,
    const QStyleOption *opt, QPainter *p, const QWidget *w) const'.

    Qt's own words: https://doc.qt.io/qt-6/qstylekitstyle.html#drawControl

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
    #  void QStyleKitStyle::drawControl(ControlElement element, const
    #      QStyleOption *opt, QPainter *p, const QWidget *w) const
    ritual = (
        'ritual_ZNK14QStyleKitStyle11drawControlEN6QStyle14ControlElementEP'
        'K12QStyleOptionP8QPainterPK7QWidget')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK14QStyleKitStyle11drawControlEN6QStyle14ControlEle'
          'mentEPK12QStyleOptionP8QPainterPK7QWidget')
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
    Calls Qt's 'void QStyleKitStyle::drawComplexControl(ComplexControl cc,
    const QStyleOptionComplex *opt, QPainter *p, const QWidget *w) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qstylekitstyle.html#drawComplexControl

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
    #  void QStyleKitStyle::drawComplexControl(ComplexControl cc, const
    #      QStyleOptionComplex *opt, QPainter *p, const QWidget *w) const
    ritual = (
        'ritual_ZNK14QStyleKitStyle18drawComplexControlEN6QStyle14ComplexCo'
        'ntrolEPK19QStyleOptionComplexP8QPainterPK7QWidget')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK14QStyleKitStyle18drawComplexControlEN6QStyle14Com'
          'plexControlEPK19QStyleOptionComplexP8QPainterPK7QWidget')
    self.uglySide.call(
        ritual,
        cc.value, self._addressOf(opt), self._addressOf(p),
        self._addressOf(w),
    )

  @overload(QWidget)
  @overload(NoneType)
  def polish(self, widget: Optional[QWidget]) -> None:
    """
    Calls Qt's 'void QStyleKitStyle::polish(QWidget *widget)'.

    Qt's own words: https://doc.qt.io/qt-6/qstylekitstyle.html#polish

    Parameters
    ----------

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QStyleKitStyle::polish(QWidget *widget)
    ritual = 'ritual_ZN14QStyleKitStyle6polishEP7QWidget'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN14QStyleKitStyle6polishEP7QWidget'
    self.uglySide.call(ritual, self._addressOf(widget))

  @overload(QApplication)
  def polish(self, application: Optional[QApplication]) -> None:
    """
    Calls Qt's 'void QStyleKitStyle::polish(QApplication *application)'.

    Qt's own words: https://doc.qt.io/qt-6/qstylekitstyle.html#polish

    Parameters
    ----------

    application : Optional[QApplication]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QStyleKitStyle::polish(QApplication *application)
    ritual = 'ritual_ZN14QStyleKitStyle6polishEP12QApplication'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN14QStyleKitStyle6polishEP12QApplication'
    self.uglySide.call(ritual, self._addressOf(application))

  @overload(QWidget)
  @overload(NoneType)
  def unpolish(self, widget: Optional[QWidget]) -> None:
    """
    Calls Qt's 'void QStyleKitStyle::unpolish(QWidget *widget)'.

    Qt's own words: https://doc.qt.io/qt-6/qstylekitstyle.html#unpolish

    Parameters
    ----------

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QStyleKitStyle::unpolish(QWidget *widget)
    ritual = 'ritual_ZN14QStyleKitStyle8unpolishEP7QWidget'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN14QStyleKitStyle8unpolishEP7QWidget'
    self.uglySide.call(ritual, self._addressOf(widget))

  @overload(QApplication)
  def unpolish(self, application: Optional[QApplication]) -> None:
    """
    Calls Qt's 'void QStyleKitStyle::unpolish(QApplication *application)'.

    Qt's own words: https://doc.qt.io/qt-6/qstylekitstyle.html#unpolish

    Parameters
    ----------

    application : Optional[QApplication]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QStyleKitStyle::unpolish(QApplication *application)
    ritual = 'ritual_ZN14QStyleKitStyle8unpolishEP12QApplication'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN14QStyleKitStyle8unpolishEP12QApplication'
    self.uglySide.call(ritual, self._addressOf(application))

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
    Calls Qt's 'bool QStyleKitStyle::eventFilter(QObject *watched, QEvent
    *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qstylekitstyle.html#eventFilter

    Parameters
    ----------

    watched : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    event : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QStyleKitStyle::eventFilter(QObject *watched, QEvent *event)
    ritual = 'ritual_ZN14QStyleKitStyle11eventFilterEP7QObjectP6QEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN14QStyleKitStyle11eventFilterEP7QObjectP6QEvent'
    return self.uglySide.call(
        ritual, self._addressOf(watched, 'QObject'), self._addressOf(event),
    )

  @overload(QEvent)
  @overload(NoneType)
  def event(self, event: Optional[QEvent]) -> bool:
    """
    Calls Qt's 'bool QStyleKitStyle::event(QEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qstylekitstyle.html#event

    Parameters
    ----------

    event : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QStyleKitStyle::event(QEvent *event)
    ritual = 'ritual_ZN14QStyleKitStyle5eventEP6QEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN14QStyleKitStyle5eventEP6QEvent'
    return self.uglySide.call(ritual, self._addressOf(event))

  @overload(str)
  def stylePathChanged(self, stylePath: str) -> None:
    """
    Calls Qt's 'void QStyleKitStyle::stylePathChanged(const QString
    &stylePath)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qstylekitstyle.html#stylePathChanged

    Parameters
    ----------

    stylePath : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QStyleKitStyle::stylePathChanged(const QString &stylePath)
    self.uglySide.call(
        'ritual_ZN14QStyleKitStyle16stylePathChangedERK7QString', stylePath,
    )

  @overload(str)
  def themeNameChanged(self, themeName: str) -> None:
    """
    Calls Qt's 'void QStyleKitStyle::themeNameChanged(const QString
    &themeName)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qstylekitstyle.html#themeNameChanged

    Parameters
    ----------

    themeName : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QStyleKitStyle::themeNameChanged(const QString &themeName)
    self.uglySide.call(
        'ritual_ZN14QStyleKitStyle16themeNameChangedERK7QString', themeName,
    )

  @overload(QStringList)
  def availableThemeNamesChanged(
      self,
      availableThemeNames: QStringList,
  ) -> None:
    """
    Calls Qt's 'void QStyleKitStyle::availableThemeNamesChanged(const
    QStringList &availableThemeNames)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qstylekitstyle.html#availableThemeNamesChanged

    Parameters
    ----------

    availableThemeNames : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QStyleKitStyle::availableThemeNamesChanged(const QStringList
    #      &availableThemeNames)
    self.uglySide.call(
        'ritual_ZN14QStyleKitStyle26availableThemeNamesChangedERK5QListI7QS'
        'tringE',
        self._valueOf(availableThemeNames),
    )

  @overload(QStringList)
  def customThemeNamesChanged(self, customThemeNames: QStringList) -> None:
    """
    Calls Qt's 'void QStyleKitStyle::customThemeNamesChanged(const
    QStringList &customThemeNames)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qstylekitstyle.html#customThemeNamesChanged

    Parameters
    ----------

    customThemeNames : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QStyleKitStyle::customThemeNamesChanged(const QStringList
    #      &customThemeNames)
    self.uglySide.call(
        'ritual_ZN14QStyleKitStyle23customThemeNamesChangedERK5QListI7QStri'
        'ngE',
        self._valueOf(customThemeNames),
    )

  def d_func(self) -> Optional[QStyleKitStylePrivate]:
    """
    Calls Qt's 'QStyleKitStylePrivate *QStyleKitStyle::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qstylekitstyle.html#d_func

    Returns
    -------

    Optional[QStyleKitStylePrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QStyleKitStylePrivate *QStyleKitStyle::d_func()
    address = self.uglySide.call('ritual_ZN14QStyleKitStyle6d_funcEv')
    from . import QStyleKitStylePrivate
    return QStyleKitStylePrivate._cuteAt(address)
