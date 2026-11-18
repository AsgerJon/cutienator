from __future__ import annotations

from typing import TYPE_CHECKING
from unittest import TestCase

from worktoy.dispatch import overload
from worktoy.mcls import BaseSpace
from worktoy.waitaminute import TypeException

from cutienator import MetaCute, WAIT

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Any


class TestWaitSettleRaises(TestCase):

  def test_settling_that_raises_keeps_the_rest(self) -> None:
    """Keep the other waiting fields when settling one of them raises."""

    class FaultyHost(metaclass=MetaCute):
      KeptLate = WAIT['KeptLate']

      @overload(KeptLate)
      def take(self, late: Any) -> str:
        return 'first'

    class OtherSpaceMeta(MetaCute):

      @classmethod
      def __prepare__(mcls, name: str, bases: tuple, **kwargs) -> BaseSpace:
        return BaseSpace(mcls, name, bases, **kwargs)

    class FaultyChild(FaultyHost, metaclass=OtherSpaceMeta):
      pass

    class SoundHost(metaclass=MetaCute):
      KeptLate = WAIT['KeptLate']

      @overload(KeptLate)
      def take(self, late: Any) -> str:
        return 'took'

    with self.assertRaises(TypeException):
      class KeptLate(metaclass=MetaCute):
        pass

    info = """Settling 'FaultyHost' raised, and 'SoundHost' was dropped
    with it: nothing is said to wait while 'SoundHost.take' is missing."""
    stillWaiting = MetaCute.getStillWaiting()
    self.assertIn('KeptLate', stillWaiting, ' '.join(info.split()))

    class KeptLate(metaclass=MetaCute):
      pass

    self.assertNotIn('KeptLate', MetaCute.getStillWaiting())
    self.assertEqual(SoundHost().take(KeptLate()), 'took')
