//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/6.12.0/Qt3DRender/private/gltfskeletonloader_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <Qt3DRender/6.12.0/Qt3DRender/private/qt3drender_global_p.h>
#include <Qt3DRender/Qt3DRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DRender/6.12.0/Qt3DRender/private/gltfskeletonloader_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DRender/6.12.0/Qt3DRender/private/skeletondata_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qjsondocument.h>
#include <QtCore/qjsonobject.h>
#include <QtCore/qbytearray.h>
#include <QtGui/qmatrix4x4.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DRender/private/gltfskeletonloader_p.h>
#include <QtGui/qopengl.h>
#include <QtCore/qdir.h>
#include <QtCore/qfile.h>
#include <QtCore/qfileinfo.h>
#include <QtCore/qiodevice.h>
#include <QtCore/qjsonarray.h>
#include <QtCore/qjsonobject.h>
#include <QtCore/qjsonvalue.h>
#include <QtCore/qversionnumber.h>
#include <Qt3DRender/private/renderlogging_p.h>
#include <Qt3DCore/private/qmath3d_p.h>
#include <Qt3DCore/private/qloadgltf_p.h>
#include <QtGui/qquaternion.h>
#include <QtCore/qloggingcategory.h>
#include <Qt3DRender/private/skeletondata_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qt3d/src/render/geometry/gltfskeletonloader.cpp, line 62, as local:gltfskeletonloader.cpp:KEY_ACCESSORS
#define KEY_ACCESSORS               QLatin1String("accessors")

//  from ../qt3d/src/render/geometry/gltfskeletonloader.cpp, line 63, as local:gltfskeletonloader.cpp:KEY_ASSET
#define KEY_ASSET                   QLatin1String("asset")

//  from ../qt3d/src/render/geometry/gltfskeletonloader.cpp, line 64, as local:gltfskeletonloader.cpp:KEY_BUFFER
#define KEY_BUFFER                  QLatin1String("buffer")

//  from ../qt3d/src/render/geometry/gltfskeletonloader.cpp, line 65, as local:gltfskeletonloader.cpp:KEY_BUFFERS
#define KEY_BUFFERS                 QLatin1String("buffers")

//  from ../qt3d/src/render/geometry/gltfskeletonloader.cpp, line 66, as local:gltfskeletonloader.cpp:KEY_BUFFER_VIEW
#define KEY_BUFFER_VIEW             QLatin1String("bufferView")

//  from ../qt3d/src/render/geometry/gltfskeletonloader.cpp, line 67, as local:gltfskeletonloader.cpp:KEY_BUFFER_VIEWS
#define KEY_BUFFER_VIEWS            QLatin1String("bufferViews")

//  from ../qt3d/src/render/geometry/gltfskeletonloader.cpp, line 68, as local:gltfskeletonloader.cpp:KEY_BYTE_LENGTH
#define KEY_BYTE_LENGTH             QLatin1String("byteLength")

//  from ../qt3d/src/render/geometry/gltfskeletonloader.cpp, line 69, as local:gltfskeletonloader.cpp:KEY_BYTE_OFFSET
#define KEY_BYTE_OFFSET             QLatin1String("byteOffset")

//  from ../qt3d/src/render/geometry/gltfskeletonloader.cpp, line 72, as local:gltfskeletonloader.cpp:KEY_CHILDREN
#define KEY_CHILDREN                QLatin1String("children")

//  from ../qt3d/src/render/geometry/gltfskeletonloader.cpp, line 73, as local:gltfskeletonloader.cpp:KEY_COMPONENT_TYPE
#define KEY_COMPONENT_TYPE          QLatin1String("componentType")

//  from ../qt3d/src/render/geometry/gltfskeletonloader.cpp, line 74, as local:gltfskeletonloader.cpp:KEY_COUNT
#define KEY_COUNT                   QLatin1String("count")

//  from ../qt3d/src/render/geometry/gltfskeletonloader.cpp, line 77, as local:gltfskeletonloader.cpp:KEY_MATRIX
#define KEY_MATRIX                  QLatin1String("matrix")

//  from ../qt3d/src/render/geometry/gltfskeletonloader.cpp, line 79, as local:gltfskeletonloader.cpp:KEY_NAME
#define KEY_NAME                    QLatin1String("name")

