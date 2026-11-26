//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DExtras/6.12.0/Qt3DExtras/private/distancefieldtextrenderer_p_p.h, Qt
//  6.12.0.
//  Edited by hand on 2026-11-26: added are 1 rituals that lean on what moc
//  writes for a class of the part Qt keeps to itself, whose ritual file
//  carries moc's output, drafted by a copy of the generator that lets those
//  names through. A copy of a meta-object is a second one: 'qobject_cast'
//  between it and Qt's own does not match. Kept as it is when the generator
//  runs again.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <Qt3DExtras/Qt3DExtras>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DExtras/6.12.0/Qt3DExtras/private/distancefieldtextrenderer_p_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
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
#include <Qt3DCore/qbuffer.h>
#include <Qt3DCore/qattribute.h>
#include <Qt3DCore/qgeometry.h>
#include <Qt3DRender/qmaterial.h>
#include <Qt3DRender/qgeometryrenderer.h>
#include <Qt3DExtras/private/qtext2dmaterial_p.h>
#include <Qt3DExtras/private/distancefieldtextrenderer_p.h>
#include <Qt3DExtras/private/distancefieldtextrenderer_p_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qt3d/src/extras/text/qtext2dmaterial.cpp, line 128, as _ZN10Qt3DExtras15QText2DMaterialC1EPN8Qt3DCore5QNodeE
namespace Qt3DExtras {
inline QText2DMaterial::QText2DMaterial(Qt3DCore::QNode *parent)
    : QMaterial(*new QText2DMaterialPrivate(), parent)
{
    Q_D(QText2DMaterial);
    d->init();
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

//  from ../qt3d/src/extras/text/distancefieldtextrenderer.cpp, line 33, as _ZN10Qt3DExtras32DistanceFieldTextRendererPrivateD1Ev
namespace Qt3DExtras {
using namespace Qt3DCore;
inline DistanceFieldTextRendererPrivate::~DistanceFieldTextRendererPrivate()
{
}
}  // namespace Qt3DExtras

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
//  -----------------------------------------------------------------------

//  A Qt3DExtras::DistanceFieldTextRendererPrivate that Python can take functions over in. Every Qt3DExtras::DistanceFieldTextRendererPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQt3DExtras_DistanceFieldTextRendererPrivateCall0)(const void *, Qt3DCore::QScene *, int *);
typedef void (*CuteQt3DExtras_DistanceFieldTextRendererPrivateCall1)(const void *, int *);
class CuteQt3DExtras_DistanceFieldTextRendererPrivate : public Qt3DExtras::DistanceFieldTextRendererPrivate {
public:
  using Qt3DExtras::DistanceFieldTextRendererPrivate::DistanceFieldTextRendererPrivate;
  void *taken[2] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN8Qt3DCore12QNodePrivate8setSceneEPNS_6QSceneE")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN8Qt3DCore12QNodePrivate6updateEv")) {
      taken[1] = call;
      return true;
    }
    return false;
  }

  //  void Qt3DCore::QNodePrivate::setScene(QScene *scene)
  void setScene(Qt3DCore::QScene *scene) override {
    if (taken[0]) {
      int handled = 0;
      CuteQt3DExtras_DistanceFieldTextRendererPrivateCall0 call = reinterpret_cast<CuteQt3DExtras_DistanceFieldTextRendererPrivateCall0>(taken[0]);
      call(this, scene, &handled);
      if (handled) return;
    }
    Qt3DCore::QNodePrivate::setScene(scene);
  }

  //  void Qt3DCore::QNodePrivate::update()
  void update() override {
    if (taken[1]) {
      int handled = 0;
      CuteQt3DExtras_DistanceFieldTextRendererPrivateCall1 call = reinterpret_cast<CuteQt3DExtras_DistanceFieldTextRendererPrivateCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    Qt3DCore::QNodePrivate::update();
  }
};

//  Qt3DExtras::DistanceFieldTextRendererPrivate::DistanceFieldTextRendererPr
//      ivate()
extern "C" Q_DECL_EXPORT
Qt3DExtras::DistanceFieldTextRendererPrivate *ritual_ZN10Qt3DExtras32DistanceFieldTextRendererPrivateC1Ev() {
  return new CuteQt3DExtras_DistanceFieldTextRendererPrivate();
}

//  Qt3DExtras::DistanceFieldTextRendererPrivate::~DistanceFieldTextRendererP
//      rivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras32DistanceFieldTextRendererPrivateD1Ev(
    Qt3DExtras::DistanceFieldTextRendererPrivate *self) {
  delete self;
}

//  DistanceFieldTextRenderer
//      *Qt3DExtras::DistanceFieldTextRendererPrivate::q_func()
extern "C" Q_DECL_EXPORT
Qt3DExtras::DistanceFieldTextRenderer *ritual_ZN10Qt3DExtras32DistanceFieldTextRendererPrivate6q_funcEv(
    Qt3DExtras::DistanceFieldTextRendererPrivate *self) {
  return self->q_func();
}

//  const DistanceFieldTextRenderer
//      *Qt3DExtras::DistanceFieldTextRendererPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const Qt3DExtras::DistanceFieldTextRenderer *ritual_ZNK10Qt3DExtras32DistanceFieldTextRendererPrivate6q_funcEv(
    const Qt3DExtras::DistanceFieldTextRendererPrivate *self) {
  return self->q_func();
}

//  void Qt3DExtras::DistanceFieldTextRendererPrivate::init()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras32DistanceFieldTextRendererPrivate4initEv(
    Qt3DExtras::DistanceFieldTextRendererPrivate *self) {
  self->init();
}

//  a Python function taken by a
//      CuteQt3DExtras_DistanceFieldTextRendererPrivate, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DExtras_DistanceFieldTextRendererPrivate(
    Qt3DExtras::DistanceFieldTextRendererPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DExtras_DistanceFieldTextRendererPrivate *>(self)->take(key, call);
}
