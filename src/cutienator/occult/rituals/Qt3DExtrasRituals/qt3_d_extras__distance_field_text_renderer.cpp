//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DExtras/6.12.0/Qt3DExtras/private/distancefieldtextrenderer_p.h, Qt
//  6.12.0.
//  Edited by hand on 2026-11-26: moc's output for
//  'Qt3DExtras::DistanceFieldTextRenderer' is pasted in, cut from what the
//  moc of Qt 6.12.0 writes for its header: Qt's library keeps it to itself;
//  added are 2 rituals that lean on what moc writes for a class of the part
//  Qt keeps to itself, whose ritual file carries moc's output, drafted by a
//  copy of the generator that lets those names through. A copy of a meta-
//  object is a second one: 'qobject_cast' between it and Qt's own does not
//  match. Kept as it is when the generator runs again.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <Qt3DExtras/Qt3DExtras>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DExtras/6.12.0/Qt3DExtras/private/distancefieldtextrenderer_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtGui/qcolor.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetatype.h>
#include <QtCore/qtmochelpers.h>
#include <memory>
#include <QtCore/qxptype_traits.h>
#include <Qt3DCore/qbuffer.h>
#include <Qt3DCore/qattribute.h>
#include <Qt3DCore/qgeometry.h>
#include <Qt3DRender/qmaterial.h>
#include <Qt3DRender/qgeometryrenderer.h>
#include <Qt3DExtras/private/qtext2dmaterial_p.h>
#include <Qt3DExtras/private/distancefieldtextrenderer_p.h>
#include <Qt3DExtras/private/distancefieldtextrenderer_p_p.h>
#include <Qt3DExtras/private/qtext2dmaterial_p.h>
#include <Qt3DExtras/private/qtext2dmaterial_p_p.h>
#include <Qt3DRender/qfilterkey.h>
#include <Qt3DRender/qmaterial.h>
#include <Qt3DRender/qeffect.h>
#include <Qt3DRender/qtechnique.h>
#include <Qt3DRender/qshaderprogram.h>
#include <Qt3DRender/qparameter.h>
#include <Qt3DRender/qrenderpass.h>
#include <Qt3DRender/qgraphicsapifilter.h>
#include <Qt3DRender/qblendequation.h>
#include <Qt3DRender/qblendequationarguments.h>
#include <Qt3DRender/qdepthtest.h>
#include <Qt3DRender/qabstracttexture.h>
#include <QtCore/QUrl>
#include <QtGui/QVector3D>
#include <QtGui/QVector4D>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from Qt3DExtras__Qt3DExtras_DistanceFieldTextRenderer.cpp, line 1, as moc:Qt3DExtras::DistanceFieldTextRenderer
#ifndef Q_CONSTINIT
#define Q_CONSTINIT
#endif
QT_WARNING_PUSH
QT_WARNING_DISABLE_DEPRECATED
namespace {
struct qt_meta_tag_ZN10Qt3DExtras25DistanceFieldTextRendererE_t {};
} // unnamed namespace

template <> constexpr inline auto Qt3DExtras::DistanceFieldTextRenderer::qt_create_metaobjectdata<qt_meta_tag_ZN10Qt3DExtras25DistanceFieldTextRendererE_t>()
{
    namespace QMC = QtMocConstants;
    QtMocHelpers::StringRefStorage qt_stringData {
        "Qt3DExtras::DistanceFieldTextRenderer"
    };

    QtMocHelpers::UintData qt_methods {
    };
    QtMocHelpers::UintData qt_properties {
    };
    QtMocHelpers::UintData qt_enums {
    };
    return QtMocHelpers::metaObjectData<DistanceFieldTextRenderer, qt_meta_tag_ZN10Qt3DExtras25DistanceFieldTextRendererE_t>(QMC::MetaObjectFlag{}, qt_stringData,
            qt_methods, qt_properties, qt_enums);
}
Q_CONSTINIT const QMetaObject Qt3DExtras::DistanceFieldTextRenderer::staticMetaObject = { {
    QMetaObject::SuperData::link<Qt3DCore::QEntity::staticMetaObject>(),
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN10Qt3DExtras25DistanceFieldTextRendererE_t>.stringdata,
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN10Qt3DExtras25DistanceFieldTextRendererE_t>.data,
    qt_static_metacall,
    nullptr,
    qt_staticMetaObjectRelocatingContent<qt_meta_tag_ZN10Qt3DExtras25DistanceFieldTextRendererE_t>.metaTypes,
    nullptr
} };

