"""
QQmlSA::PropertyPassBuilder binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQmlCompiler/6.12.0/QtQmlCompiler/private/qqmlsa_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QQmlSA::PropertyPassBuilder to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from . import QQmlSA

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class PropertyPassBuilder(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQmlSA::PropertyPassBuilder: a plain Python object
  standing in front of one C++ QQmlSA::PropertyPassBuilder.

  What exists
  -----------

  Every function of Qt's QQmlSA::PropertyPassBuilder that has a ritual and
  that Python can call so far, 2 names in all: 'registerOn',
  'registerOnBuiltin'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QQmlSA::PropertyPassBuilder::~PropertyPassBuilder()': the
    destructor: Python never removes a C++ QQmlSA::PropertyPassBuilder.
  - Qt's 'PropertyPassBuilder
    &QQmlSA::PropertyPassBuilder::withOnBinding(GenericPropertyPass::
    OnBinding onBinding)': takes a type Python has no way to hand over yet.
  - Qt's 'PropertyPassBuilder
    &QQmlSA::PropertyPassBuilder::withOnRead(GenericPropertyPass::OnRead
    onRead)': takes a type Python has no way to hand over yet.
  - Qt's 'PropertyPassBuilder
    &QQmlSA::PropertyPassBuilder::withOnCall(GenericPropertyPass::OnCall
    onCall)': takes a type Python has no way to hand over yet.
  - Qt's 'PropertyPassBuilder
    &QQmlSA::PropertyPassBuilder::withOnWrite(GenericPropertyPass::OnWrite
    onWrite)': takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  5 of the 13 functions Qt declares: 5 forbidden.

  What to expect
  --------------

  - The C++ QQmlSA::PropertyPassBuilder is created at the first use, not by
    'QQmlSA::PropertyPassBuilder(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQmlSA::PropertyPassBuilder.
  - Each name of Qt's QQmlSA::PropertyPassBuilder that has no cute function
    yet, 'withOnBinding', 'withOnCall', 'withOnRead', 'withOnWrite', holds a
    function that raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlSA::PropertyPassBuilder'

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
  def __init__(self, passManager: Optional[QQmlSA.PassManager]) -> None:
    """
    Notes what was given, for Qt's
    'QQmlSA::PropertyPassBuilder::PropertyPassBuilder(PassManager
    *passManager)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsa-propertypassbuilder.html

    Parameters
    ----------

    passManager : Optional[QQmlSA.PassManager]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QQmlSA::PropertyPassBuilder::PropertyPassBuilder(PassManager
    #      *passManager)
    self._noteCreation(PropertyPassBuilder, lambda: Rituals.call(
        'ritual_ZN6QQmlSA19PropertyPassBuilderC1EPNS_11PassManagerE',
        self._addressOf(passManager),
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

  @overload(str, str, str)
  def registerOn(self, module: str, type: str, property: str) -> None:
    """
    Calls Qt's 'void QQmlSA::PropertyPassBuilder::registerOn(QAnyStringView
    module, QAnyStringView type, QAnyStringView property)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsa-propertypassbuilder.html#registerOn

    Parameters
    ----------

    module : str
      Passed on as it is: a QString is made of it for the call.

    type : str
      Passed on as it is: a QString is made of it for the call.

    property : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQmlSA::PropertyPassBuilder::registerOn(QAnyStringView module,
    #      QAnyStringView type, QAnyStringView property)
    self.uglySide.call(
        'ritual_ZN6QQmlSA19PropertyPassBuilder10registerOnE14QAnyStringView'
        'S1_S1_',
        module, type, property,
    )

  @overload(str, str)
  def registerOnBuiltin(self, type: str, property: str) -> None:
    """
    Calls Qt's 'void
    QQmlSA::PropertyPassBuilder::registerOnBuiltin(QAnyStringView type,
    QAnyStringView property)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsa-propertypassbuilder.html#registerOnBuiltin

    Parameters
    ----------

    type : str
      Passed on as it is: a QString is made of it for the call.

    property : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQmlSA::PropertyPassBuilder::registerOnBuiltin(QAnyStringView
    #      type, QAnyStringView property)
    self.uglySide.call(
        'ritual_ZN6QQmlSA19PropertyPassBuilder17registerOnBuiltinE14QAnyStr'
        'ingViewS1_',
        type, property,
    )

  @staticmethod
  def withOnBinding(*__, **_) -> Never:
    """
    Qt's 'PropertyPassBuilder
    &QQmlSA::PropertyPassBuilder::withOnBinding(GenericPropertyPass::
    OnBinding onBinding)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQmlSA.PropertyPassBuilder.withOnBinding' has no cute function "
        "yet. Qt's 'PropertyPassBuilder "
        "&QQmlSA::PropertyPassBuilder::withOnBinding(GenericPropertyPass::On"
        "Binding onBinding)': takes a type Python has no way to hand over "
        "yet.")

  @staticmethod
  def withOnCall(*__, **_) -> Never:
    """
    Qt's 'PropertyPassBuilder
    &QQmlSA::PropertyPassBuilder::withOnCall(GenericPropertyPass::OnCall
    onCall)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQmlSA.PropertyPassBuilder.withOnCall' has no cute function yet. "
        "Qt's 'PropertyPassBuilder "
        "&QQmlSA::PropertyPassBuilder::withOnCall(GenericPropertyPass::OnCal"
        "l onCall)': takes a type Python has no way to hand over yet.")

  @staticmethod
  def withOnRead(*__, **_) -> Never:
    """
    Qt's 'PropertyPassBuilder
    &QQmlSA::PropertyPassBuilder::withOnRead(GenericPropertyPass::OnRead
    onRead)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQmlSA.PropertyPassBuilder.withOnRead' has no cute function yet. "
        "Qt's 'PropertyPassBuilder "
        "&QQmlSA::PropertyPassBuilder::withOnRead(GenericPropertyPass::OnRea"
        "d onRead)': takes a type Python has no way to hand over yet.")

  @staticmethod
  def withOnWrite(*__, **_) -> Never:
    """
    Qt's 'PropertyPassBuilder
    &QQmlSA::PropertyPassBuilder::withOnWrite(GenericPropertyPass::OnWrite
    onWrite)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQmlSA.PropertyPassBuilder.withOnWrite' has no cute function yet. "
        "Qt's 'PropertyPassBuilder "
        "&QQmlSA::PropertyPassBuilder::withOnWrite(GenericPropertyPass::OnWr"
        "ite onWrite)': takes a type Python has no way to hand over yet.")
