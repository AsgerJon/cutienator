"""
QTextImageFormat binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/qtextformat.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from . import QTextCharFormat

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from . import QTextLength
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QTextLength = WAIT['QTextLength']


class QTextImageFormat(QTextCharFormat):
  """
  The cute side of Qt's QTextImageFormat: a plain Python object standing in
  front of one C++ QTextImageFormat.

  It is built on the cute 'QTextCharFormat', as Qt's QTextImageFormat is
  built on Qt's QTextCharFormat, and has everything that class has.

  C++ hands a QTextImageFormat around as a copy, so every C++
  QTextImageFormat behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QTextImageFormat that has a ritual and that Python
  can call so far, 11 names in all: 'isValid', 'setName', 'name', 'setWidth',
  'width', 'setMaximumWidth', 'maximumWidth', 'setHeight', 'height',
  'setQuality', 'quality'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QTextImageFormat::~QTextImageFormat()': the destructor: Python
    removes its C++ QTextImageFormat by it, and has no other use for it.

  What has no ritual
  ------------------

  1 of the 15 functions Qt declares: 1 protected.

  What to expect
  --------------

  - The C++ QTextImageFormat is created at the first use, not by
    'QTextImageFormat(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QTextImageFormat back gives a copy the ritual made
    for Python, in a new cute QTextImageFormat.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QTextImageFormat'

  #  Qt's '~QTextImageFormat()'. Naming it makes this a value class: Python
  #  owns every C++ QTextImageFormat behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN16QTextImageFormatD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool QTextImageFormat::isValid() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextimageformat.html#isValid
    """
    #  bool QTextImageFormat::isValid() const
    return self.uglySide.call('ritual_ZNK16QTextImageFormat7isValidEv')

  def name(self) -> str:
    """
    Calls Qt's 'QString QTextImageFormat::name() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextimageformat.html#name

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QTextImageFormat::name() const
    return self.uglySide.call('ritual_ZNK16QTextImageFormat4nameEv')

  def width(self) -> float:
    """
    Calls Qt's 'qreal QTextImageFormat::width() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextimageformat.html#width
    """
    #  qreal QTextImageFormat::width() const
    return self.uglySide.call('ritual_ZNK16QTextImageFormat5widthEv')

  def maximumWidth(self) -> QTextLength:
    """
    Calls Qt's 'QTextLength QTextImageFormat::maximumWidth() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextimageformat.html#maximumWidth

    Returns
    -------

    QTextLength
      A new cute QTextLength around the copy Qt gave back. Python owns it.
    """
    #  QTextLength QTextImageFormat::maximumWidth() const
    address = self.uglySide.call(
        'ritual_ZNK16QTextImageFormat12maximumWidthEv',
    )
    from . import QTextLength
    return QTextLength._cuteOwning(address)

  def height(self) -> float:
    """
    Calls Qt's 'qreal QTextImageFormat::height() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextimageformat.html#height
    """
    #  qreal QTextImageFormat::height() const
    return self.uglySide.call('ritual_ZNK16QTextImageFormat6heightEv')

  def quality(self) -> int:
    """
    Calls Qt's 'int QTextImageFormat::quality() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextimageformat.html#quality
    """
    #  int QTextImageFormat::quality() const
    return self.uglySide.call('ritual_ZNK16QTextImageFormat7qualityEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setName(self, name: str) -> None:
    """
    Calls Qt's 'void QTextImageFormat::setName(const QString &name)'.

    Qt's own words: https://doc.qt.io/qt-6/qtextimageformat.html#setName

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QTextImageFormat::setName(const QString &name)
    self.uglySide.call(
        'ritual_ZN16QTextImageFormat7setNameERK7QString', name,
    )

  @overload(float)
  def setWidth(self, width: float) -> None:
    """
    Calls Qt's 'void QTextImageFormat::setWidth(qreal width)'.

    Qt's own words: https://doc.qt.io/qt-6/qtextimageformat.html#setWidth

    Parameters
    ----------

    width : float
      Passed on as it is.
    """
    #  void QTextImageFormat::setWidth(qreal width)
    self.uglySide.call('ritual_ZN16QTextImageFormat8setWidthEd', width)

  @overload(QTextLength)
  def setMaximumWidth(self, maxWidth: QTextLength) -> None:
    """
    Calls Qt's 'void QTextImageFormat::setMaximumWidth(QTextLength
    maxWidth)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextimageformat.html#setMaximumWidth

    Parameters
    ----------

    maxWidth : QTextLength
      Passed on as a value: Qt reads the C++ QTextLength, which stays
      Python's own.
    """
    #  void QTextImageFormat::setMaximumWidth(QTextLength maxWidth)
    self.uglySide.call(
        'ritual_ZN16QTextImageFormat15setMaximumWidthE11QTextLength',
        self._valueOf(maxWidth),
    )

  @overload(float)
  def setHeight(self, height: float) -> None:
    """
    Calls Qt's 'void QTextImageFormat::setHeight(qreal height)'.

    Qt's own words: https://doc.qt.io/qt-6/qtextimageformat.html#setHeight

    Parameters
    ----------

    height : float
      Passed on as it is.
    """
    #  void QTextImageFormat::setHeight(qreal height)
    self.uglySide.call('ritual_ZN16QTextImageFormat9setHeightEd', height)

  @overload(int)
  def setQuality(self, quality: int) -> None:
    """
    Calls Qt's 'void QTextImageFormat::setQuality(int quality)'.

    Qt's own words: https://doc.qt.io/qt-6/qtextimageformat.html#setQuality

    Parameters
    ----------

    quality : int
      Passed on as it is.
    """
    #  void QTextImageFormat::setQuality(int quality)
    self.uglySide.call('ritual_ZN16QTextImageFormat10setQualityEi', quality)

  @overload()
  def setQuality(self) -> None:
    """
    Calls Qt's 'void QTextImageFormat::setQuality()'.

    Qt's own words: https://doc.qt.io/qt-6/qtextimageformat.html#setQuality
    """
    #  void QTextImageFormat::setQuality()
    self.uglySide.call('ritual_ZN16QTextImageFormat10setQualityEv')

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
    Notes what was given, for Qt's 'QTextImageFormat::QTextImageFormat()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextimageformat.html#QTextImageFormat
    """
    #  QTextImageFormat::QTextImageFormat()
    self._noteCreation(QTextImageFormat, lambda: Rituals.call(
        'ritual_ZN16QTextImageFormatC1Ev',
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
