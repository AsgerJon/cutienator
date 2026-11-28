"""
QLinearGradient binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of QtGui/qbrush.h,
#  Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..QtCore import QList
from . import QGradient

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from ..QtCore import QPointF
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPointF = WAIT['QPointF']


class QLinearGradient(QGradient):
  """
  The cute side of Qt's QLinearGradient: a plain Python object standing in
  front of one C++ QLinearGradient.

  It is built on the cute 'QGradient', as Qt's QLinearGradient is built on
  Qt's QGradient, and has everything that class has.

  C++ hands a QLinearGradient around as a copy, so every C++ QLinearGradient
  behind a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QLinearGradient that has a ritual and that Python
  can call so far, 4 names in all: 'start', 'setStart', 'finalStop',
  'setFinalStop'. It can be made from Python, in 3 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QLinearGradient::~QLinearGradient()': the destructor: Python
    removes its C++ QLinearGradient by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QLinearGradient is created at the first use, not by
    'QLinearGradient(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QLinearGradient back gives a copy the ritual made for
    Python, in a new cute QLinearGradient.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QLinearGradient'

  #  Qt's '~QLinearGradient()'. Naming it makes this a value class: Python
  #  owns every C++ QLinearGradient behind a cute one, and removes it by this
  #  ritual.
  __delete_ritual__ = 'ritual_ZN15QLinearGradientD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def start(self) -> QPointF:
    """
    Calls Qt's 'QPointF QLinearGradient::start() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlineargradient.html#start

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QLinearGradient::start() const
    address = self.uglySide.call('ritual_ZNK15QLinearGradient5startEv')
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  def finalStop(self) -> QPointF:
    """
    Calls Qt's 'QPointF QLinearGradient::finalStop() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlineargradient.html#finalStop

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QLinearGradient::finalStop() const
    address = self.uglySide.call('ritual_ZNK15QLinearGradient9finalStopEv')
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QPointF)
  def setStart(self, start: QPointF) -> None:
    """
    Calls Qt's 'void QLinearGradient::setStart(const QPointF &start)'.

    Qt's own words: https://doc.qt.io/qt-6/qlineargradient.html#setStart

    Parameters
    ----------

    start : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  void QLinearGradient::setStart(const QPointF &start)
    self.uglySide.call(
        'ritual_ZN15QLinearGradient8setStartERK7QPointF',
        self._valueOf(start, 'QPointF'),
    )

  @overload(float, float)
  def setStart(self, x: float, y: float) -> None:
    """
    Calls Qt's 'void QLinearGradient::setStart(qreal x, qreal y)'.

    Qt's own words: https://doc.qt.io/qt-6/qlineargradient.html#setStart

    Parameters
    ----------

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.
    """
    #  void QLinearGradient::setStart(qreal x, qreal y)
    self.uglySide.call('ritual_ZN15QLinearGradient8setStartEdd', x, y)

  @overload(QPointF)
  def setFinalStop(self, stop: QPointF) -> None:
    """
    Calls Qt's 'void QLinearGradient::setFinalStop(const QPointF &stop)'.

    Qt's own words: https://doc.qt.io/qt-6/qlineargradient.html#setFinalStop

    Parameters
    ----------

    stop : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  void QLinearGradient::setFinalStop(const QPointF &stop)
    self.uglySide.call(
        'ritual_ZN15QLinearGradient12setFinalStopERK7QPointF',
        self._valueOf(stop, 'QPointF'),
    )

  @overload(float, float)
  def setFinalStop(self, x: float, y: float) -> None:
    """
    Calls Qt's 'void QLinearGradient::setFinalStop(qreal x, qreal y)'.

    Qt's own words: https://doc.qt.io/qt-6/qlineargradient.html#setFinalStop

    Parameters
    ----------

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.
    """
    #  void QLinearGradient::setFinalStop(qreal x, qreal y)
    self.uglySide.call('ritual_ZN15QLinearGradient12setFinalStopEdd', x, y)

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
    Notes what was given, for Qt's 'QLinearGradient::QLinearGradient()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qlineargradient.html#QLinearGradient
    """
    #  QLinearGradient::QLinearGradient()
    self._noteCreation(QLinearGradient, lambda: Rituals.call(
        'ritual_ZN15QLinearGradientC1Ev',
    ))

  @overload(QPointF, QPointF)
  def __init__(self, start: QPointF, finalStop: QPointF) -> None:
    """
    Notes what was given, for Qt's 'QLinearGradient::QLinearGradient(const
    QPointF &start, const QPointF &finalStop)', which is called at the first
    use.

    Qt's own words:
    https://doc.qt.io/qt-6/qlineargradient.html#QLinearGradient

    Parameters
    ----------

    start : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    finalStop : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  QLinearGradient::QLinearGradient(const QPointF &start, const QPointF
    #      &finalStop)
    self._noteCreation(QLinearGradient, lambda: Rituals.call(
        'ritual_ZN15QLinearGradientC1ERK7QPointFS2_',
        self._valueOf(start, 'QPointF'), self._valueOf(finalStop, 'QPointF'),
    ))

  @overload(float, float, float, float)
  def __init__(
      self,
      xStart: float,
      yStart: float,
      xFinalStop: float,
      yFinalStop: float,
  ) -> None:
    """
    Notes what was given, for Qt's 'QLinearGradient::QLinearGradient(qreal
    xStart, qreal yStart, qreal xFinalStop, qreal yFinalStop)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qlineargradient.html#QLinearGradient

    Parameters
    ----------

    xStart : float
      Passed on as it is.

    yStart : float
      Passed on as it is.

    xFinalStop : float
      Passed on as it is.

    yFinalStop : float
      Passed on as it is.
    """
    #  QLinearGradient::QLinearGradient(qreal xStart, qreal yStart, qreal
    #      xFinalStop, qreal yFinalStop)
    self._noteCreation(QLinearGradient, lambda: Rituals.call(
        'ritual_ZN15QLinearGradientC1Edddd',
        xStart, yStart, xFinalStop, yFinalStop,
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


#  Qt's 'QList<QLinearGradient>': the list of QLinearGradient, which
#  'QList[QLinearGradient]' gives. It is made here, so that there is one as
#  soon as there can be a QLinearGradient.
QList.createKind(
    QLinearGradient, 'value',
    make='ritual_list_make_QLinearGradient',
    add='ritual_list_add_QLinearGradient',
    size='ritual_list_size_QLinearGradient',
    at='ritual_list_at_QLinearGradient',
    drop='ritual_list_drop_QLinearGradient',
)
