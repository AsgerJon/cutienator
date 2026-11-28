"""
QV4::Heap::ReferenceObjectEndpoint binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qv4referenceobject_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QV4::Heap::ReferenceObjectEndpoint to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from . import QQmlNotifierEndpoint, QV4

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class ReferenceObjectEndpoint(QQmlNotifierEndpoint):
  """
  The cute side of Qt's QV4::Heap::ReferenceObjectEndpoint: a plain Python
  object standing in front of one C++ QV4::Heap::ReferenceObjectEndpoint.

  It is built on the cute 'QQmlNotifierEndpoint', as Qt's
  QV4::Heap::ReferenceObjectEndpoint is built on Qt's QQmlNotifierEndpoint,
  and has everything that class has.

  C++ hands a QV4::Heap::ReferenceObjectEndpoint around as a copy, so every
  C++ QV4::Heap::ReferenceObjectEndpoint behind a cute one is Python's own:
  it is removed, by the ritual named in '__delete_ritual__', when the cute
  object goes.

  What exists
  -----------

  No function of Qt's QV4::Heap::ReferenceObjectEndpoint yet. It can be made
  from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QV4::Heap::ReferenceObjectEndpoint::~ReferenceObjectEndpoint()':
    the destructor: Python removes its C++ QV4::Heap::ReferenceObjectEndpoint
    by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QV4::Heap::ReferenceObjectEndpoint is created at the first use,
    not by 'QV4::Heap::ReferenceObjectEndpoint(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QV4::Heap::ReferenceObjectEndpoint back gives a copy
    the ritual made for Python, in a new cute
    QV4::Heap::ReferenceObjectEndpoint.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QV4::Heap::ReferenceObjectEndpoint'

  #  Qt's '~QV4::Heap::ReferenceObjectEndpoint()'. Naming it makes this a
  #  value class: Python owns every C++ QV4::Heap::ReferenceObjectEndpoint
  #  behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN3QV44Heap23ReferenceObjectEndpointD1Ev'

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

  @overload(WAIT['QV4.Heap.ReferenceObject'])
  @overload(NoneType)
  def __init__(self, reference: Optional[QV4.Heap.ReferenceObject]) -> None:
    """
    Notes what was given, for Qt's
    'QV4::Heap::ReferenceObjectEndpoint::ReferenceObjectEndpoint(
    ReferenceObject *reference)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-heap-referenceobjectendpoint.html

    Parameters
    ----------

    reference : Optional[QV4.Heap.ReferenceObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QV4::Heap::ReferenceObjectEndpoint::ReferenceObjectEndpoint(
    #      ReferenceObject *reference)
    self._noteCreation(ReferenceObjectEndpoint, lambda: Rituals.call(
        'ritual_ZN3QV44Heap23ReferenceObjectEndpointC1EPNS0_15ReferenceObje'
        'ctE',
        self._addressOf(reference),
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