//  from ../qt3d/src/render/geometry/gltfskeletonloader.cpp, line 80, as local:gltfskeletonloader.cpp:KEY_NODES
#define KEY_NODES                   QLatin1String("nodes")

//  from ../qt3d/src/render/geometry/gltfskeletonloader.cpp, line 81, as local:gltfskeletonloader.cpp:KEY_ROTATION
#define KEY_ROTATION                QLatin1String("rotation")

//  from ../qt3d/src/render/geometry/gltfskeletonloader.cpp, line 82, as local:gltfskeletonloader.cpp:KEY_SCALE
#define KEY_SCALE                   QLatin1String("scale")

//  from ../qt3d/src/render/geometry/gltfskeletonloader.cpp, line 84, as local:gltfskeletonloader.cpp:KEY_SKINS
#define KEY_SKINS                   QLatin1String("skins")

//  from ../qt3d/src/render/geometry/gltfskeletonloader.cpp, line 86, as local:gltfskeletonloader.cpp:KEY_TRANSLATION
#define KEY_TRANSLATION             QLatin1String("translation")

//  from ../qt3d/src/render/geometry/gltfskeletonloader.cpp, line 87, as local:gltfskeletonloader.cpp:KEY_TYPE
#define KEY_TYPE                    QLatin1String("type")

//  from ../qt3d/src/render/geometry/gltfskeletonloader.cpp, line 88, as local:gltfskeletonloader.cpp:KEY_URI
#define KEY_URI                     QLatin1String("uri")

//  from ../qt3d/src/render/geometry/gltfskeletonloader.cpp, line 89, as local:gltfskeletonloader.cpp:KEY_VERSION
#define KEY_VERSION                 QLatin1String("version")

//  from ../qt3d/src/render/geometry/gltfskeletonloader.cpp, line 97, as _ZN10Qt3DRender6Render18GLTFSkeletonLoader10BufferDataC1ERK11QJsonObject
namespace Qt3DRender::Render {
using namespace Qt3DCore;
inline GLTFSkeletonLoader::BufferData::BufferData(const QJsonObject &json)
    : byteLength(json.value(KEY_BYTE_LENGTH).toInt())
    , path(json.value(KEY_URI).toString())
    , data()
{
}
}  // namespace Qt3DRender::Render

//  from ../qt3d/src/render/renderlogging.cpp, line 15, as _ZN10Qt3DRender6Render4JobsEv
namespace Qt3DRender::Render {
inline const QLoggingCategory &Jobs()
{
    static const QLoggingCategory category("Qt3D.Renderer.Jobs", QtWarningMsg);
    return category;
}
}  // namespace Qt3DRender::Render

//  from ../qt3d/src/render/geometry/skeletondata.cpp, line 15, as _ZN10Qt3DRender6Render12SkeletonData7reserveEi
namespace Qt3DRender::Render {
inline void SkeletonData::reserve(int size)
{
    joints.reserve(size);
    localPoses.reserve(size);
    jointNames.reserve(size);
}
}  // namespace Qt3DRender::Render

//  from ../qt3d/src/render/geometry/skeletondata.cpp, line 11, as _ZN10Qt3DRender6Render12SkeletonDataC1Ev
namespace Qt3DRender::Render {
inline SkeletonData::SkeletonData()
{
}
}  // namespace Qt3DRender::Render

//  from ../qt3d/src/render/geometry/gltfskeletonloader.cpp, line 285, as _ZN10Qt3DRender6Render18GLTFSkeletonLoaderC1Ev
namespace Qt3DRender::Render {
using namespace Qt3DCore;
inline GLTFSkeletonLoader::GLTFSkeletonLoader()
{
}
}  // namespace Qt3DRender::Render

//  from ../qt3d/src/render/geometry/gltfskeletonloader.cpp, line 305, as _ZN10Qt3DRender6Render18GLTFSkeletonLoader14createSkeletonERK7QString
namespace Qt3DRender::Render {
using namespace Qt3DCore;
inline SkeletonData GLTFSkeletonLoader::createSkeleton(const QString &skeletonName)
{
    if (m_skins.empty()) {
        qCWarning(Jobs, "glTF file does not contain any skins");
        return SkeletonData();
    }

    auto skin = m_skins.begin();
    if (!skeletonName.isNull()) {
        const auto result = std::find_if(m_skins.begin(), m_skins.end(),
            [skeletonName](const Skin &skin) { return skin.name == skeletonName; });
        if (result != m_skins.end())
            skin = result;
    }

    Q_ASSERT(skin != m_skins.end());
    return createSkeletonFromSkin(*skin);
}
}  // namespace Qt3DRender::Render

