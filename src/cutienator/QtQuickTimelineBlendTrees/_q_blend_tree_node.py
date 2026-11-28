"""
QBlendTreeNode binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickTimelineBlendTrees/6.12.0/QtQuickTimelineBlendTrees/private/qblendtreenode_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QBlendTreeNode to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin
from ..occult import Rituals
from ..QtCore import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QBlendTreeNode(QObject):
  """
  The cute side of Qt's QBlendTreeNode: a plain Python object standing in
  front of one C++ QBlendTreeNode.

  It is built on the cute 'QObject', as Qt's QBlendTreeNode is built on Qt's
  QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QBlendTreeNode that has a ritual and that Python can
  call so far, 7 names in all: 'metaObject', 'tr', 'outputEnabled',
  'setOutputEnabled', 'frameDataChanged', 'outputEnabledChanged',
  'handleFrameDataChanged'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QBlendTreeNode::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QBlendTreeNode::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'void QBlendTreeNode::qt_qmlMarker_uncreatable()': one of Qt's own
    inner workings.
  - Qt's 'const QHash<QQmlProperty, QVariant> &QBlendTreeNode::frameData()':
    gives a type Python has no way to take yet.

  What has no ritual
  ------------------

  2 of the 14 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QBlendTreeNode is created at the first use, not by
    'QBlendTreeNode(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QBlendTreeNode.
  - Qt tells when it has removed the C++ QBlendTreeNode. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QBlendTreeNode that has no cute function yet,
    'frameData', holds a function that raises 'NotImplementedError', and its
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
    Calls Qt's 'QString QBlendTreeNode::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qblendtreenode.html#tr

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
    #  QString QBlendTreeNode::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN14QBlendTreeNode2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QBlendTreeNode'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QBlendTreeNode::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qblendtreenode.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QBlendTreeNode::metaObject() const
    address = self.uglySide.call('ritual_ZNK14QBlendTreeNode10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def outputEnabled(self) -> bool:
    """
    Calls Qt's 'bool QBlendTreeNode::outputEnabled() const'.

    Qt's own words: https://doc.qt.io/qt-6/qblendtreenode.html#outputEnabled
    """
    #  bool QBlendTreeNode::outputEnabled() const
    return self.uglySide.call('ritual_ZNK14QBlendTreeNode13outputEnabledEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  def setOutputEnabled(self, isOutputEnabled: bool) -> None:
    """
    Calls Qt's 'void QBlendTreeNode::setOutputEnabled(bool isOutputEnabled)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qblendtreenode.html#setOutputEnabled

    Parameters
    ----------

    isOutputEnabled : bool
      Passed on as it is.
    """
    #  void QBlendTreeNode::setOutputEnabled(bool isOutputEnabled)
    self.uglySide.call(
        'ritual_ZN14QBlendTreeNode16setOutputEnabledEb', isOutputEnabled,
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
    Notes what was given, for Qt's 'QBlendTreeNode::QBlendTreeNode(QObject
    *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qblendtreenode.html#QBlendTreeNode

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QBlendTreeNode::QBlendTreeNode(QObject *parent)
    self._noteCreation(QBlendTreeNode, lambda: Rituals.call(
        'ritual_ZN14QBlendTreeNodeC1EP7QObject',
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

  def frameDataChanged(self) -> None:
    """
    Calls Qt's 'void QBlendTreeNode::frameDataChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qblendtreenode.html#frameDataChanged
    """
    #  void QBlendTreeNode::frameDataChanged()
    self.uglySide.call('ritual_ZN14QBlendTreeNode16frameDataChangedEv')

  def outputEnabledChanged(self) -> None:
    """
    Calls Qt's 'void QBlendTreeNode::outputEnabledChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qblendtreenode.html#outputEnabledChanged
    """
    #  void QBlendTreeNode::outputEnabledChanged()
    self.uglySide.call('ritual_ZN14QBlendTreeNode20outputEnabledChangedEv')

  def handleFrameDataChanged(self) -> None:
    """
    Calls Qt's 'void QBlendTreeNode::handleFrameDataChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qblendtreenode.html#handleFrameDataChanged
    """
    #  void QBlendTreeNode::handleFrameDataChanged()
    self.uglySide.call('ritual_ZN14QBlendTreeNode22handleFrameDataChangedEv')

  @staticmethod
  def frameData(*__, **_) -> Never:
    """
    Qt's 'const QHash<QQmlProperty, QVariant> &QBlendTreeNode::frameData()':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QBlendTreeNode.frameData' has no cute function yet. Qt's 'const "
        "QHash<QQmlProperty, QVariant> &QBlendTreeNode::frameData()': gives "
        "a type Python has no way to take yet.")
