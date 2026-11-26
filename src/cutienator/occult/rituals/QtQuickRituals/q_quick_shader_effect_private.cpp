//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickshadereffect_p_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtQuick/qtquickglobal.h>
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#if QT_CONFIG(quick_shadereffect)
#if QT_CONFIG(quick_shadereffect)
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickshadereffect_p.h>
#include <QtQuick/6.12.0/QtQuick/private/qquickshadereffect_p_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qurl.h>
#include <QtCore/qvariant.h>
#include <QtCore/qrect.h>
#include <QtQuick/qquickitem.h>
#include <QtCore/qbytearray.h>
#include <cstring>
#include <optional>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/private/qquickshadereffect_p_p.h>
#include <QtQuick/private/qsgcontextplugin_p.h>
#include <QtQuick/private/qsgrhisupport_p.h>
#include <QtQuick/private/qquickwindow_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/quick/items/qquickshadereffect.cpp, line 510, as local:qquickshadereffect.cpp:EffectSlotMapper
namespace QtPrivate {
class EffectSlotMapper: public QtPrivate::QSlotObjectBase
{
public:
    typedef std::function<void()> PropChangedFunc;

    explicit EffectSlotMapper(PropChangedFunc func)
    : QSlotObjectBase(&impl), _signalIndex(-1), func(func)
    { ref(); }

    void setSignalIndex(int idx) { _signalIndex = idx; }
    int signalIndex() const { return _signalIndex; }

private:
    int _signalIndex;
    PropChangedFunc func;

    static void impl(int which, QSlotObjectBase *this_, QObject *, void **a, bool *ret)
    {
    auto thiz = static_cast<EffectSlotMapper*>(this_);
    switch (which) {
    case Destroy:
        delete thiz;
        break;
    case Call:
        thiz->func();
        break;
    case Compare:
        *ret = thiz == reinterpret_cast<EffectSlotMapper *>(a[0]);
        break;
    case NumOperations: ;
    }
    }
};
}  // namespace QtPrivate

//  from ../qtdeclarative/src/quick/items/qquickshadereffect.cpp, line 838, as local:qquickshadereffect.cpp:indexToMappedId
inline constexpr int indexToMappedId(const int shaderType, const int idx)
{
    return idx | (shaderType << 16);
}

//  from ../qtdeclarative/src/quick/items/qquickshadereffect.cpp, line 843, as local:qquickshadereffect.cpp:mappedIdToIndex
inline constexpr int mappedIdToIndex(const int mappedId)
{
    return mappedId & 0xFFFF;
}

//  from ../qtdeclarative/src/quick/items/qquickshadereffect.cpp, line 848, as local:qquickshadereffect.cpp:mappedIdToShaderType
inline constexpr int mappedIdToShaderType(const int mappedId)
{
    return mappedId >> 16;
}

//  from ../qtdeclarative/src/quick/items/qquickshadereffect.cpp, line 1234, as local:qquickshadereffect.cpp:getValueFromProperty
static inline QVariant getValueFromProperty(QObject *item, const QMetaObject *itemMetaObject,
                                            const QByteArray &name, int propertyIndex)
{
    QVariant value;
    if (propertyIndex == -1) {
        value = item->property(name);
    } else {
        value = itemMetaObject->property(propertyIndex).read(item);
    }
    return value;
}

//  from ../qtdeclarative/src/quick/items/qquickshadereffect.cpp, line 830, as _ZN25QQuickShaderEffectPrivate12updatePolishEv
inline void QQuickShaderEffectPrivate::updatePolish()
{
    Q_Q(QQuickShaderEffect);
    if (!qmlEngine(q))
        return;
    maybeUpdateShaders();
}

