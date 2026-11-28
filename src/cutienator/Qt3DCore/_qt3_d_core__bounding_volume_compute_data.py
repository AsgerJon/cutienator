"""
Qt3DCore::BoundingVolumeComputeData binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DCore/6.12.0/Qt3DCore/private/calcboundingvolumejob_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means Qt3DCore::BoundingVolumeComputeData to be private: it declares
#  the class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from . import Qt3DCore

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class BoundingVolumeComputeData(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's Qt3DCore::BoundingVolumeComputeData: a plain Python
  object standing in front of one C++ Qt3DCore::BoundingVolumeComputeData.

  C++ hands a Qt3DCore::BoundingVolumeComputeData around as a copy, so every
  C++ Qt3DCore::BoundingVolumeComputeData behind a cute one is Python's own:
  it is removed, by the ritual named in '__delete_ritual__', when the cute
  object goes.

  What exists
  -----------

  Every function of Qt's Qt3DCore::BoundingVolumeComputeData that has a
  ritual and that Python can call so far, 3 names in all: 'fromView',
  'valid', 'compute'. None can be made from Python: one comes out of a
  function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'Qt3DCore::BoundingVolumeComputeData::~BoundingVolumeComputeData()':
    the destructor: Python removes its C++
    Qt3DCore::BoundingVolumeComputeData by it, and has no other use for it.

  What to expect
  --------------

  - The C++ Qt3DCore::BoundingVolumeComputeData is created at the first use,
    not by 'Qt3DCore::BoundingVolumeComputeData(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a Qt3DCore::BoundingVolumeComputeData back gives a copy
    the ritual made for Python, in a new cute
    Qt3DCore::BoundingVolumeComputeData.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(WAIT['Qt3DCore.QGeometryView'])
  @overload(NoneType)
  def fromView(
      view: Optional[Qt3DCore.QGeometryView],
  ) -> BoundingVolumeComputeData:
    """
    Calls Qt's 'BoundingVolumeComputeData
    Qt3DCore::BoundingVolumeComputeData::fromView(QGeometryView *view)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-boundingvolumecomputedata.html#fromView

    Parameters
    ----------

    view : Optional[Qt3DCore.QGeometryView]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    BoundingVolumeComputeData
      A new cute Qt3DCore::BoundingVolumeComputeData around the copy Qt gave
      back. Python owns it.
    """
    #  BoundingVolumeComputeData
    #      Qt3DCore::BoundingVolumeComputeData::fromView(QGeometryView *view)
    address = Rituals.call(
        'ritual_ZN8Qt3DCore25BoundingVolumeComputeData8fromViewEPNS_13QGeom'
        'etryViewE',
        CuteMixin._addressOf(view),
    )
    return BoundingVolumeComputeData._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DCore::BoundingVolumeComputeData'

  #  Qt's '~Qt3DCore::BoundingVolumeComputeData()'. Naming it makes this a
  #  value class: Python owns every C++ Qt3DCore::BoundingVolumeComputeData
  #  behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN8Qt3DCore25BoundingVolumeComputeDataD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def valid(self) -> bool:
    """
    Calls Qt's 'bool Qt3DCore::BoundingVolumeComputeData::valid() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-boundingvolumecomputedata.html#valid
    """
    #  bool Qt3DCore::BoundingVolumeComputeData::valid() const
    return self.uglySide.call(
        'ritual_ZNK8Qt3DCore25BoundingVolumeComputeData5validEv',
    )

  def compute(self) -> Qt3DCore.BoundingVolumeComputeResult:
    """
    Calls Qt's 'BoundingVolumeComputeResult
    Qt3DCore::BoundingVolumeComputeData::compute() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-boundingvolumecomputedata.html#compute

    Returns
    -------

    Qt3DCore.BoundingVolumeComputeResult
      A new cute Qt3DCore::BoundingVolumeComputeResult around the copy Qt
      gave back. Python owns it.
    """
    #  BoundingVolumeComputeResult
    #      Qt3DCore::BoundingVolumeComputeData::compute() const
    address = self.uglySide.call(
        'ritual_ZNK8Qt3DCore25BoundingVolumeComputeData7computeEv',
    )
    return Qt3DCore.BoundingVolumeComputeResult._cuteOwning(address)

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
