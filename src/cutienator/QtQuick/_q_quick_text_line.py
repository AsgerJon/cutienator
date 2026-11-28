"""
QQuickTextLine binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquicktext_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QQuickTextLine to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from ..QtGui import QTextLine
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QTextLine = WAIT['QTextLine']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickTextLine(QObject):
  """
  The cute side of Qt's QQuickTextLine: a plain Python object standing in
  front of one C++ QQuickTextLine.

  It is built on the cute 'QObject', as Qt's QQuickTextLine is built on Qt's
  QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickTextLine that has a ritual and that Python can
  call so far, 16 names in all: 'metaObject', 'tr', 'setLine',
  'setLineOffset', 'setFullLayoutTextLength', 'number', 'implicitWidth',
  'isLast', 'width', 'setWidth', 'height', 'setHeight', 'x', 'setX', 'y',
  'setY'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickTextLine::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QQuickTextLine::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'void QQuickTextLine::qt_qmlMarker_anonymous()': one of Qt's own
    inner workings.

  What has no ritual
  ------------------

  2 of the 22 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuickTextLine is created at the first use, not by
    'QQuickTextLine(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickTextLine.
  - Qt tells when it has removed the C++ QQuickTextLine. Every call on the
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
    Calls Qt's 'QString QQuickTextLine::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextline.html#tr

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
    #  QString QQuickTextLine::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN14QQuickTextLine2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickTextLine'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickTextLine::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextline.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickTextLine::metaObject() const
    address = self.uglySide.call('ritual_ZNK14QQuickTextLine10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def number(self) -> int:
    """
    Calls Qt's 'int QQuickTextLine::number() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextline.html#number
    """
    #  int QQuickTextLine::number() const
    return self.uglySide.call('ritual_ZNK14QQuickTextLine6numberEv')

  def implicitWidth(self) -> float:
    """
    Calls Qt's 'qreal QQuickTextLine::implicitWidth() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextline.html#implicitWidth
    """
    #  qreal QQuickTextLine::implicitWidth() const
    return self.uglySide.call('ritual_ZNK14QQuickTextLine13implicitWidthEv')

  def isLast(self) -> bool:
    """
    Calls Qt's 'bool QQuickTextLine::isLast() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextline.html#isLast
    """
    #  bool QQuickTextLine::isLast() const
    return self.uglySide.call('ritual_ZNK14QQuickTextLine6isLastEv')

  def width(self) -> float:
    """
    Calls Qt's 'qreal QQuickTextLine::width() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextline.html#width
    """
    #  qreal QQuickTextLine::width() const
    return self.uglySide.call('ritual_ZNK14QQuickTextLine5widthEv')

  def height(self) -> float:
    """
    Calls Qt's 'qreal QQuickTextLine::height() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextline.html#height
    """
    #  qreal QQuickTextLine::height() const
    return self.uglySide.call('ritual_ZNK14QQuickTextLine6heightEv')

  def x(self) -> float:
    """
    Calls Qt's 'qreal QQuickTextLine::x() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextline.html#x
    """
    #  qreal QQuickTextLine::x() const
    return self.uglySide.call('ritual_ZNK14QQuickTextLine1xEv')

  def y(self) -> float:
    """
    Calls Qt's 'qreal QQuickTextLine::y() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextline.html#y
    """
    #  qreal QQuickTextLine::y() const
    return self.uglySide.call('ritual_ZNK14QQuickTextLine1yEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QTextLine)
  @overload(NoneType)
  def setLine(self, line: Optional[QTextLine]) -> None:
    """
    Calls Qt's 'void QQuickTextLine::setLine(QTextLine *line)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextline.html#setLine

    Parameters
    ----------

    line : Optional[QTextLine]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickTextLine::setLine(QTextLine *line)
    self.uglySide.call(
        'ritual_ZN14QQuickTextLine7setLineEP9QTextLine',
        self._addressOf(line),
    )

  @overload(int)
  def setLineOffset(self, offset: int) -> None:
    """
    Calls Qt's 'void QQuickTextLine::setLineOffset(int offset)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextline.html#setLineOffset

    Parameters
    ----------

    offset : int
      Passed on as it is.
    """
    #  void QQuickTextLine::setLineOffset(int offset)
    self.uglySide.call('ritual_ZN14QQuickTextLine13setLineOffsetEi', offset)

  @overload(int)
  def setFullLayoutTextLength(self, length: int) -> None:
    """
    Calls Qt's 'void QQuickTextLine::setFullLayoutTextLength(int length)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextline.html#setFullLayoutTextLength

    Parameters
    ----------

    length : int
      Passed on as it is.
    """
    #  void QQuickTextLine::setFullLayoutTextLength(int length)
    self.uglySide.call(
        'ritual_ZN14QQuickTextLine23setFullLayoutTextLengthEi', length,
    )

  @overload(float)
  def setWidth(self, width: float) -> None:
    """
    Calls Qt's 'void QQuickTextLine::setWidth(qreal width)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextline.html#setWidth

    Parameters
    ----------

    width : float
      Passed on as it is.
    """
    #  void QQuickTextLine::setWidth(qreal width)
    self.uglySide.call('ritual_ZN14QQuickTextLine8setWidthEd', width)

  @overload(float)
  def setHeight(self, height: float) -> None:
    """
    Calls Qt's 'void QQuickTextLine::setHeight(qreal height)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextline.html#setHeight

    Parameters
    ----------

    height : float
      Passed on as it is.
    """
    #  void QQuickTextLine::setHeight(qreal height)
    self.uglySide.call('ritual_ZN14QQuickTextLine9setHeightEd', height)

  @overload(float)
  def setX(self, x: float) -> None:
    """
    Calls Qt's 'void QQuickTextLine::setX(qreal x)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextline.html#setX

    Parameters
    ----------

    x : float
      Passed on as it is.
    """
    #  void QQuickTextLine::setX(qreal x)
    self.uglySide.call('ritual_ZN14QQuickTextLine4setXEd', x)

  @overload(float)
  def setY(self, y: float) -> None:
    """
    Calls Qt's 'void QQuickTextLine::setY(qreal y)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextline.html#setY

    Parameters
    ----------

    y : float
      Passed on as it is.
    """
    #  void QQuickTextLine::setY(qreal y)
    self.uglySide.call('ritual_ZN14QQuickTextLine4setYEd', y)

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
    Notes what was given, for Qt's 'QQuickTextLine::QQuickTextLine()', which
    is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextline.html#QQuickTextLine
    """
    #  QQuickTextLine::QQuickTextLine()
    self._noteCreation(QQuickTextLine, lambda: Rituals.call(
        'ritual_ZN14QQuickTextLineC1Ev',
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
