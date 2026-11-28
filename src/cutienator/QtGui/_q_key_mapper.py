"""
QKeyMapper binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qkeymapper_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QKeyMapper to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QList, QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QKeyCombination, QMetaObject
  from . import QKeyEvent
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QKeyEvent = WAIT['QKeyEvent']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QKeyMapper(QObject):
  """
  The cute side of Qt's QKeyMapper: a plain Python object standing in front
  of one C++ QKeyMapper.

  It is built on the cute 'QObject', as Qt's QKeyMapper is built on Qt's
  QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QKeyMapper that has a ritual and that Python can
  call so far, 4 names in all: 'metaObject', 'tr', 'instance',
  'possibleKeys'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QKeyMapper::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QKeyMapper::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QKeyMapper::~QKeyMapper()': the destructor: Python never removes a
    C++ QKeyMapper.
  - Qt's 'void *QKeyMapper::resolveInterface(const char *name, int revision)
    const': gives 'void', which has no cute class yet.

  What has no ritual
  ------------------

  7 of the 16 functions Qt declares: 4 forbidden; 2 not a gap; 1 a template.

  What to expect
  --------------

  - The C++ QKeyMapper is created at the first use, not by 'QKeyMapper(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QKeyMapper.
  - Qt tells when it has removed the C++ QKeyMapper. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
  - Each name of Qt's QKeyMapper that has no cute function yet,
    'nativeInterface', 'resolveInterface', holds a function that raises
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
    Calls Qt's 'QString QKeyMapper::tr(const char *s, const char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qkeymapper.html#tr

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
    #  QString QKeyMapper::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN10QKeyMapper2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  def instance() -> Optional[QKeyMapper]:
    """
    Calls Qt's 'QKeyMapper *QKeyMapper::instance()'.

    Qt's own words: https://doc.qt.io/qt-6/qkeymapper.html#instance

    Returns
    -------

    Optional[QKeyMapper]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QKeyMapper *QKeyMapper::instance()
    address = Rituals.call('ritual_ZN10QKeyMapper8instanceEv')
    return QKeyMapper._cuteAt(address)

  @staticmethod
  @overload(QKeyEvent)
  @overload(NoneType)
  def possibleKeys(e: Optional[QKeyEvent]) -> QList[QKeyCombination]:
    """
    Calls Qt's 'QList<QKeyCombination> QKeyMapper::possibleKeys(const
    QKeyEvent *e)'.

    Qt's own words: https://doc.qt.io/qt-6/qkeymapper.html#possibleKeys

    Parameters
    ----------

    e : Optional[QKeyEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QList[QKeyCombination]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QKeyCombination> QKeyMapper::possibleKeys(const QKeyEvent *e)
    address = Rituals.call(
        'ritual_ZN10QKeyMapper12possibleKeysEPK9QKeyEvent',
        CuteMixin._addressOf(e),
    )
    from ..QtCore import QKeyCombination
    return QList[QKeyCombination]._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QKeyMapper'

  #  A C++ QKeyMapper Python makes is of a C++ class of ours, in which Python
  #  can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QKeyMapper'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QKeyMapper::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qkeymapper.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QKeyMapper::metaObject() const
    address = self.uglySide.call('ritual_ZNK10QKeyMapper10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

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
    Notes what was given, for Qt's 'QKeyMapper::QKeyMapper()', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qkeymapper.html#QKeyMapper
    """
    #  QKeyMapper::QKeyMapper()
    self._noteCreation(QKeyMapper, lambda: Rituals.call(
        'ritual_ZN10QKeyMapperC1Ev',
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

  @staticmethod
  def nativeInterface(*__, **_) -> Never:
    """
    Qt's 'QKeyMapper::nativeInterface': a template: a pattern and no single
    function.
    """
    raise NotImplementedError(
        "'QKeyMapper.nativeInterface' has no cute function yet. Qt's "
        "'QKeyMapper::nativeInterface': a template: a pattern and no single "
        "function.")

  @staticmethod
  def resolveInterface(*__, **_) -> Never:
    """
    Qt's 'void *QKeyMapper::resolveInterface(const char *name, int revision)
    const': gives 'void', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QKeyMapper.resolveInterface' has no cute function yet. Qt's 'void "
        "*QKeyMapper::resolveInterface(const char *name, int revision) "
        "const': gives 'void', which has no cute class yet.")
