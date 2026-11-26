//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DAnimation/6.12.0/Qt3DAnimation/private/gltfimporter_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <Qt3DAnimation/6.12.0/Qt3DAnimation/private/qt3danimation_global_p.h>
#include <Qt3DAnimation/Qt3DAnimation>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DAnimation/6.12.0/Qt3DAnimation/private/gltfimporter_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qjsondocument.h>
#include <QtCore/qjsonobject.h>
#include <QtCore/qbytearray.h>
#include <QtCore/QList>
#include <QtCore/QHash>
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
#include <QtCore/qloggingcategory.h>
#include <Qt3DAnimation/private/fcurve_p.h>
#include <Qt3DAnimation/private/bezierevaluator_p.h>
#include <QtCore/qjsonarray.h>
#include <QtCore/qjsonobject.h>
#include <QtCore/QLatin1String>
#include <Qt3DAnimation/private/functionrangefinder_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qt3d/src/animation/backend/gltfimporter.cpp, line 30, as local:gltfimporter.cpp:gltfTargetPropertyToChannelName
namespace Qt3DAnimation::Animation {
namespace {
inline QString gltfTargetPropertyToChannelName(const QString &propertyName)
{
    if (propertyName == QLatin1String("rotation"))
        return QLatin1String("Rotation");
    else if (propertyName == QLatin1String("translation"))
        return QLatin1String("Location");
    else if (propertyName == QLatin1String("scale"))
        return QLatin1String("Scale");

    qWarning() << "Unknown target property name";
    return QString();
}
}  // namespace
}  // namespace Qt3DAnimation::Animation

//  from ../qt3d/src/animation/backend/gltfimporter.cpp, line 43, as local:gltfimporter.cpp:gltfToQKeyFrameInterpolation
namespace Qt3DAnimation::Animation {
namespace {
inline QKeyFrame::InterpolationType gltfToQKeyFrameInterpolation(GLTFImporter::Sampler::InterpolationMode mode)
{
    switch (mode) {
    case GLTFImporter::Sampler::Linear:
        return QKeyFrame::LinearInterpolation;
    case GLTFImporter::Sampler::Step:
        return QKeyFrame::ConstantInterpolation;
    case GLTFImporter::Sampler::CubicSpline:
        return QKeyFrame::BezierInterpolation;
    case GLTFImporter::Sampler::CatmullRomSpline:
        // TODO: Implement this interpolation type
        qWarning() << "Unhandled interpolation type";
        return QKeyFrame::LinearInterpolation;
    }

    return QKeyFrame::LinearInterpolation;
}
}  // namespace
}  // namespace Qt3DAnimation::Animation

//  from ../qt3d/src/animation/backend/gltfimporter.cpp, line 92, as local:gltfimporter.cpp:KEY_ACCESSORS
#define KEY_ACCESSORS               QLatin1String("accessors")

//  from ../qt3d/src/animation/backend/gltfimporter.cpp, line 93, as local:gltfimporter.cpp:KEY_ANIMATIONS
#define KEY_ANIMATIONS              QLatin1String("animations")

//  from ../qt3d/src/animation/backend/gltfimporter.cpp, line 94, as local:gltfimporter.cpp:KEY_ASSET
#define KEY_ASSET                   QLatin1String("asset")

//  from ../qt3d/src/animation/backend/gltfimporter.cpp, line 96, as local:gltfimporter.cpp:KEY_BUFFERS
#define KEY_BUFFERS                 QLatin1String("buffers")

//  from ../qt3d/src/animation/backend/gltfimporter.cpp, line 97, as local:gltfimporter.cpp:KEY_BUFFER_VIEW
#define KEY_BUFFER_VIEW             QLatin1String("bufferView")

//  from ../qt3d/src/animation/backend/gltfimporter.cpp, line 98, as local:gltfimporter.cpp:KEY_BUFFER_VIEWS
#define KEY_BUFFER_VIEWS            QLatin1String("bufferViews")

