"""
TestQList tests the lists of Qt: 'QList[QUrl]' and its like, each a
cute class of its own, and the functions of Qt that take or give one.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

import os
import subprocess
import sys

from worktoy.waitaminute.dispatch import DispatchException
from worktoy.work_test import BaseTest

from cutienator.cute import MetaCute

import cutienator
from cutienator.QtCore import QList, QMimeData, QModelIndex
from cutienator.QtCore import QModelIndexList, QObject, QObjectList
from cutienator.QtCore import QStringList, QUrl
from cutienator.occult import Rituals

#  A function taking a list of QUrl, called with an empty list before
#  QUrl is brought in. It runs in a Python of its own, since this file
#  brings QUrl in at its top.
EMPTY_BEFORE = """
import sys

from cutienator.QtCore import QMimeData

mime = QMimeData()
print('QUrl brought in:', 'cutienator.QtCore._q_url' in sys.modules)
mime.setUrls([])
print('the empty list went through:', len(mime.urls()))
print('QUrl brought in:', 'cutienator.QtCore._q_url' in sys.modules)
"""


class TestQList(BaseTest):
  """None of these needs an application."""

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  HELPERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @classmethod
  def setUpClass(cls) -> None:
    """Builds the shared object of rituals when a ritual file is newer."""
    super().setUpClass()
    if Rituals.isStale():
      Rituals.summon()

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  TESTS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def test_each_kind_is_a_class(self) -> None:
    """'QList[QUrl]' is a class built on QList, and one class each time
    it is asked for."""
    self.assertTrue(issubclass(QList[QUrl], QList))
    self.assertIs(QList[QUrl], QList[QUrl])
    self.assertEqual(QList[QUrl].__name__, 'QList[QUrl]')
    self.assertIsNot(QList[QUrl], QList[QObject])

  def test_the_names_qt_has_for_a_kind(self) -> None:
    """The kinds Qt named go by that name, and 'QList[...]' gives the
    same class."""
    self.assertIs(QList[str], QStringList)
    self.assertIs(QList[QModelIndex], QModelIndexList)
    self.assertIs(QList[QObject], QObjectList)
    self.assertEqual(QModelIndexList.__name__, 'QModelIndexList')

  def test_what_qt_has_no_list_of(self) -> None:
    """A kind Qt has no code for is refused where it is asked for."""
    for element in (dict, int, QList, 'QUrl'):
      with self.subTest(element=element):
        with self.assertRaises(TypeError):
          QList[element]
    with self.assertRaises(TypeError):
      QList[QUrl][QUrl]
    with self.assertRaises(TypeError):
      QList()

  def test_a_list_reads_as_a_list(self) -> None:
    """'len', a place, a place from the end and 'for', and 'append'
    adds to the C++ list."""
    names = QStringList(['a', 'b'])
    names.append('c')
    self.assertEqual(len(names), 3)
    self.assertEqual((names[0], names[-1], names.at(1)), ('a', 'c', 'b'))
    self.assertEqual([*names], ['a', 'b', 'c'])
    self.assertEqual(str(names), 'QStringList([a, b, c])')
    self.assertEqual(len(QStringList()), 0)
    self.assertEqual([*QStringList(('x', 'y'))], ['x', 'y'])

  def test_a_place_the_list_does_not_have(self) -> None:
    """Qt would end the program, so it is refused before Qt is asked."""
    names = QStringList(['a', 'b'])
    for place in (2, -3, 100):
      with self.subTest(place=place):
        with self.assertRaises(IndexError):
          names[place]
    with self.assertRaises(TypeError):
      names.at('first')
    with self.assertRaises(TypeError):
      names.at(True)

  def test_a_list_holds_its_own_kind(self) -> None:
    """An element of another class is refused on the line that hands
    it over."""
    with self.assertRaises(TypeError) as context:
      QStringList(['a', 1])
    expected = "A 'QStringList' holds 'str' and nothing else"
    self.assertIn(expected, str(context.exception))
    with self.assertRaises(TypeError):
      QStringList(['a']).append(2)
    with self.assertRaises(TypeError) as context:
      QList[QUrl](['text'])
    self.assertIn("A 'QList[QUrl]' holds 'QUrl'", str(context.exception))

  def test_a_function_takes_a_list_and_gives_one(self) -> None:
    """'setUrls' takes a 'QList[QUrl]', and 'urls' gives a new one that
    Python owns."""
    mime = QMimeData()
    urls = QList[QUrl]([QUrl('http://a'), QUrl('http://b')])
    mime.setUrls(urls)
    found = mime.urls()
    self.assertIsInstance(found, QList[QUrl])
    self.assertIsNot(found, urls)
    self.assertTrue(found.uglySide.isOwned())
    self.assertEqual(len(found), 2)
    self.assertTrue(found[1] == QUrl('http://b'))
    self.assertIsInstance(found[0], QUrl)

  def test_a_list_of_python_is_made_into_one(self) -> None:
    """A function taking a list of Qt takes a list or a tuple of
    Python whose every element fits, and no other."""
    mime = QMimeData()
    mime.setUrls([QUrl('http://c')])
    self.assertEqual(len(mime.urls()), 1)
    mime.setUrls((QUrl('http://d'), QUrl('http://e')))
    self.assertEqual(len(mime.urls()), 2)
    mime.setUrls([])
    self.assertEqual(len(mime.urls()), 0)
    with self.assertRaises(DispatchException):
      mime.setUrls(['http://f'])
    with self.assertRaises(DispatchException):
      mime.setUrls(QStringList(['http://g']))

  def test_a_function_gives_a_list_of_text(self) -> None:
    """'formats' gives a QStringList."""
    mime = QMimeData()
    mime.setText('hello')
    formats = mime.formats()
    self.assertIsInstance(formats, QStringList)
    self.assertIn('text/plain', [*formats])

  def test_no_list_waits(self) -> None:
    """A kind is a class from the line that names it, so no signature
    waits for a list."""
    waiting = MetaCute.getStillWaiting()
    self.assertEqual([name for name in waiting if 'List' in name], [])

  def test_a_list_of_objects(self) -> None:
    """'children' gives the list of the very objects, by Qt's name
    for that kind."""
    parent = QObject()
    first, second = QObject(parent), QObject(parent)
    #  Nothing of Qt is made before the first use.
    first.objectName(), second.objectName()
    children = parent.children()
    self.assertIsInstance(children, QObjectList)
    self.assertEqual(len(children), 2)
    self.assertIs(children[0], first)
    self.assertIs(children[1], second)

  def test_an_empty_list_before_what_it_holds(self) -> None:
    """A function taking a list of QUrl takes an empty list before a
    QUrl was ever made: the list brings the file of QUrl in itself."""
    packageFolder = os.path.dirname(os.path.abspath(cutienator.__file__))
    environment = dict(os.environ)
    known = environment.get('PYTHONPATH', '')
    folders = [os.path.dirname(packageFolder), *known.split(os.pathsep)]
    environment['PYTHONPATH'] = os.pathsep.join(f for f in folders if f)
    done = subprocess.run(
        (sys.executable, '-B', '-c', EMPTY_BEFORE),
        capture_output=True, text=True, env=environment, timeout=120,
    )
    self.assertEqual(done.returncode, 0, done.stderr)
    expected = [
        'QUrl brought in: False',
        'the empty list went through: 0',
        'QUrl brought in: True',
    ]
    self.assertEqual(done.stdout.strip().split('\n'), expected)
