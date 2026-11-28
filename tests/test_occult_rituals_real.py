"""
TestOccultRitualsReal tests 'Rituals' against the real package: its
ritual folder, its sigil files and its target file of QtCore, with the
Qt of the machine.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

import os

from worktoy.work_test import BaseTest

from cutienator import occult
from cutienator.occult import Rituals

#  Rituals of QtCore the tests run.
_MAKE = 'ritual_ZN7QObjectC1EPS_'
_DELETE = 'ritual_ZN7QObjectD1Ev'
_NAME = 'ritual_ZNK7QObject10objectNameEv'
_SET_NAME = 'ritual_ZN7QObject13setObjectNameE14QAnyStringView'


class TestOccultRitualsReal(BaseTest):
  """
  Tests what 'Rituals' does with the package as it is shipped: where it
  finds its ritual files, which parts have cute classes, and the target
  file of QtCore opened and run, text crossing both ways.

  What to know before adding a test
  ---------------------------------

  - These tests need the target file of QtCore built, as every test of a
    cute class does. They open it, and it stays open for the rest of
    the program, as it would in any program using cutienator.
  - The rules of 'Rituals' apart from the real package are tested by
    'TestOccultRituals', on a package made up for each test.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  THE PACKAGE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def test_the_ritual_folder_lies_beside_the_module(self) -> None:
    """The ritual files lie in 'rituals' beside the package 'occult'."""
    here = os.path.dirname(os.path.abspath(occult.__file__))
    self.assertEqual(
        Rituals.getRitualFolder(), os.path.join(here, 'rituals'))
    self.assertTrue(os.path.isdir(Rituals.getPartFolder('QtCore')))

  def test_the_parts_with_cute_classes(self) -> None:
    """The parts of Qt that are packages of cutienator, found once."""
    kept = Rituals.__cute_parts__
    try:
      Rituals.__cute_parts__ = None
      found = Rituals.getComponents()
      self.assertIn('QtCore', found)
      self.assertEqual(found, tuple(sorted(found)))
      self.assertIs(Rituals.getComponents(), found)
    finally:
      Rituals.__cute_parts__ = kept

  def test_qtcore_offers_the_rituals_of_text(self) -> None:
    """QtCore lists and offers the four rituals text crosses by, and a
    part of text needs nothing more."""
    for name in Rituals._getTextRituals():
      with self.subTest(name=name):
        self.assertIn('QtCore', Rituals.getPartsOf(name))
    Rituals._checkTextRituals('QtCore')
    opened = Rituals.getOpened('QtCore')
    for name in Rituals._getTextRituals():
      with self.subTest(name=name):
        self.assertNotIn(name, Rituals.getMissing('QtCore'))
        self.assertTrue(hasattr(opened, name))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  TEXT   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def test_a_text_made_read_and_dropped(self) -> None:
    """A 'str' made a text of Qt reads back the same, letters beyond
    the first plane and lone surrogates too."""
    for text in ('', 'cute', 'rätsel ☃ 𝄞', 'lone \ud800 half'):
      with self.subTest(text=text):
        address = Rituals.giveText(text)
        try:
          self.assertEqual(Rituals.takeText(address), text)
        finally:
          Rituals._dropText(address)

  def test_a_ritual_taking_and_giving_text(self) -> None:
    """The name of a real QObject is set by a ritual taking text and read
    by one giving it."""
    address = Rituals.call(_MAKE, None)
    try:
      self.assertEqual(Rituals.call(_NAME, address), '')
      Rituals.call(_SET_NAME, address, 'cutie ☃ 𝄞')
      self.assertEqual(Rituals.call(_NAME, address), 'cutie ☃ 𝄞')
      self.assertEqual(
          Rituals.callFrom('QtCore', _NAME, address), 'cutie ☃ 𝄞')
    finally:
      Rituals.call(_DELETE, address)
