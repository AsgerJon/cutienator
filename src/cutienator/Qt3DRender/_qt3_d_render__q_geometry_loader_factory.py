"""
Qt3DRender::QGeometryLoaderFactory binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DRender/6.12.0/Qt3DRender/private/qgeometryloaderfactory_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means Qt3DRender::QGeometryLoaderFactory to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QFactoryInterface, QObject
from . import Qt3DRender

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QGeometryLoaderFactory(QObject, QFactoryInterface):
  """
  The cute side of Qt's Qt3DRender::QGeometryLoaderFactory: a plain Python
  object standing in front of one C++ Qt3DRender::QGeometryLoaderFactory.

  It is built on the cute 'QObject', as Qt's
  Qt3DRender::QGeometryLoaderFactory is built on Qt's QObject, and has
  everything that class has. It is built on the cute 'QFactoryInterface' as
  well, as Qt's Qt3DRender::QGeometryLoaderFactory is built on Qt's
  QFactoryInterface too, and has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DRender::QGeometryLoaderFactory that has a ritual
  and that Python can call so far, 3 names in all: 'metaObject', 'tr',
  'create'. None can be made from Python: one comes out of a function of
  another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *Qt3DRender::QGeometryLoaderFactory::qt_metacast(const char
    *a0)': one of Qt's own inner workings.
  - Qt's 'int
    Qt3DRender::QGeometryLoaderFactory::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'Qt3DRender::QGeometryLoaderFactory::~QGeometryLoaderFactory()': the
    destructor: Python never removes a C++
    Qt3DRender::QGeometryLoaderFactory.

  What has no ritual
  ------------------

  3 of the 9 functions Qt declares: 2 not a gap; 1 the class is abstract, so
  C++ cannot make one, and the C++ class of ours does not fill in every
  function it leaves open.

  What to expect
  --------------

  - The C++ Qt3DRender::QGeometryLoaderFactory is created at the first use,
    not by 'Qt3DRender::QGeometryLoaderFactory(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DRender::QGeometryLoaderFactory.
  - Qt tells when it has removed the C++ Qt3DRender::QGeometryLoaderFactory.
    Every call on the cute object, and every use of it as an argument, then
    raises 'RuntimeError', and nothing reaches C++.
  - Each name of Qt's Qt3DRender::QGeometryLoaderFactory that has no cute
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
    Calls Qt's 'QString Qt3DRender::QGeometryLoaderFactory::tr(const char *s,
    const char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qgeometryloaderfactory.html#tr

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
    #  QString Qt3DRender::QGeometryLoaderFactory::tr(const char *s, const
    #      char *c, int n)
    return Rituals.call(
        'ritual_ZN10Qt3DRender22QGeometryLoaderFactory2trEPKcS2_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DRender::QGeometryLoaderFactory'

  #  Qt's Qt3DRender::QGeometryLoaderFactory is built on more than one class.
  #  The part of a C++ Qt3DRender::QGeometryLoaderFactory that belongs to a
  #  class after the first begins somewhere inside the object, and the ritual
  #  named for that class gives where; see 'CuteMixin._addressAs'.
  __cast_rituals__ = {
      'QFactoryInterface':
          'ritual_cast_Qt3DRender_QGeometryLoaderFactory_QFactoryInterface',
  }

  #  A C++ Qt3DRender::QGeometryLoaderFactory Python makes is of a C++ class
  #  of ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DRender_QGeometryLoaderFactory'

  #  The functions Qt calls itself that Qt3DRender::QGeometryLoaderFactory is
  #  the first to declare. A class of a program built on it can write one
  #  anew, and Qt then calls that. For each name: the key C++ knows the
  #  function by, what it gives, and what it takes.
  __virtual_functions__ = {
      'create': (
          ('_ZN10Qt3DRender22QGeometryLoaderFactory6createERK7QString',
           ('address', 'address',
            'Qt3DRender:Qt3DRender.QGeometryLoaderInterface'),
           (
               ('address', 'text', ''),
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
    *Qt3DRender::QGeometryLoaderFactory::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qgeometryloaderfactory.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *Qt3DRender::QGeometryLoaderFactory::metaObject()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender22QGeometryLoaderFactory10metaObjectEv',
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
    Qt's 'Qt3DRender::QGeometryLoaderFactory::QGeometryLoaderFactory(QObject
    *parent)': the class is abstract, so C++ cannot make one, and the C++
    class of ours does not fill in every function it leaves open.
    """
    raise NotImplementedError(
        "'Qt3DRender.QGeometryLoaderFactory.__init__' has no cute function "
        "yet. Qt's "
        "'Qt3DRender::QGeometryLoaderFactory::QGeometryLoaderFactory(QObject"
        " *parent)': the class is abstract, so C++ cannot make one, and the "
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

  @overload(str)
  def create(
      self,
      ext: str,
  ) -> Optional[Qt3DRender.QGeometryLoaderInterface]:
    """
    Calls Qt's 'QGeometryLoaderInterface
    *Qt3DRender::QGeometryLoaderFactory::create(const QString &ext)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qgeometryloaderfactory.html#create

    Parameters
    ----------

    ext : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    Optional[Qt3DRender.QGeometryLoaderInterface]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QGeometryLoaderInterface
    #      *Qt3DRender::QGeometryLoaderFactory::create(const QString &ext)
    address = self.uglySide.call(
        'ritual_ZN10Qt3DRender22QGeometryLoaderFactory6createERK7QString',
        ext,
    )
    return Qt3DRender.QGeometryLoaderInterface._cuteAt(address)
