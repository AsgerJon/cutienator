"""
Qt3DInput::QInputChord binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DInput/qinputchord.h, Qt 6.12.0. Changes made here are lost.
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


class QInputChord(Qt3DInput.QAbstractActionInput):
  """
  The cute side of Qt's Qt3DInput::QInputChord: a plain Python object
  standing in front of one C++ Qt3DInput::QInputChord.

  It is built on the cute 'Qt3DInput::QAbstractActionInput', as Qt's
  Qt3DInput::QInputChord is built on Qt's Qt3DInput::QAbstractActionInput,
  and has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DInput::QInputChord that has a ritual and that
  Python can call so far, 8 names in all: 'metaObject', 'tr', 'timeout',
  'addChord', 'removeChord', 'setTimeout', 'timeoutChanged', 'd_func'. It can
  be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *Qt3DInput::QInputChord::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int Qt3DInput::QInputChord::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'Qt3DInput::QInputChord::~QInputChord()': the destructor: Python
    never removes a C++ Qt3DInput::QInputChord.
  - Qt's 'QList<QAbstractActionInput *> Qt3DInput::QInputChord::chords()
    const': gives a type Python has no way to take yet.
  - Qt's 'const QInputChordPrivate *Qt3DInput::QInputChord::d_func() const':
    takes in Python what 'QInputChordPrivate
    *Qt3DInput::QInputChord::d_func()' takes.

  What has no ritual
  ------------------

  2 of the 16 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ Qt3DInput::QInputChord is created at the first use, not by
    'Qt3DInput::QInputChord(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DInput::QInputChord.
  - Qt tells when it has removed the C++ Qt3DInput::QInputChord. Every call
    on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's Qt3DInput::QInputChord that has no cute function yet,
    'chords', holds a function that raises 'NotImplementedError', and its
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
    Calls Qt's 'QString Qt3DInput::QInputChord::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qt3dinput-qinputchord.html#tr

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
    #  QString Qt3DInput::QInputChord::tr(const char *s, const char *c, int
    #      n)
    return Rituals.call(
        'ritual_ZN9Qt3DInput11QInputChord2trEPKcS2_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DInput::QInputChord'

  #  A C++ Qt3DInput::QInputChord Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DInput_QInputChord'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *Qt3DInput::QInputChord::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qinputchord.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *Qt3DInput::QInputChord::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK9Qt3DInput11QInputChord10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def timeout(self) -> int:
    """
    Calls Qt's 'int Qt3DInput::QInputChord::timeout() const'.

    Qt's own words: https://doc.qt.io/qt-6/qt3dinput-qinputchord.html#timeout
    """
    #  int Qt3DInput::QInputChord::timeout() const
    return self.uglySide.call('ritual_ZNK9Qt3DInput11QInputChord7timeoutEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setTimeout(self, timeout: int) -> None:
    """
    Calls Qt's 'void Qt3DInput::QInputChord::setTimeout(int timeout)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qinputchord.html#setTimeout

    Parameters
    ----------

    timeout : int
      Passed on as it is.
    """
    #  void Qt3DInput::QInputChord::setTimeout(int timeout)
    self.uglySide.call(
        'ritual_ZN9Qt3DInput11QInputChord10setTimeoutEi', timeout,
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
  @overload(Qt3DCore.QNode)
  @overload(NoneType)
  def __init__(self, parent: Optional[Qt3DCore.QNode] = None) -> None:
    """
    Notes what was given, for Qt's
    'Qt3DInput::QInputChord::QInputChord(Qt3DCore::QNode *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qinputchord.html#QInputChord

    Parameters
    ----------

    parent : Optional[Qt3DCore.QNode]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  Qt3DInput::QInputChord::QInputChord(Qt3DCore::QNode *parent)
    self._noteCreation(QInputChord, lambda: Rituals.call(
        'ritual_ZN9Qt3DInput11QInputChordC1EPN8Qt3DCore5QNodeE',
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

  @overload(Qt3DInput.QAbstractActionInput)
  @overload(NoneType)
  def addChord(
      self,
      input: Optional[Qt3DInput.QAbstractActionInput],
  ) -> None:
    """
    Calls Qt's 'void Qt3DInput::QInputChord::addChord(QAbstractActionInput
    *input)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qinputchord.html#addChord

    Parameters
    ----------

    input : Optional[Qt3DInput.QAbstractActionInput]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DInput::QInputChord::addChord(QAbstractActionInput *input)
    self.uglySide.call(
        'ritual_ZN9Qt3DInput11QInputChord8addChordEPNS_20QAbstractActionInp'
        'utE',
        self._addressOf(input),
    )

  @overload(Qt3DInput.QAbstractActionInput)
  @overload(NoneType)
  def removeChord(
      self,
      input: Optional[Qt3DInput.QAbstractActionInput],
  ) -> None:
    """
    Calls Qt's 'void Qt3DInput::QInputChord::removeChord(QAbstractActionInput
    *input)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qinputchord.html#removeChord

    Parameters
    ----------

    input : Optional[Qt3DInput.QAbstractActionInput]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DInput::QInputChord::removeChord(QAbstractActionInput *input)
    self.uglySide.call(
        'ritual_ZN9Qt3DInput11QInputChord11removeChordEPNS_20QAbstractActio'
        'nInputE',
        self._addressOf(input),
    )

  @overload(int)
  def timeoutChanged(self, timeout: int) -> None:
    """
    Calls Qt's 'void Qt3DInput::QInputChord::timeoutChanged(int timeout)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qinputchord.html#timeoutChanged

    Parameters
    ----------

    timeout : int
      Passed on as it is.
    """
    #  void Qt3DInput::QInputChord::timeoutChanged(int timeout)
    self.uglySide.call(
        'ritual_ZN9Qt3DInput11QInputChord14timeoutChangedEi', timeout,
    )

  def d_func(self) -> Optional[Qt3DInput.QInputChordPrivate]:
    """
    Calls Qt's 'QInputChordPrivate *Qt3DInput::QInputChord::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qt3dinput-qinputchord.html#d_func

    Returns
    -------

    Optional[Qt3DInput.QInputChordPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QInputChordPrivate *Qt3DInput::QInputChord::d_func()
    address = self.uglySide.call('ritual_ZN9Qt3DInput11QInputChord6d_funcEv')
    return Qt3DInput.QInputChordPrivate._cuteAt(address)

  @staticmethod
  def chords(*__, **_) -> Never:
    """
    Qt's 'QList<QAbstractActionInput *> Qt3DInput::QInputChord::chords()
    const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'Qt3DInput.QInputChord.chords' has no cute function yet. Qt's "
        "'QList<QAbstractActionInput *> Qt3DInput::QInputChord::chords() "
        "const': gives a type Python has no way to take yet.")
