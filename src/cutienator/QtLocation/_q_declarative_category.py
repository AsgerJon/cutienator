"""
QDeclarativeCategory binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtLocation/6.12.0/QtLocation/private/qdeclarativecategory_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QDeclarativeCategory to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import QObject
from ..QtQml import QQmlParserStatus

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from . import QDeclarativeGeoServiceProvider, QPlaceCategory, QPlaceIcon
  from . import QPlaceManager
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDeclarativeGeoServiceProvider = WAIT['QDeclarativeGeoServiceProvider']
  QPlaceCategory = WAIT['QPlaceCategory']
  QPlaceIcon = WAIT['QPlaceIcon']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QDeclarativeCategory(QObject, QQmlParserStatus):
  """
  The cute side of Qt's QDeclarativeCategory: a plain Python object standing
  in front of one C++ QDeclarativeCategory.

  It is built on the cute 'QObject', as Qt's QDeclarativeCategory is built on
  Qt's QObject, and has everything that class has. It is built on the cute
  'QQmlParserStatus' as well, as Qt's QDeclarativeCategory is built on Qt's
  QQmlParserStatus too, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QDeclarativeCategory that has a ritual and that
  Python can call so far, 30 names in all: 'metaObject', 'tr', 'classBegin',
  'componentComplete', 'setPlugin', 'plugin', 'category', 'setCategory',
  'categoryId', 'setCategoryId', 'name', 'setName', 'visibility',
  'setVisibility', 'icon', 'setIcon', 'errorString', 'status', 'setStatus',
  'save', 'remove', 'pluginChanged', 'categoryIdChanged', 'nameChanged',
  'visibilityChanged', 'iconChanged', 'statusChanged', 'replyFinished',
  'pluginReady', 'manager'. It can be made from Python, in 2 ways; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QDeclarativeCategory::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QDeclarativeCategory::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QDeclarativeCategory::~QDeclarativeCategory()': the destructor:
    Python never removes a C++ QDeclarativeCategory.

  What has no ritual
  ------------------

  2 of the 37 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QDeclarativeCategory is created at the first use, not by
    'QDeclarativeCategory(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QDeclarativeCategory.
  - Qt tells when it has removed the C++ QDeclarativeCategory. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  #  The enums Qt writes inside QDeclarativeCategory, each a class in here as
  #  in C++, and the names Qt has for the combinations of its flags enums.

  class Status(CuteNum):
    """
    The enum 'QDeclarativeCategory::Status' of Qt, with the 4 names Qt gives
    in it.
    """

    Ready = Kee[int](0)
    Saving = Kee[int](1)
    Removing = Kee[int](2)
    Error = Kee[int](3)

  class Visibility(CuteNum):
    """
    The enum 'QDeclarativeCategory::Visibility' of Qt, with the 4 names Qt
    gives in it.
    """

    UnspecifiedVisibility = Kee[int](0)
    DeviceVisibility = Kee[int](1)
    PrivateVisibility = Kee[int](2)
    PublicVisibility = Kee[int](4)

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
    Calls Qt's 'QString QDeclarativeCategory::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qdeclarativecategory.html#tr

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
    #  QString QDeclarativeCategory::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN20QDeclarativeCategory2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QDeclarativeCategory'

  #  Qt's QDeclarativeCategory is built on more than one class. The part of a
  #  C++ QDeclarativeCategory that belongs to a class after the first begins
  #  somewhere inside the object, and the ritual named for that class gives
  #  where; see 'CuteMixin._addressAs'.
  __cast_rituals__ = {
      'QQmlParserStatus':
          'ritual_cast_QDeclarativeCategory_QQmlParserStatus',
  }

  #  A C++ QDeclarativeCategory Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QDeclarativeCategory'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QDeclarativeCategory::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativecategory.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QDeclarativeCategory::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK20QDeclarativeCategory10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def plugin(self) -> Optional[QDeclarativeGeoServiceProvider]:
    """
    Calls Qt's 'QDeclarativeGeoServiceProvider
    *QDeclarativeCategory::plugin() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdeclarativecategory.html#plugin

    Returns
    -------

    Optional[QDeclarativeGeoServiceProvider]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QDeclarativeGeoServiceProvider *QDeclarativeCategory::plugin() const
    address = self.uglySide.call('ritual_ZNK20QDeclarativeCategory6pluginEv')
    from . import QDeclarativeGeoServiceProvider
    return QDeclarativeGeoServiceProvider._cuteAt(address)

  def categoryId(self) -> str:
    """
    Calls Qt's 'QString QDeclarativeCategory::categoryId() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativecategory.html#categoryId

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QDeclarativeCategory::categoryId() const
    return self.uglySide.call(
        'ritual_ZNK20QDeclarativeCategory10categoryIdEv',
    )

  def name(self) -> str:
    """
    Calls Qt's 'QString QDeclarativeCategory::name() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdeclarativecategory.html#name

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QDeclarativeCategory::name() const
    return self.uglySide.call('ritual_ZNK20QDeclarativeCategory4nameEv')

  def visibility(self) -> Visibility:
    """
    Calls Qt's 'Visibility QDeclarativeCategory::visibility() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativecategory.html#visibility

    Returns
    -------

    Visibility
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Visibility(number)'
      gives.
    """
    #  Visibility QDeclarativeCategory::visibility() const
    return QDeclarativeCategory.Visibility(self.uglySide.call(
        'ritual_ZNK20QDeclarativeCategory10visibilityEv',
    ))

  def icon(self) -> QPlaceIcon:
    """
    Calls Qt's 'QPlaceIcon QDeclarativeCategory::icon() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdeclarativecategory.html#icon

    Returns
    -------

    QPlaceIcon
      A new cute QPlaceIcon around the copy Qt gave back. Python owns it.
    """
    #  QPlaceIcon QDeclarativeCategory::icon() const
    address = self.uglySide.call('ritual_ZNK20QDeclarativeCategory4iconEv')
    from . import QPlaceIcon
    return QPlaceIcon._cuteOwning(address)

  def errorString(self) -> str:
    """
    Calls Qt's 'QString QDeclarativeCategory::errorString() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativecategory.html#errorString

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QDeclarativeCategory::errorString() const
    return self.uglySide.call(
        'ritual_ZNK20QDeclarativeCategory11errorStringEv',
    )

  def status(self) -> Status:
    """
    Calls Qt's 'Status QDeclarativeCategory::status() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdeclarativecategory.html#status

    Returns
    -------

    Status
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Status(number)' gives.
    """
    #  Status QDeclarativeCategory::status() const
    return QDeclarativeCategory.Status(self.uglySide.call(
        'ritual_ZNK20QDeclarativeCategory6statusEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QDeclarativeGeoServiceProvider)
  @overload(NoneType)
  def setPlugin(
      self,
      plugin: Optional[QDeclarativeGeoServiceProvider],
  ) -> None:
    """
    Calls Qt's 'void
    QDeclarativeCategory::setPlugin(QDeclarativeGeoServiceProvider *plugin)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativecategory.html#setPlugin

    Parameters
    ----------

    plugin : Optional[QDeclarativeGeoServiceProvider]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QDeclarativeCategory::setPlugin(QDeclarativeGeoServiceProvider
    #      *plugin)
    self.uglySide.call(
        'ritual_ZN20QDeclarativeCategory9setPluginEP30QDeclarativeGeoServic'
        'eProvider',
        self._addressOf(plugin),
    )

  @overload(QPlaceCategory)
  def setCategory(self, category: QPlaceCategory) -> None:
    """
    Calls Qt's 'void QDeclarativeCategory::setCategory(const QPlaceCategory
    &category)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativecategory.html#setCategory

    Parameters
    ----------

    category : QPlaceCategory
      Passed on as a value: Qt reads the C++ QPlaceCategory, which stays
      Python's own.
    """
    #  void QDeclarativeCategory::setCategory(const QPlaceCategory &category)
    self.uglySide.call(
        'ritual_ZN20QDeclarativeCategory11setCategoryERK14QPlaceCategory',
        self._valueOf(category),
    )

  @overload(str)
  def setCategoryId(self, catID: str) -> None:
    """
    Calls Qt's 'void QDeclarativeCategory::setCategoryId(const QString
    &catID)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativecategory.html#setCategoryId

    Parameters
    ----------

    catID : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QDeclarativeCategory::setCategoryId(const QString &catID)
    self.uglySide.call(
        'ritual_ZN20QDeclarativeCategory13setCategoryIdERK7QString', catID,
    )

  @overload(str)
  def setName(self, name: str) -> None:
    """
    Calls Qt's 'void QDeclarativeCategory::setName(const QString &name)'.

    Qt's own words: https://doc.qt.io/qt-6/qdeclarativecategory.html#setName

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QDeclarativeCategory::setName(const QString &name)
    self.uglySide.call(
        'ritual_ZN20QDeclarativeCategory7setNameERK7QString', name,
    )

  @overload(Visibility)
  def setVisibility(self, visibility: Visibility) -> None:
    """
    Calls Qt's 'void QDeclarativeCategory::setVisibility(Visibility
    visibility)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativecategory.html#setVisibility

    Parameters
    ----------

    visibility : Visibility
      Passed on as its number.
    """
    #  void QDeclarativeCategory::setVisibility(Visibility visibility)
    self.uglySide.call(
        'ritual_ZN20QDeclarativeCategory13setVisibilityENS_10VisibilityE',
        visibility.value,
    )

  @overload(QPlaceIcon)
  def setIcon(self, icon: QPlaceIcon) -> None:
    """
    Calls Qt's 'void QDeclarativeCategory::setIcon(const QPlaceIcon &icon)'.

    Qt's own words: https://doc.qt.io/qt-6/qdeclarativecategory.html#setIcon

    Parameters
    ----------

    icon : QPlaceIcon
      Passed on as a value: Qt reads the C++ QPlaceIcon, which stays Python's
      own.
    """
    #  void QDeclarativeCategory::setIcon(const QPlaceIcon &icon)
    self.uglySide.call(
        'ritual_ZN20QDeclarativeCategory7setIconERK10QPlaceIcon',
        self._valueOf(icon),
    )

  @overload(Status)
  @overload(Status, str)
  def setStatus(self, status: Status, errorString: str = '') -> None:
    """
    Calls Qt's 'void QDeclarativeCategory::setStatus(Status status, const
    QString &errorString)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativecategory.html#setStatus

    Parameters
    ----------

    status : Status
      Passed on as its number.

    errorString : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.
    """
    #  void QDeclarativeCategory::setStatus(Status status, const QString
    #      &errorString)
    self.uglySide.call(
        'ritual_ZN20QDeclarativeCategory9setStatusENS_6StatusERK7QString',
        status.value, errorString,
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

  @overload()
  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's
    'QDeclarativeCategory::QDeclarativeCategory(QObject *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativecategory.html#QDeclarativeCategory

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QDeclarativeCategory::QDeclarativeCategory(QObject *parent)
    self._noteCreation(QDeclarativeCategory, lambda: Rituals.call(
        'ritual_ZN20QDeclarativeCategoryC1EP7QObject',
        self._addressOf(parent, 'QObject'),
    ))

  @overload(QPlaceCategory, QDeclarativeGeoServiceProvider)
  @overload(QPlaceCategory, NoneType)
  @overload(QPlaceCategory, QDeclarativeGeoServiceProvider, QObject)
  @overload(QPlaceCategory, QDeclarativeGeoServiceProvider, NoneType)
  @overload(QPlaceCategory, NoneType, QObject)
  @overload(QPlaceCategory, NoneType, NoneType)
  def __init__(
      self,
      category: QPlaceCategory,
      plugin: Optional[QDeclarativeGeoServiceProvider],
      parent: Optional[QObject] = None,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QDeclarativeCategory::QDeclarativeCategory(const QPlaceCategory
    &category, QDeclarativeGeoServiceProvider *plugin, QObject *parent)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativecategory.html#QDeclarativeCategory

    Parameters
    ----------

    category : QPlaceCategory
      Passed on as a value: Qt reads the C++ QPlaceCategory, which stays
      Python's own.

    plugin : Optional[QDeclarativeGeoServiceProvider]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QDeclarativeCategory::QDeclarativeCategory(const QPlaceCategory
    #      &category, QDeclarativeGeoServiceProvider *plugin, QObject
    #      *parent)
    self._noteCreation(QDeclarativeCategory, lambda: Rituals.call(
        'ritual_ZN20QDeclarativeCategoryC1ERK14QPlaceCategoryP30QDeclarativ'
        'eGeoServiceProviderP7QObject',
        self._valueOf(category), self._addressOf(plugin),
        self._addressOf(parent, 'QObject'),
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

  def classBegin(self) -> None:
    """
    Calls Qt's 'void QDeclarativeCategory::classBegin()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativecategory.html#classBegin
    """
    #  void QDeclarativeCategory::classBegin()
    ritual = 'ritual_ZN20QDeclarativeCategory10classBeginEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN20QDeclarativeCategory10classBeginEv'
    self.uglySide.call(ritual)

  def componentComplete(self) -> None:
    """
    Calls Qt's 'void QDeclarativeCategory::componentComplete()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativecategory.html#componentComplete
    """
    #  void QDeclarativeCategory::componentComplete()
    ritual = 'ritual_ZN20QDeclarativeCategory17componentCompleteEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN20QDeclarativeCategory17componentCompleteEv'
    self.uglySide.call(ritual)

  def category(self) -> QPlaceCategory:
    """
    Calls Qt's 'QPlaceCategory QDeclarativeCategory::category()'.

    Qt's own words: https://doc.qt.io/qt-6/qdeclarativecategory.html#category

    Returns
    -------

    QPlaceCategory
      A new cute QPlaceCategory around the copy Qt gave back. Python owns it.
    """
    #  QPlaceCategory QDeclarativeCategory::category()
    address = self.uglySide.call(
        'ritual_ZN20QDeclarativeCategory8categoryEv',
    )
    from . import QPlaceCategory
    return QPlaceCategory._cuteOwning(address)

  @overload()
  @overload(str)
  def save(self, parentId: str = '') -> None:
    """
    Calls Qt's 'void QDeclarativeCategory::save(const QString &parentId)'.

    Qt's own words: https://doc.qt.io/qt-6/qdeclarativecategory.html#save

    Parameters
    ----------

    parentId : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.
    """
    #  void QDeclarativeCategory::save(const QString &parentId)
    self.uglySide.call(
        'ritual_ZN20QDeclarativeCategory4saveERK7QString', parentId,
    )

  def remove(self) -> None:
    """
    Calls Qt's 'void QDeclarativeCategory::remove()'.

    Qt's own words: https://doc.qt.io/qt-6/qdeclarativecategory.html#remove
    """
    #  void QDeclarativeCategory::remove()
    self.uglySide.call('ritual_ZN20QDeclarativeCategory6removeEv')

  def pluginChanged(self) -> None:
    """
    Calls Qt's 'void QDeclarativeCategory::pluginChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativecategory.html#pluginChanged
    """
    #  void QDeclarativeCategory::pluginChanged()
    self.uglySide.call('ritual_ZN20QDeclarativeCategory13pluginChangedEv')

  def categoryIdChanged(self) -> None:
    """
    Calls Qt's 'void QDeclarativeCategory::categoryIdChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativecategory.html#categoryIdChanged
    """
    #  void QDeclarativeCategory::categoryIdChanged()
    self.uglySide.call(
        'ritual_ZN20QDeclarativeCategory17categoryIdChangedEv',
    )

  def nameChanged(self) -> None:
    """
    Calls Qt's 'void QDeclarativeCategory::nameChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativecategory.html#nameChanged
    """
    #  void QDeclarativeCategory::nameChanged()
    self.uglySide.call('ritual_ZN20QDeclarativeCategory11nameChangedEv')

  def visibilityChanged(self) -> None:
    """
    Calls Qt's 'void QDeclarativeCategory::visibilityChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativecategory.html#visibilityChanged
    """
    #  void QDeclarativeCategory::visibilityChanged()
    self.uglySide.call(
        'ritual_ZN20QDeclarativeCategory17visibilityChangedEv',
    )

  def iconChanged(self) -> None:
    """
    Calls Qt's 'void QDeclarativeCategory::iconChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativecategory.html#iconChanged
    """
    #  void QDeclarativeCategory::iconChanged()
    self.uglySide.call('ritual_ZN20QDeclarativeCategory11iconChangedEv')

  def statusChanged(self) -> None:
    """
    Calls Qt's 'void QDeclarativeCategory::statusChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativecategory.html#statusChanged
    """
    #  void QDeclarativeCategory::statusChanged()
    self.uglySide.call('ritual_ZN20QDeclarativeCategory13statusChangedEv')

  def replyFinished(self) -> None:
    """
    Calls Qt's 'void QDeclarativeCategory::replyFinished()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativecategory.html#replyFinished
    """
    #  void QDeclarativeCategory::replyFinished()
    self.uglySide.call('ritual_ZN20QDeclarativeCategory13replyFinishedEv')

  def pluginReady(self) -> None:
    """
    Calls Qt's 'void QDeclarativeCategory::pluginReady()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativecategory.html#pluginReady
    """
    #  void QDeclarativeCategory::pluginReady()
    self.uglySide.call('ritual_ZN20QDeclarativeCategory11pluginReadyEv')

  def manager(self) -> Optional[QPlaceManager]:
    """
    Calls Qt's 'QPlaceManager *QDeclarativeCategory::manager()'.

    Qt's own words: https://doc.qt.io/qt-6/qdeclarativecategory.html#manager

    Returns
    -------

    Optional[QPlaceManager]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPlaceManager *QDeclarativeCategory::manager()
    address = self.uglySide.call('ritual_ZN20QDeclarativeCategory7managerEv')
    from . import QPlaceManager
    return QPlaceManager._cuteAt(address)