void Qt3DExtras::DistanceFieldTextRenderer::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    auto *_t = static_cast<DistanceFieldTextRenderer *>(_o);
    (void)_t;
    (void)_c;
    (void)_id;
    (void)_a;
}

const QMetaObject *Qt3DExtras::DistanceFieldTextRenderer::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *Qt3DExtras::DistanceFieldTextRenderer::qt_metacast(const char *_clname)
{
    if (!_clname) return nullptr;
    if (!strcmp(_clname, qt_staticMetaObjectStaticContent<qt_meta_tag_ZN10Qt3DExtras25DistanceFieldTextRendererE_t>.strings))
        return static_cast<void*>(this);
    return Qt3DCore::QEntity::qt_metacast(_clname);
}

int Qt3DExtras::DistanceFieldTextRenderer::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = Qt3DCore::QEntity::qt_metacall(_c, _id, _a);
    return _id;
}
QT_WARNING_POP

//  from ../qt3d/src/extras/text/distancefieldtextrenderer.cpp, line 37, as _ZN10Qt3DExtras32DistanceFieldTextRendererPrivate4initEv
namespace Qt3DExtras {
using namespace Qt3DCore;
inline void DistanceFieldTextRendererPrivate::init()
{
    Q_Q(DistanceFieldTextRenderer);

    m_renderer = new Qt3DRender::QGeometryRenderer(q);
    m_renderer->setPrimitiveType(Qt3DRender::QGeometryRenderer::Triangles);

    m_geometry = new Qt3DCore::QGeometry(m_renderer);
    m_renderer->setGeometry(m_geometry);

    m_vertexBuffer = new Qt3DCore::QBuffer(m_geometry);
    m_indexBuffer = new Qt3DCore::QBuffer(m_geometry);

    m_positionAttr = new Qt3DCore::QAttribute(m_geometry);
    m_positionAttr->setName(Qt3DCore::QAttribute::defaultPositionAttributeName());
    m_positionAttr->setVertexBaseType(Qt3DCore::QAttribute::Float);
    m_positionAttr->setAttributeType(Qt3DCore::QAttribute::VertexAttribute);
    m_positionAttr->setVertexSize(3);
    m_positionAttr->setByteStride(5 * sizeof(float));
    m_positionAttr->setByteOffset(0);
    m_positionAttr->setBuffer(m_vertexBuffer);

    m_texCoordAttr = new Qt3DCore::QAttribute(m_geometry);
    m_texCoordAttr->setName(Qt3DCore::QAttribute::defaultTextureCoordinateAttributeName());
    m_texCoordAttr->setVertexBaseType(Qt3DCore::QAttribute::Float);
    m_texCoordAttr->setAttributeType(Qt3DCore::QAttribute::VertexAttribute);
    m_texCoordAttr->setVertexSize(2);
    m_texCoordAttr->setByteStride(5 * sizeof(float));
    m_texCoordAttr->setByteOffset(3 * sizeof(float));
    m_texCoordAttr->setBuffer(m_vertexBuffer);

    m_indexAttr = new Qt3DCore::QAttribute(m_geometry);
    m_indexAttr->setAttributeType(Qt3DCore::QAttribute::IndexAttribute);
    m_indexAttr->setVertexBaseType(Qt3DCore::QAttribute::UnsignedShort);
    m_indexAttr->setBuffer(m_indexBuffer);

    m_geometry->addAttribute(m_positionAttr);
    m_geometry->setBoundingVolumePositionAttribute(m_positionAttr);
    m_geometry->addAttribute(m_texCoordAttr);
    m_geometry->addAttribute(m_indexAttr);

    m_material = new QText2DMaterial(q);

    q->addComponent(m_renderer);
    q->addComponent(m_material);
}
}  // namespace Qt3DExtras

