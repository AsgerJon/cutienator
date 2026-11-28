"""
QQmlSA::LintPlugin binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQmlCompiler/qqmlsa.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from . import QQmlSA

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class LintPlugin(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQmlSA::LintPlugin: a plain Python object standing in
  front of one C++ QQmlSA::LintPlugin.

  What exists
  -----------

  Every function of Qt's QQmlSA::LintPlugin that has a ritual and that Python
  can call so far, 1 name in all: 'registerPasses'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QQmlSA::LintPlugin::~LintPlugin()': the destructor: Python never
    removes a C++ QQmlSA::LintPlugin.

  What has no ritual
  ------------------

  4 of the 7 functions Qt declares: 4 forbidden.

  What to expect
  --------------

  - The C++ QQmlSA::LintPlugin is created at the first use, not by
    'QQmlSA::LintPlugin(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQmlSA::LintPlugin.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlSA::LintPlugin'

  #  A C++ QQmlSA::LintPlugin Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQmlSA_LintPlugin'

  #  The functions Qt calls itself that QQmlSA::LintPlugin is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'registerPasses': (
          ('_ZN6QQmlSA10LintPlugin14registerPassesEPNS_11PassManagerERKNS_7'
           'ElementE',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtQmlCompiler:QQmlSA.PassManager'),
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

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'QQmlSA::LintPlugin::LintPlugin()', which
    is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qqmlsa-lintplugin.html#LintPlugin
    """
    #  QQmlSA::LintPlugin::LintPlugin()
    self._noteCreation(LintPlugin, lambda: Rituals.call(
        'ritual_ZN6QQmlSA10LintPluginC1Ev',
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

  @overload(WAIT['QQmlSA.PassManager'], WAIT['QQmlSA.Element'])
  @overload(NoneType, WAIT['QQmlSA.Element'])
  def registerPasses(
      self,
      manager: Optional[QQmlSA.PassManager],
      rootElement: QQmlSA.Element,
  ) -> None:
    """
    Calls Qt's 'void QQmlSA::LintPlugin::registerPasses(PassManager *manager,
    const Element &rootElement)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsa-lintplugin.html#registerPasses

    Parameters
    ----------

    manager : Optional[QQmlSA.PassManager]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    rootElement : QQmlSA.Element
      Passed on as a value: Qt reads the C++ QQmlSA::Element, which stays
      Python's own.
    """
    #  void QQmlSA::LintPlugin::registerPasses(PassManager *manager, const
    #      Element &rootElement)
    self.uglySide.call(
        'ritual_ZN6QQmlSA10LintPlugin14registerPassesEPNS_11PassManagerERKN'
        'S_7ElementE',
        self._addressOf(manager), self._valueOf(rootElement),
    )
