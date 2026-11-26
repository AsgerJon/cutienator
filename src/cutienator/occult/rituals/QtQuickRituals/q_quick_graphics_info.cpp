//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickgraphicsinfo_p.h, Qt 6.12.0.
//  Edited by hand on 2026-11-26: moc's output for 'QQuickGraphicsInfo' is
//  pasted in, cut from what the moc of Qt 6.12.0 writes for its header: Qt's
//  library keeps it to itself; added are 4 rituals that lean on what moc
//  writes for a class of the part Qt keeps to itself, whose ritual file
//  carries moc's output, drafted by a copy of the generator that lets those
//  names through. A copy of a meta-object is a second one: 'qobject_cast'
//  between it and Qt's own does not match. Kept as it is when the generator
//  runs again.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickgraphicsinfo_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetatype.h>
#include <QtCore/qtmochelpers.h>
#include <memory>
#include <QtCore/qxptype_traits.h>
#include <QtQuick/private/qquickgraphicsinfo_p.h>
#include <QtQuick/private/qquickitem_p.h>
#include <QtGui/qopenglcontext.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from QtQuick__QQuickGraphicsInfo.cpp, line 1, as moc:QQuickGraphicsInfo
#ifndef Q_CONSTINIT
#define Q_CONSTINIT
#endif
QT_WARNING_PUSH
QT_WARNING_DISABLE_DEPRECATED
namespace {
struct qt_meta_tag_ZN18QQuickGraphicsInfoE_t {};
} // unnamed namespace

