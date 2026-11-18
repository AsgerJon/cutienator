from __future__ import annotations

from typing import TYPE_CHECKING
from unittest import TestCase

from worktoy.dispatch import overload

from cutienator.cute import MetaCute, WAIT

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Any


class TestWaitBoundElsewhere(TestCase):

  def test_wait_read_off_base_class(self) -> None:
    """Refuse a signature naming a 'WAIT' read off the base class."""

    class BorrowHost(metaclass=MetaCute):
      BorrowLate = WAIT['BorrowLate']

      @overload(BorrowLate)
      def own(self, late: Any) -> str:
        return 'own'

    info = """'BorrowGuest.borrowed' names a 'WAIT' bound in the body of
    'BorrowHost'. No class settles it for 'BorrowGuest', so the method
    would be missing for ever."""
    with self.assertRaises(TypeError, msg=' '.join(info.split())) as ctx:
      class BorrowGuest(BorrowHost):

        @overload(BorrowHost.BorrowLate)
        def borrowed(self, late: Any) -> str:
          return 'borrowed'

    self.assertIn("BorrowLate = WAIT['BorrowLate']", str(ctx.exception))

    class BorrowLate(BorrowHost):
      pass

    self.assertNotIn('BorrowLate', MetaCute.getStillWaiting())
    self.assertEqual(BorrowHost().own(BorrowLate()), 'own')
