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

//  from ../qt3d/src/animation/backend/gltfimporter.cpp, line 97, as local:gltfimporter.cpp:KEY_BUFFER_VIEW
#define KEY_BUFFER_VIEW             QLatin1String("bufferView")

//  from ../qt3d/src/animation/backend/gltfimporter.cpp, line 100, as local:gltfimporter.cpp:KEY_BYTE_OFFSET
#define KEY_BYTE_OFFSET             QLatin1String("byteOffset")

//  from ../qt3d/src/animation/backend/gltfimporter.cpp, line 101, as local:gltfimporter.cpp:KEY_BYTE_STRIDE
#define KEY_BYTE_STRIDE             QLatin1String("byteStride")

//  from ../qt3d/src/animation/backend/gltfimporter.cpp, line 105, as local:gltfimporter.cpp:KEY_COMPONENT_TYPE
#define KEY_COMPONENT_TYPE          QLatin1String("componentType")

//  from ../qt3d/src/animation/backend/gltfimporter.cpp, line 106, as local:gltfimporter.cpp:KEY_COUNT
#define KEY_COUNT                   QLatin1String("count")

//  from ../qt3d/src/animation/backend/gltfimporter.cpp, line 126, as local:gltfimporter.cpp:KEY_TYPE
#define KEY_TYPE                    QLatin1String("type")

//  from ../qt3d/src/animation/backend/gltfimporter.cpp, line 339, as _ZN13Qt3DAnimation9Animation12GLTFImporter20accessorTypeFromJSONEi
namespace Qt3DAnimation::Animation {
inline Qt3DCore::QAttribute::VertexBaseType GLTFImporter::accessorTypeFromJSON(int componentType)
{
    if (componentType == GL_BYTE)
        return Qt3DCore::QAttribute::Byte;
    else if (componentType == GL_UNSIGNED_BYTE)
        return Qt3DCore::QAttribute::UnsignedByte;
    else if (componentType == GL_SHORT)
        return Qt3DCore::QAttribute::Short;
    else if (componentType == GL_UNSIGNED_SHORT)
        return Qt3DCore::QAttribute::UnsignedShort;
    else if (componentType == GL_UNSIGNED_INT)
        return Qt3DCore::QAttribute::UnsignedInt;
    else if (componentType == GL_FLOAT)
        return Qt3DCore::QAttribute::Float;

    // There shouldn't be an invalid case here
    qWarning("unsupported accessor type %d", componentType);
    return Qt3DCore::QAttribute::Float;
}
}  // namespace Qt3DAnimation::Animation

//  from ../qt3d/src/animation/backend/gltfimporter.cpp, line 380, as _ZN13Qt3DAnimation9Animation12GLTFImporter24accessorDataSizeFromJsonERK7QString
namespace Qt3DAnimation::Animation {
inline uint GLTFImporter::accessorDataSizeFromJson(const QString &type)
{
    QString typeName = type.toUpper();
    if (typeName == QLatin1String("SCALAR"))
        return 1;
    if (typeName == QLatin1String("VEC2"))
        return 2;
    if (typeName == QLatin1String("VEC3"))
        return 3;
    if (typeName == QLatin1String("VEC4"))
        return 4;
    if (typeName == QLatin1String("MAT2"))
        return 4;
    if (typeName == QLatin1String("MAT3"))
        return 9;
    if (typeName == QLatin1String("MAT4"))
        return 16;

    return 0;
}
}  // namespace Qt3DAnimation::Animation

//  from ../qt3d/src/animation/backend/gltfimporter.cpp, line 162, as _ZN13Qt3DAnimation9Animation12GLTFImporter12AccessorDataC1Ev
namespace Qt3DAnimation::Animation {
inline GLTFImporter::AccessorData::AccessorData()
    : type(Qt3DCore::QAttribute::Float)
    , dataSize(0)
    , count(0)
    , byteOffset(0)
    , byteStride(0)
{
}
}  // namespace Qt3DAnimation::Animation

//  from ../qt3d/src/animation/backend/gltfimporter.cpp, line 171, as _ZN13Qt3DAnimation9Animation12GLTFImporter12AccessorDataC1ERK11QJsonObject
namespace Qt3DAnimation::Animation {
inline GLTFImporter::AccessorData::AccessorData(const QJsonObject &json)
    : bufferViewIndex(json.value(KEY_BUFFER_VIEW).toInt(-1))
    , type(accessorTypeFromJSON(json.value(KEY_COMPONENT_TYPE).toInt()))
    , dataSize(accessorDataSizeFromJson(json.value(KEY_TYPE).toString()))
    , count(json.value(KEY_COUNT).toInt())
    , byteOffset(0)
    , byteStride(0)
{
    const auto byteOffsetValue = json.value(KEY_BYTE_OFFSET);
    if (!byteOffsetValue.isUndefined())
        byteOffset = byteOffsetValue.toInt();
    const auto byteStrideValue = json.value(KEY_BYTE_STRIDE);
    if (!byteStrideValue.isUndefined())
        byteStride = byteStrideValue.toInt();
}
}  // namespace Qt3DAnimation::Animation
//  -----------------------------------------------------------------------

//  Qt3DAnimation::Animation::GLTFImporter::AccessorData::AccessorData()
extern "C" Q_DECL_EXPORT
Qt3DAnimation::Animation::GLTFImporter::AccessorData *ritual_ZN13Qt3DAnimation9Animation12GLTFImporter12AccessorDataC1Ev() {
  return new Qt3DAnimation::Animation::GLTFImporter::AccessorData();
}

//  Qt3DAnimation::Animation::GLTFImporter::AccessorData::AccessorData(const
//      QJsonObject &json)
extern "C" Q_DECL_EXPORT
Qt3DAnimation::Animation::GLTFImporter::AccessorData *ritual_ZN13Qt3DAnimation9Animation12GLTFImporter12AccessorDataC1ERK11QJsonObject(
    const QJsonObject *json) {
  return new Qt3DAnimation::Animation::GLTFImporter::AccessorData(*json);
}

//  Qt3DAnimation::Animation::GLTFImporter::AccessorData::~AccessorData()
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation9Animation12GLTFImporter12AccessorDataD1Ev(
    Qt3DAnimation::Animation::GLTFImporter::AccessorData *self) {
  delete self;
}