//  from ../qtdeclarative/src/quick/items/qquickshadereffect.cpp, line 1497, as _ZN25QQuickShaderEffectPrivate15propertyChangedEi
inline void QQuickShaderEffectPrivate::propertyChanged(int mappedId)
{
    Q_Q(QQuickShaderEffect);
    const Shader type = Shader(mappedIdToShaderType(mappedId));
    const int idx = mappedIdToIndex(mappedId);
    const auto &v(m_shaders[type].shaderInfo.variables[idx]);
    auto &vd(m_shaders[type].varData[idx]);

    QVariant oldValue = vd.value;
    vd.value = getValueFromProperty(q, m_itemMetaObject, v.name, vd.propertyIndex);

    if (vd.specialType == QSGShaderEffectNode::VariableData::Source) {
        QQuickItem *source = qobject_cast<QQuickItem *>(qvariant_cast<QObject *>(oldValue));
        if (source) {
            if (q->window())
                QQuickItemPrivate::get(source)->derefWindow();
            // If the same source has been attached to two separate
            // textures/samplers, then changing one of them would trigger both
            // to be disconnected. So check first.
            if (sourceIsUnique(source, type, idx))
                QObject::disconnect(m_destroyedConnections.take(source));
        }

        source = qobject_cast<QQuickItem *>(qvariant_cast<QObject *>(vd.value));
        if (source) {
            // 'source' needs a window to get a scene graph node. It usually gets one through its
            // parent, but if the source item is "inline" rather than a reference -- i.e.
            // "property variant source: Image { }" instead of "property variant source: foo" -- it
            // will not get a parent. In those cases, 'source' should get the window from 'item'.
            if (q->window())
                QQuickItemPrivate::get(source)->refWindow(q->window());
            if (!m_destroyedConnections.contains(source))
                m_destroyedConnections.insert(source,
                    connect(source, &QObject::destroyed,
                            this, &QQuickShaderEffectPrivate::sourceDestroyed));
        }

        m_dirty |= QSGShaderEffectNode::DirtyShaderTexture;
        m_dirtyTextures[type].insert(idx);

     } else {
        m_dirty |= QSGShaderEffectNode::DirtyShaderConstant;
        m_dirtyConstants[type].insert(idx);
    }

    q->update();
}

//  from ../qtdeclarative/src/quick/items/qquickshadereffect.cpp, line 1472, as _ZNK25QQuickShaderEffectPrivate26findMappedShaderVariableIdERK10QByteArrayNS_6ShaderE
inline std::optional<int> QQuickShaderEffectPrivate::findMappedShaderVariableId(const QByteArray &name, Shader shaderType) const
{
    const auto &vars = m_shaders[shaderType].shaderInfo.variables;
    for (int idx = 0; idx < vars.size(); ++idx) {
        if (vars[idx].name == name)
            return indexToMappedId(shaderType, idx);
    }

    return {};
}

//  from ../qtdeclarative/src/quick/items/qquickshadereffect.cpp, line 1459, as _ZNK25QQuickShaderEffectPrivate26findMappedShaderVariableIdERK10QByteArray
inline std::optional<int> QQuickShaderEffectPrivate::findMappedShaderVariableId(const QByteArray &name) const
{
    for (int shaderType = 0; shaderType < NShader; ++shaderType) {
        const auto &vars = m_shaders[shaderType].shaderInfo.variables;
        for (int idx = 0; idx < vars.size(); ++idx) {
            if (vars[idx].name == name)
                return indexToMappedId(shaderType, idx);
        }
    }

    return {};
}

//  from ../qtdeclarative/src/quick/items/qquickshadereffect.cpp, line 1225, as _ZN25QQuickShaderEffectPrivate12clearMappersENS_6ShaderE
inline void QQuickShaderEffectPrivate::clearMappers(QQuickShaderEffectPrivate::Shader shaderType)
{
    for (auto *mapper : std::as_const(m_mappers[shaderType])) {
        if (mapper)
            mapper->destroyIfLastRef();
    }
    m_mappers[shaderType].clear();
}

//  from ../qtdeclarative/src/quick/items/qquickshadereffect.cpp, line 868, as _ZN25QQuickShaderEffectPrivateD1Ev
inline QQuickShaderEffectPrivate::~QQuickShaderEffectPrivate()
{
    Q_ASSERT(m_mgr == nullptr);
}

//  from ../qtdeclarative/src/quick/items/qquickshadereffect.cpp, line 903, as _ZN25QQuickShaderEffectPrivate11setBlendingEb
inline void QQuickShaderEffectPrivate::setBlending(bool enable)
{
    Q_Q(QQuickShaderEffect);
    if (m_blending == enable)
        return;

    m_blending = enable;
    q->update();
    emit q->blendingChanged();
}

//  from ../qtdeclarative/src/quick/items/qquickshadereffect.cpp, line 914, as _ZNK25QQuickShaderEffectPrivate4meshEv
inline QVariant QQuickShaderEffectPrivate::mesh() const
{
    return m_mesh ? QVariant::fromValue(static_cast<QObject *>(m_mesh))
                  : QVariant::fromValue(m_meshResolution);
}

