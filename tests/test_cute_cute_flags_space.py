"""
TestCuteCuteFlagsSpace tests 'CuteFlagsSpace', the namespace the body of
a flags class runs in.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

from worktoy.work_test import BaseTest

from cutienator.cute import CuteFlags, CuteFlagsSpace, MetaCuteFlags


class TestCuteCuteFlagsSpace(BaseTest):
  """
  Tests 'CuteFlagsSpace': the flags a body declares, the C++ number the
  class statement names, and the refusals of a flag declared wrong.

  What to know before adding a test
  ---------------------------------

  - Most tests make the namespace as 'MetaCuteFlags' makes it, and put
    flags on record with 'addFlagNumber', as 'CuteFlagsHook' does; the
    body of a class statement is tested in 'TestCuteCuteFlagsHook'.
  """

  @staticmethod
  def _space(**kwargs: object) -> CuteFlagsSpace:
    """The namespace of the body of a flags class 'Option'."""
    return MetaCuteFlags.__prepare__('Option', (CuteFlags,), **kwargs)

  def test_no_flags_on_record_at_first(self) -> None:
    """Before the body binds a flag there are none."""
    space = self._space()
    self.assertIsInstance(space, CuteFlagsSpace)
    self.assertEqual(space.getFlagNumbers(), {})
    self.assertIs(space.hasFlagNumber('Wide'), False)

  def test_the_flags_on_record(self) -> None:
    """Each flag by its name, in the order declared; what is given is a
    copy; a second name for a number is fine."""
    space = self._space()
    space.addFlagNumber('Wide', 0x1)
    space.addFlagNumber('Tall', 0x2)
    space.addFlagNumber('Broad', 0x1)
    space.addFlagNumber('NULL', 0)
    self.assertEqual(space.getFlagNumbers(),
                     dict(Wide=0x1, Tall=0x2, Broad=0x1, NULL=0))
    self.assertEqual([*space.getFlagNumbers()],
                     ['Wide', 'Tall', 'Broad', 'NULL'])
    space.getFlagNumbers()['Gone'] = 4
    self.assertIs(space.hasFlagNumber('Gone'), False)
    self.assertIs(space.hasFlagNumber('Tall'), True)

  def test_a_name_declared_twice_is_refused(self) -> None:
    """A second number for a name raises, naming it."""
    space = self._space()
    space.addFlagNumber('Wide', 0x1)
    with self.assertRaises(SyntaxError) as caught:
      space.addFlagNumber('Wide', 0x2)
    self.assertIn("'Option.Wide' is declared twice", str(caught.exception))

  def test_null_is_no_flag_at_all(self) -> None:
    """'NULL' bound to a number other than 0 raises."""
    with self.assertRaises(SyntaxError) as caught:
      self._space().addFlagNumber('NULL', 4)
    self.assertIn("'Option.NULL' is bound to 4", str(caught.exception))

  def test_the_number_of_the_class(self) -> None:
    """The C++ number named with 'number=', 'int' when none is, and how
    many bits it has and whether it has a sign."""
    self.assertEqual(self._space().getNumberName(), 'int')
    self.assertEqual(self._space().getNumberLayout(), (32, True))
    for name, layout in (
        ('signed char', (8, True)), ('unsigned char', (8, False)),
        ('short', (16, True)), ('unsigned short', (16, False)),
        ('int', (32, True)), ('unsigned int', (32, False)),
        ('long long', (64, True)), ('unsigned long long', (64, False)),
    ):
      with self.subTest(name=name):
        space = CuteFlagsSpace(MetaCuteFlags, 'Option', (), number=name)
        self.assertEqual(space.getNumberName(), name)
        self.assertEqual(space.getNumberLayout(), layout)

  def test_a_number_of_no_flags_class_is_refused(self) -> None:
    """A C++ number no flags class has, or one that is no name, raises,
    naming the ones there are."""
    for number in ('float', ['int']):
      with self.subTest(number=number):
        space = CuteFlagsSpace.__new__(CuteFlagsSpace)
        space.__key_args__ = dict(number=number)
        space.__class_name__ = 'Option'
        with self.assertRaises(ValueError) as caught:
          space.getNumberLayout()
        self.assertIn("'unsigned long long'", str(caught.exception))
