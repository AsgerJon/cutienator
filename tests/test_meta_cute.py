"""
TestMetaCute tests 'MetaCute', the metaclass that makes the cute classes.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload
from worktoy.mcls import BaseObject, BaseSpace
from worktoy.waitaminute import MissingVariable, TypeException
from worktoy.waitaminute.dispatch import DispatchException
from worktoy.waitaminute.dispatch import DuplicateSignature
from worktoy.waitaminute.meta import OverloadConflict, MixedMethodKind
from worktoy.waitaminute.meta import DelException, QuestionableSyntax
from worktoy.waitaminute.meta import ReboundOverload
from worktoy.work_test import BaseTest

from cutienator.cute import MetaCute, CuteSpace, WAIT

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Any, Callable


class TestMetaCute(BaseTest):
  """
  Tests what 'MetaCute' does as it makes cute classes: the namespace it
  gives their bodies, the note it takes of a class that waits for a
  late class, and what it settles when the late class is made. 'WAIT'
  explains the words used here.

  Run with the source folder on the path:

    PYTHONPATH=src python -m unittest discover -s tests

  What to know before adding a test
  ---------------------------------

  - 'MetaCute' knows a class by its name alone, and keeps one list of
    made classes and one of waiting fields for the whole program. Every
    test therefore makes its own classes, inside the test, under names
    no other test uses: each test has a word of its own that begins
    every class name in it, as 'Ring' in 'RingEarly' and 'RingLate'.
  - For the same reason no test may expect 'getStillWaiting' to be
    empty. A test asks whether its own name is in it, or is not.
  - A test that leaves a late class unmade leaves its name on that list
    for the rest of the run. Each test here makes every late class it
    waits for.
  - The bodies write '@overload(...)' with worktoy's 'overload', as a
    cute class file does. That it is 'CuteOverload' underneath is what
    several of the tests show.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  HELPERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def _raisedBy(self, make: Callable) -> BaseException:
    """
    Calls 'make', which is expected to raise, and gives what it raised.

    Before Python 3.12 an exception raised while a class is being made,
    from the '__set_name__' of something in its body, arrives wrapped in
    a 'RuntimeError'. The exception inside is given then, so a test
    reads the same on every Python.
    """
    try:
      make()
    except Exception as exception:
      if type(exception) is RuntimeError and exception.__cause__:
        return exception.__cause__
      return exception
    self.fail('Nothing was raised.')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  THE NAMESPACE OF A CUTE CLASS  # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def test_body_runs_in_a_cute_space(self) -> None:
    """A cute class, and a class built on it, has a CuteSpace."""

    class SpaceTop(BaseObject, metaclass=MetaCute):
      pass

    class SpaceBelow(SpaceTop):
      pass

    for cuteClass in (SpaceTop, SpaceBelow):
      with self.subTest(cuteClass=cuteClass.__name__):
        self.assertIs(type(cuteClass), MetaCute)
        self.assertIsInstance(cuteClass.getNamespace(), CuteSpace)

  def test_overloads_with_nothing_late(self) -> None:
    """A cute class waiting for nothing overloads as any worktoy class."""

    class NothingLate(BaseObject, metaclass=MetaCute):

      @overload(int)
      def take(self, number: int) -> str:
        return 'number'

      @overload(str)
      def take(self, text: str) -> str:
        return 'text'

    self.assertEqual(NothingLate().take(7), 'number')
    self.assertEqual(NothingLate().take('seven'), 'text')
    with self.assertRaises(DispatchException):
      NothingLate().take(object())
    self.assertEqual(NothingLate.getNamespace().getWaitingSignatures(), ())

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  WAITING  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def test_late_class_is_listed_until_made(self) -> None:
    """A late class is named by 'getStillWaiting' until it is made."""

    class ListedEarly(BaseObject, metaclass=MetaCute):
      ListedLate = WAIT['ListedLate']

    self.assertIn('ListedLate', MetaCute.getStillWaiting())

    class ListedLate(ListedEarly):
      pass

    self.assertNotIn('ListedLate', MetaCute.getStillWaiting())

  def test_name_holds_the_wait_then_the_class(self) -> None:
    """The name gives the WAIT before, and the late class after."""

    class SwapEarly(BaseObject, metaclass=MetaCute):
      SwapLate = WAIT['SwapLate']

    early = SwapEarly()
    self.assertIsInstance(SwapEarly.SwapLate, WAIT)
    self.assertEqual(SwapEarly.SwapLate.getWaitingName(), 'SwapLate')
    with self.assertRaises(MissingVariable):
      _ = early.SwapLate
    self.assertFalse(hasattr(early, 'SwapLate'))

    class SwapLate(SwapEarly):
      pass

    self.assertIs(SwapEarly.SwapLate, SwapLate)
    self.assertIs(early.SwapLate, SwapLate)

  def test_waiting_signature_is_kept_by_the_namespace(self) -> None:
    """The namespace holds a waiting signature until its class is made."""

    class StoredEarly(BaseObject, metaclass=MetaCute):
      StoredLate = WAIT['StoredLate']

      @overload(StoredLate)
      def meet(self, late: Any) -> str:
        return 'late'

    space = StoredEarly.getNamespace()
    waiting = space.getWaitingSignatures()
    self.assertEqual(len(waiting), 1)
    methodName, waitingOverload = waiting[0]
    self.assertEqual(methodName, 'meet')
    self.assertEqual(waitingOverload.getFunction().__name__, 'meet')

    class StoredLate(BaseObject, metaclass=MetaCute):
      pass

    self.assertEqual(space.getWaitingSignatures(), ())

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTLING   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def test_signature_takes_the_late_class_once_made(self) -> None:
    """A waiting signature takes nothing before, the late class after."""

    class RingEarly(BaseObject, metaclass=MetaCute):
      RingLate = WAIT['RingLate']

      @overload(RingLate)
      def meet(self, late: Any) -> str:
        return 'late'

      @overload(int)
      def meet(self, number: int) -> str:
        return 'number'

    early = RingEarly()
    self.assertEqual(early.meet(7), 'number')
    with self.assertRaises(DispatchException):
      early.meet(early)

    class RingLate(RingEarly):
      pass

    self.assertEqual(early.meet(RingLate()), 'late')
    self.assertEqual(early.meet(7), 'number')
    with self.assertRaises(DispatchException):
      early.meet(early)
    with self.assertRaises(DispatchException):
      early.meet('seven')

  def test_name_with_only_waiting_signatures(self) -> None:
    """A name whose every signature waits is on the class only after."""

    class OnlyEarly(BaseObject, metaclass=MetaCute):
      OnlyLate = WAIT['OnlyLate']

      @overload(OnlyLate)
      def meet(self, late: Any) -> str:
        return 'late'

    self.assertFalse(hasattr(OnlyEarly, 'meet'))

    class OnlyLate(BaseObject, metaclass=MetaCute):
      pass

    self.assertEqual(OnlyEarly().meet(OnlyLate()), 'late')
    with self.assertRaises(DispatchException):
      OnlyEarly().meet(OnlyEarly())

  def test_classes_built_on_the_waiting_class(self) -> None:
    """Classes built on the waiting class, before and after, are settled."""

    class BuiltEarly(BaseObject, metaclass=MetaCute):
      BuiltLate = WAIT['BuiltLate']

      @overload(BuiltLate)
      def meet(self, late: Any) -> str:
        return 'late'

      @overload(int)
      def meet(self, number: int) -> str:
        return 'number'

    class BuiltBefore(BuiltEarly):
      pass

    class BuiltLate(BuiltEarly):
      pass

    class BuiltAfter(BuiltEarly):
      pass

    for receiver in (BuiltEarly, BuiltBefore, BuiltLate, BuiltAfter):
      with self.subTest(receiver=receiver.__name__):
        self.assertEqual(receiver().meet(BuiltLate()), 'late')
        self.assertEqual(receiver().meet(7), 'number')

  def test_written_order_is_kept(self) -> None:
    """A signature put back lands where it was written, not at the end."""

    class AheadEarly(BaseObject, metaclass=MetaCute):
      AheadLate = WAIT['AheadLate']

      @overload(AheadLate)
      def meet(self, late: Any) -> str:
        return 'late'

      @overload(THIS)
      def meet(self, other: Any) -> str:
        return 'this'

    class AheadLate(AheadEarly):
      pass

    class AheadBelow(AheadLate):
      pass

    class BehindEarly(BaseObject, metaclass=MetaCute):
      BehindLate = WAIT['BehindLate']

      @overload(THIS)
      def meet(self, other: Any) -> str:
        return 'this'

      @overload(BehindLate)
      def meet(self, late: Any) -> str:
        return 'late'

    class BehindLate(BehindEarly):
      pass

    class BehindBelow(BehindLate):
      pass

    #  An object of a class built on the late class fits both signatures.
    #  worktoy asks them in the order they were written.
    with self.subTest(written='the late class first'):
      self.assertEqual(AheadEarly().meet(AheadBelow()), 'late')
      self.assertEqual(AheadEarly().meet(AheadLate()), 'late')
      self.assertEqual(AheadEarly().meet(AheadEarly()), 'this')
    with self.subTest(written='the late class last'):
      self.assertEqual(BehindEarly().meet(BehindBelow()), 'this')
      self.assertEqual(BehindEarly().meet(BehindLate()), 'late')
      self.assertEqual(BehindEarly().meet(BehindEarly()), 'this')

  def test_late_class_made_before_the_waiting_class(self) -> None:
    """A WAIT for a class made already is settled as its class is made."""

    class SoonerLate(BaseObject, metaclass=MetaCute):
      pass

    made = SoonerLate

    class SoonerEarly(BaseObject, metaclass=MetaCute):
      SoonerLate = WAIT['SoonerLate']

      @overload(SoonerLate)
      def meet(self, late: Any) -> str:
        return 'late'

    self.assertNotIn('SoonerLate', MetaCute.getStillWaiting())
    self.assertIs(SoonerEarly.SoonerLate, made)
    self.assertEqual(SoonerEarly().meet(made()), 'late')

  def test_two_late_classes_in_one_signature(self) -> None:
    """A signature naming two late classes waits until both are made."""

    class PairEarly(BaseObject, metaclass=MetaCute):
      PairOne = WAIT['PairOne']
      PairTwo = WAIT['PairTwo']

      @overload(PairOne, PairTwo)
      def join(self, one: Any, two: Any) -> str:
        return 'joined'

    class PairOne(BaseObject, metaclass=MetaCute):
      pass

    self.assertFalse(hasattr(PairEarly, 'join'))
    self.assertIn('PairTwo', MetaCute.getStillWaiting())
    self.assertNotIn('PairOne', MetaCute.getStillWaiting())

    class PairTwo(BaseObject, metaclass=MetaCute):
      pass

    self.assertEqual(PairEarly().join(PairOne(), PairTwo()), 'joined')
    with self.assertRaises(DispatchException):
      PairEarly().join(PairTwo(), PairOne())

  def test_constructor_naming_a_late_class(self) -> None:
    """A waiting signature of '__init__' is settled as any other."""

    class MadeEarly(BaseObject, metaclass=MetaCute):
      MadeLate = WAIT['MadeLate']

      @overload(MadeLate)
      def __init__(self, late: Any) -> None:
        self.madeFrom = 'late'

      @overload(int)
      def __init__(self, number: int) -> None:
        self.madeFrom = 'number'

    self.assertEqual(MadeEarly(7).madeFrom, 'number')

    class MadeLate(BaseObject, metaclass=MetaCute):
      pass

    self.assertEqual(MadeEarly(MadeLate()).madeFrom, 'late')
    self.assertEqual(MadeEarly(7).madeFrom, 'number')

  def test_static_and_class_functions(self) -> None:
    """A waiting signature may belong to a static or a class function."""

    class KindEarly(BaseObject, metaclass=MetaCute):
      KindLate = WAIT['KindLate']

      @staticmethod
      @overload(KindLate)
      def kindAbove(late: Any) -> str:
        return 'static above'

      @overload(KindLate)
      @staticmethod
      def kindBelow(late: Any) -> str:
        return 'static below'

      @classmethod
      @overload(KindLate)
      def ofClass(cls, late: Any) -> str:
        return cls.__name__

    class KindLate(BaseObject, metaclass=MetaCute):
      pass

    self.assertEqual(KindEarly.kindAbove(KindLate()), 'static above')
    self.assertEqual(KindEarly().kindBelow(KindLate()), 'static below')
    self.assertEqual(KindEarly.ofClass(KindLate()), 'KindEarly')
    with self.assertRaises(DispatchException):
      KindEarly.kindAbove(7)

  def test_wait_written_right_into_the_signature(self) -> None:
    """A WAIT written into '@overload' needs no line of its own."""

    class InlineEarly(BaseObject, metaclass=MetaCute):

      @overload(WAIT['InlineLate'])
      def meet(self, other: Any) -> str:
        return 'late'

      @overload(WAIT['InlineLate'], int)
      def meet(self, other: Any, count: int) -> str:
        return 'late and number'

      @overload(int)
      def meet(self, count: int) -> str:
        return 'number'

    class InlineChild(InlineEarly):

      @overload(str, WAIT['InlineLate'])
      def meet(self, word: str, other: Any) -> str:
        return 'word and late'

    self.assertIsInstance(InlineEarly.InlineLate, WAIT)
    self.assertIsNot(InlineChild.InlineLate, InlineEarly.InlineLate)
    self.assertIn('InlineLate', MetaCute.getStillWaiting())
    self.assertEqual(InlineEarly().meet(3), 'number')

    class InlineLate(BaseObject, metaclass=MetaCute):
      pass

    self.assertNotIn('InlineLate', MetaCute.getStillWaiting())
    self.assertIs(InlineEarly.InlineLate, InlineLate)
    self.assertIs(InlineChild.InlineLate, InlineLate)
    early, child, late = InlineEarly(), InlineChild(), InlineLate()
    self.assertEqual(early.meet(late), 'late')
    self.assertEqual(early.meet(late, 3), 'late and number')
    self.assertEqual(child.meet(late), 'late')
    self.assertEqual(child.meet('word', late), 'word and late')
    raised = self._raisedBy(lambda: early.meet('word', late))
    self.assertIs(type(raised), DispatchException)

  def test_signatures_sharing_one_function(self) -> None:
    """A waiting signature shares its function with other signatures.
    Those that do not wait work from the start, and each of the others
    once its late class is made."""

    class SharesOne(BaseObject, metaclass=MetaCute):

      @overload(WAIT['SharedLate'], int)
      @overload(WAIT['SharedLate'])
      @overload(type(None))
      @overload()
      def take(self, thing: Any = None, count: int = 1) -> tuple:
        return type(thing).__name__, count

      @staticmethod
      @overload(str)
      @overload(WAIT['SharedLate'], str)
      def make(*args: Any) -> int:
        return len(args)

      @overload(WAIT['SharedOther'])
      @overload(WAIT['SharedLate'], WAIT['SharedOther'])
      def both(self, *args: Any) -> int:
        return len(args)

    class BuiltOnShares(SharesOne):
      pass

    sharesOne, builtOn = SharesOne(), BuiltOnShares()
    self.assertEqual(sharesOne.take(), ('NoneType', 1))
    self.assertEqual(builtOn.take(None), ('NoneType', 1))
    self.assertEqual(SharesOne.make('text'), 1)
    self.assertFalse(hasattr(SharesOne, 'both'))
    with self.assertRaises(DispatchException):
      sharesOne.take(7)

    class SharedLate(BaseObject, metaclass=MetaCute):
      pass

    late = SharedLate()
    self.assertEqual(sharesOne.take(late), ('SharedLate', 1))
    self.assertEqual(sharesOne.take(late, 4), ('SharedLate', 4))
    self.assertEqual(builtOn.take(late, 5), ('SharedLate', 5))
    self.assertEqual(sharesOne.take(), ('NoneType', 1))
    self.assertEqual(SharesOne.make(late, 'text'), 2)
    self.assertEqual(BuiltOnShares.make('text'), 1)
    self.assertFalse(hasattr(SharesOne, 'both'))
    self.assertNotIn('SharedLate', MetaCute.getStillWaiting())
    self.assertIn('SharedOther', MetaCute.getStillWaiting())

    class SharedOther(BaseObject, metaclass=MetaCute):
      pass

    self.assertEqual(sharesOne.both(SharedOther()), 1)
    self.assertEqual(builtOn.both(late, SharedOther()), 2)
    self.assertNotIn('SharedOther', MetaCute.getStillWaiting())

  def test_plain_definition_below_is_left_alone(self) -> None:
    """A class defining the name plainly keeps its own definition."""

    class HideEarly(BaseObject, metaclass=MetaCute):
      HideLate = WAIT['HideLate']

      @overload(HideLate)
      def meet(self, late: Any) -> str:
        return 'late'

      @overload(int)
      def meet(self, number: int) -> str:
        return 'number'

    class HidePlain(HideEarly):

      def meet(self, anything: Any) -> str:
        return 'plain'

    class HideLate(BaseObject, metaclass=MetaCute):
      pass

    self.assertEqual(HidePlain().meet(HideLate()), 'plain')
    self.assertEqual(HideEarly().meet(HideLate()), 'late')

  def test_two_classes_waiting_for_one_late_class(self) -> None:
    """Every class waiting for a late class is settled when it is made."""

    class ShareOne(BaseObject, metaclass=MetaCute):
      ShareLate = WAIT['ShareLate']

      @overload(ShareLate)
      def meet(self, late: Any) -> str:
        return 'one'

    class ShareTwo(BaseObject, metaclass=MetaCute):
      ShareLate = WAIT['ShareLate']

      @overload(ShareLate)
      def meet(self, late: Any) -> str:
        return 'two'

    class ShareLate(BaseObject, metaclass=MetaCute):
      pass

    self.assertEqual(ShareOne().meet(ShareLate()), 'one')
    self.assertEqual(ShareTwo().meet(ShareLate()), 'two')
    self.assertIs(ShareOne.ShareLate, ShareLate)
    self.assertIs(ShareTwo.ShareLate, ShareLate)

  def test_a_late_class_settles_every_class_or_none(self) -> None:
    """A late class one waiting class refuses is settled in no class."""

    class WholeSound(BaseObject, metaclass=MetaCute):
      WholeLate = WAIT['WholeLate']

      @overload(WholeLate)
      def take(self, late: Any) -> str:
        return 'took'

    class WholeFaulty(BaseObject, metaclass=MetaCute):
      WholeLate = WAIT['WholeLate']

      @overload(WholeLate)
      def take(self, late: Any) -> str:
        return 'faulty'

    class OtherSpaceMeta(MetaCute):
      """Prepares a namespace that keeps no waiting signatures."""

      @classmethod
      def __prepare__(mcls, name: str, bases: tuple, **kwargs) -> Any:
        return BaseSpace(mcls, name, bases, **kwargs)

    class WholeChild(WholeFaulty, metaclass=OtherSpaceMeta):
      pass

    def makeLate() -> None:
      class WholeLate(BaseObject, metaclass=MetaCute):
        pass

    #  No dispatcher can be built again for 'WholeChild', so settling
    #  'WholeFaulty' is refused when the late class is made.
    self.assertIs(type(self._raisedBy(makeLate)), TypeException)
    #  The sound class was noted first and is as if nothing had run.
    self.assertIn('WholeLate', MetaCute.getStillWaiting())
    self.assertIsInstance(WholeSound.__dict__['WholeLate'], WAIT)
    self.assertFalse(hasattr(WholeSound, 'take'))
    wholeSpace = WholeSound.getNamespace()
    self.assertEqual(len(wholeSpace.getWaitingSignatures()), 1)
    #  The faulty class is given up, and is as it was too.
    self.assertIsInstance(WholeFaulty.__dict__['WholeLate'], WAIT)
    faultySpace = WholeFaulty.getNamespace()
    self.assertEqual(len(faultySpace.getWaitingSignatures()), 1)

    class WholeLate(BaseObject, metaclass=MetaCute):
      pass

    self.assertNotIn('WholeLate', MetaCute.getStillWaiting())
    self.assertIs(WholeSound.WholeLate, WholeLate)
    self.assertEqual(WholeSound().take(WholeLate()), 'took')
    self.assertFalse(hasattr(WholeFaulty, 'take'))

  def test_a_failed_class_statement_leaves_no_class_behind(self) -> None:
    """A class whose statement fails is not noted, and waits for nothing."""

    class GoneLate(BaseObject, metaclass=MetaCute):
      pass

    def makeHost() -> None:
      class GoneHost(BaseObject, metaclass=MetaCute):
        GoneOther = WAIT['GoneOther']

        @overload(GoneLate)
        def take(self, late: Any) -> str:
          return 'the class itself'

        @overload(WAIT['GoneLate'])
        def take(self, late: Any) -> str:
          return 'the same class by a WAIT'

    #  The class is made, its 'WAIT' is settled at once, and only then
    #  do the two functions meet at one signature.
    self.assertIs(type(self._raisedBy(makeHost)), DuplicateSignature)
    #  Its other waiting field went with it.
    self.assertNotIn('GoneOther', MetaCute.getStillWaiting())

    class GoneWaiter(BaseObject, metaclass=MetaCute):
      GoneHost = WAIT['GoneHost']

    #  No class named 'GoneHost' was made, so this one waits for it.
    self.assertIn('GoneHost', MetaCute.getStillWaiting())
    self.assertIsInstance(GoneWaiter.__dict__['GoneHost'], WAIT)

    class GoneHost(BaseObject, metaclass=MetaCute):
      pass

    self.assertNotIn('GoneHost', MetaCute.getStillWaiting())
    self.assertIs(GoneWaiter.GoneHost, GoneHost)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  REFUSALS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def test_wait_in_a_class_that_is_not_cute(self) -> None:
    """A WAIT in a class 'MetaCute' does not make is refused."""

    def make() -> None:
      class NotCute(BaseObject):
        NotCuteLate = WAIT['NotCuteLate']

    self.assertIsInstance(self._raisedBy(make), TypeError)
    self.assertNotIn('NotCuteLate', MetaCute.getStillWaiting())

  def test_add_waiting_checks_what_it_is_given(self) -> None:
    """'addWaiting' refuses anything but a class, a name and a WAIT."""
    wait = WAIT['CheckedLate']
    wrongOnes = dict(
        waitingClass=(7, 'CheckedLate', wait),
        fieldName=(BaseObject, 7, wait),
        wait=(BaseObject, 'CheckedLate', 'CheckedLate'),
    )
    for wrong, arguments in wrongOnes.items():
      with self.subTest(wrong=wrong):
        with self.assertRaises(TypeException):
          MetaCute.addWaiting(*arguments)
    self.assertNotIn('CheckedLate', MetaCute.getStillWaiting())

  def test_mistakes_in_a_body_are_refused_on_their_line(self) -> None:
    """A body misusing a waiting signature never becomes a class."""

    def stackedAbove() -> None:
      class StackAbove(BaseObject, metaclass=MetaCute):
        StackAboveLate = WAIT['StackAboveLate']

        @overload(StackAboveLate)
        @overload.fallback
        def take(self, thing: Any) -> str:
          return 'taken'

    def stackedBelow() -> None:
      class StackBelow(BaseObject, metaclass=MetaCute):
        StackBelowLate = WAIT['StackBelowLate']

        @overload.finalize
        @overload(StackBelowLate)
        def take(self, thing: Any) -> str:
          return 'taken'

    def plainAfter() -> None:
      class PlainAfter(BaseObject, metaclass=MetaCute):
        PlainAfterLate = WAIT['PlainAfterLate']

        @overload(PlainAfterLate)
        def take(self, thing: Any) -> str:
          return 'taken'

        def take(self, thing: Any) -> str:
          return 'plain'

    def twoKinds() -> None:
      class TwoKinds(BaseObject, metaclass=MetaCute):
        TwoKindsLate = WAIT['TwoKindsLate']

        @staticmethod
        @overload(TwoKindsLate)
        def take(thing: Any) -> str:
          return 'static'

        @overload(int)
        def take(self, thing: Any) -> str:
          return 'not static'

    def flexed() -> None:
      class Flexed(BaseObject, metaclass=MetaCute):
        FlexedLate = WAIT['FlexedLate']

        @overload.flex(int, FlexedLate)
        def take(self, number: int, thing: Any) -> str:
          return 'taken'

    def atDel() -> None:
      class AtDel(BaseObject, metaclass=MetaCute):
        AtDelLate = WAIT['AtDelLate']

        @overload(AtDelLate)
        def __del__(self, thing: Any) -> None:
          pass

    def misspelled() -> None:
      class Misspelled(BaseObject, metaclass=MetaCute):
        MisspelledLate = WAIT['MisspelledLate']

        @overload(MisspelledLate)
        def __setname__(self, thing: Any) -> None:
          pass

    def boundTwice() -> None:
      class BoundTwice(BaseObject, metaclass=MetaCute):
        BoundTwiceLate = WAIT['BoundTwiceLate']

        @overload(BoundTwiceLate)
        def __add__(self, thing: Any) -> str:
          return 'added'

        __radd__ = __add__

    def twoFunctions() -> None:
      class TwoFunctions(BaseObject, metaclass=MetaCute):
        TwoFunctionsLate = WAIT['TwoFunctionsLate']

        @overload(TwoFunctionsLate)
        def take(self, thing: Any) -> str:
          return 'first'

        @overload(TwoFunctionsLate)
        def take(self, thing: Any) -> str:
          return 'second'

    mistakes = (
        ('a waiting signature above a fallback', stackedAbove, TypeError),
        ('a finalizer above a waiting signature', stackedBelow, TypeError),
        ('a plain definition at its name', plainAfter, OverloadConflict),
        ('two kinds of method at its name', twoKinds, MixedMethodKind),
        ('a late class in overload.flex', flexed, TypeError),
        ('a waiting signature at __del__', atDel, DelException),
        ('one at a misspelled dunder', misspelled, QuestionableSyntax),
        ('one bound to a second name', boundTwice, ReboundOverload),
        ('two functions at one', twoFunctions, DuplicateSignature),
    )
    #  Each refusal must be exactly the one named. worktoy's own
    #  'TypeException' is a 'TypeError' too, and must not pass for ours.
    for mistake, make, expected in mistakes:
      with self.subTest(mistake=mistake):
        self.assertIs(type(self._raisedBy(make)), expected)
    #  No class was made, so no WAIT of these bodies was ever noted.
    stillWaiting = MetaCute.getStillWaiting()
    for lateName in ('StackAboveLate', 'StackBelowLate', 'PlainAfterLate',
                     'TwoKindsLate', 'FlexedLate', 'AtDelLate',
                     'MisspelledLate', 'BoundTwiceLate',
                     'TwoFunctionsLate'):
      with self.subTest(lateName=lateName):
        self.assertNotIn(lateName, stillWaiting)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  ONE LIST FOR ALL   # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def test_metaclass_based_on_meta_cute_shares_the_lists(self) -> None:
    """A metaclass based on 'MetaCute' waits and settles together with it."""

    class BasedMeta(MetaCute):
      pass

    class BasedEarly(BaseObject, metaclass=BasedMeta):
      BasedLate = WAIT['BasedLate']

      @overload(BasedLate)
      def meet(self, late: Any) -> str:
        return 'late'

    class OtherEarly(BaseObject, metaclass=MetaCute):
      OtherLate = WAIT['OtherLate']

      @overload(OtherLate)
      def meet(self, late: Any) -> str:
        return 'late'

    for metaclass in (MetaCute, BasedMeta):
      with self.subTest(asked=metaclass.__name__):
        self.assertIn('BasedLate', metaclass.getStillWaiting())
        self.assertIn('OtherLate', metaclass.getStillWaiting())

    class BasedLate(BaseObject, metaclass=MetaCute):
      pass

    class OtherLate(BaseObject, metaclass=BasedMeta):
      pass

    self.assertEqual(BasedEarly().meet(BasedLate()), 'late')
    self.assertEqual(OtherEarly().meet(OtherLate()), 'late')
    for metaclass in (MetaCute, BasedMeta):
      with self.subTest(asked=metaclass.__name__):
        self.assertNotIn('BasedLate', metaclass.getStillWaiting())
        self.assertNotIn('OtherLate', metaclass.getStillWaiting())
