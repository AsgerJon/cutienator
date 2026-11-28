"""
Qt3DRender::QStencilTestArgumentsPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DRender/6.12.0/Qt3DRender/private/qstenciltestarguments_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means Qt3DRender::QStencilTestArgumentsPrivate to be private: it
#  declares the class in a header it calls private. cutienator does not care.
#  Qt hands objects of the class out all the same, and a class we are handed
#  is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..QtCore import QObjectPrivate
from . import Qt3DRender

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional


class QStencilTestArgumentsPrivate(QObjectPrivate):
  """
  The cute side of Qt's Qt3DRender::QStencilTestArgumentsPrivate: a plain
  Python object standing in front of one C++
  Qt3DRender::QStencilTestArgumentsPrivate.

  It is built on the cute 'QObjectPrivate', as Qt's
  Qt3DRender::QStencilTestArgumentsPrivate is built on Qt's QObjectPrivate,
  and has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DRender::QStencilTestArgumentsPrivate that has a
  ritual and that Python can call so far, 1 name in all: 'q_func'. It can be
  made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QStencilTestArguments
    *Qt3DRender::QStencilTestArgumentsPrivate::q_func() const': takes in
    Python what 'QStencilTestArguments
    *Qt3DRender::QStencilTestArgumentsPrivate::q_func()' takes.

  What to expect
  --------------

  - The C++ Qt3DRender::QStencilTestArgumentsPrivate is created at the first
    use, not by 'Qt3DRender::QStencilTestArgumentsPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DRender::QStencilTestArgumentsPrivate.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DRender::QStencilTestArgumentsPrivate'

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

  @overload(Qt3DRender.QStencilTestArguments.StencilFaceMode)
  def __init__(
      self,
      face: Qt3DRender.QStencilTestArguments.StencilFaceMode,
  ) -> None:
    """
    Notes what was given, for Qt's
    'Qt3DRender::QStencilTestArgumentsPrivate::QStencilTestArgumentsPrivate(
    QStencilTestArguments::StencilFaceMode face)', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qstenciltestargumentsprivate.html

    Parameters
    ----------

    face : Qt3DRender.QStencilTestArguments.StencilFaceMode
      Passed on as its number.
    """
    #  Qt3DRender::QStencilTestArgumentsPrivate::
    #      QStencilTestArgumentsPrivate(QStencilTestArguments::
    #      StencilFaceMode face)
    self._noteCreation(QStencilTestArgumentsPrivate, lambda: Rituals.call(
        'ritual_ZN10Qt3DRender28QStencilTestArgumentsPrivateC1ENS_21QStenci'
        'lTestArguments15StencilFaceModeE',
        face.value,
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

  def q_func(self) -> Optional[Qt3DRender.QStencilTestArguments]:
    """
    Calls Qt's 'QStencilTestArguments
    *Qt3DRender::QStencilTestArgumentsPrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qstenciltestargumentsprivate.html

    Returns
    -------

    Optional[Qt3DRender.QStencilTestArguments]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QStencilTestArguments
    #      *Qt3DRender::QStencilTestArgumentsPrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN10Qt3DRender28QStencilTestArgumentsPrivate6q_funcEv',
    )
    return Qt3DRender.QStencilTestArguments._cuteAt(address)
