"""
QtVirtualKeyboard::UnipenTrace binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtVirtualKeyboard/6.12.0/QtVirtualKeyboard/private/unipentrace_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QtVirtualKeyboard::UnipenTrace to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QList, QMap, QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QVariant
  from . import QVirtualKeyboardTrace
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QVariant = WAIT['QVariant']
  QVirtualKeyboardTrace = WAIT['QVirtualKeyboardTrace']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class UnipenTrace(QObject):
  """
  The cute side of Qt's QtVirtualKeyboard::UnipenTrace: a plain Python object
  standing in front of one C++ QtVirtualKeyboard::UnipenTrace.

  It is built on the cute 'QObject', as Qt's QtVirtualKeyboard::UnipenTrace
  is built on Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QtVirtualKeyboard::UnipenTrace that has a ritual and
  that Python can call so far, 6 names in all: 'metaObject', 'tr', 'record',
  'save', 'directory', 'setDirectory'. It can be made from Python, in 1 way;
  see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QtVirtualKeyboard::UnipenTrace::qt_metacast(const char *a0)':
    one of Qt's own inner workings.
  - Qt's 'int QtVirtualKeyboard::UnipenTrace::qt_metacall(QMetaObject::Call
    a0, int a1, void **a2)': one of Qt's own inner workings.

  What has no ritual
  ------------------

  2 of the 11 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QtVirtualKeyboard::UnipenTrace is created at the first use, not
    by 'QtVirtualKeyboard::UnipenTrace(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QtVirtualKeyboard::UnipenTrace.
  - Qt tells when it has removed the C++ QtVirtualKeyboard::UnipenTrace.
    Every call on the cute object, and every use of it as an argument, then
    raises 'RuntimeError', and nothing reaches C++.
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
    Calls Qt's 'QString QtVirtualKeyboard::UnipenTrace::tr(const char *s,
    const char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-unipentrace.html#tr

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
    #  QString QtVirtualKeyboard::UnipenTrace::tr(const char *s, const char
    #      *c, int n)
    return Rituals.call(
        'ritual_ZN17QtVirtualKeyboard11UnipenTrace2trEPKcS2_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QtVirtualKeyboard::UnipenTrace'

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
    *QtVirtualKeyboard::UnipenTrace::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-unipentrace.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QtVirtualKeyboard::UnipenTrace::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK17QtVirtualKeyboard11UnipenTrace10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def directory(self) -> str:
    """
    Calls Qt's 'QString QtVirtualKeyboard::UnipenTrace::directory() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-unipentrace.html#directory

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QtVirtualKeyboard::UnipenTrace::directory() const
    return self.uglySide.call(
        'ritual_ZNK17QtVirtualKeyboard11UnipenTrace9directoryEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setDirectory(self, directory: str) -> None:
    """
    Calls Qt's 'void QtVirtualKeyboard::UnipenTrace::setDirectory(const
    QString &directory)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-unipentrace.html#setDirectory

    Parameters
    ----------

    directory : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QtVirtualKeyboard::UnipenTrace::setDirectory(const QString
    #      &directory)
    self.uglySide.call(
        'ritual_ZN17QtVirtualKeyboard11UnipenTrace12setDirectoryERK7QString',
        directory,
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

  @overload(QMap[str, QVariant], QMap[str, QVariant])
  @overload(QMap[str, QVariant], QMap[str, QVariant], QObject)
  @overload(QMap[str, QVariant], QMap[str, QVariant], NoneType)
  def __init__(
      self,
      traceCaptureDeviceInfo: QMap[str, QVariant],
      traceScreenInfo: QMap[str, QVariant],
      parent: Optional[QObject] = None,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QtVirtualKeyboard::UnipenTrace::UnipenTrace(const QVariantMap
    &traceCaptureDeviceInfo, const QVariantMap &traceScreenInfo, QObject
    *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-unipentrace.html#UnipenTrace

    Parameters
    ----------

    traceCaptureDeviceInfo : QMap[str, QVariant]
      Passed on as a map of Qt: Qt reads the C++ map, which stays Python's
      own. A dict of Python is made into one first, and refused when a key or
      a value does not fit.

    traceScreenInfo : QMap[str, QVariant]
      Passed on as a map of Qt: Qt reads the C++ map, which stays Python's
      own. A dict of Python is made into one first, and refused when a key or
      a value does not fit.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QtVirtualKeyboard::UnipenTrace::UnipenTrace(const QVariantMap
    #      &traceCaptureDeviceInfo, const QVariantMap &traceScreenInfo,
    #      QObject *parent)
    self._noteCreation(UnipenTrace, lambda: Rituals.call(
        'ritual_ZN17QtVirtualKeyboard11UnipenTraceC1ERK4QMapI7QString8QVari'
        'antES6_P7QObject',
        self._valueOf(traceCaptureDeviceInfo),
        self._valueOf(traceScreenInfo), self._addressOf(parent, 'QObject'),
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

  @overload(QList[QVirtualKeyboardTrace])
  def record(self, traceList: QList[QVirtualKeyboardTrace]) -> None:
    """
    Calls Qt's 'void QtVirtualKeyboard::UnipenTrace::record(const
    QList<QVirtualKeyboardTrace *> &traceList)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-unipentrace.html#record

    Parameters
    ----------

    traceList : QList[QVirtualKeyboardTrace]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QtVirtualKeyboard::UnipenTrace::record(const
    #      QList<QVirtualKeyboardTrace *> &traceList)
    self.uglySide.call(
        'ritual_ZN17QtVirtualKeyboard11UnipenTrace6recordERK5QListIP21QVirt'
        'ualKeyboardTraceE',
        self._valueOf(traceList),
    )

  @overload(int, int)
  def save(self, unicode: int, confidence: int) -> None:
    """
    Calls Qt's 'void QtVirtualKeyboard::UnipenTrace::save(uint unicode, uint
    confidence)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-unipentrace.html#save

    Parameters
    ----------

    unicode : int
      Passed on as it is.

    confidence : int
      Passed on as it is.
    """
    #  void QtVirtualKeyboard::UnipenTrace::save(uint unicode, uint
    #      confidence)
    self.uglySide.call(
        'ritual_ZN17QtVirtualKeyboard11UnipenTrace4saveEjj',
        unicode, confidence,
    )