//  from ../qtdeclarative/src/quick/items/qquickshadereffect.cpp, line 920, as _ZN25QQuickShaderEffectPrivate7setMeshERK8QVariant
inline void QQuickShaderEffectPrivate::setMesh(const QVariant &mesh)
{
    Q_Q(QQuickShaderEffect);
    QQuickShaderEffectMesh *newMesh = qobject_cast<QQuickShaderEffectMesh *>(qvariant_cast<QObject *>(mesh));
    if (newMesh && newMesh == m_mesh)
        return;

    if (m_mesh)
        QObject::disconnect(m_meshConnection);

    m_mesh = newMesh;

    if (m_mesh) {
        m_meshConnection = QObject::connect(m_mesh, &QQuickShaderEffectMesh::geometryChanged, q,
                                            [this] { markGeometryDirtyAndUpdate(); });
    } else {
        if (mesh.canConvert<QSize>()) {
            m_meshResolution = mesh.toSize();
        } else {
            QList<QByteArray> res = mesh.toByteArray().split('x');
            bool ok = res.size() == 2;
            if (ok) {
                int w = res.at(0).toInt(&ok);
                if (ok) {
                    int h = res.at(1).toInt(&ok);
                    if (ok)
                        m_meshResolution = QSize(w, h);
                }
            }
            if (!ok)
                qWarning("ShaderEffect: mesh property must be a size or an object deriving from QQuickShaderEffectMesh");
        }
        m_defaultMesh.setResolution(m_meshResolution);
    }

    m_dirty |= QSGShaderEffectNode::DirtyShaderMesh;
    q->update();

    emit q->meshChanged();
}

//  from ../qtdeclarative/src/quick/items/qquickshadereffect.cpp, line 961, as _ZN25QQuickShaderEffectPrivate11setCullModeEN18QQuickShaderEffect8CullModeE
inline void QQuickShaderEffectPrivate::setCullMode(QQuickShaderEffect::CullMode face)
{
    Q_Q(QQuickShaderEffect);
    if (m_cullMode == face)
        return;

    m_cullMode = face;
    q->update();
    emit q->cullModeChanged();
}

//  from ../qtdeclarative/src/quick/items/qquickshadereffect.cpp, line 972, as _ZN25QQuickShaderEffectPrivate24setSupportsAtlasTexturesEb
inline void QQuickShaderEffectPrivate::setSupportsAtlasTextures(bool supports)
{
    Q_Q(QQuickShaderEffect);
    if (m_supportsAtlasTextures == supports)
        return;

    m_supportsAtlasTextures = supports;
    markGeometryDirtyAndUpdate();
    emit q->supportsAtlasTexturesChanged();
}

//  from ../qtdeclarative/src/quick/items/qquickshadereffect.cpp, line 1007, as _ZN25QQuickShaderEffectPrivate11handleEventEP6QEvent
inline void QQuickShaderEffectPrivate::handleEvent(QEvent *event)
{
    if (event->type() == QEvent::DynamicPropertyChange) {
        const auto propertyName = static_cast<QDynamicPropertyChangeEvent *>(event)->propertyName();
        for (int i = 0; i < NShader; ++i) {
            const auto mappedId = findMappedShaderVariableId(propertyName, Shader(i));
            if (mappedId)
                propertyChanged(*mappedId);
        }
    }
}

//  from ../qtdeclarative/src/quick/items/qquickshadereffect.cpp, line 1019, as _ZN25QQuickShaderEffectPrivate21handleGeometryChangedERK6QRectFS2_
inline void QQuickShaderEffectPrivate::handleGeometryChanged(const QRectF &, const QRectF &)
{
    m_dirty |= QSGShaderEffectNode::DirtyShaderGeometry;
}

//  from ../qtdeclarative/src/quick/items/qquickshadereffect.cpp, line 1157, as _ZN25QQuickShaderEffectPrivate16handleItemChangeEN10QQuickItem10ItemChangeERKNS0_14ItemChangeDataE
inline void QQuickShaderEffectPrivate::handleItemChange(QQuickItem::ItemChange change, const QQuickItem::ItemChangeData &value)
{
    if (inDestructor)
        return;

    // Move the window ref.
    if (change == QQuickItem::ItemSceneChange) {
        for (int shaderType = 0; shaderType < NShader; ++shaderType) {
            for (const auto &vd : std::as_const(m_shaders[shaderType].varData)) {
                if (vd.specialType == QSGShaderEffectNode::VariableData::Source) {
                    QQuickItem *source = qobject_cast<QQuickItem *>(qvariant_cast<QObject *>(vd.value));
                    if (source) {
                        if (value.window)
                            QQuickItemPrivate::get(source)->refWindow(value.window);
                        else
                            QQuickItemPrivate::get(source)->derefWindow();
                    }
                }
            }
        }
    }
}

