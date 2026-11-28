"""
QAbstractExtensionManager binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDesigner/extension.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QObject
  from . import QAbstractExtensionFactory
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QAbstractExtensionFactory = WAIT['QAbstractExtensionFactory']
  QObject = WAIT['QObject']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QAbstractExtensionManager(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QAbstractExtensionManager: a plain Python object
  standing in front of one C++ QAbstractExtensionManager.

  What exists
  -----------

  Every function of Qt's QAbstractExtensionManager that has a ritual and that
  Python can call so far, 3 names in all: 'registerExtensions',
  'unregisterExtensions', 'extension'. None can be made from Python: one
  comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QAbstractExtensionManager::~QAbstractExtensionManager()': the
    destructor: Python never removes a C++ QAbstractExtensionManager.

  What to expect
  --------------

  - The C++ QAbstractExtensionManager is created at the first use, not by
    'QAbstractExtensionManager(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QAbstractExtensionManager.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QAbstractExtensionManager'

  #  A C++ QAbstractExtensionManager Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QAbstractExtensionManager'

  #  The functions Qt calls itself that QAbstractExtensionManager is the
  #  first to declare. A class of a program built on it can write one anew,
  #  and Qt then calls that. For each name: the key C++ knows the function
  #  by, what it gives, and what it takes.
  __virtual_functions__ = {
      'registerExtensions': (
          ('_ZN25QAbstractExtensionManager18registerExtensionsEP25QAbstract'
           'ExtensionFactoryRK7QString',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address',
                'QtDesigner:QAbstractExtensionFactory'),
               ('address', 'text', ''),
           )),
      ),
      'unregisterExtensions': (
          ('_ZN25QAbstractExtensionManager20unregisterExtensionsEP25QAbstra'
           'ctExtensionFactoryRK7QString',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address',
                'QtDesigner:QAbstractExtensionFactory'),
               ('address', 'text', ''),
           )),
      ),
      'extension': (
          ('_ZNK25QAbstractExtensionManager9extensionEP7QObjectRK7QString',
           ('address', 'address', 'QtCore:QObject'),
           (
               ('address', 'address', 'QtCore:QObject'),
               ('address', 'text', ''),
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

  @overload(QObject, str)
  @overload(NoneType, str)
  def extension(
      self,
      object: Optional[QObject],
      iid: str,
  ) -> Optional[QObject]:
    """
    Calls Qt's 'QObject *QAbstractExtensionManager::extension(QObject
    *object, const QString &iid) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractextensionmanager.html#extension

    Parameters
    ----------

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    iid : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    Optional[QObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QObject *QAbstractExtensionManager::extension(QObject *object, const
    #      QString &iid) const
    address = self._callAs(
        'QAbstractExtensionManager',
        'ritual_ZNK25QAbstractExtensionManager9extensionEP7QObjectRK7QStrin'
        'g',
        self._addressOf(object, 'QObject'), iid,
    )
    from ..QtCore import QObject
    return QObject._cuteAt(address)

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

  @overload(QAbstractExtensionFactory, str)
  @overload(NoneType, str)
  def registerExtensions(
      self,
      factory: Optional[QAbstractExtensionFactory],
      iid: str,
  ) -> None:
    """
    Calls Qt's 'void
    QAbstractExtensionManager::registerExtensions(QAbstractExtensionFactory
    *factory, const QString &iid)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractextensionmanager.html#registerExtensions

    Parameters
    ----------

    factory : Optional[QAbstractExtensionFactory]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    iid : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QAbstractExtensionManager::registerExtensions(
    #      QAbstractExtensionFactory *factory, const QString &iid)
    self._callAs(
        'QAbstractExtensionManager',
        'ritual_ZN25QAbstractExtensionManager18registerExtensionsEP25QAbstr'
        'actExtensionFactoryRK7QString',
        self._addressOf(factory, 'QAbstractExtensionFactory'), iid,
    )

  @overload(QAbstractExtensionFactory, str)
  @overload(NoneType, str)
  def unregisterExtensions(
      self,
      factory: Optional[QAbstractExtensionFactory],
      iid: str,
  ) -> None:
    """
    Calls Qt's 'void
    QAbstractExtensionManager::unregisterExtensions(QAbstractExtensionFactory
    *factory, const QString &iid)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractextensionmanager.html

    Parameters
    ----------

    factory : Optional[QAbstractExtensionFactory]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    iid : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QAbstractExtensionManager::unregisterExtensions(
    #      QAbstractExtensionFactory *factory, const QString &iid)
    self._callAs(
        'QAbstractExtensionManager',
        'ritual_ZN25QAbstractExtensionManager20unregisterExtensionsEP25QAbs'
        'tractExtensionFactoryRK7QString',
        self._addressOf(factory, 'QAbstractExtensionFactory'), iid,
    )
