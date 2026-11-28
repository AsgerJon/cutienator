"""
QDesignerAbstractPropertySheetFactory binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDesigner/6.12.0/QtDesigner/private/qdesigner_propertysheet_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QDesignerAbstractPropertySheetFactory to be private: it declares
#  the class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject
from . import QExtensionFactory

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from . import QExtensionManager
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QExtensionManager = WAIT['QExtensionManager']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QDesignerAbstractPropertySheetFactory(QExtensionFactory):
  """
  The cute side of Qt's QDesignerAbstractPropertySheetFactory: a plain Python
  object standing in front of one C++ QDesignerAbstractPropertySheetFactory.

  It is built on the cute 'QExtensionFactory', as Qt's
  QDesignerAbstractPropertySheetFactory is built on Qt's QExtensionFactory,
  and has everything that class has.

  What exists
  -----------

  Every function of Qt's QDesignerAbstractPropertySheetFactory that has a
  ritual and that Python can call so far, 5 names in all: 'metaObject', 'tr',
  'extension', 'objectDestroyed', 'createPropertySheet'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QDesignerAbstractPropertySheetFactory::qt_metacast(const char
    *a0)': one of Qt's own inner workings.
  - Qt's 'int
    QDesignerAbstractPropertySheetFactory::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QDesignerAbstractPropertySheetFactory::
    ~QDesignerAbstractPropertySheetFactory()': the destructor: Python never
    removes a C++ QDesignerAbstractPropertySheetFactory.

  What has no ritual
  ------------------

  2 of the 11 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QDesignerAbstractPropertySheetFactory is created at the first
    use, not by 'QDesignerAbstractPropertySheetFactory(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QDesignerAbstractPropertySheetFactory.
  - Qt tells when it has removed the C++
    QDesignerAbstractPropertySheetFactory. Every call on the cute object, and
    every use of it as an argument, then raises 'RuntimeError', and nothing
    reaches C++.
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
    Calls Qt's 'QString QDesignerAbstractPropertySheetFactory::tr(const char
    *s, const char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerabstractpropertysheetfactory.html#tr

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
    #  QString QDesignerAbstractPropertySheetFactory::tr(const char *s, const
    #      char *c, int n)
    return Rituals.call(
        'ritual_ZN37QDesignerAbstractPropertySheetFactory2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QDesignerAbstractPropertySheetFactory'

  #  A C++ QDesignerAbstractPropertySheetFactory Python makes is of a C++
  #  class of ours, in which Python can take functions over. This ritual
  #  hands one over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QDesignerAbstractPropertySheetFactory'

  #  The functions Qt calls itself that QDesignerAbstractPropertySheetFactory
  #  is the first to declare. A class of a program built on it can write one
  #  anew, and Qt then calls that. For each name: the key C++ knows the
  #  function by, what it gives, and what it takes.
  __virtual_functions__ = {
      'createPropertySheet': (
          ('_ZNK37QDesignerAbstractPropertySheetFactory19createPropertyShee'
           'tEP7QObjectS1_',
           ('address', 'address', 'QtCore:QObject'),
           (
               ('address', 'address', 'QtCore:QObject'),
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
    *QDesignerAbstractPropertySheetFactory::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerabstractpropertysheetfactory.html

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QDesignerAbstractPropertySheetFactory::metaObject()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK37QDesignerAbstractPropertySheetFactory10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  @overload(QObject, str)
  @overload(NoneType, str)
  def extension(
      self,
      object: Optional[QObject],
      iid: str,
  ) -> Optional[QObject]:
    """
    Calls Qt's 'QObject
    *QDesignerAbstractPropertySheetFactory::extension(QObject *object, const
    QString &iid) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerabstractpropertysheetfactory.html

    Parameters
    ----------

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    iid : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    Optional[QObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QObject *QDesignerAbstractPropertySheetFactory::extension(QObject
    #      *object, const QString &iid) const
    ritual = (
        'ritual_ZNK37QDesignerAbstractPropertySheetFactory9extensionEP7QObj'
        'ectRK7QString')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK37QDesignerAbstractPropertySheetFactory9extensionE'
          'P7QObjectRK7QString')
    address = self.uglySide.call(
        ritual, self._addressOf(object, 'QObject'), iid,
    )
    return QObject._cuteAt(address)

  @overload(QObject, QObject)
  @overload(QObject, NoneType)
  @overload(NoneType, QObject)
  @overload(NoneType, NoneType)
  def createPropertySheet(
      self,
      qObject: Optional[QObject],
      parent: Optional[QObject],
  ) -> Optional[QObject]:
    """
    Calls Qt's 'QObject
    *QDesignerAbstractPropertySheetFactory::createPropertySheet(QObject
    *qObject, QObject *parent) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerabstractpropertysheetfactory.html

    Parameters
    ----------

    qObject : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QObject *QDesignerAbstractPropertySheetFactory::createPropertySheet(
    #      QObject *qObject, QObject *parent) const
    address = self.uglySide.call(
        'ritual_ZNK37QDesignerAbstractPropertySheetFactory19createPropertyS'
        'heetEP7QObjectS1_',
        self._addressOf(qObject, 'QObject'), self._addressOf(parent,
        'QObject'),
    )
    return QObject._cuteAt(address)

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
  @overload(QExtensionManager)
  @overload(NoneType)
  def __init__(self, parent: Optional[QExtensionManager] = None) -> None:
    """
    Notes what was given, for Qt's 'QDesignerAbstractPropertySheetFactory::
    QDesignerAbstractPropertySheetFactory(QExtensionManager *parent)', which
    is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerabstractpropertysheetfactory.html

    Parameters
    ----------

    parent : Optional[QExtensionManager]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QDesignerAbstractPropertySheetFactory::
    #      QDesignerAbstractPropertySheetFactory(QExtensionManager *parent)
    self._noteCreation(
        QDesignerAbstractPropertySheetFactory, lambda: Rituals.call(
            'ritual_ZN37QDesignerAbstractPropertySheetFactoryC1EP17QExtensi'
            'onManager',
            self._addressOf(parent),
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
  def objectDestroyed(self, object: Optional[QObject]) -> None:
    """
    Calls Qt's 'void
    QDesignerAbstractPropertySheetFactory::objectDestroyed(QObject *object)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerabstractpropertysheetfactory.html

    Parameters
    ----------

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QDesignerAbstractPropertySheetFactory::objectDestroyed(QObject
    #      *object)
    self.uglySide.call(
        'ritual_ZN37QDesignerAbstractPropertySheetFactory15objectDestroyedE'
        'P7QObject',
        self._addressOf(object, 'QObject'),
    )
