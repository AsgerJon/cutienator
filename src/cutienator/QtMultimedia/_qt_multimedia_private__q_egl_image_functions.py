"""
QtMultimediaPrivate::QEglImageFunctions binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtMultimedia/6.12.0/QtMultimedia/private/qdmabuftextureimporter_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QtMultimediaPrivate::QEglImageFunctions to be private: it
#  declares the class in a header it calls private. cutienator does not care.
#  Qt hands objects of the class out all the same, and a class we are handed
#  is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class QEglImageFunctions(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QtMultimediaPrivate::QEglImageFunctions: a plain
  Python object standing in front of one C++
  QtMultimediaPrivate::QEglImageFunctions.

  C++ hands a QtMultimediaPrivate::QEglImageFunctions around as a copy, so
  every C++ QtMultimediaPrivate::QEglImageFunctions behind a cute one is
  Python's own: it is removed, by the ritual named in '__delete_ritual__',
  when the cute object goes.

  What exists
  -----------

  Every function of Qt's QtMultimediaPrivate::QEglImageFunctions that has a
  ritual and that Python can call so far, 2 names in all: 'instance',
  'isValid'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void
    QtMultimediaPrivate::QEglImageFunctions::glEGLImageTargetTexture2DOES(
    GLenum a0, GLeglImageOES a1) const': names 'void', which has no cute
    class yet.
  - Qt's 'QtMultimediaPrivate::QEglImageFunctions::~QEglImageFunctions()':
    the destructor: Python removes its C++
    QtMultimediaPrivate::QEglImageFunctions by it, and has no other use for
    it.

  What to expect
  --------------

  - The C++ QtMultimediaPrivate::QEglImageFunctions is created at the first
    use, not by 'QtMultimediaPrivate::QEglImageFunctions(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QtMultimediaPrivate::QEglImageFunctions back gives a
    copy the ritual made for Python, in a new cute
    QtMultimediaPrivate::QEglImageFunctions.
  - Each name of Qt's QtMultimediaPrivate::QEglImageFunctions that has no
    cute function yet, 'glEGLImageTargetTexture2DOES', holds a function that
    raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def instance() -> QEglImageFunctions:
    """
    Calls Qt's 'const QEglImageFunctions
    &QtMultimediaPrivate::QEglImageFunctions::instance()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtmultimediaprivate-qeglimagefunctions.html

    Returns
    -------

    QEglImageFunctions
      A new cute QtMultimediaPrivate::QEglImageFunctions around the copy Qt
      gave back. Python owns it.
    """
    #  const QEglImageFunctions
    #      &QtMultimediaPrivate::QEglImageFunctions::instance()
    address = Rituals.call(
        'ritual_ZN19QtMultimediaPrivate18QEglImageFunctions8instanceEv',
    )
    return QEglImageFunctions._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QtMultimediaPrivate::QEglImageFunctions'

  #  Qt's '~QtMultimediaPrivate::QEglImageFunctions()'. Naming it makes this
  #  a value class: Python owns every C++
  #  QtMultimediaPrivate::QEglImageFunctions behind a cute one, and removes
  #  it by this ritual.
  __delete_ritual__ = (
      'ritual_ZN19QtMultimediaPrivate18QEglImageFunctionsD1Ev')

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool QtMultimediaPrivate::QEglImageFunctions::isValid()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtmultimediaprivate-qeglimagefunctions.html
    """
    #  bool QtMultimediaPrivate::QEglImageFunctions::isValid() const
    return self.uglySide.call(
        'ritual_ZNK19QtMultimediaPrivate18QEglImageFunctions7isValidEv',
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
    'QtMultimediaPrivate::QEglImageFunctions::QEglImageFunctions()', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qtmultimediaprivate-qeglimagefunctions.html
    """
    #  QtMultimediaPrivate::QEglImageFunctions::QEglImageFunctions()
    self._noteCreation(QEglImageFunctions, lambda: Rituals.call(
        'ritual_ZN19QtMultimediaPrivate18QEglImageFunctionsC1Ev',
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

  @staticmethod
  def glEGLImageTargetTexture2DOES(*__, **_) -> Never:
    """
    Qt's 'void
    QtMultimediaPrivate::QEglImageFunctions::glEGLImageTargetTexture2DOES(
    GLenum a0, GLeglImageOES a1) const': names 'void', which has no cute
    class yet.
    """
    raise NotImplementedError(
        "'QtMultimediaPrivate.QEglImageFunctions.glEGLImageTargetTexture2DOE"
        "S' has no cute function yet. Qt's 'void "
        "QtMultimediaPrivate::QEglImageFunctions::glEGLImageTargetTexture2DO"
        "ES(GLenum a0, GLeglImageOES a1) const': names 'void', which has no "
        "cute class yet.")
