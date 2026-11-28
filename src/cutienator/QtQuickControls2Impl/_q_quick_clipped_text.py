"""
QQuickClippedText binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickControls2Impl/6.12.0/QtQuickControls2Impl/private/qquickclippedtext_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuickClippedText to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin
from ..occult import Rituals
from ..QtQuick import QQuickItem, QQuickText

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QRectF

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickClippedText(QQuickText):
  """
  The cute side of Qt's QQuickClippedText: a plain Python object standing in
  front of one C++ QQuickClippedText.

  It is built on the cute 'QQuickText', as Qt's QQuickClippedText is built on
  Qt's QQuickText, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickClippedText that has a ritual and that Python
  can call so far, 12 names in all: 'metaObject', 'tr', 'clipX', 'setClipX',
  'clipY', 'setClipY', 'clipWidth', 'setClipWidth', 'clipHeight',
  'setClipHeight', 'clipRect', 'markClipDirty'. It can be made from Python,
  in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickClippedText::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QQuickClippedText::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.

  What has no ritual
  ------------------

  2 of the 17 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuickClippedText is created at the first use, not by
    'QQuickClippedText(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickClippedText.
  - Qt tells when it has removed the C++ QQuickClippedText. Every call on the
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
    Calls Qt's 'QString QQuickClippedText::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickclippedtext.html#tr

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
    #  QString QQuickClippedText::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN17QQuickClippedText2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickClippedText'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickClippedText::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickclippedtext.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickClippedText::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK17QQuickClippedText10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def clipX(self) -> float:
    """
    Calls Qt's 'qreal QQuickClippedText::clipX() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickclippedtext.html#clipX
    """
    #  qreal QQuickClippedText::clipX() const
    return self.uglySide.call('ritual_ZNK17QQuickClippedText5clipXEv')

  def clipY(self) -> float:
    """
    Calls Qt's 'qreal QQuickClippedText::clipY() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickclippedtext.html#clipY
    """
    #  qreal QQuickClippedText::clipY() const
    return self.uglySide.call('ritual_ZNK17QQuickClippedText5clipYEv')

  def clipWidth(self) -> float:
    """
    Calls Qt's 'qreal QQuickClippedText::clipWidth() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickclippedtext.html#clipWidth
    """
    #  qreal QQuickClippedText::clipWidth() const
    return self.uglySide.call('ritual_ZNK17QQuickClippedText9clipWidthEv')

  def clipHeight(self) -> float:
    """
    Calls Qt's 'qreal QQuickClippedText::clipHeight() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickclippedtext.html#clipHeight
    """
    #  qreal QQuickClippedText::clipHeight() const
    return self.uglySide.call('ritual_ZNK17QQuickClippedText10clipHeightEv')

  def clipRect(self) -> QRectF:
    """
    Calls Qt's 'QRectF QQuickClippedText::clipRect() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickclippedtext.html#clipRect

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QQuickClippedText::clipRect() const
    ritual = 'ritual_ZNK17QQuickClippedText8clipRectEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK17QQuickClippedText8clipRectEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float)
  def setClipX(self, x: float) -> None:
    """
    Calls Qt's 'void QQuickClippedText::setClipX(qreal x)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickclippedtext.html#setClipX

    Parameters
    ----------

    x : float
      Passed on as it is.
    """
    #  void QQuickClippedText::setClipX(qreal x)
    self.uglySide.call('ritual_ZN17QQuickClippedText8setClipXEd', x)

  @overload(float)
  def setClipY(self, y: float) -> None:
    """
    Calls Qt's 'void QQuickClippedText::setClipY(qreal y)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickclippedtext.html#setClipY

    Parameters
    ----------

    y : float
      Passed on as it is.
    """
    #  void QQuickClippedText::setClipY(qreal y)
    self.uglySide.call('ritual_ZN17QQuickClippedText8setClipYEd', y)

  @overload(float)
  def setClipWidth(self, width: float) -> None:
    """
    Calls Qt's 'void QQuickClippedText::setClipWidth(qreal width)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickclippedtext.html#setClipWidth

    Parameters
    ----------

    width : float
      Passed on as it is.
    """
    #  void QQuickClippedText::setClipWidth(qreal width)
    self.uglySide.call('ritual_ZN17QQuickClippedText12setClipWidthEd', width)

  @overload(float)
  def setClipHeight(self, height: float) -> None:
    """
    Calls Qt's 'void QQuickClippedText::setClipHeight(qreal height)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickclippedtext.html#setClipHeight

    Parameters
    ----------

    height : float
      Passed on as it is.
    """
    #  void QQuickClippedText::setClipHeight(qreal height)
    self.uglySide.call(
        'ritual_ZN17QQuickClippedText13setClipHeightEd', height,
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
    'QQuickClippedText::QQuickClippedText(QQuickItem *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickclippedtext.html#QQuickClippedText

    Parameters
    ----------

    parent : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickClippedText::QQuickClippedText(QQuickItem *parent)
    self._noteCreation(QQuickClippedText, lambda: Rituals.call(
        'ritual_ZN17QQuickClippedTextC1EP10QQuickItem',
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

  def markClipDirty(self) -> None:
    """
    Calls Qt's 'void QQuickClippedText::markClipDirty()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickclippedtext.html#markClipDirty
    """
    #  void QQuickClippedText::markClipDirty()
    self.uglySide.call('ritual_ZN17QQuickClippedText13markClipDirtyEv')
