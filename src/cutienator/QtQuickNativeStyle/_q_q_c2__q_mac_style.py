"""
QQC2::QMacStyle binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickNativeStyle/6.12.0/QtQuickNativeStyle/private/qquickmacstyle_mac_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQC2::QMacStyle to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtGui import QIcon, QPalette
from . import QQC2
from ..QtWidgets import QStyle

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMargins, QMetaObject, QPoint, QRect, QSize
  from ..QtGui import QFont, QPainter, QPixmap
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPainter = WAIT['QPainter']
  QPixmap = WAIT['QPixmap']
  QPoint = WAIT['QPoint']
  QRect = WAIT['QRect']
  QSize = WAIT['QSize']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QMacStyle(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQC2::QMacStyle: a plain Python object standing in
  front of one C++ QQC2::QMacStyle.

  What exists
  -----------

  Every function of Qt's QQC2::QMacStyle that has a ritual and that Python
  can call so far, 18 names in all: 'metaObject', 'tr', 'drawPrimitive',
  'drawControl', 'drawComplexControl', 'subElementRect', 'subControlRect',
  'hitTestComplexControl', 'sizeFromContents', 'font', 'ninePatchMargins',
  'pixelMetric', 'styleHint', 'standardPixmap', 'generatedIconPixmap',
  'drawItemText', 'standardIcon', 'handleThemeChange'. None can be made from
  Python: one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQC2::QMacStyle::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QQC2::QMacStyle::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QMacStylePrivate *QQC2::QMacStyle::d_func()': gives
    'QMacStylePrivate', which has no cute class yet.
  - Qt's 'const QMacStylePrivate *QQC2::QMacStyle::d_func() const': gives
    'QMacStylePrivate', which has no cute class yet.

  What has no ritual
  ------------------

  9 of the 31 functions Qt declares: 4 forbidden; 3 cannot be called and
  cannot be called through the meta-object and cannot be copied; 2 not a gap.

  What to expect
  --------------

  - The C++ QQC2::QMacStyle is created at the first use, not by
    'QQC2::QMacStyle(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQC2::QMacStyle.
  - Qt tells when it has removed the C++ QQC2::QMacStyle. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQC2::QMacStyle that has no cute function yet,
    '__init__', 'create', holds a function that raises 'NotImplementedError',
    and its docstring says why.
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
    Calls Qt's 'QString QQC2::QMacStyle::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qqc2-qmacstyle.html#tr

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
    #  QString QQC2::QMacStyle::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN4QQC29QMacStyle2trEPKcS2_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQC2::QMacStyle'

  #  A C++ QQC2::QMacStyle Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQC2_QMacStyle'

  #  The functions Qt calls itself that QQC2::QMacStyle is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'drawPrimitive': (
          ('_ZNK4QQC29QMacStyle13drawPrimitiveENS_6QStyle16PrimitiveElement'
           'EPKNS_12QStyleOptionEP8QPainter',
           ('nothing', 'nothing', ''),
           (
               ('int', 'enum', 'QtWidgets:QStyle.PrimitiveElement'),
               ('address', 'address',
                'QtQuickNativeStyle:QQC2.QStyleOption'),
               ('address', 'address', 'QtGui:QPainter'),
           )),
      ),
      'drawControl': (
          ('_ZNK4QQC29QMacStyle11drawControlENS_6QStyle14ControlElementEPKN'
           'S_12QStyleOptionEP8QPainter',
           ('nothing', 'nothing', ''),
           (
               ('int', 'enum', 'QtWidgets:QStyle.ControlElement'),
               ('address', 'address',
                'QtQuickNativeStyle:QQC2.QStyleOption'),
               ('address', 'address', 'QtGui:QPainter'),
           )),
      ),
      'drawComplexControl': (
          ('_ZNK4QQC29QMacStyle18drawComplexControlENS_6QStyle14ComplexCont'
           'rolEPKNS_19QStyleOptionComplexEP8QPainter',
           ('nothing', 'nothing', ''),
           (
               ('int', 'enum', 'QtWidgets:QStyle.ComplexControl'),
               ('address', 'address',
                'QtQuickNativeStyle:QQC2.QStyleOptionComplex'),
               ('address', 'address', 'QtGui:QPainter'),
           )),
      ),
      'subElementRect': (
          ('_ZNK4QQC29QMacStyle14subElementRectENS_6QStyle10SubElementEPKNS'
           '_12QStyleOptionE',
           ('address', 'value', 'QtCore:QRect'),
           (
               ('int', 'enum', 'QtWidgets:QStyle.SubElement'),
               ('address', 'address',
                'QtQuickNativeStyle:QQC2.QStyleOption'),
           )),
      ),
      'subControlRect': (
          ('_ZNK4QQC29QMacStyle14subControlRectENS_6QStyle14ComplexControlE'
           'PKNS_19QStyleOptionComplexENS1_10SubControlE',
           ('address', 'value', 'QtCore:QRect'),
           (
               ('int', 'enum', 'QtWidgets:QStyle.ComplexControl'),
               ('address', 'address',
                'QtQuickNativeStyle:QQC2.QStyleOptionComplex'),
               ('int', 'enum', 'QtWidgets:QStyle.SubControl'),
           )),
      ),
      'hitTestComplexControl': (
          ('_ZNK4QQC29QMacStyle21hitTestComplexControlENS_6QStyle14ComplexC'
           'ontrolEPKNS_19QStyleOptionComplexERK6QPoint',
           ('int', 'enum', 'QtWidgets:QStyle.SubControl'),
           (
               ('int', 'enum', 'QtWidgets:QStyle.ComplexControl'),
               ('address', 'address',
                'QtQuickNativeStyle:QQC2.QStyleOptionComplex'),
               ('address', 'value', 'QtCore:QPoint'),
           )),
      ),
      'sizeFromContents': (
          ('_ZNK4QQC29QMacStyle16sizeFromContentsENS_6QStyle12ContentsTypeE'
           'PKNS_12QStyleOptionERK5QSize',
           ('address', 'value', 'QtCore:QSize'),
           (
               ('int', 'enum', 'QtWidgets:QStyle.ContentsType'),
               ('address', 'address',
                'QtQuickNativeStyle:QQC2.QStyleOption'),
               ('address', 'value', 'QtCore:QSize'),
           )),
      ),
      'font': (
          ('_ZNK4QQC29QMacStyle4fontENS_6QStyle14ControlElementE6QFlagsINS1'
           '_9StateFlagEE',
           ('address', 'value', 'QtGui:QFont'),
           (
               ('int', 'enum', 'QtWidgets:QStyle.ControlElement'),
               ('int', 'flags', 'QtQuickNativeStyle:QQC2.QStyle.StateFlag'),
           )),
      ),
      'ninePatchMargins': (
          ('_ZNK4QQC29QMacStyle16ninePatchMarginsENS_6QStyle14ComplexContro'
           'lEPKNS_19QStyleOptionComplexERK5QSize',
           ('address', 'value', 'QtCore:QMargins'),
           (
               ('int', 'enum', 'QtWidgets:QStyle.ComplexControl'),
               ('address', 'address',
                'QtQuickNativeStyle:QQC2.QStyleOptionComplex'),
               ('address', 'value', 'QtCore:QSize'),
           )),
      ),
      'pixelMetric': (
          ('_ZNK4QQC29QMacStyle11pixelMetricENS_6QStyle11PixelMetricEPKNS_1'
           '2QStyleOptionE',
           ('int', 'number', ''),
           (
               ('int', 'enum', 'QtWidgets:QStyle.PixelMetric'),
               ('address', 'address',
                'QtQuickNativeStyle:QQC2.QStyleOption'),
           )),
      ),
      'styleHint': (
          ('_ZNK4QQC29QMacStyle9styleHintENS_6QStyle9StyleHintEPKNS_12QStyl'
           'eOptionEPNS_16QStyleHintReturnE',
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
          ('_ZNK4QQC29QMacStyle14standardPixmapENS_6QStyle14StandardPixmapE'
           'PKNS_12QStyleOptionE',
           ('address', 'value', 'QtGui:QPixmap'),
           (
               ('int', 'enum', 'QtWidgets:QStyle.StandardPixmap'),
               ('address', 'address',
                'QtQuickNativeStyle:QQC2.QStyleOption'),
           )),
      ),
      'standardIcon': (
          ('_ZNK4QQC29QMacStyle12standardIconENS_6QStyle14StandardPixmapEPK'
           'NS_12QStyleOptionE',
           ('address', 'value', 'QtGui:QIcon'),
           (
               ('int', 'enum', 'QtWidgets:QStyle.StandardPixmap'),
               ('address', 'address',
                'QtQuickNativeStyle:QQC2.QStyleOption'),
           )),
      ),
      'handleThemeChange': (
          ('_ZN4QQC29QMacStyle17handleThemeChangeEv',
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
    Calls Qt's 'const QMetaObject *QQC2::QMacStyle::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqc2-qmacstyle.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQC2::QMacStyle::metaObject() const
    address = self.uglySide.call('ritual_ZNK4QQC29QMacStyle10metaObjectEv')
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
    Calls Qt's 'QRect QQC2::QMacStyle::subElementRect(SubElement r, const
    QStyleOption *opt) const'.

    Qt's own words: https://doc.qt.io/qt-6/qqc2-qmacstyle.html#subElementRect

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
    #  QRect QQC2::QMacStyle::subElementRect(SubElement r, const QStyleOption
    #      *opt) const
    ritual = (
        'ritual_ZNK4QQC29QMacStyle14subElementRectENS_6QStyle10SubElementEP'
        'KNS_12QStyleOptionE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK4QQC29QMacStyle14subElementRectENS_6QStyle10SubEle'
          'mentEPKNS_12QStyleOptionE')
    address = self.uglySide.call(ritual, r.value, self._addressOf(opt))
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
      opt: Optional[QQC2.QStyleOptionComplex],
      sc: QStyle.SubControl,
  ) -> QRect:
    """
    Calls Qt's 'QRect QQC2::QMacStyle::subControlRect(ComplexControl cc,
    const QStyleOptionComplex *opt, SubControl sc) const'.

    Qt's own words: https://doc.qt.io/qt-6/qqc2-qmacstyle.html#subControlRect

    Parameters
    ----------

    cc : QStyle.ComplexControl
      Passed on as its number.

    opt : Optional[QQC2.QStyleOptionComplex]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    sc : QStyle.SubControl
      Passed on as its number.

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect QQC2::QMacStyle::subControlRect(ComplexControl cc, const
    #      QStyleOptionComplex *opt, SubControl sc) const
    ritual = (
        'ritual_ZNK4QQC29QMacStyle14subControlRectENS_6QStyle14ComplexContr'
        'olEPKNS_19QStyleOptionComplexENS1_10SubControlE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK4QQC29QMacStyle14subControlRectENS_6QStyle14Comple'
          'xControlEPKNS_19QStyleOptionComplexENS1_10SubControlE')
    address = self.uglySide.call(
        ritual, cc.value, self._addressOf(opt), sc.value,
    )
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

  @overload(QStyle.ComplexControl, WAIT['QQC2.QStyleOptionComplex'], QPoint)
  @overload(QStyle.ComplexControl, NoneType, QPoint)
  def hitTestComplexControl(
      self,
      cc: QStyle.ComplexControl,
      opt: Optional[QQC2.QStyleOptionComplex],
      pt: QPoint,
  ) -> QStyle.SubControl:
    """
    Calls Qt's 'SubControl
    QQC2::QMacStyle::hitTestComplexControl(ComplexControl cc, const
    QStyleOptionComplex *opt, const QPoint &pt) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqc2-qmacstyle.html#hitTestComplexControl

    Parameters
    ----------

    cc : QStyle.ComplexControl
      Passed on as its number.

    opt : Optional[QQC2.QStyleOptionComplex]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    pt : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.

    Returns
    -------

    QStyle.SubControl
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QStyle.SubControl(number)' gives.
    """
    #  SubControl QQC2::QMacStyle::hitTestComplexControl(ComplexControl cc,
    #      const QStyleOptionComplex *opt, const QPoint &pt) const
    ritual = (
        'ritual_ZNK4QQC29QMacStyle21hitTestComplexControlENS_6QStyle14Compl'
        'exControlEPKNS_19QStyleOptionComplexERK6QPoint')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK4QQC29QMacStyle21hitTestComplexControlENS_6QStyle1'
          '4ComplexControlEPKNS_19QStyleOptionComplexERK6QPoint')
    return QStyle.SubControl(self.uglySide.call(
        ritual, cc.value, self._addressOf(opt), self._valueOf(pt),
    ))

  @overload(QStyle.ContentsType, WAIT['QQC2.QStyleOption'], QSize)
  @overload(QStyle.ContentsType, NoneType, QSize)
  def sizeFromContents(
      self,
      ct: QStyle.ContentsType,
      opt: Optional[QQC2.QStyleOption],
      contentsSize: QSize,
  ) -> QSize:
    """
    Calls Qt's 'QSize QQC2::QMacStyle::sizeFromContents(ContentsType ct,
    const QStyleOption *opt, const QSize &contentsSize) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqc2-qmacstyle.html#sizeFromContents

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
    #  QSize QQC2::QMacStyle::sizeFromContents(ContentsType ct, const
    #      QStyleOption *opt, const QSize &contentsSize) const
    ritual = (
        'ritual_ZNK4QQC29QMacStyle16sizeFromContentsENS_6QStyle12ContentsTy'
        'peEPKNS_12QStyleOptionERK5QSize')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK4QQC29QMacStyle16sizeFromContentsENS_6QStyle12Cont'
          'entsTypeEPKNS_12QStyleOptionERK5QSize')
    address = self.uglySide.call(
        ritual, ct.value, self._addressOf(opt), self._valueOf(contentsSize),
    )
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  @overload(QStyle.ControlElement, QQC2.QStyle.State)
  def font(
      self,
      element: QStyle.ControlElement,
      state: QQC2.QStyle.State,
  ) -> QFont:
    """
    Calls Qt's 'QFont QQC2::QMacStyle::font(ControlElement element, const
    QStyle::State state) const'.

    Qt's own words: https://doc.qt.io/qt-6/qqc2-qmacstyle.html#font

    Parameters
    ----------

    element : QStyle.ControlElement
      Passed on as its number.

    state : QQC2.QStyle.State
      Passed on as its number.

    Returns
    -------

    QFont
      A new cute QFont around the copy Qt gave back. Python owns it.
    """
    #  QFont QQC2::QMacStyle::font(ControlElement element, const
    #      QStyle::State state) const
    ritual = (
        'ritual_ZNK4QQC29QMacStyle4fontENS_6QStyle14ControlElementE6QFlagsI'
        'NS1_9StateFlagEE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK4QQC29QMacStyle4fontENS_6QStyle14ControlElementE6Q'
          'FlagsINS1_9StateFlagEE')
    address = self.uglySide.call(ritual, element.value, state.value)
    from ..QtGui import QFont
    return QFont._cuteOwning(address)

  @overload(QStyle.ComplexControl, WAIT['QQC2.QStyleOptionComplex'], QSize)
  @overload(QStyle.ComplexControl, NoneType, QSize)
  def ninePatchMargins(
      self,
      cc: QStyle.ComplexControl,
      opt: Optional[QQC2.QStyleOptionComplex],
      imageSize: QSize,
  ) -> QMargins:
    """
    Calls Qt's 'QMargins QQC2::QMacStyle::ninePatchMargins(ComplexControl cc,
    const QStyleOptionComplex *opt, const QSize &imageSize) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqc2-qmacstyle.html#ninePatchMargins

    Parameters
    ----------

    cc : QStyle.ComplexControl
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
    #  QMargins QQC2::QMacStyle::ninePatchMargins(ComplexControl cc, const
    #      QStyleOptionComplex *opt, const QSize &imageSize) const
    ritual = (
        'ritual_ZNK4QQC29QMacStyle16ninePatchMarginsENS_6QStyle14ComplexCon'
        'trolEPKNS_19QStyleOptionComplexERK5QSize')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK4QQC29QMacStyle16ninePatchMarginsENS_6QStyle14Comp'
          'lexControlEPKNS_19QStyleOptionComplexERK5QSize')
    address = self.uglySide.call(
        ritual, cc.value, self._addressOf(opt), self._valueOf(imageSize),
    )
    from ..QtCore import QMargins
    return QMargins._cuteOwning(address)

  @overload(QStyle.PixelMetric)
  @overload(QStyle.PixelMetric, WAIT['QQC2.QStyleOption'])
  @overload(QStyle.PixelMetric, NoneType)
  def pixelMetric(
      self,
      pm: QStyle.PixelMetric,
      opt: Optional[QQC2.QStyleOption] = None,
  ) -> int:
    """
    Calls Qt's 'int QQC2::QMacStyle::pixelMetric(PixelMetric pm, const
    QStyleOption *opt) const'.

    Qt's own words: https://doc.qt.io/qt-6/qqc2-qmacstyle.html#pixelMetric

    Parameters
    ----------

    pm : QStyle.PixelMetric
      Passed on as its number.

    opt : Optional[QQC2.QStyleOption]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  int QQC2::QMacStyle::pixelMetric(PixelMetric pm, const QStyleOption
    #      *opt) const
    ritual = (
        'ritual_ZNK4QQC29QMacStyle11pixelMetricENS_6QStyle11PixelMetricEPKN'
        'S_12QStyleOptionE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK4QQC29QMacStyle11pixelMetricENS_6QStyle11PixelMetr'
          'icEPKNS_12QStyleOptionE')
    return self.uglySide.call(ritual, pm.value, self._addressOf(opt))

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
      sh: QStyle.StyleHint,
      opt: Optional[QQC2.QStyleOption] = None,
      shret: Optional[QQC2.QStyleHintReturn] = None,
  ) -> int:
    """
    Calls Qt's 'int QQC2::QMacStyle::styleHint(StyleHint sh, const
    QStyleOption *opt, QStyleHintReturn *shret) const'.

    Qt's own words: https://doc.qt.io/qt-6/qqc2-qmacstyle.html#styleHint

    Parameters
    ----------

    sh : QStyle.StyleHint
      Passed on as its number.

    opt : Optional[QQC2.QStyleOption]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    shret : Optional[QQC2.QStyleHintReturn]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  int QQC2::QMacStyle::styleHint(StyleHint sh, const QStyleOption *opt,
    #      QStyleHintReturn *shret) const
    ritual = (
        'ritual_ZNK4QQC29QMacStyle9styleHintENS_6QStyle9StyleHintEPKNS_12QS'
        'tyleOptionEPNS_16QStyleHintReturnE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK4QQC29QMacStyle9styleHintENS_6QStyle9StyleHintEPKN'
          'S_12QStyleOptionEPNS_16QStyleHintReturnE')
    return self.uglySide.call(
        ritual, sh.value, self._addressOf(opt), self._addressOf(shret),
    )

  @overload(QStyle.StandardPixmap, WAIT['QQC2.QStyleOption'])
  @overload(QStyle.StandardPixmap, NoneType)
  def standardPixmap(
      self,
      sp: QStyle.StandardPixmap,
      opt: Optional[QQC2.QStyleOption],
  ) -> QPixmap:
    """
    Calls Qt's 'QPixmap QQC2::QMacStyle::standardPixmap(StandardPixmap sp,
    const QStyleOption *opt) const'.

    Qt's own words: https://doc.qt.io/qt-6/qqc2-qmacstyle.html#standardPixmap

    Parameters
    ----------

    sp : QStyle.StandardPixmap
      Passed on as its number.

    opt : Optional[QQC2.QStyleOption]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QPixmap
      A new cute QPixmap around the copy Qt gave back. Python owns it.
    """
    #  QPixmap QQC2::QMacStyle::standardPixmap(StandardPixmap sp, const
    #      QStyleOption *opt) const
    ritual = (
        'ritual_ZNK4QQC29QMacStyle14standardPixmapENS_6QStyle14StandardPixm'
        'apEPKNS_12QStyleOptionE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK4QQC29QMacStyle14standardPixmapENS_6QStyle14Standa'
          'rdPixmapEPKNS_12QStyleOptionE')
    address = self.uglySide.call(ritual, sp.value, self._addressOf(opt))
    from ..QtGui import QPixmap
    return QPixmap._cuteOwning(address)

  @overload(QIcon.Mode, QPixmap, WAIT['QQC2.QStyleOption'])
  @overload(QIcon.Mode, QPixmap, NoneType)
  def generatedIconPixmap(
      self,
      iconMode: QIcon.Mode,
      pixmap: QPixmap,
      opt: Optional[QQC2.QStyleOption],
  ) -> QPixmap:
    """
    Calls Qt's 'QPixmap QQC2::QMacStyle::generatedIconPixmap(QIcon::Mode
    iconMode, const QPixmap &pixmap, const QStyleOption *opt) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqc2-qmacstyle.html#generatedIconPixmap

    Parameters
    ----------

    iconMode : QIcon.Mode
      Passed on as its number.

    pixmap : QPixmap
      Passed on as a value: Qt reads the C++ QPixmap, which stays Python's
      own.

    opt : Optional[QQC2.QStyleOption]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QPixmap
      A new cute QPixmap around the copy Qt gave back. Python owns it.
    """
    #  QPixmap QQC2::QMacStyle::generatedIconPixmap(QIcon::Mode iconMode,
    #      const QPixmap &pixmap, const QStyleOption *opt) const
    ritual = (
        'ritual_ZNK4QQC29QMacStyle19generatedIconPixmapEN5QIcon4ModeERK7QPi'
        'xmapPKNS_12QStyleOptionE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK4QQC29QMacStyle19generatedIconPixmapEN5QIcon4ModeE'
          'RK7QPixmapPKNS_12QStyleOptionE')
    address = self.uglySide.call(
        ritual, iconMode.value, self._valueOf(pixmap), self._addressOf(opt),
    )
    from ..QtGui import QPixmap
    return QPixmap._cuteOwning(address)

  @overload(QStyle.StandardPixmap)
  @overload(QStyle.StandardPixmap, WAIT['QQC2.QStyleOption'])
  @overload(QStyle.StandardPixmap, NoneType)
  def standardIcon(
      self,
      standardIcon: QStyle.StandardPixmap,
      opt: Optional[QQC2.QStyleOption] = None,
  ) -> QIcon:
    """
    Calls Qt's 'QIcon QQC2::QMacStyle::standardIcon(StandardPixmap
    standardIcon, const QStyleOption *opt) const'.

    Qt's own words: https://doc.qt.io/qt-6/qqc2-qmacstyle.html#standardIcon

    Parameters
    ----------

    standardIcon : QStyle.StandardPixmap
      Passed on as its number.

    opt : Optional[QQC2.QStyleOption]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    Returns
    -------

    QIcon
      A new cute QIcon around the copy Qt gave back. Python owns it.
    """
    #  QIcon QQC2::QMacStyle::standardIcon(StandardPixmap standardIcon, const
    #      QStyleOption *opt) const
    ritual = (
        'ritual_ZNK4QQC29QMacStyle12standardIconENS_6QStyle14StandardPixmap'
        'EPKNS_12QStyleOptionE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK4QQC29QMacStyle12standardIconENS_6QStyle14Standard'
          'PixmapEPKNS_12QStyleOptionE')
    address = self.uglySide.call(
        ritual, standardIcon.value, self._addressOf(opt),
    )
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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'QQC2::QMacStyle::QMacStyle()': cannot be called and cannot be
    called through the meta-object and cannot be copied: no header file has
    its code, Qt's source does not mark it or its class for use from outside
    Qt or writes it 'inline' or nowhere, and it is no signal, slot or
    invokable function giving back nothing, of a class built on QObject, and
    Qt's source has no code for it that could be told from the rest.
    """
    raise NotImplementedError(
        "'QQC2.QMacStyle.__init__' has no cute function yet. Qt's "
        "'QQC2::QMacStyle::QMacStyle()': cannot be called and cannot be "
        "called through the meta-object and cannot be copied: no header "
        "file has its code, Qt's source does not mark it or its class for "
        "use from outside Qt or writes it 'inline' or nowhere, and it is no "
        "signal, slot or invokable function giving back nothing, of a class "
        "built on QObject, and Qt's source has no code for it that could be "
        "told from the rest.")

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
    Calls Qt's 'void QQC2::QMacStyle::drawPrimitive(PrimitiveElement pe,
    const QStyleOption *opt, QPainter *p) const'.

    Qt's own words: https://doc.qt.io/qt-6/qqc2-qmacstyle.html#drawPrimitive

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
    #  void QQC2::QMacStyle::drawPrimitive(PrimitiveElement pe, const
    #      QStyleOption *opt, QPainter *p) const
    ritual = (
        'ritual_ZNK4QQC29QMacStyle13drawPrimitiveENS_6QStyle16PrimitiveElem'
        'entEPKNS_12QStyleOptionEP8QPainter')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK4QQC29QMacStyle13drawPrimitiveENS_6QStyle16Primiti'
          'veElementEPKNS_12QStyleOptionEP8QPainter')
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
    Calls Qt's 'void QQC2::QMacStyle::drawControl(ControlElement element,
    const QStyleOption *opt, QPainter *p) const'.

    Qt's own words: https://doc.qt.io/qt-6/qqc2-qmacstyle.html#drawControl

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
    #  void QQC2::QMacStyle::drawControl(ControlElement element, const
    #      QStyleOption *opt, QPainter *p) const
    ritual = (
        'ritual_ZNK4QQC29QMacStyle11drawControlENS_6QStyle14ControlElementE'
        'PKNS_12QStyleOptionEP8QPainter')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK4QQC29QMacStyle11drawControlENS_6QStyle14ControlEl'
          'ementEPKNS_12QStyleOptionEP8QPainter')
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
    Calls Qt's 'void QQC2::QMacStyle::drawComplexControl(ComplexControl cc,
    const QStyleOptionComplex *opt, QPainter *p) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqc2-qmacstyle.html#drawComplexControl

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
    #  void QQC2::QMacStyle::drawComplexControl(ComplexControl cc, const
    #      QStyleOptionComplex *opt, QPainter *p) const
    ritual = (
        'ritual_ZNK4QQC29QMacStyle18drawComplexControlENS_6QStyle14ComplexC'
        'ontrolEPKNS_19QStyleOptionComplexEP8QPainter')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK4QQC29QMacStyle18drawComplexControlENS_6QStyle14Co'
          'mplexControlEPKNS_19QStyleOptionComplexEP8QPainter')
    self.uglySide.call(
        ritual, cc.value, self._addressOf(opt), self._addressOf(p),
    )

  @overload(QPainter, QRect, int, QPalette, bool, str)
  @overload(NoneType, QRect, int, QPalette, bool, str)
  @overload(QPainter, QRect, int, QPalette, bool, str, QPalette.ColorRole)
  @overload(NoneType, QRect, int, QPalette, bool, str, QPalette.ColorRole)
  def drawItemText(
      self,
      p: Optional[QPainter],
      r: QRect,
      flags: int,
      pal: QPalette,
      enabled: bool,
      text: str,
      textRole: QPalette.ColorRole = QPalette.ColorRole.NoRole,
  ) -> None:
    """
    Calls Qt's 'void QQC2::QMacStyle::drawItemText(QPainter *p, const QRect
    &r, int flags, const QPalette &pal, bool enabled, const QString &text,
    QPalette::ColorRole textRole) const'.

    Qt's own words: https://doc.qt.io/qt-6/qqc2-qmacstyle.html#drawItemText

    Parameters
    ----------

    p : Optional[QPainter]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    r : QRect
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
    #  void QQC2::QMacStyle::drawItemText(QPainter *p, const QRect &r, int
    #      flags, const QPalette &pal, bool enabled, const QString &text,
    #      QPalette::ColorRole textRole) const
    ritual = (
        'ritual_ZNK4QQC29QMacStyle12drawItemTextEP8QPainterRK5QRectiRK8QPal'
        'ettebRK7QStringNS6_9ColorRoleE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK4QQC29QMacStyle12drawItemTextEP8QPainterRK5QRectiR'
          'K8QPalettebRK7QStringNS6_9ColorRoleE')
    self.uglySide.call(
        ritual,
        self._addressOf(p), self._valueOf(r), flags, self._valueOf(pal),
        enabled, text, textRole.value,
    )

  def handleThemeChange(self) -> None:
    """
    Calls Qt's 'void QQC2::QMacStyle::handleThemeChange()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqc2-qmacstyle.html#handleThemeChange
    """
    #  void QQC2::QMacStyle::handleThemeChange()
    ritual = 'ritual_ZN4QQC29QMacStyle17handleThemeChangeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN4QQC29QMacStyle17handleThemeChangeEv'
    self.uglySide.call(ritual)

  @staticmethod
  def create(*__, **_) -> Never:
    """
    Qt's 'QMacStyle *QQC2::QMacStyle::create()': cannot be called and cannot
    be called through the meta-object and cannot be copied: no header file
    has its code, Qt's source does not mark it or its class for use from
    outside Qt or writes it 'inline' or nowhere, and it is no signal, slot or
    invokable function giving back nothing, of a class built on QObject, and
    Qt's source has no code for it that could be told from the rest.
    """
    raise NotImplementedError(
        "'QQC2.QMacStyle.create' has no cute function yet. Qt's 'QMacStyle "
        "*QQC2::QMacStyle::create()': cannot be called and cannot be called "
        "through the meta-object and cannot be copied: no header file has "
        "its code, Qt's source does not mark it or its class for use from "
        "outside Qt or writes it 'inline' or nowhere, and it is no signal, "
        "slot or invokable function giving back nothing, of a class built "
        "on QObject, and Qt's source has no code for it that could be told "
        "from the rest.")