//  from ../qt3d/src/render/geometry/gltfskeletonloader.cpp, line 223, as _ZN10Qt3DRender6Render18GLTFSkeletonLoader20accessorTypeFromJSONEi
namespace Qt3DRender::Render {
using namespace Qt3DCore;
inline QAttribute::VertexBaseType GLTFSkeletonLoader::accessorTypeFromJSON(int componentType)
{
    if (componentType == GL_BYTE)
        return QAttribute::Byte;
    else if (componentType == GL_UNSIGNED_BYTE)
        return QAttribute::UnsignedByte;
    else if (componentType == GL_SHORT)
        return QAttribute::Short;
    else if (componentType == GL_UNSIGNED_SHORT)
        return QAttribute::UnsignedShort;
    else if (componentType == GL_UNSIGNED_INT)
        return QAttribute::UnsignedInt;
    else if (componentType == GL_FLOAT)
        return QAttribute::Float;

    // There shouldn't be an invalid case here
    qCWarning(Jobs, "unsupported accessor type %d", componentType);
    return QAttribute::Float;
}
}  // namespace Qt3DRender::Render

//  from ../qt3d/src/render/geometry/gltfskeletonloader.cpp, line 243, as _ZN10Qt3DRender6Render18GLTFSkeletonLoader16accessorTypeSizeEN8Qt3DCore10QAttribute14VertexBaseTypeE
namespace Qt3DRender::Render {
using namespace Qt3DCore;
inline uint GLTFSkeletonLoader::accessorTypeSize(QAttribute::VertexBaseType componentType)
{
    switch (componentType) {
    case QAttribute::Byte:
    case QAttribute::UnsignedByte:
         return 1;

    case QAttribute::Short:
    case QAttribute::UnsignedShort:
        return 2;

    case QAttribute::Int:
    case QAttribute::Float:
        return 4;

    default:
        qCWarning(Jobs, "Unhandled accessor data type %d", componentType);
        return 0;
    }
}
}  // namespace Qt3DRender::Render

//  from ../qt3d/src/render/geometry/gltfskeletonloader.cpp, line 264, as _ZN10Qt3DRender6Render18GLTFSkeletonLoader24accessorDataSizeFromJsonERK7QString
namespace Qt3DRender::Render {
using namespace Qt3DCore;
inline uint GLTFSkeletonLoader::accessorDataSizeFromJson(const QString &type)
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
}  // namespace Qt3DRender::Render

//  from ../qt3d/src/render/geometry/gltfskeletonloader.cpp, line 387, as _ZN10Qt3DRender6Render18GLTFSkeletonLoader11setBasePathERK7QString
namespace Qt3DRender::Render {
using namespace Qt3DCore;
inline void GLTFSkeletonLoader::setBasePath(const QString &path)
{
    m_basePath = path;
}
}  // namespace Qt3DRender::Render

//  from ../qt3d/src/render/geometry/gltfskeletonloader.cpp, line 392, as _ZN10Qt3DRender6Render18GLTFSkeletonLoader7setJSONERK13QJsonDocument
namespace Qt3DRender::Render {
using namespace Qt3DCore;
inline bool GLTFSkeletonLoader::setJSON(const QJsonDocument &json)
{
    if (!json.isObject())
        return false;
    m_json = json;
    cleanup();
    return true;
}
}  // namespace Qt3DRender::Render

//  from ../qt3d/src/render/geometry/gltfskeletonloader.cpp, line 447, as _ZN10Qt3DRender6Render18GLTFSkeletonLoader7cleanupEv
namespace Qt3DRender::Render {
using namespace Qt3DCore;
inline void GLTFSkeletonLoader::cleanup()
{
    m_accessors.clear();
    m_bufferViews.clear();
    m_bufferDatas.clear();
}
}  // namespace Qt3DRender::Render

