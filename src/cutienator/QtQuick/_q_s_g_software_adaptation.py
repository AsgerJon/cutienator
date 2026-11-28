"""
QSGSoftwareAdaptation binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qsgsoftwareadaptation_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QSGSoftwareAdaptation to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..QtCore import QStringList
from . import QSGContextFactoryInterface, QSGContextPlugin

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QSGContext, QSGRenderLoop


class QSGSoftwareAdaptation(QSGContextPlugin):
  """
  The cute side of Qt's QSGSoftwareAdaptation: a plain Python object standing
  in front of one C++ QSGSoftwareAdaptation.

  It is built on the cute 'QSGContextPlugin', as Qt's QSGSoftwareAdaptation
  is built on Qt's QSGContextPlugin, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QSGSoftwareAdaptation that has a ritual and that
  Python can call so far, 4 names in all: 'keys', 'create', 'flags',
  'createWindowManager'. None can be made from Python: one comes out of a
  function of another class that gives one back.

  What has no ritual
  ------------------

  1 of the 5 functions Qt declares: 1 leans on 'QSGSoftwareAdaptation.

  What to expect
  --------------

  - The C++ QSGSoftwareAdaptation is created at the first use, not by
    'QSGSoftwareAdaptation(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSGSoftwareAdaptation.
  - Qt tells when it has removed the C++ QSGSoftwareAdaptation. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QSGSoftwareAdaptation that has no cute function yet,
    '__init__', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSGSoftwareAdaptation'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def keys(self) -> QStringList:
    """
    Calls Qt's 'QStringList QSGSoftwareAdaptation::keys() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsgsoftwareadaptation.html#keys

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QSGSoftwareAdaptation::keys() const
    address = self.uglySide.call('ritual_ZNK21QSGSoftwareAdaptation4keysEv')
    return QStringList._cuteOwning(address)

  @overload(str)
  def create(self, key: str) -> Optional[QSGContext]:
    """
    Calls Qt's 'QSGContext *QSGSoftwareAdaptation::create(const QString &key)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qsgsoftwareadaptation.html#create

    Parameters
    ----------

    key : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    Optional[QSGContext]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSGContext *QSGSoftwareAdaptation::create(const QString &key) const
    address = self.uglySide.call(
        'ritual_ZNK21QSGSoftwareAdaptation6createERK7QString', key,
    )
    from . import QSGContext
    return QSGContext._cuteAt(address)

  @overload(str)
  def flags(self, key: str) -> QSGContextFactoryInterface.Flags:
    """
    Calls Qt's 'QSGContextFactoryInterface::Flags
    QSGSoftwareAdaptation::flags(const QString &key) const'.

    Qt's own words: https://doc.qt.io/qt-6/qsgsoftwareadaptation.html#flags

    Parameters
    ----------

    key : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QSGContextFactoryInterface.Flags
      The value standing for the combination Qt gave back.
    """
    #  QSGContextFactoryInterface::Flags QSGSoftwareAdaptation::flags(const
    #      QString &key) const
    ritual = 'ritual_ZNK21QSGSoftwareAdaptation5flagsERK7QString'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK21QSGSoftwareAdaptation5flagsERK7QString'
    return QSGContextFactoryInterface.Flags(self.uglySide.call(ritual, key))

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
    Qt's 'QSGSoftwareAdaptation::QSGSoftwareAdaptation(QObject *parent)':
    leans on 'QSGSoftwareAdaptation::instance', which Qt's source does not
    mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QSGSoftwareAdaptation.__init__' has no cute function yet. Qt's "
        "'QSGSoftwareAdaptation::QSGSoftwareAdaptation(QObject *parent)': "
        "leans on 'QSGSoftwareAdaptation::instance', which Qt's source does "
        "not mark for use from outside Qt and has no code for that could be "
        "taken.")

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

  def createWindowManager(self) -> Optional[QSGRenderLoop]:
    """
    Calls Qt's 'QSGRenderLoop *QSGSoftwareAdaptation::createWindowManager()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsoftwareadaptation.html#createWindowManager

    Returns
    -------

    Optional[QSGRenderLoop]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSGRenderLoop *QSGSoftwareAdaptation::createWindowManager()
    address = self.uglySide.call(
        'ritual_ZN21QSGSoftwareAdaptation19createWindowManagerEv',
    )
    from . import QSGRenderLoop
    return QSGRenderLoop._cuteAt(address)