//  from ../qt3d/src/extras/text/distancefieldtextrenderer.cpp, line 21, as _ZN10Qt3DExtras32DistanceFieldTextRendererPrivateC1Ev
namespace Qt3DExtras {
using namespace Qt3DCore;
inline DistanceFieldTextRendererPrivate::DistanceFieldTextRendererPrivate()
    : m_renderer(nullptr)
    , m_geometry(nullptr)
    , m_positionAttr(nullptr)
    , m_texCoordAttr(nullptr)
    , m_indexAttr(nullptr)
    , m_vertexBuffer(nullptr)
    , m_indexBuffer(nullptr)
    , m_material(nullptr)
{
}
}  // namespace Qt3DExtras

//  from ../qt3d/src/extras/text/qtext2dmaterial.cpp, line 145, as _ZN10Qt3DExtras15QText2DMaterial23setDistanceFieldTextureEPN10Qt3DRender16QAbstractTextureE
namespace Qt3DExtras {
inline void QText2DMaterial::setDistanceFieldTexture(Qt3DRender::QAbstractTexture *tex)
{
    Q_D(QText2DMaterial);
    d->m_distanceFieldTexture = tex;

    if (tex) {
        d->m_textureParameter->setValue(QVariant::fromValue(tex));
        d->m_textureSizeParameter->setValue(QVariant::fromValue(static_cast<float>(tex->width())));
    } else {
        d->m_textureParameter->setValue(0);
        d->m_textureSizeParameter->setValue(QVariant::fromValue(1.f));
    }
}
}  // namespace Qt3DExtras

//  from ../qt3d/src/extras/text/qtext2dmaterial.cpp, line 139, as _ZN10Qt3DExtras15QText2DMaterial8setColorERK6QColor
namespace Qt3DExtras {
inline void QText2DMaterial::setColor(const QColor &color)
{
    Q_D(QText2DMaterial);
    d->m_colorParameter->setValue(QVariant::fromValue(color));
}
}  // namespace Qt3DExtras

//  from ../qt3d/src/extras/text/qtext2dmaterial.cpp, line 128, as _ZN10Qt3DExtras15QText2DMaterialC1EPN8Qt3DCore5QNodeE
namespace Qt3DExtras {
inline QText2DMaterial::QText2DMaterial(Qt3DCore::QNode *parent)
    : QMaterial(*new QText2DMaterialPrivate(), parent)
{
    Q_D(QText2DMaterial);
    d->init();
}
}  // namespace Qt3DExtras

//  from ../qt3d/src/extras/text/distancefieldtextrenderer.cpp, line 33, as _ZN10Qt3DExtras32DistanceFieldTextRendererPrivateD1Ev
namespace Qt3DExtras {
using namespace Qt3DCore;
inline DistanceFieldTextRendererPrivate::~DistanceFieldTextRendererPrivate()
{
}
}  // namespace Qt3DExtras

