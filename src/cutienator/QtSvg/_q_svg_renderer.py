"""
QSvgRenderer binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtSvg/qsvgrenderer.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import Qt, QObject
from . import QtSvg

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QByteArray, QMetaObject, QRect, QRectF, QSize
  from ..QtCore import QXmlStreamReader
  from ..QtGui import QPainter, QTransform
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']
  QPainter = WAIT['QPainter']
  QRect = WAIT['QRect']
  QRectF = WAIT['QRectF']
  QXmlStreamReader = WAIT['QXmlStreamReader']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSvgRenderer(QObject):
  """
  The cute side of Qt's QSvgRenderer: a plain Python object standing in front
  of one C++ QSvgRenderer.

  It is built on the cute 'QObject', as Qt's QSvgRenderer is built on Qt's
  QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QSvgRenderer that has a ritual and that Python can
  call so far, 26 names in all: 'metaObject', 'tr', 'isValid', 'defaultSize',
  'viewBox', 'viewBoxF', 'setViewBox', 'aspectRatioMode',
  'setAspectRatioMode', 'options', 'setOptions', 'animated',
  'framesPerSecond', 'setFramesPerSecond', 'currentFrame', 'setCurrentFrame',
  'animationDuration', 'isAnimationEnabled', 'setAnimationEnabled',
  'boundsOnElement', 'elementExists', 'transformForElement',
  'setDefaultOptions', 'load', 'render', 'repaintNeeded'. It can be made from
  Python, in 4 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QSvgRenderer::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QSvgRenderer::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QSvgRenderer::~QSvgRenderer()': the destructor: Python never
    removes a C++ QSvgRenderer.
  - Qt's 'QSvgRendererPrivate *QSvgRenderer::d_func()': gives
    'QSvgRendererPrivate', which has no cute class yet.
  - Qt's 'const QSvgRendererPrivate *QSvgRenderer::d_func() const': gives
    'QSvgRendererPrivate', which has no cute class yet.

  What has no ritual
  ------------------

  2 of the 42 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QSvgRenderer is created at the first use, not by
    'QSvgRenderer(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSvgRenderer.
  - Qt tells when it has removed the C++ QSvgRenderer. Every call on the cute
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
    Calls Qt's 'QString QSvgRenderer::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgrenderer.html#tr

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
    #  QString QSvgRenderer::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN12QSvgRenderer2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  @overload(QtSvg.Options)
  def setDefaultOptions(flags: QtSvg.Options) -> None:
    """
    Calls Qt's 'void QSvgRenderer::setDefaultOptions(QtSvg::Options flags)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsvgrenderer.html#setDefaultOptions

    Parameters
    ----------

    flags : QtSvg.Options
      Passed on as its number.
    """
    #  void QSvgRenderer::setDefaultOptions(QtSvg::Options flags)
    Rituals.call(
        'ritual_ZN12QSvgRenderer17setDefaultOptionsE6QFlagsIN5QtSvg6OptionE'
        'E',
        flags.value,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSvgRenderer'

  #  A C++ QSvgRenderer Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QSvgRenderer'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QSvgRenderer::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgrenderer.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QSvgRenderer::metaObject() const
    address = self.uglySide.call('ritual_ZNK12QSvgRenderer10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool QSvgRenderer::isValid() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgrenderer.html#isValid
    """
    #  bool QSvgRenderer::isValid() const
    return self.uglySide.call('ritual_ZNK12QSvgRenderer7isValidEv')

  def defaultSize(self) -> QSize:
    """
    Calls Qt's 'QSize QSvgRenderer::defaultSize() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgrenderer.html#defaultSize

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QSvgRenderer::defaultSize() const
    address = self.uglySide.call('ritual_ZNK12QSvgRenderer11defaultSizeEv')
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  def viewBox(self) -> QRect:
    """
    Calls Qt's 'QRect QSvgRenderer::viewBox() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgrenderer.html#viewBox

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect QSvgRenderer::viewBox() const
    address = self.uglySide.call('ritual_ZNK12QSvgRenderer7viewBoxEv')
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

  def viewBoxF(self) -> QRectF:
    """
    Calls Qt's 'QRectF QSvgRenderer::viewBoxF() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgrenderer.html#viewBoxF

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QSvgRenderer::viewBoxF() const
    address = self.uglySide.call('ritual_ZNK12QSvgRenderer8viewBoxFEv')
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  def aspectRatioMode(self) -> Qt.AspectRatioMode:
    """
    Calls Qt's 'Qt::AspectRatioMode QSvgRenderer::aspectRatioMode() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgrenderer.html#aspectRatioMode

    Returns
    -------

    Qt.AspectRatioMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'Qt.AspectRatioMode(number)' gives.
    """
    #  Qt::AspectRatioMode QSvgRenderer::aspectRatioMode() const
    return Qt.AspectRatioMode(self.uglySide.call(
        'ritual_ZNK12QSvgRenderer15aspectRatioModeEv',
    ))

  def options(self) -> QtSvg.Options:
    """
    Calls Qt's 'QtSvg::Options QSvgRenderer::options() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgrenderer.html#options

    Returns
    -------

    QtSvg.Options
      The value standing for the combination Qt gave back.
    """
    #  QtSvg::Options QSvgRenderer::options() const
    return QtSvg.Options(self.uglySide.call(
        'ritual_ZNK12QSvgRenderer7optionsEv',
    ))

  def animated(self) -> bool:
    """
    Calls Qt's 'bool QSvgRenderer::animated() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgrenderer.html#animated
    """
    #  bool QSvgRenderer::animated() const
    return self.uglySide.call('ritual_ZNK12QSvgRenderer8animatedEv')

  def framesPerSecond(self) -> int:
    """
    Calls Qt's 'int QSvgRenderer::framesPerSecond() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgrenderer.html#framesPerSecond
    """
    #  int QSvgRenderer::framesPerSecond() const
    return self.uglySide.call('ritual_ZNK12QSvgRenderer15framesPerSecondEv')

  def currentFrame(self) -> int:
    """
    Calls Qt's 'int QSvgRenderer::currentFrame() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgrenderer.html#currentFrame
    """
    #  int QSvgRenderer::currentFrame() const
    return self.uglySide.call('ritual_ZNK12QSvgRenderer12currentFrameEv')

  def animationDuration(self) -> int:
    """
    Calls Qt's 'int QSvgRenderer::animationDuration() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsvgrenderer.html#animationDuration
    """
    #  int QSvgRenderer::animationDuration() const
    return self.uglySide.call(
        'ritual_ZNK12QSvgRenderer17animationDurationEv',
    )

  def isAnimationEnabled(self) -> bool:
    """
    Calls Qt's 'bool QSvgRenderer::isAnimationEnabled() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsvgrenderer.html#isAnimationEnabled
    """
    #  bool QSvgRenderer::isAnimationEnabled() const
    return self.uglySide.call(
        'ritual_ZNK12QSvgRenderer18isAnimationEnabledEv',
    )

  @overload(str)
  def boundsOnElement(self, id: str) -> QRectF:
    """
    Calls Qt's 'QRectF QSvgRenderer::boundsOnElement(const QString &id)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgrenderer.html#boundsOnElement

    Parameters
    ----------

    id : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QSvgRenderer::boundsOnElement(const QString &id) const
    address = self.uglySide.call(
        'ritual_ZNK12QSvgRenderer15boundsOnElementERK7QString', id,
    )
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  @overload(str)
  def elementExists(self, id: str) -> bool:
    """
    Calls Qt's 'bool QSvgRenderer::elementExists(const QString &id) const'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgrenderer.html#elementExists

    Parameters
    ----------

    id : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QSvgRenderer::elementExists(const QString &id) const
    return self.uglySide.call(
        'ritual_ZNK12QSvgRenderer13elementExistsERK7QString', id,
    )

  @overload(str)
  def transformForElement(self, id: str) -> QTransform:
    """
    Calls Qt's 'QTransform QSvgRenderer::transformForElement(const QString
    &id) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsvgrenderer.html#transformForElement

    Parameters
    ----------

    id : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QTransform
      A new cute QTransform around the copy Qt gave back. Python owns it.
    """
    #  QTransform QSvgRenderer::transformForElement(const QString &id) const
    address = self.uglySide.call(
        'ritual_ZNK12QSvgRenderer19transformForElementERK7QString', id,
    )
    from ..QtGui import QTransform
    return QTransform._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QRect)
  def setViewBox(self, viewbox: QRect) -> None:
    """
    Calls Qt's 'void QSvgRenderer::setViewBox(const QRect &viewbox)'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgrenderer.html#setViewBox

    Parameters
    ----------

    viewbox : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.
    """
    #  void QSvgRenderer::setViewBox(const QRect &viewbox)
    self.uglySide.call(
        'ritual_ZN12QSvgRenderer10setViewBoxERK5QRect',
        self._valueOf(viewbox),
    )

  @overload(QRectF)
  def setViewBox(self, viewbox: QRectF) -> None:
    """
    Calls Qt's 'void QSvgRenderer::setViewBox(const QRectF &viewbox)'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgrenderer.html#setViewBox

    Parameters
    ----------

    viewbox : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void QSvgRenderer::setViewBox(const QRectF &viewbox)
    self.uglySide.call(
        'ritual_ZN12QSvgRenderer10setViewBoxERK6QRectF',
        self._valueOf(viewbox),
    )

  @overload(Qt.AspectRatioMode)
  def setAspectRatioMode(self, mode: Qt.AspectRatioMode) -> None:
    """
    Calls Qt's 'void QSvgRenderer::setAspectRatioMode(Qt::AspectRatioMode
    mode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsvgrenderer.html#setAspectRatioMode

    Parameters
    ----------

    mode : Qt.AspectRatioMode
      Passed on as its number.
    """
    #  void QSvgRenderer::setAspectRatioMode(Qt::AspectRatioMode mode)
    self.uglySide.call(
        'ritual_ZN12QSvgRenderer18setAspectRatioModeEN2Qt15AspectRatioModeE',
        mode.value,
    )

  @overload(QtSvg.Options)
  def setOptions(self, flags: QtSvg.Options) -> None:
    """
    Calls Qt's 'void QSvgRenderer::setOptions(QtSvg::Options flags)'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgrenderer.html#setOptions

    Parameters
    ----------

    flags : QtSvg.Options
      Passed on as its number.
    """
    #  void QSvgRenderer::setOptions(QtSvg::Options flags)
    self.uglySide.call(
        'ritual_ZN12QSvgRenderer10setOptionsE6QFlagsIN5QtSvg6OptionEE',
        flags.value,
    )

  @overload(int)
  def setFramesPerSecond(self, num: int) -> None:
    """
    Calls Qt's 'void QSvgRenderer::setFramesPerSecond(int num)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsvgrenderer.html#setFramesPerSecond

    Parameters
    ----------

    num : int
      Passed on as it is.
    """
    #  void QSvgRenderer::setFramesPerSecond(int num)
    self.uglySide.call('ritual_ZN12QSvgRenderer18setFramesPerSecondEi', num)

  @overload(int)
  def setCurrentFrame(self, a0: int) -> None:
    """
    Calls Qt's 'void QSvgRenderer::setCurrentFrame(int a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgrenderer.html#setCurrentFrame

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  void QSvgRenderer::setCurrentFrame(int a0)
    self.uglySide.call('ritual_ZN12QSvgRenderer15setCurrentFrameEi', a0)

  @overload(bool)
  def setAnimationEnabled(self, enable: bool) -> None:
    """
    Calls Qt's 'void QSvgRenderer::setAnimationEnabled(bool enable)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsvgrenderer.html#setAnimationEnabled

    Parameters
    ----------

    enable : bool
      Passed on as it is.
    """
    #  void QSvgRenderer::setAnimationEnabled(bool enable)
    self.uglySide.call(
        'ritual_ZN12QSvgRenderer19setAnimationEnabledEb', enable,
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

  @overload()
  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's 'QSvgRenderer::QSvgRenderer(QObject
    *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qsvgrenderer.html#QSvgRenderer

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QSvgRenderer::QSvgRenderer(QObject *parent)
    self._noteCreation(QSvgRenderer, lambda: Rituals.call(
        'ritual_ZN12QSvgRendererC1EP7QObject',
        self._addressOf(parent, 'QObject'),
    ))

  @overload(str)
  @overload(str, QObject)
  @overload(str, NoneType)
  def __init__(
      self,
      filename: str,
      parent: Optional[QObject] = None,
  ) -> None:
    """
    Notes what was given, for Qt's 'QSvgRenderer::QSvgRenderer(const QString
    &filename, QObject *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qsvgrenderer.html#QSvgRenderer

    Parameters
    ----------

    filename : str
      Passed on as it is: a QString is made of it for the call.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QSvgRenderer::QSvgRenderer(const QString &filename, QObject *parent)
    self._noteCreation(QSvgRenderer, lambda: Rituals.call(
        'ritual_ZN12QSvgRendererC1ERK7QStringP7QObject',
        filename, self._addressOf(parent, 'QObject'),
    ))

  @overload(QByteArray)
  @overload(QByteArray, QObject)
  @overload(QByteArray, NoneType)
  def __init__(
      self,
      contents: QByteArray,
      parent: Optional[QObject] = None,
  ) -> None:
    """
    Notes what was given, for Qt's 'QSvgRenderer::QSvgRenderer(const
    QByteArray &contents, QObject *parent)', which is called at the first
    use.

    Qt's own words: https://doc.qt.io/qt-6/qsvgrenderer.html#QSvgRenderer

    Parameters
    ----------

    contents : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QSvgRenderer::QSvgRenderer(const QByteArray &contents, QObject
    #      *parent)
    self._noteCreation(QSvgRenderer, lambda: Rituals.call(
        'ritual_ZN12QSvgRendererC1ERK10QByteArrayP7QObject',
        self._valueOf(contents), self._addressOf(parent, 'QObject'),
    ))

  @overload(QXmlStreamReader)
  @overload(QXmlStreamReader, QObject)
  @overload(QXmlStreamReader, NoneType)
  @overload(NoneType, QObject)
  @overload(NoneType, NoneType)
  def __init__(
      self,
      contents: Optional[QXmlStreamReader],
      parent: Optional[QObject] = None,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QSvgRenderer::QSvgRenderer(QXmlStreamReader *contents, QObject
    *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qsvgrenderer.html#QSvgRenderer

    Parameters
    ----------

    contents : Optional[QXmlStreamReader]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QSvgRenderer::QSvgRenderer(QXmlStreamReader *contents, QObject
    #      *parent)
    self._noteCreation(QSvgRenderer, lambda: Rituals.call(
        'ritual_ZN12QSvgRendererC1EP16QXmlStreamReaderP7QObject',
        self._addressOf(contents), self._addressOf(parent, 'QObject'),
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

  @overload(str)
  def load(self, filename: str) -> bool:
    """
    Calls Qt's 'bool QSvgRenderer::load(const QString &filename)'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgrenderer.html#load

    Parameters
    ----------

    filename : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QSvgRenderer::load(const QString &filename)
    return self.uglySide.call(
        'ritual_ZN12QSvgRenderer4loadERK7QString', filename,
    )

  @overload(QByteArray)
  def load(self, contents: QByteArray) -> bool:
    """
    Calls Qt's 'bool QSvgRenderer::load(const QByteArray &contents)'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgrenderer.html#load

    Parameters
    ----------

    contents : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  bool QSvgRenderer::load(const QByteArray &contents)
    return self.uglySide.call(
        'ritual_ZN12QSvgRenderer4loadERK10QByteArray',
        self._valueOf(contents),
    )

  @overload(QXmlStreamReader)
  @overload(NoneType)
  def load(self, contents: Optional[QXmlStreamReader]) -> bool:
    """
    Calls Qt's 'bool QSvgRenderer::load(QXmlStreamReader *contents)'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgrenderer.html#load

    Parameters
    ----------

    contents : Optional[QXmlStreamReader]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QSvgRenderer::load(QXmlStreamReader *contents)
    return self.uglySide.call(
        'ritual_ZN12QSvgRenderer4loadEP16QXmlStreamReader',
        self._addressOf(contents),
    )

  @overload(QPainter)
  @overload(NoneType)
  def render(self, p: Optional[QPainter]) -> None:
    """
    Calls Qt's 'void QSvgRenderer::render(QPainter *p)'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgrenderer.html#render

    Parameters
    ----------

    p : Optional[QPainter]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSvgRenderer::render(QPainter *p)
    self.uglySide.call(
        'ritual_ZN12QSvgRenderer6renderEP8QPainter', self._addressOf(p),
    )

  @overload(QPainter, QRectF)
  @overload(NoneType, QRectF)
  def render(self, p: Optional[QPainter], bounds: QRectF) -> None:
    """
    Calls Qt's 'void QSvgRenderer::render(QPainter *p, const QRectF
    &bounds)'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgrenderer.html#render

    Parameters
    ----------

    p : Optional[QPainter]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    bounds : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void QSvgRenderer::render(QPainter *p, const QRectF &bounds)
    self.uglySide.call(
        'ritual_ZN12QSvgRenderer6renderEP8QPainterRK6QRectF',
        self._addressOf(p), self._valueOf(bounds),
    )

  @overload(QPainter, str)
  @overload(NoneType, str)
  @overload(QPainter, str, QRectF)
  @overload(NoneType, str, QRectF)
  def render(
      self,
      p: Optional[QPainter],
      elementId: str,
      bounds: Optional[QRectF] = None,
  ) -> None:
    """
    Calls Qt's 'void QSvgRenderer::render(QPainter *p, const QString
    &elementId, const QRectF &bounds)'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgrenderer.html#render

    Parameters
    ----------

    p : Optional[QPainter]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    elementId : str
      Passed on as it is: a QString is made of it for the call.

    bounds : Optional[QRectF]
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own. May be left out, as in Qt: a new 'QRectF()' is then passed on.
    """
    #  void QSvgRenderer::render(QPainter *p, const QString &elementId, const
    #      QRectF &bounds)
    if bounds is None:
      from ..QtCore import QRectF
      bounds = QRectF()
    self.uglySide.call(
        'ritual_ZN12QSvgRenderer6renderEP8QPainterRK7QStringRK6QRectF',
        self._addressOf(p), elementId, self._valueOf(bounds),
    )

  def repaintNeeded(self) -> None:
    """
    Calls Qt's 'void QSvgRenderer::repaintNeeded()'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgrenderer.html#repaintNeeded
    """
    #  void QSvgRenderer::repaintNeeded()
    self.uglySide.call('ritual_ZN12QSvgRenderer13repaintNeededEv')
