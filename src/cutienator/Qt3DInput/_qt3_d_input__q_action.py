"""
Qt3DInput::QAction binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DInput/qaction.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..Qt3DCore import Qt3DCore
from . import Qt3DInput

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QAction(Qt3DCore.QNode):
  """
  The cute side of Qt's Qt3DInput::QAction: a plain Python object standing in
  front of one C++ Qt3DInput::QAction.

  It is built on the cute 'Qt3DCore::QNode', as Qt's Qt3DInput::QAction is
  built on Qt's Qt3DCore::QNode, and has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DInput::QAction that has a ritual and that Python
  can call so far, 7 names in all: 'metaObject', 'tr', 'isActive',
  'addInput', 'removeInput', 'activeChanged', 'd_func'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *Qt3DInput::QAction::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int Qt3DInput::QAction::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'Qt3DInput::QAction::~QAction()': the destructor: Python never
    removes a C++ Qt3DInput::QAction.
  - Qt's 'QList<QAbstractActionInput *> Qt3DInput::QAction::inputs() const':
    gives a type Python has no way to take yet.
  - Qt's 'const QActionPrivate *Qt3DInput::QAction::d_func() const': takes in
    Python what 'QActionPrivate *Qt3DInput::QAction::d_func()' takes.

  What has no ritual
  ------------------

  2 of the 15 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ Qt3DInput::QAction is created at the first use, not by
    'Qt3DInput::QAction(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DInput::QAction.
  - Qt tells when it has removed the C++ Qt3DInput::QAction. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's Qt3DInput::QAction that has no cute function yet,
    'inputs', holds a function that raises 'NotImplementedError', and its
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
    Calls Qt's 'QString Qt3DInput::QAction::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qt3dinput-qaction.html#tr

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
    #  QString Qt3DInput::QAction::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN9Qt3DInput7QAction2trEPKcS2_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DInput::QAction'

  #  A C++ Qt3DInput::QAction Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DInput_QAction'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *Qt3DInput::QAction::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qt3dinput-qaction.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *Qt3DInput::QAction::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK9Qt3DInput7QAction10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def isActive(self) -> bool:
    """
    Calls Qt's 'bool Qt3DInput::QAction::isActive() const'.

    Qt's own words: https://doc.qt.io/qt-6/qt3dinput-qaction.html#isActive
    """
    #  bool Qt3DInput::QAction::isActive() const
    return self.uglySide.call('ritual_ZNK9Qt3DInput7QAction8isActiveEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

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
  @overload(Qt3DCore.QNode)
  @overload(NoneType)
  def __init__(self, parent: Optional[Qt3DCore.QNode] = None) -> None:
    """
    Notes what was given, for Qt's
    'Qt3DInput::QAction::QAction(Qt3DCore::QNode *parent)', which is called
    at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qt3dinput-qaction.html#QAction

    Parameters
    ----------

    parent : Optional[Qt3DCore.QNode]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  Qt3DInput::QAction::QAction(Qt3DCore::QNode *parent)
    self._noteCreation(QAction, lambda: Rituals.call(
        'ritual_ZN9Qt3DInput7QActionC1EPN8Qt3DCore5QNodeE',
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

  @overload(WAIT['Qt3DInput.QAbstractActionInput'])
  @overload(NoneType)
  def addInput(
      self,
      input: Optional[Qt3DInput.QAbstractActionInput],
  ) -> None:
    """
    Calls Qt's 'void Qt3DInput::QAction::addInput(QAbstractActionInput
    *input)'.

    Qt's own words: https://doc.qt.io/qt-6/qt3dinput-qaction.html#addInput

    Parameters
    ----------

    input : Optional[Qt3DInput.QAbstractActionInput]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DInput::QAction::addInput(QAbstractActionInput *input)
    self.uglySide.call(
        'ritual_ZN9Qt3DInput7QAction8addInputEPNS_20QAbstractActionInputE',
        self._addressOf(input),
    )

  @overload(WAIT['Qt3DInput.QAbstractActionInput'])
  @overload(NoneType)
  def removeInput(
      self,
      input: Optional[Qt3DInput.QAbstractActionInput],
  ) -> None:
    """
    Calls Qt's 'void Qt3DInput::QAction::removeInput(QAbstractActionInput
    *input)'.

    Qt's own words: https://doc.qt.io/qt-6/qt3dinput-qaction.html#removeInput

    Parameters
    ----------

    input : Optional[Qt3DInput.QAbstractActionInput]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DInput::QAction::removeInput(QAbstractActionInput *input)
    self.uglySide.call(
        'ritual_ZN9Qt3DInput7QAction11removeInputEPNS_20QAbstractActionInpu'
        'tE',
        self._addressOf(input),
    )

  @overload(bool)
  def activeChanged(self, isActive: bool) -> None:
    """
    Calls Qt's 'void Qt3DInput::QAction::activeChanged(bool isActive)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qaction.html#activeChanged

    Parameters
    ----------

    isActive : bool
      Passed on as it is.
    """
    #  void Qt3DInput::QAction::activeChanged(bool isActive)
    self.uglySide.call(
        'ritual_ZN9Qt3DInput7QAction13activeChangedEb', isActive,
    )

  def d_func(self) -> Optional[Qt3DInput.QActionPrivate]:
    """
    Calls Qt's 'QActionPrivate *Qt3DInput::QAction::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qt3dinput-qaction.html#d_func

    Returns
    -------

    Optional[Qt3DInput.QActionPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QActionPrivate *Qt3DInput::QAction::d_func()
    address = self.uglySide.call('ritual_ZN9Qt3DInput7QAction6d_funcEv')
    return Qt3DInput.QActionPrivate._cuteAt(address)

  @staticmethod
  def inputs(*__, **_) -> Never:
    """
    Qt's 'QList<QAbstractActionInput *> Qt3DInput::QAction::inputs() const':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'Qt3DInput.QAction.inputs' has no cute function yet. Qt's "
        "'QList<QAbstractActionInput *> Qt3DInput::QAction::inputs() "
        "const': gives a type Python has no way to take yet.")
