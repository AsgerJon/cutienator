//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DExtras/6.12.0/Qt3DExtras/private/qdiffusespecularmaterial_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <Qt3DExtras/Qt3DExtras>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DExtras/6.12.0/Qt3DExtras/private/qdiffusespecularmaterial_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qvariant.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DExtras/qdiffusespecularmaterial.h>
#include <Qt3DExtras/private/qdiffusespecularmaterial_p.h>
#include <Qt3DRender/qfilterkey.h>
#include <Qt3DRender/qmaterial.h>
#include <Qt3DRender/qeffect.h>
#include <Qt3DRender/qtechnique.h>
#include <Qt3DRender/qtexture.h>
#include <Qt3DRender/qshaderprogram.h>
#include <Qt3DRender/qshaderprogrambuilder.h>
#include <Qt3DRender/qparameter.h>
#include <Qt3DRender/qrenderpass.h>
#include <Qt3DRender/qgraphicsapifilter.h>
#include <Qt3DRender/qblendequation.h>
#include <Qt3DRender/qblendequationarguments.h>
#include <Qt3DRender/qnodepthmask.h>
#include <QtCore/QUrl>
#include <QtGui/QVector3D>
#include <QtGui/QVector4D>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qt3d/src/extras/defaults/qdiffusespecularmaterial.cpp, line 31, as _ZN10Qt3DExtras31QDiffuseSpecularMaterialPrivateC1Ev
namespace Qt3DExtras {
using namespace Qt3DRender;
inline QDiffuseSpecularMaterialPrivate::QDiffuseSpecularMaterialPrivate()
    : QMaterialPrivate()
    , m_effect(new QEffect())
    , m_ambientParameter(new QParameter(QStringLiteral("ka"), QColor::fromRgbF(0.05f, 0.05f, 0.05f, 1.0f)))
    , m_diffuseParameter(new QParameter(QStringLiteral("kd"), QColor::fromRgbF(0.7f, 0.7f, 0.7f, 1.0f)))
    , m_specularParameter(new QParameter(QStringLiteral("ks"), QColor::fromRgbF(0.01f, 0.01f, 0.01f, 1.0f)))
    , m_diffuseTextureParameter(new QParameter(QStringLiteral("diffuseTexture"), QVariant()))
    , m_specularTextureParameter(new QParameter(QStringLiteral("specularTexture"), QVariant()))
    , m_shininessParameter(new QParameter(QStringLiteral("shininess"), 150.0f))
    , m_normalTextureParameter(new QParameter(QStringLiteral("normalTexture"), QVariant()))
    , m_textureScaleParameter(new QParameter(QStringLiteral("texCoordScale"), 1.0f))
    , m_gl3Technique(new QTechnique())
    , m_gl2Technique(new QTechnique())
    , m_es2Technique(new QTechnique())
    , m_rhiTechnique(new QTechnique())
    , m_gl3RenderPass(new QRenderPass())
    , m_gl2RenderPass(new QRenderPass())
    , m_es2RenderPass(new QRenderPass())
    , m_rhiRenderPass(new QRenderPass())
    , m_gl3Shader(new QShaderProgram())
    , m_gl3ShaderBuilder(new QShaderProgramBuilder())
    , m_gl2es2Shader(new QShaderProgram())
    , m_gl2es2ShaderBuilder(new QShaderProgramBuilder())
    , m_rhiShader(new QShaderProgram())
    , m_rhiShaderBuilder(new QShaderProgramBuilder())
    , m_noDepthMask(new QNoDepthMask())
    , m_blendState(new QBlendEquationArguments())
    , m_blendEquation(new QBlendEquation())
    , m_filterKey(new QFilterKey)
{
}
}  // namespace Qt3DExtras