//  from ../qtdeclarative/src/quick/items/qquickshadereffect.cpp, line 1120, as _ZN25QQuickShaderEffectPrivate18updateUniformValueERK10QByteArrayRK8QVariantP19QSGShaderEffectNode
inline bool QQuickShaderEffectPrivate::updateUniformValue(const QByteArray &name, const QVariant &value,
                                                QSGShaderEffectNode *node)
{
    Q_Q(QQuickShaderEffect);
    const auto mappedId = findMappedShaderVariableId(name);
    if (!mappedId)
        return false;

    const Shader type = Shader(mappedIdToShaderType(*mappedId));
    const int idx = mappedIdToIndex(*mappedId);

    // Update value
    m_shaders[type].varData[idx].value = value;

    // Insert dirty uniform
    QSet<int> dirtyConstants[NShader];
    dirtyConstants[type].insert(idx);

    // Sync material change
    QSGShaderEffectNode::SyncData sd;
    sd.dirty = QSGShaderEffectNode::DirtyShaderConstant;
    sd.cullMode = QSGShaderEffectNode::CullMode(m_cullMode);
    sd.blending = m_blending;
    sd.vertex.shader = &m_shaders[Vertex];
    sd.vertex.dirtyConstants = &dirtyConstants[Vertex];
    sd.vertex.dirtyTextures = {};
    sd.fragment.shader = &m_shaders[Fragment];
    sd.fragment.dirtyConstants = &dirtyConstants[Fragment];
    sd.fragment.dirtyTextures = {};
    sd.materialTypeCacheKey = q->window();
    sd.viewCount = QQuickWindowPrivate::get(q->window())->multiViewCount();

    node->syncMaterial(&sd);

    return true;
}

//  from ../qtdeclarative/src/quick/items/qquickshadereffect.cpp, line 1545, as _ZN25QQuickShaderEffectPrivate15sourceDestroyedEP7QObject
inline void QQuickShaderEffectPrivate::sourceDestroyed(QObject *object)
{
    for (int shaderType = 0; shaderType < NShader; ++shaderType) {
        for (auto &vd : m_shaders[shaderType].varData) {
            if (vd.specialType == QSGShaderEffectNode::VariableData::Source && vd.value.canConvert<QObject *>()) {
                if (qvariant_cast<QObject *>(vd.value) == object)
                    vd.value = QVariant();
            }
        }
    }
}

//  from ../qtdeclarative/src/quick/items/qquickshadereffect.cpp, line 1557, as _ZN25QQuickShaderEffectPrivate26markGeometryDirtyAndUpdateEv
inline void QQuickShaderEffectPrivate::markGeometryDirtyAndUpdate()
{
    Q_Q(QQuickShaderEffect);
    m_dirty |= QSGShaderEffectNode::DirtyShaderGeometry;
    q->update();
}

//  from ../qtdeclarative/src/quick/items/qquickshadereffect.cpp, line 1564, as _ZN25QQuickShaderEffectPrivate41markGeometryDirtyAndUpdateIfSupportsAtlasEv
inline void QQuickShaderEffectPrivate::markGeometryDirtyAndUpdateIfSupportsAtlas()
{
    if (m_supportsAtlasTextures)
        markGeometryDirtyAndUpdate();
}

//  from ../qtdeclarative/src/quick/items/qquickshadereffect.cpp, line 1483, as _ZNK25QQuickShaderEffectPrivate14sourceIsUniqueEP10QQuickItemNS_6ShaderEi
inline bool QQuickShaderEffectPrivate::sourceIsUnique(QQuickItem *source, Shader typeToSkip, int indexToSkip) const
{
    for (int shaderType = 0; shaderType < NShader; ++shaderType) {
        for (int idx = 0; idx < m_shaders[shaderType].varData.size(); ++idx) {
            if (shaderType != typeToSkip || idx != indexToSkip) {
                const auto &vd(m_shaders[shaderType].varData[idx]);
                if (vd.specialType == QSGShaderEffectNode::VariableData::Source && qvariant_cast<QObject *>(vd.value) == source)
                    return false;
            }
        }
    }
    return true;
}
//  -----------------------------------------------------------------------

