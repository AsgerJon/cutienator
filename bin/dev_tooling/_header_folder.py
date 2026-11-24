"""HeaderFolder makes, from Qt's source alone, the folder in which the
compiler finds Qt's header files."""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

import multiprocessing
import os
import re
import shutil
from concurrent.futures import ProcessPoolExecutor
from typing import TYPE_CHECKING

from worktoy.waitaminute import MissingVariable, TypeException

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Any, Dict, List, Optional, Set, Tuple


class HeaderFolder:
  """
  Makes, from Qt's source alone, the folder in which the compiler finds
  Qt's header files. No Qt that is installed anywhere is asked anything.

    headerFolder = HeaderFolder()
    headerFolder.setSourceFolder('/here/qt-everywhere-src-6.12.0/qtbase')
    headerFolder.setFolder('/some/folder/headers')
    headerFolder.make()
    headerFolder.getFolder()       # '/some/folder/headers'
    headerFolder.getQtVersion()    # '6.12.0'

  Why it is needed
  ----------------

  Qt's header files pull each other in by names such as
  'QtCore/qstring.h'. In Qt's source that file lies at
  'src/corelib/text/qstring.h', so the compiler cannot find it by the
  name it is asked for. And every header file asks which parts of Qt
  are in, as '#if QT_CONFIG(tooltip)', which no file of the source
  answers. When Qt itself is built, its build makes a folder that mends
  both. This class makes such a folder too, and it is laid out the way
  the header folder of an installed Qt is, so that what reads the one
  can read the other.

  Terms
  -----

  - Qt's source is what Qt is built from, as Qt's makers give it out.
    It is the same for every system.
  - A part of Qt is one of the pieces Qt comes in: QtCore, QtGui,
    QtWidgets, QtDBus, and the others of the folder 'qtbase': QtNetwork,
    QtSql, QtXml, QtPrintSupport, QtOpenGL, QtOpenGLWidgets and
    QtConcurrent; and of the folders beside it QtSvg, QtSvgWidgets,
    QtWebSockets, QtNetworkAuth, QtCharts, QtCore5Compat, QtWebChannel,
    QtPositioning, QtTextToSpeech, QtBluetooth, QtNfc, QtHttpServer,
    QtMultimedia, QtMultimediaWidgets, QtQml, QtQmlIntegration,
    QtQmlMeta, QtQmlModels, QtQmlWorkerScript, QtQuick and
    QtQuickWidgets. QtDBus was here first
    because header files of QtGui pull its header files in.
  - A pointer is an entry of the folder that stands for a file of the
    source: a symbolic link. No header file is copied.
  - A switch names something a build of Qt may leave in or out, as
    'tooltip'. Qt's source names them all in its 'configure.cmake'
    files. A list of switches is a header file that says of each
    whether it is in.

  You provide
  -----------

  - 'setSourceFolder': the folder 'qtbase' of Qt's source.
  - 'setFolder': where the folder is to be made. It is made anew by
    'make', so it must be a folder of its own.

  What to expect
  --------------

  - 'make' fills the folder with, for each part: a pointer to every
    header file of the part, under the name and in the folder an
    installed Qt has it; one small file for each class, named as the
    class, that pulls in the header file of that class; the file named
    as the part, which pulls in every header file meant for direct
    use on every system; and the lists of switches.
  - In the lists every switch is in, so that the compiler skips
    nothing Qt can have. The few that name the shape of a build, and
    contradict another switch when both are in, are out: see
    'getLeftOutSwitches'.
  - The compiler still reads as the system it runs on. A line Qt
    writes for another system alone stays unread.
  - Header files that Qt's build makes by running a program, as
    'qvulkanfunctions.h', are not in the folder. A header file pulling
    one in is refused by the compiler, which says so.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  Each part of Qt the folder is made for, in the order made: its
  #  name; where it lies in Qt's source, from the folder 'qtbase'; the
  #  header file of the part that brings in its list of switches; the
  #  one in its folder 'private' that brings in the switches Qt keeps to
  #  itself, '' for a part with none; and the parts it is built on, as
  #  its file '...Depends' pulls them in. The word Qt's build makes of
  #  the name, as 'CORE' in 'Q_CORE_EXPORT', is the name without 'Qt',
  #  in capitals. A part with no header file of the first kind, as
  #  QtQmlMeta, has its file of words for export there, which this
  #  folder writes as Qt's build does.
  __parts__ = (
      ('QtCore', 'src/corelib', 'qglobal.h', 'qglobal_p.h', ()),
      ('QtGui', 'src/gui', 'qtguiglobal.h', 'qtguiglobal_p.h', ('QtCore',)),
      ('QtWidgets', 'src/widgets',
       'qtwidgetsglobal.h', 'qtwidgetsglobal_p.h',
       ('QtCore', 'QtGui')),
      ('QtDBus', 'src/dbus',
       'qtdbusglobal.h', 'qtdbusglobal_p.h',
       ('QtCore',)),
      ('QtNetwork', 'src/network',
       'qtnetworkglobal.h', 'qtnetworkglobal_p.h',
       ('QtCore',)),
      ('QtSql', 'src/sql', 'qtsqlglobal.h', 'qtsqlglobal_p.h', ('QtCore',)),
      ('QtXml', 'src/xml', 'qtxmlglobal.h', '', ('QtCore',)),
      ('QtPrintSupport', 'src/printsupport',
       'qtprintsupportglobal.h', 'qtprintsupportglobal_p.h',
       ('QtCore', 'QtGui', 'QtWidgets')),
      ('QtOpenGL', 'src/opengl',
       'qtopenglglobal.h', '',
       ('QtCore', 'QtGui')),
      ('QtOpenGLWidgets', 'src/openglwidgets',
       'qtopenglwidgetsglobal.h', '',
       ('QtOpenGL', 'QtWidgets')),
      ('QtConcurrent', 'src/concurrent',
       'qtconcurrent_global.h', '',
       ('QtCore',)),
      ('QtSvg', '../qtsvg/src/svg',
       'qtsvgglobal.h', 'qtsvgglobal_p.h',
       ('QtCore', 'QtGui')),
      ('QtSvgWidgets', '../qtsvg/src/svgwidgets',
       'qtsvgwidgetsglobal.h', '',
       ('QtCore', 'QtGui', 'QtSvg', 'QtWidgets')),
      ('QtWebSockets', '../qtwebsockets/src/websockets',
       'qwebsockets_global.h', '',
       ('QtCore', 'QtNetwork')),
      ('QtNetworkAuth', '../qtnetworkauth/src/oauth',
       'qoauthglobal.h', '',
       ('QtCore', 'QtNetwork')),
      ('QtCharts', '../qtcharts/src/charts',
       'qchartglobal.h', 'qchartglobal_p.h',
       ('QtCore', 'QtGui', 'QtWidgets')),
      ('QtCore5Compat', '../qt5compat/src/core5',
       'qcore5global.h', '',
       ('QtCore',)),
      ('QtWebChannel', '../qtwebchannel/src/webchannel',
       'qwebchannelglobal.h', '',
       ('QtCore',)),
      ('QtPositioning', '../qtpositioning/src/positioning',
       'qpositioningglobal.h', 'qpositioningglobal_p.h',
       ('QtCore',)),
      ('QtTextToSpeech', '../qtspeech/src/tts',
       'qtexttospeech_global.h', '',
       ('QtCore', 'QtMultimedia')),
      ('QtBluetooth', '../qtconnectivity/src/bluetooth',
       'qtbluetoothglobal.h', 'qtbluetoothglobal_p.h',
       ('QtCore', 'QtNetwork')),
      ('QtNfc', '../qtconnectivity/src/nfc',
       'qtnfcglobal.h', 'qtnfcglobal_p.h',
       ('QtCore',)),
      ('QtHttpServer', '../qthttpserver/src/httpserver',
       'qthttpserverglobal.h', '',
       ('QtCore', 'QtNetwork')),
      ('QtMultimedia', '../qtmultimedia/src/multimedia',
       'qtmultimediaglobal.h', 'qtmultimediaglobal_p.h',
       ('QtCore', 'QtGui')),
      ('QtMultimediaWidgets', '../qtmultimedia/src/multimediawidgets',
       'qtmultimediawidgetsglobal.h', '',
       ('QtCore', 'QtGui', 'QtMultimedia', 'QtWidgets')),
      ('QtQml', '../qtdeclarative/src/qml',
       'qtqmlglobal.h', 'qtqmlglobal_p.h',
       ('QtCore', 'QtQmlIntegration')),
      ('QtQmlIntegration', '../qtdeclarative/src/qmlintegration',
       'qqmlintegration.h', '',
       ()),
      ('QtQmlMeta', '../qtdeclarative/src/qmlmeta',
       'qtqmlmetaexports.h', '',
       ('QtCore', 'QtQml')),
      ('QtQmlModels', '../qtdeclarative/src/qmlmodels',
       'qtqmlmodelsglobal.h', 'qtqmlmodelsglobal_p.h',
       ('QtCore', 'QtQml')),
      ('QtQmlWorkerScript', '../qtdeclarative/src/qmlworkerscript',
       'qtqmlworkerscriptglobal.h', 'qtqmlworkerscriptglobal_p.h',
       ('QtCore', 'QtQml')),
      ('QtQuick', '../qtdeclarative/src/quick',
       'qtquickglobal.h', 'qtquickglobal_p.h',
       ('QtCore', 'QtGui', 'QtQml')),
      ('QtQuickWidgets', '../qtdeclarative/src/quickwidgets',
       'qtquickwidgetsglobal.h', '',
       ('QtCore', 'QtGui', 'QtQml', 'QtQuick', 'QtWidgets')),
      ('QtQmlCore', '../qtdeclarative/src/core',
       'qtqmlcoreexports.h', 'qqmlcoreglobal_p.h',
       ('QtCore', 'QtQml')),
      ('QtQuickEffects', '../qtdeclarative/src/effects',
       'qtquickeffectsexports.h', 'qtquickeffectsglobal_p.h',
       ('QtCore', 'QtGui', 'QtQml', 'QtQuick')),
      ('QtLabsAnimation', '../qtdeclarative/src/labs/animation',
       'qtlabsanimationexports.h', 'qqmlanimationglobal_p.h',
       ()),
      ('QtLabsQmlModels', '../qtdeclarative/src/labs/models',
       'qtlabsqmlmodelsexports.h', 'qqmlmodelsglobal_p.h',
       ()),
      ('QtLabsPlatform', '../qtdeclarative/src/labs/platform',
       'qtlabsplatformexports.h', '',
       ()),
      ('QtLabsStyleKit', '../qtdeclarative/src/labs/stylekit',
       'qtlabsstylekitexports.h', 'qqstylekitglobal_p.h',
       ('QtWidgets',)),
      ('QtLabsStyleKitImpl', '../qtdeclarative/src/labs/stylekit/impl',
       'qtlabsstylekitimplexports.h', '',
       ()),
      ('QtLabsSynchronizer', '../qtdeclarative/src/labs/synchronizer',
       'qtlabssynchronizerexports.h', '',
       ('QtCore',)),
      ('QtQuickParticles', '../qtdeclarative/src/particles',
       'qtquickparticlesexports.h', 'qtquickparticlesglobal_p.h',
       ('QtQuick',)),
      ('QtQmlCompiler', '../qtdeclarative/src/qmlcompiler',
       'qtqmlcompilerexports.h', '',
       ('QtCore', 'QtQml')),
      ('QtQmlDesignSupport', '../qtdeclarative/src/qmldesignsupport',
       'qtqmldesignsupportexports.h', '',
       ('QtCore', 'QtQml')),
      ('QtQmlNetwork', '../qtdeclarative/src/qmlnetwork',
       'qtqmlnetworkexports.h', '',
       ('QtCore', 'QtNetwork', 'QtQml')),
      ('QtQmlXmlListModel', '../qtdeclarative/src/qmlxmllistmodel',
       'qtqmlxmllistmodelexports.h', 'qtqmlxmllistmodelglobal_p.h',
       ('QtCore', 'QtQml')),
      ('QtQuickControls2', '../qtdeclarative/src/quickcontrols',
       'qtquickcontrols2global.h', '',
       ('QtCore', 'QtGui', 'QtQuick')),
      ('QtQuickControls2Basic', '../qtdeclarative/src/quickcontrols/basic',
       'qtquickcontrols2basicexports.h', '',
       ()),
      ('QtQuickControls2BasicStyleImpl',
       '../qtdeclarative/src/quickcontrols/basic/impl',
       'qtquickcontrols2basicstyleimplexports.h', '',
       ()),
      ('QtQuickControls2FluentWinUI3',
       '../qtdeclarative/src/quickcontrols/fluentwinui3',
       'qtquickcontrols2fluentwinui3exports.h', '',
       ()),
      ('QtQuickControls2FluentWinUI3StyleImpl',
       '../qtdeclarative/src/quickcontrols/fluentwinui3/impl',
       'qtquickcontrols2fluentwinui3styleimplexports.h',
       'qquickfluentwinui3styleimplglobal_p.h',
       ()),
      ('QtQuickControls2Fusion', '../qtdeclarative/src/quickcontrols/fusion',
       'qtquickcontrols2fusionexports.h', '',
       ()),
      ('QtQuickControls2FusionStyleImpl',
       '../qtdeclarative/src/quickcontrols/fusion/impl',
       'qtquickcontrols2fusionstyleimplexports.h', '',
       ()),
      ('QtQuickControls2Imagine',
       '../qtdeclarative/src/quickcontrols/imagine',
       'qtquickcontrols2imagineexports.h', '',
       ()),
      ('QtQuickControls2Material',
       '../qtdeclarative/src/quickcontrols/material',
       'qtquickcontrols2materialexports.h', '',
       ()),
      ('QtQuickControls2MaterialStyleImpl',
       '../qtdeclarative/src/quickcontrols/material/impl',
       'qtquickcontrols2materialstyleimplexports.h', '',
       ()),
      ('QtQuickControls2Universal',
       '../qtdeclarative/src/quickcontrols/universal',
       'qtquickcontrols2universalexports.h', '',
       ()),
      ('QtQuickControls2UniversalStyleImpl',
       '../qtdeclarative/src/quickcontrols/universal/impl',
       'qtquickcontrols2universalstyleimplexports.h', '',
       ()),
      ('QtQuickControls2Impl', '../qtdeclarative/src/quickcontrolsimpl',
       'qtquickcontrols2implexports.h', 'qtquickcontrols2implglobal_p.h',
       ('QtCore', 'QtGui', 'QtQuick')),
      ('QtQuickDialogs2', '../qtdeclarative/src/quickdialogs/quickdialogs',
       'qtquickdialogs2exports.h', 'qtquickdialogs2global_p.h',
       ('QtCore', 'QtGui', 'QtQuick')),
      ('QtQuickDialogs2QuickImpl',
       '../qtdeclarative/src/quickdialogs/quickdialogsquickimpl',
       'qtquickdialogs2quickimplexports.h',
       'qtquickdialogs2quickimplglobal_p.h',
       ('QtCore', 'QtGui', 'QtQuick')),
      ('QtQuickShapes', '../qtdeclarative/src/quickshapes',
       'qquickshapesglobal.h', 'qquickshapesglobal_p.h',
       ('QtCore', 'QtQml')),
      ('QtQuickShapesDesignHelpers',
       '../qtdeclarative/src/quickshapes/designhelpers',
       'qquickshapesdesignhelpersglobal.h',
       'qquickshapesdesignhelpersglobal_p.h',
       ('QtCore', 'QtQml')),
      ('QtQuickTemplates2', '../qtdeclarative/src/quicktemplates',
       'qtquicktemplates2exports.h', 'qtquicktemplates2global_p.h',
       ('QtCore', 'QtGui', 'QtQuick', 'QtQmlModels')),
      ('QtQuickVectorImage', '../qtdeclarative/src/quickvectorimage',
       'qtquickvectorimageexports.h', '',
       ()),
      ('QtScxml', '../qtscxml/src/scxml',
       'qscxmlglobals.h', 'qscxmlglobals_p.h',
       ('QtCore',)),
      ('QtScxmlQml', '../qtscxml/src/scxmlqml',
       'qtscxmlqmlexports.h', 'qscxmlqmlglobals_p.h',
       ('QtCore', 'QtQml', 'QtScxml')),
      ('QtStateMachine', '../qtscxml/src/statemachine',
       'qstatemachineglobal.h', 'qstatemachineglobal_p.h',
       ('QtCore', 'QtGui')),
      ('QtStateMachineQml', '../qtscxml/src/statemachineqml',
       'qtstatemachineqmlexports.h', 'qstatemachineqmlglobals_p.h',
       ('QtCore', 'QtQml', 'QtStateMachine')),
      ('QtHelp', '../qttools/src/assistant/help',
       'qhelp_global.h', '',
       ('QtCore', 'QtSql', 'QtGui', 'QtWidgets')),
      ('QtDesigner', '../qttools/src/designer/src/lib',
       'sdk_global.h', '',
       ('QtCore', 'QtGui', 'QtUiPlugin', 'QtWidgets', 'QtXml',
        'QtOpenGLWidgets')),
      ('QtUiTools', '../qttools/src/uitools',
       'qtuitoolsglobal.h', '',
       ('QtCore', 'QtGui', 'QtWidgets', 'QtOpenGLWidgets')),
      ('QtLocation', '../qtlocation/src/location',
       'qlocationglobal.h', 'qlocationglobal_p.h',
       ('QtCore', 'QtPositioning', 'QtPositioningQuick')),
      ('QtQuick3DAssetImport', '../qtquick3d/src/assetimport',
       'qtquick3dassetimportexports.h', 'qtquick3dassetimportglobal_p.h',
       ('QtCore', 'QtGui', 'QtQml', 'QtQuick3DUtils')),
      ('QtQuick3DAssetUtils', '../qtquick3d/src/assetutils',
       'qtquick3dassetutilsexports.h', 'qtquick3dassetutilsglobal_p.h',
       ('QtCore', 'QtGui', 'QtQuick')),
      ('QtQuick3DHelpers', '../qtquick3d/src/helpers',
       'qtquick3dhelpersexports.h', 'qtquick3dhelpersglobal_p.h',
       ('QtQml', 'QtQuick')),
      ('QtQuick3DIblBaker', '../qtquick3d/src/iblbaker',
       'qtquick3diblbakerexports.h', '',
       ('QtCore', 'QtGui', 'QtQuick', 'QtQuick3DRuntimeRender')),
      ('QtQuick3D', '../qtquick3d/src/quick3d',
       'qtquick3dglobal.h', 'qtquick3dglobal_p.h',
       ('QtCore', 'QtGui', 'QtQml', 'QtQuick', 'QtQuick3DRuntimeRender')),
      ('QtQuick3DParticles', '../qtquick3d/src/quick3dparticles',
       'qtquick3dparticlesglobal.h', 'qtquick3dparticlesglobal_p.h',
       ('QtCore', 'QtGui', 'QtQml', 'QtQuick', 'QtQuick3DRuntimeRender',
        'QtQuick3DAssetImport', 'QtQuick3D')),
      ('QtQuick3DRuntimeRender', '../qtquick3d/src/runtimerender',
       'qtquick3druntimerenderglobal.h', 'qtquick3druntimerenderglobal_p.h',
       ('QtCore', 'QtGui', 'QtQuick', 'QtQuick3DUtils', 'QtShaderTools',
        'QtConcurrent')),
      ('QtQuick3DUtils', '../qtquick3d/src/utils',
       'qtquick3dutilsexports.h', 'qtquick3dutilsglobal_p.h',
       ('QtCore', 'QtGui')),
      ('QtQuickLayouts', '../qtdeclarative/src/quicklayouts',
       'qtquicklayoutsexports.h', 'qquicklayoutglobal_p.h',
       ('QtCore', 'QtQml')),
      ('QtQuickDialogs2Utils',
       '../qtdeclarative/src/quickdialogs/quickdialogsutils',
       'qtquickdialogs2utilsexports.h', 'qtquickdialogs2utilsglobal_p.h',
       ('QtCore',)),
      ('QtLabsFolderListModel', '../qtdeclarative/src/labs/folderlistmodel',
       'qtlabsfolderlistmodelexports.h', 'qquickfolderlistmodelglobal_p.h',
       ()),
      ('QtLabsSettings', '../qtdeclarative/src/labs/settings',
       'qtlabssettingsexports.h', 'qqmlsettingsglobal_p.h',
       ('QtCore', 'QtQml')),
      ('QtLabsWavefrontMesh', '../qtdeclarative/src/labs/wavefrontmesh',
       'qtlabswavefrontmeshexports.h', 'qqmlwavefrontmeshglobal_p.h',
       ()),
      ('QtQmlLocalStorage', '../qtdeclarative/src/qmllocalstorage',
       'qtqmllocalstorageexports.h', 'qqmllocalstorageglobal_p.h',
       ('QtSql',)),
      ('QtScxmlGlobal', '../qtscxml/src/global',
       'qtscxmlglobal-config.h', '',
       ()),
      ('QtUiPlugin', '../qttools/src/uiplugin',
       'qdesignerexportwidget.h', '',
       ('QtCore', 'QtGui', 'QtWidgets')),
      ('QtPositioningQuick', '../qtpositioning/src/positioningquick',
       'qpositioningquickglobal.h', 'qpositioningquickglobal_p.h',
       ('QtCore', 'QtPositioning', 'QtQml', 'QtQuick')),
      ('QtShaderTools', '../qtshadertools/src/shadertools',
       'qtshadertoolsglobal.h', '',
       ('QtCore', 'QtGui')),
  )
  __part_folders__ = {row[0]: row[1] for row in __parts__}
  __part_words__ = {row[0]: row[0][2:].upper() for row in __parts__}
  __global_headers__ = {row[0]: row[2] for row in __parts__}
  __private_global_headers__ = {
      row[0]: row[3] for row in __parts__ if row[3]}
  __part_needs__ = {row[0]: row[4] for row in __parts__}
  #  The name of the lists of switches of a part, where it is not the
  #  name of the part in small letters: its 'CMakeLists.txt' says
  #  'CONFIG_MODULE_NAME', as 'testlib' for QtTest.
  __config_names__ = dict()  # type: Dict[str, str]
  #  Modules of Qt's source that are no part, by hand: QtTest and
  #  QtQuickTest declare their classes for Gui and Widgets only where an
  #  app's build defines 'QT_GUI_LIB' and 'QT_WIDGETS_LIB' (his call).
  __left_out_parts__ = ('QtTest', 'QtQuickTest')
  #  The parts found in Qt's source beyond the table; see
  #  '_addFoundParts'.
  __found_parts__ = ()  # type: Tuple[str, ...]
  #  Switches that are out while every other switch is in, because
  #  each contradicts another one when both are in. 'static' names the
  #  shape of a build, against 'shared'. The four of OpenGL ES are the
  #  other of two kinds of OpenGL that Qt's source says exclude each
  #  other; the kind for desktops is the one that is in.
  __left_out_switches__ = (
      'static', 'opengles2', 'opengles3', 'opengles31', 'opengles32',
  )
  #  What Qt keeps of the system and the compiler it is built for, as
  #  'qplatformdefs.h'. The compiler here reads as Linux.
  __spec_name__ = 'linux-g++'
  #  The file written last into the folder. It says what the folder
  #  was made from, and marks the folder as one made here.
  __stamp_name__ = 'made_by_header_folder.txt'
  #  The three ways Qt's source declares a switch.
  __switch_line__ = re.compile(
      r'^qt_feature(?:_deprecated|_alias)?\("([^"]+)"(.*?)^\)',
      re.S | re.M)
  #  A line of a 'CMakeLists.txt' that names the header files of one of
  #  the folders an installed Qt keeps apart, as 'qpa'.
  __filter_line__ = re.compile(r'\b([A-Z]+)_HEADER_FILTERS\s+"([^"]+)"')
  #  A line that declares a class by its name and does not end there.
  #  Between the word 'class' and the name Qt writes marks of its own,
  #  as 'Q_CORE_EXPORT' and 'QT6_ONLY(Q_CORE_EXPORT)'.
  __class_line__ = re.compile(
      r'^(?:template\s*<[^;{]*>\s*)?(?:class|struct)\s+'
      r'(?:Q[A-Z0-9_]+(?:\([^()]*\))?\s+)*(Q[A-Za-z0-9_]+)\b(?![^;{]*;)')
  #  A line that gives a type another name, which Qt's build treats as
  #  it treats a class.
  __alias_lines__ = (
      re.compile(r'^typedef\s+[^;{}()]*?\b(Q[A-Za-z0-9_]+)\s*;'),
      re.compile(r'^using\s+(Q[A-Za-z0-9_]+)\s*='),
  )
  #  Lines by which Qt declares the classes that walk through a list
  #  or a map, each with the names it gives them.
  __walker_lines__ = (
      (re.compile(r'^Q_DECLARE_SEQUENTIAL_ITERATOR\((\w+)\)'),
       ('Q%sIterator',)),
      (re.compile(r'^Q_DECLARE_MUTABLE_SEQUENTIAL_ITERATOR\((\w+)\)'),
       ('QMutable%sIterator',)),
      (re.compile(r'^Q_DECLARE_ASSOCIATIVE_ITERATOR\((\w+)\)'),
       ('Q%sIterator',)),
      (re.compile(r'^Q_DECLARE_MUTABLE_ASSOCIATIVE_ITERATOR\((\w+)\)'),
       ('QMutable%sIterator',)),
  )
  __named_class__ = re.compile(r'^\s*#\s*pragma\s+qt_class\((\w+)\)')
  #  Where a 'CMakeLists.txt' of the source begins to list files of a
  #  part: for all of it, or, with 'CONDITION', for where that holds.
  __sources_call__ = re.compile(
      r'^qt_internal_(?:add_module|extend_target)\(\s*(\w+)', re.M)
  #  The words a condition of such a list may be made of and still hold
  #  on every system: the switches of Qt, which are all in here, and
  #  the words that join them.
  __everywhere_word__ = re.compile(r'^(?:QT_FEATURE_\w+|AND|OR|NOT)$')

  #  What a word of a condition in Qt's 'CMakeLists.txt' files means to
  #  the compiler: a system, or one of two compilers. A condition with
  #  any other word than these, a switch of Qt, 'TARGET Qt::...' and
  #  the words that join them cannot be asked of a compiler.
  __system_words__ = dict(
      WIN32='defined(Q_OS_WIN)', APPLE='defined(Q_OS_DARWIN)',
      MACOS='defined(Q_OS_MACOS)', IOS='defined(Q_OS_IOS)',
      UIKIT='(defined(Q_OS_IOS) || defined(Q_OS_TVOS) || '
            'defined(Q_OS_VISIONOS))',
      VISIONOS='defined(Q_OS_VISIONOS)', WATCHOS='defined(Q_OS_WATCHOS)',
      LINUX='defined(Q_OS_LINUX)', UNIX='defined(Q_OS_UNIX)',
      ANDROID='defined(Q_OS_ANDROID)', WASM='defined(Q_OS_WASM)',
      QNX='defined(Q_OS_QNX)', INTEGRITY='defined(Q_OS_INTEGRITY)',
      VXWORKS='defined(Q_OS_VXWORKS)', HAIKU='defined(Q_OS_HAIKU)',
      FREEBSD='defined(Q_OS_FREEBSD)', NETBSD='defined(Q_OS_NETBSD)',
      OPENBSD='defined(Q_OS_OPENBSD)', SOLARIS='defined(Q_OS_SOLARIS)',
      CYGWIN='defined(Q_OS_CYGWIN)', OHOS='defined(Q_OS_HARMONY)',
      MSVC='defined(Q_CC_MSVC)', MINGW='defined(Q_CC_MINGW)',
  )
  #  The words after which 'qt_internal_extend_target' lists other things
  #  than its condition.
  __list_words__ = re.compile(
      r'\b(?:SOURCES|DEFINES|PUBLIC_DEFINES|LIBRARIES|PUBLIC_LIBRARIES|'
      r'INCLUDE_DIRECTORIES|PUBLIC_INCLUDE_DIRECTORIES|COMPILE_OPTIONS|'
      r'PUBLIC_COMPILE_OPTIONS|LINK_OPTIONS|PUBLIC_LINK_OPTIONS|'
      r'NO_UNITY_BUILD_SOURCES|NO_PCH_SOURCES|ATTRIBUTION_FILE_DIR_PATHS|'
      r'PRIVATE_MODULE_INTERFACE|NO_UNITY_BUILD|SYSTEM_INCLUDE_DIRECTORIES|'
      r'PUBLIC_SYSTEM_INCLUDE_DIRECTORIES)\b')

  #  Private Variables
  __source_folder__ = None  # type: Optional[str]
  __made_folder__ = None  # type: Optional[str]
  __qt_version__ = None  # type: Optional[str]
  #  For each part, under the name of each of its header files, the
  #  condition under which Qt installs it; see 'getInstallCondition'.
  __install_conditions__ = None  # type: Optional[Dict[str, Any]]
  #  For each switch of Qt, the part whose list has it, and whether that
  #  is the list Qt keeps to itself; see 'getSwitchOwner'.
  __switch_owners__ = None  # type: Optional[Dict[str, Tuple[str, bool]]]

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def getSourceFolder(self) -> str:
    """
    Gives the folder 'qtbase' of Qt's source.

    Provided by you, through 'setSourceFolder'.

    Raises
    ------

    MissingVariable
      'setSourceFolder' has not been called.
    """
    if self.__source_folder__ is None:
      raise MissingVariable(self, '__source_folder__', str)
    return self.__source_folder__

  def getFolder(self) -> str:
    """
    Gives the folder that is made.

    Provided by you, through 'setFolder'. Whether it has been made yet
    is said by 'isMade'.

    Raises
    ------

    MissingVariable
      'setFolder' has not been called.
    """
    if self.__made_folder__ is None:
      raise MissingVariable(self, '__made_folder__', str)
    return self.__made_folder__

  def getPartNames(self) -> Tuple[str, ...]:
    """Gives the parts of Qt the folder is made for."""
    return (*self.__part_folders__,)

  @classmethod
  def getPartPlace(cls, partName: str) -> str:
    """
    Gives where one part of Qt lies in Qt's source, from the folder
    'qtbase': 'src/corelib' for 'QtCore', '../qtsvg/src/svg' for
    'QtSvg'.

    Raises
    ------

    LookupError
      The folder is made for no part of that name.
    """
    if partName not in cls.__part_folders__:
      infoSpec = """No folder of Qt's source is known for the part '%s'."""
      raise LookupError(infoSpec % partName)
    return cls.__part_folders__[partName]

  @classmethod
  def getGlobalHeader(cls, partName: str) -> str:
    """
    Gives the name of the header file of one part that brings in its
    list of switches, as 'qglobal.h' for 'QtCore': what has to be read
    before an '#if QT_CONFIG(...)' of the part can be answered.

    Raises
    ------

    LookupError
      The folder is made for no part of that name.
    """
    cls.getPartPlace(partName)
    return cls.__global_headers__[partName]

  @classmethod
  def getPrivateGlobalHeader(cls, partName: str) -> str:
    """
    Gives the name of the header file in the folder 'private' of one
    part that brings in the switches Qt keeps to itself, as
    'qglobal_p.h' for 'QtCore'; '' for a part with none, as QtXml.

    Raises
    ------

    LookupError
      The folder is made for no part of that name.
    """
    cls.getPartPlace(partName)
    return cls.__private_global_headers__.get(partName, '')

  @classmethod
  def getPartNeeds(cls, partName: str) -> Tuple[str, ...]:
    """
    Gives the parts one part of Qt builds on, as Qt's build names them
    for whoever uses the part: ('QtCore', 'QtGui') for 'QtWidgets'.
    Those whose header files its header files may pull in.

    Raises
    ------

    LookupError
      The folder is made for no part of that name.
    """
    cls.getPartPlace(partName)
    return (*cls.__part_needs__[partName],)

  def getInstallCondition(self, headerPath: str) -> Optional[str]:
    """
    Gives the condition under which Qt installs a header file of a
    part, written for the compiler, as 'defined(Q_OS_WIN)' or
    'QT_CONFIG(ctf)': where it does not hold, an installed Qt has no
    such file, and a ritual file pulling it in stands under it.

    Read from the 'CMakeLists.txt' files of the part: the 'if' around
    the line naming the header file, and the 'CONDITION' of
    'qt_internal_extend_target'. Named more than once, the conditions
    are joined by '||'.

    Returns
    -------

    Optional[str]
      '' for a header file Qt installs always. None for one whose
      condition asks what no compiler knows, as 'MSVC AND
      (TEST_architecture_arch STREQUAL "i386")', and for a file of no
      part.
    """
    real = os.path.realpath(headerPath)
    owner, length = None, 0  # type: Optional[str], int
    for partName in self.getPartNames():
      folder = os.path.realpath(self.getPartFolder(partName))
      if real.startswith(folder + os.sep) and len(folder) > length:
        owner, length = partName, len(folder)
    if owner is None:
      return None
    kept = self.__install_conditions__
    if kept is None:
      kept = self.__install_conditions__ = dict()
    if owner not in kept:
      kept[owner] = self._readInstallConditions(owner)
    return kept[owner].get(os.path.basename(real), '')

  def getSwitchOwner(self, switchName: str) -> Optional[Tuple[str, bool]]:
    """
    Gives the part whose list of switches has a switch, as 'QtNetwork'
    for 'http', and whether it is the list Qt keeps to itself; None for
    a switch no 'configure.cmake' of the parts declares. The switches
    of the file 'configure.cmake' of 'qtbase' itself are those of
    QtCore.
    """
    if self.__switch_owners__ is None:
      owners = dict()  # type: Dict[str, Tuple[str, bool]]
      places = [(
          'QtCore', os.path.join(self.getSourceFolder(), 'configure.cmake'))]
      places.extend(
          (partName, os.path.join(
              self.getPartFolder(partName), 'configure.cmake'))
          for partName in self.getPartNames())
      for partName, path in places:
        public, private = self._findSwitches(path)
        for name in public:
          owners.setdefault(name, (partName, False))
        for name in private:
          owners.setdefault(name, (partName, True))
      self.__switch_owners__ = owners
    return self.__switch_owners__.get(switchName)

  def getPartFolder(self, partName: str) -> str:
    """
    Gives the folder of the source that holds one part of Qt, as
    'src/corelib' in the source folder for 'QtCore'.

    Raises
    ------

    LookupError
      No folder is known for that part, or the source has none.
    """
    if partName not in self.__part_folders__:
      infoSpec = """No folder of Qt's source is known for the part '%s'."""
      raise LookupError(infoSpec % partName)
    folder = os.path.join(
        self.getSourceFolder(), self.__part_folders__[partName])
    if not os.path.isdir(folder):
      infoSpec = """Qt's source has no folder '%s'."""
      raise LookupError(infoSpec % folder)
    return folder

  def getQtVersion(self, **kwargs) -> str:
    """
    Gives the version of Qt its source is, as '6.12.0'.

    Found for you: the source names it in its file '.cmake.conf'. You
    pass nothing; the keyword is for the method's own use.

    Raises
    ------

    LookupError
      The file names no version.
    """
    if self.__qt_version__ is None:
      if kwargs.get('_recursion', False):
        raise RecursionError
      path = os.path.join(self.getSourceFolder(), '.cmake.conf')
      with open(path) as file:
        found = re.search(
            r'QT_REPO_MODULE_VERSION\s+"(\d+\.\d+\.\d+)"', file.read())
      if found is None:
        infoSpec = """'%s' names no version of Qt."""
        raise LookupError(infoSpec % path)
      self.__qt_version__ = found.group(1)
      return self.getQtVersion(_recursion=True)
    return self.__qt_version__

  def getSpecFolder(self) -> str:
    """Gives the folder of the source with what Qt keeps of the system
    and the compiler it is built for, among it 'qplatformdefs.h', which
    some header files Qt calls private pull in. The compiler here reads
    as Linux, so it is the one for Linux."""
    return os.path.join(
        self.getSourceFolder(), 'mkspecs', self.__spec_name__)

  def getLeftOutSwitches(self) -> Tuple[str, ...]:
    """Gives the switches the lists say are out, while every other
    switch is in. They name the shape of a build, as 'static', and not
    a thing Qt can have."""
    return (*self.__left_out_switches__,)

  def getStampFile(self) -> str:
    """Gives the path of the file written last into the folder."""
    return os.path.join(self.getFolder(), self.__stamp_name__)

  def getStamp(self) -> str:
    """Gives what the stamp of a folder made from this source says:
    the source folder and the version of Qt."""
    return 'made from %s, Qt %s\n' % (
        self.getSourceFolder(), self.getQtVersion())

  def isMade(self) -> bool:
    """Says whether the folder has been made from this very source: it
    carries the stamp this source gives."""
    try:
      with open(self.getStampFile()) as file:
        return True if file.read() == self.getStamp() else False
    except OSError:
      return False

  def getHeaderFiles(self, partName: str) -> Tuple[str, ...]:
    """
    Gives the full path of every header file of one part in the
    source, in alphabetical order of their names. The header files
    under a folder 'doc' are examples for Qt's documentation and are
    left out. Of two header files with one name the first in
    alphabetical order of their paths is kept, as Qt's own build
    keeps one. A header file no 'CMakeLists.txt' of the part names is
    left out as well: Qt installs only the header files its build is
    told of, and those others, as 'qlocale_data_p.h', are read by
    Qt's own '.cpp' files alone.
    """
    root = self.getPartFolder(partName)
    #  A part may lie inside the folder of another, as QtLabsStyleKitImpl
    #  in 'labs/stylekit/impl' inside that of QtLabsStyleKit: its files
    #  are its own.
    others = {
        os.path.realpath(self.getPartFolder(name))
        for name in self.getPartNames() if name != partName}
    walked = []  # type: List[Tuple[str, List[str]]]
    for here, folders, names in os.walk(root):
      folders[:] = sorted(
          name for name in folders
          if not self._isOtherModule(os.path.join(here, name), others))
      walked.append((here, sorted(names)))
    walked.sort()
    byName = dict()  # type: Dict[str, str]
    told = set()  # type: Set[str]
    for here, names in walked:
      if 'CMakeLists.txt' in names:
        with open(os.path.join(here, 'CMakeLists.txt')) as file:
          told.update(re.findall(r'([\w.+-]+\.h)\b', file.read()))
    for here, names in walked:
      if 'doc' in os.path.relpath(here, root).split(os.sep):
        continue
      for name in sorted(names):
        if name.endswith('.h') and name not in byName and name in told:
          byName[name] = os.path.join(here, name)
    return (*(byName[name] for name in sorted(byName)),)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def setSourceFolder(self, sourceFolder: str) -> None:
    """
    Tells where Qt's source lies.

    Parameters
    ----------

    sourceFolder : str
      The folder 'qtbase' of Qt's source, which holds 'src'.

    Raises
    ------

    TypeException
      The path is not text.

    FileNotFoundError
      There is no such folder, or it holds no 'src'.
    """
    if not isinstance(sourceFolder, str):
      raise TypeException('sourceFolder', sourceFolder, str)
    sourceFolder = os.path.abspath(sourceFolder)
    if not os.path.isdir(os.path.join(sourceFolder, 'src')):
      infoSpec = """There is no folder 'src' in '%s'."""
      raise FileNotFoundError(infoSpec % sourceFolder)
    self.__source_folder__ = sourceFolder
    self._addFoundParts()
    self.__qt_version__ = None

  def setFolder(self, folder: str) -> None:
    """
    Tells where the folder is to be made.

    Parameters
    ----------

    folder : str
      A folder of its own. It need not exist. If it does, it has to be
      empty or to carry the stamp of a folder made here, since 'make'
      removes what is in it.

    Raises
    ------

    TypeException
      The path is not text.

    FileExistsError
      The folder holds something and carries no stamp of ours.
    """
    if not isinstance(folder, str):
      raise TypeException('folder', folder, str)
    folder = os.path.abspath(folder)
    if os.path.isdir(folder) and os.listdir(folder):
      if not os.path.isfile(os.path.join(folder, self.__stamp_name__)):
        infoSpec = """'%s' holds files and was not made here, so it is
        not made anew."""
        raise FileExistsError(' '.join((infoSpec % folder).split()))
    self.__made_folder__ = folder

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def _readInstallConditions(self, partName: str) -> Dict[str, Any]:
    """Gives, under the name of each header file the 'CMakeLists.txt'
    files of one part name, the condition under which Qt installs it,
    as 'getInstallCondition' gives it. A folder of another part inside
    that of this one is passed over."""
    root = self.getPartFolder(partName)
    others = {
        os.path.realpath(self.getPartFolder(name))
        for name in self.getPartNames() if name != partName}
    found = dict()  # type: Dict[str, List[str]]
    for here, folders, names in os.walk(root):
      folders[:] = sorted(
          name for name in folders
          if not self._isOtherModule(os.path.join(here, name), others))
      if 'CMakeLists.txt' not in names:
        continue
      with open(os.path.join(here, 'CMakeLists.txt')) as file:
        commands = self._readCommands(file.read())
      #  For each 'if' that is open: the condition of the branch read
      #  now, and the conditions of the branches before it.
      opened = []  # type: List[Tuple[str, List[str]]]
      for word, arguments in commands:
        word = word.lower()
        if word == 'if':
          opened.append((arguments, [arguments]))
          continue
        if word in ('elseif', 'else') and opened:
          before = opened[-1][1]
          parts = ['NOT (%s)' % one for one in before]
          if word == 'elseif':
            parts.append('(%s)' % arguments)
          opened[-1] = (' AND '.join(parts), [*before, arguments])
          continue
        if word == 'endif' and opened:
          opened.pop()
          continue
        conditions = [one for one, _ in opened]
        if word == 'qt_internal_extend_target':
          own = re.search(r'\bCONDITION\b(.*)', arguments, re.S)
          if own is not None:
            asked = self.__list_words__.split(own.group(1), 1)[0]
            conditions.append(' '.join(asked.split()))
        joined = ' AND '.join('(%s)' % one for one in conditions)
        if len(conditions) == 1:
          joined = conditions[0]
        for name in re.findall(r'([\w.+-]+\.h)\b', arguments):
          found.setdefault(os.path.basename(name), []).append(joined)
    conditions = dict()  # type: Dict[str, Any]
    for name, asked in found.items():
      if '' in asked:
        conditions[name] = ''
        continue
      spoken = [self._translateCondition(one) for one in asked]
      if None in spoken:
        conditions[name] = None
      elif len({*spoken}) == 1:
        conditions[name] = spoken[0]
      else:
        conditions[name] = ' || '.join(
            '(%s)' % one for one in dict.fromkeys(spoken))
    return conditions

  def _readModuleRows(self) -> Dict[str, Any]:
    """
    Gives a row, as those of '__parts__', for every module of Qt's
    source: each 'qt_internal_add_module' and 'qt_internal_add_qml_module'
    of the 'CMakeLists.txt' files under a folder 'src' of 'qtbase' and
    of the folders beside it. Left out are a module Qt builds as a
    static library or keeps to its own build ('STATIC',
    'INTERNAL_MODULE'), one that installs no header files of its own
    ('NO_MODULE_HEADERS', as qttools' 'Linguist', made only so that an
    old CMake package keeps working), one with no header file, and one
    in the folder of another.

    Under the name of the part, as 'QtCharts': where it lies, from
    'qtbase'; its header file that brings in its switches, the one
    whose name holds 'global', or else its file of words for export;
    the one in its folder 'private', or ''; the parts Qt builds it on
    ('PUBLIC_LIBRARIES'); and the name of its lists of switches.
    """
    everywhere = os.path.dirname(os.path.abspath(self.getSourceFolder()))
    skipped = ('3rdparty', 'tests', 'examples', 'doc', 'plugins')
    found = dict()  # type: Dict[str, Any]
    taken = set()  # type: Set[str]
    for repo in sorted(os.listdir(everywhere)):
      top = os.path.join(everywhere, repo, 'src')
      if not os.path.isdir(top):
        continue
      for here, folders, names in os.walk(top):
        folders[:] = sorted(n for n in folders if n not in skipped)
        if 'CMakeLists.txt' not in names:
          continue
        with open(os.path.join(here, 'CMakeLists.txt')) as file:
          commands = self._readCommands(file.read())
        for word, arguments in commands:
          if word not in (
              'qt_internal_add_module', 'qt_internal_add_qml_module'):
            continue
          words = arguments.split()
          if not words or re.search(
              r'\b(?:STATIC|INTERNAL_MODULE|NO_MODULE_HEADERS)\b',
              arguments):
            continue
          partName = 'Qt%s' % words[0]
          real = os.path.realpath(here)
          if partName in found or real in taken:
            continue
          if not re.match(r'^[0-9]*[A-Z][A-Za-z0-9]*$', words[0]) or (
              words[0].endswith('Private')) or (
              partName in self.__left_out_parts__):
            #  A plugin of QML in small letters, as 'quick3dinputplugin',
            #  a module Qt keeps to its own tests, or one left out by
            #  hand.
            continue
          headers = []  # type: List[str]
          for inner, under, files in os.walk(here):
            under[:] = sorted(
                n for n in under if n not in skipped and not
                self._isOtherModule(os.path.join(inner, n), set()))
            headers.extend(n for n in files if n.endswith('.h'))
          if not headers:
            continue
          taken.add(real)
          low = partName.lower()
          public = sorted(
              n for n in headers if re.search(r'globals?\.h$', n))
          own = [
              n for n in ('%sglobal.h' % low, 'q%sglobal.h' % low[2:])
              if n in public]
          if own or public:
            globalHeader = (own or public)[0]
          elif 'NO_GENERATE_CPP_EXPORTS' in arguments:
            globalHeader = sorted(headers)[0]
          else:
            globalHeader = '%sexports.h' % low
          private = sorted(
              n for n in headers if re.search(r'globals?_p\.h$', n))
          ownPrivate = [
              n for n in ('%sglobal_p.h' % low, 'q%sglobal_p.h' % low[2:])
              if n in private]
          privateHeader = (ownPrivate or private or [''])[0]
          libraries = re.search(
              r'\bPUBLIC_LIBRARIES\b(.*?)(?:\n\s*[A-Z_]{3,}\s*\n|$)',
              arguments, re.S)
          needs = []  # type: List[str]
          for name in re.findall(
              r'Qt::(\w+)', libraries.group(1) if libraries else ''):
            name = 'Qt%s' % re.sub(r'Private$', '', name)
            if name not in needs and name != partName:
              needs.append(name)
          config = re.search(r'\bCONFIG_MODULE_NAME\s+(\w+)', arguments)
          found[partName] = (
              os.path.relpath(here, self.getSourceFolder()), globalHeader,
              privateHeader, (*needs,),
              'qt%s' % config.group(1) if config else '')
    return found

  def _addFoundParts(self) -> None:
    """
    Adds to the table of parts every module of Qt's source it has no row
    for, as '_readModuleRows' finds them, so that every part is asked
    of the one table. A module in the folder of a part of the table is
    left out, and so is a part it is built on that is not in the table
    either way.
    """
    cls = type(self)
    rows = self._readModuleRows()
    known = {
        os.path.realpath(os.path.join(self.getSourceFolder(), place))
        for place in cls.__part_folders__.values()}
    added = []  # type: List[str]
    for partName, row in rows.items():
      place, globalHeader, privateHeader, needs, config = row
      real = os.path.realpath(os.path.join(self.getSourceFolder(), place))
      if partName in cls.__part_folders__ or real in known:
        continue
      cls.__part_folders__[partName] = place
      cls.__part_words__[partName] = partName[2:].upper()
      cls.__global_headers__[partName] = globalHeader
      if privateHeader:
        cls.__private_global_headers__[partName] = privateHeader
      cls.__part_needs__[partName] = needs
      if config:
        cls.__config_names__[partName] = config
      added.append(partName)
    for partName in added:
      cls.__part_needs__[partName] = (*(
          name for name in cls.__part_needs__[partName]
          if name in cls.__part_folders__),)
    cls.__found_parts__ = (*cls.__found_parts__, *added)

  @staticmethod
  def _isOtherModule(folder: str, others: Set[str]) -> bool:
    """Says whether a folder inside that of a part is the folder of
    another part, or of a module or plugin of Qt of its own, as
    QuickNativeStyle in 'quickcontrols/quicknativestyle': its files are
    its own, and none of the part."""
    if os.path.realpath(folder) in others:
      return True
    path = os.path.join(folder, 'CMakeLists.txt')
    if not os.path.isfile(path):
      return False
    with open(path) as file:
      text = file.read()
    return re.search(
        r'^\s*qt_internal_add_(?:qml_)?(?:module|plugin)\s*\(',
        text, re.M) is not None

  @staticmethod
  def _readCommands(text: str) -> List[Tuple[str, str]]:
    """Gives each command of the text of a 'CMakeLists.txt', in order,
    with what stands between its brackets; comments are left out."""
    lines = []  # type: List[str]
    for line in text.split('\n'):
      quoted, cut = False, len(line)
      for index, letter in enumerate(line):
        if letter == '"':
          quoted = not quoted
        elif letter == '#' and not quoted:
          cut = index
          break
      lines.append(line[:cut])
    text = '\n'.join(lines)
    found = []  # type: List[Tuple[str, str]]
    for match in re.finditer(r'(?m)^\s*([A-Za-z_]\w*)\s*\(', text):
      depth, index, quoted = 1, match.end(), False
      while index < len(text) and depth:
        letter = text[index]
        if letter == '"':
          quoted = not quoted
        elif not quoted and letter == '(':
          depth += 1
        elif not quoted and letter == ')':
          depth -= 1
        index += 1
      found.append((match.group(1), text[match.end():index - 1]))
    return found

  def _translateCondition(self, condition: str) -> Optional[str]:
    """Writes a condition of a 'CMakeLists.txt' for the compiler, as
    'QT_CONFIG(textcodec) && defined(Q_OS_WIN)' for 'QT_FEATURE_textcodec
    AND WIN32'; None when a word of it cannot be."""
    tokens = re.findall(r'\(|\)|"[^"]*"|[^\s()]+', condition)
    spoken, index = [], 0  # type: List[str], int
    while index < len(tokens):
      token = tokens[index]
      if token in ('(', ')'):
        spoken.append(token)
      elif token in ('AND', 'OR', 'NOT'):
        spoken.append(dict(AND='&&', OR='||', NOT='!')[token])
      elif token.startswith('QT_FEATURE_'):
        spoken.append('QT_CONFIG(%s)' % token[len('QT_FEATURE_'):])
      elif token in self.__system_words__:
        spoken.append(self.__system_words__[token])
      elif token == 'TARGET' and index + 1 < len(tokens):
        index += 1
        target = re.sub(r'Private$', '', tokens[index])
        known = target.startswith('Qt::') and (
            'Qt%s' % target[len('Qt::'):] in self.__part_folders__)
        spoken.append('1' if known else '0')
      else:
        return None
      index += 1
    text = ' '.join(spoken)
    text = text.replace('( ', '(').replace(' )', ')').replace('! ', '!')
    return text

  def _findSwitches(self, path: str) -> Tuple[List[str], List[str]]:
    """Gives the switches one 'configure.cmake' of the source declares:
    those it marks PUBLIC, and those it marks PRIVATE. A switch may be
    both. What is no letter and no digit in a name becomes '_', as
    Qt's build writes it."""
    public, private = [], []  # type: List[str], List[str]
    if not os.path.isfile(path):
      #  A part with no switches of its own, as QtDBus, has no such
      #  file: what it can have is switched for Qt as a whole.
      return public, private
    with open(path) as file:
      text = file.read()
    for found in self.__switch_line__.finditer(text):
      name = re.sub(r'[^A-Za-z0-9_]', '_', found.group(1))
      if re.search(r'\bPUBLIC\b', found.group(2)):
        public.append(name)
      if re.search(r'\bPRIVATE\b', found.group(2)):
        private.append(name)
    return public, private

  def _writeList(self, path: str, names: List[str], *lines: str) -> None:
    """Writes one list of switches: every switch is in, but for those
    of 'getLeftOutSwitches'. The lines given stand above them."""
    word = re.sub(r'[^A-Za-z0-9]', '_', os.path.basename(path)).upper()
    out = ['#ifndef CUTIENATOR_%s' % word, '#define CUTIENATOR_%s' % word]
    out.extend(lines)
    for name in names:
      value = -1 if name in self.__left_out_switches__ else 1
      out.append('#define QT_FEATURE_%s %d' % (name, value))
    out.append('#endif')
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w') as file:
      file.write('%s\n' % '\n'.join(out))

  def _findFilters(self, partName: str) -> List[Tuple[str, Any]]:
    """Gives, for one part, the folders an installed Qt keeps apart,
    each with the pattern of the header files that go into it, as the
    part's 'CMakeLists.txt' names them: 'qpa' and 'rhi' for QtGui."""
    path = os.path.join(self.getPartFolder(partName), 'CMakeLists.txt')
    with open(path) as file:
      text = file.read()
    found = []  # type: List[Tuple[str, Any]]
    for match in self.__filter_line__.finditer(text):
      pattern = match.group(2).replace('\\\\', '\\')
      found.append((match.group(1).lower(), re.compile(pattern)))
    return found

  def _findInnerFolder(self, name: str, filters: List[Any]) -> str:
    """Gives the folder inside the part's own that a header file goes
    into: 'private' for one ending in '_p.h', 'qpa' and the like for
    one a pattern names, and '' for one meant for everybody."""
    for folder, pattern in filters:
      if pattern.search(name):
        return folder
    return 'private' if name.endswith('_p.h') else ''

  def _findEverywhereHeaders(self, partName: str) -> Any:
    """
    Gives the names of the header files of a part that Qt's source
    lists for every system: in the part's 'CMakeLists.txt' they stand
    in the list of the part itself, or in one whose 'CONDITION' names
    nothing but switches of Qt. A header file listed only under a
    condition that names a system, as 'WIN32' or 'ANDROID', is for
    that system, and one listed nowhere is not known to be for all.

    Only these go into the file named as the part, as Qt's own build
    puts only the header files of the system it builds for into it.
    The others still lie in the folder, each to be read by itself.
    """
    path = os.path.join(self.getPartFolder(partName), 'CMakeLists.txt')
    with open(path) as file:
      text = file.read()
    target = partName[len('Qt'):]
    found = set()  # type: Any
    for call in self.__sources_call__.finditer(text):
      if call.group(1) != target:
        continue
      depth, end = 0, len(text)
      for index in range(call.start(), len(text)):
        letter = text[index]
        depth += 1 if letter == '(' else -1 if letter == ')' else 0
        if depth == 0 and letter == ')':
          end = index
          break
      block = text[call.end():end]
      block = re.sub(r'#[^\n]*', '', block)
      head = block.split('SOURCES')[0]
      if 'CONDITION' in head:
        asked = head.split('CONDITION', 1)[1]
        words = re.findall(r'[A-Za-z_][A-Za-z0-9_]*', asked)
        if not all(self.__everywhere_word__.match(word) for word in words):
          continue
      found.update(
          os.path.basename(name)
          for name in re.findall(r'[\w/+.-]+\.h\b', block))
    return found

  def _findClassNames(self, path: str, partName: str = '') -> List[str]:
    """
    Gives the classes one header file is the header file of: those it
    declares outside of everything else but a namespace named as the
    part, as Qt3D's classes in 'namespace Qt3DRender {' of the part
    Qt3DRender, and those it names with '#pragma qt_class(...)'.
    Reading stops where the header file says '#pragma
    qt_sync_stop_processing', as Qt's own build stops there.
    """
    with open(path, errors='replace') as file:
      text = file.read()
    text = re.sub(r'/\*.*?\*/', ' ', text, flags=re.S)
    found, depth = [], 0  # type: List[str], int
    #  For each '{' that is open, whether it opened a namespace; a
    #  namespace whose '{' stands on a line of its own waits for it.
    opened, waiting = [], False  # type: List[bool], bool
    namespaceLine = re.compile(
        r'^\s*(?:inline\s+)?namespace\s+([\w:]+)\s*(\{)?')
    for line in text.split('\n'):
      line = re.sub(r'//.*$', '', line)
      named = self.__named_class__.match(line)
      if named is not None:
        if named.group(1) not in found:
          found.append(named.group(1))
        continue
      if 'qt_sync_stop_processing' in line:
        break
      if line.lstrip().startswith('#'):
        continue
      if depth == 0:
        names = []  # type: List[str]
        declared = self.__class_line__.match(line)
        if declared is not None:
          names.append(declared.group(1))
        for pattern in self.__alias_lines__:
          named = pattern.match(line)
          if named is not None:
            names.append(named.group(1))
        for pattern, shapes in self.__walker_lines__:
          named = pattern.match(line)
          if named is not None:
            names.extend(shape % named.group(1) for shape in shapes)
        found.extend(name for name in names if name not in found)
      opening = namespaceLine.match(line)
      if opening is not None and opening.group(1) != partName:
        opening = None
      namespaceBrace = opening is not None and opening.group(2) is not None
      if opening is not None and not namespaceBrace and not (
          '=' in line or ';' in line):
        waiting = True
      for letter in line:
        if letter == '{':
          opened.append(waiting or namespaceBrace)
          waiting = namespaceBrace = False
        elif letter == '}' and opened:
          opened.pop()
      depth = sum(1 for one in opened if not one)
    return found

  def _fillFromPattern(self, pattern: str, target: str,
                       **words: str) -> None:
    """Writes one file from a pattern that lies in Qt's source, with
    each '@word@' of the pattern filled in."""
    with open(os.path.join(self.getSourceFolder(), pattern)) as file:
      text = file.read()
    for word, value in words.items():
      text = text.replace('@%s@' % word, value)
    left = re.search(r'@\w+@', text)
    if left is not None:
      infoSpec = """The pattern '%s' of Qt's source has '%s', which
      nothing fills in."""
      info = infoSpec % (pattern, left.group(0))
      raise LookupError(' '.join(info.split()))
    with open(target, 'w') as file:
      file.write(text)

  def _makePart(self, partName: str) -> None:
    """Makes the folder of one part: the pointers, the files named as
    classes, the file named as the part, and the lists of switches."""
    version = self.getQtVersion()
    target = os.path.join(self.getFolder(), partName)
    inner = os.path.join(target, version, partName)
    os.makedirs(os.path.join(inner, 'private'), exist_ok=True)
    filters = self._findFilters(partName)
    everywhere = self._findEverywhereHeaders(partName)
    #  The header file a part is built with, as 'qt_pch.h', is named in
    #  its 'CMakeLists.txt' after 'PRECOMPILED_HEADER'. It is for the
    #  building of Qt alone and is no header file of Qt for anyone
    #  else, so the folder has none.
    listPath = os.path.join(self.getPartFolder(partName), 'CMakeLists.txt')
    with open(listPath) as file:
      buildOnly = {
          os.path.basename(name) for name in re.findall(
              r'PRECOMPILED_HEADER\s+"([^"]+)"', file.read())}
    direct, classFiles = [], dict()  # type: List[Any], Dict[str, str]
    for path in self.getHeaderFiles(partName):
      name = os.path.basename(path)
      if name in buildOnly:
        continue
      folder = self._findInnerFolder(name, filters)
      if folder:
        os.makedirs(os.path.join(inner, folder), exist_ok=True)
        os.symlink(path, os.path.join(inner, folder, name))
        continue
      os.symlink(path, os.path.join(target, name))
      with open(path, errors='replace') as file:
        text = file.read()
      #  The rule of Qt's own build for the file named as the part: a
      #  header file meant for everybody whose name has no '_', and
      #  that does not say 'qt_no_master_include'. Here it also has to
      #  be one Qt's source lists for every system.
      wanted = name in everywhere and '_' not in name
      if wanted and 'qt_no_master_include' not in text:
        required = re.search(
            r'^ *QT_REQUIRE_CONFIG\((\w+)\);?$', text, re.M)
        direct.append((name, required.group(1) if required else ''))
      for className in self._findClassNames(path, partName):
        classFiles.setdefault(className, name)
    for className, name in sorted(classFiles.items()):
      with open(os.path.join(target, className), 'w') as file:
        file.write('#include <%s/%s>\n' % (partName, name))
    needs = self.__part_needs__[partName]
    with open(os.path.join(target, '%sDepends' % partName), 'w') as file:
      file.write(''.join('#include <%s/%s>\n' % (n, n) for n in needs))
    with open(os.path.join(target, partName), 'w') as file:
      file.write('#include <%s/%sDepends>\n' % (partName, partName))
      #  What a switch of the part is set to is known only once this
      #  header file of the part has been read.
      file.write('#include <%s/%s>\n' % (
          partName, self.__global_headers__[partName]))
      for name, switch in direct:
        line = '#include <%s/%s>\n' % (partName, name)
        if switch:
          #  A header file that is all of one switch of Qt is pulled
          #  in only where that switch is in, as Qt's build has it.
          line = '#if QT_CONFIG(%s)\n%s#endif\n' % (switch, line)
        file.write(line)
    low, word = partName.lower(), self.__part_words__[partName]
    config = self.__config_names__.get(partName, low)
    public, private = self._findSwitches(
        os.path.join(self.getPartFolder(partName), 'configure.cmake'))
    self._writeList(os.path.join(target, '%s-config.h' % config), public)
    self._writeList(
        os.path.join(inner, 'private', '%s-config_p.h' % config), private)
    self._fillFromPattern(
        'cmake/modulecppexports.h.in',
        os.path.join(target, '%sexports.h' % low),
        header_base_name_upper='%sEXPORTS' % low.upper(),
        module_define_infix=word)
    major, minor, patch = (int(one) for one in version.split('.'))
    with open(os.path.join(target, '%sversion.h' % low), 'w') as file:
      file.write('#define %s_VERSION_STR "%s"\n' % (low.upper(), version))
      file.write('#define %s_VERSION 0x%02x%02x%02x\n' % (
          low.upper(), major, minor, patch))

  def make(self) -> None:
    """
    Makes the folder, anew when it is there already.

    Raises
    ------

    FileExistsError
      The folder holds something and carries no stamp of ours.
    """
    folder = self.getFolder()
    if os.path.isdir(folder) and os.listdir(folder):
      if not os.path.isfile(self.getStampFile()):
        infoSpec = """'%s' holds files and was not made here, so it is
        not made anew."""
        raise FileExistsError(' '.join((infoSpec % folder).split()))
      shutil.rmtree(folder)
    os.makedirs(folder, exist_ok=True)
    #  Each part has a folder of its own: they are made at once, one
    #  process each, as many as the machine has cores.
    context = multiprocessing.get_context('fork')
    with ProcessPoolExecutor(
        os.cpu_count() or 1, mp_context=context) as pool:
      for _ in pool.map(self._makePart, self.getPartNames()):
        pass
    #  The switches of Qt as a whole, and the two files Qt keeps with
    #  QtCore for all of it.
    version = self.getQtVersion()
    major, minor, patch = version.split('.')
    core = os.path.join(folder, 'QtCore')
    public, private = self._findSwitches(
        os.path.join(self.getSourceFolder(), 'configure.cmake'))
    self._writeList(
        os.path.join(core, 'qconfig.h'), public,
        '#define QT_VERSION_STR "%s"' % version,
        '#define QT_VERSION_MAJOR %s' % major,
        '#define QT_VERSION_MINOR %s' % minor,
        '#define QT_VERSION_PATCH %s' % patch,
        #  With this the word 'Q_CORE_EXPORT' and its like leave a mark
        #  the compiler writes down, so what Qt marks can be told.
        '#define QT_VISIBILITY_AVAILABLE')
    self._writeList(os.path.join(
        core, version, 'QtCore', 'private', 'qconfig_p.h'), private)
    self._fillFromPattern(
        'src/corelib/global/qtdeprecationdefinitions.h.in',
        os.path.join(core, 'qtdeprecationdefinitions.h'),
        #  Qt's own values, as its 'src/corelib/CMakeLists.txt' sets
        #  them: nothing Qt has deprecated since 5.0 is taken away, and
        #  all of it carries its notice.
        QT_DISABLE_DEPRECATED_UP_TO='0x050000',
        QT_WARN_DEPRECATED_UP_TO='0x070000')
    with open(self.getStampFile(), 'w') as file:
      file.write(self.getStamp())

  def __str__(self) -> str:
    """Says what the folder is made from and whether it is made."""
    clsName = type(self).__name__
    if self.__source_folder__ is None or self.__made_folder__ is None:
      return '<%s still waiting for its two folders>' % clsName
    state = 'made' if self.isMade() else 'not made yet'
    return '<%s %s from %s, %s>' % (
        clsName, self.getFolder(), self.getSourceFolder(), state)

  __repr__ = __str__