//  from ../qt3d/src/extras/defaults/qdiffusespecularmaterial.cpp, line 63, as _ZN10Qt3DExtras31QDiffuseSpecularMaterialPrivate4initEv
namespace Qt3DExtras {
using namespace Qt3DRender;
inline void QDiffuseSpecularMaterialPrivate::init()
{
    Q_Q(QDiffuseSpecularMaterial);

    connect(m_ambientParameter, &Qt3DRender::QParameter::valueChanged,
            this, &QDiffuseSpecularMaterialPrivate::handleAmbientChanged);
    QObject::connect(m_diffuseParameter, &Qt3DRender::QParameter::valueChanged,
                     q, &QDiffuseSpecularMaterial::diffuseChanged);
    QObject::connect(m_specularParameter, &Qt3DRender::QParameter::valueChanged,
                     q, &QDiffuseSpecularMaterial::specularChanged);
    connect(m_shininessParameter, &Qt3DRender::QParameter::valueChanged,
            this, &QDiffuseSpecularMaterialPrivate::handleShininessChanged);
    QObject::connect(m_normalTextureParameter, &Qt3DRender::QParameter::valueChanged,
                     q, &QDiffuseSpecularMaterial::normalChanged);
    connect(m_textureScaleParameter, &Qt3DRender::QParameter::valueChanged,
            this, &QDiffuseSpecularMaterialPrivate::handleTextureScaleChanged);
    QObject::connect(m_noDepthMask, &QNoDepthMask::enabledChanged,
                     q, &QDiffuseSpecularMaterial::alphaBlendingEnabledChanged);

    m_gl3Shader->setVertexShaderCode(QShaderProgram::loadSource(QUrl(QStringLiteral("qrc:/shaders/gl3/default.vert"))));
    m_gl3ShaderBuilder->setParent(q);
    m_gl3ShaderBuilder->setShaderProgram(m_gl3Shader);
    m_gl3ShaderBuilder->setFragmentShaderGraph(QUrl(QStringLiteral("qrc:/shaders/graphs/phong.frag.json")));
    m_gl3ShaderBuilder->setEnabledLayers({QStringLiteral("diffuse"),
                                               QStringLiteral("specular"),
                                               QStringLiteral("normal")});

    m_gl2es2Shader->setVertexShaderCode(QShaderProgram::loadSource(QUrl(QStringLiteral("qrc:/shaders/es2/default.vert"))));
    m_gl2es2ShaderBuilder->setParent(q);
    m_gl2es2ShaderBuilder->setShaderProgram(m_gl2es2Shader);
    m_gl2es2ShaderBuilder->setFragmentShaderGraph(QUrl(QStringLiteral("qrc:/shaders/graphs/phong.frag.json")));
    m_gl2es2ShaderBuilder->setEnabledLayers({QStringLiteral("diffuse"),
                                                  QStringLiteral("specular"),
                                                  QStringLiteral("normal")});

    m_rhiShader->setVertexShaderCode(QShaderProgram::loadSource(QUrl(QStringLiteral("qrc:/shaders/rhi/default_pos_norm.vert"))));
    m_rhiShaderBuilder->setParent(q);
    m_rhiShaderBuilder->setShaderProgram(m_rhiShader);
    m_rhiShaderBuilder->setFragmentShaderGraph(QUrl(QStringLiteral("qrc:/shaders/graphs/phong.frag.json")));
    m_rhiShaderBuilder->setEnabledLayers({QStringLiteral("diffuse"),
                                               QStringLiteral("specular"),
                                               QStringLiteral("normal")});


    m_gl3Technique->graphicsApiFilter()->setApi(QGraphicsApiFilter::OpenGL);
    m_gl3Technique->graphicsApiFilter()->setMajorVersion(3);
    m_gl3Technique->graphicsApiFilter()->setMinorVersion(1);
    m_gl3Technique->graphicsApiFilter()->setProfile(QGraphicsApiFilter::CoreProfile);

    m_gl2Technique->graphicsApiFilter()->setApi(QGraphicsApiFilter::OpenGL);
    m_gl2Technique->graphicsApiFilter()->setMajorVersion(2);
    m_gl2Technique->graphicsApiFilter()->setMinorVersion(0);
    m_gl2Technique->graphicsApiFilter()->setProfile(QGraphicsApiFilter::NoProfile);

    m_es2Technique->graphicsApiFilter()->setApi(QGraphicsApiFilter::OpenGLES);
    m_es2Technique->graphicsApiFilter()->setMajorVersion(2);
    m_es2Technique->graphicsApiFilter()->setMinorVersion(0);
    m_es2Technique->graphicsApiFilter()->setProfile(QGraphicsApiFilter::NoProfile);

    m_rhiTechnique->graphicsApiFilter()->setApi(QGraphicsApiFilter::RHI);
    m_rhiTechnique->graphicsApiFilter()->setMajorVersion(1);
    m_rhiTechnique->graphicsApiFilter()->setMinorVersion(0);

    m_noDepthMask->setEnabled(false);
    m_blendState->setEnabled(false);
    m_blendState->setSourceRgb(QBlendEquationArguments::SourceAlpha);
    m_blendState->setDestinationRgb(QBlendEquationArguments::OneMinusSourceAlpha);
    m_blendEquation->setEnabled(false);
    m_blendEquation->setBlendFunction(QBlendEquation::Add);

    m_gl3RenderPass->setShaderProgram(m_gl3Shader);
    m_gl2RenderPass->setShaderProgram(m_gl2es2Shader);
    m_es2RenderPass->setShaderProgram(m_gl2es2Shader);
    m_rhiRenderPass->setShaderProgram(m_rhiShader);

    m_gl3RenderPass->addRenderState(m_noDepthMask);
    m_gl3RenderPass->addRenderState(m_blendState);
    m_gl3RenderPass->addRenderState(m_blendEquation);

    m_gl2RenderPass->addRenderState(m_noDepthMask);
    m_gl2RenderPass->addRenderState(m_blendState);
    m_gl2RenderPass->addRenderState(m_blendEquation);

    m_es2RenderPass->addRenderState(m_noDepthMask);
    m_es2RenderPass->addRenderState(m_blendState);
    m_es2RenderPass->addRenderState(m_blendEquation);

    m_rhiRenderPass->addRenderState(m_noDepthMask);
    m_rhiRenderPass->addRenderState(m_blendState);
    m_rhiRenderPass->addRenderState(m_blendEquation);

    m_gl3Technique->addRenderPass(m_gl3RenderPass);
    m_gl2Technique->addRenderPass(m_gl2RenderPass);
    m_es2Technique->addRenderPass(m_es2RenderPass);
    m_rhiTechnique->addRenderPass(m_rhiRenderPass);

    m_filterKey->setParent(q);
    m_filterKey->setName(QStringLiteral("renderingStyle"));
    m_filterKey->setValue(QStringLiteral("forward"));

    m_gl3Technique->addFilterKey(m_filterKey);
    m_gl2Technique->addFilterKey(m_filterKey);
    m_es2Technique->addFilterKey(m_filterKey);
    m_rhiTechnique->addFilterKey(m_filterKey);

    m_effect->addTechnique(m_gl3Technique);
    m_effect->addTechnique(m_gl2Technique);
    m_effect->addTechnique(m_es2Technique);
    m_effect->addTechnique(m_rhiTechnique);

    m_effect->addParameter(m_ambientParameter);
    m_effect->addParameter(m_diffuseParameter);
    m_effect->addParameter(m_specularParameter);
    m_effect->addParameter(m_shininessParameter);
    m_effect->addParameter(m_textureScaleParameter);

    q->setEffect(m_effect);
}
}  // namespace Qt3DExtras

