"""
QCanvasGradientBrushPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCanvasPainter/6.12.0/QtCanvasPainter/private/qcanvasgradient_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QCanvasGradientBrushPrivate to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, CuteFlags, MetaCute
from ..occult import Rituals
from . import QCanvasBrush, QCanvasBrushPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class QCanvasGradientBrushPrivate(QCanvasBrushPrivate):
  """
  The cute side of Qt's QCanvasGradientBrushPrivate: a plain Python object
  standing in front of one C++ QCanvasGradientBrushPrivate.

  It is built on the cute 'QCanvasBrushPrivate', as Qt's
  QCanvasGradientBrushPrivate is built on Qt's QCanvasBrushPrivate, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QCanvasGradientBrushPrivate that has a ritual and
  that Python can call so far, 1 name in all: 'generateGradientKey'. It can
  be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'bool QCanvasGradientBrushPrivate::equals(const QCanvasBrushPrivate
    &other) const': takes a type Python has no way to hand over yet.
  - Qt's 'const QCanvasGradientBrushPrivate
    *QCanvasGradientBrushPrivate::get(const QCanvasGradient &gradient)':
    takes a type Python has no way to hand over yet.
  - Qt's 'QCanvasGradientBrushPrivate
    *QCanvasGradientBrushPrivate::get(QCanvasGradient &gradient)': takes a
    type Python has no way to hand over yet.

  What has no ritual
  ------------------

  2 of the 7 functions Qt declares: 1 a template; 1 Qt's library has no name
  for it, and its code in Qt's source does not compile apart from its file.

  What to expect
  --------------

  - The C++ QCanvasGradientBrushPrivate is created at the first use, not by
    'QCanvasGradientBrushPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QCanvasGradientBrushPrivate.
  - Each name of Qt's QCanvasGradientBrushPrivate that has no cute function
    yet, 'updateGradientTexture', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QCanvasGradientBrushPrivate, each a class in
  #  here as in C++, and the names Qt has for the combinations of its flags
  #  enums.

  class DirtyFlag(CuteFlags, scoped=True):
    """
    The flags enum 'QCanvasGradientBrushPrivate::DirtyFlag' of Qt, with the 3
    names Qt gives in it. Qt names the type of its combinations
    'QCanvasGradientBrushPrivate::DirtyFlags'. C++ keeps these names inside
    the enum, so the class that holds the enum does not have them.
    """

    Stops = 0x1
    Values = 0x2
    All = 0xff

  DirtyFlags = DirtyFlag

  #  The classes Qt writes inside QCanvasGradientBrushPrivate, each a class
  #  in here as in C++.

  class QCanvasGradientData(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QCanvasGradientBrushPrivate::QCanvasGradientData: a
    plain Python object standing in front of one C++
    QCanvasGradientBrushPrivate::QCanvasGradientData.

    C++ hands a QCanvasGradientBrushPrivate::QCanvasGradientData around as a
    copy, so every C++ QCanvasGradientBrushPrivate::QCanvasGradientData
    behind a cute one is Python's own: it is removed, by the ritual named in
    '__delete_ritual__', when the cute object goes.

    What exists
    -----------

    No function of Qt's QCanvasGradientBrushPrivate::QCanvasGradientData yet.
    It can be made from Python, in 1 way; see '__init__'.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QCanvasGradientBrushPrivate::QCanvasGradientData::
      ~QCanvasGradientData()': the destructor: Python removes its C++
      QCanvasGradientBrushPrivate::QCanvasGradientData by it, and has no
      other use for it.

    What to expect
    --------------

    - The C++ QCanvasGradientBrushPrivate::QCanvasGradientData is created at
      the first use, not by
      'QCanvasGradientBrushPrivate::QCanvasGradientData(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QCanvasGradientBrushPrivate::QCanvasGradientData
      back gives a copy the ritual made for Python, in a new cute
      QCanvasGradientBrushPrivate::QCanvasGradientData.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QCanvasGradientBrushPrivate::QCanvasGradientData'

    #  Qt's '~QCanvasGradientBrushPrivate::QCanvasGradientData()'. Naming it
    #  makes this a value class: Python owns every C++
    #  QCanvasGradientBrushPrivate::QCanvasGradientData behind a cute one,
    #  and removes it by this ritual.
    __delete_ritual__ = (
        'ritual_ZN27QCanvasGradientBrushPrivate19QCanvasGradientDataD1Ev')

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

    @overload()
    def __init__(self) -> None:
      """
      Notes what was given, for Qt's
      'QCanvasGradientBrushPrivate::QCanvasGradientData::QCanvasGradientData(
      )', which is called at the first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qcanvasgradientbrushprivate-qcanvasgradientdata.html
      """
      #  QCanvasGradientBrushPrivate::QCanvasGradientData::
      #      QCanvasGradientData()
      self._noteCreation(
          QCanvasGradientBrushPrivate.QCanvasGradientData, lambda: Rituals.call(
              'ritual_ZN27QCanvasGradientBrushPrivate19QCanvasGradientDataC'
              '1Ev',
          ))

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

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QCanvasGradientBrushPrivate'

  #  A C++ QCanvasGradientBrushPrivate Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QCanvasGradientBrushPrivate'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def generateGradientKey(self) -> int:
    """
    Calls Qt's 'qint64 QCanvasGradientBrushPrivate::generateGradientKey()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanvasgradientbrushprivate.html
    """
    #  qint64 QCanvasGradientBrushPrivate::generateGradientKey() const
    return self.uglySide.call(
        'ritual_ZNK27QCanvasGradientBrushPrivate19generateGradientKeyEv',
    )

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

  @overload(QCanvasBrush.BrushType)
  def __init__(self, type: QCanvasBrush.BrushType) -> None:
    """
    Notes what was given, for Qt's
    'QCanvasGradientBrushPrivate::QCanvasGradientBrushPrivate(QCanvasBrush::
    BrushType type)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanvasgradientbrushprivate.html

    Parameters
    ----------

    type : QCanvasBrush.BrushType
      Passed on as its number.
    """
    #  QCanvasGradientBrushPrivate::QCanvasGradientBrushPrivate(
    #      QCanvasBrush::BrushType type)
    self._noteCreation(QCanvasGradientBrushPrivate, lambda: Rituals.call(
        'ritual_ZN27QCanvasGradientBrushPrivateC1EN12QCanvasBrush9BrushType'
        'E',
        type.value,
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

  @staticmethod
  def updateGradientTexture(*__, **_) -> Never:
    """
    Qt's 'void
    QCanvasGradientBrushPrivate::updateGradientTexture(QCanvasPainter
    *painter)': Qt's library has no name for it, and its code in Qt's source
    does not compile apart from its file: use of undeclared identifier
    'QCPAINTER_GRADIENT_SIZE'.
    """
    raise NotImplementedError(
        "'QCanvasGradientBrushPrivate.updateGradientTexture' has no cute "
        "function yet. Qt's 'void "
        "QCanvasGradientBrushPrivate::updateGradientTexture(QCanvasPainter "
        "*painter)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: use of undeclared "
        "identifier 'QCPAINTER_GRADIENT_SIZE'.")
