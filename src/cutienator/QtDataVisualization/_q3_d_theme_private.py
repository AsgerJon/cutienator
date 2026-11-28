"""
Q3DThemePrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDataVisualization/6.12.0/QtDataVisualization/private/q3dtheme_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means Q3DThemePrivate to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
  from . import Q3DTheme
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  Q3DTheme = WAIT['Q3DTheme']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class Q3DThemePrivate(QObject):
  """
  The cute side of Qt's Q3DThemePrivate: a plain Python object standing in
  front of one C++ Q3DThemePrivate.

  It is built on the cute 'QObject', as Qt's Q3DThemePrivate is built on Qt's
  QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's Q3DThemePrivate that has a ritual and that Python
  can call so far, 8 names in all: 'metaObject', 'tr', 'resetDirtyBits',
  'isDefaultTheme', 'setDefaultTheme', 'isForcePredefinedType',
  'setForcePredefinedType', 'needRender'. It can be made from Python, in 1
  way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *Q3DThemePrivate::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int Q3DThemePrivate::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'Q3DThemePrivate::~Q3DThemePrivate()': the destructor: Python never
    removes a C++ Q3DThemePrivate.
  - Qt's 'bool Q3DThemePrivate::sync(Q3DThemePrivate &other)': takes a type
    Python has no way to hand over yet.

  What has no ritual
  ------------------

  2 of the 15 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ Q3DThemePrivate is created at the first use, not by
    'Q3DThemePrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Q3DThemePrivate.
  - Qt tells when it has removed the C++ Q3DThemePrivate. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's Q3DThemePrivate that has no cute function yet, 'sync',
    holds a function that raises 'NotImplementedError', and its docstring
    says why.
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
    Calls Qt's 'QString Q3DThemePrivate::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/q3dthemeprivate.html#tr

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
    #  QString Q3DThemePrivate::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN15Q3DThemePrivate2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Q3DThemePrivate'

  #  A C++ Q3DThemePrivate Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Q3DThemePrivate'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *Q3DThemePrivate::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/q3dthemeprivate.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *Q3DThemePrivate::metaObject() const
    address = self.uglySide.call('ritual_ZNK15Q3DThemePrivate10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  def setDefaultTheme(self, isDefault: bool) -> None:
    """
    Calls Qt's 'void Q3DThemePrivate::setDefaultTheme(bool isDefault)'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dthemeprivate.html#setDefaultTheme

    Parameters
    ----------

    isDefault : bool
      Passed on as it is.
    """
    #  void Q3DThemePrivate::setDefaultTheme(bool isDefault)
    self.uglySide.call(
        'ritual_ZN15Q3DThemePrivate15setDefaultThemeEb', isDefault,
    )

  @overload(bool)
  def setForcePredefinedType(self, enable: bool) -> None:
    """
    Calls Qt's 'void Q3DThemePrivate::setForcePredefinedType(bool enable)'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dthemeprivate.html#setForcePredefinedType

    Parameters
    ----------

    enable : bool
      Passed on as it is.
    """
    #  void Q3DThemePrivate::setForcePredefinedType(bool enable)
    self.uglySide.call(
        'ritual_ZN15Q3DThemePrivate22setForcePredefinedTypeEb', enable,
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

  @overload(Q3DTheme)
  @overload(NoneType)
  def __init__(self, q: Optional[Q3DTheme]) -> None:
    """
    Notes what was given, for Qt's 'Q3DThemePrivate::Q3DThemePrivate(Q3DTheme
    *q)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dthemeprivate.html#Q3DThemePrivate

    Parameters
    ----------

    q : Optional[Q3DTheme]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  Q3DThemePrivate::Q3DThemePrivate(Q3DTheme *q)
    self._noteCreation(Q3DThemePrivate, lambda: Rituals.call(
        'ritual_ZN15Q3DThemePrivateC1EP8Q3DTheme', self._addressOf(q),
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

  def resetDirtyBits(self) -> None:
    """
    Calls Qt's 'void Q3DThemePrivate::resetDirtyBits()'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dthemeprivate.html#resetDirtyBits
    """
    #  void Q3DThemePrivate::resetDirtyBits()
    self.uglySide.call('ritual_ZN15Q3DThemePrivate14resetDirtyBitsEv')

  def isDefaultTheme(self) -> bool:
    """
    Calls Qt's 'bool Q3DThemePrivate::isDefaultTheme()'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dthemeprivate.html#isDefaultTheme
    """
    #  bool Q3DThemePrivate::isDefaultTheme()
    return self.uglySide.call('ritual_ZN15Q3DThemePrivate14isDefaultThemeEv')

  def isForcePredefinedType(self) -> bool:
    """
    Calls Qt's 'bool Q3DThemePrivate::isForcePredefinedType()'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dthemeprivate.html#isForcePredefinedType
    """
    #  bool Q3DThemePrivate::isForcePredefinedType()
    return self.uglySide.call(
        'ritual_ZN15Q3DThemePrivate21isForcePredefinedTypeEv',
    )

  def needRender(self) -> None:
    """
    Calls Qt's 'void Q3DThemePrivate::needRender()'.

    Qt's own words: https://doc.qt.io/qt-6/q3dthemeprivate.html#needRender
    """
    #  void Q3DThemePrivate::needRender()
    self.uglySide.call('ritual_ZN15Q3DThemePrivate10needRenderEv')

  @staticmethod
  def sync(*__, **_) -> Never:
    """
    Qt's 'bool Q3DThemePrivate::sync(Q3DThemePrivate &other)': takes a type
    Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'Q3DThemePrivate.sync' has no cute function yet. Qt's 'bool "
        "Q3DThemePrivate::sync(Q3DThemePrivate &other)': takes a type "
        "Python has no way to hand over yet.")