template <> constexpr inline auto QQuickGraphicsInfo::qt_create_metaobjectdata<qt_meta_tag_ZN18QQuickGraphicsInfoE_t>()
{
    namespace QMC = QtMocConstants;
    QtMocHelpers::StringRefStorage qt_stringData {
        "QQuickGraphicsInfo",
        "QML.Element",
        "GraphicsInfo",
        "QML.AddedInVersion",
        "520",
        "QML.Creatable",
        "false",
        "QML.UncreatableReason",
        "GraphicsInfo is only available via attached properties.",
        "QML.Attached",
        "apiChanged",
        "",
        "shaderTypeChanged",
        "shaderCompilationTypeChanged",
        "shaderSourceTypeChanged",
        "majorVersionChanged",
        "minorVersionChanged",
        "profileChanged",
        "renderableTypeChanged",
        "updateInfo",
        "setWindow",
        "QQuickWindow*",
        "window",
        "api",
        "GraphicsApi",
        "shaderType",
        "ShaderType",
        "shaderCompilationType",
        "ShaderCompilationType",
        "shaderSourceType",
        "ShaderSourceType",
        "majorVersion",
        "minorVersion",
        "profile",
        "OpenGLContextProfile",
        "renderableType",
        "RenderableType",
        "Unknown",
        "Software",
        "OpenVG",
        "OpenGL",
        "Direct3D11",
        "Vulkan",
        "Metal",
        "Null",
        "Direct3D12",
        "OpenGLRhi",
        "Direct3D11Rhi",
        "VulkanRhi",
        "MetalRhi",
        "NullRhi",
        "UnknownShadingLanguage",
        "GLSL",
        "HLSL",
        "RhiShader",
        "RuntimeCompilation",
        "OfflineCompilation",
        "ShaderSourceString",
        "ShaderSourceFile",
        "ShaderByteCode",
        "OpenGLNoProfile",
        "OpenGLCoreProfile",
        "OpenGLCompatibilityProfile",
        "SurfaceFormatUnspecified",
        "SurfaceFormatOpenGL",
        "SurfaceFormatOpenGLES"
    };

    QtMocHelpers::UintData qt_methods {
        // Signal 'apiChanged'
        QtMocHelpers::SignalData<void()>(10, 11, QMC::AccessPublic, QMetaType::Void),
        // Signal 'shaderTypeChanged'
        QtMocHelpers::SignalData<void()>(12, 11, QMC::AccessPublic, QMetaType::Void),
        // Signal 'shaderCompilationTypeChanged'
        QtMocHelpers::SignalData<void()>(13, 11, QMC::AccessPublic, QMetaType::Void),
        // Signal 'shaderSourceTypeChanged'
        QtMocHelpers::SignalData<void()>(14, 11, QMC::AccessPublic, QMetaType::Void),
        // Signal 'majorVersionChanged'
        QtMocHelpers::SignalData<void()>(15, 11, QMC::AccessPublic, QMetaType::Void),
        // Signal 'minorVersionChanged'
        QtMocHelpers::SignalData<void()>(16, 11, QMC::AccessPublic, QMetaType::Void),
        // Signal 'profileChanged'
        QtMocHelpers::SignalData<void()>(17, 11, QMC::AccessPublic, QMetaType::Void),
        // Signal 'renderableTypeChanged'
        QtMocHelpers::SignalData<void()>(18, 11, QMC::AccessPublic, QMetaType::Void),
        // Slot 'updateInfo'
        QtMocHelpers::SlotData<void()>(19, 11, QMC::AccessPrivate, QMetaType::Void),
        // Slot 'setWindow'
        QtMocHelpers::SlotData<void(QQuickWindow *)>(20, 11, QMC::AccessPrivate, QMetaType::Void, {{
            { 0x80000000 | 21, 22 },
        }}),
    };
    QtMocHelpers::UintData qt_properties {
        // property 'api'
        QtMocHelpers::PropertyData<enum GraphicsApi>(23, 0x80000000 | 24, QMC::DefaultPropertyFlags | QMC::EnumOrFlag | QMC::Final, 0),
        // property 'shaderType'
        QtMocHelpers::PropertyData<enum ShaderType>(25, 0x80000000 | 26, QMC::DefaultPropertyFlags | QMC::EnumOrFlag | QMC::Final, 1),
        // property 'shaderCompilationType'
        QtMocHelpers::PropertyData<enum ShaderCompilationType>(27, 0x80000000 | 28, QMC::DefaultPropertyFlags | QMC::EnumOrFlag | QMC::Final, 2),
        // property 'shaderSourceType'
        QtMocHelpers::PropertyData<enum ShaderSourceType>(29, 0x80000000 | 30, QMC::DefaultPropertyFlags | QMC::EnumOrFlag | QMC::Final, 3),
        // property 'majorVersion'
        QtMocHelpers::PropertyData<int>(31, QMetaType::Int, QMC::DefaultPropertyFlags | QMC::Final, 4),
        // property 'minorVersion'
        QtMocHelpers::PropertyData<int>(32, QMetaType::Int, QMC::DefaultPropertyFlags | QMC::Final, 5),
        // property 'profile'
        QtMocHelpers::PropertyData<enum OpenGLContextProfile>(33, 0x80000000 | 34, QMC::DefaultPropertyFlags | QMC::EnumOrFlag | QMC::Final, 6),
        // property 'renderableType'
        QtMocHelpers::PropertyData<enum RenderableType>(35, 0x80000000 | 36, QMC::DefaultPropertyFlags | QMC::EnumOrFlag | QMC::Final, 7),
    };
    QtMocHelpers::UintData qt_enums {
        // enum 'GraphicsApi'
        QtMocHelpers::EnumData<enum GraphicsApi>(24, 24, QMC::EnumFlags{}).add({
            {   37, GraphicsApi::Unknown },
            {   38, GraphicsApi::Software },
            {   39, GraphicsApi::OpenVG },
            {   40, GraphicsApi::OpenGL },
            {   41, GraphicsApi::Direct3D11 },
            {   42, GraphicsApi::Vulkan },
            {   43, GraphicsApi::Metal },
            {   44, GraphicsApi::Null },
            {   45, GraphicsApi::Direct3D12 },
            {   46, GraphicsApi::OpenGLRhi },
            {   47, GraphicsApi::Direct3D11Rhi },
            {   48, GraphicsApi::VulkanRhi },
            {   49, GraphicsApi::MetalRhi },
            {   50, GraphicsApi::NullRhi },
        }),
        // enum 'ShaderType'
        QtMocHelpers::EnumData<enum ShaderType>(26, 26, QMC::EnumFlags{}).add({
            {   51, ShaderType::UnknownShadingLanguage },
            {   52, ShaderType::GLSL },
            {   53, ShaderType::HLSL },
            {   54, ShaderType::RhiShader },
        }),
        // enum 'ShaderCompilationType'
        QtMocHelpers::EnumData<enum ShaderCompilationType>(28, 28, QMC::EnumFlags{}).add({
            {   55, ShaderCompilationType::RuntimeCompilation },
            {   56, ShaderCompilationType::OfflineCompilation },
        }),
        // enum 'ShaderSourceType'
        QtMocHelpers::EnumData<enum ShaderSourceType>(30, 30, QMC::EnumFlags{}).add({
            {   57, ShaderSourceType::ShaderSourceString },
            {   58, ShaderSourceType::ShaderSourceFile },
            {   59, ShaderSourceType::ShaderByteCode },
        }),
        // enum 'OpenGLContextProfile'
        QtMocHelpers::EnumData<enum OpenGLContextProfile>(34, 34, QMC::EnumFlags{}).add({
            {   60, OpenGLContextProfile::OpenGLNoProfile },
            {   61, OpenGLContextProfile::OpenGLCoreProfile },
            {   62, OpenGLContextProfile::OpenGLCompatibilityProfile },
        }),
        // enum 'RenderableType'
        QtMocHelpers::EnumData<enum RenderableType>(36, 36, QMC::EnumFlags{}).add({
            {   63, RenderableType::SurfaceFormatUnspecified },
            {   64, RenderableType::SurfaceFormatOpenGL },
            {   65, RenderableType::SurfaceFormatOpenGLES },
        }),
    };
    QtMocHelpers::UintData qt_constructors {};
    QtMocHelpers::ClassInfos qt_classinfo({
            {    1,    2 },
            {    3,    4 },
            {    5,    6 },
            {    7,    8 },
            {    9,    0 },
    });
    return QtMocHelpers::metaObjectData<QQuickGraphicsInfo, void>(QMC::MetaObjectFlag{}, qt_stringData,
            qt_methods, qt_properties, qt_enums, qt_constructors, qt_classinfo);
}
Q_CONSTINIT const QMetaObject QQuickGraphicsInfo::staticMetaObject = { {
    QMetaObject::SuperData::link<QObject::staticMetaObject>(),
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN18QQuickGraphicsInfoE_t>.stringdata,
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN18QQuickGraphicsInfoE_t>.data,
    qt_static_metacall,
    nullptr,
    qt_staticMetaObjectRelocatingContent<qt_meta_tag_ZN18QQuickGraphicsInfoE_t>.metaTypes,
    nullptr
} };

