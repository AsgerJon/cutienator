"""
QDesignerMetaDataBaseInterface binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDesigner/abstractmetadatabase.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin
from ..occult import Rituals
from ..QtCore import QList, QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
  from . import QDesignerFormEditorInterface
  from . import QDesignerMetaDataBaseItemInterface

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QDesignerMetaDataBaseInterface(QObject):
  """
  The cute side of Qt's QDesignerMetaDataBaseInterface: a plain Python object
  standing in front of one C++ QDesignerMetaDataBaseInterface.

  It is built on the cute 'QObject', as Qt's QDesignerMetaDataBaseInterface
  is built on Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QDesignerMetaDataBaseInterface that has a ritual and
  that Python can call so far, 8 names in all: 'metaObject', 'tr', 'item',
  'add', 'remove', 'objects', 'core', 'changed'. None can be made from
  Python: one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QDesignerMetaDataBaseInterface::qt_metacast(const char *a0)':
    one of Qt's own inner workings.
  - Qt's 'int QDesignerMetaDataBaseInterface::qt_metacall(QMetaObject::Call
    a0, int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QDesignerMetaDataBaseInterface::~QDesignerMetaDataBaseInterface()':
    the destructor: Python never removes a C++
    QDesignerMetaDataBaseInterface.

  What has no ritual
  ------------------

  3 of the 14 functions Qt declares: 2 not a gap; 1 the class is abstract, so
  C++ cannot make one, and the C++ class of ours does not fill in every
  function it leaves open.

  What to expect
  --------------

  - The C++ QDesignerMetaDataBaseInterface is created at the first use, not
    by 'QDesignerMetaDataBaseInterface(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QDesignerMetaDataBaseInterface.
  - Qt tells when it has removed the C++ QDesignerMetaDataBaseInterface.
    Every call on the cute object, and every use of it as an argument, then
    raises 'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QDesignerMetaDataBaseInterface that has no cute
    function yet, '__init__', holds a function that raises
    'NotImplementedError', and its docstring says why.
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
    Calls Qt's 'QString QDesignerMetaDataBaseInterface::tr(const char *s,
    const char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignermetadatabaseinterface.html#tr

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
    #  QString QDesignerMetaDataBaseInterface::tr(const char *s, const char
    #      *c, int n)
    return Rituals.call(
        'ritual_ZN30QDesignerMetaDataBaseInterface2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QDesignerMetaDataBaseInterface'

  #  A C++ QDesignerMetaDataBaseInterface Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QDesignerMetaDataBaseInterface'

  #  The functions Qt calls itself that QDesignerMetaDataBaseInterface is the
  #  first to declare and that cannot be handed to Python yet, each as Qt
  #  declares it. A class of a program that writes one of them anew is
  #  refused, since Qt would never call what it wrote; see
  #  'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'objects': (
          'QList<QObject *> QDesignerMetaDataBaseInterface::objects() const',
      ),
  }

  #  The functions Qt calls itself that QDesignerMetaDataBaseInterface is the
  #  first to declare. A class of a program built on it can write one anew,
  #  and Qt then calls that. For each name: the key C++ knows the function
  #  by, what it gives, and what it takes.
  __virtual_functions__ = {
      'item': (
          ('_ZNK30QDesignerMetaDataBaseInterface4itemEP7QObject',
           ('address', 'address',
            'QtDesigner:QDesignerMetaDataBaseItemInterface'),
           (
               ('address', 'address', 'QtCore:QObject'),
           )),
      ),
      'add': (
          ('_ZN30QDesignerMetaDataBaseInterface3addEP7QObject',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtCore:QObject'),
           )),
      ),
      'remove': (
          ('_ZN30QDesignerMetaDataBaseInterface6removeEP7QObject',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtCore:QObject'),
           )),
      ),
      'core': (
          ('_ZNK30QDesignerMetaDataBaseInterface4coreEv',
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
    *QDesignerMetaDataBaseInterface::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignermetadatabaseinterface.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QDesignerMetaDataBaseInterface::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK30QDesignerMetaDataBaseInterface10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  @overload(QObject)
  @overload(NoneType)
  def item(
      self,
      object: Optional[QObject],
  ) -> Optional[QDesignerMetaDataBaseItemInterface]:
    """
    Calls Qt's 'QDesignerMetaDataBaseItemInterface
    *QDesignerMetaDataBaseInterface::item(QObject *object) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignermetadatabaseinterface.html#item

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
    #      *QDesignerMetaDataBaseInterface::item(QObject *object) const
    address = self.uglySide.call(
        'ritual_ZNK30QDesignerMetaDataBaseInterface4itemEP7QObject',
        self._addressOf(object, 'QObject'),
    )
    from . import QDesignerMetaDataBaseItemInterface
    return QDesignerMetaDataBaseItemInterface._cuteAt(address)

  def objects(self) -> QList[QObject]:
    """
    Calls Qt's 'QList<QObject *> QDesignerMetaDataBaseInterface::objects()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignermetadatabaseinterface.html#objects

    Returns
    -------

    QList[QObject]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QObject *> QDesignerMetaDataBaseInterface::objects() const
    address = self.uglySide.call(
        'ritual_ZNK30QDesignerMetaDataBaseInterface7objectsEv',
    )
    return QList[QObject]._cuteOwning(address)

  def core(self) -> Optional[QDesignerFormEditorInterface]:
    """
    Calls Qt's 'QDesignerFormEditorInterface
    *QDesignerMetaDataBaseInterface::core() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignermetadatabaseinterface.html#core

    Returns
    -------

    Optional[QDesignerFormEditorInterface]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QDesignerFormEditorInterface *QDesignerMetaDataBaseInterface::core()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK30QDesignerMetaDataBaseInterface4coreEv',
    )
    from . import QDesignerFormEditorInterface
    return QDesignerFormEditorInterface._cuteAt(address)

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
    Qt's
    'QDesignerMetaDataBaseInterface::QDesignerMetaDataBaseInterface(QObject
    *parent)': the class is abstract, so C++ cannot make one, and the C++
    class of ours does not fill in every function it leaves open.
    """
    raise NotImplementedError(
        "'QDesignerMetaDataBaseInterface.__init__' has no cute function "
        "yet. Qt's "
        "'QDesignerMetaDataBaseInterface::QDesignerMetaDataBaseInterface(QOb"
        "ject *parent)': the class is abstract, so C++ cannot make one, and "
        "the C++ class of ours does not fill in every function it leaves "
        "open.")

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
    Calls Qt's 'void QDesignerMetaDataBaseInterface::add(QObject *object)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignermetadatabaseinterface.html#add

    Parameters
    ----------

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QDesignerMetaDataBaseInterface::add(QObject *object)
    self.uglySide.call(
        'ritual_ZN30QDesignerMetaDataBaseInterface3addEP7QObject',
        self._addressOf(object, 'QObject'),
    )

  @overload(QObject)
  @overload(NoneType)
  def remove(self, object: Optional[QObject]) -> None:
    """
    Calls Qt's 'void QDesignerMetaDataBaseInterface::remove(QObject
    *object)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignermetadatabaseinterface.html#remove

    Parameters
    ----------

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QDesignerMetaDataBaseInterface::remove(QObject *object)
    self.uglySide.call(
        'ritual_ZN30QDesignerMetaDataBaseInterface6removeEP7QObject',
        self._addressOf(object, 'QObject'),
    )

  def changed(self) -> None:
    """
    Calls Qt's 'void QDesignerMetaDataBaseInterface::changed()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignermetadatabaseinterface.html#changed
    """
    #  void QDesignerMetaDataBaseInterface::changed()
    self.uglySide.call('ritual_ZN30QDesignerMetaDataBaseInterface7changedEv')
