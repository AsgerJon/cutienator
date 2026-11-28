"""
QQuickPen binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquickrectangle_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QQuickPen to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject

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


class QQuickPen(QObject):
  """
  The cute side of Qt's QQuickPen: a plain Python object standing in front of
  one C++ QQuickPen.

  It is built on the cute 'QObject', as Qt's QQuickPen is built on Qt's
  QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickPen that has a ritual and that Python can call
  so far, 12 names in all: 'metaObject', 'tr', 'width', 'setWidth', 'color',
  'setColor', 'pixelAligned', 'setPixelAligned', 'isValid', 'widthChanged',
  'colorChanged', 'pixelAlignedChanged'. It can be made from Python, in 1
  way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickPen::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QQuickPen::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'void QQuickPen::qt_qmlMarker_anonymous()': one of Qt's own inner
    workings.

  What has no ritual
  ------------------

  2 of the 18 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuickPen is created at the first use, not by 'QQuickPen(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickPen.
  - Qt tells when it has removed the C++ QQuickPen. Every call on the cute
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
    Calls Qt's 'QString QQuickPen::tr(const char *s, const char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpen.html#tr

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
    #  QString QQuickPen::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN9QQuickPen2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickPen'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickPen::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpen.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickPen::metaObject() const
    address = self.uglySide.call('ritual_ZNK9QQuickPen10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def width(self) -> float:
    """
    Calls Qt's 'qreal QQuickPen::width() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpen.html#width
    """
    #  qreal QQuickPen::width() const
    return self.uglySide.call('ritual_ZNK9QQuickPen5widthEv')

  def color(self) -> QColor:
    """
    Calls Qt's 'QColor QQuickPen::color() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpen.html#color

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QQuickPen::color() const
    address = self.uglySide.call('ritual_ZNK9QQuickPen5colorEv')
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def pixelAligned(self) -> bool:
    """
    Calls Qt's 'bool QQuickPen::pixelAligned() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpen.html#pixelAligned
    """
    #  bool QQuickPen::pixelAligned() const
    return self.uglySide.call('ritual_ZNK9QQuickPen12pixelAlignedEv')

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool QQuickPen::isValid() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpen.html#isValid
    """
    #  bool QQuickPen::isValid() const
    return self.uglySide.call('ritual_ZNK9QQuickPen7isValidEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float)
  def setWidth(self, w: float) -> None:
    """
    Calls Qt's 'void QQuickPen::setWidth(qreal w)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpen.html#setWidth

    Parameters
    ----------

    w : float
      Passed on as it is.
    """
    #  void QQuickPen::setWidth(qreal w)
    self.uglySide.call('ritual_ZN9QQuickPen8setWidthEd', w)

  @overload(QColor)
  def setColor(self, c: QColor) -> None:
    """
    Calls Qt's 'void QQuickPen::setColor(const QColor &c)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpen.html#setColor

    Parameters
    ----------

    c : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QQuickPen::setColor(const QColor &c)
    self.uglySide.call(
        'ritual_ZN9QQuickPen8setColorERK6QColor', self._valueOf(c),
    )

  @overload(bool)
  def setPixelAligned(self, aligned: bool) -> None:
    """
    Calls Qt's 'void QQuickPen::setPixelAligned(bool aligned)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpen.html#setPixelAligned

    Parameters
    ----------

    aligned : bool
      Passed on as it is.
    """
    #  void QQuickPen::setPixelAligned(bool aligned)
    self.uglySide.call('ritual_ZN9QQuickPen15setPixelAlignedEb', aligned)

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
    Notes what was given, for Qt's 'QQuickPen::QQuickPen(QObject *parent)',
    which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qquickpen.html#QQuickPen

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickPen::QQuickPen(QObject *parent)
    self._noteCreation(QQuickPen, lambda: Rituals.call(
        'ritual_ZN9QQuickPenC1EP7QObject',
        self._addressOf(parent, 'QObject'),
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

  def widthChanged(self) -> None:
    """
    Calls Qt's 'void QQuickPen::widthChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpen.html#widthChanged
    """
    #  void QQuickPen::widthChanged()
    self.uglySide.call('ritual_ZN9QQuickPen12widthChangedEv')

  def colorChanged(self) -> None:
    """
    Calls Qt's 'void QQuickPen::colorChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpen.html#colorChanged
    """
    #  void QQuickPen::colorChanged()
    self.uglySide.call('ritual_ZN9QQuickPen12colorChangedEv')

  def pixelAlignedChanged(self) -> None:
    """
    Calls Qt's 'void QQuickPen::pixelAlignedChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpen.html#pixelAlignedChanged
    """
    #  void QQuickPen::pixelAlignedChanged()
    self.uglySide.call('ritual_ZN9QQuickPen19pixelAlignedChangedEv')