void QQuickGraphicsInfo::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    auto *_t = static_cast<QQuickGraphicsInfo *>(_o);
    if (_c == QMetaObject::InvokeMetaMethod) {
        switch (_id) {
        case 0: _t->apiChanged(); break;
        case 1: _t->shaderTypeChanged(); break;
        case 2: _t->shaderCompilationTypeChanged(); break;
        case 3: _t->shaderSourceTypeChanged(); break;
        case 4: _t->majorVersionChanged(); break;
        case 5: _t->minorVersionChanged(); break;
        case 6: _t->profileChanged(); break;
        case 7: _t->renderableTypeChanged(); break;
        case 8: _t->updateInfo(); break;
        case 9: _t->setWindow((*reinterpret_cast<std::add_pointer_t<QQuickWindow*>>(_a[1]))); break;
        default: ;
        }
    }
    if (_c == QMetaObject::IndexOfMethod) {
        if (QtMocHelpers::indexOfMethod<void (QQuickGraphicsInfo::*)()>(_a, &QQuickGraphicsInfo::apiChanged, 0))
            return;
        if (QtMocHelpers::indexOfMethod<void (QQuickGraphicsInfo::*)()>(_a, &QQuickGraphicsInfo::shaderTypeChanged, 1))
            return;
        if (QtMocHelpers::indexOfMethod<void (QQuickGraphicsInfo::*)()>(_a, &QQuickGraphicsInfo::shaderCompilationTypeChanged, 2))
            return;
        if (QtMocHelpers::indexOfMethod<void (QQuickGraphicsInfo::*)()>(_a, &QQuickGraphicsInfo::shaderSourceTypeChanged, 3))
            return;
        if (QtMocHelpers::indexOfMethod<void (QQuickGraphicsInfo::*)()>(_a, &QQuickGraphicsInfo::majorVersionChanged, 4))
            return;
        if (QtMocHelpers::indexOfMethod<void (QQuickGraphicsInfo::*)()>(_a, &QQuickGraphicsInfo::minorVersionChanged, 5))
            return;
        if (QtMocHelpers::indexOfMethod<void (QQuickGraphicsInfo::*)()>(_a, &QQuickGraphicsInfo::profileChanged, 6))
            return;
        if (QtMocHelpers::indexOfMethod<void (QQuickGraphicsInfo::*)()>(_a, &QQuickGraphicsInfo::renderableTypeChanged, 7))
            return;
    }
    if (_c == QMetaObject::ReadProperty) {
        void *_v = _a[0];
        switch (_id) {
        case 0: *reinterpret_cast<enum GraphicsApi*>(_v) = _t->api(); break;
        case 1: *reinterpret_cast<enum ShaderType*>(_v) = _t->shaderType(); break;
        case 2: *reinterpret_cast<enum ShaderCompilationType*>(_v) = _t->shaderCompilationType(); break;
        case 3: *reinterpret_cast<enum ShaderSourceType*>(_v) = _t->shaderSourceType(); break;
        case 4: *reinterpret_cast<int*>(_v) = _t->majorVersion(); break;
        case 5: *reinterpret_cast<int*>(_v) = _t->minorVersion(); break;
        case 6: *reinterpret_cast<enum OpenGLContextProfile*>(_v) = _t->profile(); break;
        case 7: *reinterpret_cast<enum RenderableType*>(_v) = _t->renderableType(); break;
        default: break;
        }
    }
}

