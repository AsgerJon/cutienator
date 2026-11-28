"""
Qt3DCore::QAspectFactory binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DCore/6.12.0/Qt3DCore/private/qaspectfactory_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means Qt3DCore::QAspectFactory to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QList
from . import Qt3DCore

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QLatin1String, QObject
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QLatin1String = WAIT['QLatin1String']
  QObject = WAIT['QObject']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QAspectFactory(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's Qt3DCore::QAspectFactory: a plain Python object
  standing in front of one C++ Qt3DCore::QAspectFactory.

  C++ hands a Qt3DCore::QAspectFactory around as a copy, so every C++
  Qt3DCore::QAspectFactory behind a cute one is Python's own: it is removed,
  by the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's Qt3DCore::QAspectFactory that has a ritual and that
  Python can call so far, 3 names in all: 'availableFactories',
  'createAspect', 'aspectName'. It can be made from Python, in 2 ways; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'Qt3DCore::QAspectFactory::~QAspectFactory()': the destructor:
    Python removes its C++ Qt3DCore::QAspectFactory by it, and has no other
    use for it.
  - Qt's 'QAspectFactory &Qt3DCore::QAspectFactory::operator=(const
    QAspectFactory &other)': assignment: Python binds a name and has no
    operator for it.
  - Qt's 'QAspectFactory &Qt3DCore::QAspectFactory::operator=(QAspectFactory
    &&other)': assignment: Python binds a name and has no operator for it.
  - Qt's 'void Qt3DCore::QAspectFactory::swap(QAspectFactory &other)': takes
    a type Python has no way to hand over yet.

  What to expect
  --------------

  - The C++ Qt3DCore::QAspectFactory is created at the first use, not by
    'Qt3DCore::QAspectFactory(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a Qt3DCore::QAspectFactory back gives a copy the ritual
    made for Python, in a new cute Qt3DCore::QAspectFactory.
  - Each name of Qt's Qt3DCore::QAspectFactory that has no cute function yet,
    'swap', holds a function that raises 'NotImplementedError', and its
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
  __qt_class__ = 'Qt3DCore::QAspectFactory'

  #  Qt's '~Qt3DCore::QAspectFactory()'. Naming it makes this a value class:
  #  Python owns every C++ Qt3DCore::QAspectFactory behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN8Qt3DCore14QAspectFactoryD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def availableFactories(self) -> QList[QLatin1String]:
    """
    Calls Qt's 'QList<QLatin1String>
    Qt3DCore::QAspectFactory::availableFactories() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qaspectfactory.html#availableFactories

    Returns
    -------

    QList[QLatin1String]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QLatin1String> Qt3DCore::QAspectFactory::availableFactories()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK8Qt3DCore14QAspectFactory18availableFactoriesEv',
    )
    from ..QtCore import QLatin1String
    return QList[QLatin1String]._cuteOwning(address)

  @overload(QLatin1String)
  @overload(QLatin1String, QObject)
  @overload(QLatin1String, NoneType)
  def createAspect(
      self,
      aspect: QLatin1String,
      parent: Optional[QObject] = None,
  ) -> Optional[Qt3DCore.QAbstractAspect]:
    """
    Calls Qt's 'QAbstractAspect *Qt3DCore::QAspectFactory::createAspect(const
    QLatin1String &aspect, QObject *parent) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qaspectfactory.html#createAspect

    Parameters
    ----------

    aspect : QLatin1String
      Passed on as a value: Qt reads the C++ QLatin1String, which stays
      Python's own.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    Returns
    -------

    Optional[Qt3DCore.QAbstractAspect]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractAspect *Qt3DCore::QAspectFactory::createAspect(const
    #      QLatin1String &aspect, QObject *parent) const
    address = self.uglySide.call(
        'ritual_ZNK8Qt3DCore14QAspectFactory12createAspectERK13QLatin1Strin'
        'gP7QObject',
        self._valueOf(aspect), self._addressOf(parent, 'QObject'),
    )
    return Qt3DCore.QAbstractAspect._cuteAt(address)

  @overload(WAIT['Qt3DCore.QAbstractAspect'])
  @overload(NoneType)
  def aspectName(
      self,
      aspect: Optional[Qt3DCore.QAbstractAspect],
  ) -> QLatin1String:
    """
    Calls Qt's 'QLatin1String
    Qt3DCore::QAspectFactory::aspectName(QAbstractAspect *aspect) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qaspectfactory.html#aspectName

    Parameters
    ----------

    aspect : Optional[Qt3DCore.QAbstractAspect]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QLatin1String
      A new cute QLatin1String around the copy Qt gave back. Python owns it.
    """
    #  QLatin1String Qt3DCore::QAspectFactory::aspectName(QAbstractAspect
    #      *aspect) const
    address = self.uglySide.call(
        'ritual_ZNK8Qt3DCore14QAspectFactory10aspectNameEPNS_15QAbstractAsp'
        'ectE',
        self._addressOf(aspect),
    )
    from ..QtCore import QLatin1String
    return QLatin1String._cuteOwning(address)

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
    Notes what was given, for Qt's
    'Qt3DCore::QAspectFactory::QAspectFactory()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qaspectfactory.html#QAspectFactory
    """
    #  Qt3DCore::QAspectFactory::QAspectFactory()
    self._noteCreation(QAspectFactory, lambda: Rituals.call(
        'ritual_ZN8Qt3DCore14QAspectFactoryC1Ev',
    ))

  @overload(THIS)
  def __init__(self, other: QAspectFactory) -> None:
    """
    Notes what was given, for Qt's
    'Qt3DCore::QAspectFactory::QAspectFactory(const QAspectFactory &other)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qaspectfactory.html#QAspectFactory

    Parameters
    ----------

    other : QAspectFactory
      Passed on as a value: Qt reads the C++ Qt3DCore::QAspectFactory, which
      stays Python's own.
    """
    #  Qt3DCore::QAspectFactory::QAspectFactory(const QAspectFactory &other)
    self._noteCreation(QAspectFactory, lambda: Rituals.call(
        'ritual_ZN8Qt3DCore14QAspectFactoryC1ERKS0_', self._valueOf(other),
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
  def swap(*__, **_) -> Never:
    """
    Qt's 'void Qt3DCore::QAspectFactory::swap(QAspectFactory &other)': takes
    a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'Qt3DCore.QAspectFactory.swap' has no cute function yet. Qt's "
        "'void Qt3DCore::QAspectFactory::swap(QAspectFactory &other)': "
        "takes a type Python has no way to hand over yet.")
