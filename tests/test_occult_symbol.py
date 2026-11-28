"""
TestOccultSymbol tests 'Symbol', one entry of the list of names a shared
object offers.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

from worktoy.work_test import BaseTest

from cutienator.occult import Symbol


class TestOccultSymbol(BaseTest):
  """
  Tests 'Symbol': its five values, that nothing changes them once made,
  how two of them compare, and which kinds of entry are code.

  What to know before adding a test
  ---------------------------------

  - A 'Symbol' is made from five plain values, so every test makes its
    own; nothing of a real shared object is read here. 'SharedObject'
    makes them from a file, and its test reads one.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  HELPERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def _make(**changed: object) -> Symbol:
    """A symbol of QTimer::start, with any of its five values changed."""
    values = dict(
        mangled='_ZN6QTimer5startEv', readable='QTimer::start()',
        kind='T', position=4096, version='Qt_6',
    )
    values.update(changed)
    return Symbol(**values)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  VALUES   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def test_the_five_values_are_kept(self) -> None:
    """Each value given to the constructor is read back as given."""
    symbol = self._make()
    self.assertEqual(symbol.mangled, '_ZN6QTimer5startEv')
    self.assertEqual(symbol.readable, 'QTimer::start()')
    self.assertEqual(symbol.kind, 'T')
    self.assertEqual(symbol.position, 4096)
    self.assertEqual(symbol.version, 'Qt_6')

  def test_the_values_lie_in_slots(self) -> None:
    """The five values lie in slots, so a symbol has no '__dict__'."""
    symbol = self._make()
    self.assertEqual(
        Symbol.__slots__,
        ('mangled', 'readable', 'kind', 'position', 'version'))
    self.assertFalse(hasattr(symbol, '__dict__'))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTHING CHANGES IT   # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def test_setting_a_value_is_refused(self) -> None:
    """Setting any value, or a name it has not, raises and names it."""
    symbol = self._make()
    for name in (*Symbol.__slots__, 'other'):
      with self.subTest(name=name):
        with self.assertRaises(AttributeError) as caught:
          setattr(symbol, name, 'changed')
        self.assertIn("'%s' was not set" % name, str(caught.exception))
    self.assertEqual(symbol, self._make())

  def test_deleting_a_value_is_refused(self) -> None:
    """Deleting any value raises and names it, and the value stays."""
    symbol = self._make()
    for name in Symbol.__slots__:
      with self.subTest(name=name):
        with self.assertRaises(AttributeError) as caught:
          delattr(symbol, name)
        self.assertIn("'%s' was not deleted" % name, str(caught.exception))
    self.assertEqual(symbol, self._make())

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  COMPARING  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def test_symbols_of_the_same_five_values_are_equal(self) -> None:
    """Two symbols made of the same values are equal and hash alike."""
    first, second = self._make(), self._make()
    self.assertIsNot(first, second)
    self.assertEqual(first, second)
    self.assertEqual(hash(first), hash(second))
    self.assertEqual(len({first, second}), 1)

  def test_one_value_apart_makes_them_unequal(self) -> None:
    """A symbol differing in any one of the five values is not equal."""
    others = dict(
        mangled='_ZN6QTimer4stopEv', readable='QTimer::stop()', kind='D',
        position=8192, version='',
    )
    for name, value in others.items():
      with self.subTest(name=name):
        self.assertNotEqual(self._make(), self._make(**{name: value}))

  def test_a_symbol_is_not_equal_to_other_things(self) -> None:
    """Compared with what is no symbol, '__eq__' leaves it to the other."""
    symbol = self._make()
    self.assertIs(symbol.__eq__(symbol.mangled), NotImplemented)
    self.assertNotEqual(symbol, symbol.mangled)
    self.assertNotEqual(symbol, symbol._getValues())

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  TEXT   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def test_str_is_the_readable_name(self) -> None:
    """'str' gives the name as C++ source writes it."""
    self.assertEqual(str(self._make()), 'QTimer::start()')

  def test_repr_names_both_spellings(self) -> None:
    """'repr' gives the class, the readable name and the stored one."""
    self.assertEqual(
        repr(self._make()),
        "<Symbol 'QTimer::start()' stored as '_ZN6QTimer5startEv'>")

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CODE OR DATA   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def test_the_letters_of_code_are_functions(self) -> None:
    """Each letter 'nm' prints for code makes a function."""
    for kind in ('T', 't', 'W', 'w', 'i'):
      with self.subTest(kind=kind):
        self.assertIs(self._make(kind=kind).isFunction(), True)

  def test_the_letters_of_data_are_not_functions(self) -> None:
    """A letter 'nm' prints for data, or for nothing known, is no
    function."""
    for kind in ('D', 'd', 'R', 'r', 'B', 'b', 'U', 'V', ''):
      with self.subTest(kind=kind):
        self.assertIs(self._make(kind=kind).isFunction(), False)
