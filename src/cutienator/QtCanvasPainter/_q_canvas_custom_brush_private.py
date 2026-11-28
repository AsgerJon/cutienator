"""
QCanvasCustomBrushPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCanvasPainter/6.12.0/QtCanvasPainter/private/qcanvascustombrush_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QCanvasCustomBrushPrivate to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from . import QCanvasBrushPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QCPaint, QCanvasBrush, QCanvasCustomBrush, QCanvasPainter
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QCanvasBrush = WAIT['QCanvasBrush']
  QCanvasCustomBrush = WAIT['QCanvasCustomBrush']
  QCanvasPainter = WAIT['QCanvasPainter']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QCanvasCustomBrushPrivate(QCanvasBrushPrivate):
  """
  The cute side of Qt's QCanvasCustomBrushPrivate: a plain Python object
  standing in front of one C++ QCanvasCustomBrushPrivate.

  It is built on the cute 'QCanvasBrushPrivate', as Qt's
  QCanvasCustomBrushPrivate is built on Qt's QCanvasBrushPrivate, and has
  everything that class has.

  C++ hands a QCanvasCustomBrushPrivate around as a copy, so every C++
  QCanvasCustomBrushPrivate behind a cute one is Python's own: it is removed,
  by the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QCanvasCustomBrushPrivate that has a ritual and that
  Python can call so far, 5 names in all: 'clone', 'createPaint', 'get',
  'create', 'getFromCanvasBrush'. It can be made from Python, in 2 ways; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'bool QCanvasCustomBrushPrivate::equals(const QCanvasBrushPrivate
    &other) const': takes a type Python has no way to hand over yet.
  - Qt's 'const QCanvasCustomBrushPrivate
    *QCanvasCustomBrushPrivate::get(const QCanvasCustomBrush *brush)': takes
    in Python what 'QCanvasCustomBrushPrivate
    *QCanvasCustomBrushPrivate::get(QCanvasCustomBrush *brush)' takes.
  - Qt's 'QCanvasCustomBrushPrivate
    *QCanvasCustomBrushPrivate::get(QCanvasCustomBrush &brush)': takes a type
    Python has no way to hand over yet.
  - Qt's 'const QCanvasCustomBrushPrivate
    *QCanvasCustomBrushPrivate::get(const QCanvasCustomBrush &brush)': takes
    in Python what 'QCanvasCustomBrushPrivate
    *QCanvasCustomBrushPrivate::get(QCanvasCustomBrush *brush)' takes.
  - Qt's 'QCanvasCustomBrushPrivate::~QCanvasCustomBrushPrivate()': the
    destructor: Python removes its C++ QCanvasCustomBrushPrivate by it, and
    has no other use for it.

  What to expect
  --------------

  - The C++ QCanvasCustomBrushPrivate is created at the first use, not by
    'QCanvasCustomBrushPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QCanvasCustomBrushPrivate back gives a copy the
    ritual made for Python, in a new cute QCanvasCustomBrushPrivate.
  """

  #  The classes Qt writes inside QCanvasCustomBrushPrivate, each a class in
  #  here as in C++.

  class CommonUniforms(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QCanvasCustomBrushPrivate::CommonUniforms: a plain
    Python object standing in front of one C++
    QCanvasCustomBrushPrivate::CommonUniforms.

    C++ hands a QCanvasCustomBrushPrivate::CommonUniforms around as a copy,
    so every C++ QCanvasCustomBrushPrivate::CommonUniforms behind a cute one
    is Python's own: it is removed, by the ritual named in
    '__delete_ritual__', when the cute object goes.

    What exists
    -----------

    No function of Qt's QCanvasCustomBrushPrivate::CommonUniforms yet. None
    can be made from Python: one comes out of a function of another class
    that gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QCanvasCustomBrushPrivate::CommonUniforms::~CommonUniforms()':
      the destructor: Python removes its C++
      QCanvasCustomBrushPrivate::CommonUniforms by it, and has no other use
      for it.

    What to expect
    --------------

    - The C++ QCanvasCustomBrushPrivate::CommonUniforms is created at the
      first use, not by 'QCanvasCustomBrushPrivate::CommonUniforms(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QCanvasCustomBrushPrivate::CommonUniforms back
      gives a copy the ritual made for Python, in a new cute
      QCanvasCustomBrushPrivate::CommonUniforms.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QCanvasCustomBrushPrivate::CommonUniforms'

    #  Qt's '~QCanvasCustomBrushPrivate::CommonUniforms()'. Naming it makes
    #  this a value class: Python owns every C++
    #  QCanvasCustomBrushPrivate::CommonUniforms behind a cute one, and
    #  removes it by this ritual.
    __delete_ritual__ = (
        'ritual_ZN25QCanvasCustomBrushPrivate14CommonUniformsD1Ev')

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QCanvasCustomBrush)
  @overload(NoneType)
  def get(
      brush: Optional[QCanvasCustomBrush],
  ) -> Optional[QCanvasCustomBrushPrivate]:
    """
    Calls Qt's 'QCanvasCustomBrushPrivate
    *QCanvasCustomBrushPrivate::get(QCanvasCustomBrush *brush)'.

    Qt's own words: https://doc.qt.io/qt-6/qcanvascustombrushprivate.html#get

    Parameters
    ----------

    brush : Optional[QCanvasCustomBrush]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QCanvasCustomBrushPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QCanvasCustomBrushPrivate
    #      *QCanvasCustomBrushPrivate::get(QCanvasCustomBrush *brush)
    address = Rituals.call(
        'ritual_ZN25QCanvasCustomBrushPrivate3getEP18QCanvasCustomBrush',
        CuteMixin._addressOf(brush),
    )
    return QCanvasCustomBrushPrivate._cuteAt(address)

  @staticmethod
  @overload(THIS)
  @overload(NoneType)
  def create(p: Optional[QCanvasCustomBrushPrivate]) -> QCanvasCustomBrush:
    """
    Calls Qt's 'QCanvasCustomBrush
    QCanvasCustomBrushPrivate::create(QCanvasCustomBrushPrivate *p)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanvascustombrushprivate.html#create

    Parameters
    ----------

    p : Optional[QCanvasCustomBrushPrivate]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QCanvasCustomBrush
      A new cute QCanvasCustomBrush around the copy Qt gave back. Python owns
      it.
    """
    #  QCanvasCustomBrush
    #      QCanvasCustomBrushPrivate::create(QCanvasCustomBrushPrivate *p)
    address = Rituals.call(
        'ritual_ZN25QCanvasCustomBrushPrivate6createEPS_',
        CuteMixin._addressOf(p),
    )
    from . import QCanvasCustomBrush
    return QCanvasCustomBrush._cuteOwning(address)

  @staticmethod
  @overload(QCanvasBrush)
  def getFromCanvasBrush(brush: QCanvasBrush) -> QCanvasCustomBrush:
    """
    Calls Qt's 'QCanvasCustomBrush
    QCanvasCustomBrushPrivate::getFromCanvasBrush(const QCanvasBrush
    &brush)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanvascustombrushprivate.html#getFromCanvasBrush

    Parameters
    ----------

    brush : QCanvasBrush
      Passed on as a value: Qt reads the C++ QCanvasBrush, which stays
      Python's own.

    Returns
    -------

    QCanvasCustomBrush
      A new cute QCanvasCustomBrush around the copy Qt gave back. Python owns
      it.
    """
    #  QCanvasCustomBrush QCanvasCustomBrushPrivate::getFromCanvasBrush(const
    #      QCanvasBrush &brush)
    address = Rituals.call(
        'ritual_ZN25QCanvasCustomBrushPrivate18getFromCanvasBrushERK12QCanv'
        'asBrush',
        CuteMixin._valueOf(brush),
    )
    from . import QCanvasCustomBrush
    return QCanvasCustomBrush._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QCanvasCustomBrushPrivate'

  #  A C++ QCanvasCustomBrushPrivate Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QCanvasCustomBrushPrivate'

  #  Qt's '~QCanvasCustomBrushPrivate()'. Naming it makes this a value class:
  #  Python owns every C++ QCanvasCustomBrushPrivate behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN25QCanvasCustomBrushPrivateD1Ev'

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
    Calls Qt's 'QCPaint QCanvasCustomBrushPrivate::createPaint(QCanvasPainter
    *painter) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanvascustombrushprivate.html#createPaint

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
    #  QCPaint QCanvasCustomBrushPrivate::createPaint(QCanvasPainter
    #      *painter) const
    ritual = (
        'ritual_ZNK25QCanvasCustomBrushPrivate11createPaintEP14QCanvasPaint'
        'er')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK25QCanvasCustomBrushPrivate11createPaintEP14QCanva'
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

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'QCanvasCustomBrushPrivate::QCanvasCustomBrushPrivate()', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanvascustombrushprivate.html
    """
    #  QCanvasCustomBrushPrivate::QCanvasCustomBrushPrivate()
    self._noteCreation(QCanvasCustomBrushPrivate, lambda: Rituals.call(
        'ritual_ZN25QCanvasCustomBrushPrivateC1Ev',
    ))

  @overload(THIS)
  def __init__(self, a0: QCanvasCustomBrushPrivate) -> None:
    """
    Notes what was given, for Qt's
    'QCanvasCustomBrushPrivate::QCanvasCustomBrushPrivate(const
    QCanvasCustomBrushPrivate &a0)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanvascustombrushprivate.html

    Parameters
    ----------

    a0 : QCanvasCustomBrushPrivate
      Passed on as a value: Qt reads the C++ QCanvasCustomBrushPrivate, which
      stays Python's own.
    """
    #  QCanvasCustomBrushPrivate::QCanvasCustomBrushPrivate(const
    #      QCanvasCustomBrushPrivate &a0)
    self._noteCreation(QCanvasCustomBrushPrivate, lambda: Rituals.call(
        'ritual_ZN25QCanvasCustomBrushPrivateC1ERKS_', self._valueOf(a0),
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
    Calls Qt's 'QCanvasBrushPrivate *QCanvasCustomBrushPrivate::clone()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanvascustombrushprivate.html#clone

    Returns
    -------

    Optional[QCanvasBrushPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QCanvasBrushPrivate *QCanvasCustomBrushPrivate::clone()
    ritual = 'ritual_ZN25QCanvasCustomBrushPrivate5cloneEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN25QCanvasCustomBrushPrivate5cloneEv'
    address = self.uglySide.call(ritual)
    return QCanvasBrushPrivate._cuteAt(address)
