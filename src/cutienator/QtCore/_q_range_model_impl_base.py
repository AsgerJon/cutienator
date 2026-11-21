"""
QRangeModelImplBase binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/qrangemodel_impl.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QRangeModel
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QRangeModel = WAIT['QRangeModel']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QRangeModelImplBase(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QRangeModelImplBase: a plain Python object standing
  in front of one C++ QRangeModelImplBase.

  What exists
  -----------

  Every function of Qt's QRangeModelImplBase that has a ritual and that
  Python can call so far, 1 name in all: 'getImplementation'. None can be
  made from Python: one comes out of a function of another class that gives
  one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QRangeModelImplBase
    *QRangeModelImplBase::getImplementation(const QRangeModel *model)': takes
    in Python what 'QRangeModelImplBase
    *QRangeModelImplBase::getImplementation(QRangeModel *model)' takes.

  What has no ritual
  ------------------

  72 of the 74 functions Qt declares: 36 protected; 31 declared and nowhere
  to be found; 5 takes or gives a type that cannot be passed yet.

  What to expect
  --------------

  - The C++ QRangeModelImplBase is created at the first use, not by
    'QRangeModelImplBase(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QRangeModelImplBase.
  """

  #  The enums Qt writes inside QRangeModelImplBase, each a class in here as
  #  in C++, and the names Qt has for the combinations of its flags enums.

  class AutoConnectPolicy(CuteNum, scoped=True):
    """
    The enum 'QRangeModelImplBase::AutoConnectPolicy' of Qt, with the 3 names
    Qt gives in it. C++ keeps these names inside the enum, so the class that
    holds the enum does not have them.
    """

    NULL = Kee[int](0)
    Full = Kee[int](1)
    OnRead = Kee[int](2)

  class DropOperation(CuteNum, scoped=True):
    """
    The enum 'QRangeModelImplBase::DropOperation' of Qt, with the 6 names Qt
    gives in it. C++ keeps these names inside the enum, so the class that
    holds the enum does not have them.
    """

    DontDrop = Kee[int](0)
    Automatic = Kee[int](1)
    OverwriteAndIgnore = Kee[int](2)
    OverwriteAndExtend = Kee[int](3)
    InsertAsSiblings = Kee[int](4)
    InsertAsChildren = Kee[int](5)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QRangeModel)
  @overload(NoneType)
  def getImplementation(
      model: Optional[QRangeModel],
  ) -> Optional[QRangeModelImplBase]:
    """
    Calls Qt's 'QRangeModelImplBase
    *QRangeModelImplBase::getImplementation(QRangeModel *model)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrangemodelimplbase.html#getImplementation

    Parameters
    ----------

    model : Optional[QRangeModel]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QRangeModelImplBase]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QRangeModelImplBase
    #      *QRangeModelImplBase::getImplementation(QRangeModel *model)
    address = Rituals.call(
        'ritual_ZN19QRangeModelImplBase17getImplementationEP11QRangeModel',
        CuteMixin._addressOf(model),
    )
    return QRangeModelImplBase._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QRangeModelImplBase'

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