//  from ../qt3d/src/extras/text/qtext2dmaterial.cpp, line 50, as _ZN10Qt3DExtras22QText2DMaterialPrivate4initEv
namespace Qt3DExtras {
inline void QText2DMaterialPrivate::init()
{
    m_rhiShaderProgram->setVertexShaderCode(Qt3DRender::QShaderProgram::loadSource(QUrl(QStringLiteral("qrc:/shaders/rhi/distancefieldtext.vert"))));
    m_rhiShaderProgram->setFragmentShaderCode(Qt3DRender::QShaderProgram::loadSource(QUrl(QStringLiteral("qrc:/shaders/rhi/distancefieldtext.frag"))));

    m_gl3ShaderProgram->setVertexShaderCode(Qt3DRender::QShaderProgram::loadSource(QUrl(QStringLiteral("qrc:/shaders/gl3/distancefieldtext.vert"))));
    m_gl3ShaderProgram->setFragmentShaderCode(Qt3DRender::QShaderProgram::loadSource(QUrl(QStringLiteral("qrc:/shaders/gl3/distancefieldtext.frag"))));

    m_gl2es2ShaderProgram->setVertexShaderCode(Qt3DRender::QShaderProgram::loadSource(QUrl(QStringLiteral("qrc:/shaders/es2/distancefieldtext.vert"))));
    m_gl2es2ShaderProgram->setFragmentShaderCode(Qt3DRender::QShaderProgram::loadSource(QUrl(QStringLiteral("qrc:/shaders/es2/distancefieldtext.frag"))));

    m_blend->setBlendFunction(Qt3DRender::QBlendEquation::Add);
    m_blendArgs->setSourceRgba(Qt3DRender::QBlendEquationArguments::SourceAlpha);
    m_blendArgs->setDestinationRgba(Qt3DRender::QBlendEquationArguments::OneMinusSourceAlpha);
    m_depthTest->setDepthFunction(Qt3DRender::QDepthTest::LessOrEqual);

    m_gl3RenderPass->setShaderProgram(m_gl3ShaderProgram);
    m_gl3RenderPass->addRenderState(m_blend);
    m_gl3RenderPass->addRenderState(m_blendArgs);
    m_gl3RenderPass->addRenderState(m_depthTest);

    m_gl2RenderPass->setShaderProgram(m_gl2es2ShaderProgram);
    m_gl2RenderPass->addRenderState(m_blend);
    m_gl2RenderPass->addRenderState(m_blendArgs);
    m_gl2RenderPass->addRenderState(m_depthTest);

    m_es2RenderPass->setShaderProgram(m_gl2es2ShaderProgram);
    m_es2RenderPass->addRenderState(m_blend);
    m_es2RenderPass->addRenderState(m_blendArgs);
    m_es2RenderPass->addRenderState(m_depthTest);

    m_rhiRenderPass->setShaderProgram(m_rhiShaderProgram);
    m_rhiRenderPass->addRenderState(m_blend);
    m_rhiRenderPass->addRenderState(m_blendArgs);
    m_rhiRenderPass->addRenderState(m_depthTest);

    m_gl3Technique->graphicsApiFilter()->setApi(Qt3DRender::QGraphicsApiFilter::OpenGL);
    m_gl3Technique->graphicsApiFilter()->setMajorVersion(3);
    m_gl3Technique->graphicsApiFilter()->setMinorVersion(1);
    m_gl3Technique->graphicsApiFilter()->setProfile(Qt3DRender::QGraphicsApiFilter::CoreProfile);
    m_gl3Technique->addRenderPass(m_gl3RenderPass);

    m_gl2Technique->graphicsApiFilter()->setApi(Qt3DRender::QGraphicsApiFilter::OpenGL);
    m_gl2Technique->graphicsApiFilter()->setMajorVersion(2);
    m_gl2Technique->graphicsApiFilter()->setMinorVersion(0);
    m_gl2Technique->graphicsApiFilter()->setProfile(Qt3DRender::QGraphicsApiFilter::NoProfile);
    m_gl2Technique->addRenderPass(m_gl2RenderPass);

    m_es2Technique->graphicsApiFilter()->setApi(Qt3DRender::QGraphicsApiFilter::OpenGLES);
    m_es2Technique->graphicsApiFilter()->setMajorVersion(2);
    m_es2Technique->graphicsApiFilter()->setMinorVersion(0);
    m_es2Technique->graphicsApiFilter()->setProfile(Qt3DRender::QGraphicsApiFilter::NoProfile);
    m_es2Technique->addRenderPass(m_es2RenderPass);

    m_rhiTechnique->graphicsApiFilter()->setApi(Qt3DRender::QGraphicsApiFilter::RHI);
    m_rhiTechnique->graphicsApiFilter()->setMajorVersion(1);
    m_rhiTechnique->graphicsApiFilter()->setMinorVersion(0);
    m_rhiTechnique->addRenderPass(m_rhiRenderPass);

    Qt3DRender::QFilterKey *filterKey = new Qt3DRender::QFilterKey(q_func());
    filterKey->setName(QStringLiteral("renderingStyle"));
    filterKey->setValue(QStringLiteral("forward"));
    m_gl3Technique->addFilterKey(filterKey);
    m_gl2Technique->addFilterKey(filterKey);
    m_es2Technique->addFilterKey(filterKey);
    m_rhiTechnique->addFilterKey(filterKey);

    m_effect->addTechnique(m_gl3Technique);
    m_effect->addTechnique(m_gl2Technique);
    m_effect->addTechnique(m_es2Technique);
    m_effect->addTechnique(m_rhiTechnique);
    m_effect->addParameter(m_textureParameter);
    m_effect->addParameter(m_textureSizeParameter);
    m_effect->addParameter(m_colorParameter);

    q_func()->setEffect(m_effect);
}
}  // namespace Qt3DExtras

