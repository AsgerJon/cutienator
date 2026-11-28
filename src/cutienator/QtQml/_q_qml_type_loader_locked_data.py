"""
QQmlTypeLoaderLockedData binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qqmltypeloaderdata_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QQmlTypeLoaderLockedData to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from . import QV4

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QQmlTypeLoaderThread

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQmlTypeLoaderLockedData(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQmlTypeLoaderLockedData: a plain Python object
  standing in front of one C++ QQmlTypeLoaderLockedData.

  What exists
  -----------

  Every function of Qt's QQmlTypeLoaderLockedData that has a ritual and that
  Python can call so far, 3 names in all: 'thread', 'engine',
  'isCurrentJsEngineThread'. It can be made from Python, in 1 way; see
  '__init__'.

  What has no ritual
  ------------------

  6 of the 10 functions Qt declares: 4 forbidden; 2 leans on 'QQmlThread.

  What to expect
  --------------

  - The C++ QQmlTypeLoaderLockedData is created at the first use, not by
    'QQmlTypeLoaderLockedData(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQmlTypeLoaderLockedData.
  - Each name of Qt's QQmlTypeLoaderLockedData that has no cute function yet,
    'createThread', 'deleteThread', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlTypeLoaderLockedData'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def thread(self) -> Optional[QQmlTypeLoaderThread]:
    """
    Calls Qt's 'QQmlTypeLoaderThread *QQmlTypeLoaderLockedData::thread()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmltypeloaderlockeddata.html#thread

    Returns
    -------

    Optional[QQmlTypeLoaderThread]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlTypeLoaderThread *QQmlTypeLoaderLockedData::thread() const
    address = self.uglySide.call(
        'ritual_ZNK24QQmlTypeLoaderLockedData6threadEv',
    )
    from . import QQmlTypeLoaderThread
    return QQmlTypeLoaderThread._cuteAt(address)

  def engine(self) -> Optional[QV4.ExecutionEngine]:
    """
    Calls Qt's 'QV4::ExecutionEngine *QQmlTypeLoaderLockedData::engine()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmltypeloaderlockeddata.html#engine

    Returns
    -------

    Optional[QV4.ExecutionEngine]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QV4::ExecutionEngine *QQmlTypeLoaderLockedData::engine() const
    address = self.uglySide.call(
        'ritual_ZNK24QQmlTypeLoaderLockedData6engineEv',
    )
    return QV4.ExecutionEngine._cuteAt(address)

  def isCurrentJsEngineThread(self) -> bool:
    """
    Calls Qt's 'bool QQmlTypeLoaderLockedData::isCurrentJsEngineThread()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmltypeloaderlockeddata.html
    """
    #  bool QQmlTypeLoaderLockedData::isCurrentJsEngineThread() const
    return self.uglySide.call(
        'ritual_ZNK24QQmlTypeLoaderLockedData23isCurrentJsEngineThreadEv',
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

  @overload(WAIT['QV4.ExecutionEngine'])
  @overload(NoneType)
  def __init__(self, engine: Optional[QV4.ExecutionEngine]) -> None:
    """
    Notes what was given, for Qt's
    'QQmlTypeLoaderLockedData::QQmlTypeLoaderLockedData(QV4::ExecutionEngine
    *engine)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmltypeloaderlockeddata.html

    Parameters
    ----------

    engine : Optional[QV4.ExecutionEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QQmlTypeLoaderLockedData::QQmlTypeLoaderLockedData(QV4::
    #      ExecutionEngine *engine)
    self._noteCreation(QQmlTypeLoaderLockedData, lambda: Rituals.call(
        'ritual_ZN24QQmlTypeLoaderLockedDataC1EPN3QV415ExecutionEngineE',
        self._addressOf(engine),
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
  def createThread(*__, **_) -> Never:
    """
    Qt's 'void QQmlTypeLoaderLockedData::createThread(QQmlTypeLoader
    *loader)': leans on 'QQmlThread::startup()', which Qt's source does not
    mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQmlTypeLoaderLockedData.createThread' has no cute function yet. "
        "Qt's 'void QQmlTypeLoaderLockedData::createThread(QQmlTypeLoader "
        "*loader)': leans on 'QQmlThread::startup()', which Qt's source "
        "does not mark for use from outside Qt and has no code for that "
        "could be taken.")

  @staticmethod
  def deleteThread(*__, **_) -> Never:
    """
    Qt's 'void QQmlTypeLoaderLockedData::deleteThread()': leans on
    'QQmlThread::shutdown()', which Qt's source does not mark for use from
    outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQmlTypeLoaderLockedData.deleteThread' has no cute function yet. "
        "Qt's 'void QQmlTypeLoaderLockedData::deleteThread()': leans on "
        "'QQmlThread::shutdown()', which Qt's source does not mark for use "
        "from outside Qt and has no code for that could be taken.")
