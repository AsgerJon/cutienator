"""
CuteOverload is what a cute class body gets when it reads the name
'overload'.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload, TypeSig

from . import WAIT, WaitingOverload

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Any, Callable


class CuteOverload:
  """
  Does in a cute class body what worktoy's 'overload' does, and also
  takes a signature naming a late class. See 'WAIT' for the whole
  story; this is step 2 and 3 of it.

  You do not import it and you do not write its name. A cute class file
  imports worktoy's 'overload' as any worktoy class file does, and the
  body writes '@overload(...)'. When the body reads that name,
  'CuteSpace' hands it this class instead:

    from worktoy.dispatch import overload

    class QObject(CuteMixin, metaclass=MetaCute):

      QThread = WAIT['QThread']

      @overload(QThread)            # this class: 'QThread' is a 'WAIT'
      def moveToThread(self, thread: QThread) -> bool: ...

      @overload(int)                # this class, handing on to worktoy
      def startTimer(self, interval: int) -> int: ...

  Why it exists
  -------------

  worktoy's 'overload' checks its signature on the very line it is
  written on, and takes a class or 'THIS' and nothing else. A 'WAIT' is
  refused there, before any namespace or metaclass is asked. So the
  body must get another 'overload' to begin with, and the only one who
  can give it another is the namespace the body runs in.

  What one use of it does
  -----------------------

  - '@overload(int)', with classes and 'THIS' only: the very same as
    worktoy's 'overload(int)'. It is called right here, checks the
    signature on this line, and its decorator gets the function. The
    body ends up with worktoy's own record, as in any worktoy class.
  - '@overload(QThread)', with a 'WAIT' among the entries: worktoy's
    'overload' is not called. The entries that are no 'WAIT' are
    checked as worktoy checks them. The function is put in a
    'WaitingOverload' with the entries, and that is what the name is
    bound to. 'CuteSpace' takes it from there.
  - 'overload.fallback', 'overload.finalize' and 'overload.flex' are
    worktoy's own, reached through this class.

  What to expect
  --------------

  - A signature with nothing late in it behaves exactly as in a class
    that is not cute. Nothing is added to it and nothing is checked
    twice.
  - A waiting signature needs a function of its own. Putting it on a
    function together with other 'overload' decorators is refused with
    'TypeError' on the line of the decorator that meets the other one,
    whichever of the two is written on top.
  - 'overload.flex' with a 'WAIT' is refused with 'TypeError'.
  - '@classmethod' and '@staticmethod' may be written above the
    decorator or below it, as with worktoy's 'overload'.
  - It is never made into an object: calling it gives a decorator, as
    calling worktoy's 'overload' does.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def _refuseShared(decorated: Any, decoratorName: str) -> None:
    """
    Refuses a decorator that would share one function with a waiting
    signature.

    Parameters
    ----------

    decorated : Any
      What the decorator received, with any 'classmethod' or
      'staticmethod' already taken off.

    decoratorName : str
      The decorator as the body wrote it, as 'overload.fallback', for
      the message.

    Raises
    ------

    TypeError
      'decorated' is a 'WaitingOverload'.
    """
    if not isinstance(decorated, WaitingOverload):
      return
    infoSpec = """'%s' is written above a signature that names a class
    still waited for. Such a signature needs a function of its own:
    write the function a second time for the decorator above it."""
    raise TypeError(' '.join((infoSpec % decoratorName).split()))

  @staticmethod
  def fallback(function: Any) -> Any:
    """
    worktoy's 'overload.fallback', reached through the name 'overload'
    of a cute class body. See there for what it does.

    Raises
    ------

    TypeError
      It is written above a waiting signature on one function.
    """
    _, decorated = overload.peelMethodKinds(function)
    CuteOverload._refuseShared(decorated, 'overload.fallback')
    return overload.fallback(function)

  @staticmethod
  def finalize(function: Any) -> Any:
    """
    worktoy's 'overload.finalize', reached through the name 'overload'
    of a cute class body. See there for what it does.

    Raises
    ------

    TypeError
      It is written above a waiting signature on one function.
    """
    _, decorated = overload.peelMethodKinds(function)
    CuteOverload._refuseShared(decorated, 'overload.finalize')
    return overload.finalize(function)

  @staticmethod
  def flex(*signatureEntries: Any) -> Callable:
    """
    worktoy's 'overload.flex', reached through the name 'overload' of a
    cute class body. See there for what it does.

    Raises
    ------

    TypeError
      A 'WAIT' is among the entries, or it is written above a waiting
      signature on one function.
    """
    for entry in signatureEntries:
      if isinstance(entry, WAIT):
        infoSpec = """'overload.flex' cannot take %s: a class still
        waited for can only stand in a plain '@overload(...)'."""
        raise TypeError(' '.join((infoSpec % entry).split()))
    flexDecorator = overload.flex(*signatureEntries)

    def decorator(function: Any) -> Any:
      _, decorated = overload.peelMethodKinds(function)
      CuteOverload._refuseShared(decorated, 'overload.flex')
      return flexDecorator(function)

    return decorator

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables

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

  def __new__(cls, *signatureEntries: Any) -> Callable:
    """
    Takes what stands between the brackets of '@overload(...)' in a
    cute class body, and gives the decorator for the function below.

    Parameters
    ----------

    *signatureEntries : Any
      The classes of the arguments after 'self', as for worktoy's
      'overload'. An entry may also be a 'WAIT' bound higher up in the
      same body.

    Returns
    -------

    Callable
      A decorator. Without a 'WAIT' among the entries it gives what
      worktoy's own decorator gives. With one, it gives a
      'WaitingOverload' holding the entries, the function, and any
      'classmethod' or 'staticmethod' found around the function.

    Raises
    ------

    TypeException, TypeError, UncheckableType
      An entry is no class, as worktoy's 'overload' refuses it. Raised
      on this line.
    """
    waits = [e for e in signatureEntries if isinstance(e, WAIT)]
    if waits:
      rest = [e for e in signatureEntries if not isinstance(e, WAIT)]
      TypeSig.validateTypes(*rest, variadic=False)
      plainDecorator = None
    else:
      plainDecorator = overload(*signatureEntries)

    def decorator(function: Any) -> Any:
      """Decorates the function below one '@overload(...)' line."""
      methodKinds, decorated = overload.peelMethodKinds(function)
      cls._refuseShared(decorated, 'overload')
      if plainDecorator is not None:
        return plainDecorator(function)
      if isinstance(decorated, overload):
        infoSpec = """The signature naming %s is written above another
        'overload' decorator. A signature naming a class still waited
        for needs a function of its own: write the function once more
        for it."""
        raise TypeError(' '.join((infoSpec % waits[0]).split()))
      waitingOverload = WaitingOverload()
      waitingOverload.setSignatureEntries(*signatureEntries)
      waitingOverload.setFunction(decorated)
      waitingOverload.setMethodKinds(*methodKinds)
      return waitingOverload

    return decorator

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
