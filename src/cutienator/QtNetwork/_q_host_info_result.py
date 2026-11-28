"""
QHostInfoResult binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtNetwork/6.12.0/QtNetwork/private/qhostinfo_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QHostInfoResult to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..QtCore import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
  from . import QHostInfo
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QHostInfo = WAIT['QHostInfo']


class QHostInfoResult(QObject):
  """
  The cute side of Qt's QHostInfoResult: a plain Python object standing in
  front of one C++ QHostInfoResult.

  It is built on the cute 'QObject', as Qt's QHostInfoResult is built on Qt's
  QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QHostInfoResult that has a ritual and that Python
  can call so far, 3 names in all: 'metaObject', 'resultsReady',
  'finalizePostResultsReady'. None can be made from Python: one comes out of
  a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QHostInfoResult::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QHostInfoResult::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QHostInfoResult::~QHostInfoResult()': the destructor: Python never
    removes a C++ QHostInfoResult.

  What has no ritual
  ------------------

  6 of the 12 functions Qt declares: 3 leans on 'QHostInfoResult; 2 not a
  gap; 1 the compiler refuses its ritual as it would be written here.

  What to expect
  --------------

  - The C++ QHostInfoResult is created at the first use, not by
    'QHostInfoResult(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QHostInfoResult.
  - Qt tells when it has removed the C++ QHostInfoResult. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QHostInfoResult that has no cute function yet,
    '__init__', 'postResultsReady', holds a function that raises
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
  __qt_class__ = 'QHostInfoResult'

  #  A C++ QHostInfoResult Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QHostInfoResult'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QHostInfoResult::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qhostinforesult.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QHostInfoResult::metaObject() const
    address = self.uglySide.call('ritual_ZNK15QHostInfoResult10metaObjectEv')
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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    - Qt's 'QHostInfoResult::QHostInfoResult(const QObject *receiver,
      QtPrivate::SlotObjUniquePtr slot)': the compiler refuses its ritual as
      it would be written here: call to deleted constructor of
      'QtPrivate::SlotObjUniquePtr' (aka 'std::unique_ptr<QSlotObjectBase,
      QSlotObjectBase::Deleter>').
    - Qt's 'QHostInfoResult::QHostInfoResult(QHostInfoResult *other)': leans
      on 'QHostInfoResult::qt_metacall(QMetaObject::Call, int, void**)',
      which Qt's source does not mark for use from outside Qt and has no code
      for that could be taken.
    """
    raise NotImplementedError(
        "'QHostInfoResult.__init__' has no cute function yet. Qt's "
        "'QHostInfoResult::QHostInfoResult(const QObject *receiver, "
        "QtPrivate::SlotObjUniquePtr slot)': the compiler refuses its "
        "ritual as it would be written here: call to deleted constructor of "
        "'QtPrivate::SlotObjUniquePtr' (aka "
        "'std::unique_ptr<QSlotObjectBase, QSlotObjectBase::Deleter>'). "
        "Qt's 'QHostInfoResult::QHostInfoResult(QHostInfoResult *other)': "
        "leans on 'QHostInfoResult::qt_metacall(QMetaObject::Call, int, "
        "void**)', which Qt's source does not mark for use from outside Qt "
        "and has no code for that could be taken.")

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

  @overload(QHostInfo)
  def resultsReady(self, info: QHostInfo) -> None:
    """
    Calls Qt's 'void QHostInfoResult::resultsReady(const QHostInfo &info)'.

    Qt's own words: https://doc.qt.io/qt-6/qhostinforesult.html#resultsReady

    Parameters
    ----------

    info : QHostInfo
      Passed on as a value: Qt reads the C++ QHostInfo, which stays Python's
      own.
    """
    #  void QHostInfoResult::resultsReady(const QHostInfo &info)
    self.uglySide.call(
        'ritual_ZN15QHostInfoResult12resultsReadyERK9QHostInfo',
        self._valueOf(info),
    )

  @overload(QHostInfo)
  def finalizePostResultsReady(self, info: QHostInfo) -> None:
    """
    Calls Qt's 'void QHostInfoResult::finalizePostResultsReady(const
    QHostInfo &info)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhostinforesult.html#finalizePostResultsReady

    Parameters
    ----------

    info : QHostInfo
      Passed on as a value: Qt reads the C++ QHostInfo, which stays Python's
      own.
    """
    #  void QHostInfoResult::finalizePostResultsReady(const QHostInfo &info)
    self.uglySide.call(
        'ritual_ZN15QHostInfoResult24finalizePostResultsReadyERK9QHostInfo',
        self._valueOf(info),
    )

  @staticmethod
  def postResultsReady(*__, **_) -> Never:
    """
    Qt's 'void QHostInfoResult::postResultsReady(const QHostInfo &info)':
    leans on 'QHostInfoResult::resultsReady(QHostInfo const&)', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'QHostInfoResult.postResultsReady' has no cute function yet. Qt's "
        "'void QHostInfoResult::postResultsReady(const QHostInfo &info)': "
        "leans on 'QHostInfoResult::resultsReady(QHostInfo const&)', which "
        "Qt's source does not mark for use from outside Qt and has no code "
        "for that could be taken.")
