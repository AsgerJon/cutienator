"""
QDesignerPropertySheet binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDesigner/6.12.0/QtDesigner/private/qdesigner_propertysheet_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QDesignerPropertySheet to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteFlags, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import QObject
from . import QDesignerDynamicPropertySheetExtension
from . import QDesignerPropertySheetExtension, qdesigner_internal

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QVariant
  from . import QDesignerFormEditorInterface
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QDesignerPropertySheet(QObject, QDesignerPropertySheetExtension, QDesignerDynamicPropertySheetExtension):
  """
  The cute side of Qt's QDesignerPropertySheet: a plain Python object
  standing in front of one C++ QDesignerPropertySheet.

  It is built on the cute 'QObject', as Qt's QDesignerPropertySheet is built
  on Qt's QObject, and has everything that class has. It is built on the cute
  'QDesignerPropertySheetExtension' as well, as Qt's QDesignerPropertySheet
  is built on Qt's QDesignerPropertySheetExtension too, and has everything
  that class has. It is built on the cute
  'QDesignerDynamicPropertySheetExtension' as well, as Qt's
  QDesignerPropertySheet is built on Qt's
  QDesignerDynamicPropertySheetExtension too, and has everything that class
  has.

  What exists
  -----------

  Every function of Qt's QDesignerPropertySheet that has a ritual and that
  Python can call so far, 50 names in all: 'metaObject', 'tr', 'indexOf',
  'count', 'propertyName', 'propertyGroup', 'setPropertyGroup', 'hasReset',
  'reset', 'isAttribute', 'setAttribute', 'isVisible', 'setVisible',
  'property', 'setProperty', 'isChanged', 'setChanged',
  'dynamicPropertiesAllowed', 'addDynamicProperty', 'removeDynamicProperty',
  'isDynamicProperty', 'canAddDynamicProperty', 'isDefaultDynamicProperty',
  'isResourceProperty', 'defaultResourceProperty', 'pixmapCache',
  'setPixmapCache', 'iconCache', 'setIconCache', 'createFakeProperty',
  'isEnabled', 'object', 'internalDynamicPropertiesEnabled',
  'setInternalDynamicPropertiesEnabled', 'formEditorForObject',
  'isAdditionalProperty', 'isFakeProperty', 'resolvePropertyValue',
  'metaProperty', 'setFakeProperty', 'clearFakeProperties',
  'isFakeLayoutProperty', 'isDynamic', 'formWindowBase', 'core',
  'objectTypeFromObject', 'objectFlagsFromObject', 'propertyTypeFromName',
  'propertyType', 'objectType'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QDesignerPropertySheet::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QDesignerPropertySheet::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QDesignerPropertySheet::~QDesignerPropertySheet()': the destructor:
    Python never removes a C++ QDesignerPropertySheet.

  What has no ritual
  ------------------

  2 of the 56 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QDesignerPropertySheet is created at the first use, not by
    'QDesignerPropertySheet(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QDesignerPropertySheet.
  - Qt tells when it has removed the C++ QDesignerPropertySheet. Every call
    on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  #  The enums Qt writes inside QDesignerPropertySheet, each a class in here
  #  as in C++, and the names Qt has for the combinations of its flags enums.

  class ObjectFlag(CuteFlags):
    """
    The flags enum 'QDesignerPropertySheet::ObjectFlag' of Qt, with the 1
    names Qt gives in it. Qt names the type of its combinations
    'QDesignerPropertySheet::ObjectFlags'.
    """

    CheckableProperty = 0x1

  ObjectFlags = ObjectFlag

  class ObjectType(CuteNum):
    """
    The enum 'QDesignerPropertySheet::ObjectType' of Qt, with the 4 names Qt
    gives in it.
    """

    ObjectNone = Kee[int](0)
    ObjectLabel = Kee[int](1)
    ObjectLayout = Kee[int](2)
    ObjectLayoutWidget = Kee[int](3)

  class PropertyType(CuteNum):
    """
    The enum 'QDesignerPropertySheet::PropertyType' of Qt, with the 34 names
    Qt gives in it.
    """

    PropertyNone = Kee[int](0)
    PropertyLayoutObjectName = Kee[int](1)
    PropertyLayoutLeftMargin = Kee[int](2)
    PropertyLayoutTopMargin = Kee[int](3)
    PropertyLayoutRightMargin = Kee[int](4)
    PropertyLayoutBottomMargin = Kee[int](5)
    PropertyLayoutSpacing = Kee[int](6)
    PropertyLayoutHorizontalSpacing = Kee[int](7)
    PropertyLayoutVerticalSpacing = Kee[int](8)
    PropertyLayoutSizeConstraint = Kee[int](9)
    PropertyLayoutFieldGrowthPolicy = Kee[int](10)
    PropertyLayoutRowWrapPolicy = Kee[int](11)
    PropertyLayoutLabelAlignment = Kee[int](12)
    PropertyLayoutFormAlignment = Kee[int](13)
    PropertyLayoutBoxStretch = Kee[int](14)
    PropertyLayoutGridRowStretch = Kee[int](15)
    PropertyLayoutGridColumnStretch = Kee[int](16)
    PropertyLayoutGridRowMinimumHeight = Kee[int](17)
    PropertyLayoutGridColumnMinimumWidth = Kee[int](18)
    PropertyBuddy = Kee[int](19)
    PropertyAccessibility = Kee[int](20)
    PropertyGeometry = Kee[int](21)
    PropertyChecked = Kee[int](22)
    PropertyCheckable = Kee[int](23)
    PropertyVisible = Kee[int](24)
    PropertyWindowTitle = Kee[int](25)
    PropertyWindowIcon = Kee[int](26)
    PropertyWindowFilePath = Kee[int](27)
    PropertyWindowOpacity = Kee[int](28)
    PropertyWindowIconText = Kee[int](29)
    PropertyWindowModality = Kee[int](30)
    PropertyWindowModified = Kee[int](31)
    PropertyStyleSheet = Kee[int](32)
    PropertyText = Kee[int](33)

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
    Calls Qt's 'QString QDesignerPropertySheet::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qdesignerpropertysheet.html#tr

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
    #  QString QDesignerPropertySheet::tr(const char *s, const char *c, int
    #      n)
    return Rituals.call(
        'ritual_ZN22QDesignerPropertySheet2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  def internalDynamicPropertiesEnabled() -> bool:
    """
    Calls Qt's 'bool
    QDesignerPropertySheet::internalDynamicPropertiesEnabled()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerpropertysheet.html
    """
    #  bool QDesignerPropertySheet::internalDynamicPropertiesEnabled()
    return Rituals.call(
        'ritual_ZN22QDesignerPropertySheet32internalDynamicPropertiesEnable'
        'dEv',
    )

  @staticmethod
  @overload(bool)
  def setInternalDynamicPropertiesEnabled(v: bool) -> None:
    """
    Calls Qt's 'void
    QDesignerPropertySheet::setInternalDynamicPropertiesEnabled(bool v)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerpropertysheet.html

    Parameters
    ----------

    v : bool
      Passed on as it is.
    """
    #  void QDesignerPropertySheet::setInternalDynamicPropertiesEnabled(bool
    #      v)
    Rituals.call(
        'ritual_ZN22QDesignerPropertySheet35setInternalDynamicPropertiesEna'
        'bledEb',
        v,
    )

  @staticmethod
  @overload(QObject)
  @overload(NoneType)
  def formEditorForObject(
      o: Optional[QObject],
  ) -> Optional[QDesignerFormEditorInterface]:
    """
    Calls Qt's 'QDesignerFormEditorInterface
    *QDesignerPropertySheet::formEditorForObject(QObject *o)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerpropertysheet.html#formEditorForObject

    Parameters
    ----------

    o : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QDesignerFormEditorInterface]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QDesignerFormEditorInterface
    #      *QDesignerPropertySheet::formEditorForObject(QObject *o)
    address = Rituals.call(
        'ritual_ZN22QDesignerPropertySheet19formEditorForObjectEP7QObject',
        CuteMixin._addressOf(o, 'QObject'),
    )
    from . import QDesignerFormEditorInterface
    return QDesignerFormEditorInterface._cuteAt(address)

  @staticmethod
  @overload(QObject)
  @overload(NoneType)
  def objectTypeFromObject(o: Optional[QObject]) -> ObjectType:
    """
    Calls Qt's 'ObjectType QDesignerPropertySheet::objectTypeFromObject(const
    QObject *o)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerpropertysheet.html#objectTypeFromObject

    Parameters
    ----------

    o : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    ObjectType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'ObjectType(number)'
      gives.
    """
    #  ObjectType QDesignerPropertySheet::objectTypeFromObject(const QObject
    #      *o)
    return QDesignerPropertySheet.ObjectType(Rituals.call(
        'ritual_ZN22QDesignerPropertySheet20objectTypeFromObjectEPK7QObject',
        CuteMixin._addressOf(o, 'QObject'),
    ))

  @staticmethod
  @overload(QObject)
  @overload(NoneType)
  def objectFlagsFromObject(o: Optional[QObject]) -> ObjectFlags:
    """
    Calls Qt's 'ObjectFlags
    QDesignerPropertySheet::objectFlagsFromObject(const QObject *o)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerpropertysheet.html#objectFlagsFromObject

    Parameters
    ----------

    o : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    ObjectFlags
      The value standing for the combination Qt gave back.
    """
    #  ObjectFlags QDesignerPropertySheet::objectFlagsFromObject(const
    #      QObject *o)
    return QDesignerPropertySheet.ObjectFlags(Rituals.call(
        'ritual_ZN22QDesignerPropertySheet21objectFlagsFromObjectEPK7QObjec'
        't',
        CuteMixin._addressOf(o, 'QObject'),
    ))

  @staticmethod
  @overload(str)
  def propertyTypeFromName(name: str) -> PropertyType:
    """
    Calls Qt's 'PropertyType
    QDesignerPropertySheet::propertyTypeFromName(const QString &name)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerpropertysheet.html#propertyTypeFromName

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    PropertyType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'PropertyType(number)'
      gives.
    """
    #  PropertyType QDesignerPropertySheet::propertyTypeFromName(const
    #      QString &name)
    return QDesignerPropertySheet.PropertyType(Rituals.call(
        'ritual_ZN22QDesignerPropertySheet20propertyTypeFromNameERK7QString',
        name,
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QDesignerPropertySheet'

  #  Qt's QDesignerPropertySheet is built on more than one class. The part of
  #  a C++ QDesignerPropertySheet that belongs to a class after the first
  #  begins somewhere inside the object, and the ritual named for that class
  #  gives where; see 'CuteMixin._addressAs'.
  __cast_rituals__ = {
      'QDesignerPropertySheetExtension':
          'ritual_cast_QDesignerPropertySheet_QDesignerPropertySheetExtension',
      'QDesignerDynamicPropertySheetExtension':
          'ritual_cast_QDesignerPropertySheet_QDesignerDynamicPropertySheetExtension',
  }

  #  A C++ QDesignerPropertySheet Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QDesignerPropertySheet'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QDesignerPropertySheet::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerpropertysheet.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QDesignerPropertySheet::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK22QDesignerPropertySheet10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  @overload(str)
  def indexOf(self, name: str) -> int:
    """
    Calls Qt's 'int QDesignerPropertySheet::indexOf(const QString &name)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerpropertysheet.html#indexOf

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  int QDesignerPropertySheet::indexOf(const QString &name) const
    ritual = 'ritual_ZNK22QDesignerPropertySheet7indexOfERK7QString'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK22QDesignerPropertySheet7indexOfERK7QString'
    return self.uglySide.call(ritual, name)

  def count(self) -> int:
    """
    Calls Qt's 'int QDesignerPropertySheet::count() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdesignerpropertysheet.html#count
    """
    #  int QDesignerPropertySheet::count() const
    ritual = 'ritual_ZNK22QDesignerPropertySheet5countEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK22QDesignerPropertySheet5countEv'
    return self.uglySide.call(ritual)

  @overload(int)
  def propertyName(self, index: int) -> str:
    """
    Calls Qt's 'QString QDesignerPropertySheet::propertyName(int index)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerpropertysheet.html#propertyName

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QDesignerPropertySheet::propertyName(int index) const
    ritual = 'ritual_ZNK22QDesignerPropertySheet12propertyNameEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK22QDesignerPropertySheet12propertyNameEi'
    return self.uglySide.call(ritual, index)

  @overload(int)
  def propertyGroup(self, index: int) -> str:
    """
    Calls Qt's 'QString QDesignerPropertySheet::propertyGroup(int index)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerpropertysheet.html#propertyGroup

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QDesignerPropertySheet::propertyGroup(int index) const
    ritual = 'ritual_ZNK22QDesignerPropertySheet13propertyGroupEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK22QDesignerPropertySheet13propertyGroupEi'
    return self.uglySide.call(ritual, index)

  @overload(int)
  def hasReset(self, index: int) -> bool:
    """
    Calls Qt's 'bool QDesignerPropertySheet::hasReset(int index) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerpropertysheet.html#hasReset

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  bool QDesignerPropertySheet::hasReset(int index) const
    ritual = 'ritual_ZNK22QDesignerPropertySheet8hasResetEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK22QDesignerPropertySheet8hasResetEi'
    return self.uglySide.call(ritual, index)

  @overload(int)
  def isAttribute(self, index: int) -> bool:
    """
    Calls Qt's 'bool QDesignerPropertySheet::isAttribute(int index) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerpropertysheet.html#isAttribute

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  bool QDesignerPropertySheet::isAttribute(int index) const
    ritual = 'ritual_ZNK22QDesignerPropertySheet11isAttributeEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK22QDesignerPropertySheet11isAttributeEi'
    return self.uglySide.call(ritual, index)

  @overload(int)
  def isVisible(self, index: int) -> bool:
    """
    Calls Qt's 'bool QDesignerPropertySheet::isVisible(int index) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerpropertysheet.html#isVisible

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  bool QDesignerPropertySheet::isVisible(int index) const
    ritual = 'ritual_ZNK22QDesignerPropertySheet9isVisibleEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK22QDesignerPropertySheet9isVisibleEi'
    return self.uglySide.call(ritual, index)

  @overload(int)
  def property(self, index: int) -> QVariant:
    """
    Calls Qt's 'QVariant QDesignerPropertySheet::property(int index) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerpropertysheet.html#property

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QDesignerPropertySheet::property(int index) const
    ritual = 'ritual_ZNK22QDesignerPropertySheet8propertyEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK22QDesignerPropertySheet8propertyEi'
    address = self.uglySide.call(ritual, index)
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  @overload(int)
  def isChanged(self, index: int) -> bool:
    """
    Calls Qt's 'bool QDesignerPropertySheet::isChanged(int index) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerpropertysheet.html#isChanged

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  bool QDesignerPropertySheet::isChanged(int index) const
    ritual = 'ritual_ZNK22QDesignerPropertySheet9isChangedEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK22QDesignerPropertySheet9isChangedEi'
    return self.uglySide.call(ritual, index)

  def dynamicPropertiesAllowed(self) -> bool:
    """
    Calls Qt's 'bool QDesignerPropertySheet::dynamicPropertiesAllowed()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerpropertysheet.html
    """
    #  bool QDesignerPropertySheet::dynamicPropertiesAllowed() const
    ritual = 'ritual_ZNK22QDesignerPropertySheet24dynamicPropertiesAllowedEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK22QDesignerPropertySheet24dynamicPropertiesAllowed'
          'Ev')
    return self.uglySide.call(ritual)

  @overload(int)
  def isDynamicProperty(self, index: int) -> bool:
    """
    Calls Qt's 'bool QDesignerPropertySheet::isDynamicProperty(int index)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerpropertysheet.html#isDynamicProperty

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  bool QDesignerPropertySheet::isDynamicProperty(int index) const
    ritual = 'ritual_ZNK22QDesignerPropertySheet17isDynamicPropertyEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK22QDesignerPropertySheet17isDynamicPropertyEi'
    return self.uglySide.call(ritual, index)

  @overload(str)
  def canAddDynamicProperty(self, propertyName: str) -> bool:
    """
    Calls Qt's 'bool QDesignerPropertySheet::canAddDynamicProperty(const
    QString &propertyName) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerpropertysheet.html#canAddDynamicProperty

    Parameters
    ----------

    propertyName : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QDesignerPropertySheet::canAddDynamicProperty(const QString
    #      &propertyName) const
    ritual = (
        'ritual_ZNK22QDesignerPropertySheet21canAddDynamicPropertyERK7QStri'
        'ng')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK22QDesignerPropertySheet21canAddDynamicPropertyERK'
          '7QString')
    return self.uglySide.call(ritual, propertyName)

  @overload(int)
  def isDefaultDynamicProperty(self, index: int) -> bool:
    """
    Calls Qt's 'bool QDesignerPropertySheet::isDefaultDynamicProperty(int
    index) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerpropertysheet.html

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  bool QDesignerPropertySheet::isDefaultDynamicProperty(int index) const
    return self.uglySide.call(
        'ritual_ZNK22QDesignerPropertySheet24isDefaultDynamicPropertyEi',
        index,
    )

  @overload(int)
  def isResourceProperty(self, index: int) -> bool:
    """
    Calls Qt's 'bool QDesignerPropertySheet::isResourceProperty(int index)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerpropertysheet.html#isResourceProperty

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  bool QDesignerPropertySheet::isResourceProperty(int index) const
    return self.uglySide.call(
        'ritual_ZNK22QDesignerPropertySheet18isResourcePropertyEi', index,
    )

  @overload(int)
  def defaultResourceProperty(self, index: int) -> QVariant:
    """
    Calls Qt's 'QVariant QDesignerPropertySheet::defaultResourceProperty(int
    index) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerpropertysheet.html

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QDesignerPropertySheet::defaultResourceProperty(int index)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK22QDesignerPropertySheet23defaultResourcePropertyEi',
        index,
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  def pixmapCache(self) -> Optional[qdesigner_internal.DesignerPixmapCache]:
    """
    Calls Qt's 'qdesigner_internal::DesignerPixmapCache
    *QDesignerPropertySheet::pixmapCache() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerpropertysheet.html#pixmapCache

    Returns
    -------

    Optional[qdesigner_internal.DesignerPixmapCache]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  qdesigner_internal::DesignerPixmapCache
    #      *QDesignerPropertySheet::pixmapCache() const
    address = self.uglySide.call(
        'ritual_ZNK22QDesignerPropertySheet11pixmapCacheEv',
    )
    return qdesigner_internal.DesignerPixmapCache._cuteAt(address)

  def iconCache(self) -> Optional[qdesigner_internal.DesignerIconCache]:
    """
    Calls Qt's 'qdesigner_internal::DesignerIconCache
    *QDesignerPropertySheet::iconCache() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerpropertysheet.html#iconCache

    Returns
    -------

    Optional[qdesigner_internal.DesignerIconCache]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  qdesigner_internal::DesignerIconCache
    #      *QDesignerPropertySheet::iconCache() const
    address = self.uglySide.call(
        'ritual_ZNK22QDesignerPropertySheet9iconCacheEv',
    )
    return qdesigner_internal.DesignerIconCache._cuteAt(address)

  @overload(int)
  def isEnabled(self, index: int) -> bool:
    """
    Calls Qt's 'bool QDesignerPropertySheet::isEnabled(int index) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerpropertysheet.html#isEnabled

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  bool QDesignerPropertySheet::isEnabled(int index) const
    ritual = 'ritual_ZNK22QDesignerPropertySheet9isEnabledEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK22QDesignerPropertySheet9isEnabledEi'
    return self.uglySide.call(ritual, index)

  def object(self) -> Optional[QObject]:
    """
    Calls Qt's 'QObject *QDesignerPropertySheet::object() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdesignerpropertysheet.html#object

    Returns
    -------

    Optional[QObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QObject *QDesignerPropertySheet::object() const
    address = self.uglySide.call(
        'ritual_ZNK22QDesignerPropertySheet6objectEv',
    )
    return QObject._cuteAt(address)

  @overload(int)
  def isAdditionalProperty(self, index: int) -> bool:
    """
    Calls Qt's 'bool QDesignerPropertySheet::isAdditionalProperty(int index)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerpropertysheet.html#isAdditionalProperty

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  bool QDesignerPropertySheet::isAdditionalProperty(int index) const
    return self.uglySide.call(
        'ritual_ZNK22QDesignerPropertySheet20isAdditionalPropertyEi', index,
    )

  @overload(int)
  def isFakeProperty(self, index: int) -> bool:
    """
    Calls Qt's 'bool QDesignerPropertySheet::isFakeProperty(int index)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerpropertysheet.html#isFakeProperty

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  bool QDesignerPropertySheet::isFakeProperty(int index) const
    return self.uglySide.call(
        'ritual_ZNK22QDesignerPropertySheet14isFakePropertyEi', index,
    )

  @overload(int, QVariant)
  def resolvePropertyValue(self, index: int, value: QVariant) -> QVariant:
    """
    Calls Qt's 'QVariant QDesignerPropertySheet::resolvePropertyValue(int
    index, const QVariant &value) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerpropertysheet.html#resolvePropertyValue

    Parameters
    ----------

    index : int
      Passed on as it is.

    value : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QDesignerPropertySheet::resolvePropertyValue(int index, const
    #      QVariant &value) const
    address = self.uglySide.call(
        'ritual_ZNK22QDesignerPropertySheet20resolvePropertyValueEiRK8QVari'
        'ant',
        index, self._valueOf(value),
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  @overload(int)
  def metaProperty(self, index: int) -> QVariant:
    """
    Calls Qt's 'QVariant QDesignerPropertySheet::metaProperty(int index)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerpropertysheet.html#metaProperty

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QDesignerPropertySheet::metaProperty(int index) const
    address = self.uglySide.call(
        'ritual_ZNK22QDesignerPropertySheet12metaPropertyEi', index,
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  @overload(int)
  def isFakeLayoutProperty(self, index: int) -> bool:
    """
    Calls Qt's 'bool QDesignerPropertySheet::isFakeLayoutProperty(int index)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerpropertysheet.html#isFakeLayoutProperty

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  bool QDesignerPropertySheet::isFakeLayoutProperty(int index) const
    return self.uglySide.call(
        'ritual_ZNK22QDesignerPropertySheet20isFakeLayoutPropertyEi', index,
    )

  @overload(int)
  def isDynamic(self, index: int) -> bool:
    """
    Calls Qt's 'bool QDesignerPropertySheet::isDynamic(int index) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerpropertysheet.html#isDynamic

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  bool QDesignerPropertySheet::isDynamic(int index) const
    return self.uglySide.call(
        'ritual_ZNK22QDesignerPropertySheet9isDynamicEi', index,
    )

  def formWindowBase(self) -> Optional[qdesigner_internal.FormWindowBase]:
    """
    Calls Qt's 'qdesigner_internal::FormWindowBase
    *QDesignerPropertySheet::formWindowBase() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerpropertysheet.html#formWindowBase

    Returns
    -------

    Optional[qdesigner_internal.FormWindowBase]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  qdesigner_internal::FormWindowBase
    #      *QDesignerPropertySheet::formWindowBase() const
    address = self.uglySide.call(
        'ritual_ZNK22QDesignerPropertySheet14formWindowBaseEv',
    )
    return qdesigner_internal.FormWindowBase._cuteAt(address)

  def core(self) -> Optional[QDesignerFormEditorInterface]:
    """
    Calls Qt's 'QDesignerFormEditorInterface *QDesignerPropertySheet::core()
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qdesignerpropertysheet.html#core

    Returns
    -------

    Optional[QDesignerFormEditorInterface]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QDesignerFormEditorInterface *QDesignerPropertySheet::core() const
    address = self.uglySide.call('ritual_ZNK22QDesignerPropertySheet4coreEv')
    from . import QDesignerFormEditorInterface
    return QDesignerFormEditorInterface._cuteAt(address)

  @overload(int)
  def propertyType(self, index: int) -> PropertyType:
    """
    Calls Qt's 'PropertyType QDesignerPropertySheet::propertyType(int index)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerpropertysheet.html#propertyType

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    PropertyType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'PropertyType(number)'
      gives.
    """
    #  PropertyType QDesignerPropertySheet::propertyType(int index) const
    return QDesignerPropertySheet.PropertyType(self.uglySide.call(
        'ritual_ZNK22QDesignerPropertySheet12propertyTypeEi', index,
    ))

  def objectType(self) -> ObjectType:
    """
    Calls Qt's 'ObjectType QDesignerPropertySheet::objectType() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerpropertysheet.html#objectType

    Returns
    -------

    ObjectType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'ObjectType(number)'
      gives.
    """
    #  ObjectType QDesignerPropertySheet::objectType() const
    return QDesignerPropertySheet.ObjectType(self.uglySide.call(
        'ritual_ZNK22QDesignerPropertySheet10objectTypeEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int, str)
  def setPropertyGroup(self, index: int, group: str) -> None:
    """
    Calls Qt's 'void QDesignerPropertySheet::setPropertyGroup(int index,
    const QString &group)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerpropertysheet.html#setPropertyGroup

    Parameters
    ----------

    index : int
      Passed on as it is.

    group : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QDesignerPropertySheet::setPropertyGroup(int index, const QString
    #      &group)
    ritual = (
        'ritual_ZN22QDesignerPropertySheet16setPropertyGroupEiRK7QString')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN22QDesignerPropertySheet16setPropertyGroupEiRK7QStr'
          'ing')
    self.uglySide.call(ritual, index, group)

  @overload(int, bool)
  def setAttribute(self, index: int, b: bool) -> None:
    """
    Calls Qt's 'void QDesignerPropertySheet::setAttribute(int index, bool
    b)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerpropertysheet.html#setAttribute

    Parameters
    ----------

    index : int
      Passed on as it is.

    b : bool
      Passed on as it is.
    """
    #  void QDesignerPropertySheet::setAttribute(int index, bool b)
    ritual = 'ritual_ZN22QDesignerPropertySheet12setAttributeEib'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN22QDesignerPropertySheet12setAttributeEib'
    self.uglySide.call(ritual, index, b)

  @overload(int, bool)
  def setVisible(self, index: int, b: bool) -> None:
    """
    Calls Qt's 'void QDesignerPropertySheet::setVisible(int index, bool b)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerpropertysheet.html#setVisible

    Parameters
    ----------

    index : int
      Passed on as it is.

    b : bool
      Passed on as it is.
    """
    #  void QDesignerPropertySheet::setVisible(int index, bool b)
    ritual = 'ritual_ZN22QDesignerPropertySheet10setVisibleEib'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN22QDesignerPropertySheet10setVisibleEib'
    self.uglySide.call(ritual, index, b)

  @overload(int, QVariant)
  def setProperty(self, index: int, value: QVariant) -> None:
    """
    Calls Qt's 'void QDesignerPropertySheet::setProperty(int index, const
    QVariant &value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerpropertysheet.html#setProperty

    Parameters
    ----------

    index : int
      Passed on as it is.

    value : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void QDesignerPropertySheet::setProperty(int index, const QVariant
    #      &value)
    ritual = 'ritual_ZN22QDesignerPropertySheet11setPropertyEiRK8QVariant'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN22QDesignerPropertySheet11setPropertyEiRK8QVariant')
    self.uglySide.call(ritual, index, self._valueOf(value))

  @overload(int, bool)
  def setChanged(self, index: int, changed: bool) -> None:
    """
    Calls Qt's 'void QDesignerPropertySheet::setChanged(int index, bool
    changed)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerpropertysheet.html#setChanged

    Parameters
    ----------

    index : int
      Passed on as it is.

    changed : bool
      Passed on as it is.
    """
    #  void QDesignerPropertySheet::setChanged(int index, bool changed)
    ritual = 'ritual_ZN22QDesignerPropertySheet10setChangedEib'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN22QDesignerPropertySheet10setChangedEib'
    self.uglySide.call(ritual, index, changed)

  @overload(WAIT['qdesigner_internal.DesignerPixmapCache'])
  @overload(NoneType)
  def setPixmapCache(
      self,
      cache: Optional[qdesigner_internal.DesignerPixmapCache],
  ) -> None:
    """
    Calls Qt's 'void
    QDesignerPropertySheet::setPixmapCache(qdesigner_internal::
    DesignerPixmapCache *cache)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerpropertysheet.html#setPixmapCache

    Parameters
    ----------

    cache : Optional[qdesigner_internal.DesignerPixmapCache]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QDesignerPropertySheet::setPixmapCache(qdesigner_internal::
    #      DesignerPixmapCache *cache)
    self.uglySide.call(
        'ritual_ZN22QDesignerPropertySheet14setPixmapCacheEPN18qdesigner_in'
        'ternal19DesignerPixmapCacheE',
        self._addressOf(cache),
    )

  @overload(WAIT['qdesigner_internal.DesignerIconCache'])
  @overload(NoneType)
  def setIconCache(
      self,
      cache: Optional[qdesigner_internal.DesignerIconCache],
  ) -> None:
    """
    Calls Qt's 'void
    QDesignerPropertySheet::setIconCache(qdesigner_internal::
    DesignerIconCache *cache)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerpropertysheet.html#setIconCache

    Parameters
    ----------

    cache : Optional[qdesigner_internal.DesignerIconCache]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QDesignerPropertySheet::setIconCache(qdesigner_internal::
    #      DesignerIconCache *cache)
    self.uglySide.call(
        'ritual_ZN22QDesignerPropertySheet12setIconCacheEPN18qdesigner_inte'
        'rnal17DesignerIconCacheE',
        self._addressOf(cache),
    )

  @overload(int, QVariant)
  def setFakeProperty(self, index: int, value: QVariant) -> None:
    """
    Calls Qt's 'void QDesignerPropertySheet::setFakeProperty(int index, const
    QVariant &value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerpropertysheet.html#setFakeProperty

    Parameters
    ----------

    index : int
      Passed on as it is.

    value : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void QDesignerPropertySheet::setFakeProperty(int index, const QVariant
    #      &value)
    self.uglySide.call(
        'ritual_ZN22QDesignerPropertySheet15setFakePropertyEiRK8QVariant',
        index, self._valueOf(value),
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

  @overload(QObject)
  @overload(NoneType)
  @overload(QObject, QObject)
  @overload(QObject, NoneType)
  @overload(NoneType, QObject)
  @overload(NoneType, NoneType)
  def __init__(
      self,
      object: Optional[QObject],
      parent: Optional[QObject] = None,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QDesignerPropertySheet::QDesignerPropertySheet(QObject *object, QObject
    *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerpropertysheet.html#QDesignerPropertySheet

    Parameters
    ----------

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QDesignerPropertySheet::QDesignerPropertySheet(QObject *object,
    #      QObject *parent)
    self._noteCreation(QDesignerPropertySheet, lambda: Rituals.call(
        'ritual_ZN22QDesignerPropertySheetC1EP7QObjectS1_',
        self._addressOf(object, 'QObject'), self._addressOf(parent,
        'QObject'),
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

  @overload(int)
  def reset(self, index: int) -> bool:
    """
    Calls Qt's 'bool QDesignerPropertySheet::reset(int index)'.

    Qt's own words: https://doc.qt.io/qt-6/qdesignerpropertysheet.html#reset

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  bool QDesignerPropertySheet::reset(int index)
    ritual = 'ritual_ZN22QDesignerPropertySheet5resetEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN22QDesignerPropertySheet5resetEi'
    return self.uglySide.call(ritual, index)

  @overload(str, QVariant)
  def addDynamicProperty(self, propertyName: str, value: QVariant) -> int:
    """
    Calls Qt's 'int QDesignerPropertySheet::addDynamicProperty(const QString
    &propertyName, const QVariant &value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerpropertysheet.html#addDynamicProperty

    Parameters
    ----------

    propertyName : str
      Passed on as it is: a QString is made of it for the call.

    value : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  int QDesignerPropertySheet::addDynamicProperty(const QString
    #      &propertyName, const QVariant &value)
    ritual = (
        'ritual_ZN22QDesignerPropertySheet18addDynamicPropertyERK7QStringRK'
        '8QVariant')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN22QDesignerPropertySheet18addDynamicPropertyERK7QSt'
          'ringRK8QVariant')
    return self.uglySide.call(ritual, propertyName, self._valueOf(value))

  @overload(int)
  def removeDynamicProperty(self, index: int) -> bool:
    """
    Calls Qt's 'bool QDesignerPropertySheet::removeDynamicProperty(int
    index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerpropertysheet.html#removeDynamicProperty

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  bool QDesignerPropertySheet::removeDynamicProperty(int index)
    ritual = 'ritual_ZN22QDesignerPropertySheet21removeDynamicPropertyEi'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN22QDesignerPropertySheet21removeDynamicPropertyEi')
    return self.uglySide.call(ritual, index)

  @overload(str)
  @overload(str, QVariant)
  def createFakeProperty(
      self,
      propertyName: str,
      value: Optional[QVariant] = None,
  ) -> int:
    """
    Calls Qt's 'int QDesignerPropertySheet::createFakeProperty(const QString
    &propertyName, const QVariant &value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerpropertysheet.html#createFakeProperty

    Parameters
    ----------

    propertyName : str
      Passed on as it is: a QString is made of it for the call.

    value : Optional[QVariant]
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own. May be left out, as in Qt: a new 'QVariant()' is then passed on.
    """
    #  int QDesignerPropertySheet::createFakeProperty(const QString
    #      &propertyName, const QVariant &value)
    if value is None:
      from ..QtCore import QVariant
      value = QVariant()
    return self.uglySide.call(
        'ritual_ZN22QDesignerPropertySheet18createFakePropertyERK7QStringRK'
        '8QVariant',
        propertyName, self._valueOf(value),
    )

  def clearFakeProperties(self) -> None:
    """
    Calls Qt's 'void QDesignerPropertySheet::clearFakeProperties()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerpropertysheet.html#clearFakeProperties
    """
    #  void QDesignerPropertySheet::clearFakeProperties()
    self.uglySide.call(
        'ritual_ZN22QDesignerPropertySheet19clearFakePropertiesEv',
    )
