"""
WaitingOverload is what a stack of '@overload' decorators leaves at a
name in a class body when one of its signatures names a late class.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

from types import FunctionType
from typing import TYPE_CHECKING

from worktoy.waitaminute import MissingVariable, TypeException

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Any, Callable, List, Optional, Tuple


class WaitingOverload:
  """
  Holds one function of a class body together with every signature its
  stack of '@overload' decorators gives it, when at least one of them
  names a late class. See 'WAIT' for the whole story; this is step 3
  of it.

  You never make one yourself. 'CuteOverload' makes it where worktoy's
  'overload' would have made its own record, and 'CuteSpace' takes it
  out of the class body as it is bound:

    @overload(QIcon, str)                    # names a late class
    @overload(str)                           # names none
    def setText(self, *args): ...            # the name is bound to a
                                             # 'WaitingOverload' here

  Terms
  -----

  - A signature entry is one thing between the brackets of
    '@overload(...)': a class, 'THIS', or a 'WAIT'.
  - A method kind is 'classmethod' or 'staticmethod'. A function with
    neither is an instance method.

  Provided by 'CuteOverload'
  --------------------------

  - 'setFunction': the function under the decorators. Required.
  - 'addSignature': what stood between the brackets of one decorator,
    once for each decorator of the stack, the lowest first.
  - 'addMethodKinds': each '@classmethod' or '@staticmethod' written
    in the stack.

  What to expect
  --------------

  - It only holds. It checks nothing about the signatures and calls
    nothing.
  - It is no function and cannot be called. One left on a class would
    mean that a body other than a cute one used 'CuteOverload'.
  - 'CuteSpace' puts each signature naming no late class on record at
    once, and keeps each of the others as a 'WaitingSignature'.
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
  __stacked_signatures__: Optional[List[Tuple[Any, ...]]] = None
  __waiting_function__: Optional[Callable] = None
  __method_kinds__: Optional[Tuple[Any, ...]] = None

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def getSignatures(self) -> Tuple[Tuple[Any, ...], ...]:
    """
    Gives the signatures of the stack, each as its entries, the one of
    the lowest decorator first. That is the order worktoy puts the
    signatures of a stack on record in.

    Provided through 'addSignature'. It is empty before the first call.
    """
    return (*(self.__stacked_signatures__ or ()),)

  def getFunction(self) -> Callable:
    """
    Gives the function the stack decorates, without any 'classmethod' or
    'staticmethod' around it.

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
    Gives the method kinds written in the stack, outermost first. It is
    empty for an instance method.
    """
    return self.__method_kinds__ or ()

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def addSignature(self, *signatureEntries: Any) -> None:
    """
    Adds the signature of one more decorator of the stack, above those
    added before. No entry at all is the signature of '@overload()'.

    Parameters
    ----------

    *signatureEntries : Any
      The entries, in the order they were written.
    """
    if self.__stacked_signatures__ is None:
      self.__stacked_signatures__ = []
    self.__stacked_signatures__.append((*signatureEntries,))

  def setFunction(self, function: Callable) -> None:
    """
    Tells which function the stack decorates. Required.

    Raises
    ------

    TypeException
      'function' cannot be called.
    """
    if not callable(function):
      raise TypeException('function', function, FunctionType)
    self.__waiting_function__ = function

  def addMethodKinds(self, *methodKinds: Any) -> None:
    """
    Adds method kinds written above those added before.

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
    self.__method_kinds__ = (*methodKinds, *self.getMethodKinds())

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def __str__(self) -> str:
    """Says which function waits, and for which signatures."""
    clsName = type(self).__name__
    if self.__waiting_function__ is None:
      return '<%s with no function yet>' % clsName
    name = getattr(self.__waiting_function__, '__name__', '?')
    shown = '; '.join(
        '(%s)' % ', '.join(
            getattr(entry, '__name__', None) or str(entry)
            for entry in entries
        ) for entries in self.getSignatures()
    )
    return "<%s of '%s', with %s>" % (clsName, name, shown)

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
