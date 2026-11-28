"""
Qt3DExtras::QText2DMaterial binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DExtras/6.12.0/Qt3DExtras/private/qtext2dmaterial_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means Qt3DExtras::QText2DMaterial to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..Qt3DRender import Qt3DRender

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
  from ..QtGui import QColor
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QColor = WAIT['QColor']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QText2DMaterial(Qt3DRender.QMaterial):
  """
  The cute side of Qt's Qt3DExtras::QText2DMaterial: a plain Python object
  standing in front of one C++ Qt3DExtras::QText2DMaterial.

  It is built on the cute 'Qt3DRender::QMaterial', as Qt's
  Qt3DExtras::QText2DMaterial is built on Qt's Qt3DRender::QMaterial, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DExtras::QText2DMaterial that has a ritual and
  that Python can call so far, 3 names in all: 'metaObject', 'setColor',
  'setDistanceFieldTexture'. None can be made from Python: one comes out of a
  function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *Qt3DExtras::QText2DMaterial::qt_metacast(const char *a0)':
    one of Qt's own inner workings.
  - Qt's 'int Qt3DExtras::QText2DMaterial::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'Qt3DExtras::QText2DMaterial::~QText2DMaterial()': the destructor:
    Python never removes a C++ Qt3DExtras::QText2DMaterial.
  - Qt's 'QText2DMaterialPrivate *Qt3DExtras::QText2DMaterial::d_func()':
    gives 'Qt3DExtras::QText2DMaterialPrivate', which has no cute class yet.
  - Qt's 'const QText2DMaterialPrivate *Qt3DExtras::QText2DMaterial::d_func()
    const': gives 'Qt3DExtras::QText2DMaterialPrivate', which has no cute
    class yet.

  What has no ritual
  ------------------

  4 of the 12 functions Qt declares: 2 not a gap; 2 leans on 'Qt3DExtras.

  What to expect
  --------------

  - The C++ Qt3DExtras::QText2DMaterial is created at the first use, not by
    'Qt3DExtras::QText2DMaterial(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DExtras::QText2DMaterial.
  - Qt tells when it has removed the C++ Qt3DExtras::QText2DMaterial. Every
    call on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's Qt3DExtras::QText2DMaterial that has no cute function
    yet, '__init__', holds a function that raises 'NotImplementedError', and
    its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DExtras::QText2DMaterial'

  #  A C++ Qt3DExtras::QText2DMaterial Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DExtras_QText2DMaterial'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *Qt3DExtras::QText2DMaterial::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qtext2dmaterial.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *Qt3DExtras::QText2DMaterial::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DExtras15QText2DMaterial10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QColor)
  def setColor(self, color: QColor) -> None:
    """
    Calls Qt's 'void Qt3DExtras::QText2DMaterial::setColor(const QColor
    &color)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qtext2dmaterial.html#setColor

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void Qt3DExtras::QText2DMaterial::setColor(const QColor &color)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras15QText2DMaterial8setColorERK6QColor',
        self._valueOf(color),
    )

  @overload(WAIT['Qt3DRender.QAbstractTexture'])
  @overload(NoneType)
  def setDistanceFieldTexture(
      self,
      tex: Optional[Qt3DRender.QAbstractTexture],
  ) -> None:
    """
    Calls Qt's 'void
    Qt3DExtras::QText2DMaterial::setDistanceFieldTexture(Qt3DRender::
    QAbstractTexture *tex)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qtext2dmaterial.html

    Parameters
    ----------

    tex : Optional[Qt3DRender.QAbstractTexture]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DExtras::QText2DMaterial::setDistanceFieldTexture(Qt3DRender::
    #      QAbstractTexture *tex)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras15QText2DMaterial23setDistanceFieldTextureEPN'
        '10Qt3DRender16QAbstractTextureE',
        self._addressOf(tex),
    )

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
    Qt's 'Qt3DExtras::QText2DMaterial::QText2DMaterial(Qt3DCore::QNode
    *parent)': leans on
    'Qt3DExtras::QText2DMaterial::qt_metacall(QMetaObject::Call, int,
    void**)', which Qt's source does not mark for use from outside Qt and has
    no code for that could be taken.
    """
    raise NotImplementedError(
        "'Qt3DExtras.QText2DMaterial.__init__' has no cute function yet. "
        "Qt's 'Qt3DExtras::QText2DMaterial::QText2DMaterial(Qt3DCore::QNode "
        "*parent)': leans on "
        "'Qt3DExtras::QText2DMaterial::qt_metacall(QMetaObject::Call, int, "
        "void**)', which Qt's source does not mark for use from outside Qt "
        "and has no code for that could be taken.")

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