//  from ../qt3d/src/extras/defaults/qdiffusespecularmaterial.cpp, line 182, as _ZN10Qt3DExtras31QDiffuseSpecularMaterialPrivate20handleAmbientChangedERK8QVariant
namespace Qt3DExtras {
using namespace Qt3DRender;
inline void QDiffuseSpecularMaterialPrivate::handleAmbientChanged(const QVariant &var)
{
    Q_Q(QDiffuseSpecularMaterial);
    emit q->ambientChanged(var.value<QColor>());
}
}  // namespace Qt3DExtras

//  from ../qt3d/src/extras/defaults/qdiffusespecularmaterial.cpp, line 188, as _ZN10Qt3DExtras31QDiffuseSpecularMaterialPrivate22handleShininessChangedERK8QVariant
namespace Qt3DExtras {
using namespace Qt3DRender;
inline void QDiffuseSpecularMaterialPrivate::handleShininessChanged(const QVariant &var)
{
    Q_Q(QDiffuseSpecularMaterial);
    emit q->shininessChanged(var.toFloat());
}
}  // namespace Qt3DExtras

//  from ../qt3d/src/extras/defaults/qdiffusespecularmaterial.cpp, line 194, as _ZN10Qt3DExtras31QDiffuseSpecularMaterialPrivate25handleTextureScaleChangedERK8QVariant
namespace Qt3DExtras {
using namespace Qt3DRender;
inline void QDiffuseSpecularMaterialPrivate::handleTextureScaleChanged(const QVariant &var)
{
    Q_Q(QDiffuseSpecularMaterial);
    emit q->textureScaleChanged(var.toFloat());
}
}  // namespace Qt3DExtras
//  -----------------------------------------------------------------------

