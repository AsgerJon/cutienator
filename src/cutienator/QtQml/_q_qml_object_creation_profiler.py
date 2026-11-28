"""
QQmlObjectCreationProfiler binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qqmlprofiler_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QQmlObjectCreationProfiler to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from . import QV4

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QUrl
  from . import QQmlProfiler
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQmlProfiler = WAIT['QQmlProfiler']
  QUrl = WAIT['QUrl']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQmlObjectCreationProfiler(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQmlObjectCreationProfiler: a plain Python object
  standing in front of one C++ QQmlObjectCreationProfiler.

  C++ hands a QQmlObjectCreationProfiler around as a copy, so every C++
  QQmlObjectCreationProfiler behind a cute one is Python's own: it is
  removed, by the ritual named in '__delete_ritual__', when the cute object
  goes.

  What exists
  -----------

  Every function of Qt's QQmlObjectCreationProfiler that has a ritual and
  that Python can call so far, 1 name in all: 'update'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QQmlObjectCreationProfiler::~QQmlObjectCreationProfiler()': the
    destructor: Python removes its C++ QQmlObjectCreationProfiler by it, and
    has no other use for it.

  What to expect
  --------------

  - The C++ QQmlObjectCreationProfiler is created at the first use, not by
    'QQmlObjectCreationProfiler(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QQmlObjectCreationProfiler back gives a copy the
    ritual made for Python, in a new cute QQmlObjectCreationProfiler.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlObjectCreationProfiler'

  #  Qt's '~QQmlObjectCreationProfiler()'. Naming it makes this a value
  #  class: Python owns every C++ QQmlObjectCreationProfiler behind a cute
  #  one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN26QQmlObjectCreationProfilerD1Ev'

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

  @overload(QQmlProfiler, WAIT['QV4.CompiledData.Object'])
  @overload(QQmlProfiler, NoneType)
  @overload(NoneType, WAIT['QV4.CompiledData.Object'])
  @overload(NoneType, NoneType)
  def __init__(
      self,
      profiler: Optional[QQmlProfiler],
      obj: Optional[QV4.CompiledData.Object],
  ) -> None:
    """
    Notes what was given, for Qt's
    'QQmlObjectCreationProfiler::QQmlObjectCreationProfiler(QQmlProfiler
    *profiler, const QV4::CompiledData::Object *obj)', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlobjectcreationprofiler.html

    Parameters
    ----------

    profiler : Optional[QQmlProfiler]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    obj : Optional[QV4.CompiledData.Object]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QQmlObjectCreationProfiler::QQmlObjectCreationProfiler(QQmlProfiler
    #      *profiler, const QV4::CompiledData::Object *obj)
    self._noteCreation(QQmlObjectCreationProfiler, lambda: Rituals.call(
        'ritual_ZN26QQmlObjectCreationProfilerC1EP12QQmlProfilerPKN3QV412Co'
        'mpiledData6ObjectE',
        self._addressOf(profiler), self._addressOf(obj),
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

  @overload(
      WAIT['QV4.ExecutableCompilationUnit'], WAIT['QV4.CompiledData.Object'],
      str, QUrl,
  )
  @overload(WAIT['QV4.ExecutableCompilationUnit'], NoneType, str, QUrl)
  @overload(NoneType, WAIT['QV4.CompiledData.Object'], str, QUrl)
  @overload(NoneType, NoneType, str, QUrl)
  def update(
      self,
      ref: Optional[QV4.ExecutableCompilationUnit],
      obj: Optional[QV4.CompiledData.Object],
      typeName: str,
      url: QUrl,
  ) -> None:
    """
    Calls Qt's 'void
    QQmlObjectCreationProfiler::update(QV4::ExecutableCompilationUnit *ref,
    const QV4::CompiledData::Object *obj, const QString &typeName, const QUrl
    &url)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlobjectcreationprofiler.html#update

    Parameters
    ----------

    ref : Optional[QV4.ExecutableCompilationUnit]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    obj : Optional[QV4.CompiledData.Object]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    typeName : str
      Passed on as it is: a QString is made of it for the call.

    url : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  void QQmlObjectCreationProfiler::update(QV4::ExecutableCompilationUnit
    #      *ref, const QV4::CompiledData::Object *obj, const QString
    #      &typeName, const QUrl &url)
    self.uglySide.call(
        'ritual_ZN26QQmlObjectCreationProfiler6updateEPN3QV425ExecutableCom'
        'pilationUnitEPKNS0_12CompiledData6ObjectERK7QStringRK4QUrl',
        self._addressOf(ref), self._addressOf(obj), typeName,
        self._valueOf(url),
    )
