"""
QSSGAssetImporter binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3DAssetImport/6.12.0/QtQuick3DAssetImport/private/qssgassetimporter_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QSSGAssetImporter to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin
from ..occult import Rituals
from ..QtCore import QObject, QStringList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QJsonObject, QMetaObject

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSSGAssetImporter(QObject):
  """
  The cute side of Qt's QSSGAssetImporter: a plain Python object standing in
  front of one C++ QSSGAssetImporter.

  It is built on the cute 'QObject', as Qt's QSSGAssetImporter is built on
  Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QSSGAssetImporter that has a ritual and that Python
  can call so far, 8 names in all: 'metaObject', 'tr', 'name',
  'inputExtensions', 'outputExtension', 'type', 'importOptions',
  'typeDescription'. None can be made from Python: one comes out of a
  function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QSSGAssetImporter::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QSSGAssetImporter::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QString QSSGAssetImporter::import(const QString &sourceFile, const
    QDir &savePath, const QJsonObject &options, QStringList
    *generatedFiles)': names 'QStringList', which has no cute class yet.
  - Qt's 'QString QSSGAssetImporter::import(const QUrl &url, const
    QJsonObject &options, QSSGSceneDesc::Scene &scene)': takes a type Python
    has no way to hand over yet.

  What has no ritual
  ------------------

  2 of the 14 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QSSGAssetImporter is created at the first use, not by
    'QSSGAssetImporter(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSSGAssetImporter.
  - Qt tells when it has removed the C++ QSSGAssetImporter. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QSSGAssetImporter that has no cute function yet,
    'import_', holds a function that raises 'NotImplementedError', and its
    docstring says why.
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
    Calls Qt's 'QString QSSGAssetImporter::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qssgassetimporter.html#tr

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
    #  QString QSSGAssetImporter::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN17QSSGAssetImporter2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSSGAssetImporter'

  #  A C++ QSSGAssetImporter Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QSSGAssetImporter'

  #  The functions Qt calls itself that QSSGAssetImporter is the first to
  #  declare and that cannot be handed to Python yet, each as Qt declares it.
  #  A class of a program that writes one of them anew is refused, since Qt
  #  would never call what it wrote; see 'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'inputExtensions': (
          'QStringList QSSGAssetImporter::inputExtensions() const',
      ),
      'import': (
          'QString QSSGAssetImporter::import(const QString &, const QDir '
          '&, const QJsonObject &, QStringList *)',
          'QString QSSGAssetImporter::import(const QUrl &, const '
          'QJsonObject &, QSSGSceneDesc::Scene &)',
      ),
  }

  #  The functions Qt calls itself that QSSGAssetImporter is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'name': (
          ('_ZNK17QSSGAssetImporter4nameEv',
           ('address', 'text', ''),
           ()),
      ),
      'outputExtension': (
          ('_ZNK17QSSGAssetImporter15outputExtensionEv',
           ('address', 'text', ''),
           ()),
      ),
      'type': (
          ('_ZNK17QSSGAssetImporter4typeEv',
           ('address', 'text', ''),
           ()),
      ),
      'importOptions': (
          ('_ZNK17QSSGAssetImporter13importOptionsEv',
           ('address', 'value', 'QtCore:QJsonObject'),
           ()),
      ),
      'typeDescription': (
          ('_ZNK17QSSGAssetImporter15typeDescriptionEv',
           ('address', 'text', ''),
           ()),
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
    Calls Qt's 'const QMetaObject *QSSGAssetImporter::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qssgassetimporter.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QSSGAssetImporter::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK17QSSGAssetImporter10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def name(self) -> str:
    """
    Calls Qt's 'QString QSSGAssetImporter::name() const'.

    Qt's own words: https://doc.qt.io/qt-6/qssgassetimporter.html#name

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QSSGAssetImporter::name() const
    return self.uglySide.call('ritual_ZNK17QSSGAssetImporter4nameEv')

  def inputExtensions(self) -> QStringList:
    """
    Calls Qt's 'QStringList QSSGAssetImporter::inputExtensions() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgassetimporter.html#inputExtensions

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QSSGAssetImporter::inputExtensions() const
    address = self.uglySide.call(
        'ritual_ZNK17QSSGAssetImporter15inputExtensionsEv',
    )
    return QStringList._cuteOwning(address)

  def outputExtension(self) -> str:
    """
    Calls Qt's 'QString QSSGAssetImporter::outputExtension() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgassetimporter.html#outputExtension

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QSSGAssetImporter::outputExtension() const
    return self.uglySide.call(
        'ritual_ZNK17QSSGAssetImporter15outputExtensionEv',
    )

  def type(self) -> str:
    """
    Calls Qt's 'QString QSSGAssetImporter::type() const'.

    Qt's own words: https://doc.qt.io/qt-6/qssgassetimporter.html#type

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QSSGAssetImporter::type() const
    return self.uglySide.call('ritual_ZNK17QSSGAssetImporter4typeEv')

  def importOptions(self) -> QJsonObject:
    """
    Calls Qt's 'QJsonObject QSSGAssetImporter::importOptions() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgassetimporter.html#importOptions

    Returns
    -------

    QJsonObject
      A new cute QJsonObject around the copy Qt gave back. Python owns it.
    """
    #  QJsonObject QSSGAssetImporter::importOptions() const
    address = self.uglySide.call(
        'ritual_ZNK17QSSGAssetImporter13importOptionsEv',
    )
    from ..QtCore import QJsonObject
    return QJsonObject._cuteOwning(address)

  def typeDescription(self) -> str:
    """
    Calls Qt's 'QString QSSGAssetImporter::typeDescription() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgassetimporter.html#typeDescription

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QSSGAssetImporter::typeDescription() const
    return self.uglySide.call(
        'ritual_ZNK17QSSGAssetImporter15typeDescriptionEv',
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
  def import_(*__, **_) -> Never:
    """
    - Qt's 'QString QSSGAssetImporter::import(const QString &sourceFile,
      const QDir &savePath, const QJsonObject &options, QStringList
      *generatedFiles)': names 'QStringList', which has no cute class yet.
    - Qt's 'QString QSSGAssetImporter::import(const QUrl &url, const
      QJsonObject &options, QSSGSceneDesc::Scene &scene)': takes a type
      Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QSSGAssetImporter.import_' has no cute function yet. Qt's "
        "'QString QSSGAssetImporter::import(const QString &sourceFile, "
        "const QDir &savePath, const QJsonObject &options, QStringList "
        "*generatedFiles)': names 'QStringList', which has no cute class "
        "yet. Qt's 'QString QSSGAssetImporter::import(const QUrl &url, "
        "const QJsonObject &options, QSSGSceneDesc::Scene &scene)': takes a "
        "type Python has no way to hand over yet.")
