"""
QSSGFragmentShaderGenerator binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrendershadercodegenerator_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QSSGFragmentShaderGenerator to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..occult import Rituals
from . import QSSGStageGeneratorBase


class QSSGFragmentShaderGenerator(QSSGStageGeneratorBase):
  """
  The cute side of Qt's QSSGFragmentShaderGenerator: a plain Python object
  standing in front of one C++ QSSGFragmentShaderGenerator.

  It is built on the cute 'QSSGStageGeneratorBase', as Qt's
  QSSGFragmentShaderGenerator is built on Qt's QSSGStageGeneratorBase, and
  has everything that class has.

  C++ hands a QSSGFragmentShaderGenerator around as a copy, so every C++
  QSSGFragmentShaderGenerator behind a cute one is Python's own: it is
  removed, by the ritual named in '__delete_ritual__', when the cute object
  goes.

  What exists
  -----------

  Every function of Qt's QSSGFragmentShaderGenerator that has a ritual and
  that Python can call so far, 2 names in all: 'addShaderIncomingMap',
  'addShaderOutgoingMap'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSSGFragmentShaderGenerator::~QSSGFragmentShaderGenerator()': the
    destructor: Python removes its C++ QSSGFragmentShaderGenerator by it, and
    has no other use for it.

  What to expect
  --------------

  - The C++ QSSGFragmentShaderGenerator is created at the first use, not by
    'QSSGFragmentShaderGenerator(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QSSGFragmentShaderGenerator back gives a copy the
    ritual made for Python, in a new cute QSSGFragmentShaderGenerator.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSSGFragmentShaderGenerator'

  #  Qt's '~QSSGFragmentShaderGenerator()'. Naming it makes this a value
  #  class: Python owns every C++ QSSGFragmentShaderGenerator behind a cute
  #  one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN27QSSGFragmentShaderGeneratorD1Ev'

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
    'QSSGFragmentShaderGenerator::QSSGFragmentShaderGenerator()', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgfragmentshadergenerator.html
    """
    #  QSSGFragmentShaderGenerator::QSSGFragmentShaderGenerator()
    self._noteCreation(QSSGFragmentShaderGenerator, lambda: Rituals.call(
        'ritual_ZN27QSSGFragmentShaderGeneratorC1Ev',
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

  def addShaderIncomingMap(self) -> None:
    """
    Calls Qt's 'void QSSGFragmentShaderGenerator::addShaderIncomingMap()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgfragmentshadergenerator.html
    """
    #  void QSSGFragmentShaderGenerator::addShaderIncomingMap()
    self.uglySide.call(
        'ritual_ZN27QSSGFragmentShaderGenerator20addShaderIncomingMapEv',
    )

  def addShaderOutgoingMap(self) -> None:
    """
    Calls Qt's 'void QSSGFragmentShaderGenerator::addShaderOutgoingMap()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgfragmentshadergenerator.html
    """
    #  void QSSGFragmentShaderGenerator::addShaderOutgoingMap()
    self.uglySide.call(
        'ritual_ZN27QSSGFragmentShaderGenerator20addShaderOutgoingMapEv',
    )
