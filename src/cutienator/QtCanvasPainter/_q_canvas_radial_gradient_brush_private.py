"""
QCanvasRadialGradientBrushPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCanvasPainter/6.12.0/QtCanvasPainter/private/qcanvasgradient_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QCanvasRadialGradientBrushPrivate to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from . import QCanvasBrushPrivate, QCanvasGradientBrushPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtGui import QColor
  from . import QCPaint, QCanvasPainter
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QCanvasPainter = WAIT['QCanvasPainter']
  QColor = WAIT['QColor']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QCanvasRadialGradientBrushPrivate(QCanvasGradientBrushPrivate):
  """
  The cute side of Qt's QCanvasRadialGradientBrushPrivate: a plain Python
  object standing in front of one C++ QCanvasRadialGradientBrushPrivate.

  It is built on the cute 'QCanvasGradientBrushPrivate', as Qt's
  QCanvasRadialGradientBrushPrivate is built on Qt's
  QCanvasGradientBrushPrivate, and has everything that class has.

  C++ hands a QCanvasRadialGradientBrushPrivate around as a copy, so every
  C++ QCanvasRadialGradientBrushPrivate behind a cute one is Python's own: it
  is removed, by the ritual named in '__delete_ritual__', when the cute
  object goes.

  What exists
  -----------

  Every function of Qt's QCanvasRadialGradientBrushPrivate that has a ritual
  and that Python can call so far, 3 names in all: 'createPaint',
  'createRadialGradient', 'clone'. None can be made from Python: one comes
  out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's
    'QCanvasRadialGradientBrushPrivate::~QCanvasRadialGradientBrushPrivate(
    )': the destructor: Python removes its C++
    QCanvasRadialGradientBrushPrivate by it, and has no other use for it.

  What has no ritual
  ------------------

  2 of the 6 functions Qt declares: 2 leans on 'QCanvasGradientBrushPrivate.

  What to expect
  --------------

  - The C++ QCanvasRadialGradientBrushPrivate is created at the first use,
    not by 'QCanvasRadialGradientBrushPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QCanvasRadialGradientBrushPrivate back gives a copy
    the ritual made for Python, in a new cute
    QCanvasRadialGradientBrushPrivate.
  - Each name of Qt's QCanvasRadialGradientBrushPrivate that has no cute
    function yet, '__init__', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QCanvasRadialGradientBrushPrivate'

  #  A C++ QCanvasRadialGradientBrushPrivate Python makes is of a C++ class
  #  of ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QCanvasRadialGradientBrushPrivate'

  #  Qt's '~QCanvasRadialGradientBrushPrivate()'. Naming it makes this a
  #  value class: Python owns every C++ QCanvasRadialGradientBrushPrivate
  #  behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN33QCanvasRadialGradientBrushPrivateD1Ev'

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
    QCanvasRadialGradientBrushPrivate::createPaint(QCanvasPainter *painter)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanvasradialgradientbrushprivate.html#createPaint

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
    #  QCPaint QCanvasRadialGradientBrushPrivate::createPaint(QCanvasPainter
    #      *painter) const
    address = self.uglySide.call(
        'ritual_ZNK33QCanvasRadialGradientBrushPrivate11createPaintEP14QCan'
        'vasPainter',
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
    - Qt's
      'QCanvasRadialGradientBrushPrivate::QCanvasRadialGradientBrushPrivate(
      )': leans on
      'QCanvasGradientBrushPrivate::updateGradientTexture(QCanvasPainter*)',
      which Qt's source does not mark for use from outside Qt and has no code
      for that could be taken.
    - Qt's
      'QCanvasRadialGradientBrushPrivate::QCanvasRadialGradientBrushPrivate(
      const QCanvasRadialGradientBrushPrivate &a0)': leans on
      'QCanvasGradientBrushPrivate::updateGradientTexture(QCanvasPainter*)',
      which Qt's source does not mark for use from outside Qt and has no code
      for that could be taken.
    """
    raise NotImplementedError(
        "'QCanvasRadialGradientBrushPrivate.__init__' has no cute function "
        "yet. Qt's "
        "'QCanvasRadialGradientBrushPrivate::QCanvasRadialGradientBrushPriva"
        "te()': leans on "
        "'QCanvasGradientBrushPrivate::updateGradientTexture(QCanvasPainter*"
        ")', which Qt's source does not mark for use from outside Qt and "
        "has no code for that could be taken. Qt's "
        "'QCanvasRadialGradientBrushPrivate::QCanvasRadialGradientBrushPriva"
        "te(const QCanvasRadialGradientBrushPrivate &a0)': leans on "
        "'QCanvasGradientBrushPrivate::updateGradientTexture(QCanvasPainter*"
        ")', which Qt's source does not mark for use from outside Qt and "
        "has no code for that could be taken.")

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

  @overload(QColor, QColor, int)
  def createRadialGradient(
      self,
      iColor: QColor,
      oColor: QColor,
      imageId: int,
  ) -> None:
    """
    Calls Qt's 'void
    QCanvasRadialGradientBrushPrivate::createRadialGradient(QColor iColor,
    QColor oColor, int imageId) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanvasradialgradientbrushprivate.html

    Parameters
    ----------

    iColor : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.

    oColor : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.

    imageId : int
      Passed on as it is.
    """
    #  void QCanvasRadialGradientBrushPrivate::createRadialGradient(QColor
    #      iColor, QColor oColor, int imageId) const
    self.uglySide.call(
        'ritual_ZNK33QCanvasRadialGradientBrushPrivate20createRadialGradien'
        'tE6QColorS0_i',
        self._valueOf(iColor), self._valueOf(oColor), imageId,
    )

  def clone(self) -> Optional[QCanvasBrushPrivate]:
    """
    Calls Qt's 'QCanvasBrushPrivate
    *QCanvasRadialGradientBrushPrivate::clone()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanvasradialgradientbrushprivate.html#clone

    Returns
    -------

    Optional[QCanvasBrushPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QCanvasBrushPrivate *QCanvasRadialGradientBrushPrivate::clone()
    address = self.uglySide.call(
        'ritual_ZN33QCanvasRadialGradientBrushPrivate5cloneEv',
    )
    return QCanvasBrushPrivate._cuteAt(address)
