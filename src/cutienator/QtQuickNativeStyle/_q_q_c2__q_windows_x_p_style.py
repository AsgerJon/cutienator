"""
QQC2::QWindowsXPStyle binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickNativeStyle/6.12.0/QtQuickNativeStyle/private/qquickwindowsxpstyle_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQC2::QWindowsXPStyle to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from . import QQC2
from ..QtWidgets import QStyle

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMargins, QMetaObject, QRect, QSize
  from ..QtGui import QIcon, QPainter, QPalette, QPixmap
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPainter = WAIT['QPainter']
  QSize = WAIT['QSize']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QWindowsXPStyle(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQC2::QWindowsXPStyle: a plain Python object standing
  in front of one C++ QQC2::QWindowsXPStyle.

  What exists
  -----------

  Every function of Qt's QQC2::QWindowsXPStyle that has a ritual and that
  Python can call so far, 14 names in all: 'metaObject', 'tr',
  'drawPrimitive', 'drawControl', 'subElementRect', 'subControlRect',
  'drawComplexControl', 'sizeFromContents', 'pixelMetric', 'styleHint',
  'standardPalette', 'standardPixmap', 'standardIcon', 'ninePatchMargins'. It
  can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQC2::QWindowsXPStyle::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QQC2::QWindowsXPStyle::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QQC2::QWindowsXPStyle::QWindowsXPStyle(QWindowsXPStylePrivate
    &dd)': takes a type Python has no way to hand over yet.
  - Qt's 'QQC2::QWindowsXPStyle::~QWindowsXPStyle()': the destructor: Python
    never removes a C++ QQC2::QWindowsXPStyle.
  - Qt's 'QWindowsXPStylePrivate *QQC2::QWindowsXPStyle::d_func()': gives
    'QWindowsXPStylePrivate', which has no cute class yet.
  - Qt's 'const QWindowsXPStylePrivate *QQC2::QWindowsXPStyle::d_func()
    const': gives 'QWindowsXPStylePrivate', which has no cute class yet.

  What has no ritual
  ------------------

  6 of the 27 functions Qt declares: 4 forbidden; 2 not a gap.

  What to expect
  --------------

  - The C++ QQC2::QWindowsXPStyle is created at the first use, not by
    'QQC2::QWindowsXPStyle(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQC2::QWindowsXPStyle.
  - Qt tells when it has removed the C++ QQC2::QWindowsXPStyle. Every call on
    the cute object, and every use of it as an argument, then raises
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
    Calls Qt's 'QString QQC2::QWindowsXPStyle::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qqc2-qwindowsxpstyle.html#tr

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
    #  QString QQC2::QWindowsXPStyle::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN4QQC215QWindowsXPStyle2trEPKcS2_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQC2::QWindowsXPStyle'

  #  A C++ QQC2::QWindowsXPStyle Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQC2_QWindowsXPStyle'

  #  The functions Qt calls itself that QQC2::QWindowsXPStyle is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'drawPrimitive': (
          ('_ZNK4QQC215QWindowsXPStyle13drawPrimitiveENS_6QStyle16Primitive'
           'ElementEPKNS_12QStyleOptionEP8QPainter',
           ('nothing', 'nothing', ''),
           (
               ('int', 'enum', 'QtWidgets:QStyle.PrimitiveElement'),
               ('address', 'address',
                'QtQuickNativeStyle:QQC2.QStyleOption'),
               ('address', 'address', 'QtGui:QPainter'),
           )),
      ),
      'drawControl': (
          ('_ZNK4QQC215QWindowsXPStyle11drawControlENS_6QStyle14ControlElem'
           'entEPKNS_12QStyleOptionEP8QPainter',
           ('nothing', 'nothing', ''),
           (
               ('int', 'enum', 'QtWidgets:QStyle.ControlElement'),
               ('address', 'address',
                'QtQuickNativeStyle:QQC2.QStyleOption'),
               ('address', 'address', 'QtGui:QPainter'),
           )),
      ),
      'subElementRect': (
          ('_ZNK4QQC215QWindowsXPStyle14subElementRectENS_6QStyle10SubEleme'
           'ntEPKNS_12QStyleOptionE',
           ('address', 'value', 'QtCore:QRect'),
           (
               ('int', 'enum', 'QtWidgets:QStyle.SubElement'),
               ('address', 'address',
                'QtQuickNativeStyle:QQC2.QStyleOption'),
           )),
      ),
      'subControlRect': (
          ('_ZNK4QQC215QWindowsXPStyle14subControlRectENS_6QStyle14ComplexC'
           'ontrolEPKNS_19QStyleOptionComplexENS1_10SubControlE',
           ('address', 'value', 'QtCore:QRect'),
           (
               ('int', 'enum', 'QtWidgets:QStyle.ComplexControl'),
               ('address', 'address',
                'QtQuickNativeStyle:QQC2.QStyleOptionComplex'),
               ('int', 'enum', 'QtWidgets:QStyle.SubControl'),
           )),
      ),
      'drawComplexControl': (
          ('_ZNK4QQC215QWindowsXPStyle18drawComplexControlENS_6QStyle14Comp'
           'lexControlEPKNS_19QStyleOptionComplexEP8QPainter',
           ('nothing', 'nothing', ''),
           (
               ('int', 'enum', 'QtWidgets:QStyle.ComplexControl'),
               ('address', 'address',
                'QtQuickNativeStyle:QQC2.QStyleOptionComplex'),
               ('address', 'address', 'QtGui:QPainter'),
           )),
      ),
      'sizeFromContents': (
          ('_ZNK4QQC215QWindowsXPStyle16sizeFromContentsENS_6QStyle12Conten'
           'tsTypeEPKNS_12QStyleOptionERK5QSize',
           ('address', 'value', 'QtCore:QSize'),
           (
               ('int', 'enum', 'QtWidgets:QStyle.ContentsType'),
               ('address', 'address',
                'QtQuickNativeStyle:QQC2.QStyleOption'),
               ('address', 'value', 'QtCore:QSize'),
           )),
      ),
      'pixelMetric': (
          ('_ZNK4QQC215QWindowsXPStyle11pixelMetricENS_6QStyle11PixelMetric'
           'EPKNS_12QStyleOptionE',
           ('int', 'number', ''),
           (
               ('int', 'enum', 'QtWidgets:QStyle.PixelMetric'),
               ('address', 'address',
                'QtQuickNativeStyle:QQC2.QStyleOption'),
           )),
      ),
      'styleHint': (
          ('_ZNK4QQC215QWindowsXPStyle9styleHintENS_6QStyle9StyleHintEPKNS_'
           '12QStyleOptionEPNS_16QStyleHintReturnE',
           ('int', 'number', ''),
           (
               ('int', 'enum', 'QtWidgets:QStyle.StyleHint'),
               ('address', 'address',
                'QtQuickNativeStyle:QQC2.QStyleOption'),
               ('address', 'address',
                'QtQuickNativeStyle:QQC2.QStyleHintReturn'),
           )),
      ),
      'standardPixmap': (
          ('_ZNK4QQC215QWindowsXPStyle14standardPixmapENS_6QStyle14Standard'
           'PixmapEPKNS_12QStyleOptionE',
           ('address', 'value', 'QtGui:QPixmap'),
           (
               ('int', 'enum', 'QtWidgets:QStyle.StandardPixmap'),
               ('address', 'address',
                'QtQuickNativeStyle:QQC2.QStyleOption'),
           )),
      ),
      'standardIcon': (
          ('_ZNK4QQC215QWindowsXPStyle12standardIconENS_6QStyle14StandardPi'
           'xmapEPKNS_12QStyleOptionE',
           ('address', 'value', 'QtGui:QIcon'),
           (
               ('int', 'enum', 'QtWidgets:QStyle.StandardPixmap'),
               ('address', 'address',
                'QtQuickNativeStyle:QQC2.QStyleOption'),
           )),
      ),
      'ninePatchMargins': (
          ('_ZNK4QQC215QWindowsXPStyle16ninePatchMarginsENS_6QStyle14Comple'
           'xControlEPKNS_19QStyleOptionComplexERK5QSize',
           ('address', 'value', 'QtCore:QMargins'),
           (
               ('int', 'enum',
                'QtQuickNativeStyle:QQC2.QStyle.ComplexControl'),
               ('address', 'address',
                'QtQuickNativeStyle:QQC2.QStyleOptionComplex'),
               ('address', 'value', 'QtCore:QSize'),
           )),
      ),
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQC2::QWindowsXPStyle::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqc2-qwindowsxpstyle.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQC2::QWindowsXPStyle::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK4QQC215QWindowsXPStyle10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  @overload(QStyle.SubElement, WAIT['QQC2.QStyleOption'])
  @overload(QStyle.SubElement, NoneType)
  def subElementRect(
      self,
      r: QStyle.SubElement,
      option: Optional[QQC2.QStyleOption],
  ) -> QRect:
    """
    Calls Qt's 'QRect QQC2::QWindowsXPStyle::subElementRect(SubElement r,
    const QStyleOption *option) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqc2-qwindowsxpstyle.html#subElementRect

    Parameters
    ----------

    r : QStyle.SubElement
      Passed on as its number.

    option : Optional[QQC2.QStyleOption]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect QQC2::QWindowsXPStyle::subElementRect(SubElement r, const
    #      QStyleOption *option) const
    ritual = (
        'ritual_ZNK4QQC215QWindowsXPStyle14subElementRectENS_6QStyle10SubEl'
        'ementEPKNS_12QStyleOptionE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK4QQC215QWindowsXPStyle14subElementRectENS_6QStyle1'
          '0SubElementEPKNS_12QStyleOptionE')
    address = self.uglySide.call(ritual, r.value, self._addressOf(option))
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

  @overload(
      QStyle.ComplexControl, WAIT['QQC2.QStyleOptionComplex'],
      QStyle.SubControl,
  )
  @overload(QStyle.ComplexControl, NoneType, QStyle.SubControl)
  def subControlRect(
      self,
      cc: QStyle.ComplexControl,
      option: Optional[QQC2.QStyleOptionComplex],
      sc: QStyle.SubControl,
  ) -> QRect:
    """
    Calls Qt's 'QRect QQC2::QWindowsXPStyle::subControlRect(ComplexControl
    cc, const QStyleOptionComplex *option, SubControl sc) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqc2-qwindowsxpstyle.html#subControlRect

    Parameters
    ----------

    cc : QStyle.ComplexControl
      Passed on as its number.

    option : Optional[QQC2.QStyleOptionComplex]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    sc : QStyle.SubControl
      Passed on as its number.

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect QQC2::QWindowsXPStyle::subControlRect(ComplexControl cc, const
    #      QStyleOptionComplex *option, SubControl sc) const
    ritual = (
        'ritual_ZNK4QQC215QWindowsXPStyle14subControlRectENS_6QStyle14Compl'
        'exControlEPKNS_19QStyleOptionComplexENS1_10SubControlE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK4QQC215QWindowsXPStyle14subControlRectENS_6QStyle1'
          '4ComplexControlEPKNS_19QStyleOptionComplexENS1_10SubControlE')
    address = self.uglySide.call(
        ritual, cc.value, self._addressOf(option), sc.value,
    )
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

  @overload(QStyle.ContentsType, WAIT['QQC2.QStyleOption'], QSize)
  @overload(QStyle.ContentsType, NoneType, QSize)
  def sizeFromContents(
      self,
      ct: QStyle.ContentsType,
      option: Optional[QQC2.QStyleOption],
      contentsSize: QSize,
  ) -> QSize:
    """
    Calls Qt's 'QSize QQC2::QWindowsXPStyle::sizeFromContents(ContentsType
    ct, const QStyleOption *option, const QSize &contentsSize) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqc2-qwindowsxpstyle.html#sizeFromContents

    Parameters
    ----------

    ct : QStyle.ContentsType
      Passed on as its number.

    option : Optional[QQC2.QStyleOption]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    contentsSize : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QQC2::QWindowsXPStyle::sizeFromContents(ContentsType ct, const
    #      QStyleOption *option, const QSize &contentsSize) const
    ritual = (
        'ritual_ZNK4QQC215QWindowsXPStyle16sizeFromContentsENS_6QStyle12Con'
        'tentsTypeEPKNS_12QStyleOptionERK5QSize')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK4QQC215QWindowsXPStyle16sizeFromContentsENS_6QStyl'
          'e12ContentsTypeEPKNS_12QStyleOptionERK5QSize')
    address = self.uglySide.call(
        ritual,
        ct.value, self._addressOf(option), self._valueOf(contentsSize),
    )
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  @overload(QStyle.PixelMetric)
  @overload(QStyle.PixelMetric, WAIT['QQC2.QStyleOption'])
  @overload(QStyle.PixelMetric, NoneType)
  def pixelMetric(
      self,
      pm: QStyle.PixelMetric,
      option: Optional[QQC2.QStyleOption] = None,
  ) -> int:
    """
    Calls Qt's 'int QQC2::QWindowsXPStyle::pixelMetric(PixelMetric pm, const
    QStyleOption *option) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqc2-qwindowsxpstyle.html#pixelMetric

    Parameters
    ----------

    pm : QStyle.PixelMetric
      Passed on as its number.

    option : Optional[QQC2.QStyleOption]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  int QQC2::QWindowsXPStyle::pixelMetric(PixelMetric pm, const
    #      QStyleOption *option) const
    ritual = (
        'ritual_ZNK4QQC215QWindowsXPStyle11pixelMetricENS_6QStyle11PixelMet'
        'ricEPKNS_12QStyleOptionE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK4QQC215QWindowsXPStyle11pixelMetricENS_6QStyle11Pi'
          'xelMetricEPKNS_12QStyleOptionE')
    return self.uglySide.call(ritual, pm.value, self._addressOf(option))

  @overload(QStyle.StyleHint)
  @overload(QStyle.StyleHint, WAIT['QQC2.QStyleOption'])
  @overload(QStyle.StyleHint, NoneType)
  @overload(
      QStyle.StyleHint, WAIT['QQC2.QStyleOption'],
      WAIT['QQC2.QStyleHintReturn'],
  )
  @overload(QStyle.StyleHint, WAIT['QQC2.QStyleOption'], NoneType)
  @overload(QStyle.StyleHint, NoneType, WAIT['QQC2.QStyleHintReturn'])
  @overload(QStyle.StyleHint, NoneType, NoneType)
  def styleHint(
      self,
      hint: QStyle.StyleHint,
      option: Optional[QQC2.QStyleOption] = None,
      returnData: Optional[QQC2.QStyleHintReturn] = None,
  ) -> int:
    """
    Calls Qt's 'int QQC2::QWindowsXPStyle::styleHint(StyleHint hint, const
    QStyleOption *option, QStyleHintReturn *returnData) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqc2-qwindowsxpstyle.html#styleHint

    Parameters
    ----------

    hint : QStyle.StyleHint
      Passed on as its number.

    option : Optional[QQC2.QStyleOption]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    returnData : Optional[QQC2.QStyleHintReturn]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  int QQC2::QWindowsXPStyle::styleHint(StyleHint hint, const
    #      QStyleOption *option, QStyleHintReturn *returnData) const
    ritual = (
        'ritual_ZNK4QQC215QWindowsXPStyle9styleHintENS_6QStyle9StyleHintEPK'
        'NS_12QStyleOptionEPNS_16QStyleHintReturnE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK4QQC215QWindowsXPStyle9styleHintENS_6QStyle9StyleH'
          'intEPKNS_12QStyleOptionEPNS_16QStyleHintReturnE')
    return self.uglySide.call(
        ritual,
        hint.value, self._addressOf(option), self._addressOf(returnData),
    )

  def standardPalette(self) -> QPalette:
    """
    Calls Qt's 'QPalette QQC2::QWindowsXPStyle::standardPalette() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqc2-qwindowsxpstyle.html#standardPalette

    Returns
    -------

    QPalette
      A new cute QPalette around the copy Qt gave back. Python owns it.
    """
    #  QPalette QQC2::QWindowsXPStyle::standardPalette() const
    ritual = 'ritual_ZNK4QQC215QWindowsXPStyle15standardPaletteEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK4QQC215QWindowsXPStyle15standardPaletteEv'
    address = self.uglySide.call(ritual)
    from ..QtGui import QPalette
    return QPalette._cuteOwning(address)

  @overload(QStyle.StandardPixmap, WAIT['QQC2.QStyleOption'])
  @overload(QStyle.StandardPixmap, NoneType)
  def standardPixmap(
      self,
      standardIcon: QStyle.StandardPixmap,
      option: Optional[QQC2.QStyleOption],
  ) -> QPixmap:
    """
    Calls Qt's 'QPixmap QQC2::QWindowsXPStyle::standardPixmap(StandardPixmap
    standardIcon, const QStyleOption *option) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqc2-qwindowsxpstyle.html#standardPixmap

    Parameters
    ----------

    standardIcon : QStyle.StandardPixmap
      Passed on as its number.

    option : Optional[QQC2.QStyleOption]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QPixmap
      A new cute QPixmap around the copy Qt gave back. Python owns it.
    """
    #  QPixmap QQC2::QWindowsXPStyle::standardPixmap(StandardPixmap
    #      standardIcon, const QStyleOption *option) const
    ritual = (
        'ritual_ZNK4QQC215QWindowsXPStyle14standardPixmapENS_6QStyle14Stand'
        'ardPixmapEPKNS_12QStyleOptionE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK4QQC215QWindowsXPStyle14standardPixmapENS_6QStyle1'
          '4StandardPixmapEPKNS_12QStyleOptionE')
    address = self.uglySide.call(
        ritual, standardIcon.value, self._addressOf(option),
    )
    from ..QtGui import QPixmap
    return QPixmap._cuteOwning(address)

  @overload(QStyle.StandardPixmap)
  @overload(QStyle.StandardPixmap, WAIT['QQC2.QStyleOption'])
  @overload(QStyle.StandardPixmap, NoneType)
  def standardIcon(
      self,
      standardIcon: QStyle.StandardPixmap,
      option: Optional[QQC2.QStyleOption] = None,
  ) -> QIcon:
    """
    Calls Qt's 'QIcon QQC2::QWindowsXPStyle::standardIcon(StandardPixmap
    standardIcon, const QStyleOption *option) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqc2-qwindowsxpstyle.html#standardIcon

    Parameters
    ----------

    standardIcon : QStyle.StandardPixmap
      Passed on as its number.

    option : Optional[QQC2.QStyleOption]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    Returns
    -------

    QIcon
      A new cute QIcon around the copy Qt gave back. Python owns it.
    """
    #  QIcon QQC2::QWindowsXPStyle::standardIcon(StandardPixmap standardIcon,
    #      const QStyleOption *option) const
    ritual = (
        'ritual_ZNK4QQC215QWindowsXPStyle12standardIconENS_6QStyle14Standar'
        'dPixmapEPKNS_12QStyleOptionE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK4QQC215QWindowsXPStyle12standardIconENS_6QStyle14S'
          'tandardPixmapEPKNS_12QStyleOptionE')
    address = self.uglySide.call(
        ritual, standardIcon.value, self._addressOf(option),
    )
    from ..QtGui import QIcon
    return QIcon._cuteOwning(address)

  @overload(
      QQC2.QStyle.ComplexControl, WAIT['QQC2.QStyleOptionComplex'], QSize,
  )
  @overload(QQC2.QStyle.ComplexControl, NoneType, QSize)
  def ninePatchMargins(
      self,
      cc: QQC2.QStyle.ComplexControl,
      opt: Optional[QQC2.QStyleOptionComplex],
      imageSize: QSize,
  ) -> QMargins:
    """
    Calls Qt's 'QMargins
    QQC2::QWindowsXPStyle::ninePatchMargins(QStyle::ComplexControl cc, const
    QStyleOptionComplex *opt, const QSize &imageSize) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqc2-qwindowsxpstyle.html#ninePatchMargins

    Parameters
    ----------

    cc : QQC2.QStyle.ComplexControl
      Passed on as its number.

    opt : Optional[QQC2.QStyleOptionComplex]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    imageSize : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.

    Returns
    -------

    QMargins
      A new cute QMargins around the copy Qt gave back. Python owns it.
    """
    #  QMargins
    #      QQC2::QWindowsXPStyle::ninePatchMargins(QStyle::ComplexControl cc,
    #      const QStyleOptionComplex *opt, const QSize &imageSize) const
    ritual = (
        'ritual_ZNK4QQC215QWindowsXPStyle16ninePatchMarginsENS_6QStyle14Com'
        'plexControlEPKNS_19QStyleOptionComplexERK5QSize')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK4QQC215QWindowsXPStyle16ninePatchMarginsENS_6QStyl'
          'e14ComplexControlEPKNS_19QStyleOptionComplexERK5QSize')
    address = self.uglySide.call(
        ritual, cc.value, self._addressOf(opt), self._valueOf(imageSize),
    )
    from ..QtCore import QMargins
    return QMargins._cuteOwning(address)

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
    Notes what was given, for Qt's
    'QQC2::QWindowsXPStyle::QWindowsXPStyle()', which is called at the first
    use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqc2-qwindowsxpstyle.html#QWindowsXPStyle
    """
    #  QQC2::QWindowsXPStyle::QWindowsXPStyle()
    self._noteCreation(QWindowsXPStyle, lambda: Rituals.call(
        'ritual_ZN4QQC215QWindowsXPStyleC1Ev',
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

  @overload(QStyle.PrimitiveElement, WAIT['QQC2.QStyleOption'], QPainter)
  @overload(QStyle.PrimitiveElement, WAIT['QQC2.QStyleOption'], NoneType)
  @overload(QStyle.PrimitiveElement, NoneType, QPainter)
  @overload(QStyle.PrimitiveElement, NoneType, NoneType)
  def drawPrimitive(
      self,
      pe: QStyle.PrimitiveElement,
      option: Optional[QQC2.QStyleOption],
      p: Optional[QPainter],
  ) -> None:
    """
    Calls Qt's 'void QQC2::QWindowsXPStyle::drawPrimitive(PrimitiveElement
    pe, const QStyleOption *option, QPainter *p) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqc2-qwindowsxpstyle.html#drawPrimitive

    Parameters
    ----------

    pe : QStyle.PrimitiveElement
      Passed on as its number.

    option : Optional[QQC2.QStyleOption]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    p : Optional[QPainter]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQC2::QWindowsXPStyle::drawPrimitive(PrimitiveElement pe, const
    #      QStyleOption *option, QPainter *p) const
    ritual = (
        'ritual_ZNK4QQC215QWindowsXPStyle13drawPrimitiveENS_6QStyle16Primit'
        'iveElementEPKNS_12QStyleOptionEP8QPainter')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK4QQC215QWindowsXPStyle13drawPrimitiveENS_6QStyle16'
          'PrimitiveElementEPKNS_12QStyleOptionEP8QPainter')
    self.uglySide.call(
        ritual, pe.value, self._addressOf(option), self._addressOf(p),
    )

  @overload(QStyle.ControlElement, WAIT['QQC2.QStyleOption'], QPainter)
  @overload(QStyle.ControlElement, WAIT['QQC2.QStyleOption'], NoneType)
  @overload(QStyle.ControlElement, NoneType, QPainter)
  @overload(QStyle.ControlElement, NoneType, NoneType)
  def drawControl(
      self,
      element: QStyle.ControlElement,
      option: Optional[QQC2.QStyleOption],
      p: Optional[QPainter],
  ) -> None:
    """
    Calls Qt's 'void QQC2::QWindowsXPStyle::drawControl(ControlElement
    element, const QStyleOption *option, QPainter *p) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqc2-qwindowsxpstyle.html#drawControl

    Parameters
    ----------

    element : QStyle.ControlElement
      Passed on as its number.

    option : Optional[QQC2.QStyleOption]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    p : Optional[QPainter]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQC2::QWindowsXPStyle::drawControl(ControlElement element, const
    #      QStyleOption *option, QPainter *p) const
    ritual = (
        'ritual_ZNK4QQC215QWindowsXPStyle11drawControlENS_6QStyle14ControlE'
        'lementEPKNS_12QStyleOptionEP8QPainter')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK4QQC215QWindowsXPStyle11drawControlENS_6QStyle14Co'
          'ntrolElementEPKNS_12QStyleOptionEP8QPainter')
    self.uglySide.call(
        ritual, element.value, self._addressOf(option), self._addressOf(p),
    )

  @overload(
      QStyle.ComplexControl, WAIT['QQC2.QStyleOptionComplex'], QPainter,
  )
  @overload(
      QStyle.ComplexControl, WAIT['QQC2.QStyleOptionComplex'], NoneType,
  )
  @overload(QStyle.ComplexControl, NoneType, QPainter)
  @overload(QStyle.ComplexControl, NoneType, NoneType)
  def drawComplexControl(
      self,
      cc: QStyle.ComplexControl,
      option: Optional[QQC2.QStyleOptionComplex],
      p: Optional[QPainter],
  ) -> None:
    """
    Calls Qt's 'void QQC2::QWindowsXPStyle::drawComplexControl(ComplexControl
    cc, const QStyleOptionComplex *option, QPainter *p) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqc2-qwindowsxpstyle.html#drawComplexControl

    Parameters
    ----------

    cc : QStyle.ComplexControl
      Passed on as its number.

    option : Optional[QQC2.QStyleOptionComplex]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    p : Optional[QPainter]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQC2::QWindowsXPStyle::drawComplexControl(ComplexControl cc,
    #      const QStyleOptionComplex *option, QPainter *p) const
    ritual = (
        'ritual_ZNK4QQC215QWindowsXPStyle18drawComplexControlENS_6QStyle14C'
        'omplexControlEPKNS_19QStyleOptionComplexEP8QPainter')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK4QQC215QWindowsXPStyle18drawComplexControlENS_6QSt'
          'yle14ComplexControlEPKNS_19QStyleOptionComplexEP8QPainter')
    self.uglySide.call(
        ritual, cc.value, self._addressOf(option), self._addressOf(p),
    )
