"""
QQuickStateOperation binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquickstate_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QQuickStateOperation to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QList, QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from . import QQuickState, QQuickStateAction, QQuickStateOperationPrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQuickState = WAIT['QQuickState']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickStateOperation(QObject):
  """
  The cute side of Qt's QQuickStateOperation: a plain Python object standing
  in front of one C++ QQuickStateOperation.

  It is built on the cute 'QObject', as Qt's QQuickStateOperation is built on
  Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickStateOperation that has a ritual and that
  Python can call so far, 6 names in all: 'metaObject', 'tr', 'actions',
  'state', 'setState', 'd_func'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickStateOperation::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QQuickStateOperation::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'void QQuickStateOperation::qt_qmlMarker_anonymous()': one of Qt's
    own inner workings.
  - Qt's 'QQuickStateOperation::QQuickStateOperation(QObjectPrivate &dd,
    QObject *parent)': takes a type Python has no way to hand over yet.
  - Qt's 'const QQuickStateOperationPrivate *QQuickStateOperation::d_func()
    const': takes in Python what 'QQuickStateOperationPrivate
    *QQuickStateOperation::d_func()' takes.

  What has no ritual
  ------------------

  4 of the 16 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QQuickStateOperation is created at the first use, not by
    'QQuickStateOperation(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickStateOperation.
  - Qt tells when it has removed the C++ QQuickStateOperation. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(str)
  @overload(NoneType)
  @overload(str, str)
  @overload(str, NoneType)
  @overload(NoneType, str)
  @overload(NoneType, NoneType)
  @overload(str, str, int)
  @overload(str, NoneType, int)
  @overload(NoneType, str, int)
  @overload(NoneType, NoneType, int)
  def tr(s: Optional[str], c: Optional[str] = None, n: int = -1) -> str:
    """
    Calls Qt's 'QString QQuickStateOperation::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickstateoperation.html#tr

    Parameters
    ----------

    s : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    c : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text. May
      be left out, as in Qt: it is then None.

    n : int
      Passed on as it is. May be left out, as in Qt: it is then -1.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuickStateOperation::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN20QQuickStateOperation2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickStateOperation'

  #  The functions Qt calls itself that QQuickStateOperation is the first to
  #  declare and that cannot be handed to Python yet, each as Qt declares it.
  #  A class of a program that writes one of them anew is refused, since Qt
  #  would never call what it wrote; see 'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'actions': (
          'ActionList QQuickStateOperation::actions()',
      ),
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickStateOperation::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickstateoperation.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickStateOperation::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK20QQuickStateOperation10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def state(self) -> Optional[QQuickState]:
    """
    Calls Qt's 'QQuickState *QQuickStateOperation::state() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickstateoperation.html#state

    Returns
    -------

    Optional[QQuickState]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickState *QQuickStateOperation::state() const
    address = self.uglySide.call('ritual_ZNK20QQuickStateOperation5stateEv')
    from . import QQuickState
    return QQuickState._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QQuickState)
  @overload(NoneType)
  def setState(self, state: Optional[QQuickState]) -> None:
    """
    Calls Qt's 'void QQuickStateOperation::setState(QQuickState *state)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickstateoperation.html#setState

    Parameters
    ----------

    state : Optional[QQuickState]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickStateOperation::setState(QQuickState *state)
    self.uglySide.call(
        'ritual_ZN20QQuickStateOperation8setStateEP11QQuickState',
        self._addressOf(state),
    )

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
  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's
    'QQuickStateOperation::QQuickStateOperation(QObject *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickstateoperation.html#QQuickStateOperation

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickStateOperation::QQuickStateOperation(QObject *parent)
    self._noteCreation(QQuickStateOperation, lambda: Rituals.call(
        'ritual_ZN20QQuickStateOperationC1EP7QObject',
        self._addressOf(parent, 'QObject'),
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

  def actions(self) -> QList[QQuickStateAction]:
    """
    Calls Qt's 'ActionList QQuickStateOperation::actions()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickstateoperation.html#actions

    Returns
    -------

    QList[QQuickStateAction]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  ActionList QQuickStateOperation::actions()
    address = self.uglySide.call('ritual_ZN20QQuickStateOperation7actionsEv')
    from . import QQuickStateAction
    return QList[QQuickStateAction]._cuteOwning(address)

  def d_func(self) -> Optional[QQuickStateOperationPrivate]:
    """
    Calls Qt's 'QQuickStateOperationPrivate *QQuickStateOperation::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickstateoperation.html#d_func

    Returns
    -------

    Optional[QQuickStateOperationPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickStateOperationPrivate *QQuickStateOperation::d_func()
    address = self.uglySide.call('ritual_ZN20QQuickStateOperation6d_funcEv')
    from . import QQuickStateOperationPrivate
    return QQuickStateOperationPrivate._cuteAt(address)
