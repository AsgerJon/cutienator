"""
QBrush binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of QtGui/qbrush.h,
#  Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import Qt

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QColor, QGradient, QImage, QPixmap, QTransform
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QColor = WAIT['QColor']
  QGradient = WAIT['QGradient']
  QImage = WAIT['QImage']
  QPixmap = WAIT['QPixmap']
  QTransform = WAIT['QTransform']


class QBrush(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QBrush: a plain Python object standing in front of
  one C++ QBrush.

  C++ hands a QBrush around as a copy, so every C++ QBrush behind a cute one
  is Python's own: it is removed, by the ritual named in '__delete_ritual__',
  when the cute object goes.

  What exists
  -----------

  Every function of Qt's QBrush that has a ritual and that Python can call so
  far, 13 names in all: 'style', 'setStyle', 'transform', 'setTransform',
  'texture', 'setTexture', 'textureImage', 'setTextureImage', 'color',
  'setColor', 'gradient', 'isOpaque', 'isDetached'. It can be made from
  Python, in 10 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QBrush::~QBrush()': the destructor: Python removes its C++ QBrush
    by it, and has no other use for it.
  - Qt's 'QVariant QBrush::operator QVariant() const': an operator, which is
    not reflected yet.
  - Qt's 'bool QBrush::operator==(const QBrush &b) const': an operator, which
    is not reflected yet.
  - Qt's 'bool QBrush::operator!=(const QBrush &b) const': an operator, which
    is not reflected yet.

  What has no ritual
  ------------------

  11 of the 39 functions Qt declares: 7 takes or gives a type that cannot be
  passed yet; 4 private.

  What to expect
  --------------

  - The C++ QBrush is created at the first use, not by 'QBrush(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QBrush back gives a copy the ritual made for Python,
    in a new cute QBrush.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QBrush'

  #  Qt's '~QBrush()'. Naming it makes this a value class: Python owns every
  #  C++ QBrush behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN6QBrushD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def style(self) -> Qt.BrushStyle:
    """
    Calls Qt's 'Qt::BrushStyle QBrush::style() const'.

    Qt's own words: https://doc.qt.io/qt-6/qbrush.html#style

    Returns
    -------

    Qt.BrushStyle
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Qt.BrushStyle(number)'
      gives.
    """
    #  Qt::BrushStyle QBrush::style() const
    return Qt.BrushStyle(self.uglySide.call('ritual_ZNK6QBrush5styleEv'))

  def transform(self) -> QTransform:
    """
    Calls Qt's 'QTransform QBrush::transform() const'.

    Qt's own words: https://doc.qt.io/qt-6/qbrush.html#transform

    Returns
    -------

    QTransform
      A new cute QTransform around the copy Qt gave back. Python owns it.
    """
    #  QTransform QBrush::transform() const
    address = self.uglySide.call('ritual_ZNK6QBrush9transformEv')
    from . import QTransform
    return QTransform._cuteOwning(address)

  def texture(self) -> QPixmap:
    """
    Calls Qt's 'QPixmap QBrush::texture() const'.

    Qt's own words: https://doc.qt.io/qt-6/qbrush.html#texture

    Returns
    -------

    QPixmap
      A new cute QPixmap around the copy Qt gave back. Python owns it.
    """
    #  QPixmap QBrush::texture() const
    address = self.uglySide.call('ritual_ZNK6QBrush7textureEv')
    from . import QPixmap
    return QPixmap._cuteOwning(address)

  def textureImage(self) -> QImage:
    """
    Calls Qt's 'QImage QBrush::textureImage() const'.

    Qt's own words: https://doc.qt.io/qt-6/qbrush.html#textureImage

    Returns
    -------

    QImage
      A new cute QImage around the copy Qt gave back. Python owns it.
    """
    #  QImage QBrush::textureImage() const
    address = self.uglySide.call('ritual_ZNK6QBrush12textureImageEv')
    from . import QImage
    return QImage._cuteOwning(address)

  def color(self) -> QColor:
    """
    Calls Qt's 'const QColor &QBrush::color() const'.

    Qt's own words: https://doc.qt.io/qt-6/qbrush.html#color

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  const QColor &QBrush::color() const
    address = self.uglySide.call('ritual_ZNK6QBrush5colorEv')
    from . import QColor
    return QColor._cuteOwning(address)

  def gradient(self) -> Optional[QGradient]:
    """
    Calls Qt's 'const QGradient *QBrush::gradient() const'.

    Qt's own words: https://doc.qt.io/qt-6/qbrush.html#gradient

    Returns
    -------

    Optional[QGradient]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QGradient *QBrush::gradient() const
    address = self.uglySide.call('ritual_ZNK6QBrush8gradientEv')
    from . import QGradient
    return QGradient._cuteAt(address)

  def isOpaque(self) -> bool:
    """
    Calls Qt's 'bool QBrush::isOpaque() const'.

    Qt's own words: https://doc.qt.io/qt-6/qbrush.html#isOpaque
    """
    #  bool QBrush::isOpaque() const
    return self.uglySide.call('ritual_ZNK6QBrush8isOpaqueEv')

  def isDetached(self) -> bool:
    """
    Calls Qt's 'bool QBrush::isDetached() const'.

    Qt's own words: https://doc.qt.io/qt-6/qbrush.html#isDetached
    """
    #  bool QBrush::isDetached() const
    return self.uglySide.call('ritual_ZNK6QBrush10isDetachedEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(Qt.BrushStyle)
  def setStyle(self, a0: Qt.BrushStyle) -> None:
    """
    Calls Qt's 'void QBrush::setStyle(Qt::BrushStyle a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qbrush.html#setStyle

    Parameters
    ----------

    a0 : Qt.BrushStyle
      Passed on as its number.
    """
    #  void QBrush::setStyle(Qt::BrushStyle a0)
    self.uglySide.call(
        'ritual_ZN6QBrush8setStyleEN2Qt10BrushStyleE', a0.value,
    )

  @overload(QTransform)
  def setTransform(self, a0: QTransform) -> None:
    """
    Calls Qt's 'void QBrush::setTransform(const QTransform &a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qbrush.html#setTransform

    Parameters
    ----------

    a0 : QTransform
      Passed on as a value: Qt reads the C++ QTransform, which stays Python's
      own.
    """
    #  void QBrush::setTransform(const QTransform &a0)
    self.uglySide.call(
        'ritual_ZN6QBrush12setTransformERK10QTransform', self._valueOf(a0),
    )

  @overload(QPixmap)
  def setTexture(self, pixmap: QPixmap) -> None:
    """
    Calls Qt's 'void QBrush::setTexture(const QPixmap &pixmap)'.

    Qt's own words: https://doc.qt.io/qt-6/qbrush.html#setTexture

    Parameters
    ----------

    pixmap : QPixmap
      Passed on as a value: Qt reads the C++ QPixmap, which stays Python's
      own.
    """
    #  void QBrush::setTexture(const QPixmap &pixmap)
    self.uglySide.call(
        'ritual_ZN6QBrush10setTextureERK7QPixmap', self._valueOf(pixmap),
    )

  @overload(QImage)
  def setTextureImage(self, image: QImage) -> None:
    """
    Calls Qt's 'void QBrush::setTextureImage(const QImage &image)'.

    Qt's own words: https://doc.qt.io/qt-6/qbrush.html#setTextureImage

    Parameters
    ----------

    image : QImage
      Passed on as a value: Qt reads the C++ QImage, which stays Python's
      own.
    """
    #  void QBrush::setTextureImage(const QImage &image)
    self.uglySide.call(
        'ritual_ZN6QBrush15setTextureImageERK6QImage', self._valueOf(image),
    )

  @overload(QColor)
  def setColor(self, color: QColor) -> None:
    """
    Calls Qt's 'void QBrush::setColor(const QColor &color)'.

    Qt's own words: https://doc.qt.io/qt-6/qbrush.html#setColor

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QBrush::setColor(const QColor &color)
    self.uglySide.call(
        'ritual_ZN6QBrush8setColorERK6QColor', self._valueOf(color),
    )

  @overload(Qt.GlobalColor)
  def setColor(self, color: Qt.GlobalColor) -> None:
    """
    Calls Qt's 'void QBrush::setColor(Qt::GlobalColor color)'.

    Qt's own words: https://doc.qt.io/qt-6/qbrush.html#setColor

    Parameters
    ----------

    color : Qt.GlobalColor
      Passed on as its number.
    """
    #  void QBrush::setColor(Qt::GlobalColor color)
    self.uglySide.call(
        'ritual_ZN6QBrush8setColorEN2Qt11GlobalColorE', color.value,
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
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'QBrush::QBrush()', which is called at the
    first use.

    Qt's own words: https://doc.qt.io/qt-6/qbrush.html#QBrush
    """
    #  QBrush::QBrush()
    self._noteCreation(QBrush, lambda: Rituals.call('ritual_ZN6QBrushC1Ev'))

  @overload(Qt.BrushStyle)
  def __init__(self, bs: Qt.BrushStyle) -> None:
    """
    Notes what was given, for Qt's 'QBrush::QBrush(Qt::BrushStyle bs)', which
    is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qbrush.html#QBrush

    Parameters
    ----------

    bs : Qt.BrushStyle
      Passed on as its number.
    """
    #  QBrush::QBrush(Qt::BrushStyle bs)
    self._noteCreation(QBrush, lambda: Rituals.call(
        'ritual_ZN6QBrushC1EN2Qt10BrushStyleE', bs.value,
    ))

  @overload(QColor)
  @overload(QColor, Qt.BrushStyle)
  def __init__(
      self,
      color: QColor,
      bs: Qt.BrushStyle = Qt.BrushStyle.SolidPattern,
  ) -> None:
    """
    Notes what was given, for Qt's 'QBrush::QBrush(const QColor &color,
    Qt::BrushStyle bs)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qbrush.html#QBrush

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.

    bs : Qt.BrushStyle
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.BrushStyle.SolidPattern.
    """
    #  QBrush::QBrush(const QColor &color, Qt::BrushStyle bs)
    self._noteCreation(QBrush, lambda: Rituals.call(
        'ritual_ZN6QBrushC1ERK6QColorN2Qt10BrushStyleE',
        self._valueOf(color), bs.value,
    ))

  @overload(Qt.GlobalColor)
  @overload(Qt.GlobalColor, Qt.BrushStyle)
  def __init__(
      self,
      color: Qt.GlobalColor,
      bs: Qt.BrushStyle = Qt.BrushStyle.SolidPattern,
  ) -> None:
    """
    Notes what was given, for Qt's 'QBrush::QBrush(Qt::GlobalColor color,
    Qt::BrushStyle bs)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qbrush.html#QBrush

    Parameters
    ----------

    color : Qt.GlobalColor
      Passed on as its number.

    bs : Qt.BrushStyle
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.BrushStyle.SolidPattern.
    """
    #  QBrush::QBrush(Qt::GlobalColor color, Qt::BrushStyle bs)
    self._noteCreation(QBrush, lambda: Rituals.call(
        'ritual_ZN6QBrushC1EN2Qt11GlobalColorENS0_10BrushStyleE',
        color.value, bs.value,
    ))

  @overload(QColor, QPixmap)
  def __init__(self, color: QColor, pixmap: QPixmap) -> None:
    """
    Notes what was given, for Qt's 'QBrush::QBrush(const QColor &color, const
    QPixmap &pixmap)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qbrush.html#QBrush

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.

    pixmap : QPixmap
      Passed on as a value: Qt reads the C++ QPixmap, which stays Python's
      own.
    """
    #  QBrush::QBrush(const QColor &color, const QPixmap &pixmap)
    self._noteCreation(QBrush, lambda: Rituals.call(
        'ritual_ZN6QBrushC1ERK6QColorRK7QPixmap',
        self._valueOf(color), self._valueOf(pixmap),
    ))

  @overload(Qt.GlobalColor, QPixmap)
  def __init__(self, color: Qt.GlobalColor, pixmap: QPixmap) -> None:
    """
    Notes what was given, for Qt's 'QBrush::QBrush(Qt::GlobalColor color,
    const QPixmap &pixmap)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qbrush.html#QBrush

    Parameters
    ----------

    color : Qt.GlobalColor
      Passed on as its number.

    pixmap : QPixmap
      Passed on as a value: Qt reads the C++ QPixmap, which stays Python's
      own.
    """
    #  QBrush::QBrush(Qt::GlobalColor color, const QPixmap &pixmap)
    self._noteCreation(QBrush, lambda: Rituals.call(
        'ritual_ZN6QBrushC1EN2Qt11GlobalColorERK7QPixmap',
        color.value, self._valueOf(pixmap),
    ))

  @overload(QPixmap)
  def __init__(self, pixmap: QPixmap) -> None:
    """
    Notes what was given, for Qt's 'QBrush::QBrush(const QPixmap &pixmap)',
    which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qbrush.html#QBrush

    Parameters
    ----------

    pixmap : QPixmap
      Passed on as a value: Qt reads the C++ QPixmap, which stays Python's
      own.
    """
    #  QBrush::QBrush(const QPixmap &pixmap)
    self._noteCreation(QBrush, lambda: Rituals.call(
        'ritual_ZN6QBrushC1ERK7QPixmap', self._valueOf(pixmap),
    ))

  @overload(QImage)
  def __init__(self, image: QImage) -> None:
    """
    Notes what was given, for Qt's 'QBrush::QBrush(const QImage &image)',
    which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qbrush.html#QBrush

    Parameters
    ----------

    image : QImage
      Passed on as a value: Qt reads the C++ QImage, which stays Python's
      own.
    """
    #  QBrush::QBrush(const QImage &image)
    self._noteCreation(QBrush, lambda: Rituals.call(
        'ritual_ZN6QBrushC1ERK6QImage', self._valueOf(image),
    ))

  @overload(THIS)
  def __init__(self, brush: QBrush) -> None:
    """
    Notes what was given, for Qt's 'QBrush::QBrush(const QBrush &brush)',
    which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qbrush.html#QBrush

    Parameters
    ----------

    brush : QBrush
      Passed on as a value: Qt reads the C++ QBrush, which stays Python's
      own.
    """
    #  QBrush::QBrush(const QBrush &brush)
    self._noteCreation(QBrush, lambda: Rituals.call(
        'ritual_ZN6QBrushC1ERKS_', self._valueOf(brush),
    ))

  @overload(QGradient)
  def __init__(self, gradient: QGradient) -> None:
    """
    Notes what was given, for Qt's 'QBrush::QBrush(const QGradient
    &gradient)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qbrush.html#QBrush

    Parameters
    ----------

    gradient : QGradient
      Passed on as a value: Qt reads the C++ QGradient, which stays Python's
      own.
    """
    #  QBrush::QBrush(const QGradient &gradient)
    self._noteCreation(QBrush, lambda: Rituals.call(
        'ritual_ZN6QBrushC1ERK9QGradient', self._valueOf(gradient),
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
