"""
WaitingOverload is what a waiting signature leaves at a name in a class
body.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

from types import FunctionType
from typing import TYPE_CHECKING

from worktoy.waitaminute import MissingVariable, TypeException

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Any, Callable, Optional, Tuple


class WaitingOverload:
  """
  Holds one function of a class body together with a signature that
  names a late class, until the late class is made. See 'WAIT' for the
  whole story; this is step 3 and 4 of it.

  You never make one yourself. 'CuteOverload' makes it where worktoy's
  'overload' would have made its own record, and 'CuteSpace' takes it
  out of the class body as it is bound:

    QThread = WAIT['QThread']

    @overload(QThread)                       # 'CuteOverload' in a cute body
    def moveToThread(self, thread): ...      # the name is bound to a
                                             # 'WaitingOverload' here

  Terms
  -----

  - A signature entry is one thing between the brackets of
    '@overload(...)': a class, 'THIS', or a 'WAIT'.
  - A method kind is 'classmethod' or 'staticmethod'. A function with
    neither is an instance method.

  Provided by 'CuteOverload'
  --------------------------

  - 'setSignatureEntries': what stood between the brackets. Required.
  - 'setFunction': the function under the decorator. Required.
  - 'setMethodKinds': each '@classmethod' or '@staticmethod' written
    between the decorator and the function. Required, also when there
    is none.

  What to expect
  --------------

  - It only holds. It checks nothing about the signature and calls
    nothing.
  - It is no function and cannot be called. One left on a class would
    mean that a body other than a cute one used 'CuteOverload'.
  - 'CuteSpace' replaces the entries as late classes are made, through
    'setSignatureEntries', until no 'WAIT' is left among them.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables

  #  Fallback Variables

  #  Private Variables
  __signature_entries__: Optional[Tuple[Any, ...]] = None
  __waiting_function__: Optional[Callable] = None
  __method_kinds__: Optional[Tuple[Any, ...]] = None

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def getSignatureEntries(self) -> Tuple[Any, ...]:
    """
    Gives the entries of the waiting signature, in the order they were
    written: classes, 'THIS', and at least one 'WAIT' until the last
    late class among them is made.

    Provided through 'setSignatureEntries'.

    Raises
    ------

    MissingVariable
      'setSignatureEntries' has not been called.
    """
    if self.__signature_entries__ is None:
      raise MissingVariable(self, '__signature_entries__', tuple)
    return self.__signature_entries__

  def getFunction(self) -> Callable:
    """
    Gives the function the waiting signature belongs to, without any
    'classmethod' or 'staticmethod' around it.

    Provided through 'setFunction'.

    Raises
    ------

    MissingVariable
      'setFunction' has not been called.
    """
    if self.__waiting_function__ is None:
      raise MissingVariable(self, '__waiting_function__', FunctionType)
    return self.__waiting_function__

  def getMethodKinds(self) -> Tuple[Any, ...]:
    """
    Gives the method kinds written between the decorator and the
    function, outermost first. It is empty for an instance method.

    Provided through 'setMethodKinds'.

    Raises
    ------

    MissingVariable
      'setMethodKinds' has not been called.
    """
    if self.__method_kinds__ is None:
      raise MissingVariable(self, '__method_kinds__', tuple)
    return self.__method_kinds__

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def setSignatureEntries(self, *signatureEntries: Any) -> None:
    """
    Tells which entries the waiting signature has.

    Required. Calling it again replaces the entries, which is how
    'CuteSpace' puts a class in the place of its 'WAIT'.

    Parameters
    ----------

    *signatureEntries : Any
      One or more entries, in the order they were written.

    Raises
    ------

    ValueError
      Called with no entry at all. A signature without entries names no
      late class and has no reason to wait.
    """
    if not signatureEntries:
      infoSpec = """A waiting signature has at least one entry, and none
      was given."""
      raise ValueError(' '.join(infoSpec.split()))
    self.__signature_entries__ = (*signatureEntries,)

  def setFunction(self, function: Callable) -> None:
    """
    Tells which function the waiting signature belongs to.

    Required. Calling it again replaces the function given before.

    Parameters
    ----------

    function : Callable
      The function itself, taken out of any 'classmethod' or
      'staticmethod' around it.

    Raises
    ------

    TypeException
      'function' cannot be called.
    """
    if not callable(function):
      raise TypeException('function', function, FunctionType)
    self.__waiting_function__ = function

  def setMethodKinds(self, *methodKinds: Any) -> None:
    """
    Tells which method kinds were written between the decorator and the
    function.

    Required, also with nothing to give: no kind means an instance
    method. Calling it again replaces the kinds given before.

    Parameters
    ----------

    *methodKinds : Any
      Each 'classmethod' or 'staticmethod', outermost first.

    Raises
    ------

    TypeException
      An entry is neither 'classmethod' nor 'staticmethod'.
    """
    for methodKind in methodKinds:
      if methodKind is not classmethod and methodKind is not staticmethod:
        raise TypeException('methodKind', methodKind, type)
    self.__method_kinds__ = (*methodKinds,)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def __str__(self) -> str:
    """Says which function waits, and for which signature."""
    clsName = type(self).__name__
    if self.__waiting_function__ is None:
      return '<%s with no function yet>' % clsName
    name = getattr(self.__waiting_function__, '__name__', '?')
    entries = self.__signature_entries__ or ()
    shown = ', '.join(
        getattr(entry, '__name__', None) or str(entry) for entry in entries
    )
    return "<%s of '%s', waiting as (%s)>" % (clsName, name, shown)

  __repr__ = __str__

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
