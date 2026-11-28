"""
Qt3DRender::QStencilTestPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DRender/6.12.0/Qt3DRender/private/qstenciltest_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means Qt3DRender::QStencilTestPrivate to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from . import Qt3DRender

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional


class QStencilTestPrivate(Qt3DRender.QRenderStatePrivate):
  """
  The cute side of Qt's Qt3DRender::QStencilTestPrivate: a plain Python
  object standing in front of one C++ Qt3DRender::QStencilTestPrivate.

  It is built on the cute 'Qt3DRender::QRenderStatePrivate', as Qt's
  Qt3DRender::QStencilTestPrivate is built on Qt's
  Qt3DRender::QRenderStatePrivate, and has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DRender::QStencilTestPrivate that has a ritual
  and that Python can call so far, 1 name in all: 'q_func'. It can be made
  from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QStencilTest *Qt3DRender::QStencilTestPrivate::q_func()
    const': takes in Python what 'QStencilTest
    *Qt3DRender::QStencilTestPrivate::q_func()' takes.
  - Qt's 'void Qt3DRender::QStencilTestPrivate::fillData(QStencilTestData
    &data) const': takes a type Python has no way to hand over yet.

  What to expect
  --------------

  - The C++ Qt3DRender::QStencilTestPrivate is created at the first use, not
    by 'Qt3DRender::QStencilTestPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DRender::QStencilTestPrivate.
  - Each name of Qt's Qt3DRender::QStencilTestPrivate that has no cute
    function yet, 'fillData', holds a function that raises
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
  __qt_class__ = 'Qt3DRender::QStencilTestPrivate'

  #  A C++ Qt3DRender::QStencilTestPrivate Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DRender_QStencilTestPrivate'

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
    'Qt3DRender::QStencilTestPrivate::QStencilTestPrivate()', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qstenciltestprivate.html
    """
    #  Qt3DRender::QStencilTestPrivate::QStencilTestPrivate()
    self._noteCreation(QStencilTestPrivate, lambda: Rituals.call(
        'ritual_ZN10Qt3DRender19QStencilTestPrivateC1Ev',
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

  def q_func(self) -> Optional[Qt3DRender.QStencilTest]:
    """
    Calls Qt's 'QStencilTest *Qt3DRender::QStencilTestPrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qstenciltestprivate.html#q_func

    Returns
    -------

    Optional[Qt3DRender.QStencilTest]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QStencilTest *Qt3DRender::QStencilTestPrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN10Qt3DRender19QStencilTestPrivate6q_funcEv',
    )
    return Qt3DRender.QStencilTest._cuteAt(address)

  @staticmethod
  def fillData(*__, **_) -> Never:
    """
    Qt's 'void Qt3DRender::QStencilTestPrivate::fillData(QStencilTestData
    &data) const': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'Qt3DRender.QStencilTestPrivate.fillData' has no cute function "
        "yet. Qt's 'void "
        "Qt3DRender::QStencilTestPrivate::fillData(QStencilTestData &data) "
        "const': takes a type Python has no way to hand over yet.")
