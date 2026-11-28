"""
QSGStyledTextMaterial binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qsgdefaultglyphnode_p_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QSGStyledTextMaterial to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from . import QSGMaterial, QSGRendererInterface, QSGTextMaskMaterial

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtGui import QColor, QVector2D, QVector4D
  from . import QSGMaterialShader, QSGMaterialType
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QColor = WAIT['QColor']
  QVector2D = WAIT['QVector2D']
  QVector4D = WAIT['QVector4D']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSGStyledTextMaterial(QSGTextMaskMaterial):
  """
  The cute side of Qt's QSGStyledTextMaterial: a plain Python object standing
  in front of one C++ QSGStyledTextMaterial.

  It is built on the cute 'QSGTextMaskMaterial', as Qt's
  QSGStyledTextMaterial is built on Qt's QSGTextMaskMaterial, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QSGStyledTextMaterial that has a ritual and that
  Python can call so far, 7 names in all: 'setStyleShift', 'styleShift',
  'setStyleColor', 'styleColor', 'type', 'createShader', 'compare'. None can
  be made from Python: one comes out of a function of another class that
  gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSGStyledTextMaterial::~QSGStyledTextMaterial()': the destructor:
    Python never removes a C++ QSGStyledTextMaterial.

  What has no ritual
  ------------------

  1 of the 10 functions Qt declares: 1 leans on 'QSGStyledTextMaterial.

  What to expect
  --------------

  - The C++ QSGStyledTextMaterial is created at the first use, not by
    'QSGStyledTextMaterial(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSGStyledTextMaterial.
  - Each name of Qt's QSGStyledTextMaterial that has no cute function yet,
    '__init__', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSGStyledTextMaterial'

  #  A C++ QSGStyledTextMaterial Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QSGStyledTextMaterial'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def styleShift(self) -> QVector2D:
    """
    Calls Qt's 'const QVector2D &QSGStyledTextMaterial::styleShift() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgstyledtextmaterial.html#styleShift

    Returns
    -------

    QVector2D
      A new cute QVector2D around the copy Qt gave back. Python owns it.
    """
    #  const QVector2D &QSGStyledTextMaterial::styleShift() const
    address = self.uglySide.call(
        'ritual_ZNK21QSGStyledTextMaterial10styleShiftEv',
    )
    from ..QtGui import QVector2D
    return QVector2D._cuteOwning(address)

  def styleColor(self) -> QVector4D:
    """
    Calls Qt's 'const QVector4D &QSGStyledTextMaterial::styleColor() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgstyledtextmaterial.html#styleColor

    Returns
    -------

    QVector4D
      A new cute QVector4D around the copy Qt gave back. Python owns it.
    """
    #  const QVector4D &QSGStyledTextMaterial::styleColor() const
    address = self.uglySide.call(
        'ritual_ZNK21QSGStyledTextMaterial10styleColorEv',
    )
    from ..QtGui import QVector4D
    return QVector4D._cuteOwning(address)

  def type(self) -> Optional[QSGMaterialType]:
    """
    Calls Qt's 'QSGMaterialType *QSGStyledTextMaterial::type() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsgstyledtextmaterial.html#type

    Returns
    -------

    Optional[QSGMaterialType]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSGMaterialType *QSGStyledTextMaterial::type() const
    ritual = 'ritual_ZNK21QSGStyledTextMaterial4typeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK21QSGStyledTextMaterial4typeEv'
    address = self.uglySide.call(ritual)
    from . import QSGMaterialType
    return QSGMaterialType._cuteAt(address)

  @overload(QSGRendererInterface.RenderMode)
  def createShader(
      self,
      renderMode: QSGRendererInterface.RenderMode,
  ) -> Optional[QSGMaterialShader]:
    """
    Calls Qt's 'QSGMaterialShader
    *QSGStyledTextMaterial::createShader(QSGRendererInterface::RenderMode
    renderMode) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgstyledtextmaterial.html#createShader

    Parameters
    ----------

    renderMode : QSGRendererInterface.RenderMode
      Passed on as its number.

    Returns
    -------

    Optional[QSGMaterialShader]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSGMaterialShader
    #      *QSGStyledTextMaterial::createShader(QSGRendererInterface::
    #      RenderMode renderMode) const
    address = self.uglySide.call(
        'ritual_ZNK21QSGStyledTextMaterial12createShaderEN20QSGRendererInte'
        'rface10RenderModeE',
        renderMode.value,
    )
    from . import QSGMaterialShader
    return QSGMaterialShader._cuteAt(address)

  @overload(QSGMaterial)
  @overload(NoneType)
  def compare(self, other: Optional[QSGMaterial]) -> int:
    """
    Calls Qt's 'int QSGStyledTextMaterial::compare(const QSGMaterial *other)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qsgstyledtextmaterial.html#compare

    Parameters
    ----------

    other : Optional[QSGMaterial]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  int QSGStyledTextMaterial::compare(const QSGMaterial *other) const
    ritual = 'ritual_ZNK21QSGStyledTextMaterial7compareEPK11QSGMaterial'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK21QSGStyledTextMaterial7compareEPK11QSGMaterial')
    return self.uglySide.call(ritual, self._addressOf(other))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QVector2D)
  def setStyleShift(self, shift: QVector2D) -> None:
    """
    Calls Qt's 'void QSGStyledTextMaterial::setStyleShift(const QVector2D
    &shift)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgstyledtextmaterial.html#setStyleShift

    Parameters
    ----------

    shift : QVector2D
      Passed on as a value: Qt reads the C++ QVector2D, which stays Python's
      own.
    """
    #  void QSGStyledTextMaterial::setStyleShift(const QVector2D &shift)
    self.uglySide.call(
        'ritual_ZN21QSGStyledTextMaterial13setStyleShiftERK9QVector2D',
        self._valueOf(shift),
    )

  @overload(QColor)
  def setStyleColor(self, c: QColor) -> None:
    """
    Calls Qt's 'void QSGStyledTextMaterial::setStyleColor(const QColor &c)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgstyledtextmaterial.html#setStyleColor

    Parameters
    ----------

    c : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QSGStyledTextMaterial::setStyleColor(const QColor &c)
    self.uglySide.call(
        'ritual_ZN21QSGStyledTextMaterial13setStyleColorERK6QColor',
        self._valueOf(c),
    )

  @overload(QVector4D)
  def setStyleColor(self, color: QVector4D) -> None:
    """
    Calls Qt's 'void QSGStyledTextMaterial::setStyleColor(const QVector4D
    &color)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgstyledtextmaterial.html#setStyleColor

    Parameters
    ----------

    color : QVector4D
      Passed on as a value: Qt reads the C++ QVector4D, which stays Python's
      own.
    """
    #  void QSGStyledTextMaterial::setStyleColor(const QVector4D &color)
    self.uglySide.call(
        'ritual_ZN21QSGStyledTextMaterial13setStyleColorERK9QVector4D',
        self._valueOf(color),
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
    Qt's 'QSGStyledTextMaterial::QSGStyledTextMaterial(QSGRenderContext *rc,
    const QRawFont &font)': leans on
    'QSGStyledTextMaterial::createShader(QSGRendererInterface::RenderMode)
    const', which Qt's source does not mark for use from outside Qt and has
    no code for that could be taken.
    """
    raise NotImplementedError(
        "'QSGStyledTextMaterial.__init__' has no cute function yet. Qt's "
        "'QSGStyledTextMaterial::QSGStyledTextMaterial(QSGRenderContext "
        "*rc, const QRawFont &font)': leans on "
        "'QSGStyledTextMaterial::createShader(QSGRendererInterface::RenderMo"
        "de) const', which Qt's source does not mark for use from outside "
        "Qt and has no code for that could be taken.")

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
