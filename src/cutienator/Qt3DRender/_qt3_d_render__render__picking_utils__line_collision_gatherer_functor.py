"""
Qt3DRender::Render::PickingUtils::LineCollisionGathererFunctor binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DRender/6.12.0/Qt3DRender/private/pickboundingvolumeutils_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means Qt3DRender::Render::PickingUtils::LineCollisionGathererFunctor to
#  be private: it declares the class in a header it calls private. cutienator
#  does not care. Qt hands objects of the class out all the same, and a class
#  we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from ..cute import WAIT
from . import Qt3DRender


class LineCollisionGathererFunctor(Qt3DRender.Render.PickingUtils.AbstractCollisionGathererFunctor):
  """
  The cute side of Qt's
  Qt3DRender::Render::PickingUtils::LineCollisionGathererFunctor: a plain
  Python object standing in front of one C++
  Qt3DRender::Render::PickingUtils::LineCollisionGathererFunctor.

  It is built on the cute
  'Qt3DRender::Render::PickingUtils::AbstractCollisionGathererFunctor', as
  Qt's Qt3DRender::Render::PickingUtils::LineCollisionGathererFunctor is
  built on Qt's
  Qt3DRender::Render::PickingUtils::AbstractCollisionGathererFunctor, and has
  everything that class has.

  C++ hands a Qt3DRender::Render::PickingUtils::LineCollisionGathererFunctor
  around as a copy, so every C++
  Qt3DRender::Render::PickingUtils::LineCollisionGathererFunctor behind a
  cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  No function of Qt's
  Qt3DRender::Render::PickingUtils::LineCollisionGathererFunctor yet. None
  can be made from Python: one comes out of a function of another class that
  gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'HitList
    Qt3DRender::Render::PickingUtils::LineCollisionGathererFunctor::
    computeHits(const std::vector<Entity *> &entities,
    Qt3DRender::QPickingSettings::PickResultMode mode)': takes a type Python
    has no way to hand over yet.
  - Qt's 'HitList
    Qt3DRender::Render::PickingUtils::LineCollisionGathererFunctor::pick(
    const Entity *entity) const': gives a type Python has no way to take yet.
  - Qt's 'Qt3DRender::Render::PickingUtils::LineCollisionGathererFunctor::
    ~LineCollisionGathererFunctor()': the destructor: Python removes its C++
    Qt3DRender::Render::PickingUtils::LineCollisionGathererFunctor by it, and
    has no other use for it.

  What to expect
  --------------

  - The C++ Qt3DRender::Render::PickingUtils::LineCollisionGathererFunctor is
    created at the first use, not by
    'Qt3DRender::Render::PickingUtils::LineCollisionGathererFunctor(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a
    Qt3DRender::Render::PickingUtils::LineCollisionGathererFunctor back gives
    a copy the ritual made for Python, in a new cute
    Qt3DRender::Render::PickingUtils::LineCollisionGathererFunctor.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DRender::Render::PickingUtils::LineCollisionGathererFunctor'

  #  Qt's
  #  '~Qt3DRender::Render::PickingUtils::LineCollisionGathererFunctor()'.
  #  Naming it makes this a value class: Python owns every C++
  #  Qt3DRender::Render::PickingUtils::LineCollisionGathererFunctor behind a
  #  cute one, and removes it by this ritual.
  __delete_ritual__ = (
      'ritual_ZN10Qt3DRender6Render12PickingUtils28LineCollisionGathererFunctorD1Ev')

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
