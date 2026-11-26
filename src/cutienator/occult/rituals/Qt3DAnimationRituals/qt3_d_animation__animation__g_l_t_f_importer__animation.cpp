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

//  from ../qt3d/src/animation/backend/gltfimporter.cpp, line 103, as local:gltfimporter.cpp:KEY_CHANNELS
#define KEY_CHANNELS                QLatin1String("channels")

//  from ../qt3d/src/animation/backend/gltfimporter.cpp, line 108, as local:gltfimporter.cpp:KEY_INPUT
#define KEY_INPUT                   QLatin1String("input")

//  from ../qt3d/src/animation/backend/gltfimporter.cpp, line 109, as local:gltfimporter.cpp:KEY_INTERPOLATION
#define KEY_INTERPOLATION           QLatin1String("interpolation")

//  from ../qt3d/src/animation/backend/gltfimporter.cpp, line 113, as local:gltfimporter.cpp:KEY_NAME
#define KEY_NAME                    QLatin1String("name")

//  from ../qt3d/src/animation/backend/gltfimporter.cpp, line 114, as local:gltfimporter.cpp:KEY_NODE
#define KEY_NODE                    QLatin1String("node")

//  from ../qt3d/src/animation/backend/gltfimporter.cpp, line 116, as local:gltfimporter.cpp:KEY_OUTPUT
#define KEY_OUTPUT                  QLatin1String("output")

//  from ../qt3d/src/animation/backend/gltfimporter.cpp, line 117, as local:gltfimporter.cpp:KEY_PATH
#define KEY_PATH                    QLatin1String("path")

//  from ../qt3d/src/animation/backend/gltfimporter.cpp, line 119, as local:gltfimporter.cpp:KEY_SAMPLER
#define KEY_SAMPLER                 QLatin1String("sampler")

//  from ../qt3d/src/animation/backend/gltfimporter.cpp, line 120, as local:gltfimporter.cpp:KEY_SAMPLERS
#define KEY_SAMPLERS                QLatin1String("samplers")

//  from ../qt3d/src/animation/backend/gltfimporter.cpp, line 124, as local:gltfimporter.cpp:KEY_TARGET
#define KEY_TARGET                  QLatin1String("target")

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

//  from ../qt3d/src/animation/backend/gltfimporter.cpp, line 227, as _ZN13Qt3DAnimation9Animation12GLTFImporter7SamplerC1ERK11QJsonObject
namespace Qt3DAnimation::Animation {
inline GLTFImporter::Sampler::Sampler(const QJsonObject &json)
    : inputAccessorIndex(json.value(KEY_INPUT).toInt())
    , outputAccessorIndex(json.value(KEY_OUTPUT).toInt())
    , interpolationMode(Linear)
{
    const auto interpolation = json.value(KEY_INTERPOLATION).toString();
    if (interpolation == QLatin1String("LINEAR"))
        interpolationMode = Linear;
    else if (interpolation == QLatin1String("STEP"))
        interpolationMode = Step;
    else if (interpolation == QLatin1String("CATMULLROMSPLINE"))
        interpolationMode = CatmullRomSpline;
    else if (interpolation == QLatin1String("CUBICSPLINE"))
        interpolationMode = CubicSpline;
}
}  // namespace Qt3DAnimation::Animation

//  from ../qt3d/src/animation/backend/gltfimporter.cpp, line 255, as _ZN13Qt3DAnimation9Animation12GLTFImporter9AnimationC1Ev
namespace Qt3DAnimation::Animation {
inline GLTFImporter::Animation::Animation()
    : name()
    , channels()
    , samplers()
{
}
}  // namespace Qt3DAnimation::Animation

//  from ../qt3d/src/animation/backend/gltfimporter.cpp, line 262, as _ZN13Qt3DAnimation9Animation12GLTFImporter9AnimationC1ERK11QJsonObject
namespace Qt3DAnimation::Animation {
inline GLTFImporter::Animation::Animation(const QJsonObject &json)
    : name(json.value(KEY_NAME).toString())
{
    QJsonArray channelsArray = json.value(KEY_CHANNELS).toArray();
    channels.reserve(channelsArray.size());
    for (const auto channelValue : channelsArray) {
        Channel channel(channelValue.toObject());
        channels.push_back(channel);
    }

    QJsonArray samplersArray = json.value(KEY_SAMPLERS).toArray();
    samplers.reserve(samplersArray.size());
    for (const auto samplerValue : samplersArray) {
        Sampler sampler(samplerValue.toObject());
        samplers.push_back(sampler);
    }
}
}  // namespace Qt3DAnimation::Animation
//  -----------------------------------------------------------------------

//  Qt3DAnimation::Animation::GLTFImporter::Animation::Animation()
extern "C" Q_DECL_EXPORT
Qt3DAnimation::Animation::GLTFImporter::Animation *ritual_ZN13Qt3DAnimation9Animation12GLTFImporter9AnimationC1Ev() {
  return new Qt3DAnimation::Animation::GLTFImporter::Animation();
}

//  Qt3DAnimation::Animation::GLTFImporter::Animation::Animation(const
//      QJsonObject &json)
extern "C" Q_DECL_EXPORT
Qt3DAnimation::Animation::GLTFImporter::Animation *ritual_ZN13Qt3DAnimation9Animation12GLTFImporter9AnimationC1ERK11QJsonObject(
    const QJsonObject *json) {
  return new Qt3DAnimation::Animation::GLTFImporter::Animation(*json);
}

//  Qt3DAnimation::Animation::GLTFImporter::Animation::~Animation()
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation9Animation12GLTFImporter9AnimationD1Ev(
    Qt3DAnimation::Animation::GLTFImporter::Animation *self) {
  delete self;
}
