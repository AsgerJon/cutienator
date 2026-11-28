"""
QMultimediaPrivate::QQmlContextSourceResolver binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtMultimediaQuick/6.12.0/QtMultimediaQuick/private/qqmlcontext_source_resolver_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QMultimediaPrivate::QQmlContextSourceResolver to be private: it
#  declares the class in a header it calls private. cutienator does not care.
#  Qt hands objects of the class out all the same, and a class we are handed
#  is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..QtMultimedia import QMultimediaPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QObject, QUrl
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QObject = WAIT['QObject']
  QUrl = WAIT['QUrl']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQmlContextSourceResolver(QMultimediaPrivate.AbstractSourceResolver):
  """
  The cute side of Qt's QMultimediaPrivate::QQmlContextSourceResolver: a
  plain Python object standing in front of one C++
  QMultimediaPrivate::QQmlContextSourceResolver.

  It is built on the cute 'QMultimediaPrivate::AbstractSourceResolver', as
  Qt's QMultimediaPrivate::QQmlContextSourceResolver is built on Qt's
  QMultimediaPrivate::AbstractSourceResolver, and has everything that class
  has.

  C++ hands a QMultimediaPrivate::QQmlContextSourceResolver around as a copy,
  so every C++ QMultimediaPrivate::QQmlContextSourceResolver behind a cute
  one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QMultimediaPrivate::QQmlContextSourceResolver that
  has a ritual and that Python can call so far, 1 name in all: 'resolve'. It
  can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QMultimediaPrivate::QQmlContextSourceResolver::
    ~QQmlContextSourceResolver()': the destructor: Python removes its C++
    QMultimediaPrivate::QQmlContextSourceResolver by it, and has no other use
    for it.

  What to expect
  --------------

  - The C++ QMultimediaPrivate::QQmlContextSourceResolver is created at the
    first use, not by 'QMultimediaPrivate::QQmlContextSourceResolver(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QMultimediaPrivate::QQmlContextSourceResolver back
    gives a copy the ritual made for Python, in a new cute
    QMultimediaPrivate::QQmlContextSourceResolver.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QMultimediaPrivate::QQmlContextSourceResolver'

  #  Qt's '~QMultimediaPrivate::QQmlContextSourceResolver()'. Naming it makes
  #  this a value class: Python owns every C++
  #  QMultimediaPrivate::QQmlContextSourceResolver behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = (
      'ritual_ZN18QMultimediaPrivate25QQmlContextSourceResolverD1Ev')

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QUrl)
  def resolve(self, a0: QUrl) -> QUrl:
    """
    Calls Qt's 'QUrl
    QMultimediaPrivate::QQmlContextSourceResolver::resolve(QUrl a0) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmultimediaprivate-qqmlcontextsourceresolver.html

    Parameters
    ----------

    a0 : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QMultimediaPrivate::QQmlContextSourceResolver::resolve(QUrl a0)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK18QMultimediaPrivate25QQmlContextSourceResolver7resolveE'
        '4QUrl',
        self._valueOf(a0),
    )
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

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

  @overload(QObject)
  @overload(NoneType)
  def __init__(self, objectForContext: Optional[QObject]) -> None:
    """
    Notes what was given, for Qt's
    'QMultimediaPrivate::QQmlContextSourceResolver::
    QQmlContextSourceResolver(QObject *objectForContext)', which is called at
    the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qmultimediaprivate-qqmlcontextsourceresolver.html

    Parameters
    ----------

    objectForContext : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QMultimediaPrivate::QQmlContextSourceResolver::
    #      QQmlContextSourceResolver(QObject *objectForContext)
    self._noteCreation(QQmlContextSourceResolver, lambda: Rituals.call(
        'ritual_ZN18QMultimediaPrivate25QQmlContextSourceResolverC1EP7QObje'
        'ct',
        self._addressOf(objectForContext, 'QObject'),
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
