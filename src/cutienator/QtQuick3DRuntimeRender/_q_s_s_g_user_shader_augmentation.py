"""
QSSGUserShaderAugmentation binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrendershadercache_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QSSGUserShaderAugmentation to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from ..cute import CuteMixin, MetaCute


class QSSGUserShaderAugmentation(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QSSGUserShaderAugmentation: a plain Python object
  standing in front of one C++ QSSGUserShaderAugmentation.

  C++ hands a QSSGUserShaderAugmentation around as a copy, so every C++
  QSSGUserShaderAugmentation behind a cute one is Python's own: it is
  removed, by the ritual named in '__delete_ritual__', when the cute object
  goes.

  What exists
  -----------

  Every function of Qt's QSSGUserShaderAugmentation that has a ritual and
  that Python can call so far, 2 names in all: 'hasUserAugmentation',
  'hasPropertyUniforms'. None can be made from Python: one comes out of a
  function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSSGUserShaderAugmentation::~QSSGUserShaderAugmentation()': the
    destructor: Python removes its C++ QSSGUserShaderAugmentation by it, and
    has no other use for it.

  What to expect
  --------------

  - The C++ QSSGUserShaderAugmentation is created at the first use, not by
    'QSSGUserShaderAugmentation(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QSSGUserShaderAugmentation back gives a copy the
    ritual made for Python, in a new cute QSSGUserShaderAugmentation.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSSGUserShaderAugmentation'

  #  Qt's '~QSSGUserShaderAugmentation()'. Naming it makes this a value
  #  class: Python owns every C++ QSSGUserShaderAugmentation behind a cute
  #  one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN26QSSGUserShaderAugmentationD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def hasUserAugmentation(self) -> bool:
    """
    Calls Qt's 'bool QSSGUserShaderAugmentation::hasUserAugmentation()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgusershaderaugmentation.html
    """
    #  bool QSSGUserShaderAugmentation::hasUserAugmentation() const
    return self.uglySide.call(
        'ritual_ZNK26QSSGUserShaderAugmentation19hasUserAugmentationEv',
    )

  def hasPropertyUniforms(self) -> bool:
    """
    Calls Qt's 'bool QSSGUserShaderAugmentation::hasPropertyUniforms()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgusershaderaugmentation.html
    """
    #  bool QSSGUserShaderAugmentation::hasPropertyUniforms() const
    return self.uglySide.call(
        'ritual_ZNK26QSSGUserShaderAugmentation19hasPropertyUniformsEv',
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
