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

//  from ../qt3d/src/animation/backend/gltfimporter.cpp, line 99, as local:gltfimporter.cpp:KEY_BYTE_LENGTH
#define KEY_BYTE_LENGTH             QLatin1String("byteLength")

//  from ../qt3d/src/animation/backend/gltfimporter.cpp, line 127, as local:gltfimporter.cpp:KEY_URI
#define KEY_URI                     QLatin1String("uri")

//  from ../qt3d/src/animation/backend/gltfimporter.cpp, line 130, as _ZN13Qt3DAnimation9Animation12GLTFImporter10BufferDataC1Ev
namespace Qt3DAnimation::Animation {
inline GLTFImporter::BufferData::BufferData()
    : byteLength(0)
    , data()
{
}
}  // namespace Qt3DAnimation::Animation

//  from ../qt3d/src/animation/backend/gltfimporter.cpp, line 136, as _ZN13Qt3DAnimation9Animation12GLTFImporter10BufferDataC1ERK11QJsonObject
namespace Qt3DAnimation::Animation {
inline GLTFImporter::BufferData::BufferData(const QJsonObject &json)
    : byteLength(json.value(KEY_BYTE_LENGTH).toInt())
    , path(json.value(KEY_URI).toString())
    , data()
{
}
}  // namespace Qt3DAnimation::Animation
//  -----------------------------------------------------------------------

//  Qt3DAnimation::Animation::GLTFImporter::BufferData::BufferData()
extern "C" Q_DECL_EXPORT
Qt3DAnimation::Animation::GLTFImporter::BufferData *ritual_ZN13Qt3DAnimation9Animation12GLTFImporter10BufferDataC1Ev() {
  return new Qt3DAnimation::Animation::GLTFImporter::BufferData();
}

//  Qt3DAnimation::Animation::GLTFImporter::BufferData::BufferData(const
//      QJsonObject &json)
extern "C" Q_DECL_EXPORT
Qt3DAnimation::Animation::GLTFImporter::BufferData *ritual_ZN13Qt3DAnimation9Animation12GLTFImporter10BufferDataC1ERK11QJsonObject(
    const QJsonObject *json) {
  return new Qt3DAnimation::Animation::GLTFImporter::BufferData(*json);
}

//  Qt3DAnimation::Animation::GLTFImporter::BufferData::~BufferData()
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation9Animation12GLTFImporter10BufferDataD1Ev(
    Qt3DAnimation::Animation::GLTFImporter::BufferData *self) {
  delete self;
}
