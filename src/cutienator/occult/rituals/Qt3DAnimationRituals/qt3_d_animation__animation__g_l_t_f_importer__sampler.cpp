//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DAnimation/6.12.0/Qt3DAnimation/private/gltfimporter_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <Qt3DAnimation/6.12.0/Qt3DAnimation/private/qt3danimation_global_p.h>
#include <Qt3DAnimation/Qt3DAnimation>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DAnimation/6.12.0/Qt3DAnimation/private/gltfimporter_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qjsonobject.h>
#include <QtCore/qstring.h>
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

//  from ../qt3d/src/animation/backend/gltfimporter.cpp, line 108, as local:gltfimporter.cpp:KEY_INPUT
#define KEY_INPUT                   QLatin1String("input")

//  from ../qt3d/src/animation/backend/gltfimporter.cpp, line 109, as local:gltfimporter.cpp:KEY_INTERPOLATION
#define KEY_INTERPOLATION           QLatin1String("interpolation")

//  from ../qt3d/src/animation/backend/gltfimporter.cpp, line 116, as local:gltfimporter.cpp:KEY_OUTPUT
#define KEY_OUTPUT                  QLatin1String("output")

//  from ../qt3d/src/animation/backend/gltfimporter.cpp, line 220, as _ZN13Qt3DAnimation9Animation12GLTFImporter7SamplerC1Ev
namespace Qt3DAnimation::Animation {
inline GLTFImporter::Sampler::Sampler()
    : inputAccessorIndex(-1)
    , outputAccessorIndex(-1)
    , interpolationMode(Linear)
{
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

//  from ../qt3d/src/animation/backend/gltfimporter.cpp, line 243, as _ZNK13Qt3DAnimation9Animation12GLTFImporter7Sampler23interpolationModeStringEv
namespace Qt3DAnimation::Animation {
inline QString GLTFImporter::Sampler::interpolationModeString() const
{
    switch (interpolationMode) {
    case Linear: return QLatin1String("LINEAR");
    case Step: return QLatin1String("STEP");
    case CatmullRomSpline: return QLatin1String("CATMULLROMSPLINE");
    case CubicSpline: return QLatin1String("CUBICSPLINE");
    }

    return QLatin1String("Unknown");
}
}  // namespace Qt3DAnimation::Animation
//  -----------------------------------------------------------------------

//  Qt3DAnimation::Animation::GLTFImporter::Sampler::Sampler()
extern "C" Q_DECL_EXPORT
Qt3DAnimation::Animation::GLTFImporter::Sampler *ritual_ZN13Qt3DAnimation9Animation12GLTFImporter7SamplerC1Ev() {
  return new Qt3DAnimation::Animation::GLTFImporter::Sampler();
}

//  Qt3DAnimation::Animation::GLTFImporter::Sampler::Sampler(const
//      QJsonObject &json)
extern "C" Q_DECL_EXPORT
Qt3DAnimation::Animation::GLTFImporter::Sampler *ritual_ZN13Qt3DAnimation9Animation12GLTFImporter7SamplerC1ERK11QJsonObject(
    const QJsonObject *json) {
  return new Qt3DAnimation::Animation::GLTFImporter::Sampler(*json);
}

//  QString Qt3DAnimation::Animation::GLTFImporter::Sampler::interpolationMod
//      eString() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK13Qt3DAnimation9Animation12GLTFImporter7Sampler23interpolationModeStringEv(
    const Qt3DAnimation::Animation::GLTFImporter::Sampler *self) {
  return new QString(self->interpolationModeString());
}

//  Qt3DAnimation::Animation::GLTFImporter::Sampler::~Sampler()
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation9Animation12GLTFImporter7SamplerD1Ev(
    Qt3DAnimation::Animation::GLTFImporter::Sampler *self) {
  delete self;
}
