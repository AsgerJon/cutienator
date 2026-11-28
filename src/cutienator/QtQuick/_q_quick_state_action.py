"""
QQuickStateAction binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquickstate_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QQuickStateAction to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QObject, QVariant
  from ..QtQml import QQmlProperty
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QObject = WAIT['QObject']
  QQmlProperty = WAIT['QQmlProperty']
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickStateAction(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQuickStateAction: a plain Python object standing in
  front of one C++ QQuickStateAction.

  C++ hands a QQuickStateAction around as a copy, so every C++
  QQuickStateAction behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QQuickStateAction that has a ritual and that Python
  can call so far, 1 name in all: 'deleteFromBinding'. It can be made from
  Python, in 3 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QQuickStateAction::~QQuickStateAction()': the destructor: Python
    removes its C++ QQuickStateAction by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QQuickStateAction is created at the first use, not by
    'QQuickStateAction(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QQuickStateAction back gives a copy the ritual made
    for Python, in a new cute QQuickStateAction.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickStateAction'

  #  Qt's '~QQuickStateAction()'. Naming it makes this a value class: Python
  #  owns every C++ QQuickStateAction behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN17QQuickStateActionD1Ev'

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
    Notes what was given, for Qt's 'QQuickStateAction::QQuickStateAction()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickstateaction.html#QQuickStateAction
    """
    #  QQuickStateAction::QQuickStateAction()
    self._noteCreation(QQuickStateAction, lambda: Rituals.call(
        'ritual_ZN17QQuickStateActionC1Ev',
    ))

  @overload(QObject, str, QVariant)
  @overload(NoneType, str, QVariant)
  def __init__(self, a0: Optional[QObject], a1: str, a2: QVariant) -> None:
    """
    Notes what was given, for Qt's
    'QQuickStateAction::QQuickStateAction(QObject *a0, const QString &a1,
    const QVariant &a2)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickstateaction.html#QQuickStateAction

    Parameters
    ----------

    a0 : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    a1 : str
      Passed on as it is: a QString is made of it for the call.

    a2 : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  QQuickStateAction::QQuickStateAction(QObject *a0, const QString &a1,
    #      const QVariant &a2)
    self._noteCreation(QQuickStateAction, lambda: Rituals.call(
        'ritual_ZN17QQuickStateActionC1EP7QObjectRK7QStringRK8QVariant',
        self._addressOf(a0, 'QObject'), a1, self._valueOf(a2),
    ))

  @overload(QObject, QQmlProperty, str, QVariant)
  @overload(NoneType, QQmlProperty, str, QVariant)
  def __init__(
      self,
      a0: Optional[QObject],
      property: QQmlProperty,
      a2: str,
      a3: QVariant,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QQuickStateAction::QQuickStateAction(QObject *a0, const QQmlProperty
    &property, const QString &a2, const QVariant &a3)', which is called at
    the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickstateaction.html#QQuickStateAction

    Parameters
    ----------

    a0 : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    property : QQmlProperty
      Passed on as a value: Qt reads the C++ QQmlProperty, which stays
      Python's own.

    a2 : str
      Passed on as it is: a QString is made of it for the call.

    a3 : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  QQuickStateAction::QQuickStateAction(QObject *a0, const QQmlProperty
    #      &property, const QString &a2, const QVariant &a3)
    self._noteCreation(QQuickStateAction, lambda: Rituals.call(
        'ritual_ZN17QQuickStateActionC1EP7QObjectRK12QQmlPropertyRK7QString'
        'RK8QVariant',
        self._addressOf(a0, 'QObject'), self._valueOf(property), a2,
        self._valueOf(a3),
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

  def deleteFromBinding(self) -> None:
    """
    Calls Qt's 'void QQuickStateAction::deleteFromBinding()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickstateaction.html#deleteFromBinding
    """
    #  void QQuickStateAction::deleteFromBinding()
    self.uglySide.call('ritual_ZN17QQuickStateAction17deleteFromBindingEv')


#  Qt's 'QList<QQuickStateAction>': the list of QQuickStateAction, which
#  'QList[QQuickStateAction]' gives. It is made here, so that there is one as
#  soon as there can be a QQuickStateAction. Qt has a name of its own for it.
QQuickStateActions = QList.createKind(
    QQuickStateAction, 'value',
    name='QQuickStateActions',
    make='ritual_list_make_QQuickStateAction',
    add='ritual_list_add_QQuickStateAction',
    size='ritual_list_size_QQuickStateAction',
    at='ritual_list_at_QQuickStateAction',
    drop='ritual_list_drop_QQuickStateAction',
)
