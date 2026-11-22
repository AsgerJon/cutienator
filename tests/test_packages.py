"""
TestPackages tests that the packages of the parts of Qt bring a class
in the first time it is asked for, and not before, and that the file
of a class brings in what the class is built on and lets every other
class it names wait.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

import os
import subprocess
import sys

from worktoy.work_test import BaseTest

import cutienator
from cutienator import QtCore, QtGui, QtWidgets
from cutienator.occult import Rituals

#  Run in a Python of its own, which has brought in nothing yet.
ASKED_FOR = """
import sys

import cutienator.QtWidgets

held = [name for name in sys.modules if '._q_' in name]
print('before:', len(held))
from cutienator.QtCore import QSize
held = [name for name in sys.modules if '._q_' in name]
print('size brought in:', 'cutienator.QtCore._q_size' in held)
print('widget not brought in:', 'cutienator.QtWidgets._q_widget' not in held)
"""

#  Run in a Python of its own as well. 'QWidget' is built on 'QObject'
#  and names 'QFont' and 'QLayout' without being built on them.
WAITED_FOR = """
import sys

from cutienator import QtCore, QtGui, QtWidgets
from cutienator.cute import MetaCute
from cutienator.QtWidgets import QWidget

classFiles = set()
for part in (QtCore, QtGui, QtWidgets):
  for fileName in part.__class_files__.values():
    classFiles.add('%s.%s' % (part.__name__, fileName))
held = sorted(name.rpartition('._')[2] for name in sys.modules
              if name in classFiles)
print('class files brought in:', ' '.join(held))
print('waits for QFont:', 'QFont' in MetaCute.getStillWaiting())
print('setFont is there:', hasattr(QWidget, 'setFont'))
try:
  QWidget.setFont(None, 7)
except Exception as exception:
  print('setFont refuses:', type(exception).__name__)
from cutienator.QtGui import QFont
print('waits for QFont:', 'QFont' in MetaCute.getStillWaiting())
print('setFont is there:', hasattr(QWidget, 'setFont'))
print('QWidget holds QFont:', QWidget.QFont is QFont)
print('QThread brought in:', 'cutienator.QtCore._q_thread' in sys.modules)
thread = QtCore.QObject().thread()
print('QThread brought in:', 'cutienator.QtCore._q_thread' in sys.modules)
print('given:', type(thread).__name__)
"""


class TestPackages(BaseTest):
  """
  Tests the package files of 'QtCore', 'QtGui' and 'QtWidgets': each
  names its classes, and brings one in when it is asked for. And tests
  what the file of a class brings in with it.
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

  def _runAlone(self, code: str) -> list:
    """Runs code in a Python of its own, which has brought in nothing
    yet, and gives the lines it printed."""
    packageFolder = os.path.dirname(os.path.abspath(cutienator.__file__))
    environment = dict(os.environ)
    known = environment.get('PYTHONPATH', '')
    folders = [os.path.dirname(packageFolder), *known.split(os.pathsep)]
    environment['PYTHONPATH'] = os.pathsep.join(f for f in folders if f)
    done = subprocess.run(
        (sys.executable, '-B', '-c', code), capture_output=True,
        text=True, env=environment, timeout=120,
    )
    self.assertEqual(done.returncode, 0, done.stderr)
    return done.stdout.strip().split('\n')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  TESTS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def test_every_name_of_a_package_gives_its_class(self) -> None:
    """Each name a package lists gives a class of that name."""
    for package in (QtCore, QtGui, QtWidgets):
      self.assertEqual(dir(package), sorted(package.__all__))
      for name in package.__all__:
        with self.subTest(package=package.__name__, name=name):
          self.assertEqual(getattr(package, name).__name__, name)

  def test_a_class_is_kept_once_brought_in(self) -> None:
    """Asked for twice, it is the same class."""
    self.assertIs(QtCore.QSize, QtCore.QSize)
    self.assertIn('QSize', vars(QtCore))

  def test_what_qt_writes_inside_a_class_stands_inside_it(self) -> None:
    """An enum, and a class Qt writes inside another, stands inside its
    class and is named as C++ names it. It has no other name: the
    package of its part does not know it."""
    connection = QtCore.QMetaObject.Connection
    self.assertEqual(connection.__qualname__, 'QMetaObject.Connection')
    self.assertEqual(connection.__qt_class__, 'QMetaObject::Connection')
    named = (
        (QtCore.QEvent.Type, 'QEvent.Type'),
        (QtCore.Qt.AlignmentFlag, 'Qt.AlignmentFlag'),
        (QtGui.QPalette.ColorRole, 'QPalette.ColorRole'),
        (QtWidgets.QWidget.RenderFlag, 'QWidget.RenderFlag'),
    )
    for enumClass, qualifiedName in named:
      with self.subTest(named=qualifiedName):
        self.assertEqual(enumClass.__qualname__, qualifiedName)
    self.assertIs(QtCore.Qt.Alignment, QtCore.Qt.AlignmentFlag)
    widget = QtWidgets.QWidget
    self.assertIs(widget.RenderFlags, widget.RenderFlag)
    unknown = (
        'Connection', 'Type', 'AlignmentFlag', 'QEventType',
        'QMetaObjectConnection', 'QtAlignmentFlag', 'QPaletteColorRole',
    )
    for package in (QtCore, QtGui, QtWidgets):
      for name in unknown:
        with self.subTest(package=package.__name__, name=name):
          with self.assertRaises(AttributeError):
            getattr(package, name)

  def test_a_name_that_is_no_class_is_refused(self) -> None:
    """As for any module: 'AttributeError', and so 'ImportError'."""
    with self.assertRaises(AttributeError):
      QtCore.QNothingAtAll
    with self.assertRaises(ImportError):
      from cutienator.QtWidgets import QNothingAtAll  # noqa

  def test_nothing_is_brought_in_before_it_is_asked_for(self) -> None:
    """Bringing in a package brings in no class file. Asking for one
    class brings in that one, and not the others."""
    expected = [
      'before: 0',
      'size brought in: True',
      'widget not brought in: True',
    ]
    self.assertEqual(self._runAlone(ASKED_FOR), expected)

  def test_a_class_file_brings_in_what_its_class_is_built_on(self) -> None:
    """The file of 'QWidget' brings in the files of 'QObject' and
    'QPaintDevice', which it is built on, the namespace 'Qt', and the
    file of each class that
    holds an enum or a class it or 'QObject' names: 'QPalette',
    'QSizePolicy' and 'QMetaObject'. It brings in no other class. A
    signature naming another class waits until a program brings that
    class in, or a function gives an object of it; its function is
    on the class all the while, and refuses every call until then."""
    expected = [
      'class files brought in: q_list q_meta_object q_object '
      'q_paint_device q_palette q_size_policy q_widget qt',
      'waits for QFont: True',
      'setFont is there: True',
      'setFont refuses: DispatchException',
      'waits for QFont: False',
      'setFont is there: True',
      'QWidget holds QFont: True',
      'QThread brought in: False',
      'QThread brought in: True',
      'given: QThread',
    ]
    self.assertEqual(self._runAlone(WAITED_FOR), expected)
