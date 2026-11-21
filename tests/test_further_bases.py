"""
TestFurtherBases tests the cute classes whose class of Qt is built on
more than one class, as QWidget on QObject and QPaintDevice.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

import os
import subprocess
import sys

from worktoy.waitaminute import MissingVariable, TypeException
from worktoy.work_test import BaseTest

import cutienator
from cutienator.QtCore import QObject, QIODevice, QIODeviceBase
from cutienator.QtGui import QPaintDevice, QPixmap, QSurface, QWindow
from cutienator.QtWidgets import QWidget, QPushButton, QLayout, QLayoutItem
from cutienator.QtWidgets import QGraphicsItem, QGraphicsObject
from cutienator.occult import Rituals, Ugly

#  Run in a Python of its own, since Qt has one application for each
#  program, and the other tests run without one.
AS_EITHER = """
import sys

from cutienator.QtCore import QPoint
from cutienator.QtGui import QPainter, QPixmap, QRegion
from cutienator.QtWidgets import QApplication, QWidget, QPushButton
from cutienator.QtWidgets import QVBoxLayout, QHBoxLayout
from cutienator.QtWidgets import QGraphicsScene, QGraphicsWidget

app = QApplication(sys.argv)
widget, button = QWidget(), QPushButton('ok')
print('of the paint device:', widget.logicalDpiX() > 0, button.depth() > 0)
print('of the widget itself:', widget.width() > 0)
pixmap = QPixmap(40, 30)
widget.render(pixmap, QPoint(), QRegion(), QWidget.RenderFlags(3))
painter = QPainter(pixmap)
print('given back:', painter.device() is pixmap)
painter.end()
painter = QPainter()
print('a widget is taken:', painter.begin(widget) in (True, False))
painter.end()
outer, inner = QVBoxLayout(), QHBoxLayout()
outer.addItem(inner)
print('a layout as an item:', outer.count(), outer.itemAt(0) is inner)
print('its own part:', inner.layout() is inner)
scene, item = QGraphicsScene(), QGraphicsWidget()
scene.addItem(item)
print('an object as an item:', item.scene() is scene)
"""


class Device:
  """Stands in for a class others are built on beside another."""

  __qt_class__ = 'Device'


class Screen(Device):
  """Stands in for a class built on such a class."""

  __qt_class__ = 'Screen'


class TestFurtherBases(BaseTest):
  """
  Tests that such a cute class is built on the cute class of each class
  its class of Qt is built on, that it names the ritual giving where
  the part of an object belonging to a further one is, and that an
  object is taken and found again as either.
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

  def test_a_class_is_built_on_both(self) -> None:
    """Each is built on the first class and on the further one, in the
    order C++ names them."""
    pairs = (
        (QWidget, QObject, QPaintDevice),
        (QLayout, QObject, QLayoutItem),
        (QGraphicsObject, QObject, QGraphicsItem),
        (QWindow, QObject, QSurface),
        (QIODevice, QObject, QIODeviceBase),
    )
    for cuteClass, first, further in pairs:
      with self.subTest(cuteClass=cuteClass.__name__):
        self.assertEqual(cuteClass.__bases__[:2], (first, further))
        self.assertTrue(issubclass(cuteClass, further))
    self.assertTrue(issubclass(QPushButton, QPaintDevice))
    self.assertFalse(issubclass(QPaintDevice, QObject))
    self.assertFalse(issubclass(QPixmap, QObject))

  def test_the_ritual_of_the_further_class_is_named(self) -> None:
    """The class names, for the further class, the ritual that gives
    where its part of an object is, and the shared object has it."""
    named = {'QPaintDevice': 'ritual_cast_QWidget_QPaintDevice'}
    self.assertEqual(QWidget.__dict__['__cast_rituals__'], named)
    self.assertIsNone(QPaintDevice.__cast_rituals__)
    self.assertNotIn('__cast_rituals__', QPushButton.__dict__)
    self.assertIn('ritual_cast_QWidget_QPaintDevice', Rituals.getRows())

  def test_a_part_is_found_through_the_further_class(self) -> None:
    """'_findCast' names the ritual for the further class and for what
    that one is built on, and none for the first class."""

    class Holder(QObject, Screen):
      __qt_class__ = 'Holder'
      __cast_rituals__ = {'Screen': 'ritual_of_the_screen'}

    class Heir(Holder):
      __qt_class__ = 'Heir'

    for cuteClass in (Holder, Heir):
      held = cuteClass.__new__(cuteClass)
      with self.subTest(cuteClass=cuteClass.__name__):
        self.assertEqual(held._findCast('Screen'), 'ritual_of_the_screen')
        self.assertEqual(held._findCast('Device'), 'ritual_of_the_screen')
        self.assertIsNone(held._findCast('QObject'))
        self.assertIsNone(held._findCast('Holder'))
        self.assertIsNone(held._findCast('Nothing'))
    self.assertIsNone(QObject.__new__(QObject)._findCast('Screen'))

  def test_an_ugly_is_found_by_the_address_of_a_part(self) -> None:
    """An address told to an Ugly as that of a part leads to it, and
    its own address stays what it was."""
    ugly = Ugly()
    with self.assertRaises(MissingVariable):
      ugly.addPartAddress(0x7300)
    ugly.setAddress(0x7200)
    ugly.addPartAddress(0x7210)
    ugly.addPartAddress(0x7200)
    self.assertIs(Ugly.at(0x7210), ugly)
    self.assertIs(Ugly.at(0x7200), ugly)
    self.assertEqual(ugly.getAddress(), 0x7200)
    for wrong in ('0x7210', 7.5, True, None):
      with self.subTest(wrong=repr(wrong)):
        with self.assertRaises(TypeException):
          ugly.addPartAddress(wrong)
    for wrong in (0, -4):
      with self.subTest(wrong=wrong):
        with self.assertRaises(ValueError):
          ugly.addPartAddress(wrong)

  def test_an_object_is_taken_and_found_as_either(self) -> None:
    """A widget has the functions of a paint device and is taken where
    one is; a layout is taken as an item and found again as itself; so
    is an object of the graphics scene."""
    packageFolder = os.path.dirname(os.path.abspath(cutienator.__file__))
    environment = dict(os.environ)
    environment['QT_QPA_PLATFORM'] = 'offscreen'
    known = environment.get('PYTHONPATH', '')
    folders = [os.path.dirname(packageFolder), *known.split(os.pathsep)]
    environment['PYTHONPATH'] = os.pathsep.join(f for f in folders if f)
    done = subprocess.run(
        (sys.executable, '-B', '-c', AS_EITHER), capture_output=True,
        text=True, env=environment, timeout=120,
    )
    self.assertEqual(done.returncode, 0, done.stderr)
    expected = [
      'of the paint device: True True',
      'of the widget itself: True',
      'given back: True',
      'a widget is taken: True',
      'a layout as an item: 1 True',
      'its own part: True',
      'an object as an item: True',
    ]
    self.assertEqual(done.stdout.strip().split('\n'), expected)