//  from ../qt3d/src/animation/backend/gltfimporter.cpp, line 99, as local:gltfimporter.cpp:KEY_BYTE_LENGTH
#define KEY_BYTE_LENGTH             QLatin1String("byteLength")

//  from ../qt3d/src/animation/backend/gltfimporter.cpp, line 100, as local:gltfimporter.cpp:KEY_BYTE_OFFSET
#define KEY_BYTE_OFFSET             QLatin1String("byteOffset")

//  from ../qt3d/src/animation/backend/gltfimporter.cpp, line 104, as local:gltfimporter.cpp:KEY_CHILDREN
#define KEY_CHILDREN                QLatin1String("children")

//  from ../qt3d/src/animation/backend/gltfimporter.cpp, line 105, as local:gltfimporter.cpp:KEY_COMPONENT_TYPE
#define KEY_COMPONENT_TYPE          QLatin1String("componentType")

//  from ../qt3d/src/animation/backend/gltfimporter.cpp, line 106, as local:gltfimporter.cpp:KEY_COUNT
#define KEY_COUNT                   QLatin1String("count")

//  from ../qt3d/src/animation/backend/gltfimporter.cpp, line 111, as local:gltfimporter.cpp:KEY_MATRIX
#define KEY_MATRIX                  QLatin1String("matrix")

//  from ../qt3d/src/animation/backend/gltfimporter.cpp, line 113, as local:gltfimporter.cpp:KEY_NAME
#define KEY_NAME                    QLatin1String("name")

//  from ../qt3d/src/animation/backend/gltfimporter.cpp, line 115, as local:gltfimporter.cpp:KEY_NODES
#define KEY_NODES                   QLatin1String("nodes")

//  from ../qt3d/src/animation/backend/gltfimporter.cpp, line 118, as local:gltfimporter.cpp:KEY_ROTATION
#define KEY_ROTATION                QLatin1String("rotation")

//  from ../qt3d/src/animation/backend/gltfimporter.cpp, line 121, as local:gltfimporter.cpp:KEY_SCALE
#define KEY_SCALE                   QLatin1String("scale")

//  from ../qt3d/src/animation/backend/gltfimporter.cpp, line 123, as local:gltfimporter.cpp:KEY_SKINS
#define KEY_SKINS                   QLatin1String("skins")

//  from ../qt3d/src/animation/backend/gltfimporter.cpp, line 125, as local:gltfimporter.cpp:KEY_TRANSLATION
#define KEY_TRANSLATION             QLatin1String("translation")

//  from ../qt3d/src/animation/backend/gltfimporter.cpp, line 126, as local:gltfimporter.cpp:KEY_TYPE
#define KEY_TYPE                    QLatin1String("type")

//  from ../qt3d/src/animation/backend/gltfimporter.cpp, line 127, as local:gltfimporter.cpp:KEY_URI
#define KEY_URI                     QLatin1String("uri")

//  from ../qt3d/src/animation/backend/gltfimporter.cpp, line 128, as local:gltfimporter.cpp:KEY_VERSION
#define KEY_VERSION                 QLatin1String("version")

//  from ../qt3d/src/animation/backend/gltfimporter.cpp, line 136, as _ZN13Qt3DAnimation9Animation12GLTFImporter10BufferDataC1ERK11QJsonObject
namespace Qt3DAnimation::Animation {
inline GLTFImporter::BufferData::BufferData(const QJsonObject &json)
    : byteLength(json.value(KEY_BYTE_LENGTH).toInt())
    , path(json.value(KEY_URI).toString())
    , data()
{
}
}  // namespace Qt3DAnimation::Animation

//  from ../qt3d/src/animation/animationlogging.cpp, line 13, as _ZN13Qt3DAnimation9Animation4JobsEv
namespace Qt3DAnimation::Animation {
inline const QLoggingCategory &Jobs()
{
    static const QLoggingCategory category("Qt3D.Animation.Jobs", QtWarningMsg);
    return category;
}
}  // namespace Qt3DAnimation::Animation

