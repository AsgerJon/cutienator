"""
QScxmlInvokableServicePrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtScxml/6.12.0/QtScxml/private/qscxmlinvokableservice_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QScxmlInvokableServicePrivate to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..QtCore import QObjectPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QScxmlStateMachine
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QScxmlStateMachine = WAIT['QScxmlStateMachine']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QScxmlInvokableServicePrivate(QObjectPrivate):
  """
  The cute side of Qt's QScxmlInvokableServicePrivate: a plain Python object
  standing in front of one C++ QScxmlInvokableServicePrivate.

  It is built on the cute 'QObjectPrivate', as Qt's
  QScxmlInvokableServicePrivate is built on Qt's QObjectPrivate, and has
  everything that class has.

  What exists
  -----------

  No function of Qt's QScxmlInvokableServicePrivate yet. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QString
    QScxmlInvokableServicePrivate::calculateId(QScxmlStateMachine *parent,
    const QScxmlExecutableContent::InvokeInfo &invokeInfo, bool *ok) const':
    takes a number to change where it is.
  - Qt's 'QVariantMap
    QScxmlInvokableServicePrivate::calculateData(QScxmlStateMachine *parent,
    const QList<QScxmlExecutableContent::ParameterInfo> &parameters, const
    QList<QScxmlExecutableContent::StringId> &names, bool *ok) const': takes
    a type Python has no way to hand over yet.

  What to expect
  --------------

  - The C++ QScxmlInvokableServicePrivate is created at the first use, not by
    'QScxmlInvokableServicePrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QScxmlInvokableServicePrivate.
  - Each name of Qt's QScxmlInvokableServicePrivate that has no cute function
    yet, 'calculateData', 'calculateId', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QScxmlInvokableServicePrivate'

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

  @overload(QScxmlStateMachine)
  @overload(NoneType)
  def __init__(
      self,
      parentStateMachine: Optional[QScxmlStateMachine],
  ) -> None:
    """
    Notes what was given, for Qt's
    'QScxmlInvokableServicePrivate::QScxmlInvokableServicePrivate(
    QScxmlStateMachine *parentStateMachine)', which is called at the first
    use.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmlinvokableserviceprivate.html

    Parameters
    ----------

    parentStateMachine : Optional[QScxmlStateMachine]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QScxmlInvokableServicePrivate::QScxmlInvokableServicePrivate(
    #      QScxmlStateMachine *parentStateMachine)
    self._noteCreation(QScxmlInvokableServicePrivate, lambda: Rituals.call(
        'ritual_ZN29QScxmlInvokableServicePrivateC1EP18QScxmlStateMachine',
        self._addressOf(parentStateMachine),
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
  def calculateData(*__, **_) -> Never:
    """
    Qt's 'QVariantMap
    QScxmlInvokableServicePrivate::calculateData(QScxmlStateMachine *parent,
    const QList<QScxmlExecutableContent::ParameterInfo> &parameters, const
    QList<QScxmlExecutableContent::StringId> &names, bool *ok) const': takes
    a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QScxmlInvokableServicePrivate.calculateData' has no cute function "
        "yet. Qt's 'QVariantMap "
        "QScxmlInvokableServicePrivate::calculateData(QScxmlStateMachine "
        "*parent, const QList<QScxmlExecutableContent::ParameterInfo> "
        "&parameters, const QList<QScxmlExecutableContent::StringId> "
        "&names, bool *ok) const': takes a type Python has no way to hand "
        "over yet.")

  @staticmethod
  def calculateId(*__, **_) -> Never:
    """
    Qt's 'QString
    QScxmlInvokableServicePrivate::calculateId(QScxmlStateMachine *parent,
    const QScxmlExecutableContent::InvokeInfo &invokeInfo, bool *ok) const':
    takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QScxmlInvokableServicePrivate.calculateId' has no cute function "
        "yet. Qt's 'QString "
        "QScxmlInvokableServicePrivate::calculateId(QScxmlStateMachine "
        "*parent, const QScxmlExecutableContent::InvokeInfo &invokeInfo, "
        "bool *ok) const': takes a number to change where it is.")
