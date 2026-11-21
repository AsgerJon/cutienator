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

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import Qt, QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QPointF, QRectF, QSizeF
  from . import QPaintDevice, QTextBlock, QTextDocument, QTextFormat
  from . import QTextFrame
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPaintDevice = WAIT['QPaintDevice']
  QPointF = WAIT['QPointF']
  QTextBlock = WAIT['QTextBlock']
  QTextFrame = WAIT['QTextFrame']

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
  that Python can call so far, 16 names in all: 'metaObject', 'tr',
  'hitTest', 'anchorAt', 'imageAt', 'formatAt', 'blockWithMarkerAt',
  'pageCount', 'documentSize', 'frameBoundingRect', 'blockBoundingRect',
  'setPaintDevice', 'paintDevice', 'document', 'registerHandler',
  'unregisterHandler'. None can be made from Python: one comes out of a
  function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QAbstractTextDocumentLayout::~QAbstractTextDocumentLayout()': the
    destructor: Python never removes a C++ QAbstractTextDocumentLayout.
  - Qt's 'void QAbstractTextDocumentLayout::draw(QPainter *painter, const
    PaintContext &context)': names
    'QAbstractTextDocumentLayout::PaintContext', which has no cute class yet.
  - Qt's 'QTextObjectInterface
    *QAbstractTextDocumentLayout::handlerForObject(int objectType) const':
    gives 'QTextObjectInterface', which has no cute class yet.

  What has no ritual
  ------------------

  18 of the 37 functions Qt declares: 7 protected; 4 a signal; 3 private; 2
  takes or gives a type that cannot be passed yet; 1 a template; 1 the class
  is abstract, so C++ cannot make one.

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
        self._valueOf(point), accuracy.value,
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
        self._valueOf(pos),
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
        self._valueOf(pos),
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
        self._valueOf(pos),
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
        self._valueOf(pos),
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
        self._addressOf(device),
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
        objectType, self._addressOf(component),
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
        objectType, self._addressOf(component),
    )
