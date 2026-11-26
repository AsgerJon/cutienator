//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DExtras/6.12.0/Qt3DExtras/private/qtexturematerial_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <Qt3DExtras/Qt3DExtras>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DExtras/6.12.0/Qt3DExtras/private/qtexturematerial_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qvariant.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DExtras/qtexturematerial.h>
#include <Qt3DExtras/private/qtexturematerial_p.h>
#include <Qt3DRender/qfilterkey.h>
#include <Qt3DRender/qmaterial.h>
#include <Qt3DRender/qeffect.h>
#include <Qt3DRender/qtexture.h>
#include <Qt3DRender/qtechnique.h>
#include <Qt3DRender/qshaderprogram.h>
#include <Qt3DRender/qparameter.h>
#include <Qt3DRender/qrenderpass.h>
#include <Qt3DRender/qgraphicsapifilter.h>
#include <Qt3DRender/qblendequation.h>
#include <Qt3DRender/qblendequationarguments.h>
#include <Qt3DRender/qnodepthmask.h>
#include <QtCore/QUrl>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qt3d/src/extras/defaults/qtexturematerial.cpp, line 26, as _ZN10Qt3DExtras23QTextureMaterialPrivateC1Ev
namespace Qt3DExtras {
using namespace Qt3DRender;
inline QTextureMaterialPrivate::QTextureMaterialPrivate()
    : QMaterialPrivate()
    , m_textureEffect(new QEffect)
    , m_textureParameter(new QParameter(QStringLiteral("diffuseTexture"), new QTexture2D))
    , m_textureTransformParameter(new QParameter(QStringLiteral("texCoordTransform"), QVariant::fromValue(QMatrix3x3())))
    , m_textureGL3Technique(new QTechnique)
    , m_textureGL2Technique(new QTechnique)
    , m_textureES2Technique(new QTechnique)
    , m_textureRHITechnique(new QTechnique)
    , m_textureGL3RenderPass(new QRenderPass)
    , m_textureGL2RenderPass(new QRenderPass)
    , m_textureES2RenderPass(new QRenderPass)
    , m_textureRHIRenderPass(new QRenderPass)
    , m_textureGL3Shader(new QShaderProgram)
    , m_textureGL2ES2Shader(new QShaderProgram)
    , m_textureRHIShader(new QShaderProgram)
    , m_noDepthMask(new QNoDepthMask())
    , m_blendState(new QBlendEquationArguments())
    , m_blendEquation(new QBlendEquation())
    , m_filterKey(new QFilterKey)
{
}
}  // namespace Qt3DExtras

