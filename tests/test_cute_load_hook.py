"""
TestCuteLoadHook tests 'CuteLoadHook', which builds the overloaded
method of a name again after its class is made.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload, Dispatcher, TypeSig
from worktoy.mcls import BaseObject
from worktoy.mcls.space_hooks import LoadSpaceHook
from worktoy.waitaminute.dispatch import DispatchException
from worktoy.work_test import BaseTest

from cutienator import MetaCute, CuteSpace, CuteLoadHook

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Any


class TestCuteLoadHook(BaseTest):
  """
  Tests 'CuteLoadHook' on its own: where it sits among the hooks of a
  'CuteSpace', that it takes no part while a class is made, and what
  'buildAgain' gives for a class that exists.

  A dispatcher that 'buildAgain' gives is placed nowhere. To see what it
  takes, a test places it by hand on the class it was built for and
  calls it through an object, as 'MetaCute' does when it settles a late
  class.

  The cute classes made here wait for nothing, so no test has to mind
  the names 'MetaCute' keeps.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  HELPERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def _place(dispatcher: Dispatcher, cuteClass: type, name: str) -> Any:
    """
    Places a dispatcher on a class under a name, as if the class had
    been made with it, and gives the method of a new object of the
    class.
    """
    type.__setattr__(cuteClass, name, dispatcher)
    dispatcher.__set_name__(cuteClass, name)
    return getattr(cuteClass(), name)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  AMONG THE HOOKS  # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def test_cute_space_declares_it_after_worktoys_own(self) -> None:
    """'CuteSpace' has it as 'cuteLoadHook', after 'loadSpaceHook'."""
    self.assertIsInstance(CuteSpace.cuteLoadHook, CuteLoadHook)
    self.assertIsInstance(CuteSpace.cuteLoadHook, LoadSpaceHook)
    names = [hook.getFieldName() for hook in CuteSpace.classGetHooks()]
    self.assertIn('loadSpaceHook', names)
    self.assertIn('cuteLoadHook', names)
    worktoysOwn = names.index('loadSpaceHook')
    self.assertLess(worktoysOwn, names.index('cuteLoadHook'))
    self.assertEqual(names.count('cuteLoadHook'), 1)

  def test_takes_no_part_while_a_class_is_made(self) -> None:
    """Its three phases claim nothing and change nothing."""
    hook = CuteSpace.cuteLoadHook
    with self.subTest(phase='setItemPhase'):
      self.assertIs(hook.setItemPhase('meet', 7), False)
    with self.subTest(phase='delItemPhase'):
      self.assertIs(hook.delItemPhase('meet', 7), False)
    with self.subTest(phase='postCompilePhase'):
      compiled = dict(meet=7)
      self.assertIs(hook.postCompilePhase(compiled), compiled)
      self.assertEqual(compiled, dict(meet=7))

  def test_a_cute_class_is_made_as_any_worktoy_class(self) -> None:
    """With the hook in the namespace, each name still has one dispatcher."""

    class MadeOnce(BaseObject, metaclass=MetaCute):

      @overload(int)
      def take(self, number: int) -> str:
        return 'number'

      @overload(str)
      def take(self, text: str) -> str:
        return 'text'

    self.assertIsInstance(MadeOnce.__dict__['take'], Dispatcher)
    self.assertEqual(MadeOnce().take(7), 'number')
    self.assertEqual(MadeOnce().take('seven'), 'text')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  BUILDING AGAIN   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def test_build_again_gives_a_new_dispatcher_each_time(self) -> None:
    """'buildAgain' gives a new dispatcher and places it nowhere."""

    class BuiltNew(BaseObject, metaclass=MetaCute):

      @overload(int)
      def take(self, number: int) -> str:
        return 'number'

    own = BuiltNew.__dict__['take']
    space = BuiltNew.getNamespace()
    first = space.cuteLoadHook.buildAgain('take')
    second = space.cuteLoadHook.buildAgain('take')
    for built in (first, second):
      self.assertIsInstance(built, Dispatcher)
      self.assertIsNot(built, own)
    self.assertIsNot(first, second)
    self.assertIs(BuiltNew.__dict__['take'], own)

  def test_a_name_with_nothing_on_record_gives_none(self) -> None:
    """For a name that is not overloaded, 'buildAgain' gives None."""

    class BuiltNone(BaseObject, metaclass=MetaCute):

      def plain(self) -> str:
        return 'plain'

    space = BuiltNone.getNamespace()
    for name in ('plain', 'nothingOfTheKind'):
      with self.subTest(name=name):
        self.assertIsNone(space.cuteLoadHook.buildAgain(name))

  def test_built_again_takes_what_the_first_one_took(self) -> None:
    """Built from the same record, it takes the same calls."""

    class BuiltSame(BaseObject, metaclass=MetaCute):

      @overload(int)
      def take(self, number: int) -> str:
        return 'number'

      @overload(str)
      def take(self, text: str) -> str:
        return 'text'

    space = BuiltSame.getNamespace()
    built = space.cuteLoadHook.buildAgain('take')
    take = self._place(built, BuiltSame, 'take')
    self.assertEqual(take(7), 'number')
    self.assertEqual(take('seven'), 'text')
    with self.assertRaises(DispatchException):
      take(object())

  def test_built_again_reads_the_record_as_it_is_now(self) -> None:
    """A signature put on record after the class is made is in it."""

    class Token:
      pass

    class BuiltLater(BaseObject, metaclass=MetaCute):

      @overload(int)
      def take(self, number: int) -> str:
        return 'number'

    def takeToken(self: Any, token: Token) -> str:
      return 'token'

    with self.assertRaises(DispatchException):
      BuiltLater().take(Token())
    space = BuiltLater.getNamespace()
    space.addOverload('take', TypeSig(Token), takeToken)
    with self.assertRaises(DispatchException):
      BuiltLater().take(Token())
    built = space.cuteLoadHook.buildAgain('take')
    take = self._place(built, BuiltLater, 'take')
    self.assertEqual(take(Token()), 'token')
    self.assertEqual(take(7), 'number')

  def test_built_again_for_a_class_built_on_another(self) -> None:
    """It holds the signatures of the class and of what it is built on."""

    class BuiltTop(BaseObject, metaclass=MetaCute):

      @overload(int)
      def take(self, number: int) -> str:
        return 'number, from the top'

      @overload(str)
      def take(self, text: str) -> str:
        return 'text, from the top'

    class BuiltBelow(BuiltTop):

      @overload(str)
      def take(self, text: str) -> str:
        return 'text, from below'

    space = BuiltBelow.getNamespace()
    built = space.cuteLoadHook.buildAgain('take')
    take = self._place(built, BuiltBelow, 'take')
    self.assertEqual(take(7), 'number, from the top')
    self.assertEqual(take('seven'), 'text, from below')
    self.assertEqual(BuiltTop().take('seven'), 'text, from the top')
