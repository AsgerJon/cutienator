"""
QSSGRhiInputAssemblerStatePrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrhicontext_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QSSGRhiInputAssemblerStatePrivate to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from ..cute import CuteMixin, MetaCute

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class QSSGRhiInputAssemblerStatePrivate(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QSSGRhiInputAssemblerStatePrivate: a plain Python
  object standing in front of one C++ QSSGRhiInputAssemblerStatePrivate.

  C++ hands a QSSGRhiInputAssemblerStatePrivate around as a copy, so every
  C++ QSSGRhiInputAssemblerStatePrivate behind a cute one is Python's own: it
  is removed, by the ritual named in '__delete_ritual__', when the cute
  object goes.

  What exists
  -----------

  No function of Qt's QSSGRhiInputAssemblerStatePrivate yet. None can be made
  from Python: one comes out of a function of another class that gives one
  back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const InputAssemblerState
    &QSSGRhiInputAssemblerStatePrivate::get(const
    QSSGRhiGraphicsPipelineState &ps)': gives a type Python has no way to
    take yet.
  - Qt's 'InputAssemblerState
    &QSSGRhiInputAssemblerStatePrivate::get(QSSGRhiGraphicsPipelineState
    &ps)': takes a type Python has no way to hand over yet.
  - Qt's
    'QSSGRhiInputAssemblerStatePrivate::~QSSGRhiInputAssemblerStatePrivate(
    )': the destructor: Python removes its C++
    QSSGRhiInputAssemblerStatePrivate by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QSSGRhiInputAssemblerStatePrivate is created at the first use,
    not by 'QSSGRhiInputAssemblerStatePrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QSSGRhiInputAssemblerStatePrivate back gives a copy
    the ritual made for Python, in a new cute
    QSSGRhiInputAssemblerStatePrivate.
  - Each name of Qt's QSSGRhiInputAssemblerStatePrivate that has no cute
    function yet, 'get', holds a function that raises 'NotImplementedError',
    and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSSGRhiInputAssemblerStatePrivate'

  #  Qt's '~QSSGRhiInputAssemblerStatePrivate()'. Naming it makes this a
  #  value class: Python owns every C++ QSSGRhiInputAssemblerStatePrivate
  #  behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN33QSSGRhiInputAssemblerStatePrivateD1Ev'

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
  def get(*__, **_) -> Never:
    """
    - Qt's 'const InputAssemblerState
      &QSSGRhiInputAssemblerStatePrivate::get(const
      QSSGRhiGraphicsPipelineState &ps)': gives a type Python has no way to
      take yet.
    - Qt's 'InputAssemblerState
      &QSSGRhiInputAssemblerStatePrivate::get(QSSGRhiGraphicsPipelineState
      &ps)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QSSGRhiInputAssemblerStatePrivate.get' has no cute function yet. "
        "Qt's 'const InputAssemblerState "
        "&QSSGRhiInputAssemblerStatePrivate::get(const "
        "QSSGRhiGraphicsPipelineState &ps)': gives a type Python has no way "
        "to take yet. Qt's 'InputAssemblerState "
        "&QSSGRhiInputAssemblerStatePrivate::get(QSSGRhiGraphicsPipelineStat"
        "e &ps)': takes a type Python has no way to hand over yet.")