//  from ../qt3d/src/extras/defaults/qtexturematerial.cpp, line 49, as _ZN10Qt3DExtras23QTextureMaterialPrivate4initEv
namespace Qt3DExtras {
using namespace Qt3DRender;
inline void QTextureMaterialPrivate::init()
{
    connect(m_textureParameter, &Qt3DRender::QParameter::valueChanged,
            this, &QTextureMaterialPrivate::handleTextureChanged);
    connect(m_textureTransformParameter, &Qt3DRender::QParameter::valueChanged,
            this, &QTextureMaterialPrivate::handleTextureTransformChanged);

    m_textureGL3Shader->setVertexShaderCode(QShaderProgram::loadSource(QUrl(QStringLiteral("qrc:/shaders/gl3/unlittexture.vert"))));
    m_textureGL3Shader->setFragmentShaderCode(QShaderProgram::loadSource(QUrl(QStringLiteral("qrc:/shaders/gl3/unlittexture.frag"))));
    m_textureGL2ES2Shader->setVertexShaderCode(QShaderProgram::loadSource(QUrl(QStringLiteral("qrc:/shaders/es2/unlittexture.vert"))));
    m_textureGL2ES2Shader->setFragmentShaderCode(QShaderProgram::loadSource(QUrl(QStringLiteral("qrc:/shaders/es2/unlittexture.frag"))));
    m_textureRHIShader->setVertexShaderCode(QShaderProgram::loadSource(QUrl(QStringLiteral("qrc:/shaders/rhi/unlittexture.vert"))));
    m_textureRHIShader->setFragmentShaderCode(QShaderProgram::loadSource(QUrl(QStringLiteral("qrc:/shaders/rhi/unlittexture.frag"))));

    m_textureGL3Technique->graphicsApiFilter()->setApi(QGraphicsApiFilter::OpenGL);
    m_textureGL3Technique->graphicsApiFilter()->setMajorVersion(3);
    m_textureGL3Technique->graphicsApiFilter()->setMinorVersion(1);
    m_textureGL3Technique->graphicsApiFilter()->setProfile(QGraphicsApiFilter::CoreProfile);

    m_textureGL2Technique->graphicsApiFilter()->setApi(QGraphicsApiFilter::OpenGL);
    m_textureGL2Technique->graphicsApiFilter()->setMajorVersion(2);
    m_textureGL2Technique->graphicsApiFilter()->setMinorVersion(0);
    m_textureGL2Technique->graphicsApiFilter()->setProfile(QGraphicsApiFilter::NoProfile);

    m_textureES2Technique->graphicsApiFilter()->setApi(QGraphicsApiFilter::OpenGLES);
    m_textureES2Technique->graphicsApiFilter()->setMajorVersion(2);
    m_textureES2Technique->graphicsApiFilter()->setMinorVersion(0);
    m_textureES2Technique->graphicsApiFilter()->setProfile(QGraphicsApiFilter::NoProfile);

    m_textureRHITechnique->graphicsApiFilter()->setApi(QGraphicsApiFilter::RHI);
    m_textureRHITechnique->graphicsApiFilter()->setMajorVersion(1);
    m_textureRHITechnique->graphicsApiFilter()->setMinorVersion(0);

    m_noDepthMask->setEnabled(false);
    m_blendState->setEnabled(false);
    m_blendState->setSourceRgb(QBlendEquationArguments::SourceAlpha);
    m_blendState->setDestinationRgb(QBlendEquationArguments::OneMinusSourceAlpha);
    m_blendEquation->setEnabled(false);
    m_blendEquation->setBlendFunction(QBlendEquation::Add);

    Q_Q(QTextureMaterial);
    m_filterKey->setParent(q);
    m_filterKey->setName(QStringLiteral("renderingStyle"));
    m_filterKey->setValue(QStringLiteral("forward"));

    m_textureGL3Technique->addFilterKey(m_filterKey);
    m_textureGL2Technique->addFilterKey(m_filterKey);
    m_textureES2Technique->addFilterKey(m_filterKey);
    m_textureRHITechnique->addFilterKey(m_filterKey);

    m_textureGL3RenderPass->setShaderProgram(m_textureGL3Shader);
    m_textureGL2RenderPass->setShaderProgram(m_textureGL2ES2Shader);
    m_textureES2RenderPass->setShaderProgram(m_textureGL2ES2Shader);
    m_textureRHIRenderPass->setShaderProgram(m_textureRHIShader);

    m_textureGL3RenderPass->addRenderState(m_noDepthMask);
    m_textureGL3RenderPass->addRenderState(m_blendState);
    m_textureGL3RenderPass->addRenderState(m_blendEquation);

    m_textureGL2RenderPass->addRenderState(m_noDepthMask);
    m_textureGL2RenderPass->addRenderState(m_blendState);
    m_textureGL2RenderPass->addRenderState(m_blendEquation);

    m_textureES2RenderPass->addRenderState(m_noDepthMask);
    m_textureES2RenderPass->addRenderState(m_blendState);
    m_textureES2RenderPass->addRenderState(m_blendEquation);

    m_textureRHIRenderPass->addRenderState(m_noDepthMask);
    m_textureRHIRenderPass->addRenderState(m_blendState);
    m_textureRHIRenderPass->addRenderState(m_blendEquation);

    m_textureGL3Technique->addRenderPass(m_textureGL3RenderPass);
    m_textureGL2Technique->addRenderPass(m_textureGL2RenderPass);
    m_textureES2Technique->addRenderPass(m_textureES2RenderPass);
    m_textureRHITechnique->addRenderPass(m_textureRHIRenderPass);

    m_textureEffect->addTechnique(m_textureGL3Technique);
    m_textureEffect->addTechnique(m_textureGL2Technique);
    m_textureEffect->addTechnique(m_textureES2Technique);
    m_textureEffect->addTechnique(m_textureRHITechnique);

    m_textureEffect->addParameter(m_textureParameter);
    m_textureEffect->addParameter(m_textureTransformParameter);

    q->setEffect(m_textureEffect);
}
}  // namespace Qt3DExtras

//  from ../qt3d/src/extras/defaults/qtexturematerial.cpp, line 136, as _ZN10Qt3DExtras23QTextureMaterialPrivate20handleTextureChangedERK8QVariant
namespace Qt3DExtras {
using namespace Qt3DRender;
inline void QTextureMaterialPrivate::handleTextureChanged(const QVariant &var)
{
    Q_Q(QTextureMaterial);
    emit q->textureChanged(var.value<QAbstractTexture *>());
}
}  // namespace Qt3DExtras

