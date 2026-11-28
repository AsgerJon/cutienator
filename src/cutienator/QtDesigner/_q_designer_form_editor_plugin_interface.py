"""
QDesignerFormEditorPluginInterface binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDesigner/abstractformeditorplugin.h, Qt 6.12.0. Changes made here are
#  lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtGui import QAction
  from . import QDesignerFormEditorInterface
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDesignerFormEditorInterface = WAIT['QDesignerFormEditorInterface']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QDesignerFormEditorPluginInterface(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QDesignerFormEditorPluginInterface: a plain Python
  object standing in front of one C++ QDesignerFormEditorPluginInterface.

  What exists
  -----------

  Every function of Qt's QDesignerFormEditorPluginInterface that has a ritual
  and that Python can call so far, 4 names in all: 'isInitialized',
  'initialize', 'action', 'core'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's
    'QDesignerFormEditorPluginInterface::~QDesignerFormEditorPluginInterface(
    )': the destructor: Python never removes a C++
    QDesignerFormEditorPluginInterface.

  What has no ritual
  ------------------

  4 of the 10 functions Qt declares: 4 forbidden.

  What to expect
  --------------

  - The C++ QDesignerFormEditorPluginInterface is created at the first use,
    not by 'QDesignerFormEditorPluginInterface(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QDesignerFormEditorPluginInterface.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QDesignerFormEditorPluginInterface'

  #  A C++ QDesignerFormEditorPluginInterface Python makes is of a C++ class
  #  of ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QDesignerFormEditorPluginInterface'

  #  The functions Qt calls itself that QDesignerFormEditorPluginInterface is
  #  the first to declare. A class of a program built on it can write one
  #  anew, and Qt then calls that. For each name: the key C++ knows the
  #  function by, what it gives, and what it takes.
  __virtual_functions__ = {
      'isInitialized': (
          ('_ZNK34QDesignerFormEditorPluginInterface13isInitializedEv',
           ('bool', 'number', ''),
           ()),
      ),
      'initialize': (
          ('_ZN34QDesignerFormEditorPluginInterface10initializeEP28QDesigne'
           'rFormEditorInterface',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address',
                'QtDesigner:QDesignerFormEditorInterface'),
           )),
      ),
      'action': (
          ('_ZNK34QDesignerFormEditorPluginInterface6actionEv',
           ('address', 'address', 'QtGui:QAction'),
           ()),
      ),
      'core': (
          ('_ZNK34QDesignerFormEditorPluginInterface4coreEv',
           ('address', 'address', 'QtDesigner:QDesignerFormEditorInterface'),
           ()),
      ),
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isInitialized(self) -> bool:
    """
    Calls Qt's 'bool QDesignerFormEditorPluginInterface::isInitialized()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerformeditorplugininterface.html
    """
    #  bool QDesignerFormEditorPluginInterface::isInitialized() const
    return self.uglySide.call(
        'ritual_ZNK34QDesignerFormEditorPluginInterface13isInitializedEv',
    )

  def action(self) -> Optional[QAction]:
    """
    Calls Qt's 'QAction *QDesignerFormEditorPluginInterface::action() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerformeditorplugininterface.html#action

    Returns
    -------

    Optional[QAction]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAction *QDesignerFormEditorPluginInterface::action() const
    address = self.uglySide.call(
        'ritual_ZNK34QDesignerFormEditorPluginInterface6actionEv',
    )
    from ..QtGui import QAction
    return QAction._cuteAt(address)

  def core(self) -> Optional[QDesignerFormEditorInterface]:
    """
    Calls Qt's 'QDesignerFormEditorInterface
    *QDesignerFormEditorPluginInterface::core() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerformeditorplugininterface.html#core

    Returns
    -------

    Optional[QDesignerFormEditorInterface]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QDesignerFormEditorInterface
    #      *QDesignerFormEditorPluginInterface::core() const
    address = self.uglySide.call(
        'ritual_ZNK34QDesignerFormEditorPluginInterface4coreEv',
    )
    from . import QDesignerFormEditorInterface
    return QDesignerFormEditorInterface._cuteAt(address)

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
    Notes what was given, for Qt's
    'QDesignerFormEditorPluginInterface::QDesignerFormEditorPluginInterface(
    )', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerformeditorplugininterface.html
    """
    #  QDesignerFormEditorPluginInterface::
    #      QDesignerFormEditorPluginInterface()
    self._noteCreation(
        QDesignerFormEditorPluginInterface, lambda: Rituals.call(
            'ritual_ZN34QDesignerFormEditorPluginInterfaceC1Ev',
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

  @overload(QDesignerFormEditorInterface)
  @overload(NoneType)
  def initialize(self, core: Optional[QDesignerFormEditorInterface]) -> None:
    """
    Calls Qt's 'void QDesignerFormEditorPluginInterface::initialize(
    QDesignerFormEditorInterface *core)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerformeditorplugininterface.html#initialize

    Parameters
    ----------

    core : Optional[QDesignerFormEditorInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QDesignerFormEditorPluginInterface::initialize(
    #      QDesignerFormEditorInterface *core)
    self.uglySide.call(
        'ritual_ZN34QDesignerFormEditorPluginInterface10initializeEP28QDesi'
        'gnerFormEditorInterface',
        self._addressOf(core),
    )
