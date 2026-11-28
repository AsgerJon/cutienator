"""
QQuickWebEngineScriptCollection binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWebEngineQuick/6.12.0/QtWebEngineQuick/private/qquickwebenginescriptcollection_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuickWebEngineScriptCollection to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QList, QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from ..QtWebEngineCore import QWebEngineScript, QWebEngineScriptCollection
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QWebEngineScript = WAIT['QWebEngineScript']
  QWebEngineScriptCollection = WAIT['QWebEngineScriptCollection']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickWebEngineScriptCollection(QObject):
  """
  The cute side of Qt's QQuickWebEngineScriptCollection: a plain Python
  object standing in front of one C++ QQuickWebEngineScriptCollection.

  It is built on the cute 'QObject', as Qt's QQuickWebEngineScriptCollection
  is built on Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickWebEngineScriptCollection that has a ritual
  and that Python can call so far, 10 names in all: 'metaObject', 'tr',
  'contains', 'find', 'insert', 'remove', 'clear', 'collection',
  'setCollection', 'collectionChanged'. It can be made from Python, in 1 way;
  see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickWebEngineScriptCollection::qt_metacast(const char
    *a0)': one of Qt's own inner workings.
  - Qt's 'int QQuickWebEngineScriptCollection::qt_metacall(QMetaObject::Call
    a0, int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'void QQuickWebEngineScriptCollection::qt_qmlMarker_anonymous()':
    one of Qt's own inner workings.
  - Qt's
    'QQuickWebEngineScriptCollection::~QQuickWebEngineScriptCollection()':
    the destructor: Python never removes a C++
    QQuickWebEngineScriptCollection.

  What has no ritual
  ------------------

  4 of the 20 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QQuickWebEngineScriptCollection is created at the first use, not
    by 'QQuickWebEngineScriptCollection(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickWebEngineScriptCollection.
  - Qt tells when it has removed the C++ QQuickWebEngineScriptCollection.
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
    Calls Qt's 'QString QQuickWebEngineScriptCollection::tr(const char *s,
    const char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebenginescriptcollection.html#tr

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
    #  QString QQuickWebEngineScriptCollection::tr(const char *s, const char
    #      *c, int n)
    return Rituals.call(
        'ritual_ZN31QQuickWebEngineScriptCollection2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickWebEngineScriptCollection'

  #  A C++ QQuickWebEngineScriptCollection Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickWebEngineScriptCollection'

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
    *QQuickWebEngineScriptCollection::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebenginescriptcollection.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickWebEngineScriptCollection::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK31QQuickWebEngineScriptCollection10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  @overload(QWebEngineScript)
  def contains(self, value: QWebEngineScript) -> bool:
    """
    Calls Qt's 'bool QQuickWebEngineScriptCollection::contains(const
    QWebEngineScript &value) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebenginescriptcollection.html#contains

    Parameters
    ----------

    value : QWebEngineScript
      Passed on as a value: Qt reads the C++ QWebEngineScript, which stays
      Python's own.
    """
    #  bool QQuickWebEngineScriptCollection::contains(const QWebEngineScript
    #      &value) const
    return self.uglySide.call(
        'ritual_ZNK31QQuickWebEngineScriptCollection8containsERK16QWebEngin'
        'eScript',
        self._valueOf(value),
    )

  @overload(str)
  def find(self, name: str) -> QList[QWebEngineScript]:
    """
    Calls Qt's 'QList<QWebEngineScript>
    QQuickWebEngineScriptCollection::find(const QString &name) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebenginescriptcollection.html#find

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QList[QWebEngineScript]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QWebEngineScript> QQuickWebEngineScriptCollection::find(const
    #      QString &name) const
    address = self.uglySide.call(
        'ritual_ZNK31QQuickWebEngineScriptCollection4findERK7QString', name,
    )
    from ..QtWebEngineCore import QWebEngineScript
    return QList[QWebEngineScript]._cuteOwning(address)

  def collection(self) -> QList[QWebEngineScript]:
    """
    Calls Qt's 'QList<QWebEngineScript>
    QQuickWebEngineScriptCollection::collection() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebenginescriptcollection.html#collection

    Returns
    -------

    QList[QWebEngineScript]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QWebEngineScript> QQuickWebEngineScriptCollection::collection()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK31QQuickWebEngineScriptCollection10collectionEv',
    )
    from ..QtWebEngineCore import QWebEngineScript
    return QList[QWebEngineScript]._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QList[QWebEngineScript])
  def setCollection(self, scripts: QList[QWebEngineScript]) -> None:
    """
    Calls Qt's 'void QQuickWebEngineScriptCollection::setCollection(const
    QList<QWebEngineScript> &scripts)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebenginescriptcollection.html#setCollection

    Parameters
    ----------

    scripts : QList[QWebEngineScript]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QQuickWebEngineScriptCollection::setCollection(const
    #      QList<QWebEngineScript> &scripts)
    self.uglySide.call(
        'ritual_ZN31QQuickWebEngineScriptCollection13setCollectionERK5QList'
        'I16QWebEngineScriptE',
        self._valueOf(scripts),
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

  @overload(QWebEngineScriptCollection)
  @overload(NoneType)
  def __init__(self, d: Optional[QWebEngineScriptCollection]) -> None:
    """
    Notes what was given, for Qt's
    'QQuickWebEngineScriptCollection::QQuickWebEngineScriptCollection(
    QWebEngineScriptCollection *d)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebenginescriptcollection.html

    Parameters
    ----------

    d : Optional[QWebEngineScriptCollection]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QQuickWebEngineScriptCollection::QQuickWebEngineScriptCollection(
    #      QWebEngineScriptCollection *d)
    self._noteCreation(QQuickWebEngineScriptCollection, lambda: Rituals.call(
        'ritual_ZN31QQuickWebEngineScriptCollectionC1EP26QWebEngineScriptCo'
        'llection',
        self._addressOf(d),
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

  @overload(QWebEngineScript)
  def insert(self, a0: QWebEngineScript) -> None:
    """
    Calls Qt's 'void QQuickWebEngineScriptCollection::insert(const
    QWebEngineScript &a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebenginescriptcollection.html#insert

    Parameters
    ----------

    a0 : QWebEngineScript
      Passed on as a value: Qt reads the C++ QWebEngineScript, which stays
      Python's own.
    """
    #  void QQuickWebEngineScriptCollection::insert(const QWebEngineScript
    #      &a0)
    self.uglySide.call(
        'ritual_ZN31QQuickWebEngineScriptCollection6insertERK16QWebEngineSc'
        'ript',
        self._valueOf(a0),
    )

  @overload(QList[QWebEngineScript])
  def insert(self, list: QList[QWebEngineScript]) -> None:
    """
    Calls Qt's 'void QQuickWebEngineScriptCollection::insert(const
    QList<QWebEngineScript> &list)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebenginescriptcollection.html#insert

    Parameters
    ----------

    list : QList[QWebEngineScript]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QQuickWebEngineScriptCollection::insert(const
    #      QList<QWebEngineScript> &list)
    self.uglySide.call(
        'ritual_ZN31QQuickWebEngineScriptCollection6insertERK5QListI16QWebE'
        'ngineScriptE',
        self._valueOf(list),
    )

  @overload(QWebEngineScript)
  def remove(self, a0: QWebEngineScript) -> bool:
    """
    Calls Qt's 'bool QQuickWebEngineScriptCollection::remove(const
    QWebEngineScript &a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebenginescriptcollection.html#remove

    Parameters
    ----------

    a0 : QWebEngineScript
      Passed on as a value: Qt reads the C++ QWebEngineScript, which stays
      Python's own.
    """
    #  bool QQuickWebEngineScriptCollection::remove(const QWebEngineScript
    #      &a0)
    return self.uglySide.call(
        'ritual_ZN31QQuickWebEngineScriptCollection6removeERK16QWebEngineSc'
        'ript',
        self._valueOf(a0),
    )

  def clear(self) -> None:
    """
    Calls Qt's 'void QQuickWebEngineScriptCollection::clear()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebenginescriptcollection.html#clear
    """
    #  void QQuickWebEngineScriptCollection::clear()
    self.uglySide.call('ritual_ZN31QQuickWebEngineScriptCollection5clearEv')

  def collectionChanged(self) -> None:
    """
    Calls Qt's 'void QQuickWebEngineScriptCollection::collectionChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebenginescriptcollection.html
    """
    #  void QQuickWebEngineScriptCollection::collectionChanged()
    self.uglySide.call(
        'ritual_ZN31QQuickWebEngineScriptCollection17collectionChangedEv',
    )