//  from ../qt3d/src/animation/backend/fcurve.cpp, line 128, as _ZN13Qt3DAnimation9Animation6FCurve14appendKeyframeEfRKNS0_8KeyframeE
namespace Qt3DAnimation::Animation {
inline void FCurve::appendKeyframe(float localTime, const Keyframe &keyframe)
{
    m_localTimes.append(localTime);
    m_keyframes.append(keyframe);
}
}  // namespace Qt3DAnimation::Animation

//  from ../qt3d/src/animation/backend/fcurve.cpp, line 16, as _ZN13Qt3DAnimation9Animation6FCurveC1Ev
namespace Qt3DAnimation::Animation {
inline FCurve::FCurve()
    : m_rangeFinder(&m_localTimes)
{
}
}  // namespace Qt3DAnimation::Animation

//  from ../qt3d/src/animation/backend/functionrangefinder.cpp, line 39, as _ZN13Qt3DAnimation9Animation19FunctionRangeFinderC1EP5QListIfE
namespace Qt3DAnimation::Animation {
inline FunctionRangeFinder::FunctionRangeFinder(QList<float> *x)
    : m_x(x)
    , m_previousLowerBound(0)
    , m_correlated(0)
    , m_rangeSize(2)
    , m_correlationThreshold(1)
    , m_ascending(true)
{
    updateAutomaticCorrelationThreshold();
    if (!m_x->isEmpty())
        m_ascending = (m_x->last() >= m_x->first());
}
}  // namespace Qt3DAnimation::Animation

//  from ../qt3d/src/animation/backend/gltfimporter.cpp, line 401, as _ZN13Qt3DAnimation9Animation12GLTFImporterC1Ev
namespace Qt3DAnimation::Animation {
inline GLTFImporter::GLTFImporter()
{
}
}  // namespace Qt3DAnimation::Animation

