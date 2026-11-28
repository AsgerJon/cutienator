"""
QQuickDesignerCustomObjectData binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquickdesignercustomobjectdata_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QQuickDesignerCustomObjectData to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QByteArray, QObject, QVariant
  from ..QtQml import QQmlAnyBinding, QQmlContext
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']
  QQmlContext = WAIT['QQmlContext']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickDesignerCustomObjectData(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQuickDesignerCustomObjectData: a plain Python object
  standing in front of one C++ QQuickDesignerCustomObjectData.

  C++ hands a QQuickDesignerCustomObjectData around as a copy, so every C++
  QQuickDesignerCustomObjectData behind a cute one is Python's own: it is
  removed, by the ritual named in '__delete_ritual__', when the cute object
  goes.

  What exists
  -----------

  Every function of Qt's QQuickDesignerCustomObjectData that has a ritual and
  that Python can call so far, 8 names in all: 'populateResetHashes',
  'object', 'getResetValue', 'doResetProperty', 'hasValidResetBinding',
  'getResetBinding', 'setPropertyBinding', 'keepBindingFromGettingDeleted'.
  None can be made from Python: one comes out of a function of another class
  that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'bool
    QQuickDesignerCustomObjectData::hasBindingForProperty(QQmlContext
    *context, const QQuickDesignerSupport::PropertyName &propertyName, bool
    *hasChanged) const': takes a number to change where it is.
  - Qt's 'QQuickDesignerCustomObjectData::~QQuickDesignerCustomObjectData()':
    the destructor: Python removes its C++ QQuickDesignerCustomObjectData by
    it, and has no other use for it.

  What has no ritual
  ------------------

  10 of the 20 functions Qt declares: 7 leans on
  'QQuickDesignerCustomObjectData; 3 Qt's library has no name for it, and its
  code in Qt's source does not compile apart from its file.

  What to expect
  --------------

  - The C++ QQuickDesignerCustomObjectData is created at the first use, not
    by 'QQuickDesignerCustomObjectData(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QQuickDesignerCustomObjectData back gives a copy the
    ritual made for Python, in a new cute QQuickDesignerCustomObjectData.
  - Each name of Qt's QQuickDesignerCustomObjectData that has no cute
    function yet, '__init__', 'get', 'handleDestroyed',
    'hasBindingForProperty', 'registerData', holds a function that raises
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
  __qt_class__ = 'QQuickDesignerCustomObjectData'

  #  Qt's '~QQuickDesignerCustomObjectData()'. Naming it makes this a value
  #  class: Python owns every C++ QQuickDesignerCustomObjectData behind a
  #  cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN30QQuickDesignerCustomObjectDataD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def object(self) -> Optional[QObject]:
    """
    Calls Qt's 'QObject *QQuickDesignerCustomObjectData::object() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdesignercustomobjectdata.html#object

    Returns
    -------

    Optional[QObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QObject *QQuickDesignerCustomObjectData::object() const
    address = self.uglySide.call(
        'ritual_ZNK30QQuickDesignerCustomObjectData6objectEv',
    )
    from ..QtCore import QObject
    return QObject._cuteAt(address)

  @overload(QByteArray)
  def getResetValue(self, propertyName: QByteArray) -> QVariant:
    """
    Calls Qt's 'QVariant QQuickDesignerCustomObjectData::getResetValue(const
    QQuickDesignerSupport::PropertyName &propertyName) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdesignercustomobjectdata.html#getResetValue

    Parameters
    ----------

    propertyName : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QQuickDesignerCustomObjectData::getResetValue(const
    #      QQuickDesignerSupport::PropertyName &propertyName) const
    address = self.uglySide.call(
        'ritual_ZNK30QQuickDesignerCustomObjectData13getResetValueERK10QByt'
        'eArray',
        self._valueOf(propertyName),
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  @overload(QByteArray)
  def hasValidResetBinding(self, propertyName: QByteArray) -> bool:
    """
    Calls Qt's 'bool
    QQuickDesignerCustomObjectData::hasValidResetBinding(const
    QQuickDesignerSupport::PropertyName &propertyName) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdesignercustomobjectdata.html

    Parameters
    ----------

    propertyName : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  bool QQuickDesignerCustomObjectData::hasValidResetBinding(const
    #      QQuickDesignerSupport::PropertyName &propertyName) const
    return self.uglySide.call(
        'ritual_ZNK30QQuickDesignerCustomObjectData20hasValidResetBindingER'
        'K10QByteArray',
        self._valueOf(propertyName),
    )

  @overload(QByteArray)
  def getResetBinding(self, propertyName: QByteArray) -> QQmlAnyBinding:
    """
    Calls Qt's 'QQmlAnyBinding
    QQuickDesignerCustomObjectData::getResetBinding(const
    QQuickDesignerSupport::PropertyName &propertyName) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdesignercustomobjectdata.html

    Parameters
    ----------

    propertyName : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    Returns
    -------

    QQmlAnyBinding
      A new cute QQmlAnyBinding around the copy Qt gave back. Python owns it.
    """
    #  QQmlAnyBinding QQuickDesignerCustomObjectData::getResetBinding(const
    #      QQuickDesignerSupport::PropertyName &propertyName) const
    address = self.uglySide.call(
        'ritual_ZNK30QQuickDesignerCustomObjectData15getResetBindingERK10QB'
        'yteArray',
        self._valueOf(propertyName),
    )
    from ..QtQml import QQmlAnyBinding
    return QQmlAnyBinding._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QQmlContext, QByteArray, str)
  @overload(NoneType, QByteArray, str)
  def setPropertyBinding(
      self,
      context: Optional[QQmlContext],
      propertyName: QByteArray,
      expression: str,
  ) -> None:
    """
    Calls Qt's 'void
    QQuickDesignerCustomObjectData::setPropertyBinding(QQmlContext *context,
    const QQuickDesignerSupport::PropertyName &propertyName, const QString
    &expression)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdesignercustomobjectdata.html

    Parameters
    ----------

    context : Optional[QQmlContext]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    propertyName : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    expression : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQuickDesignerCustomObjectData::setPropertyBinding(QQmlContext
    #      *context, const QQuickDesignerSupport::PropertyName &propertyName,
    #      const QString &expression)
    self.uglySide.call(
        'ritual_ZN30QQuickDesignerCustomObjectData18setPropertyBindingEP11Q'
        'QmlContextRK10QByteArrayRK7QString',
        self._addressOf(context), self._valueOf(propertyName), expression,
    )

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
    'QQuickDesignerCustomObjectData::QQuickDesignerCustomObjectData(QObject
    *object)': Qt's library has no name for it, and its code in Qt's source
    does not compile apart from its file: use of undeclared identifier
    's_designerObjectToDataHash'.
    """
    raise NotImplementedError(
        "'QQuickDesignerCustomObjectData.__init__' has no cute function "
        "yet. Qt's "
        "'QQuickDesignerCustomObjectData::QQuickDesignerCustomObjectData(QOb"
        "ject *object)': Qt's library has no name for it, and its code in "
        "Qt's source does not compile apart from its file: use of "
        "undeclared identifier 's_designerObjectToDataHash'.")

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

  def populateResetHashes(self) -> None:
    """
    Calls Qt's 'void QQuickDesignerCustomObjectData::populateResetHashes()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdesignercustomobjectdata.html
    """
    #  void QQuickDesignerCustomObjectData::populateResetHashes()
    self.uglySide.call(
        'ritual_ZN30QQuickDesignerCustomObjectData19populateResetHashesEv',
    )

  @overload(QQmlContext, QByteArray)
  @overload(NoneType, QByteArray)
  def doResetProperty(
      self,
      context: Optional[QQmlContext],
      propertyName: QByteArray,
  ) -> None:
    """
    Calls Qt's 'void
    QQuickDesignerCustomObjectData::doResetProperty(QQmlContext *context,
    const QQuickDesignerSupport::PropertyName &propertyName)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdesignercustomobjectdata.html

    Parameters
    ----------

    context : Optional[QQmlContext]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    propertyName : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void QQuickDesignerCustomObjectData::doResetProperty(QQmlContext
    #      *context, const QQuickDesignerSupport::PropertyName &propertyName)
    self.uglySide.call(
        'ritual_ZN30QQuickDesignerCustomObjectData15doResetPropertyEP11QQml'
        'ContextRK10QByteArray',
        self._addressOf(context), self._valueOf(propertyName),
    )

  @overload(QQmlContext, QByteArray)
  @overload(NoneType, QByteArray)
  def keepBindingFromGettingDeleted(
      self,
      context: Optional[QQmlContext],
      propertyName: QByteArray,
  ) -> None:
    """
    Calls Qt's 'void
    QQuickDesignerCustomObjectData::keepBindingFromGettingDeleted(QQmlContext
    *context, const QQuickDesignerSupport::PropertyName &propertyName)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdesignercustomobjectdata.html

    Parameters
    ----------

    context : Optional[QQmlContext]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    propertyName : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void QQuickDesignerCustomObjectData::keepBindingFromGettingDeleted(
    #      QQmlContext *context, const QQuickDesignerSupport::PropertyName
    #      &propertyName)
    self.uglySide.call(
        'ritual_ZN30QQuickDesignerCustomObjectData29keepBindingFromGettingD'
        'eletedEP11QQmlContextRK10QByteArray',
        self._addressOf(context), self._valueOf(propertyName),
    )

  @staticmethod
  def get(*__, **_) -> Never:
    """
    Qt's 'QQuickDesignerCustomObjectData
    *QQuickDesignerCustomObjectData::get(QObject *object)': Qt's library has
    no name for it, and its code in Qt's source does not compile apart from
    its file: use of undeclared identifier 's_designerObjectToDataHash'.
    """
    raise NotImplementedError(
        "'QQuickDesignerCustomObjectData.get' has no cute function yet. "
        "Qt's 'QQuickDesignerCustomObjectData "
        "*QQuickDesignerCustomObjectData::get(QObject *object)': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: use of undeclared identifier "
        "'s_designerObjectToDataHash'.")

  @staticmethod
  def handleDestroyed(*__, **_) -> Never:
    """
    Qt's 'void QQuickDesignerCustomObjectData::handleDestroyed()': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: use of undeclared identifier
    's_designerObjectToDataHash'.
    """
    raise NotImplementedError(
        "'QQuickDesignerCustomObjectData.handleDestroyed' has no cute "
        "function yet. Qt's 'void "
        "QQuickDesignerCustomObjectData::handleDestroyed()': Qt's library "
        "has no name for it, and its code in Qt's source does not compile "
        "apart from its file: use of undeclared identifier "
        "'s_designerObjectToDataHash'.")

  @staticmethod
  def hasBindingForProperty(*__, **_) -> Never:
    """
    - Qt's 'bool
      QQuickDesignerCustomObjectData::hasBindingForProperty(QQmlContext
      *context, const QQuickDesignerSupport::PropertyName &propertyName, bool
      *hasChanged) const': takes a number to change where it is.
    - Qt's 'bool
      QQuickDesignerCustomObjectData::hasBindingForProperty(QObject *object,
      QQmlContext *context, const QQuickDesignerSupport::PropertyName
      &propertyName, bool *hasChanged)': leans on
      'QQuickDesignerCustomObjectData::get(QObject*)', which Qt's source does
      not mark for use from outside Qt and has no code for that could be
      taken.
    """
    raise NotImplementedError(
        "'QQuickDesignerCustomObjectData.hasBindingForProperty' has no cute "
        "function yet. Qt's 'bool "
        "QQuickDesignerCustomObjectData::hasBindingForProperty(QQmlContext "
        "*context, const QQuickDesignerSupport::PropertyName &propertyName, "
        "bool *hasChanged) const': takes a number to change where it is. "
        "Qt's 'bool "
        "QQuickDesignerCustomObjectData::hasBindingForProperty(QObject "
        "*object, QQmlContext *context, const "
        "QQuickDesignerSupport::PropertyName &propertyName, bool "
        "*hasChanged)': leans on "
        "'QQuickDesignerCustomObjectData::get(QObject*)', which Qt's source "
        "does not mark for use from outside Qt and has no code for that "
        "could be taken.")

  @staticmethod
  def registerData(*__, **_) -> Never:
    """
    Qt's 'void QQuickDesignerCustomObjectData::registerData(QObject
    *object)': leans on
    'QQuickDesignerCustomObjectData::QQuickDesignerCustomObjectData(
    QObject*)', which Qt's source does not mark for use from outside Qt and
    has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQuickDesignerCustomObjectData.registerData' has no cute function "
        "yet. Qt's 'void "
        "QQuickDesignerCustomObjectData::registerData(QObject *object)': "
        "leans on "
        "'QQuickDesignerCustomObjectData::QQuickDesignerCustomObjectData(QOb"
        "ject*)', which Qt's source does not mark for use from outside Qt "
        "and has no code for that could be taken.")
