"""
QSSGRenderShaderMetadata::Uniform binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrendershadermetadata_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QSSGRenderShaderMetadata::Uniform to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute
from ..occult import Rituals


class Uniform(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QSSGRenderShaderMetadata::Uniform: a plain Python
  object standing in front of one C++ QSSGRenderShaderMetadata::Uniform.

  C++ hands a QSSGRenderShaderMetadata::Uniform around as a copy, so every
  C++ QSSGRenderShaderMetadata::Uniform behind a cute one is Python's own: it
  is removed, by the ritual named in '__delete_ritual__', when the cute
  object goes.

  What exists
  -----------

  Every function of Qt's QSSGRenderShaderMetadata::Uniform that has a ritual
  and that Python can call so far, 1 name in all: 'conditionFromString'. None
  can be made from Python: one comes out of a function of another class that
  gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSSGRenderShaderMetadata::Uniform::~Uniform()': the destructor:
    Python removes its C++ QSSGRenderShaderMetadata::Uniform by it, and has
    no other use for it.

  What to expect
  --------------

  - The C++ QSSGRenderShaderMetadata::Uniform is created at the first use,
    not by 'QSSGRenderShaderMetadata::Uniform(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QSSGRenderShaderMetadata::Uniform back gives a copy
    the ritual made for Python, in a new cute
    QSSGRenderShaderMetadata::Uniform.
  """

  #  The enums Qt writes inside QSSGRenderShaderMetadata::Uniform, each a
  #  class in here as in C++, and the names Qt has for the combinations of
  #  its flags enums.

  class Condition(CuteNum):
    """
    The enum 'QSSGRenderShaderMetadata::Uniform::Condition' of Qt, with the 3
    names Qt gives in it.
    """

    NULL = Kee[int](0)
    Regular = Kee[int](1)
    Negated = Kee[int](2)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(str)
  def conditionFromString(condition: str) -> Condition:
    """
    Calls Qt's 'Condition
    QSSGRenderShaderMetadata::Uniform::conditionFromString(const QString
    &condition)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrendershadermetadata-uniform.html

    Parameters
    ----------

    condition : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    Condition
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Condition(number)' gives.
    """
    #  Condition QSSGRenderShaderMetadata::Uniform::conditionFromString(const
    #      QString &condition)
    return Uniform.Condition(Rituals.call(
        'ritual_ZN24QSSGRenderShaderMetadata7Uniform19conditionFromStringER'
        'K7QString',
        condition,
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSSGRenderShaderMetadata::Uniform'

  #  Qt's '~QSSGRenderShaderMetadata::Uniform()'. Naming it makes this a
  #  value class: Python owns every C++ QSSGRenderShaderMetadata::Uniform
  #  behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN24QSSGRenderShaderMetadata7UniformD1Ev'

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
