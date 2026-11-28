"""
Qt3DAnimation::Animation::GLTFImporter binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DAnimation/6.12.0/Qt3DAnimation/private/gltfimporter_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means Qt3DAnimation::Animation::GLTFImporter to be private: it declares
#  the class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from ..Qt3DCore import Qt3DCore

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from ..QtCore import QByteArray, QJsonDocument, QJsonObject
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QJsonDocument = WAIT['QJsonDocument']
  QJsonObject = WAIT['QJsonObject']


class GLTFImporter(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's Qt3DAnimation::Animation::GLTFImporter: a plain
  Python object standing in front of one C++
  Qt3DAnimation::Animation::GLTFImporter.

  C++ hands a Qt3DAnimation::Animation::GLTFImporter around as a copy, so
  every C++ Qt3DAnimation::Animation::GLTFImporter behind a cute one is
  Python's own: it is removed, by the ritual named in '__delete_ritual__',
  when the cute object goes.

  What exists
  -----------

  Every function of Qt's Qt3DAnimation::Animation::GLTFImporter that has a
  ritual and that Python can call so far, 10 names in all:
  'createAnimationData', 'accessorTypeFromJSON', 'accessorTypeSize',
  'accessorDataSizeFromJson', 'setBasePath', 'setJSON', 'cleanup',
  'processJSONBuffer', 'setupNodeParentLinks', 'resolveLocalData'. It can be
  made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QList<Animation>
    Qt3DAnimation::Animation::GLTFImporter::animations() const': gives a type
    Python has no way to take yet.
  - Qt's 'QHash<qsizetype, qsizetype>
    Qt3DAnimation::Animation::GLTFImporter::createNodeIndexToJointIndexMap(
    const Skin &skin) const': gives a type Python has no way to take yet.
  - Qt's 'RawData Qt3DAnimation::Animation::GLTFImporter::accessorData(int
    accessorIndex, int index) const': gives a type Python has no way to take
    yet.
  - Qt's 'Qt3DAnimation::Animation::GLTFImporter::~GLTFImporter()': the
    destructor: Python removes its C++ Qt3DAnimation::Animation::GLTFImporter
    by it, and has no other use for it.

  What has no ritual
  ------------------

  8 of the 23 functions Qt declares: 8 leans on 'Qt3DAnimation.

  What to expect
  --------------

  - The C++ Qt3DAnimation::Animation::GLTFImporter is created at the first
    use, not by 'Qt3DAnimation::Animation::GLTFImporter(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a Qt3DAnimation::Animation::GLTFImporter back gives a
    copy the ritual made for Python, in a new cute
    Qt3DAnimation::Animation::GLTFImporter.
  - Each name of Qt's Qt3DAnimation::Animation::GLTFImporter that has no cute
    function yet, 'accessorData', 'animations',
    'createNodeIndexToJointIndexMap', 'load', 'parse', 'parseGLTF2',
    'processJSONAccessor', 'processJSONAnimation', 'processJSONBufferView',
    'processJSONNode', 'processJSONSkin', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The classes Qt writes inside Qt3DAnimation::Animation::GLTFImporter,
  #  each a class in here as in C++.

  class AccessorData(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's
    Qt3DAnimation::Animation::GLTFImporter::AccessorData: a plain Python
    object standing in front of one C++
    Qt3DAnimation::Animation::GLTFImporter::AccessorData.

    C++ hands a Qt3DAnimation::Animation::GLTFImporter::AccessorData around
    as a copy, so every C++
    Qt3DAnimation::Animation::GLTFImporter::AccessorData behind a cute one is
    Python's own: it is removed, by the ritual named in '__delete_ritual__',
    when the cute object goes.

    What exists
    -----------

    No function of Qt's Qt3DAnimation::Animation::GLTFImporter::AccessorData
    yet. It can be made from Python, in 2 ways; see '__init__'.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's
      'Qt3DAnimation::Animation::GLTFImporter::AccessorData::~AccessorData(
      )': the destructor: Python removes its C++
      Qt3DAnimation::Animation::GLTFImporter::AccessorData by it, and has no
      other use for it.

    What to expect
    --------------

    - The C++ Qt3DAnimation::Animation::GLTFImporter::AccessorData is created
      at the first use, not by
      'Qt3DAnimation::Animation::GLTFImporter::AccessorData(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a
      Qt3DAnimation::Animation::GLTFImporter::AccessorData back gives a copy
      the ritual made for Python, in a new cute
      Qt3DAnimation::Animation::GLTFImporter::AccessorData.
    """

    #  The cute classes this class names and is not built on. Each waits
    #  until it is made; see 'WAIT'. A type checker reads the imports at the
    #  top of the file instead.
    if not TYPE_CHECKING:
      QJsonObject = WAIT['QJsonObject']

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'Qt3DAnimation::Animation::GLTFImporter::AccessorData'

    #  Qt's '~Qt3DAnimation::Animation::GLTFImporter::AccessorData()'. Naming
    #  it makes this a value class: Python owns every C++
    #  Qt3DAnimation::Animation::GLTFImporter::AccessorData behind a cute
    #  one, and removes it by this ritual.
    __delete_ritual__ = (
        'ritual_ZN13Qt3DAnimation9Animation12GLTFImporter12AccessorDataD1Ev')

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @overload()
    def __init__(self) -> None:
      """
      Notes what was given, for Qt's
      'Qt3DAnimation::Animation::GLTFImporter::AccessorData::AccessorData()',
      which is called at the first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qt3danimation-animation-gltfimporter-accessordata.html
      """
      #  Qt3DAnimation::Animation::GLTFImporter::AccessorData::AccessorData()
      self._noteCreation(GLTFImporter.AccessorData, lambda: Rituals.call(
          'ritual_ZN13Qt3DAnimation9Animation12GLTFImporter12AccessorDataC1'
          'Ev',
      ))

    @overload(QJsonObject)
    def __init__(self, json: QJsonObject) -> None:
      """
      Notes what was given, for Qt's
      'Qt3DAnimation::Animation::GLTFImporter::AccessorData::AccessorData(
      const QJsonObject &json)', which is called at the first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qt3danimation-animation-gltfimporter-accessordata.html

      Parameters
      ----------

      json : QJsonObject
        Passed on as a value: Qt reads the C++ QJsonObject, which stays
        Python's own.
      """
      #  Qt3DAnimation::Animation::GLTFImporter::AccessorData::
      #      AccessorData(const QJsonObject &json)
      self._noteCreation(GLTFImporter.AccessorData, lambda: Rituals.call(
          'ritual_ZN13Qt3DAnimation9Animation12GLTFImporter12AccessorDataC1'
          'ERK11QJsonObject',
          self._valueOf(json),
      ))

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  class Animation(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's Qt3DAnimation::Animation::GLTFImporter::Animation:
    a plain Python object standing in front of one C++
    Qt3DAnimation::Animation::GLTFImporter::Animation.

    C++ hands a Qt3DAnimation::Animation::GLTFImporter::Animation around as a
    copy, so every C++ Qt3DAnimation::Animation::GLTFImporter::Animation
    behind a cute one is Python's own: it is removed, by the ritual named in
    '__delete_ritual__', when the cute object goes.

    What exists
    -----------

    No function of Qt's Qt3DAnimation::Animation::GLTFImporter::Animation
    yet. It can be made from Python, in 2 ways; see '__init__'.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'Qt3DAnimation::Animation::GLTFImporter::Animation::~Animation()':
      the destructor: Python removes its C++
      Qt3DAnimation::Animation::GLTFImporter::Animation by it, and has no
      other use for it.

    What to expect
    --------------

    - The C++ Qt3DAnimation::Animation::GLTFImporter::Animation is created at
      the first use, not by
      'Qt3DAnimation::Animation::GLTFImporter::Animation(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a Qt3DAnimation::Animation::GLTFImporter::Animation
      back gives a copy the ritual made for Python, in a new cute
      Qt3DAnimation::Animation::GLTFImporter::Animation.
    """

    #  The cute classes this class names and is not built on. Each waits
    #  until it is made; see 'WAIT'. A type checker reads the imports at the
    #  top of the file instead.
    if not TYPE_CHECKING:
      QJsonObject = WAIT['QJsonObject']

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'Qt3DAnimation::Animation::GLTFImporter::Animation'

    #  Qt's '~Qt3DAnimation::Animation::GLTFImporter::Animation()'. Naming it
    #  makes this a value class: Python owns every C++
    #  Qt3DAnimation::Animation::GLTFImporter::Animation behind a cute one,
    #  and removes it by this ritual.
    __delete_ritual__ = (
        'ritual_ZN13Qt3DAnimation9Animation12GLTFImporter9AnimationD1Ev')

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @overload()
    def __init__(self) -> None:
      """
      Notes what was given, for Qt's
      'Qt3DAnimation::Animation::GLTFImporter::Animation::Animation()', which
      is called at the first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qt3danimation-animation-gltfimporter-animation.html
      """
      #  Qt3DAnimation::Animation::GLTFImporter::Animation::Animation()
      self._noteCreation(GLTFImporter.Animation, lambda: Rituals.call(
          'ritual_ZN13Qt3DAnimation9Animation12GLTFImporter9AnimationC1Ev',
      ))

    @overload(QJsonObject)
    def __init__(self, json: QJsonObject) -> None:
      """
      Notes what was given, for Qt's
      'Qt3DAnimation::Animation::GLTFImporter::Animation::Animation(const
      QJsonObject &json)', which is called at the first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qt3danimation-animation-gltfimporter-animation.html

      Parameters
      ----------

      json : QJsonObject
        Passed on as a value: Qt reads the C++ QJsonObject, which stays
        Python's own.
      """
      #  Qt3DAnimation::Animation::GLTFImporter::Animation::Animation(const
      #      QJsonObject &json)
      self._noteCreation(GLTFImporter.Animation, lambda: Rituals.call(
          'ritual_ZN13Qt3DAnimation9Animation12GLTFImporter9AnimationC1ERK1'
          '1QJsonObject',
          self._valueOf(json),
      ))

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  class AnimationNameAndChannels(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's
    Qt3DAnimation::Animation::GLTFImporter::AnimationNameAndChannels: a plain
    Python object standing in front of one C++
    Qt3DAnimation::Animation::GLTFImporter::AnimationNameAndChannels.

    C++ hands a
    Qt3DAnimation::Animation::GLTFImporter::AnimationNameAndChannels around
    as a copy, so every C++
    Qt3DAnimation::Animation::GLTFImporter::AnimationNameAndChannels behind a
    cute one is Python's own: it is removed, by the ritual named in
    '__delete_ritual__', when the cute object goes.

    What exists
    -----------

    No function of Qt's
    Qt3DAnimation::Animation::GLTFImporter::AnimationNameAndChannels yet.
    None can be made from Python: one comes out of a function of another
    class that gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's
      'Qt3DAnimation::Animation::GLTFImporter::AnimationNameAndChannels::
      ~AnimationNameAndChannels()': the destructor: Python removes its C++
      Qt3DAnimation::Animation::GLTFImporter::AnimationNameAndChannels by it,
      and has no other use for it.

    What to expect
    --------------

    - The C++
      Qt3DAnimation::Animation::GLTFImporter::AnimationNameAndChannels is
      created at the first use, not by
      'Qt3DAnimation::Animation::GLTFImporter::AnimationNameAndChannels(
      ...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a
      Qt3DAnimation::Animation::GLTFImporter::AnimationNameAndChannels back
      gives a copy the ritual made for Python, in a new cute
      Qt3DAnimation::Animation::GLTFImporter::AnimationNameAndChannels.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'Qt3DAnimation::Animation::GLTFImporter::AnimationNameAndChannels'

    #  Qt's
    #  '~Qt3DAnimation::Animation::GLTFImporter::AnimationNameAndChannels()'.
    #  Naming it makes this a value class: Python owns every C++
    #  Qt3DAnimation::Animation::GLTFImporter::AnimationNameAndChannels
    #  behind a cute one, and removes it by this ritual.
    __delete_ritual__ = (
        'ritual_ZN13Qt3DAnimation9Animation12GLTFImporter24AnimationNameAndChannelsD1Ev')

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  class BufferData(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's Qt3DAnimation::Animation::GLTFImporter::BufferData:
    a plain Python object standing in front of one C++
    Qt3DAnimation::Animation::GLTFImporter::BufferData.

    C++ hands a Qt3DAnimation::Animation::GLTFImporter::BufferData around as
    a copy, so every C++ Qt3DAnimation::Animation::GLTFImporter::BufferData
    behind a cute one is Python's own: it is removed, by the ritual named in
    '__delete_ritual__', when the cute object goes.

    What exists
    -----------

    No function of Qt's Qt3DAnimation::Animation::GLTFImporter::BufferData
    yet. It can be made from Python, in 2 ways; see '__init__'.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's
      'Qt3DAnimation::Animation::GLTFImporter::BufferData::~BufferData()':
      the destructor: Python removes its C++
      Qt3DAnimation::Animation::GLTFImporter::BufferData by it, and has no
      other use for it.

    What to expect
    --------------

    - The C++ Qt3DAnimation::Animation::GLTFImporter::BufferData is created
      at the first use, not by
      'Qt3DAnimation::Animation::GLTFImporter::BufferData(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a Qt3DAnimation::Animation::GLTFImporter::BufferData
      back gives a copy the ritual made for Python, in a new cute
      Qt3DAnimation::Animation::GLTFImporter::BufferData.
    """

    #  The cute classes this class names and is not built on. Each waits
    #  until it is made; see 'WAIT'. A type checker reads the imports at the
    #  top of the file instead.
    if not TYPE_CHECKING:
      QJsonObject = WAIT['QJsonObject']

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'Qt3DAnimation::Animation::GLTFImporter::BufferData'

    #  Qt's '~Qt3DAnimation::Animation::GLTFImporter::BufferData()'. Naming
    #  it makes this a value class: Python owns every C++
    #  Qt3DAnimation::Animation::GLTFImporter::BufferData behind a cute one,
    #  and removes it by this ritual.
    __delete_ritual__ = (
        'ritual_ZN13Qt3DAnimation9Animation12GLTFImporter10BufferDataD1Ev')

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @overload()
    def __init__(self) -> None:
      """
      Notes what was given, for Qt's
      'Qt3DAnimation::Animation::GLTFImporter::BufferData::BufferData()',
      which is called at the first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qt3danimation-animation-gltfimporter-bufferdata.html
      """
      #  Qt3DAnimation::Animation::GLTFImporter::BufferData::BufferData()
      self._noteCreation(GLTFImporter.BufferData, lambda: Rituals.call(
          'ritual_ZN13Qt3DAnimation9Animation12GLTFImporter10BufferDataC1Ev',
      ))

    @overload(QJsonObject)
    def __init__(self, json: QJsonObject) -> None:
      """
      Notes what was given, for Qt's
      'Qt3DAnimation::Animation::GLTFImporter::BufferData::BufferData(const
      QJsonObject &json)', which is called at the first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qt3danimation-animation-gltfimporter-bufferdata.html

      Parameters
      ----------

      json : QJsonObject
        Passed on as a value: Qt reads the C++ QJsonObject, which stays
        Python's own.
      """
      #  Qt3DAnimation::Animation::GLTFImporter::BufferData::BufferData(const
      #      QJsonObject &json)
      self._noteCreation(GLTFImporter.BufferData, lambda: Rituals.call(
          'ritual_ZN13Qt3DAnimation9Animation12GLTFImporter10BufferDataC1ER'
          'K11QJsonObject',
          self._valueOf(json),
      ))

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  class BufferView(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's Qt3DAnimation::Animation::GLTFImporter::BufferView:
    a plain Python object standing in front of one C++
    Qt3DAnimation::Animation::GLTFImporter::BufferView.

    C++ hands a Qt3DAnimation::Animation::GLTFImporter::BufferView around as
    a copy, so every C++ Qt3DAnimation::Animation::GLTFImporter::BufferView
    behind a cute one is Python's own: it is removed, by the ritual named in
    '__delete_ritual__', when the cute object goes.

    What exists
    -----------

    No function of Qt's Qt3DAnimation::Animation::GLTFImporter::BufferView
    yet. It can be made from Python, in 2 ways; see '__init__'.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's
      'Qt3DAnimation::Animation::GLTFImporter::BufferView::~BufferView()':
      the destructor: Python removes its C++
      Qt3DAnimation::Animation::GLTFImporter::BufferView by it, and has no
      other use for it.

    What to expect
    --------------

    - The C++ Qt3DAnimation::Animation::GLTFImporter::BufferView is created
      at the first use, not by
      'Qt3DAnimation::Animation::GLTFImporter::BufferView(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a Qt3DAnimation::Animation::GLTFImporter::BufferView
      back gives a copy the ritual made for Python, in a new cute
      Qt3DAnimation::Animation::GLTFImporter::BufferView.
    """

    #  The cute classes this class names and is not built on. Each waits
    #  until it is made; see 'WAIT'. A type checker reads the imports at the
    #  top of the file instead.
    if not TYPE_CHECKING:
      QJsonObject = WAIT['QJsonObject']

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'Qt3DAnimation::Animation::GLTFImporter::BufferView'

    #  Qt's '~Qt3DAnimation::Animation::GLTFImporter::BufferView()'. Naming
    #  it makes this a value class: Python owns every C++
    #  Qt3DAnimation::Animation::GLTFImporter::BufferView behind a cute one,
    #  and removes it by this ritual.
    __delete_ritual__ = (
        'ritual_ZN13Qt3DAnimation9Animation12GLTFImporter10BufferViewD1Ev')

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @overload()
    def __init__(self) -> None:
      """
      Notes what was given, for Qt's
      'Qt3DAnimation::Animation::GLTFImporter::BufferView::BufferView()',
      which is called at the first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qt3danimation-animation-gltfimporter-bufferview.html
      """
      #  Qt3DAnimation::Animation::GLTFImporter::BufferView::BufferView()
      self._noteCreation(GLTFImporter.BufferView, lambda: Rituals.call(
          'ritual_ZN13Qt3DAnimation9Animation12GLTFImporter10BufferViewC1Ev',
      ))

    @overload(QJsonObject)
    def __init__(self, json: QJsonObject) -> None:
      """
      Notes what was given, for Qt's
      'Qt3DAnimation::Animation::GLTFImporter::BufferView::BufferView(const
      QJsonObject &json)', which is called at the first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qt3danimation-animation-gltfimporter-bufferview.html

      Parameters
      ----------

      json : QJsonObject
        Passed on as a value: Qt reads the C++ QJsonObject, which stays
        Python's own.
      """
      #  Qt3DAnimation::Animation::GLTFImporter::BufferView::BufferView(const
      #      QJsonObject &json)
      self._noteCreation(GLTFImporter.BufferView, lambda: Rituals.call(
          'ritual_ZN13Qt3DAnimation9Animation12GLTFImporter10BufferViewC1ER'
          'K11QJsonObject',
          self._valueOf(json),
      ))

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  class Channel(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's Qt3DAnimation::Animation::GLTFImporter::Channel: a
    plain Python object standing in front of one C++
    Qt3DAnimation::Animation::GLTFImporter::Channel.

    C++ hands a Qt3DAnimation::Animation::GLTFImporter::Channel around as a
    copy, so every C++ Qt3DAnimation::Animation::GLTFImporter::Channel behind
    a cute one is Python's own: it is removed, by the ritual named in
    '__delete_ritual__', when the cute object goes.

    What exists
    -----------

    No function of Qt's Qt3DAnimation::Animation::GLTFImporter::Channel yet.
    It can be made from Python, in 2 ways; see '__init__'.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'Qt3DAnimation::Animation::GLTFImporter::Channel::~Channel()': the
      destructor: Python removes its C++
      Qt3DAnimation::Animation::GLTFImporter::Channel by it, and has no other
      use for it.

    What to expect
    --------------

    - The C++ Qt3DAnimation::Animation::GLTFImporter::Channel is created at
      the first use, not by
      'Qt3DAnimation::Animation::GLTFImporter::Channel(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a Qt3DAnimation::Animation::GLTFImporter::Channel
      back gives a copy the ritual made for Python, in a new cute
      Qt3DAnimation::Animation::GLTFImporter::Channel.
    """

    #  The cute classes this class names and is not built on. Each waits
    #  until it is made; see 'WAIT'. A type checker reads the imports at the
    #  top of the file instead.
    if not TYPE_CHECKING:
      QJsonObject = WAIT['QJsonObject']

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'Qt3DAnimation::Animation::GLTFImporter::Channel'

    #  Qt's '~Qt3DAnimation::Animation::GLTFImporter::Channel()'. Naming it
    #  makes this a value class: Python owns every C++
    #  Qt3DAnimation::Animation::GLTFImporter::Channel behind a cute one, and
    #  removes it by this ritual.
    __delete_ritual__ = (
        'ritual_ZN13Qt3DAnimation9Animation12GLTFImporter7ChannelD1Ev')

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @overload()
    def __init__(self) -> None:
      """
      Notes what was given, for Qt's
      'Qt3DAnimation::Animation::GLTFImporter::Channel::Channel()', which is
      called at the first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qt3danimation-animation-gltfimporter-channel.html
      """
      #  Qt3DAnimation::Animation::GLTFImporter::Channel::Channel()
      self._noteCreation(GLTFImporter.Channel, lambda: Rituals.call(
          'ritual_ZN13Qt3DAnimation9Animation12GLTFImporter7ChannelC1Ev',
      ))

    @overload(QJsonObject)
    def __init__(self, json: QJsonObject) -> None:
      """
      Notes what was given, for Qt's
      'Qt3DAnimation::Animation::GLTFImporter::Channel::Channel(const
      QJsonObject &json)', which is called at the first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qt3danimation-animation-gltfimporter-channel.html

      Parameters
      ----------

      json : QJsonObject
        Passed on as a value: Qt reads the C++ QJsonObject, which stays
        Python's own.
      """
      #  Qt3DAnimation::Animation::GLTFImporter::Channel::Channel(const
      #      QJsonObject &json)
      self._noteCreation(GLTFImporter.Channel, lambda: Rituals.call(
          'ritual_ZN13Qt3DAnimation9Animation12GLTFImporter7ChannelC1ERK11Q'
          'JsonObject',
          self._valueOf(json),
      ))

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  class Node(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's Qt3DAnimation::Animation::GLTFImporter::Node: a
    plain Python object standing in front of one C++
    Qt3DAnimation::Animation::GLTFImporter::Node.

    C++ hands a Qt3DAnimation::Animation::GLTFImporter::Node around as a
    copy, so every C++ Qt3DAnimation::Animation::GLTFImporter::Node behind a
    cute one is Python's own: it is removed, by the ritual named in
    '__delete_ritual__', when the cute object goes.

    What exists
    -----------

    No function of Qt's Qt3DAnimation::Animation::GLTFImporter::Node yet. It
    can be made from Python, in 1 way; see '__init__'.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'Qt3DAnimation::Animation::GLTFImporter::Node::~Node()': the
      destructor: Python removes its C++
      Qt3DAnimation::Animation::GLTFImporter::Node by it, and has no other
      use for it.

    What has no ritual
    ------------------

    1 of the 3 functions Qt declares: 1 Qt's library has no name for it, and
    its code in Qt's source does not compile apart from its file.

    What to expect
    --------------

    - The C++ Qt3DAnimation::Animation::GLTFImporter::Node is created at the
      first use, not by 'Qt3DAnimation::Animation::GLTFImporter::Node(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a Qt3DAnimation::Animation::GLTFImporter::Node back
      gives a copy the ritual made for Python, in a new cute
      Qt3DAnimation::Animation::GLTFImporter::Node.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'Qt3DAnimation::Animation::GLTFImporter::Node'

    #  Qt's '~Qt3DAnimation::Animation::GLTFImporter::Node()'. Naming it
    #  makes this a value class: Python owns every C++
    #  Qt3DAnimation::Animation::GLTFImporter::Node behind a cute one, and
    #  removes it by this ritual.
    __delete_ritual__ = (
        'ritual_ZN13Qt3DAnimation9Animation12GLTFImporter4NodeD1Ev')

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @overload()
    def __init__(self) -> None:
      """
      Notes what was given, for Qt's
      'Qt3DAnimation::Animation::GLTFImporter::Node::Node()', which is called
      at the first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qt3danimation-animation-gltfimporter-node.html
      """
      #  Qt3DAnimation::Animation::GLTFImporter::Node::Node()
      self._noteCreation(GLTFImporter.Node, lambda: Rituals.call(
          'ritual_ZN13Qt3DAnimation9Animation12GLTFImporter4NodeC1Ev',
      ))

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  class Sampler(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's Qt3DAnimation::Animation::GLTFImporter::Sampler: a
    plain Python object standing in front of one C++
    Qt3DAnimation::Animation::GLTFImporter::Sampler.

    C++ hands a Qt3DAnimation::Animation::GLTFImporter::Sampler around as a
    copy, so every C++ Qt3DAnimation::Animation::GLTFImporter::Sampler behind
    a cute one is Python's own: it is removed, by the ritual named in
    '__delete_ritual__', when the cute object goes.

    What exists
    -----------

    Every function of Qt's Qt3DAnimation::Animation::GLTFImporter::Sampler
    that has a ritual and that Python can call so far, 1 name in all:
    'interpolationModeString'. It can be made from Python, in 2 ways; see
    '__init__'.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'Qt3DAnimation::Animation::GLTFImporter::Sampler::~Sampler()': the
      destructor: Python removes its C++
      Qt3DAnimation::Animation::GLTFImporter::Sampler by it, and has no other
      use for it.

    What to expect
    --------------

    - The C++ Qt3DAnimation::Animation::GLTFImporter::Sampler is created at
      the first use, not by
      'Qt3DAnimation::Animation::GLTFImporter::Sampler(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a Qt3DAnimation::Animation::GLTFImporter::Sampler
      back gives a copy the ritual made for Python, in a new cute
      Qt3DAnimation::Animation::GLTFImporter::Sampler.
    """

    #  The cute classes this class names and is not built on. Each waits
    #  until it is made; see 'WAIT'. A type checker reads the imports at the
    #  top of the file instead.
    if not TYPE_CHECKING:
      QJsonObject = WAIT['QJsonObject']

    #  The enums Qt writes inside
    #  Qt3DAnimation::Animation::GLTFImporter::Sampler, each a class in here
    #  as in C++, and the names Qt has for the combinations of its flags
    #  enums.

    class InterpolationMode(CuteNum):
      """
      The enum
      'Qt3DAnimation::Animation::GLTFImporter::Sampler::InterpolationMode' of
      Qt, with the 4 names Qt gives in it.
      """

      Linear = Kee[int](0)
      Step = Kee[int](1)
      CatmullRomSpline = Kee[int](2)
      CubicSpline = Kee[int](3)

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'Qt3DAnimation::Animation::GLTFImporter::Sampler'

    #  Qt's '~Qt3DAnimation::Animation::GLTFImporter::Sampler()'. Naming it
    #  makes this a value class: Python owns every C++
    #  Qt3DAnimation::Animation::GLTFImporter::Sampler behind a cute one, and
    #  removes it by this ritual.
    __delete_ritual__ = (
        'ritual_ZN13Qt3DAnimation9Animation12GLTFImporter7SamplerD1Ev')

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    def interpolationModeString(self) -> str:
      """
      Calls Qt's 'QString Qt3DAnimation::Animation::GLTFImporter::Sampler::
      interpolationModeString() const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qt3danimation-animation-gltfimporter-sampler.html

      Returns
      -------

      str
        The text Qt gave back.
      """
      #  QString Qt3DAnimation::Animation::GLTFImporter::Sampler::
      #      interpolationModeString() const
      return self.uglySide.call(
          'ritual_ZNK13Qt3DAnimation9Animation12GLTFImporter7Sampler23inter'
          'polationModeStringEv',
      )

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @overload()
    def __init__(self) -> None:
      """
      Notes what was given, for Qt's
      'Qt3DAnimation::Animation::GLTFImporter::Sampler::Sampler()', which is
      called at the first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qt3danimation-animation-gltfimporter-sampler.html
      """
      #  Qt3DAnimation::Animation::GLTFImporter::Sampler::Sampler()
      self._noteCreation(GLTFImporter.Sampler, lambda: Rituals.call(
          'ritual_ZN13Qt3DAnimation9Animation12GLTFImporter7SamplerC1Ev',
      ))

    @overload(QJsonObject)
    def __init__(self, json: QJsonObject) -> None:
      """
      Notes what was given, for Qt's
      'Qt3DAnimation::Animation::GLTFImporter::Sampler::Sampler(const
      QJsonObject &json)', which is called at the first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qt3danimation-animation-gltfimporter-sampler.html

      Parameters
      ----------

      json : QJsonObject
        Passed on as a value: Qt reads the C++ QJsonObject, which stays
        Python's own.
      """
      #  Qt3DAnimation::Animation::GLTFImporter::Sampler::Sampler(const
      #      QJsonObject &json)
      self._noteCreation(GLTFImporter.Sampler, lambda: Rituals.call(
          'ritual_ZN13Qt3DAnimation9Animation12GLTFImporter7SamplerC1ERK11Q'
          'JsonObject',
          self._valueOf(json),
      ))

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  class Skin(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's Qt3DAnimation::Animation::GLTFImporter::Skin: a
    plain Python object standing in front of one C++
    Qt3DAnimation::Animation::GLTFImporter::Skin.

    C++ hands a Qt3DAnimation::Animation::GLTFImporter::Skin around as a
    copy, so every C++ Qt3DAnimation::Animation::GLTFImporter::Skin behind a
    cute one is Python's own: it is removed, by the ritual named in
    '__delete_ritual__', when the cute object goes.

    What exists
    -----------

    No function of Qt's Qt3DAnimation::Animation::GLTFImporter::Skin yet. It
    can be made from Python, in 2 ways; see '__init__'.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'Qt3DAnimation::Animation::GLTFImporter::Skin::~Skin()': the
      destructor: Python removes its C++
      Qt3DAnimation::Animation::GLTFImporter::Skin by it, and has no other
      use for it.

    What to expect
    --------------

    - The C++ Qt3DAnimation::Animation::GLTFImporter::Skin is created at the
      first use, not by 'Qt3DAnimation::Animation::GLTFImporter::Skin(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a Qt3DAnimation::Animation::GLTFImporter::Skin back
      gives a copy the ritual made for Python, in a new cute
      Qt3DAnimation::Animation::GLTFImporter::Skin.
    """

    #  The cute classes this class names and is not built on. Each waits
    #  until it is made; see 'WAIT'. A type checker reads the imports at the
    #  top of the file instead.
    if not TYPE_CHECKING:
      QJsonObject = WAIT['QJsonObject']

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'Qt3DAnimation::Animation::GLTFImporter::Skin'

    #  Qt's '~Qt3DAnimation::Animation::GLTFImporter::Skin()'. Naming it
    #  makes this a value class: Python owns every C++
    #  Qt3DAnimation::Animation::GLTFImporter::Skin behind a cute one, and
    #  removes it by this ritual.
    __delete_ritual__ = (
        'ritual_ZN13Qt3DAnimation9Animation12GLTFImporter4SkinD1Ev')

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @overload()
    def __init__(self) -> None:
      """
      Notes what was given, for Qt's
      'Qt3DAnimation::Animation::GLTFImporter::Skin::Skin()', which is called
      at the first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qt3danimation-animation-gltfimporter-skin.html
      """
      #  Qt3DAnimation::Animation::GLTFImporter::Skin::Skin()
      self._noteCreation(GLTFImporter.Skin, lambda: Rituals.call(
          'ritual_ZN13Qt3DAnimation9Animation12GLTFImporter4SkinC1Ev',
      ))

    @overload(QJsonObject)
    def __init__(self, json: QJsonObject) -> None:
      """
      Notes what was given, for Qt's
      'Qt3DAnimation::Animation::GLTFImporter::Skin::Skin(const QJsonObject
      &json)', which is called at the first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qt3danimation-animation-gltfimporter-skin.html

      Parameters
      ----------

      json : QJsonObject
        Passed on as a value: Qt reads the C++ QJsonObject, which stays
        Python's own.
      """
      #  Qt3DAnimation::Animation::GLTFImporter::Skin::Skin(const QJsonObject
      #      &json)
      self._noteCreation(GLTFImporter.Skin, lambda: Rituals.call(
          'ritual_ZN13Qt3DAnimation9Animation12GLTFImporter4SkinC1ERK11QJso'
          'nObject',
          self._valueOf(json),
      ))

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(int)
  def accessorTypeFromJSON(
      componentType: int,
  ) -> Qt3DCore.QAttribute.VertexBaseType:
    """
    Calls Qt's 'Qt3DCore::QAttribute::VertexBaseType
    Qt3DAnimation::Animation::GLTFImporter::accessorTypeFromJSON(int
    componentType)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-animation-gltfimporter.html

    Parameters
    ----------

    componentType : int
      Passed on as it is.

    Returns
    -------

    Qt3DCore.QAttribute.VertexBaseType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'Qt3DCore.QAttribute.VertexBaseType(number)' gives.
    """
    #  Qt3DCore::QAttribute::VertexBaseType
    #      Qt3DAnimation::Animation::GLTFImporter::accessorTypeFromJSON(int
    #      componentType)
    return Qt3DCore.QAttribute.VertexBaseType(Rituals.call(
        'ritual_ZN13Qt3DAnimation9Animation12GLTFImporter20accessorTypeFrom'
        'JSONEi',
        componentType,
    ))

  @staticmethod
  @overload(Qt3DCore.QAttribute.VertexBaseType)
  def accessorTypeSize(
      componentType: Qt3DCore.QAttribute.VertexBaseType,
  ) -> int:
    """
    Calls Qt's 'uint
    Qt3DAnimation::Animation::GLTFImporter::accessorTypeSize(Qt3DCore::
    QAttribute::VertexBaseType componentType)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-animation-gltfimporter.html

    Parameters
    ----------

    componentType : Qt3DCore.QAttribute.VertexBaseType
      Passed on as its number.
    """
    #  uint Qt3DAnimation::Animation::GLTFImporter::accessorTypeSize(
    #      Qt3DCore::QAttribute::VertexBaseType componentType)
    return Rituals.call(
        'ritual_ZN13Qt3DAnimation9Animation12GLTFImporter16accessorTypeSize'
        'EN8Qt3DCore10QAttribute14VertexBaseTypeE',
        componentType.value,
    )

  @staticmethod
  @overload(str)
  def accessorDataSizeFromJson(type: str) -> int:
    """
    Calls Qt's 'uint
    Qt3DAnimation::Animation::GLTFImporter::accessorDataSizeFromJson(const
    QString &type)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-animation-gltfimporter.html

    Parameters
    ----------

    type : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  uint Qt3DAnimation::Animation::GLTFImporter::accessorDataSizeFromJson(
    #      const QString &type)
    return Rituals.call(
        'ritual_ZN13Qt3DAnimation9Animation12GLTFImporter24accessorDataSize'
        'FromJsonERK7QString',
        type,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DAnimation::Animation::GLTFImporter'

  #  Qt's '~Qt3DAnimation::Animation::GLTFImporter()'. Naming it makes this a
  #  value class: Python owns every C++
  #  Qt3DAnimation::Animation::GLTFImporter behind a cute one, and removes it
  #  by this ritual.
  __delete_ritual__ = 'ritual_ZN13Qt3DAnimation9Animation12GLTFImporterD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  @overload(int, str)
  def createAnimationData(
      self,
      animationIndex: int,
      animationName: str = '',
  ) -> AnimationNameAndChannels:
    """
    Calls Qt's 'AnimationNameAndChannels
    Qt3DAnimation::Animation::GLTFImporter::createAnimationData(qsizetype
    animationIndex, const QString &animationName) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-animation-gltfimporter.html

    Parameters
    ----------

    animationIndex : int
      Passed on as it is.

    animationName : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.

    Returns
    -------

    AnimationNameAndChannels
      A new cute
      Qt3DAnimation::Animation::GLTFImporter::AnimationNameAndChannels around
      the copy Qt gave back. Python owns it.
    """
    #  AnimationNameAndChannels
    #      Qt3DAnimation::Animation::GLTFImporter::createAnimationData(
    #      qsizetype animationIndex, const QString &animationName) const
    address = self.uglySide.call(
        'ritual_ZNK13Qt3DAnimation9Animation12GLTFImporter19createAnimation'
        'DataExRK7QString',
        animationIndex, animationName,
    )
    return Qt3DAnimation.Animation.GLTFImporter.AnimationNameAndChannels._cuteOwning(address)

  @overload(str)
  def resolveLocalData(self, path: str) -> QByteArray:
    """
    Calls Qt's 'QByteArray
    Qt3DAnimation::Animation::GLTFImporter::resolveLocalData(const QString
    &path) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-animation-gltfimporter.html

    Parameters
    ----------

    path : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray
    #      Qt3DAnimation::Animation::GLTFImporter::resolveLocalData(const
    #      QString &path) const
    address = self.uglySide.call(
        'ritual_ZNK13Qt3DAnimation9Animation12GLTFImporter16resolveLocalDat'
        'aERK7QString',
        path,
    )
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setBasePath(self, path: str) -> None:
    """
    Calls Qt's 'void
    Qt3DAnimation::Animation::GLTFImporter::setBasePath(const QString
    &path)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-animation-gltfimporter.html

    Parameters
    ----------

    path : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void Qt3DAnimation::Animation::GLTFImporter::setBasePath(const QString
    #      &path)
    self.uglySide.call(
        'ritual_ZN13Qt3DAnimation9Animation12GLTFImporter11setBasePathERK7Q'
        'String',
        path,
    )

  @overload(QJsonDocument)
  def setJSON(self, json: QJsonDocument) -> bool:
    """
    Calls Qt's 'bool Qt3DAnimation::Animation::GLTFImporter::setJSON(const
    QJsonDocument &json)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-animation-gltfimporter.html#setJSON

    Parameters
    ----------

    json : QJsonDocument
      Passed on as a value: Qt reads the C++ QJsonDocument, which stays
      Python's own.
    """
    #  bool Qt3DAnimation::Animation::GLTFImporter::setJSON(const
    #      QJsonDocument &json)
    return self.uglySide.call(
        'ritual_ZN13Qt3DAnimation9Animation12GLTFImporter7setJSONERK13QJson'
        'Document',
        self._valueOf(json),
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
    Notes what was given, for Qt's
    'Qt3DAnimation::Animation::GLTFImporter::GLTFImporter()', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-animation-gltfimporter.html
    """
    #  Qt3DAnimation::Animation::GLTFImporter::GLTFImporter()
    self._noteCreation(GLTFImporter, lambda: Rituals.call(
        'ritual_ZN13Qt3DAnimation9Animation12GLTFImporterC1Ev',
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

  def cleanup(self) -> None:
    """
    Calls Qt's 'void Qt3DAnimation::Animation::GLTFImporter::cleanup()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-animation-gltfimporter.html#cleanup
    """
    #  void Qt3DAnimation::Animation::GLTFImporter::cleanup()
    self.uglySide.call(
        'ritual_ZN13Qt3DAnimation9Animation12GLTFImporter7cleanupEv',
    )

  @overload(QJsonObject)
  def processJSONBuffer(self, json: QJsonObject) -> bool:
    """
    Calls Qt's 'bool
    Qt3DAnimation::Animation::GLTFImporter::processJSONBuffer(const
    QJsonObject &json)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-animation-gltfimporter.html

    Parameters
    ----------

    json : QJsonObject
      Passed on as a value: Qt reads the C++ QJsonObject, which stays
      Python's own.
    """
    #  bool Qt3DAnimation::Animation::GLTFImporter::processJSONBuffer(const
    #      QJsonObject &json)
    return self.uglySide.call(
        'ritual_ZN13Qt3DAnimation9Animation12GLTFImporter17processJSONBuffe'
        'rERK11QJsonObject',
        self._valueOf(json),
    )

  def setupNodeParentLinks(self) -> None:
    """
    Calls Qt's 'void
    Qt3DAnimation::Animation::GLTFImporter::setupNodeParentLinks()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-animation-gltfimporter.html
    """
    #  void Qt3DAnimation::Animation::GLTFImporter::setupNodeParentLinks()
    self.uglySide.call(
        'ritual_ZN13Qt3DAnimation9Animation12GLTFImporter20setupNodeParentL'
        'inksEv',
    )

  @staticmethod
  def accessorData(*__, **_) -> Never:
    """
    Qt's 'RawData Qt3DAnimation::Animation::GLTFImporter::accessorData(int
    accessorIndex, int index) const': gives a type Python has no way to take
    yet.
    """
    raise NotImplementedError(
        "'Qt3DAnimation.Animation.GLTFImporter.accessorData' has no cute "
        "function yet. Qt's 'RawData "
        "Qt3DAnimation::Animation::GLTFImporter::accessorData(int "
        "accessorIndex, int index) const': gives a type Python has no way "
        "to take yet.")

  @staticmethod
  def animations(*__, **_) -> Never:
    """
    Qt's 'const QList<Animation>
    Qt3DAnimation::Animation::GLTFImporter::animations() const': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'Qt3DAnimation.Animation.GLTFImporter.animations' has no cute "
        "function yet. Qt's 'const QList<Animation> "
        "Qt3DAnimation::Animation::GLTFImporter::animations() const': gives "
        "a type Python has no way to take yet.")

  @staticmethod
  def createNodeIndexToJointIndexMap(*__, **_) -> Never:
    """
    Qt's 'QHash<qsizetype, qsizetype>
    Qt3DAnimation::Animation::GLTFImporter::createNodeIndexToJointIndexMap(
    const Skin &skin) const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'Qt3DAnimation.Animation.GLTFImporter.createNodeIndexToJointIndexMa"
        "p' has no cute function yet. Qt's 'QHash<qsizetype, qsizetype> "
        "Qt3DAnimation::Animation::GLTFImporter::createNodeIndexToJointIndex"
        "Map(const Skin &skin) const': gives a type Python has no way to "
        "take yet.")

  @staticmethod
  def load(*__, **_) -> Never:
    """
    Qt's 'bool Qt3DAnimation::Animation::GLTFImporter::load(QIODevice
    *ioDev)': leans on
    'Qt3DAnimation::Animation::GLTFImporter::BufferView::BufferView(
    QJsonObject const&)', which Qt's source does not mark for use from
    outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'Qt3DAnimation.Animation.GLTFImporter.load' has no cute function "
        "yet. Qt's 'bool "
        "Qt3DAnimation::Animation::GLTFImporter::load(QIODevice *ioDev)': "
        "leans on "
        "'Qt3DAnimation::Animation::GLTFImporter::BufferView::BufferView(QJs"
        "onObject const&)', which Qt's source does not mark for use from "
        "outside Qt and has no code for that could be taken.")

  @staticmethod
  def parse(*__, **_) -> Never:
    """
    Qt's 'bool Qt3DAnimation::Animation::GLTFImporter::parse()': leans on
    'Qt3DAnimation::Animation::GLTFImporter::BufferView::BufferView(
    QJsonObject const&)', which Qt's source does not mark for use from
    outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'Qt3DAnimation.Animation.GLTFImporter.parse' has no cute function "
        "yet. Qt's 'bool Qt3DAnimation::Animation::GLTFImporter::parse()': "
        "leans on "
        "'Qt3DAnimation::Animation::GLTFImporter::BufferView::BufferView(QJs"
        "onObject const&)', which Qt's source does not mark for use from "
        "outside Qt and has no code for that could be taken.")

  @staticmethod
  def parseGLTF2(*__, **_) -> Never:
    """
    Qt's 'bool Qt3DAnimation::Animation::GLTFImporter::parseGLTF2()': leans
    on 'Qt3DAnimation::Animation::GLTFImporter::BufferView::BufferView(
    QJsonObject const&)', which Qt's source does not mark for use from
    outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'Qt3DAnimation.Animation.GLTFImporter.parseGLTF2' has no cute "
        "function yet. Qt's 'bool "
        "Qt3DAnimation::Animation::GLTFImporter::parseGLTF2()': leans on "
        "'Qt3DAnimation::Animation::GLTFImporter::BufferView::BufferView(QJs"
        "onObject const&)', which Qt's source does not mark for use from "
        "outside Qt and has no code for that could be taken.")

  @staticmethod
  def processJSONAccessor(*__, **_) -> Never:
    """
    Qt's 'bool
    Qt3DAnimation::Animation::GLTFImporter::processJSONAccessor(const
    QJsonObject &json)': leans on
    'Qt3DAnimation::Animation::GLTFImporter::AccessorData::AccessorData(
    QJsonObject const&)', which Qt's source does not mark for use from
    outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'Qt3DAnimation.Animation.GLTFImporter.processJSONAccessor' has no "
        "cute function yet. Qt's 'bool "
        "Qt3DAnimation::Animation::GLTFImporter::processJSONAccessor(const "
        "QJsonObject &json)': leans on "
        "'Qt3DAnimation::Animation::GLTFImporter::AccessorData::AccessorData"
        "(QJsonObject const&)', which Qt's source does not mark for use "
        "from outside Qt and has no code for that could be taken.")

  @staticmethod
  def processJSONAnimation(*__, **_) -> Never:
    """
    Qt's 'bool
    Qt3DAnimation::Animation::GLTFImporter::processJSONAnimation(const
    QJsonObject &json)': leans on
    'Qt3DAnimation::Animation::GLTFImporter::Animation::Animation(QJsonObject
    const&)', which Qt's source does not mark for use from outside Qt and has
    no code for that could be taken.
    """
    raise NotImplementedError(
        "'Qt3DAnimation.Animation.GLTFImporter.processJSONAnimation' has no "
        "cute function yet. Qt's 'bool "
        "Qt3DAnimation::Animation::GLTFImporter::processJSONAnimation(const "
        "QJsonObject &json)': leans on "
        "'Qt3DAnimation::Animation::GLTFImporter::Animation::Animation(QJson"
        "Object const&)', which Qt's source does not mark for use from "
        "outside Qt and has no code for that could be taken.")

  @staticmethod
  def processJSONBufferView(*__, **_) -> Never:
    """
    Qt's 'bool
    Qt3DAnimation::Animation::GLTFImporter::processJSONBufferView(const
    QJsonObject &json)': leans on
    'Qt3DAnimation::Animation::GLTFImporter::BufferView::BufferView(
    QJsonObject const&)', which Qt's source does not mark for use from
    outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'Qt3DAnimation.Animation.GLTFImporter.processJSONBufferView' has "
        "no cute function yet. Qt's 'bool "
        "Qt3DAnimation::Animation::GLTFImporter::processJSONBufferView(const"
        " QJsonObject &json)': leans on "
        "'Qt3DAnimation::Animation::GLTFImporter::BufferView::BufferView(QJs"
        "onObject const&)', which Qt's source does not mark for use from "
        "outside Qt and has no code for that could be taken.")

  @staticmethod
  def processJSONNode(*__, **_) -> Never:
    """
    Qt's 'bool Qt3DAnimation::Animation::GLTFImporter::processJSONNode(const
    QJsonObject &json)': leans on
    'Qt3DAnimation::Animation::GLTFImporter::Node::Node(QJsonObject const&)',
    which Qt's source does not mark for use from outside Qt and has no code
    for that could be taken.
    """
    raise NotImplementedError(
        "'Qt3DAnimation.Animation.GLTFImporter.processJSONNode' has no cute "
        "function yet. Qt's 'bool "
        "Qt3DAnimation::Animation::GLTFImporter::processJSONNode(const "
        "QJsonObject &json)': leans on "
        "'Qt3DAnimation::Animation::GLTFImporter::Node::Node(QJsonObject "
        "const&)', which Qt's source does not mark for use from outside Qt "
        "and has no code for that could be taken.")

  @staticmethod
  def processJSONSkin(*__, **_) -> Never:
    """
    Qt's 'bool Qt3DAnimation::Animation::GLTFImporter::processJSONSkin(const
    QJsonObject &json)': leans on
    'Qt3DAnimation::Animation::GLTFImporter::Skin::Skin(QJsonObject const&)',
    which Qt's source does not mark for use from outside Qt and has no code
    for that could be taken.
    """
    raise NotImplementedError(
        "'Qt3DAnimation.Animation.GLTFImporter.processJSONSkin' has no cute "
        "function yet. Qt's 'bool "
        "Qt3DAnimation::Animation::GLTFImporter::processJSONSkin(const "
        "QJsonObject &json)': leans on "
        "'Qt3DAnimation::Animation::GLTFImporter::Skin::Skin(QJsonObject "
        "const&)', which Qt's source does not mark for use from outside Qt "
        "and has no code for that could be taken.")