//  from ../qt3d/src/extras/text/qtext2dmaterial.cpp, line 26, as _ZN10Qt3DExtras22QText2DMaterialPrivateC1Ev
namespace Qt3DExtras {
inline QText2DMaterialPrivate::QText2DMaterialPrivate()
    : QMaterialPrivate()
    , m_effect(new Qt3DRender::QEffect())
    , m_distanceFieldTexture(nullptr)
    , m_textureParameter(new Qt3DRender::QParameter(QStringLiteral("distanceFieldTexture"), QVariant(0)))
    , m_textureSizeParameter(new Qt3DRender::QParameter(QStringLiteral("textureWidth"), QVariant(256.f)))
    , m_colorParameter(new Qt3DRender::QParameter(QStringLiteral("color"), QVariant(QColor(255, 255, 255, 255))))
    , m_gl3Technique(new Qt3DRender::QTechnique())
    , m_gl2Technique(new Qt3DRender::QTechnique())
    , m_es2Technique(new Qt3DRender::QTechnique())
    , m_rhiTechnique(new Qt3DRender::QTechnique())
    , m_gl3RenderPass(new Qt3DRender::QRenderPass())
    , m_gl2RenderPass(new Qt3DRender::QRenderPass())
    , m_es2RenderPass(new Qt3DRender::QRenderPass())
    , m_rhiRenderPass(new Qt3DRender::QRenderPass())
    , m_rhiShaderProgram(new Qt3DRender::QShaderProgram())
    , m_gl3ShaderProgram(new Qt3DRender::QShaderProgram())
    , m_gl2es2ShaderProgram(new Qt3DRender::QShaderProgram())
    , m_blend(new Qt3DRender::QBlendEquation())
    , m_blendArgs(new Qt3DRender::QBlendEquationArguments())
    , m_depthTest(new Qt3DRender::QDepthTest())
{
}
}  // namespace Qt3DExtras

//  from ../qt3d/src/extras/text/distancefieldtextrenderer.cpp, line 84, as _ZN10Qt3DExtras25DistanceFieldTextRendererC1EPN8Qt3DCore5QNodeE
namespace Qt3DExtras {
using namespace Qt3DCore;
inline DistanceFieldTextRenderer::DistanceFieldTextRenderer(QNode *parent)
    : QEntity(*new DistanceFieldTextRendererPrivate(), parent)
{
    Q_D(DistanceFieldTextRenderer);
    d->init();
}
}  // namespace Qt3DExtras

//  from ../qt3d/src/extras/text/distancefieldtextrenderer.cpp, line 91, as _ZN10Qt3DExtras25DistanceFieldTextRendererD1Ev
namespace Qt3DExtras {
using namespace Qt3DCore;
inline DistanceFieldTextRenderer::~DistanceFieldTextRenderer()
{
}
}  // namespace Qt3DExtras

