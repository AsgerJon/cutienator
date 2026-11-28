"""
QSSGAssetImporterFactory binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3DAssetImport/6.12.0/QtQuick3DAssetImport/private/qssgassetimporterfactory_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QSSGAssetImporterFactory to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals
from ..QtCore import QStringList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QSSGAssetImporter


class QSSGAssetImporterFactory(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QSSGAssetImporterFactory: a plain Python object
  standing in front of one C++ QSSGAssetImporterFactory.

  C++ hands a QSSGAssetImporterFactory around as a copy, so every C++
  QSSGAssetImporterFactory behind a cute one is Python's own: it is removed,
  by the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QSSGAssetImporterFactory that has a ritual and that
  Python can call so far, 2 names in all: 'keys', 'create'. None can be made
  from Python: one comes out of a function of another class that gives one
  back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSSGAssetImporterFactory::~QSSGAssetImporterFactory()': the
    destructor: Python removes its C++ QSSGAssetImporterFactory by it, and
    has no other use for it.

  What to expect
  --------------

  - The C++ QSSGAssetImporterFactory is created at the first use, not by
    'QSSGAssetImporterFactory(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QSSGAssetImporterFactory back gives a copy the ritual
    made for Python, in a new cute QSSGAssetImporterFactory.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def keys() -> QStringList:
    """
    Calls Qt's 'QStringList QSSGAssetImporterFactory::keys()'.

    Qt's own words: https://doc.qt.io/qt-6/qssgassetimporterfactory.html#keys

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QSSGAssetImporterFactory::keys()
    address = Rituals.call('ritual_ZN24QSSGAssetImporterFactory4keysEv')
    return QStringList._cuteOwning(address)

  @staticmethod
  @overload(str, QStringList)
  def create(name: str, args: QStringList) -> Optional[QSSGAssetImporter]:
    """
    Calls Qt's 'QSSGAssetImporter *QSSGAssetImporterFactory::create(const
    QString &name, const QStringList &args)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgassetimporterfactory.html#create

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.

    args : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    Returns
    -------

    Optional[QSSGAssetImporter]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSSGAssetImporter *QSSGAssetImporterFactory::create(const QString
    #      &name, const QStringList &args)
    address = Rituals.call(
        'ritual_ZN24QSSGAssetImporterFactory6createERK7QStringRK5QListIS0_E',
        name, CuteMixin._valueOf(args),
    )
    from . import QSSGAssetImporter
    return QSSGAssetImporter._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSSGAssetImporterFactory'

  #  Qt's '~QSSGAssetImporterFactory()'. Naming it makes this a value class:
  #  Python owns every C++ QSSGAssetImporterFactory behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN24QSSGAssetImporterFactoryD1Ev'

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
