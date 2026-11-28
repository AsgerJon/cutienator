"""
ObjectHelper binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDataVisualization/6.12.0/QtDataVisualization/private/objecthelper_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means ObjectHelper to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from ..QtCore import QList
from . import AbstractObjectHelper

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from ..QtGui import QVector2D, QVector3D


class ObjectHelper(AbstractObjectHelper):
  """
  The cute side of Qt's ObjectHelper: a plain Python object standing in front
  of one C++ ObjectHelper.

  It is built on the cute 'AbstractObjectHelper', as Qt's ObjectHelper is
  built on Qt's AbstractObjectHelper, and has everything that class has.

  C++ hands a ObjectHelper around as a copy, so every C++ ObjectHelper behind
  a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's ObjectHelper that has a ritual and that Python can
  call so far, 4 names in all: 'objectFile', 'indexedvertices', 'indexedUVs',
  'indexedNormals'. None can be made from Python: one comes out of a function
  of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'ObjectHelper::~ObjectHelper()': the destructor: Python removes its
    C++ ObjectHelper by it, and has no other use for it.
  - Qt's 'const QList<GLuint> &ObjectHelper::indices() const': gives a type
    Python has no way to take yet.

  What has no ritual
  ------------------

  5 of the 11 functions Qt declares: 2 takes or gives a type that cannot be
  passed yet; 2 leans on 'MeshLoader; 1 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file.

  What to expect
  --------------

  - The C++ ObjectHelper is created at the first use, not by
    'ObjectHelper(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a ObjectHelper back gives a copy the ritual made for
    Python, in a new cute ObjectHelper.
  - Each name of Qt's ObjectHelper that has no cute function yet, '__init__',
    'getObjectHelper', 'indices', 'load', 'releaseObjectHelper',
    'resetObjectHelper', holds a function that raises 'NotImplementedError',
    and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'ObjectHelper'

  #  A C++ ObjectHelper Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_ObjectHelper'

  #  Qt's '~ObjectHelper()'. Naming it makes this a value class: Python owns
  #  every C++ ObjectHelper behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN12ObjectHelperD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def indexedvertices(self) -> QList[QVector3D]:
    """
    Calls Qt's 'const QList<QVector3D> &ObjectHelper::indexedvertices()
    const'.

    Qt's own words: https://doc.qt.io/qt-6/objecthelper.html#indexedvertices

    Returns
    -------

    QList[QVector3D]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  const QList<QVector3D> &ObjectHelper::indexedvertices() const
    address = self.uglySide.call(
        'ritual_ZNK12ObjectHelper15indexedverticesEv',
    )
    from ..QtGui import QVector3D
    return QList[QVector3D]._cuteOwning(address)

  def indexedUVs(self) -> QList[QVector2D]:
    """
    Calls Qt's 'const QList<QVector2D> &ObjectHelper::indexedUVs() const'.

    Qt's own words: https://doc.qt.io/qt-6/objecthelper.html#indexedUVs

    Returns
    -------

    QList[QVector2D]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  const QList<QVector2D> &ObjectHelper::indexedUVs() const
    address = self.uglySide.call('ritual_ZNK12ObjectHelper10indexedUVsEv')
    from ..QtGui import QVector2D
    return QList[QVector2D]._cuteOwning(address)

  def indexedNormals(self) -> QList[QVector3D]:
    """
    Calls Qt's 'const QList<QVector3D> &ObjectHelper::indexedNormals()
    const'.

    Qt's own words: https://doc.qt.io/qt-6/objecthelper.html#indexedNormals

    Returns
    -------

    QList[QVector3D]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  const QList<QVector3D> &ObjectHelper::indexedNormals() const
    address = self.uglySide.call(
        'ritual_ZNK12ObjectHelper14indexedNormalsEv',
    )
    from ..QtGui import QVector3D
    return QList[QVector3D]._cuteOwning(address)

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
    Qt's 'ObjectHelper::ObjectHelper(const QString &objectFile)': leans on
    'MeshLoader::loadOBJ(QString const&, QList<QVector3D>&,
    QList<QVector2D>&, QList<QVector3D>&)', which Qt's source does not mark
    for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'ObjectHelper.__init__' has no cute function yet. Qt's "
        "'ObjectHelper::ObjectHelper(const QString &objectFile)': leans on "
        "'MeshLoader::loadOBJ(QString const&, QList<QVector3D>&, "
        "QList<QVector2D>&, QList<QVector3D>&)', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
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

  def objectFile(self) -> str:
    """
    Calls Qt's 'const QString &ObjectHelper::objectFile()'.

    Qt's own words: https://doc.qt.io/qt-6/objecthelper.html#objectFile

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  const QString &ObjectHelper::objectFile()
    return self.uglySide.call('ritual_ZN12ObjectHelper10objectFileEv')

  @staticmethod
  def getObjectHelper(*__, **_) -> Never:
    """
    Qt's 'ObjectHelper *ObjectHelper::getObjectHelper(const
    Abstract3DRenderer *cacheId, const QString &objectFile)': Qt's library
    has no name for it, and its code in Qt's source does not compile apart
    from its file: use of undeclared identifier 'ObjectHelperRef'.
    """
    raise NotImplementedError(
        "'ObjectHelper.getObjectHelper' has no cute function yet. Qt's "
        "'ObjectHelper *ObjectHelper::getObjectHelper(const "
        "Abstract3DRenderer *cacheId, const QString &objectFile)': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: use of undeclared identifier "
        "'ObjectHelperRef'.")

  @staticmethod
  def indices(*__, **_) -> Never:
    """
    Qt's 'const QList<GLuint> &ObjectHelper::indices() const': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'ObjectHelper.indices' has no cute function yet. Qt's 'const "
        "QList<GLuint> &ObjectHelper::indices() const': gives a type Python "
        "has no way to take yet.")

  @staticmethod
  def load(*__, **_) -> Never:
    """
    Qt's 'void ObjectHelper::load()': leans on 'MeshLoader::loadOBJ(QString
    const&, QList<QVector3D>&, QList<QVector2D>&, QList<QVector3D>&)', which
    Qt's source does not mark for use from outside Qt and has no code for
    that could be taken.
    """
    raise NotImplementedError(
        "'ObjectHelper.load' has no cute function yet. Qt's 'void "
        "ObjectHelper::load()': leans on 'MeshLoader::loadOBJ(QString "
        "const&, QList<QVector3D>&, QList<QVector2D>&, QList<QVector3D>&)', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")

  @staticmethod
  def releaseObjectHelper(*__, **_) -> Never:
    """
    Qt's 'void ObjectHelper::releaseObjectHelper(const Abstract3DRenderer
    *cacheId, ObjectHelper *&obj)': takes or gives a type that cannot be
    passed yet: ObjectHelper *&.
    """
    raise NotImplementedError(
        "'ObjectHelper.releaseObjectHelper' has no cute function yet. Qt's "
        "'void ObjectHelper::releaseObjectHelper(const Abstract3DRenderer "
        "*cacheId, ObjectHelper *&obj)': takes or gives a type that cannot "
        "be passed yet: ObjectHelper *&.")

  @staticmethod
  def resetObjectHelper(*__, **_) -> Never:
    """
    Qt's 'void ObjectHelper::resetObjectHelper(const Abstract3DRenderer
    *cacheId, ObjectHelper *&obj, const QString &meshFile)': takes or gives a
    type that cannot be passed yet: ObjectHelper *&.
    """
    raise NotImplementedError(
        "'ObjectHelper.resetObjectHelper' has no cute function yet. Qt's "
        "'void ObjectHelper::resetObjectHelper(const Abstract3DRenderer "
        "*cacheId, ObjectHelper *&obj, const QString &meshFile)': takes or "
        "gives a type that cannot be passed yet: ObjectHelper *&.")