//  from ../qt3d/src/extras/text/distancefieldtextrenderer.cpp, line 95, as _ZN10Qt3DExtras25DistanceFieldTextRenderer12setGlyphDataEPN10Qt3DRender16QAbstractTextureERKSt6vectorIfSaIfEERKS4_ItSaItEE
namespace Qt3DExtras {
using namespace Qt3DCore;
inline void DistanceFieldTextRenderer::setGlyphData(Qt3DRender::QAbstractTexture *glyphTexture,
                                             const std::vector<float> &vertexData,
                                             const std::vector<quint16> &indexData)
{
    Q_D(DistanceFieldTextRenderer);

    const size_t vertexCount = vertexData.size() / 5;

    d->m_vertexBuffer->setData(QByteArray((char*) vertexData.data(), vertexData.size() * sizeof(float)));
    d->m_indexBuffer->setData(QByteArray((char*) indexData.data(), indexData.size() * sizeof(quint16)));
    d->m_positionAttr->setCount(uint(vertexCount));
    d->m_texCoordAttr->setCount(uint(vertexCount));
    d->m_indexAttr->setCount(uint(indexData.size()));

    d->m_material->setDistanceFieldTexture(glyphTexture);
}
}  // namespace Qt3DExtras

//  from ../qt3d/src/extras/text/distancefieldtextrenderer.cpp, line 112, as _ZN10Qt3DExtras25DistanceFieldTextRenderer8setColorERK6QColor
namespace Qt3DExtras {
using namespace Qt3DCore;
inline void DistanceFieldTextRenderer::setColor(const QColor &color)
{
    Q_D(DistanceFieldTextRenderer);
    d->m_material->setColor(color);
}
}  // namespace Qt3DExtras
//  -----------------------------------------------------------------------

