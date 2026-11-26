//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DAnimation/6.12.0/Qt3DAnimation/private/gltfimporter_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <Qt3DAnimation/6.12.0/Qt3DAnimation/private/qt3danimation_global_p.h>
#include <Qt3DAnimation/Qt3DAnimation>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DAnimation/6.12.0/Qt3DAnimation/private/gltfimporter_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DAnimation/private/gltfimporter_p.h>
#include <Qt3DCore/private/qloadgltf_p.h>
#include <Qt3DAnimation/private/animationlogging_p.h>
#include <Qt3DAnimation/private/fcurve_p.h>
#include <Qt3DAnimation/private/keyframe_p.h>
#include <QtGui/qopengl.h>
#include <QtGui/qquaternion.h>
#include <QtGui/qvector2d.h>
#include <QtGui/qvector3d.h>
#include <QtGui/qvector4d.h>
#include <QtCore/qdir.h>
#include <QtCore/qfile.h>
#include <QtCore/qfileinfo.h>
#include <QtCore/qiodevice.h>
#include <QtCore/qversionnumber.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qt3d/src/animation/backend/gltfimporter.cpp, line 104, as local:gltfimporter.cpp:KEY_CHILDREN
#define KEY_CHILDREN                QLatin1String("children")

//  from ../qt3d/src/animation/backend/gltfimporter.cpp, line 111, as local:gltfimporter.cpp:KEY_MATRIX
#define KEY_MATRIX                  QLatin1String("matrix")

//  from ../qt3d/src/animation/backend/gltfimporter.cpp, line 113, as local:gltfimporter.cpp:KEY_NAME
#define KEY_NAME                    QLatin1String("name")

//  from ../qt3d/src/animation/backend/gltfimporter.cpp, line 118, as local:gltfimporter.cpp:KEY_ROTATION
#define KEY_ROTATION                QLatin1String("rotation")

//  from ../qt3d/src/animation/backend/gltfimporter.cpp, line 121, as local:gltfimporter.cpp:KEY_SCALE
#define KEY_SCALE                   QLatin1String("scale")

//  from ../qt3d/src/animation/backend/gltfimporter.cpp, line 125, as local:gltfimporter.cpp:KEY_TRANSLATION
#define KEY_TRANSLATION             QLatin1String("translation")

//  from ../qt3d/src/animation/backend/gltfimporter.cpp, line 280, as _ZN13Qt3DAnimation9Animation12GLTFImporter4NodeC1Ev
namespace Qt3DAnimation::Animation {
inline GLTFImporter::Node::Node()
    : localTransform()
    , childNodeIndices()
    , name()
    , parentNodeIndex(-1)
    , cameraIndex(-1)
    , meshIndex(-1)
    , skinIndex(-1)
{
}
}  // namespace Qt3DAnimation::Animation
//  -----------------------------------------------------------------------

//  Qt3DAnimation::Animation::GLTFImporter::Node::Node()
extern "C" Q_DECL_EXPORT
Qt3DAnimation::Animation::GLTFImporter::Node *ritual_ZN13Qt3DAnimation9Animation12GLTFImporter4NodeC1Ev() {
  return new Qt3DAnimation::Animation::GLTFImporter::Node();
}

//  Qt3DAnimation::Animation::GLTFImporter::Node::~Node()
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation9Animation12GLTFImporter4NodeD1Ev(
    Qt3DAnimation::Animation::GLTFImporter::Node *self) {
  delete self;
}
