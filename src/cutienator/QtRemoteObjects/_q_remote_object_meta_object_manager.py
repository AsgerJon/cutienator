"""
QRemoteObjectMetaObjectManager binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtRemoteObjects/6.12.0/QtRemoteObjects/private/qremoteobjectnode_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QRemoteObjectMetaObjectManager to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QMetaObject = WAIT['QMetaObject']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QRemoteObjectMetaObjectManager(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QRemoteObjectMetaObjectManager: a plain Python object
  standing in front of one C++ QRemoteObjectMetaObjectManager.

  C++ hands a QRemoteObjectMetaObjectManager around as a copy, so every C++
  QRemoteObjectMetaObjectManager behind a cute one is Python's own: it is
  removed, by the ritual named in '__delete_ritual__', when the cute object
  goes.

  What exists
  -----------

  Every function of Qt's QRemoteObjectMetaObjectManager that has a ritual and
  that Python can call so far, 2 names in all: 'metaObjectForType',
  'addFromMetaObject'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QRemoteObjectMetaObjectManager::~QRemoteObjectMetaObjectManager()':
    the destructor: Python removes its C++ QRemoteObjectMetaObjectManager by
    it, and has no other use for it.

  What has no ritual
  ------------------

  1 of the 5 functions Qt declares: 1 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file.

  What to expect
  --------------

  - The C++ QRemoteObjectMetaObjectManager is created at the first use, not
    by 'QRemoteObjectMetaObjectManager(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QRemoteObjectMetaObjectManager back gives a copy the
    ritual made for Python, in a new cute QRemoteObjectMetaObjectManager.
  - Each name of Qt's QRemoteObjectMetaObjectManager that has no cute
    function yet, 'addDynamicType', holds a function that raises
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
  __qt_class__ = 'QRemoteObjectMetaObjectManager'

  #  Qt's '~QRemoteObjectMetaObjectManager()'. Naming it makes this a value
  #  class: Python owns every C++ QRemoteObjectMetaObjectManager behind a
  #  cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN30QRemoteObjectMetaObjectManagerD1Ev'

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
    Notes what was given, for Qt's
    'QRemoteObjectMetaObjectManager::QRemoteObjectMetaObjectManager()', which
    is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qremoteobjectmetaobjectmanager.html
    """
    #  QRemoteObjectMetaObjectManager::QRemoteObjectMetaObjectManager()
    self._noteCreation(QRemoteObjectMetaObjectManager, lambda: Rituals.call(
        'ritual_ZN30QRemoteObjectMetaObjectManagerC1Ev',
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
  def metaObjectForType(self, type: str) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject
    *QRemoteObjectMetaObjectManager::metaObjectForType(const QString &type)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qremoteobjectmetaobjectmanager.html

    Parameters
    ----------

    type : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject
    #      *QRemoteObjectMetaObjectManager::metaObjectForType(const QString
    #      &type)
    address = self.uglySide.call(
        'ritual_ZN30QRemoteObjectMetaObjectManager17metaObjectForTypeERK7QS'
        'tring',
        type,
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  @overload(QMetaObject)
  @overload(NoneType)
  def addFromMetaObject(self, a0: Optional[QMetaObject]) -> None:
    """
    Calls Qt's 'void QRemoteObjectMetaObjectManager::addFromMetaObject(const
    QMetaObject *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qremoteobjectmetaobjectmanager.html

    Parameters
    ----------

    a0 : Optional[QMetaObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QRemoteObjectMetaObjectManager::addFromMetaObject(const
    #      QMetaObject *a0)
    self.uglySide.call(
        'ritual_ZN30QRemoteObjectMetaObjectManager17addFromMetaObjectEPK11Q'
        'MetaObject',
        self._addressOf(a0, 'QMetaObject'),
    )

  @staticmethod
  def addDynamicType(*__, **_) -> Never:
    """
    Qt's 'QMetaObject
    *QRemoteObjectMetaObjectManager::addDynamicType(QtROIoDeviceBase
    *connection, QDataStream &in)': Qt's library has no name for it, and its
    code in Qt's source does not compile apart from its file: unknown type
    name 'ClassData'; did you mean 'QRemoteObjectInternalTypes::ClassData'?.
    """
    raise NotImplementedError(
        "'QRemoteObjectMetaObjectManager.addDynamicType' has no cute "
        "function yet. Qt's 'QMetaObject "
        "*QRemoteObjectMetaObjectManager::addDynamicType(QtROIoDeviceBase "
        "*connection, QDataStream &in)': Qt's library has no name for it, "
        "and its code in Qt's source does not compile apart from its file: "
        "unknown type name 'ClassData'; did you mean "
        "'QRemoteObjectInternalTypes::ClassData'?.")