//  from ../qt3d/src/render/geometry/gltfskeletonloader.cpp, line 454, as _ZN10Qt3DRender6Render18GLTFSkeletonLoader17processJSONBufferERK11QJsonObject
namespace Qt3DRender::Render {
using namespace Qt3DCore;
inline bool GLTFSkeletonLoader::processJSONBuffer(const QJsonObject &json)
{
    // Store buffer details and load data into memory
    BufferData buffer(json);
    buffer.data = resolveLocalData(buffer.path);
    if (buffer.data.isEmpty())
        return false;

    m_bufferDatas.push_back(buffer);
    return true;
}
}  // namespace Qt3DRender::Render

//  from ../qt3d/src/render/geometry/gltfskeletonloader.cpp, line 522, as _ZN10Qt3DRender6Render18GLTFSkeletonLoader20setupNodeParentLinksEv
namespace Qt3DRender::Render {
using namespace Qt3DCore;
inline void GLTFSkeletonLoader::setupNodeParentLinks()
{
    const size_t nodeCount = m_nodes.size();
    for (size_t i = 0; i < nodeCount; ++i) {
        const Node &node = m_nodes[i];
        const std::vector<int> &childNodeIndices = node.childNodeIndices;
        for (const auto childNodeIndex : childNodeIndices) {
            Q_ASSERT(childNodeIndex < int(m_nodes.size()));
            Node &childNode = m_nodes[size_t(childNodeIndex)];
            Q_ASSERT(childNode.parentNodeIndex == -1);
            childNode.parentNodeIndex = int(i);
        }
    }
}
}  // namespace Qt3DRender::Render

//  from ../qt3d/src/render/geometry/gltfskeletonloader.cpp, line 537, as _ZNK10Qt3DRender6Render18GLTFSkeletonLoader16resolveLocalDataERK7QString
namespace Qt3DRender::Render {
using namespace Qt3DCore;
inline QByteArray GLTFSkeletonLoader::resolveLocalData(const QString &path) const
{
    QDir d(m_basePath);
    Q_ASSERT(d.exists());

    QString absPath = d.absoluteFilePath(path);
    QFile f(absPath);
    if (!f.open(QIODevice::ReadOnly))
        return QByteArray();
    return f.readAll();
}
}  // namespace Qt3DRender::Render

//  from ../qt3d/src/render/geometry/gltfskeletonloader.cpp, line 324, as _ZNK10Qt3DRender6Render18GLTFSkeletonLoader22createSkeletonFromSkinERKNS1_4SkinE
namespace Qt3DRender::Render {
using namespace Qt3DCore;
inline SkeletonData GLTFSkeletonLoader::createSkeletonFromSkin(const Skin &skin) const
{
    SkeletonData skel;

    const int jointCount = int(skin.jointNodeIndices.size());
    skel.reserve(jointCount);

    QHash<const Node *, int> jointIndexMap;
    for (int i = 0; i < jointCount; ++i) {
        // Get a pointer to the node for this joint and store it in
        // a map to the JointInfo index. We can later use this to set
        // the parent indices of the joints
        const Node *node = &m_nodes[skin.jointNodeIndices[i]];
        jointIndexMap.insert(node, i);

        JointInfo joint;
        joint.inverseBindPose = inverseBindMatrix(skin, i);
        joint.parentIndex = jointIndexMap.value(&m_nodes[node->parentNodeIndex], -1);
        if (joint.parentIndex == -1 && i != 0)
            qCDebug(Jobs) << "Cannot find parent joint for joint" << i;

        skel.joints.push_back(joint);
        skel.localPoses.push_back(node->localTransform);
        skel.jointNames.push_back(node->name);
    }

    return skel;
}
}  // namespace Qt3DRender::Render

//  from ../qt3d/src/render/geometry/gltfskeletonloader.cpp, line 353, as _ZNK10Qt3DRender6Render18GLTFSkeletonLoader17inverseBindMatrixERKNS1_4SkinEi
namespace Qt3DRender::Render {
using namespace Qt3DCore;
inline QMatrix4x4 GLTFSkeletonLoader::inverseBindMatrix(const Skin &skin, int jointIndex) const
{
    // Create a matrix and copy the data into it
    RawData rawData = accessorData(skin.inverseBindAccessorIndex, jointIndex);
    QMatrix4x4 m;
    memcpy(m.data(), rawData.data, rawData.byteLength);
    return m;
}
}  // namespace Qt3DRender::Render

