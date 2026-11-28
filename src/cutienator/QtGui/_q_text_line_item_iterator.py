"""
QTextLineItemIterator binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qtextengine_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QTextLineItemIterator to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from . import QTextLayout

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QPointF
  from . import QFixed, QTextEngine
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QFixed = WAIT['QFixed']
  QPointF = WAIT['QPointF']
  QTextEngine = WAIT['QTextEngine']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QTextLineItemIterator(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QTextLineItemIterator: a plain Python object standing
  in front of one C++ QTextLineItemIterator.

  C++ hands a QTextLineItemIterator around as a copy, so every C++
  QTextLineItemIterator behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QTextLineItemIterator that has a ritual and that
  Python can call so far, 4 names in all: 'atEnd', 'atBeginning',
  'getSelectionBounds', 'isOutsideSelection'. It can be made from Python, in
  1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QScriptItem &QTextLineItemIterator::next()': gives a type Python
    has no way to take yet.
  - Qt's 'QTextLineItemIterator::~QTextLineItemIterator()': the destructor:
    Python removes its C++ QTextLineItemIterator by it, and has no other use
    for it.

  What to expect
  --------------

  - The C++ QTextLineItemIterator is created at the first use, not by
    'QTextLineItemIterator(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QTextLineItemIterator back gives a copy the ritual
    made for Python, in a new cute QTextLineItemIterator.
  - Each name of Qt's QTextLineItemIterator that has no cute function yet,
    'next', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QTextLineItemIterator'

  #  Qt's '~QTextLineItemIterator()'. Naming it makes this a value class:
  #  Python owns every C++ QTextLineItemIterator behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN21QTextLineItemIteratorD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def atEnd(self) -> bool:
    """
    Calls Qt's 'bool QTextLineItemIterator::atEnd() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextlineitemiterator.html#atEnd
    """
    #  bool QTextLineItemIterator::atEnd() const
    return self.uglySide.call('ritual_ZNK21QTextLineItemIterator5atEndEv')

  def atBeginning(self) -> bool:
    """
    Calls Qt's 'bool QTextLineItemIterator::atBeginning() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextlineitemiterator.html#atBeginning
    """
    #  bool QTextLineItemIterator::atBeginning() const
    return self.uglySide.call(
        'ritual_ZNK21QTextLineItemIterator11atBeginningEv',
    )

  @overload(QFixed, QFixed)
  @overload(QFixed, NoneType)
  @overload(NoneType, QFixed)
  @overload(NoneType, NoneType)
  def getSelectionBounds(
      self,
      selectionX: Optional[QFixed],
      selectionWidth: Optional[QFixed],
  ) -> bool:
    """
    Calls Qt's 'bool QTextLineItemIterator::getSelectionBounds(QFixed
    *selectionX, QFixed *selectionWidth) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextlineitemiterator.html#getSelectionBounds

    Parameters
    ----------

    selectionX : Optional[QFixed]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    selectionWidth : Optional[QFixed]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QTextLineItemIterator::getSelectionBounds(QFixed *selectionX,
    #      QFixed *selectionWidth) const
    return self.uglySide.call(
        'ritual_ZNK21QTextLineItemIterator18getSelectionBoundsEP6QFixedS1_',
        self._addressOf(selectionX), self._addressOf(selectionWidth),
    )

  def isOutsideSelection(self) -> bool:
    """
    Calls Qt's 'bool QTextLineItemIterator::isOutsideSelection() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextlineitemiterator.html#isOutsideSelection
    """
    #  bool QTextLineItemIterator::isOutsideSelection() const
    return self.uglySide.call(
        'ritual_ZNK21QTextLineItemIterator18isOutsideSelectionEv',
    )

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

  @overload(QTextEngine, int)
  @overload(NoneType, int)
  @overload(QTextEngine, int, QPointF)
  @overload(NoneType, int, QPointF)
  @overload(QTextEngine, int, QPointF, QTextLayout.FormatRange)
  @overload(QTextEngine, int, QPointF, NoneType)
  @overload(NoneType, int, QPointF, QTextLayout.FormatRange)
  @overload(NoneType, int, QPointF, NoneType)
  def __init__(
      self,
      eng: Optional[QTextEngine],
      lineNum: int,
      pos: Optional[QPointF] = None,
      _selection: Optional[QTextLayout.FormatRange] = None,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QTextLineItemIterator::QTextLineItemIterator(QTextEngine *eng, int
    lineNum, const QPointF &pos, const QTextLayout::FormatRange
    *_selection)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextlineitemiterator.html#QTextLineItemIterator

    Parameters
    ----------

    eng : Optional[QTextEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    lineNum : int
      Passed on as it is.

    pos : Optional[QPointF]
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own. May be left out, as in Qt: a new 'QPointF()' is then passed on.

    _selection : Optional[QTextLayout.FormatRange]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QTextLineItemIterator::QTextLineItemIterator(QTextEngine *eng, int
    #      lineNum, const QPointF &pos, const QTextLayout::FormatRange
    #      *_selection)
    if pos is None:
      from ..QtCore import QPointF
      pos = QPointF()
    self._noteCreation(QTextLineItemIterator, lambda: Rituals.call(
        'ritual_ZN21QTextLineItemIteratorC1EP11QTextEngineiRK7QPointFPKN11Q'
        'TextLayout11FormatRangeE',
        self._addressOf(eng), lineNum, self._valueOf(pos, 'QPointF'),
        self._addressOf(_selection),
    ))

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

  @staticmethod
  def next(*__, **_) -> Never:
    """
    Qt's 'QScriptItem &QTextLineItemIterator::next()': gives a type Python
    has no way to take yet.
    """
    raise NotImplementedError(
        "'QTextLineItemIterator.next' has no cute function yet. Qt's "
        "'QScriptItem &QTextLineItemIterator::next()': gives a type Python "
        "has no way to take yet.")
