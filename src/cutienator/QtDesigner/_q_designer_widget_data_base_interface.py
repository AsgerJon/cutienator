"""
QDesignerWidgetDataBaseInterface binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDesigner/abstractwidgetdatabase.h, Qt 6.12.0. Changes made here are
#  lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from . import QDesignerFormEditorInterface
  from . import QDesignerWidgetDataBaseItemInterface
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDesignerWidgetDataBaseItemInterface = WAIT['QDesignerWidgetDataBaseItemInterface']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QDesignerWidgetDataBaseInterface(QObject):
  """
  The cute side of Qt's QDesignerWidgetDataBaseInterface: a plain Python
  object standing in front of one C++ QDesignerWidgetDataBaseInterface.

  It is built on the cute 'QObject', as Qt's QDesignerWidgetDataBaseInterface
  is built on Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QDesignerWidgetDataBaseInterface that has a ritual
  and that Python can call so far, 13 names in all: 'metaObject', 'tr',
  'count', 'item', 'indexOf', 'insert', 'append', 'indexOfObject',
  'indexOfClassName', 'core', 'isContainer', 'isCustom', 'changed'. It can be
  made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QDesignerWidgetDataBaseInterface::qt_metacast(const char
    *a0)': one of Qt's own inner workings.
  - Qt's 'int QDesignerWidgetDataBaseInterface::qt_metacall(QMetaObject::Call
    a0, int a1, void **a2)': one of Qt's own inner workings.
  - Qt's
    'QDesignerWidgetDataBaseInterface::~QDesignerWidgetDataBaseInterface()':
    the destructor: Python never removes a C++
    QDesignerWidgetDataBaseInterface.

  What has no ritual
  ------------------

  2 of the 19 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QDesignerWidgetDataBaseInterface is created at the first use, not
    by 'QDesignerWidgetDataBaseInterface(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QDesignerWidgetDataBaseInterface.
  - Qt tells when it has removed the C++ QDesignerWidgetDataBaseInterface.
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
    Calls Qt's 'QString QDesignerWidgetDataBaseInterface::tr(const char *s,
    const char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerwidgetdatabaseinterface.html#tr

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
    #  QString QDesignerWidgetDataBaseInterface::tr(const char *s, const char
    #      *c, int n)
    return Rituals.call(
        'ritual_ZN32QDesignerWidgetDataBaseInterface2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QDesignerWidgetDataBaseInterface'

  #  A C++ QDesignerWidgetDataBaseInterface Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QDesignerWidgetDataBaseInterface'

  #  The functions Qt calls itself that QDesignerWidgetDataBaseInterface is
  #  the first to declare. A class of a program built on it can write one
  #  anew, and Qt then calls that. For each name: the key C++ knows the
  #  function by, what it gives, and what it takes.
  __virtual_functions__ = {
      'count': (
          ('_ZNK32QDesignerWidgetDataBaseInterface5countEv',
           ('int', 'number', ''),
           ()),
      ),
      'item': (
          ('_ZNK32QDesignerWidgetDataBaseInterface4itemEi',
           ('address', 'address',
            'QtDesigner:QDesignerWidgetDataBaseItemInterface'),
           (
               ('int', 'number', ''),
           )),
      ),
      'indexOf': (
          ('_ZNK32QDesignerWidgetDataBaseInterface7indexOfEP36QDesignerWidg'
           'etDataBaseItemInterface',
           ('int', 'number', ''),
           (
               ('address', 'address',
                'QtDesigner:QDesignerWidgetDataBaseItemInterface'),
           )),
      ),
      'insert': (
          ('_ZN32QDesignerWidgetDataBaseInterface6insertEiP36QDesignerWidge'
           'tDataBaseItemInterface',
           ('nothing', 'nothing', ''),
           (
               ('int', 'number', ''),
               ('address', 'address',
                'QtDesigner:QDesignerWidgetDataBaseItemInterface'),
           )),
      ),
      'append': (
          ('_ZN32QDesignerWidgetDataBaseInterface6appendEP36QDesignerWidget'
           'DataBaseItemInterface',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address',
                'QtDesigner:QDesignerWidgetDataBaseItemInterface'),
           )),
      ),
      'indexOfObject': (
          ('_ZNK32QDesignerWidgetDataBaseInterface13indexOfObjectEP7QObject'
           'b',
           ('int', 'number', ''),
           (
               ('address', 'address', 'QtCore:QObject'),
               ('bool', 'number', ''),
           )),
      ),
      'indexOfClassName': (
          ('_ZNK32QDesignerWidgetDataBaseInterface16indexOfClassNameERK7QSt'
           'ringb',
           ('int', 'number', ''),
           (
               ('address', 'text', ''),
               ('bool', 'number', ''),
           )),
      ),
      'core': (
          ('_ZNK32QDesignerWidgetDataBaseInterface4coreEv',
           ('address', 'address', 'QtDesigner:QDesignerFormEditorInterface'),
           ()),
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
    *QDesignerWidgetDataBaseInterface::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerwidgetdatabaseinterface.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QDesignerWidgetDataBaseInterface::metaObject()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK32QDesignerWidgetDataBaseInterface10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def count(self) -> int:
    """
    Calls Qt's 'int QDesignerWidgetDataBaseInterface::count() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerwidgetdatabaseinterface.html#count
    """
    #  int QDesignerWidgetDataBaseInterface::count() const
    ritual = 'ritual_ZNK32QDesignerWidgetDataBaseInterface5countEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK32QDesignerWidgetDataBaseInterface5countEv'
    return self.uglySide.call(ritual)

  @overload(int)
  def item(
      self,
      index: int,
  ) -> Optional[QDesignerWidgetDataBaseItemInterface]:
    """
    Calls Qt's 'QDesignerWidgetDataBaseItemInterface
    *QDesignerWidgetDataBaseInterface::item(int index) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerwidgetdatabaseinterface.html#item

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    Optional[QDesignerWidgetDataBaseItemInterface]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QDesignerWidgetDataBaseItemInterface
    #      *QDesignerWidgetDataBaseInterface::item(int index) const
    ritual = 'ritual_ZNK32QDesignerWidgetDataBaseInterface4itemEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK32QDesignerWidgetDataBaseInterface4itemEi'
    address = self.uglySide.call(ritual, index)
    from . import QDesignerWidgetDataBaseItemInterface
    return QDesignerWidgetDataBaseItemInterface._cuteAt(address)

  @overload(QDesignerWidgetDataBaseItemInterface)
  @overload(NoneType)
  def indexOf(
      self,
      item: Optional[QDesignerWidgetDataBaseItemInterface],
  ) -> int:
    """
    Calls Qt's 'int QDesignerWidgetDataBaseInterface::indexOf(
    QDesignerWidgetDataBaseItemInterface *item) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerwidgetdatabaseinterface.html#indexOf

    Parameters
    ----------

    item : Optional[QDesignerWidgetDataBaseItemInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  int QDesignerWidgetDataBaseInterface::indexOf(
    #      QDesignerWidgetDataBaseItemInterface *item) const
    ritual = (
        'ritual_ZNK32QDesignerWidgetDataBaseInterface7indexOfEP36QDesignerW'
        'idgetDataBaseItemInterface')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK32QDesignerWidgetDataBaseInterface7indexOfEP36QDes'
          'ignerWidgetDataBaseItemInterface')
    return self.uglySide.call(ritual, self._addressOf(item))

  @overload(QObject)
  @overload(NoneType)
  @overload(QObject, bool)
  @overload(NoneType, bool)
  def indexOfObject(
      self,
      object: Optional[QObject],
      resolveName: bool = True,
  ) -> int:
    """
    Calls Qt's 'int QDesignerWidgetDataBaseInterface::indexOfObject(QObject
    *object, bool resolveName) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerwidgetdatabaseinterface.html

    Parameters
    ----------

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    resolveName : bool
      Passed on as it is. May be left out, as in Qt: it is then True.
    """
    #  int QDesignerWidgetDataBaseInterface::indexOfObject(QObject *object,
    #      bool resolveName) const
    ritual = (
        'ritual_ZNK32QDesignerWidgetDataBaseInterface13indexOfObjectEP7QObj'
        'ectb')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK32QDesignerWidgetDataBaseInterface13indexOfObjectE'
          'P7QObjectb')
    return self.uglySide.call(
        ritual, self._addressOf(object, 'QObject'), resolveName,
    )

  @overload(str)
  @overload(str, bool)
  def indexOfClassName(
      self,
      className: str,
      resolveName: bool = True,
  ) -> int:
    """
    Calls Qt's 'int QDesignerWidgetDataBaseInterface::indexOfClassName(const
    QString &className, bool resolveName) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerwidgetdatabaseinterface.html

    Parameters
    ----------

    className : str
      Passed on as it is: a QString is made of it for the call.

    resolveName : bool
      Passed on as it is. May be left out, as in Qt: it is then True.
    """
    #  int QDesignerWidgetDataBaseInterface::indexOfClassName(const QString
    #      &className, bool resolveName) const
    ritual = (
        'ritual_ZNK32QDesignerWidgetDataBaseInterface16indexOfClassNameERK7'
        'QStringb')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK32QDesignerWidgetDataBaseInterface16indexOfClassNa'
          'meERK7QStringb')
    return self.uglySide.call(ritual, className, resolveName)

  def core(self) -> Optional[QDesignerFormEditorInterface]:
    """
    Calls Qt's 'QDesignerFormEditorInterface
    *QDesignerWidgetDataBaseInterface::core() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerwidgetdatabaseinterface.html#core

    Returns
    -------

    Optional[QDesignerFormEditorInterface]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QDesignerFormEditorInterface *QDesignerWidgetDataBaseInterface::core()
    #      const
    ritual = 'ritual_ZNK32QDesignerWidgetDataBaseInterface4coreEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK32QDesignerWidgetDataBaseInterface4coreEv'
    address = self.uglySide.call(ritual)
    from . import QDesignerFormEditorInterface
    return QDesignerFormEditorInterface._cuteAt(address)

  @overload(QObject)
  @overload(NoneType)
  @overload(QObject, bool)
  @overload(NoneType, bool)
  def isContainer(
      self,
      object: Optional[QObject],
      resolveName: bool = True,
  ) -> bool:
    """
    Calls Qt's 'bool QDesignerWidgetDataBaseInterface::isContainer(QObject
    *object, bool resolveName) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerwidgetdatabaseinterface.html#isContainer

    Parameters
    ----------

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    resolveName : bool
      Passed on as it is. May be left out, as in Qt: it is then True.
    """
    #  bool QDesignerWidgetDataBaseInterface::isContainer(QObject *object,
    #      bool resolveName) const
    return self.uglySide.call(
        'ritual_ZNK32QDesignerWidgetDataBaseInterface11isContainerEP7QObjec'
        'tb',
        self._addressOf(object, 'QObject'), resolveName,
    )

  @overload(QObject)
  @overload(NoneType)
  @overload(QObject, bool)
  @overload(NoneType, bool)
  def isCustom(
      self,
      object: Optional[QObject],
      resolveName: bool = True,
  ) -> bool:
    """
    Calls Qt's 'bool QDesignerWidgetDataBaseInterface::isCustom(QObject
    *object, bool resolveName) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerwidgetdatabaseinterface.html#isCustom

    Parameters
    ----------

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    resolveName : bool
      Passed on as it is. May be left out, as in Qt: it is then True.
    """
    #  bool QDesignerWidgetDataBaseInterface::isCustom(QObject *object, bool
    #      resolveName) const
    return self.uglySide.call(
        'ritual_ZNK32QDesignerWidgetDataBaseInterface8isCustomEP7QObjectb',
        self._addressOf(object, 'QObject'), resolveName,
    )

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
  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's
    'QDesignerWidgetDataBaseInterface::QDesignerWidgetDataBaseInterface(
    QObject *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerwidgetdatabaseinterface.html

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QDesignerWidgetDataBaseInterface::
    #      QDesignerWidgetDataBaseInterface(QObject *parent)
    self._noteCreation(
        QDesignerWidgetDataBaseInterface, lambda: Rituals.call(
            'ritual_ZN32QDesignerWidgetDataBaseInterfaceC1EP7QObject',
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

  @overload(int, QDesignerWidgetDataBaseItemInterface)
  @overload(int, NoneType)
  def insert(
      self,
      index: int,
      item: Optional[QDesignerWidgetDataBaseItemInterface],
  ) -> None:
    """
    Calls Qt's 'void QDesignerWidgetDataBaseInterface::insert(int index,
    QDesignerWidgetDataBaseItemInterface *item)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerwidgetdatabaseinterface.html#insert

    Parameters
    ----------

    index : int
      Passed on as it is.

    item : Optional[QDesignerWidgetDataBaseItemInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QDesignerWidgetDataBaseInterface::insert(int index,
    #      QDesignerWidgetDataBaseItemInterface *item)
    ritual = (
        'ritual_ZN32QDesignerWidgetDataBaseInterface6insertEiP36QDesignerWi'
        'dgetDataBaseItemInterface')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN32QDesignerWidgetDataBaseInterface6insertEiP36QDesi'
          'gnerWidgetDataBaseItemInterface')
    self.uglySide.call(ritual, index, self._addressOf(item))

  @overload(QDesignerWidgetDataBaseItemInterface)
  @overload(NoneType)
  def append(
      self,
      item: Optional[QDesignerWidgetDataBaseItemInterface],
  ) -> None:
    """
    Calls Qt's 'void QDesignerWidgetDataBaseInterface::append(
    QDesignerWidgetDataBaseItemInterface *item)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerwidgetdatabaseinterface.html#append

    Parameters
    ----------

    item : Optional[QDesignerWidgetDataBaseItemInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QDesignerWidgetDataBaseInterface::append(
    #      QDesignerWidgetDataBaseItemInterface *item)
    ritual = (
        'ritual_ZN32QDesignerWidgetDataBaseInterface6appendEP36QDesignerWid'
        'getDataBaseItemInterface')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN32QDesignerWidgetDataBaseInterface6appendEP36QDesig'
          'nerWidgetDataBaseItemInterface')
    self.uglySide.call(ritual, self._addressOf(item))

  def changed(self) -> None:
    """
    Calls Qt's 'void QDesignerWidgetDataBaseInterface::changed()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerwidgetdatabaseinterface.html#changed
    """
    #  void QDesignerWidgetDataBaseInterface::changed()
    self.uglySide.call(
        'ritual_ZN32QDesignerWidgetDataBaseInterface7changedEv',
    )