//  A QQuickShaderEffectPrivate that Python can take functions over in. Every QQuickShaderEffectPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(quick_shadereffect)
typedef void (*CuteQQuickShaderEffectPrivateCall0)(const void *, int *);
#endif  // QT_CONFIG(quick_shadereffect)
typedef void (*CuteQQuickShaderEffectPrivateCall1)(const void *, QQuickPointerHandler *, int *);
typedef void (*CuteQQuickShaderEffectPrivateCall2)(const void *, QQuickPointerHandler *, int *);
typedef void * (*CuteQQuickShaderEffectPrivateCall3)(const void *, const QMetaObject *, int *);
typedef void (*CuteQQuickShaderEffectPrivateCall4)(const void *, QQuickItem *, bool, int *);
typedef bool (*CuteQQuickShaderEffectPrivateCall5)(const void *, int, int *);
typedef qreal (*CuteQQuickShaderEffectPrivateCall6)(const void *, int *);
typedef qreal (*CuteQQuickShaderEffectPrivateCall7)(const void *, int *);
typedef void (*CuteQQuickShaderEffectPrivateCall8)(const void *, int *);
typedef void (*CuteQQuickShaderEffectPrivateCall9)(const void *, int *);
#if QT_CONFIG(accessibility)
typedef int (*CuteQQuickShaderEffectPrivateCall10)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
typedef bool (*CuteQQuickShaderEffectPrivateCall11)(const void *, QQuickItem *, int *);
typedef bool (*CuteQQuickShaderEffectPrivateCall12)(const void *, QPointerEvent *, bool, int *);
#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
typedef bool (*CuteQQuickShaderEffectPrivateCall13)(const void *, QContextMenuEvent *, int *);
#endif  // QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
typedef void (*CuteQQuickShaderEffectPrivateCall14)(const void *, bool, int *);
typedef void * (*CuteQQuickShaderEffectPrivateCall15)(const void *, int *);
typedef void (*CuteQQuickShaderEffectPrivateCall16)(const void *, int *);
typedef void (*CuteQQuickShaderEffectPrivateCall17)(const void *, int, int *);
class CuteQQuickShaderEffectPrivate : public QQuickShaderEffectPrivate {
public:
  using QQuickShaderEffectPrivate::QQuickShaderEffectPrivate;
  void *taken[18] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(quick_shadereffect)
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate12updatePolishEv")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_shadereffect)
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate17addPointerHandlerEP20QQuickPointerHandler")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate20removePointerHandlerEP20QQuickPointerHandler")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate33attachedPropertyPropagator_parentEPK11QMetaObject")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate25registerAsContainmentMaskEP10QQuickItemb")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate24setLastFocusChangeReasonEN2Qt11FocusReasonE")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK17QQuickItemPrivate16getImplicitWidthEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK17QQuickItemPrivate17getImplicitHeightEv")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate20implicitWidthChangedEv")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate21implicitHeightChangedEv")) {
      taken[9] = call;
      return true;
    }
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK17QQuickItemPrivate14accessibleRoleEv")) {
      taken[10] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate16transformChangedEP10QQuickItem")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate18handlePointerEventEP13QPointerEventb")) {
      taken[12] = call;
      return true;
    }
#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate22handleContextMenuEventEP17QContextMenuEvent")) {
      taken[13] = call;
      return true;
    }
#endif  // QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate10setVisibleEb")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate19createTransformNodeEv")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate12mirrorChangeEv")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK17QQuickItemPrivate12dumpItemTreeEi")) {
      taken[17] = call;
      return true;
    }
    return false;
  }

#if QT_CONFIG(quick_shadereffect)
  //  void QQuickShaderEffectPrivate::updatePolish()
  void updatePolish() override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickShaderEffectPrivateCall0 call = reinterpret_cast<CuteQQuickShaderEffectPrivateCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickShaderEffectPrivate::updatePolish();
  }
