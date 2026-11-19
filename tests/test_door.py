"""
TestDoor tests the door of the cute functions: a member of an enum of Qt
is taken where Qt takes the number.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee
from worktoy.mcls import BaseObject
from worktoy.waitaminute.dispatch import DispatchException
from worktoy.work_test import BaseTest

from cutienator.cute import CuteNum, CuteFlags, DoorNumber, MetaCute, WAIT
from cutienator.QtCore import QObject, QSize
from cutienator.occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Any


class ItemDataRole(CuteNum):
  """Stands in for 'Qt::ItemDataRole'."""
  DisplayRole = Kee[int](0)
  DecorationRole = Kee[int](1)
  EditRole = Kee[int](2)


class DialogCode(CuteNum):
  """Stands in for 'QDialog::DialogCode'."""
  Rejected = Kee[int](0)
  Accepted = Kee[int](1)


class AspectRatioMode(CuteNum):
  """Stands in for 'Qt::AspectRatioMode'."""
  IgnoreAspectRatio = Kee[int](0)
  KeepAspectRatio = Kee[int](1)


class AlignmentFlag(CuteFlags):
  """Stands in for 'Qt::AlignmentFlag'."""
  AlignLeft = 0x0001
  AlignTop = 0x0020


class DoorModel(BaseObject, metaclass=MetaCute):
  """A cute class whose functions take numbers and a member."""

  @overload(str, int)
  def data(self, index: str, role: int) -> str:
    return '%s, role %d' % (index, role)

  @overload(int)
  def kind(self, number: int) -> type:
    return type(number)

  @overload(ItemDataRole)
  def setRole(self, role: ItemDataRole) -> str:
    return role.name

  @classmethod
  @overload(int)
  def ofClass(cls, number: int) -> str:
    return '%s %d' % (cls.__name__, number)

  @staticmethod
  @overload(int)
  def ofNothing(number: int) -> str:
    return 'number %d' % number


class DoorChild(DoorModel):
  """A cute class built on another, with a dispatcher of its own."""

  @overload(str, str)
  def data(self, index: str, text: str) -> str:
    return '%s, text %s' % (index, text)

  @overload(str, float)
  def data(self, index: str, factor: float) -> str:
    return super().data(index, ItemDataRole.EditRole)


class OwnFallback(BaseObject, metaclass=MetaCute):
  """A cute class that declares a fallback of its own."""

  @overload(int)
  def take(self, number: int) -> str:
    return 'number'

  @overload.fallback
  def take(self, *args: Any) -> str:
    return 'fallback got %s' % type(args[0]).__name__


class TestDoor(BaseTest):
  """
  Tests that a call no signature takes as written is tried once more
  with each member swapped for its number, that nothing else gets
  through that way, and that a call taken as written is left alone.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  HELPERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @classmethod
  def setUpClass(cls) -> None:
    """Builds the shared object of rituals when a ritual file is newer."""
    super().setUpClass()
    if Rituals.isStale():
      Rituals.build()

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  TESTS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def test_a_member_where_qt_takes_the_number(self) -> None:
    """A member of an enum goes in as its number."""
    model = DoorModel()
    taken = model.data('cell', ItemDataRole.EditRole)
    self.assertEqual(taken, 'cell, role 2')

  def test_a_value_of_flags_where_qt_takes_the_number(self) -> None:
    """A value of flags goes in as its number."""
    both = AlignmentFlag.AlignLeft | AlignmentFlag.AlignTop
    self.assertEqual(DoorModel().data('cell', both), 'cell, role 33')

  def test_a_number_is_taken_as_ever(self) -> None:
    """A call taken as written never comes near the door."""
    model = DoorModel()
    self.assertEqual(model.data('cell', 2), 'cell, role 2')
    self.assertIs(model.kind(2), int)

  def test_what_the_function_is_handed(self) -> None:
    """The function gets a 'DoorNumber', which is an 'int'."""
    handed = DoorModel().kind(ItemDataRole.EditRole)
    self.assertIs(handed, DoorNumber)
    self.assertTrue(issubclass(handed, int))

  def test_a_member_where_qt_takes_the_member(self) -> None:
    """The member itself arrives, and so do its number and its name."""
    model = DoorModel()
    self.assertEqual(model.setRole(ItemDataRole.EditRole), 'EditRole')
    self.assertEqual(model.setRole(2), 'EditRole')
    self.assertEqual(model.setRole('EditRole'), 'EditRole')

  def test_a_member_of_another_enum_does_not_slip_in(self) -> None:
    """Not even when its number has a name in the enum Qt takes."""
    model = DoorModel()
    with self.assertRaises(DispatchException):
      model.setRole(DialogCode.Accepted)
    with self.assertRaises(DispatchException):
      model.setRole(AlignmentFlag.AlignLeft)

  def test_a_refusal_names_the_call_as_written(self) -> None:
    """The refusal holds the member, not the number it was swapped for."""
    model = DoorModel()
    with self.assertRaises(DispatchException) as context:
      model.setRole(DialogCode.Accepted)
    self.assertEqual(context.exception.posArgs, (DialogCode.Accepted,))
    with self.assertRaises(DispatchException) as context:
      model.data('cell', None)
    self.assertEqual(context.exception.posArgs, ('cell', None))

  def test_the_door_of_a_classmethod(self) -> None:
    """The class the method was called on is kept."""
    taken = DoorModel.ofClass(ItemDataRole.EditRole)
    self.assertEqual(taken, 'DoorModel 2')
    self.assertEqual(DoorModel().ofClass(DialogCode.Accepted), 'DoorModel 1')

  def test_the_door_of_a_staticmethod(self) -> None:
    """A static method takes a member where it takes a number."""
    self.assertEqual(DoorModel.ofNothing(ItemDataRole.EditRole), 'number 2')
    self.assertEqual(DoorModel().ofNothing(2), 'number 2')
    with self.assertRaises(DispatchException):
      DoorModel.ofNothing('two')

  def test_a_class_built_on_another_has_doors_of_its_own(self) -> None:
    """What it inherits and what it adds both take a member."""
    child = DoorChild()
    taken = child.data('cell', ItemDataRole.DecorationRole)
    self.assertEqual(taken, 'cell, role 1')
    self.assertEqual(child.data('cell', 'word'), 'cell, text word')
    self.assertEqual(DoorChild.ofClass(DialogCode.Accepted), 'DoorChild 1')

  def test_a_door_reached_through_super(self) -> None:
    """A call handed up with a member goes through the door of the
    class it was handed to."""
    self.assertEqual(DoorChild().data('cell', 0.5), 'cell, role 2')

  def test_a_fallback_of_the_class_stands_in_for_the_door(self) -> None:
    """A class that declares a fallback gets the member unswapped."""
    own = OwnFallback()
    self.assertEqual(own.take(1), 'number')
    taken = own.take(ItemDataRole.EditRole)
    self.assertEqual(taken, 'fallback got ItemDataRole')

  def test_a_name_with_nothing_on_record_gets_no_door(self) -> None:
    """A plain definition that hides the overloads stays what the
    class has."""

    class DoorTop(BaseObject, metaclass=MetaCute):
      @overload(int)
      def act(self, number: int) -> str:
        return 'overloaded'

    class DoorMiddle(DoorTop):
      def act(self) -> str:
        return 'plain'

    class DoorBottom(DoorMiddle):
      pass

    self.assertNotIn('act', DoorBottom.__dict__)
    self.assertEqual(DoorBottom().act(), 'plain')

  def test_the_door_after_a_late_class_is_made(self) -> None:
    """A dispatcher built again has a door as well."""

    class DoorHost(BaseObject, metaclass=MetaCute):
      DoorLate = WAIT['DoorLate']

      @overload(int)
      def take(self, number: int) -> str:
        return 'number %d' % number

      @overload(DoorLate)
      def take(self, late: Any) -> str:
        return 'late'

    host = DoorHost()
    self.assertEqual(host.take(ItemDataRole.EditRole), 'number 2')

    class DoorLate(BaseObject, metaclass=MetaCute):
      pass

    self.assertEqual(host.take(DoorLate()), 'late')
    self.assertEqual(host.take(ItemDataRole.EditRole), 'number 2')

  def test_the_namespace_knows_its_class(self) -> None:
    """Once the class is made, and not before."""
    self.assertIs(DoorModel.getNamespace().getCuteClass(), DoorModel)
    self.assertIs(DoorChild.getNamespace().getCuteClass(), DoorChild)
    space = MetaCute.__prepare__('NotMadeYet', ())
    with self.assertRaises(RuntimeError):
      space.getCuteClass()
    with self.assertRaises(RuntimeError):
      DoorModel.getNamespace().setCuteClass(DoorModel)

  def test_a_member_into_a_real_function_of_qt(self) -> None:
    """'QSize.setWidth' takes a number in Qt."""
    size = QSize(4, 2)
    size.setWidth(ItemDataRole.EditRole)
    self.assertEqual((size.width(), size.height()), (2, 2))

  def test_a_member_into_a_real_static_function_of_qt(self) -> None:
    """'QObject.tr' takes its count as a number in Qt."""
    byNumber = QObject.tr('hello', None, 2)
    byMember = QObject.tr('hello', None, ItemDataRole.EditRole)
    self.assertEqual(byMember, byNumber)
