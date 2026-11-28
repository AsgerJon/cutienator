"""
QQmlSA::ElementPass binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQmlCompiler/qqmlsa.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from . import QQmlSA

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class ElementPass(QQmlSA.GenericPass):
  """
  The cute side of Qt's QQmlSA::ElementPass: a plain Python object standing
  in front of one C++ QQmlSA::ElementPass.

  It is built on the cute 'QQmlSA::GenericPass', as Qt's QQmlSA::ElementPass
  is built on Qt's QQmlSA::GenericPass, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQmlSA::ElementPass that has a ritual and that
  Python can call so far, 2 names in all: 'shouldRun', 'run'. It can be made
  from Python, in 1 way; see '__init__'.

  What to expect
  --------------

  - The C++ QQmlSA::ElementPass is created at the first use, not by
    'QQmlSA::ElementPass(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQmlSA::ElementPass.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlSA::ElementPass'

  #  A C++ QQmlSA::ElementPass Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQmlSA_ElementPass'

  #  The functions Qt calls itself that QQmlSA::ElementPass is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'shouldRun': (
          ('_ZN6QQmlSA11ElementPass9shouldRunERKNS_7ElementE',
           ('bool', 'number', ''),
           (
               ('address', 'value', 'QtQmlCompiler:QQmlSA.Element'),
           )),
      ),
      'run': (
          ('_ZN6QQmlSA11ElementPass3runERKNS_7ElementE',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtQmlCompiler:QQmlSA.Element'),
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

  @overload(WAIT['QQmlSA.PassManager'])
  @overload(NoneType)
  def __init__(self, manager: Optional[QQmlSA.PassManager]) -> None:
    """
    Notes what was given, for Qt's
    'QQmlSA::ElementPass::ElementPass(PassManager *manager)', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsa-elementpass.html#ElementPass

    Parameters
    ----------

    manager : Optional[QQmlSA.PassManager]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QQmlSA::ElementPass::ElementPass(PassManager *manager)
    self._noteCreation(ElementPass, lambda: Rituals.call(
        'ritual_ZN6QQmlSA11ElementPassC1EPNS_11PassManagerE',
        self._addressOf(manager),
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

  @overload(WAIT['QQmlSA.Element'])
  def shouldRun(self, element: QQmlSA.Element) -> bool:
    """
    Calls Qt's 'bool QQmlSA::ElementPass::shouldRun(const Element &element)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlsa-elementpass.html#shouldRun

    Parameters
    ----------

    element : QQmlSA.Element
      Passed on as a value: Qt reads the C++ QQmlSA::Element, which stays
      Python's own.
    """
    #  bool QQmlSA::ElementPass::shouldRun(const Element &element)
    ritual = 'ritual_ZN6QQmlSA11ElementPass9shouldRunERKNS_7ElementE'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN6QQmlSA11ElementPass9shouldRunERKNS_7ElementE'
    return self.uglySide.call(ritual, self._valueOf(element))

  @overload(WAIT['QQmlSA.Element'])
  def run(self, element: QQmlSA.Element) -> None:
    """
    Calls Qt's 'void QQmlSA::ElementPass::run(const Element &element)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlsa-elementpass.html#run

    Parameters
    ----------

    element : QQmlSA.Element
      Passed on as a value: Qt reads the C++ QQmlSA::Element, which stays
      Python's own.
    """
    #  void QQmlSA::ElementPass::run(const Element &element)
    self.uglySide.call(
        'ritual_ZN6QQmlSA11ElementPass3runERKNS_7ElementE',
        self._valueOf(element),
    )