#endif  // QT_CONFIG(quick_shadereffect)

  //  void QQuickItemPrivate::addPointerHandler(QQuickPointerHandler *h)
  void addPointerHandler(QQuickPointerHandler *h) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickShaderEffectPrivateCall1 call = reinterpret_cast<CuteQQuickShaderEffectPrivateCall1>(taken[1]);
      call(this, h, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::addPointerHandler(h);
  }

  //  void QQuickItemPrivate::removePointerHandler(QQuickPointerHandler *h)
  void removePointerHandler(QQuickPointerHandler *h) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickShaderEffectPrivateCall2 call = reinterpret_cast<CuteQQuickShaderEffectPrivateCall2>(taken[2]);
      call(this, h, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::removePointerHandler(h);
  }

  //  QtPrivate::QQuickAttachedPropertyPropagator
  //      *QQuickItemPrivate::attachedPropertyPropagator_parent(const
  //      QMetaObject *attachedType)
  QtPrivate::QQuickAttachedPropertyPropagator *attachedPropertyPropagator_parent(
      const QMetaObject *attachedType) override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickShaderEffectPrivateCall3 call = reinterpret_cast<CuteQQuickShaderEffectPrivateCall3>(taken[3]);
      void * given = call(this, attachedType, &handled);
      if (handled) return static_cast<QtPrivate::QQuickAttachedPropertyPropagator *>(given);
    }
    return QQuickItemPrivate::attachedPropertyPropagator_parent(attachedType);
  }

  //  void QQuickItemPrivate::registerAsContainmentMask(QQuickItem *a0,
  //      bool a1)
  void registerAsContainmentMask(QQuickItem *a0, bool a1) override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuickShaderEffectPrivateCall4 call = reinterpret_cast<CuteQQuickShaderEffectPrivateCall4>(taken[4]);
      call(this, a0, a1, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::registerAsContainmentMask(a0, a1);
  }

  //  bool QQuickItemPrivate::setLastFocusChangeReason(Qt::FocusReason
  //      reason)
  bool setLastFocusChangeReason(Qt::FocusReason reason) override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuickShaderEffectPrivateCall5 call = reinterpret_cast<CuteQQuickShaderEffectPrivateCall5>(taken[5]);
      bool given = call(this, static_cast<int>(reason), &handled);
      if (handled) return given;
    }
    return QQuickItemPrivate::setLastFocusChangeReason(reason);
  }

  //  qreal QQuickItemPrivate::getImplicitWidth() const
  qreal getImplicitWidth() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuickShaderEffectPrivateCall6 call = reinterpret_cast<CuteQQuickShaderEffectPrivateCall6>(taken[6]);
      qreal given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickItemPrivate::getImplicitWidth();
  }

  //  qreal QQuickItemPrivate::getImplicitHeight() const
  qreal getImplicitHeight() const override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuickShaderEffectPrivateCall7 call = reinterpret_cast<CuteQQuickShaderEffectPrivateCall7>(taken[7]);
      qreal given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickItemPrivate::getImplicitHeight();
  }

  //  void QQuickItemPrivate::implicitWidthChanged()
  void implicitWidthChanged() override {
    if (taken[8]) {
      int handled = 0;
      CuteQQuickShaderEffectPrivateCall8 call = reinterpret_cast<CuteQQuickShaderEffectPrivateCall8>(taken[8]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::implicitWidthChanged();
  }

  //  void QQuickItemPrivate::implicitHeightChanged()
  void implicitHeightChanged() override {
    if (taken[9]) {
      int handled = 0;
      CuteQQuickShaderEffectPrivateCall9 call = reinterpret_cast<CuteQQuickShaderEffectPrivateCall9>(taken[9]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::implicitHeightChanged();
  }

#if QT_CONFIG(accessibility)
  //  QAccessible::Role QQuickItemPrivate::accessibleRole() const
  QAccessible::Role accessibleRole() const override {
    if (taken[10]) {
      int handled = 0;
      CuteQQuickShaderEffectPrivateCall10 call = reinterpret_cast<CuteQQuickShaderEffectPrivateCall10>(taken[10]);
      int given = call(this, &handled);
      if (handled) return static_cast<QAccessible::Role>(given);
    }
    return QQuickItemPrivate::accessibleRole();
  }
#endif  // QT_CONFIG(accessibility)

  //  bool QQuickItemPrivate::transformChanged(QQuickItem *transformedItem)
  bool transformChanged(QQuickItem *transformedItem) override {
    if (taken[11]) {
      int handled = 0;
      CuteQQuickShaderEffectPrivateCall11 call = reinterpret_cast<CuteQQuickShaderEffectPrivateCall11>(taken[11]);
      bool given = call(this, transformedItem, &handled);
      if (handled) return given;
    }
    return QQuickItemPrivate::transformChanged(transformedItem);
  }

  //  bool QQuickItemPrivate::handlePointerEvent(QPointerEvent *a0, bool
  //      avoidGrabbers)
  bool handlePointerEvent(QPointerEvent *a0, bool avoidGrabbers) override {
    if (taken[12]) {
      int handled = 0;
      CuteQQuickShaderEffectPrivateCall12 call = reinterpret_cast<CuteQQuickShaderEffectPrivateCall12>(taken[12]);
      bool given = call(this, a0, avoidGrabbers, &handled);
      if (handled) return given;
    }
    return QQuickItemPrivate::handlePointerEvent(a0, avoidGrabbers);
  }

#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
  //  bool QQuickItemPrivate::handleContextMenuEvent(QContextMenuEvent
  //      *event)
  bool handleContextMenuEvent(QContextMenuEvent *event) override {
    if (taken[13]) {
      int handled = 0;
      CuteQQuickShaderEffectPrivateCall13 call = reinterpret_cast<CuteQQuickShaderEffectPrivateCall13>(taken[13]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QQuickItemPrivate::handleContextMenuEvent(event);
  }
#endif  // QT_VERSION < QT_VERSION_CHECK(7, 0, 0)

  //  void QQuickItemPrivate::setVisible(bool visible)
  void setVisible(bool visible) override {
    if (taken[14]) {
      int handled = 0;
      CuteQQuickShaderEffectPrivateCall14 call = reinterpret_cast<CuteQQuickShaderEffectPrivateCall14>(taken[14]);
      call(this, visible, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::setVisible(visible);
  }

  //  QSGTransformNode *QQuickItemPrivate::createTransformNode()
  QSGTransformNode *createTransformNode() override {
    if (taken[15]) {
      int handled = 0;
      CuteQQuickShaderEffectPrivateCall15 call = reinterpret_cast<CuteQQuickShaderEffectPrivateCall15>(taken[15]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QSGTransformNode *>(given);
    }
    return QQuickItemPrivate::createTransformNode();
  }

  //  void QQuickItemPrivate::mirrorChange()
  void mirrorChange() override {
    if (taken[16]) {
      int handled = 0;
      CuteQQuickShaderEffectPrivateCall16 call = reinterpret_cast<CuteQQuickShaderEffectPrivateCall16>(taken[16]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::mirrorChange();
  }

  //  void QQuickItemPrivate::dumpItemTree(int indent) const
  void dumpItemTree(int indent) const override {
    if (taken[17]) {
      int handled = 0;
      CuteQQuickShaderEffectPrivateCall17 call = reinterpret_cast<CuteQQuickShaderEffectPrivateCall17>(taken[17]);
      call(this, indent, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::dumpItemTree(indent);
  }
};

//  QQuickShaderEffect *QQuickShaderEffectPrivate::q_func()
extern "C" Q_DECL_EXPORT
QQuickShaderEffect *ritual_ZN25QQuickShaderEffectPrivate6q_funcEv(
    QQuickShaderEffectPrivate *self) {
  return self->q_func();
}

//  const QQuickShaderEffect *QQuickShaderEffectPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QQuickShaderEffect *ritual_ZNK25QQuickShaderEffectPrivate6q_funcEv(
    const QQuickShaderEffectPrivate *self) {
  return self->q_func();
}

//  QQuickShaderEffectPrivate::~QQuickShaderEffectPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQuickShaderEffectPrivateD1Ev(
    QQuickShaderEffectPrivate *self) {
  delete self;
}

//  void QQuickShaderEffectPrivate::updatePolish()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQuickShaderEffectPrivate12updatePolishEv(
    QQuickShaderEffectPrivate *self) {
  self->updatePolish();
}

//  QUrl QQuickShaderEffectPrivate::fragmentShader() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK25QQuickShaderEffectPrivate14fragmentShaderEv(
    const QQuickShaderEffectPrivate *self) {
  return new QUrl(self->fragmentShader());
}

//  QUrl QQuickShaderEffectPrivate::vertexShader() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK25QQuickShaderEffectPrivate12vertexShaderEv(
    const QQuickShaderEffectPrivate *self) {
  return new QUrl(self->vertexShader());
}

//  bool QQuickShaderEffectPrivate::blending() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK25QQuickShaderEffectPrivate8blendingEv(
    const QQuickShaderEffectPrivate *self) {
  return self->blending();
}

//  void QQuickShaderEffectPrivate::setBlending(bool enable)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQuickShaderEffectPrivate11setBlendingEb(
    QQuickShaderEffectPrivate *self,
    bool enable) {
  self->setBlending(enable);
}

//  QVariant QQuickShaderEffectPrivate::mesh() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK25QQuickShaderEffectPrivate4meshEv(
    const QQuickShaderEffectPrivate *self) {
  return new QVariant(self->mesh());
}

//  void QQuickShaderEffectPrivate::setMesh(const QVariant &mesh)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQuickShaderEffectPrivate7setMeshERK8QVariant(
    QQuickShaderEffectPrivate *self,
    const QVariant *mesh) {
  self->setMesh(*mesh);
}

//  QQuickShaderEffect::CullMode QQuickShaderEffectPrivate::cullMode() const
extern "C" Q_DECL_EXPORT
QQuickShaderEffect::CullMode ritual_ZNK25QQuickShaderEffectPrivate8cullModeEv(
    const QQuickShaderEffectPrivate *self) {
  return self->cullMode();
}

//  void QQuickShaderEffectPrivate::setCullMode(QQuickShaderEffect::CullMode
//      face)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQuickShaderEffectPrivate11setCullModeEN18QQuickShaderEffect8CullModeE(
    QQuickShaderEffectPrivate *self,
    QQuickShaderEffect::CullMode face) {
  self->setCullMode(face);
}

//  bool QQuickShaderEffectPrivate::supportsAtlasTextures() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK25QQuickShaderEffectPrivate21supportsAtlasTexturesEv(
    const QQuickShaderEffectPrivate *self) {
  return self->supportsAtlasTextures();
}

//  void QQuickShaderEffectPrivate::setSupportsAtlasTextures(bool supports)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQuickShaderEffectPrivate24setSupportsAtlasTexturesEb(
    QQuickShaderEffectPrivate *self,
    bool supports) {
  self->setSupportsAtlasTextures(supports);
}

