"""
QQuickPathText binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquickpath_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QQuickPathText to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject
from . import QQuickPathElement

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
  from ..QtGui import QFont
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QFont = WAIT['QFont']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickPathText(QQuickPathElement):
  """
  The cute side of Qt's QQuickPathText: a plain Python object standing in
  front of one C++ QQuickPathText.

  It is built on the cute 'QQuickPathElement', as Qt's QQuickPathText is
  built on Qt's QQuickPathElement, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickPathText that has a ritual and that Python can
  call so far, 18 names in all: 'metaObject', 'tr', 'x', 'y', 'text', 'font',
  'setX', 'setY', 'setText', 'setFont', 'width', 'height', 'xChanged',
  'yChanged', 'textChanged', 'fontChanged', 'invalidate', 'updatePath'. It
  can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickPathText::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QQuickPathText::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'void QQuickPathText::addToPath(QPainterPath &path)': takes a type
    Python has no way to hand over yet.

  What has no ritual
  ------------------

  2 of the 24 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuickPathText is created at the first use, not by
    'QQuickPathText(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickPathText.
  - Qt tells when it has removed the C++ QQuickPathText. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQuickPathText that has no cute function yet,
    'addToPath', holds a function that raises 'NotImplementedError', and its
    docstring says why.
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
    Calls Qt's 'QString QQuickPathText::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpathtext.html#tr

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
    #  QString QQuickPathText::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN14QQuickPathText2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickPathText'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickPathText::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpathtext.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickPathText::metaObject() const
    address = self.uglySide.call('ritual_ZNK14QQuickPathText10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def x(self) -> float:
    """
    Calls Qt's 'qreal QQuickPathText::x() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpathtext.html#x
    """
    #  qreal QQuickPathText::x() const
    return self.uglySide.call('ritual_ZNK14QQuickPathText1xEv')

  def y(self) -> float:
    """
    Calls Qt's 'qreal QQuickPathText::y() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpathtext.html#y
    """
    #  qreal QQuickPathText::y() const
    return self.uglySide.call('ritual_ZNK14QQuickPathText1yEv')

  def text(self) -> str:
    """
    Calls Qt's 'QString QQuickPathText::text() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpathtext.html#text

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuickPathText::text() const
    return self.uglySide.call('ritual_ZNK14QQuickPathText4textEv')

  def font(self) -> QFont:
    """
    Calls Qt's 'QFont QQuickPathText::font() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpathtext.html#font

    Returns
    -------

    QFont
      A new cute QFont around the copy Qt gave back. Python owns it.
    """
    #  QFont QQuickPathText::font() const
    address = self.uglySide.call('ritual_ZNK14QQuickPathText4fontEv')
    from ..QtGui import QFont
    return QFont._cuteOwning(address)

  def width(self) -> float:
    """
    Calls Qt's 'qreal QQuickPathText::width() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpathtext.html#width
    """
    #  qreal QQuickPathText::width() const
    return self.uglySide.call('ritual_ZNK14QQuickPathText5widthEv')

  def height(self) -> float:
    """
    Calls Qt's 'qreal QQuickPathText::height() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpathtext.html#height
    """
    #  qreal QQuickPathText::height() const
    return self.uglySide.call('ritual_ZNK14QQuickPathText6heightEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float)
  def setX(self, x: float) -> None:
    """
    Calls Qt's 'void QQuickPathText::setX(qreal x)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpathtext.html#setX

    Parameters
    ----------

    x : float
      Passed on as it is.
    """
    #  void QQuickPathText::setX(qreal x)
    self.uglySide.call('ritual_ZN14QQuickPathText4setXEd', x)

  @overload(float)
  def setY(self, y: float) -> None:
    """
    Calls Qt's 'void QQuickPathText::setY(qreal y)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpathtext.html#setY

    Parameters
    ----------

    y : float
      Passed on as it is.
    """
    #  void QQuickPathText::setY(qreal y)
    self.uglySide.call('ritual_ZN14QQuickPathText4setYEd', y)

  @overload(str)
  def setText(self, text: str) -> None:
    """
    Calls Qt's 'void QQuickPathText::setText(const QString &text)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpathtext.html#setText

    Parameters
    ----------

    text : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQuickPathText::setText(const QString &text)
    self.uglySide.call('ritual_ZN14QQuickPathText7setTextERK7QString', text)

  @overload(QFont)
  def setFont(self, font: QFont) -> None:
    """
    Calls Qt's 'void QQuickPathText::setFont(const QFont &font)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpathtext.html#setFont

    Parameters
    ----------

    font : QFont
      Passed on as a value: Qt reads the C++ QFont, which stays Python's own.
    """
    #  void QQuickPathText::setFont(const QFont &font)
    self.uglySide.call(
        'ritual_ZN14QQuickPathText7setFontERK5QFont', self._valueOf(font),
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
    Notes what was given, for Qt's 'QQuickPathText::QQuickPathText(QObject
    *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qquickpathtext.html#QQuickPathText

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickPathText::QQuickPathText(QObject *parent)
    self._noteCreation(QQuickPathText, lambda: Rituals.call(
        'ritual_ZN14QQuickPathTextC1EP7QObject',
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

  def xChanged(self) -> None:
    """
    Calls Qt's 'void QQuickPathText::xChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpathtext.html#xChanged
    """
    #  void QQuickPathText::xChanged()
    self.uglySide.call('ritual_ZN14QQuickPathText8xChangedEv')

  def yChanged(self) -> None:
    """
    Calls Qt's 'void QQuickPathText::yChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpathtext.html#yChanged
    """
    #  void QQuickPathText::yChanged()
    self.uglySide.call('ritual_ZN14QQuickPathText8yChangedEv')

  def textChanged(self) -> None:
    """
    Calls Qt's 'void QQuickPathText::textChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpathtext.html#textChanged
    """
    #  void QQuickPathText::textChanged()
    self.uglySide.call('ritual_ZN14QQuickPathText11textChangedEv')

  def fontChanged(self) -> None:
    """
    Calls Qt's 'void QQuickPathText::fontChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpathtext.html#fontChanged
    """
    #  void QQuickPathText::fontChanged()
    self.uglySide.call('ritual_ZN14QQuickPathText11fontChangedEv')

  def invalidate(self) -> None:
    """
    Calls Qt's 'void QQuickPathText::invalidate()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpathtext.html#invalidate
    """
    #  void QQuickPathText::invalidate()
    self.uglySide.call('ritual_ZN14QQuickPathText10invalidateEv')

  def updatePath(self) -> None:
    """
    Calls Qt's 'void QQuickPathText::updatePath() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpathtext.html#updatePath
    """
    #  void QQuickPathText::updatePath() const
    self.uglySide.call('ritual_ZNK14QQuickPathText10updatePathEv')

  @staticmethod
  def addToPath(*__, **_) -> Never:
    """
    Qt's 'void QQuickPathText::addToPath(QPainterPath &path)': takes a type
    Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQuickPathText.addToPath' has no cute function yet. Qt's 'void "
        "QQuickPathText::addToPath(QPainterPath &path)': takes a type "
        "Python has no way to hand over yet.")
