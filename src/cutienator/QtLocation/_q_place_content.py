"""
QPlaceContent binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtLocation/qplacecontent.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QMap

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QVariant
  from . import QPlaceContentPrivate, QPlaceSupplier, QPlaceUser
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPlaceSupplier = WAIT['QPlaceSupplier']
  QPlaceUser = WAIT['QPlaceUser']
  QVariant = WAIT['QVariant']


class QPlaceContent(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QPlaceContent: a plain Python object standing in
  front of one C++ QPlaceContent.

  C++ hands a QPlaceContent around as a copy, so every C++ QPlaceContent
  behind a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QPlaceContent that has a ritual and that Python can
  call so far, 13 names in all: 'detach', '__eq__', '__ne__', 'type',
  'value', 'setValue', 'supplier', 'setSupplier', 'user', 'setUser',
  'attribution', 'setAttribution', 'd_func'. It can be made from Python, in 2
  ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QPlaceContent::~QPlaceContent()': the destructor: Python removes
    its C++ QPlaceContent by it, and has no other use for it.
  - Qt's 'QPlaceContent &QPlaceContent::operator=(const QPlaceContent
    &other)': assignment: Python binds a name and has no operator for it.
  - Qt's 'QPlaceContent::QPlaceContent(QPlaceContent &&other)': takes a type
    Python has no way to hand over yet.
  - Qt's 'QPlaceContent &QPlaceContent::operator=(QPlaceContent &&other)':
    assignment: Python binds a name and has no operator for it.
  - Qt's 'void QPlaceContent::swap(QPlaceContent &other)': takes a type
    Python has no way to hand over yet.
  - Qt's 'QList<DataTag> QPlaceContent::dataTags() const': gives a type
    Python has no way to take yet.
  - Qt's 'const QPlaceContentPrivate *QPlaceContent::d_func() const': takes
    in Python what 'QPlaceContentPrivate *QPlaceContent::d_func()' takes.

  What to expect
  --------------

  - The C++ QPlaceContent is created at the first use, not by
    'QPlaceContent(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QPlaceContent back gives a copy the ritual made for
    Python, in a new cute QPlaceContent.
  - Each name of Qt's QPlaceContent that has no cute function yet,
    'dataTags', 'swap', holds a function that raises 'NotImplementedError',
    and its docstring says why.
  """

  #  The enums Qt writes inside QPlaceContent, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class DataTag(CuteNum):
    """
    The enum 'QPlaceContent::DataTag' of Qt, with the 16 names Qt gives in
    it.
    """

    ContentSupplier = Kee[int](0)
    ContentUser = Kee[int](1)
    ContentAttribution = Kee[int](2)
    ImageId = Kee[int](3)
    ImageUrl = Kee[int](4)
    ImageMimeType = Kee[int](5)
    EditorialTitle = Kee[int](6)
    EditorialText = Kee[int](7)
    EditorialLanguage = Kee[int](8)
    ReviewId = Kee[int](9)
    ReviewDateTime = Kee[int](10)
    ReviewTitle = Kee[int](11)
    ReviewText = Kee[int](12)
    ReviewLanguage = Kee[int](13)
    ReviewRating = Kee[int](14)
    CustomDataTag = Kee[int](1000)

  class Type(CuteNum):
    """
    The enum 'QPlaceContent::Type' of Qt, with the 5 names Qt gives in it.
    """

    NoType = Kee[int](0)
    ImageType = Kee[int](1)
    ReviewType = Kee[int](2)
    EditorialType = Kee[int](3)
    CustomType = Kee[int](256)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QPlaceContent'

  #  Qt's '~QPlaceContent()'. Naming it makes this a value class: Python owns
  #  every C++ QPlaceContent behind a cute one, and removes it by this
  #  ritual.
  __delete_ritual__ = 'ritual_ZN13QPlaceContentD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def type(self) -> Type:
    """
    Calls Qt's 'QPlaceContent::Type QPlaceContent::type() const'.

    Qt's own words: https://doc.qt.io/qt-6/qplacecontent.html#type

    Returns
    -------

    Type
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Type(number)' gives.
    """
    #  QPlaceContent::Type QPlaceContent::type() const
    return QPlaceContent.Type(self.uglySide.call(
        'ritual_ZNK13QPlaceContent4typeEv',
    ))

  @overload(DataTag)
  def value(self, tag: DataTag) -> QVariant:
    """
    Calls Qt's 'QVariant QPlaceContent::value(DataTag tag) const'.

    Qt's own words: https://doc.qt.io/qt-6/qplacecontent.html#value

    Parameters
    ----------

    tag : DataTag
      Passed on as its number.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QPlaceContent::value(DataTag tag) const
    address = self.uglySide.call(
        'ritual_ZNK13QPlaceContent5valueENS_7DataTagE', tag.value,
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  def supplier(self) -> QPlaceSupplier:
    """
    Calls Qt's 'QPlaceSupplier QPlaceContent::supplier() const'.

    Qt's own words: https://doc.qt.io/qt-6/qplacecontent.html#supplier

    Returns
    -------

    QPlaceSupplier
      A new cute QPlaceSupplier around the copy Qt gave back. Python owns it.
    """
    #  QPlaceSupplier QPlaceContent::supplier() const
    address = self.uglySide.call('ritual_ZNK13QPlaceContent8supplierEv')
    from . import QPlaceSupplier
    return QPlaceSupplier._cuteOwning(address)

  def user(self) -> QPlaceUser:
    """
    Calls Qt's 'QPlaceUser QPlaceContent::user() const'.

    Qt's own words: https://doc.qt.io/qt-6/qplacecontent.html#user

    Returns
    -------

    QPlaceUser
      A new cute QPlaceUser around the copy Qt gave back. Python owns it.
    """
    #  QPlaceUser QPlaceContent::user() const
    address = self.uglySide.call('ritual_ZNK13QPlaceContent4userEv')
    from . import QPlaceUser
    return QPlaceUser._cuteOwning(address)

  def attribution(self) -> str:
    """
    Calls Qt's 'QString QPlaceContent::attribution() const'.

    Qt's own words: https://doc.qt.io/qt-6/qplacecontent.html#attribution

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QPlaceContent::attribution() const
    return self.uglySide.call('ritual_ZNK13QPlaceContent11attributionEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(DataTag, QVariant)
  def setValue(self, tag: DataTag, a1: QVariant) -> None:
    """
    Calls Qt's 'void QPlaceContent::setValue(DataTag tag, const QVariant
    &a1)'.

    Qt's own words: https://doc.qt.io/qt-6/qplacecontent.html#setValue

    Parameters
    ----------

    tag : DataTag
      Passed on as its number.

    a1 : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void QPlaceContent::setValue(DataTag tag, const QVariant &a1)
    self.uglySide.call(
        'ritual_ZN13QPlaceContent8setValueENS_7DataTagERK8QVariant',
        tag.value, self._valueOf(a1),
    )

  @overload(QPlaceSupplier)
  def setSupplier(self, supplier: QPlaceSupplier) -> None:
    """
    Calls Qt's 'void QPlaceContent::setSupplier(const QPlaceSupplier
    &supplier)'.

    Qt's own words: https://doc.qt.io/qt-6/qplacecontent.html#setSupplier

    Parameters
    ----------

    supplier : QPlaceSupplier
      Passed on as a value: Qt reads the C++ QPlaceSupplier, which stays
      Python's own.
    """
    #  void QPlaceContent::setSupplier(const QPlaceSupplier &supplier)
    self.uglySide.call(
        'ritual_ZN13QPlaceContent11setSupplierERK14QPlaceSupplier',
        self._valueOf(supplier),
    )

  @overload(QPlaceUser)
  def setUser(self, user: QPlaceUser) -> None:
    """
    Calls Qt's 'void QPlaceContent::setUser(const QPlaceUser &user)'.

    Qt's own words: https://doc.qt.io/qt-6/qplacecontent.html#setUser

    Parameters
    ----------

    user : QPlaceUser
      Passed on as a value: Qt reads the C++ QPlaceUser, which stays Python's
      own.
    """
    #  void QPlaceContent::setUser(const QPlaceUser &user)
    self.uglySide.call(
        'ritual_ZN13QPlaceContent7setUserERK10QPlaceUser',
        self._valueOf(user),
    )

  @overload(str)
  def setAttribution(self, attribution: str) -> None:
    """
    Calls Qt's 'void QPlaceContent::setAttribution(const QString
    &attribution)'.

    Qt's own words: https://doc.qt.io/qt-6/qplacecontent.html#setAttribution

    Parameters
    ----------

    attribution : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QPlaceContent::setAttribution(const QString &attribution)
    self.uglySide.call(
        'ritual_ZN13QPlaceContent14setAttributionERK7QString', attribution,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __eq__(self, other: QPlaceContent) -> bool:
    """
    Calls Qt's 'bool QPlaceContent::operator==(const QPlaceContent &other)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qplacecontent.html#operator==

    Parameters
    ----------

    other : QPlaceContent
      Passed on as a value: Qt reads the C++ QPlaceContent, which stays
      Python's own.
    """
    #  bool QPlaceContent::operator==(const QPlaceContent &other) const
    return self.uglySide.call(
        'ritual_ZNK13QPlaceContenteqERKS_', self._valueOf(other),
    )

  @overload.fallback
  def __eq__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(THIS)
  def __ne__(self, other: QPlaceContent) -> bool:
    """
    Calls Qt's 'bool QPlaceContent::operator!=(const QPlaceContent &other)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qplacecontent.html#operator!=

    Parameters
    ----------

    other : QPlaceContent
      Passed on as a value: Qt reads the C++ QPlaceContent, which stays
      Python's own.
    """
    #  bool QPlaceContent::operator!=(const QPlaceContent &other) const
    return self.uglySide.call(
        'ritual_ZNK13QPlaceContentneERKS_', self._valueOf(other),
    )

  @overload.fallback
  def __ne__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload()
  @overload(Type)
  def __init__(self, type: Type = Type.NoType) -> None:
    """
    Notes what was given, for Qt's 'QPlaceContent::QPlaceContent(Type type)',
    which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qplacecontent.html#QPlaceContent

    Parameters
    ----------

    type : Type
      Passed on as its number. May be left out, as in Qt: it is then
      Type.NoType.
    """
    #  QPlaceContent::QPlaceContent(Type type)
    self._noteCreation(QPlaceContent, lambda: Rituals.call(
        'ritual_ZN13QPlaceContentC1ENS_4TypeE', type.value,
    ))

  @overload(THIS)
  def __init__(self, other: QPlaceContent) -> None:
    """
    Notes what was given, for Qt's 'QPlaceContent::QPlaceContent(const
    QPlaceContent &other)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qplacecontent.html#QPlaceContent

    Parameters
    ----------

    other : QPlaceContent
      Passed on as a value: Qt reads the C++ QPlaceContent, which stays
      Python's own.
    """
    #  QPlaceContent::QPlaceContent(const QPlaceContent &other)
    self._noteCreation(QPlaceContent, lambda: Rituals.call(
        'ritual_ZN13QPlaceContentC1ERKS_', self._valueOf(other),
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

  def detach(self) -> None:
    """
    Calls Qt's 'void QPlaceContent::detach()'.

    Qt's own words: https://doc.qt.io/qt-6/qplacecontent.html#detach
    """
    #  void QPlaceContent::detach()
    self.uglySide.call('ritual_ZN13QPlaceContent6detachEv')

  def d_func(self) -> Optional[QPlaceContentPrivate]:
    """
    Calls Qt's 'QPlaceContentPrivate *QPlaceContent::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qplacecontent.html#d_func

    Returns
    -------

    Optional[QPlaceContentPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPlaceContentPrivate *QPlaceContent::d_func()
    address = self.uglySide.call('ritual_ZN13QPlaceContent6d_funcEv')
    from . import QPlaceContentPrivate
    return QPlaceContentPrivate._cuteAt(address)

  @staticmethod
  def dataTags(*__, **_) -> Never:
    """
    Qt's 'QList<DataTag> QPlaceContent::dataTags() const': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QPlaceContent.dataTags' has no cute function yet. Qt's "
        "'QList<DataTag> QPlaceContent::dataTags() const': gives a type "
        "Python has no way to take yet.")

  @staticmethod
  def swap(*__, **_) -> Never:
    """
    Qt's 'void QPlaceContent::swap(QPlaceContent &other)': takes a type
    Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QPlaceContent.swap' has no cute function yet. Qt's 'void "
        "QPlaceContent::swap(QPlaceContent &other)': takes a type Python "
        "has no way to hand over yet.")


#  Qt's 'QMap<int, QPlaceContent>': the QMap from a number to QPlaceContent,
#  which 'QMap[int, QPlaceContent]' gives. It is completed here, in the file
#  of the class of its values.
QMap.createKind(
    int, QPlaceContent, 'value',
    make='ritual_map_make_QMap_int_QPlaceContent',
    put='ritual_map_put_QMap_int_QPlaceContent',
    size='ritual_map_size_QMap_int_QPlaceContent',
    key='ritual_map_key_QMap_int_QPlaceContent',
    value='ritual_map_value_QMap_int_QPlaceContent',
    has='ritual_map_has_QMap_int_QPlaceContent',
    get='ritual_map_get_QMap_int_QPlaceContent',
    drop='ritual_map_drop_QMap_int_QPlaceContent',
)
