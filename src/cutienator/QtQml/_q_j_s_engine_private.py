"""
QJSEnginePrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qjsengine_p.h, Qt 6.12.0. Changes made here are
#  lost.
#
#  Qt means QJSEnginePrivate to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObjectPrivate
from . import QV4

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QJSEngine
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QJSEngine = WAIT['QJSEngine']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QJSEnginePrivate(QObjectPrivate):
  """
  The cute side of Qt's QJSEnginePrivate: a plain Python object standing in
  front of one C++ QJSEnginePrivate.

  It is built on the cute 'QObjectPrivate', as Qt's QJSEnginePrivate is built
  on Qt's QObjectPrivate, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QJSEnginePrivate that has a ritual and that Python
  can call so far, 6 names in all: 'q_func', 'get', 'addToDebugServer',
  'removeFromDebugServer', 'uiLanguageChanged',
  '_qt_property_uiLanguage_offset'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QJSEngine *QJSEnginePrivate::q_func() const': takes in Python
    what 'QJSEngine *QJSEnginePrivate::q_func()' takes.
  - Qt's 'const QJSEnginePrivate *QJSEnginePrivate::get(const QJSEngine *e)':
    takes in Python what 'QJSEnginePrivate *QJSEnginePrivate::get(QJSEngine
    *e)' takes.
  - Qt's 'const QJSEngine *QJSEnginePrivate::get(const QJSEnginePrivate *e)':
    takes in Python what 'QJSEnginePrivate *QJSEnginePrivate::get(QJSEngine
    *e)' takes.
  - Qt's 'QJSEnginePrivate::~QJSEnginePrivate()': the destructor: Python
    never removes a C++ QJSEnginePrivate.

  What to expect
  --------------

  - The C++ QJSEnginePrivate is created at the first use, not by
    'QJSEnginePrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QJSEnginePrivate.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QJSEngine)
  @overload(NoneType)
  def get(e: Optional[QJSEngine]) -> Optional[QJSEnginePrivate]:
    """
    Calls Qt's 'QJSEnginePrivate *QJSEnginePrivate::get(QJSEngine *e)'.

    Qt's own words: https://doc.qt.io/qt-6/qjsengineprivate.html#get

    Parameters
    ----------

    e : Optional[QJSEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QJSEnginePrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QJSEnginePrivate *QJSEnginePrivate::get(QJSEngine *e)
    address = Rituals.call(
        'ritual_ZN16QJSEnginePrivate3getEP9QJSEngine',
        CuteMixin._addressOf(e),
    )
    return QJSEnginePrivate._cuteAt(address)

  @staticmethod
  @overload(THIS)
  def get(e: Optional[QJSEnginePrivate]) -> Optional[QJSEngine]:
    """
    Calls Qt's 'QJSEngine *QJSEnginePrivate::get(QJSEnginePrivate *e)'.

    Qt's own words: https://doc.qt.io/qt-6/qjsengineprivate.html#get

    Parameters
    ----------

    e : Optional[QJSEnginePrivate]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QJSEngine]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QJSEngine *QJSEnginePrivate::get(QJSEnginePrivate *e)
    address = Rituals.call(
        'ritual_ZN16QJSEnginePrivate3getEPS_', CuteMixin._addressOf(e),
    )
    from . import QJSEngine
    return QJSEngine._cuteAt(address)

  @staticmethod
  @overload(WAIT['QV4.ExecutionEngine'])
  def get(e: Optional[QV4.ExecutionEngine]) -> Optional[QJSEnginePrivate]:
    """
    Calls Qt's 'QJSEnginePrivate *QJSEnginePrivate::get(QV4::ExecutionEngine
    *e)'.

    Qt's own words: https://doc.qt.io/qt-6/qjsengineprivate.html#get

    Parameters
    ----------

    e : Optional[QV4.ExecutionEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QJSEnginePrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QJSEnginePrivate *QJSEnginePrivate::get(QV4::ExecutionEngine *e)
    address = Rituals.call(
        'ritual_ZN16QJSEnginePrivate3getEPN3QV415ExecutionEngineE',
        CuteMixin._addressOf(e),
    )
    return QJSEnginePrivate._cuteAt(address)

  @staticmethod
  @overload(QJSEngine)
  @overload(NoneType)
  def addToDebugServer(q: Optional[QJSEngine]) -> None:
    """
    Calls Qt's 'void QJSEnginePrivate::addToDebugServer(QJSEngine *q)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qjsengineprivate.html#addToDebugServer

    Parameters
    ----------

    q : Optional[QJSEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QJSEnginePrivate::addToDebugServer(QJSEngine *q)
    Rituals.call(
        'ritual_ZN16QJSEnginePrivate16addToDebugServerEP9QJSEngine',
        CuteMixin._addressOf(q),
    )

  @staticmethod
  @overload(QJSEngine)
  @overload(NoneType)
  def removeFromDebugServer(q: Optional[QJSEngine]) -> None:
    """
    Calls Qt's 'void QJSEnginePrivate::removeFromDebugServer(QJSEngine *q)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qjsengineprivate.html#removeFromDebugServer

    Parameters
    ----------

    q : Optional[QJSEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QJSEnginePrivate::removeFromDebugServer(QJSEngine *q)
    Rituals.call(
        'ritual_ZN16QJSEnginePrivate21removeFromDebugServerEP9QJSEngine',
        CuteMixin._addressOf(q),
    )

  @staticmethod
  def _qt_property_uiLanguage_offset() -> int:
    """
    Calls Qt's 'size_t QJSEnginePrivate::_qt_property_uiLanguage_offset()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qjsengineprivate.html
    """
    #  size_t QJSEnginePrivate::_qt_property_uiLanguage_offset()
    return Rituals.call(
        'ritual_ZN16QJSEnginePrivate30_qt_property_uiLanguage_offsetEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QJSEnginePrivate'

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
    Notes what was given, for Qt's 'QJSEnginePrivate::QJSEnginePrivate()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qjsengineprivate.html#QJSEnginePrivate
    """
    #  QJSEnginePrivate::QJSEnginePrivate()
    self._noteCreation(QJSEnginePrivate, lambda: Rituals.call(
        'ritual_ZN16QJSEnginePrivateC1Ev',
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

  def q_func(self) -> Optional[QJSEngine]:
    """
    Calls Qt's 'QJSEngine *QJSEnginePrivate::q_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qjsengineprivate.html#q_func

    Returns
    -------

    Optional[QJSEngine]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QJSEngine *QJSEnginePrivate::q_func()
    address = self.uglySide.call('ritual_ZN16QJSEnginePrivate6q_funcEv')
    from . import QJSEngine
    return QJSEngine._cuteAt(address)

  def uiLanguageChanged(self) -> None:
    """
    Calls Qt's 'void QJSEnginePrivate::uiLanguageChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qjsengineprivate.html#uiLanguageChanged
    """
    #  void QJSEnginePrivate::uiLanguageChanged()
    self.uglySide.call('ritual_ZN16QJSEnginePrivate17uiLanguageChangedEv')
