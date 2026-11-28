"""
TestCuteCuteLoadHook tests 'CuteLoadHook', which builds the dispatcher
of an overloaded name again after its class is made.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

from unittest import mock

from worktoy.dispatch import Dispatcher, TypeSig
from worktoy.work_test import BaseTest

from cutienator.cute import CuteLoadHook, MetaCute


class TestCuteCuteLoadHook(BaseTest):
  """
  Tests 'CuteLoadHook': the phases it leaves to worktoy, the class it
  tells the namespace, and the dispatchers it builds again from the
  record. How 'MetaCute' places them is tested in 'TestCuteMetaCute'.

  What to know before adding a test
  ---------------------------------

  - The hook is read through the namespace of a class, as
    'space.cuteLoadHook'.
  - Each test has a fresh record of the classes made and of the fields
    waiting, in 'setUp'.
  """

  def setUp(self) -> None:
    """A fresh record of the classes made and of the fields waiting."""
    super().setUp()
    for name in ('__made_classes__', '__waiting_fields__'):
      patcher = mock.patch.object(MetaCute, name, dict())
      patcher.start()
      self.addCleanup(patcher.stop)

  @staticmethod
  def _cutie() -> type:
    """A class with one overloaded name of two signatures."""

    class QCutie(metaclass=MetaCute):
      @overload(int)
      def size(self, n: int) -> str:
        return 'int'

      @overload(str)
      def size(self, s: str) -> str:
        return 'str'

    return QCutie

  def test_it_is_the_namespaces(self) -> None:
    """The namespace of a cute class has one, and it knows the
    namespace."""
    space = self._cutie().getNamespace()
    hook = space.cuteLoadHook
    self.assertIsInstance(hook, CuteLoadHook)
    self.assertIs(hook.space, space)

  def test_the_phases_it_leaves_to_worktoy(self) -> None:
    """Binding and deleting claim nothing; the compiled namespace is
    handed back as it is."""
    hook = self._cutie().getNamespace().cuteLoadHook
    self.assertIs(hook.setItemPhase('size', 1, None), False)
    self.assertIs(hook.delItemPhase('size', 1), False)
    compiled = dict(size=1)
    self.assertIs(hook.postCompilePhase(compiled), compiled)

  def test_it_tells_the_namespace_its_class(self) -> None:
    """Once the class is made, the namespace knows it, and the class is
    handed back."""
    QCutie = self._cutie()
    self.assertIs(QCutie.getNamespace().getCuteClass(), QCutie)
    space = MetaCute.__prepare__('QOther', ())
    self.assertIs(space.cuteLoadHook.newClassPhase(QCutie), QCutie)
    self.assertIs(space.getCuteClass(), QCutie)

  def test_building_again(self) -> None:
    """A new dispatcher each time, of every signature on record in the
    order written, placed nowhere; nothing for a name with nothing."""
    QCutie = self._cutie()
    hook = QCutie.getNamespace().cuteLoadHook
    first = hook.buildAgain('size')
    self.assertIsInstance(first, Dispatcher)
    self.assertIsNot(hook.buildAgain('size'), first)
    self.assertIsNot(QCutie.__dict__['size'], first)
    self.assertEqual(first._getDeclaredSigs(), [TypeSig(int), TypeSig(str)])
    self.assertIsNone(hook.buildAgain('nothing'))