//  void QQuickShaderEffectPrivate::handleEvent(QEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQuickShaderEffectPrivate11handleEventEP6QEvent(
    QQuickShaderEffectPrivate *self,
    QEvent *a0) {
  self->handleEvent(a0);
}

//  void QQuickShaderEffectPrivate::handleGeometryChanged(const QRectF
//      &newGeometry, const QRectF &oldGeometry)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQuickShaderEffectPrivate21handleGeometryChangedERK6QRectFS2_(
    QQuickShaderEffectPrivate *self,
    const QRectF *newGeometry,
    const QRectF *oldGeometry) {
  self->handleGeometryChanged(*newGeometry, *oldGeometry);
}

//  void QQuickShaderEffectPrivate::handleItemChange(QQuickItem::ItemChange
//      change, const QQuickItem::ItemChangeData &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQuickShaderEffectPrivate16handleItemChangeEN10QQuickItem10ItemChangeERKNS0_14ItemChangeDataE(
    QQuickShaderEffectPrivate *self,
    QQuickItem::ItemChange change,
    const QQuickItem::ItemChangeData *value) {
  self->handleItemChange(change, *value);
}

//  bool QQuickShaderEffectPrivate::updateUniformValue(const QByteArray
//      &name, const QVariant &value, QSGShaderEffectNode *node)
extern "C" Q_DECL_EXPORT
bool ritual_ZN25QQuickShaderEffectPrivate18updateUniformValueERK10QByteArrayRK8QVariantP19QSGShaderEffectNode(
    QQuickShaderEffectPrivate *self,
    const QByteArray *name,
    const QVariant *value,
    QSGShaderEffectNode *node) {
  return self->updateUniformValue(*name, *value, node);
}

