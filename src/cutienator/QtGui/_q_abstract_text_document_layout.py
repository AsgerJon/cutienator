"""
QAbstractTextDocumentLayout binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/qabstracttextdocumentlayout.h, Qt 6.12.0. Changes made here are
#  lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import Qt, QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QPointF, QRectF, QSizeF
  from . import QAbstractTextDocumentLayoutPrivate, QPaintDevice, QPainter
  from . import QTextBlock, QTextCharFormat, QTextDocument, QTextFormat
  from . import QTextFrame, QTextInlineObject, QTextObjectInterface
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPaintDevice = WAIT['QPaintDevice']
  QPainter = WAIT['QPainter']
  QPointF = WAIT['QPointF']
  QRectF = WAIT['QRectF']
  QSizeF = WAIT['QSizeF']
  QTextBlock = WAIT['QTextBlock']
  QTextDocument = WAIT['QTextDocument']
  QTextFormat = WAIT['QTextFormat']
  QTextFrame = WAIT['QTextFrame']
  QTextInlineObject = WAIT['QTextInlineObject']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QAbstractTextDocumentLayout(QObject):
  """
  The cute side of Qt's QAbstractTextDocumentLayout: a plain Python object
  standing in front of one C++ QAbstractTextDocumentLayout.

  It is built on the cute 'QObject', as Qt's QAbstractTextDocumentLayout is
  built on Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QAbstractTextDocumentLayout that has a ritual and
  that Python can call so far, 29 names in all: 'metaObject', 'tr', 'd_func',
  'draw', 'hitTest', 'anchorAt', 'imageAt', 'formatAt', 'blockWithMarkerAt',
  'pageCount', 'documentSize', 'frameBoundingRect', 'blockBoundingRect',
  'setPaintDevice', 'paintDevice', 'document', 'registerHandler',
  'unregisterHandler', 'handlerForObject', 'update', 'updateBlock',
  'documentSizeChanged', 'pageCountChanged', 'documentChanged',
  'resizeInlineObject', 'positionInlineObject', 'drawInlineObject',
  'formatIndex', 'format'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QAbstractTextDocumentLayout::qt_metacast(const char *a0)':
    one of Qt's own inner workings.
  - Qt's 'int QAbstractTextDocumentLayout::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'const QAbstractTextDocumentLayoutPrivate
    *QAbstractTextDocumentLayout::d_func() const': takes in Python what
    'QAbstractTextDocumentLayoutPrivate
    *QAbstractTextDocumentLayout::d_func()' takes.
  - Qt's 'QAbstractTextDocumentLayout::~QAbstractTextDocumentLayout()': the
    destructor: Python never removes a C++ QAbstractTextDocumentLayout.
  - Qt's 'QAbstractTextDocumentLayout::QAbstractTextDocumentLayout(
    QAbstractTextDocumentLayoutPrivate &a0, QTextDocument *a1)': takes a type
    Python has no way to hand over yet.

  What has no ritual
  ------------------

  2 of the 37 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QAbstractTextDocumentLayout is created at the first use, not by
    'QAbstractTextDocumentLayout(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QAbstractTextDocumentLayout.
  - Qt tells when it has removed the C++ QAbstractTextDocumentLayout. Every
    call on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  #  The classes Qt writes inside QAbstractTextDocumentLayout, each a class
  #  in here as in C++.

  class PaintContext(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QAbstractTextDocumentLayout::PaintContext: a plain
    Python object standing in front of one C++
    QAbstractTextDocumentLayout::PaintContext.

    C++ hands a QAbstractTextDocumentLayout::PaintContext around as a copy,
    so every C++ QAbstractTextDocumentLayout::PaintContext behind a cute one
    is Python's own: it is removed, by the ritual named in
    '__delete_ritual__', when the cute object goes.

    What exists
    -----------

    No function of Qt's QAbstractTextDocumentLayout::PaintContext yet. It can
    be made from Python, in 1 way; see '__init__'.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QAbstractTextDocumentLayout::PaintContext::~PaintContext()': the
      destructor: Python removes its C++
      QAbstractTextDocumentLayout::PaintContext by it, and has no other use
      for it.

    What to expect
    --------------

    - The C++ QAbstractTextDocumentLayout::PaintContext is created at the
      first use, not by 'QAbstractTextDocumentLayout::PaintContext(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QAbstractTextDocumentLayout::PaintContext back
      gives a copy the ritual made for Python, in a new cute
      QAbstractTextDocumentLayout::PaintContext.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QAbstractTextDocumentLayout::PaintContext'

    #  Qt's '~QAbstractTextDocumentLayout::PaintContext()'. Naming it makes
    #  this a value class: Python owns every C++
    #  QAbstractTextDocumentLayout::PaintContext behind a cute one, and
    #  removes it by this ritual.
    __delete_ritual__ = (
        'ritual_ZN27QAbstractTextDocumentLayout12PaintContextD1Ev')

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
      'QAbstractTextDocumentLayout::PaintContext::PaintContext()', which is
      called at the first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qabstracttextdocumentlayout-paintcontext.html
      """
      #  QAbstractTextDocumentLayout::PaintContext::PaintContext()
      self._noteCreation(
          QAbstractTextDocumentLayout.PaintContext, lambda: Rituals.call(
              'ritual_ZN27QAbstractTextDocumentLayout12PaintContextC1Ev',
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

  class Selection(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QAbstractTextDocumentLayout::Selection: a plain
    Python object standing in front of one C++
    QAbstractTextDocumentLayout::Selection.

    C++ hands a QAbstractTextDocumentLayout::Selection around as a copy, so
    every C++ QAbstractTextDocumentLayout::Selection behind a cute one is
    Python's own: it is removed, by the ritual named in '__delete_ritual__',
    when the cute object goes.

    What exists
    -----------

    No function of Qt's QAbstractTextDocumentLayout::Selection yet. None can
    be made from Python: one comes out of a function of another class that
    gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QAbstractTextDocumentLayout::Selection::~Selection()': the
      destructor: Python removes its C++
      QAbstractTextDocumentLayout::Selection by it, and has no other use for
      it.

    What to expect
    --------------

    - The C++ QAbstractTextDocumentLayout::Selection is created at the first
      use, not by 'QAbstractTextDocumentLayout::Selection(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QAbstractTextDocumentLayout::Selection back gives a
      copy the ritual made for Python, in a new cute
      QAbstractTextDocumentLayout::Selection.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QAbstractTextDocumentLayout::Selection'

    #  Qt's '~QAbstractTextDocumentLayout::Selection()'. Naming it makes this
    #  a value class: Python owns every C++
    #  QAbstractTextDocumentLayout::Selection behind a cute one, and removes
    #  it by this ritual.
    __delete_ritual__ = (
        'ritual_ZN27QAbstractTextDocumentLayout9SelectionD1Ev')

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
    Calls Qt's 'QString QAbstractTextDocumentLayout::tr(const char *s, const
    char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstracttextdocumentlayout.html#tr

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
    #  QString QAbstractTextDocumentLayout::tr(const char *s, const char *c,
    #      int n)
    return Rituals.call(
        'ritual_ZN27QAbstractTextDocumentLayout2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QAbstractTextDocumentLayout'

  #  A C++ QAbstractTextDocumentLayout Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QAbstractTextDocumentLayout'

  #  The functions Qt calls itself that QAbstractTextDocumentLayout is the
  #  first to declare. A class of a program built on it can write one anew,
  #  and Qt then calls that. For each name: the key C++ knows the function
  #  by, what it gives, and what it takes.
  __virtual_functions__ = {
      'draw': (
          ('_ZN27QAbstractTextDocumentLayout4drawEP8QPainterRKNS_12PaintCon'
           'textE',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtGui:QPainter'),
               ('address', 'value',
                'QtGui:QAbstractTextDocumentLayout.PaintContext'),
           )),
      ),
      'hitTest': (
          ('_ZNK27QAbstractTextDocumentLayout7hitTestERK7QPointFN2Qt15HitTe'
           'stAccuracyE',
           ('int', 'number', ''),
           (
               ('address', 'value', 'QtCore:QPointF'),
               ('int', 'enum', 'QtCore:Qt.HitTestAccuracy'),
           )),
      ),
      'pageCount': (
          ('_ZNK27QAbstractTextDocumentLayout9pageCountEv',
           ('int', 'number', ''),
           ()),
      ),
      'documentSize': (
          ('_ZNK27QAbstractTextDocumentLayout12documentSizeEv',
           ('address', 'value', 'QtCore:QSizeF'),
           ()),
      ),
      'frameBoundingRect': (
          ('_ZNK27QAbstractTextDocumentLayout17frameBoundingRectEP10QTextFr'
           'ame',
           ('address', 'value', 'QtCore:QRectF'),
           (
               ('address', 'address', 'QtGui:QTextFrame'),
           )),
      ),
      'blockBoundingRect': (
          ('_ZNK27QAbstractTextDocumentLayout17blockBoundingRectERK10QTextB'
           'lock',
           ('address', 'value', 'QtCore:QRectF'),
           (
               ('address', 'value', 'QtGui:QTextBlock'),
           )),
      ),
      'documentChanged': (
          ('_ZN27QAbstractTextDocumentLayout15documentChangedEiii',
           ('nothing', 'nothing', ''),
           (
               ('int', 'number', ''),
               ('int', 'number', ''),
               ('int', 'number', ''),
           )),
      ),
      'resizeInlineObject': (
          ('_ZN27QAbstractTextDocumentLayout18resizeInlineObjectE17QTextInl'
           'ineObjectiRK11QTextFormat',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtGui:QTextInlineObject'),
               ('int', 'number', ''),
               ('address', 'value', 'QtGui:QTextFormat'),
           )),
      ),
      'positionInlineObject': (
          ('_ZN27QAbstractTextDocumentLayout20positionInlineObjectE17QTextI'
           'nlineObjectiRK11QTextFormat',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtGui:QTextInlineObject'),
               ('int', 'number', ''),
               ('address', 'value', 'QtGui:QTextFormat'),
           )),
      ),
      'drawInlineObject': (
          ('_ZN27QAbstractTextDocumentLayout16drawInlineObjectEP8QPainterRK'
           '6QRectF17QTextInlineObjectiRK11QTextFormat',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtGui:QPainter'),
               ('address', 'value', 'QtCore:QRectF'),
               ('address', 'value', 'QtGui:QTextInlineObject'),
               ('int', 'number', ''),
               ('address', 'value', 'QtGui:QTextFormat'),
           )),
      ),
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QAbstractTextDocumentLayout::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstracttextdocumentlayout.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QAbstractTextDocumentLayout::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK27QAbstractTextDocumentLayout10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  @overload(QPointF, Qt.HitTestAccuracy)
  def hitTest(self, point: QPointF, accuracy: Qt.HitTestAccuracy) -> int:
    """
    Calls Qt's 'int QAbstractTextDocumentLayout::hitTest(const QPointF
    &point, Qt::HitTestAccuracy accuracy) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstracttextdocumentlayout.html#hitTest

    Parameters
    ----------

    point : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    accuracy : Qt.HitTestAccuracy
      Passed on as its number.
    """
    #  int QAbstractTextDocumentLayout::hitTest(const QPointF &point,
    #      Qt::HitTestAccuracy accuracy) const
    return self.uglySide.call(
        'ritual_ZNK27QAbstractTextDocumentLayout7hitTestERK7QPointFN2Qt15Hi'
        'tTestAccuracyE',
        self._valueOf(point, 'QPointF'), accuracy.value,
    )

  @overload(QPointF)
  def anchorAt(self, pos: QPointF) -> str:
    """
    Calls Qt's 'QString QAbstractTextDocumentLayout::anchorAt(const QPointF
    &pos) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstracttextdocumentlayout.html#anchorAt

    Parameters
    ----------

    pos : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QAbstractTextDocumentLayout::anchorAt(const QPointF &pos)
    #      const
    return self.uglySide.call(
        'ritual_ZNK27QAbstractTextDocumentLayout8anchorAtERK7QPointF',
        self._valueOf(pos, 'QPointF'),
    )

  @overload(QPointF)
  def imageAt(self, pos: QPointF) -> str:
    """
    Calls Qt's 'QString QAbstractTextDocumentLayout::imageAt(const QPointF
    &pos) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstracttextdocumentlayout.html#imageAt

    Parameters
    ----------

    pos : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QAbstractTextDocumentLayout::imageAt(const QPointF &pos) const
    return self.uglySide.call(
        'ritual_ZNK27QAbstractTextDocumentLayout7imageAtERK7QPointF',
        self._valueOf(pos, 'QPointF'),
    )

  @overload(QPointF)
  def formatAt(self, pos: QPointF) -> QTextFormat:
    """
    Calls Qt's 'QTextFormat QAbstractTextDocumentLayout::formatAt(const
    QPointF &pos) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstracttextdocumentlayout.html#formatAt

    Parameters
    ----------

    pos : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    Returns
    -------

    QTextFormat
      A new cute QTextFormat around the copy Qt gave back. Python owns it.
    """
    #  QTextFormat QAbstractTextDocumentLayout::formatAt(const QPointF &pos)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK27QAbstractTextDocumentLayout8formatAtERK7QPointF',
        self._valueOf(pos, 'QPointF'),
    )
    from . import QTextFormat
    return QTextFormat._cuteOwning(address)

  @overload(QPointF)
  def blockWithMarkerAt(self, pos: QPointF) -> QTextBlock:
    """
    Calls Qt's 'QTextBlock
    QAbstractTextDocumentLayout::blockWithMarkerAt(const QPointF &pos)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstracttextdocumentlayout.html#blockWithMarkerAt

    Parameters
    ----------

    pos : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    Returns
    -------

    QTextBlock
      A new cute QTextBlock around the copy Qt gave back. Python owns it.
    """
    #  QTextBlock QAbstractTextDocumentLayout::blockWithMarkerAt(const
    #      QPointF &pos) const
    address = self.uglySide.call(
        'ritual_ZNK27QAbstractTextDocumentLayout17blockWithMarkerAtERK7QPoi'
        'ntF',
        self._valueOf(pos, 'QPointF'),
    )
    from . import QTextBlock
    return QTextBlock._cuteOwning(address)

  def pageCount(self) -> int:
    """
    Calls Qt's 'int QAbstractTextDocumentLayout::pageCount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstracttextdocumentlayout.html#pageCount
    """
    #  int QAbstractTextDocumentLayout::pageCount() const
    return self.uglySide.call(
        'ritual_ZNK27QAbstractTextDocumentLayout9pageCountEv',
    )

  def documentSize(self) -> QSizeF:
    """
    Calls Qt's 'QSizeF QAbstractTextDocumentLayout::documentSize() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstracttextdocumentlayout.html#documentSize

    Returns
    -------

    QSizeF
      A new cute QSizeF around the copy Qt gave back. Python owns it.
    """
    #  QSizeF QAbstractTextDocumentLayout::documentSize() const
    address = self.uglySide.call(
        'ritual_ZNK27QAbstractTextDocumentLayout12documentSizeEv',
    )
    from ..QtCore import QSizeF
    return QSizeF._cuteOwning(address)

  @overload(QTextFrame)
  @overload(NoneType)
  def frameBoundingRect(self, frame: Optional[QTextFrame]) -> QRectF:
    """
    Calls Qt's 'QRectF
    QAbstractTextDocumentLayout::frameBoundingRect(QTextFrame *frame) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstracttextdocumentlayout.html#frameBoundingRect

    Parameters
    ----------

    frame : Optional[QTextFrame]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QAbstractTextDocumentLayout::frameBoundingRect(QTextFrame
    #      *frame) const
    address = self.uglySide.call(
        'ritual_ZNK27QAbstractTextDocumentLayout17frameBoundingRectEP10QTex'
        'tFrame',
        self._addressOf(frame),
    )
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  @overload(QTextBlock)
  def blockBoundingRect(self, block: QTextBlock) -> QRectF:
    """
    Calls Qt's 'QRectF QAbstractTextDocumentLayout::blockBoundingRect(const
    QTextBlock &block) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstracttextdocumentlayout.html#blockBoundingRect

    Parameters
    ----------

    block : QTextBlock
      Passed on as a value: Qt reads the C++ QTextBlock, which stays Python's
      own.

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QAbstractTextDocumentLayout::blockBoundingRect(const QTextBlock
    #      &block) const
    address = self.uglySide.call(
        'ritual_ZNK27QAbstractTextDocumentLayout17blockBoundingRectERK10QTe'
        'xtBlock',
        self._valueOf(block),
    )
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  def paintDevice(self) -> Optional[QPaintDevice]:
    """
    Calls Qt's 'QPaintDevice *QAbstractTextDocumentLayout::paintDevice()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstracttextdocumentlayout.html#paintDevice

    Returns
    -------

    Optional[QPaintDevice]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPaintDevice *QAbstractTextDocumentLayout::paintDevice() const
    address = self.uglySide.call(
        'ritual_ZNK27QAbstractTextDocumentLayout11paintDeviceEv',
    )
    from . import QPaintDevice
    return QPaintDevice._cuteAt(address)

  def document(self) -> Optional[QTextDocument]:
    """
    Calls Qt's 'QTextDocument *QAbstractTextDocumentLayout::document()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstracttextdocumentlayout.html#document

    Returns
    -------

    Optional[QTextDocument]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QTextDocument *QAbstractTextDocumentLayout::document() const
    address = self.uglySide.call(
        'ritual_ZNK27QAbstractTextDocumentLayout8documentEv',
    )
    from . import QTextDocument
    return QTextDocument._cuteAt(address)

  @overload(int)
  def handlerForObject(
      self,
      objectType: int,
  ) -> Optional[QTextObjectInterface]:
    """
    Calls Qt's 'QTextObjectInterface
    *QAbstractTextDocumentLayout::handlerForObject(int objectType) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstracttextdocumentlayout.html#handlerForObject

    Parameters
    ----------

    objectType : int
      Passed on as it is.

    Returns
    -------

    Optional[QTextObjectInterface]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QTextObjectInterface
    #      *QAbstractTextDocumentLayout::handlerForObject(int objectType)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK27QAbstractTextDocumentLayout16handlerForObjectEi',
        objectType,
    )
    from . import QTextObjectInterface
    return QTextObjectInterface._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QPaintDevice)
  @overload(NoneType)
  def setPaintDevice(self, device: Optional[QPaintDevice]) -> None:
    """
    Calls Qt's 'void QAbstractTextDocumentLayout::setPaintDevice(QPaintDevice
    *device)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstracttextdocumentlayout.html#setPaintDevice

    Parameters
    ----------

    device : Optional[QPaintDevice]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAbstractTextDocumentLayout::setPaintDevice(QPaintDevice *device)
    self.uglySide.call(
        'ritual_ZN27QAbstractTextDocumentLayout14setPaintDeviceEP12QPaintDe'
        'vice',
        self._addressOf(device, 'QPaintDevice'),
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
    Notes what was given, for Qt's
    'QAbstractTextDocumentLayout::QAbstractTextDocumentLayout(QTextDocument
    *doc)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstracttextdocumentlayout.html

    Parameters
    ----------

    doc : Optional[QTextDocument]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QAbstractTextDocumentLayout::QAbstractTextDocumentLayout(QTextDocument
    #      *doc)
    self._noteCreation(QAbstractTextDocumentLayout, lambda: Rituals.call(
        'ritual_ZN27QAbstractTextDocumentLayoutC1EP13QTextDocument',
        self._addressOf(doc),
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

  def d_func(self) -> Optional[QAbstractTextDocumentLayoutPrivate]:
    """
    Calls Qt's 'QAbstractTextDocumentLayoutPrivate
    *QAbstractTextDocumentLayout::d_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstracttextdocumentlayout.html#d_func

    Returns
    -------

    Optional[QAbstractTextDocumentLayoutPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractTextDocumentLayoutPrivate
    #      *QAbstractTextDocumentLayout::d_func()
    address = self.uglySide.call(
        'ritual_ZN27QAbstractTextDocumentLayout6d_funcEv',
    )
    from . import QAbstractTextDocumentLayoutPrivate
    return QAbstractTextDocumentLayoutPrivate._cuteAt(address)

  @overload(QPainter, PaintContext)
  @overload(NoneType, PaintContext)
  def draw(self, painter: Optional[QPainter], context: PaintContext) -> None:
    """
    Calls Qt's 'void QAbstractTextDocumentLayout::draw(QPainter *painter,
    const PaintContext &context)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstracttextdocumentlayout.html#draw

    Parameters
    ----------

    painter : Optional[QPainter]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    context : PaintContext
      Passed on as a value: Qt reads the C++
      QAbstractTextDocumentLayout::PaintContext, which stays Python's own.
    """
    #  void QAbstractTextDocumentLayout::draw(QPainter *painter, const
    #      PaintContext &context)
    self.uglySide.call(
        'ritual_ZN27QAbstractTextDocumentLayout4drawEP8QPainterRKNS_12Paint'
        'ContextE',
        self._addressOf(painter), self._valueOf(context),
    )

  @overload(int, QObject)
  @overload(int, NoneType)
  def registerHandler(
      self,
      objectType: int,
      component: Optional[QObject],
  ) -> None:
    """
    Calls Qt's 'void QAbstractTextDocumentLayout::registerHandler(int
    objectType, QObject *component)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstracttextdocumentlayout.html#registerHandler

    Parameters
    ----------

    objectType : int
      Passed on as it is.

    component : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAbstractTextDocumentLayout::registerHandler(int objectType,
    #      QObject *component)
    self.uglySide.call(
        'ritual_ZN27QAbstractTextDocumentLayout15registerHandlerEiP7QObject',
        objectType, self._addressOf(component, 'QObject'),
    )

  @overload(int)
  @overload(int, QObject)
  @overload(int, NoneType)
  def unregisterHandler(
      self,
      objectType: int,
      component: Optional[QObject] = None,
  ) -> None:
    """
    Calls Qt's 'void QAbstractTextDocumentLayout::unregisterHandler(int
    objectType, QObject *component)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstracttextdocumentlayout.html#unregisterHandler

    Parameters
    ----------

    objectType : int
      Passed on as it is.

    component : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  void QAbstractTextDocumentLayout::unregisterHandler(int objectType,
    #      QObject *component)
    self.uglySide.call(
        'ritual_ZN27QAbstractTextDocumentLayout17unregisterHandlerEiP7QObje'
        'ct',
        objectType, self._addressOf(component, 'QObject'),
    )

  @overload()
  @overload(QRectF)
  def update(self, a0: Optional[QRectF] = None) -> None:
    """
    Calls Qt's 'void QAbstractTextDocumentLayout::update(const QRectF &a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstracttextdocumentlayout.html#update

    Parameters
    ----------

    a0 : Optional[QRectF]
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own. May be left out, as in Qt: a new 'QRectF(0.0, 0.0, 1000000000.0,
      1000000000.0)' is then passed on.
    """
    #  void QAbstractTextDocumentLayout::update(const QRectF &a0)
    if a0 is None:
      from ..QtCore import QRectF
      a0 = QRectF(0.0, 0.0, 1000000000.0, 1000000000.0)
    self.uglySide.call(
        'ritual_ZN27QAbstractTextDocumentLayout6updateERK6QRectF',
        self._valueOf(a0),
    )

  @overload(QTextBlock)
  def updateBlock(self, block: QTextBlock) -> None:
    """
    Calls Qt's 'void QAbstractTextDocumentLayout::updateBlock(const
    QTextBlock &block)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstracttextdocumentlayout.html#updateBlock

    Parameters
    ----------

    block : QTextBlock
      Passed on as a value: Qt reads the C++ QTextBlock, which stays Python's
      own.
    """
    #  void QAbstractTextDocumentLayout::updateBlock(const QTextBlock &block)
    self.uglySide.call(
        'ritual_ZN27QAbstractTextDocumentLayout11updateBlockERK10QTextBlock',
        self._valueOf(block),
    )

  @overload(QSizeF)
  def documentSizeChanged(self, newSize: QSizeF) -> None:
    """
    Calls Qt's 'void QAbstractTextDocumentLayout::documentSizeChanged(const
    QSizeF &newSize)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstracttextdocumentlayout.html

    Parameters
    ----------

    newSize : QSizeF
      Passed on as a value: Qt reads the C++ QSizeF, which stays Python's
      own.
    """
    #  void QAbstractTextDocumentLayout::documentSizeChanged(const QSizeF
    #      &newSize)
    self.uglySide.call(
        'ritual_ZN27QAbstractTextDocumentLayout19documentSizeChangedERK6QSi'
        'zeF',
        self._valueOf(newSize),
    )

  @overload(int)
  def pageCountChanged(self, newPages: int) -> None:
    """
    Calls Qt's 'void QAbstractTextDocumentLayout::pageCountChanged(int
    newPages)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstracttextdocumentlayout.html#pageCountChanged

    Parameters
    ----------

    newPages : int
      Passed on as it is.
    """
    #  void QAbstractTextDocumentLayout::pageCountChanged(int newPages)
    self.uglySide.call(
        'ritual_ZN27QAbstractTextDocumentLayout16pageCountChangedEi',
        newPages,
    )

  @overload(int, int, int)
  def documentChanged(
      self,
      from_: int,
      charsRemoved: int,
      charsAdded: int,
  ) -> None:
    """
    Calls Qt's 'void QAbstractTextDocumentLayout::documentChanged(int from,
    int charsRemoved, int charsAdded)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstracttextdocumentlayout.html#documentChanged

    Parameters
    ----------

    from_ : int
      Passed on as it is.

    charsRemoved : int
      Passed on as it is.

    charsAdded : int
      Passed on as it is.
    """
    #  void QAbstractTextDocumentLayout::documentChanged(int from, int
    #      charsRemoved, int charsAdded)
    self.uglySide.call(
        'ritual_ZN27QAbstractTextDocumentLayout15documentChangedEiii',
        from_, charsRemoved, charsAdded,
    )

  @overload(QTextInlineObject, int, QTextFormat)
  def resizeInlineObject(
      self,
      item: QTextInlineObject,
      posInDocument: int,
      format: QTextFormat,
  ) -> None:
    """
    Calls Qt's 'void
    QAbstractTextDocumentLayout::resizeInlineObject(QTextInlineObject item,
    int posInDocument, const QTextFormat &format)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstracttextdocumentlayout.html

    Parameters
    ----------

    item : QTextInlineObject
      Passed on as a value: Qt reads the C++ QTextInlineObject, which stays
      Python's own.

    posInDocument : int
      Passed on as it is.

    format : QTextFormat
      Passed on as a value: Qt reads the C++ QTextFormat, which stays
      Python's own.
    """
    #  void QAbstractTextDocumentLayout::resizeInlineObject(QTextInlineObject
    #      item, int posInDocument, const QTextFormat &format)
    ritual = (
        'ritual_ZN27QAbstractTextDocumentLayout18resizeInlineObjectE17QText'
        'InlineObjectiRK11QTextFormat')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN27QAbstractTextDocumentLayout18resizeInlineObjectE1'
          '7QTextInlineObjectiRK11QTextFormat')
    self.uglySide.call(
        ritual, self._valueOf(item), posInDocument, self._valueOf(format),
    )

  @overload(QTextInlineObject, int, QTextFormat)
  def positionInlineObject(
      self,
      item: QTextInlineObject,
      posInDocument: int,
      format: QTextFormat,
  ) -> None:
    """
    Calls Qt's 'void
    QAbstractTextDocumentLayout::positionInlineObject(QTextInlineObject item,
    int posInDocument, const QTextFormat &format)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstracttextdocumentlayout.html

    Parameters
    ----------

    item : QTextInlineObject
      Passed on as a value: Qt reads the C++ QTextInlineObject, which stays
      Python's own.

    posInDocument : int
      Passed on as it is.

    format : QTextFormat
      Passed on as a value: Qt reads the C++ QTextFormat, which stays
      Python's own.
    """
    #  void QAbstractTextDocumentLayout::positionInlineObject(
    #      QTextInlineObject item, int posInDocument, const QTextFormat
    #      &format)
    ritual = (
        'ritual_ZN27QAbstractTextDocumentLayout20positionInlineObjectE17QTe'
        'xtInlineObjectiRK11QTextFormat')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN27QAbstractTextDocumentLayout20positionInlineObject'
          'E17QTextInlineObjectiRK11QTextFormat')
    self.uglySide.call(
        ritual, self._valueOf(item), posInDocument, self._valueOf(format),
    )

  @overload(QPainter, QRectF, QTextInlineObject, int, QTextFormat)
  @overload(NoneType, QRectF, QTextInlineObject, int, QTextFormat)
  def drawInlineObject(
      self,
      painter: Optional[QPainter],
      rect: QRectF,
      object: QTextInlineObject,
      posInDocument: int,
      format: QTextFormat,
  ) -> None:
    """
    Calls Qt's 'void QAbstractTextDocumentLayout::drawInlineObject(QPainter
    *painter, const QRectF &rect, QTextInlineObject object, int
    posInDocument, const QTextFormat &format)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstracttextdocumentlayout.html#drawInlineObject

    Parameters
    ----------

    painter : Optional[QPainter]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    rect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    object : QTextInlineObject
      Passed on as a value: Qt reads the C++ QTextInlineObject, which stays
      Python's own.

    posInDocument : int
      Passed on as it is.

    format : QTextFormat
      Passed on as a value: Qt reads the C++ QTextFormat, which stays
      Python's own.
    """
    #  void QAbstractTextDocumentLayout::drawInlineObject(QPainter *painter,
    #      const QRectF &rect, QTextInlineObject object, int posInDocument,
    #      const QTextFormat &format)
    ritual = (
        'ritual_ZN27QAbstractTextDocumentLayout16drawInlineObjectEP8QPainte'
        'rRK6QRectF17QTextInlineObjectiRK11QTextFormat')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN27QAbstractTextDocumentLayout16drawInlineObjectEP8Q'
          'PainterRK6QRectF17QTextInlineObjectiRK11QTextFormat')
    self.uglySide.call(
        ritual,
        self._addressOf(painter), self._valueOf(rect), self._valueOf(object),
        posInDocument, self._valueOf(format),
    )

  @overload(int)
  def formatIndex(self, pos: int) -> int:
    """
    Calls Qt's 'int QAbstractTextDocumentLayout::formatIndex(int pos)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstracttextdocumentlayout.html#formatIndex

    Parameters
    ----------

    pos : int
      Passed on as it is.
    """
    #  int QAbstractTextDocumentLayout::formatIndex(int pos)
    return self.uglySide.call(
        'ritual_ZN27QAbstractTextDocumentLayout11formatIndexEi', pos,
    )

  @overload(int)
  def format(self, pos: int) -> QTextCharFormat:
    """
    Calls Qt's 'QTextCharFormat QAbstractTextDocumentLayout::format(int
    pos)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstracttextdocumentlayout.html#format

    Parameters
    ----------

    pos : int
      Passed on as it is.

    Returns
    -------

    QTextCharFormat
      A new cute QTextCharFormat around the copy Qt gave back. Python owns
      it.
    """
    #  QTextCharFormat QAbstractTextDocumentLayout::format(int pos)
    address = self.uglySide.call(
        'ritual_ZN27QAbstractTextDocumentLayout6formatEi', pos,
    )
    from . import QTextCharFormat
    return QTextCharFormat._cuteOwning(address)
