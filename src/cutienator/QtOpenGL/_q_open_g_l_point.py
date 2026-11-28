"""
QOpenGLPoint binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtOpenGL/6.12.0/QtOpenGL/private/qopengl2pexvertexarray_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QOpenGLPoint to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QPointF
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPointF = WAIT['QPointF']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QOpenGLPoint(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QOpenGLPoint: a plain Python object standing in front
  of one C++ QOpenGLPoint.

  C++ hands a QOpenGLPoint around as a copy, so every C++ QOpenGLPoint behind
  a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  No function of Qt's QOpenGLPoint yet. It can be made from Python, in 3
  ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QPointF QOpenGLPoint::operator QPointF()': an operator Python has
    no name for.
  - Qt's 'QPointF QOpenGLPoint::operator QPointF() const': an operator Python
    has no name for.
  - Qt's 'QOpenGLPoint::~QOpenGLPoint()': the destructor: Python removes its
    C++ QOpenGLPoint by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QOpenGLPoint is created at the first use, not by
    'QOpenGLPoint(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QOpenGLPoint back gives a copy the ritual made for
    Python, in a new cute QOpenGLPoint.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QOpenGLPoint'

  #  Qt's '~QOpenGLPoint()'. Naming it makes this a value class: Python owns
  #  every C++ QOpenGLPoint behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN12QOpenGLPointD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

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

  @overload(float, float)
  def __init__(self, new_x: float, new_y: float) -> None:
    """
    Notes what was given, for Qt's 'QOpenGLPoint::QOpenGLPoint(GLfloat new_x,
    GLfloat new_y)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qopenglpoint.html#QOpenGLPoint

    Parameters
    ----------

    new_x : float
      Passed on as it is.

    new_y : float
      Passed on as it is.
    """
    #  QOpenGLPoint::QOpenGLPoint(GLfloat new_x, GLfloat new_y)
    self._noteCreation(QOpenGLPoint, lambda: Rituals.call(
        'ritual_ZN12QOpenGLPointC1Eff', new_x, new_y,
    ))

  @overload(QPointF)
  def __init__(self, p: QPointF) -> None:
    """
    Notes what was given, for Qt's 'QOpenGLPoint::QOpenGLPoint(const QPointF
    &p)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qopenglpoint.html#QOpenGLPoint

    Parameters
    ----------

    p : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  QOpenGLPoint::QOpenGLPoint(const QPointF &p)
    self._noteCreation(QOpenGLPoint, lambda: Rituals.call(
        'ritual_ZN12QOpenGLPointC1ERK7QPointF', self._valueOf(p, 'QPointF'),
    ))

  @overload(NoneType)
  def __init__(self, p: Optional[QPointF]) -> None:
    """
    Notes what was given, for Qt's 'QOpenGLPoint::QOpenGLPoint(const QPointF
    *p)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qopenglpoint.html#QOpenGLPoint

    Parameters
    ----------

    p : Optional[QPointF]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QOpenGLPoint::QOpenGLPoint(const QPointF *p)
    self._noteCreation(QOpenGLPoint, lambda: Rituals.call(
        'ritual_ZN12QOpenGLPointC1EPK7QPointF',
        self._addressOf(p, 'QPointF'),
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
