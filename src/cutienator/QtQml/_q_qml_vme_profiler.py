"""
QQmlVmeProfiler binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qqmlprofiler_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QQmlVmeProfiler to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from . import QQmlProfilerDefinitions, QV4

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QQmlProfiler
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQmlProfiler = WAIT['QQmlProfiler']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQmlVmeProfiler(QQmlProfilerDefinitions):
  """
  The cute side of Qt's QQmlVmeProfiler: a plain Python object standing in
  front of one C++ QQmlVmeProfiler.

  It is built on the cute 'QQmlProfilerDefinitions', as Qt's QQmlVmeProfiler
  is built on Qt's QQmlProfilerDefinitions, and has everything that class
  has.

  C++ hands a QQmlVmeProfiler around as a copy, so every C++ QQmlVmeProfiler
  behind a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QQmlVmeProfiler that has a ritual and that Python
  can call so far, 3 names in all: 'init', 'pop', 'push'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QQmlVmeProfiler::~QQmlVmeProfiler()': the destructor: Python
    removes its C++ QQmlVmeProfiler by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QQmlVmeProfiler is created at the first use, not by
    'QQmlVmeProfiler(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QQmlVmeProfiler back gives a copy the ritual made for
    Python, in a new cute QQmlVmeProfiler.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlVmeProfiler'

  #  Qt's '~QQmlVmeProfiler()'. Naming it makes this a value class: Python
  #  owns every C++ QQmlVmeProfiler behind a cute one, and removes it by this
  #  ritual.
  __delete_ritual__ = 'ritual_ZN15QQmlVmeProfilerD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

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
    Notes what was given, for Qt's 'QQmlVmeProfiler::QQmlVmeProfiler()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlvmeprofiler.html#QQmlVmeProfiler
    """
    #  QQmlVmeProfiler::QQmlVmeProfiler()
    self._noteCreation(QQmlVmeProfiler, lambda: Rituals.call(
        'ritual_ZN15QQmlVmeProfilerC1Ev',
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

  @overload(QQmlProfiler)
  @overload(NoneType)
  def init(self, p: Optional[QQmlProfiler]) -> None:
    """
    Calls Qt's 'void QQmlVmeProfiler::init(QQmlProfiler *p)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlvmeprofiler.html#init

    Parameters
    ----------

    p : Optional[QQmlProfiler]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlVmeProfiler::init(QQmlProfiler *p)
    self.uglySide.call(
        'ritual_ZN15QQmlVmeProfiler4initEP12QQmlProfiler',
        self._addressOf(p),
    )

  def pop(self) -> Optional[QV4.CompiledData.Object]:
    """
    Calls Qt's 'const QV4::CompiledData::Object *QQmlVmeProfiler::pop()'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlvmeprofiler.html#pop

    Returns
    -------

    Optional[QV4.CompiledData.Object]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QV4::CompiledData::Object *QQmlVmeProfiler::pop()
    address = self.uglySide.call('ritual_ZN15QQmlVmeProfiler3popEv')
    return QV4.CompiledData.Object._cuteAt(address)

  @overload(WAIT['QV4.CompiledData.Object'])
  @overload(NoneType)
  def push(self, object: Optional[QV4.CompiledData.Object]) -> None:
    """
    Calls Qt's 'void QQmlVmeProfiler::push(const QV4::CompiledData::Object
    *object)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlvmeprofiler.html#push

    Parameters
    ----------

    object : Optional[QV4.CompiledData.Object]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlVmeProfiler::push(const QV4::CompiledData::Object *object)
    self.uglySide.call(
        'ritual_ZN15QQmlVmeProfiler4pushEPKN3QV412CompiledData6ObjectE',
        self._addressOf(object),
    )
