"""
QTextEngine binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qtextengine_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QTextEngine to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import Qt
from . import QTextCursor

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QCharAttributes, QLineF
  from . import QAbstractTextDocumentLayout, QFixed, QFont, QFontEngine
  from . import QGlyphLayout, QPainter, QPen, QScriptItem, QScriptLine
  from . import QTextCharFormat, QTextFormatCollection, glyph_metrics_t
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QFixed = WAIT['QFixed']
  QFont = WAIT['QFont']
  QLineF = WAIT['QLineF']
  QPainter = WAIT['QPainter']
  QScriptItem = WAIT['QScriptItem']
  QScriptLine = WAIT['QScriptLine']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QTextEngine(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QTextEngine: a plain Python object standing in front
  of one C++ QTextEngine.

  C++ hands a QTextEngine around as a copy, so every C++ QTextEngine behind a
  cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QTextEngine that has a ritual and that Python can
  call so far, 56 names in all: 'invalidate', 'clearLineData', 'validate',
  'itemize', 'isRightToLeft', 'attributes', 'shape', 'justify', 'alignLine',
  'width', 'boundingBox', 'tightBoundingBox', 'length', 'fontEngine', 'font',
  'availableGlyphs', 'shapedGlyphs', 'ensureSpace', 'freeMemory', 'findItem',
  'formatCollection', 'format', 'docLayout', 'formatIndex',
  'calculateTabWidth', 'visualCursorMovement', 'preeditAreaPosition',
  'preeditAreaText', 'setPreeditArea', 'hasFormats', 'init', 'indexFormats',
  'resolveFormats', 'atWordSeparator', 'elidedText', 'shapeLine',
  'leadingSpaceWidth', 'offsetInLigature', 'positionInLigature',
  'previousLogicalPosition', 'nextLogicalPosition',
  'lineNumberForTextPosition', 'positionAfterVisualMovement',
  'resetFontEngineCache', 'enableDelayDecorations', 'addUnderline',
  'addStrikeOut', 'addOverline', 'drawDecorations', 'clearDecorations',
  'adjustUnderlines', 'setBoundary', 'addRequiredBoundaries', 'shapeText',
  'endOfLine', 'beginningOfLine'. It can be made from Python, in 2 ways; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QTextEngine::~QTextEngine()': the destructor: Python removes its
    C++ QTextEngine by it, and has no other use for it.
  - Qt's 'void QTextEngine::bidiReorder(int numRuns, const quint8 *levels,
    int *visualOrder)': names 'quint8', which has no cute class yet.
  - Qt's 'QList<QTextLayout::FormatRange> QTextEngine::formats() const':
    gives a type Python has no way to take yet.
  - Qt's 'void QTextEngine::setFormats(const QList<QTextLayout::FormatRange>
    &formats)': takes a type Python has no way to hand over yet.
  - Qt's 'std::vector<int> QTextEngine::insertionPointsForLine(int lineNum)':
    gives a type Python has no way to take yet.
  - Qt's 'void QTextEngine::addItemDecoration(QPainter *painter, const QLineF
    &line, ItemDecorationList *decorationList)': names
    'QTextEngine::ItemDecorationList', which has no cute class yet.
  - Qt's 'void QTextEngine::drawItemDecorationList(QPainter *painter, const
    ItemDecorationList &decorationList)': takes a type Python has no way to
    hand over yet.
  - Qt's 'int QTextEngine::shapeTextWithHarfbuzzNG(const QScriptItem &si,
    const ushort *string, int stringBaseIndex, int stringLength, int
    itemLength, QFontEngine *fontEngine, QSpan<uint> itemBoundaries, bool
    kerningEnabled, bool hasLetterSpacing, const QMap<QFont::Tag, quint32>
    &features) const': names 'ushort', which has no cute class yet.
  - Qt's 'int QTextEngine::getClusterLength(unsigned short *logClusters,
    const QCharAttributes *attributes, int from, int to, int glyph_pos, int
    *start)': takes a number to change where it is.

  What has no ritual
  ------------------

  2 of the 71 functions Qt declares: 1 takes or gives a type that cannot be
  passed yet; 1 the compiler refuses its ritual as it would be written here.

  What to expect
  --------------

  - The C++ QTextEngine is created at the first use, not by
    'QTextEngine(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QTextEngine back gives a copy the ritual made for
    Python, in a new cute QTextEngine.
  - Each name of Qt's QTextEngine that has no cute function yet,
    'addItemDecoration', 'bidiReorder', 'drawItemDecorationList', 'formats',
    'getClusterLength', 'insertionPointsForLine', 'logClusters',
    'setFormats', 'shapeTextWithHarfbuzzNG', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QTextEngine, each a class in here as in C++,
  #  and the names Qt has for the combinations of its flags enums.

  class LayoutState(CuteNum):
    """
    The enum 'QTextEngine::LayoutState' of Qt, with the 3 names Qt gives in
    it.
    """

    LayoutEmpty = Kee[int](0)
    InLayout = Kee[int](1)
    LayoutFailed = Kee[int](2)

  class Mode(CuteNum):
    """
    The enum 'QTextEngine::Mode' of Qt, with the 1 names Qt gives in it.
    """

    WidthOnly = Kee[int](7)

  #  The classes Qt writes inside QTextEngine, each a class in here as in
  #  C++.

  class ItemDecoration(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QTextEngine::ItemDecoration: a plain Python object
    standing in front of one C++ QTextEngine::ItemDecoration.

    C++ hands a QTextEngine::ItemDecoration around as a copy, so every C++
    QTextEngine::ItemDecoration behind a cute one is Python's own: it is
    removed, by the ritual named in '__delete_ritual__', when the cute object
    goes.

    What exists
    -----------

    No function of Qt's QTextEngine::ItemDecoration yet. It can be made from
    Python, in 2 ways; see '__init__'.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QTextEngine::ItemDecoration::~ItemDecoration()': the destructor:
      Python removes its C++ QTextEngine::ItemDecoration by it, and has no
      other use for it.

    What to expect
    --------------

    - The C++ QTextEngine::ItemDecoration is created at the first use, not by
      'QTextEngine::ItemDecoration(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QTextEngine::ItemDecoration back gives a copy the
      ritual made for Python, in a new cute QTextEngine::ItemDecoration.
    """

    #  The cute classes this class names and is not built on. Each waits
    #  until it is made; see 'WAIT'. A type checker reads the imports at the
    #  top of the file instead.
    if not TYPE_CHECKING:
      QPen = WAIT['QPen']

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QTextEngine::ItemDecoration'

    #  Qt's '~QTextEngine::ItemDecoration()'. Naming it makes this a value
    #  class: Python owns every C++ QTextEngine::ItemDecoration behind a cute
    #  one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN11QTextEngine14ItemDecorationD1Ev'

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

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
      Notes what was given, for Qt's
      'QTextEngine::ItemDecoration::ItemDecoration()', which is called at the
      first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qtextengine-itemdecoration.html#ItemDecoration
      """
      #  QTextEngine::ItemDecoration::ItemDecoration()
      self._noteCreation(QTextEngine.ItemDecoration, lambda: Rituals.call(
          'ritual_ZN11QTextEngine14ItemDecorationC1Ev',
      ))

    @overload(float, float, float, QPen)
    def __init__(self, x1: float, x2: float, y: float, pen: QPen) -> None:
      """
      Notes what was given, for Qt's
      'QTextEngine::ItemDecoration::ItemDecoration(qreal x1, qreal x2, qreal
      y, const QPen &pen)', which is called at the first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qtextengine-itemdecoration.html#ItemDecoration

      Parameters
      ----------

      x1 : float
        Passed on as it is.

      x2 : float
        Passed on as it is.

      y : float
        Passed on as it is.

      pen : QPen
        Passed on as a value: Qt reads the C++ QPen, which stays Python's
        own.
      """
      #  QTextEngine::ItemDecoration::ItemDecoration(qreal x1, qreal x2,
      #      qreal y, const QPen &pen)
      self._noteCreation(QTextEngine.ItemDecoration, lambda: Rituals.call(
          'ritual_ZN11QTextEngine14ItemDecorationC1EdddRK4QPen',
          x1, x2, y, self._valueOf(pen),
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

  class LayoutData(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QTextEngine::LayoutData: a plain Python object
    standing in front of one C++ QTextEngine::LayoutData.

    C++ hands a QTextEngine::LayoutData around as a copy, so every C++
    QTextEngine::LayoutData behind a cute one is Python's own: it is removed,
    by the ritual named in '__delete_ritual__', when the cute object goes.

    What exists
    -----------

    Every function of Qt's QTextEngine::LayoutData that has a ritual and that
    Python can call so far, 1 name in all: 'reallocate'. It can be made from
    Python, in 1 way; see '__init__'.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QTextEngine::LayoutData::LayoutData(const QString &str, void
      **stack_memory, qsizetype mem_size)': takes a type Python has no way to
      hand over yet.
    - Qt's 'QTextEngine::LayoutData::~LayoutData()': the destructor: Python
      removes its C++ QTextEngine::LayoutData by it, and has no other use for
      it.

    What to expect
    --------------

    - The C++ QTextEngine::LayoutData is created at the first use, not by
      'QTextEngine::LayoutData(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QTextEngine::LayoutData back gives a copy the
      ritual made for Python, in a new cute QTextEngine::LayoutData.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QTextEngine::LayoutData'

    #  Qt's '~QTextEngine::LayoutData()'. Naming it makes this a value class:
    #  Python owns every C++ QTextEngine::LayoutData behind a cute one, and
    #  removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN11QTextEngine10LayoutDataD1Ev'

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

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
      Notes what was given, for Qt's 'QTextEngine::LayoutData::LayoutData()',
      which is called at the first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qtextengine-layoutdata.html#LayoutData
      """
      #  QTextEngine::LayoutData::LayoutData()
      self._noteCreation(QTextEngine.LayoutData, lambda: Rituals.call(
          'ritual_ZN11QTextEngine10LayoutDataC1Ev',
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

    @overload(int)
    def reallocate(self, totalGlyphs: int) -> bool:
      """
      Calls Qt's 'bool QTextEngine::LayoutData::reallocate(int totalGlyphs)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qtextengine-layoutdata.html#reallocate

      Parameters
      ----------

      totalGlyphs : int
        Passed on as it is.
      """
      #  bool QTextEngine::LayoutData::reallocate(int totalGlyphs)
      return self.uglySide.call(
          'ritual_ZN11QTextEngine10LayoutData10reallocateEi', totalGlyphs,
      )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(THIS)
  @overload(NoneType)
  def init(e: Optional[QTextEngine]) -> None:
    """
    Calls Qt's 'void QTextEngine::init(QTextEngine *e)'.

    Qt's own words: https://doc.qt.io/qt-6/qtextengine.html#init

    Parameters
    ----------

    e : Optional[QTextEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QTextEngine::init(QTextEngine *e)
    Rituals.call('ritual_ZN11QTextEngine4initEPS_', CuteMixin._addressOf(e))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QTextEngine'

  #  Qt's '~QTextEngine()'. Naming it makes this a value class: Python owns
  #  every C++ QTextEngine behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN11QTextEngineD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isRightToLeft(self) -> bool:
    """
    Calls Qt's 'bool QTextEngine::isRightToLeft() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextengine.html#isRightToLeft
    """
    #  bool QTextEngine::isRightToLeft() const
    return self.uglySide.call('ritual_ZNK11QTextEngine13isRightToLeftEv')

  def attributes(self) -> Optional[QCharAttributes]:
    """
    Calls Qt's 'const QCharAttributes *QTextEngine::attributes() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextengine.html#attributes

    Returns
    -------

    Optional[QCharAttributes]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QCharAttributes *QTextEngine::attributes() const
    address = self.uglySide.call('ritual_ZNK11QTextEngine10attributesEv')
    from ..QtCore import QCharAttributes
    return QCharAttributes._cuteAt(address)

  @overload(int, int)
  def width(self, charFrom: int, numChars: int) -> QFixed:
    """
    Calls Qt's 'QFixed QTextEngine::width(int charFrom, int numChars) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextengine.html#width

    Parameters
    ----------

    charFrom : int
      Passed on as it is.

    numChars : int
      Passed on as it is.

    Returns
    -------

    QFixed
      A new cute QFixed around the copy Qt gave back. Python owns it.
    """
    #  QFixed QTextEngine::width(int charFrom, int numChars) const
    address = self.uglySide.call(
        'ritual_ZNK11QTextEngine5widthEii', charFrom, numChars,
    )
    from . import QFixed
    return QFixed._cuteOwning(address)

  @overload(int, int)
  def boundingBox(self, from_: int, len: int) -> glyph_metrics_t:
    """
    Calls Qt's 'glyph_metrics_t QTextEngine::boundingBox(int from, int len)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextengine.html#boundingBox

    Parameters
    ----------

    from_ : int
      Passed on as it is.

    len : int
      Passed on as it is.

    Returns
    -------

    glyph_metrics_t
      A new cute glyph_metrics_t around the copy Qt gave back. Python owns
      it.
    """
    #  glyph_metrics_t QTextEngine::boundingBox(int from, int len) const
    address = self.uglySide.call(
        'ritual_ZNK11QTextEngine11boundingBoxEii', from_, len,
    )
    from . import glyph_metrics_t
    return glyph_metrics_t._cuteOwning(address)

  @overload(int, int)
  def tightBoundingBox(self, from_: int, len: int) -> glyph_metrics_t:
    """
    Calls Qt's 'glyph_metrics_t QTextEngine::tightBoundingBox(int from, int
    len) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextengine.html#tightBoundingBox

    Parameters
    ----------

    from_ : int
      Passed on as it is.

    len : int
      Passed on as it is.

    Returns
    -------

    glyph_metrics_t
      A new cute glyph_metrics_t around the copy Qt gave back. Python owns
      it.
    """
    #  glyph_metrics_t QTextEngine::tightBoundingBox(int from, int len) const
    address = self.uglySide.call(
        'ritual_ZNK11QTextEngine16tightBoundingBoxEii', from_, len,
    )
    from . import glyph_metrics_t
    return glyph_metrics_t._cuteOwning(address)

  @overload(int)
  def length(self, item: int) -> int:
    """
    Calls Qt's 'int QTextEngine::length(int item) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextengine.html#length

    Parameters
    ----------

    item : int
      Passed on as it is.
    """
    #  int QTextEngine::length(int item) const
    return self.uglySide.call('ritual_ZNK11QTextEngine6lengthEi', item)

  @overload(QScriptItem)
  @overload(NoneType)
  def length(self, si: Optional[QScriptItem]) -> int:
    """
    Calls Qt's 'int QTextEngine::length(const QScriptItem *si) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextengine.html#length

    Parameters
    ----------

    si : Optional[QScriptItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  int QTextEngine::length(const QScriptItem *si) const
    return self.uglySide.call(
        'ritual_ZNK11QTextEngine6lengthEPK11QScriptItem',
        self._addressOf(si),
    )

  @overload(QScriptItem)
  @overload(QScriptItem, QFixed)
  @overload(QScriptItem, NoneType)
  @overload(QScriptItem, QFixed, QFixed)
  @overload(QScriptItem, QFixed, NoneType)
  @overload(QScriptItem, NoneType, QFixed)
  @overload(QScriptItem, NoneType, NoneType)
  @overload(QScriptItem, QFixed, QFixed, QFixed)
  @overload(QScriptItem, QFixed, QFixed, NoneType)
  @overload(QScriptItem, QFixed, NoneType, QFixed)
  @overload(QScriptItem, QFixed, NoneType, NoneType)
  @overload(QScriptItem, NoneType, QFixed, QFixed)
  @overload(QScriptItem, NoneType, QFixed, NoneType)
  @overload(QScriptItem, NoneType, NoneType, QFixed)
  @overload(QScriptItem, NoneType, NoneType, NoneType)
  def fontEngine(
      self,
      si: QScriptItem,
      ascent: Optional[QFixed] = None,
      descent: Optional[QFixed] = None,
      leading: Optional[QFixed] = None,
  ) -> Optional[QFontEngine]:
    """
    Calls Qt's 'QFontEngine *QTextEngine::fontEngine(const QScriptItem &si,
    QFixed *ascent, QFixed *descent, QFixed *leading) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextengine.html#fontEngine

    Parameters
    ----------

    si : QScriptItem
      Passed on as a value: Qt reads the C++ QScriptItem, which stays
      Python's own.

    ascent : Optional[QFixed]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    descent : Optional[QFixed]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    leading : Optional[QFixed]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    Returns
    -------

    Optional[QFontEngine]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QFontEngine *QTextEngine::fontEngine(const QScriptItem &si, QFixed
    #      *ascent, QFixed *descent, QFixed *leading) const
    address = self.uglySide.call(
        'ritual_ZNK11QTextEngine10fontEngineERK11QScriptItemP6QFixedS4_S4_',
        self._valueOf(si), self._addressOf(ascent), self._addressOf(descent),
        self._addressOf(leading),
    )
    from . import QFontEngine
    return QFontEngine._cuteAt(address)

  @overload(QScriptItem)
  def font(self, si: QScriptItem) -> QFont:
    """
    Calls Qt's 'QFont QTextEngine::font(const QScriptItem &si) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextengine.html#font

    Parameters
    ----------

    si : QScriptItem
      Passed on as a value: Qt reads the C++ QScriptItem, which stays
      Python's own.

    Returns
    -------

    QFont
      A new cute QFont around the copy Qt gave back. Python owns it.
    """
    #  QFont QTextEngine::font(const QScriptItem &si) const
    address = self.uglySide.call(
        'ritual_ZNK11QTextEngine4fontERK11QScriptItem', self._valueOf(si),
    )
    from . import QFont
    return QFont._cuteOwning(address)

  @overload()
  def font(self) -> QFont:
    """
    Calls Qt's 'QFont QTextEngine::font() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextengine.html#font

    Returns
    -------

    QFont
      A new cute QFont around the copy Qt gave back. Python owns it.
    """
    #  QFont QTextEngine::font() const
    address = self.uglySide.call('ritual_ZNK11QTextEngine4fontEv')
    from . import QFont
    return QFont._cuteOwning(address)

  @overload(QScriptItem)
  @overload(NoneType)
  def availableGlyphs(self, si: Optional[QScriptItem]) -> QGlyphLayout:
    """
    Calls Qt's 'QGlyphLayout QTextEngine::availableGlyphs(const QScriptItem
    *si) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextengine.html#availableGlyphs

    Parameters
    ----------

    si : Optional[QScriptItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QGlyphLayout
      A new cute QGlyphLayout around the copy Qt gave back. Python owns it.
    """
    #  QGlyphLayout QTextEngine::availableGlyphs(const QScriptItem *si) const
    address = self.uglySide.call(
        'ritual_ZNK11QTextEngine15availableGlyphsEPK11QScriptItem',
        self._addressOf(si),
    )
    from . import QGlyphLayout
    return QGlyphLayout._cuteOwning(address)

  @overload(QScriptItem)
  @overload(NoneType)
  def shapedGlyphs(self, si: Optional[QScriptItem]) -> QGlyphLayout:
    """
    Calls Qt's 'QGlyphLayout QTextEngine::shapedGlyphs(const QScriptItem *si)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextengine.html#shapedGlyphs

    Parameters
    ----------

    si : Optional[QScriptItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QGlyphLayout
      A new cute QGlyphLayout around the copy Qt gave back. Python owns it.
    """
    #  QGlyphLayout QTextEngine::shapedGlyphs(const QScriptItem *si) const
    address = self.uglySide.call(
        'ritual_ZNK11QTextEngine12shapedGlyphsEPK11QScriptItem',
        self._addressOf(si),
    )
    from . import QGlyphLayout
    return QGlyphLayout._cuteOwning(address)

  @overload(int)
  def ensureSpace(self, nGlyphs: int) -> bool:
    """
    Calls Qt's 'bool QTextEngine::ensureSpace(int nGlyphs) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextengine.html#ensureSpace

    Parameters
    ----------

    nGlyphs : int
      Passed on as it is.
    """
    #  bool QTextEngine::ensureSpace(int nGlyphs) const
    return self.uglySide.call(
        'ritual_ZNK11QTextEngine11ensureSpaceEi', nGlyphs,
    )

  @overload(int)
  @overload(int, int)
  def findItem(self, strPos: int, firstItem: int = 0) -> int:
    """
    Calls Qt's 'int QTextEngine::findItem(int strPos, int firstItem) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextengine.html#findItem

    Parameters
    ----------

    strPos : int
      Passed on as it is.

    firstItem : int
      Passed on as it is. May be left out, as in Qt: it is then 0.
    """
    #  int QTextEngine::findItem(int strPos, int firstItem) const
    return self.uglySide.call(
        'ritual_ZNK11QTextEngine8findItemEii', strPos, firstItem,
    )

  def formatCollection(self) -> Optional[QTextFormatCollection]:
    """
    Calls Qt's 'QTextFormatCollection *QTextEngine::formatCollection()
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextengine.html#formatCollection

    Returns
    -------

    Optional[QTextFormatCollection]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QTextFormatCollection *QTextEngine::formatCollection() const
    address = self.uglySide.call(
        'ritual_ZNK11QTextEngine16formatCollectionEv',
    )
    from . import QTextFormatCollection
    return QTextFormatCollection._cuteAt(address)

  @overload(QScriptItem)
  @overload(NoneType)
  def format(self, si: Optional[QScriptItem]) -> QTextCharFormat:
    """
    Calls Qt's 'QTextCharFormat QTextEngine::format(const QScriptItem *si)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextengine.html#format

    Parameters
    ----------

    si : Optional[QScriptItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QTextCharFormat
      A new cute QTextCharFormat around the copy Qt gave back. Python owns
      it.
    """
    #  QTextCharFormat QTextEngine::format(const QScriptItem *si) const
    address = self.uglySide.call(
        'ritual_ZNK11QTextEngine6formatEPK11QScriptItem',
        self._addressOf(si),
    )
    from . import QTextCharFormat
    return QTextCharFormat._cuteOwning(address)

  def docLayout(self) -> Optional[QAbstractTextDocumentLayout]:
    """
    Calls Qt's 'QAbstractTextDocumentLayout *QTextEngine::docLayout() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextengine.html#docLayout

    Returns
    -------

    Optional[QAbstractTextDocumentLayout]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractTextDocumentLayout *QTextEngine::docLayout() const
    address = self.uglySide.call('ritual_ZNK11QTextEngine9docLayoutEv')
    from . import QAbstractTextDocumentLayout
    return QAbstractTextDocumentLayout._cuteAt(address)

  @overload(QScriptItem)
  @overload(NoneType)
  def formatIndex(self, si: Optional[QScriptItem]) -> int:
    """
    Calls Qt's 'int QTextEngine::formatIndex(const QScriptItem *si) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextengine.html#formatIndex

    Parameters
    ----------

    si : Optional[QScriptItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  int QTextEngine::formatIndex(const QScriptItem *si) const
    return self.uglySide.call(
        'ritual_ZNK11QTextEngine11formatIndexEPK11QScriptItem',
        self._addressOf(si),
    )

  @overload(int, QFixed)
  def calculateTabWidth(self, index: int, x: QFixed) -> QFixed:
    """
    Calls Qt's 'QFixed QTextEngine::calculateTabWidth(int index, QFixed x)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextengine.html#calculateTabWidth

    Parameters
    ----------

    index : int
      Passed on as it is.

    x : QFixed
      Passed on as a value: Qt reads the C++ QFixed, which stays Python's
      own.

    Returns
    -------

    QFixed
      A new cute QFixed around the copy Qt gave back. Python owns it.
    """
    #  QFixed QTextEngine::calculateTabWidth(int index, QFixed x) const
    address = self.uglySide.call(
        'ritual_ZNK11QTextEngine17calculateTabWidthEi6QFixed',
        index, self._valueOf(x),
    )
    from . import QFixed
    return QFixed._cuteOwning(address)

  def visualCursorMovement(self) -> bool:
    """
    Calls Qt's 'bool QTextEngine::visualCursorMovement() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextengine.html#visualCursorMovement
    """
    #  bool QTextEngine::visualCursorMovement() const
    return self.uglySide.call(
        'ritual_ZNK11QTextEngine20visualCursorMovementEv',
    )

  def preeditAreaPosition(self) -> int:
    """
    Calls Qt's 'int QTextEngine::preeditAreaPosition() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextengine.html#preeditAreaPosition
    """
    #  int QTextEngine::preeditAreaPosition() const
    return self.uglySide.call(
        'ritual_ZNK11QTextEngine19preeditAreaPositionEv',
    )

  def preeditAreaText(self) -> str:
    """
    Calls Qt's 'QString QTextEngine::preeditAreaText() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextengine.html#preeditAreaText

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QTextEngine::preeditAreaText() const
    return self.uglySide.call('ritual_ZNK11QTextEngine15preeditAreaTextEv')

  def hasFormats(self) -> bool:
    """
    Calls Qt's 'bool QTextEngine::hasFormats() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextengine.html#hasFormats
    """
    #  bool QTextEngine::hasFormats() const
    return self.uglySide.call('ritual_ZNK11QTextEngine10hasFormatsEv')

  @overload(int)
  def atWordSeparator(self, position: int) -> bool:
    """
    Calls Qt's 'bool QTextEngine::atWordSeparator(int position) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextengine.html#atWordSeparator

    Parameters
    ----------

    position : int
      Passed on as it is.
    """
    #  bool QTextEngine::atWordSeparator(int position) const
    return self.uglySide.call(
        'ritual_ZNK11QTextEngine15atWordSeparatorEi', position,
    )

  @overload(Qt.TextElideMode, QFixed)
  @overload(Qt.TextElideMode, QFixed, int)
  @overload(Qt.TextElideMode, QFixed, int, int)
  @overload(Qt.TextElideMode, QFixed, int, int, int)
  def elidedText(
      self,
      mode: Qt.TextElideMode,
      width: QFixed,
      flags: int = 0,
      from_: int = 0,
      count: int = -1,
  ) -> str:
    """
    Calls Qt's 'QString QTextEngine::elidedText(Qt::TextElideMode mode,
    QFixed width, int flags, int from, int count) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextengine.html#elidedText

    Parameters
    ----------

    mode : Qt.TextElideMode
      Passed on as its number.

    width : QFixed
      Passed on as a value: Qt reads the C++ QFixed, which stays Python's
      own.

    flags : int
      Passed on as it is. May be left out, as in Qt: it is then 0.

    from_ : int
      Passed on as it is. May be left out, as in Qt: it is then 0.

    count : int
      Passed on as it is. May be left out, as in Qt: it is then -1.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QTextEngine::elidedText(Qt::TextElideMode mode, QFixed width,
    #      int flags, int from, int count) const
    return self.uglySide.call(
        'ritual_ZNK11QTextEngine10elidedTextEN2Qt13TextElideModeE6QFixediii',
        mode.value, self._valueOf(width), flags, from_, count,
    )

  @overload(int)
  def previousLogicalPosition(self, oldPos: int) -> int:
    """
    Calls Qt's 'int QTextEngine::previousLogicalPosition(int oldPos) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextengine.html#previousLogicalPosition

    Parameters
    ----------

    oldPos : int
      Passed on as it is.
    """
    #  int QTextEngine::previousLogicalPosition(int oldPos) const
    return self.uglySide.call(
        'ritual_ZNK11QTextEngine23previousLogicalPositionEi', oldPos,
    )

  @overload(int)
  def nextLogicalPosition(self, oldPos: int) -> int:
    """
    Calls Qt's 'int QTextEngine::nextLogicalPosition(int oldPos) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextengine.html#nextLogicalPosition

    Parameters
    ----------

    oldPos : int
      Passed on as it is.
    """
    #  int QTextEngine::nextLogicalPosition(int oldPos) const
    return self.uglySide.call(
        'ritual_ZNK11QTextEngine19nextLogicalPositionEi', oldPos,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int, str)
  def setPreeditArea(self, position: int, text: str) -> None:
    """
    Calls Qt's 'void QTextEngine::setPreeditArea(int position, const QString
    &text)'.

    Qt's own words: https://doc.qt.io/qt-6/qtextengine.html#setPreeditArea

    Parameters
    ----------

    position : int
      Passed on as it is.

    text : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QTextEngine::setPreeditArea(int position, const QString &text)
    self.uglySide.call(
        'ritual_ZN11QTextEngine14setPreeditAreaEiRK7QString', position, text,
    )

  @overload(int)
  def setBoundary(self, strPos: int) -> None:
    """
    Calls Qt's 'void QTextEngine::setBoundary(int strPos) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextengine.html#setBoundary

    Parameters
    ----------

    strPos : int
      Passed on as it is.
    """
    #  void QTextEngine::setBoundary(int strPos) const
    self.uglySide.call('ritual_ZNK11QTextEngine11setBoundaryEi', strPos)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'QTextEngine::QTextEngine()', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qtextengine.html#QTextEngine
    """
    #  QTextEngine::QTextEngine()
    self._noteCreation(QTextEngine, lambda: Rituals.call(
        'ritual_ZN11QTextEngineC1Ev',
    ))

  @overload(str, QFont)
  def __init__(self, str: str, f: QFont) -> None:
    """
    Notes what was given, for Qt's 'QTextEngine::QTextEngine(const QString
    &str, const QFont &f)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qtextengine.html#QTextEngine

    Parameters
    ----------

    str : str
      Passed on as it is: a QString is made of it for the call.

    f : QFont
      Passed on as a value: Qt reads the C++ QFont, which stays Python's own.
    """
    #  QTextEngine::QTextEngine(const QString &str, const QFont &f)
    self._noteCreation(QTextEngine, lambda: Rituals.call(
        'ritual_ZN11QTextEngineC1ERK7QStringRK5QFont', str, self._valueOf(f),
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

  def invalidate(self) -> None:
    """
    Calls Qt's 'void QTextEngine::invalidate()'.

    Qt's own words: https://doc.qt.io/qt-6/qtextengine.html#invalidate
    """
    #  void QTextEngine::invalidate()
    self.uglySide.call('ritual_ZN11QTextEngine10invalidateEv')

  def clearLineData(self) -> None:
    """
    Calls Qt's 'void QTextEngine::clearLineData()'.

    Qt's own words: https://doc.qt.io/qt-6/qtextengine.html#clearLineData
    """
    #  void QTextEngine::clearLineData()
    self.uglySide.call('ritual_ZN11QTextEngine13clearLineDataEv')

  def validate(self) -> None:
    """
    Calls Qt's 'void QTextEngine::validate() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextengine.html#validate
    """
    #  void QTextEngine::validate() const
    self.uglySide.call('ritual_ZNK11QTextEngine8validateEv')

  def itemize(self) -> None:
    """
    Calls Qt's 'void QTextEngine::itemize() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextengine.html#itemize
    """
    #  void QTextEngine::itemize() const
    self.uglySide.call('ritual_ZNK11QTextEngine7itemizeEv')

  @overload(int)
  def shape(self, item: int) -> None:
    """
    Calls Qt's 'void QTextEngine::shape(int item) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextengine.html#shape

    Parameters
    ----------

    item : int
      Passed on as it is.
    """
    #  void QTextEngine::shape(int item) const
    self.uglySide.call('ritual_ZNK11QTextEngine5shapeEi', item)

  @overload(QScriptLine)
  def justify(self, si: QScriptLine) -> None:
    """
    Calls Qt's 'void QTextEngine::justify(const QScriptLine &si)'.

    Qt's own words: https://doc.qt.io/qt-6/qtextengine.html#justify

    Parameters
    ----------

    si : QScriptLine
      Passed on as a value: Qt reads the C++ QScriptLine, which stays
      Python's own.
    """
    #  void QTextEngine::justify(const QScriptLine &si)
    self.uglySide.call(
        'ritual_ZN11QTextEngine7justifyERK11QScriptLine', self._valueOf(si),
    )

  @overload(QScriptLine)
  def alignLine(self, line: QScriptLine) -> QFixed:
    """
    Calls Qt's 'QFixed QTextEngine::alignLine(const QScriptLine &line)'.

    Qt's own words: https://doc.qt.io/qt-6/qtextengine.html#alignLine

    Parameters
    ----------

    line : QScriptLine
      Passed on as a value: Qt reads the C++ QScriptLine, which stays
      Python's own.

    Returns
    -------

    QFixed
      A new cute QFixed around the copy Qt gave back. Python owns it.
    """
    #  QFixed QTextEngine::alignLine(const QScriptLine &line)
    address = self.uglySide.call(
        'ritual_ZN11QTextEngine9alignLineERK11QScriptLine',
        self._valueOf(line),
    )
    from . import QFixed
    return QFixed._cuteOwning(address)

  def freeMemory(self) -> None:
    """
    Calls Qt's 'void QTextEngine::freeMemory()'.

    Qt's own words: https://doc.qt.io/qt-6/qtextengine.html#freeMemory
    """
    #  void QTextEngine::freeMemory()
    self.uglySide.call('ritual_ZN11QTextEngine10freeMemoryEv')

  def indexFormats(self) -> None:
    """
    Calls Qt's 'void QTextEngine::indexFormats()'.

    Qt's own words: https://doc.qt.io/qt-6/qtextengine.html#indexFormats
    """
    #  void QTextEngine::indexFormats()
    self.uglySide.call('ritual_ZN11QTextEngine12indexFormatsEv')

  def resolveFormats(self) -> None:
    """
    Calls Qt's 'void QTextEngine::resolveFormats() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextengine.html#resolveFormats
    """
    #  void QTextEngine::resolveFormats() const
    self.uglySide.call('ritual_ZNK11QTextEngine14resolveFormatsEv')

  @overload(QScriptLine)
  def shapeLine(self, line: QScriptLine) -> None:
    """
    Calls Qt's 'void QTextEngine::shapeLine(const QScriptLine &line)'.

    Qt's own words: https://doc.qt.io/qt-6/qtextengine.html#shapeLine

    Parameters
    ----------

    line : QScriptLine
      Passed on as a value: Qt reads the C++ QScriptLine, which stays
      Python's own.
    """
    #  void QTextEngine::shapeLine(const QScriptLine &line)
    self.uglySide.call(
        'ritual_ZN11QTextEngine9shapeLineERK11QScriptLine',
        self._valueOf(line),
    )

  @overload(QScriptLine)
  def leadingSpaceWidth(self, line: QScriptLine) -> QFixed:
    """
    Calls Qt's 'QFixed QTextEngine::leadingSpaceWidth(const QScriptLine
    &line)'.

    Qt's own words: https://doc.qt.io/qt-6/qtextengine.html#leadingSpaceWidth

    Parameters
    ----------

    line : QScriptLine
      Passed on as a value: Qt reads the C++ QScriptLine, which stays
      Python's own.

    Returns
    -------

    QFixed
      A new cute QFixed around the copy Qt gave back. Python owns it.
    """
    #  QFixed QTextEngine::leadingSpaceWidth(const QScriptLine &line)
    address = self.uglySide.call(
        'ritual_ZN11QTextEngine17leadingSpaceWidthERK11QScriptLine',
        self._valueOf(line),
    )
    from . import QFixed
    return QFixed._cuteOwning(address)

  @overload(QScriptItem, int, int, int)
  @overload(NoneType, int, int, int)
  def offsetInLigature(
      self,
      si: Optional[QScriptItem],
      pos: int,
      max: int,
      glyph_pos: int,
  ) -> QFixed:
    """
    Calls Qt's 'QFixed QTextEngine::offsetInLigature(const QScriptItem *si,
    int pos, int max, int glyph_pos)'.

    Qt's own words: https://doc.qt.io/qt-6/qtextengine.html#offsetInLigature

    Parameters
    ----------

    si : Optional[QScriptItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    pos : int
      Passed on as it is.

    max : int
      Passed on as it is.

    glyph_pos : int
      Passed on as it is.

    Returns
    -------

    QFixed
      A new cute QFixed around the copy Qt gave back. Python owns it.
    """
    #  QFixed QTextEngine::offsetInLigature(const QScriptItem *si, int pos,
    #      int max, int glyph_pos)
    address = self.uglySide.call(
        'ritual_ZN11QTextEngine16offsetInLigatureEPK11QScriptItemiii',
        self._addressOf(si), pos, max, glyph_pos,
    )
    from . import QFixed
    return QFixed._cuteOwning(address)

  @overload(QScriptItem, int, QFixed, QFixed, int, bool)
  @overload(NoneType, int, QFixed, QFixed, int, bool)
  def positionInLigature(
      self,
      si: Optional[QScriptItem],
      end: int,
      x: QFixed,
      edge: QFixed,
      glyph_pos: int,
      cursorOnCharacter: bool,
  ) -> int:
    """
    Calls Qt's 'int QTextEngine::positionInLigature(const QScriptItem *si,
    int end, QFixed x, QFixed edge, int glyph_pos, bool cursorOnCharacter)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextengine.html#positionInLigature

    Parameters
    ----------

    si : Optional[QScriptItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    end : int
      Passed on as it is.

    x : QFixed
      Passed on as a value: Qt reads the C++ QFixed, which stays Python's
      own.

    edge : QFixed
      Passed on as a value: Qt reads the C++ QFixed, which stays Python's
      own.

    glyph_pos : int
      Passed on as it is.

    cursorOnCharacter : bool
      Passed on as it is.
    """
    #  int QTextEngine::positionInLigature(const QScriptItem *si, int end,
    #      QFixed x, QFixed edge, int glyph_pos, bool cursorOnCharacter)
    return self.uglySide.call(
        'ritual_ZN11QTextEngine18positionInLigatureEPK11QScriptItemi6QFixed'
        'S3_ib',
        self._addressOf(si), end, self._valueOf(x), self._valueOf(edge),
        glyph_pos, cursorOnCharacter,
    )

  @overload(int)
  def lineNumberForTextPosition(self, pos: int) -> int:
    """
    Calls Qt's 'int QTextEngine::lineNumberForTextPosition(int pos)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextengine.html#lineNumberForTextPosition

    Parameters
    ----------

    pos : int
      Passed on as it is.
    """
    #  int QTextEngine::lineNumberForTextPosition(int pos)
    return self.uglySide.call(
        'ritual_ZN11QTextEngine25lineNumberForTextPositionEi', pos,
    )

  @overload(int, QTextCursor.MoveOperation)
  def positionAfterVisualMovement(
      self,
      oldPos: int,
      op: QTextCursor.MoveOperation,
  ) -> int:
    """
    Calls Qt's 'int QTextEngine::positionAfterVisualMovement(int oldPos,
    QTextCursor::MoveOperation op)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextengine.html#positionAfterVisualMovement

    Parameters
    ----------

    oldPos : int
      Passed on as it is.

    op : QTextCursor.MoveOperation
      Passed on as its number.
    """
    #  int QTextEngine::positionAfterVisualMovement(int oldPos,
    #      QTextCursor::MoveOperation op)
    return self.uglySide.call(
        'ritual_ZN11QTextEngine27positionAfterVisualMovementEiN11QTextCurso'
        'r13MoveOperationE',
        oldPos, op.value,
    )

  def resetFontEngineCache(self) -> None:
    """
    Calls Qt's 'void QTextEngine::resetFontEngineCache()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextengine.html#resetFontEngineCache
    """
    #  void QTextEngine::resetFontEngineCache()
    self.uglySide.call('ritual_ZN11QTextEngine20resetFontEngineCacheEv')

  @overload()
  @overload(bool)
  def enableDelayDecorations(self, enable: bool = True) -> None:
    """
    Calls Qt's 'void QTextEngine::enableDelayDecorations(bool enable)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextengine.html#enableDelayDecorations

    Parameters
    ----------

    enable : bool
      Passed on as it is. May be left out, as in Qt: it is then True.
    """
    #  void QTextEngine::enableDelayDecorations(bool enable)
    self.uglySide.call(
        'ritual_ZN11QTextEngine22enableDelayDecorationsEb', enable,
    )

  @overload(QPainter, QLineF)
  @overload(NoneType, QLineF)
  def addUnderline(self, painter: Optional[QPainter], line: QLineF) -> None:
    """
    Calls Qt's 'void QTextEngine::addUnderline(QPainter *painter, const
    QLineF &line)'.

    Qt's own words: https://doc.qt.io/qt-6/qtextengine.html#addUnderline

    Parameters
    ----------

    painter : Optional[QPainter]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    line : QLineF
      Passed on as a value: Qt reads the C++ QLineF, which stays Python's
      own.
    """
    #  void QTextEngine::addUnderline(QPainter *painter, const QLineF &line)
    self.uglySide.call(
        'ritual_ZN11QTextEngine12addUnderlineEP8QPainterRK6QLineF',
        self._addressOf(painter), self._valueOf(line),
    )

  @overload(QPainter, QLineF)
  @overload(NoneType, QLineF)
  def addStrikeOut(self, painter: Optional[QPainter], line: QLineF) -> None:
    """
    Calls Qt's 'void QTextEngine::addStrikeOut(QPainter *painter, const
    QLineF &line)'.

    Qt's own words: https://doc.qt.io/qt-6/qtextengine.html#addStrikeOut

    Parameters
    ----------

    painter : Optional[QPainter]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    line : QLineF
      Passed on as a value: Qt reads the C++ QLineF, which stays Python's
      own.
    """
    #  void QTextEngine::addStrikeOut(QPainter *painter, const QLineF &line)
    self.uglySide.call(
        'ritual_ZN11QTextEngine12addStrikeOutEP8QPainterRK6QLineF',
        self._addressOf(painter), self._valueOf(line),
    )

  @overload(QPainter, QLineF)
  @overload(NoneType, QLineF)
  def addOverline(self, painter: Optional[QPainter], line: QLineF) -> None:
    """
    Calls Qt's 'void QTextEngine::addOverline(QPainter *painter, const QLineF
    &line)'.

    Qt's own words: https://doc.qt.io/qt-6/qtextengine.html#addOverline

    Parameters
    ----------

    painter : Optional[QPainter]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    line : QLineF
      Passed on as a value: Qt reads the C++ QLineF, which stays Python's
      own.
    """
    #  void QTextEngine::addOverline(QPainter *painter, const QLineF &line)
    self.uglySide.call(
        'ritual_ZN11QTextEngine11addOverlineEP8QPainterRK6QLineF',
        self._addressOf(painter), self._valueOf(line),
    )

  @overload(QPainter)
  @overload(NoneType)
  def drawDecorations(self, painter: Optional[QPainter]) -> None:
    """
    Calls Qt's 'void QTextEngine::drawDecorations(QPainter *painter)'.

    Qt's own words: https://doc.qt.io/qt-6/qtextengine.html#drawDecorations

    Parameters
    ----------

    painter : Optional[QPainter]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QTextEngine::drawDecorations(QPainter *painter)
    self.uglySide.call(
        'ritual_ZN11QTextEngine15drawDecorationsEP8QPainter',
        self._addressOf(painter),
    )

  def clearDecorations(self) -> None:
    """
    Calls Qt's 'void QTextEngine::clearDecorations()'.

    Qt's own words: https://doc.qt.io/qt-6/qtextengine.html#clearDecorations
    """
    #  void QTextEngine::clearDecorations()
    self.uglySide.call('ritual_ZN11QTextEngine16clearDecorationsEv')

  def adjustUnderlines(self) -> None:
    """
    Calls Qt's 'void QTextEngine::adjustUnderlines()'.

    Qt's own words: https://doc.qt.io/qt-6/qtextengine.html#adjustUnderlines
    """
    #  void QTextEngine::adjustUnderlines()
    self.uglySide.call('ritual_ZN11QTextEngine16adjustUnderlinesEv')

  def addRequiredBoundaries(self) -> None:
    """
    Calls Qt's 'void QTextEngine::addRequiredBoundaries() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextengine.html#addRequiredBoundaries
    """
    #  void QTextEngine::addRequiredBoundaries() const
    self.uglySide.call('ritual_ZNK11QTextEngine21addRequiredBoundariesEv')

  @overload(int)
  def shapeText(self, item: int) -> None:
    """
    Calls Qt's 'void QTextEngine::shapeText(int item) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextengine.html#shapeText

    Parameters
    ----------

    item : int
      Passed on as it is.
    """
    #  void QTextEngine::shapeText(int item) const
    self.uglySide.call('ritual_ZNK11QTextEngine9shapeTextEi', item)

  @overload(int)
  def endOfLine(self, lineNum: int) -> int:
    """
    Calls Qt's 'int QTextEngine::endOfLine(int lineNum)'.

    Qt's own words: https://doc.qt.io/qt-6/qtextengine.html#endOfLine

    Parameters
    ----------

    lineNum : int
      Passed on as it is.
    """
    #  int QTextEngine::endOfLine(int lineNum)
    return self.uglySide.call('ritual_ZN11QTextEngine9endOfLineEi', lineNum)

  @overload(int)
  def beginningOfLine(self, lineNum: int) -> int:
    """
    Calls Qt's 'int QTextEngine::beginningOfLine(int lineNum)'.

    Qt's own words: https://doc.qt.io/qt-6/qtextengine.html#beginningOfLine

    Parameters
    ----------

    lineNum : int
      Passed on as it is.
    """
    #  int QTextEngine::beginningOfLine(int lineNum)
    return self.uglySide.call(
        'ritual_ZN11QTextEngine15beginningOfLineEi', lineNum,
    )

  @staticmethod
  def addItemDecoration(*__, **_) -> Never:
    """
    Qt's 'void QTextEngine::addItemDecoration(QPainter *painter, const QLineF
    &line, ItemDecorationList *decorationList)': names
    'QTextEngine::ItemDecorationList', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QTextEngine.addItemDecoration' has no cute function yet. Qt's "
        "'void QTextEngine::addItemDecoration(QPainter *painter, const "
        "QLineF &line, ItemDecorationList *decorationList)': names "
        "'QTextEngine::ItemDecorationList', which has no cute class yet.")

  @staticmethod
  def bidiReorder(*__, **_) -> Never:
    """
    Qt's 'void QTextEngine::bidiReorder(int numRuns, const quint8 *levels,
    int *visualOrder)': names 'quint8', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QTextEngine.bidiReorder' has no cute function yet. Qt's 'void "
        "QTextEngine::bidiReorder(int numRuns, const quint8 *levels, int "
        "*visualOrder)': names 'quint8', which has no cute class yet.")

  @staticmethod
  def drawItemDecorationList(*__, **_) -> Never:
    """
    Qt's 'void QTextEngine::drawItemDecorationList(QPainter *painter, const
    ItemDecorationList &decorationList)': takes a type Python has no way to
    hand over yet.
    """
    raise NotImplementedError(
        "'QTextEngine.drawItemDecorationList' has no cute function yet. "
        "Qt's 'void QTextEngine::drawItemDecorationList(QPainter *painter, "
        "const ItemDecorationList &decorationList)': takes a type Python "
        "has no way to hand over yet.")

  @staticmethod
  def formats(*__, **_) -> Never:
    """
    Qt's 'QList<QTextLayout::FormatRange> QTextEngine::formats() const':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QTextEngine.formats' has no cute function yet. Qt's "
        "'QList<QTextLayout::FormatRange> QTextEngine::formats() const': "
        "gives a type Python has no way to take yet.")

  @staticmethod
  def getClusterLength(*__, **_) -> Never:
    """
    Qt's 'int QTextEngine::getClusterLength(unsigned short *logClusters,
    const QCharAttributes *attributes, int from, int to, int glyph_pos, int
    *start)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QTextEngine.getClusterLength' has no cute function yet. Qt's 'int "
        "QTextEngine::getClusterLength(unsigned short *logClusters, const "
        "QCharAttributes *attributes, int from, int to, int glyph_pos, int "
        "*start)': takes a number to change where it is.")

  @staticmethod
  def insertionPointsForLine(*__, **_) -> Never:
    """
    Qt's 'std::vector<int> QTextEngine::insertionPointsForLine(int lineNum)':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QTextEngine.insertionPointsForLine' has no cute function yet. "
        "Qt's 'std::vector<int> QTextEngine::insertionPointsForLine(int "
        "lineNum)': gives a type Python has no way to take yet.")

  @staticmethod
  def logClusters(*__, **_) -> Never:
    """
    Qt's 'unsigned short *QTextEngine::logClusters(const QScriptItem *si)
    const': takes or gives a type that cannot be passed yet: unsigned short
    *.
    """
    raise NotImplementedError(
        "'QTextEngine.logClusters' has no cute function yet. Qt's 'unsigned "
        "short *QTextEngine::logClusters(const QScriptItem *si) const': "
        "takes or gives a type that cannot be passed yet: unsigned short *.")

  @staticmethod
  def setFormats(*__, **_) -> Never:
    """
    Qt's 'void QTextEngine::setFormats(const QList<QTextLayout::FormatRange>
    &formats)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QTextEngine.setFormats' has no cute function yet. Qt's 'void "
        "QTextEngine::setFormats(const QList<QTextLayout::FormatRange> "
        "&formats)': takes a type Python has no way to hand over yet.")

  @staticmethod
  def shapeTextWithHarfbuzzNG(*__, **_) -> Never:
    """
    Qt's 'int QTextEngine::shapeTextWithHarfbuzzNG(const QScriptItem &si,
    const ushort *string, int stringBaseIndex, int stringLength, int
    itemLength, QFontEngine *fontEngine, QSpan<uint> itemBoundaries, bool
    kerningEnabled, bool hasLetterSpacing, const QMap<QFont::Tag, quint32>
    &features) const': names 'ushort', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QTextEngine.shapeTextWithHarfbuzzNG' has no cute function yet. "
        "Qt's 'int QTextEngine::shapeTextWithHarfbuzzNG(const QScriptItem "
        "&si, const ushort *string, int stringBaseIndex, int stringLength, "
        "int itemLength, QFontEngine *fontEngine, QSpan<uint> "
        "itemBoundaries, bool kerningEnabled, bool hasLetterSpacing, const "
        "QMap<QFont::Tag, quint32> &features) const': names 'ushort', which "
        "has no cute class yet.")
