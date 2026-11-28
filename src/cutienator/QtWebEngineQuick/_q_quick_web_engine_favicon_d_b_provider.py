"""
QQuickWebEngineFaviconDBProvider binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWebEngineQuick/6.12.0/QtWebEngineQuick/private/qquickwebenginefaviconprovider_p_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuickWebEngineFaviconDBProvider to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from . import QQuickWebEngineFaviconProvider

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QUrl
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QUrl = WAIT['QUrl']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickWebEngineFaviconDBProvider(QQuickWebEngineFaviconProvider):
  """
  The cute side of Qt's QQuickWebEngineFaviconDBProvider: a plain Python
  object standing in front of one C++ QQuickWebEngineFaviconDBProvider.

  It is built on the cute 'QQuickWebEngineFaviconProvider', as Qt's
  QQuickWebEngineFaviconDBProvider is built on Qt's
  QQuickWebEngineFaviconProvider, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickWebEngineFaviconDBProvider that has a ritual
  and that Python can call so far, 5 names in all: 'metaObject', 'tr',
  'identifier', 'faviconProviderUrl', 'isIconUrl'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickWebEngineFaviconDBProvider::qt_metacast(const char
    *a0)': one of Qt's own inner workings.
  - Qt's 'int QQuickWebEngineFaviconDBProvider::qt_metacall(QMetaObject::Call
    a0, int a1, void **a2)': one of Qt's own inner workings.

  What has no ritual
  ------------------

  2 of the 10 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuickWebEngineFaviconDBProvider is created at the first use, not
    by 'QQuickWebEngineFaviconDBProvider(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickWebEngineFaviconDBProvider.
  - Qt tells when it has removed the C++ QQuickWebEngineFaviconDBProvider.
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
    Calls Qt's 'QString QQuickWebEngineFaviconDBProvider::tr(const char *s,
    const char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebenginefavicondbprovider.html#tr

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
    #  QString QQuickWebEngineFaviconDBProvider::tr(const char *s, const char
    #      *c, int n)
    return Rituals.call(
        'ritual_ZN32QQuickWebEngineFaviconDBProvider2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  def identifier() -> str:
    """
    Calls Qt's 'QString QQuickWebEngineFaviconDBProvider::identifier()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebenginefavicondbprovider.html#identifier

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuickWebEngineFaviconDBProvider::identifier()
    return Rituals.call(
        'ritual_ZN32QQuickWebEngineFaviconDBProvider10identifierEv',
    )

  @staticmethod
  @overload(QUrl)
  def faviconProviderUrl(a0: QUrl) -> QUrl:
    """
    Calls Qt's 'QUrl
    QQuickWebEngineFaviconDBProvider::faviconProviderUrl(const QUrl &a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebenginefavicondbprovider.html

    Parameters
    ----------

    a0 : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QQuickWebEngineFaviconDBProvider::faviconProviderUrl(const QUrl
    #      &a0)
    address = Rituals.call(
        'ritual_ZN32QQuickWebEngineFaviconDBProvider18faviconProviderUrlERK'
        '4QUrl',
        CuteMixin._valueOf(a0),
    )
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickWebEngineFaviconDBProvider'

  #  A C++ QQuickWebEngineFaviconDBProvider Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickWebEngineFaviconDBProvider'

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
    *QQuickWebEngineFaviconDBProvider::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebenginefavicondbprovider.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickWebEngineFaviconDBProvider::metaObject()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK32QQuickWebEngineFaviconDBProvider10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def isIconUrl(self) -> bool:
    """
    Calls Qt's 'bool QQuickWebEngineFaviconDBProvider::isIconUrl() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebenginefavicondbprovider.html#isIconUrl
    """
    #  bool QQuickWebEngineFaviconDBProvider::isIconUrl() const
    ritual = 'ritual_ZNK32QQuickWebEngineFaviconDBProvider9isIconUrlEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK32QQuickWebEngineFaviconDBProvider9isIconUrlEv'
    return self.uglySide.call(ritual)

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
    'QQuickWebEngineFaviconDBProvider::QQuickWebEngineFaviconDBProvider()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebenginefavicondbprovider.html
    """
    #  QQuickWebEngineFaviconDBProvider::QQuickWebEngineFaviconDBProvider()
    self._noteCreation(
        QQuickWebEngineFaviconDBProvider, lambda: Rituals.call(
            'ritual_ZN32QQuickWebEngineFaviconDBProviderC1Ev',
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
