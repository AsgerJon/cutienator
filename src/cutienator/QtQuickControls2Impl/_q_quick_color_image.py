"""
QQuickColorImage binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickControls2Impl/6.12.0/QtQuickControls2Impl/private/qquickcolorimage_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuickColorImage to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtQuick import QQuickImage, QQuickItem

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from ..QtGui import QColor
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QColor = WAIT['QColor']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickColorImage(QQuickImage):
  """
  The cute side of Qt's QQuickColorImage: a plain Python object standing in
  front of one C++ QQuickColorImage.

  It is built on the cute 'QQuickImage', as Qt's QQuickColorImage is built on
  Qt's QQuickImage, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickColorImage that has a ritual and that Python
  can call so far, 11 names in all: 'metaObject', 'tr', 'color', 'setColor',
  'resetColor', 'defaultColor', 'setDefaultColor', 'resetDefaultColor',
  'colorChanged', 'defaultColorChanged', 'pixmapChange'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickColorImage::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QQuickColorImage::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.

  What has no ritual
  ------------------

  2 of the 16 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuickColorImage is created at the first use, not by
    'QQuickColorImage(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickColorImage.
  - Qt tells when it has removed the C++ QQuickColorImage. Every call on the
    cute object, and every use of it as an argument, then raises
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
    Calls Qt's 'QString QQuickColorImage::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcolorimage.html#tr

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
    #  QString QQuickColorImage::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN16QQuickColorImage2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickColorImage'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickColorImage::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcolorimage.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickColorImage::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK16QQuickColorImage10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def color(self) -> QColor:
    """
    Calls Qt's 'QColor QQuickColorImage::color() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcolorimage.html#color

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QQuickColorImage::color() const
    address = self.uglySide.call('ritual_ZNK16QQuickColorImage5colorEv')
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def defaultColor(self) -> QColor:
    """
    Calls Qt's 'QColor QQuickColorImage::defaultColor() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcolorimage.html#defaultColor

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QQuickColorImage::defaultColor() const
    address = self.uglySide.call(
        'ritual_ZNK16QQuickColorImage12defaultColorEv',
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QColor)
  def setColor(self, color: QColor) -> None:
    """
    Calls Qt's 'void QQuickColorImage::setColor(const QColor &color)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcolorimage.html#setColor

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QQuickColorImage::setColor(const QColor &color)
    self.uglySide.call(
        'ritual_ZN16QQuickColorImage8setColorERK6QColor',
        self._valueOf(color),
    )

  @overload(QColor)
  def setDefaultColor(self, color: QColor) -> None:
    """
    Calls Qt's 'void QQuickColorImage::setDefaultColor(const QColor &color)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcolorimage.html#setDefaultColor

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QQuickColorImage::setDefaultColor(const QColor &color)
    self.uglySide.call(
        'ritual_ZN16QQuickColorImage15setDefaultColorERK6QColor',
        self._valueOf(color),
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
  @overload(QQuickItem)
  @overload(NoneType)
  def __init__(self, parent: Optional[QQuickItem] = None) -> None:
    """
    Notes what was given, for Qt's
    'QQuickColorImage::QQuickColorImage(QQuickItem *parent)', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcolorimage.html#QQuickColorImage

    Parameters
    ----------

    parent : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickColorImage::QQuickColorImage(QQuickItem *parent)
    self._noteCreation(QQuickColorImage, lambda: Rituals.call(
        'ritual_ZN16QQuickColorImageC1EP10QQuickItem',
        self._addressOf(parent),
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

  def resetColor(self) -> None:
    """
    Calls Qt's 'void QQuickColorImage::resetColor()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcolorimage.html#resetColor
    """
    #  void QQuickColorImage::resetColor()
    self.uglySide.call('ritual_ZN16QQuickColorImage10resetColorEv')

  def resetDefaultColor(self) -> None:
    """
    Calls Qt's 'void QQuickColorImage::resetDefaultColor()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcolorimage.html#resetDefaultColor
    """
    #  void QQuickColorImage::resetDefaultColor()
    self.uglySide.call('ritual_ZN16QQuickColorImage17resetDefaultColorEv')

  def colorChanged(self) -> None:
    """
    Calls Qt's 'void QQuickColorImage::colorChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcolorimage.html#colorChanged
    """
    #  void QQuickColorImage::colorChanged()
    self.uglySide.call('ritual_ZN16QQuickColorImage12colorChangedEv')

  def defaultColorChanged(self) -> None:
    """
    Calls Qt's 'void QQuickColorImage::defaultColorChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcolorimage.html#defaultColorChanged
    """
    #  void QQuickColorImage::defaultColorChanged()
    self.uglySide.call('ritual_ZN16QQuickColorImage19defaultColorChangedEv')

  def pixmapChange(self) -> None:
    """
    Calls Qt's 'void QQuickColorImage::pixmapChange()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcolorimage.html#pixmapChange
    """
    #  void QQuickColorImage::pixmapChange()
    ritual = 'ritual_ZN16QQuickColorImage12pixmapChangeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN16QQuickColorImage12pixmapChangeEv'
    self.uglySide.call(ritual)
