"""
TestCuteUnsupportedMeta tests 'UnsupportedMeta', which makes the classes
that stand in a cute class for a class of Qt with no cute class yet.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

from unittest import mock

from worktoy.work_test import BaseTest

from cutienator.cute import MetaCute, UnsupportedMeta, WAIT


class TestCuteUnsupportedMeta(BaseTest):
  """
  Tests 'UnsupportedMeta': a stand-in refuses to be called and refuses
  every attribute it does not have, saying what it stands for, and one
  of a class of Qt is noted, so a 'WAIT' for that class settles on it.

  What to know before adding a test
  ---------------------------------

  - 'MetaCute' keeps the classes made, and the fields waiting, for the
    whole program. Each test here has a fresh record of both, in
    'setUp', so nothing it makes reaches the classes of the package.
  """

  def setUp(self) -> None:
    """A fresh record of the classes made and of the fields waiting."""
    super().setUp()
    for name in ('__made_classes__', '__waiting_fields__'):
      patcher = mock.patch.object(MetaCute, name, dict())
      patcher.start()
      self.addCleanup(patcher.stop)

  def test_a_stand_in_cannot_be_called(self) -> None:
    """Calling a stand-in raises, naming it and what it stands for."""

    class QGone(metaclass=UnsupportedMeta):
      """The class 'QGone' of Qt, which has no cute class yet."""

    with self.assertRaises(NotImplementedError) as caught:
      QGone(1, key=2)
    said = str(caught.exception)
    self.assertIn("'%s' cannot be called" % QGone.__qualname__, said)
    self.assertIn("The class 'QGone' of Qt, which has no cute", said)

  def test_a_stand_in_has_no_attributes_of_its_own(self) -> None:
    """An attribute it has not raises, saying what it stands for; a
    dunder it has not is an ordinary 'AttributeError'."""

    class QGone(metaclass=UnsupportedMeta):
      """Stands for QGone."""

    with self.assertRaises(NotImplementedError) as caught:
      QGone.size
    self.assertIn("has no attribute 'size'", str(caught.exception))
    self.assertIn('Stands for QGone.', str(caught.exception))
    with self.assertRaises(AttributeError) as caught:
      QGone.__wrapped__
    self.assertNotIsInstance(caught.exception, NotImplementedError)
    self.assertFalse(hasattr(QGone, '__length_hint__'))

  def test_the_info_of_a_stand_in(self) -> None:
    """Its docstring on one line, or nothing without one."""

    class QGone(metaclass=UnsupportedMeta):
      """
      Stands for
        QGone.
      """

    class QNoDoc(metaclass=UnsupportedMeta):
      pass

    self.assertEqual(QGone.getInfo(), 'Stands for QGone.')
    self.assertEqual(QNoDoc.getInfo(), '')

  def test_a_stand_in_of_a_class_of_qt_is_noted(self) -> None:
    """A stand-in naming its class of Qt is noted by that name, and a
    'WAIT' for it settles on it; one naming none is not noted."""

    class QWaiter(metaclass=MetaCute):
      Later = WAIT['QStoodIn']

    self.assertIsInstance(QWaiter.__dict__['Later'], WAIT)

    class QStoodIn(metaclass=UnsupportedMeta):
      __qt_class__ = 'QStoodIn'

    class QPlain(metaclass=UnsupportedMeta):
      pass

    self.assertIs(QWaiter.Later, QStoodIn)
    made = MetaCute._getMadeClasses()
    self.assertIs(made['QStoodIn'], QStoodIn)
    self.assertNotIn('QPlain', made)
