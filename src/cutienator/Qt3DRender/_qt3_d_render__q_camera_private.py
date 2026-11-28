"""
Qt3DRender::QCameraPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DRender/6.12.0/Qt3DRender/private/qcamera_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means Qt3DRender::QCameraPrivate to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..Qt3DCore import Qt3DCore
from . import Qt3DRender

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional


class QCameraPrivate(Qt3DCore.QEntityPrivate):
  """
  The cute side of Qt's Qt3DRender::QCameraPrivate: a plain Python object
  standing in front of one C++ Qt3DRender::QCameraPrivate.

  It is built on the cute 'Qt3DCore::QEntityPrivate', as Qt's
  Qt3DRender::QCameraPrivate is built on Qt's Qt3DCore::QEntityPrivate, and
  has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DRender::QCameraPrivate that has a ritual and
  that Python can call so far, 2 names in all: 'q_func',
  'updateViewMatrixAndTransform'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QCamera *Qt3DRender::QCameraPrivate::q_func() const': takes
    in Python what 'QCamera *Qt3DRender::QCameraPrivate::q_func()' takes.

  What to expect
  --------------

  - The C++ Qt3DRender::QCameraPrivate is created at the first use, not by
    'Qt3DRender::QCameraPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DRender::QCameraPrivate.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DRender::QCameraPrivate'

  #  A C++ Qt3DRender::QCameraPrivate Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DRender_QCameraPrivate'

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

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'Qt3DRender::QCameraPrivate::QCameraPrivate()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qcameraprivate.html#QCameraPrivate
    """
    #  Qt3DRender::QCameraPrivate::QCameraPrivate()
    self._noteCreation(QCameraPrivate, lambda: Rituals.call(
        'ritual_ZN10Qt3DRender14QCameraPrivateC1Ev',
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

  def q_func(self) -> Optional[Qt3DRender.QCamera]:
    """
    Calls Qt's 'QCamera *Qt3DRender::QCameraPrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qcameraprivate.html#q_func

    Returns
    -------

    Optional[Qt3DRender.QCamera]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QCamera *Qt3DRender::QCameraPrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN10Qt3DRender14QCameraPrivate6q_funcEv',
    )
    return Qt3DRender.QCamera._cuteAt(address)

  @overload()
  @overload(bool)
  def updateViewMatrixAndTransform(self, doEmit: bool = True) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::QCameraPrivate::updateViewMatrixAndTransform(bool doEmit)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qcameraprivate.html

    Parameters
    ----------

    doEmit : bool
      Passed on as it is. May be left out, as in Qt: it is then True.
    """
    #  void Qt3DRender::QCameraPrivate::updateViewMatrixAndTransform(bool
    #      doEmit)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender14QCameraPrivate28updateViewMatrixAndTransfor'
        'mEb',
        doEmit,
    )
