"""
QCanvasLinearGradient binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCanvasPainter/qcanvaslineargradient.h, Qt 6.12.0. Changes made here are
#  lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from . import QCanvasGradient

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from ..QtCore import QPointF
  from . import QCanvasBrush
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QCanvasBrush = WAIT['QCanvasBrush']
  QPointF = WAIT['QPointF']


class QCanvasLinearGradient(QCanvasGradient):
  """
  The cute side of Qt's QCanvasLinearGradient: a plain Python object standing
  in front of one C++ QCanvasLinearGradient.

  It is built on the cute 'QCanvasGradient', as Qt's QCanvasLinearGradient is
  built on Qt's QCanvasGradient, and has everything that class has.

  C++ hands a QCanvasLinearGradient around as a copy, so every C++
  QCanvasLinearGradient behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QCanvasLinearGradient that has a ritual and that
  Python can call so far, 4 names in all: 'startPosition',
  'setStartPosition', 'endPosition', 'setEndPosition'. It can be made from
  Python, in 5 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QCanvasLinearGradient &QCanvasLinearGradient::operator=(const
    QCanvasLinearGradient &a0)': assignment: Python binds a name and has no
    operator for it.
  - Qt's 'QCanvasLinearGradient::QCanvasLinearGradient(QCanvasLinearGradient
    &&a0)': takes a type Python has no way to hand over yet.
  - Qt's 'QCanvasLinearGradient
    &QCanvasLinearGradient::operator=(QCanvasLinearGradient &&a0)':
    assignment: Python binds a name and has no operator for it.
  - Qt's 'QCanvasLinearGradient::~QCanvasLinearGradient()': the destructor:
    Python removes its C++ QCanvasLinearGradient by it, and has no other use
    for it.
  - Qt's 'void QCanvasLinearGradient::swap(QCanvasLinearGradient &other)':
    takes a type Python has no way to hand over yet.

  What to expect
  --------------

  - The C++ QCanvasLinearGradient is created at the first use, not by
    'QCanvasLinearGradient(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QCanvasLinearGradient back gives a copy the ritual
    made for Python, in a new cute QCanvasLinearGradient.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QCanvasLinearGradient'

  #  Qt's '~QCanvasLinearGradient()'. Naming it makes this a value class:
  #  Python owns every C++ QCanvasLinearGradient behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN21QCanvasLinearGradientD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def startPosition(self) -> QPointF:
    """
    Calls Qt's 'QPointF QCanvasLinearGradient::startPosition() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanvaslineargradient.html#startPosition

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QCanvasLinearGradient::startPosition() const
    address = self.uglySide.call(
        'ritual_ZNK21QCanvasLinearGradient13startPositionEv',
    )
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  def endPosition(self) -> QPointF:
    """
    Calls Qt's 'QPointF QCanvasLinearGradient::endPosition() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanvaslineargradient.html#endPosition

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QCanvasLinearGradient::endPosition() const
    address = self.uglySide.call(
        'ritual_ZNK21QCanvasLinearGradient11endPositionEv',
    )
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float, float)
  def setStartPosition(self, x: float, y: float) -> None:
    """
    Calls Qt's 'void QCanvasLinearGradient::setStartPosition(qreal x, qreal
    y)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanvaslineargradient.html#setStartPosition

    Parameters
    ----------

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.
    """
    #  void QCanvasLinearGradient::setStartPosition(qreal x, qreal y)
    self.uglySide.call(
        'ritual_ZN21QCanvasLinearGradient16setStartPositionEdd', x, y,
    )

  @overload(QPointF)
  def setStartPosition(self, start: QPointF) -> None:
    """
    Calls Qt's 'void QCanvasLinearGradient::setStartPosition(QPointF start)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanvaslineargradient.html#setStartPosition

    Parameters
    ----------

    start : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  void QCanvasLinearGradient::setStartPosition(QPointF start)
    self.uglySide.call(
        'ritual_ZN21QCanvasLinearGradient16setStartPositionE7QPointF',
        self._valueOf(start, 'QPointF'),
    )

  @overload(float, float)
  def setEndPosition(self, x: float, y: float) -> None:
    """
    Calls Qt's 'void QCanvasLinearGradient::setEndPosition(qreal x, qreal
    y)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanvaslineargradient.html#setEndPosition

    Parameters
    ----------

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.
    """
    #  void QCanvasLinearGradient::setEndPosition(qreal x, qreal y)
    self.uglySide.call(
        'ritual_ZN21QCanvasLinearGradient14setEndPositionEdd', x, y,
    )

  @overload(QPointF)
  def setEndPosition(self, end: QPointF) -> None:
    """
    Calls Qt's 'void QCanvasLinearGradient::setEndPosition(QPointF end)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanvaslineargradient.html#setEndPosition

    Parameters
    ----------

    end : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  void QCanvasLinearGradient::setEndPosition(QPointF end)
    self.uglySide.call(
        'ritual_ZN21QCanvasLinearGradient14setEndPositionE7QPointF',
        self._valueOf(end, 'QPointF'),
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
    Notes what was given, for Qt's
    'QCanvasLinearGradient::QCanvasLinearGradient()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanvaslineargradient.html#QCanvasLinearGradient
    """
    #  QCanvasLinearGradient::QCanvasLinearGradient()
    self._noteCreation(QCanvasLinearGradient, lambda: Rituals.call(
        'ritual_ZN21QCanvasLinearGradientC1Ev',
    ))

  @overload(float, float, float, float)
  def __init__(
      self,
      startX: float,
      startY: float,
      endX: float,
      endY: float,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QCanvasLinearGradient::QCanvasLinearGradient(qreal startX, qreal startY,
    qreal endX, qreal endY)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanvaslineargradient.html#QCanvasLinearGradient

    Parameters
    ----------

    startX : float
      Passed on as it is.

    startY : float
      Passed on as it is.

    endX : float
      Passed on as it is.

    endY : float
      Passed on as it is.
    """
    #  QCanvasLinearGradient::QCanvasLinearGradient(qreal startX, qreal
    #      startY, qreal endX, qreal endY)
    self._noteCreation(QCanvasLinearGradient, lambda: Rituals.call(
        'ritual_ZN21QCanvasLinearGradientC1Edddd',
        startX, startY, endX, endY,
    ))

  @overload(QPointF, QPointF)
  def __init__(self, start: QPointF, end: QPointF) -> None:
    """
    Notes what was given, for Qt's
    'QCanvasLinearGradient::QCanvasLinearGradient(QPointF start, QPointF
    end)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanvaslineargradient.html#QCanvasLinearGradient

    Parameters
    ----------

    start : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    end : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  QCanvasLinearGradient::QCanvasLinearGradient(QPointF start, QPointF
    #      end)
    self._noteCreation(QCanvasLinearGradient, lambda: Rituals.call(
        'ritual_ZN21QCanvasLinearGradientC1E7QPointFS0_',
        self._valueOf(start, 'QPointF'), self._valueOf(end, 'QPointF'),
    ))

  @overload(THIS)
  def __init__(self, a0: QCanvasLinearGradient) -> None:
    """
    Notes what was given, for Qt's
    'QCanvasLinearGradient::QCanvasLinearGradient(const QCanvasLinearGradient
    &a0)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanvaslineargradient.html#QCanvasLinearGradient

    Parameters
    ----------

    a0 : QCanvasLinearGradient
      Passed on as a value: Qt reads the C++ QCanvasLinearGradient, which
      stays Python's own.
    """
    #  QCanvasLinearGradient::QCanvasLinearGradient(const
    #      QCanvasLinearGradient &a0)
    self._noteCreation(QCanvasLinearGradient, lambda: Rituals.call(
        'ritual_ZN21QCanvasLinearGradientC1ERKS_', self._valueOf(a0),
    ))

  @overload(QCanvasBrush)
  def __init__(self, brush: QCanvasBrush) -> None:
    """
    Notes what was given, for Qt's
    'QCanvasLinearGradient::QCanvasLinearGradient(const QCanvasBrush
    &brush)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanvaslineargradient.html#QCanvasLinearGradient

    Parameters
    ----------

    brush : QCanvasBrush
      Passed on as a value: Qt reads the C++ QCanvasBrush, which stays
      Python's own.
    """
    #  QCanvasLinearGradient::QCanvasLinearGradient(const QCanvasBrush
    #      &brush)
    self._noteCreation(QCanvasLinearGradient, lambda: Rituals.call(
        'ritual_ZN21QCanvasLinearGradientC1ERK12QCanvasBrush',
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
