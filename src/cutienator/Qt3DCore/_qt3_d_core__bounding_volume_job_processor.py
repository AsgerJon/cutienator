"""
Qt3DCore::BoundingVolumeJobProcessor binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DCore/6.12.0/Qt3DCore/private/calcboundingvolumejob_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means Qt3DCore::BoundingVolumeJobProcessor to be private: it declares
#  the class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from . import Qt3DCore


class BoundingVolumeJobProcessor(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's Qt3DCore::BoundingVolumeJobProcessor: a plain Python
  object standing in front of one C++ Qt3DCore::BoundingVolumeJobProcessor.

  What exists
  -----------

  Every function of Qt's Qt3DCore::BoundingVolumeJobProcessor that has a
  ritual and that Python can call so far, 1 name in all: 'process'. None can
  be made from Python: one comes out of a function of another class that
  gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's
    'Qt3DCore::BoundingVolumeJobProcessor::~BoundingVolumeJobProcessor()':
    the destructor: Python never removes a C++
    Qt3DCore::BoundingVolumeJobProcessor.

  What to expect
  --------------

  - The C++ Qt3DCore::BoundingVolumeJobProcessor is created at the first use,
    not by 'Qt3DCore::BoundingVolumeJobProcessor(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DCore::BoundingVolumeJobProcessor.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DCore::BoundingVolumeJobProcessor'

  #  A C++ Qt3DCore::BoundingVolumeJobProcessor Python makes is of a C++
  #  class of ours, in which Python can take functions over. This ritual
  #  hands one over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DCore_BoundingVolumeJobProcessor'

  #  The functions Qt calls itself that Qt3DCore::BoundingVolumeJobProcessor
  #  is the first to declare. A class of a program built on it can write one
  #  anew, and Qt then calls that. For each name: the key C++ knows the
  #  function by, what it gives, and what it takes.
  __virtual_functions__ = {
      'process': (
          ('_ZN8Qt3DCore26BoundingVolumeJobProcessor7processERKNS_27Boundin'
           'gVolumeComputeResultEb',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value',
                'Qt3DCore:Qt3DCore.BoundingVolumeComputeResult'),
               ('bool', 'number', ''),
           )),
      ),
  }

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

  @overload(WAIT['Qt3DCore.BoundingVolumeComputeResult'], bool)
  def process(
      self,
      result: Qt3DCore.BoundingVolumeComputeResult,
      computedResult: bool,
  ) -> None:
    """
    Calls Qt's 'void Qt3DCore::BoundingVolumeJobProcessor::process(const
    BoundingVolumeComputeResult &result, bool computedResult)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-boundingvolumejobprocessor.html#process

    Parameters
    ----------

    result : Qt3DCore.BoundingVolumeComputeResult
      Passed on as a value: Qt reads the C++
      Qt3DCore::BoundingVolumeComputeResult, which stays Python's own.

    computedResult : bool
      Passed on as it is.
    """
    #  void Qt3DCore::BoundingVolumeJobProcessor::process(const
    #      BoundingVolumeComputeResult &result, bool computedResult)
    self._callAs(
        'Qt3DCore::BoundingVolumeJobProcessor',
        'ritual_ZN8Qt3DCore26BoundingVolumeJobProcessor7processERKNS_27Boun'
        'dingVolumeComputeResultEb',
        self._valueOf(result), computedResult,
    )
