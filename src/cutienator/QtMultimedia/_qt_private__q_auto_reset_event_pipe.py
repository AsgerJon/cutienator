"""
QtPrivate::QAutoResetEventPipe binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtMultimedia/6.12.0/QtMultimedia/private/qautoresetevent_pipe_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QtPrivate::QAutoResetEventPipe to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
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


class QAutoResetEventPipe(QObject):
  """
  The cute side of Qt's QtPrivate::QAutoResetEventPipe: a plain Python object
  standing in front of one C++ QtPrivate::QAutoResetEventPipe.

  It is built on the cute 'QObject', as Qt's QtPrivate::QAutoResetEventPipe
  is built on Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QtPrivate::QAutoResetEventPipe that has a ritual and
  that Python can call so far, 5 names in all: 'metaObject', 'tr', 'isValid',
  'set', 'activated'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QtPrivate::QAutoResetEventPipe::qt_metacast(const char *a0)':
    one of Qt's own inner workings.
  - Qt's 'int QtPrivate::QAutoResetEventPipe::qt_metacall(QMetaObject::Call
    a0, int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QtPrivate::QAutoResetEventPipe::~QAutoResetEventPipe()': the
    destructor: Python never removes a C++ QtPrivate::QAutoResetEventPipe.

  What has no ritual
  ------------------

  8 of the 17 functions Qt declares: 4 forbidden; 2 not a gap; 2 a template.

  What to expect
  --------------

  - The C++ QtPrivate::QAutoResetEventPipe is created at the first use, not
    by 'QtPrivate::QAutoResetEventPipe(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QtPrivate::QAutoResetEventPipe.
  - Qt tells when it has removed the C++ QtPrivate::QAutoResetEventPipe.
    Every call on the cute object, and every use of it as an argument, then
    raises 'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QtPrivate::QAutoResetEventPipe that has no cute
    function yet, 'callOnActivated', holds a function that raises
    'NotImplementedError', and its docstring says why.
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
    Calls Qt's 'QString QtPrivate::QAutoResetEventPipe::tr(const char *s,
    const char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtprivate-qautoreseteventpipe.html#tr

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
    #  QString QtPrivate::QAutoResetEventPipe::tr(const char *s, const char
    #      *c, int n)
    return Rituals.call(
        'ritual_ZN9QtPrivate19QAutoResetEventPipe2trEPKcS2_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QtPrivate::QAutoResetEventPipe'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject
    *QtPrivate::QAutoResetEventPipe::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtprivate-qautoreseteventpipe.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QtPrivate::QAutoResetEventPipe::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK9QtPrivate19QAutoResetEventPipe10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool QtPrivate::QAutoResetEventPipe::isValid() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtprivate-qautoreseteventpipe.html#isValid
    """
    #  bool QtPrivate::QAutoResetEventPipe::isValid() const
    return self.uglySide.call(
        'ritual_ZNK9QtPrivate19QAutoResetEventPipe7isValidEv',
    )

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
  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's
    'QtPrivate::QAutoResetEventPipe::QAutoResetEventPipe(QObject *parent)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qtprivate-qautoreseteventpipe.html

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QtPrivate::QAutoResetEventPipe::QAutoResetEventPipe(QObject *parent)
    self._noteCreation(QAutoResetEventPipe, lambda: Rituals.call(
        'ritual_ZN9QtPrivate19QAutoResetEventPipeC1EP7QObject',
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

  def set(self) -> None:
    """
    Calls Qt's 'void QtPrivate::QAutoResetEventPipe::set()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtprivate-qautoreseteventpipe.html#set
    """
    #  void QtPrivate::QAutoResetEventPipe::set()
    self.uglySide.call('ritual_ZN9QtPrivate19QAutoResetEventPipe3setEv')

  def activated(self) -> None:
    """
    Calls Qt's 'void QtPrivate::QAutoResetEventPipe::activated()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtprivate-qautoreseteventpipe.html#activated
    """
    #  void QtPrivate::QAutoResetEventPipe::activated()
    self.uglySide.call(
        'ritual_ZN9QtPrivate19QAutoResetEventPipe9activatedEv',
    )

  @staticmethod
  def callOnActivated(*__, **_) -> Never:
    """
    Qt's 'QtPrivate::QAutoResetEventPipe::callOnActivated': a template: a
    pattern and no single function.
    """
    raise NotImplementedError(
        "'QtPrivate.QAutoResetEventPipe.callOnActivated' has no cute "
        "function yet. Qt's "
        "'QtPrivate::QAutoResetEventPipe::callOnActivated': a template: a "
        "pattern and no single function.")
