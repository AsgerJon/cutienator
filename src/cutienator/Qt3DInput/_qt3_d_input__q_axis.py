"""
Qt3DInput::QAxis binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DInput/qaxis.h, Qt 6.12.0. Changes made here are lost.
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


class QAxis(Qt3DCore.QNode):
  """
  The cute side of Qt's Qt3DInput::QAxis: a plain Python object standing in
  front of one C++ Qt3DInput::QAxis.

  It is built on the cute 'Qt3DCore::QNode', as Qt's Qt3DInput::QAxis is
  built on Qt's Qt3DCore::QNode, and has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DInput::QAxis that has a ritual and that Python
  can call so far, 7 names in all: 'metaObject', 'tr', 'addInput',
  'removeInput', 'value', 'valueChanged', 'd_func'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *Qt3DInput::QAxis::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int Qt3DInput::QAxis::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'Qt3DInput::QAxis::~QAxis()': the destructor: Python never removes a
    C++ Qt3DInput::QAxis.
  - Qt's 'QList<QAbstractAxisInput *> Qt3DInput::QAxis::inputs() const':
    gives a type Python has no way to take yet.
  - Qt's 'const QAxisPrivate *Qt3DInput::QAxis::d_func() const': takes in
    Python what 'QAxisPrivate *Qt3DInput::QAxis::d_func()' takes.

  What has no ritual
  ------------------

  2 of the 15 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ Qt3DInput::QAxis is created at the first use, not by
    'Qt3DInput::QAxis(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DInput::QAxis.
  - Qt tells when it has removed the C++ Qt3DInput::QAxis. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's Qt3DInput::QAxis that has no cute function yet,
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
    Calls Qt's 'QString Qt3DInput::QAxis::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qt3dinput-qaxis.html#tr

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
    #  QString Qt3DInput::QAxis::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN9Qt3DInput5QAxis2trEPKcS2_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DInput::QAxis'

  #  A C++ Qt3DInput::QAxis Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DInput_QAxis'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *Qt3DInput::QAxis::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qt3dinput-qaxis.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *Qt3DInput::QAxis::metaObject() const
    address = self.uglySide.call('ritual_ZNK9Qt3DInput5QAxis10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def value(self) -> float:
    """
    Calls Qt's 'float Qt3DInput::QAxis::value() const'.

    Qt's own words: https://doc.qt.io/qt-6/qt3dinput-qaxis.html#value
    """
    #  float Qt3DInput::QAxis::value() const
    return self.uglySide.call('ritual_ZNK9Qt3DInput5QAxis5valueEv')

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
    Notes what was given, for Qt's 'Qt3DInput::QAxis::QAxis(Qt3DCore::QNode
    *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qt3dinput-qaxis.html#QAxis

    Parameters
    ----------

    parent : Optional[Qt3DCore.QNode]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  Qt3DInput::QAxis::QAxis(Qt3DCore::QNode *parent)
    self._noteCreation(QAxis, lambda: Rituals.call(
        'ritual_ZN9Qt3DInput5QAxisC1EPN8Qt3DCore5QNodeE',
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

  @overload(WAIT['Qt3DInput.QAbstractAxisInput'])
  @overload(NoneType)
  def addInput(self, input: Optional[Qt3DInput.QAbstractAxisInput]) -> None:
    """
    Calls Qt's 'void Qt3DInput::QAxis::addInput(QAbstractAxisInput *input)'.

    Qt's own words: https://doc.qt.io/qt-6/qt3dinput-qaxis.html#addInput

    Parameters
    ----------

    input : Optional[Qt3DInput.QAbstractAxisInput]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DInput::QAxis::addInput(QAbstractAxisInput *input)
    self.uglySide.call(
        'ritual_ZN9Qt3DInput5QAxis8addInputEPNS_18QAbstractAxisInputE',
        self._addressOf(input),
    )

  @overload(WAIT['Qt3DInput.QAbstractAxisInput'])
  @overload(NoneType)
  def removeInput(
      self,
      input: Optional[Qt3DInput.QAbstractAxisInput],
  ) -> None:
    """
    Calls Qt's 'void Qt3DInput::QAxis::removeInput(QAbstractAxisInput
    *input)'.

    Qt's own words: https://doc.qt.io/qt-6/qt3dinput-qaxis.html#removeInput

    Parameters
    ----------

    input : Optional[Qt3DInput.QAbstractAxisInput]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DInput::QAxis::removeInput(QAbstractAxisInput *input)
    self.uglySide.call(
        'ritual_ZN9Qt3DInput5QAxis11removeInputEPNS_18QAbstractAxisInputE',
        self._addressOf(input),
    )

  @overload(float)
  def valueChanged(self, value: float) -> None:
    """
    Calls Qt's 'void Qt3DInput::QAxis::valueChanged(float value)'.

    Qt's own words: https://doc.qt.io/qt-6/qt3dinput-qaxis.html#valueChanged

    Parameters
    ----------

    value : float
      Passed on as it is.
    """
    #  void Qt3DInput::QAxis::valueChanged(float value)
    self.uglySide.call('ritual_ZN9Qt3DInput5QAxis12valueChangedEf', value)

  def d_func(self) -> Optional[Qt3DInput.QAxisPrivate]:
    """
    Calls Qt's 'QAxisPrivate *Qt3DInput::QAxis::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qt3dinput-qaxis.html#d_func

    Returns
    -------

    Optional[Qt3DInput.QAxisPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAxisPrivate *Qt3DInput::QAxis::d_func()
    address = self.uglySide.call('ritual_ZN9Qt3DInput5QAxis6d_funcEv')
    return Qt3DInput.QAxisPrivate._cuteAt(address)

  @staticmethod
  def inputs(*__, **_) -> Never:
    """
    Qt's 'QList<QAbstractAxisInput *> Qt3DInput::QAxis::inputs() const':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'Qt3DInput.QAxis.inputs' has no cute function yet. Qt's "
        "'QList<QAbstractAxisInput *> Qt3DInput::QAxis::inputs() const': "
        "gives a type Python has no way to take yet.")
