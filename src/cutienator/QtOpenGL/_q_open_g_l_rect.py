"""
QOpenGLRect binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtOpenGL/6.12.0/QtOpenGL/private/qopengl2pexvertexarray_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QOpenGLRect to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from ..QtCore import QRectF
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QRectF = WAIT['QRectF']


class QOpenGLRect(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QOpenGLRect: a plain Python object standing in front
  of one C++ QOpenGLRect.

  C++ hands a QOpenGLRect around as a copy, so every C++ QOpenGLRect behind a
  cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  No function of Qt's QOpenGLRect yet. It can be made from Python, in 2 ways;
  see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QRectF QOpenGLRect::operator QRectF() const': an operator Python
    has no name for.
  - Qt's 'QOpenGLRect::~QOpenGLRect()': the destructor: Python removes its
    C++ QOpenGLRect by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QOpenGLRect is created at the first use, not by
    'QOpenGLRect(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QOpenGLRect back gives a copy the ritual made for
    Python, in a new cute QOpenGLRect.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QOpenGLRect'

  #  Qt's '~QOpenGLRect()'. Naming it makes this a value class: Python owns
  #  every C++ QOpenGLRect behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN11QOpenGLRectD1Ev'

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

  @overload(QRectF)
  def __init__(self, r: QRectF) -> None:
    """
    Notes what was given, for Qt's 'QOpenGLRect::QOpenGLRect(const QRectF
    &r)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qopenglrect.html#QOpenGLRect

    Parameters
    ----------

    r : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  QOpenGLRect::QOpenGLRect(const QRectF &r)
    self._noteCreation(QOpenGLRect, lambda: Rituals.call(
        'ritual_ZN11QOpenGLRectC1ERK6QRectF', self._valueOf(r),
    ))

  @overload(float, float, float, float)
  def __init__(self, l: float, t: float, r: float, b: float) -> None:
    """
    Notes what was given, for Qt's 'QOpenGLRect::QOpenGLRect(GLfloat l,
    GLfloat t, GLfloat r, GLfloat b)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qopenglrect.html#QOpenGLRect

    Parameters
    ----------

    l : float
      Passed on as it is.

    t : float
      Passed on as it is.

    r : float
      Passed on as it is.

    b : float
      Passed on as it is.
    """
    #  QOpenGLRect::QOpenGLRect(GLfloat l, GLfloat t, GLfloat r, GLfloat b)
    self._noteCreation(QOpenGLRect, lambda: Rituals.call(
        'ritual_ZN11QOpenGLRectC1Effff', l, t, r, b,
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
