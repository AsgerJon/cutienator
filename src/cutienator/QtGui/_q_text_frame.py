"""
QTextFrame binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/qtextobject.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from . import QTextObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from . import QTextCursor, QTextDocument, QTextFrameFormat
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QTextDocument = WAIT['QTextDocument']
  QTextFrameFormat = WAIT['QTextFrameFormat']

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
  call so far, 9 names in all: 'metaObject', 'tr', 'setFrameFormat',
  'frameFormat', 'firstCursorPosition', 'lastCursorPosition',
  'firstPosition', 'lastPosition', 'parentFrame'. It can be made from Python,
  in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QTextFrame::~QTextFrame()': the destructor: Python never removes a
    C++ QTextFrame.
  - Qt's 'QTextFrameLayoutData *QTextFrame::layoutData() const': gives
    'QTextFrameLayoutData', which has no cute class yet.
  - Qt's 'void QTextFrame::setLayoutData(QTextFrameLayoutData *data)': names
    'QTextFrameLayoutData', which has no cute class yet.
  - Qt's 'iterator QTextFrame::begin() const': gives 'QTextFrame::iterator',
    which has no cute class yet.
  - Qt's 'iterator QTextFrame::end() const': gives 'QTextFrame::iterator',
    which has no cute class yet.

  What has no ritual
  ------------------

  10 of the 25 functions Qt declares: 3 takes or gives a type that cannot be
  passed yet; 3 private; 2 forbidden; 1 a template; 1 protected.

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