const QMetaObject *QQuickGraphicsInfo::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *QQuickGraphicsInfo::qt_metacast(const char *_clname)
{
    if (!_clname) return nullptr;
    if (!strcmp(_clname, qt_staticMetaObjectStaticContent<qt_meta_tag_ZN18QQuickGraphicsInfoE_t>.strings))
        return static_cast<void*>(this);
    return QObject::qt_metacast(_clname);
}

int QQuickGraphicsInfo::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QObject::qt_metacall(_c, _id, _a);
    if (_id < 0)
        return _id;
    if (_c == QMetaObject::InvokeMetaMethod) {
        if (_id < 10)
            qt_static_metacall(this, _c, _id, _a);
        _id -= 10;
    }
    if (_c == QMetaObject::RegisterMethodArgumentMetaType) {
        if (_id < 10)
            *reinterpret_cast<QMetaType *>(_a[0]) = QMetaType();
        _id -= 10;
    }
    if (_c == QMetaObject::ReadProperty || _c == QMetaObject::WriteProperty
            || _c == QMetaObject::ResetProperty || _c == QMetaObject::BindableProperty
            || _c == QMetaObject::RegisterPropertyMetaType) {
        qt_static_metacall(this, _c, _id, _a);
        _id -= 8;
    }
    return _id;
}

// SIGNAL 0
void QQuickGraphicsInfo::apiChanged()
{
    QMetaObject::activate(this, &staticMetaObject, 0, nullptr);
}

// SIGNAL 1
void QQuickGraphicsInfo::shaderTypeChanged()
{
    QMetaObject::activate(this, &staticMetaObject, 1, nullptr);
}

// SIGNAL 2
void QQuickGraphicsInfo::shaderCompilationTypeChanged()
{
    QMetaObject::activate(this, &staticMetaObject, 2, nullptr);
}