//  void QQuickShaderEffectPrivate::sourceDestroyed(QObject *object)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQuickShaderEffectPrivate15sourceDestroyedEP7QObject(
    QQuickShaderEffectPrivate *self,
    QObject *object) {
  self->sourceDestroyed(object);
}

//  void QQuickShaderEffectPrivate::markGeometryDirtyAndUpdate()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQuickShaderEffectPrivate26markGeometryDirtyAndUpdateEv(
    QQuickShaderEffectPrivate *self) {
  self->markGeometryDirtyAndUpdate();
}

//  void
//      QQuickShaderEffectPrivate::markGeometryDirtyAndUpdateIfSupportsAtlas(
//      )
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQuickShaderEffectPrivate41markGeometryDirtyAndUpdateIfSupportsAtlasEv(
    QQuickShaderEffectPrivate *self) {
  self->markGeometryDirtyAndUpdateIfSupportsAtlas();
}

//  bool QQuickShaderEffectPrivate::sourceIsUnique(QQuickItem *source, Shader
//      typeToSkip, int indexToSkip) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK25QQuickShaderEffectPrivate14sourceIsUniqueEP10QQuickItemNS_6ShaderEi(
    const QQuickShaderEffectPrivate *self,
    QQuickItem *source,
    QQuickShaderEffectPrivate::Shader typeToSkip,
    int indexToSkip) {
  return self->sourceIsUnique(source, typeToSkip, indexToSkip);
}

//  a Python function taken by a CuteQQuickShaderEffectPrivate, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickShaderEffectPrivate(
    QQuickShaderEffectPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickShaderEffectPrivate *>(self)->take(key, call);
}

//  a std::optional<int> a ritual of QQuickShaderEffectPrivate gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QQuickShaderEffectPrivate__std_optional_int(
    std::optional<int> *self) {
  delete self;
}

#endif  // QT_CONFIG(quick_shadereffect)
#endif  // QT_CONFIG(quick_shadereffect)
