"""
qdesigner_internal::MetaDataBase binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDesigner/6.12.0/QtDesigner/private/metadatabase_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means qdesigner_internal::MetaDataBase to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QList, QObject
from . import QDesignerMetaDataBaseInterface, qdesigner_internal

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from . import QDesignerFormEditorInterface
  from . import QDesignerMetaDataBaseItemInterface
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDesignerFormEditorInterface = WAIT['QDesignerFormEditorInterface']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class MetaDataBase(QDesignerMetaDataBaseInterface):
  """
  The cute side of Qt's qdesigner_internal::MetaDataBase: a plain Python
  object standing in front of one C++ qdesigner_internal::MetaDataBase.

  It is built on the cute 'QDesignerMetaDataBaseInterface', as Qt's
  qdesigner_internal::MetaDataBase is built on Qt's
  QDesignerMetaDataBaseInterface, and has everything that class has.

  What exists
  -----------

  Every function of Qt's qdesigner_internal::MetaDataBase that has a ritual
  and that Python can call so far, 9 names in all: 'metaObject', 'tr',
  'core', 'item', 'metaDataBaseItem', 'add', 'remove', 'objects',
  'slotDestroyed'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *qdesigner_internal::MetaDataBase::qt_metacast(const char
    *a0)': one of Qt's own inner workings.
  - Qt's 'int qdesigner_internal::MetaDataBase::qt_metacall(QMetaObject::Call
    a0, int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'qdesigner_internal::MetaDataBase::~MetaDataBase()': the destructor:
    Python never removes a C++ qdesigner_internal::MetaDataBase.

  What has no ritual
  ------------------

  2 of the 15 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ qdesigner_internal::MetaDataBase is created at the first use, not
    by 'qdesigner_internal::MetaDataBase(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ qdesigner_internal::MetaDataBase.
  - Qt tells when it has removed the C++ qdesigner_internal::MetaDataBase.
    Every call on the cute object, and every use of it as an argument, then
    raises 'RuntimeError', and nothing reaches C++.
  """

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
    Calls Qt's 'QString qdesigner_internal::MetaDataBase::tr(const char *s,
    const char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-metadatabase.html#tr

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
    #  QString qdesigner_internal::MetaDataBase::tr(const char *s, const char
    #      *c, int n)
    return Rituals.call(
        'ritual_ZN18qdesigner_internal12MetaDataBase2trEPKcS2_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'qdesigner_internal::MetaDataBase'

  #  A C++ qdesigner_internal::MetaDataBase Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_qdesigner_internal_MetaDataBase'

  #  The functions Qt calls itself that qdesigner_internal::MetaDataBase is
  #  the first to declare. A class of a program built on it can write one
  #  anew, and Qt then calls that. For each name: the key C++ knows the
  #  function by, what it gives, and what it takes.
  __virtual_functions__ = {
      'metaDataBaseItem': (
          ('_ZNK18qdesigner_internal12MetaDataBase16metaDataBaseItemEP7QObj'
           'ect',
           ('address', 'address',
            'QtDesigner:qdesigner_internal.MetaDataBaseItem'),
           (
               ('address', 'address', 'QtCore:QObject'),
           )),
      ),
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject
    *qdesigner_internal::MetaDataBase::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-metadatabase.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *qdesigner_internal::MetaDataBase::metaObject()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK18qdesigner_internal12MetaDataBase10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def core(self) -> Optional[QDesignerFormEditorInterface]:
    """
    Calls Qt's 'QDesignerFormEditorInterface
    *qdesigner_internal::MetaDataBase::core() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-metadatabase.html#core

    Returns
    -------

    Optional[QDesignerFormEditorInterface]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QDesignerFormEditorInterface *qdesigner_internal::MetaDataBase::core()
    #      const
    ritual = 'ritual_ZNK18qdesigner_internal12MetaDataBase4coreEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK18qdesigner_internal12MetaDataBase4coreEv'
    address = self.uglySide.call(ritual)
    from . import QDesignerFormEditorInterface
    return QDesignerFormEditorInterface._cuteAt(address)

  @overload(QObject)
  @overload(NoneType)
  def item(
      self,
      object: Optional[QObject],
  ) -> Optional[QDesignerMetaDataBaseItemInterface]:
    """
    Calls Qt's 'QDesignerMetaDataBaseItemInterface
    *qdesigner_internal::MetaDataBase::item(QObject *object) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-metadatabase.html#item

    Parameters
    ----------

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QDesignerMetaDataBaseItemInterface]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QDesignerMetaDataBaseItemInterface
    #      *qdesigner_internal::MetaDataBase::item(QObject *object) const
    ritual = 'ritual_ZNK18qdesigner_internal12MetaDataBase4itemEP7QObject'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK18qdesigner_internal12MetaDataBase4itemEP7QObject')
    address = self.uglySide.call(ritual, self._addressOf(object, 'QObject'))
    from . import QDesignerMetaDataBaseItemInterface
    return QDesignerMetaDataBaseItemInterface._cuteAt(address)

  @overload(QObject)
  @overload(NoneType)
  def metaDataBaseItem(
      self,
      object: Optional[QObject],
  ) -> Optional[qdesigner_internal.MetaDataBaseItem]:
    """
    Calls Qt's 'MetaDataBaseItem
    *qdesigner_internal::MetaDataBase::metaDataBaseItem(QObject *object)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-metadatabase.html

    Parameters
    ----------

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[qdesigner_internal.MetaDataBaseItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  MetaDataBaseItem
    #      *qdesigner_internal::MetaDataBase::metaDataBaseItem(QObject
    #      *object) const
    ritual = (
        'ritual_ZNK18qdesigner_internal12MetaDataBase16metaDataBaseItemEP7Q'
        'Object')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK18qdesigner_internal12MetaDataBase16metaDataBaseIt'
          'emEP7QObject')
    address = self.uglySide.call(ritual, self._addressOf(object, 'QObject'))
    return qdesigner_internal.MetaDataBaseItem._cuteAt(address)

  def objects(self) -> QList[QObject]:
    """
    Calls Qt's 'QObjectList qdesigner_internal::MetaDataBase::objects()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-metadatabase.html#objects

    Returns
    -------

    QList[QObject]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QObjectList qdesigner_internal::MetaDataBase::objects() const
    address = self.uglySide.call(
        'ritual_ZNK18qdesigner_internal12MetaDataBase7objectsEv',
    )
    return QList[QObject]._cuteOwning(address)

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

  @overload(QDesignerFormEditorInterface)
  @overload(NoneType)
  @overload(QDesignerFormEditorInterface, QObject)
  @overload(QDesignerFormEditorInterface, NoneType)
  @overload(NoneType, QObject)
  @overload(NoneType, NoneType)
  def __init__(
      self,
      core: Optional[QDesignerFormEditorInterface],
      parent: Optional[QObject] = None,
  ) -> None:
    """
    Notes what was given, for Qt's
    'qdesigner_internal::MetaDataBase::MetaDataBase(
    QDesignerFormEditorInterface *core, QObject *parent)', which is called at
    the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-metadatabase.html#MetaDataBase

    Parameters
    ----------

    core : Optional[QDesignerFormEditorInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  qdesigner_internal::MetaDataBase::MetaDataBase(
    #      QDesignerFormEditorInterface *core, QObject *parent)
    self._noteCreation(MetaDataBase, lambda: Rituals.call(
        'ritual_ZN18qdesigner_internal12MetaDataBaseC1EP28QDesignerFormEdit'
        'orInterfaceP7QObject',
        self._addressOf(core), self._addressOf(parent, 'QObject'),
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

  @overload(QObject)
  @overload(NoneType)
  def add(self, object: Optional[QObject]) -> None:
    """
    Calls Qt's 'void qdesigner_internal::MetaDataBase::add(QObject *object)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-metadatabase.html#add

    Parameters
    ----------

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void qdesigner_internal::MetaDataBase::add(QObject *object)
    ritual = 'ritual_ZN18qdesigner_internal12MetaDataBase3addEP7QObject'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18qdesigner_internal12MetaDataBase3addEP7QObject')
    self.uglySide.call(ritual, self._addressOf(object, 'QObject'))

  @overload(QObject)
  @overload(NoneType)
  def remove(self, object: Optional[QObject]) -> None:
    """
    Calls Qt's 'void qdesigner_internal::MetaDataBase::remove(QObject
    *object)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-metadatabase.html#remove

    Parameters
    ----------

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void qdesigner_internal::MetaDataBase::remove(QObject *object)
    ritual = 'ritual_ZN18qdesigner_internal12MetaDataBase6removeEP7QObject'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18qdesigner_internal12MetaDataBase6removeEP7QObject')
    self.uglySide.call(ritual, self._addressOf(object, 'QObject'))

  @overload(QObject)
  @overload(NoneType)
  def slotDestroyed(self, object: Optional[QObject]) -> None:
    """
    Calls Qt's 'void qdesigner_internal::MetaDataBase::slotDestroyed(QObject
    *object)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-metadatabase.html#slotDestroyed

    Parameters
    ----------

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void qdesigner_internal::MetaDataBase::slotDestroyed(QObject *object)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal12MetaDataBase13slotDestroyedEP7QObje'
        'ct',
        self._addressOf(object, 'QObject'),
    )