//  from ../qt3d/src/extras/defaults/qtexturematerial.cpp, line 142, as _ZN10Qt3DExtras23QTextureMaterialPrivate29handleTextureTransformChangedERK8QVariant
namespace Qt3DExtras {
using namespace Qt3DRender;
inline void QTextureMaterialPrivate::handleTextureTransformChanged(const QVariant &var)
{
    Q_Q(QTextureMaterial);
    const QMatrix3x3 matrix = var.value<QMatrix3x3>();
    emit q->textureTransformChanged(matrix);
    emit q->textureOffsetChanged(QVector2D(matrix(0, 2), matrix(1, 2)));
}
}  // namespace Qt3DExtras
//  -----------------------------------------------------------------------

//  A Qt3DExtras::QTextureMaterialPrivate that Python can take functions over in. Every Qt3DExtras::QTextureMaterialPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQt3DExtras_QTextureMaterialPrivateCall0)(const void *, Qt3DCore::QScene *, int *);
typedef void (*CuteQt3DExtras_QTextureMaterialPrivateCall1)(const void *, int *);
class CuteQt3DExtras_QTextureMaterialPrivate : public Qt3DExtras::QTextureMaterialPrivate {
public:
  using Qt3DExtras::QTextureMaterialPrivate::QTextureMaterialPrivate;
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
      CuteQt3DExtras_QTextureMaterialPrivateCall0 call = reinterpret_cast<CuteQt3DExtras_QTextureMaterialPrivateCall0>(taken[0]);
      call(this, scene, &handled);
      if (handled) return;
    }
    Qt3DCore::QNodePrivate::setScene(scene);
  }

  //  void Qt3DCore::QNodePrivate::update()
  void update() override {
    if (taken[1]) {
      int handled = 0;
      CuteQt3DExtras_QTextureMaterialPrivateCall1 call = reinterpret_cast<CuteQt3DExtras_QTextureMaterialPrivateCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    Qt3DCore::QNodePrivate::update();
  }
};

//  Qt3DExtras::QTextureMaterialPrivate::QTextureMaterialPrivate()
extern "C" Q_DECL_EXPORT
Qt3DExtras::QTextureMaterialPrivate *ritual_ZN10Qt3DExtras23QTextureMaterialPrivateC1Ev() {
  return new CuteQt3DExtras_QTextureMaterialPrivate();
}

//  void Qt3DExtras::QTextureMaterialPrivate::init()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras23QTextureMaterialPrivate4initEv(
    Qt3DExtras::QTextureMaterialPrivate *self) {
  self->init();
}

//  void Qt3DExtras::QTextureMaterialPrivate::handleTextureChanged(const
//      QVariant &var)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras23QTextureMaterialPrivate20handleTextureChangedERK8QVariant(
    Qt3DExtras::QTextureMaterialPrivate *self,
    const QVariant *var) {
  self->handleTextureChanged(*var);
}

//  void
//      Qt3DExtras::QTextureMaterialPrivate::handleTextureTransformChanged(co
//      nst QVariant &var)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras23QTextureMaterialPrivate29handleTextureTransformChangedERK8QVariant(
    Qt3DExtras::QTextureMaterialPrivate *self,
    const QVariant *var) {
  self->handleTextureTransformChanged(*var);
}

//  QTextureMaterial *Qt3DExtras::QTextureMaterialPrivate::q_func()
extern "C" Q_DECL_EXPORT
Qt3DExtras::QTextureMaterial *ritual_ZN10Qt3DExtras23QTextureMaterialPrivate6q_funcEv(
    Qt3DExtras::QTextureMaterialPrivate *self) {
  return self->q_func();
}

//  const QTextureMaterial *Qt3DExtras::QTextureMaterialPrivate::q_func()
//      const
extern "C" Q_DECL_EXPORT
const Qt3DExtras::QTextureMaterial *ritual_ZNK10Qt3DExtras23QTextureMaterialPrivate6q_funcEv(
    const Qt3DExtras::QTextureMaterialPrivate *self) {
  return self->q_func();
}

//  a Python function taken by a CuteQt3DExtras_QTextureMaterialPrivate, for
//      the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DExtras_QTextureMaterialPrivate(
    Qt3DExtras::QTextureMaterialPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DExtras_QTextureMaterialPrivate *>(self)->take(key, call);
}
