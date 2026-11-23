"""
QOpenGLContextGroup binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/qopenglcontext.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin
from ..occult import Rituals
from ..QtCore import QList, QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from . import QOpenGLContext

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QOpenGLContextGroup(QObject):
  """
  The cute side of Qt's QOpenGLContextGroup: a plain Python object standing
  in front of one C++ QOpenGLContextGroup.

  It is built on the cute 'QObject', as Qt's QOpenGLContextGroup is built on
  Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QOpenGLContextGroup that has a ritual and that
  Python can call so far, 4 names in all: 'metaObject', 'tr', 'shares',
  'currentContextGroup'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QOpenGLContextGroup::~QOpenGLContextGroup()': the destructor:
    Python never removes a C++ QOpenGLContextGroup.

  What has no ritual
  ------------------

  6 of the 12 functions Qt declares: 4 takes or gives a type that cannot be
  passed yet; 1 a template; 1 declared and nowhere to be found.

  What to expect
  --------------

  - The C++ QOpenGLContextGroup is created at the first use, not by
    'QOpenGLContextGroup(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QOpenGLContextGroup.
  - Qt tells when it has removed the C++ QOpenGLContextGroup. Every call on
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
    Calls Qt's 'QString QOpenGLContextGroup::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qopenglcontextgroup.html#tr

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
    #  QString QOpenGLContextGroup::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN19QOpenGLContextGroup2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  def currentContextGroup() -> Optional[QOpenGLContextGroup]:
    """
    Calls Qt's 'QOpenGLContextGroup
    *QOpenGLContextGroup::currentContextGroup()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglcontextgroup.html#currentContextGroup

    Returns
    -------

    Optional[QOpenGLContextGroup]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QOpenGLContextGroup *QOpenGLContextGroup::currentContextGroup()
    address = Rituals.call(
        'ritual_ZN19QOpenGLContextGroup19currentContextGroupEv',
    )
    return QOpenGLContextGroup._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QOpenGLContextGroup'

  #  A C++ QOpenGLContextGroup Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QOpenGLContextGroup'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QOpenGLContextGroup::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglcontextgroup.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QOpenGLContextGroup::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK19QOpenGLContextGroup10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def shares(self) -> QList[QOpenGLContext]:
    """
    Calls Qt's 'QList<QOpenGLContext *> QOpenGLContextGroup::shares() const'.

    Qt's own words: https://doc.qt.io/qt-6/qopenglcontextgroup.html#shares

    Returns
    -------

    QList[QOpenGLContext]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QOpenGLContext *> QOpenGLContextGroup::shares() const
    address = self.uglySide.call('ritual_ZNK19QOpenGLContextGroup6sharesEv')
    from . import QOpenGLContext
    return QList[QOpenGLContext]._cuteOwning(address)

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
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'QOpenGLContextGroup::QOpenGLContextGroup()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglcontextgroup.html#QOpenGLContextGroup
    """
    #  QOpenGLContextGroup::QOpenGLContextGroup()
    self._noteCreation(QOpenGLContextGroup, lambda: Rituals.call(
        'ritual_ZN19QOpenGLContextGroupC1Ev',
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
