"""
MetaCute provides the general 'metaclass' for the 'cutienator' library.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.mcls import BaseMeta
from worktoy.waitaminute import TypeException

from . import WAIT, CuteSpace

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Any, Dict, List, Optional, Tuple

  WaitingField = Tuple[type, str, WAIT]
  Family = List[Tuple[type, CuteSpace]]


class MetaCute(BaseMeta):
  """
  MetaCute provides the general 'metaclass' for the 'cutienator' library.
  It makes every cute class, and so it is the one place that sees each
  of them the moment it exists. It uses that for one job so far:
  settling the classes that wait for a class made later. See 'WAIT' for
  the whole story; this is step 1, 5 and 6 of it.

    class QObject(CuteMixin, metaclass=MetaCute):
      QThread = WAIT['QThread']
      ...

    MetaCute.getStillWaiting()         # ('QThread',)

    class QThread(QObject):            # 'MetaCute' notices this one
      ...

    MetaCute.getStillWaiting()         # ()

  Terms
  -----

  - A late class, a waiting class and a waiting signature are as 'WAIT'
    explains them.
  - A waiting field is one 'WAIT' in the body of a waiting class,
    together with that class and the name it is bound to: 'QObject',
    'QThread', and the 'WAIT' at 'QObject.QThread'.
  - To settle a waiting field is to do, once its late class is made,
    what the waiting class could not do when it was made itself.
  - A dispatcher is the one object worktoy puts at an overloaded name,
    which picks the function for each call.

  You provide
  -----------

  Nothing here. You write 'metaclass=MetaCute' on a cute class that is
  built on no other cute class, and the 'WAIT' lines in the bodies.

  What it does
  ------------

  - '__prepare__' gives the body of every cute class a 'CuteSpace' to
    run in.
  - 'addWaiting' takes note of a waiting field. The 'WAIT' calls it
    itself, as its class is made.
  - '__init__' runs each time a cute class has just been made. It notes
    the class down by its name, and settles every waiting field whose
    late class is now on the list. For one waiting field that is:
    1. The late class is put at the name of the waiting class, in the
       place of the 'WAIT': 'QObject.QThread' is 'QThread' from now on.
    2. The 'CuteSpace' of the waiting class puts the signatures that
       waited for it back on record, each where it was written.
    3. The dispatcher of each name that got a signature back is built
       again and placed, on the waiting class and on every class built
       on it so far, since each class has dispatchers of its own.

  What to expect
  --------------

  - One list of waiting fields and one list of made classes serve every
    cute class in the program, also the classes of a metaclass based on
    this one.
  - A class is recognised by its name alone: a cute class by the name
    Qt has for it, its own '__qt_class__' with dots for '::', as
    'Qt3DCore.QEntity' or 'QV4.Heap.Object', and any other class, as
    one a program writes, by its '__name__'. Where two parts of Qt have
    a class of the same name, as 'QBarSeries' of QtCharts and of
    QtGraphs, the body of each says its part as well, in its own
    '__qt_part__', and the class is recognised by both, as
    'QtCharts:QBarSeries'. Two classes of one name are not told apart
    otherwise: the one made last is the one a later 'WAIT' is settled
    with.
  - A 'WAIT' for a class that is made already is settled right as its
    waiting class is made.
  - 'getStillWaiting' names what is waited for and not made. After
    every cute class of a program is imported it should be empty.
  - A dispatcher built again replaces the one that was there. A method
    that was read off an object before, and kept, still goes by the old
    one, and hands a call the old one has no signature for on to the
    new one; see the door of 'CuteSpace'.
  - Settling is all or nothing. When one waiting field cannot be
    settled, as when its class has two functions at what becomes one
    signature, the class statement that was running fails, and that
    class is not noted as made. The faulty field is given up. Every
    other field keeps waiting, untouched, and is settled when the class
    is written again.
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
  #  Kept on 'MetaCute' itself and read off it by name, so a metaclass
  #  based on this one shares them. For each late class by name, the
  #  waiting fields that wait for it.
  __waiting_fields__: Optional[Dict[str, List[WaitingField]]] = None
  #  Every cute class made so far, by name.
  __made_classes__: Optional[Dict[str, type]] = None

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @classmethod
  def _getWaitingFields(mcls) -> Dict[str, List[WaitingField]]:
    """Gives the one list of waiting fields, making it if need be."""
    if MetaCute.__waiting_fields__ is None:
      MetaCute.__waiting_fields__ = dict()
    return MetaCute.__waiting_fields__

  @classmethod
  def _getMadeClasses(mcls) -> Dict[str, type]:
    """Gives the one list of cute classes made, making it if need be."""
    if MetaCute.__made_classes__ is None:
      MetaCute.__made_classes__ = dict()
    return MetaCute.__made_classes__

  @classmethod
  def getStillWaiting(mcls) -> Tuple[str, ...]:
    """
    Gives the name of every late class that some cute class waits for
    and that is not made yet, in alphabetical order.

    Found for you, from the waiting fields noted by 'addWaiting' and
    not yet settled. Ask it after importing every cute class of a
    program: a name left then is a class that was promised by a 'WAIT'
    and never written, or written under another name.

    Returns
    -------

    Tuple[str, ...]
      The names, as ('QThread',). It is empty when nothing waits.
    """
    waitingFields = mcls._getWaitingFields()
    return (*sorted(name for name in waitingFields if waitingFields[name]),)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @classmethod
  def addWaiting(
      mcls,
      waitingClass: type,
      fieldName: str,
      wait: WAIT,
  ) -> None:
    """
    Takes note that a cute class waits for a late class.

    Called by the 'WAIT' itself, from 'WAIT.hookSetName', as its class
    is made. You never call it. The waiting field is settled by
    '__init__': at once when the late class is made already, otherwise
    when it is made.

    Parameters
    ----------

    waitingClass : type
      The class whose body holds the 'WAIT'.

    fieldName : str
      The name the 'WAIT' is bound to in that body.

    wait : WAIT
      The 'WAIT'. It knows the name of the late class.

    Raises
    ------

    TypeException
      'waitingClass' is no class, 'fieldName' no text, or 'wait' no
      'WAIT'.
    """
    if not isinstance(waitingClass, type):
      raise TypeException('waitingClass', waitingClass, type)
    if not isinstance(fieldName, str):
      raise TypeException('fieldName', fieldName, str)
    if not isinstance(wait, WAIT):
      raise TypeException('wait', wait, WAIT)
    waitingFields = mcls._getWaitingFields()
    waitingFor = waitingFields.setdefault(wait.getWaitingName(), [])
    waitingFor.append((waitingClass, fieldName, wait))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @classmethod
  def __prepare__(mcls, name: str, bases: tuple, **kwargs) -> CuteSpace:
    """
    Gives the namespace the body of a cute class runs in: a new
    'CuteSpace'.

    Python calls this at every class statement of a cute class, before
    the body runs. You never call it.
    """
    return CuteSpace(mcls, name, bases, **kwargs)

  def __init__(cls, name: str, bases: tuple, space: Any, **kwargs) -> None:
    """
    Runs when a cute class has just been made, and settles every
    waiting field whose late class is now made.

    Python calls this at the end of every class statement of a cute
    class. You never call it. First worktoy does all it does for any
    class. Then the class is noted down by its name, and each waiting
    field whose late class is on the list is settled. That covers both
    ways round: the fields of other classes that waited for this one,
    and the fields of this class waiting for a class made before it.

    When any of that raises, the class statement fails, and the lists
    are left as if it had never run: the class is not noted as made,
    and its own waiting fields are forgotten. See '_settleReady' for
    what becomes of the waiting fields of other classes.

    Parameters
    ----------

    name : str
      The name of the class just made.

    bases : tuple
      The classes it is built on, as the class statement names them.

    space : Any
      The 'CuteSpace' its body ran in.
    """
    mcls = type(cls)
    madeClasses = mcls._getMadeClasses()
    known = mcls._getKnownName(name, space)
    madeBefore = madeClasses.get(known, None)
    try:
      super().__init__(name, bases, space, **kwargs)
      madeClasses[known] = cls
      mcls._settleReady()
    except BaseException:
      if madeBefore is None:
        madeClasses.pop(known, None)
      else:
        madeClasses[known] = madeBefore
      mcls._forgetClass(cls)
      raise

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def _getKnownName(name: str, space: Any) -> str:
    """
    Gives the name a class just made is noted under: the dotted name of
    its own '__qt_class__', as 'Qt3DCore.QEntity', and before it its own
    '__qt_part__', which only a class whose name another part of Qt has
    as well says, as 'QtCharts:QBarSeries'. A class without its own
    '__qt_class__', as one a program builds on a cute class, which
    inherits that and is not the class of Qt, is noted by its name.
    """
    qtName = dict.get(space, '__qt_class__', None)
    known = qtName.replace('::', '.') if isinstance(qtName, str) else name
    qtPart = dict.get(space, '__qt_part__', None)
    if isinstance(qtPart, str):
      known = '%s:%s' % (qtPart, known)
    return known

  @classmethod
  def noteStandIn(mcls, standIn: type) -> None:
    """
    Notes a class that stands in a cute class, one 'UnsupportedMeta'
    makes for a class of Qt that has no cute class yet, as made, under
    the name a cute class of its '__qt_class__' and '__qt_part__' would
    be noted under, and settles each waiting field waiting for it. So a
    'WAIT' for that class holds the stand-in, and what takes or gives
    one raises NotImplementedError, saying why, when it is used.

    'UnsupportedMeta' calls this at the end of the class statement of a
    stand-in with a '__qt_class__' of its own. You never call it.
    """
    madeClasses = mcls._getMadeClasses()
    known = mcls._getKnownName(standIn.__name__, dict(vars(standIn)))
    madeBefore = madeClasses.get(known, None)
    madeClasses[known] = standIn
    try:
      mcls._settleReady()
    except BaseException:
      if madeBefore is None:
        madeClasses.pop(known, None)
      else:
        madeClasses[known] = madeBefore
      raise

  @classmethod
  def _settleReady(mcls) -> None:
    """
    Settles every waiting field whose late class is made: all of them,
    or none.

    It goes in two rounds. In the first, the 'CuteSpace' of each
    waiting class puts its signatures back on record. That is the one
    step that can be refused: worktoy raises 'DuplicateSignature' when
    two functions end up at one signature. In the second round the late
    class is put at each field and the dispatchers are built again,
    which nothing refuses.

    When the first round is refused for one waiting field, every
    namespace changed so far is put back as it was, that one field is
    given up, and the refusal is raised, so the class statement that
    was running fails. No class has been touched by then. The other
    fields keep waiting, whichever order they were noted in, and are
    settled when the class is written again. The field given up is
    never settled: the refusal named its fault.

    Raises
    ------

    DuplicateSignature
      A signature put back equals one its waiting class already has for
      another function.

    TypeException
      A waiting class, or a class built on it, has a namespace that is
      no 'CuteSpace'. That takes a metaclass based on this one that
      prepares another namespace.
    """
    madeClasses = mcls._getMadeClasses()
    ready = []  # type: List[Tuple[str, WaitingField]]
    for lateName, waitingFor in mcls._getWaitingFields().items():
      if lateName in madeClasses:
        ready.extend((lateName, waitingField) for waitingField in waitingFor)
    named = []  # type: List[Tuple[Any, ...]]
    for lateName, waitingField in ready:
      waitingClass, fieldName, wait = waitingField
      try:
        family = mcls._getFamily(waitingClass)
        space = family[0][1]
        records = space.keepRecords()
        methodNames = space.nameLateClass(wait, madeClasses[lateName])
      except BaseException as exception:
        for _, _, namedFamily, _, namedRecords in reversed(named):
          namedFamily[0][1].restoreRecords(namedRecords)
        if isinstance(exception, Exception):
          mcls._dropWaiting(lateName, waitingField)
        raise
      named.append((lateName, waitingField, family, methodNames, records))
    for lateName, waitingField, family, methodNames, _ in named:
      waitingClass, fieldName, _ = waitingField
      mcls._dropWaiting(lateName, waitingField)
      type.__setattr__(waitingClass, fieldName, madeClasses[lateName])
      mcls._buildAgain(family, methodNames)

  @classmethod
  def _dropWaiting(mcls, lateName: str, waitingField: WaitingField) -> None:
    """Takes one waiting field off the list: it is settled, or given up."""
    waitingFields = mcls._getWaitingFields()
    waitingFor = waitingFields.get(lateName, [])
    for index, held in enumerate(waitingFor):
      if held is waitingField:
        del waitingFor[index]
        break
    if not waitingFor:
      waitingFields.pop(lateName, None)

  @classmethod
  def _forgetClass(mcls, cuteClass: type) -> None:
    """Takes every waiting field of one class off the list: it was never
    made, since its class statement failed."""
    waitingFields = mcls._getWaitingFields()
    for lateName in [*waitingFields]:
      for waitingField in [*waitingFields[lateName]]:
        if waitingField[0] is cuteClass:
          mcls._dropWaiting(lateName, waitingField)

  @classmethod
  def _getFamily(mcls, cuteClass: type) -> Family:
    """
    Gives a class and every class built on it so far, each with the
    'CuteSpace' its body ran in. The class itself comes first, and a
    class always comes after the one it is built on.

    Parameters
    ----------

    cuteClass : type
      The class to start at.

    Raises
    ------

    TypeException
      One of them has a namespace that is no 'CuteSpace', so nothing
      kept its waiting signatures and nothing can build its dispatchers
      again.
    """
    space = cuteClass.getNamespace()
    if not isinstance(space, CuteSpace):
      raise TypeException('space', space, CuteSpace)
    family = [(cuteClass, space)]
    for subclass in type.__subclasses__(cuteClass):
      for member in mcls._getFamily(subclass):
        if all(member[0] is not held[0] for held in family):
          family.append(member)
    return family

  @classmethod
  def _buildAgain(
      mcls,
      family: Family,
      methodNames: Tuple[str, ...],
  ) -> None:
    """
    Builds the dispatchers of some names again and places them, on a
    class and on every class built on it so far.

    A class that defines one of the names plainly in its own body keeps
    that definition, as it did when it was made: a plain definition
    hides the overloads behind it.

    Parameters
    ----------

    family : Family
      The waiting class and the classes built on it, as '_getFamily'
      gave them.

    methodNames : Tuple[str, ...]
      The names that got a signature back, as 'CuteSpace.nameLateClass'
      gave them.
    """
    for cuteClass, space in family:
      for methodName in methodNames:
        if dict.__contains__(space, methodName):
          continue
        dispatcher = space.cuteLoadHook.buildAgain(methodName)
        if dispatcher is None:
          continue
        type.__setattr__(cuteClass, methodName, dispatcher)
        dispatcher.__set_name__(cuteClass, methodName)

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
