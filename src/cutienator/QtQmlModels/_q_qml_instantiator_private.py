"""
QQmlInstantiatorPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQmlModels/6.12.0/QtQmlModels/private/qqmlinstantiator_p_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QQmlInstantiatorPrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObjectPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QObject
  from . import QQmlChangeSet, QQmlDelegateModelPointer, QQmlInstantiator
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QObject = WAIT['QObject']
  QQmlChangeSet = WAIT['QQmlChangeSet']
  QQmlDelegateModelPointer = WAIT['QQmlDelegateModelPointer']
  QQmlInstantiator = WAIT['QQmlInstantiator']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQmlInstantiatorPrivate(QObjectPrivate):
  """
  The cute side of Qt's QQmlInstantiatorPrivate: a plain Python object
  standing in front of one C++ QQmlInstantiatorPrivate.

  It is built on the cute 'QObjectPrivate', as Qt's QQmlInstantiatorPrivate
  is built on Qt's QObjectPrivate, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQmlInstantiatorPrivate that has a ritual and that
  Python can call so far, 9 names in all: 'q_func', 'clear', 'regenerate',
  '_q_createdItem', '_q_modelUpdated', 'modelObject', 'get', 'connectModel',
  'disconnectModel'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QQmlInstantiator *QQmlInstantiatorPrivate::q_func() const':
    takes in Python what 'QQmlInstantiator
    *QQmlInstantiatorPrivate::q_func()' takes.
  - Qt's 'const QQmlInstantiatorPrivate *QQmlInstantiatorPrivate::get(const
    QQmlInstantiator *instantiator)': takes in Python what
    'QQmlInstantiatorPrivate *QQmlInstantiatorPrivate::get(QQmlInstantiator
    *instantiator)' takes.

  What to expect
  --------------

  - The C++ QQmlInstantiatorPrivate is created at the first use, not by
    'QQmlInstantiatorPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQmlInstantiatorPrivate.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QQmlInstantiator)
  @overload(NoneType)
  def get(
      instantiator: Optional[QQmlInstantiator],
  ) -> Optional[QQmlInstantiatorPrivate]:
    """
    Calls Qt's 'QQmlInstantiatorPrivate
    *QQmlInstantiatorPrivate::get(QQmlInstantiator *instantiator)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlinstantiatorprivate.html#get

    Parameters
    ----------

    instantiator : Optional[QQmlInstantiator]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QQmlInstantiatorPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlInstantiatorPrivate *QQmlInstantiatorPrivate::get(QQmlInstantiator
    #      *instantiator)
    address = Rituals.call(
        'ritual_ZN23QQmlInstantiatorPrivate3getEP16QQmlInstantiator',
        CuteMixin._addressOf(instantiator),
    )
    return QQmlInstantiatorPrivate._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlInstantiatorPrivate'

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
    Notes what was given, for Qt's
    'QQmlInstantiatorPrivate::QQmlInstantiatorPrivate()', which is called at
    the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlinstantiatorprivate.html
    """
    #  QQmlInstantiatorPrivate::QQmlInstantiatorPrivate()
    self._noteCreation(QQmlInstantiatorPrivate, lambda: Rituals.call(
        'ritual_ZN23QQmlInstantiatorPrivateC1Ev',
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

  def q_func(self) -> Optional[QQmlInstantiator]:
    """
    Calls Qt's 'QQmlInstantiator *QQmlInstantiatorPrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlinstantiatorprivate.html#q_func

    Returns
    -------

    Optional[QQmlInstantiator]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlInstantiator *QQmlInstantiatorPrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN23QQmlInstantiatorPrivate6q_funcEv',
    )
    from . import QQmlInstantiator
    return QQmlInstantiator._cuteAt(address)

  def clear(self) -> None:
    """
    Calls Qt's 'void QQmlInstantiatorPrivate::clear()'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlinstantiatorprivate.html#clear
    """
    #  void QQmlInstantiatorPrivate::clear()
    self.uglySide.call('ritual_ZN23QQmlInstantiatorPrivate5clearEv')

  def regenerate(self) -> None:
    """
    Calls Qt's 'void QQmlInstantiatorPrivate::regenerate()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlinstantiatorprivate.html#regenerate
    """
    #  void QQmlInstantiatorPrivate::regenerate()
    self.uglySide.call('ritual_ZN23QQmlInstantiatorPrivate10regenerateEv')

  @overload(int, QObject)
  @overload(int, NoneType)
  def _q_createdItem(self, a0: int, a1: Optional[QObject]) -> None:
    """
    Calls Qt's 'void QQmlInstantiatorPrivate::_q_createdItem(int a0, QObject
    *a1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlinstantiatorprivate.html#_q_createdItem

    Parameters
    ----------

    a0 : int
      Passed on as it is.

    a1 : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlInstantiatorPrivate::_q_createdItem(int a0, QObject *a1)
    self.uglySide.call(
        'ritual_ZN23QQmlInstantiatorPrivate14_q_createdItemEiP7QObject',
        a0, self._addressOf(a1, 'QObject'),
    )

  @overload(QQmlChangeSet, bool)
  def _q_modelUpdated(self, a0: QQmlChangeSet, a1: bool) -> None:
    """
    Calls Qt's 'void QQmlInstantiatorPrivate::_q_modelUpdated(const
    QQmlChangeSet &a0, bool a1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlinstantiatorprivate.html#_q_modelUpdated

    Parameters
    ----------

    a0 : QQmlChangeSet
      Passed on as a value: Qt reads the C++ QQmlChangeSet, which stays
      Python's own.

    a1 : bool
      Passed on as it is.
    """
    #  void QQmlInstantiatorPrivate::_q_modelUpdated(const QQmlChangeSet &a0,
    #      bool a1)
    self.uglySide.call(
        'ritual_ZN23QQmlInstantiatorPrivate15_q_modelUpdatedERK13QQmlChange'
        'Setb',
        self._valueOf(a0), a1,
    )

  @overload(int, bool)
  def modelObject(self, index: int, async_: bool) -> Optional[QObject]:
    """
    Calls Qt's 'QObject *QQmlInstantiatorPrivate::modelObject(int index, bool
    async)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlinstantiatorprivate.html#modelObject

    Parameters
    ----------

    index : int
      Passed on as it is.

    async_ : bool
      Passed on as it is.

    Returns
    -------

    Optional[QObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QObject *QQmlInstantiatorPrivate::modelObject(int index, bool async)
    address = self.uglySide.call(
        'ritual_ZN23QQmlInstantiatorPrivate11modelObjectEib', index, async_,
    )
    from ..QtCore import QObject
    return QObject._cuteAt(address)

  @overload(QQmlInstantiator, QQmlDelegateModelPointer)
  @overload(QQmlInstantiator, NoneType)
  @overload(NoneType, QQmlDelegateModelPointer)
  @overload(NoneType, NoneType)
  def connectModel(
      self,
      q: Optional[QQmlInstantiator],
      model: Optional[QQmlDelegateModelPointer],
  ) -> None:
    """
    Calls Qt's 'void QQmlInstantiatorPrivate::connectModel(QQmlInstantiator
    *q, QQmlDelegateModelPointer *model)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlinstantiatorprivate.html#connectModel

    Parameters
    ----------

    q : Optional[QQmlInstantiator]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    model : Optional[QQmlDelegateModelPointer]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlInstantiatorPrivate::connectModel(QQmlInstantiator *q,
    #      QQmlDelegateModelPointer *model)
    self.uglySide.call(
        'ritual_ZN23QQmlInstantiatorPrivate12connectModelEP16QQmlInstantiat'
        'orP24QQmlDelegateModelPointer',
        self._addressOf(q), self._addressOf(model),
    )

  @overload(QQmlInstantiator, QQmlDelegateModelPointer)
  @overload(QQmlInstantiator, NoneType)
  @overload(NoneType, QQmlDelegateModelPointer)
  @overload(NoneType, NoneType)
  def disconnectModel(
      self,
      q: Optional[QQmlInstantiator],
      model: Optional[QQmlDelegateModelPointer],
  ) -> None:
    """
    Calls Qt's 'void
    QQmlInstantiatorPrivate::disconnectModel(QQmlInstantiator *q,
    QQmlDelegateModelPointer *model)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlinstantiatorprivate.html#disconnectModel

    Parameters
    ----------

    q : Optional[QQmlInstantiator]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    model : Optional[QQmlDelegateModelPointer]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlInstantiatorPrivate::disconnectModel(QQmlInstantiator *q,
    #      QQmlDelegateModelPointer *model)
    self.uglySide.call(
        'ritual_ZN23QQmlInstantiatorPrivate15disconnectModelEP16QQmlInstant'
        'iatorP24QQmlDelegateModelPointer',
        self._addressOf(q), self._addressOf(model),
    )