//  A Qt3DExtras::QDiffuseSpecularMaterialPrivate that Python can take functions over in. Every Qt3DExtras::QDiffuseSpecularMaterialPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQt3DExtras_QDiffuseSpecularMaterialPrivateCall0)(const void *, Qt3DCore::QScene *, int *);
typedef void (*CuteQt3DExtras_QDiffuseSpecularMaterialPrivateCall1)(const void *, int *);
class CuteQt3DExtras_QDiffuseSpecularMaterialPrivate : public Qt3DExtras::QDiffuseSpecularMaterialPrivate {
public:
  using Qt3DExtras::QDiffuseSpecularMaterialPrivate::QDiffuseSpecularMaterialPrivate;
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
      CuteQt3DExtras_QDiffuseSpecularMaterialPrivateCall0 call = reinterpret_cast<CuteQt3DExtras_QDiffuseSpecularMaterialPrivateCall0>(taken[0]);
      call(this, scene, &handled);
      if (handled) return;
    }
    Qt3DCore::QNodePrivate::setScene(scene);
  }

  //  void Qt3DCore::QNodePrivate::update()
  void update() override {
    if (taken[1]) {
      int handled = 0;
      CuteQt3DExtras_QDiffuseSpecularMaterialPrivateCall1 call = reinterpret_cast<CuteQt3DExtras_QDiffuseSpecularMaterialPrivateCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    Qt3DCore::QNodePrivate::update();
  }
};

//  Qt3DExtras::QDiffuseSpecularMaterialPrivate::QDiffuseSpecularMaterialPriv
//      ate()
extern "C" Q_DECL_EXPORT
Qt3DExtras::QDiffuseSpecularMaterialPrivate *ritual_ZN10Qt3DExtras31QDiffuseSpecularMaterialPrivateC1Ev() {
  return new CuteQt3DExtras_QDiffuseSpecularMaterialPrivate();
}

//  void Qt3DExtras::QDiffuseSpecularMaterialPrivate::init()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras31QDiffuseSpecularMaterialPrivate4initEv(
    Qt3DExtras::QDiffuseSpecularMaterialPrivate *self) {
  self->init();
}

//  void
//      Qt3DExtras::QDiffuseSpecularMaterialPrivate::handleAmbientChanged(con
//      st QVariant &var)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras31QDiffuseSpecularMaterialPrivate20handleAmbientChangedERK8QVariant(
    Qt3DExtras::QDiffuseSpecularMaterialPrivate *self,
    const QVariant *var) {
  self->handleAmbientChanged(*var);
}

//  void
//      Qt3DExtras::QDiffuseSpecularMaterialPrivate::handleShininessChanged(c
//      onst QVariant &var)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras31QDiffuseSpecularMaterialPrivate22handleShininessChangedERK8QVariant(
    Qt3DExtras::QDiffuseSpecularMaterialPrivate *self,
    const QVariant *var) {
  self->handleShininessChanged(*var);
}

//  void Qt3DExtras::QDiffuseSpecularMaterialPrivate::handleTextureScaleChang
//      ed(const QVariant &var)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras31QDiffuseSpecularMaterialPrivate25handleTextureScaleChangedERK8QVariant(
    Qt3DExtras::QDiffuseSpecularMaterialPrivate *self,
    const QVariant *var) {
  self->handleTextureScaleChanged(*var);
}

//  QDiffuseSpecularMaterial
//      *Qt3DExtras::QDiffuseSpecularMaterialPrivate::q_func()
extern "C" Q_DECL_EXPORT
Qt3DExtras::QDiffuseSpecularMaterial *ritual_ZN10Qt3DExtras31QDiffuseSpecularMaterialPrivate6q_funcEv(
    Qt3DExtras::QDiffuseSpecularMaterialPrivate *self) {
  return self->q_func();
}

//  const QDiffuseSpecularMaterial
//      *Qt3DExtras::QDiffuseSpecularMaterialPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const Qt3DExtras::QDiffuseSpecularMaterial *ritual_ZNK10Qt3DExtras31QDiffuseSpecularMaterialPrivate6q_funcEv(
    const Qt3DExtras::QDiffuseSpecularMaterialPrivate *self) {
  return self->q_func();
}

//  a Python function taken by a
//      CuteQt3DExtras_QDiffuseSpecularMaterialPrivate, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DExtras_QDiffuseSpecularMaterialPrivate(
    Qt3DExtras::QDiffuseSpecularMaterialPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DExtras_QDiffuseSpecularMaterialPrivate *>(self)->take(key, call);
}
