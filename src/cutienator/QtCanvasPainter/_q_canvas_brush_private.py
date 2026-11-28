"""
QCanvasBrushPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCanvasPainter/6.12.0/QtCanvasPainter/private/qcanvasbrush_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QCanvasBrushPrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QSharedData

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QCPaint, QCanvasBrush, QCanvasPainter
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QCanvasBrush = WAIT['QCanvasBrush']
  QCanvasPainter = WAIT['QCanvasPainter']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QCanvasBrushPrivate(QSharedData):
  """
  The cute side of Qt's QCanvasBrushPrivate: a plain Python object standing
  in front of one C++ QCanvasBrushPrivate.

  It is built on the cute 'QSharedData', as Qt's QCanvasBrushPrivate is built
  on Qt's QSharedData, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QCanvasBrushPrivate that has a ritual and that
  Python can call so far, 4 names in all: 'clone', 'createPaint', 'get',
  'create'. None can be made from Python: one comes out of a function of
  another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QCanvasBrushPrivate::~QCanvasBrushPrivate()': the destructor:
    Python never removes a C++ QCanvasBrushPrivate.
  - Qt's 'bool QCanvasBrushPrivate::equals(const QCanvasBrushPrivate &other)
    const': takes a type Python has no way to hand over yet.
  - Qt's 'QCanvasBrushPrivate *QCanvasBrushPrivate::get(QCanvasBrush
    &brush)': takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  1 of the 8 functions Qt declares: 1 the class is abstract, so C++ cannot
  make one, and the C++ class of ours does not fill in every function it
  leaves open.

  What to expect
  --------------

  - The C++ QCanvasBrushPrivate is created at the first use, not by
    'QCanvasBrushPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QCanvasBrushPrivate.
  - Each name of Qt's QCanvasBrushPrivate that has no cute function yet,
    '__init__', 'equals', holds a function that raises 'NotImplementedError',
    and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QCanvasBrush)
  def get(brush: QCanvasBrush) -> Optional[QCanvasBrushPrivate]:
    """
    Calls Qt's 'QCanvasBrushPrivate *QCanvasBrushPrivate::get(const
    QCanvasBrush &brush)'.

    Qt's own words: https://doc.qt.io/qt-6/qcanvasbrushprivate.html#get

    Parameters
    ----------

    brush : QCanvasBrush
      Passed on as a value: Qt reads the C++ QCanvasBrush, which stays
      Python's own.

    Returns
    -------

    Optional[QCanvasBrushPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QCanvasBrushPrivate *QCanvasBrushPrivate::get(const QCanvasBrush
    #      &brush)
    address = Rituals.call(
        'ritual_ZN19QCanvasBrushPrivate3getERK12QCanvasBrush',
        CuteMixin._valueOf(brush),
    )
    return QCanvasBrushPrivate._cuteAt(address)

  @staticmethod
  @overload(THIS)
  @overload(NoneType)
  def create(p: Optional[QCanvasBrushPrivate]) -> QCanvasBrush:
    """
    Calls Qt's 'QCanvasBrush QCanvasBrushPrivate::create(QCanvasBrushPrivate
    *p)'.

    Qt's own words: https://doc.qt.io/qt-6/qcanvasbrushprivate.html#create

    Parameters
    ----------

    p : Optional[QCanvasBrushPrivate]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QCanvasBrush
      A new cute QCanvasBrush around the copy Qt gave back. Python owns it.
    """
    #  QCanvasBrush QCanvasBrushPrivate::create(QCanvasBrushPrivate *p)
    address = Rituals.call(
        'ritual_ZN19QCanvasBrushPrivate6createEPS_', CuteMixin._addressOf(p),
    )
    from . import QCanvasBrush
    return QCanvasBrush._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QCanvasBrushPrivate'

  #  A C++ QCanvasBrushPrivate Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QCanvasBrushPrivate'

  #  The functions Qt calls itself that QCanvasBrushPrivate is the first to
  #  declare and that cannot be handed to Python yet, each as Qt declares it.
  #  A class of a program that writes one of them anew is refused, since Qt
  #  would never call what it wrote; see 'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'equals': (
          'bool QCanvasBrushPrivate::equals(const QCanvasBrushPrivate &) '
          'const noexcept',
      ),
  }

  #  The functions Qt calls itself that QCanvasBrushPrivate is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'clone': (
          ('_ZN19QCanvasBrushPrivate5cloneEv',
           ('address', 'address', 'QtCanvasPainter:QCanvasBrushPrivate'),
           ()),
      ),
      'createPaint': (
          ('_ZNK19QCanvasBrushPrivate11createPaintEP14QCanvasPainter',
           ('address', 'value', 'QtCanvasPainter:QCPaint'),
           (
               ('address', 'address', 'QtCanvasPainter:QCanvasPainter'),
           )),
      ),
  }

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
    Calls Qt's 'QCPaint QCanvasBrushPrivate::createPaint(QCanvasPainter
    *painter) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanvasbrushprivate.html#createPaint

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
    #  QCPaint QCanvasBrushPrivate::createPaint(QCanvasPainter *painter)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK19QCanvasBrushPrivate11createPaintEP14QCanvasPainter',
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
    Qt's 'QCanvasBrushPrivate::QCanvasBrushPrivate(QCanvasBrush::BrushType
    t)': the class is abstract, so C++ cannot make one, and the C++ class of
    ours does not fill in every function it leaves open.
    """
    raise NotImplementedError(
        "'QCanvasBrushPrivate.__init__' has no cute function yet. Qt's "
        "'QCanvasBrushPrivate::QCanvasBrushPrivate(QCanvasBrush::BrushType "
        "t)': the class is abstract, so C++ cannot make one, and the C++ "
        "class of ours does not fill in every function it leaves open.")

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
    Calls Qt's 'QCanvasBrushPrivate *QCanvasBrushPrivate::clone()'.

    Qt's own words: https://doc.qt.io/qt-6/qcanvasbrushprivate.html#clone

    Returns
    -------

    Optional[QCanvasBrushPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QCanvasBrushPrivate *QCanvasBrushPrivate::clone()
    address = self.uglySide.call('ritual_ZN19QCanvasBrushPrivate5cloneEv')
    return QCanvasBrushPrivate._cuteAt(address)

  @staticmethod
  def equals(*__, **_) -> Never:
    """
    Qt's 'bool QCanvasBrushPrivate::equals(const QCanvasBrushPrivate &other)
    const': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QCanvasBrushPrivate.equals' has no cute function yet. Qt's 'bool "
        "QCanvasBrushPrivate::equals(const QCanvasBrushPrivate &other) "
        "const': takes a type Python has no way to hand over yet.")
