"""
QCanvasImagePatternPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCanvasPainter/6.12.0/QtCanvasPainter/private/qcanvasimagepattern_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QCanvasImagePatternPrivate to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from . import QCanvasBrushPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QCPaint, QCanvasBrush, QCanvasImagePattern, QCanvasPainter
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QCanvasBrush = WAIT['QCanvasBrush']
  QCanvasImagePattern = WAIT['QCanvasImagePattern']
  QCanvasPainter = WAIT['QCanvasPainter']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QCanvasImagePatternPrivate(QCanvasBrushPrivate):
  """
  The cute side of Qt's QCanvasImagePatternPrivate: a plain Python object
  standing in front of one C++ QCanvasImagePatternPrivate.

  It is built on the cute 'QCanvasBrushPrivate', as Qt's
  QCanvasImagePatternPrivate is built on Qt's QCanvasBrushPrivate, and has
  everything that class has.

  C++ hands a QCanvasImagePatternPrivate around as a copy, so every C++
  QCanvasImagePatternPrivate behind a cute one is Python's own: it is
  removed, by the ritual named in '__delete_ritual__', when the cute object
  goes.

  What exists
  -----------

  Every function of Qt's QCanvasImagePatternPrivate that has a ritual and
  that Python can call so far, 6 names in all: 'nextSerialNumber', 'clone',
  'createPaint', 'get', 'create', 'getFromCanvasBrush'. None can be made from
  Python: one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'bool QCanvasImagePatternPrivate::equals(const QCanvasBrushPrivate
    &other) const': takes a type Python has no way to hand over yet.
  - Qt's 'const QCanvasImagePatternPrivate
    *QCanvasImagePatternPrivate::get(const QCanvasImagePattern *brush)':
    takes in Python what 'QCanvasImagePatternPrivate
    *QCanvasImagePatternPrivate::get(QCanvasImagePattern *brush)' takes.
  - Qt's 'QCanvasImagePatternPrivate::~QCanvasImagePatternPrivate()': the
    destructor: Python removes its C++ QCanvasImagePatternPrivate by it, and
    has no other use for it.

  What has no ritual
  ------------------

  2 of the 11 functions Qt declares: 2 leans on 'QCanvasImagePatternPrivate.

  What to expect
  --------------

  - The C++ QCanvasImagePatternPrivate is created at the first use, not by
    'QCanvasImagePatternPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QCanvasImagePatternPrivate back gives a copy the
    ritual made for Python, in a new cute QCanvasImagePatternPrivate.
  - Each name of Qt's QCanvasImagePatternPrivate that has no cute function
    yet, '__init__', holds a function that raises 'NotImplementedError', and
    its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def nextSerialNumber() -> int:
    """
    Calls Qt's 'uint QCanvasImagePatternPrivate::nextSerialNumber()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanvasimagepatternprivate.html#nextSerialNumber
    """
    #  uint QCanvasImagePatternPrivate::nextSerialNumber()
    return Rituals.call(
        'ritual_ZN26QCanvasImagePatternPrivate16nextSerialNumberEv',
    )

  @staticmethod
  @overload(QCanvasImagePattern)
  @overload(NoneType)
  def get(
      brush: Optional[QCanvasImagePattern],
  ) -> Optional[QCanvasImagePatternPrivate]:
    """
    Calls Qt's 'QCanvasImagePatternPrivate
    *QCanvasImagePatternPrivate::get(QCanvasImagePattern *brush)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanvasimagepatternprivate.html#get

    Parameters
    ----------

    brush : Optional[QCanvasImagePattern]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QCanvasImagePatternPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QCanvasImagePatternPrivate
    #      *QCanvasImagePatternPrivate::get(QCanvasImagePattern *brush)
    address = Rituals.call(
        'ritual_ZN26QCanvasImagePatternPrivate3getEP19QCanvasImagePattern',
        CuteMixin._addressOf(brush),
    )
    return QCanvasImagePatternPrivate._cuteAt(address)

  @staticmethod
  @overload(THIS)
  @overload(NoneType)
  def create(p: Optional[QCanvasImagePatternPrivate]) -> QCanvasImagePattern:
    """
    Calls Qt's 'QCanvasImagePattern
    QCanvasImagePatternPrivate::create(QCanvasImagePatternPrivate *p)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanvasimagepatternprivate.html#create

    Parameters
    ----------

    p : Optional[QCanvasImagePatternPrivate]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QCanvasImagePattern
      A new cute QCanvasImagePattern around the copy Qt gave back. Python
      owns it.
    """
    #  QCanvasImagePattern
    #      QCanvasImagePatternPrivate::create(QCanvasImagePatternPrivate *p)
    address = Rituals.call(
        'ritual_ZN26QCanvasImagePatternPrivate6createEPS_',
        CuteMixin._addressOf(p),
    )
    from . import QCanvasImagePattern
    return QCanvasImagePattern._cuteOwning(address)

  @staticmethod
  @overload(QCanvasBrush)
  def getFromCanvasBrush(brush: QCanvasBrush) -> QCanvasImagePattern:
    """
    Calls Qt's 'QCanvasImagePattern
    QCanvasImagePatternPrivate::getFromCanvasBrush(const QCanvasBrush
    &brush)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanvasimagepatternprivate.html#getFromCanvasBrush

    Parameters
    ----------

    brush : QCanvasBrush
      Passed on as a value: Qt reads the C++ QCanvasBrush, which stays
      Python's own.

    Returns
    -------

    QCanvasImagePattern
      A new cute QCanvasImagePattern around the copy Qt gave back. Python
      owns it.
    """
    #  QCanvasImagePattern
    #      QCanvasImagePatternPrivate::getFromCanvasBrush(const QCanvasBrush
    #      &brush)
    address = Rituals.call(
        'ritual_ZN26QCanvasImagePatternPrivate18getFromCanvasBrushERK12QCan'
        'vasBrush',
        CuteMixin._valueOf(brush),
    )
    from . import QCanvasImagePattern
    return QCanvasImagePattern._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QCanvasImagePatternPrivate'

  #  A C++ QCanvasImagePatternPrivate Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QCanvasImagePatternPrivate'

  #  Qt's '~QCanvasImagePatternPrivate()'. Naming it makes this a value
  #  class: Python owns every C++ QCanvasImagePatternPrivate behind a cute
  #  one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN26QCanvasImagePatternPrivateD1Ev'

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
    Calls Qt's 'QCPaint
    QCanvasImagePatternPrivate::createPaint(QCanvasPainter *painter) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanvasimagepatternprivate.html#createPaint

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
    #  QCPaint QCanvasImagePatternPrivate::createPaint(QCanvasPainter
    #      *painter) const
    address = self.uglySide.call(
        'ritual_ZNK26QCanvasImagePatternPrivate11createPaintEP14QCanvasPain'
        'ter',
        self._addressOf(painter),
    )
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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    - Qt's 'QCanvasImagePatternPrivate::QCanvasImagePatternPrivate(const
      QCanvasImagePatternPrivate &a0)': leans on
      'QCanvasImagePatternPrivate::createPaint(QCanvasPainter*) const', which
      Qt's source does not mark for use from outside Qt and has no code for
      that could be taken.
    - Qt's 'QCanvasImagePatternPrivate::QCanvasImagePatternPrivate()': leans
      on 'QCanvasImagePatternPrivate::createPaint(QCanvasPainter*) const',
      which Qt's source does not mark for use from outside Qt and has no code
      for that could be taken.
    """
    raise NotImplementedError(
        "'QCanvasImagePatternPrivate.__init__' has no cute function yet. "
        "Qt's 'QCanvasImagePatternPrivate::QCanvasImagePatternPrivate(const "
        "QCanvasImagePatternPrivate &a0)': leans on "
        "'QCanvasImagePatternPrivate::createPaint(QCanvasPainter*) const', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken. Qt's "
        "'QCanvasImagePatternPrivate::QCanvasImagePatternPrivate()': leans "
        "on 'QCanvasImagePatternPrivate::createPaint(QCanvasPainter*) "
        "const', which Qt's source does not mark for use from outside Qt "
        "and has no code for that could be taken.")

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
    Calls Qt's 'QCanvasBrushPrivate *QCanvasImagePatternPrivate::clone()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanvasimagepatternprivate.html#clone

    Returns
    -------

    Optional[QCanvasBrushPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QCanvasBrushPrivate *QCanvasImagePatternPrivate::clone()
    address = self.uglySide.call(
        'ritual_ZN26QCanvasImagePatternPrivate5cloneEv',
    )
    return QCanvasBrushPrivate._cuteAt(address)
