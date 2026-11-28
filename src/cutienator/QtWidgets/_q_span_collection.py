"""
QSpanCollection binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/6.12.0/QtWidgets/private/qtableview_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QSpanCollection to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSpanCollection(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QSpanCollection: a plain Python object standing in
  front of one C++ QSpanCollection.

  C++ hands a QSpanCollection around as a copy, so every C++ QSpanCollection
  behind a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QSpanCollection that has a ritual and that Python
  can call so far, 8 names in all: 'addSpan', 'updateSpan', 'spanAt',
  'clear', 'updateInsertedRows', 'updateInsertedColumns',
  'updateRemovedRows', 'updateRemovedColumns'. None can be made from Python:
  one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSpanCollection::~QSpanCollection()': the destructor: Python
    removes its C++ QSpanCollection by it, and has no other use for it.
  - Qt's 'QSet<Span *> QSpanCollection::spansInRect(int x, int y, int w, int
    h) const': gives a type Python has no way to take yet.
  - Qt's 'bool QSpanCollection::cleanSpanSubIndex(SubIndex &subindex, int
    end, bool update)': takes a type Python has no way to hand over yet.

  What to expect
  --------------

  - The C++ QSpanCollection is created at the first use, not by
    'QSpanCollection(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QSpanCollection back gives a copy the ritual made for
    Python, in a new cute QSpanCollection.
  - Each name of Qt's QSpanCollection that has no cute function yet,
    'cleanSpanSubIndex', 'spansInRect', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The classes Qt writes inside QSpanCollection, each a class in here as in
  #  C++.

  class Span(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QSpanCollection::Span: a plain Python object
    standing in front of one C++ QSpanCollection::Span.

    C++ hands a QSpanCollection::Span around as a copy, so every C++
    QSpanCollection::Span behind a cute one is Python's own: it is removed,
    by the ritual named in '__delete_ritual__', when the cute object goes.

    What exists
    -----------

    Every function of Qt's QSpanCollection::Span that has a ritual and that
    Python can call so far, 6 names in all: 'top', 'left', 'bottom', 'right',
    'height', 'width'. It can be made from Python, in 2 ways; see '__init__'.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QSpanCollection::Span::~Span()': the destructor: Python removes
      its C++ QSpanCollection::Span by it, and has no other use for it.

    What to expect
    --------------

    - The C++ QSpanCollection::Span is created at the first use, not by
      'QSpanCollection::Span(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QSpanCollection::Span back gives a copy the ritual
      made for Python, in a new cute QSpanCollection::Span.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QSpanCollection::Span'

    #  Qt's '~QSpanCollection::Span()'. Naming it makes this a value class:
    #  Python owns every C++ QSpanCollection::Span behind a cute one, and
    #  removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN15QSpanCollection4SpanD1Ev'

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    def top(self) -> int:
      """
      Calls Qt's 'int QSpanCollection::Span::top() const'.

      Qt's own words: https://doc.qt.io/qt-6/qspancollection-span.html#top
      """
      #  int QSpanCollection::Span::top() const
      return self.uglySide.call('ritual_ZNK15QSpanCollection4Span3topEv')

    def left(self) -> int:
      """
      Calls Qt's 'int QSpanCollection::Span::left() const'.

      Qt's own words: https://doc.qt.io/qt-6/qspancollection-span.html#left
      """
      #  int QSpanCollection::Span::left() const
      return self.uglySide.call('ritual_ZNK15QSpanCollection4Span4leftEv')

    def bottom(self) -> int:
      """
      Calls Qt's 'int QSpanCollection::Span::bottom() const'.

      Qt's own words: https://doc.qt.io/qt-6/qspancollection-span.html#bottom
      """
      #  int QSpanCollection::Span::bottom() const
      return self.uglySide.call('ritual_ZNK15QSpanCollection4Span6bottomEv')

    def right(self) -> int:
      """
      Calls Qt's 'int QSpanCollection::Span::right() const'.

      Qt's own words: https://doc.qt.io/qt-6/qspancollection-span.html#right
      """
      #  int QSpanCollection::Span::right() const
      return self.uglySide.call('ritual_ZNK15QSpanCollection4Span5rightEv')

    def height(self) -> int:
      """
      Calls Qt's 'int QSpanCollection::Span::height() const'.

      Qt's own words: https://doc.qt.io/qt-6/qspancollection-span.html#height
      """
      #  int QSpanCollection::Span::height() const
      return self.uglySide.call('ritual_ZNK15QSpanCollection4Span6heightEv')

    def width(self) -> int:
      """
      Calls Qt's 'int QSpanCollection::Span::width() const'.

      Qt's own words: https://doc.qt.io/qt-6/qspancollection-span.html#width
      """
      #  int QSpanCollection::Span::width() const
      return self.uglySide.call('ritual_ZNK15QSpanCollection4Span5widthEv')

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @overload()
    def __init__(self) -> None:
      """
      Notes what was given, for Qt's 'QSpanCollection::Span::Span()', which
      is called at the first use.

      Qt's own words: https://doc.qt.io/qt-6/qspancollection-span.html#Span
      """
      #  QSpanCollection::Span::Span()
      self._noteCreation(QSpanCollection.Span, lambda: Rituals.call(
          'ritual_ZN15QSpanCollection4SpanC1Ev',
      ))

    @overload(int, int, int, int)
    def __init__(
        self,
        row: int,
        column: int,
        rowCount: int,
        columnCount: int,
    ) -> None:
      """
      Notes what was given, for Qt's 'QSpanCollection::Span::Span(int row,
      int column, int rowCount, int columnCount)', which is called at the
      first use.

      Qt's own words: https://doc.qt.io/qt-6/qspancollection-span.html#Span

      Parameters
      ----------

      row : int
        Passed on as it is.

      column : int
        Passed on as it is.

      rowCount : int
        Passed on as it is.

      columnCount : int
        Passed on as it is.
      """
      #  QSpanCollection::Span::Span(int row, int column, int rowCount, int
      #      columnCount)
      self._noteCreation(QSpanCollection.Span, lambda: Rituals.call(
          'ritual_ZN15QSpanCollection4SpanC1Eiiii',
          row, column, rowCount, columnCount,
      ))

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSpanCollection'

  #  Qt's '~QSpanCollection()'. Naming it makes this a value class: Python
  #  owns every C++ QSpanCollection behind a cute one, and removes it by this
  #  ritual.
  __delete_ritual__ = 'ritual_ZN15QSpanCollectionD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int, int)
  def spanAt(self, x: int, y: int) -> Optional[Span]:
    """
    Calls Qt's 'Span *QSpanCollection::spanAt(int x, int y) const'.

    Qt's own words: https://doc.qt.io/qt-6/qspancollection.html#spanAt

    Parameters
    ----------

    x : int
      Passed on as it is.

    y : int
      Passed on as it is.

    Returns
    -------

    Optional[Span]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Span *QSpanCollection::spanAt(int x, int y) const
    address = self.uglySide.call(
        'ritual_ZNK15QSpanCollection6spanAtEii', x, y,
    )
    return QSpanCollection.Span._cuteAt(address)

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

  @overload(Span)
  @overload(NoneType)
  def addSpan(self, span: Optional[Span]) -> None:
    """
    Calls Qt's 'void QSpanCollection::addSpan(Span *span)'.

    Qt's own words: https://doc.qt.io/qt-6/qspancollection.html#addSpan

    Parameters
    ----------

    span : Optional[Span]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSpanCollection::addSpan(Span *span)
    self.uglySide.call(
        'ritual_ZN15QSpanCollection7addSpanEPNS_4SpanE',
        self._addressOf(span),
    )

  @overload(Span, int)
  @overload(NoneType, int)
  def updateSpan(self, span: Optional[Span], old_height: int) -> None:
    """
    Calls Qt's 'void QSpanCollection::updateSpan(Span *span, int
    old_height)'.

    Qt's own words: https://doc.qt.io/qt-6/qspancollection.html#updateSpan

    Parameters
    ----------

    span : Optional[Span]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    old_height : int
      Passed on as it is.
    """
    #  void QSpanCollection::updateSpan(Span *span, int old_height)
    self.uglySide.call(
        'ritual_ZN15QSpanCollection10updateSpanEPNS_4SpanEi',
        self._addressOf(span), old_height,
    )

  def clear(self) -> None:
    """
    Calls Qt's 'void QSpanCollection::clear()'.

    Qt's own words: https://doc.qt.io/qt-6/qspancollection.html#clear
    """
    #  void QSpanCollection::clear()
    self.uglySide.call('ritual_ZN15QSpanCollection5clearEv')

  @overload(int, int)
  def updateInsertedRows(self, start: int, end: int) -> None:
    """
    Calls Qt's 'void QSpanCollection::updateInsertedRows(int start, int
    end)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qspancollection.html#updateInsertedRows

    Parameters
    ----------

    start : int
      Passed on as it is.

    end : int
      Passed on as it is.
    """
    #  void QSpanCollection::updateInsertedRows(int start, int end)
    self.uglySide.call(
        'ritual_ZN15QSpanCollection18updateInsertedRowsEii', start, end,
    )

  @overload(int, int)
  def updateInsertedColumns(self, start: int, end: int) -> None:
    """
    Calls Qt's 'void QSpanCollection::updateInsertedColumns(int start, int
    end)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qspancollection.html#updateInsertedColumns

    Parameters
    ----------

    start : int
      Passed on as it is.

    end : int
      Passed on as it is.
    """
    #  void QSpanCollection::updateInsertedColumns(int start, int end)
    self.uglySide.call(
        'ritual_ZN15QSpanCollection21updateInsertedColumnsEii', start, end,
    )

  @overload(int, int)
  def updateRemovedRows(self, start: int, end: int) -> None:
    """
    Calls Qt's 'void QSpanCollection::updateRemovedRows(int start, int end)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qspancollection.html#updateRemovedRows

    Parameters
    ----------

    start : int
      Passed on as it is.

    end : int
      Passed on as it is.
    """
    #  void QSpanCollection::updateRemovedRows(int start, int end)
    self.uglySide.call(
        'ritual_ZN15QSpanCollection17updateRemovedRowsEii', start, end,
    )

  @overload(int, int)
  def updateRemovedColumns(self, start: int, end: int) -> None:
    """
    Calls Qt's 'void QSpanCollection::updateRemovedColumns(int start, int
    end)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qspancollection.html#updateRemovedColumns

    Parameters
    ----------

    start : int
      Passed on as it is.

    end : int
      Passed on as it is.
    """
    #  void QSpanCollection::updateRemovedColumns(int start, int end)
    self.uglySide.call(
        'ritual_ZN15QSpanCollection20updateRemovedColumnsEii', start, end,
    )

  @staticmethod
  def cleanSpanSubIndex(*__, **_) -> Never:
    """
    Qt's 'bool QSpanCollection::cleanSpanSubIndex(SubIndex &subindex, int
    end, bool update)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QSpanCollection.cleanSpanSubIndex' has no cute function yet. Qt's "
        "'bool QSpanCollection::cleanSpanSubIndex(SubIndex &subindex, int "
        "end, bool update)': takes a type Python has no way to hand over "
        "yet.")

  @staticmethod
  def spansInRect(*__, **_) -> Never:
    """
    Qt's 'QSet<Span *> QSpanCollection::spansInRect(int x, int y, int w, int
    h) const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QSpanCollection.spansInRect' has no cute function yet. Qt's "
        "'QSet<Span *> QSpanCollection::spansInRect(int x, int y, int w, "
        "int h) const': gives a type Python has no way to take yet.")
