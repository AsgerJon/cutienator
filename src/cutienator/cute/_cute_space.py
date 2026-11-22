"""
CuteSpace is the namespace the body of a cute class runs in.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

import threading
from typing import TYPE_CHECKING

from worktoy.dispatch import overload, TypeSig
from worktoy.mcls import BaseSpace
from worktoy.mcls.space_hooks import LoadSpaceHook
from worktoy.waitaminute import TypeException
from worktoy.waitaminute.dispatch import DuplicateSignature
from worktoy.waitaminute.dispatch import DispatchException
from worktoy.waitaminute.meta import OverloadConflict, ReboundOverload

from . import DoorNumber, CuteFlags, CuteNum
from . import WAIT, WaitingOverload, WaitingSignature
from . import CuteOverload, CuteLoadHook

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Any, Callable, Dict, List, Optional, Tuple

  WaitingItem = Tuple[str, WaitingSignature]

#  The doors a call is passing through right now, for each thread apart;
#  see 'CuteSpace._createDoor'.
_PASSING = threading.local()


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
    space.getWaitingSignatures()        # what of its body still waits

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
     'CuteOverload' gives for a stack of '@overload' decorators with a
     waiting signature among them. '__setitem__' takes it where worktoy
     takes an overload of its own. The hooks ahead of the one that
     gathers overloads are asked first, and they refuse what they
     refuse of any binding, as '__del__' or a misspelled dunder. Then
     each signature of the stack that names no late class is put on
     record, as worktoy would have put it, and each of the others is
     kept in 'getWaitingSignatures', as a 'WaitingSignature'. The
     'WaitingOverload' itself is not stored in the class. Every other
     binding goes to 'BaseSpace' as it is.

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
    with 'OverloadConflict', on its own line.
  - A name may hold a function called on the class beside functions
    called on an object, as worktoy allows it, waiting signatures
    included: 'file.exists()' beside 'QFile.exists(fileName)'. The
    kind of each function is put on record as worktoy records it. One
    function declared as both a classmethod and a staticmethod is
    refused with 'MixedMethodKind'.
  - A 'WAIT' written right into a signature, as
    '@overload(WAIT['QThread'])', is bound in the body for you, at the
    name of its late class, as the line 'QThread = WAIT['QThread']'
    would. Written twice, or beside that line, it is one and the same
    'WAIT'.
  - A 'WAIT' no class body binds yet, as one bound at the top of a
    file, is bound in the body of the first class that names it in a
    signature, and serves that class alone. The class files the dev
    tooling writes name their late classes that way.
  - A waiting signature may share its function with other
    '@overload(...)' signatures, waiting or not, in one stack of
    decorators. Those that do not wait work from the start, and each
    of the others comes back at the place it was written in.
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
    dispatcher. A name whose every signature waits is on the class all
    the same: it refuses every call with 'DispatchException' until
    then.
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

  The door does one thing more. When a late class is made, each name
  that got a signature back gets a new dispatcher, and a function read
  off an object before that still goes by the old one. Python reads
  the function before it works out what the call hands over, so in
  'mime.setData(name, mime.data(name))' the function is read first,
  'mime.data' then brings in QByteArray, and the call arrives at a
  function that still waits for it. So when the door is reached, the
  call is tried once more on the function as it is now, whether or
  not a member was swapped.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def _isOneSignature(
      first: WaitingSignature,
      other: WaitingSignature,
  ) -> bool:
    """
    Says whether two waiting signatures will be one and the same
    signature once their late classes are made: the same entries in the
    same places, a 'WAIT' counting as the late class it stands for.

    Parameters
    ----------

    first : WaitingSignature
      One waiting signature.

    other : WaitingSignature
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
  #  'WaitingSignature' itself for one that still waits.
  __declared_signatures__: Optional[Dict[str, List[Any]]] = None
  #  The class the body became, once it is made; see 'setCuteClass'.
  __cute_class__: Optional[type] = None
  #  For each overloaded name asked about so far, the namespaces of the
  #  classes this one inherits overloads of that name from; see
  #  '_getInheritedSpaces'.
  __inherited_spaces__: Optional[Dict[str, List[Any]]] = None
  #  The doors of each overloaded name asked about so far, each with the
  #  kind of method it is; see '_getDoors'.
  __doors__: Optional[Dict[str, List[Tuple[Callable, Any]]]] = None

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
    """Gives the list behind 'getWaitingSignatures', making it if need be."""
    if self.__waiting_overloads__ is None:
      self.__waiting_overloads__ = []
    return self.__waiting_overloads__

  def getWaitingSignatures(self) -> Tuple[WaitingItem, ...]:
    """
    Gives the waiting signatures of this body that still wait, in the
    order they were written.

    Kept for you: '__setitem__' adds each one as the body binds it, and
    'nameLateClass' removes each one whose last late class is made.

    Returns
    -------

    Tuple[WaitingItem, ...]
      A 'Tuple[Tuple[str, WaitingSignature], ...]': the name the
      signature was written at, as 'moveToThread', and the
      'WaitingSignature' holding its entries and its function. It is
      empty for a body that waits for nothing, and again once every
      late class of the body is made.
    """
    return (*self._getWaitingList(),)

  def _getDeclaredSignatures(self, methodName: str) -> List[Any]:
    """
    Gives everything this body wrote at one overloaded name, in the
    order it was written: a worktoy signature for each one that is on
    record, and the 'WaitingSignature' itself for each one that still
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
    binding. Then each signature of its stack is taken in the order it
    was written. A 'WAIT' it names that no line of the body binds is
    bound first, at the name of its late class. A signature naming no
    late class is put on record through 'addOverload'. One naming a
    late class is kept in 'getWaitingSignatures', as a
    'WaitingSignature'. The 'WaitingOverload' goes no further: it is
    not stored in the class. Everything else goes to 'BaseSpace' as it
    is, and the signatures worktoy puts on record for it are noted in
    the order of the body.

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
      A waiting signature is written as both a classmethod and a
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
      is made the two would be one signature. Or a signature of the
      stack that names no late class is on record at the name for
      another function already.
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
    function = bound.getFunction()
    self.addMethodKind(key, methodKind)
    #  worktoy builds the dispatchers of a name by the kind of each
    #  function, and takes a function with no kind on record for an
    #  ordinary method. So the kind is put on record here, as worktoy
    #  puts it for an overload of its own, before any signature.
    self.addFunctionKind(key, methodKind, function)
    #  Each signature of the stack is taken in the order it was written.
    #  One naming no late class goes on record at once, as worktoy would
    #  have put it. One naming a late class is kept until that class is
    #  made.
    for written in bound.getSignatures():
      #  Every 'WAIT' the signature names becomes the one this body
      #  binds for that late class. One no line of the body binds is
      #  bound here, by this very method.
      entries = []
      for entry in written:
        if isinstance(entry, WAIT):
          entry = self._getOwnWait(key, entry)
        entries.append(entry)
      if not any(isinstance(entry, WAIT) for entry in entries):
        before = len(self.getOverloads().get(key, []))
        self.addOverload(key, TypeSig(*entries), function)
        for signature, _ in self.getOverloads().get(key, [])[before:]:
          self._getDeclaredSignatures(key).append(signature)
        continue
      waiting = WaitingSignature()
      waiting.setSignatureEntries(*entries)
      waiting.setFunction(function)
      #  Two functions at what will be one signature are refused here,
      #  on the line of the second, as worktoy refuses them for an
      #  overload of its own. One function written there twice is taken
      #  once.
      for heldName, held in self._getWaitingList():
        if heldName != key or not self._isOneSignature(held, waiting):
          continue
        if held.getFunction() is function:
          break
        raise DuplicateSignature(held, held.getFunction(), function)
      else:
        self._getWaitingList().append((key, waiting))
        self._getDeclaredSignatures(key).append(waiting)
    self.addClaimedName(bound, key)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def _findDoorKinds(self, methodName: str) -> Tuple[Any, ...]:
    """
    Says which doors a name gets, each by the kind of method it is.
    worktoy builds the dispatchers of a name by the kind of each
    function, so a door has to have one.

    - A name of ordinary methods alone: one door, an ordinary method.
      It is handed the object first.
    - A name with a classmethod: one door, a classmethod. worktoy lets
      such a fallback stand alone, and hands it the class either way.
    - A name of staticmethods alone: one door, a staticmethod. One
      dispatcher serves such a name both ways.
    - A name of ordinary methods beside staticmethods, as
      'file.exists()' beside 'QFile.exists(fileName)': two doors.
      worktoy gives such a name one dispatcher for calls on an object
      and one for calls on the class, and lets it hold one fallback
      for each. The ordinary one stands in the first and is handed the
      object, the static one in the second.

    Returns
    -------

    Tuple[Any, ...]
      For each door 'classmethod', 'staticmethod', or None for an
      ordinary method.
    """
    kinds = [k for _, k in BaseSpace.collectFunctionKinds(self, methodName)]
    if all(kind is None for kind in kinds):
      return (None,)
    if any(kind is classmethod for kind in kinds):
      return (classmethod,)
    if any(kind is None for kind in kinds):
      return (None, staticmethod)
    return (staticmethod,)

  def _getDoors(self, methodName: str) -> List[Tuple[Callable, Any]]:
    """
    Gives the doors of one overloaded name of the class, making them at
    the first asking, each with its kind of method. A door is the
    function a dispatcher of the name calls when no signature takes a
    call as written. 'collectFallback' and 'collectFallbacks' hand them
    to worktoy, and 'collectFunctionKinds' tells worktoy their kinds.
    """
    if self.__doors__ is None:
      self.__doors__ = dict()
    try:
      return self.__doors__[methodName]
    except KeyError:
      doors = [
          (self._createDoor(methodName, doorKind), doorKind)
          for doorKind in self._findDoorKinds(methodName)
      ]
      self.__doors__[methodName] = doors
      return doors

  def _createDoor(self, methodName: str, doorKind: Any) -> Callable:
    """
    Makes the door of one overloaded name of the class.

    Parameters
    ----------

    methodName : str
      The overloaded name, as 'data'.

    doorKind : Any
      The kind of method the door is: 'classmethod', 'staticmethod', or
      None for an ordinary method.

    Returns
    -------

    Callable
      The door. It takes the call as worktoy hands it to a function of
      its kind: the object first for an ordinary method, the class
      first for a classmethod, and nothing before the arguments for a
      staticmethod.
    """
    space = self

    def door(*args: Any, **kwargs: Any) -> Any:
      owner = space.getCuteClass()
      dispatcher = owner.__dict__[methodName]
      if doorKind is staticmethod:
        receiver, given = owner, args
      else:
        receiver, given = args[0], args[1:]
      #  The dispatcher gives the function that takes the calls this door
      #  stands for: read through an object for the door that is an
      #  ordinary method, and through the class for the others. At a
      #  name with ordinary methods beside others those are two.
      if doorKind is None:
        bound = dispatcher.__get__(receiver, owner)
      else:
        bound = dispatcher.__get__(None, owner)
      function = getattr(bound, '__func__', bound)
      swapped, wasSwapped = [], False
      for arg in given:
        if isinstance(arg, (CuteNum, CuteFlags)):
          arg, wasSwapped = DoorNumber(arg.value), True
        swapped.append(arg)
      #  The call is tried once more on the function as it is now, with
      #  each member swapped. With nothing swapped it is still tried:
      #  the function that sent it here may have been read off its
      #  object before a class it waited for was made. A try that ends
      #  at this very door again, for the same object, is refused.
      try:
        passing = _PASSING.doors
      except AttributeError:
        passing = _PASSING.doors = set()
      mark = (door, id(receiver))
      if mark in passing:
        raise DispatchException(dispatcher, given, kwargs)
      passing.add(mark)
      try:
        return function(receiver, *swapped, **kwargs)
      except DispatchException as dispatchException:
        if dispatchException.dispatch is not dispatcher:
          if dispatchException.dispatch is not getattr(
              dispatcher, '__class_dispatcher__', None):
            raise
      finally:
        passing.discard(mark)
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

  def _getInheritedSpaces(self, name: str) -> List[Any]:
    """
    Gives the namespaces of the classes this one inherits overloads of
    a name from, as worktoy works them out, and keeps the answer.

    worktoy asks this each time it gathers something for the dispatcher
    of a name: its signatures of three kinds, its fallback, its
    finalizer and its kind of method, and the door asks three times
    more. Each asking walks every class this one is built on. A cute
    class has hundreds of overloaded names and is built on several
    classes, so the walk is done once for each name and the answer is
    kept. It cannot change while the namespace lives: it follows from
    the classes the body is built on, and from the kind of method the
    body gave the name, and both are fixed when the body has ended,
    which is before worktoy first asks.

    Parameters
    ----------

    name : str
      The overloaded name.

    Returns
    -------

    List[Any]
      The namespaces, in the order worktoy gives them. It is the list
      that is kept, so it is not to be changed.
    """
    if self.__inherited_spaces__ is None:
      self.__inherited_spaces__ = dict()
    try:
      return self.__inherited_spaces__[name]
    except KeyError:
      spaces = BaseSpace._getInheritedSpaces(self, name)
      self.__inherited_spaces__[name] = spaces
      return spaces

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
    whose every signature still waits gets the door as well, so the
    name is on the class and refuses every call until a late class is
    made. A name with nothing on record and nothing waiting gets none.

    Parameters
    ----------

    name : str
      The overloaded name.

    Returns
    -------

    Optional[Callable]
      The declared fallback, or the door, or None for a name with
      nothing on record and nothing waiting.
    """
    fallback = BaseSpace.collectFallback(self, name)
    if fallback is not None:
      return fallback
    registries = (
      self.collectOverloads(name),
      self.collectFlexes(name),
      self.collectVariadics(name),
    )
    if not any(registries) and not self._hasWaiting(name):
      return None
    return self._getDoors(name)[0][0]

  def collectFallbacks(self, name: str) -> list:
    """
    Gives every function the dispatchers of a name call when no
    signature takes a call: what 'collectFallback' gives, any fallback
    the class or a class it is built on declares for the other way of
    calling, and each door of the name that no declared one stands in
    the place of.

    worktoy asks this as it builds the dispatchers of a name. A name
    with ordinary methods beside staticmethods has two doors, and
    worktoy lets it hold one fallback for calls on an object and one
    for calls on the class. A fallback declared with
    '@overload.fallback' keeps its side, and a door fills the other.

    Parameters
    ----------

    name : str
      The overloaded name.

    Returns
    -------

    list
      The functions, as worktoy gathers them, with the doors added. It
      is empty for a name with nothing on record and nothing waiting.
    """
    gathered = BaseSpace.collectFallbacks(self, name)
    if not gathered:
      return gathered
    doors = self._getDoors(name)
    kinds = self.collectFunctionKinds(name)
    for door, doorKind in doors:
      if any(held is door for held in gathered):
        continue
      heldKinds = [self._kindIn(kinds, held) for held in gathered]
      if any(self._mayMeet(heldKind, doorKind) for heldKind in heldKinds):
        #  A call that reaches this door reaches a fallback gathered
        #  already, which keeps its place.
        continue
      gathered.append(door)
    return gathered

  def collectFunctionKinds(self, name: str) -> list:
    """
    Gives each function of a name with its kind of method, as worktoy
    gathers them, and each door of the name with its own.

    worktoy asks this as it builds the dispatchers of a name, and takes
    a function it finds no kind for to be an ordinary method. A door is
    handed over by 'collectFallback' or 'collectFallbacks' and declared
    nowhere, so its kind is told here.

    Parameters
    ----------

    name : str
      The overloaded name.

    Returns
    -------

    list
      A 'List[Tuple[Callable, Any]]': each function with 'classmethod',
      'staticmethod', or None for an ordinary method.
    """
    kinds = BaseSpace.collectFunctionKinds(self, name)
    doors = (self.__doors__ or dict()).get(name, ())
    return [*kinds, *doors]

  def _hasWaiting(self, name: str) -> bool:
    """
    Says whether a signature still waits at a name, in this body or in
    the body of a class this one inherits the name from.
    """
    for space in (self, *self._getInheritedSpaces(name)):
      if not isinstance(space, CuteSpace):
        continue
      for methodName, _ in space._getWaitingList():
        if methodName == name:
          return True
    return False

  def getOverloadNames(self) -> List[str]:
    """
    Gives every name the class gets a dispatcher for: each name worktoy
    finds overloads at, and each name at which a signature still waits,
    in this body or in the body of a class this one is built on.

    worktoy asks this as the class is made. A name whose every
    signature waits is among them, so it is on the class from the
    start: it holds a dispatcher with the door alone, which refuses
    every call with 'DispatchException' until a late class is made.
    Without it the name would not be on the class at all, and reading
    it would raise 'AttributeError'.
    """
    names = BaseSpace.getOverloadNames(self)
    for space in (self, *self._getLookupSpaces()):
      if not isinstance(space, CuteSpace):
        continue
      for methodName, _ in space._getWaitingList():
        if methodName not in names:
          names.append(methodName)
    return names

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
    for methodName, waitingSignature in self.getWaitingSignatures():
      entries = []
      for entry in waitingSignature.getSignatureEntries():
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
      waitingSignature.setSignatureEntries(*entries)
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
    for waitingSignature, entries in records['entries']:
      waitingSignature.setSignatureEntries(*entries)

  def nameLateClass(self, wait: WAIT, lateClass: type) -> Tuple[str, ...]:
    """
    Tells the namespace that a late class its body waited for is made,
    and has it put the signatures that waited for it back on record.

    'MetaCute' calls this, once for each 'WAIT' of the waiting class
    that the new class settles. You never call it. In every waiting
    signature the 'WAIT' is replaced by the class. A signature with no
    'WAIT' left is put on record through 'BaseSpace.addOverload', at
    the place it was written in, and waits no more. One still naming
    another late class stays among 'getWaitingSignatures'.

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
    for waitingItem in self.getWaitingSignatures():
      methodName, waitingSignature = waitingItem
      entries = waitingSignature.getSignatureEntries()
      if not any(entry is wait for entry in entries):
        continue
      entries = (*(lateClass if e is wait else e for e in entries),)
      waitingSignature.setSignatureEntries(*entries)
      if any(isinstance(entry, WAIT) for entry in entries):
        continue
      self._getWaitingList().remove(waitingItem)
      signature = TypeSig(*entries)
      before = len(self.getOverloads().get(methodName, []))
      self.addOverload(methodName, signature, waitingSignature.getFunction())
      declared = self._getDeclaredSignatures(methodName)
      written = declared.index(waitingSignature)
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
