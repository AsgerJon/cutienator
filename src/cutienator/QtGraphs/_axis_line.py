"""
AxisLine binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGraphs/6.12.0/QtGraphs/private/axisline_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means AxisLine to be private: it declares the class in a header it
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


class AxisLine(QQuickShaderEffect):
  """
  The cute side of Qt's AxisLine: a plain Python object standing in front of
  one C++ AxisLine.

  It is built on the cute 'QQuickShaderEffect', as Qt's AxisLine is built on
  Qt's QQuickShaderEffect, and has everything that class has.

  What exists
  -----------

  Every function of Qt's AxisLine that has a ritual and that Python can call
  so far, 14 names in all: 'metaObject', 'setupShaders', 'iResolution',
  'smoothing', 'color', 'lineWidth', 'isHorizontal', 'componentComplete',
  'geometryChange', 'iResolutionChanged', 'smoothingChanged', 'colorChanged',
  'lineWidthChanged', 'isHorizontalChanged'. None can be made from Python:
  one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *AxisLine::qt_metacast(const char *a0)': one of Qt's own inner
    workings.
  - Qt's 'int AxisLine::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'AxisLine::~AxisLine()': the destructor: Python never removes a C++
    AxisLine.

  What has no ritual
  ------------------

  8 of the 25 functions Qt declares: 6 leans on 'AxisLine; 2 not a gap.

  What to expect
  --------------

  - The C++ AxisLine is created at the first use, not by 'AxisLine(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ AxisLine.
  - Qt tells when it has removed the C++ AxisLine. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
  - Each name of Qt's AxisLine that has no cute function yet, '__init__',
    'setColor', 'setIsHorizontal', 'setLineWidth', 'setSmoothing', holds a
    function that raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'AxisLine'

  #  A C++ AxisLine Python makes is of a C++ class of ours, in which Python
  #  can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_AxisLine'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *AxisLine::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/axisline.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *AxisLine::metaObject() const
    address = self.uglySide.call('ritual_ZNK8AxisLine10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def iResolution(self) -> QVector3D:
    """
    Calls Qt's 'QVector3D AxisLine::iResolution() const'.

    Qt's own words: https://doc.qt.io/qt-6/axisline.html#iResolution

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  QVector3D AxisLine::iResolution() const
    address = self.uglySide.call('ritual_ZNK8AxisLine11iResolutionEv')
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  def smoothing(self) -> float:
    """
    Calls Qt's 'qreal AxisLine::smoothing() const'.

    Qt's own words: https://doc.qt.io/qt-6/axisline.html#smoothing
    """
    #  qreal AxisLine::smoothing() const
    return self.uglySide.call('ritual_ZNK8AxisLine9smoothingEv')

  def color(self) -> QColor:
    """
    Calls Qt's 'QColor AxisLine::color() const'.

    Qt's own words: https://doc.qt.io/qt-6/axisline.html#color

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor AxisLine::color() const
    address = self.uglySide.call('ritual_ZNK8AxisLine5colorEv')
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def lineWidth(self) -> float:
    """
    Calls Qt's 'qreal AxisLine::lineWidth() const'.

    Qt's own words: https://doc.qt.io/qt-6/axisline.html#lineWidth
    """
    #  qreal AxisLine::lineWidth() const
    return self.uglySide.call('ritual_ZNK8AxisLine9lineWidthEv')

  def isHorizontal(self) -> bool:
    """
    Calls Qt's 'bool AxisLine::isHorizontal() const'.

    Qt's own words: https://doc.qt.io/qt-6/axisline.html#isHorizontal
    """
    #  bool AxisLine::isHorizontal() const
    return self.uglySide.call('ritual_ZNK8AxisLine12isHorizontalEv')

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
    Qt's 'AxisLine::AxisLine(QQuickItem *parent)': leans on
    'AxisLine::qt_metacall(QMetaObject::Call, int, void**)', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'AxisLine.__init__' has no cute function yet. Qt's "
        "'AxisLine::AxisLine(QQuickItem *parent)': leans on "
        "'AxisLine::qt_metacall(QMetaObject::Call, int, void**)', which "
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
    Calls Qt's 'void AxisLine::setupShaders()'.

    Qt's own words: https://doc.qt.io/qt-6/axisline.html#setupShaders
    """
    #  void AxisLine::setupShaders()
    self.uglySide.call('ritual_ZN8AxisLine12setupShadersEv')

  def componentComplete(self) -> None:
    """
    Calls Qt's 'void AxisLine::componentComplete()'.

    Qt's own words: https://doc.qt.io/qt-6/axisline.html#componentComplete
    """
    #  void AxisLine::componentComplete()
    ritual = 'ritual_ZN8AxisLine17componentCompleteEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN8AxisLine17componentCompleteEv'
    self.uglySide.call(ritual)

  @overload(QRectF, QRectF)
  def geometryChange(self, newGeometry: QRectF, oldGeometry: QRectF) -> None:
    """
    Calls Qt's 'void AxisLine::geometryChange(const QRectF &newGeometry,
    const QRectF &oldGeometry)'.

    Qt's own words: https://doc.qt.io/qt-6/axisline.html#geometryChange

    Parameters
    ----------

    newGeometry : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    oldGeometry : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void AxisLine::geometryChange(const QRectF &newGeometry, const QRectF
    #      &oldGeometry)
    self.uglySide.call(
        'ritual_ZN8AxisLine14geometryChangeERK6QRectFS2_',
        self._valueOf(newGeometry), self._valueOf(oldGeometry),
    )

  def iResolutionChanged(self) -> None:
    """
    Calls Qt's 'void AxisLine::iResolutionChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/axisline.html#iResolutionChanged
    """
    #  void AxisLine::iResolutionChanged()
    self.uglySide.call('ritual_ZN8AxisLine18iResolutionChangedEv')

  def smoothingChanged(self) -> None:
    """
    Calls Qt's 'void AxisLine::smoothingChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/axisline.html#smoothingChanged
    """
    #  void AxisLine::smoothingChanged()
    self.uglySide.call('ritual_ZN8AxisLine16smoothingChangedEv')

  def colorChanged(self) -> None:
    """
    Calls Qt's 'void AxisLine::colorChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/axisline.html#colorChanged
    """
    #  void AxisLine::colorChanged()
    self.uglySide.call('ritual_ZN8AxisLine12colorChangedEv')

  def lineWidthChanged(self) -> None:
    """
    Calls Qt's 'void AxisLine::lineWidthChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/axisline.html#lineWidthChanged
    """
    #  void AxisLine::lineWidthChanged()
    self.uglySide.call('ritual_ZN8AxisLine16lineWidthChangedEv')

  def isHorizontalChanged(self) -> None:
    """
    Calls Qt's 'void AxisLine::isHorizontalChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/axisline.html#isHorizontalChanged
    """
    #  void AxisLine::isHorizontalChanged()
    self.uglySide.call('ritual_ZN8AxisLine19isHorizontalChangedEv')

  @staticmethod
  def setColor(*__, **_) -> Never:
    """
    Qt's 'void AxisLine::setColor(QColor newColor)': leans on
    'AxisLine::colorChanged()', which Qt's source does not mark for use from
    outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'AxisLine.setColor' has no cute function yet. Qt's 'void "
        "AxisLine::setColor(QColor newColor)': leans on "
        "'AxisLine::colorChanged()', which Qt's source does not mark for "
        "use from outside Qt and has no code for that could be taken.")

  @staticmethod
  def setIsHorizontal(*__, **_) -> Never:
    """
    Qt's 'void AxisLine::setIsHorizontal(bool newIsHorizontal)': leans on
    'AxisLine::isHorizontalChanged()', which Qt's source does not mark for
    use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'AxisLine.setIsHorizontal' has no cute function yet. Qt's 'void "
        "AxisLine::setIsHorizontal(bool newIsHorizontal)': leans on "
        "'AxisLine::isHorizontalChanged()', which Qt's source does not mark "
        "for use from outside Qt and has no code for that could be taken.")

  @staticmethod
  def setLineWidth(*__, **_) -> Never:
    """
    Qt's 'void AxisLine::setLineWidth(qreal newLineWidth)': leans on
    'AxisLine::lineWidthChanged()', which Qt's source does not mark for use
    from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'AxisLine.setLineWidth' has no cute function yet. Qt's 'void "
        "AxisLine::setLineWidth(qreal newLineWidth)': leans on "
        "'AxisLine::lineWidthChanged()', which Qt's source does not mark "
        "for use from outside Qt and has no code for that could be taken.")

  @staticmethod
  def setSmoothing(*__, **_) -> Never:
    """
    Qt's 'void AxisLine::setSmoothing(qreal newSmoothing)': leans on
    'AxisLine::smoothingChanged()', which Qt's source does not mark for use
    from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'AxisLine.setSmoothing' has no cute function yet. Qt's 'void "
        "AxisLine::setSmoothing(qreal newSmoothing)': leans on "
        "'AxisLine::smoothingChanged()', which Qt's source does not mark "
        "for use from outside Qt and has no code for that could be taken.")
