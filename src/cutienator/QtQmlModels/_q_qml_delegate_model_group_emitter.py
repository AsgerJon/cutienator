"""
QQmlDelegateModelGroupEmitter binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQmlModels/6.12.0/QtQmlModels/private/qqmldelegatemodel_p_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QQmlDelegateModelGroupEmitter to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QQmlChangeSet, QQuickPackage
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQmlChangeSet = WAIT['QQmlChangeSet']
  QQuickPackage = WAIT['QQuickPackage']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQmlDelegateModelGroupEmitter(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQmlDelegateModelGroupEmitter: a plain Python object
  standing in front of one C++ QQmlDelegateModelGroupEmitter.

  What exists
  -----------

  Every function of Qt's QQmlDelegateModelGroupEmitter that has a ritual and
  that Python can call so far, 4 names in all: 'emitModelUpdated',
  'createdPackage', 'initPackage', 'destroyingPackage'. None can be made from
  Python: one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QQmlDelegateModelGroupEmitter::~QQmlDelegateModelGroupEmitter()':
    the destructor: Python never removes a C++ QQmlDelegateModelGroupEmitter.

  What to expect
  --------------

  - The C++ QQmlDelegateModelGroupEmitter is created at the first use, not by
    'QQmlDelegateModelGroupEmitter(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQmlDelegateModelGroupEmitter.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlDelegateModelGroupEmitter'

  #  A C++ QQmlDelegateModelGroupEmitter Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQmlDelegateModelGroupEmitter'

  #  The functions Qt calls itself that QQmlDelegateModelGroupEmitter is the
  #  first to declare. A class of a program built on it can write one anew,
  #  and Qt then calls that. For each name: the key C++ knows the function
  #  by, what it gives, and what it takes.
  __virtual_functions__ = {
      'emitModelUpdated': (
          ('_ZN29QQmlDelegateModelGroupEmitter16emitModelUpdatedERK13QQmlCh'
           'angeSetb',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtQmlModels:QQmlChangeSet'),
               ('bool', 'number', ''),
           )),
      ),
      'createdPackage': (
          ('_ZN29QQmlDelegateModelGroupEmitter14createdPackageEiP13QQuickPa'
           'ckage',
           ('nothing', 'nothing', ''),
           (
               ('int', 'number', ''),
               ('address', 'address', 'QtQmlModels:QQuickPackage'),
           )),
      ),
      'initPackage': (
          ('_ZN29QQmlDelegateModelGroupEmitter11initPackageEiP13QQuickPacka'
           'ge',
           ('nothing', 'nothing', ''),
           (
               ('int', 'number', ''),
               ('address', 'address', 'QtQmlModels:QQuickPackage'),
           )),
      ),
      'destroyingPackage': (
          ('_ZN29QQmlDelegateModelGroupEmitter17destroyingPackageEP13QQuick'
           'Package',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtQmlModels:QQuickPackage'),
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

  @overload(QQmlChangeSet, bool)
  def emitModelUpdated(self, changeSet: QQmlChangeSet, reset: bool) -> None:
    """
    Calls Qt's 'void QQmlDelegateModelGroupEmitter::emitModelUpdated(const
    QQmlChangeSet &changeSet, bool reset)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmldelegatemodelgroupemitter.html

    Parameters
    ----------

    changeSet : QQmlChangeSet
      Passed on as a value: Qt reads the C++ QQmlChangeSet, which stays
      Python's own.

    reset : bool
      Passed on as it is.
    """
    #  void QQmlDelegateModelGroupEmitter::emitModelUpdated(const
    #      QQmlChangeSet &changeSet, bool reset)
    self._callAs(
        'QQmlDelegateModelGroupEmitter',
        'ritual_ZN29QQmlDelegateModelGroupEmitter16emitModelUpdatedERK13QQm'
        'lChangeSetb',
        self._valueOf(changeSet), reset,
    )

  @overload(int, QQuickPackage)
  @overload(int, NoneType)
  def createdPackage(self, a0: int, a1: Optional[QQuickPackage]) -> None:
    """
    Calls Qt's 'void QQmlDelegateModelGroupEmitter::createdPackage(int a0,
    QQuickPackage *a1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmldelegatemodelgroupemitter.html#createdPackage

    Parameters
    ----------

    a0 : int
      Passed on as it is.

    a1 : Optional[QQuickPackage]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlDelegateModelGroupEmitter::createdPackage(int a0,
    #      QQuickPackage *a1)
    ritual = (
        'ritual_ZN29QQmlDelegateModelGroupEmitter14createdPackageEiP13QQuic'
        'kPackage')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN29QQmlDelegateModelGroupEmitter14createdPackageEiP1'
          '3QQuickPackage')
    self._callAs(
        'QQmlDelegateModelGroupEmitter', ritual, a0, self._addressOf(a1),
    )

  @overload(int, QQuickPackage)
  @overload(int, NoneType)
  def initPackage(self, a0: int, a1: Optional[QQuickPackage]) -> None:
    """
    Calls Qt's 'void QQmlDelegateModelGroupEmitter::initPackage(int a0,
    QQuickPackage *a1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmldelegatemodelgroupemitter.html#initPackage

    Parameters
    ----------

    a0 : int
      Passed on as it is.

    a1 : Optional[QQuickPackage]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlDelegateModelGroupEmitter::initPackage(int a0, QQuickPackage
    #      *a1)
    ritual = (
        'ritual_ZN29QQmlDelegateModelGroupEmitter11initPackageEiP13QQuickPa'
        'ckage')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN29QQmlDelegateModelGroupEmitter11initPackageEiP13QQ'
          'uickPackage')
    self._callAs(
        'QQmlDelegateModelGroupEmitter', ritual, a0, self._addressOf(a1),
    )

  @overload(QQuickPackage)
  @overload(NoneType)
  def destroyingPackage(self, a0: Optional[QQuickPackage]) -> None:
    """
    Calls Qt's 'void
    QQmlDelegateModelGroupEmitter::destroyingPackage(QQuickPackage *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmldelegatemodelgroupemitter.html

    Parameters
    ----------

    a0 : Optional[QQuickPackage]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlDelegateModelGroupEmitter::destroyingPackage(QQuickPackage
    #      *a0)
    ritual = (
        'ritual_ZN29QQmlDelegateModelGroupEmitter17destroyingPackageEP13QQu'
        'ickPackage')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN29QQmlDelegateModelGroupEmitter17destroyingPackageE'
          'P13QQuickPackage')
    self._callAs(
        'QQmlDelegateModelGroupEmitter', ritual, self._addressOf(a0),
    )
