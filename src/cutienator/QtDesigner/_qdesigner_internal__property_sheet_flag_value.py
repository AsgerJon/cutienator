"""
qdesigner_internal::PropertySheetFlagValue binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDesigner/6.12.0/QtDesigner/private/qdesigner_utils_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means qdesigner_internal::PropertySheetFlagValue to be private: it
#  declares the class in a header it calls private. cutienator does not care.
#  Qt hands objects of the class out all the same, and a class we are handed
#  is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from . import qdesigner_internal


class PropertySheetFlagValue(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's qdesigner_internal::PropertySheetFlagValue: a plain
  Python object standing in front of one C++
  qdesigner_internal::PropertySheetFlagValue.

  C++ hands a qdesigner_internal::PropertySheetFlagValue around as a copy, so
  every C++ qdesigner_internal::PropertySheetFlagValue behind a cute one is
  Python's own: it is removed, by the ritual named in '__delete_ritual__',
  when the cute object goes.

  What exists
  -----------

  No function of Qt's qdesigner_internal::PropertySheetFlagValue yet. It can
  be made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's
    'qdesigner_internal::PropertySheetFlagValue::~PropertySheetFlagValue()':
    the destructor: Python removes its C++
    qdesigner_internal::PropertySheetFlagValue by it, and has no other use
    for it.

  What to expect
  --------------

  - The C++ qdesigner_internal::PropertySheetFlagValue is created at the
    first use, not by 'qdesigner_internal::PropertySheetFlagValue(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a qdesigner_internal::PropertySheetFlagValue back gives
    a copy the ritual made for Python, in a new cute
    qdesigner_internal::PropertySheetFlagValue.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'qdesigner_internal::PropertySheetFlagValue'

  #  Qt's '~qdesigner_internal::PropertySheetFlagValue()'. Naming it makes
  #  this a value class: Python owns every C++
  #  qdesigner_internal::PropertySheetFlagValue behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = (
      'ritual_ZN18qdesigner_internal22PropertySheetFlagValueD1Ev')

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

  @overload(int, WAIT['qdesigner_internal.DesignerMetaFlags'])
  def __init__(
      self,
      v: int,
      mf: qdesigner_internal.DesignerMetaFlags,
  ) -> None:
    """
    Notes what was given, for Qt's
    'qdesigner_internal::PropertySheetFlagValue::PropertySheetFlagValue(int
    v, const DesignerMetaFlags &mf)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-propertysheetflagvalue.html

    Parameters
    ----------

    v : int
      Passed on as it is.

    mf : qdesigner_internal.DesignerMetaFlags
      Passed on as a value: Qt reads the C++
      qdesigner_internal::DesignerMetaFlags, which stays Python's own.
    """
    #  qdesigner_internal::PropertySheetFlagValue::PropertySheetFlagValue(int
    #      v, const DesignerMetaFlags &mf)
    self._noteCreation(PropertySheetFlagValue, lambda: Rituals.call(
        'ritual_ZN18qdesigner_internal22PropertySheetFlagValueC1EiRKNS_17De'
        'signerMetaFlagsE',
        v, self._valueOf(mf),
    ))

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'qdesigner_internal::PropertySheetFlagValue::PropertySheetFlagValue()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-propertysheetflagvalue.html
    """
    #  qdesigner_internal::PropertySheetFlagValue::PropertySheetFlagValue()
    self._noteCreation(PropertySheetFlagValue, lambda: Rituals.call(
        'ritual_ZN18qdesigner_internal22PropertySheetFlagValueC1Ev',
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
