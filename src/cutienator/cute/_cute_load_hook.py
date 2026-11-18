"""
CuteLoadHook builds the overloaded method of a name again, after its
class is made.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.mcls.space_hooks import LoadSpaceHook

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Any, Optional

  from worktoy.dispatch import Dispatcher


class CuteLoadHook(LoadSpaceHook):
  """
  Builds, for a class that exists already, the one object that stands at
  an overloaded name and picks the function for each call. worktoy
  calls that object a dispatcher. See 'WAIT' for the whole story; this
  is the last part of step 6.

  You never call it. 'MetaCute' does, when a late class is made:

    space = QObject.getNamespace()             # the 'CuteSpace' of QObject
    dispatcher = space.cuteLoadHook.buildAgain('moveToThread')

  Why it exists
  -------------

  worktoy builds the dispatcher of each overloaded name once, as the
  class is made, from the signatures on record in the namespace of the
  class and in the namespaces of the classes it is built on. A waiting
  signature is not on record then. When its late class is made,
  'CuteSpace' puts it on record, and the dispatcher has to be built
  once more from the full record, for the waiting class and for every
  class built on it so far, since each class has a dispatcher of its
  own.

  The building itself is worktoy's, in 'LoadSpaceHook'. This class is
  based on it only to reach that work from a class of our own.

  What to expect
  --------------

  - It takes no part while a class body runs or is made into a class.
    The hook 'loadSpaceHook' that 'CuteSpace' inherits from worktoy
    does all of that, unchanged. The three phases this class would
    otherwise run a second time do nothing here.
  - Once the class is made, it tells the namespace which class its
    body became; see 'newClassPhase'.
  - 'buildAgain' reads the record as it is at that moment. It gives a
    new dispatcher every time and puts it nowhere. 'MetaCute' places
    it on the class.
  - A dispatcher built again is the same as one built the first time
    from the same record: signatures in the order they were written,
    those of the class itself before those of the classes it is built
    on.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def setItemPhase(self, key: str, val: Any, old: Any = None, ) -> bool:
    """
    Does nothing, and claims nothing: 'loadSpaceHook' has already seen
    the binding, and 'CuteSpace' has already taken any waiting
    signature.
    """
    return False

  def delItemPhase(self, key: str, val: Any = None, ) -> bool:
    """Does nothing, and claims nothing: 'loadSpaceHook' has seen it."""
    return False

  def postCompilePhase(self, compiledSpace: dict) -> dict:
    """
    Changes nothing: 'loadSpaceHook' has just built every dispatcher of
    the class, and building them a second time here would only replace
    each with its like.
    """
    return compiledSpace

  def newClassPhase(self, cls: Any) -> Any:
    """
    Tells the namespace which class its body became, and hands the
    class back unchanged. worktoy calls this once the class is made.

    The doors of the class need it; see 'CuteSpace.setCuteClass'.
    """
    self.space.setCuteClass(cls)
    return cls

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def buildAgain(self, methodName: str) -> Optional[Dispatcher]:
    """
    Builds the dispatcher of one overloaded name from the record as it
    is now, for the class of the namespace this hook was read through.

    Parameters
    ----------

    methodName : str
      The overloaded name, as 'moveToThread'.

    Returns
    -------

    Optional[Dispatcher]
      A new dispatcher holding every signature on record for the name,
      of the class and of the classes it is built on. It is placed
      nowhere yet. None when nothing is on record for the name.
    """
    return self._buildDispatcher(methodName)
