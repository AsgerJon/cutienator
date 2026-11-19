"""
TestQWidgets tests the cute classes of QtWidgets that the dev tooling
wrote, up to the first window: a window with a title and a button that
quits.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

import os
import subprocess
import sys

from worktoy.waitaminute import TypeException
from worktoy.work_test import BaseTest

import cutienator
from cutienator.QtCore import QObject
from cutienator.QtWidgets import QAbstractButton, QPushButton, QWidget
from cutienator.occult import Rituals


class Window(QWidget):
  """A class of a program, built on a cute class as programs do."""


#  The first window. It runs in a Python of its own, since Qt has one
#  application for each program, and the other tests run without one.
FIRST_WINDOW = """
import sys

from cutienator.QtCore import QObject, QTimer, QCoreApplication
from cutienator.QtWidgets import QApplication, QWidget, QPushButton

app = QApplication(sys.argv)
print('made at once:', app.uglySide.isWatched())
print('the one application:', QCoreApplication.instance() is app)
window = QWidget()
window.setWindowTitle('cutienator')
window.resize(320, 120)
button = QPushButton('Quit', window)
QObject.connect(button, '2clicked()', app, '1quit()')
window.show()
print('title:', window.windowTitle())
print('button:', button.text())
print('parent:', button.parent() is window)
print('size:', window.width(), window.height())
print('visible:', window.isVisible())
QTimer.singleShot(50, button, '1click()')
print('ended with:', QApplication.exec())
"""


class TestQWidgets(BaseTest):
  """
  Tests what the first window needs: that a class Qt cannot make is
  refused, that a class of a program is made as its cute class is, and
  that the window itself runs.
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

  def test_the_classes_are_built_as_qt_builds_them(self) -> None:
    """Each cute class is built on the cute class of its parent in Qt."""
    self.assertTrue(issubclass(QPushButton, QAbstractButton))
    self.assertTrue(issubclass(QAbstractButton, QWidget))
    self.assertTrue(issubclass(QWidget, QObject))
    self.assertEqual(QPushButton.__qt_class__, 'QPushButton')

  def test_a_class_qt_cannot_make_is_refused(self) -> None:
    """Qt's QAbstractButton is abstract. It has the '__init__' of the
    class it is built on, which makes a QWidget, and that is refused."""
    with self.assertRaises(TypeError) as context:
      QAbstractButton()
    self.assertIn('QAbstractButton', str(context.exception))

  def test_a_class_of_a_program_is_made_as_its_cute_class(self) -> None:
    """A class built on 'QWidget' is made by what 'QWidget' is made
    by. Nothing of Qt is made before the first use."""
    self.assertIsInstance(Window(), QWidget)
    self.assertIsInstance(Window(None), QWidget)

  def test_the_texts_a_program_was_started_with(self) -> None:
    """They are kept as Qt takes them: a count, and the first text."""
    countAddress, firstAddress = Rituals.keepStartTexts(['one', 'two'])
    self.assertIsInstance(countAddress, int)
    self.assertIsInstance(firstAddress, int)
    with self.assertRaises(TypeException):
      Rituals.keepStartTexts('one two')
    with self.assertRaises(TypeException):
      Rituals.keepStartTexts(['one', 2])

  def test_the_first_window(self) -> None:
    """A window with a title and a button that quits the application,
    shown nowhere: Qt draws it in memory."""
    packageFolder = os.path.dirname(os.path.abspath(cutienator.__file__))
    environment = dict(os.environ)
    environment['QT_QPA_PLATFORM'] = 'offscreen'
    known = environment.get('PYTHONPATH', '')
    folders = [os.path.dirname(packageFolder), *known.split(os.pathsep)]
    environment['PYTHONPATH'] = os.pathsep.join(f for f in folders if f)
    done = subprocess.run(
        (sys.executable, '-B', '-c', FIRST_WINDOW), capture_output=True,
        text=True, env=environment, timeout=120,
    )
    self.assertEqual(done.returncode, 0, done.stderr)
    expected = [
      'made at once: True',
      'the one application: True',
      'title: cutienator',
      'button: Quit',
      'parent: True',
      'size: 320 120',
      'visible: True',
      'ended with: 0',
    ]
    self.assertEqual(done.stdout.strip().split('\n'), expected)