// SIGNAL 3
void QQuickGraphicsInfo::shaderSourceTypeChanged()
{
    QMetaObject::activate(this, &staticMetaObject, 3, nullptr);
}

// SIGNAL 4
void QQuickGraphicsInfo::majorVersionChanged()
{
    QMetaObject::activate(this, &staticMetaObject, 4, nullptr);
}

// SIGNAL 5
void QQuickGraphicsInfo::minorVersionChanged()
{
    QMetaObject::activate(this, &staticMetaObject, 5, nullptr);
}

// SIGNAL 6
void QQuickGraphicsInfo::profileChanged()
{
    QMetaObject::activate(this, &staticMetaObject, 6, nullptr);
}

// SIGNAL 7
void QQuickGraphicsInfo::renderableTypeChanged()
{
    QMetaObject::activate(this, &staticMetaObject, 7, nullptr);
}
QT_WARNING_POP

//  from ../qtdeclarative/src/quick/items/qquickgraphicsinfo.cpp, line 210, as _ZN18QQuickGraphicsInfo10updateInfoEv
inline void QQuickGraphicsInfo::updateInfo()
{
    // The queries via the RIF do not depend on isSceneGraphInitialized(), they only need a window.
    if (m_window) {
        QSGRendererInterface *rif = m_window->rendererInterface();
        if (rif) {
            GraphicsApi newAPI = GraphicsApi(rif->graphicsApi());
            if (m_api != newAPI) {
                m_api = newAPI;
                emit apiChanged();
                m_shaderType = ShaderType(rif->shaderType());
                emit shaderTypeChanged();
                m_shaderCompilationType = ShaderCompilationType(int(rif->shaderCompilationType()));
                emit shaderCompilationTypeChanged();
                m_shaderSourceType = ShaderSourceType(int(rif->shaderSourceType()));
                emit shaderSourceTypeChanged();
            }
        }
    }

    QSurfaceFormat format = QSurfaceFormat::defaultFormat();
#if QT_CONFIG(opengl)
    if (m_window && m_window->isSceneGraphInitialized()) {
        QOpenGLContext *context = QQuickWindowPrivate::get(m_window)->openglContext();
        if (context)
            format = context->format();
    }
#endif
    if (m_majorVersion != format.majorVersion()) {
        m_majorVersion = format.majorVersion();
        emit majorVersionChanged();
    }
    if (m_minorVersion != format.minorVersion()) {
        m_minorVersion = format.minorVersion();
        emit minorVersionChanged();
    }
    OpenGLContextProfile profile = static_cast<OpenGLContextProfile>(format.profile());
    if (m_profile != profile) {
        m_profile = profile;
        emit profileChanged();
    }
    RenderableType renderableType = static_cast<RenderableType>(format.renderableType());
    if (m_renderableType != renderableType) {
        m_renderableType = renderableType;
        emit renderableTypeChanged();
    }
}

//  from ../qtdeclarative/src/quick/items/qquickgraphicsinfo.cpp, line 258, as _ZN18QQuickGraphicsInfo9setWindowEP12QQuickWindow
inline void QQuickGraphicsInfo::setWindow(QQuickWindow *window)
{
    if (m_window != window) {
        if (m_window) {
            disconnect(m_window, SIGNAL(sceneGraphInitialized()), this, SLOT(updateInfo()));
            disconnect(m_window, SIGNAL(sceneGraphInvalidated()), this, SLOT(updateInfo()));
        }
        if (window) {
            connect(window, SIGNAL(sceneGraphInitialized()), this, SLOT(updateInfo()));
            connect(window, SIGNAL(sceneGraphInvalidated()), this, SLOT(updateInfo()));
        }
        m_window = window;
    }
    updateInfo();
}

//  from ../qtdeclarative/src/quick/items/qquickgraphicsinfo.cpp, line 28, as _ZN18QQuickGraphicsInfoC1EP10QQuickItem
inline QQuickGraphicsInfo::QQuickGraphicsInfo(QQuickItem *item)
    : QObject(item)
{
    if (Q_LIKELY(item)) {
        connect(item, &QQuickItem::windowChanged, this, &QQuickGraphicsInfo::setWindow);
        setWindow(item->window());
    }
}

