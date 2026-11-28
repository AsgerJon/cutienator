"""
QDesignerTaskMenuExtension binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDesigner/taskmenu.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from ..cute import CuteMixin, MetaCute
from ..QtCore import QList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtGui import QAction


class QDesignerTaskMenuExtension(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QDesignerTaskMenuExtension: a plain Python object
  standing in front of one C++ QDesignerTaskMenuExtension.

  What exists
  -----------

  Every function of Qt's QDesignerTaskMenuExtension that has a ritual and
  that Python can call so far, 2 names in all: 'preferredEditAction',
  'taskActions'. None can be made from Python: one comes out of a function of
  another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QDesignerTaskMenuExtension::~QDesignerTaskMenuExtension()': the
    destructor: Python never removes a C++ QDesignerTaskMenuExtension.

  What has no ritual
  ------------------

  5 of the 8 functions Qt declares: 4 forbidden; 1 the class is abstract, so
  C++ cannot make one, and the C++ class of ours does not fill in every
  function it leaves open.

  What to expect
  --------------

  - The C++ QDesignerTaskMenuExtension is created at the first use, not by
    'QDesignerTaskMenuExtension(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QDesignerTaskMenuExtension.
  - Each name of Qt's QDesignerTaskMenuExtension that has no cute function
    yet, '__init__', holds a function that raises 'NotImplementedError', and
    its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QDesignerTaskMenuExtension'

  #  A C++ QDesignerTaskMenuExtension Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QDesignerTaskMenuExtension'

  #  The functions Qt calls itself that QDesignerTaskMenuExtension is the
  #  first to declare and that cannot be handed to Python yet, each as Qt
  #  declares it. A class of a program that writes one of them anew is
  #  refused, since Qt would never call what it wrote; see
  #  'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'taskActions': (
          'QList<QAction *> QDesignerTaskMenuExtension::taskActions() const',
      ),
  }

  #  The functions Qt calls itself that QDesignerTaskMenuExtension is the
  #  first to declare. A class of a program built on it can write one anew,
  #  and Qt then calls that. For each name: the key C++ knows the function
  #  by, what it gives, and what it takes.
  __virtual_functions__ = {
      'preferredEditAction': (
          ('_ZNK26QDesignerTaskMenuExtension19preferredEditActionEv',
           ('address', 'address', 'QtGui:QAction'),
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

  def preferredEditAction(self) -> Optional[QAction]:
    """
    Calls Qt's 'QAction *QDesignerTaskMenuExtension::preferredEditAction()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignertaskmenuextension.html

    Returns
    -------

    Optional[QAction]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAction *QDesignerTaskMenuExtension::preferredEditAction() const
    ritual = 'ritual_ZNK26QDesignerTaskMenuExtension19preferredEditActionEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK26QDesignerTaskMenuExtension19preferredEditActionE'
          'v')
    address = self._callAs('QDesignerTaskMenuExtension', ritual)
    from ..QtGui import QAction
    return QAction._cuteAt(address)

  def taskActions(self) -> QList[QAction]:
    """
    Calls Qt's 'QList<QAction *> QDesignerTaskMenuExtension::taskActions()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignertaskmenuextension.html#taskActions

    Returns
    -------

    QList[QAction]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QAction *> QDesignerTaskMenuExtension::taskActions() const
    address = self._callAs(
        'QDesignerTaskMenuExtension',
        'ritual_ZNK26QDesignerTaskMenuExtension11taskActionsEv',
    )
    from ..QtGui import QAction
    return QList[QAction]._cuteOwning(address)

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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'QDesignerTaskMenuExtension::QDesignerTaskMenuExtension()': the
    class is abstract, so C++ cannot make one, and the C++ class of ours does
    not fill in every function it leaves open.
    """
    raise NotImplementedError(
        "'QDesignerTaskMenuExtension.__init__' has no cute function yet. "
        "Qt's 'QDesignerTaskMenuExtension::QDesignerTaskMenuExtension()': "
        "the class is abstract, so C++ cannot make one, and the C++ class "
        "of ours does not fill in every function it leaves open.")

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
