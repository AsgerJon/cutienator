"""
TestCuteCuteSpace tests 'CuteSpace', the namespace the body of a cute
class runs in.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

from unittest import mock

from worktoy.dispatch import TypeSig
from worktoy.keenum import Kee
from worktoy.mcls import BaseObject
from worktoy.mcls.space_hooks import ReservedNamespaceHook
from worktoy.waitaminute import TypeException
from worktoy.waitaminute.dispatch import DispatchException
from worktoy.waitaminute.dispatch import DuplicateSignature
from worktoy.waitaminute.meta import HookException
from worktoy.waitaminute.meta import MixedMethodKind
from worktoy.waitaminute.meta import OverloadConflict, ReboundOverload
from worktoy.work_test import BaseTest

from cutienator.cute import CuteFlags, CuteNum, CuteOverload, CuteSpace
from cutienator.cute import DoorNumber, MetaCute, WAIT, WaitingSignature


class _Mode(CuteNum):
  """An enum a method of a test takes as its number."""
  Fast = Kee[int](1)


class _Option(CuteFlags):
  """Flags a method of a test takes as its number."""
  Wide = 0x2


def _take(self, later: object) -> str:
  """A function a waiting signature is written for."""
  return 'later'


class TestCuteCuteSpace(BaseTest):
  """
  Tests 'CuteSpace' through class bodies: what a body binds, the
  signatures that wait for a late class, the doors through which an
  overloaded name is called when no signature takes the call, and how
  a late class is named in the record.

  What to know before adding a test
  ---------------------------------

  - Each test has a fresh record of the classes 'MetaCute' made and of
    the fields waiting, in 'setUp', so the late classes of a test may
    have any name.
  - A class body reads 'overload' and gets 'CuteOverload', whatever the
    module binds at that name.
  """

  def setUp(self) -> None:
    """A fresh record of the classes made and of the fields waiting."""
    super().setUp()
    for name in ('__made_classes__', '__waiting_fields__'):
      patcher = mock.patch.object(MetaCute, name, dict())
      patcher.start()
      self.addCleanup(patcher.stop)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  THE NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def test_a_cute_body_runs_in_it(self) -> None:
    """'MetaCute' gives a body a 'CuteSpace', which knows its class once
    the class is made, once."""
    space = MetaCute.__prepare__('QCutie', ())
    self.assertIsInstance(space, CuteSpace)
    with self.assertRaises(RuntimeError) as caught:
      space.getCuteClass()
    self.assertIn("'QCutie' is not made yet", str(caught.exception))

    class QCutie(metaclass=MetaCute):
      pass

    space = QCutie.getNamespace()
    self.assertIs(space.getCuteClass(), QCutie)
    with self.assertRaises(RuntimeError):
      space.setCuteClass(QCutie)

  def test_reading_overload_gives_cute_overload(self) -> None:
    """The name 'overload' read in a body is 'CuteOverload', unless the
    body binds it; other names it does not have are not there."""
    space = MetaCute.__prepare__('QCutie', ())
    self.assertIs(space['overload'], CuteOverload)
    with self.assertRaises(KeyError):
      space['nothing']
    space['overload'] = 'own'
    self.assertEqual(space['overload'], 'own')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  PLAIN SIGNATURES   # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def test_plain_signatures_are_worktoys(self) -> None:
    """Signatures naming no late class are worktoy's, in the order
    written."""

    class QCutie(metaclass=MetaCute):
      @overload(int)
      def size(self, n: int) -> str:
        return 'int %d' % n

      @overload(str)
      def size(self, s: str) -> str:
        return 'str %s' % s

    self.assertEqual(QCutie().size(3), 'int 3')
    self.assertEqual(QCutie().size('x'), 'str x')
    space = QCutie.getNamespace()
    self.assertEqual(space._getDeclaredSignatures('size'),
                     [TypeSig(int), TypeSig(str)])
    self.assertEqual(space.getWaitingSignatures(), ())

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  WAITING SIGNATURES   # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def test_a_signature_waits_until_the_late_class_is_made(self) -> None:
    """A signature naming a 'WAIT' waits, kept by the namespace and not
    by worktoy, until the late class is made; then it takes the class,
    in the place it was written."""

    class QWaiter(metaclass=MetaCute):
      QLater = WAIT['QLater']

      @overload(int)
      def take(self, n: int) -> str:
        return 'int'

      @overload(QLater)
      def take(self, later: object) -> str:
        return 'later'

      @overload(str)
      def take(self, s: str) -> str:
        return 'str'

    space = QWaiter.getNamespace()
    (name, waiting), = space.getWaitingSignatures()
    self.assertEqual(name, 'take')
    self.assertIsInstance(waiting, WaitingSignature)
    self.assertEqual(QWaiter().take(1), 'int')

    class QLater(metaclass=MetaCute):
      pass

    self.assertEqual(space.getWaitingSignatures(), ())
    self.assertEqual(QWaiter().take(QLater()), 'later')
    self.assertEqual(space._getDeclaredSignatures('take'), [
        TypeSig(int), TypeSig(QLater), TypeSig(str)])
    self.assertEqual([s for s, _ in space.getOverloads()['take']], [
        TypeSig(int), TypeSig(QLater), TypeSig(str)])

  def test_a_name_of_waiting_signatures_alone(self) -> None:
    """A name whose every signature waits is called through its door
    until then, which refuses every call."""

    class QWaiter(metaclass=MetaCute):
      QLater = WAIT['QLater']

      @overload(QLater)
      def take(self, later: object) -> str:
        return 'later'

    with self.assertRaises(DispatchException):
      QWaiter().take(1)
    self.assertIs(QWaiter.getNamespace().hasOverloads('take'), True)

    class QLater(metaclass=MetaCute):
      pass

    self.assertEqual(QWaiter().take(QLater()), 'later')

  def test_a_wait_written_into_the_signature_is_bound(self) -> None:
    """A 'WAIT' no line binds, written into a signature, is bound at the
    name of the late class, once for each late class."""

    class QWaiter(metaclass=MetaCute):
      @overload(WAIT['QLater'])
      def take(self, later: object) -> str:
        return 'one'

      @overload(WAIT['QLater'], int)
      def take(self, later: object, n: int) -> str:
        return 'two'

    self.assertIsInstance(QWaiter.__dict__['QLater'], WAIT)
    waits = {id(w.getSignatureEntries()[0])
             for _, w in QWaiter.getNamespace().getWaitingSignatures()}
    self.assertEqual(len(waits), 1)

    class QLater(metaclass=MetaCute):
      pass

    self.assertIs(QWaiter.QLater, QLater)
    self.assertEqual(QWaiter().take(QLater(), 2), 'two')

  def test_two_late_classes_in_one_signature(self) -> None:
    """A signature naming two late classes waits for both."""

    class QWaiter(metaclass=MetaCute):
      @overload(WAIT['QFirst'], WAIT['QSecond'])
      def take(self, a: object, b: object) -> str:
        return 'both'

    class QFirst(metaclass=MetaCute):
      pass

    self.assertEqual(len(QWaiter.getNamespace().getWaitingSignatures()), 1)

    class QSecond(metaclass=MetaCute):
      pass

    self.assertEqual(QWaiter().take(QFirst(), QSecond()), 'both')

  def test_signatures_sharing_one_function(self) -> None:
    """A stack of plain and waiting signatures shares one function, and
    a waiting signature written twice for it is kept once."""

    class QWaiter(metaclass=MetaCute):
      QLater = WAIT['QLater']

      @overload(QLater)
      @overload(QLater)
      @overload(int)
      def take(self, value: object) -> str:
        return 'shared'

    self.assertEqual(len(QWaiter.getNamespace().getWaitingSignatures()), 1)
    self.assertEqual(QWaiter().take(3), 'shared')

  def test_two_functions_at_one_waiting_signature(self) -> None:
    """Two functions at one waiting signature are refused."""
    with self.assertRaises((DuplicateSignature, HookException)):

      class QWaiter(metaclass=MetaCute):
        QLater = WAIT['QLater']

        @overload(QLater)
        def take(self, later: object) -> str:
          return 'one'

        @overload(WAIT['QLater'])
        def take(self, later: object) -> str:
          return 'two'

  def test_waiting_signatures_that_differ_are_kept(self) -> None:
    """Waiting signatures of other lengths, or other entries, are all
    kept."""

    class QWaiter(metaclass=MetaCute):
      QLater = WAIT['QLater']

      @overload(QLater)
      def take(self, later: object) -> str:
        return 'one'

      @overload(QLater, int)
      def take(self, later: object, n: int) -> str:
        return 'two'

      @overload(QLater, str)
      def take(self, later: object, s: str) -> str:
        return 'three'

      @overload(QLater)
      def give(self, later: object) -> str:
        return 'give'

    self.assertEqual(len(QWaiter.getNamespace().getWaitingSignatures()), 4)

  def test_kinds_of_method_are_noted(self) -> None:
    """A static or class method waiting is noted as that kind; mixing
    the two at one name is refused."""

    class QWaiter(metaclass=MetaCute):
      QLater = WAIT['QLater']

      @staticmethod
      @overload(QLater)
      def make(later: object) -> str:
        return 'static'

      @classmethod
      @overload(QLater)
      def build(cls, later: object) -> str:
        return cls.__name__

    class QLater(metaclass=MetaCute):
      pass

    self.assertEqual(QWaiter.make(QLater()), 'static')
    self.assertEqual(QWaiter.build(QLater()), 'QWaiter')
    with self.assertRaises((MixedMethodKind, HookException)):

      class QMixed(metaclass=MetaCute):
        QLater2 = WAIT['QLater2']

        @staticmethod
        @overload(QLater2)
        @classmethod
        @overload(int)
        def make(cls, value: object) -> str:
          return 'mixed'

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  WHAT A BODY MAY NOT DO   # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def test_a_plain_definition_then_a_waiting_signature(self) -> None:
    """A waiting signature at a name defined plainly is refused."""
    with self.assertRaises((OverloadConflict, HookException)):

      class QWaiter(metaclass=MetaCute):
        def take(self) -> str:
          return 'plain'

        @overload(WAIT['QLater'])
        def take(self, later: object) -> str:
          return 'later'

  def test_one_waiting_record_at_two_names(self) -> None:
    """A waiting overload bound at a second name is refused."""
    with self.assertRaises((ReboundOverload, HookException)):

      class QWaiter(metaclass=MetaCute):
        @overload(WAIT['QLater'])
        def take(self, later: object) -> str:
          return 'later'

        other = take

  def test_a_wait_of_another_body(self) -> None:
    """A signature naming a 'WAIT' bound in another class's body is
    refused, saying to bind one in this body."""
    with self.assertRaises((TypeError, HookException)) as caught:

      class QFirst(metaclass=MetaCute):
        QLater = WAIT['QLater']

      class QSecond(metaclass=MetaCute):
        @overload(QFirst.__dict__['QLater'])
        def take(self, later: object) -> str:
          return 'later'

    self.assertIn("bound in the body of 'QFirst'", _said(caught))

  def test_a_name_taken_keeps_a_wait_from_being_bound(self) -> None:
    """A 'WAIT' written into a signature, whose name the body binds to
    something else, is refused."""
    with self.assertRaises((TypeError, HookException)) as caught:

      class QWaiter(metaclass=MetaCute):
        QLater = 'taken'

        @overload(WAIT['QLater'])
        def take(self, later: object) -> str:
          return 'later'

    self.assertIn("the name 'QLater' is taken", _said(caught))

  def test_a_wait_unbound_before_the_body_ends(self) -> None:
    """A 'WAIT' a signature names, deleted from the body before it ends,
    is refused."""
    with self.assertRaises(TypeError) as caught:

      class QWaiter(metaclass=MetaCute):
        QLater = WAIT['QLater']

        @overload(QLater)
        def take(self, later: object) -> str:
          return 'later'

        del QLater

    self.assertIn('no longer binds it', str(caught.exception))

  def test_two_waits_of_one_name_are_one_signature(self) -> None:
    """Two 'WAIT' objects of the same name, in the same place, make one
    signature; of other names they do not."""
    first, other = WaitingSignature(), WaitingSignature()
    first.setSignatureEntries(WAIT['QLater'], int)
    other.setSignatureEntries(WAIT['QLater'], int)
    self.assertIs(CuteSpace._isOneSignature(first, other), True)
    other.setSignatureEntries(WAIT['QOther'], int)
    self.assertIs(CuteSpace._isOneSignature(first, other), False)

  def test_a_space_with_no_load_hook(self) -> None:
    """With no load hook of worktoy's among the hooks, every hook is
    asked, and a waiting signature is still kept."""
    space = MetaCute.__prepare__('QCutie', ())
    waiting = CuteOverload(WAIT['QLater'])(_take)
    with mock.patch.object(CuteSpace, 'getHooks', return_value=[]):
      space['take'] = waiting
    (name, _), = space.getWaitingSignatures()
    self.assertEqual(name, 'take')

  def test_making_a_wait_that_leaves_none_does_not_loop(self) -> None:
    """When binding a 'WAIT' for a signature leaves none, it raises."""
    space = MetaCute.__prepare__('QCutie', ())
    with mock.patch.object(CuteSpace, '_createOwnWait'):
      with self.assertRaises(RecursionError):
        space._getOwnWait('take', WAIT['QLater'])

  def test_a_hook_ahead_of_worktoys_may_claim_a_name(self) -> None:
    """A hook ahead of worktoy's load hook claiming a waiting name keeps
    it from the namespace."""
    with mock.patch.object(
        ReservedNamespaceHook, 'setItemPhase', return_value=True):

      class QWaiter(metaclass=MetaCute):
        @overload(WAIT['QLater'])
        def take(self, later: object) -> str:
          return 'later'

    self.assertEqual(QWaiter.getNamespace().getWaitingSignatures(), ())

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  DOORS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def _cutie(self) -> type:
    """A cute class whose methods take numbers, each kind of method."""

    class QCutie(metaclass=MetaCute):
      @overload(int)
      def size(self, n: int) -> str:
        return 'size %d %s' % (n, type(n).__name__)

      @staticmethod
      @overload(int)
      def make(n: int) -> str:
        return 'make %d %s' % (n, type(n).__name__)

      @classmethod
      @overload(int)
      def build(cls, n: int) -> str:
        return 'build %s %d' % (cls.__name__, n)

      @overload(int)
      def both(self, n: int) -> str:
        return 'both on %s' % type(self).__name__

      @staticmethod
      @overload(str)
      def both(s: str) -> str:
        return 'both static'

    return QCutie

  def test_the_doors_of_each_kind(self) -> None:
    """A name of methods has one door, one of class methods or static
    methods its own, and one of methods and static methods both."""
    space = self._cutie().getNamespace()
    for name, kinds in (('size', (None,)), ('make', (staticmethod,)),
                        ('build', (classmethod,)),
                        ('both', (None, staticmethod))):
      with self.subTest(name=name):
        self.assertEqual(space._findDoorKinds(name), kinds)
        doors = space._getDoors(name)
        self.assertEqual([kind for _, kind in doors], [*kinds])
        self.assertIs(space._getDoors(name), doors)

  def test_a_member_passes_as_its_number(self) -> None:
    """A member of an enum, or a value of flags, no signature takes is
    handed in again as its number, by each kind of method."""
    QCutie = self._cutie()
    self.assertEqual(QCutie().size(_Mode.Fast), 'size 1 DoorNumber')
    self.assertEqual(QCutie.make(_Option.Wide), 'make 2 DoorNumber')
    self.assertEqual(QCutie.build(_Mode.Fast), 'build QCutie 1')
    self.assertEqual(QCutie().both(_Mode.Fast), 'both on QCutie')

  def test_what_no_signature_takes_is_refused(self) -> None:
    """What no signature takes, once handed in again, is refused by the
    dispatcher of the name."""
    QCutie = self._cutie()
    for call in (lambda: QCutie().size(2.5), lambda: QCutie.make('x'),
                 lambda: QCutie.build(None)):
      with self.subTest(call=call):
        with self.assertRaises(DispatchException):
          call()

  def test_a_door_is_not_passed_twice(self) -> None:
    """A door reached again while it passes a call is refused."""
    QCutie = self._cutie()
    space = QCutie.getNamespace()
    door, _ = space._getDoors('size')[0]
    cutie = QCutie()

    class Again:
      def __index__(self) -> int:
        return door(cutie, 1)

    with mock.patch.object(DoorNumber, '__new__',
                           side_effect=lambda cls, n: door(cutie, 1)):
      with self.assertRaises(DispatchException):
        door(cutie, _Mode.Fast)

  def test_a_dispatch_of_another_name_is_raised_as_it_is(self) -> None:
    """A refused call of another name inside the function is not taken
    for one of this name."""

    class QCutie(metaclass=MetaCute):
      @overload(int)
      def size(self, n: int) -> str:
        return self.other('not an int')

      @overload(int)
      def other(self, n: int) -> str:
        return 'other'

    with self.assertRaises(DispatchException) as caught:
      QCutie().size(_Mode.Fast)
    dispatcher = QCutie.__dict__['other']
    self.assertIs(caught.exception.dispatch, dispatcher)

  def test_a_fallback_of_its_own(self) -> None:
    """A name with a fallback of its own keeps it, and gets no door."""

    class QCutie(metaclass=MetaCute):
      @overload(int)
      def size(self, n: int) -> str:
        return 'int'

      @overload.fallback
      def size(self, *args: object) -> str:
        return 'fallback'

    self.assertEqual(QCutie().size(_Mode.Fast), 'fallback')
    self.assertEqual(QCutie().size(2.5), 'fallback')

  def test_a_fallback_and_a_door_of_another_kind(self) -> None:
    """A name with a fallback of one kind and functions of another gets
    a door for the other."""

    class QCutie(metaclass=MetaCute):
      @overload(int)
      def both(self, n: int) -> str:
        return 'method'

      @staticmethod
      @overload(str)
      def both(s: str) -> str:
        return 'static'

      @staticmethod
      @overload.fallback
      def both(*args: object) -> str:
        return 'static fallback'

    self.assertEqual(QCutie().both(3), 'method')
    self.assertEqual(QCutie.both('x'), 'static')
    self.assertEqual(QCutie.both(2.5), 'static fallback')
    space = QCutie.getNamespace()
    kinds = [kind for _, kind in space.collectFunctionKinds('both')]
    self.assertIn(staticmethod, kinds)

  def test_a_door_of_class_methods_beside_methods(self) -> None:
    """At a name of methods beside class methods the door is a class
    method; what it reads through the class refuses for the name."""

    class QCutie(metaclass=MetaCute):
      @overload(int)
      def mix(self, n: int) -> str:
        return 'method'

      @classmethod
      @overload(str)
      def mix(cls, s: str) -> str:
        return 'class'

    space = QCutie.getNamespace()
    self.assertEqual(space._findDoorKinds('mix'), (classmethod,))
    self.assertEqual(QCutie().mix(1), 'method')
    self.assertEqual(QCutie.mix('x'), 'class')
    with self.assertRaises(DispatchException) as caught:
      QCutie().mix(2.5)
    self.assertIs(caught.exception.dispatch, QCutie.__dict__['mix'])

  def test_a_refusal_through_the_class_is_the_names(self) -> None:
    """A refusal by the dispatcher a name keeps for calls through the
    class is a refusal of the name, and the door refuses the call as
    written. No class body found so far makes a door reach it, so a
    stand-in dispatcher holds it here."""
    space = MetaCute.__prepare__('QCutie', ())
    door = space._createDoor('take', staticmethod)
    onClass = object()

    def refuse(*args: object) -> None:
      raise DispatchException(onClass, args)

    class Dispatcher:
      """Stands in for the dispatcher of the name."""
      __class_dispatcher__ = onClass

      def __get__(self, instance: object, owner: type) -> object:
        return refuse

    class Owner:
      """Stands in for the class the body became."""
      take = Dispatcher()

    space.setCuteClass(Owner)
    with self.assertRaises(DispatchException) as caught:
      door(_Mode.Fast)
    self.assertIs(caught.exception.dispatch, Owner.__dict__['take'])

  def test_no_fallbacks_for_a_name_with_nothing(self) -> None:
    """A name with nothing on record and nothing waiting has no
    fallbacks, and no doors are made for it."""
    space = self._cutie().getNamespace()
    self.assertEqual(space.collectFallbacks('nothing'), [])

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  INHERITED  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def test_a_class_built_on_a_waiting_class(self) -> None:
    """A class built on a class whose signature waits waits too, and
    takes the late class with it; its inherited spaces are kept."""

    class QBase(metaclass=MetaCute):
      QLater = WAIT['QLater']

      @overload(QLater)
      def take(self, later: object) -> str:
        return 'base'

    class QDerived(QBase):
      @overload(int)
      def take(self, n: int) -> str:
        return 'derived'

    space = QDerived.getNamespace()
    self.assertIs(space._hasWaiting('take'), True)
    self.assertIn('take', space.getOverloadNames())
    self.assertIs(space._getInheritedSpaces('take'),
                  space._getInheritedSpaces('take'))

    class QLater(metaclass=MetaCute):
      pass

    self.assertEqual(QDerived().take(QLater()), 'base')
    self.assertEqual(QDerived().take(1), 'derived')
    self.assertIs(space._hasWaiting('take'), False)

  def test_a_cute_class_built_on_a_plain_one(self) -> None:
    """Classes along the way whose namespace is no 'CuteSpace' are
    passed by."""

    class Plain(BaseObject):
      def other(self) -> str:
        return 'plain'

    class QCutie(Plain, metaclass=MetaCute):
      @overload(int)
      def size(self, n: int) -> str:
        return 'int'

    space = QCutie.getNamespace()
    self.assertIs(space._hasWaiting('size'), False)
    self.assertIn('size', space.getOverloadNames())
    self.assertIsNone(space.collectFallback('other'))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMING A LATE CLASS  # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def _waiter(self) -> type:
    """A class with a signature waiting for two late classes, and two
    waiting for one of them, between plain ones."""

    class QWaiter(metaclass=MetaCute):
      QLater = WAIT['QLater']
      QOther = WAIT['QOther']

      @overload(int)
      def take(self, n: int) -> str:
        return 'int'

      @overload(QLater)
      def take(self, later: object) -> str:
        return 'later'

      @overload(QLater, QOther)
      def take(self, later: object, other: object) -> str:
        return 'both'

      @overload(QLater)
      def give(self, later: object) -> str:
        return 'give'

    return QWaiter

  def test_naming_a_late_class_gives_the_names_changed(self) -> None:
    """Each name whose signatures are complete now is given once."""
    QWaiter = self._waiter()
    space = QWaiter.getNamespace()
    wait = QWaiter.__dict__['QLater']

    class QStand(BaseObject):
      pass

    self.assertEqual(space.nameLateClass(wait, QStand), ('take', 'give'))
    self.assertEqual(len(space.getWaitingSignatures()), 1)
    other = QWaiter.__dict__['QOther']
    self.assertEqual(space.nameLateClass(other, QStand), ('take',))
    self.assertEqual(space.nameLateClass(other, QStand), ())

  def test_naming_a_class_no_signature_is_complete_for(self) -> None:
    """Naming a late class that leaves every signature waiting gives no
    name, and passes by the signatures that do not name it."""
    QWaiter = self._waiter()
    space = QWaiter.getNamespace()
    self.assertEqual(space.nameLateClass(QWaiter.__dict__['QOther'], int),
                     ())
    self.assertEqual(len(space.getWaitingSignatures()), 3)

  def test_a_signature_named_twice_is_taken_once(self) -> None:
    """A signature that becomes one on record already is taken once."""

    class QWaiter(metaclass=MetaCute):
      QLater = WAIT['QLater']

      @overload(QLater)
      @overload(int)
      def take(self, value: object) -> str:
        return 'shared'

    space = QWaiter.getNamespace()
    space.nameLateClass(QWaiter.__dict__['QLater'], int)
    self.assertEqual(space._getDeclaredSignatures('take'), [TypeSig(int)])
    self.assertEqual(len(space.getOverloads()['take']), 1)

  def test_naming_is_all_or_nothing(self) -> None:
    """When naming fails, everything is put back as it was."""
    QWaiter = self._waiter()
    space = QWaiter.getNamespace()
    before = space.keepRecords()
    with mock.patch.object(CuteSpace, 'addOverload',
                           side_effect=ValueError('refused')):
      with self.assertRaises(ValueError):
        space.nameLateClass(QWaiter.__dict__['QLater'], int)
    after = space.keepRecords()
    self.assertEqual(after['onRecord'], before['onRecord'])
    self.assertEqual(after['waitingList'], before['waitingList'])
    self.assertEqual(after['declared'], before['declared'])
    for waiting, entries in before['entries']:
      with self.subTest(waiting=waiting):
        self.assertEqual(waiting.getSignatureEntries(), entries)

  def test_naming_checks_what_it_is_given(self) -> None:
    """Naming takes a 'WAIT' and a class, and refuses anything else."""
    space = self._waiter().getNamespace()
    with self.assertRaises(TypeException):
      space.nameLateClass('QLater', int)
    with self.assertRaises(TypeException):
      space.nameLateClass(WAIT['QLater'], 'int')


def _said(caught: object) -> str:
  """What was raised, or, when a hook wrapped it, what it wrapped."""
  exception = caught.exception
  cause = getattr(exception, '__cause__', None)
  return '%s %s' % (exception, cause)
