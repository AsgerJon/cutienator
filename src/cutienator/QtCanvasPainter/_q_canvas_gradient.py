"""
QCanvasGradient binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCanvasPainter/qcanvasgradient.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QList
from . import QCanvasBrush

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from ..QtGui import QColor
  from . import QCanvasGradientStop, QCanvasImage
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QCanvasGradientStop = WAIT['QCanvasGradientStop']
  QCanvasImage = WAIT['QCanvasImage']
  QColor = WAIT['QColor']


class QCanvasGradient(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QCanvasGradient: a plain Python object standing in
  front of one C++ QCanvasGradient.

  What exists
  -----------

  Every function of Qt's QCanvasGradient that has a ritual and that Python
  can call so far, 10 names in all: 'type', 'startColor', 'setStartColor',
  'endColor', 'setEndColor', 'setColorAt', 'setStops', 'stops', 'setImage',
  'addColorStop'. It can be made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QCanvasBrush QCanvasGradient::operator QCanvasBrush() const': an
    operator Python has no name for.
  - Qt's 'QVariant QCanvasGradient::operator QVariant() const': an operator
    Python has no name for.
  - Qt's 'QCanvasGradient::QCanvasGradient(const QCanvasGradient &a0)': takes
    a type Python has no way to hand over yet.
  - Qt's 'QCanvasGradient &QCanvasGradient::operator=(const QCanvasGradient
    &a0)': assignment: Python binds a name and has no operator for it.
  - Qt's 'QCanvasGradient::QCanvasGradient(QCanvasGradient &&a0)': takes a
    type Python has no way to hand over yet.
  - Qt's 'QCanvasGradient &QCanvasGradient::operator=(QCanvasGradient &&a0)':
    assignment: Python binds a name and has no operator for it.
  - Qt's 'QCanvasGradient::~QCanvasGradient()': the destructor: Python never
    removes a C++ QCanvasGradient.
  - Qt's 'void QCanvasGradient::swap(QCanvasGradient &other)': takes a type
    Python has no way to hand over yet.
  - Qt's 'bool operator==(const QCanvasGradient &lhs, const QCanvasGradient
    &rhs)': an operator between other classes, written inside this one.
  - Qt's 'bool operator!=(const QCanvasGradient &lhs, const QCanvasGradient
    &rhs)': an operator between other classes, written inside this one.
  - Qt's 'QDebug operator<<(QDebug a0, const QCanvasGradient &a1)': an
    operator between other classes, written inside this one.
  - Qt's 'QDataStream &operator<<(QDataStream &a0, const QCanvasGradient
    &a1)': an operator between other classes, written inside this one.
  - Qt's 'QDataStream &operator>>(QDataStream &a0, QCanvasGradient &a1)': an
    operator between other classes, written inside this one.

  What has no ritual
  ------------------

  2 of the 27 functions Qt declares: 1 forbidden; 1 not a gap.

  What to expect
  --------------

  - The C++ QCanvasGradient is created at the first use, not by
    'QCanvasGradient(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QCanvasGradient.
  - Each name of Qt's QCanvasGradient that has no cute function yet, 'swap',
    holds a function that raises 'NotImplementedError', and its docstring
    says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QCanvasGradient'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def type(self) -> QCanvasBrush.BrushType:
    """
    Calls Qt's 'QCanvasBrush::BrushType QCanvasGradient::type() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcanvasgradient.html#type

    Returns
    -------

    QCanvasBrush.BrushType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QCanvasBrush.BrushType(number)' gives.
    """
    #  QCanvasBrush::BrushType QCanvasGradient::type() const
    return QCanvasBrush.BrushType(self.uglySide.call(
        'ritual_ZNK15QCanvasGradient4typeEv',
    ))

  def startColor(self) -> QColor:
    """
    Calls Qt's 'QColor QCanvasGradient::startColor() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcanvasgradient.html#startColor

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QCanvasGradient::startColor() const
    address = self.uglySide.call('ritual_ZNK15QCanvasGradient10startColorEv')
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def endColor(self) -> QColor:
    """
    Calls Qt's 'QColor QCanvasGradient::endColor() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcanvasgradient.html#endColor

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QCanvasGradient::endColor() const
    address = self.uglySide.call('ritual_ZNK15QCanvasGradient8endColorEv')
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def stops(self) -> QList[QCanvasGradientStop]:
    """
    Calls Qt's 'QCanvasGradientStops QCanvasGradient::stops() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcanvasgradient.html#stops

    Returns
    -------

    QList[QCanvasGradientStop]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QCanvasGradientStops QCanvasGradient::stops() const
    address = self.uglySide.call('ritual_ZNK15QCanvasGradient5stopsEv')
    from . import QCanvasGradientStop
    return QList[QCanvasGradientStop]._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QColor)
  def setStartColor(self, color: QColor) -> None:
    """
    Calls Qt's 'void QCanvasGradient::setStartColor(QColor color)'.

    Qt's own words: https://doc.qt.io/qt-6/qcanvasgradient.html#setStartColor

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QCanvasGradient::setStartColor(QColor color)
    self.uglySide.call(
        'ritual_ZN15QCanvasGradient13setStartColorE6QColor',
        self._valueOf(color),
    )

  @overload(QColor)
  def setEndColor(self, color: QColor) -> None:
    """
    Calls Qt's 'void QCanvasGradient::setEndColor(QColor color)'.

    Qt's own words: https://doc.qt.io/qt-6/qcanvasgradient.html#setEndColor

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QCanvasGradient::setEndColor(QColor color)
    self.uglySide.call(
        'ritual_ZN15QCanvasGradient11setEndColorE6QColor',
        self._valueOf(color),
    )

  @overload(float, QColor)
  def setColorAt(self, position: float, color: QColor) -> None:
    """
    Calls Qt's 'void QCanvasGradient::setColorAt(qreal position, QColor
    color)'.

    Qt's own words: https://doc.qt.io/qt-6/qcanvasgradient.html#setColorAt

    Parameters
    ----------

    position : float
      Passed on as it is.

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QCanvasGradient::setColorAt(qreal position, QColor color)
    self.uglySide.call(
        'ritual_ZN15QCanvasGradient10setColorAtEd6QColor',
        position, self._valueOf(color),
    )

  @overload(QList[QCanvasGradientStop])
  def setStops(self, stops: QList[QCanvasGradientStop]) -> None:
    """
    Calls Qt's 'void QCanvasGradient::setStops(const QCanvasGradientStops
    &stops)'.

    Qt's own words: https://doc.qt.io/qt-6/qcanvasgradient.html#setStops

    Parameters
    ----------

    stops : QList[QCanvasGradientStop]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QCanvasGradient::setStops(const QCanvasGradientStops &stops)
    self.uglySide.call(
        'ritual_ZN15QCanvasGradient8setStopsERK5QListI19QCanvasGradientStop'
        'E',
        self._valueOf(stops),
    )

  @overload(QCanvasImage)
  @overload(QCanvasImage, int)
  def setImage(self, image: QCanvasImage, index: int = 0) -> None:
    """
    Calls Qt's 'void QCanvasGradient::setImage(const QCanvasImage &image, int
    index)'.

    Qt's own words: https://doc.qt.io/qt-6/qcanvasgradient.html#setImage

    Parameters
    ----------

    image : QCanvasImage
      Passed on as a value: Qt reads the C++ QCanvasImage, which stays
      Python's own.

    index : int
      Passed on as it is. May be left out, as in Qt: it is then 0.
    """
    #  void QCanvasGradient::setImage(const QCanvasImage &image, int index)
    self.uglySide.call(
        'ritual_ZN15QCanvasGradient8setImageERK12QCanvasImagei',
        self._valueOf(image), index,
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

  @overload(QCanvasBrush.BrushType)
  def __init__(self, type: QCanvasBrush.BrushType) -> None:
    """
    Notes what was given, for Qt's
    'QCanvasGradient::QCanvasGradient(QCanvasBrush::BrushType type)', which
    is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanvasgradient.html#QCanvasGradient

    Parameters
    ----------

    type : QCanvasBrush.BrushType
      Passed on as its number.
    """
    #  QCanvasGradient::QCanvasGradient(QCanvasBrush::BrushType type)
    self._noteCreation(QCanvasGradient, lambda: Rituals.call(
        'ritual_ZN15QCanvasGradientC1EN12QCanvasBrush9BrushTypeE',
        type.value,
    ))

  @overload(QCanvasBrush)
  def __init__(self, brush: QCanvasBrush) -> None:
    """
    Notes what was given, for Qt's 'QCanvasGradient::QCanvasGradient(const
    QCanvasBrush &brush)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanvasgradient.html#QCanvasGradient

    Parameters
    ----------

    brush : QCanvasBrush
      Passed on as a value: Qt reads the C++ QCanvasBrush, which stays
      Python's own.
    """
    #  QCanvasGradient::QCanvasGradient(const QCanvasBrush &brush)
    self._noteCreation(QCanvasGradient, lambda: Rituals.call(
        'ritual_ZN15QCanvasGradientC1ERK12QCanvasBrush',
        self._valueOf(brush),
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

  @overload(float, QColor)
  def addColorStop(self, position: float, color: QColor) -> None:
    """
    Calls Qt's 'void QCanvasGradient::addColorStop(qreal position, QColor
    color)'.

    Qt's own words: https://doc.qt.io/qt-6/qcanvasgradient.html#addColorStop

    Parameters
    ----------

    position : float
      Passed on as it is.

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QCanvasGradient::addColorStop(qreal position, QColor color)
    self.uglySide.call(
        'ritual_ZN15QCanvasGradient12addColorStopEd6QColor',
        position, self._valueOf(color),
    )

  @staticmethod
  def swap(*__, **_) -> Never:
    """
    Qt's 'void QCanvasGradient::swap(QCanvasGradient &other)': takes a type
    Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QCanvasGradient.swap' has no cute function yet. Qt's 'void "
        "QCanvasGradient::swap(QCanvasGradient &other)': takes a type "
        "Python has no way to hand over yet.")
