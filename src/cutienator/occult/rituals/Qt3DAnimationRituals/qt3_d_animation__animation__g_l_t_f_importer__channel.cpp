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
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qt3d/src/animation/backend/gltfimporter.cpp, line 114, as local:gltfimporter.cpp:KEY_NODE
#define KEY_NODE                    QLatin1String("node")

//  from ../qt3d/src/animation/backend/gltfimporter.cpp, line 117, as local:gltfimporter.cpp:KEY_PATH
#define KEY_PATH                    QLatin1String("path")

//  from ../qt3d/src/animation/backend/gltfimporter.cpp, line 119, as local:gltfimporter.cpp:KEY_SAMPLER
#define KEY_SAMPLER                 QLatin1String("sampler")

//  from ../qt3d/src/animation/backend/gltfimporter.cpp, line 124, as local:gltfimporter.cpp:KEY_TARGET
#define KEY_TARGET                  QLatin1String("target")

//  from ../qt3d/src/animation/backend/gltfimporter.cpp, line 203, as _ZN13Qt3DAnimation9Animation12GLTFImporter7ChannelC1Ev
namespace Qt3DAnimation::Animation {
inline GLTFImporter::Channel::Channel()
    : samplerIndex(-1)
    , targetNodeIndex(-1)
    , targetProperty()
{
}
}  // namespace Qt3DAnimation::Animation

//  from ../qt3d/src/animation/backend/gltfimporter.cpp, line 210, as _ZN13Qt3DAnimation9Animation12GLTFImporter7ChannelC1ERK11QJsonObject
namespace Qt3DAnimation::Animation {
inline GLTFImporter::Channel::Channel(const QJsonObject &json)
    : samplerIndex(json.value(KEY_SAMPLER).toInt())
    , targetNodeIndex(-1)
    , targetProperty()
{
    const auto targetJson = json.value(KEY_TARGET).toObject();
    targetNodeIndex = targetJson.value(KEY_NODE).toInt();
    targetProperty = targetJson.value(KEY_PATH).toString();
}
}  // namespace Qt3DAnimation::Animation
//  -----------------------------------------------------------------------

//  Qt3DAnimation::Animation::GLTFImporter::Channel::Channel()
extern "C" Q_DECL_EXPORT
Qt3DAnimation::Animation::GLTFImporter::Channel *ritual_ZN13Qt3DAnimation9Animation12GLTFImporter7ChannelC1Ev() {
  return new Qt3DAnimation::Animation::GLTFImporter::Channel();
}

//  Qt3DAnimation::Animation::GLTFImporter::Channel::Channel(const
//      QJsonObject &json)
extern "C" Q_DECL_EXPORT
Qt3DAnimation::Animation::GLTFImporter::Channel *ritual_ZN13Qt3DAnimation9Animation12GLTFImporter7ChannelC1ERK11QJsonObject(
    const QJsonObject *json) {
  return new Qt3DAnimation::Animation::GLTFImporter::Channel(*json);
}

//  Qt3DAnimation::Animation::GLTFImporter::Channel::~Channel()
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation9Animation12GLTFImporter7ChannelD1Ev(
    Qt3DAnimation::Animation::GLTFImporter::Channel *self) {
  delete self;
}