//  A Qt3DExtras::DistanceFieldTextRenderer that Python can take functions over in. Every Qt3DExtras::DistanceFieldTextRenderer
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DExtras_DistanceFieldTextRendererCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DExtras_DistanceFieldTextRendererCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DExtras_DistanceFieldTextRendererCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DExtras_DistanceFieldTextRendererCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DExtras_DistanceFieldTextRendererCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DExtras_DistanceFieldTextRendererCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DExtras_DistanceFieldTextRendererCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQt3DExtras_DistanceFieldTextRenderer : public Qt3DExtras::DistanceFieldTextRenderer {
public:
  using Qt3DExtras::DistanceFieldTextRenderer::DistanceFieldTextRenderer;
  void *taken[7] = {};

  bool take(const char *key, void *call) {
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[0] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[1] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[2] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[0]) {
      int handled = 0;
      CuteQt3DExtras_DistanceFieldTextRendererCall0 call = reinterpret_cast<CuteQt3DExtras_DistanceFieldTextRendererCall0>(taken[0]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQt3DExtras_DistanceFieldTextRendererCall1 call = reinterpret_cast<CuteQt3DExtras_DistanceFieldTextRendererCall1>(taken[1]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQt3DExtras_DistanceFieldTextRendererCall2 call = reinterpret_cast<CuteQt3DExtras_DistanceFieldTextRendererCall2>(taken[2]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQt3DExtras_DistanceFieldTextRendererCall3 call = reinterpret_cast<CuteQt3DExtras_DistanceFieldTextRendererCall3>(taken[3]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQt3DExtras_DistanceFieldTextRendererCall4 call = reinterpret_cast<CuteQt3DExtras_DistanceFieldTextRendererCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[5]) {
      int handled = 0;
      CuteQt3DExtras_DistanceFieldTextRendererCall5 call = reinterpret_cast<CuteQt3DExtras_DistanceFieldTextRendererCall5>(taken[5]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[6]) {
      int handled = 0;
      CuteQt3DExtras_DistanceFieldTextRendererCall6 call = reinterpret_cast<CuteQt3DExtras_DistanceFieldTextRendererCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *Qt3DExtras::DistanceFieldTextRenderer::metaObject()
//      const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK10Qt3DExtras25DistanceFieldTextRenderer10metaObjectEv(
    const Qt3DExtras::DistanceFieldTextRenderer *self) {
  return self->metaObject();
}

//  void *Qt3DExtras::DistanceFieldTextRenderer::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN10Qt3DExtras25DistanceFieldTextRenderer11qt_metacastEPKc(
    Qt3DExtras::DistanceFieldTextRenderer *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int Qt3DExtras::DistanceFieldTextRenderer::qt_metacall(QMetaObject::Call
//      a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN10Qt3DExtras25DistanceFieldTextRenderer11qt_metacallEN11QMetaObject4CallEiPPv(
    Qt3DExtras::DistanceFieldTextRenderer *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString Qt3DExtras::DistanceFieldTextRenderer::tr(const char *s, const
//      char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN10Qt3DExtras25DistanceFieldTextRenderer2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(Qt3DExtras::DistanceFieldTextRenderer::tr(s, c, n));
}

//  Qt3DExtras::DistanceFieldTextRenderer::DistanceFieldTextRenderer(Qt3DCore
//      ::QNode *parent)
extern "C" Q_DECL_EXPORT
Qt3DExtras::DistanceFieldTextRenderer *ritual_ZN10Qt3DExtras25DistanceFieldTextRendererC1EPN8Qt3DCore5QNodeE(
    Qt3DCore::QNode *parent) {
  return new CuteQt3DExtras_DistanceFieldTextRenderer(parent);
}

//  Qt3DExtras::DistanceFieldTextRenderer::~DistanceFieldTextRenderer()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras25DistanceFieldTextRendererD1Ev(
    Qt3DExtras::DistanceFieldTextRenderer *self) {
  delete self;
}

//  void Qt3DExtras::DistanceFieldTextRenderer::setGlyphData(Qt3DRender::QAbs
//      tractTexture *glyphTexture, const std::vector<float> &vertexData,
//      const std::vector<quint16> &indexData)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras25DistanceFieldTextRenderer12setGlyphDataEPN10Qt3DRender16QAbstractTextureERKSt6vectorIfSaIfEERKS4_ItSaItEE(
    Qt3DExtras::DistanceFieldTextRenderer *self,
    Qt3DRender::QAbstractTexture *glyphTexture,
    const std::vector<float> *vertexData,
    const std::vector<quint16> *indexData) {
  self->setGlyphData(glyphTexture, *vertexData, *indexData);
}

//  void Qt3DExtras::DistanceFieldTextRenderer::setColor(const QColor &color)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras25DistanceFieldTextRenderer8setColorERK6QColor(
    Qt3DExtras::DistanceFieldTextRenderer *self,
    const QColor *color) {
  self->setColor(*color);
}

//  DistanceFieldTextRendererPrivate
//      *Qt3DExtras::DistanceFieldTextRenderer::d_func()
extern "C" Q_DECL_EXPORT
Qt3DExtras::DistanceFieldTextRendererPrivate *ritual_ZN10Qt3DExtras25DistanceFieldTextRenderer6d_funcEv(
    Qt3DExtras::DistanceFieldTextRenderer *self) {
  return self->d_func();
}

//  const DistanceFieldTextRendererPrivate
//      *Qt3DExtras::DistanceFieldTextRenderer::d_func() const
extern "C" Q_DECL_EXPORT
const Qt3DExtras::DistanceFieldTextRendererPrivate *ritual_ZNK10Qt3DExtras25DistanceFieldTextRenderer6d_funcEv(
    const Qt3DExtras::DistanceFieldTextRenderer *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQt3DExtras_DistanceFieldTextRenderer,
//      for the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DExtras_DistanceFieldTextRenderer(
    Qt3DExtras::DistanceFieldTextRenderer *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DExtras_DistanceFieldTextRenderer *>(self)->take(key, call);
}
