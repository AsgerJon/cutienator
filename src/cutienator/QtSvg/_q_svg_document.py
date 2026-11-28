"""
QSvgDocument binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtSvg/6.12.0/QtSvg/private/qsvgdocument_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QSvgDocument to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from . import QtSvg, QSvgNode, QSvgStructureNode

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QRectF, QSize
  from ..QtGui import QPainter, QTransform
  from . import QSvgFont
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPainter = WAIT['QPainter']
  QRectF = WAIT['QRectF']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSvgDocument(QSvgStructureNode):
  """
  The cute side of Qt's QSvgDocument: a plain Python object standing in front
  of one C++ QSvgDocument.

  It is built on the cute 'QSvgStructureNode', as Qt's QSvgDocument is built
  on Qt's QSvgStructureNode, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QSvgDocument that has a ritual and that Python can
  call so far, 30 names in all: 'type', 'size', 'setWidth', 'setHeight',
  'width', 'height', 'widthPercent', 'heightPercent', 'preserveAspectRatio',
  'setPreserveAspectRatio', 'viewBox', 'setViewBox',
  'isCalculatingImplicitViewBox', 'options', 'draw', 'transformForElement',
  'boundsOnElement', 'elementExists', 'svgFont', 'addNamedNode', 'namedNode',
  'restartAnimation', 'currentElapsed', 'animated', 'setAnimated',
  'animationDuration', 'currentFrame', 'setCurrentFrame',
  'setFramesPerSecond', 'mapSourceToTarget'. It can be made from Python, in 1
  way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'std::unique_ptr<QSvgDocument> QSvgDocument::load(const QString
    &file, QtSvg::Options options, QtSvg::AnimatorType type)': gives a type
    Python has no way to take yet.
  - Qt's 'std::unique_ptr<QSvgDocument> QSvgDocument::load(const QByteArray
    &contents, QtSvg::Options options, QtSvg::AnimatorType type)': gives a
    type Python has no way to take yet.
  - Qt's 'std::unique_ptr<QSvgDocument> QSvgDocument::load(QXmlStreamReader
    *contents, QtSvg::Options options, QtSvg::AnimatorType type)': gives a
    type Python has no way to take yet.
  - Qt's 'bool QSvgDocument::isLikelySvg(QIODevice *device, bool
    *isCompressed)': takes a number to change where it is.
  - Qt's 'QSvgDocument::~QSvgDocument()': the destructor: Python never
    removes a C++ QSvgDocument.
  - Qt's 'void QSvgDocument::drawCommand(QPainter *a0, QSvgExtraStates &a1)':
    takes a type Python has no way to hand over yet.
  - Qt's 'void QSvgDocument::addPaintServer(QSvgPaintServerSharedPtr
    paintServer, const QString &id)': takes a type Python has no way to hand
    over yet.
  - Qt's 'QSvgPaintServerSharedPtr QSvgDocument::paintServer(QStringView id)
    const': gives a type Python has no way to take yet.
  - Qt's 'QSharedPointer<QSvgAbstractAnimator> QSvgDocument::animator()
    const': gives a type Python has no way to take yet.

  What has no ritual
  ------------------

  1 of the 43 functions Qt declares: 1 the compiler refuses its ritual as it
  would be written here.

  What to expect
  --------------

  - The C++ QSvgDocument is created at the first use, not by
    'QSvgDocument(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSvgDocument.
  - Each name of Qt's QSvgDocument that has no cute function yet,
    'addPaintServer', 'addSvgFont', 'animator', 'isLikelySvg', 'load',
    'paintServer', holds a function that raises 'NotImplementedError', and
    its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSvgDocument'

  #  A C++ QSvgDocument Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QSvgDocument'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def type(self) -> QSvgNode.Type:
    """
    Calls Qt's 'Type QSvgDocument::type() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgdocument.html#type

    Returns
    -------

    QSvgNode.Type
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'QSvgNode.Type(number)'
      gives.
    """
    #  Type QSvgDocument::type() const
    ritual = 'ritual_ZNK12QSvgDocument4typeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK12QSvgDocument4typeEv'
    return QSvgNode.Type(self.uglySide.call(ritual))

  def size(self) -> QSize:
    """
    Calls Qt's 'QSize QSvgDocument::size() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgdocument.html#size

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QSvgDocument::size() const
    address = self.uglySide.call('ritual_ZNK12QSvgDocument4sizeEv')
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  def width(self) -> int:
    """
    Calls Qt's 'int QSvgDocument::width() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgdocument.html#width
    """
    #  int QSvgDocument::width() const
    return self.uglySide.call('ritual_ZNK12QSvgDocument5widthEv')

  def height(self) -> int:
    """
    Calls Qt's 'int QSvgDocument::height() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgdocument.html#height
    """
    #  int QSvgDocument::height() const
    return self.uglySide.call('ritual_ZNK12QSvgDocument6heightEv')

  def widthPercent(self) -> bool:
    """
    Calls Qt's 'bool QSvgDocument::widthPercent() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgdocument.html#widthPercent
    """
    #  bool QSvgDocument::widthPercent() const
    return self.uglySide.call('ritual_ZNK12QSvgDocument12widthPercentEv')

  def heightPercent(self) -> bool:
    """
    Calls Qt's 'bool QSvgDocument::heightPercent() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgdocument.html#heightPercent
    """
    #  bool QSvgDocument::heightPercent() const
    return self.uglySide.call('ritual_ZNK12QSvgDocument13heightPercentEv')

  def preserveAspectRatio(self) -> bool:
    """
    Calls Qt's 'bool QSvgDocument::preserveAspectRatio() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsvgdocument.html#preserveAspectRatio
    """
    #  bool QSvgDocument::preserveAspectRatio() const
    return self.uglySide.call(
        'ritual_ZNK12QSvgDocument19preserveAspectRatioEv',
    )

  def viewBox(self) -> QRectF:
    """
    Calls Qt's 'QRectF QSvgDocument::viewBox() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgdocument.html#viewBox

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QSvgDocument::viewBox() const
    address = self.uglySide.call('ritual_ZNK12QSvgDocument7viewBoxEv')
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  def isCalculatingImplicitViewBox(self) -> bool:
    """
    Calls Qt's 'bool QSvgDocument::isCalculatingImplicitViewBox() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsvgdocument.html#isCalculatingImplicitViewBox
    """
    #  bool QSvgDocument::isCalculatingImplicitViewBox() const
    return self.uglySide.call(
        'ritual_ZNK12QSvgDocument28isCalculatingImplicitViewBoxEv',
    )

  def options(self) -> QtSvg.Options:
    """
    Calls Qt's 'QtSvg::Options QSvgDocument::options() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgdocument.html#options

    Returns
    -------

    QtSvg.Options
      The value standing for the combination Qt gave back.
    """
    #  QtSvg::Options QSvgDocument::options() const
    return QtSvg.Options(self.uglySide.call(
        'ritual_ZNK12QSvgDocument7optionsEv',
    ))

  @overload(str)
  def transformForElement(self, id: str) -> QTransform:
    """
    Calls Qt's 'QTransform QSvgDocument::transformForElement(const QString
    &id) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsvgdocument.html#transformForElement

    Parameters
    ----------

    id : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QTransform
      A new cute QTransform around the copy Qt gave back. Python owns it.
    """
    #  QTransform QSvgDocument::transformForElement(const QString &id) const
    address = self.uglySide.call(
        'ritual_ZNK12QSvgDocument19transformForElementERK7QString', id,
    )
    from ..QtGui import QTransform
    return QTransform._cuteOwning(address)

  @overload(str)
  def boundsOnElement(self, id: str) -> QRectF:
    """
    Calls Qt's 'QRectF QSvgDocument::boundsOnElement(const QString &id)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgdocument.html#boundsOnElement

    Parameters
    ----------

    id : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QSvgDocument::boundsOnElement(const QString &id) const
    address = self.uglySide.call(
        'ritual_ZNK12QSvgDocument15boundsOnElementERK7QString', id,
    )
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  @overload(str)
  def elementExists(self, id: str) -> bool:
    """
    Calls Qt's 'bool QSvgDocument::elementExists(const QString &id) const'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgdocument.html#elementExists

    Parameters
    ----------

    id : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QSvgDocument::elementExists(const QString &id) const
    return self.uglySide.call(
        'ritual_ZNK12QSvgDocument13elementExistsERK7QString', id,
    )

  @overload(str)
  def svgFont(self, family: str) -> Optional[QSvgFont]:
    """
    Calls Qt's 'QSvgFont *QSvgDocument::svgFont(const QString &family)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgdocument.html#svgFont

    Parameters
    ----------

    family : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    Optional[QSvgFont]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSvgFont *QSvgDocument::svgFont(const QString &family) const
    address = self.uglySide.call(
        'ritual_ZNK12QSvgDocument7svgFontERK7QString', family,
    )
    from . import QSvgFont
    return QSvgFont._cuteAt(address)

  @overload(str)
  def namedNode(self, id: str) -> Optional[QSvgNode]:
    """
    Calls Qt's 'QSvgNode *QSvgDocument::namedNode(const QString &id) const'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgdocument.html#namedNode

    Parameters
    ----------

    id : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    Optional[QSvgNode]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSvgNode *QSvgDocument::namedNode(const QString &id) const
    address = self.uglySide.call(
        'ritual_ZNK12QSvgDocument9namedNodeERK7QString', id,
    )
    return QSvgNode._cuteAt(address)

  def currentElapsed(self) -> int:
    """
    Calls Qt's 'qint64 QSvgDocument::currentElapsed() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgdocument.html#currentElapsed
    """
    #  qint64 QSvgDocument::currentElapsed() const
    return self.uglySide.call('ritual_ZNK12QSvgDocument14currentElapsedEv')

  def animated(self) -> bool:
    """
    Calls Qt's 'bool QSvgDocument::animated() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgdocument.html#animated
    """
    #  bool QSvgDocument::animated() const
    return self.uglySide.call('ritual_ZNK12QSvgDocument8animatedEv')

  def animationDuration(self) -> int:
    """
    Calls Qt's 'int QSvgDocument::animationDuration() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsvgdocument.html#animationDuration
    """
    #  int QSvgDocument::animationDuration() const
    return self.uglySide.call(
        'ritual_ZNK12QSvgDocument17animationDurationEv',
    )

  def currentFrame(self) -> int:
    """
    Calls Qt's 'int QSvgDocument::currentFrame() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgdocument.html#currentFrame
    """
    #  int QSvgDocument::currentFrame() const
    return self.uglySide.call('ritual_ZNK12QSvgDocument12currentFrameEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int, bool)
  def setWidth(self, len: int, percent: bool) -> None:
    """
    Calls Qt's 'void QSvgDocument::setWidth(int len, bool percent)'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgdocument.html#setWidth

    Parameters
    ----------

    len : int
      Passed on as it is.

    percent : bool
      Passed on as it is.
    """
    #  void QSvgDocument::setWidth(int len, bool percent)
    self.uglySide.call('ritual_ZN12QSvgDocument8setWidthEib', len, percent)

  @overload(int, bool)
  def setHeight(self, len: int, percent: bool) -> None:
    """
    Calls Qt's 'void QSvgDocument::setHeight(int len, bool percent)'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgdocument.html#setHeight

    Parameters
    ----------

    len : int
      Passed on as it is.

    percent : bool
      Passed on as it is.
    """
    #  void QSvgDocument::setHeight(int len, bool percent)
    self.uglySide.call('ritual_ZN12QSvgDocument9setHeightEib', len, percent)

  @overload(bool)
  def setPreserveAspectRatio(self, on: bool) -> None:
    """
    Calls Qt's 'void QSvgDocument::setPreserveAspectRatio(bool on)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsvgdocument.html#setPreserveAspectRatio

    Parameters
    ----------

    on : bool
      Passed on as it is.
    """
    #  void QSvgDocument::setPreserveAspectRatio(bool on)
    self.uglySide.call(
        'ritual_ZN12QSvgDocument22setPreserveAspectRatioEb', on,
    )

  @overload(QRectF)
  def setViewBox(self, rect: QRectF) -> None:
    """
    Calls Qt's 'void QSvgDocument::setViewBox(const QRectF &rect)'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgdocument.html#setViewBox

    Parameters
    ----------

    rect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void QSvgDocument::setViewBox(const QRectF &rect)
    self.uglySide.call(
        'ritual_ZN12QSvgDocument10setViewBoxERK6QRectF', self._valueOf(rect),
    )

  @overload(bool)
  def setAnimated(self, a: bool) -> None:
    """
    Calls Qt's 'void QSvgDocument::setAnimated(bool a)'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgdocument.html#setAnimated

    Parameters
    ----------

    a : bool
      Passed on as it is.
    """
    #  void QSvgDocument::setAnimated(bool a)
    self.uglySide.call('ritual_ZN12QSvgDocument11setAnimatedEb', a)

  @overload(int)
  def setCurrentFrame(self, a0: int) -> None:
    """
    Calls Qt's 'void QSvgDocument::setCurrentFrame(int a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgdocument.html#setCurrentFrame

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  void QSvgDocument::setCurrentFrame(int a0)
    self.uglySide.call('ritual_ZN12QSvgDocument15setCurrentFrameEi', a0)

  @overload(int)
  def setFramesPerSecond(self, num: int) -> None:
    """
    Calls Qt's 'void QSvgDocument::setFramesPerSecond(int num)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsvgdocument.html#setFramesPerSecond

    Parameters
    ----------

    num : int
      Passed on as it is.
    """
    #  void QSvgDocument::setFramesPerSecond(int num)
    self.uglySide.call('ritual_ZN12QSvgDocument18setFramesPerSecondEi', num)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QtSvg.Options, QtSvg.AnimatorType)
  def __init__(
      self,
      options: QtSvg.Options,
      type: QtSvg.AnimatorType,
  ) -> None:
    """
    Notes what was given, for Qt's 'QSvgDocument::QSvgDocument(QtSvg::Options
    options, QtSvg::AnimatorType type)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qsvgdocument.html#QSvgDocument

    Parameters
    ----------

    options : QtSvg.Options
      Passed on as its number.

    type : QtSvg.AnimatorType
      Passed on as its number.
    """
    #  QSvgDocument::QSvgDocument(QtSvg::Options options, QtSvg::AnimatorType
    #      type)
    self._noteCreation(QSvgDocument, lambda: Rituals.call(
        'ritual_ZN12QSvgDocumentC1E6QFlagsIN5QtSvg6OptionEENS1_12AnimatorTy'
        'peE',
        options.value, type.value,
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

  @overload(QPainter)
  @overload(NoneType)
  def draw(self, p: Optional[QPainter]) -> None:
    """
    Calls Qt's 'void QSvgDocument::draw(QPainter *p)'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgdocument.html#draw

    Parameters
    ----------

    p : Optional[QPainter]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSvgDocument::draw(QPainter *p)
    self.uglySide.call(
        'ritual_ZN12QSvgDocument4drawEP8QPainter', self._addressOf(p),
    )

  @overload(QPainter, QRectF)
  @overload(NoneType, QRectF)
  def draw(self, p: Optional[QPainter], bounds: QRectF) -> None:
    """
    Calls Qt's 'void QSvgDocument::draw(QPainter *p, const QRectF &bounds)'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgdocument.html#draw

    Parameters
    ----------

    p : Optional[QPainter]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    bounds : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void QSvgDocument::draw(QPainter *p, const QRectF &bounds)
    self.uglySide.call(
        'ritual_ZN12QSvgDocument4drawEP8QPainterRK6QRectF',
        self._addressOf(p), self._valueOf(bounds),
    )

  @overload(QPainter, str)
  @overload(NoneType, str)
  @overload(QPainter, str, QRectF)
  @overload(NoneType, str, QRectF)
  def draw(
      self,
      p: Optional[QPainter],
      id: str,
      bounds: Optional[QRectF] = None,
  ) -> None:
    """
    Calls Qt's 'void QSvgDocument::draw(QPainter *p, const QString &id, const
    QRectF &bounds)'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgdocument.html#draw

    Parameters
    ----------

    p : Optional[QPainter]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    id : str
      Passed on as it is: a QString is made of it for the call.

    bounds : Optional[QRectF]
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own. May be left out, as in Qt: a new 'QRectF()' is then passed on.
    """
    #  void QSvgDocument::draw(QPainter *p, const QString &id, const QRectF
    #      &bounds)
    if bounds is None:
      from ..QtCore import QRectF
      bounds = QRectF()
    self.uglySide.call(
        'ritual_ZN12QSvgDocument4drawEP8QPainterRK7QStringRK6QRectF',
        self._addressOf(p), id, self._valueOf(bounds),
    )

  @overload(str, QSvgNode)
  @overload(str, NoneType)
  def addNamedNode(self, id: str, node: Optional[QSvgNode]) -> None:
    """
    Calls Qt's 'void QSvgDocument::addNamedNode(const QString &id, QSvgNode
    *node)'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgdocument.html#addNamedNode

    Parameters
    ----------

    id : str
      Passed on as it is: a QString is made of it for the call.

    node : Optional[QSvgNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSvgDocument::addNamedNode(const QString &id, QSvgNode *node)
    self.uglySide.call(
        'ritual_ZN12QSvgDocument12addNamedNodeERK7QStringP8QSvgNode',
        id, self._addressOf(node),
    )

  def restartAnimation(self) -> None:
    """
    Calls Qt's 'void QSvgDocument::restartAnimation()'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgdocument.html#restartAnimation
    """
    #  void QSvgDocument::restartAnimation()
    self.uglySide.call('ritual_ZN12QSvgDocument16restartAnimationEv')

  @overload(QPainter, QRectF)
  @overload(NoneType, QRectF)
  @overload(QPainter, QRectF, QRectF)
  @overload(NoneType, QRectF, QRectF)
  def mapSourceToTarget(
      self,
      p: Optional[QPainter],
      targetRect: QRectF,
      sourceRect: Optional[QRectF] = None,
  ) -> None:
    """
    Calls Qt's 'void QSvgDocument::mapSourceToTarget(QPainter *p, const
    QRectF &targetRect, const QRectF &sourceRect)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsvgdocument.html#mapSourceToTarget

    Parameters
    ----------

    p : Optional[QPainter]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    targetRect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    sourceRect : Optional[QRectF]
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own. May be left out, as in Qt: a new 'QRectF()' is then passed on.
    """
    #  void QSvgDocument::mapSourceToTarget(QPainter *p, const QRectF
    #      &targetRect, const QRectF &sourceRect)
    if sourceRect is None:
      from ..QtCore import QRectF
      sourceRect = QRectF()
    self.uglySide.call(
        'ritual_ZN12QSvgDocument17mapSourceToTargetEP8QPainterRK6QRectFS4_',
        self._addressOf(p), self._valueOf(targetRect),
        self._valueOf(sourceRect),
    )

  @staticmethod
  def addPaintServer(*__, **_) -> Never:
    """
    Qt's 'void QSvgDocument::addPaintServer(QSvgPaintServerSharedPtr
    paintServer, const QString &id)': takes a type Python has no way to hand
    over yet.
    """
    raise NotImplementedError(
        "'QSvgDocument.addPaintServer' has no cute function yet. Qt's 'void "
        "QSvgDocument::addPaintServer(QSvgPaintServerSharedPtr paintServer, "
        "const QString &id)': takes a type Python has no way to hand over "
        "yet.")

  @staticmethod
  def addSvgFont(*__, **_) -> Never:
    """
    Qt's 'void QSvgDocument::addSvgFont(const QString &name, QSvgFontPtr
    font)': the compiler refuses its ritual as it would be written here: call
    to deleted constructor of 'QSvgFontPtr' (aka
    'std::unique_ptr<QSvgFont>').
    """
    raise NotImplementedError(
        "'QSvgDocument.addSvgFont' has no cute function yet. Qt's 'void "
        "QSvgDocument::addSvgFont(const QString &name, QSvgFontPtr font)': "
        "the compiler refuses its ritual as it would be written here: call "
        "to deleted constructor of 'QSvgFontPtr' (aka "
        "'std::unique_ptr<QSvgFont>').")

  @staticmethod
  def animator(*__, **_) -> Never:
    """
    Qt's 'QSharedPointer<QSvgAbstractAnimator> QSvgDocument::animator()
    const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QSvgDocument.animator' has no cute function yet. Qt's "
        "'QSharedPointer<QSvgAbstractAnimator> QSvgDocument::animator() "
        "const': gives a type Python has no way to take yet.")

  @staticmethod
  def isLikelySvg(*__, **_) -> Never:
    """
    Qt's 'bool QSvgDocument::isLikelySvg(QIODevice *device, bool
    *isCompressed)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QSvgDocument.isLikelySvg' has no cute function yet. Qt's 'bool "
        "QSvgDocument::isLikelySvg(QIODevice *device, bool *isCompressed)': "
        "takes a number to change where it is.")

  @staticmethod
  def load(*__, **_) -> Never:
    """
    - Qt's 'std::unique_ptr<QSvgDocument> QSvgDocument::load(const QString
      &file, QtSvg::Options options, QtSvg::AnimatorType type)': gives a type
      Python has no way to take yet.
    - Qt's 'std::unique_ptr<QSvgDocument> QSvgDocument::load(const QByteArray
      &contents, QtSvg::Options options, QtSvg::AnimatorType type)': gives a
      type Python has no way to take yet.
    - Qt's 'std::unique_ptr<QSvgDocument> QSvgDocument::load(QXmlStreamReader
      *contents, QtSvg::Options options, QtSvg::AnimatorType type)': gives a
      type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QSvgDocument.load' has no cute function yet. Qt's "
        "'std::unique_ptr<QSvgDocument> QSvgDocument::load(const QString "
        "&file, QtSvg::Options options, QtSvg::AnimatorType type)': gives a "
        "type Python has no way to take yet. Qt's "
        "'std::unique_ptr<QSvgDocument> QSvgDocument::load(const QByteArray "
        "&contents, QtSvg::Options options, QtSvg::AnimatorType type)': "
        "gives a type Python has no way to take yet. Qt's "
        "'std::unique_ptr<QSvgDocument> QSvgDocument::load(QXmlStreamReader "
        "*contents, QtSvg::Options options, QtSvg::AnimatorType type)': "
        "gives a type Python has no way to take yet.")

  @staticmethod
  def paintServer(*__, **_) -> Never:
    """
    Qt's 'QSvgPaintServerSharedPtr QSvgDocument::paintServer(QStringView id)
    const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QSvgDocument.paintServer' has no cute function yet. Qt's "
        "'QSvgPaintServerSharedPtr QSvgDocument::paintServer(QStringView "
        "id) const': gives a type Python has no way to take yet.")
