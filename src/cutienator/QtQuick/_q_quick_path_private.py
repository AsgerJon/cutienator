"""
QQuickPathPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquickpath_p_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QQuickPathPrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import QObjectPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QQuickPath, QQuickPathElement
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQuickPath = WAIT['QQuickPath']
  QQuickPathElement = WAIT['QQuickPathElement']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickPathPrivate(QObjectPrivate):
  """
  The cute side of Qt's QQuickPathPrivate: a plain Python object standing in
  front of one C++ QQuickPathPrivate.

  It is built on the cute 'QObjectPrivate', as Qt's QQuickPathPrivate is
  built on Qt's QObjectPrivate, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickPathPrivate that has a ritual and that Python
  can call so far, 8 names in all: 'q_func', 'get', 'appendPathElement',
  'removeLastPathElement', 'replacePathElement', 'clearPathElements',
  'enablePathElement', 'disablePathElement'. It can be made from Python, in 1
  way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QQuickPath *QQuickPathPrivate::q_func() const': takes in
    Python what 'QQuickPath *QQuickPathPrivate::q_func()' takes.
  - Qt's 'const QQuickPathPrivate *QQuickPathPrivate::get(const QQuickPath
    *path)': takes in Python what 'QQuickPathPrivate
    *QQuickPathPrivate::get(QQuickPath *path)' takes.

  What to expect
  --------------

  - The C++ QQuickPathPrivate is created at the first use, not by
    'QQuickPathPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickPathPrivate.
  """

  #  The enums Qt writes inside QQuickPathPrivate, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class DeleteElementPolicy(CuteNum, scoped=True):
    """
    The enum 'QQuickPathPrivate::DeleteElementPolicy' of Qt, with the 2 names
    Qt gives in it. C++ keeps these names inside the enum, so the class that
    holds the enum does not have them.
    """

    DontDelete = Kee[int](0)
    Delete = Kee[int](1)

  class ProcessPathPolicy(CuteNum, scoped=True):
    """
    The enum 'QQuickPathPrivate::ProcessPathPolicy' of Qt, with the 2 names
    Qt gives in it. C++ keeps these names inside the enum, so the class that
    holds the enum does not have them.
    """

    DontProcess = Kee[int](0)
    Process = Kee[int](1)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QQuickPath)
  @overload(NoneType)
  def get(path: Optional[QQuickPath]) -> Optional[QQuickPathPrivate]:
    """
    Calls Qt's 'QQuickPathPrivate *QQuickPathPrivate::get(QQuickPath *path)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpathprivate.html#get

    Parameters
    ----------

    path : Optional[QQuickPath]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QQuickPathPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickPathPrivate *QQuickPathPrivate::get(QQuickPath *path)
    address = Rituals.call(
        'ritual_ZN17QQuickPathPrivate3getEP10QQuickPath',
        CuteMixin._addressOf(path),
    )
    return QQuickPathPrivate._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickPathPrivate'

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
    Notes what was given, for Qt's 'QQuickPathPrivate::QQuickPathPrivate()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpathprivate.html#QQuickPathPrivate
    """
    #  QQuickPathPrivate::QQuickPathPrivate()
    self._noteCreation(QQuickPathPrivate, lambda: Rituals.call(
        'ritual_ZN17QQuickPathPrivateC1Ev',
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

  def q_func(self) -> Optional[QQuickPath]:
    """
    Calls Qt's 'QQuickPath *QQuickPathPrivate::q_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpathprivate.html#q_func

    Returns
    -------

    Optional[QQuickPath]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickPath *QQuickPathPrivate::q_func()
    address = self.uglySide.call('ritual_ZN17QQuickPathPrivate6q_funcEv')
    from . import QQuickPath
    return QQuickPath._cuteAt(address)

  @overload(QQuickPathElement)
  @overload(NoneType)
  @overload(QQuickPathElement, ProcessPathPolicy)
  @overload(NoneType, ProcessPathPolicy)
  def appendPathElement(
      self,
      pathElement: Optional[QQuickPathElement],
      processPathPolicy: ProcessPathPolicy = ProcessPathPolicy.Process,
  ) -> None:
    """
    Calls Qt's 'void QQuickPathPrivate::appendPathElement(QQuickPathElement
    *pathElement, ProcessPathPolicy processPathPolicy)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpathprivate.html#appendPathElement

    Parameters
    ----------

    pathElement : Optional[QQuickPathElement]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    processPathPolicy : ProcessPathPolicy
      Passed on as its number. May be left out, as in Qt: it is then
      ProcessPathPolicy.Process.
    """
    #  void QQuickPathPrivate::appendPathElement(QQuickPathElement
    #      *pathElement, ProcessPathPolicy processPathPolicy)
    self.uglySide.call(
        'ritual_ZN17QQuickPathPrivate17appendPathElementEP17QQuickPathEleme'
        'ntNS_17ProcessPathPolicyE',
        self._addressOf(pathElement), processPathPolicy.value,
    )

  def removeLastPathElement(self) -> None:
    """
    Calls Qt's 'void QQuickPathPrivate::removeLastPathElement()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpathprivate.html#removeLastPathElement
    """
    #  void QQuickPathPrivate::removeLastPathElement()
    self.uglySide.call(
        'ritual_ZN17QQuickPathPrivate21removeLastPathElementEv',
    )

  @overload(int, QQuickPathElement)
  @overload(int, NoneType)
  def replacePathElement(
      self,
      position: int,
      pathElement: Optional[QQuickPathElement],
  ) -> None:
    """
    Calls Qt's 'void QQuickPathPrivate::replacePathElement(qsizetype
    position, QQuickPathElement *pathElement)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpathprivate.html#replacePathElement

    Parameters
    ----------

    position : int
      Passed on as it is.

    pathElement : Optional[QQuickPathElement]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickPathPrivate::replacePathElement(qsizetype position,
    #      QQuickPathElement *pathElement)
    self.uglySide.call(
        'ritual_ZN17QQuickPathPrivate18replacePathElementExP17QQuickPathEle'
        'ment',
        position, self._addressOf(pathElement),
    )

  @overload()
  @overload(DeleteElementPolicy)
  def clearPathElements(
      self,
      deleteElementPolicy: DeleteElementPolicy = (
          DeleteElementPolicy.DontDelete),
  ) -> None:
    """
    Calls Qt's 'void QQuickPathPrivate::clearPathElements(DeleteElementPolicy
    deleteElementPolicy)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpathprivate.html#clearPathElements

    Parameters
    ----------

    deleteElementPolicy : DeleteElementPolicy
      Passed on as its number. May be left out, as in Qt: it is then
      DeleteElementPolicy.DontDelete.
    """
    #  void QQuickPathPrivate::clearPathElements(DeleteElementPolicy
    #      deleteElementPolicy)
    self.uglySide.call(
        'ritual_ZN17QQuickPathPrivate17clearPathElementsENS_19DeleteElement'
        'PolicyE',
        deleteElementPolicy.value,
    )

  @overload(QQuickPathElement)
  @overload(NoneType)
  def enablePathElement(
      self,
      pathElement: Optional[QQuickPathElement],
  ) -> None:
    """
    Calls Qt's 'void QQuickPathPrivate::enablePathElement(QQuickPathElement
    *pathElement)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpathprivate.html#enablePathElement

    Parameters
    ----------

    pathElement : Optional[QQuickPathElement]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickPathPrivate::enablePathElement(QQuickPathElement
    #      *pathElement)
    self.uglySide.call(
        'ritual_ZN17QQuickPathPrivate17enablePathElementEP17QQuickPathEleme'
        'nt',
        self._addressOf(pathElement),
    )

  @overload(QQuickPathElement)
  @overload(NoneType)
  def disablePathElement(
      self,
      pathElement: Optional[QQuickPathElement],
  ) -> None:
    """
    Calls Qt's 'void QQuickPathPrivate::disablePathElement(QQuickPathElement
    *pathElement)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpathprivate.html#disablePathElement

    Parameters
    ----------

    pathElement : Optional[QQuickPathElement]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickPathPrivate::disablePathElement(QQuickPathElement
    #      *pathElement)
    self.uglySide.call(
        'ritual_ZN17QQuickPathPrivate18disablePathElementEP17QQuickPathElem'
        'ent',
        self._addressOf(pathElement),
    )
