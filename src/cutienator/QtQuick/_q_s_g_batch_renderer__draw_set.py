"""
QSGBatchRenderer::DrawSet binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qsgbatchrenderer_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QSGBatchRenderer::DrawSet to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals


class DrawSet(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QSGBatchRenderer::DrawSet: a plain Python object
  standing in front of one C++ QSGBatchRenderer::DrawSet.

  C++ hands a QSGBatchRenderer::DrawSet around as a copy, so every C++
  QSGBatchRenderer::DrawSet behind a cute one is Python's own: it is removed,
  by the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  No function of Qt's QSGBatchRenderer::DrawSet yet. It can be made from
  Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSGBatchRenderer::DrawSet::~DrawSet()': the destructor: Python
    removes its C++ QSGBatchRenderer::DrawSet by it, and has no other use for
    it.

  What to expect
  --------------

  - The C++ QSGBatchRenderer::DrawSet is created at the first use, not by
    'QSGBatchRenderer::DrawSet(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QSGBatchRenderer::DrawSet back gives a copy the
    ritual made for Python, in a new cute QSGBatchRenderer::DrawSet.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSGBatchRenderer::DrawSet'

  #  Qt's '~QSGBatchRenderer::DrawSet()'. Naming it makes this a value class:
  #  Python owns every C++ QSGBatchRenderer::DrawSet behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN16QSGBatchRenderer7DrawSetD1Ev'

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

  @overload(int, int, int)
  def __init__(self, v: int, z: int, i: int) -> None:
    """
    Notes what was given, for Qt's 'QSGBatchRenderer::DrawSet::DrawSet(int v,
    int z, int i)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgbatchrenderer-drawset.html#DrawSet

    Parameters
    ----------

    v : int
      Passed on as it is.

    z : int
      Passed on as it is.

    i : int
      Passed on as it is.
    """
    #  QSGBatchRenderer::DrawSet::DrawSet(int v, int z, int i)
    self._noteCreation(DrawSet, lambda: Rituals.call(
        'ritual_ZN16QSGBatchRenderer7DrawSetC1Eiii', v, z, i,
    ))

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'QSGBatchRenderer::DrawSet::DrawSet()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgbatchrenderer-drawset.html#DrawSet
    """
    #  QSGBatchRenderer::DrawSet::DrawSet()
    self._noteCreation(DrawSet, lambda: Rituals.call(
        'ritual_ZN16QSGBatchRenderer7DrawSetC1Ev',
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
