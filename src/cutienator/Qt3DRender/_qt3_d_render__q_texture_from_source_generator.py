"""
Qt3DRender::QTextureFromSourceGenerator binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DRender/6.12.0/Qt3DRender/private/qtexture_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means Qt3DRender::QTextureFromSourceGenerator to be private: it
#  declares the class in a header it calls private. cutienator does not care.
#  Qt hands objects of the class out all the same, and a class we are handed
#  is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from . import Qt3DRender

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from ..QtCore import QUrl


class QTextureFromSourceGenerator(Qt3DRender.QTextureGenerator):
  """
  The cute side of Qt's Qt3DRender::QTextureFromSourceGenerator: a plain
  Python object standing in front of one C++
  Qt3DRender::QTextureFromSourceGenerator.

  It is built on the cute 'Qt3DRender::QTextureGenerator', as Qt's
  Qt3DRender::QTextureFromSourceGenerator is built on Qt's
  Qt3DRender::QTextureGenerator, and has everything that class has. Qt's
  Qt3DRender::QTextureFromSourceGenerator is built on Qt's
  QEnableSharedFromThis<QTextureFromSourceGenerator> as well, which is not
  reflected.

  C++ hands a Qt3DRender::QTextureFromSourceGenerator around as a copy, so
  every C++ Qt3DRender::QTextureFromSourceGenerator behind a cute one is
  Python's own: it is removed, by the ritual named in '__delete_ritual__',
  when the cute object goes.

  What exists
  -----------

  Every function of Qt's Qt3DRender::QTextureFromSourceGenerator that has a
  ritual and that Python can call so far, 4 names in all: 'status', 'id',
  'url', 'isMirrored'. None can be made from Python: one comes out of a
  function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QTextureDataPtr
    Qt3DRender::QTextureFromSourceGenerator::operator()()': gives a type
    Python has no way to take yet.
  - Qt's 'bool Qt3DRender::QTextureFromSourceGenerator::operator==(const
    QTextureGenerator &other) const': takes a type Python has no way to hand
    over yet.
  - Qt's
    'Qt3DRender::QTextureFromSourceGenerator::~QTextureFromSourceGenerator(
    )': the destructor: Python removes its C++
    Qt3DRender::QTextureFromSourceGenerator by it, and has no other use for
    it.

  What has no ritual
  ------------------

  2 of the 9 functions Qt declares: 2 leans on 'Qt3DRender.

  What to expect
  --------------

  - The C++ Qt3DRender::QTextureFromSourceGenerator is created at the first
    use, not by 'Qt3DRender::QTextureFromSourceGenerator(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a Qt3DRender::QTextureFromSourceGenerator back gives a
    copy the ritual made for Python, in a new cute
    Qt3DRender::QTextureFromSourceGenerator.
  - Each name of Qt's Qt3DRender::QTextureFromSourceGenerator that has no
    cute function yet, '__init__', holds a function that raises
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
  __qt_class__ = 'Qt3DRender::QTextureFromSourceGenerator'

  #  Qt's '~Qt3DRender::QTextureFromSourceGenerator()'. Naming it makes this
  #  a value class: Python owns every C++
  #  Qt3DRender::QTextureFromSourceGenerator behind a cute one, and removes
  #  it by this ritual.
  __delete_ritual__ = (
      'ritual_ZN10Qt3DRender27QTextureFromSourceGeneratorD1Ev')

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def status(self) -> Qt3DRender.QAbstractTexture.Status:
    """
    Calls Qt's 'QAbstractTexture::Status
    Qt3DRender::QTextureFromSourceGenerator::status() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qtexturefromsourcegenerator.html#status

    Returns
    -------

    Qt3DRender.QAbstractTexture.Status
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'Qt3DRender.QAbstractTexture.Status(number)' gives.
    """
    #  QAbstractTexture::Status
    #      Qt3DRender::QTextureFromSourceGenerator::status() const
    return Qt3DRender.QAbstractTexture.Status(self.uglySide.call(
        'ritual_ZNK10Qt3DRender27QTextureFromSourceGenerator6statusEv',
    ))

  def id(self) -> int:
    """
    Calls Qt's 'qintptr Qt3DRender::QTextureFromSourceGenerator::id() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qtexturefromsourcegenerator.html#id
    """
    #  qintptr Qt3DRender::QTextureFromSourceGenerator::id() const
    ritual = 'ritual_ZNK10Qt3DRender27QTextureFromSourceGenerator2idEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK10Qt3DRender27QTextureFromSourceGenerator2idEv'
    return self.uglySide.call(ritual)

  def url(self) -> QUrl:
    """
    Calls Qt's 'QUrl Qt3DRender::QTextureFromSourceGenerator::url() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qtexturefromsourcegenerator.html#url

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl Qt3DRender::QTextureFromSourceGenerator::url() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender27QTextureFromSourceGenerator3urlEv',
    )
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  def isMirrored(self) -> bool:
    """
    Calls Qt's 'bool Qt3DRender::QTextureFromSourceGenerator::isMirrored()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qtexturefromsourcegenerator.html
    """
    #  bool Qt3DRender::QTextureFromSourceGenerator::isMirrored() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender27QTextureFromSourceGenerator10isMirroredEv',
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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    - Qt's
      'Qt3DRender::QTextureFromSourceGenerator::QTextureFromSourceGenerator(
      QTextureLoader *textureLoader, Qt3DCore::QAspectEngine *engine,
      Qt3DCore::QNodeId textureId)': leans on
      'Qt3DRender::TextureLoadingHelper::loadTextureData(QIODevice*, QString
      const&, bool, bool)', which Qt's source does not mark for use from
      outside Qt and has no code for that could be taken.
    - Qt's
      'Qt3DRender::QTextureFromSourceGenerator::QTextureFromSourceGenerator(
      const QTextureFromSourceGenerator &other)': leans on
      'Qt3DRender::TextureLoadingHelper::loadTextureData(QIODevice*, QString
      const&, bool, bool)', which Qt's source does not mark for use from
      outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'Qt3DRender.QTextureFromSourceGenerator.__init__' has no cute "
        "function yet. Qt's "
        "'Qt3DRender::QTextureFromSourceGenerator::QTextureFromSourceGenerat"
        "or(QTextureLoader *textureLoader, Qt3DCore::QAspectEngine *engine, "
        "Qt3DCore::QNodeId textureId)': leans on "
        "'Qt3DRender::TextureLoadingHelper::loadTextureData(QIODevice*, "
        "QString const&, bool, bool)', which Qt's source does not mark for "
        "use from outside Qt and has no code for that could be taken. Qt's "
        "'Qt3DRender::QTextureFromSourceGenerator::QTextureFromSourceGenerat"
        "or(const QTextureFromSourceGenerator &other)': leans on "
        "'Qt3DRender::TextureLoadingHelper::loadTextureData(QIODevice*, "
        "QString const&, bool, bool)', which Qt's source does not mark for "
        "use from outside Qt and has no code for that could be taken.")

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
