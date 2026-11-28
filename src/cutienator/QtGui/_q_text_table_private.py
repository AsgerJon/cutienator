"""
QTextTablePrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qtexttable_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QTextTablePrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from . import QTextFramePrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QChar
  from . import QTextDocumentPrivate, QTextTable, QTextTableFormat
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QChar = WAIT['QChar']
  QTextDocumentPrivate = WAIT['QTextDocumentPrivate']
  QTextTableFormat = WAIT['QTextTableFormat']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QTextTablePrivate(QTextFramePrivate):
  """
  The cute side of Qt's QTextTablePrivate: a plain Python object standing in
  front of one C++ QTextTablePrivate.

  It is built on the cute 'QTextFramePrivate', as Qt's QTextTablePrivate is
  built on Qt's QTextFramePrivate, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QTextTablePrivate that has a ritual and that Python
  can call so far, 5 names in all: 'q_func', 'createTable', 'fragmentAdded',
  'fragmentRemoved', 'update'. None can be made from Python: one comes out of
  a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QTextTable *QTextTablePrivate::q_func() const': takes in
    Python what 'QTextTable *QTextTablePrivate::q_func()' takes.

  What has no ritual
  ------------------

  2 of the 8 functions Qt declares: 1 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file; 1 leans on
  'QTextTablePrivate.

  What to expect
  --------------

  - The C++ QTextTablePrivate is created at the first use, not by
    'QTextTablePrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QTextTablePrivate.
  - Each name of Qt's QTextTablePrivate that has no cute function yet,
    '__init__', 'findCellIndex', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QTextDocumentPrivate, int, int, int, QTextTableFormat)
  @overload(NoneType, int, int, int, QTextTableFormat)
  def createTable(
      a0: Optional[QTextDocumentPrivate],
      pos: int,
      rows: int,
      cols: int,
      tableFormat: QTextTableFormat,
  ) -> Optional[QTextTable]:
    """
    Calls Qt's 'QTextTable
    *QTextTablePrivate::createTable(QTextDocumentPrivate *a0, int pos, int
    rows, int cols, const QTextTableFormat &tableFormat)'.

    Qt's own words: https://doc.qt.io/qt-6/qtexttableprivate.html#createTable

    Parameters
    ----------

    a0 : Optional[QTextDocumentPrivate]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    pos : int
      Passed on as it is.

    rows : int
      Passed on as it is.

    cols : int
      Passed on as it is.

    tableFormat : QTextTableFormat
      Passed on as a value: Qt reads the C++ QTextTableFormat, which stays
      Python's own.

    Returns
    -------

    Optional[QTextTable]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QTextTable *QTextTablePrivate::createTable(QTextDocumentPrivate *a0,
    #      int pos, int rows, int cols, const QTextTableFormat &tableFormat)
    address = Rituals.call(
        'ritual_ZN17QTextTablePrivate11createTableEP20QTextDocumentPrivatei'
        'iiRK16QTextTableFormat',
        CuteMixin._addressOf(a0), pos, rows, cols,
        CuteMixin._valueOf(tableFormat),
    )
    from . import QTextTable
    return QTextTable._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QTextTablePrivate'

  #  A C++ QTextTablePrivate Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QTextTablePrivate'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'QTextTablePrivate::QTextTablePrivate(QTextDocument *document)':
    leans on 'QTextTablePrivate::fragmentAdded(QChar, unsigned int)', which
    Qt's source does not mark for use from outside Qt and has no code for
    that could be taken.
    """
    raise NotImplementedError(
        "'QTextTablePrivate.__init__' has no cute function yet. Qt's "
        "'QTextTablePrivate::QTextTablePrivate(QTextDocument *document)': "
        "leans on 'QTextTablePrivate::fragmentAdded(QChar, unsigned int)', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def q_func(self) -> Optional[QTextTable]:
    """
    Calls Qt's 'QTextTable *QTextTablePrivate::q_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qtexttableprivate.html#q_func

    Returns
    -------

    Optional[QTextTable]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QTextTable *QTextTablePrivate::q_func()
    address = self.uglySide.call('ritual_ZN17QTextTablePrivate6q_funcEv')
    from . import QTextTable
    return QTextTable._cuteAt(address)

  @overload(QChar, int)
  def fragmentAdded(self, type: QChar, fragment: int) -> None:
    """
    Calls Qt's 'void QTextTablePrivate::fragmentAdded(QChar type, uint
    fragment)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtexttableprivate.html#fragmentAdded

    Parameters
    ----------

    type : QChar
      Passed on as a value: Qt reads the C++ QChar, which stays Python's own.

    fragment : int
      Passed on as it is.
    """
    #  void QTextTablePrivate::fragmentAdded(QChar type, uint fragment)
    self.uglySide.call(
        'ritual_ZN17QTextTablePrivate13fragmentAddedE5QCharj',
        self._valueOf(type), fragment,
    )

  @overload(QChar, int)
  def fragmentRemoved(self, type: QChar, fragment: int) -> None:
    """
    Calls Qt's 'void QTextTablePrivate::fragmentRemoved(QChar type, uint
    fragment)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtexttableprivate.html#fragmentRemoved

    Parameters
    ----------

    type : QChar
      Passed on as a value: Qt reads the C++ QChar, which stays Python's own.

    fragment : int
      Passed on as it is.
    """
    #  void QTextTablePrivate::fragmentRemoved(QChar type, uint fragment)
    ritual = 'ritual_ZN17QTextTablePrivate15fragmentRemovedE5QCharj'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QTextTablePrivate15fragmentRemovedE5QCharj'
    self.uglySide.call(ritual, self._valueOf(type), fragment)

  def update(self) -> None:
    """
    Calls Qt's 'void QTextTablePrivate::update() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtexttableprivate.html#update
    """
    #  void QTextTablePrivate::update() const
    self.uglySide.call('ritual_ZNK17QTextTablePrivate6updateEv')

  @staticmethod
  def findCellIndex(*__, **_) -> Never:
    """
    Qt's 'int QTextTablePrivate::findCellIndex(int fragment) const': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: no matching function for call to object of type
    'std::less<void>'.
    """
    raise NotImplementedError(
        "'QTextTablePrivate.findCellIndex' has no cute function yet. Qt's "
        "'int QTextTablePrivate::findCellIndex(int fragment) const': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: no matching function for call to "
        "object of type 'std::less<void>'.")
