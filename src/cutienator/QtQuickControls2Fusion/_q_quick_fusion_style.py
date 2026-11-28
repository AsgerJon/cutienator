"""
QQuickFusionStyle binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickControls2Fusion/6.12.0/QtQuickControls2Fusion/private/qquickfusionstyle_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuickFusionStyle to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QObject
  from ..QtGui import QColor
  from ..QtQuick import QQuickPalette
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QColor = WAIT['QColor']
  QObject = WAIT['QObject']
  QQuickPalette = WAIT['QQuickPalette']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickFusionStyle(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQuickFusionStyle: a plain Python object standing in
  front of one C++ QQuickFusionStyle.

  What exists
  -----------

  Every function of Qt's QQuickFusionStyle that has a ritual and that Python
  can call so far, 19 names in all: 'metaObject', 'tr', 'lightShade',
  'darkShade', 'topShadow', 'innerContrastLine', 'isHighContrast',
  'highlight', 'highlightedText', 'outline', 'highlightedOutline',
  'tabFrameColor', 'buttonColor', 'buttonOutline', 'gradientStart',
  'gradientStop', 'mergedColors', 'grooveColor', 'highContrastChanged'. It
  can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickFusionStyle::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QQuickFusionStyle::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'void QQuickFusionStyle::qt_qmlMarker_singleton()': one of Qt's own
    inner workings.

  What has no ritual
  ------------------

  2 of the 25 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuickFusionStyle is created at the first use, not by
    'QQuickFusionStyle(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickFusionStyle.
  - Qt tells when it has removed the C++ QQuickFusionStyle. Every call on the
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
    Calls Qt's 'QString QQuickFusionStyle::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickfusionstyle.html#tr

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
    #  QString QQuickFusionStyle::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN17QQuickFusionStyle2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  def lightShade() -> QColor:
    """
    Calls Qt's 'QColor QQuickFusionStyle::lightShade()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickfusionstyle.html#lightShade

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QQuickFusionStyle::lightShade()
    address = Rituals.call('ritual_ZN17QQuickFusionStyle10lightShadeEv')
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  @staticmethod
  def darkShade() -> QColor:
    """
    Calls Qt's 'QColor QQuickFusionStyle::darkShade()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickfusionstyle.html#darkShade

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QQuickFusionStyle::darkShade()
    address = Rituals.call('ritual_ZN17QQuickFusionStyle9darkShadeEv')
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  @staticmethod
  def topShadow() -> QColor:
    """
    Calls Qt's 'QColor QQuickFusionStyle::topShadow()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickfusionstyle.html#topShadow

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QQuickFusionStyle::topShadow()
    address = Rituals.call('ritual_ZN17QQuickFusionStyle9topShadowEv')
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  @staticmethod
  def innerContrastLine() -> QColor:
    """
    Calls Qt's 'QColor QQuickFusionStyle::innerContrastLine()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfusionstyle.html#innerContrastLine

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QQuickFusionStyle::innerContrastLine()
    address = Rituals.call(
        'ritual_ZN17QQuickFusionStyle17innerContrastLineEv',
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  @staticmethod
  def isHighContrast() -> bool:
    """
    Calls Qt's 'bool QQuickFusionStyle::isHighContrast()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfusionstyle.html#isHighContrast
    """
    #  bool QQuickFusionStyle::isHighContrast()
    return Rituals.call('ritual_ZN17QQuickFusionStyle14isHighContrastEv')

  @staticmethod
  @overload(QQuickPalette)
  @overload(NoneType)
  def highlight(palette: Optional[QQuickPalette]) -> QColor:
    """
    Calls Qt's 'QColor QQuickFusionStyle::highlight(QQuickPalette *palette)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickfusionstyle.html#highlight

    Parameters
    ----------

    palette : Optional[QQuickPalette]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QQuickFusionStyle::highlight(QQuickPalette *palette)
    address = Rituals.call(
        'ritual_ZN17QQuickFusionStyle9highlightEP13QQuickPalette',
        CuteMixin._addressOf(palette),
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  @staticmethod
  @overload(QQuickPalette)
  @overload(NoneType)
  def highlightedText(palette: Optional[QQuickPalette]) -> QColor:
    """
    Calls Qt's 'QColor QQuickFusionStyle::highlightedText(QQuickPalette
    *palette)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfusionstyle.html#highlightedText

    Parameters
    ----------

    palette : Optional[QQuickPalette]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QQuickFusionStyle::highlightedText(QQuickPalette *palette)
    address = Rituals.call(
        'ritual_ZN17QQuickFusionStyle15highlightedTextEP13QQuickPalette',
        CuteMixin._addressOf(palette),
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  @staticmethod
  @overload(QQuickPalette)
  @overload(NoneType)
  def outline(palette: Optional[QQuickPalette]) -> QColor:
    """
    Calls Qt's 'QColor QQuickFusionStyle::outline(QQuickPalette *palette)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickfusionstyle.html#outline

    Parameters
    ----------

    palette : Optional[QQuickPalette]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QQuickFusionStyle::outline(QQuickPalette *palette)
    address = Rituals.call(
        'ritual_ZN17QQuickFusionStyle7outlineEP13QQuickPalette',
        CuteMixin._addressOf(palette),
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  @staticmethod
  @overload(QQuickPalette)
  @overload(NoneType)
  def highlightedOutline(palette: Optional[QQuickPalette]) -> QColor:
    """
    Calls Qt's 'QColor QQuickFusionStyle::highlightedOutline(QQuickPalette
    *palette)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfusionstyle.html#highlightedOutline

    Parameters
    ----------

    palette : Optional[QQuickPalette]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QQuickFusionStyle::highlightedOutline(QQuickPalette *palette)
    address = Rituals.call(
        'ritual_ZN17QQuickFusionStyle18highlightedOutlineEP13QQuickPalette',
        CuteMixin._addressOf(palette),
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  @staticmethod
  @overload(QQuickPalette)
  @overload(NoneType)
  def tabFrameColor(palette: Optional[QQuickPalette]) -> QColor:
    """
    Calls Qt's 'QColor QQuickFusionStyle::tabFrameColor(QQuickPalette
    *palette)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfusionstyle.html#tabFrameColor

    Parameters
    ----------

    palette : Optional[QQuickPalette]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QQuickFusionStyle::tabFrameColor(QQuickPalette *palette)
    address = Rituals.call(
        'ritual_ZN17QQuickFusionStyle13tabFrameColorEP13QQuickPalette',
        CuteMixin._addressOf(palette),
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  @staticmethod
  @overload(QQuickPalette)
  @overload(NoneType)
  @overload(QQuickPalette, bool)
  @overload(NoneType, bool)
  @overload(QQuickPalette, bool, bool)
  @overload(NoneType, bool, bool)
  @overload(QQuickPalette, bool, bool, bool)
  @overload(NoneType, bool, bool, bool)
  def buttonColor(
      palette: Optional[QQuickPalette],
      highlighted: bool = False,
      down: bool = False,
      hovered: bool = False,
  ) -> QColor:
    """
    Calls Qt's 'QColor QQuickFusionStyle::buttonColor(QQuickPalette *palette,
    bool highlighted, bool down, bool hovered)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickfusionstyle.html#buttonColor

    Parameters
    ----------

    palette : Optional[QQuickPalette]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    highlighted : bool
      Passed on as it is. May be left out, as in Qt: it is then False.

    down : bool
      Passed on as it is. May be left out, as in Qt: it is then False.

    hovered : bool
      Passed on as it is. May be left out, as in Qt: it is then False.

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QQuickFusionStyle::buttonColor(QQuickPalette *palette, bool
    #      highlighted, bool down, bool hovered)
    address = Rituals.call(
        'ritual_ZN17QQuickFusionStyle11buttonColorEP13QQuickPalettebbb',
        CuteMixin._addressOf(palette), highlighted, down, hovered,
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  @staticmethod
  @overload(QQuickPalette)
  @overload(NoneType)
  @overload(QQuickPalette, bool)
  @overload(NoneType, bool)
  @overload(QQuickPalette, bool, bool)
  @overload(NoneType, bool, bool)
  def buttonOutline(
      palette: Optional[QQuickPalette],
      highlighted: bool = False,
      enabled: bool = True,
  ) -> QColor:
    """
    Calls Qt's 'QColor QQuickFusionStyle::buttonOutline(QQuickPalette
    *palette, bool highlighted, bool enabled)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfusionstyle.html#buttonOutline

    Parameters
    ----------

    palette : Optional[QQuickPalette]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    highlighted : bool
      Passed on as it is. May be left out, as in Qt: it is then False.

    enabled : bool
      Passed on as it is. May be left out, as in Qt: it is then True.

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QQuickFusionStyle::buttonOutline(QQuickPalette *palette, bool
    #      highlighted, bool enabled)
    address = Rituals.call(
        'ritual_ZN17QQuickFusionStyle13buttonOutlineEP13QQuickPalettebb',
        CuteMixin._addressOf(palette), highlighted, enabled,
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  @staticmethod
  @overload(QColor)
  def gradientStart(baseColor: QColor) -> QColor:
    """
    Calls Qt's 'QColor QQuickFusionStyle::gradientStart(const QColor
    &baseColor)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfusionstyle.html#gradientStart

    Parameters
    ----------

    baseColor : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QQuickFusionStyle::gradientStart(const QColor &baseColor)
    address = Rituals.call(
        'ritual_ZN17QQuickFusionStyle13gradientStartERK6QColor',
        CuteMixin._valueOf(baseColor),
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  @staticmethod
  @overload(QColor)
  def gradientStop(baseColor: QColor) -> QColor:
    """
    Calls Qt's 'QColor QQuickFusionStyle::gradientStop(const QColor
    &baseColor)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfusionstyle.html#gradientStop

    Parameters
    ----------

    baseColor : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QQuickFusionStyle::gradientStop(const QColor &baseColor)
    address = Rituals.call(
        'ritual_ZN17QQuickFusionStyle12gradientStopERK6QColor',
        CuteMixin._valueOf(baseColor),
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  @staticmethod
  @overload(QColor, QColor)
  @overload(QColor, QColor, int)
  def mergedColors(
      colorA: QColor,
      colorB: QColor,
      factor: int = 50,
  ) -> QColor:
    """
    Calls Qt's 'QColor QQuickFusionStyle::mergedColors(const QColor &colorA,
    const QColor &colorB, int factor)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfusionstyle.html#mergedColors

    Parameters
    ----------

    colorA : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.

    colorB : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.

    factor : int
      Passed on as it is. May be left out, as in Qt: it is then 50.

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QQuickFusionStyle::mergedColors(const QColor &colorA, const
    #      QColor &colorB, int factor)
    address = Rituals.call(
        'ritual_ZN17QQuickFusionStyle12mergedColorsERK6QColorS2_i',
        CuteMixin._valueOf(colorA), CuteMixin._valueOf(colorB), factor,
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  @staticmethod
  @overload(QQuickPalette)
  @overload(NoneType)
  def grooveColor(palette: Optional[QQuickPalette]) -> QColor:
    """
    Calls Qt's 'QColor QQuickFusionStyle::grooveColor(QQuickPalette
    *palette)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickfusionstyle.html#grooveColor

    Parameters
    ----------

    palette : Optional[QQuickPalette]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QQuickFusionStyle::grooveColor(QQuickPalette *palette)
    address = Rituals.call(
        'ritual_ZN17QQuickFusionStyle11grooveColorEP13QQuickPalette',
        CuteMixin._addressOf(palette),
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickFusionStyle'

  #  A C++ QQuickFusionStyle Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickFusionStyle'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickFusionStyle::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickfusionstyle.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickFusionStyle::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK17QQuickFusionStyle10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

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
  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's
    'QQuickFusionStyle::QQuickFusionStyle(QObject *parent)', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfusionstyle.html#QQuickFusionStyle

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickFusionStyle::QQuickFusionStyle(QObject *parent)
    self._noteCreation(QQuickFusionStyle, lambda: Rituals.call(
        'ritual_ZN17QQuickFusionStyleC1EP7QObject',
        self._addressOf(parent, 'QObject'),
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

  def highContrastChanged(self) -> None:
    """
    Calls Qt's 'void QQuickFusionStyle::highContrastChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfusionstyle.html#highContrastChanged
    """
    #  void QQuickFusionStyle::highContrastChanged()
    self.uglySide.call('ritual_ZN17QQuickFusionStyle19highContrastChangedEv')
