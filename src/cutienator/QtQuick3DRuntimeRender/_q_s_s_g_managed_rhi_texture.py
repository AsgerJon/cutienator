"""
QSSGManagedRhiTexture binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrhicontext_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QSSGManagedRhiTexture to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class QSSGManagedRhiTexture(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QSSGManagedRhiTexture: a plain Python object standing
  in front of one C++ QSSGManagedRhiTexture.

  What exists
  -----------

  Every function of Qt's QSSGManagedRhiTexture that has a ritual and that
  Python can call so far, 2 names in all: 'isValid', 'invalidate'. It can be
  made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const std::unique_ptr<QRhiTexture>
    &QSSGManagedRhiTexture::texture() const': gives a type Python has no way
    to take yet.
  - Qt's 'QSSGManagedRhiTexture::QSSGManagedRhiTexture(const
    std::shared_ptr<QSSGUserRenderPassManager> &manager, QRhiTexture
    *texture, Private a2)': takes a type Python has no way to hand over yet.
  - Qt's 'QSSGManagedRhiTexture::~QSSGManagedRhiTexture()': the destructor:
    Python never removes a C++ QSSGManagedRhiTexture.
  - Qt's 'Ptr QSSGManagedRhiTexture::make_copy(const Ptr &other)': takes a
    type Python has no way to hand over yet.

  What has no ritual
  ------------------

  3 of the 10 functions Qt declares: 2 forbidden; 1 the compiler refuses its
  ritual as it would be written here.

  What to expect
  --------------

  - The C++ QSSGManagedRhiTexture is created at the first use, not by
    'QSSGManagedRhiTexture(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSSGManagedRhiTexture.
  - Each name of Qt's QSSGManagedRhiTexture that has no cute function yet,
    'make_copy', 'texture', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSSGManagedRhiTexture'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool QSSGManagedRhiTexture::isValid() const'.

    Qt's own words: https://doc.qt.io/qt-6/qssgmanagedrhitexture.html#isValid
    """
    #  bool QSSGManagedRhiTexture::isValid() const
    return self.uglySide.call('ritual_ZNK21QSSGManagedRhiTexture7isValidEv')

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
    'QSSGManagedRhiTexture::QSSGManagedRhiTexture()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgmanagedrhitexture.html#QSSGManagedRhiTexture
    """
    #  QSSGManagedRhiTexture::QSSGManagedRhiTexture()
    self._noteCreation(QSSGManagedRhiTexture, lambda: Rituals.call(
        'ritual_ZN21QSSGManagedRhiTextureC1Ev',
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

  def invalidate(self) -> None:
    """
    Calls Qt's 'void QSSGManagedRhiTexture::invalidate()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgmanagedrhitexture.html#invalidate
    """
    #  void QSSGManagedRhiTexture::invalidate()
    self.uglySide.call('ritual_ZN21QSSGManagedRhiTexture10invalidateEv')

  @staticmethod
  def make_copy(*__, **_) -> Never:
    """
    Qt's 'Ptr QSSGManagedRhiTexture::make_copy(const Ptr &other)': takes a
    type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QSSGManagedRhiTexture.make_copy' has no cute function yet. Qt's "
        "'Ptr QSSGManagedRhiTexture::make_copy(const Ptr &other)': takes a "
        "type Python has no way to hand over yet.")

  @staticmethod
  def texture(*__, **_) -> Never:
    """
    Qt's 'const std::unique_ptr<QRhiTexture>
    &QSSGManagedRhiTexture::texture() const': gives a type Python has no way
    to take yet.
    """
    raise NotImplementedError(
        "'QSSGManagedRhiTexture.texture' has no cute function yet. Qt's "
        "'const std::unique_ptr<QRhiTexture> "
        "&QSSGManagedRhiTexture::texture() const': gives a type Python has "
        "no way to take yet.")
