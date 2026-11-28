"""
QRemoteObjectAbstractPersistedStore binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtRemoteObjects/qremoteobjectnode.h, Qt 6.12.0. Changes made here are
#  lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QList, QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QByteArray, QMetaObject, QVariant
  from . import QRemoteObjectAbstractPersistedStorePrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QRemoteObjectAbstractPersistedStore(QObject):
  """
  The cute side of Qt's QRemoteObjectAbstractPersistedStore: a plain Python
  object standing in front of one C++ QRemoteObjectAbstractPersistedStore.

  It is built on the cute 'QObject', as Qt's
  QRemoteObjectAbstractPersistedStore is built on Qt's QObject, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QRemoteObjectAbstractPersistedStore that has a
  ritual and that Python can call so far, 5 names in all: 'metaObject', 'tr',
  'saveProperties', 'restoreProperties', 'd_func'. None can be made from
  Python: one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QRemoteObjectAbstractPersistedStore::qt_metacast(const char
    *a0)': one of Qt's own inner workings.
  - Qt's 'int
    QRemoteObjectAbstractPersistedStore::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QRemoteObjectAbstractPersistedStore::
    ~QRemoteObjectAbstractPersistedStore()': the destructor: Python never
    removes a C++ QRemoteObjectAbstractPersistedStore.
  - Qt's 'const QRemoteObjectAbstractPersistedStorePrivate
    *QRemoteObjectAbstractPersistedStore::d_func() const': takes in Python
    what 'QRemoteObjectAbstractPersistedStorePrivate
    *QRemoteObjectAbstractPersistedStore::d_func()' takes.

  What has no ritual
  ------------------

  4 of the 13 functions Qt declares: 2 not a gap; 2 the class is abstract, so
  C++ cannot make one, and the C++ class of ours does not fill in every
  function it leaves open.

  What to expect
  --------------

  - The C++ QRemoteObjectAbstractPersistedStore is created at the first use,
    not by 'QRemoteObjectAbstractPersistedStore(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QRemoteObjectAbstractPersistedStore.
  - Qt tells when it has removed the C++ QRemoteObjectAbstractPersistedStore.
    Every call on the cute object, and every use of it as an argument, then
    raises 'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QRemoteObjectAbstractPersistedStore that has no cute
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
    Calls Qt's 'QString QRemoteObjectAbstractPersistedStore::tr(const char
    *s, const char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qremoteobjectabstractpersistedstore.html#tr

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
    #  QString QRemoteObjectAbstractPersistedStore::tr(const char *s, const
    #      char *c, int n)
    return Rituals.call(
        'ritual_ZN35QRemoteObjectAbstractPersistedStore2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QRemoteObjectAbstractPersistedStore'

  #  A C++ QRemoteObjectAbstractPersistedStore Python makes is of a C++ class
  #  of ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QRemoteObjectAbstractPersistedStore'

  #  The functions Qt calls itself that QRemoteObjectAbstractPersistedStore
  #  is the first to declare and that cannot be handed to Python yet, each as
  #  Qt declares it. A class of a program that writes one of them anew is
  #  refused, since Qt would never call what it wrote; see
  #  'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'saveProperties': (
          'void QRemoteObjectAbstractPersistedStore::saveProperties(const '
          'QString &, const QByteArray &, const QVariantList &)',
      ),
      'restoreProperties': (
          'QVariantList '
          'QRemoteObjectAbstractPersistedStore::restoreProperties(const '
          'QString &, const QByteArray &)',
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
    *QRemoteObjectAbstractPersistedStore::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qremoteobjectabstractpersistedstore.html

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QRemoteObjectAbstractPersistedStore::metaObject()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK35QRemoteObjectAbstractPersistedStore10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

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
    - Qt's 'QRemoteObjectAbstractPersistedStore::
      QRemoteObjectAbstractPersistedStore(QObject *parent)': the class is
      abstract, so C++ cannot make one, and the C++ class of ours does not
      fill in every function it leaves open.
    - Qt's 'QRemoteObjectAbstractPersistedStore::
      QRemoteObjectAbstractPersistedStore(
      QRemoteObjectAbstractPersistedStorePrivate &a0, QObject *parent)': the
      class is abstract, so C++ cannot make one, and the C++ class of ours
      does not fill in every function it leaves open.
    """
    raise NotImplementedError(
        "'QRemoteObjectAbstractPersistedStore.__init__' has no cute "
        "function yet. Qt's "
        "'QRemoteObjectAbstractPersistedStore::QRemoteObjectAbstractPersiste"
        "dStore(QObject *parent)': the class is abstract, so C++ cannot "
        "make one, and the C++ class of ours does not fill in every "
        "function it leaves open. Qt's "
        "'QRemoteObjectAbstractPersistedStore::QRemoteObjectAbstractPersiste"
        "dStore(QRemoteObjectAbstractPersistedStorePrivate &a0, QObject "
        "*parent)': the class is abstract, so C++ cannot make one, and the "
        "C++ class of ours does not fill in every function it leaves open.")

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

  @overload(str, QByteArray, QList[QVariant])
  def saveProperties(
      self,
      repName: str,
      repSig: QByteArray,
      values: QList[QVariant],
  ) -> None:
    """
    Calls Qt's 'void
    QRemoteObjectAbstractPersistedStore::saveProperties(const QString
    &repName, const QByteArray &repSig, const QVariantList &values)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qremoteobjectabstractpersistedstore.html

    Parameters
    ----------

    repName : str
      Passed on as it is: a QString is made of it for the call.

    repSig : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    values : QList[QVariant]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QRemoteObjectAbstractPersistedStore::saveProperties(const QString
    #      &repName, const QByteArray &repSig, const QVariantList &values)
    self.uglySide.call(
        'ritual_ZN35QRemoteObjectAbstractPersistedStore14savePropertiesERK7'
        'QStringRK10QByteArrayRK5QListI8QVariantE',
        repName, self._valueOf(repSig), self._valueOf(values),
    )

  @overload(str, QByteArray)
  def restoreProperties(
      self,
      repName: str,
      repSig: QByteArray,
  ) -> QList[QVariant]:
    """
    Calls Qt's 'QVariantList
    QRemoteObjectAbstractPersistedStore::restoreProperties(const QString
    &repName, const QByteArray &repSig)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qremoteobjectabstractpersistedstore.html

    Parameters
    ----------

    repName : str
      Passed on as it is: a QString is made of it for the call.

    repSig : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    Returns
    -------

    QList[QVariant]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QVariantList
    #      QRemoteObjectAbstractPersistedStore::restoreProperties(const
    #      QString &repName, const QByteArray &repSig)
    address = self.uglySide.call(
        'ritual_ZN35QRemoteObjectAbstractPersistedStore17restorePropertiesE'
        'RK7QStringRK10QByteArray',
        repName, self._valueOf(repSig),
    )
    from ..QtCore import QVariant
    return QList[QVariant]._cuteOwning(address)

  def d_func(self) -> Optional[QRemoteObjectAbstractPersistedStorePrivate]:
    """
    Calls Qt's 'QRemoteObjectAbstractPersistedStorePrivate
    *QRemoteObjectAbstractPersistedStore::d_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qremoteobjectabstractpersistedstore.html#d_func

    Returns
    -------

    Optional[QRemoteObjectAbstractPersistedStorePrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QRemoteObjectAbstractPersistedStorePrivate
    #      *QRemoteObjectAbstractPersistedStore::d_func()
    address = self.uglySide.call(
        'ritual_ZN35QRemoteObjectAbstractPersistedStore6d_funcEv',
    )
    from . import QRemoteObjectAbstractPersistedStorePrivate
    return QRemoteObjectAbstractPersistedStorePrivate._cuteAt(address)
