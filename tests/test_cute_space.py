"""
TestCuteSpace tests 'CuteSpace', the namespace the body of a cute class
runs in.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.mcls import BaseObject
from worktoy.mcls.space_hooks import AbstractSpaceHook
from worktoy.waitaminute import TypeException
from worktoy.waitaminute.dispatch import DuplicateSignature
from worktoy.waitaminute.meta import OverloadConflict, MixedMethodKind
from worktoy.waitaminute.meta import ClaimedName, ReboundOverload
from worktoy.waitaminute.meta import DelException, QuestionableSyntax
from worktoy.waitaminute.meta import UnboundClassHook, SlotsRefused
from worktoy.waitaminute.meta import HookException
from worktoy.work_test import BaseTest

from cutienator.cute import MetaCute, CuteSpace, CuteOverload, WAIT
from cutienator.cute import WaitingOverload

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Any, List, Tuple


class TestCuteSpace(BaseTest):
  """
  Tests 'CuteSpace' on its own. Each test gets a namespace from
  'MetaCute.__prepare__', as a class statement would, and then reads
  and binds names in it by hand, the way a class body does line by
  line. No class is made from it, so what is tested is the namespace
  alone: what it answers, what it keeps, and what 'nameLateClass' puts
  back.

  No test here makes a cute class, and a 'WAIT' in no class body is
  noted nowhere, so none has to mind the names 'MetaCute' keeps.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  HELPERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def _makeSpace(className: str) -> CuteSpace:
    """Gives the namespace a class statement of that name would run in."""
    return MetaCute.__prepare__(className, (BaseObject,))

  @staticmethod
  def _first(self: Any, thing: Any) -> str:
    """A function to bind in a namespace. It is never called."""
    return 'first'

  @staticmethod
  def _second(self: Any, thing: Any) -> str:
    """Another function to bind in a namespace. It is never called."""
    return 'second'

  @staticmethod
  def _third(self: Any, thing: Any) -> str:
    """A third function to bind in a namespace. It is never called."""
    return 'third'

  @staticmethod
  def _bindWait(space: CuteSpace, lateName: str) -> WAIT:
    """Binds a new 'WAIT' at the name of its late class, as a body does."""
    wait = WAIT[lateName]
    space[lateName] = wait
    return wait

  @staticmethod
  def _onRecord(space: CuteSpace, name: str) -> List[Tuple[Any, ...]]:
    """Gives the signatures worktoy has on record at a name, in order."""
    onRecord = space.getOverloads().get(name, [])
    return [signature.getRawTypes() for signature, _ in onRecord]

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  WHAT IT ANSWERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def test_prepare_gives_a_cute_space(self) -> None:
    """'MetaCute.__prepare__' gives a new 'CuteSpace' each time."""
    space = self._makeSpace('PreparedOnce')
    self.assertIsInstance(space, CuteSpace)
    self.assertIsNot(space, self._makeSpace('PreparedOnce'))
    self.assertEqual(space.getWaitingOverloads(), ())

  def test_reading_overload_gives_cute_overload(self) -> None:
    """The name 'overload' is answered with 'CuteOverload'."""
    space = self._makeSpace('ReadsOverload')
    self.assertIs(space['overload'], CuteOverload)

  def test_a_body_binding_overload_itself_gets_its_own(self) -> None:
    """A body that binds 'overload' itself reads back what it bound."""
    space = self._makeSpace('BindsOverload')
    space['overload'] = 7
    self.assertEqual(space['overload'], 7)

  def test_every_other_name_is_left_to_the_file(self) -> None:
    """A name the body never bound raises 'KeyError', as it must."""
    space = self._makeSpace('ReadsOthers')
    for name in ('staticmethod', 'THIS', 'WAIT', 'overloads', 'Overload'):
      with self.subTest(name=name):
        with self.assertRaises(KeyError):
          _ = space[name]

  def test_the_hooks_are_shown_the_read_of_overload(self) -> None:
    """A hook of the namespace sees the body read 'overload'."""
    seen = []

    class SeeingHook(AbstractSpaceHook):
      """Notes every name read in the namespace it works for."""

      def getItemPhase(self, key: str, value: Any) -> None:
        """Notes the name."""
        seen.append(key)

    class SeeingSpace(CuteSpace):
      """A 'CuteSpace' with a hook that notes what is read."""

      seeingHook = SeeingHook()

    space = SeeingSpace(MetaCute, 'SeenReading', (BaseObject,))
    self.assertIs(space['overload'], CuteOverload)
    self.assertEqual(seen, ['overload'])

  def test_a_hook_can_refuse_the_read_of_overload(self) -> None:
    """A hook refusing the read of 'overload' is heard, as for any name."""

    class RefusingHook(AbstractSpaceHook):
      """Refuses every read of the name 'overload'."""

      def getItemPhase(self, key: str, value: Any) -> None:
        """Raises for 'overload'."""
        if key == 'overload':
          raise ValueError(key)

    class RefusingSpace(CuteSpace):
      """A 'CuteSpace' with a hook that refuses 'overload'."""

      refusingHook = RefusingHook()

    space = RefusingSpace(MetaCute, 'RefusedReading', (BaseObject,))
    with self.assertRaises(HookException):
      _ = space['overload']

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  WHAT IT KEEPS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def test_a_waiting_overload_is_kept_and_not_stored(self) -> None:
    """A 'WaitingOverload' is kept by the namespace and stored nowhere."""
    space = self._makeSpace('KeepsOne')
    wait = self._bindWait(space, 'KeepsLate')
    waitingOverload = CuteOverload(wait)(self._first)
    space['meet'] = waitingOverload
    self.assertFalse(dict.__contains__(space, 'meet'))
    kept = (('meet', waitingOverload),)
    self.assertEqual(space.getWaitingOverloads(), kept)
    self.assertEqual(self._onRecord(space, 'meet'), [])
    self.assertTrue(space.hasOverloads('meet'))
    self.assertFalse(space.hasOverloads('greet'))

  def test_a_wait_written_into_the_signature_is_bound(self) -> None:
    """A WAIT no line binds is bound at the name of its late class."""
    space = self._makeSpace('BindsInline')
    wait = WAIT['InlineLate']
    waitingOverload = CuteOverload(wait)(self._first)
    space['meet'] = waitingOverload
    self.assertIs(dict.__getitem__(space, 'InlineLate'), wait)
    self.assertIs(space['InlineLate'], wait)
    self.assertEqual(waitingOverload.getSignatureEntries(), (wait,))
    kept = (('meet', waitingOverload),)
    self.assertEqual(space.getWaitingOverloads(), kept)
    self.assertIs(space.compile()['InlineLate'], wait)

  def test_one_wait_for_each_late_class(self) -> None:
    """Written twice, or beside its line, a WAIT is one and the same."""
    with self.subTest(written='twice into signatures'):
      space = self._makeSpace('InlineTwice')
      first, second = WAIT['TwiceInlineLate'], WAIT['TwiceInlineLate']
      space['meet'] = CuteOverload(first)(self._first)
      space['greet'] = CuteOverload(int, second)(self._second)
      self.assertIs(dict.__getitem__(space, 'TwiceInlineLate'), first)
      (_, met), (_, greeted) = space.getWaitingOverloads()
      self.assertEqual(met.getSignatureEntries(), (first,))
      self.assertEqual(greeted.getSignatureEntries(), (int, first))
    with self.subTest(written='below its own line'):
      space = self._makeSpace('InlineBelow')
      wait = self._bindWait(space, 'BelowLineLate')
      space['meet'] = CuteOverload(WAIT['BelowLineLate'])(self._first)
      (_, met), = space.getWaitingOverloads()
      self.assertEqual(met.getSignatureEntries(), (wait,))
      self.assertIs(dict.__getitem__(space, 'BelowLineLate'), wait)
    with self.subTest(written='above its own line'):
      space = self._makeSpace('InlineAbove')
      space['meet'] = CuteOverload(WAIT['AboveLineLate'])(self._first)
      wait = self._bindWait(space, 'AboveLineLate')
      self.assertIs(space.compile()['AboveLineLate'], wait)
      (_, met), = space.getWaitingOverloads()
      self.assertEqual(met.getSignatureEntries(), (wait,))
    with self.subTest(written='at a name of its own choosing'):
      space = self._makeSpace('InlineNamed')
      wait = WAIT['NamedLate']
      space['Thread'] = wait
      space['meet'] = CuteOverload(WAIT['NamedLate'])(self._first)
      (_, met), = space.getWaitingOverloads()
      self.assertEqual(met.getSignatureEntries(), (wait,))
      self.assertFalse(dict.__contains__(space, 'NamedLate'))

  def test_two_late_classes_written_into_one_signature(self) -> None:
    """Each WAIT of a signature is bound at the name of its own class."""

    class LateOne:
      pass

    class LateTwo:
      pass

    space = self._makeSpace('InlinePair')
    one, two = WAIT['PairFirst'], WAIT['PairSecond']
    space['join'] = CuteOverload(one, int, two)(self._first)
    self.assertIs(dict.__getitem__(space, 'PairFirst'), one)
    self.assertIs(dict.__getitem__(space, 'PairSecond'), two)
    self.assertEqual(space.nameLateClass(one, LateOne), ())
    self.assertEqual(space.nameLateClass(two, LateTwo), ('join',))
    named = [(LateOne, int, LateTwo)]
    self.assertEqual(self._onRecord(space, 'join'), named)

  def test_the_body_can_read_the_name_again(self) -> None:
    """A name bound to a waiting signature still reads as bound."""
    space = self._makeSpace('ReadsAgain')
    wait = self._bindWait(space, 'AgainLate')
    waitingOverload = CuteOverload(wait)(self._first)
    space['meet'] = waitingOverload
    self.assertIs(space['meet'], waitingOverload)

  def test_everything_else_goes_to_worktoy_as_it_is(self) -> None:
    """A plain value is stored, and worktoy's record is put on record."""
    space = self._makeSpace('PassesOn')
    space['size'] = 7
    space['meet'] = CuteOverload(int)(self._first)
    self.assertEqual(dict.__getitem__(space, 'size'), 7)
    self.assertFalse(dict.__contains__(space, 'meet'))
    self.assertEqual(self._onRecord(space, 'meet'), [(int,)])
    self.assertEqual(space.getWaitingOverloads(), ())

  def test_the_kind_of_method_is_noted(self) -> None:
    """A kind written above or below a waiting signature is noted."""
    space = self._makeSpace('NotesKinds')
    wait = self._bindWait(space, 'KindsLate')
    space['above'] = staticmethod(CuteOverload(wait)(self._first))
    space['below'] = CuteOverload(wait)(classmethod(self._second))
    space['neither'] = CuteOverload(wait)(self._third)
    kinds = space.getMethodKinds()
    self.assertIs(kinds['above'], staticmethod)
    self.assertIs(kinds['below'], classmethod)
    self.assertIsNone(kinds['neither'])
    for _, waitingOverload in space.getWaitingOverloads():
      self.assertIsInstance(waitingOverload, WaitingOverload)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  WHAT IT REFUSES  # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def test_plain_definition_then_waiting_signature(self) -> None:
    """A waiting signature at a plainly defined name is refused."""
    space = self._makeSpace('PlainFirst')
    wait = self._bindWait(space, 'PlainFirstLate')
    space['meet'] = self._first
    with self.assertRaises(OverloadConflict):
      space['meet'] = CuteOverload(wait)(self._second)
    self.assertEqual(space.getWaitingOverloads(), ())

  def test_waiting_signature_then_plain_definition(self) -> None:
    """A plain definition at the name of a waiting signature is refused."""
    space = self._makeSpace('PlainSecond')
    wait = self._bindWait(space, 'PlainSecondLate')
    space['meet'] = CuteOverload(wait)(self._first)
    with self.assertRaises(OverloadConflict):
      space['meet'] = self._second
    self.assertEqual(len(space.getWaitingOverloads()), 1)

  def test_two_kinds_of_method_at_one_name(self) -> None:
    """A name is one kind of method, waiting signatures included."""
    with self.subTest(order='the waiting signature first'):
      space = self._makeSpace('KindFirst')
      wait = self._bindWait(space, 'TwoKindLate')
      space['meet'] = staticmethod(CuteOverload(wait)(self._first))
      with self.assertRaises(MixedMethodKind):
        space['meet'] = CuteOverload(int)(self._second)
    with self.subTest(order='the waiting signature last'):
      space = self._makeSpace('KindLast')
      wait = self._bindWait(space, 'TwoKindLate')
      space['meet'] = CuteOverload(int)(self._first)
      with self.assertRaises(MixedMethodKind):
        space['meet'] = staticmethod(CuteOverload(wait)(self._second))
    with self.subTest(order='both kinds on one function'):
      space = self._makeSpace('KindBoth')
      wait = self._bindWait(space, 'TwoKindLate')
      both = classmethod(CuteOverload(wait)(staticmethod(self._first)))
      with self.assertRaises(MixedMethodKind):
        space['meet'] = both

  def test_deleting_the_name_of_a_waiting_signature(self) -> None:
    """A body deleting such a name is refused when the class is made."""
    space = self._makeSpace('DeletesOne')
    wait = self._bindWait(space, 'DeletesLate')
    space['meet'] = CuteOverload(wait)(self._first)
    del space['meet']
    with self.assertRaises(ClaimedName):
      space.compile()

  def test_worktoy_screens_the_name_of_a_waiting_signature(self) -> None:
    """A waiting signature is refused at a name worktoy refuses."""
    refusals = (
      ('__del__', DelException),
      ('__slots__', SlotsRefused),
      ('__setname__', QuestionableSyntax),
      ('__class_call__', UnboundClassHook),
    )
    for name, refusal in refusals:
      with self.subTest(name=name):
        space = self._makeSpace('Screened')
        wait = self._bindWait(space, 'ScreenedLate')
        waitingOverload = CuteOverload(wait)(self._first)
        with self.assertRaises(refusal):
          space[name] = waitingOverload
        self.assertEqual(space.getWaitingOverloads(), ())

  def test_a_class_hook_takes_a_waiting_classmethod(self) -> None:
    """A class hook takes a waiting signature under '@classmethod'."""
    space = self._makeSpace('HookedClass')
    wait = self._bindWait(space, 'HookedLate')
    waitingOverload = CuteOverload(wait)(self._first)
    space['__class_call__'] = classmethod(waitingOverload)
    kept = (('__class_call__', waitingOverload),)
    self.assertEqual(space.getWaitingOverloads(), kept)
    self.assertIs(space.getMethodKinds()['__class_call__'], classmethod)

  def test_a_name_taken_keeps_a_wait_from_being_bound(self) -> None:
    """A WAIT no line binds is refused when its name is taken."""
    takers = dict(
        number=7, function=self._first,
        record=CuteOverload(int)(self._first),
    )
    for taker, value in takers.items():
      with self.subTest(taker=taker):
        space = self._makeSpace('NameTaken')
        space['TakenLate'] = value
        waitingOverload = CuteOverload(WAIT['TakenLate'])(self._second)
        with self.assertRaises(TypeError) as context:
          space['meet'] = waitingOverload
        self.assertIs(type(context.exception), TypeError)
        self.assertIn("'NameTaken.meet'", str(context.exception))
        self.assertIn("'TakenLate'", str(context.exception))
        self.assertEqual(space.getWaitingOverloads(), ())

  def test_a_wait_unbound_before_the_body_ends_is_refused(self) -> None:
    """A WAIT named in a signature must still be bound as the body ends."""
    with self.subTest(wait='its name deleted'):
      space = self._makeSpace('DropsWait')
      wait = self._bindWait(space, 'DropsLate')
      space['meet'] = CuteOverload(wait)(self._first)
      del space['DropsLate']
      with self.assertRaises(TypeError) as context:
        space.compile()
      self.assertIs(type(context.exception), TypeError)
      self.assertIn("'DropsWait.meet'", str(context.exception))
    with self.subTest(wait='its name bound to something else'):
      space = self._makeSpace('SwapsWait')
      wait = self._bindWait(space, 'SwapsLate')
      space['meet'] = CuteOverload(wait)(self._first)
      space['SwapsLate'] = 7
      with self.assertRaises(TypeError) as context:
        space.compile()
      self.assertIs(type(context.exception), TypeError)
    with self.subTest(wait='left where it is'):
      space = self._makeSpace('KeepsWait')
      wait = self._bindWait(space, 'LeftLate')
      space['meet'] = CuteOverload(wait)(self._first)
      self.assertIs(space.compile()['LeftLate'], wait)

  def test_two_functions_at_one_waiting_signature(self) -> None:
    """The second function at one waiting signature is refused."""
    with self.subTest(named='by the same WAIT'):
      space = self._makeSpace('TwoAtOne')
      wait = self._bindWait(space, 'TwoAtOneLate')
      first = CuteOverload(int, wait)(self._first)
      space['meet'] = first
      with self.assertRaises(DuplicateSignature):
        space['meet'] = CuteOverload(int, wait)(self._second)
      self.assertEqual(space.getWaitingOverloads(), (('meet', first),))
    with self.subTest(named='by two WAITs for one late class'):
      space = self._makeSpace('TwoNames')
      wait, again = WAIT['TwoNamesLate'], WAIT['TwoNamesLate']
      space['Late'], space['Again'] = wait, again
      space['meet'] = CuteOverload(wait)(self._first)
      with self.assertRaises(DuplicateSignature):
        space['meet'] = CuteOverload(again)(self._second)
    with self.subTest(named='at another name'):
      space = self._makeSpace('OtherName')
      wait = self._bindWait(space, 'OtherNameLate')
      space['meet'] = CuteOverload(wait)(self._first)
      space['greet'] = CuteOverload(wait)(self._second)
      self.assertEqual(len(space.getWaitingOverloads()), 2)

  def test_waiting_signatures_that_differ_are_all_kept(self) -> None:
    """Signatures that will not be one signature stand side by side."""
    space = self._makeSpace('SideBySide')
    wait = self._bindWait(space, 'SideLate')
    other = self._bindWait(space, 'SideOther')
    space['meet'] = CuteOverload(wait)(self._first)
    space['meet'] = CuteOverload(other)(self._second)
    space['meet'] = CuteOverload(wait, int)(self._third)
    space['meet'] = CuteOverload(int, wait)(self._first)
    space['meet'] = CuteOverload(wait, wait)(self._second)
    self.assertEqual(len(space.getWaitingOverloads()), 5)

  def test_one_function_written_twice_is_taken_once(self) -> None:
    """One function twice at one waiting signature is no mistake."""

    class Late:
      pass

    space = self._makeSpace('WrittenTwice')
    wait = self._bindWait(space, 'WrittenTwiceLate')
    space['meet'] = CuteOverload(wait)(self._first)
    space['meet'] = CuteOverload(wait)(self._first)
    self.assertEqual(len(space.getWaitingOverloads()), 1)
    self.assertEqual(space.nameLateClass(wait, Late), ('meet',))
    self.assertEqual(self._onRecord(space, 'meet'), [(Late,)])

  def test_a_waiting_signature_is_bound_once(self) -> None:
    """Binding one waiting signature a second time is refused."""
    for secondName in ('__radd__', '__add__'):
      with self.subTest(secondName=secondName):
        space = self._makeSpace('BoundTwice')
        wait = self._bindWait(space, 'TwiceLate')
        waitingOverload = CuteOverload(wait)(self._first)
        space['__add__'] = waitingOverload
        with self.assertRaises(ReboundOverload):
          space[secondName] = waitingOverload
        kept = (('__add__', waitingOverload),)
        self.assertEqual(space.getWaitingOverloads(), kept)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  WHAT IT PUTS BACK  # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def test_signature_goes_back_where_it_was_written(self) -> None:
    """A signature put back lands between its neighbours, not last."""

    class Late:
      pass

    places = dict(first=(0, 1, 2), middle=(1, 0, 2), last=(1, 2, 0))
    for place, order in places.items():
      with self.subTest(written=place):
        space = self._makeSpace('Places%s' % place.capitalize())
        wait = self._bindWait(space, 'PlacesLate')
        written = [
            CuteOverload(wait)(self._first),
            CuteOverload(int)(self._second),
            CuteOverload(str)(self._third),
        ]
        written = [written[at] for at in order]
        for record in written:
          space['meet'] = record
        self.assertEqual(space.nameLateClass(wait, Late), ('meet',))
        expected = [((Late,), (int,), (str,))[at] for at in order]
        self.assertEqual(self._onRecord(space, 'meet'), expected)
        self.assertEqual(space.getWaitingOverloads(), ())

  def test_only_the_signatures_of_that_wait_go_back(self) -> None:
    """A signature waiting for another class stays where it is."""

    class Late:
      pass

    space = self._makeSpace('OnlyThatOne')
    wait = self._bindWait(space, 'OnlyThatLate')
    other = self._bindWait(space, 'OnlyOtherLate')
    space['meet'] = CuteOverload(wait)(self._first)
    space['greet'] = CuteOverload(other)(self._second)
    self.assertEqual(space.nameLateClass(wait, Late), ('meet',))
    self.assertEqual(self._onRecord(space, 'meet'), [(Late,)])
    self.assertEqual(self._onRecord(space, 'greet'), [])
    waiting = space.getWaitingOverloads()
    self.assertEqual([name for name, _ in waiting], ['greet'])

  def test_two_waits_in_one_signature(self) -> None:
    """A signature naming two late classes goes back after the second."""

    class LateOne:
      pass

    class LateTwo:
      pass

    space = self._makeSpace('TwoInOne')
    one = self._bindWait(space, 'TwoInOneFirst')
    two = self._bindWait(space, 'TwoInOneSecond')
    space['join'] = CuteOverload(one, int, two)(self._first)
    self.assertEqual(space.nameLateClass(two, LateTwo), ())
    self.assertEqual(self._onRecord(space, 'join'), [])
    (_, waitingOverload), = space.getWaitingOverloads()
    halfNamed = (one, int, LateTwo)
    self.assertEqual(waitingOverload.getSignatureEntries(), halfNamed)
    self.assertEqual(space.nameLateClass(one, LateOne), ('join',))
    allNamed = [(LateOne, int, LateTwo)]
    self.assertEqual(self._onRecord(space, 'join'), allNamed)
    self.assertEqual(space.getWaitingOverloads(), ())

  def test_several_names_are_given_once_each(self) -> None:
    """Each name that got a signature back is given once, in order."""

    class Late:
      pass

    space = self._makeSpace('SeveralNames')
    wait = self._bindWait(space, 'SeveralLate')
    space['meet'] = CuteOverload(wait)(self._first)
    space['greet'] = CuteOverload(wait)(self._second)
    space['meet'] = CuteOverload(wait, int)(self._third)
    self.assertEqual(space.nameLateClass(wait, Late), ('meet', 'greet'))
    self.assertEqual(self._onRecord(space, 'meet'), [(Late,), (Late, int)])
    self.assertEqual(self._onRecord(space, 'greet'), [(Late,)])

  def test_naming_a_late_class_is_all_or_nothing(self) -> None:
    """A late class worktoy refuses leaves the namespace as it was."""

    class Late:
      pass

    space = self._makeSpace('AllOrNothing')
    wait = self._bindWait(space, 'RefusedLate')
    space['meet'] = CuteOverload(str)(self._first)
    space['meet'] = CuteOverload(wait, int)(self._first)
    space['meet'] = CuteOverload(Late)(self._second)
    space['meet'] = CuteOverload(wait)(self._third)
    before = space.getWaitingOverloads()
    #  '(wait, int)' goes back first. Then '(wait)' meets '(Late)' of
    #  another function, and worktoy refuses it.
    with self.assertRaises(DuplicateSignature):
      space.nameLateClass(wait, Late)
    self.assertEqual(space.getWaitingOverloads(), before)
    self.assertEqual(self._onRecord(space, 'meet'), [(str,), (Late,)])
    for _, waitingOverload in before:
      self.assertIn(wait, waitingOverload.getSignatureEntries())

  def test_records_are_kept_and_put_back(self) -> None:
    """'restoreRecords' puts back what 'keepRecords' copied."""

    class Late:
      pass

    space = self._makeSpace('KeepsRecords')
    wait = self._bindWait(space, 'RecordsLate')
    space['meet'] = CuteOverload(int)(self._first)
    waitingOverload = CuteOverload(wait)(self._second)
    space['meet'] = waitingOverload
    records = space.keepRecords()
    self.assertEqual(space.nameLateClass(wait, Late), ('meet',))
    self.assertEqual(self._onRecord(space, 'meet'), [(int,), (Late,)])
    space.restoreRecords(records)
    self.assertEqual(self._onRecord(space, 'meet'), [(int,)])
    kept = (('meet', waitingOverload),)
    self.assertEqual(space.getWaitingOverloads(), kept)
    self.assertEqual(waitingOverload.getSignatureEntries(), (wait,))
    #  From there the late class is named as if for the first time.
    self.assertEqual(space.nameLateClass(wait, Late), ('meet',))
    self.assertEqual(self._onRecord(space, 'meet'), [(int,), (Late,)])

  def test_naming_a_class_nothing_waits_for(self) -> None:
    """A WAIT no signature names gives nothing back and changes nothing."""

    class Late:
      pass

    space = self._makeSpace('NothingWaits')
    space['meet'] = CuteOverload(int)(self._first)
    self.assertEqual(space.nameLateClass(WAIT['NothingLate'], Late), ())
    self.assertEqual(self._onRecord(space, 'meet'), [(int,)])

  def test_name_late_class_checks_what_it_is_given(self) -> None:
    """'nameLateClass' refuses anything but a WAIT and a class."""
    space = self._makeSpace('ChecksGiven')
    wait = WAIT['ChecksLate']
    with self.subTest(wrong='text where the WAIT belongs'):
      with self.assertRaises(TypeException):
        space.nameLateClass('ChecksLate', BaseObject)
    with self.subTest(wrong='text where the class belongs'):
      with self.assertRaises(TypeException):
        space.nameLateClass(wait, 'ChecksLate')
