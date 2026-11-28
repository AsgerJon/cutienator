"""
Qt3DCore::QAbstractAspectJobManager binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DCore/6.12.0/Qt3DCore/private/qabstractaspectjobmanager_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means Qt3DCore::QAbstractAspectJobManager to be private: it declares
#  the class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin
from ..occult import Rituals
from ..QtCore import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QAbstractAspectJobManager(QObject):
  """
  The cute side of Qt's Qt3DCore::QAbstractAspectJobManager: a plain Python
  object standing in front of one C++ Qt3DCore::QAbstractAspectJobManager.

  It is built on the cute 'QObject', as Qt's
  Qt3DCore::QAbstractAspectJobManager is built on Qt's QObject, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DCore::QAbstractAspectJobManager that has a
  ritual and that Python can call so far, 4 names in all: 'metaObject', 'tr',
  'initialize', 'waitForAllJobs'. None can be made from Python: one comes out
  of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *Qt3DCore::QAbstractAspectJobManager::qt_metacast(const char
    *a0)': one of Qt's own inner workings.
  - Qt's 'int
    Qt3DCore::QAbstractAspectJobManager::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'void Qt3DCore::QAbstractAspectJobManager::enqueueJobs(const
    std::vector<QAspectJobPtr> &jobQueue)': takes a type Python has no way to
    hand over yet.
  - Qt's 'void
    Qt3DCore::QAbstractAspectJobManager::waitForPerThreadFunction(JobFunction
    func, void *arg)': takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  3 of the 11 functions Qt declares: 2 not a gap; 1 the class is abstract, so
  C++ cannot make one, and the C++ class of ours does not fill in every
  function it leaves open.

  What to expect
  --------------

  - The C++ Qt3DCore::QAbstractAspectJobManager is created at the first use,
    not by 'Qt3DCore::QAbstractAspectJobManager(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DCore::QAbstractAspectJobManager.
  - Qt tells when it has removed the C++ Qt3DCore::QAbstractAspectJobManager.
    Every call on the cute object, and every use of it as an argument, then
    raises 'RuntimeError', and nothing reaches C++.
  - Each name of Qt's Qt3DCore::QAbstractAspectJobManager that has no cute
    function yet, '__init__', 'enqueueJobs', 'waitForPerThreadFunction',
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
    Calls Qt's 'QString Qt3DCore::QAbstractAspectJobManager::tr(const char
    *s, const char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qabstractaspectjobmanager.html#tr

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
    #  QString Qt3DCore::QAbstractAspectJobManager::tr(const char *s, const
    #      char *c, int n)
    return Rituals.call(
        'ritual_ZN8Qt3DCore25QAbstractAspectJobManager2trEPKcS2_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DCore::QAbstractAspectJobManager'

  #  A C++ Qt3DCore::QAbstractAspectJobManager Python makes is of a C++ class
  #  of ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DCore_QAbstractAspectJobManager'

  #  The functions Qt calls itself that Qt3DCore::QAbstractAspectJobManager
  #  is the first to declare and that cannot be handed to Python yet, each as
  #  Qt declares it. A class of a program that writes one of them anew is
  #  refused, since Qt would never call what it wrote; see
  #  'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'enqueueJobs': (
          'void Qt3DCore::QAbstractAspectJobManager::enqueueJobs(const '
          'std::vector<QAspectJobPtr> &)',
      ),
      'waitForPerThreadFunction': (
          'void '
          'Qt3DCore::QAbstractAspectJobManager::waitForPerThreadFunction(Jo'
          'bFunction, void *)',
      ),
  }

  #  The functions Qt calls itself that Qt3DCore::QAbstractAspectJobManager
  #  is the first to declare. A class of a program built on it can write one
  #  anew, and Qt then calls that. For each name: the key C++ knows the
  #  function by, what it gives, and what it takes.
  __virtual_functions__ = {
      'initialize': (
          ('_ZN8Qt3DCore25QAbstractAspectJobManager10initializeEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'waitForAllJobs': (
          ('_ZN8Qt3DCore25QAbstractAspectJobManager14waitForAllJobsEv',
           ('int', 'number', ''),
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
    Calls Qt's 'const QMetaObject
    *Qt3DCore::QAbstractAspectJobManager::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qabstractaspectjobmanager.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *Qt3DCore::QAbstractAspectJobManager::metaObject()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK8Qt3DCore25QAbstractAspectJobManager10metaObjectEv',
    )
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
    Qt's
    'Qt3DCore::QAbstractAspectJobManager::QAbstractAspectJobManager(QObject
    *p)': the class is abstract, so C++ cannot make one, and the C++ class of
    ours does not fill in every function it leaves open.
    """
    raise NotImplementedError(
        "'Qt3DCore.QAbstractAspectJobManager.__init__' has no cute function "
        "yet. Qt's "
        "'Qt3DCore::QAbstractAspectJobManager::QAbstractAspectJobManager(QOb"
        "ject *p)': the class is abstract, so C++ cannot make one, and the "
        "C++ class of ours does not fill in every function it leaves open.")

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

  def initialize(self) -> None:
    """
    Calls Qt's 'void Qt3DCore::QAbstractAspectJobManager::initialize()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qabstractaspectjobmanager.html#initialize
    """
    #  void Qt3DCore::QAbstractAspectJobManager::initialize()
    ritual = 'ritual_ZN8Qt3DCore25QAbstractAspectJobManager10initializeEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN8Qt3DCore25QAbstractAspectJobManager10initializeEv')
    self.uglySide.call(ritual)

  def waitForAllJobs(self) -> int:
    """
    Calls Qt's 'int Qt3DCore::QAbstractAspectJobManager::waitForAllJobs()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qabstractaspectjobmanager.html
    """
    #  int Qt3DCore::QAbstractAspectJobManager::waitForAllJobs()
    return self.uglySide.call(
        'ritual_ZN8Qt3DCore25QAbstractAspectJobManager14waitForAllJobsEv',
    )

  @staticmethod
  def enqueueJobs(*__, **_) -> Never:
    """
    Qt's 'void Qt3DCore::QAbstractAspectJobManager::enqueueJobs(const
    std::vector<QAspectJobPtr> &jobQueue)': takes a type Python has no way to
    hand over yet.
    """
    raise NotImplementedError(
        "'Qt3DCore.QAbstractAspectJobManager.enqueueJobs' has no cute "
        "function yet. Qt's 'void "
        "Qt3DCore::QAbstractAspectJobManager::enqueueJobs(const "
        "std::vector<QAspectJobPtr> &jobQueue)': takes a type Python has no "
        "way to hand over yet.")

  @staticmethod
  def waitForPerThreadFunction(*__, **_) -> Never:
    """
    Qt's 'void
    Qt3DCore::QAbstractAspectJobManager::waitForPerThreadFunction(JobFunction
    func, void *arg)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'Qt3DCore.QAbstractAspectJobManager.waitForPerThreadFunction' has "
        "no cute function yet. Qt's 'void "
        "Qt3DCore::QAbstractAspectJobManager::waitForPerThreadFunction(JobFu"
        "nction func, void *arg)': takes a type Python has no way to hand "
        "over yet.")
