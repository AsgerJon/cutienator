"""
QmlIR::Signal binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qqmlirbuilder_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QmlIR::Signal to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..QtCore import QStringList
from . import QV4

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class Signal(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QmlIR::Signal: a plain Python object standing in
  front of one C++ QmlIR::Signal.

  C++ hands a QmlIR::Signal around as a copy, so every C++ QmlIR::Signal
  behind a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QmlIR::Signal that has a ritual and that Python can
  call so far, 2 names in all: 'parameterStringList', 'parameterCount'. None
  can be made from Python: one comes out of a function of another class that
  gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QmlIR::Signal::~Signal()': the destructor: Python removes its C++
    QmlIR::Signal by it, and has no other use for it.

  What has no ritual
  ------------------

  2 of the 5 functions Qt declares: 2 the compiler refuses its ritual as it
  would be written here.

  What to expect
  --------------

  - The C++ QmlIR::Signal is created at the first use, not by
    'QmlIR::Signal(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QmlIR::Signal back gives a copy the ritual made for
    Python, in a new cute QmlIR::Signal.
  - Each name of Qt's QmlIR::Signal that has no cute function yet,
    'parametersBegin', 'parametersEnd', holds a function that raises
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
  __qt_class__ = 'QmlIR::Signal'

  #  Qt's '~QmlIR::Signal()'. Naming it makes this a value class: Python owns
  #  every C++ QmlIR::Signal behind a cute one, and removes it by this
  #  ritual.
  __delete_ritual__ = 'ritual_ZN5QmlIR6SignalD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(WAIT['QV4.Compiler.StringTableGenerator'])
  @overload(NoneType)
  def parameterStringList(
      self,
      stringPool: Optional[QV4.Compiler.StringTableGenerator],
  ) -> QStringList:
    """
    Calls Qt's 'QStringList QmlIR::Signal::parameterStringList(const
    QV4::Compiler::StringTableGenerator *stringPool) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmlir-signal.html#parameterStringList

    Parameters
    ----------

    stringPool : Optional[QV4.Compiler.StringTableGenerator]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QmlIR::Signal::parameterStringList(const
    #      QV4::Compiler::StringTableGenerator *stringPool) const
    address = self.uglySide.call(
        'ritual_ZNK5QmlIR6Signal19parameterStringListEPKN3QV48Compiler20Str'
        'ingTableGeneratorE',
        self._addressOf(stringPool),
    )
    return QStringList._cuteOwning(address)

  def parameterCount(self) -> int:
    """
    Calls Qt's 'int QmlIR::Signal::parameterCount() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmlir-signal.html#parameterCount
    """
    #  int QmlIR::Signal::parameterCount() const
    return self.uglySide.call('ritual_ZNK5QmlIR6Signal14parameterCountEv')

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

  @staticmethod
  def parametersBegin(*__, **_) -> Never:
    """
    Qt's 'PoolList<Parameter>::Iterator QmlIR::Signal::parametersBegin()
    const': the compiler refuses its ritual as it would be written here: no
    template named 'PoolList'; did you mean 'QmlIR::PoolList'?.
    """
    raise NotImplementedError(
        "'QmlIR.Signal.parametersBegin' has no cute function yet. Qt's "
        "'PoolList<Parameter>::Iterator QmlIR::Signal::parametersBegin() "
        "const': the compiler refuses its ritual as it would be written "
        "here: no template named 'PoolList'; did you mean "
        "'QmlIR::PoolList'?.")

  @staticmethod
  def parametersEnd(*__, **_) -> Never:
    """
    Qt's 'PoolList<Parameter>::Iterator QmlIR::Signal::parametersEnd()
    const': the compiler refuses its ritual as it would be written here: no
    template named 'PoolList'; did you mean 'QmlIR::PoolList'?.
    """
    raise NotImplementedError(
        "'QmlIR.Signal.parametersEnd' has no cute function yet. Qt's "
        "'PoolList<Parameter>::Iterator QmlIR::Signal::parametersEnd() "
        "const': the compiler refuses its ritual as it would be written "
        "here: no template named 'PoolList'; did you mean "
        "'QmlIR::PoolList'?.")