//  from ../qt3d/src/animation/backend/gltfimporter.cpp, line 431, as _ZNK13Qt3DAnimation9Animation12GLTFImporter19createAnimationDataExRK7QString
namespace Qt3DAnimation::Animation {
inline GLTFImporter::AnimationNameAndChannels GLTFImporter::createAnimationData(qsizetype animationIndex, const QString &animationName) const
{
    AnimationNameAndChannels nameAndChannels;
    if (m_animations.isEmpty()) {
        qCWarning(Jobs) << "File does not contain any animation data";
        return nameAndChannels;
    }

    if (m_animations.size() == 1) {
        animationIndex = 0;
    } else if (animationIndex < 0 && !animationName.isEmpty()) {
        for (qsizetype i = 0; i < m_animations.size(); ++i) {
            if (m_animations[i].name == animationName) {
                animationIndex = i;
                break;
            }
        }
    }

    if (animationIndex < 0 || animationIndex >= m_animations.size()) {
        qCWarning(Jobs) << "Invalid animation index. Skipping.";
        return nameAndChannels;
    }
    const Animation &animation = m_animations[animationIndex];
    nameAndChannels.name = animation.name;

    // Create node index to joint index lookup tables for each skin
    QList<QHash<qsizetype, qsizetype>> nodeIndexToJointIndexMaps;
    nodeIndexToJointIndexMaps.reserve(m_skins.size());
    for (const auto &skin : m_skins)
        nodeIndexToJointIndexMaps.push_back(createNodeIndexToJointIndexMap(skin));

    for (const auto &channel : animation.channels) {
        Qt3DAnimation::Animation::Channel outputChannel;
        outputChannel.name = gltfTargetPropertyToChannelName(channel.targetProperty);

        // Find the node index to joint index map that contains the target node and
        // look up the joint index from it. If no such map is found, the target joint
        // is not part of a skeleton and so we can just set the jointIndex to -1.
        qsizetype jointIndex = -1;
        for (const auto &map : nodeIndexToJointIndexMaps) {
            const auto result = map.find(channel.targetNodeIndex);
            if (result != map.cend()) {
                jointIndex = result.value();
                break;
            }
        }
        outputChannel.jointIndex = jointIndex;

        const auto &sampler = animation.samplers[channel.samplerIndex];
        const auto interpolationType = gltfToQKeyFrameInterpolation(sampler.interpolationMode);

        if (sampler.inputAccessorIndex == -1 || sampler.outputAccessorIndex == -1) {
            qWarning() << "Skipping channel due to invalid accessor indices in the sampler" << Qt::endl;
            continue;
        }

        const auto &inputAccessor = m_accessors[sampler.inputAccessorIndex];
        const auto &outputAccessor = m_accessors[sampler.outputAccessorIndex];

        if (inputAccessor.type != Qt3DCore::QAttribute::Float) {
            qWarning() << "Input accessor has wrong data type. Skipping channel.";
            continue;
        }

        if (outputAccessor.type != Qt3DCore::QAttribute::Float) {
            qWarning() << "Output accessor has wrong data type. Skipping channel.";
            continue;
        }

        if (inputAccessor.count != outputAccessor.count) {
            qWarning() << "Warning!!! Input accessor has" << inputAccessor.count
                       << "entries and output accessor has" << outputAccessor.count
                       << "entries. They should match. Please check your data.";
            continue;
        }

        // TODO: Allow Qt 3D animation data to share timestamps between multiple
        // channel components. I.e. allow key frame values of composite types.
        // Doesn't give as much freedom but more efficient at runtime.

        // Get the key frame times first as these are common to all components of the
        // key frame values.
        const int keyFrameCount = inputAccessor.count;
        QVector<float> keyframeTimes(keyFrameCount);
        for (int i = 0; i < keyFrameCount; ++i) {
            const auto rawTimestamp = accessorData(sampler.inputAccessorIndex, i);
            keyframeTimes[i] = *reinterpret_cast<const float*>(rawTimestamp.data);
        }

        // Create a ChannelComponent for each component of the output sampler and
        // populate it with data.
        switch (outputAccessor.dataSize) {
        // TODO: Handle other types as needed
        case 3: {
            // vec3
            const int componentCount = 3;

            // Construct the channel component names and add component to the channel
            const QStringList suffixes
                    = (QStringList() << QLatin1String("X") << QLatin1String("Y") << QLatin1String("Z"));
            outputChannel.channelComponents.resize(componentCount);
            for (int componentIndex = 0; componentIndex < componentCount; ++componentIndex) {
                outputChannel.channelComponents[componentIndex].name
                        = QString(QLatin1String("%1 %2")).arg(outputChannel.name,
                                                              suffixes[componentIndex]);
            }

            // Populate the fcurves in the channel components
            for (int i = 0; i < keyFrameCount; ++i) {
                const auto rawKeyframeValue = accessorData(sampler.outputAccessorIndex, i);
                QVector3D v;
                memcpy(&v, rawKeyframeValue.data, rawKeyframeValue.byteLength);

                for (int componentIndex = 0; componentIndex < componentCount; ++componentIndex) {
                    Keyframe keyFrame;
                    keyFrame.interpolation = interpolationType;
                    keyFrame.value = v[componentIndex];
                    outputChannel.channelComponents[componentIndex].fcurve.appendKeyframe(keyframeTimes[i], keyFrame);
                }
            }

            break;
        } // case 3

        case 4: {
            // vec4 or quaternion
            const int componentCount = 4;

            // Construct the channel component names and add component to the channel
            const QStringList rotationSuffixes = (QStringList()
                << QLatin1String("X") << QLatin1String("Y") << QLatin1String("Z") << QLatin1String("W"));
            const QStringList standardSuffixes = (QStringList()
                << QLatin1String("X") << QLatin1String("Y") << QLatin1String("Z"));
            const QStringList suffixes = (channel.targetProperty == QLatin1String("rotation"))
                   ? rotationSuffixes : standardSuffixes;
            outputChannel.channelComponents.resize(componentCount);
            for (int componentIndex = 0; componentIndex < componentCount; ++componentIndex) {
                outputChannel.channelComponents[componentIndex].name
                        = QString(QLatin1String("%1 %2")).arg(outputChannel.name,
                                                              suffixes[componentIndex]);
            }

            // Populate the fcurves in the channel components
            for (int i = 0; i < keyFrameCount; ++i) {
                const auto rawKeyframeValue = accessorData(sampler.outputAccessorIndex, i);
                QVector4D v;
                memcpy(&v, rawKeyframeValue.data, rawKeyframeValue.byteLength);

                for (int componentIndex = 0; componentIndex < componentCount; ++componentIndex) {
                    Keyframe keyFrame;
                    keyFrame.interpolation = interpolationType;
                    keyFrame.value = v[componentIndex];
                    outputChannel.channelComponents[componentIndex].fcurve.appendKeyframe(keyframeTimes[i], keyFrame);
                }
            }

            break;
        } // case 4
        }

        nameAndChannels.channels.push_back(outputChannel);
    }

    return nameAndChannels;
}
}  // namespace Qt3DAnimation::Animation

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

