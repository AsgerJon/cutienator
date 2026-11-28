"""
QShaderKey binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/rhi/qshader.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QList
from . import QShader

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from . import QShaderVersion
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QShaderVersion = WAIT['QShaderVersion']


class QShaderKey(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QShaderKey: a plain Python object standing in front
  of one C++ QShaderKey.

  C++ hands a QShaderKey around as a copy, so every C++ QShaderKey behind a
  cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QShaderKey that has a ritual and that Python can
  call so far, 6 names in all: 'source', 'setSource', 'sourceVersion',
  'setSourceVersion', 'sourceVariant', 'setSourceVariant'. It can be made
  from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QShaderKey::~QShaderKey()': the destructor: Python removes its C++
    QShaderKey by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QShaderKey is created at the first use, not by 'QShaderKey(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QShaderKey back gives a copy the ritual made for
    Python, in a new cute QShaderKey.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QShaderKey'

  #  Qt's '~QShaderKey()'. Naming it makes this a value class: Python owns
  #  every C++ QShaderKey behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN10QShaderKeyD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def source(self) -> QShader.Source:
    """
    Calls Qt's 'QShader::Source QShaderKey::source() const'.

    Qt's own words: https://doc.qt.io/qt-6/qshaderkey.html#source

    Returns
    -------

    QShader.Source
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'QShader.Source(number)'
      gives.
    """
    #  QShader::Source QShaderKey::source() const
    return QShader.Source(self.uglySide.call(
        'ritual_ZNK10QShaderKey6sourceEv',
    ))

  def sourceVersion(self) -> QShaderVersion:
    """
    Calls Qt's 'QShaderVersion QShaderKey::sourceVersion() const'.

    Qt's own words: https://doc.qt.io/qt-6/qshaderkey.html#sourceVersion

    Returns
    -------

    QShaderVersion
      A new cute QShaderVersion around the copy Qt gave back. Python owns it.
    """
    #  QShaderVersion QShaderKey::sourceVersion() const
    address = self.uglySide.call('ritual_ZNK10QShaderKey13sourceVersionEv')
    from . import QShaderVersion
    return QShaderVersion._cuteOwning(address)

  def sourceVariant(self) -> QShader.Variant:
    """
    Calls Qt's 'QShader::Variant QShaderKey::sourceVariant() const'.

    Qt's own words: https://doc.qt.io/qt-6/qshaderkey.html#sourceVariant

    Returns
    -------

    QShader.Variant
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'QShader.Variant(number)'
      gives.
    """
    #  QShader::Variant QShaderKey::sourceVariant() const
    return QShader.Variant(self.uglySide.call(
        'ritual_ZNK10QShaderKey13sourceVariantEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QShader.Source)
  def setSource(self, s: QShader.Source) -> None:
    """
    Calls Qt's 'void QShaderKey::setSource(QShader::Source s)'.

    Qt's own words: https://doc.qt.io/qt-6/qshaderkey.html#setSource

    Parameters
    ----------

    s : QShader.Source
      Passed on as its number.
    """
    #  void QShaderKey::setSource(QShader::Source s)
    self.uglySide.call(
        'ritual_ZN10QShaderKey9setSourceEN7QShader6SourceE', s.value,
    )

  @overload(QShaderVersion)
  def setSourceVersion(self, sver: QShaderVersion) -> None:
    """
    Calls Qt's 'void QShaderKey::setSourceVersion(const QShaderVersion
    &sver)'.

    Qt's own words: https://doc.qt.io/qt-6/qshaderkey.html#setSourceVersion

    Parameters
    ----------

    sver : QShaderVersion
      Passed on as a value: Qt reads the C++ QShaderVersion, which stays
      Python's own.
    """
    #  void QShaderKey::setSourceVersion(const QShaderVersion &sver)
    self.uglySide.call(
        'ritual_ZN10QShaderKey16setSourceVersionERK14QShaderVersion',
        self._valueOf(sver),
    )

  @overload(QShader.Variant)
  def setSourceVariant(self, svar: QShader.Variant) -> None:
    """
    Calls Qt's 'void QShaderKey::setSourceVariant(QShader::Variant svar)'.

    Qt's own words: https://doc.qt.io/qt-6/qshaderkey.html#setSourceVariant

    Parameters
    ----------

    svar : QShader.Variant
      Passed on as its number.
    """
    #  void QShaderKey::setSourceVariant(QShader::Variant svar)
    self.uglySide.call(
        'ritual_ZN10QShaderKey16setSourceVariantEN7QShader7VariantE',
        svar.value,
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

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'QShaderKey::QShaderKey()', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qshaderkey.html#QShaderKey
    """
    #  QShaderKey::QShaderKey()
    self._noteCreation(QShaderKey, lambda: Rituals.call(
        'ritual_ZN10QShaderKeyC1Ev',
    ))

  @overload(QShader.Source, QShaderVersion)
  @overload(QShader.Source, QShaderVersion, QShader.Variant)
  def __init__(
      self,
      s: QShader.Source,
      sver: QShaderVersion,
      svar: QShader.Variant = QShader.Variant.StandardShader,
  ) -> None:
    """
    Notes what was given, for Qt's 'QShaderKey::QShaderKey(QShader::Source s,
    const QShaderVersion &sver, QShader::Variant svar)', which is called at
    the first use.

    Qt's own words: https://doc.qt.io/qt-6/qshaderkey.html#QShaderKey

    Parameters
    ----------

    s : QShader.Source
      Passed on as its number.

    sver : QShaderVersion
      Passed on as a value: Qt reads the C++ QShaderVersion, which stays
      Python's own.

    svar : QShader.Variant
      Passed on as its number. May be left out, as in Qt: it is then
      QShader.Variant.StandardShader.
    """
    #  QShaderKey::QShaderKey(QShader::Source s, const QShaderVersion &sver,
    #      QShader::Variant svar)
    self._noteCreation(QShaderKey, lambda: Rituals.call(
        'ritual_ZN10QShaderKeyC1EN7QShader6SourceERK14QShaderVersionNS0_7Va'
        'riantE',
        s.value, self._valueOf(sver), svar.value,
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


#  Qt's 'QList<QShaderKey>': the list of QShaderKey, which
#  'QList[QShaderKey]' gives. It is made here, so that there is one as soon
#  as there can be a QShaderKey.
QList.createKind(
    QShaderKey, 'value',
    make='ritual_list_make_QShaderKey',
    add='ritual_list_add_QShaderKey',
    size='ritual_list_size_QShaderKey',
    at='ritual_list_at_QShaderKey',
    drop='ritual_list_drop_QShaderKey',
)
