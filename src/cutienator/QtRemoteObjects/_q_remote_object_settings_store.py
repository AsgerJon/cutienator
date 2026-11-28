"""
QRemoteObjectSettingsStore binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtRemoteObjects/qremoteobjectsettingsstore.h, Qt 6.12.0. Changes made here
#  are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QList, QObject
from . import QRemoteObjectAbstractPersistedStore

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QByteArray, QMetaObject, QVariant
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QRemoteObjectSettingsStore(QRemoteObjectAbstractPersistedStore):
  """
  The cute side of Qt's QRemoteObjectSettingsStore: a plain Python object
  standing in front of one C++ QRemoteObjectSettingsStore.

  It is built on the cute 'QRemoteObjectAbstractPersistedStore', as Qt's
  QRemoteObjectSettingsStore is built on Qt's
  QRemoteObjectAbstractPersistedStore, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QRemoteObjectSettingsStore that has a ritual and
  that Python can call so far, 4 names in all: 'metaObject', 'tr',
  'saveProperties', 'restoreProperties'. It can be made from Python, in 1
  way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QRemoteObjectSettingsStore::qt_metacast(const char *a0)': one
    of Qt's own inner workings.
  - Qt's 'int QRemoteObjectSettingsStore::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QRemoteObjectSettingsStore::~QRemoteObjectSettingsStore()': the
    destructor: Python never removes a C++ QRemoteObjectSettingsStore.
  - Qt's 'QRemoteObjectSettingsStorePrivate
    *QRemoteObjectSettingsStore::d_func()': gives
    'QRemoteObjectSettingsStorePrivate', which has no cute class yet.
  - Qt's 'const QRemoteObjectSettingsStorePrivate
    *QRemoteObjectSettingsStore::d_func() const': gives
    'QRemoteObjectSettingsStorePrivate', which has no cute class yet.

  What has no ritual
  ------------------

  2 of the 12 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QRemoteObjectSettingsStore is created at the first use, not by
    'QRemoteObjectSettingsStore(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QRemoteObjectSettingsStore.
  - Qt tells when it has removed the C++ QRemoteObjectSettingsStore. Every
    call on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
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
    Calls Qt's 'QString QRemoteObjectSettingsStore::tr(const char *s, const
    char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qremoteobjectsettingsstore.html#tr

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
    #  QString QRemoteObjectSettingsStore::tr(const char *s, const char *c,
    #      int n)
    return Rituals.call(
        'ritual_ZN26QRemoteObjectSettingsStore2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QRemoteObjectSettingsStore'

  #  A C++ QRemoteObjectSettingsStore Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QRemoteObjectSettingsStore'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QRemoteObjectSettingsStore::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qremoteobjectsettingsstore.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QRemoteObjectSettingsStore::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK26QRemoteObjectSettingsStore10metaObjectEv',
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

  @overload()
  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's
    'QRemoteObjectSettingsStore::QRemoteObjectSettingsStore(QObject
    *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qremoteobjectsettingsstore.html

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QRemoteObjectSettingsStore::QRemoteObjectSettingsStore(QObject
    #      *parent)
    self._noteCreation(QRemoteObjectSettingsStore, lambda: Rituals.call(
        'ritual_ZN26QRemoteObjectSettingsStoreC1EP7QObject',
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

  @overload(str, QByteArray, QList[QVariant])
  def saveProperties(
      self,
      repName: str,
      repSig: QByteArray,
      values: QList[QVariant],
  ) -> None:
    """
    Calls Qt's 'void QRemoteObjectSettingsStore::saveProperties(const QString
    &repName, const QByteArray &repSig, const QVariantList &values)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qremoteobjectsettingsstore.html#saveProperties

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
    #  void QRemoteObjectSettingsStore::saveProperties(const QString
    #      &repName, const QByteArray &repSig, const QVariantList &values)
    self.uglySide.call(
        'ritual_ZN26QRemoteObjectSettingsStore14savePropertiesERK7QStringRK'
        '10QByteArrayRK5QListI8QVariantE',
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
    QRemoteObjectSettingsStore::restoreProperties(const QString &repName,
    const QByteArray &repSig)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qremoteobjectsettingsstore.html#restoreProperties

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
    #  QVariantList QRemoteObjectSettingsStore::restoreProperties(const
    #      QString &repName, const QByteArray &repSig)
    address = self.uglySide.call(
        'ritual_ZN26QRemoteObjectSettingsStore17restorePropertiesERK7QStrin'
        'gRK10QByteArray',
        repName, self._valueOf(repSig),
    )
    from ..QtCore import QVariant
    return QList[QVariant]._cuteOwning(address)