//  from ../qtdeclarative/src/quick/items/qquickgraphicsinfo.cpp, line 37, as _ZN18QQuickGraphicsInfoC1EP12QQuickWindow
inline QQuickGraphicsInfo::QQuickGraphicsInfo(QQuickWindow *window)
    : QObject(window)
{
    if (Q_LIKELY(window))
        setWindow(window);
}

//  from ../qtdeclarative/src/quick/items/qquickgraphicsinfo.cpp, line 44, as _ZN18QQuickGraphicsInfo21qmlAttachedPropertiesEP7QObject
inline QQuickGraphicsInfo *QQuickGraphicsInfo::qmlAttachedProperties(QObject *object)
{
    if (QQuickItem *item = qobject_cast<QQuickItem *>(object))
        return new QQuickGraphicsInfo(item);
    if (QQuickWindow *window = qobject_cast<QQuickWindow *>(object))
        return new QQuickGraphicsInfo(window);

    return nullptr;
}
//  -----------------------------------------------------------------------

//  const QMetaObject *QQuickGraphicsInfo::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK18QQuickGraphicsInfo10metaObjectEv(
    const QQuickGraphicsInfo *self) {
  return self->metaObject();
}

//  void *QQuickGraphicsInfo::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN18QQuickGraphicsInfo11qt_metacastEPKc(
    QQuickGraphicsInfo *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickGraphicsInfo::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN18QQuickGraphicsInfo11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickGraphicsInfo *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuickGraphicsInfo::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN18QQuickGraphicsInfo2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickGraphicsInfo::tr(s, c, n));
}

//  void QQuickGraphicsInfo::qt_qmlMarker_uncreatable()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickGraphicsInfo24qt_qmlMarker_uncreatableEv(
    QQuickGraphicsInfo *self) {
  self->qt_qmlMarker_uncreatable();
}

//  void QQuickGraphicsInfo::qt_qmlMarker_attached()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickGraphicsInfo21qt_qmlMarker_attachedEv(
    QQuickGraphicsInfo *self) {
  self->qt_qmlMarker_attached();
}

//  QQuickGraphicsInfo::QQuickGraphicsInfo(QQuickItem *item)
extern "C" Q_DECL_EXPORT
QQuickGraphicsInfo *ritual_ZN18QQuickGraphicsInfoC1EP10QQuickItem(
    QQuickItem *item) {
  return new QQuickGraphicsInfo(item);
}

//  QQuickGraphicsInfo::QQuickGraphicsInfo(QQuickWindow *window)
extern "C" Q_DECL_EXPORT
QQuickGraphicsInfo *ritual_ZN18QQuickGraphicsInfoC1EP12QQuickWindow(
    QQuickWindow *window) {
  return new QQuickGraphicsInfo(window);
}

//  QQuickGraphicsInfo *QQuickGraphicsInfo::qmlAttachedProperties(QObject
//      *object)
extern "C" Q_DECL_EXPORT
QQuickGraphicsInfo *ritual_ZN18QQuickGraphicsInfo21qmlAttachedPropertiesEP7QObject(
    QObject *object) {
  return QQuickGraphicsInfo::qmlAttachedProperties(object);
}

//  GraphicsApi QQuickGraphicsInfo::api() const
extern "C" Q_DECL_EXPORT
QQuickGraphicsInfo::GraphicsApi ritual_ZNK18QQuickGraphicsInfo3apiEv(
    const QQuickGraphicsInfo *self) {
  return self->api();
}

//  ShaderType QQuickGraphicsInfo::shaderType() const
extern "C" Q_DECL_EXPORT
QQuickGraphicsInfo::ShaderType ritual_ZNK18QQuickGraphicsInfo10shaderTypeEv(
    const QQuickGraphicsInfo *self) {
  return self->shaderType();
}