//  from ../qt3d/src/animation/backend/gltfimporter.cpp, line 359, as _ZN13Qt3DAnimation9Animation12GLTFImporter16accessorTypeSizeEN8Qt3DCore10QAttribute14VertexBaseTypeE
namespace Qt3DAnimation::Animation {
inline uint GLTFImporter::accessorTypeSize(Qt3DCore::QAttribute::VertexBaseType componentType)
{
    switch (componentType) {
    case Qt3DCore::QAttribute::Byte:
    case Qt3DCore::QAttribute::UnsignedByte:
         return 1;

    case Qt3DCore::QAttribute::Short:
    case Qt3DCore::QAttribute::UnsignedShort:
        return 2;

    case Qt3DCore::QAttribute::Int:
    case Qt3DCore::QAttribute::Float:
        return 4;

    default:
        qWarning("Unhandled accessor data type %d", componentType);
        return 0;
    }
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

//  from ../qt3d/src/animation/backend/gltfimporter.cpp, line 623, as _ZN13Qt3DAnimation9Animation12GLTFImporter11setBasePathERK7QString
namespace Qt3DAnimation::Animation {
inline void GLTFImporter::setBasePath(const QString &path)
{
    m_basePath = path;
}
}  // namespace Qt3DAnimation::Animation

//  from ../qt3d/src/animation/backend/gltfimporter.cpp, line 628, as _ZN13Qt3DAnimation9Animation12GLTFImporter7setJSONERK13QJsonDocument
namespace Qt3DAnimation::Animation {
inline bool GLTFImporter::setJSON(const QJsonDocument &json)
{
    if (!json.isObject())
        return false;
    m_json = json;
    cleanup();
    return true;
}
}  // namespace Qt3DAnimation::Animation

//  from ../qt3d/src/animation/backend/gltfimporter.cpp, line 687, as _ZN13Qt3DAnimation9Animation12GLTFImporter7cleanupEv
namespace Qt3DAnimation::Animation {
inline void GLTFImporter::cleanup()
{
    m_accessors.clear();
    m_bufferViews.clear();
    m_bufferDatas.clear();
}
}  // namespace Qt3DAnimation::Animation

//  from ../qt3d/src/animation/backend/gltfimporter.cpp, line 421, as _ZNK13Qt3DAnimation9Animation12GLTFImporter30createNodeIndexToJointIndexMapERKNS1_4SkinE
namespace Qt3DAnimation::Animation {
inline QHash<qsizetype, qsizetype> GLTFImporter::createNodeIndexToJointIndexMap(const Skin &skin) const
{
    const qsizetype jointCount = skin.jointNodeIndices.size();
    QHash<qsizetype, qsizetype> nodeIndexToJointIndexMap;
    nodeIndexToJointIndexMap.reserve(jointCount);
    for (qsizetype i = 0; i < jointCount; ++i)
        nodeIndexToJointIndexMap.insert(skin.jointNodeIndices[i], i);
    return nodeIndexToJointIndexMap;
}
}  // namespace Qt3DAnimation::Animation

//  from ../qt3d/src/animation/backend/gltfimporter.cpp, line 694, as _ZN13Qt3DAnimation9Animation12GLTFImporter17processJSONBufferERK11QJsonObject
namespace Qt3DAnimation::Animation {
inline bool GLTFImporter::processJSONBuffer(const QJsonObject &json)
{
    // Store buffer details and load data into memory
    BufferData buffer(json);
    buffer.data = resolveLocalData(buffer.path);
    if (buffer.data.isEmpty())
        return false;

    m_bufferDatas.push_back(buffer);
    return true;
}
}  // namespace Qt3DAnimation::Animation

//  from ../qt3d/src/animation/backend/gltfimporter.cpp, line 790, as _ZN13Qt3DAnimation9Animation12GLTFImporter20setupNodeParentLinksEv
namespace Qt3DAnimation::Animation {
inline void GLTFImporter::setupNodeParentLinks()
{
    const qsizetype nodeCount = m_nodes.size();
    for (qsizetype i = 0; i < nodeCount; ++i) {
        const Node &node = m_nodes[i];
        const QList<qsizetype> &childNodeIndices = node.childNodeIndices;
        for (const auto childNodeIndex : childNodeIndices) {
            Q_ASSERT(childNodeIndex < m_nodes.size());
            Node &childNode = m_nodes[childNodeIndex];
            Q_ASSERT(childNode.parentNodeIndex == -1);
            childNode.parentNodeIndex = i;
        }
    }
}
}  // namespace Qt3DAnimation::Animation

//  from ../qt3d/src/animation/backend/gltfimporter.cpp, line 805, as _ZNK13Qt3DAnimation9Animation12GLTFImporter16resolveLocalDataERK7QString
namespace Qt3DAnimation::Animation {
inline QByteArray GLTFImporter::resolveLocalData(const QString &path) const
{
    QDir d(m_basePath);
    Q_ASSERT(d.exists());

    QString absPath = d.absoluteFilePath(path);
    QFile f(absPath);
    if (!f.open(QIODevice::ReadOnly))
        return QByteArray();
    return f.readAll();
}
}  // namespace Qt3DAnimation::Animation

//  from ../qt3d/src/animation/backend/gltfimporter.cpp, line 598, as _ZNK13Qt3DAnimation9Animation12GLTFImporter12accessorDataEii
namespace Qt3DAnimation::Animation {
inline GLTFImporter::RawData GLTFImporter::accessorData(int accessorIndex, int index) const
{
    const AccessorData &accessor = m_accessors[accessorIndex];
    const BufferView &bufferView = m_bufferViews[accessor.bufferViewIndex];
    const BufferData &bufferData = m_bufferDatas[bufferView.bufferIndex];
    const QByteArray &ba = bufferData.data;
    const char *rawData = ba.constData() + bufferView.byteOffset + accessor.byteOffset;

    const uint typeSize = accessorTypeSize(accessor.type);
    const qsizetype stride = (accessor.byteStride == 0)
            ? accessor.dataSize * typeSize
            : accessor.byteStride;

    const char* data = rawData + index * stride;
    if (data - rawData > ba.size()) {
        qWarning("Attempting to access data beyond end of buffer");
        return RawData{ nullptr, 0 };
    }

    const quint64 byteLength = accessor.dataSize * typeSize;
    RawData rd{ data, byteLength };

    return rd;
}
}  // namespace Qt3DAnimation::Animation
//  -----------------------------------------------------------------------

//  Qt3DAnimation::Animation::GLTFImporter::GLTFImporter()
extern "C" Q_DECL_EXPORT
Qt3DAnimation::Animation::GLTFImporter *ritual_ZN13Qt3DAnimation9Animation12GLTFImporterC1Ev() {
  return new Qt3DAnimation::Animation::GLTFImporter();
}

//  const QList<Animation>
//      Qt3DAnimation::Animation::GLTFImporter::animations() const
extern "C" Q_DECL_EXPORT
QList<Qt3DAnimation::Animation::GLTFImporter::Animation> *ritual_ZNK13Qt3DAnimation9Animation12GLTFImporter10animationsEv(
    const Qt3DAnimation::Animation::GLTFImporter *self) {
  return new QList<Qt3DAnimation::Animation::GLTFImporter::Animation>(
      self->animations());
}

//  AnimationNameAndChannels
//      Qt3DAnimation::Animation::GLTFImporter::createAnimationData(qsizetype
//      animationIndex, const QString &animationName) const
extern "C" Q_DECL_EXPORT
Qt3DAnimation::Animation::GLTFImporter::AnimationNameAndChannels *ritual_ZNK13Qt3DAnimation9Animation12GLTFImporter19createAnimationDataExRK7QString(
    const Qt3DAnimation::Animation::GLTFImporter *self,
    qsizetype animationIndex,
    const QString *animationName) {
  return new Qt3DAnimation::Animation::GLTFImporter::AnimationNameAndChannels(
      self->createAnimationData(
          animationIndex,
          *animationName));
}

//  Qt3DCore::QAttribute::VertexBaseType
//      Qt3DAnimation::Animation::GLTFImporter::accessorTypeFromJSON(int
//      componentType)
extern "C" Q_DECL_EXPORT
Qt3DCore::QAttribute::VertexBaseType ritual_ZN13Qt3DAnimation9Animation12GLTFImporter20accessorTypeFromJSONEi(
    int componentType) {
  return Qt3DAnimation::Animation::GLTFImporter::accessorTypeFromJSON(
      componentType);
}

//  uint Qt3DAnimation::Animation::GLTFImporter::accessorTypeSize(Qt3DCore::Q
//      Attribute::VertexBaseType componentType)
extern "C" Q_DECL_EXPORT
uint ritual_ZN13Qt3DAnimation9Animation12GLTFImporter16accessorTypeSizeEN8Qt3DCore10QAttribute14VertexBaseTypeE(
    Qt3DCore::QAttribute::VertexBaseType componentType) {
  return Qt3DAnimation::Animation::GLTFImporter::accessorTypeSize(
      componentType);
}

//  uint
//      Qt3DAnimation::Animation::GLTFImporter::accessorDataSizeFromJson(cons
//      t QString &type)
extern "C" Q_DECL_EXPORT
uint ritual_ZN13Qt3DAnimation9Animation12GLTFImporter24accessorDataSizeFromJsonERK7QString(
    const QString *type) {
  return Qt3DAnimation::Animation::GLTFImporter::accessorDataSizeFromJson(
      *type);
}

//  void Qt3DAnimation::Animation::GLTFImporter::setBasePath(const QString
//      &path)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation9Animation12GLTFImporter11setBasePathERK7QString(
    Qt3DAnimation::Animation::GLTFImporter *self,
    const QString *path) {
  self->setBasePath(*path);
}

//  bool Qt3DAnimation::Animation::GLTFImporter::setJSON(const QJsonDocument
//      &json)
extern "C" Q_DECL_EXPORT
bool ritual_ZN13Qt3DAnimation9Animation12GLTFImporter7setJSONERK13QJsonDocument(
    Qt3DAnimation::Animation::GLTFImporter *self,
    const QJsonDocument *json) {
  return self->setJSON(*json);
}

//  void Qt3DAnimation::Animation::GLTFImporter::cleanup()
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation9Animation12GLTFImporter7cleanupEv(
    Qt3DAnimation::Animation::GLTFImporter *self) {
  self->cleanup();
}

//  QHash<qsizetype, qsizetype> Qt3DAnimation::Animation::GLTFImporter::creat
//      eNodeIndexToJointIndexMap(const Skin &skin) const
extern "C" Q_DECL_EXPORT
QHash<qsizetype, qsizetype> *ritual_ZNK13Qt3DAnimation9Animation12GLTFImporter30createNodeIndexToJointIndexMapERKNS1_4SkinE(
    const Qt3DAnimation::Animation::GLTFImporter *self,
    const Qt3DAnimation::Animation::GLTFImporter::Skin *skin) {
  return new QHash<qsizetype, qsizetype>(
      self->createNodeIndexToJointIndexMap(
          *skin));
}

//  bool Qt3DAnimation::Animation::GLTFImporter::processJSONBuffer(const
//      QJsonObject &json)
extern "C" Q_DECL_EXPORT
bool ritual_ZN13Qt3DAnimation9Animation12GLTFImporter17processJSONBufferERK11QJsonObject(
    Qt3DAnimation::Animation::GLTFImporter *self,
    const QJsonObject *json) {
  return self->processJSONBuffer(*json);
}

//  void Qt3DAnimation::Animation::GLTFImporter::setupNodeParentLinks()
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation9Animation12GLTFImporter20setupNodeParentLinksEv(
    Qt3DAnimation::Animation::GLTFImporter *self) {
  self->setupNodeParentLinks();
}

//  QByteArray Qt3DAnimation::Animation::GLTFImporter::resolveLocalData(const
//      QString &path) const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK13Qt3DAnimation9Animation12GLTFImporter16resolveLocalDataERK7QString(
    const Qt3DAnimation::Animation::GLTFImporter *self,
    const QString *path) {
  return new QByteArray(self->resolveLocalData(*path));
}

