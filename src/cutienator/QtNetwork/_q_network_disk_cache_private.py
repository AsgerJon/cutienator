"""
QNetworkDiskCachePrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtNetwork/6.12.0/QtNetwork/private/qnetworkdiskcache_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QNetworkDiskCachePrivate to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from . import QAbstractNetworkCachePrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QUrl
  from . import QCacheItem, QNetworkDiskCache
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QCacheItem = WAIT['QCacheItem']
  QUrl = WAIT['QUrl']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QNetworkDiskCachePrivate(QAbstractNetworkCachePrivate):
  """
  The cute side of Qt's QNetworkDiskCachePrivate: a plain Python object
  standing in front of one C++ QNetworkDiskCachePrivate.

  It is built on the cute 'QAbstractNetworkCachePrivate', as Qt's
  QNetworkDiskCachePrivate is built on Qt's QAbstractNetworkCachePrivate, and
  has everything that class has.

  What exists
  -----------

  Every function of Qt's QNetworkDiskCachePrivate that has a ritual and that
  Python can call so far, 5 names in all: 'uniqueFileName', 'cacheFileName',
  'storeItem', 'prepareLayout', 'q_func'. It can be made from Python, in 1
  way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QNetworkDiskCache *QNetworkDiskCachePrivate::q_func() const':
    takes in Python what 'QNetworkDiskCache
    *QNetworkDiskCachePrivate::q_func()' takes.

  What has no ritual
  ------------------

  2 of the 9 functions Qt declares: 1 cannot be called and cannot be called
  through the meta-object and cannot be copied; 1 Qt's library has no name
  for it, and its code in Qt's source does not compile apart from its file.

  What to expect
  --------------

  - The C++ QNetworkDiskCachePrivate is created at the first use, not by
    'QNetworkDiskCachePrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QNetworkDiskCachePrivate.
  - Each name of Qt's QNetworkDiskCachePrivate that has no cute function yet,
    'crc32', 'removeFile', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QUrl)
  def uniqueFileName(url: QUrl) -> str:
    """
    Calls Qt's 'QString QNetworkDiskCachePrivate::uniqueFileName(const QUrl
    &url)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkdiskcacheprivate.html#uniqueFileName

    Parameters
    ----------

    url : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QNetworkDiskCachePrivate::uniqueFileName(const QUrl &url)
    return Rituals.call(
        'ritual_ZN24QNetworkDiskCachePrivate14uniqueFileNameERK4QUrl',
        CuteMixin._valueOf(url),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QNetworkDiskCachePrivate'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QUrl)
  def cacheFileName(self, url: QUrl) -> str:
    """
    Calls Qt's 'QString QNetworkDiskCachePrivate::cacheFileName(const QUrl
    &url) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkdiskcacheprivate.html#cacheFileName

    Parameters
    ----------

    url : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QNetworkDiskCachePrivate::cacheFileName(const QUrl &url) const
    return self.uglySide.call(
        'ritual_ZNK24QNetworkDiskCachePrivate13cacheFileNameERK4QUrl',
        self._valueOf(url),
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
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'QNetworkDiskCachePrivate::QNetworkDiskCachePrivate()', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkdiskcacheprivate.html
    """
    #  QNetworkDiskCachePrivate::QNetworkDiskCachePrivate()
    self._noteCreation(QNetworkDiskCachePrivate, lambda: Rituals.call(
        'ritual_ZN24QNetworkDiskCachePrivateC1Ev',
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

  @overload(QCacheItem)
  @overload(NoneType)
  def storeItem(self, item: Optional[QCacheItem]) -> None:
    """
    Calls Qt's 'void QNetworkDiskCachePrivate::storeItem(QCacheItem *item)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkdiskcacheprivate.html#storeItem

    Parameters
    ----------

    item : Optional[QCacheItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QNetworkDiskCachePrivate::storeItem(QCacheItem *item)
    self.uglySide.call(
        'ritual_ZN24QNetworkDiskCachePrivate9storeItemEP10QCacheItem',
        self._addressOf(item),
    )

  def prepareLayout(self) -> None:
    """
    Calls Qt's 'void QNetworkDiskCachePrivate::prepareLayout()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkdiskcacheprivate.html#prepareLayout
    """
    #  void QNetworkDiskCachePrivate::prepareLayout()
    self.uglySide.call(
        'ritual_ZN24QNetworkDiskCachePrivate13prepareLayoutEv',
    )

  def q_func(self) -> Optional[QNetworkDiskCache]:
    """
    Calls Qt's 'QNetworkDiskCache *QNetworkDiskCachePrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkdiskcacheprivate.html#q_func

    Returns
    -------

    Optional[QNetworkDiskCache]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QNetworkDiskCache *QNetworkDiskCachePrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN24QNetworkDiskCachePrivate6q_funcEv',
    )
    from . import QNetworkDiskCache
    return QNetworkDiskCache._cuteAt(address)

  @staticmethod
  def crc32(*__, **_) -> Never:
    """
    Qt's 'quint32 QNetworkDiskCachePrivate::crc32(const char *data, uint
    len)': cannot be called and cannot be called through the meta-object and
    cannot be copied: no header file has its code, Qt's source does not mark
    it or its class for use from outside Qt or writes it 'inline' or nowhere,
    and it is no signal, slot or invokable function giving back nothing, of a
    class built on QObject, and Qt's source has no code for it that could be
    told from the rest.
    """
    raise NotImplementedError(
        "'QNetworkDiskCachePrivate.crc32' has no cute function yet. Qt's "
        "'quint32 QNetworkDiskCachePrivate::crc32(const char *data, uint "
        "len)': cannot be called and cannot be called through the "
        "meta-object and cannot be copied: no header file has its code, "
        "Qt's source does not mark it or its class for use from outside Qt "
        "or writes it 'inline' or nowhere, and it is no signal, slot or "
        "invokable function giving back nothing, of a class built on "
        "QObject, and Qt's source has no code for it that could be told "
        "from the rest.")

  @staticmethod
  def removeFile(*__, **_) -> Never:
    """
    Qt's 'bool QNetworkDiskCachePrivate::removeFile(const QString &file)':
    Qt's library has no name for it, and its code in Qt's source does not
    compile apart from its file: use of undeclared identifier
    'CACHE_POSTFIX'.
    """
    raise NotImplementedError(
        "'QNetworkDiskCachePrivate.removeFile' has no cute function yet. "
        "Qt's 'bool QNetworkDiskCachePrivate::removeFile(const QString "
        "&file)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: use of undeclared "
        "identifier 'CACHE_POSTFIX'.")
