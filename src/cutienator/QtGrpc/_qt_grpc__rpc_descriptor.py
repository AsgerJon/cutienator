"""
QtGrpc::RpcDescriptor binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGrpc/qtgrpcnamespace.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from ..QtCore import QDebug
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDebug = WAIT['QDebug']


class RpcDescriptor(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QtGrpc::RpcDescriptor: a plain Python object standing
  in front of one C++ QtGrpc::RpcDescriptor.

  C++ hands a QtGrpc::RpcDescriptor around as a copy, so every C++
  QtGrpc::RpcDescriptor behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QtGrpc::RpcDescriptor that has a ritual and that
  Python can call so far, 7 names in all: '__eq__', '__ne__', '__lt__',
  '__gt__', '__le__', '__ge__', '__rlshift__'. None can be made from Python:
  one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QtGrpc::RpcDescriptor::~RpcDescriptor()': the destructor: Python
    removes its C++ QtGrpc::RpcDescriptor by it, and has no other use for it.

  What has no ritual
  ------------------

  2 of the 10 functions Qt declares: 2 forbidden.

  What to expect
  --------------

  - The C++ QtGrpc::RpcDescriptor is created at the first use, not by
    'QtGrpc::RpcDescriptor(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QtGrpc::RpcDescriptor back gives a copy the ritual
    made for Python, in a new cute QtGrpc::RpcDescriptor.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QtGrpc::RpcDescriptor'

  #  Qt's '~QtGrpc::RpcDescriptor()'. Naming it makes this a value class:
  #  Python owns every C++ QtGrpc::RpcDescriptor behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN6QtGrpc13RpcDescriptorD1Ev'

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

  @overload(THIS)
  def __eq__(self, rhs: RpcDescriptor) -> bool:
    """
    Calls Qt's 'bool operator==(const RpcDescriptor &lhs, const RpcDescriptor
    &rhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtgrpc-rpcdescriptor.html#operator==

    Parameters
    ----------

    rhs : RpcDescriptor
      Passed on as a value: Qt reads the C++ QtGrpc::RpcDescriptor, which
      stays Python's own.
    """
    #  bool operator==(const RpcDescriptor &lhs, const RpcDescriptor &rhs)
    return Rituals.call(
        'ritual_ZN6QtGrpceqERKNS_13RpcDescriptorES2_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload.fallback
  def __eq__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(THIS)
  def __ne__(self, rhs: RpcDescriptor) -> bool:
    """
    Calls Qt's 'bool operator!=(const RpcDescriptor &lhs, const RpcDescriptor
    &rhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtgrpc-rpcdescriptor.html#operator!=

    Parameters
    ----------

    rhs : RpcDescriptor
      Passed on as a value: Qt reads the C++ QtGrpc::RpcDescriptor, which
      stays Python's own.
    """
    #  bool operator!=(const RpcDescriptor &lhs, const RpcDescriptor &rhs)
    return Rituals.call(
        'ritual_ZN6QtGrpcneERKNS_13RpcDescriptorES2_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload.fallback
  def __ne__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(THIS)
  def __lt__(self, rhs: RpcDescriptor) -> bool:
    """
    Calls Qt's 'bool operator<(const RpcDescriptor &lhs, const RpcDescriptor
    &rhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtgrpc-rpcdescriptor.html#operator<

    Parameters
    ----------

    rhs : RpcDescriptor
      Passed on as a value: Qt reads the C++ QtGrpc::RpcDescriptor, which
      stays Python's own.
    """
    #  bool operator<(const RpcDescriptor &lhs, const RpcDescriptor &rhs)
    return Rituals.call(
        'ritual_ZN6QtGrpcltERKNS_13RpcDescriptorES2_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload.fallback
  def __lt__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(THIS)
  def __gt__(self, rhs: RpcDescriptor) -> bool:
    """
    Calls Qt's 'bool operator>(const RpcDescriptor &lhs, const RpcDescriptor
    &rhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtgrpc-rpcdescriptor.html#operator>

    Parameters
    ----------

    rhs : RpcDescriptor
      Passed on as a value: Qt reads the C++ QtGrpc::RpcDescriptor, which
      stays Python's own.
    """
    #  bool operator>(const RpcDescriptor &lhs, const RpcDescriptor &rhs)
    return Rituals.call(
        'ritual_ZN6QtGrpcgtERKNS_13RpcDescriptorES2_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload.fallback
  def __gt__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(THIS)
  def __le__(self, rhs: RpcDescriptor) -> bool:
    """
    Calls Qt's 'bool operator<=(const RpcDescriptor &lhs, const RpcDescriptor
    &rhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtgrpc-rpcdescriptor.html#operator<=

    Parameters
    ----------

    rhs : RpcDescriptor
      Passed on as a value: Qt reads the C++ QtGrpc::RpcDescriptor, which
      stays Python's own.
    """
    #  bool operator<=(const RpcDescriptor &lhs, const RpcDescriptor &rhs)
    return Rituals.call(
        'ritual_ZN6QtGrpcleERKNS_13RpcDescriptorES2_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload.fallback
  def __le__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(THIS)
  def __ge__(self, rhs: RpcDescriptor) -> bool:
    """
    Calls Qt's 'bool operator>=(const RpcDescriptor &lhs, const RpcDescriptor
    &rhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtgrpc-rpcdescriptor.html#operator>=

    Parameters
    ----------

    rhs : RpcDescriptor
      Passed on as a value: Qt reads the C++ QtGrpc::RpcDescriptor, which
      stays Python's own.
    """
    #  bool operator>=(const RpcDescriptor &lhs, const RpcDescriptor &rhs)
    return Rituals.call(
        'ritual_ZN6QtGrpcgeERKNS_13RpcDescriptorES2_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload.fallback
  def __ge__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(QDebug)
  def __rlshift__(self, debug: QDebug) -> QDebug:
    """
    Calls Qt's 'QDebug operator<<(QDebug debug, const RpcDescriptor
    &description)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtgrpc-rpcdescriptor.html#operator<<

    Parameters
    ----------

    debug : QDebug
      Passed on as a value: Qt reads the C++ QDebug, which stays Python's
      own.

    Returns
    -------

    QDebug
      A new cute QDebug around the copy Qt gave back. Python owns it.
    """
    #  QDebug operator<<(QDebug debug, const RpcDescriptor &description)
    address = Rituals.call(
        'ritual_ZN6QtGrpclsE6QDebugRKNS_13RpcDescriptorE',
        CuteMixin._valueOf(debug), CuteMixin._valueOf(self),
    )
    from ..QtCore import QDebug
    return QDebug._cuteOwning(address)

  @overload.fallback
  def __rlshift__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

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
