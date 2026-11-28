"""
TestCuteMetaCute tests 'MetaCute', the metaclass of every cute class,
which settles the classes that wait for a class made later.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

from unittest import mock

from worktoy.mcls import BaseObject, BaseSpace
from worktoy.waitaminute import TypeException
from worktoy.waitaminute.dispatch import DispatchException
from worktoy.waitaminute.dispatch import DuplicateSignature
from worktoy.work_test import BaseTest

from cutienator.cute import CuteLoadHook, CuteSpace, MetaCute, WAIT


class _Stop(BaseException):
  """Raised where nothing but a 'BaseException' would do."""


class _OtherSpaceMeta(MetaCute):
  """Prepares a namespace that keeps no waiting signatures."""

  @classmethod
  def __prepare__(mcls, name: str, bases: tuple, **kwargs) -> BaseSpace:
    """A namespace of worktoy's, not a 'CuteSpace'."""
    return BaseSpace(mcls, name, bases, **kwargs)


class TestCuteMetaCute(BaseTest):
  """
  Tests 'MetaCute': the classes it notes as made, the waiting fields it
  notes and settles, settling all or nothing, and the dispatchers it
  builds again on a waiting class and the classes built on it.

  What to know before adding a test
  ---------------------------------

  - Each test has a fresh record of the classes made and of the fields
    waiting, in 'setUp', so the late classes of a test may have any
    name.
  - A class body reads 'overload' and gets 'CuteOverload'.
  - A 'WAIT' in a class 'MetaCute' does not make raises in
    '__set_name__', which Python 3.11 and before wrap in RuntimeError.
  """

  def setUp(self) -> None:
    """A fresh record of the classes made and of the fields waiting."""
    super().setUp()
    for name in ('__made_classes__', '__waiting_fields__'):
      patcher = mock.patch.object(MetaCute, name, dict())
      patcher.start()
      self.addCleanup(patcher.stop)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  HELPERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def _waiter(name: str = 'QWaiter') -> type:
    """A class whose one signature waits for 'QLater'."""

    class QWaiter(metaclass=MetaCute):
      QLater = WAIT['QLater']

      @overload(QLater)
      def take(self, later: object) -> str:
        return 'later'

    QWaiter.__name__ = name
    return QWaiter

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  THE LISTS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def test_the_lists_are_made_at_the_first_asking(self) -> None:
    """With no list yet, the first asking makes it, and later askings
    give the same."""
    with mock.patch.object(MetaCute, '__waiting_fields__', None):
      with mock.patch.object(MetaCute, '__made_classes__', None):
        waiting = MetaCute._getWaitingFields()
        made = MetaCute._getMadeClasses()
        self.assertEqual((waiting, made), ({}, {}))
        self.assertIs(MetaCute._getWaitingFields(), waiting)
        self.assertIs(MetaCute._getMadeClasses(), made)

  def test_what_is_still_waited_for(self) -> None:
    """The names waited for and not made, in alphabetical order; a name
    nothing waits for any more is left out."""
    class QWaiter(metaclass=MetaCute):
      QZebra = WAIT['QZebra']
      QAlpha = WAIT['QAlpha']

    MetaCute._getWaitingFields()['QEmpty'] = []
    self.assertEqual(MetaCute.getStillWaiting(), ('QAlpha', 'QZebra'))

  def test_add_waiting_checks_what_it_is_given(self) -> None:
    """A class, a name and a 'WAIT', and nothing else."""
    wait = WAIT['QChecked']
    for wrong in ((7, 'QChecked', wait), (BaseObject, 7, wait),
                  (BaseObject, 'QChecked', 'QChecked')):
      with self.subTest(wrong=wrong):
        with self.assertRaises(TypeException):
          MetaCute.addWaiting(*wrong)
    self.assertEqual(MetaCute.getStillWaiting(), ())

  def test_a_wait_in_a_class_that_is_not_cute(self) -> None:
    """A 'WAIT' in the body of a class 'MetaCute' did not make is
    refused, and nothing waits."""
    with self.assertRaises((TypeError, RuntimeError)):

      class NotCute(BaseObject):
        QLater = WAIT['QLater']

    self.assertEqual(MetaCute.getStillWaiting(), ())

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  MAKING A CLASS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def test_a_body_runs_in_a_cute_space(self) -> None:
    """'__prepare__' gives a new 'CuteSpace' each time."""
    first = MetaCute.__prepare__('QCutie', ())
    self.assertIsInstance(first, CuteSpace)
    self.assertIsNot(MetaCute.__prepare__('QCutie', ()), first)

  def test_a_class_is_noted_by_its_name(self) -> None:
    """A class is noted under its name, or its own '__qt_class__' with
    dots for '::', with its own '__qt_part__' before that."""

    class Plain(metaclass=MetaCute):
      pass

    class QEntity(metaclass=MetaCute):
      __qt_class__ = 'Qt3DCore::QEntity'

    class QBarSeries(metaclass=MetaCute):
      __qt_class__ = 'QBarSeries'
      __qt_part__ = 'QtCharts'

    class QOdd(metaclass=MetaCute):
      __qt_class__ = 7

    made = MetaCute._getMadeClasses()
    self.assertIs(made['Plain'], Plain)
    self.assertIs(made['Qt3DCore.QEntity'], QEntity)
    self.assertIs(made['QtCharts:QBarSeries'], QBarSeries)
    self.assertIs(made['QOdd'], QOdd)

  def test_a_class_built_on_a_cute_class_by_its_own_name(self) -> None:
    """'__qt_class__' inherited is not the class's own, so the class is
    noted by its name."""

    class QEntity(metaclass=MetaCute):
      __qt_class__ = 'Qt3DCore::QEntity'

    class Mine(QEntity):
      pass

    self.assertIs(MetaCute._getMadeClasses()['Mine'], Mine)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTLING   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def test_a_late_class_made_later_settles_the_field(self) -> None:
    """The late class takes the place of the 'WAIT', and the signature
    that waited takes calls."""
    QWaiter = self._waiter()
    self.assertEqual(MetaCute.getStillWaiting(), ('QLater',))
    with self.assertRaises(DispatchException):
      QWaiter().take(1)

    class QLater(metaclass=MetaCute):
      pass

    self.assertEqual(MetaCute.getStillWaiting(), ())
    self.assertIs(QWaiter.QLater, QLater)
    self.assertEqual(QWaiter().take(QLater()), 'later')

  def test_a_late_class_made_before_settles_at_once(self) -> None:
    """A 'WAIT' for a class made already is settled as its class is
    made."""

    class QLater(metaclass=MetaCute):
      pass

    QWaiter = self._waiter()
    self.assertEqual(MetaCute.getStillWaiting(), ())
    self.assertIs(QWaiter.QLater, QLater)

  def test_every_class_waiting_is_settled(self) -> None:
    """Two classes waiting for one late class are both settled."""
    first, other = self._waiter('QFirst'), self._waiter('QOther')

    class QLater(metaclass=MetaCute):
      pass

    self.assertEqual(first().take(QLater()), 'later')
    self.assertEqual(other().take(QLater()), 'later')

  def test_settling_is_all_or_nothing(self) -> None:
    """When one waiting field cannot be settled, the namespaces settled
    before it are put back, it is given up, and the others wait on."""
    sound = self._waiter('QSound')
    faulty = self._waiter('QFaulty')

    class QChild(faulty, metaclass=_OtherSpaceMeta):
      pass

    def makeLate() -> type:
      class QLater(metaclass=MetaCute):
        pass

      return QLater

    with self.assertRaises(TypeException):
      makeLate()
    self.assertNotIn('QLater', MetaCute._getMadeClasses())
    self.assertEqual(MetaCute.getStillWaiting(), ('QLater',))
    self.assertIsInstance(sound.__dict__['QLater'], WAIT)
    self.assertEqual(len(sound.getNamespace().getWaitingSignatures()), 1)
    QLater = makeLate()
    self.assertEqual(MetaCute.getStillWaiting(), ())
    self.assertEqual(sound().take(QLater()), 'later')
    self.assertIsInstance(faulty.__dict__['QLater'], WAIT)

  def test_a_base_exception_gives_no_field_up(self) -> None:
    """What is no 'Exception', as an interrupt, gives up no field."""
    self._waiter()
    with mock.patch.object(CuteSpace, 'nameLateClass', side_effect=_Stop):
      with self.assertRaises(_Stop):

        class QLater(metaclass=MetaCute):
          pass

    self.assertEqual(MetaCute.getStillWaiting(), ('QLater',))

  def test_a_failed_class_statement_leaves_nothing(self) -> None:
    """A class whose statement fails is not noted as made, and its own
    waiting fields are forgotten."""

    class QLater(metaclass=MetaCute):
      pass

    with self.assertRaises(DuplicateSignature):

      class QHost(metaclass=MetaCute):
        QOther = WAIT['QOther']

        @overload(QLater)
        def take(self, later: object) -> str:
          return 'the class itself'

        @overload(WAIT['QLater'])
        def take(self, later: object) -> str:
          return 'the same class by a WAIT'

    self.assertNotIn('QHost', MetaCute._getMadeClasses())
    self.assertEqual(MetaCute.getStillWaiting(), ())

  def test_a_failed_class_statement_keeps_the_one_before(self) -> None:
    """A class of a name made before, whose second statement fails,
    stays the one noted."""

    class QLater(metaclass=MetaCute):
      pass

    class QHost(metaclass=MetaCute):
      pass

    before = QHost
    with self.assertRaises(DuplicateSignature):

      class QHost(metaclass=MetaCute):
        @overload(QLater)
        def take(self, later: object) -> str:
          return 'one'

        @overload(WAIT['QLater'])
        def take(self, later: object) -> str:
          return 'two'

    self.assertIs(MetaCute._getMadeClasses()['QHost'], before)

  def test_a_metaclass_based_on_it_shares_the_lists(self) -> None:
    """A metaclass based on 'MetaCute' waits and settles with it."""

    class BasedMeta(MetaCute):
      pass

    class QBased(metaclass=BasedMeta):
      QLater = WAIT['QLater']

      @overload(QLater)
      def take(self, later: object) -> str:
        return 'based'

    self.assertEqual(MetaCute.getStillWaiting(), ('QLater',))

    class QLater(metaclass=MetaCute):
      pass

    self.assertEqual(BasedMeta.getStillWaiting(), ())
    self.assertEqual(QBased().take(QLater()), 'based')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STAND-INS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def test_a_stand_in_is_noted_and_settles(self) -> None:
    """A stand-in is noted under the name of its '__qt_class__' and
    '__qt_part__', and settles what waits for it."""
    QWaiter = self._waiter()

    class Stand:
      __qt_class__ = 'QLater'

    MetaCute.noteStandIn(Stand)
    self.assertIs(MetaCute._getMadeClasses()['QLater'], Stand)
    self.assertIs(QWaiter.QLater, Stand)

    class Parted:
      __qt_class__ = 'QBarSeries'
      __qt_part__ = 'QtCharts'

    MetaCute.noteStandIn(Parted)
    self.assertIs(MetaCute._getMadeClasses()['QtCharts:QBarSeries'], Parted)

  def test_a_stand_in_that_fails_to_settle(self) -> None:
    """When settling refuses, the stand-in is not noted, and the class
    noted before at its name stays."""
    self._waiter()

    class Stand:
      __qt_class__ = 'QLater'

    with mock.patch.object(CuteSpace, 'nameLateClass', side_effect=_Stop):
      with self.assertRaises(_Stop):
        MetaCute.noteStandIn(Stand)
      self.assertNotIn('QLater', MetaCute._getMadeClasses())
      before = object()
      MetaCute._getMadeClasses()['QLater'] = before
      with self.assertRaises(_Stop):
        MetaCute.noteStandIn(Stand)
      self.assertIs(MetaCute._getMadeClasses()['QLater'], before)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  THE WAITING FIELDS   # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def test_dropping_a_waiting_field(self) -> None:
    """Only the field given is dropped; the name goes when none is left;
    a field not on the list changes nothing."""
    first, other = self._waiter('QFirst'), self._waiter('QOther')
    fields = MetaCute._getWaitingFields()
    firstField, otherField = fields['QLater']
    MetaCute._dropWaiting('QLater', otherField)
    self.assertEqual(fields['QLater'], [firstField])
    MetaCute._dropWaiting('QLater', otherField)
    self.assertEqual(fields['QLater'], [firstField])
    MetaCute._dropWaiting('QLater', firstField)
    self.assertNotIn('QLater', fields)
    MetaCute._dropWaiting('QNothing', firstField)
    self.assertNotIn('QNothing', fields)

  def test_forgetting_a_class(self) -> None:
    """Every waiting field of the class is dropped, and no other."""

    class QFirst(metaclass=MetaCute):
      QLater = WAIT['QLater']
      QOther = WAIT['QOther']

    other = self._waiter('QOtherWaiter')
    MetaCute._forgetClass(QFirst)
    fields = MetaCute._getWaitingFields()
    self.assertEqual([*fields], ['QLater'])
    self.assertIs(fields['QLater'][0][0], other)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  THE FAMILY   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def test_the_family_of_a_class(self) -> None:
    """The class first, then each class built on it once, after the one
    it is built on."""
    QBase = self._waiter('QBase')

    class QLeft(QBase):
      pass

    class QRight(QBase):
      pass

    class QBottom(QLeft, QRight):
      pass

    family = [cls for cls, _ in MetaCute._getFamily(QBase)]
    self.assertEqual(family, [QBase, QLeft, QBottom, QRight])

  def test_a_family_member_with_no_cute_space(self) -> None:
    """A class whose namespace is no 'CuteSpace' is refused."""
    QBase = self._waiter('QBase')

    class QChild(QBase, metaclass=_OtherSpaceMeta):
      pass

    with self.assertRaises(TypeException):
      MetaCute._getFamily(QBase)

  def test_the_family_is_built_again(self) -> None:
    """A class built on the waiting class gets the signature too; one
    that defines the name plainly keeps its own."""
    QBase = self._waiter('QBase')

    class QBuilt(QBase):
      pass

    class QPlain(QBase):
      def take(self, later: object) -> str:
        return 'plain'

    class QLater(metaclass=MetaCute):
      pass

    self.assertEqual(QBuilt().take(QLater()), 'later')
    self.assertEqual(QPlain().take(QLater()), 'plain')

  def test_a_name_with_nothing_to_build(self) -> None:
    """A name whose dispatcher would be nothing is left as it is."""
    QWaiter = self._waiter()
    before = QWaiter.__dict__['take']
    with mock.patch.object(CuteLoadHook, 'buildAgain', return_value=None):

      class QLater(metaclass=MetaCute):
        pass

    self.assertIs(QWaiter.__dict__['take'], before)