//  from ../qt3d/src/render/geometry/gltfskeletonloader.cpp, line 362, as _ZNK10Qt3DRender6Render18GLTFSkeletonLoader12accessorDataEii
namespace Qt3DRender::Render {
using namespace Qt3DCore;
inline GLTFSkeletonLoader::RawData GLTFSkeletonLoader::accessorData(int accessorIndex, int index) const
{
    const AccessorData &accessor = m_accessors[accessorIndex];
    const BufferView &bufferView = m_bufferViews[accessor.bufferViewIndex];
    const BufferData &bufferData = m_bufferDatas[bufferView.bufferIndex];
    const QByteArray &ba = bufferData.data;
    const char *rawData = ba.constData() + bufferView.byteOffset + accessor.byteOffset;

    const uint typeSize = accessorTypeSize(accessor.type);
    const int stride = (accessor.byteStride == 0)
            ? accessor.dataSize * typeSize
            : accessor.byteStride;

    const char* data = rawData + index * stride;
    if (data - rawData > ba.size()) {
        qCWarning(Jobs, "Attempting to access data beyond end of buffer");
        return RawData{ nullptr, 0 };
    }

    const quint64 byteLength = accessor.dataSize * typeSize;
    RawData rd{ data, byteLength };

    return rd;
}
}  // namespace Qt3DRender::Render
//  -----------------------------------------------------------------------

//  Qt3DRender::Render::GLTFSkeletonLoader::GLTFSkeletonLoader()
extern "C" Q_DECL_EXPORT
Qt3DRender::Render::GLTFSkeletonLoader *ritual_ZN10Qt3DRender6Render18GLTFSkeletonLoaderC1Ev() {
  return new Qt3DRender::Render::GLTFSkeletonLoader();
}

//  SkeletonData Qt3DRender::Render::GLTFSkeletonLoader::createSkeleton(const
//      QString &skeletonName)
extern "C" Q_DECL_EXPORT
Qt3DRender::Render::SkeletonData *ritual_ZN10Qt3DRender6Render18GLTFSkeletonLoader14createSkeletonERK7QString(
    Qt3DRender::Render::GLTFSkeletonLoader *self,
    const QString *skeletonName) {
  return new Qt3DRender::Render::SkeletonData(
      self->createSkeleton(
          *skeletonName));
}

//  Qt3DCore::QAttribute::VertexBaseType
//      Qt3DRender::Render::GLTFSkeletonLoader::accessorTypeFromJSON(int
//      componentType)
extern "C" Q_DECL_EXPORT
Qt3DCore::QAttribute::VertexBaseType ritual_ZN10Qt3DRender6Render18GLTFSkeletonLoader20accessorTypeFromJSONEi(
    int componentType) {
  return Qt3DRender::Render::GLTFSkeletonLoader::accessorTypeFromJSON(
      componentType);
}

//  uint Qt3DRender::Render::GLTFSkeletonLoader::accessorTypeSize(Qt3DCore::Q
//      Attribute::VertexBaseType componentType)
extern "C" Q_DECL_EXPORT
uint ritual_ZN10Qt3DRender6Render18GLTFSkeletonLoader16accessorTypeSizeEN8Qt3DCore10QAttribute14VertexBaseTypeE(
    Qt3DCore::QAttribute::VertexBaseType componentType) {
  return Qt3DRender::Render::GLTFSkeletonLoader::accessorTypeSize(
      componentType);
}

//  uint
//      Qt3DRender::Render::GLTFSkeletonLoader::accessorDataSizeFromJson(cons
//      t QString &type)
extern "C" Q_DECL_EXPORT
uint ritual_ZN10Qt3DRender6Render18GLTFSkeletonLoader24accessorDataSizeFromJsonERK7QString(
    const QString *type) {
  return Qt3DRender::Render::GLTFSkeletonLoader::accessorDataSizeFromJson(
      *type);
}

//  void Qt3DRender::Render::GLTFSkeletonLoader::setBasePath(const QString
//      &path)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render18GLTFSkeletonLoader11setBasePathERK7QString(
    Qt3DRender::Render::GLTFSkeletonLoader *self,
    const QString *path) {
  self->setBasePath(*path);
}

