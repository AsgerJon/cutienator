"""
TestPrivateClasses tests the classes Qt keeps in headers it calls
private, and hands out all the same: 'QListWidget.model()' gives a
QListModel. cutienator has those classes like any other, and where
Qt's library has no name for one of their functions, the code of the
function is taken from Qt's own source.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

import os
import subprocess
import sys

from worktoy.work_test import BaseTest

import cutienator
from cutienator.occult import Rituals

#  The widgets need an application, so this runs in a Python of its
#  own. Each line it prints is a name, a colon and what was found.
HANDED_OUT = """
from cutienator.QtCore import QAbstractItemModel, QAbstractListModel
from cutienator.QtWidgets import QApplication, QListModel, QListWidget
from cutienator.QtWidgets import QMessageBox, QPushButton, QTableModel
from cutienator.QtWidgets import QTableWidget, QTreeModel, QTreeWidget
from cutienator.QtWidgets import QCalendarWidget, QStyledItemDelegate
from cutienator.QtWidgets import QMainWindow, QMainWindowLayout
from cutienator.QtWidgets import QTableView, QToolBar

app = QApplication([])
widget = QListWidget()
for text in ('apple', 'banana', 'cherry'):
  widget.addItem(text)
model = widget.model()
print('class:', type(model).__name__)
print('built on:', isinstance(model, QListModel),
      isinstance(model, QAbstractListModel),
      isinstance(model, QAbstractItemModel))
print('rows:', model.rowCount())
print('at:', model.at(1).text(), model.at(1) is widget.item(1))
model.move(0, 2)
print('moved:', [widget.item(i).text() for i in range(widget.count())])
taken = model.take(0)
print('taken:', taken.text(), model.rowCount())
model.clear()
print('cleared:', model.rowCount())
print('table:', type(QTableWidget(2, 3).model()) is QTableModel)
print('tree:', type(QTreeWidget().model()) is QTreeModel)
box = QMessageBox()
box.addButton(QMessageBox.StandardButton.Ok)
found = box.button(QMessageBox.StandardButton.Ok)
print('button:', type(found) is QPushButton)
window = QMainWindow()
layout = window.layout()
print('layout:', type(layout) is QMainWindowLayout, layout.documentMode())
print('toolbar:', type(QToolBar(window).layout()).__name__)
children = QCalendarWidget().children()
print('nearest:', [
    sum(1 for child in children if type(child) is cuteClass)
    for cuteClass in (QTableView, QStyledItemDelegate)])
try:
  QListModel(widget)
  print('made: yes')
except Exception as exception:
  print('made:', type(exception).__name__)
"""


class TestPrivateClasses(BaseTest):
  """Runs one program in a Python of its own."""

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  HELPERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  __found_lines__ = None

  @classmethod
  def setUpClass(cls) -> None:
    """Builds the shared object of rituals when a ritual file is newer,
    and runs the program once for every test."""
    super().setUpClass()
    if Rituals.isStale():
      Rituals.summon()
    packageFolder = os.path.dirname(os.path.abspath(cutienator.__file__))
    environment = dict(os.environ)
    known = environment.get('PYTHONPATH', '')
    folders = [os.path.dirname(packageFolder), *known.split(os.pathsep)]
    environment['PYTHONPATH'] = os.pathsep.join(f for f in folders if f)
    environment.setdefault('QT_QPA_PLATFORM', 'offscreen')
    done = subprocess.run(
        (sys.executable, '-B', '-c', HANDED_OUT),
        capture_output=True, text=True, env=environment, timeout=120,
    )
    if done.returncode:
      raise RuntimeError(done.stderr)
    found = dict()
    for line in done.stdout.strip().split('\n'):
      name, _, said = line.partition(': ')
      found[name] = said
    cls.__found_lines__ = found

  def _found(self, name: str) -> str:
    """Gives what the program printed after one name."""
    return self.__found_lines__[name]

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  TESTS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def test_an_object_gets_the_class_it_really_is(self) -> None:
    """The model of a QListWidget, which Qt hands out as a
    QAbstractItemModel, is a QListModel, built on what Qt builds it
    on. A table and a tree have a QTableModel and a QTreeModel."""
    self.assertEqual(self._found('class'), 'QListModel')
    self.assertEqual(self._found('built on'), 'True True True')
    self.assertEqual(self._found('table'), 'True')
    self.assertEqual(self._found('tree'), 'True')

  def test_a_class_qt_gives_out_gets_the_class_it_really_is(self) -> None:
    """A button Qt made, handed out as a QAbstractButton, is a
    QPushButton."""
    self.assertEqual(self._found('button'), 'True')

  def test_the_layout_of_a_main_window(self) -> None:
    """The layout Qt gives a QMainWindow is a QMainWindowLayout, of a
    header Qt calls private, and so is the QToolBarLayout of a
    toolbar. Their own functions can be called."""
    self.assertEqual(self._found('layout'), 'True False')
    self.assertEqual(self._found('toolbar'), 'QToolBarLayout')

  def test_a_class_cutienator_has_not_gives_the_nearest_it_has(
      self) -> None:
    """A QCalendarWidget holds a view and a delegate of classes Qt
    writes inside its own code, on top of QTableView and of
    QStyledItemDelegate. Handed out as QObjects, they are a QTableView
    and a QStyledItemDelegate: the nearest classes there are."""
    self.assertEqual(self._found('nearest'), '[1, 1]')

  def test_what_qt_looks_up_in_the_object(self) -> None:
    """'rowCount' is found by C++ in the object, as for any model."""
    self.assertEqual(self._found('rows'), '3')

  def test_the_own_functions_of_a_private_class(self) -> None:
    """Qt's library has no name for 'at', 'move', 'take' and 'clear'
    of QListModel. Their code comes from Qt's source, and they do to
    the widget what Qt's own do."""
    self.assertEqual(self._found('at'), 'banana True')
    self.assertEqual(self._found('moved'), "['banana', 'apple', 'cherry']")
    self.assertEqual(self._found('taken'), 'banana 2')
    self.assertEqual(self._found('cleared'), '0')

  def test_what_cannot_be_taken_is_left_out(self) -> None:
    """A QListModel cannot be made from Python: its maker leans on the
    tables Qt makes of the class when Qt is built, which Qt's library
    does not offer and Qt's source does not hold."""
    self.assertNotEqual(self._found('made'), 'yes')
