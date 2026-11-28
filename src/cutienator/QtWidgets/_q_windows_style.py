"""
QWindowsStyle binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/6.12.0/QtWidgets/private/qwindowsstyle_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QWindowsStyle to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject
from . import QCommonStyle, QStyle

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QEvent, QMetaObject, QRect, QSize
  from ..QtGui import QIcon, QPainter, QPixmap
  from . import QApplication, QStyleHintReturn, QStyleOption
  from . import QStyleOptionComplex, QWidget, QWindowsStylePrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QApplication = WAIT['QApplication']
  QEvent = WAIT['QEvent']
  QPainter = WAIT['QPainter']
  QSize = WAIT['QSize']
  QStyleHintReturn = WAIT['QStyleHintReturn']
  QStyleOption = WAIT['QStyleOption']
  QStyleOptionComplex = WAIT['QStyleOptionComplex']
  QWidget = WAIT['QWidget']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QWindowsStyle(QCommonStyle):
  """
  The cute side of Qt's QWindowsStyle: a plain Python object standing in
  front of one C++ QWindowsStyle.

  It is built on the cute 'QCommonStyle', as Qt's QWindowsStyle is built on
  Qt's QCommonStyle, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QWindowsStyle that has a ritual and that Python can
  call so far, 15 names in all: 'metaObject', 'tr', 'polish', 'unpolish',
  'drawPrimitive', 'drawControl', 'subElementRect', 'drawComplexControl',
  'sizeFromContents', 'pixelMetric', 'styleHint', 'standardPixmap',
  'standardIcon', 'eventFilter', 'd_func'. It can be made from Python, in 1
  way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QWindowsStyle::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QWindowsStyle::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QWindowsStyle::~QWindowsStyle()': the destructor: Python never
    removes a C++ QWindowsStyle.
  - Qt's 'void QWindowsStyle::polish(QPalette &a0)': takes a type Python has
    no way to hand over yet.
  - Qt's 'QWindowsStyle::QWindowsStyle(QWindowsStylePrivate &dd)': takes a
    type Python has no way to hand over yet.
  - Qt's 'const QWindowsStylePrivate *QWindowsStyle::d_func() const': takes
    in Python what 'QWindowsStylePrivate *QWindowsStyle::d_func()' takes.

  What has no ritual
  ------------------

  6 of the 30 functions Qt declares: 4 forbidden; 2 not a gap.

  What to expect
  --------------

  - The C++ QWindowsStyle is created at the first use, not by
    'QWindowsStyle(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QWindowsStyle.
  - Qt tells when it has removed the C++ QWindowsStyle. Every call on the
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
    Calls Qt's 'QString QWindowsStyle::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qwindowsstyle.html#tr

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
    #  QString QWindowsStyle::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN13QWindowsStyle2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QWindowsStyle'

  #  A C++ QWindowsStyle Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QWindowsStyle'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QWindowsStyle::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwindowsstyle.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QWindowsStyle::metaObject() const
    address = self.uglySide.call('ritual_ZNK13QWindowsStyle10metaObjectEv')
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
    Calls Qt's 'QRect QWindowsStyle::subElementRect(SubElement r, const
    QStyleOption *opt, const QWidget *widget) const'.

    Qt's own words: https://doc.qt.io/qt-6/qwindowsstyle.html#subElementRect

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
    #  QRect QWindowsStyle::subElementRect(SubElement r, const QStyleOption
    #      *opt, const QWidget *widget) const
    ritual = (
        'ritual_ZNK13QWindowsStyle14subElementRectEN6QStyle10SubElementEPK1'
        '2QStyleOptionPK7QWidget')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK13QWindowsStyle14subElementRectEN6QStyle10SubEleme'
          'ntEPK12QStyleOptionPK7QWidget')
    address = self.uglySide.call(
        ritual, r.value, self._addressOf(opt), self._addressOf(widget),
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
    Calls Qt's 'QSize QWindowsStyle::sizeFromContents(ContentsType ct, const
    QStyleOption *opt, const QSize &contentsSize, const QWidget *widget)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwindowsstyle.html#sizeFromContents

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
    #  QSize QWindowsStyle::sizeFromContents(ContentsType ct, const
    #      QStyleOption *opt, const QSize &contentsSize, const QWidget
    #      *widget) const
    ritual = (
        'ritual_ZNK13QWindowsStyle16sizeFromContentsEN6QStyle12ContentsType'
        'EPK12QStyleOptionRK5QSizePK7QWidget')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK13QWindowsStyle16sizeFromContentsEN6QStyle12Conten'
          'tsTypeEPK12QStyleOptionRK5QSizePK7QWidget')
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
      pm: QStyle.PixelMetric,
      option: Optional[QStyleOption] = None,
      widget: Optional[QWidget] = None,
  ) -> int:
    """
    Calls Qt's 'int QWindowsStyle::pixelMetric(PixelMetric pm, const
    QStyleOption *option, const QWidget *widget) const'.

    Qt's own words: https://doc.qt.io/qt-6/qwindowsstyle.html#pixelMetric

    Parameters
    ----------

    pm : QStyle.PixelMetric
      Passed on as its number.

    option : Optional[QStyleOption]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  int QWindowsStyle::pixelMetric(PixelMetric pm, const QStyleOption
    #      *option, const QWidget *widget) const
    ritual = (
        'ritual_ZNK13QWindowsStyle11pixelMetricEN6QStyle11PixelMetricEPK12Q'
        'StyleOptionPK7QWidget')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK13QWindowsStyle11pixelMetricEN6QStyle11PixelMetric'
          'EPK12QStyleOptionPK7QWidget')
    return self.uglySide.call(
        ritual, pm.value, self._addressOf(option), self._addressOf(widget),
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
      hint: QStyle.StyleHint,
      opt: Optional[QStyleOption] = None,
      widget: Optional[QWidget] = None,
      returnData: Optional[QStyleHintReturn] = None,
  ) -> int:
    """
    Calls Qt's 'int QWindowsStyle::styleHint(StyleHint hint, const
    QStyleOption *opt, const QWidget *widget, QStyleHintReturn *returnData)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qwindowsstyle.html#styleHint

    Parameters
    ----------

    hint : QStyle.StyleHint
      Passed on as its number.

    opt : Optional[QStyleOption]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    returnData : Optional[QStyleHintReturn]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  int QWindowsStyle::styleHint(StyleHint hint, const QStyleOption *opt,
    #      const QWidget *widget, QStyleHintReturn *returnData) const
    ritual = (
        'ritual_ZNK13QWindowsStyle9styleHintEN6QStyle9StyleHintEPK12QStyleO'
        'ptionPK7QWidgetP16QStyleHintReturn')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK13QWindowsStyle9styleHintEN6QStyle9StyleHintEPK12Q'
          'StyleOptionPK7QWidgetP16QStyleHintReturn')
    return self.uglySide.call(
        ritual,
        hint.value, self._addressOf(opt), self._addressOf(widget),
        self._addressOf(returnData),
    )

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
    Calls Qt's 'QPixmap QWindowsStyle::standardPixmap(StandardPixmap
    standardPixmap, const QStyleOption *opt, const QWidget *widget) const'.

    Qt's own words: https://doc.qt.io/qt-6/qwindowsstyle.html#standardPixmap

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
    #  QPixmap QWindowsStyle::standardPixmap(StandardPixmap standardPixmap,
    #      const QStyleOption *opt, const QWidget *widget) const
    ritual = (
        'ritual_ZNK13QWindowsStyle14standardPixmapEN6QStyle14StandardPixmap'
        'EPK12QStyleOptionPK7QWidget')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK13QWindowsStyle14standardPixmapEN6QStyle14Standard'
          'PixmapEPK12QStyleOptionPK7QWidget')
    address = self.uglySide.call(
        ritual,
        standardPixmap.value, self._addressOf(opt), self._addressOf(widget),
    )
    from ..QtGui import QPixmap
    return QPixmap._cuteOwning(address)

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
    Calls Qt's 'QIcon QWindowsStyle::standardIcon(StandardPixmap
    standardIcon, const QStyleOption *option, const QWidget *widget) const'.

    Qt's own words: https://doc.qt.io/qt-6/qwindowsstyle.html#standardIcon

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
    #  QIcon QWindowsStyle::standardIcon(StandardPixmap standardIcon, const
    #      QStyleOption *option, const QWidget *widget) const
    ritual = (
        'ritual_ZNK13QWindowsStyle12standardIconEN6QStyle14StandardPixmapEP'
        'K12QStyleOptionPK7QWidget')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK13QWindowsStyle12standardIconEN6QStyle14StandardPi'
          'xmapEPK12QStyleOptionPK7QWidget')
    address = self.uglySide.call(
        ritual,
        standardIcon.value, self._addressOf(option), self._addressOf(widget),
    )
    from ..QtGui import QIcon
    return QIcon._cuteOwning(address)

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
    Notes what was given, for Qt's 'QWindowsStyle::QWindowsStyle()', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qwindowsstyle.html#QWindowsStyle
    """
    #  QWindowsStyle::QWindowsStyle()
    self._noteCreation(QWindowsStyle, lambda: Rituals.call(
        'ritual_ZN13QWindowsStyleC1Ev',
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
  def polish(self, a0: Optional[QApplication]) -> None:
    """
    Calls Qt's 'void QWindowsStyle::polish(QApplication *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qwindowsstyle.html#polish

    Parameters
    ----------

    a0 : Optional[QApplication]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWindowsStyle::polish(QApplication *a0)
    ritual = 'ritual_ZN13QWindowsStyle6polishEP12QApplication'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN13QWindowsStyle6polishEP12QApplication'
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(QWidget)
  def polish(self, a0: Optional[QWidget]) -> None:
    """
    Calls Qt's 'void QWindowsStyle::polish(QWidget *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qwindowsstyle.html#polish

    Parameters
    ----------

    a0 : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWindowsStyle::polish(QWidget *a0)
    ritual = 'ritual_ZN13QWindowsStyle6polishEP7QWidget'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN13QWindowsStyle6polishEP7QWidget'
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(QApplication)
  @overload(NoneType)
  def unpolish(self, a0: Optional[QApplication]) -> None:
    """
    Calls Qt's 'void QWindowsStyle::unpolish(QApplication *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qwindowsstyle.html#unpolish

    Parameters
    ----------

    a0 : Optional[QApplication]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWindowsStyle::unpolish(QApplication *a0)
    ritual = 'ritual_ZN13QWindowsStyle8unpolishEP12QApplication'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN13QWindowsStyle8unpolishEP12QApplication'
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(QWidget)
  def unpolish(self, a0: Optional[QWidget]) -> None:
    """
    Calls Qt's 'void QWindowsStyle::unpolish(QWidget *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qwindowsstyle.html#unpolish

    Parameters
    ----------

    a0 : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWindowsStyle::unpolish(QWidget *a0)
    ritual = 'ritual_ZN13QWindowsStyle8unpolishEP7QWidget'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN13QWindowsStyle8unpolishEP7QWidget'
    self.uglySide.call(ritual, self._addressOf(a0))

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
    Calls Qt's 'void QWindowsStyle::drawPrimitive(PrimitiveElement pe, const
    QStyleOption *opt, QPainter *p, const QWidget *w) const'.

    Qt's own words: https://doc.qt.io/qt-6/qwindowsstyle.html#drawPrimitive

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
    #  void QWindowsStyle::drawPrimitive(PrimitiveElement pe, const
    #      QStyleOption *opt, QPainter *p, const QWidget *w) const
    ritual = (
        'ritual_ZNK13QWindowsStyle13drawPrimitiveEN6QStyle16PrimitiveElemen'
        'tEPK12QStyleOptionP8QPainterPK7QWidget')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK13QWindowsStyle13drawPrimitiveEN6QStyle16Primitive'
          'ElementEPK12QStyleOptionP8QPainterPK7QWidget')
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
    Calls Qt's 'void QWindowsStyle::drawControl(ControlElement element, const
    QStyleOption *opt, QPainter *p, const QWidget *w) const'.

    Qt's own words: https://doc.qt.io/qt-6/qwindowsstyle.html#drawControl

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
    #  void QWindowsStyle::drawControl(ControlElement element, const
    #      QStyleOption *opt, QPainter *p, const QWidget *w) const
    ritual = (
        'ritual_ZNK13QWindowsStyle11drawControlEN6QStyle14ControlElementEPK'
        '12QStyleOptionP8QPainterPK7QWidget')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK13QWindowsStyle11drawControlEN6QStyle14ControlElem'
          'entEPK12QStyleOptionP8QPainterPK7QWidget')
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
    Calls Qt's 'void QWindowsStyle::drawComplexControl(ComplexControl cc,
    const QStyleOptionComplex *opt, QPainter *p, const QWidget *w) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwindowsstyle.html#drawComplexControl

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
    #  void QWindowsStyle::drawComplexControl(ComplexControl cc, const
    #      QStyleOptionComplex *opt, QPainter *p, const QWidget *w) const
    ritual = (
        'ritual_ZNK13QWindowsStyle18drawComplexControlEN6QStyle14ComplexCon'
        'trolEPK19QStyleOptionComplexP8QPainterPK7QWidget')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK13QWindowsStyle18drawComplexControlEN6QStyle14Comp'
          'lexControlEPK19QStyleOptionComplexP8QPainterPK7QWidget')
    self.uglySide.call(
        ritual,
        cc.value, self._addressOf(opt), self._addressOf(p),
        self._addressOf(w),
    )

  @overload(QObject, QEvent)
  @overload(QObject, NoneType)
  @overload(NoneType, QEvent)
  @overload(NoneType, NoneType)
  def eventFilter(self, o: Optional[QObject], e: Optional[QEvent]) -> bool:
    """
    Calls Qt's 'bool QWindowsStyle::eventFilter(QObject *o, QEvent *e)'.

    Qt's own words: https://doc.qt.io/qt-6/qwindowsstyle.html#eventFilter

    Parameters
    ----------

    o : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    e : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QWindowsStyle::eventFilter(QObject *o, QEvent *e)
    ritual = 'ritual_ZN13QWindowsStyle11eventFilterEP7QObjectP6QEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN13QWindowsStyle11eventFilterEP7QObjectP6QEvent'
    return self.uglySide.call(
        ritual, self._addressOf(o, 'QObject'), self._addressOf(e),
    )

  def d_func(self) -> Optional[QWindowsStylePrivate]:
    """
    Calls Qt's 'QWindowsStylePrivate *QWindowsStyle::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qwindowsstyle.html#d_func

    Returns
    -------

    Optional[QWindowsStylePrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWindowsStylePrivate *QWindowsStyle::d_func()
    address = self.uglySide.call('ritual_ZN13QWindowsStyle6d_funcEv')
    from . import QWindowsStylePrivate
    return QWindowsStylePrivate._cuteAt(address)