//  RawData Qt3DAnimation::Animation::GLTFImporter::accessorData(int
//      accessorIndex, int index) const
extern "C" Q_DECL_EXPORT
Qt3DAnimation::Animation::GLTFImporter::RawData *ritual_ZNK13Qt3DAnimation9Animation12GLTFImporter12accessorDataEii(
    const Qt3DAnimation::Animation::GLTFImporter *self,
    int accessorIndex,
    int index) {
  return new Qt3DAnimation::Animation::GLTFImporter::RawData(
      self->accessorData(
          accessorIndex,
          index));
}

//  Qt3DAnimation::Animation::GLTFImporter::~GLTFImporter()
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation9Animation12GLTFImporterD1Ev(
    Qt3DAnimation::Animation::GLTFImporter *self) {
  delete self;
}

//  a QList<Qt3DAnimation::Animation::GLTFImporter::Animation> a ritual of
//      Qt3DAnimation::Animation::GLTFImporter gave
extern "C" Q_DECL_EXPORT
void ritual_drop_Qt3DAnimation_Animation_GLTFImporter__QList_Qt3DAnimation_Animation_GLTFImporter_Animation(
    QList<Qt3DAnimation::Animation::GLTFImporter::Animation> *self) {
  delete self;
}

//  a QHash<qsizetype, qsizetype> a ritual of
//      Qt3DAnimation::Animation::GLTFImporter gave
extern "C" Q_DECL_EXPORT
void ritual_drop_Qt3DAnimation_Animation_GLTFImporter__QHash_qsizetype_qsizetype(
    QHash<qsizetype, qsizetype> *self) {
  delete self;
}

//  a Qt3DAnimation::Animation::GLTFImporter::RawData a ritual of
//      Qt3DAnimation::Animation::GLTFImporter gave
extern "C" Q_DECL_EXPORT
void ritual_drop_Qt3DAnimation_Animation_GLTFImporter__Qt3DAnimation_Animation_GLTFImporter_RawData(
    Qt3DAnimation::Animation::GLTFImporter::RawData *self) {
  delete self;
}
