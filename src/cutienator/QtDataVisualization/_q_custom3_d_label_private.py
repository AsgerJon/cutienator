"""
QCustom3DLabelPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDataVisualization/6.12.0/QtDataVisualization/private/qcustom3dlabel_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QCustom3DLabelPrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from . import QCustom3DItemPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject


class QCustom3DLabelPrivate(QCustom3DItemPrivate):
  """
  The cute side of Qt's QCustom3DLabelPrivate: a plain Python object standing
  in front of one C++ QCustom3DLabelPrivate.

  It is built on the cute 'QCustom3DItemPrivate', as Qt's
  QCustom3DLabelPrivate is built on Qt's QCustom3DItemPrivate, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QCustom3DLabelPrivate that has a ritual and that
  Python can call so far, 2 names in all: 'metaObject', 'resetDirtyBits'.
  None can be made from Python: one comes out of a function of another class
  that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QCustom3DLabelPrivate::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QCustom3DLabelPrivate::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QCustom3DLabelPrivate::~QCustom3DLabelPrivate()': the destructor:
    Python never removes a C++ QCustom3DLabelPrivate.

  What has no ritual
  ------------------

  8 of the 13 functions Qt declares: 3 leans on 'QCustom3DLabelPrivate; 3
  leans on 'Utils; 2 not a gap.

  What to expect
  --------------

  - The C++ QCustom3DLabelPrivate is created at the first use, not by
    'QCustom3DLabelPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QCustom3DLabelPrivate.
  - Qt tells when it has removed the C++ QCustom3DLabelPrivate. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QCustom3DLabelPrivate that has no cute function yet,
    '__init__', 'createTextureImage', 'handleTextureChange', holds a function
    that raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QCustom3DLabelPrivate'
  #  The part of Qt it is of, as another part has a class of its name too.
  __qt_part__ = 'QtDataVisualization'

  #  A C++ QCustom3DLabelPrivate Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QCustom3DLabelPrivate'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QCustom3DLabelPrivate::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcustom3dlabelprivate.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QCustom3DLabelPrivate::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK21QCustom3DLabelPrivate10metaObjectEv',
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
    - Qt's 'QCustom3DLabelPrivate::QCustom3DLabelPrivate(QCustom3DLabel *q)':
      leans on 'QCustom3DLabelPrivate::qt_metacall(QMetaObject::Call, int,
      void**)', which Qt's source does not mark for use from outside Qt and
      has no code for that could be taken.
    - Qt's 'QCustom3DLabelPrivate::QCustom3DLabelPrivate(QCustom3DLabel *q,
      const QString &text, const QFont &font, const QVector3D &position,
      const QVector3D &scaling, const QQuaternion &rotation)': leans on
      'QCustom3DLabelPrivate::qt_metacall(QMetaObject::Call, int, void**)',
      which Qt's source does not mark for use from outside Qt and has no code
      for that could be taken.
    """
    raise NotImplementedError(
        "'QCustom3DLabelPrivate.__init__' has no cute function yet. Qt's "
        "'QCustom3DLabelPrivate::QCustom3DLabelPrivate(QCustom3DLabel *q)': "
        "leans on 'QCustom3DLabelPrivate::qt_metacall(QMetaObject::Call, "
        "int, void**)', which Qt's source does not mark for use from "
        "outside Qt and has no code for that could be taken. Qt's "
        "'QCustom3DLabelPrivate::QCustom3DLabelPrivate(QCustom3DLabel *q, "
        "const QString &text, const QFont &font, const QVector3D &position, "
        "const QVector3D &scaling, const QQuaternion &rotation)': leans on "
        "'QCustom3DLabelPrivate::qt_metacall(QMetaObject::Call, int, "
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

  def resetDirtyBits(self) -> None:
    """
    Calls Qt's 'void QCustom3DLabelPrivate::resetDirtyBits()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcustom3dlabelprivate.html#resetDirtyBits
    """
    #  void QCustom3DLabelPrivate::resetDirtyBits()
    self.uglySide.call('ritual_ZN21QCustom3DLabelPrivate14resetDirtyBitsEv')

  @staticmethod
  def createTextureImage(*__, **_) -> Never:
    """
    - Qt's 'void QCustom3DLabelPrivate::createTextureImage()': leans on
      'Utils::printTextToImage(QFont const&, QString const&, QColor const&,
      QColor const&, bool, bool, int)', which Qt's source does not mark for
      use from outside Qt and has no code for that could be taken.
    - Qt's 'void QCustom3DLabelPrivate::createTextureImage(const QColor
      &bgrColor, const QColor &txtColor, bool background, bool borders)':
      leans on 'Utils::printTextToImage(QFont const&, QString const&, QColor
      const&, QColor const&, bool, bool, int)', which Qt's source does not
      mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QCustom3DLabelPrivate.createTextureImage' has no cute function "
        "yet. Qt's 'void QCustom3DLabelPrivate::createTextureImage()': "
        "leans on 'Utils::printTextToImage(QFont const&, QString const&, "
        "QColor const&, QColor const&, bool, bool, int)', which Qt's source "
        "does not mark for use from outside Qt and has no code for that "
        "could be taken. Qt's 'void "
        "QCustom3DLabelPrivate::createTextureImage(const QColor &bgrColor, "
        "const QColor &txtColor, bool background, bool borders)': leans on "
        "'Utils::printTextToImage(QFont const&, QString const&, QColor "
        "const&, QColor const&, bool, bool, int)', which Qt's source does "
        "not mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def handleTextureChange(*__, **_) -> Never:
    """
    Qt's 'void QCustom3DLabelPrivate::handleTextureChange()': leans on
    'Utils::printTextToImage(QFont const&, QString const&, QColor const&,
    QColor const&, bool, bool, int)', which Qt's source does not mark for use
    from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QCustom3DLabelPrivate.handleTextureChange' has no cute function "
        "yet. Qt's 'void QCustom3DLabelPrivate::handleTextureChange()': "
        "leans on 'Utils::printTextToImage(QFont const&, QString const&, "
        "QColor const&, QColor const&, bool, bool, int)', which Qt's source "
        "does not mark for use from outside Qt and has no code for that "
        "could be taken.")
