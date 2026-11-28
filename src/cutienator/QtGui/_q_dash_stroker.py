"""
QDashStroker binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qstroker_p.h, Qt 6.12.0. Changes made here are
#  lost.
#
#  Qt means QDashStroker to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..QtCore import Qt
from . import QStrokerOps

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QStroker
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QStroker = WAIT['QStroker']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QDashStroker(QStrokerOps):
  """
  The cute side of Qt's QDashStroker: a plain Python object standing in front
  of one C++ QDashStroker.

  It is built on the cute 'QStrokerOps', as Qt's QDashStroker is built on
  Qt's QStrokerOps, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QDashStroker that has a ritual and that Python can
  call so far, 8 names in all: 'stroker', 'repetitionLimit', 'setDashOffset',
  'dashOffset', 'end', 'setStrokeWidth', 'setMiterLimit',
  'processCurrentSubpath'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QDashStroker::~QDashStroker()': the destructor: Python never
    removes a C++ QDashStroker.
  - Qt's 'QList<qfixed> QDashStroker::patternForStyle(Qt::PenStyle style)':
    gives a type Python has no way to take yet.
  - Qt's 'void QDashStroker::setDashPattern(const QList<qfixed>
    &dashPattern)': takes a type Python has no way to hand over yet.
  - Qt's 'QList<qfixed> QDashStroker::dashPattern() const': gives a type
    Python has no way to take yet.
  - Qt's 'void QDashStroker::begin(void *data)': names 'void', which has no
    cute class yet.

  What to expect
  --------------

  - The C++ QDashStroker is created at the first use, not by
    'QDashStroker(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QDashStroker.
  - Each name of Qt's QDashStroker that has no cute function yet,
    'dashPattern', 'patternForStyle', 'setDashPattern', holds a function that
    raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def repetitionLimit() -> int:
    """
    Calls Qt's 'int QDashStroker::repetitionLimit()'.

    Qt's own words: https://doc.qt.io/qt-6/qdashstroker.html#repetitionLimit
    """
    #  int QDashStroker::repetitionLimit()
    return Rituals.call('ritual_ZN12QDashStroker15repetitionLimitEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QDashStroker'

  #  A C++ QDashStroker Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QDashStroker'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def stroker(self) -> Optional[QStroker]:
    """
    Calls Qt's 'QStroker *QDashStroker::stroker() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdashstroker.html#stroker

    Returns
    -------

    Optional[QStroker]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QStroker *QDashStroker::stroker() const
    address = self.uglySide.call('ritual_ZNK12QDashStroker7strokerEv')
    from . import QStroker
    return QStroker._cuteAt(address)

  def dashOffset(self) -> float:
    """
    Calls Qt's 'qreal QDashStroker::dashOffset() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdashstroker.html#dashOffset
    """
    #  qreal QDashStroker::dashOffset() const
    return self.uglySide.call('ritual_ZNK12QDashStroker10dashOffsetEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float)
  def setDashOffset(self, offset: float) -> None:
    """
    Calls Qt's 'void QDashStroker::setDashOffset(qreal offset)'.

    Qt's own words: https://doc.qt.io/qt-6/qdashstroker.html#setDashOffset

    Parameters
    ----------

    offset : float
      Passed on as it is.
    """
    #  void QDashStroker::setDashOffset(qreal offset)
    self.uglySide.call('ritual_ZN12QDashStroker13setDashOffsetEd', offset)

  @overload(float)
  def setStrokeWidth(self, width: float) -> None:
    """
    Calls Qt's 'void QDashStroker::setStrokeWidth(qreal width)'.

    Qt's own words: https://doc.qt.io/qt-6/qdashstroker.html#setStrokeWidth

    Parameters
    ----------

    width : float
      Passed on as it is.
    """
    #  void QDashStroker::setStrokeWidth(qreal width)
    self.uglySide.call('ritual_ZN12QDashStroker14setStrokeWidthEd', width)

  @overload(float)
  def setMiterLimit(self, limit: float) -> None:
    """
    Calls Qt's 'void QDashStroker::setMiterLimit(qreal limit)'.

    Qt's own words: https://doc.qt.io/qt-6/qdashstroker.html#setMiterLimit

    Parameters
    ----------

    limit : float
      Passed on as it is.
    """
    #  void QDashStroker::setMiterLimit(qreal limit)
    self.uglySide.call('ritual_ZN12QDashStroker13setMiterLimitEd', limit)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QStroker)
  @overload(NoneType)
  def __init__(self, stroker: Optional[QStroker]) -> None:
    """
    Notes what was given, for Qt's 'QDashStroker::QDashStroker(QStroker
    *stroker)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qdashstroker.html#QDashStroker

    Parameters
    ----------

    stroker : Optional[QStroker]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QDashStroker::QDashStroker(QStroker *stroker)
    self._noteCreation(QDashStroker, lambda: Rituals.call(
        'ritual_ZN12QDashStrokerC1EP8QStroker', self._addressOf(stroker),
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

  def end(self) -> None:
    """
    Calls Qt's 'void QDashStroker::end()'.

    Qt's own words: https://doc.qt.io/qt-6/qdashstroker.html#end
    """
    #  void QDashStroker::end()
    ritual = 'ritual_ZN12QDashStroker3endEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN12QDashStroker3endEv'
    self.uglySide.call(ritual)

  def processCurrentSubpath(self) -> None:
    """
    Calls Qt's 'void QDashStroker::processCurrentSubpath()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdashstroker.html#processCurrentSubpath
    """
    #  void QDashStroker::processCurrentSubpath()
    ritual = 'ritual_ZN12QDashStroker21processCurrentSubpathEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN12QDashStroker21processCurrentSubpathEv'
    self.uglySide.call(ritual)

  @staticmethod
  def dashPattern(*__, **_) -> Never:
    """
    Qt's 'QList<qfixed> QDashStroker::dashPattern() const': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QDashStroker.dashPattern' has no cute function yet. Qt's "
        "'QList<qfixed> QDashStroker::dashPattern() const': gives a type "
        "Python has no way to take yet.")

  @staticmethod
  def patternForStyle(*__, **_) -> Never:
    """
    Qt's 'QList<qfixed> QDashStroker::patternForStyle(Qt::PenStyle style)':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QDashStroker.patternForStyle' has no cute function yet. Qt's "
        "'QList<qfixed> QDashStroker::patternForStyle(Qt::PenStyle style)': "
        "gives a type Python has no way to take yet.")

  @staticmethod
  def setDashPattern(*__, **_) -> Never:
    """
    Qt's 'void QDashStroker::setDashPattern(const QList<qfixed>
    &dashPattern)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QDashStroker.setDashPattern' has no cute function yet. Qt's 'void "
        "QDashStroker::setDashPattern(const QList<qfixed> &dashPattern)': "
        "takes a type Python has no way to hand over yet.")
