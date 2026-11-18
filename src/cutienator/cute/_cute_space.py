"""
CuteSpace is the namespace the body of a cute class runs in.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload, TypeSig
from worktoy.mcls import BaseSpace
from worktoy.mcls.space_hooks import LoadSpaceHook
from worktoy.waitaminute import TypeException
from worktoy.waitaminute.dispatch import DuplicateSignature
from worktoy.waitaminute.dispatch import DispatchException
from worktoy.waitaminute.meta import OverloadConflict, ReboundOverload

from . import DoorNumber, CuteFlags, CuteNum
from . import WAIT, WaitingOverload, CuteOverload, CuteLoadHook

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Any, Callable, Dict, List, Optional, Tuple

  WaitingItem = Tuple[str, WaitingOverload]


class CuteSpace(BaseSpace):
  """
  The namespace 'MetaCute' prepares for the body of every cute class.
  It is worktoy's 'BaseSpace' with one thing added: it keeps the
  signatures of the body that name a late class until that class is
  made. See 'WAIT' for the whole story; this is step 2, 4 and the
  middle of step 6.

  You never make one and seldom meet one. 'MetaCute.__prepare__' makes
  it, the class body runs in it, and it stays with the class:

    space = QObject.getNamespace()     # the 'CuteSpace' of 'QObject'
    space.getWaitingOverloads()        # what of its body still waits

  Terms
  -----

  - The body is the indented code under a class statement. Python runs
    it with a namespace taking every name it binds and answering every
    name it reads.
  - A late class, a waiting class and a waiting signature are as
    'WAIT' explains them.
  - A dispatcher is the one object worktoy puts at an overloaded name,
    which picks the function for each call.

  What it adds to 'BaseSpace'
  ---------------------------

  1. The body reads the name 'overload'. '__getitem__' answers with
     'CuteOverload', unless the body bound that name itself. Every
     read goes to 'BaseSpace' first, this one too, so the hooks of the
     namespace see each read as worktoy shows it to them.

     This is the one name the namespace answers for without the body
     having bound it. For every other name it raises 'KeyError', as
     'BaseSpace' does, and Python then looks in the file. A namespace
     that answers for names it does not hold hides what the file
     imported, so this stays the only one.

  2. The body binds a name to a 'WaitingOverload', which is what
     'CuteOverload' gives for a waiting signature. '__setitem__' takes
     it where worktoy takes an overload of its own. The hooks ahead of
     the one that gathers overloads are asked first, and they refuse
     what they refuse of any binding, as '__del__' or a misspelled
     dunder. Then it is kept in 'getWaitingOverloads' and is not
     stored in the class. Every other binding goes to 'BaseSpace' as
     it is.

     It cannot be left to the hook that gathers overloads. That hook
     would note a 'WaitingOverload' down as a plain definition of the
     name, and then refuse the next real '@overload' at that name.

  3. The place of every signature of a name is noted as it is written,
     waiting or not. When a late class is made, 'nameLateClass' puts
     each signature that waited for it back at its own place.

  What to expect
  --------------

  - A body with no 'WAIT' in it behaves exactly as in a 'BaseSpace'.
  - A waiting signature counts as an overload of its name from the
    line it is written on: a plain definition at that name is refused
    with 'OverloadConflict', and another kind of method at it with
    'MixedMethodKind', both on their own line.
  - A 'WAIT' written right into a signature, as
    '@overload(WAIT['QThread'])', is bound in the body for you, at the
    name of its late class, as the line 'QThread = WAIT['QThread']'
    would. Written twice, or beside that line, it is one and the same
    'WAIT'.
  - A signature naming the 'WAIT' of another class, as
    'QObject.QThread' in the body of a class built on 'QObject', is
    refused with 'TypeError' on that line: no class would settle it,
    and its method would be missing for ever. So is a body that deletes
    the name of a 'WAIT' it has named, as the class is made.
  - A waiting signature is refused wherever worktoy refuses an
    overload: at '__del__', at a misspelled dunder as '__setname__',
    and bound to a second name, as in '__radd__ = __add__'.
  - Two functions at one waiting signature are refused with
    'DuplicateSignature' on the line of the second, as worktoy refuses
    two functions at one signature.
  - At one of worktoy's class hooks, as '__class_call__', a waiting
    signature is written with '@classmethod' above '@overload'.
  - Until its late class is made, a waiting signature is in no
    dispatcher. A name whose every signature waits is not on the class
    at all until then.
  - worktoy matches the signatures of one class in the order they were
    written, so the more special one is written first. That order is
    kept across the wait: a signature put back lands where it was
    written, not at the end.

  The door
  --------

  A is A: a member of an enum of Qt is never a number. Qt still takes
  the number in many places, as 'data(index, int role)', and C++ lets
  a member be given there. So every overloaded name of a cute class
  gets a door: when no signature takes a call as it is written, each
  member of an enum or value of flags in it is swapped for its number,
  and the call is tried once more. A call that is taken as written
  never comes near the door. See 'collectFallback' and 'DoorNumber'.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def _isOneSignature(
      first: WaitingOverload,
      other: WaitingOverload,
  ) -> bool:
    """
    Says whether two waiting signatures will be one and the same
    signature once their late classes are made: the same entries in the
    same places, a 'WAIT' counting as the late class it stands for.

    Parameters
    ----------

    first : WaitingOverload
      One waiting signature.

    other : WaitingOverload
      Another, written at the same name.
    """
    firstEntries = first.getSignatureEntries()
    otherEntries = other.getSignatureEntries()
    if len(firstEntries) != len(otherEntries):
      return False
    for one, another in zip(firstEntries, otherEntries):
      if one is another:
        continue
      if isinstance(one, WAIT) and isinstance(another, WAIT):
        if one.getWaitingName() == another.getWaitingName():
          continue
      return False
    return True

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  Builds a dispatcher again after the class is made. It takes no part
  #  while the body runs; see 'CuteLoadHook'.
  cuteLoadHook = CuteLoadHook()

  #  Fallback Variables

  #  Private Variables
  #  The waiting signatures of this body that still wait, each with the
  #  name it was written at, in the order they were written.
  __waiting_overloads__: Optional[List[WaitingItem]] = None
  #  For each overloaded name of this body, everything written at it in
  #  order: a worktoy signature for one that is on record, the
  #  'WaitingOverload' itself for one that still waits.
  __declared_signatures__: Optional[Dict[str, List[Any]]] = None
  #  The class the body became, once it is made; see 'setCuteClass'.
  __cute_class__: Optional[type] = None

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def getCuteClass(self) -> type:
    """
    Gives the class the body of this namespace became.

    Raises
    ------

    RuntimeError
      The class is not made yet.
    """
    if self.__cute_class__ is None:
      infoSpec = """The class '%s' is not made yet, so its namespace has
      no class to give."""
      info = infoSpec % (self.getClassName(),)
      raise RuntimeError(' '.join(info.split()))
    return self.__cute_class__

  def _getWaitingList(self) -> List[WaitingItem]:
    """Gives the list behind 'getWaitingOverloads', making it if need be."""
    if self.__waiting_overloads__ is None:
      self.__waiting_overloads__ = []
    return self.__waiting_overloads__

  def getWaitingOverloads(self) -> Tuple[WaitingItem, ...]:
    """
    Gives the waiting signatures of this body that still wait, in the
    order they were written.

    Kept for you: '__setitem__' adds each one as the body binds it, and
    'nameLateClass' removes each one whose last late class is made.

    Returns
    -------

    Tuple[WaitingItem, ...]
      A 'Tuple[Tuple[str, WaitingOverload], ...]': the name the
      signature was written at, as 'moveToThread', and the
      'WaitingOverload' holding its entries and its function. It is
      empty for a body that waits for nothing, and again once every
      late class of the body is made.
    """
    return (*self._getWaitingList(),)

  def _getDeclaredSignatures(self, methodName: str) -> List[Any]:
    """
    Gives everything this body wrote at one overloaded name, in the
    order it was written: a worktoy signature for each one that is on
    record, and the 'WaitingOverload' itself for each one that still
    waits. The list is the one kept, so changing it changes the note.
    """
    if self.__declared_signatures__ is None:
      self.__declared_signatures__ = dict()
    return self.__declared_signatures__.setdefault(methodName, [])

  def keepRecords(self) -> Dict[str, Any]:
    """
    Gives a copy of everything 'nameLateClass' changes, for
    'restoreRecords' to put back.

    'MetaCute' calls this before it has a late class named here. When
    the late class cannot be named in every class that waits for it,
    each namespace that was changed is put back as it was.

    Returns
    -------

    Dict[str, Any]
      The signatures on record for each name, the waiting signatures
      with the entries of each, and the place of everything written.
      It is for 'restoreRecords' alone.
    """
    waitingList = self._getWaitingList()
    declared = self.__declared_signatures__ or dict()
    overloads = self.getOverloads()
    return dict(
        onRecord={name: [*pairs] for name, pairs in overloads.items()},
        waitingList=[*waitingList],
        entries=[(w, w.getSignatureEntries()) for _, w in waitingList],
        declared={name: [*written] for name, written in declared.items()},
    )

  def _findOwnWait(self, wait: WAIT) -> Optional[WAIT]:
    """
    Gives the 'WAIT' this body binds for the late class that 'wait'
    stands for: 'wait' itself when the body binds it, else another
    'WAIT' the body binds for the same late class, else None.
    """
    lateName = wait.getWaitingName()
    found = None
    for value in dict.values(self):
      if value is wait:
        return wait
      if found is None and isinstance(value, WAIT):
        if value.getWaitingName() == lateName:
          found = value
    return found

  def _createOwnWait(self, methodName: str, wait: WAIT) -> None:
    """
    Binds a 'WAIT' that a signature names and no line of the body binds,
    at the name of its late class, as the line
    'QThread = WAIT['QThread']' would.

    The name is bound through '__setitem__', as any line of the body
    binds one, so the hooks of worktoy see it as well.

    Parameters
    ----------

    methodName : str
      The name the signature is written at, for the messages.

    wait : WAIT
      The 'WAIT' the signature names.

    Raises
    ------

    TypeError
      'wait' is bound in the body of another class, which alone it is
      settled for, or the name of its late class is taken in this body
      already.
    """
    className = self.getClassName()
    lateName = wait.getWaitingName()
    owner = wait.getFieldOwner()
    if owner is not None:
      infoSpec = """'%s.%s' names a 'WAIT' bound in the body of '%s'. No
      class settles it for '%s', so the method would be missing for
      ever. Give the body of '%s' a line of its own, above the method:
      %s = %s"""
      info = infoSpec % (
          className, methodName, owner.__name__, className, className,
          lateName, wait,
      )
      raise TypeError(' '.join(info.split()))
    taken = dict.__contains__(self, lateName)
    if taken or lateName in self.getShadowSpace():
      infoSpec = """'%s.%s' names %s, which no line of the body of '%s'
      binds, and the name '%s' is taken there already, so it cannot be
      bound at that name for you. Bind it yourself at a name that is
      free, on a line above the method, and name that in the
      signature."""
      info = infoSpec % (className, methodName, wait, className, lateName)
      raise TypeError(' '.join(info.split()))
    self[lateName] = wait

  def _getOwnWait(self, methodName: str, wait: WAIT, **kwargs) -> WAIT:
    """
    Gives the 'WAIT' of this body that stands for the late class a
    signature names, binding one first when the body has none.

    A signature may name a 'WAIT' the body bound on a line of its own,
    or one written right into it, as '@overload(WAIT['QThread'])'.
    Either way it comes out as one 'WAIT' per late class, bound at a
    name of the body, which is what 'MetaCute' settles.

    Parameters
    ----------

    methodName : str
      The name the signature is written at, for the messages.

    wait : WAIT
      The 'WAIT' the signature names. The keyword is for the method's
      own use.

    Returns
    -------

    WAIT
      'wait' itself when the body binds it, or was just made to; else
      the 'WAIT' the body binds for the same late class.

    Raises
    ------

    TypeError
      As '_createOwnWait' raises it.
    """
    ownWait = self._findOwnWait(wait)
    if ownWait is None:
      if kwargs.get('_recursion', False):
        raise RecursionError
      self._createOwnWait(methodName, wait)
      return self._getOwnWait(methodName, wait, _recursion=True)
    return ownWait

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def setCuteClass(self, cuteClass: type) -> None:
    """
    Tells the namespace which class its body became. 'CuteLoadHook'
    calls this once, as the class is made. You never call it.

    The doors of the class need it: a door finds the dispatcher it
    belongs to on this class.

    Raises
    ------

    RuntimeError
      The namespace was told its class already.
    """
    if self.__cute_class__ is not None:
      infoSpec = """The namespace of '%s' was told its class already."""
      raise RuntimeError(infoSpec % (self.getClassName(),))
    self.__cute_class__ = cuteClass

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def __getitem__(self, key: str, **kwargs) -> Any:
    """
    Answers a name the class body reads. Python asks here first, and
    looks in the file only when this raises 'KeyError'.

    Every read goes to 'BaseSpace' first, which shows it to the hooks
    of the namespace. The name 'overload' is then answered with
    'CuteOverload' when the body did not bind that name itself. So
    '@overload(...)' in a cute body is always 'CuteOverload', whatever
    the file imported under the name, and that is what lets a
    signature name a 'WAIT'.

    Parameters
    ----------

    key : str
      The name read.

    Returns
    -------

    Any
      'CuteOverload' for 'overload', else what the body bound at the
      name.

    Raises
    ------

    KeyError
      The body never bound the name, and it is not 'overload'. Python
      then looks among the names of the file.

    HookException
      A hook of the namespace refused the read.
    """
    try:
      return BaseSpace.__getitem__(self, key, **kwargs)
    except KeyError:
      if key == 'overload':
        return CuteOverload
      raise

  def __setitem__(self, key: str, val: Any, **kwargs) -> None:
    """
    Takes a name the class body binds. Python calls this for every
    assignment, function and class statement of the body.

    A 'WaitingOverload', with or without a 'classmethod' or
    'staticmethod' around it, is taken where worktoy takes an overload
    of its own. The hooks ahead of the one that gathers overloads are
    asked first, in their order, and refuse what they refuse of any
    binding. A 'WAIT' the signature names that no line of the body
    binds is bound first, at the name of its late class. Then the
    'WaitingOverload' is kept in 'getWaitingOverloads' and goes no
    further: it is not stored in the class. Everything else goes to
    'BaseSpace' as it is, and the signatures worktoy puts on record
    for it are noted in the order of the body.

    Parameters
    ----------

    key : str
      The name bound.

    val : Any
      The value bound.

    Raises
    ------

    OverloadConflict
      A waiting signature is written at a name the body defined plainly
      before.

    ReboundOverload
      A waiting signature is bound a second time in the body, as in
      '__radd__ = __add__'.

    MixedMethodKind
      A waiting signature is written as another kind of method than the
      name has in this body already, or as both a classmethod and a
      staticmethod.

    DelException, QuestionableSyntax, UnboundClassHook, ReservedName
      A waiting signature is written at a name worktoy refuses, or
      refuses for what is bound there. They come from the hooks of
      worktoy, as for any binding.

    TypeError
      A waiting signature names a 'WAIT' bound in the body of another
      class, or one no line binds whose name is taken in this body; see
      '_createOwnWait'.

    DuplicateSignature
      A waiting signature is written at a name that already has the
      same waiting signature for another function. Once the late class
      is made the two would be one signature.
    """
    methodKinds, bound = overload.peelMethodKinds(val)
    if not isinstance(bound, WaitingOverload):
      before = len(self.getOverloads().get(key, []))
      BaseSpace.__setitem__(self, key, val, **kwargs)
      for signature, _ in self.getOverloads().get(key, [])[before:]:
        self._getDeclaredSignatures(key).append(signature)
      return
    className = self.getClassName()
    #  The body may read the name again further down, and deleting it is
    #  refused as for any overload: both go by this note of 'BaseSpace',
    #  which takes every binding before a hook is asked.
    shadowSpace = self.getShadowSpace()
    shadowSpace[key] = val
    self.__shadow_space__ = shadowSpace
    try:
      oldVal = dict.__getitem__(self, key)
    except KeyError:
      oldVal = None
    #  The hooks ahead of the one that gathers overloads screen the
    #  binding. One of them taking it for itself ends it here, as it
    #  ends an overload of worktoy's own.
    for hook in self.getHooks():
      if isinstance(hook, LoadSpaceHook):
        break
      if hook.setItemPhase(key, val, oldVal):
        return
    if key in self.getPlainNames():
      raise OverloadConflict(className, key, False)
    claimedName = self.getClaimedName(bound)
    if claimedName is not None:
      raise ReboundOverload(className, claimedName, key)
    methodKinds = (*methodKinds, *bound.getMethodKinds())
    methodKind = overload.agreeMethodKind(methodKinds, key, className)
    self.addMethodKind(key, methodKind)
    #  Every 'WAIT' the signature names becomes the one this body binds
    #  for that late class. One written right into the signature is bound
    #  here, by this very method.
    entries = []
    for entry in bound.getSignatureEntries():
      if isinstance(entry, WAIT):
        entry = self._getOwnWait(key, entry)
      entries.append(entry)
    bound.setSignatureEntries(*entries)
    #  Two functions at what will be one signature are refused here, on
    #  the line of the second, as worktoy refuses them for an overload
    #  of its own. One function written there twice is taken once.
    for heldName, held in self._getWaitingList():
      if heldName != key or not self._isOneSignature(held, bound):
        continue
      heldFunction, function = held.getFunction(), bound.getFunction()
      if heldFunction is function:
        return
      raise DuplicateSignature(held, heldFunction, function)
    self.addClaimedName(bound, key)
    self._getWaitingList().append((key, bound))
    self._getDeclaredSignatures(key).append(bound)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def _createDoor(self, methodName: str) -> Callable:
    """
    Makes the door of one overloaded name of the class: the function
    its dispatcher calls when no signature takes a call as written.

    Parameters
    ----------

    methodName : str
      The overloaded name, as 'data'.

    Returns
    -------

    Callable
      The door. It takes the call as it came: the object or class the
      method was called on first, or nothing before the arguments for
      a static method.
    """
    space = self

    def door(*args: Any, **kwargs: Any) -> Any:
      owner = space.getCuteClass()
      dispatcher = owner.__dict__[methodName]
      if dispatcher.getMethodKind() is staticmethod:
        receiver, given = owner, args
      else:
        receiver, given = args[0], args[1:]
      swapped, wasSwapped = [], False
      for arg in given:
        if isinstance(arg, (CuteNum, CuteFlags)):
          arg, wasSwapped = DoorNumber(arg.value), True
        swapped.append(arg)
      if not wasSwapped:
        raise DispatchException(dispatcher, given, kwargs)
      bound = dispatcher.__get__(None, owner)
      function = getattr(bound, '__func__', bound)
      try:
        return function(receiver, *swapped, **kwargs)
      except DispatchException as dispatchException:
        if dispatchException.dispatch is not dispatcher:
          raise
      #  The refusal names the call as it was written, members and all.
      raise DispatchException(dispatcher, given, kwargs)

    return door

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def hasOverloads(self, name: str) -> bool:
    """
    Says whether the body declared an overload at a name, a waiting
    signature counting as one.

    worktoy asks this when the body binds a plain value, and refuses
    the binding with 'OverloadConflict' when the answer is True. With
    the waiting signatures counted, a plain definition written after a
    waiting signature of the same name is refused as well, where it
    would otherwise take the name and leave the signature with nothing
    to come back to.

    Parameters
    ----------

    name : str
      The name asked about.
    """
    for methodName, _ in self._getWaitingList():
      if methodName == name:
        return True
    return BaseSpace.hasOverloads(self, name)

  def collectFallback(self, name: str) -> Optional[Callable]:
    """
    Gives the function the dispatcher of a name calls when no signature
    takes a call: the fallback the class or a class it is built on
    declares with '@overload.fallback', or else the door.

    worktoy asks this as it builds the dispatcher of a name. A name
    with no signature on record gets no door, since a door alone would
    put a dispatcher where the class has none.

    Parameters
    ----------

    name : str
      The overloaded name.

    Returns
    -------

    Optional[Callable]
      The declared fallback, or the door, or None for a name with
      nothing on record.
    """
    fallback = BaseSpace.collectFallback(self, name)
    if fallback is not None:
      return fallback
    registries = (
      self.collectOverloads(name),
      self.collectFlexes(name),
      self.collectVariadics(name),
    )
    if not any(registries):
      return None
    return self._createDoor(name)

  def postCompile(self, namespace: dict) -> dict:
    """
    Checks, as the body ends, that every 'WAIT' a waiting signature of
    the body names is still bound in it.

    worktoy calls this once, when the class is about to be made, after
    its hooks have built the dispatchers. A line binding a 'WAIT' for
    the same late class further down the body takes the place of the
    one a signature named. A body that deletes the name of a 'WAIT' it
    has named, or binds that name to something else, is refused: the
    class would hold no 'WAIT' to be settled, and the signature would
    wait for ever.

    Parameters
    ----------

    namespace : dict
      The dictionary the class is made from, as worktoy assembled it.

    Returns
    -------

    dict
      The same dictionary, unchanged.

    Raises
    ------

    TypeError
      A waiting signature names a 'WAIT' for a late class that the body
      binds no 'WAIT' for any more.
    """
    namespace = BaseSpace.postCompile(self, namespace)
    className = self.getClassName()
    for methodName, waitingOverload in self.getWaitingOverloads():
      entries = []
      for entry in waitingOverload.getSignatureEntries():
        if isinstance(entry, WAIT):
          ownWait = self._findOwnWait(entry)
          if ownWait is None:
            infoSpec = """'%s.%s' names %s, and the body of '%s' no
            longer binds it as it ends: its name was deleted or bound
            to something else. Nothing settles it, so the method would
            be missing for ever."""
            info = infoSpec % (className, methodName, entry, className)
            raise TypeError(' '.join(info.split()))
          entry = ownWait
        entries.append(entry)
      waitingOverload.setSignatureEntries(*entries)
    return namespace

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def restoreRecords(self, records: Dict[str, Any]) -> None:
    """
    Puts back what 'keepRecords' copied: the namespace has on record,
    and keeps waiting, exactly what it did when the copy was taken.

    Parameters
    ----------

    records : Dict[str, Any]
      What 'keepRecords' gave.
    """
    onRecord, declared = records['onRecord'], records['declared']
    self.__overload_map__ = {n: [*pairs] for n, pairs in onRecord.items()}
    self.__waiting_overloads__ = [*records['waitingList']]
    self.__declared_signatures__ = {n: [*w] for n, w in declared.items()}
    for waitingOverload, entries in records['entries']:
      waitingOverload.setSignatureEntries(*entries)

  def nameLateClass(self, wait: WAIT, lateClass: type) -> Tuple[str, ...]:
    """
    Tells the namespace that a late class its body waited for is made,
    and has it put the signatures that waited for it back on record.

    'MetaCute' calls this, once for each 'WAIT' of the waiting class
    that the new class settles. You never call it. In every waiting
    signature the 'WAIT' is replaced by the class. A signature with no
    'WAIT' left is put on record through 'BaseSpace.addOverload', at
    the place it was written in, and waits no more. One still naming
    another late class stays among 'getWaitingOverloads'.

    Nothing is built here. The dispatchers of the names given back are
    out of date from this moment on, and 'MetaCute' builds them again.

    It is all or nothing. When worktoy refuses one of the signatures,
    the namespace is put back as it was before the call.

    Parameters
    ----------

    wait : WAIT
      The 'WAIT' of this body that stood for the class.

    lateClass : type
      The class, now made.

    Returns
    -------

    Tuple[str, ...]
      The names that got a signature back, as 'moveToThread', each
      once, in the order their signatures were written. It is empty
      when no signature became complete.

    Raises
    ------

    TypeException
      'wait' is not a 'WAIT', or 'lateClass' is not a class.

    DuplicateSignature
      The signature put back equals one the body already declared at
      that name for another function. Nothing is changed then.
    """
    if not isinstance(wait, WAIT):
      raise TypeException('wait', wait, WAIT)
    if not isinstance(lateClass, type):
      raise TypeException('lateClass', lateClass, type)
    records = self.keepRecords()
    try:
      return self._nameLateClass(wait, lateClass)
    except BaseException:
      self.restoreRecords(records)
      raise

  def _nameLateClass(self, wait: WAIT, lateClass: type) -> Tuple[str, ...]:
    """
    Does the work of 'nameLateClass', which puts the namespace back as
    it was when this raises half way.
    """
    methodNames = []  # type: List[str]
    for waitingItem in self.getWaitingOverloads():
      methodName, waitingOverload = waitingItem
      entries = waitingOverload.getSignatureEntries()
      if not any(entry is wait for entry in entries):
        continue
      entries = (*(lateClass if e is wait else e for e in entries),)
      waitingOverload.setSignatureEntries(*entries)
      if any(isinstance(entry, WAIT) for entry in entries):
        continue
      self._getWaitingList().remove(waitingItem)
      signature = TypeSig(*entries)
      before = len(self.getOverloads().get(methodName, []))
      self.addOverload(methodName, signature, waitingOverload.getFunction())
      declared = self._getDeclaredSignatures(methodName)
      written = declared.index(waitingOverload)
      onRecord = self.getOverloads()[methodName]
      if len(onRecord) == before:
        #  worktoy had the same signature for the same function already,
        #  and took nothing new.
        del declared[written]
      else:
        #  'addOverload' put it last. It belongs before every signature
        #  that was written after it and is on record.
        place = sum(
            1 for earlier in declared[:written]
            if isinstance(earlier, TypeSig)
        )
        onRecord.insert(place, onRecord.pop())
        declared[written] = signature
      if methodName not in methodNames:
        methodNames.append(methodName)
    return (*methodNames,)
