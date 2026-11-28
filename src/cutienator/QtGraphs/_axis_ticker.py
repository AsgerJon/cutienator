"""
AxisTicker binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGraphs/6.12.0/QtGraphs/private/axisticker_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means AxisTicker to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..QtQuick import QQuickShaderEffect

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QRectF
  from ..QtGui import QColor, QVector3D
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QRectF = WAIT['QRectF']


class AxisTicker(QQuickShaderEffect):
  """
  The cute side of Qt's AxisTicker: a plain Python object standing in front
  of one C++ AxisTicker.

  It is built on the cute 'QQuickShaderEffect', as Qt's AxisTicker is built
  on Qt's QQuickShaderEffect, and has everything that class has.

  What exists
  -----------

  Every function of Qt's AxisTicker that has a ritual and that Python can
  call so far, 36 names in all: 'metaObject', 'setupShaders', 'iResolution',
  'smoothing', 'origo', 'subTicksVisible', 'spacing', 'displacement',
  'subTickColor', 'tickColor', 'subTickLineWidth', 'tickLineWidth',
  'subTickScale', 'subTickLength', 'isHorizontal', 'isFlipped',
  'isLogarithmic', 'base', 'componentComplete', 'geometryChange',
  'iResolutionChanged', 'smoothingChanged', 'origoChanged',
  'subTicksVisibleChanged', 'spacingChanged', 'displacementChanged',
  'subTickColorChanged', 'tickColorChanged', 'subTickLineWidthChanged',
  'tickLineWidthChanged', 'subTickScaleChanged', 'subTickLengthChanged',
  'isHorizontalChanged', 'flippedChanged', 'logarithmicChanged',
  'baseChanged'. None can be made from Python: one comes out of a function of
  another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *AxisTicker::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int AxisTicker::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'AxisTicker::~AxisTicker()': the destructor: Python never removes a
    C++ AxisTicker.

  What has no ritual
  ------------------

  19 of the 58 functions Qt declares: 17 leans on 'AxisTicker; 2 not a gap.

  What to expect
  --------------

  - The C++ AxisTicker is created at the first use, not by 'AxisTicker(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ AxisTicker.
  - Qt tells when it has removed the C++ AxisTicker. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
  - Each name of Qt's AxisTicker that has no cute function yet, '__init__',
    'setBase', 'setDisplacement', 'setFlipped', 'setIsHorizontal',
    'setLogarithmic', 'setOrigo', 'setSmoothing', 'setSpacing',
    'setSubTickColor', 'setSubTickLength', 'setSubTickLineWidth',
    'setSubTickScale', 'setSubTicksVisible', 'setTickColor',
    'setTickLineWidth', holds a function that raises 'NotImplementedError',
    and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'AxisTicker'

  #  A C++ AxisTicker Python makes is of a C++ class of ours, in which Python
  #  can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_AxisTicker'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *AxisTicker::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/axisticker.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *AxisTicker::metaObject() const
    address = self.uglySide.call('ritual_ZNK10AxisTicker10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def iResolution(self) -> QVector3D:
    """
    Calls Qt's 'QVector3D AxisTicker::iResolution() const'.

    Qt's own words: https://doc.qt.io/qt-6/axisticker.html#iResolution

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  QVector3D AxisTicker::iResolution() const
    address = self.uglySide.call('ritual_ZNK10AxisTicker11iResolutionEv')
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  def smoothing(self) -> float:
    """
    Calls Qt's 'qreal AxisTicker::smoothing() const'.

    Qt's own words: https://doc.qt.io/qt-6/axisticker.html#smoothing
    """
    #  qreal AxisTicker::smoothing() const
    return self.uglySide.call('ritual_ZNK10AxisTicker9smoothingEv')

  def origo(self) -> int:
    """
    Calls Qt's 'int AxisTicker::origo() const'.

    Qt's own words: https://doc.qt.io/qt-6/axisticker.html#origo
    """
    #  int AxisTicker::origo() const
    return self.uglySide.call('ritual_ZNK10AxisTicker5origoEv')

  def subTicksVisible(self) -> bool:
    """
    Calls Qt's 'bool AxisTicker::subTicksVisible() const'.

    Qt's own words: https://doc.qt.io/qt-6/axisticker.html#subTicksVisible
    """
    #  bool AxisTicker::subTicksVisible() const
    return self.uglySide.call('ritual_ZNK10AxisTicker15subTicksVisibleEv')

  def spacing(self) -> float:
    """
    Calls Qt's 'qreal AxisTicker::spacing() const'.

    Qt's own words: https://doc.qt.io/qt-6/axisticker.html#spacing
    """
    #  qreal AxisTicker::spacing() const
    return self.uglySide.call('ritual_ZNK10AxisTicker7spacingEv')

  def displacement(self) -> float:
    """
    Calls Qt's 'qreal AxisTicker::displacement() const'.

    Qt's own words: https://doc.qt.io/qt-6/axisticker.html#displacement
    """
    #  qreal AxisTicker::displacement() const
    return self.uglySide.call('ritual_ZNK10AxisTicker12displacementEv')

  def subTickColor(self) -> QColor:
    """
    Calls Qt's 'QColor AxisTicker::subTickColor() const'.

    Qt's own words: https://doc.qt.io/qt-6/axisticker.html#subTickColor

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor AxisTicker::subTickColor() const
    address = self.uglySide.call('ritual_ZNK10AxisTicker12subTickColorEv')
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def tickColor(self) -> QColor:
    """
    Calls Qt's 'QColor AxisTicker::tickColor() const'.

    Qt's own words: https://doc.qt.io/qt-6/axisticker.html#tickColor

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor AxisTicker::tickColor() const
    address = self.uglySide.call('ritual_ZNK10AxisTicker9tickColorEv')
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def subTickLineWidth(self) -> float:
    """
    Calls Qt's 'qreal AxisTicker::subTickLineWidth() const'.

    Qt's own words: https://doc.qt.io/qt-6/axisticker.html#subTickLineWidth
    """
    #  qreal AxisTicker::subTickLineWidth() const
    return self.uglySide.call('ritual_ZNK10AxisTicker16subTickLineWidthEv')

  def tickLineWidth(self) -> float:
    """
    Calls Qt's 'qreal AxisTicker::tickLineWidth() const'.

    Qt's own words: https://doc.qt.io/qt-6/axisticker.html#tickLineWidth
    """
    #  qreal AxisTicker::tickLineWidth() const
    return self.uglySide.call('ritual_ZNK10AxisTicker13tickLineWidthEv')

  def subTickScale(self) -> float:
    """
    Calls Qt's 'qreal AxisTicker::subTickScale() const'.

    Qt's own words: https://doc.qt.io/qt-6/axisticker.html#subTickScale
    """
    #  qreal AxisTicker::subTickScale() const
    return self.uglySide.call('ritual_ZNK10AxisTicker12subTickScaleEv')

  def subTickLength(self) -> float:
    """
    Calls Qt's 'qreal AxisTicker::subTickLength() const'.

    Qt's own words: https://doc.qt.io/qt-6/axisticker.html#subTickLength
    """
    #  qreal AxisTicker::subTickLength() const
    return self.uglySide.call('ritual_ZNK10AxisTicker13subTickLengthEv')

  def isHorizontal(self) -> bool:
    """
    Calls Qt's 'bool AxisTicker::isHorizontal() const'.

    Qt's own words: https://doc.qt.io/qt-6/axisticker.html#isHorizontal
    """
    #  bool AxisTicker::isHorizontal() const
    return self.uglySide.call('ritual_ZNK10AxisTicker12isHorizontalEv')

  def isFlipped(self) -> bool:
    """
    Calls Qt's 'bool AxisTicker::isFlipped() const'.

    Qt's own words: https://doc.qt.io/qt-6/axisticker.html#isFlipped
    """
    #  bool AxisTicker::isFlipped() const
    return self.uglySide.call('ritual_ZNK10AxisTicker9isFlippedEv')

  def isLogarithmic(self) -> bool:
    """
    Calls Qt's 'bool AxisTicker::isLogarithmic() const'.

    Qt's own words: https://doc.qt.io/qt-6/axisticker.html#isLogarithmic
    """
    #  bool AxisTicker::isLogarithmic() const
    return self.uglySide.call('ritual_ZNK10AxisTicker13isLogarithmicEv')

  def base(self) -> float:
    """
    Calls Qt's 'qreal AxisTicker::base() const'.

    Qt's own words: https://doc.qt.io/qt-6/axisticker.html#base
    """
    #  qreal AxisTicker::base() const
    return self.uglySide.call('ritual_ZNK10AxisTicker4baseEv')

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
    Qt's 'AxisTicker::AxisTicker(QQuickItem *parent)': leans on
    'AxisTicker::qt_metacall(QMetaObject::Call, int, void**)', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'AxisTicker.__init__' has no cute function yet. Qt's "
        "'AxisTicker::AxisTicker(QQuickItem *parent)': leans on "
        "'AxisTicker::qt_metacall(QMetaObject::Call, int, void**)', which "
        "Qt's source does not mark for use from outside Qt and has no code "
        "for that could be taken.")

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

  def setupShaders(self) -> None:
    """
    Calls Qt's 'void AxisTicker::setupShaders()'.

    Qt's own words: https://doc.qt.io/qt-6/axisticker.html#setupShaders
    """
    #  void AxisTicker::setupShaders()
    self.uglySide.call('ritual_ZN10AxisTicker12setupShadersEv')

  def componentComplete(self) -> None:
    """
    Calls Qt's 'void AxisTicker::componentComplete()'.

    Qt's own words: https://doc.qt.io/qt-6/axisticker.html#componentComplete
    """
    #  void AxisTicker::componentComplete()
    ritual = 'ritual_ZN10AxisTicker17componentCompleteEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN10AxisTicker17componentCompleteEv'
    self.uglySide.call(ritual)

  @overload(QRectF, QRectF)
  def geometryChange(self, newGeometry: QRectF, oldGeometry: QRectF) -> None:
    """
    Calls Qt's 'void AxisTicker::geometryChange(const QRectF &newGeometry,
    const QRectF &oldGeometry)'.

    Qt's own words: https://doc.qt.io/qt-6/axisticker.html#geometryChange

    Parameters
    ----------

    newGeometry : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    oldGeometry : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void AxisTicker::geometryChange(const QRectF &newGeometry, const
    #      QRectF &oldGeometry)
    self.uglySide.call(
        'ritual_ZN10AxisTicker14geometryChangeERK6QRectFS2_',
        self._valueOf(newGeometry), self._valueOf(oldGeometry),
    )

  def iResolutionChanged(self) -> None:
    """
    Calls Qt's 'void AxisTicker::iResolutionChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/axisticker.html#iResolutionChanged
    """
    #  void AxisTicker::iResolutionChanged()
    self.uglySide.call('ritual_ZN10AxisTicker18iResolutionChangedEv')

  def smoothingChanged(self) -> None:
    """
    Calls Qt's 'void AxisTicker::smoothingChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/axisticker.html#smoothingChanged
    """
    #  void AxisTicker::smoothingChanged()
    self.uglySide.call('ritual_ZN10AxisTicker16smoothingChangedEv')

  def origoChanged(self) -> None:
    """
    Calls Qt's 'void AxisTicker::origoChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/axisticker.html#origoChanged
    """
    #  void AxisTicker::origoChanged()
    self.uglySide.call('ritual_ZN10AxisTicker12origoChangedEv')

  def subTicksVisibleChanged(self) -> None:
    """
    Calls Qt's 'void AxisTicker::subTicksVisibleChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/axisticker.html#subTicksVisibleChanged
    """
    #  void AxisTicker::subTicksVisibleChanged()
    self.uglySide.call('ritual_ZN10AxisTicker22subTicksVisibleChangedEv')

  def spacingChanged(self) -> None:
    """
    Calls Qt's 'void AxisTicker::spacingChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/axisticker.html#spacingChanged
    """
    #  void AxisTicker::spacingChanged()
    self.uglySide.call('ritual_ZN10AxisTicker14spacingChangedEv')

  def displacementChanged(self) -> None:
    """
    Calls Qt's 'void AxisTicker::displacementChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/axisticker.html#displacementChanged
    """
    #  void AxisTicker::displacementChanged()
    self.uglySide.call('ritual_ZN10AxisTicker19displacementChangedEv')

  def subTickColorChanged(self) -> None:
    """
    Calls Qt's 'void AxisTicker::subTickColorChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/axisticker.html#subTickColorChanged
    """
    #  void AxisTicker::subTickColorChanged()
    self.uglySide.call('ritual_ZN10AxisTicker19subTickColorChangedEv')

  def tickColorChanged(self) -> None:
    """
    Calls Qt's 'void AxisTicker::tickColorChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/axisticker.html#tickColorChanged
    """
    #  void AxisTicker::tickColorChanged()
    self.uglySide.call('ritual_ZN10AxisTicker16tickColorChangedEv')

  def subTickLineWidthChanged(self) -> None:
    """
    Calls Qt's 'void AxisTicker::subTickLineWidthChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/axisticker.html#subTickLineWidthChanged
    """
    #  void AxisTicker::subTickLineWidthChanged()
    self.uglySide.call('ritual_ZN10AxisTicker23subTickLineWidthChangedEv')

  def tickLineWidthChanged(self) -> None:
    """
    Calls Qt's 'void AxisTicker::tickLineWidthChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/axisticker.html#tickLineWidthChanged
    """
    #  void AxisTicker::tickLineWidthChanged()
    self.uglySide.call('ritual_ZN10AxisTicker20tickLineWidthChangedEv')

  def subTickScaleChanged(self) -> None:
    """
    Calls Qt's 'void AxisTicker::subTickScaleChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/axisticker.html#subTickScaleChanged
    """
    #  void AxisTicker::subTickScaleChanged()
    self.uglySide.call('ritual_ZN10AxisTicker19subTickScaleChangedEv')

  def subTickLengthChanged(self) -> None:
    """
    Calls Qt's 'void AxisTicker::subTickLengthChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/axisticker.html#subTickLengthChanged
    """
    #  void AxisTicker::subTickLengthChanged()
    self.uglySide.call('ritual_ZN10AxisTicker20subTickLengthChangedEv')

  def isHorizontalChanged(self) -> None:
    """
    Calls Qt's 'void AxisTicker::isHorizontalChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/axisticker.html#isHorizontalChanged
    """
    #  void AxisTicker::isHorizontalChanged()
    self.uglySide.call('ritual_ZN10AxisTicker19isHorizontalChangedEv')

  def flippedChanged(self) -> None:
    """
    Calls Qt's 'void AxisTicker::flippedChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/axisticker.html#flippedChanged
    """
    #  void AxisTicker::flippedChanged()
    self.uglySide.call('ritual_ZN10AxisTicker14flippedChangedEv')

  def logarithmicChanged(self) -> None:
    """
    Calls Qt's 'void AxisTicker::logarithmicChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/axisticker.html#logarithmicChanged
    """
    #  void AxisTicker::logarithmicChanged()
    self.uglySide.call('ritual_ZN10AxisTicker18logarithmicChangedEv')

  def baseChanged(self) -> None:
    """
    Calls Qt's 'void AxisTicker::baseChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/axisticker.html#baseChanged
    """
    #  void AxisTicker::baseChanged()
    self.uglySide.call('ritual_ZN10AxisTicker11baseChangedEv')

  @staticmethod
  def setBase(*__, **_) -> Never:
    """
    Qt's 'void AxisTicker::setBase(qreal newBase)': leans on
    'AxisTicker::baseChanged()', which Qt's source does not mark for use from
    outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'AxisTicker.setBase' has no cute function yet. Qt's 'void "
        "AxisTicker::setBase(qreal newBase)': leans on "
        "'AxisTicker::baseChanged()', which Qt's source does not mark for "
        "use from outside Qt and has no code for that could be taken.")

  @staticmethod
  def setDisplacement(*__, **_) -> Never:
    """
    Qt's 'void AxisTicker::setDisplacement(qreal newDisplacement)': leans on
    'AxisTicker::displacementChanged()', which Qt's source does not mark for
    use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'AxisTicker.setDisplacement' has no cute function yet. Qt's 'void "
        "AxisTicker::setDisplacement(qreal newDisplacement)': leans on "
        "'AxisTicker::displacementChanged()', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def setFlipped(*__, **_) -> Never:
    """
    Qt's 'void AxisTicker::setFlipped(bool newFlipped)': leans on
    'AxisTicker::flippedChanged()', which Qt's source does not mark for use
    from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'AxisTicker.setFlipped' has no cute function yet. Qt's 'void "
        "AxisTicker::setFlipped(bool newFlipped)': leans on "
        "'AxisTicker::flippedChanged()', which Qt's source does not mark "
        "for use from outside Qt and has no code for that could be taken.")

  @staticmethod
  def setIsHorizontal(*__, **_) -> Never:
    """
    Qt's 'void AxisTicker::setIsHorizontal(bool newIsHorizontal)': leans on
    'AxisTicker::isHorizontalChanged()', which Qt's source does not mark for
    use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'AxisTicker.setIsHorizontal' has no cute function yet. Qt's 'void "
        "AxisTicker::setIsHorizontal(bool newIsHorizontal)': leans on "
        "'AxisTicker::isHorizontalChanged()', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def setLogarithmic(*__, **_) -> Never:
    """
    Qt's 'void AxisTicker::setLogarithmic(bool newLogarithmic)': leans on
    'AxisTicker::logarithmicChanged()', which Qt's source does not mark for
    use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'AxisTicker.setLogarithmic' has no cute function yet. Qt's 'void "
        "AxisTicker::setLogarithmic(bool newLogarithmic)': leans on "
        "'AxisTicker::logarithmicChanged()', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def setOrigo(*__, **_) -> Never:
    """
    Qt's 'void AxisTicker::setOrigo(int newOrigo)': leans on
    'AxisTicker::origoChanged()', which Qt's source does not mark for use
    from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'AxisTicker.setOrigo' has no cute function yet. Qt's 'void "
        "AxisTicker::setOrigo(int newOrigo)': leans on "
        "'AxisTicker::origoChanged()', which Qt's source does not mark for "
        "use from outside Qt and has no code for that could be taken.")

  @staticmethod
  def setSmoothing(*__, **_) -> Never:
    """
    Qt's 'void AxisTicker::setSmoothing(qreal newSmoothing)': leans on
    'AxisTicker::smoothingChanged()', which Qt's source does not mark for use
    from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'AxisTicker.setSmoothing' has no cute function yet. Qt's 'void "
        "AxisTicker::setSmoothing(qreal newSmoothing)': leans on "
        "'AxisTicker::smoothingChanged()', which Qt's source does not mark "
        "for use from outside Qt and has no code for that could be taken.")

  @staticmethod
  def setSpacing(*__, **_) -> Never:
    """
    Qt's 'void AxisTicker::setSpacing(qreal newSpacing)': leans on
    'AxisTicker::spacingChanged()', which Qt's source does not mark for use
    from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'AxisTicker.setSpacing' has no cute function yet. Qt's 'void "
        "AxisTicker::setSpacing(qreal newSpacing)': leans on "
        "'AxisTicker::spacingChanged()', which Qt's source does not mark "
        "for use from outside Qt and has no code for that could be taken.")

  @staticmethod
  def setSubTickColor(*__, **_) -> Never:
    """
    Qt's 'void AxisTicker::setSubTickColor(QColor newSubTickColor)': leans on
    'AxisTicker::subTickColorChanged()', which Qt's source does not mark for
    use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'AxisTicker.setSubTickColor' has no cute function yet. Qt's 'void "
        "AxisTicker::setSubTickColor(QColor newSubTickColor)': leans on "
        "'AxisTicker::subTickColorChanged()', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def setSubTickLength(*__, **_) -> Never:
    """
    Qt's 'void AxisTicker::setSubTickLength(qreal newSubTickLength)': leans
    on 'AxisTicker::subTickLengthChanged()', which Qt's source does not mark
    for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'AxisTicker.setSubTickLength' has no cute function yet. Qt's 'void "
        "AxisTicker::setSubTickLength(qreal newSubTickLength)': leans on "
        "'AxisTicker::subTickLengthChanged()', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def setSubTickLineWidth(*__, **_) -> Never:
    """
    Qt's 'void AxisTicker::setSubTickLineWidth(qreal newSubTickLineWidth)':
    leans on 'AxisTicker::subTickLineWidthChanged()', which Qt's source does
    not mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'AxisTicker.setSubTickLineWidth' has no cute function yet. Qt's "
        "'void AxisTicker::setSubTickLineWidth(qreal newSubTickLineWidth)': "
        "leans on 'AxisTicker::subTickLineWidthChanged()', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def setSubTickScale(*__, **_) -> Never:
    """
    Qt's 'void AxisTicker::setSubTickScale(qreal newSubTickScale)': leans on
    'AxisTicker::subTickScaleChanged()', which Qt's source does not mark for
    use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'AxisTicker.setSubTickScale' has no cute function yet. Qt's 'void "
        "AxisTicker::setSubTickScale(qreal newSubTickScale)': leans on "
        "'AxisTicker::subTickScaleChanged()', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def setSubTicksVisible(*__, **_) -> Never:
    """
    Qt's 'void AxisTicker::setSubTicksVisible(bool newSubTicksVisible)':
    leans on 'AxisTicker::subTicksVisibleChanged()', which Qt's source does
    not mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'AxisTicker.setSubTicksVisible' has no cute function yet. Qt's "
        "'void AxisTicker::setSubTicksVisible(bool newSubTicksVisible)': "
        "leans on 'AxisTicker::subTicksVisibleChanged()', which Qt's source "
        "does not mark for use from outside Qt and has no code for that "
        "could be taken.")

  @staticmethod
  def setTickColor(*__, **_) -> Never:
    """
    Qt's 'void AxisTicker::setTickColor(QColor newTickColor)': leans on
    'AxisTicker::tickColorChanged()', which Qt's source does not mark for use
    from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'AxisTicker.setTickColor' has no cute function yet. Qt's 'void "
        "AxisTicker::setTickColor(QColor newTickColor)': leans on "
        "'AxisTicker::tickColorChanged()', which Qt's source does not mark "
        "for use from outside Qt and has no code for that could be taken.")

  @staticmethod
  def setTickLineWidth(*__, **_) -> Never:
    """
    Qt's 'void AxisTicker::setTickLineWidth(qreal newTickLineWidth)': leans
    on 'AxisTicker::tickLineWidthChanged()', which Qt's source does not mark
    for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'AxisTicker.setTickLineWidth' has no cute function yet. Qt's 'void "
        "AxisTicker::setTickLineWidth(qreal newTickLineWidth)': leans on "
        "'AxisTicker::tickLineWidthChanged()', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")
