"""
QQuickPaddedRectangle binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickControls2Impl/6.12.0/QtQuickControls2Impl/private/qquickpaddedrectangle_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuickPaddedRectangle to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtQuick import QQuickItem, QQuickRectangle

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from ..QtQuick import QSGNode
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QSGNode = WAIT['QSGNode']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickPaddedRectangle(QQuickRectangle):
  """
  The cute side of Qt's QQuickPaddedRectangle: a plain Python object standing
  in front of one C++ QQuickPaddedRectangle.

  It is built on the cute 'QQuickRectangle', as Qt's QQuickPaddedRectangle is
  built on Qt's QQuickRectangle, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickPaddedRectangle that has a ritual and that
  Python can call so far, 23 names in all: 'metaObject', 'tr', 'padding',
  'setPadding', 'resetPadding', 'topPadding', 'setTopPadding',
  'resetTopPadding', 'leftPadding', 'setLeftPadding', 'resetLeftPadding',
  'rightPadding', 'setRightPadding', 'resetRightPadding', 'bottomPadding',
  'setBottomPadding', 'resetBottomPadding', 'paddingChanged',
  'topPaddingChanged', 'leftPaddingChanged', 'rightPaddingChanged',
  'bottomPaddingChanged', 'updatePaintNode'. It can be made from Python, in 1
  way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickPaddedRectangle::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QQuickPaddedRectangle::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.

  What has no ritual
  ------------------

  2 of the 32 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuickPaddedRectangle is created at the first use, not by
    'QQuickPaddedRectangle(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickPaddedRectangle.
  - Qt tells when it has removed the C++ QQuickPaddedRectangle. Every call on
    the cute object, and every use of it as an argument, then raises
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
    Calls Qt's 'QString QQuickPaddedRectangle::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpaddedrectangle.html#tr

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
    #  QString QQuickPaddedRectangle::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN21QQuickPaddedRectangle2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickPaddedRectangle'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickPaddedRectangle::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpaddedrectangle.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickPaddedRectangle::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK21QQuickPaddedRectangle10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def padding(self) -> float:
    """
    Calls Qt's 'qreal QQuickPaddedRectangle::padding() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpaddedrectangle.html#padding
    """
    #  qreal QQuickPaddedRectangle::padding() const
    return self.uglySide.call('ritual_ZNK21QQuickPaddedRectangle7paddingEv')

  def topPadding(self) -> float:
    """
    Calls Qt's 'qreal QQuickPaddedRectangle::topPadding() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpaddedrectangle.html#topPadding
    """
    #  qreal QQuickPaddedRectangle::topPadding() const
    return self.uglySide.call(
        'ritual_ZNK21QQuickPaddedRectangle10topPaddingEv',
    )

  def leftPadding(self) -> float:
    """
    Calls Qt's 'qreal QQuickPaddedRectangle::leftPadding() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpaddedrectangle.html#leftPadding
    """
    #  qreal QQuickPaddedRectangle::leftPadding() const
    return self.uglySide.call(
        'ritual_ZNK21QQuickPaddedRectangle11leftPaddingEv',
    )

  def rightPadding(self) -> float:
    """
    Calls Qt's 'qreal QQuickPaddedRectangle::rightPadding() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpaddedrectangle.html#rightPadding
    """
    #  qreal QQuickPaddedRectangle::rightPadding() const
    return self.uglySide.call(
        'ritual_ZNK21QQuickPaddedRectangle12rightPaddingEv',
    )

  def bottomPadding(self) -> float:
    """
    Calls Qt's 'qreal QQuickPaddedRectangle::bottomPadding() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpaddedrectangle.html#bottomPadding
    """
    #  qreal QQuickPaddedRectangle::bottomPadding() const
    return self.uglySide.call(
        'ritual_ZNK21QQuickPaddedRectangle13bottomPaddingEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float)
  def setPadding(self, padding: float) -> None:
    """
    Calls Qt's 'void QQuickPaddedRectangle::setPadding(qreal padding)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpaddedrectangle.html#setPadding

    Parameters
    ----------

    padding : float
      Passed on as it is.
    """
    #  void QQuickPaddedRectangle::setPadding(qreal padding)
    self.uglySide.call(
        'ritual_ZN21QQuickPaddedRectangle10setPaddingEd', padding,
    )

  @overload(float)
  def setTopPadding(self, padding: float) -> None:
    """
    Calls Qt's 'void QQuickPaddedRectangle::setTopPadding(qreal padding)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpaddedrectangle.html#setTopPadding

    Parameters
    ----------

    padding : float
      Passed on as it is.
    """
    #  void QQuickPaddedRectangle::setTopPadding(qreal padding)
    self.uglySide.call(
        'ritual_ZN21QQuickPaddedRectangle13setTopPaddingEd', padding,
    )

  @overload(float, bool)
  def setTopPadding(self, padding: float, has: bool) -> None:
    """
    Calls Qt's 'void QQuickPaddedRectangle::setTopPadding(qreal padding, bool
    has)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpaddedrectangle.html#setTopPadding

    Parameters
    ----------

    padding : float
      Passed on as it is.

    has : bool
      Passed on as it is.
    """
    #  void QQuickPaddedRectangle::setTopPadding(qreal padding, bool has)
    self.uglySide.call(
        'ritual_ZN21QQuickPaddedRectangle13setTopPaddingEdb', padding, has,
    )

  @overload(float)
  def setLeftPadding(self, padding: float) -> None:
    """
    Calls Qt's 'void QQuickPaddedRectangle::setLeftPadding(qreal padding)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpaddedrectangle.html#setLeftPadding

    Parameters
    ----------

    padding : float
      Passed on as it is.
    """
    #  void QQuickPaddedRectangle::setLeftPadding(qreal padding)
    self.uglySide.call(
        'ritual_ZN21QQuickPaddedRectangle14setLeftPaddingEd', padding,
    )

  @overload(float, bool)
  def setLeftPadding(self, padding: float, has: bool) -> None:
    """
    Calls Qt's 'void QQuickPaddedRectangle::setLeftPadding(qreal padding,
    bool has)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpaddedrectangle.html#setLeftPadding

    Parameters
    ----------

    padding : float
      Passed on as it is.

    has : bool
      Passed on as it is.
    """
    #  void QQuickPaddedRectangle::setLeftPadding(qreal padding, bool has)
    self.uglySide.call(
        'ritual_ZN21QQuickPaddedRectangle14setLeftPaddingEdb', padding, has,
    )

  @overload(float)
  def setRightPadding(self, padding: float) -> None:
    """
    Calls Qt's 'void QQuickPaddedRectangle::setRightPadding(qreal padding)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpaddedrectangle.html#setRightPadding

    Parameters
    ----------

    padding : float
      Passed on as it is.
    """
    #  void QQuickPaddedRectangle::setRightPadding(qreal padding)
    self.uglySide.call(
        'ritual_ZN21QQuickPaddedRectangle15setRightPaddingEd', padding,
    )

  @overload(float, bool)
  def setRightPadding(self, padding: float, has: bool) -> None:
    """
    Calls Qt's 'void QQuickPaddedRectangle::setRightPadding(qreal padding,
    bool has)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpaddedrectangle.html#setRightPadding

    Parameters
    ----------

    padding : float
      Passed on as it is.

    has : bool
      Passed on as it is.
    """
    #  void QQuickPaddedRectangle::setRightPadding(qreal padding, bool has)
    self.uglySide.call(
        'ritual_ZN21QQuickPaddedRectangle15setRightPaddingEdb', padding, has,
    )

  @overload(float)
  def setBottomPadding(self, padding: float) -> None:
    """
    Calls Qt's 'void QQuickPaddedRectangle::setBottomPadding(qreal padding)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpaddedrectangle.html#setBottomPadding

    Parameters
    ----------

    padding : float
      Passed on as it is.
    """
    #  void QQuickPaddedRectangle::setBottomPadding(qreal padding)
    self.uglySide.call(
        'ritual_ZN21QQuickPaddedRectangle16setBottomPaddingEd', padding,
    )

  @overload(float, bool)
  def setBottomPadding(self, padding: float, has: bool) -> None:
    """
    Calls Qt's 'void QQuickPaddedRectangle::setBottomPadding(qreal padding,
    bool has)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpaddedrectangle.html#setBottomPadding

    Parameters
    ----------

    padding : float
      Passed on as it is.

    has : bool
      Passed on as it is.
    """
    #  void QQuickPaddedRectangle::setBottomPadding(qreal padding, bool has)
    self.uglySide.call(
        'ritual_ZN21QQuickPaddedRectangle16setBottomPaddingEdb',
        padding, has,
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
    'QQuickPaddedRectangle::QQuickPaddedRectangle(QQuickItem *parent)', which
    is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpaddedrectangle.html#QQuickPaddedRectangle

    Parameters
    ----------

    parent : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickPaddedRectangle::QQuickPaddedRectangle(QQuickItem *parent)
    self._noteCreation(QQuickPaddedRectangle, lambda: Rituals.call(
        'ritual_ZN21QQuickPaddedRectangleC1EP10QQuickItem',
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

  def resetPadding(self) -> None:
    """
    Calls Qt's 'void QQuickPaddedRectangle::resetPadding()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpaddedrectangle.html#resetPadding
    """
    #  void QQuickPaddedRectangle::resetPadding()
    self.uglySide.call('ritual_ZN21QQuickPaddedRectangle12resetPaddingEv')

  def resetTopPadding(self) -> None:
    """
    Calls Qt's 'void QQuickPaddedRectangle::resetTopPadding()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpaddedrectangle.html#resetTopPadding
    """
    #  void QQuickPaddedRectangle::resetTopPadding()
    self.uglySide.call('ritual_ZN21QQuickPaddedRectangle15resetTopPaddingEv')

  def resetLeftPadding(self) -> None:
    """
    Calls Qt's 'void QQuickPaddedRectangle::resetLeftPadding()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpaddedrectangle.html#resetLeftPadding
    """
    #  void QQuickPaddedRectangle::resetLeftPadding()
    self.uglySide.call(
        'ritual_ZN21QQuickPaddedRectangle16resetLeftPaddingEv',
    )

  def resetRightPadding(self) -> None:
    """
    Calls Qt's 'void QQuickPaddedRectangle::resetRightPadding()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpaddedrectangle.html#resetRightPadding
    """
    #  void QQuickPaddedRectangle::resetRightPadding()
    self.uglySide.call(
        'ritual_ZN21QQuickPaddedRectangle17resetRightPaddingEv',
    )

  def resetBottomPadding(self) -> None:
    """
    Calls Qt's 'void QQuickPaddedRectangle::resetBottomPadding()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpaddedrectangle.html#resetBottomPadding
    """
    #  void QQuickPaddedRectangle::resetBottomPadding()
    self.uglySide.call(
        'ritual_ZN21QQuickPaddedRectangle18resetBottomPaddingEv',
    )

  def paddingChanged(self) -> None:
    """
    Calls Qt's 'void QQuickPaddedRectangle::paddingChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpaddedrectangle.html#paddingChanged
    """
    #  void QQuickPaddedRectangle::paddingChanged()
    self.uglySide.call('ritual_ZN21QQuickPaddedRectangle14paddingChangedEv')

  def topPaddingChanged(self) -> None:
    """
    Calls Qt's 'void QQuickPaddedRectangle::topPaddingChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpaddedrectangle.html#topPaddingChanged
    """
    #  void QQuickPaddedRectangle::topPaddingChanged()
    self.uglySide.call(
        'ritual_ZN21QQuickPaddedRectangle17topPaddingChangedEv',
    )

  def leftPaddingChanged(self) -> None:
    """
    Calls Qt's 'void QQuickPaddedRectangle::leftPaddingChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpaddedrectangle.html#leftPaddingChanged
    """
    #  void QQuickPaddedRectangle::leftPaddingChanged()
    self.uglySide.call(
        'ritual_ZN21QQuickPaddedRectangle18leftPaddingChangedEv',
    )

  def rightPaddingChanged(self) -> None:
    """
    Calls Qt's 'void QQuickPaddedRectangle::rightPaddingChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpaddedrectangle.html#rightPaddingChanged
    """
    #  void QQuickPaddedRectangle::rightPaddingChanged()
    self.uglySide.call(
        'ritual_ZN21QQuickPaddedRectangle19rightPaddingChangedEv',
    )

  def bottomPaddingChanged(self) -> None:
    """
    Calls Qt's 'void QQuickPaddedRectangle::bottomPaddingChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpaddedrectangle.html#bottomPaddingChanged
    """
    #  void QQuickPaddedRectangle::bottomPaddingChanged()
    self.uglySide.call(
        'ritual_ZN21QQuickPaddedRectangle20bottomPaddingChangedEv',
    )

  @overload(QSGNode, QQuickItem.UpdatePaintNodeData)
  @overload(QSGNode, NoneType)
  @overload(NoneType, QQuickItem.UpdatePaintNodeData)
  @overload(NoneType, NoneType)
  def updatePaintNode(
      self,
      a0: Optional[QSGNode],
      a1: Optional[QQuickItem.UpdatePaintNodeData],
  ) -> Optional[QSGNode]:
    """
    Calls Qt's 'QSGNode *QQuickPaddedRectangle::updatePaintNode(QSGNode *a0,
    UpdatePaintNodeData *a1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpaddedrectangle.html#updatePaintNode

    Parameters
    ----------

    a0 : Optional[QSGNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    a1 : Optional[QQuickItem.UpdatePaintNodeData]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QSGNode]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSGNode *QQuickPaddedRectangle::updatePaintNode(QSGNode *a0,
    #      UpdatePaintNodeData *a1)
    ritual = (
        'ritual_ZN21QQuickPaddedRectangle15updatePaintNodeEP7QSGNodePN10QQu'
        'ickItem19UpdatePaintNodeDataE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN21QQuickPaddedRectangle15updatePaintNodeEP7QSGNodeP'
          'N10QQuickItem19UpdatePaintNodeDataE')
    address = self.uglySide.call(
        ritual, self._addressOf(a0, 'QSGNode'), self._addressOf(a1),
    )
    from ..QtQuick import QSGNode
    return QSGNode._cuteAt(address)
