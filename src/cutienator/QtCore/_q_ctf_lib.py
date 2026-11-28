"""
QCtfLib binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/6.12.0/QtCore/private/qctf_p.h, Qt 6.12.0. Changes made here are
#  lost.
#
#  Qt means QCtfLib to be private: it declares the class in a header it calls
#  private. cutienator does not care. Qt hands objects of the class out all
#  the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from . import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QByteArray, QCtfTracePointEvent, QMetaObject
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']
  QCtfTracePointEvent = WAIT['QCtfTracePointEvent']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QCtfLib(QObject):
  """
  The cute side of Qt's QCtfLib: a plain Python object standing in front of
  one C++ QCtfLib.

  It is built on the cute 'QObject', as Qt's QCtfLib is built on Qt's
  QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QCtfLib that has a ritual and that Python can call
  so far, 5 names in all: 'metaObject', 'tr', 'tracepointEnabled',
  'doTracepoint', 'sessionEnabled'. None can be made from Python: one comes
  out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QCtfLib::qt_metacast(const char *a0)': one of Qt's own inner
    workings.
  - Qt's 'int QCtfLib::qt_metacall(QMetaObject::Call a0, int a1, void **a2)':
    one of Qt's own inner workings.
  - Qt's 'QCtfLib::~QCtfLib()': the destructor: Python never removes a C++
    QCtfLib.
  - Qt's 'QCtfTracePointPrivate *QCtfLib::initializeTracepoint(const
    QCtfTracePointEvent &point)': gives 'QCtfTracePointPrivate', which has no
    cute class yet.
  - Qt's 'void QCtfLib::shutdown(bool *shutdown)': takes a number to change
    where it is.

  What has no ritual
  ------------------

  5 of the 15 functions Qt declares: 2 not a gap; 2 forbidden; 1 the class is
  abstract, so C++ cannot make one, and the C++ class of ours does not fill
  in every function it leaves open.

  What to expect
  --------------

  - The C++ QCtfLib is created at the first use, not by 'QCtfLib(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QCtfLib.
  - Qt tells when it has removed the C++ QCtfLib. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
  - Each name of Qt's QCtfLib that has no cute function yet, '__init__',
    'initializeTracepoint', 'shutdown', holds a function that raises
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
    Calls Qt's 'QString QCtfLib::tr(const char *s, const char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qctflib.html#tr

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
    #  QString QCtfLib::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN7QCtfLib2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QCtfLib'

  #  A C++ QCtfLib Python makes is of a C++ class of ours, in which Python
  #  can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QCtfLib'

  #  The functions Qt calls itself that QCtfLib is the first to declare and
  #  that cannot be handed to Python yet, each as Qt declares it. A class of
  #  a program that writes one of them anew is refused, since Qt would never
  #  call what it wrote; see 'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'initializeTracepoint': (
          'QCtfTracePointPrivate *QCtfLib::initializeTracepoint(const '
          'QCtfTracePointEvent &)',
      ),
      'shutdown': (
          'void QCtfLib::shutdown(bool *)',
      ),
  }

  #  The functions Qt calls itself that QCtfLib is the first to declare. A
  #  class of a program built on it can write one anew, and Qt then calls
  #  that. For each name: the key C++ knows the function by, what it gives,
  #  and what it takes.
  __virtual_functions__ = {
      'tracepointEnabled': (
          ('_ZN7QCtfLib17tracepointEnabledERK19QCtfTracePointEvent',
           ('bool', 'number', ''),
           (
               ('address', 'value', 'QtCore:QCtfTracePointEvent'),
           )),
      ),
      'doTracepoint': (
          ('_ZN7QCtfLib12doTracepointERK19QCtfTracePointEventRK10QByteArray',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtCore:QCtfTracePointEvent'),
               ('address', 'value', 'QtCore:QByteArray'),
           )),
      ),
      'sessionEnabled': (
          ('_ZN7QCtfLib14sessionEnabledEv',
           ('bool', 'number', ''),
           ()),
      ),
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QCtfLib::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qctflib.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QCtfLib::metaObject() const
    address = self.uglySide.call('ritual_ZNK7QCtfLib10metaObjectEv')
    from . import QMetaObject
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
    Qt's 'QCtfLib::QCtfLib(QObject *parent)': the class is abstract, so C++
    cannot make one, and the C++ class of ours does not fill in every
    function it leaves open.
    """
    raise NotImplementedError(
        "'QCtfLib.__init__' has no cute function yet. Qt's "
        "'QCtfLib::QCtfLib(QObject *parent)': the class is abstract, so C++ "
        "cannot make one, and the C++ class of ours does not fill in every "
        "function it leaves open.")

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

  @overload(QCtfTracePointEvent)
  def tracepointEnabled(self, point: QCtfTracePointEvent) -> bool:
    """
    Calls Qt's 'bool QCtfLib::tracepointEnabled(const QCtfTracePointEvent
    &point)'.

    Qt's own words: https://doc.qt.io/qt-6/qctflib.html#tracepointEnabled

    Parameters
    ----------

    point : QCtfTracePointEvent
      Passed on as a value: Qt reads the C++ QCtfTracePointEvent, which stays
      Python's own.
    """
    #  bool QCtfLib::tracepointEnabled(const QCtfTracePointEvent &point)
    return self.uglySide.call(
        'ritual_ZN7QCtfLib17tracepointEnabledERK19QCtfTracePointEvent',
        self._valueOf(point),
    )

  @overload(QCtfTracePointEvent, QByteArray)
  def doTracepoint(
      self,
      point: QCtfTracePointEvent,
      arr: QByteArray,
  ) -> None:
    """
    Calls Qt's 'void QCtfLib::doTracepoint(const QCtfTracePointEvent &point,
    const QByteArray &arr)'.

    Qt's own words: https://doc.qt.io/qt-6/qctflib.html#doTracepoint

    Parameters
    ----------

    point : QCtfTracePointEvent
      Passed on as a value: Qt reads the C++ QCtfTracePointEvent, which stays
      Python's own.

    arr : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void QCtfLib::doTracepoint(const QCtfTracePointEvent &point, const
    #      QByteArray &arr)
    self.uglySide.call(
        'ritual_ZN7QCtfLib12doTracepointERK19QCtfTracePointEventRK10QByteAr'
        'ray',
        self._valueOf(point), self._valueOf(arr),
    )

  def sessionEnabled(self) -> bool:
    """
    Calls Qt's 'bool QCtfLib::sessionEnabled()'.

    Qt's own words: https://doc.qt.io/qt-6/qctflib.html#sessionEnabled
    """
    #  bool QCtfLib::sessionEnabled()
    return self.uglySide.call('ritual_ZN7QCtfLib14sessionEnabledEv')

  @staticmethod
  def initializeTracepoint(*__, **_) -> Never:
    """
    Qt's 'QCtfTracePointPrivate *QCtfLib::initializeTracepoint(const
    QCtfTracePointEvent &point)': gives 'QCtfTracePointPrivate', which has no
    cute class yet.
    """
    raise NotImplementedError(
        "'QCtfLib.initializeTracepoint' has no cute function yet. Qt's "
        "'QCtfTracePointPrivate *QCtfLib::initializeTracepoint(const "
        "QCtfTracePointEvent &point)': gives 'QCtfTracePointPrivate', which "
        "has no cute class yet.")

  @staticmethod
  def shutdown(*__, **_) -> Never:
    """
    Qt's 'void QCtfLib::shutdown(bool *shutdown)': takes a number to change
    where it is.
    """
    raise NotImplementedError(
        "'QCtfLib.shutdown' has no cute function yet. Qt's 'void "
        "QCtfLib::shutdown(bool *shutdown)': takes a number to change where "
        "it is.")
