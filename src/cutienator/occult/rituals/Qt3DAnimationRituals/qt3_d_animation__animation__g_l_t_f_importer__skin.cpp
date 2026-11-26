//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DAnimation/6.12.0/Qt3DAnimation/private/gltfimporter_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <Qt3DAnimation/6.12.0/Qt3DAnimation/private/qt3danimation_global_p.h>
#include <Qt3DAnimation/Qt3DAnimation>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DAnimation/6.12.0/Qt3DAnimation/private/gltfimporter_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qjsonobject.h>
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
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qt3d/src/animation/backend/gltfimporter.cpp, line 107, as local:gltfimporter.cpp:KEY_JOINTS
#define KEY_JOINTS                  QLatin1String("joints")

//  from ../qt3d/src/animation/backend/gltfimporter.cpp, line 110, as local:gltfimporter.cpp:KEY_INVERSE_BIND_MATRICES
#define KEY_INVERSE_BIND_MATRICES   QLatin1String("inverseBindMatrices")

//  from ../qt3d/src/animation/backend/gltfimporter.cpp, line 113, as local:gltfimporter.cpp:KEY_NAME
#define KEY_NAME                    QLatin1String("name")

//  from ../qt3d/src/animation/backend/gltfimporter.cpp, line 187, as _ZN13Qt3DAnimation9Animation12GLTFImporter4SkinC1Ev
namespace Qt3DAnimation::Animation {
inline GLTFImporter::Skin::Skin()
    : inverseBindAccessorIndex(-1)
    , jointNodeIndices()
{
}
}  // namespace Qt3DAnimation::Animation

//  from ../qt3d/src/animation/backend/gltfimporter.cpp, line 193, as _ZN13Qt3DAnimation9Animation12GLTFImporter4SkinC1ERK11QJsonObject
namespace Qt3DAnimation::Animation {
inline GLTFImporter::Skin::Skin(const QJsonObject &json)
    : name(json.value(KEY_NAME).toString())
    , inverseBindAccessorIndex(json.value(KEY_INVERSE_BIND_MATRICES).toInt())
{
    QJsonArray jointNodes = json.value(KEY_JOINTS).toArray();
    jointNodeIndices.reserve(jointNodes.size());
    for (const auto jointNodeValue : jointNodes)
        jointNodeIndices.push_back(jointNodeValue.toInt());
}
}  // namespace Qt3DAnimation::Animation
//  -----------------------------------------------------------------------

//  Qt3DAnimation::Animation::GLTFImporter::Skin::Skin()
extern "C" Q_DECL_EXPORT
Qt3DAnimation::Animation::GLTFImporter::Skin *ritual_ZN13Qt3DAnimation9Animation12GLTFImporter4SkinC1Ev() {
  return new Qt3DAnimation::Animation::GLTFImporter::Skin();
}

//  Qt3DAnimation::Animation::GLTFImporter::Skin::Skin(const QJsonObject
//      &json)
extern "C" Q_DECL_EXPORT
Qt3DAnimation::Animation::GLTFImporter::Skin *ritual_ZN13Qt3DAnimation9Animation12GLTFImporter4SkinC1ERK11QJsonObject(
    const QJsonObject *json) {
  return new Qt3DAnimation::Animation::GLTFImporter::Skin(*json);
}

//  Qt3DAnimation::Animation::GLTFImporter::Skin::~Skin()
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation9Animation12GLTFImporter4SkinD1Ev(
    Qt3DAnimation::Animation::GLTFImporter::Skin *self) {
  delete self;
}