//  ShaderCompilationType QQuickGraphicsInfo::shaderCompilationType() const
extern "C" Q_DECL_EXPORT
QQuickGraphicsInfo::ShaderCompilationType ritual_ZNK18QQuickGraphicsInfo21shaderCompilationTypeEv(
    const QQuickGraphicsInfo *self) {
  return self->shaderCompilationType();
}

//  ShaderSourceType QQuickGraphicsInfo::shaderSourceType() const
extern "C" Q_DECL_EXPORT
QQuickGraphicsInfo::ShaderSourceType ritual_ZNK18QQuickGraphicsInfo16shaderSourceTypeEv(
    const QQuickGraphicsInfo *self) {
  return self->shaderSourceType();
}

//  int QQuickGraphicsInfo::majorVersion() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK18QQuickGraphicsInfo12majorVersionEv(
    const QQuickGraphicsInfo *self) {
  return self->majorVersion();
}

//  int QQuickGraphicsInfo::minorVersion() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK18QQuickGraphicsInfo12minorVersionEv(
    const QQuickGraphicsInfo *self) {
  return self->minorVersion();
}

//  OpenGLContextProfile QQuickGraphicsInfo::profile() const
extern "C" Q_DECL_EXPORT
QQuickGraphicsInfo::OpenGLContextProfile ritual_ZNK18QQuickGraphicsInfo7profileEv(
    const QQuickGraphicsInfo *self) {
  return self->profile();
}

//  RenderableType QQuickGraphicsInfo::renderableType() const
extern "C" Q_DECL_EXPORT
QQuickGraphicsInfo::RenderableType ritual_ZNK18QQuickGraphicsInfo14renderableTypeEv(
    const QQuickGraphicsInfo *self) {
  return self->renderableType();
}

//  void QQuickGraphicsInfo::apiChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickGraphicsInfo10apiChangedEv(QQuickGraphicsInfo *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuickGraphicsInfo")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "apiChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "apiChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuickGraphicsInfo::shaderTypeChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickGraphicsInfo17shaderTypeChangedEv(
    QQuickGraphicsInfo *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuickGraphicsInfo")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "shaderTypeChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "shaderTypeChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuickGraphicsInfo::shaderCompilationTypeChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickGraphicsInfo28shaderCompilationTypeChangedEv(
    QQuickGraphicsInfo *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuickGraphicsInfo")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "shaderCompilationTypeChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "shaderCompilationTypeChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuickGraphicsInfo::shaderSourceTypeChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickGraphicsInfo23shaderSourceTypeChangedEv(
    QQuickGraphicsInfo *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuickGraphicsInfo")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "shaderSourceTypeChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "shaderSourceTypeChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuickGraphicsInfo::majorVersionChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickGraphicsInfo19majorVersionChangedEv(
    QQuickGraphicsInfo *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuickGraphicsInfo")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "majorVersionChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "majorVersionChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuickGraphicsInfo::minorVersionChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickGraphicsInfo19minorVersionChangedEv(
    QQuickGraphicsInfo *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuickGraphicsInfo")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "minorVersionChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "minorVersionChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuickGraphicsInfo::profileChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickGraphicsInfo14profileChangedEv(
    QQuickGraphicsInfo *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuickGraphicsInfo")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "profileChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "profileChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuickGraphicsInfo::renderableTypeChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickGraphicsInfo21renderableTypeChangedEv(
    QQuickGraphicsInfo *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuickGraphicsInfo")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "renderableTypeChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "renderableTypeChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuickGraphicsInfo::updateInfo()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickGraphicsInfo10updateInfoEv(QQuickGraphicsInfo *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuickGraphicsInfo")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "updateInfo()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "updateInfo()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuickGraphicsInfo::setWindow(QQuickWindow *window)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickGraphicsInfo9setWindowEP12QQuickWindow(
    QQuickGraphicsInfo *self,
    QQuickWindow *window) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuickGraphicsInfo")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "setWindow(QQuickWindow *)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "setWindow(QQuickWindow *)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(&window)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}
