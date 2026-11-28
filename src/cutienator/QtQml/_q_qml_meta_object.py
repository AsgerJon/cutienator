"""
QQmlMetaObject binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qqmlmetaobject_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QQmlMetaObject to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QMetaObject
from . import QQmlPropertyCache

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaType, QObject, QString
  from . import QQmlPropertyData
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QObject = WAIT['QObject']
  QQmlPropertyData = WAIT['QQmlPropertyData']
  QString = WAIT['QString']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQmlMetaObject(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQmlMetaObject: a plain Python object standing in
  front of one C++ QQmlMetaObject.

  C++ hands a QQmlMetaObject around as a copy, so every C++ QQmlMetaObject
  behind a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QQmlMetaObject that has a ritual and that Python can
  call so far, 6 names in all: 'isNull', 'className', 'propertyCount',
  'metaObject', 'methodReturnType', 'canConvert'. It can be made from Python,
  in 5 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QQmlMetaObject &QQmlMetaObject::operator=(const QQmlMetaObject
    &a0)': assignment: Python binds a name and has no operator for it.
  - Qt's 'void
    QQmlMetaObject::resolveGadgetMethodOrPropertyIndex(QMetaObject::Call
    type, const QMetaObject **metaObject, int *index)': takes a type Python
    has no way to hand over yet.
  - Qt's 'QQmlMetaObject::~QQmlMetaObject()': the destructor: Python removes
    its C++ QQmlMetaObject by it, and has no other use for it.

  What has no ritual
  ------------------

  7 of the 21 functions Qt declares: 7 a template.

  What to expect
  --------------

  - The C++ QQmlMetaObject is created at the first use, not by
    'QQmlMetaObject(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QQmlMetaObject back gives a copy the ritual made for
    Python, in a new cute QQmlMetaObject.
  - Each name of Qt's QQmlMetaObject that has no cute function yet,
    'constructorParameterTypes', 'constructorReturnAndParameterTypes',
    'methodParameterTypes', 'methodReturnAndParameterTypes', 'parameterType',
    'resolveGadgetMethodOrPropertyIndex', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(THIS, THIS)
  def canConvert(from_: QQmlMetaObject, to: QQmlMetaObject) -> bool:
    """
    Calls Qt's 'bool QQmlMetaObject::canConvert(const QQmlMetaObject &from,
    const QQmlMetaObject &to)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlmetaobject.html#canConvert

    Parameters
    ----------

    from_ : QQmlMetaObject
      Passed on as a value: Qt reads the C++ QQmlMetaObject, which stays
      Python's own.

    to : QQmlMetaObject
      Passed on as a value: Qt reads the C++ QQmlMetaObject, which stays
      Python's own.
    """
    #  bool QQmlMetaObject::canConvert(const QQmlMetaObject &from, const
    #      QQmlMetaObject &to)
    return Rituals.call(
        'ritual_ZN14QQmlMetaObject10canConvertERKS_S1_',
        CuteMixin._valueOf(from_), CuteMixin._valueOf(to),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlMetaObject'

  #  Qt's '~QQmlMetaObject()'. Naming it makes this a value class: Python
  #  owns every C++ QQmlMetaObject behind a cute one, and removes it by this
  #  ritual.
  __delete_ritual__ = 'ritual_ZN14QQmlMetaObjectD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isNull(self) -> bool:
    """
    Calls Qt's 'bool QQmlMetaObject::isNull() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlmetaobject.html#isNull
    """
    #  bool QQmlMetaObject::isNull() const
    return self.uglySide.call('ritual_ZNK14QQmlMetaObject6isNullEv')

  def className(self) -> Optional[str]:
    """
    Calls Qt's 'const char *QQmlMetaObject::className() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlmetaobject.html#className

    Returns
    -------

    Optional[str]
      The text Qt gave back. None when Qt gave back no text.
    """
    #  const char *QQmlMetaObject::className() const
    chars = self.uglySide.call('ritual_ZNK14QQmlMetaObject9classNameEv')
    return None if chars is None else chars.decode()

  def propertyCount(self) -> int:
    """
    Calls Qt's 'int QQmlMetaObject::propertyCount() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlmetaobject.html#propertyCount
    """
    #  int QQmlMetaObject::propertyCount() const
    return self.uglySide.call('ritual_ZNK14QQmlMetaObject13propertyCountEv')

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQmlMetaObject::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlmetaobject.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQmlMetaObject::metaObject() const
    address = self.uglySide.call('ritual_ZNK14QQmlMetaObject10metaObjectEv')
    return QMetaObject._cuteAt(address)

  @overload(QQmlPropertyData)
  @overload(QQmlPropertyData, QString)
  @overload(QQmlPropertyData, NoneType)
  def methodReturnType(
      self,
      data: QQmlPropertyData,
      unknownTypeError: Optional[QString] = None,
  ) -> QMetaType:
    """
    Calls Qt's 'QMetaType QQmlMetaObject::methodReturnType(const
    QQmlPropertyData &data, QString *unknownTypeError) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlmetaobject.html#methodReturnType

    Parameters
    ----------

    data : QQmlPropertyData
      Passed on as a value: Qt reads the C++ QQmlPropertyData, which stays
      Python's own.

    unknownTypeError : Optional[QString]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    Returns
    -------

    QMetaType
      A new cute QMetaType around the copy Qt gave back. Python owns it.
    """
    #  QMetaType QQmlMetaObject::methodReturnType(const QQmlPropertyData
    #      &data, QString *unknownTypeError) const
    address = self.uglySide.call(
        'ritual_ZNK14QQmlMetaObject16methodReturnTypeERK16QQmlPropertyDataP'
        '7QString',
        self._valueOf(data), self._addressOf(unknownTypeError),
    )
    from ..QtCore import QMetaType
    return QMetaType._cuteOwning(address)

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
    Notes what was given, for Qt's 'QQmlMetaObject::QQmlMetaObject()', which
    is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qqmlmetaobject.html#QQmlMetaObject
    """
    #  QQmlMetaObject::QQmlMetaObject()
    self._noteCreation(QQmlMetaObject, lambda: Rituals.call(
        'ritual_ZN14QQmlMetaObjectC1Ev',
    ))

  @overload(QObject)
  @overload(NoneType)
  def __init__(self, a0: Optional[QObject]) -> None:
    """
    Notes what was given, for Qt's 'QQmlMetaObject::QQmlMetaObject(const
    QObject *a0)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qqmlmetaobject.html#QQmlMetaObject

    Parameters
    ----------

    a0 : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QQmlMetaObject::QQmlMetaObject(const QObject *a0)
    self._noteCreation(QQmlMetaObject, lambda: Rituals.call(
        'ritual_ZN14QQmlMetaObjectC1EPK7QObject',
        self._addressOf(a0, 'QObject'),
    ))

  @overload(QMetaObject)
  def __init__(self, a0: Optional[QMetaObject]) -> None:
    """
    Notes what was given, for Qt's 'QQmlMetaObject::QQmlMetaObject(const
    QMetaObject *a0)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qqmlmetaobject.html#QQmlMetaObject

    Parameters
    ----------

    a0 : Optional[QMetaObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QQmlMetaObject::QQmlMetaObject(const QMetaObject *a0)
    self._noteCreation(QQmlMetaObject, lambda: Rituals.call(
        'ritual_ZN14QQmlMetaObjectC1EPK11QMetaObject',
        self._addressOf(a0, 'QMetaObject'),
    ))

  @overload(QQmlPropertyCache.ConstPtr)
  def __init__(self, a0: QQmlPropertyCache.ConstPtr) -> None:
    """
    Notes what was given, for Qt's 'QQmlMetaObject::QQmlMetaObject(const
    QQmlPropertyCache::ConstPtr &a0)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qqmlmetaobject.html#QQmlMetaObject

    Parameters
    ----------

    a0 : QQmlPropertyCache.ConstPtr
      Passed on as a value: Qt reads the C++ QQmlPropertyCache::ConstPtr,
      which stays Python's own.
    """
    #  QQmlMetaObject::QQmlMetaObject(const QQmlPropertyCache::ConstPtr &a0)
    self._noteCreation(QQmlMetaObject, lambda: Rituals.call(
        'ritual_ZN14QQmlMetaObjectC1ERKN17QQmlPropertyCache8ConstPtrE',
        self._valueOf(a0),
    ))

  @overload(THIS)
  def __init__(self, a0: QQmlMetaObject) -> None:
    """
    Notes what was given, for Qt's 'QQmlMetaObject::QQmlMetaObject(const
    QQmlMetaObject &a0)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qqmlmetaobject.html#QQmlMetaObject

    Parameters
    ----------

    a0 : QQmlMetaObject
      Passed on as a value: Qt reads the C++ QQmlMetaObject, which stays
      Python's own.
    """
    #  QQmlMetaObject::QQmlMetaObject(const QQmlMetaObject &a0)
    self._noteCreation(QQmlMetaObject, lambda: Rituals.call(
        'ritual_ZN14QQmlMetaObjectC1ERKS_', self._valueOf(a0),
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
  def constructorParameterTypes(*__, **_) -> Never:
    """
    Qt's 'QQmlMetaObject::constructorParameterTypes': a template: a pattern
    and no single function.
    """
    raise NotImplementedError(
        "'QQmlMetaObject.constructorParameterTypes' has no cute function "
        "yet. Qt's 'QQmlMetaObject::constructorParameterTypes': a template: "
        "a pattern and no single function.")

  @staticmethod
  def constructorReturnAndParameterTypes(*__, **_) -> Never:
    """
    Qt's 'QQmlMetaObject::constructorReturnAndParameterTypes': a template: a
    pattern and no single function.
    """
    raise NotImplementedError(
        "'QQmlMetaObject.constructorReturnAndParameterTypes' has no cute "
        "function yet. Qt's "
        "'QQmlMetaObject::constructorReturnAndParameterTypes': a template: "
        "a pattern and no single function.")

  @staticmethod
  def methodParameterTypes(*__, **_) -> Never:
    """
    Qt's 'QQmlMetaObject::methodParameterTypes': a template: a pattern and no
    single function.
    """
    raise NotImplementedError(
        "'QQmlMetaObject.methodParameterTypes' has no cute function yet. "
        "Qt's 'QQmlMetaObject::methodParameterTypes': a template: a pattern "
        "and no single function.")

  @staticmethod
  def methodReturnAndParameterTypes(*__, **_) -> Never:
    """
    Qt's 'QQmlMetaObject::methodReturnAndParameterTypes': a template: a
    pattern and no single function.
    """
    raise NotImplementedError(
        "'QQmlMetaObject.methodReturnAndParameterTypes' has no cute "
        "function yet. Qt's "
        "'QQmlMetaObject::methodReturnAndParameterTypes': a template: a "
        "pattern and no single function.")

  @staticmethod
  def parameterType(*__, **_) -> Never:
    """
    Qt's 'QQmlMetaObject::parameterType': a template: a pattern and no single
    function.
    """
    raise NotImplementedError(
        "'QQmlMetaObject.parameterType' has no cute function yet. Qt's "
        "'QQmlMetaObject::parameterType': a template: a pattern and no "
        "single function.")

  @staticmethod
  def resolveGadgetMethodOrPropertyIndex(*__, **_) -> Never:
    """
    Qt's 'void
    QQmlMetaObject::resolveGadgetMethodOrPropertyIndex(QMetaObject::Call
    type, const QMetaObject **metaObject, int *index)': takes a type Python
    has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQmlMetaObject.resolveGadgetMethodOrPropertyIndex' has no cute "
        "function yet. Qt's 'void "
        "QQmlMetaObject::resolveGadgetMethodOrPropertyIndex(QMetaObject::Cal"
        "l type, const QMetaObject **metaObject, int *index)': takes a type "
        "Python has no way to hand over yet.")
