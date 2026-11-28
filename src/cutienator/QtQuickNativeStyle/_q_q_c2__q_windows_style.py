"""
QQC2::QWindowsStyle binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickNativeStyle/6.12.0/QtQuickNativeStyle/private/qquickwindowsstyle_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQC2::QWindowsStyle to be private: it declares the class in a
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

  from ..QtCore import QMetaObject, QRect, QSize, QTimerEvent
  from ..QtGui import QIcon, QPainter, QPixmap
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPainter = WAIT['QPainter']
  QSize = WAIT['QSize']
  QTimerEvent = WAIT['QTimerEvent']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QWindowsStyle(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQC2::QWindowsStyle: a plain Python object standing
  in front of one C++ QQC2::QWindowsStyle.

  What exists
  -----------

  Every function of Qt's QQC2::QWindowsStyle that has a ritual and that
  Python can call so far, 15 names in all: 'metaObject', 'tr',
  'drawPrimitive', 'drawControl', 'drawComplexControl', 'subElementRect',
  'sizeFromContents', 'pixelMetric', 'styleHint', 'standardPixmap',
  'standardIcon', 'polish', 'timerEvent', 'd_func', 'refreshPalette'. It can
  be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQC2::QWindowsStyle::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QQC2::QWindowsStyle::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QQC2::QWindowsStyle::~QWindowsStyle()': the destructor: Python
    never removes a C++ QQC2::QWindowsStyle.
  - Qt's 'QQC2::QWindowsStyle::QWindowsStyle(QWindowsStylePrivate &dd)':
    takes a type Python has no way to hand over yet.
  - Qt's 'const QWindowsStylePrivate *QQC2::QWindowsStyle::d_func() const':
    takes in Python what 'QWindowsStylePrivate
    *QQC2::QWindowsStyle::d_func()' takes.

  What has no ritual
  ------------------

  6 of the 27 functions Qt declares: 4 forbidden; 2 not a gap.

  What to expect
  --------------

  - The C++ QQC2::QWindowsStyle is created at the first use, not by
    'QQC2::QWindowsStyle(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQC2::QWindowsStyle.
  - Qt tells when it has removed the C++ QQC2::QWindowsStyle. Every call on
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
    Calls Qt's 'QString QQC2::QWindowsStyle::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qqc2-qwindowsstyle.html#tr

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
    #  QString QQC2::QWindowsStyle::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN4QQC213QWindowsStyle2trEPKcS2_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQC2::QWindowsStyle'

  #  A C++ QQC2::QWindowsStyle Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQC2_QWindowsStyle'

  #  The functions Qt calls itself that QQC2::QWindowsStyle is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'drawPrimitive': (
          ('_ZNK4QQC213QWindowsStyle13drawPrimitiveENS_6QStyle16PrimitiveEl'
           'ementEPKNS_12QStyleOptionEP8QPainter',
           ('nothing', 'nothing', ''),
           (
               ('int', 'enum', 'QtWidgets:QStyle.PrimitiveElement'),
               ('address', 'address',
                'QtQuickNativeStyle:QQC2.QStyleOption'),
               ('address', 'address', 'QtGui:QPainter'),
           )),
      ),
      'drawControl': (
          ('_ZNK4QQC213QWindowsStyle11drawControlENS_6QStyle14ControlElemen'
           'tEPKNS_12QStyleOptionEP8QPainter',
           ('nothing', 'nothing', ''),
           (
               ('int', 'enum', 'QtWidgets:QStyle.ControlElement'),
               ('address', 'address',
                'QtQuickNativeStyle:QQC2.QStyleOption'),
               ('address', 'address', 'QtGui:QPainter'),
           )),
      ),
      'drawComplexControl': (
          ('_ZNK4QQC213QWindowsStyle18drawComplexControlENS_6QStyle14Comple'
           'xControlEPKNS_19QStyleOptionComplexEP8QPainter',
           ('nothing', 'nothing', ''),
           (
               ('int', 'enum', 'QtWidgets:QStyle.ComplexControl'),
               ('address', 'address',
                'QtQuickNativeStyle:QQC2.QStyleOptionComplex'),
               ('address', 'address', 'QtGui:QPainter'),
           )),
      ),
      'subElementRect': (
          ('_ZNK4QQC213QWindowsStyle14subElementRectENS_6QStyle10SubElement'
           'EPKNS_12QStyleOptionE',
           ('address', 'value', 'QtCore:QRect'),
           (
               ('int', 'enum', 'QtWidgets:QStyle.SubElement'),
               ('address', 'address',
                'QtQuickNativeStyle:QQC2.QStyleOption'),
           )),
      ),
      'sizeFromContents': (
          ('_ZNK4QQC213QWindowsStyle16sizeFromContentsENS_6QStyle12Contents'
           'TypeEPKNS_12QStyleOptionERK5QSize',
           ('address', 'value', 'QtCore:QSize'),
           (
               ('int', 'enum', 'QtWidgets:QStyle.ContentsType'),
               ('address', 'address',
                'QtQuickNativeStyle:QQC2.QStyleOption'),
               ('address', 'value', 'QtCore:QSize'),
           )),
      ),
      'pixelMetric': (
          ('_ZNK4QQC213QWindowsStyle11pixelMetricENS_6QStyle11PixelMetricEP'
           'KNS_12QStyleOptionE',
           ('int', 'number', ''),
           (
               ('int', 'enum', 'QtWidgets:QStyle.PixelMetric'),
               ('address', 'address',
                'QtQuickNativeStyle:QQC2.QStyleOption'),
           )),
      ),
      'styleHint': (
          ('_ZNK4QQC213QWindowsStyle9styleHintENS_6QStyle9StyleHintEPKNS_12'
           'QStyleOptionEPNS_16QStyleHintReturnE',
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
          ('_ZNK4QQC213QWindowsStyle14standardPixmapENS_6QStyle14StandardPi'
           'xmapEPKNS_12QStyleOptionE',
           ('address', 'value', 'QtGui:QPixmap'),
           (
               ('int', 'enum', 'QtWidgets:QStyle.StandardPixmap'),
               ('address', 'address',
                'QtQuickNativeStyle:QQC2.QStyleOption'),
           )),
      ),
      'standardIcon': (
          ('_ZNK4QQC213QWindowsStyle12standardIconENS_6QStyle14StandardPixm'
           'apEPKNS_12QStyleOptionE',
           ('address', 'value', 'QtGui:QIcon'),
           (
               ('int', 'enum', 'QtWidgets:QStyle.StandardPixmap'),
               ('address', 'address',
                'QtQuickNativeStyle:QQC2.QStyleOption'),
           )),
      ),
      'polish': (
          ('_ZN4QQC213QWindowsStyle6polishEv',
           ('nothing', 'nothing', ''),
           ()),
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
    Calls Qt's 'const QMetaObject *QQC2::QWindowsStyle::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqc2-qwindowsstyle.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQC2::QWindowsStyle::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK4QQC213QWindowsStyle10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  @overload(QStyle.SubElement, WAIT['QQC2.QStyleOption'])
  @overload(QStyle.SubElement, NoneType)
  def subElementRect(
      self,
      r: QStyle.SubElement,
      opt: Optional[QQC2.QStyleOption],
  ) -> QRect:
    """
    Calls Qt's 'QRect QQC2::QWindowsStyle::subElementRect(SubElement r, const
    QStyleOption *opt) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqc2-qwindowsstyle.html#subElementRect

    Parameters
    ----------

    r : QStyle.SubElement
      Passed on as its number.

    opt : Optional[QQC2.QStyleOption]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect QQC2::QWindowsStyle::subElementRect(SubElement r, const
    #      QStyleOption *opt) const
    ritual = (
        'ritual_ZNK4QQC213QWindowsStyle14subElementRectENS_6QStyle10SubElem'
        'entEPKNS_12QStyleOptionE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK4QQC213QWindowsStyle14subElementRectENS_6QStyle10S'
          'ubElementEPKNS_12QStyleOptionE')
    address = self.uglySide.call(ritual, r.value, self._addressOf(opt))
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

  @overload(QStyle.ContentsType, WAIT['QQC2.QStyleOption'], QSize)
  @overload(QStyle.ContentsType, NoneType, QSize)
  def sizeFromContents(
      self,
      ct: QStyle.ContentsType,
      opt: Optional[QQC2.QStyleOption],
      contentsSize: QSize,
  ) -> QSize:
    """
    Calls Qt's 'QSize QQC2::QWindowsStyle::sizeFromContents(ContentsType ct,
    const QStyleOption *opt, const QSize &contentsSize) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqc2-qwindowsstyle.html#sizeFromContents

    Parameters
    ----------

    ct : QStyle.ContentsType
      Passed on as its number.

    opt : Optional[QQC2.QStyleOption]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    contentsSize : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QQC2::QWindowsStyle::sizeFromContents(ContentsType ct, const
    #      QStyleOption *opt, const QSize &contentsSize) const
    ritual = (
        'ritual_ZNK4QQC213QWindowsStyle16sizeFromContentsENS_6QStyle12Conte'
        'ntsTypeEPKNS_12QStyleOptionERK5QSize')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK4QQC213QWindowsStyle16sizeFromContentsENS_6QStyle1'
          '2ContentsTypeEPKNS_12QStyleOptionERK5QSize')
    address = self.uglySide.call(
        ritual, ct.value, self._addressOf(opt), self._valueOf(contentsSize),
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
    Calls Qt's 'int QQC2::QWindowsStyle::pixelMetric(PixelMetric pm, const
    QStyleOption *option) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqc2-qwindowsstyle.html#pixelMetric

    Parameters
    ----------

    pm : QStyle.PixelMetric
      Passed on as its number.

    option : Optional[QQC2.QStyleOption]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  int QQC2::QWindowsStyle::pixelMetric(PixelMetric pm, const
    #      QStyleOption *option) const
    ritual = (
        'ritual_ZNK4QQC213QWindowsStyle11pixelMetricENS_6QStyle11PixelMetri'
        'cEPKNS_12QStyleOptionE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK4QQC213QWindowsStyle11pixelMetricENS_6QStyle11Pixe'
          'lMetricEPKNS_12QStyleOptionE')
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
      opt: Optional[QQC2.QStyleOption] = None,
      returnData: Optional[QQC2.QStyleHintReturn] = None,
  ) -> int:
    """
    Calls Qt's 'int QQC2::QWindowsStyle::styleHint(StyleHint hint, const
    QStyleOption *opt, QStyleHintReturn *returnData) const'.

    Qt's own words: https://doc.qt.io/qt-6/qqc2-qwindowsstyle.html#styleHint

    Parameters
    ----------

    hint : QStyle.StyleHint
      Passed on as its number.

    opt : Optional[QQC2.QStyleOption]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    returnData : Optional[QQC2.QStyleHintReturn]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  int QQC2::QWindowsStyle::styleHint(StyleHint hint, const QStyleOption
    #      *opt, QStyleHintReturn *returnData) const
    ritual = (
        'ritual_ZNK4QQC213QWindowsStyle9styleHintENS_6QStyle9StyleHintEPKNS'
        '_12QStyleOptionEPNS_16QStyleHintReturnE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK4QQC213QWindowsStyle9styleHintENS_6QStyle9StyleHin'
          'tEPKNS_12QStyleOptionEPNS_16QStyleHintReturnE')
    return self.uglySide.call(
        ritual,
        hint.value, self._addressOf(opt), self._addressOf(returnData),
    )

  @overload(QStyle.StandardPixmap, WAIT['QQC2.QStyleOption'])
  @overload(QStyle.StandardPixmap, NoneType)
  def standardPixmap(
      self,
      standardPixmap: QStyle.StandardPixmap,
      opt: Optional[QQC2.QStyleOption],
  ) -> QPixmap:
    """
    Calls Qt's 'QPixmap QQC2::QWindowsStyle::standardPixmap(StandardPixmap
    standardPixmap, const QStyleOption *opt) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqc2-qwindowsstyle.html#standardPixmap

    Parameters
    ----------

    standardPixmap : QStyle.StandardPixmap
      Passed on as its number.

    opt : Optional[QQC2.QStyleOption]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QPixmap
      A new cute QPixmap around the copy Qt gave back. Python owns it.
    """
    #  QPixmap QQC2::QWindowsStyle::standardPixmap(StandardPixmap
    #      standardPixmap, const QStyleOption *opt) const
    ritual = (
        'ritual_ZNK4QQC213QWindowsStyle14standardPixmapENS_6QStyle14Standar'
        'dPixmapEPKNS_12QStyleOptionE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK4QQC213QWindowsStyle14standardPixmapENS_6QStyle14S'
          'tandardPixmapEPKNS_12QStyleOptionE')
    address = self.uglySide.call(
        ritual, standardPixmap.value, self._addressOf(opt),
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
    Calls Qt's 'QIcon QQC2::QWindowsStyle::standardIcon(StandardPixmap
    standardIcon, const QStyleOption *option) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqc2-qwindowsstyle.html#standardIcon

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
    #  QIcon QQC2::QWindowsStyle::standardIcon(StandardPixmap standardIcon,
    #      const QStyleOption *option) const
    ritual = (
        'ritual_ZNK4QQC213QWindowsStyle12standardIconENS_6QStyle14StandardP'
        'ixmapEPKNS_12QStyleOptionE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK4QQC213QWindowsStyle12standardIconENS_6QStyle14Sta'
          'ndardPixmapEPKNS_12QStyleOptionE')
    address = self.uglySide.call(
        ritual, standardIcon.value, self._addressOf(option),
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
    Notes what was given, for Qt's 'QQC2::QWindowsStyle::QWindowsStyle()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqc2-qwindowsstyle.html#QWindowsStyle
    """
    #  QQC2::QWindowsStyle::QWindowsStyle()
    self._noteCreation(QWindowsStyle, lambda: Rituals.call(
        'ritual_ZN4QQC213QWindowsStyleC1Ev',
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
      opt: Optional[QQC2.QStyleOption],
      p: Optional[QPainter],
  ) -> None:
    """
    Calls Qt's 'void QQC2::QWindowsStyle::drawPrimitive(PrimitiveElement pe,
    const QStyleOption *opt, QPainter *p) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqc2-qwindowsstyle.html#drawPrimitive

    Parameters
    ----------

    pe : QStyle.PrimitiveElement
      Passed on as its number.

    opt : Optional[QQC2.QStyleOption]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    p : Optional[QPainter]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQC2::QWindowsStyle::drawPrimitive(PrimitiveElement pe, const
    #      QStyleOption *opt, QPainter *p) const
    ritual = (
        'ritual_ZNK4QQC213QWindowsStyle13drawPrimitiveENS_6QStyle16Primitiv'
        'eElementEPKNS_12QStyleOptionEP8QPainter')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK4QQC213QWindowsStyle13drawPrimitiveENS_6QStyle16Pr'
          'imitiveElementEPKNS_12QStyleOptionEP8QPainter')
    self.uglySide.call(
        ritual, pe.value, self._addressOf(opt), self._addressOf(p),
    )

  @overload(QStyle.ControlElement, WAIT['QQC2.QStyleOption'], QPainter)
  @overload(QStyle.ControlElement, WAIT['QQC2.QStyleOption'], NoneType)
  @overload(QStyle.ControlElement, NoneType, QPainter)
  @overload(QStyle.ControlElement, NoneType, NoneType)
  def drawControl(
      self,
      element: QStyle.ControlElement,
      opt: Optional[QQC2.QStyleOption],
      p: Optional[QPainter],
  ) -> None:
    """
    Calls Qt's 'void QQC2::QWindowsStyle::drawControl(ControlElement element,
    const QStyleOption *opt, QPainter *p) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqc2-qwindowsstyle.html#drawControl

    Parameters
    ----------

    element : QStyle.ControlElement
      Passed on as its number.

    opt : Optional[QQC2.QStyleOption]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    p : Optional[QPainter]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQC2::QWindowsStyle::drawControl(ControlElement element, const
    #      QStyleOption *opt, QPainter *p) const
    ritual = (
        'ritual_ZNK4QQC213QWindowsStyle11drawControlENS_6QStyle14ControlEle'
        'mentEPKNS_12QStyleOptionEP8QPainter')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK4QQC213QWindowsStyle11drawControlENS_6QStyle14Cont'
          'rolElementEPKNS_12QStyleOptionEP8QPainter')
    self.uglySide.call(
        ritual, element.value, self._addressOf(opt), self._addressOf(p),
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
      opt: Optional[QQC2.QStyleOptionComplex],
      p: Optional[QPainter],
  ) -> None:
    """
    Calls Qt's 'void QQC2::QWindowsStyle::drawComplexControl(ComplexControl
    cc, const QStyleOptionComplex *opt, QPainter *p) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqc2-qwindowsstyle.html#drawComplexControl

    Parameters
    ----------

    cc : QStyle.ComplexControl
      Passed on as its number.

    opt : Optional[QQC2.QStyleOptionComplex]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    p : Optional[QPainter]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQC2::QWindowsStyle::drawComplexControl(ComplexControl cc, const
    #      QStyleOptionComplex *opt, QPainter *p) const
    ritual = (
        'ritual_ZNK4QQC213QWindowsStyle18drawComplexControlENS_6QStyle14Com'
        'plexControlEPKNS_19QStyleOptionComplexEP8QPainter')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK4QQC213QWindowsStyle18drawComplexControlENS_6QStyl'
          'e14ComplexControlEPKNS_19QStyleOptionComplexEP8QPainter')
    self.uglySide.call(
        ritual, cc.value, self._addressOf(opt), self._addressOf(p),
    )

  def polish(self) -> None:
    """
    Calls Qt's 'void QQC2::QWindowsStyle::polish()'.

    Qt's own words: https://doc.qt.io/qt-6/qqc2-qwindowsstyle.html#polish
    """
    #  void QQC2::QWindowsStyle::polish()
    ritual = 'ritual_ZN4QQC213QWindowsStyle6polishEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN4QQC213QWindowsStyle6polishEv'
    self.uglySide.call(ritual)

  @overload(QTimerEvent)
  @overload(NoneType)
  def timerEvent(self, event: Optional[QTimerEvent]) -> None:
    """
    Calls Qt's 'void QQC2::QWindowsStyle::timerEvent(QTimerEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qqc2-qwindowsstyle.html#timerEvent

    Parameters
    ----------

    event : Optional[QTimerEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQC2::QWindowsStyle::timerEvent(QTimerEvent *event)
    ritual = 'ritual_ZN4QQC213QWindowsStyle10timerEventEP11QTimerEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN4QQC213QWindowsStyle10timerEventEP11QTimerEvent'
    self.uglySide.call(ritual, self._addressOf(event))

  def d_func(self) -> Optional[QQC2.QWindowsStylePrivate]:
    """
    Calls Qt's 'QWindowsStylePrivate *QQC2::QWindowsStyle::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qqc2-qwindowsstyle.html#d_func

    Returns
    -------

    Optional[QQC2.QWindowsStylePrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWindowsStylePrivate *QQC2::QWindowsStyle::d_func()
    address = self.uglySide.call('ritual_ZN4QQC213QWindowsStyle6d_funcEv')
    return QQC2.QWindowsStylePrivate._cuteAt(address)

  def refreshPalette(self) -> None:
    """
    Calls Qt's 'void QQC2::QWindowsStyle::refreshPalette()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqc2-qwindowsstyle.html#refreshPalette
    """
    #  void QQC2::QWindowsStyle::refreshPalette()
    self.uglySide.call('ritual_ZN4QQC213QWindowsStyle14refreshPaletteEv')
