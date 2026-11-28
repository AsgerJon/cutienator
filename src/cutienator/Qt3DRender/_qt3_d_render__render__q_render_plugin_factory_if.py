"""
Qt3DRender::Render::QRenderPluginFactoryIf binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DRender/6.12.0/Qt3DRender/private/qrenderpluginfactoryif_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means Qt3DRender::Render::QRenderPluginFactoryIf to be private: it
#  declares the class in a header it calls private. cutienator does not care.
#  Qt hands objects of the class out all the same, and a class we are handed
#  is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject, QStringList
from . import Qt3DRender

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QRenderPluginFactoryIf(QObject):
  """
  The cute side of Qt's Qt3DRender::Render::QRenderPluginFactoryIf: a plain
  Python object standing in front of one C++
  Qt3DRender::Render::QRenderPluginFactoryIf.

  It is built on the cute 'QObject', as Qt's
  Qt3DRender::Render::QRenderPluginFactoryIf is built on Qt's QObject, and
  has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DRender::Render::QRenderPluginFactoryIf that has
  a ritual and that Python can call so far, 3 names in all: 'metaObject',
  'tr', 'create'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *Qt3DRender::Render::QRenderPluginFactoryIf::qt_metacast(const
    char *a0)': one of Qt's own inner workings.
  - Qt's 'int
    Qt3DRender::Render::QRenderPluginFactoryIf::qt_metacall(QMetaObject::Call
    a0, int a1, void **a2)': one of Qt's own inner workings.
  - Qt's
    'Qt3DRender::Render::QRenderPluginFactoryIf::~QRenderPluginFactoryIf()':
    the destructor: Python never removes a C++
    Qt3DRender::Render::QRenderPluginFactoryIf.

  What has no ritual
  ------------------

  2 of the 9 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ Qt3DRender::Render::QRenderPluginFactoryIf is created at the
    first use, not by 'Qt3DRender::Render::QRenderPluginFactoryIf(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DRender::Render::QRenderPluginFactoryIf.
  - Qt tells when it has removed the C++
    Qt3DRender::Render::QRenderPluginFactoryIf. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
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
    Calls Qt's 'QString Qt3DRender::Render::QRenderPluginFactoryIf::tr(const
    char *s, const char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-qrenderpluginfactoryif.html#tr

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
    #  QString Qt3DRender::Render::QRenderPluginFactoryIf::tr(const char *s,
    #      const char *c, int n)
    return Rituals.call(
        'ritual_ZN10Qt3DRender6Render22QRenderPluginFactoryIf2trEPKcS3_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DRender::Render::QRenderPluginFactoryIf'

  #  A C++ Qt3DRender::Render::QRenderPluginFactoryIf Python makes is of a
  #  C++ class of ours, in which Python can take functions over. This ritual
  #  hands one over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DRender_Render_QRenderPluginFactoryIf'

  #  The functions Qt calls itself that
  #  Qt3DRender::Render::QRenderPluginFactoryIf is the first to declare and
  #  that cannot be handed to Python yet, each as Qt declares it. A class of
  #  a program that writes one of them anew is refused, since Qt would never
  #  call what it wrote; see 'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'create': (
          'QRenderPlugin '
          '*Qt3DRender::Render::QRenderPluginFactoryIf::create(const '
          'QString &, const QStringList &)',
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
    *Qt3DRender::Render::QRenderPluginFactoryIf::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-qrenderpluginfactoryif.html

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject
    #      *Qt3DRender::Render::QRenderPluginFactoryIf::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render22QRenderPluginFactoryIf10metaObjectE'
        'v',
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
    'Qt3DRender::Render::QRenderPluginFactoryIf::QRenderPluginFactoryIf(
    QObject *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-qrenderpluginfactoryif.html

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  Qt3DRender::Render::QRenderPluginFactoryIf::
    #      QRenderPluginFactoryIf(QObject *parent)
    self._noteCreation(QRenderPluginFactoryIf, lambda: Rituals.call(
        'ritual_ZN10Qt3DRender6Render22QRenderPluginFactoryIfC1EP7QObject',
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

  @overload(str, QStringList)
  def create(
      self,
      key: str,
      paramList: QStringList,
  ) -> Optional[Qt3DRender.Render.QRenderPlugin]:
    """
    Calls Qt's 'QRenderPlugin
    *Qt3DRender::Render::QRenderPluginFactoryIf::create(const QString &key,
    const QStringList &paramList)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-qrenderpluginfactoryif.html

    Parameters
    ----------

    key : str
      Passed on as it is: a QString is made of it for the call.

    paramList : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    Returns
    -------

    Optional[Qt3DRender.Render.QRenderPlugin]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QRenderPlugin
    #      *Qt3DRender::Render::QRenderPluginFactoryIf::create(const QString
    #      &key, const QStringList &paramList)
    address = self.uglySide.call(
        'ritual_ZN10Qt3DRender6Render22QRenderPluginFactoryIf6createERK7QSt'
        'ringRK5QListIS2_E',
        key, self._valueOf(paramList),
    )
    return Qt3DRender.Render.QRenderPlugin._cuteAt(address)
