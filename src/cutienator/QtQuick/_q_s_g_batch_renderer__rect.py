"""
QSGBatchRenderer::Rect binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qsgbatchrenderer_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QSGBatchRenderer::Rect to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from ..QtGui import QMatrix4x4
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QMatrix4x4 = WAIT['QMatrix4x4']


class Rect(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QSGBatchRenderer::Rect: a plain Python object
  standing in front of one C++ QSGBatchRenderer::Rect.

  C++ hands a QSGBatchRenderer::Rect around as a copy, so every C++
  QSGBatchRenderer::Rect behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QSGBatchRenderer::Rect that has a ritual and that
  Python can call so far, 4 names in all: 'map', 'set', 'intersects',
  'isOutsideFloatRange'. None can be made from Python: one comes out of a
  function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void QSGBatchRenderer::Rect::operator|=(const Pt &pt)': an operator
    Python has no name for.
  - Qt's 'void QSGBatchRenderer::Rect::operator|=(const Rect &r)': an
    operator Python has no name for.
  - Qt's 'QSGBatchRenderer::Rect::~Rect()': the destructor: Python removes
    its C++ QSGBatchRenderer::Rect by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QSGBatchRenderer::Rect is created at the first use, not by
    'QSGBatchRenderer::Rect(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QSGBatchRenderer::Rect back gives a copy the ritual
    made for Python, in a new cute QSGBatchRenderer::Rect.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSGBatchRenderer::Rect'

  #  Qt's '~QSGBatchRenderer::Rect()'. Naming it makes this a value class:
  #  Python owns every C++ QSGBatchRenderer::Rect behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN16QSGBatchRenderer4RectD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isOutsideFloatRange(self) -> bool:
    """
    Calls Qt's 'bool QSGBatchRenderer::Rect::isOutsideFloatRange() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgbatchrenderer-rect.html#isOutsideFloatRange
    """
    #  bool QSGBatchRenderer::Rect::isOutsideFloatRange() const
    return self.uglySide.call(
        'ritual_ZNK16QSGBatchRenderer4Rect19isOutsideFloatRangeEv',
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

  @overload(QMatrix4x4)
  def map(self, m: QMatrix4x4) -> None:
    """
    Calls Qt's 'void QSGBatchRenderer::Rect::map(const QMatrix4x4 &m)'.

    Qt's own words: https://doc.qt.io/qt-6/qsgbatchrenderer-rect.html#map

    Parameters
    ----------

    m : QMatrix4x4
      Passed on as a value: Qt reads the C++ QMatrix4x4, which stays Python's
      own.
    """
    #  void QSGBatchRenderer::Rect::map(const QMatrix4x4 &m)
    self.uglySide.call(
        'ritual_ZN16QSGBatchRenderer4Rect3mapERK10QMatrix4x4',
        self._valueOf(m),
    )

  @overload(float, float, float, float)
  def set(
      self,
      left: float,
      top: float,
      right: float,
      bottom: float,
  ) -> None:
    """
    Calls Qt's 'void QSGBatchRenderer::Rect::set(float left, float top, float
    right, float bottom)'.

    Qt's own words: https://doc.qt.io/qt-6/qsgbatchrenderer-rect.html#set

    Parameters
    ----------

    left : float
      Passed on as it is.

    top : float
      Passed on as it is.

    right : float
      Passed on as it is.

    bottom : float
      Passed on as it is.
    """
    #  void QSGBatchRenderer::Rect::set(float left, float top, float right,
    #      float bottom)
    self.uglySide.call(
        'ritual_ZN16QSGBatchRenderer4Rect3setEffff',
        left, top, right, bottom,
    )

  @overload(THIS)
  def intersects(self, r: Rect) -> bool:
    """
    Calls Qt's 'bool QSGBatchRenderer::Rect::intersects(const Rect &r)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgbatchrenderer-rect.html#intersects

    Parameters
    ----------

    r : Rect
      Passed on as a value: Qt reads the C++ QSGBatchRenderer::Rect, which
      stays Python's own.
    """
    #  bool QSGBatchRenderer::Rect::intersects(const Rect &r)
    return self.uglySide.call(
        'ritual_ZN16QSGBatchRenderer4Rect10intersectsERKS0_',
        self._valueOf(r),
    )
