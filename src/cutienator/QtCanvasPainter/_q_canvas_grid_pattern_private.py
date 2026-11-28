"""
QCanvasGridPatternPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCanvasPainter/6.12.0/QtCanvasPainter/private/qcanvasgridpattern_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QCanvasGridPatternPrivate to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from . import QCanvasBrushPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QCPaint, QCanvasBrush, QCanvasGridPattern, QCanvasPainter
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QCanvasBrush = WAIT['QCanvasBrush']
  QCanvasGridPattern = WAIT['QCanvasGridPattern']
  QCanvasPainter = WAIT['QCanvasPainter']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QCanvasGridPatternPrivate(QCanvasBrushPrivate):
  """
  The cute side of Qt's QCanvasGridPatternPrivate: a plain Python object
  standing in front of one C++ QCanvasGridPatternPrivate.

  It is built on the cute 'QCanvasBrushPrivate', as Qt's
  QCanvasGridPatternPrivate is built on Qt's QCanvasBrushPrivate, and has
  everything that class has.

  C++ hands a QCanvasGridPatternPrivate around as a copy, so every C++
  QCanvasGridPatternPrivate behind a cute one is Python's own: it is removed,
  by the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QCanvasGridPatternPrivate that has a ritual and that
  Python can call so far, 6 names in all: 'clone', 'createPaint', 'get',
  'create', 'getFromCanvasBrush', 'createGridPattern'. It can be made from
  Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'bool QCanvasGridPatternPrivate::equals(const QCanvasBrushPrivate
    &other) const': takes a type Python has no way to hand over yet.
  - Qt's 'const QCanvasGridPatternPrivate
    *QCanvasGridPatternPrivate::get(const QCanvasGridPattern *brush)': takes
    in Python what 'QCanvasGridPatternPrivate
    *QCanvasGridPatternPrivate::get(QCanvasGridPattern *brush)' takes.
  - Qt's 'QCanvasGridPatternPrivate::~QCanvasGridPatternPrivate()': the
    destructor: Python removes its C++ QCanvasGridPatternPrivate by it, and
    has no other use for it.

  What to expect
  --------------

  - The C++ QCanvasGridPatternPrivate is created at the first use, not by
    'QCanvasGridPatternPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QCanvasGridPatternPrivate back gives a copy the
    ritual made for Python, in a new cute QCanvasGridPatternPrivate.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QCanvasGridPattern)
  @overload(NoneType)
  def get(
      brush: Optional[QCanvasGridPattern],
  ) -> Optional[QCanvasGridPatternPrivate]:
    """
    Calls Qt's 'QCanvasGridPatternPrivate
    *QCanvasGridPatternPrivate::get(QCanvasGridPattern *brush)'.

    Qt's own words: https://doc.qt.io/qt-6/qcanvasgridpatternprivate.html#get

    Parameters
    ----------

    brush : Optional[QCanvasGridPattern]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QCanvasGridPatternPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QCanvasGridPatternPrivate
    #      *QCanvasGridPatternPrivate::get(QCanvasGridPattern *brush)
    address = Rituals.call(
        'ritual_ZN25QCanvasGridPatternPrivate3getEP18QCanvasGridPattern',
        CuteMixin._addressOf(brush),
    )
    return QCanvasGridPatternPrivate._cuteAt(address)

  @staticmethod
  @overload(THIS)
  @overload(NoneType)
  def create(p: Optional[QCanvasGridPatternPrivate]) -> QCanvasGridPattern:
    """
    Calls Qt's 'QCanvasGridPattern
    QCanvasGridPatternPrivate::create(QCanvasGridPatternPrivate *p)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanvasgridpatternprivate.html#create

    Parameters
    ----------

    p : Optional[QCanvasGridPatternPrivate]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QCanvasGridPattern
      A new cute QCanvasGridPattern around the copy Qt gave back. Python owns
      it.
    """
    #  QCanvasGridPattern
    #      QCanvasGridPatternPrivate::create(QCanvasGridPatternPrivate *p)
    address = Rituals.call(
        'ritual_ZN25QCanvasGridPatternPrivate6createEPS_',
        CuteMixin._addressOf(p),
    )
    from . import QCanvasGridPattern
    return QCanvasGridPattern._cuteOwning(address)

  @staticmethod
  @overload(QCanvasBrush)
  def getFromCanvasBrush(brush: QCanvasBrush) -> QCanvasGridPattern:
    """
    Calls Qt's 'QCanvasGridPattern
    QCanvasGridPatternPrivate::getFromCanvasBrush(const QCanvasBrush
    &brush)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanvasgridpatternprivate.html#getFromCanvasBrush

    Parameters
    ----------

    brush : QCanvasBrush
      Passed on as a value: Qt reads the C++ QCanvasBrush, which stays
      Python's own.

    Returns
    -------

    QCanvasGridPattern
      A new cute QCanvasGridPattern around the copy Qt gave back. Python owns
      it.
    """
    #  QCanvasGridPattern QCanvasGridPatternPrivate::getFromCanvasBrush(const
    #      QCanvasBrush &brush)
    address = Rituals.call(
        'ritual_ZN25QCanvasGridPatternPrivate18getFromCanvasBrushERK12QCanv'
        'asBrush',
        CuteMixin._valueOf(brush),
    )
    from . import QCanvasGridPattern
    return QCanvasGridPattern._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QCanvasGridPatternPrivate'

  #  A C++ QCanvasGridPatternPrivate Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QCanvasGridPatternPrivate'

  #  Qt's '~QCanvasGridPatternPrivate()'. Naming it makes this a value class:
  #  Python owns every C++ QCanvasGridPatternPrivate behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN25QCanvasGridPatternPrivateD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QCanvasPainter)
  @overload(NoneType)
  def createPaint(self, painter: Optional[QCanvasPainter]) -> QCPaint:
    """
    Calls Qt's 'QCPaint QCanvasGridPatternPrivate::createPaint(QCanvasPainter
    *painter) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanvasgridpatternprivate.html#createPaint

    Parameters
    ----------

    painter : Optional[QCanvasPainter]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QCPaint
      A new cute QCPaint around the copy Qt gave back. Python owns it.
    """
    #  QCPaint QCanvasGridPatternPrivate::createPaint(QCanvasPainter
    #      *painter) const
    ritual = (
        'ritual_ZNK25QCanvasGridPatternPrivate11createPaintEP14QCanvasPaint'
        'er')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK25QCanvasGridPatternPrivate11createPaintEP14QCanva'
          'sPainter')
    address = self.uglySide.call(ritual, self._addressOf(painter))
    from . import QCPaint
    return QCPaint._cuteOwning(address)

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

  @overload(THIS)
  def __init__(self, a0: QCanvasGridPatternPrivate) -> None:
    """
    Notes what was given, for Qt's
    'QCanvasGridPatternPrivate::QCanvasGridPatternPrivate(const
    QCanvasGridPatternPrivate &a0)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanvasgridpatternprivate.html

    Parameters
    ----------

    a0 : QCanvasGridPatternPrivate
      Passed on as a value: Qt reads the C++ QCanvasGridPatternPrivate, which
      stays Python's own.
    """
    #  QCanvasGridPatternPrivate::QCanvasGridPatternPrivate(const
    #      QCanvasGridPatternPrivate &a0)
    self._noteCreation(QCanvasGridPatternPrivate, lambda: Rituals.call(
        'ritual_ZN25QCanvasGridPatternPrivateC1ERKS_', self._valueOf(a0),
    ))

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'QCanvasGridPatternPrivate::QCanvasGridPatternPrivate()', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanvasgridpatternprivate.html
    """
    #  QCanvasGridPatternPrivate::QCanvasGridPatternPrivate()
    self._noteCreation(QCanvasGridPatternPrivate, lambda: Rituals.call(
        'ritual_ZN25QCanvasGridPatternPrivateC1Ev',
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

  def clone(self) -> Optional[QCanvasBrushPrivate]:
    """
    Calls Qt's 'QCanvasBrushPrivate *QCanvasGridPatternPrivate::clone()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanvasgridpatternprivate.html#clone

    Returns
    -------

    Optional[QCanvasBrushPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QCanvasBrushPrivate *QCanvasGridPatternPrivate::clone()
    ritual = 'ritual_ZN25QCanvasGridPatternPrivate5cloneEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN25QCanvasGridPatternPrivate5cloneEv'
    address = self.uglySide.call(ritual)
    return QCanvasBrushPrivate._cuteAt(address)

  def createGridPattern(self) -> None:
    """
    Calls Qt's 'void QCanvasGridPatternPrivate::createGridPattern() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanvasgridpatternprivate.html#createGridPattern
    """
    #  void QCanvasGridPatternPrivate::createGridPattern() const
    self.uglySide.call(
        'ritual_ZNK25QCanvasGridPatternPrivate17createGridPatternEv',
    )
