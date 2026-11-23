"""
QTextFrame binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/qtextobject.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QList
from . import QTextObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from . import QTextBlock, QTextCursor, QTextDocument, QTextFrameFormat
  from . import QTextFrameLayoutData
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QTextDocument = WAIT['QTextDocument']
  QTextFrameFormat = WAIT['QTextFrameFormat']
  QTextFrameLayoutData = WAIT['QTextFrameLayoutData']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QTextFrame(QTextObject):
  """
  The cute side of Qt's QTextFrame: a plain Python object standing in front
  of one C++ QTextFrame.

  It is built on the cute 'QTextObject', as Qt's QTextFrame is built on Qt's
  QTextObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QTextFrame that has a ritual and that Python can
  call so far, 14 names in all: 'metaObject', 'tr', 'setFrameFormat',
  'frameFormat', 'firstCursorPosition', 'lastCursorPosition',
  'firstPosition', 'lastPosition', 'layoutData', 'setLayoutData',
  'childFrames', 'parentFrame', 'begin', 'end'. It can be made from Python,
  in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QTextFrame::~QTextFrame()': the destructor: Python never removes a
    C++ QTextFrame.

  What has no ritual
  ------------------

  9 of the 25 functions Qt declares: 5 takes or gives a type that cannot be
  passed yet; 2 forbidden; 1 a template; 1 declared and nowhere to be found.

  What to expect
  --------------

  - The C++ QTextFrame is created at the first use, not by 'QTextFrame(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QTextFrame.
  - Qt tells when it has removed the C++ QTextFrame. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
  """

  #  The classes Qt writes inside QTextFrame, each a class in here as in C++.

  class iterator(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QTextFrame::iterator: a plain Python object
    standing in front of one C++ QTextFrame::iterator.

    C++ hands a QTextFrame::iterator around as a copy, so every C++
    QTextFrame::iterator behind a cute one is Python's own: it is removed, by
    the ritual named in '__delete_ritual__', when the cute object goes.

    What exists
    -----------

    Every function of Qt's QTextFrame::iterator that has a ritual and that
    Python can call so far, 6 names in all: 'parentFrame', 'currentFrame',
    'currentBlock', 'atEnd', '__eq__', '__ne__'. It can be made from Python,
    in 2 ways; see '__init__'.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'iterator QTextFrame::iterator::operator++(int a0)': an operator
      Python has no name for.
    - Qt's 'iterator QTextFrame::iterator::operator--(int a0)': an operator
      Python has no name for.
    - Qt's 'QTextFrame::iterator::~iterator()': the destructor: Python
      removes its C++ QTextFrame::iterator by it, and has no other use for
      it.

    What has no ritual
    ------------------

    2 of the 13 functions Qt declares: 2 takes or gives a type that cannot be
    passed yet.

    What to expect
    --------------

    - The C++ QTextFrame::iterator is created at the first use, not by
      'QTextFrame::iterator(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QTextFrame::iterator back gives a copy the ritual
      made for Python, in a new cute QTextFrame::iterator.
    """

    #  The cute classes this class names and is not built on. Each waits
    #  until it is made; see 'WAIT'. A type checker reads the imports at the
    #  top of the file instead.
    if not TYPE_CHECKING:
      QTextFrame = WAIT['QTextFrame']

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QTextFrame::iterator'

    #  Qt's '~QTextFrame::iterator()'. Naming it makes this a value class:
    #  Python owns every C++ QTextFrame::iterator behind a cute one, and
    #  removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN10QTextFrame8iteratorD1Ev'

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    def parentFrame(self) -> Optional[QTextFrame]:
      """
      Calls Qt's 'QTextFrame *QTextFrame::iterator::parentFrame() const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qtextframe-iterator.html#parentFrame

      Returns
      -------

      Optional[QTextFrame]
        The cute object standing for what Qt gave back. None when Qt gave
        back no object.
      """
      #  QTextFrame *QTextFrame::iterator::parentFrame() const
      address = self.uglySide.call(
          'ritual_ZNK10QTextFrame8iterator11parentFrameEv',
      )
      return QTextFrame._cuteAt(address)

    def currentFrame(self) -> Optional[QTextFrame]:
      """
      Calls Qt's 'QTextFrame *QTextFrame::iterator::currentFrame() const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qtextframe-iterator.html#currentFrame

      Returns
      -------

      Optional[QTextFrame]
        The cute object standing for what Qt gave back. None when Qt gave
        back no object.
      """
      #  QTextFrame *QTextFrame::iterator::currentFrame() const
      address = self.uglySide.call(
          'ritual_ZNK10QTextFrame8iterator12currentFrameEv',
      )
      return QTextFrame._cuteAt(address)

    def currentBlock(self) -> QTextBlock:
      """
      Calls Qt's 'QTextBlock QTextFrame::iterator::currentBlock() const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qtextframe-iterator.html#currentBlock

      Returns
      -------

      QTextBlock
        A new cute QTextBlock around the copy Qt gave back. Python owns it.
      """
      #  QTextBlock QTextFrame::iterator::currentBlock() const
      address = self.uglySide.call(
          'ritual_ZNK10QTextFrame8iterator12currentBlockEv',
      )
      from . import QTextBlock
      return QTextBlock._cuteOwning(address)

    def atEnd(self) -> bool:
      """
      Calls Qt's 'bool QTextFrame::iterator::atEnd() const'.

      Qt's own words: https://doc.qt.io/qt-6/qtextframe-iterator.html#atEnd
      """
      #  bool QTextFrame::iterator::atEnd() const
      return self.uglySide.call('ritual_ZNK10QTextFrame8iterator5atEndEv')

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @overload(THIS)
    def __eq__(self, o: QTextFrame.iterator) -> bool:
      """
      Calls Qt's 'bool QTextFrame::iterator::operator==(const iterator &o)
      const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qtextframe-iterator.html#operator==

      Parameters
      ----------

      o : QTextFrame.iterator
        Passed on as a value: Qt reads the C++ QTextFrame::iterator, which
        stays Python's own.
      """
      #  bool QTextFrame::iterator::operator==(const iterator &o) const
      return self.uglySide.call(
          'ritual_ZNK10QTextFrame8iteratoreqERKS0_', self._valueOf(o),
      )

    @overload.fallback
    def __eq__(self, *args: object) -> object:
      """
      Tells Python that no function of this name takes what it was
      handed, with Python's own word for it. Python then asks the
      other side of the operator.
      """
      return NotImplemented

    @overload(THIS)
    def __ne__(self, o: QTextFrame.iterator) -> bool:
      """
      Calls Qt's 'bool QTextFrame::iterator::operator!=(const iterator &o)
      const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qtextframe-iterator.html#operator!=

      Parameters
      ----------

      o : QTextFrame.iterator
        Passed on as a value: Qt reads the C++ QTextFrame::iterator, which
        stays Python's own.
      """
      #  bool QTextFrame::iterator::operator!=(const iterator &o) const
      return self.uglySide.call(
          'ritual_ZNK10QTextFrame8iteratorneERKS0_', self._valueOf(o),
      )

    @overload.fallback
    def __ne__(self, *args: object) -> object:
      """
      Tells Python that no function of this name takes what it was
      handed, with Python's own word for it. Python then asks the
      other side of the operator.
      """
      return NotImplemented

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @overload(QTextFrame, int, int, int)
    @overload(NoneType, int, int, int)
    def __init__(
        self,
        frame: Optional[QTextFrame],
        block: int,
        begin: int,
        end: int,
    ) -> None:
      """
      Notes what was given, for Qt's
      'QTextFrame::iterator::iterator(QTextFrame *frame, int block, int
      begin, int end)', which is called at the first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qtextframe-iterator.html#iterator

      Parameters
      ----------

      frame : Optional[QTextFrame]
        Passed on as the address of its C++ object. None is passed on as no
        object.

      block : int
        Passed on as it is.

      begin : int
        Passed on as it is.

      end : int
        Passed on as it is.
      """
      #  QTextFrame::iterator::iterator(QTextFrame *frame, int block, int
      #      begin, int end)
      self._noteCreation(QTextFrame.iterator, lambda: Rituals.call(
          'ritual_ZN10QTextFrame8iteratorC1EPS_iii',
          self._addressOf(frame), block, begin, end,
      ))

    @overload()
    def __init__(self) -> None:
      """
      Notes what was given, for Qt's 'QTextFrame::iterator::iterator()',
      which is called at the first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qtextframe-iterator.html#iterator
      """
      #  QTextFrame::iterator::iterator()
      self._noteCreation(QTextFrame.iterator, lambda: Rituals.call(
          'ritual_ZN10QTextFrame8iteratorC1Ev',
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

  @staticmethod
  @overload(str)
  @overload(NoneType)
  @overload(str, str)
  @overload(str, NoneType)
  @overload(NoneType, str)
  @overload(NoneType, NoneType)
  @overload(str, str, int)
  @overload(str, NoneType, int)
  @overload(NoneType, str, int)
  @overload(NoneType, NoneType, int)
  def tr(s: Optional[str], c: Optional[str] = None, n: int = -1) -> str:
    """
    Calls Qt's 'QString QTextFrame::tr(const char *s, const char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qtextframe.html#tr

    Parameters
    ----------

    s : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    c : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text. May
      be left out, as in Qt: it is then None.

    n : int
      Passed on as it is. May be left out, as in Qt: it is then -1.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QTextFrame::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN10QTextFrame2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QTextFrame'

  #  A C++ QTextFrame Python makes is of a C++ class of ours, in which Python
  #  can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QTextFrame'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QTextFrame::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextframe.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QTextFrame::metaObject() const
    address = self.uglySide.call('ritual_ZNK10QTextFrame10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def frameFormat(self) -> QTextFrameFormat:
    """
    Calls Qt's 'QTextFrameFormat QTextFrame::frameFormat() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextframe.html#frameFormat

    Returns
    -------

    QTextFrameFormat
      A new cute QTextFrameFormat around the copy Qt gave back. Python owns
      it.
    """
    #  QTextFrameFormat QTextFrame::frameFormat() const
    address = self.uglySide.call('ritual_ZNK10QTextFrame11frameFormatEv')
    from . import QTextFrameFormat
    return QTextFrameFormat._cuteOwning(address)

  def firstCursorPosition(self) -> QTextCursor:
    """
    Calls Qt's 'QTextCursor QTextFrame::firstCursorPosition() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextframe.html#firstCursorPosition

    Returns
    -------

    QTextCursor
      A new cute QTextCursor around the copy Qt gave back. Python owns it.
    """
    #  QTextCursor QTextFrame::firstCursorPosition() const
    address = self.uglySide.call(
        'ritual_ZNK10QTextFrame19firstCursorPositionEv',
    )
    from . import QTextCursor
    return QTextCursor._cuteOwning(address)

  def lastCursorPosition(self) -> QTextCursor:
    """
    Calls Qt's 'QTextCursor QTextFrame::lastCursorPosition() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextframe.html#lastCursorPosition

    Returns
    -------

    QTextCursor
      A new cute QTextCursor around the copy Qt gave back. Python owns it.
    """
    #  QTextCursor QTextFrame::lastCursorPosition() const
    address = self.uglySide.call(
        'ritual_ZNK10QTextFrame18lastCursorPositionEv',
    )
    from . import QTextCursor
    return QTextCursor._cuteOwning(address)

  def firstPosition(self) -> int:
    """
    Calls Qt's 'int QTextFrame::firstPosition() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextframe.html#firstPosition
    """
    #  int QTextFrame::firstPosition() const
    return self.uglySide.call('ritual_ZNK10QTextFrame13firstPositionEv')

  def lastPosition(self) -> int:
    """
    Calls Qt's 'int QTextFrame::lastPosition() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextframe.html#lastPosition
    """
    #  int QTextFrame::lastPosition() const
    return self.uglySide.call('ritual_ZNK10QTextFrame12lastPositionEv')

  def layoutData(self) -> Optional[QTextFrameLayoutData]:
    """
    Calls Qt's 'QTextFrameLayoutData *QTextFrame::layoutData() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextframe.html#layoutData

    Returns
    -------

    Optional[QTextFrameLayoutData]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QTextFrameLayoutData *QTextFrame::layoutData() const
    address = self.uglySide.call('ritual_ZNK10QTextFrame10layoutDataEv')
    from . import QTextFrameLayoutData
    return QTextFrameLayoutData._cuteAt(address)

  def childFrames(self) -> QList[QTextFrame]:
    """
    Calls Qt's 'QList<QTextFrame *> QTextFrame::childFrames() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextframe.html#childFrames

    Returns
    -------

    QList[QTextFrame]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QTextFrame *> QTextFrame::childFrames() const
    address = self.uglySide.call('ritual_ZNK10QTextFrame11childFramesEv')
    return QList[QTextFrame]._cuteOwning(address)

  def parentFrame(self) -> Optional[QTextFrame]:
    """
    Calls Qt's 'QTextFrame *QTextFrame::parentFrame() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextframe.html#parentFrame

    Returns
    -------

    Optional[QTextFrame]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QTextFrame *QTextFrame::parentFrame() const
    address = self.uglySide.call('ritual_ZNK10QTextFrame11parentFrameEv')
    return QTextFrame._cuteAt(address)

  def begin(self) -> iterator:
    """
    Calls Qt's 'iterator QTextFrame::begin() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextframe.html#begin

    Returns
    -------

    iterator
      A new cute QTextFrame::iterator around the copy Qt gave back. Python
      owns it.
    """
    #  iterator QTextFrame::begin() const
    address = self.uglySide.call('ritual_ZNK10QTextFrame5beginEv')
    return QTextFrame.iterator._cuteOwning(address)

  def end(self) -> iterator:
    """
    Calls Qt's 'iterator QTextFrame::end() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextframe.html#end

    Returns
    -------

    iterator
      A new cute QTextFrame::iterator around the copy Qt gave back. Python
      owns it.
    """
    #  iterator QTextFrame::end() const
    address = self.uglySide.call('ritual_ZNK10QTextFrame3endEv')
    return QTextFrame.iterator._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QTextFrameFormat)
  def setFrameFormat(self, format: QTextFrameFormat) -> None:
    """
    Calls Qt's 'void QTextFrame::setFrameFormat(const QTextFrameFormat
    &format)'.

    Qt's own words: https://doc.qt.io/qt-6/qtextframe.html#setFrameFormat

    Parameters
    ----------

    format : QTextFrameFormat
      Passed on as a value: Qt reads the C++ QTextFrameFormat, which stays
      Python's own.
    """
    #  void QTextFrame::setFrameFormat(const QTextFrameFormat &format)
    self.uglySide.call(
        'ritual_ZN10QTextFrame14setFrameFormatERK16QTextFrameFormat',
        self._valueOf(format),
    )

  @overload(QTextFrameLayoutData)
  @overload(NoneType)
  def setLayoutData(self, data: Optional[QTextFrameLayoutData]) -> None:
    """
    Calls Qt's 'void QTextFrame::setLayoutData(QTextFrameLayoutData *data)'.

    Qt's own words: https://doc.qt.io/qt-6/qtextframe.html#setLayoutData

    Parameters
    ----------

    data : Optional[QTextFrameLayoutData]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QTextFrame::setLayoutData(QTextFrameLayoutData *data)
    self.uglySide.call(
        'ritual_ZN10QTextFrame13setLayoutDataEP20QTextFrameLayoutData',
        self._addressOf(data),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QTextDocument)
  @overload(NoneType)
  def __init__(self, doc: Optional[QTextDocument]) -> None:
    """
    Notes what was given, for Qt's 'QTextFrame::QTextFrame(QTextDocument
    *doc)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qtextframe.html#QTextFrame

    Parameters
    ----------

    doc : Optional[QTextDocument]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QTextFrame::QTextFrame(QTextDocument *doc)
    self._noteCreation(QTextFrame, lambda: Rituals.call(
        'ritual_ZN10QTextFrameC1EP13QTextDocument', self._addressOf(doc),
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


#  Qt's 'QList<QTextFrame *>': the list of QTextFrame, which
#  'QList[QTextFrame]' gives. It is made here, so that there is one as soon
#  as there can be a QTextFrame.
QList.createKind(
    QTextFrame, 'address',
    make='ritual_list_make_QTextFrame_ptr',
    add='ritual_list_add_QTextFrame_ptr',
    size='ritual_list_size_QTextFrame_ptr',
    at='ritual_list_at_QTextFrame_ptr',
    drop='ritual_list_drop_QTextFrame_ptr',
)
