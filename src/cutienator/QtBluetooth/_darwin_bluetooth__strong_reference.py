"""
DarwinBluetooth::StrongReference binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtBluetooth/6.12.0/QtBluetooth/private/btraii_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means DarwinBluetooth::StrongReference to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class StrongReference(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's DarwinBluetooth::StrongReference: a plain Python
  object standing in front of one C++ DarwinBluetooth::StrongReference.

  What exists
  -----------

  Every function of Qt's DarwinBluetooth::StrongReference that has a ritual
  and that Python can call so far, 1 name in all: '__bool__'. It can be made
  from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void DarwinBluetooth::StrongReference::swap(StrongReference
    &other)': takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  10 of the 13 functions Qt declares: 9 cannot be called and cannot be called
  through the meta-object and cannot be copied; 1 a template.

  What to expect
  --------------

  - The C++ DarwinBluetooth::StrongReference is created at the first use, not
    by 'DarwinBluetooth::StrongReference(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ DarwinBluetooth::StrongReference.
  - Each name of Qt's DarwinBluetooth::StrongReference that has no cute
    function yet, 'getAs', 'release', 'reset', 'swap', holds a function that
    raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'DarwinBluetooth::StrongReference'

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

  def __bool__(self) -> bool:
    """
    Calls Qt's 'bool DarwinBluetooth::StrongReference::operator bool()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/darwinbluetooth-strongreference.html#operator bool
    """
    #  bool DarwinBluetooth::StrongReference::operator bool() const
    return self.uglySide.call(
        'ritual_ZNK15DarwinBluetooth15StrongReferencecvbEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'DarwinBluetooth::StrongReference::StrongReference()', which is called at
    the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/darwinbluetooth-strongreference.html
    """
    #  DarwinBluetooth::StrongReference::StrongReference()
    self._noteCreation(StrongReference, lambda: Rituals.call(
        'ritual_ZN15DarwinBluetooth15StrongReferenceC1Ev',
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

  @staticmethod
  def getAs(*__, **_) -> Never:
    """
    Qt's 'DarwinBluetooth::StrongReference::getAs': a template: a pattern and
    no single function.
    """
    raise NotImplementedError(
        "'DarwinBluetooth.StrongReference.getAs' has no cute function yet. "
        "Qt's 'DarwinBluetooth::StrongReference::getAs': a template: a "
        "pattern and no single function.")

  @staticmethod
  def release(*__, **_) -> Never:
    """
    Qt's 'void *DarwinBluetooth::StrongReference::release()': cannot be
    called and cannot be called through the meta-object and cannot be copied:
    no header file has its code, Qt's source does not mark it or its class
    for use from outside Qt or writes it 'inline' or nowhere, and it is no
    signal, slot or invokable function giving back nothing, of a class built
    on QObject, and Qt's source has no code for it that could be told from
    the rest.
    """
    raise NotImplementedError(
        "'DarwinBluetooth.StrongReference.release' has no cute function "
        "yet. Qt's 'void *DarwinBluetooth::StrongReference::release()': "
        "cannot be called and cannot be called through the meta-object and "
        "cannot be copied: no header file has its code, Qt's source does "
        "not mark it or its class for use from outside Qt or writes it "
        "'inline' or nowhere, and it is no signal, slot or invokable "
        "function giving back nothing, of a class built on QObject, and "
        "Qt's source has no code for it that could be told from the rest.")

  @staticmethod
  def reset(*__, **_) -> Never:
    """
    - Qt's 'void DarwinBluetooth::StrongReference::reset()': cannot be called
      and cannot be called through the meta-object and cannot be copied: no
      header file has its code, Qt's source does not mark it or its class for
      use from outside Qt or writes it 'inline' or nowhere, and it is no
      signal, slot or invokable function giving back nothing, of a class
      built on QObject, and Qt's source has no code for it that could be told
      from the rest.
    - Qt's 'void DarwinBluetooth::StrongReference::reset(void *newInstance,
      RetainPolicy policy)': cannot be called and cannot be called through
      the meta-object and cannot be copied: no header file has its code, Qt's
      source does not mark it or its class for use from outside Qt or writes
      it 'inline' or nowhere, and it is no signal, slot or invokable function
      giving back nothing, of a class built on QObject, and Qt's source has
      no code for it that could be told from the rest.
    """
    raise NotImplementedError(
        "'DarwinBluetooth.StrongReference.reset' has no cute function yet. "
        "Qt's 'void DarwinBluetooth::StrongReference::reset()': cannot be "
        "called and cannot be called through the meta-object and cannot be "
        "copied: no header file has its code, Qt's source does not mark it "
        "or its class for use from outside Qt or writes it 'inline' or "
        "nowhere, and it is no signal, slot or invokable function giving "
        "back nothing, of a class built on QObject, and Qt's source has no "
        "code for it that could be told from the rest. Qt's 'void "
        "DarwinBluetooth::StrongReference::reset(void *newInstance, "
        "RetainPolicy policy)': cannot be called and cannot be called "
        "through the meta-object and cannot be copied: no header file has "
        "its code, Qt's source does not mark it or its class for use from "
        "outside Qt or writes it 'inline' or nowhere, and it is no signal, "
        "slot or invokable function giving back nothing, of a class built "
        "on QObject, and Qt's source has no code for it that could be told "
        "from the rest.")

  @staticmethod
  def swap(*__, **_) -> Never:
    """
    Qt's 'void DarwinBluetooth::StrongReference::swap(StrongReference
    &other)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'DarwinBluetooth.StrongReference.swap' has no cute function yet. "
        "Qt's 'void DarwinBluetooth::StrongReference::swap(StrongReference "
        "&other)': takes a type Python has no way to hand over yet.")
