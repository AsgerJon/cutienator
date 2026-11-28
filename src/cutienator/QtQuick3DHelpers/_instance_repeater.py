"""
InstanceRepeater binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3DHelpers/6.12.0/QtQuick3DHelpers/private/instancerepeater_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means InstanceRepeater to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from ..QtQuick3D import QQuick3DInstancing, QQuick3DNode
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQuick3DInstancing = WAIT['QQuick3DInstancing']
  QQuick3DNode = WAIT['QQuick3DNode']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class InstanceRepeater(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's InstanceRepeater: a plain Python object standing in
  front of one C++ InstanceRepeater.

  What exists
  -----------

  Every function of Qt's InstanceRepeater that has a ritual and that Python
  can call so far, 6 names in all: 'metaObject', 'tr', 'instancing',
  'setInstancing', 'instancingChanged', 'initDelegate'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *InstanceRepeater::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int InstanceRepeater::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.

  What has no ritual
  ------------------

  2 of the 11 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ InstanceRepeater is created at the first use, not by
    'InstanceRepeater(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ InstanceRepeater.
  - Qt tells when it has removed the C++ InstanceRepeater. Every call on the
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
    Calls Qt's 'QString InstanceRepeater::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/instancerepeater.html#tr

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
    #  QString InstanceRepeater::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN16InstanceRepeater2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'InstanceRepeater'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *InstanceRepeater::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/instancerepeater.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *InstanceRepeater::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK16InstanceRepeater10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def instancing(self) -> Optional[QQuick3DInstancing]:
    """
    Calls Qt's 'QQuick3DInstancing *InstanceRepeater::instancing() const'.

    Qt's own words: https://doc.qt.io/qt-6/instancerepeater.html#instancing

    Returns
    -------

    Optional[QQuick3DInstancing]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuick3DInstancing *InstanceRepeater::instancing() const
    address = self.uglySide.call(
        'ritual_ZNK16InstanceRepeater10instancingEv',
    )
    from ..QtQuick3D import QQuick3DInstancing
    return QQuick3DInstancing._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QQuick3DInstancing)
  @overload(NoneType)
  def setInstancing(self, instancing: Optional[QQuick3DInstancing]) -> None:
    """
    Calls Qt's 'void InstanceRepeater::setInstancing(QQuick3DInstancing
    *instancing)'.

    Qt's own words:
    https://doc.qt.io/qt-6/instancerepeater.html#setInstancing

    Parameters
    ----------

    instancing : Optional[QQuick3DInstancing]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void InstanceRepeater::setInstancing(QQuick3DInstancing *instancing)
    self.uglySide.call(
        'ritual_ZN16InstanceRepeater13setInstancingEP18QQuick3DInstancing',
        self._addressOf(instancing),
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
  @overload(QQuick3DNode)
  @overload(NoneType)
  def __init__(self, parent: Optional[QQuick3DNode] = None) -> None:
    """
    Notes what was given, for Qt's
    'InstanceRepeater::InstanceRepeater(QQuick3DNode *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/instancerepeater.html#InstanceRepeater

    Parameters
    ----------

    parent : Optional[QQuick3DNode]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  InstanceRepeater::InstanceRepeater(QQuick3DNode *parent)
    self._noteCreation(InstanceRepeater, lambda: Rituals.call(
        'ritual_ZN16InstanceRepeaterC1EP12QQuick3DNode',
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

  def instancingChanged(self) -> None:
    """
    Calls Qt's 'void InstanceRepeater::instancingChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/instancerepeater.html#instancingChanged
    """
    #  void InstanceRepeater::instancingChanged()
    self.uglySide.call('ritual_ZN16InstanceRepeater17instancingChangedEv')

  @overload(int, QQuick3DNode)
  @overload(int, NoneType)
  def initDelegate(self, index: int, node: Optional[QQuick3DNode]) -> None:
    """
    Calls Qt's 'void InstanceRepeater::initDelegate(int index, QQuick3DNode
    *node)'.

    Qt's own words: https://doc.qt.io/qt-6/instancerepeater.html#initDelegate

    Parameters
    ----------

    index : int
      Passed on as it is.

    node : Optional[QQuick3DNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void InstanceRepeater::initDelegate(int index, QQuick3DNode *node)
    ritual = 'ritual_ZN16InstanceRepeater12initDelegateEiP12QQuick3DNode'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN16InstanceRepeater12initDelegateEiP12QQuick3DNode')
    self.uglySide.call(ritual, index, self._addressOf(node))