//  bool Qt3DRender::Render::GLTFSkeletonLoader::setJSON(const QJsonDocument
//      &json)
extern "C" Q_DECL_EXPORT
bool ritual_ZN10Qt3DRender6Render18GLTFSkeletonLoader7setJSONERK13QJsonDocument(
    Qt3DRender::Render::GLTFSkeletonLoader *self,
    const QJsonDocument *json) {
  return self->setJSON(*json);
}

//  void Qt3DRender::Render::GLTFSkeletonLoader::cleanup()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render18GLTFSkeletonLoader7cleanupEv(
    Qt3DRender::Render::GLTFSkeletonLoader *self) {
  self->cleanup();
}

//  bool Qt3DRender::Render::GLTFSkeletonLoader::processJSONBuffer(const
//      QJsonObject &json)
extern "C" Q_DECL_EXPORT
bool ritual_ZN10Qt3DRender6Render18GLTFSkeletonLoader17processJSONBufferERK11QJsonObject(
    Qt3DRender::Render::GLTFSkeletonLoader *self,
    const QJsonObject *json) {
  return self->processJSONBuffer(*json);
}

//  void Qt3DRender::Render::GLTFSkeletonLoader::setupNodeParentLinks()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render18GLTFSkeletonLoader20setupNodeParentLinksEv(
    Qt3DRender::Render::GLTFSkeletonLoader *self) {
  self->setupNodeParentLinks();
}

//  QByteArray Qt3DRender::Render::GLTFSkeletonLoader::resolveLocalData(const
//      QString &path) const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK10Qt3DRender6Render18GLTFSkeletonLoader16resolveLocalDataERK7QString(
    const Qt3DRender::Render::GLTFSkeletonLoader *self,
    const QString *path) {
  return new QByteArray(self->resolveLocalData(*path));
}

//  SkeletonData
//      Qt3DRender::Render::GLTFSkeletonLoader::createSkeletonFromSkin(const
//      Skin &skin) const
extern "C" Q_DECL_EXPORT
Qt3DRender::Render::SkeletonData *ritual_ZNK10Qt3DRender6Render18GLTFSkeletonLoader22createSkeletonFromSkinERKNS1_4SkinE(
    const Qt3DRender::Render::GLTFSkeletonLoader *self,
    const Qt3DRender::Render::GLTFSkeletonLoader::Skin *skin) {
  return new Qt3DRender::Render::SkeletonData(
      self->createSkeletonFromSkin(
          *skin));
}

//  QMatrix4x4
//      Qt3DRender::Render::GLTFSkeletonLoader::inverseBindMatrix(const Skin
//      &skin, int jointIndex) const
extern "C" Q_DECL_EXPORT
QMatrix4x4 *ritual_ZNK10Qt3DRender6Render18GLTFSkeletonLoader17inverseBindMatrixERKNS1_4SkinEi(
    const Qt3DRender::Render::GLTFSkeletonLoader *self,
    const Qt3DRender::Render::GLTFSkeletonLoader::Skin *skin,
    int jointIndex) {
  return new QMatrix4x4(self->inverseBindMatrix(*skin, jointIndex));
}

//  RawData Qt3DRender::Render::GLTFSkeletonLoader::accessorData(int
//      accessorIndex, int index) const
extern "C" Q_DECL_EXPORT
Qt3DRender::Render::GLTFSkeletonLoader::RawData *ritual_ZNK10Qt3DRender6Render18GLTFSkeletonLoader12accessorDataEii(
    const Qt3DRender::Render::GLTFSkeletonLoader *self,
    int accessorIndex,
    int index) {
  return new Qt3DRender::Render::GLTFSkeletonLoader::RawData(
      self->accessorData(
          accessorIndex,
          index));
}

//  Qt3DRender::Render::GLTFSkeletonLoader::~GLTFSkeletonLoader()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render18GLTFSkeletonLoaderD1Ev(
    Qt3DRender::Render::GLTFSkeletonLoader *self) {
  delete self;
}

//  a Qt3DRender::Render::GLTFSkeletonLoader::RawData a ritual of
//      Qt3DRender::Render::GLTFSkeletonLoader gave
extern "C" Q_DECL_EXPORT
void ritual_drop_Qt3DRender_Render_GLTFSkeletonLoader__Qt3DRender_Render_GLTFSkeletonLoader_RawData(
    Qt3DRender::Render::GLTFSkeletonLoader::RawData *self) {
  delete self;
}
