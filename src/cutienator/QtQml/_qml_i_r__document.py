"""
QmlIR::Document binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qqmlirbuilder_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QmlIR::Document to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from . import QmlIR

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional


class Document(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QmlIR::Document: a plain Python object standing in
  front of one C++ QmlIR::Document.

  What exists
  -----------

  Every function of Qt's QmlIR::Document that has a ritual and that Python
  can call so far, 5 names in all: 'isSingleton', 'registerString',
  'stringAt', 'objectCount', 'objectAt'. It can be made from Python, in 1
  way; see '__init__'.

  What has no ritual
  ------------------

  4 of the 10 functions Qt declares: 4 forbidden.

  What to expect
  --------------

  - The C++ QmlIR::Document is created at the first use, not by
    'QmlIR::Document(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QmlIR::Document.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QmlIR::Document'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isSingleton(self) -> bool:
    """
    Calls Qt's 'bool QmlIR::Document::isSingleton() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmlir-document.html#isSingleton
    """
    #  bool QmlIR::Document::isSingleton() const
    return self.uglySide.call('ritual_ZNK5QmlIR8Document11isSingletonEv')

  @overload(int)
  def stringAt(self, index: int) -> str:
    """
    Calls Qt's 'QString QmlIR::Document::stringAt(int index) const'.

    Qt's own words: https://doc.qt.io/qt-6/qmlir-document.html#stringAt

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QmlIR::Document::stringAt(int index) const
    return self.uglySide.call('ritual_ZNK5QmlIR8Document8stringAtEi', index)

  def objectCount(self) -> int:
    """
    Calls Qt's 'int QmlIR::Document::objectCount() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmlir-document.html#objectCount
    """
    #  int QmlIR::Document::objectCount() const
    return self.uglySide.call('ritual_ZNK5QmlIR8Document11objectCountEv')

  @overload(int)
  def objectAt(self, i: int) -> Optional[QmlIR.Object]:
    """
    Calls Qt's 'Object *QmlIR::Document::objectAt(int i) const'.

    Qt's own words: https://doc.qt.io/qt-6/qmlir-document.html#objectAt

    Parameters
    ----------

    i : int
      Passed on as it is.

    Returns
    -------

    Optional[QmlIR.Object]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Object *QmlIR::Document::objectAt(int i) const
    address = self.uglySide.call('ritual_ZNK5QmlIR8Document8objectAtEi', i)
    return QmlIR.Object._cuteAt(address)

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

  @overload(str, str, bool)
  def __init__(self, fileName: str, finalUrl: str, debugMode: bool) -> None:
    """
    Notes what was given, for Qt's 'QmlIR::Document::Document(const QString
    &fileName, const QString &finalUrl, bool debugMode)', which is called at
    the first use.

    Qt's own words: https://doc.qt.io/qt-6/qmlir-document.html#Document

    Parameters
    ----------

    fileName : str
      Passed on as it is: a QString is made of it for the call.

    finalUrl : str
      Passed on as it is: a QString is made of it for the call.

    debugMode : bool
      Passed on as it is.
    """
    #  QmlIR::Document::Document(const QString &fileName, const QString
    #      &finalUrl, bool debugMode)
    self._noteCreation(Document, lambda: Rituals.call(
        'ritual_ZN5QmlIR8DocumentC1ERK7QStringS3_b',
        fileName, finalUrl, debugMode,
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

  @overload(str)
  def registerString(self, str: str) -> int:
    """
    Calls Qt's 'int QmlIR::Document::registerString(const QString &str)'.

    Qt's own words: https://doc.qt.io/qt-6/qmlir-document.html#registerString

    Parameters
    ----------

    str : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  int QmlIR::Document::registerString(const QString &str)
    return self.uglySide.call(
        'ritual_ZN5QmlIR8Document14registerStringERK7QString', str,
    )
