//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DExtras/6.12.0/Qt3DExtras/private/qphongalphamaterial_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <Qt3DExtras/Qt3DExtras>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DExtras/6.12.0/Qt3DExtras/private/qphongalphamaterial_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qvariant.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DExtras/qphongalphamaterial.h>
#include <Qt3DExtras/private/qphongalphamaterial_p.h>
#include <Qt3DRender/qfilterkey.h>
#include <Qt3DRender/qmaterial.h>
#include <Qt3DRender/qeffect.h>
#include <Qt3DRender/qtechnique.h>
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
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qt3d/src/extras/defaults/qphongalphamaterial.cpp, line 29, as _ZN10Qt3DExtras26QPhongAlphaMaterialPrivateC1Ev
namespace Qt3DExtras {
using namespace Qt3DRender;
inline QPhongAlphaMaterialPrivate::QPhongAlphaMaterialPrivate()
    : QMaterialPrivate()
    , m_phongEffect(new QEffect())
    , m_ambientParameter(new QParameter(QStringLiteral("ka"), QColor::fromRgbF(0.05f, 0.05f, 0.05f, 1.0f)))
    , m_diffuseParameter(new QParameter(QStringLiteral("kd"), QColor::fromRgbF(0.7f, 0.7f, 0.7f, 0.5f)))
    , m_specularParameter(new QParameter(QStringLiteral("ks"), QColor::fromRgbF(0.01f, 0.01f, 0.01f, 1.0f)))
    , m_shininessParameter(new QParameter(QStringLiteral("shininess"), 150.0f))
    , m_phongAlphaGL3Technique(new QTechnique())
    , m_phongAlphaGL2Technique(new QTechnique())
    , m_phongAlphaES2Technique(new QTechnique())
    , m_phongAlphaRHITechnique(new QTechnique())
    , m_phongAlphaGL3RenderPass(new QRenderPass())
    , m_phongAlphaGL2RenderPass(new QRenderPass())
    , m_phongAlphaES2RenderPass(new QRenderPass())
    , m_phongAlphaRHIRenderPass(new QRenderPass())
    , m_phongAlphaGL3Shader(new QShaderProgram())
    , m_phongAlphaGL3ShaderBuilder(new QShaderProgramBuilder())
    , m_phongAlphaGL2ES2Shader(new QShaderProgram())
    , m_phongAlphaGL2ES2ShaderBuilder(new QShaderProgramBuilder())
    , m_phongAlphaRHIShader(new QShaderProgram())
    , m_phongAlphaRHIShaderBuilder(new QShaderProgramBuilder())
    , m_noDepthMask(new QNoDepthMask())
    , m_blendState(new QBlendEquationArguments())
    , m_blendEquation(new QBlendEquation())
    , m_filterKey(new QFilterKey)
{
}
}  // namespace Qt3DExtras

//  from ../qt3d/src/extras/defaults/qphongalphamaterial.cpp, line 58, as _ZN10Qt3DExtras26QPhongAlphaMaterialPrivate4initEv
namespace Qt3DExtras {
using namespace Qt3DRender;
inline void QPhongAlphaMaterialPrivate::init()
{
    Q_Q(QPhongAlphaMaterial);

    connect(m_ambientParameter, &Qt3DRender::QParameter::valueChanged,
            this, &QPhongAlphaMaterialPrivate::handleAmbientChanged);
    connect(m_diffuseParameter, &Qt3DRender::QParameter::valueChanged,
            this, &QPhongAlphaMaterialPrivate::handleDiffuseChanged);
    connect(m_specularParameter, &Qt3DRender::QParameter::valueChanged,
            this, &QPhongAlphaMaterialPrivate::handleSpecularChanged);
    connect(m_shininessParameter, &Qt3DRender::QParameter::valueChanged,
            this, &QPhongAlphaMaterialPrivate::handleShininessChanged);

    m_phongAlphaGL3Shader->setVertexShaderCode(QShaderProgram::loadSource(QUrl(QStringLiteral("qrc:/shaders/gl3/default.vert"))));
    m_phongAlphaGL3ShaderBuilder->setParent(q);
    m_phongAlphaGL3ShaderBuilder->setShaderProgram(m_phongAlphaGL3Shader);
    m_phongAlphaGL3ShaderBuilder->setFragmentShaderGraph(QUrl(QStringLiteral("qrc:/shaders/graphs/phong.frag.json")));
    m_phongAlphaGL3ShaderBuilder->setEnabledLayers({QStringLiteral("diffuse"),
                                                    QStringLiteral("specular"),
                                                    QStringLiteral("normal")});

    m_phongAlphaGL2ES2Shader->setVertexShaderCode(QShaderProgram::loadSource(QUrl(QStringLiteral("qrc:/shaders/es2/default.vert"))));
    m_phongAlphaGL2ES2ShaderBuilder->setParent(q);
    m_phongAlphaGL2ES2ShaderBuilder->setShaderProgram(m_phongAlphaGL2ES2Shader);
    m_phongAlphaGL2ES2ShaderBuilder->setFragmentShaderGraph(QUrl(QStringLiteral("qrc:/shaders/graphs/phong.frag.json")));
    m_phongAlphaGL2ES2ShaderBuilder->setEnabledLayers({QStringLiteral("diffuse"),
                                                       QStringLiteral("specular"),
                                                       QStringLiteral("normal")});

    m_phongAlphaRHIShader->setVertexShaderCode(QShaderProgram::loadSource(QUrl(QStringLiteral("qrc:/shaders/rhi/default_pos_norm.vert"))));
    m_phongAlphaRHIShaderBuilder->setParent(q);
    m_phongAlphaRHIShaderBuilder->setShaderProgram(m_phongAlphaRHIShader);
    m_phongAlphaRHIShaderBuilder->setFragmentShaderGraph(QUrl(QStringLiteral("qrc:/shaders/graphs/phong.frag.json")));
    m_phongAlphaRHIShaderBuilder->setEnabledLayers({QStringLiteral("diffuse"),
                                                       QStringLiteral("specular"),
                                                       QStringLiteral("normal")});

    m_phongAlphaGL3Technique->graphicsApiFilter()->setApi(QGraphicsApiFilter::OpenGL);
    m_phongAlphaGL3Technique->graphicsApiFilter()->setMajorVersion(3);
    m_phongAlphaGL3Technique->graphicsApiFilter()->setMinorVersion(1);
    m_phongAlphaGL3Technique->graphicsApiFilter()->setProfile(QGraphicsApiFilter::CoreProfile);

    m_phongAlphaGL2Technique->graphicsApiFilter()->setApi(QGraphicsApiFilter::OpenGL);
    m_phongAlphaGL2Technique->graphicsApiFilter()->setMajorVersion(2);
    m_phongAlphaGL2Technique->graphicsApiFilter()->setMinorVersion(0);
    m_phongAlphaGL2Technique->graphicsApiFilter()->setProfile(QGraphicsApiFilter::NoProfile);

    m_phongAlphaES2Technique->graphicsApiFilter()->setApi(QGraphicsApiFilter::OpenGLES);
    m_phongAlphaES2Technique->graphicsApiFilter()->setMajorVersion(2);
    m_phongAlphaES2Technique->graphicsApiFilter()->setMinorVersion(0);
    m_phongAlphaES2Technique->graphicsApiFilter()->setProfile(QGraphicsApiFilter::NoProfile);

    m_phongAlphaRHITechnique->graphicsApiFilter()->setApi(QGraphicsApiFilter::RHI);
    m_phongAlphaRHITechnique->graphicsApiFilter()->setMajorVersion(1);
    m_phongAlphaRHITechnique->graphicsApiFilter()->setMinorVersion(0);

    m_filterKey->setParent(q);
    m_filterKey->setName(QStringLiteral("renderingStyle"));
    m_filterKey->setValue(QStringLiteral("forward"));

    m_phongAlphaGL3Technique->addFilterKey(m_filterKey);
    m_phongAlphaGL2Technique->addFilterKey(m_filterKey);
    m_phongAlphaES2Technique->addFilterKey(m_filterKey);
    m_phongAlphaRHITechnique->addFilterKey(m_filterKey);

    m_blendState->setSourceRgb(QBlendEquationArguments::SourceAlpha);
    m_blendState->setDestinationRgb(QBlendEquationArguments::OneMinusSourceAlpha);
    m_blendEquation->setBlendFunction(QBlendEquation::Add);

    m_phongAlphaGL3RenderPass->setShaderProgram(m_phongAlphaGL3Shader);
    m_phongAlphaGL2RenderPass->setShaderProgram(m_phongAlphaGL2ES2Shader);
    m_phongAlphaES2RenderPass->setShaderProgram(m_phongAlphaGL2ES2Shader);
    m_phongAlphaRHIRenderPass->setShaderProgram(m_phongAlphaRHIShader);

    m_phongAlphaGL3RenderPass->addRenderState(m_noDepthMask);
    m_phongAlphaGL3RenderPass->addRenderState(m_blendState);
    m_phongAlphaGL3RenderPass->addRenderState(m_blendEquation);

    m_phongAlphaGL2RenderPass->addRenderState(m_noDepthMask);
    m_phongAlphaGL2RenderPass->addRenderState(m_blendState);
    m_phongAlphaGL2RenderPass->addRenderState(m_blendEquation);

    m_phongAlphaES2RenderPass->addRenderState(m_noDepthMask);
    m_phongAlphaES2RenderPass->addRenderState(m_blendState);
    m_phongAlphaES2RenderPass->addRenderState(m_blendEquation);

    m_phongAlphaRHIRenderPass->addRenderState(m_noDepthMask);
    m_phongAlphaRHIRenderPass->addRenderState(m_blendState);
    m_phongAlphaRHIRenderPass->addRenderState(m_blendEquation);

    m_phongAlphaGL3Technique->addRenderPass(m_phongAlphaGL3RenderPass);
    m_phongAlphaGL2Technique->addRenderPass(m_phongAlphaGL2RenderPass);
    m_phongAlphaES2Technique->addRenderPass(m_phongAlphaES2RenderPass);
    m_phongAlphaRHITechnique->addRenderPass(m_phongAlphaRHIRenderPass);

    m_phongEffect->addTechnique(m_phongAlphaGL3Technique);
    m_phongEffect->addTechnique(m_phongAlphaGL2Technique);
    m_phongEffect->addTechnique(m_phongAlphaES2Technique);
    m_phongEffect->addTechnique(m_phongAlphaRHITechnique);

    m_phongEffect->addParameter(m_ambientParameter);
    m_phongEffect->addParameter(m_diffuseParameter);
    m_phongEffect->addParameter(m_specularParameter);
    m_phongEffect->addParameter(m_shininessParameter);

    q->setEffect(m_phongEffect);
}
}  // namespace Qt3DExtras

//  from ../qt3d/src/extras/defaults/qphongalphamaterial.cpp, line 166, as _ZN10Qt3DExtras26QPhongAlphaMaterialPrivate20handleAmbientChangedERK8QVariant
namespace Qt3DExtras {
using namespace Qt3DRender;
inline void QPhongAlphaMaterialPrivate::handleAmbientChanged(const QVariant &var)
{
    Q_Q(QPhongAlphaMaterial);
    emit q->ambientChanged(var.value<QColor>());
}
}  // namespace Qt3DExtras

//  from ../qt3d/src/extras/defaults/qphongalphamaterial.cpp, line 172, as _ZN10Qt3DExtras26QPhongAlphaMaterialPrivate20handleDiffuseChangedERK8QVariant
namespace Qt3DExtras {
using namespace Qt3DRender;
inline void QPhongAlphaMaterialPrivate::handleDiffuseChanged(const QVariant &var)
{
    Q_Q(QPhongAlphaMaterial);
    emit q->diffuseChanged(var.value<QColor>());
    emit q->alphaChanged(var.value<QColor>().alphaF());
}
}  // namespace Qt3DExtras

//  from ../qt3d/src/extras/defaults/qphongalphamaterial.cpp, line 179, as _ZN10Qt3DExtras26QPhongAlphaMaterialPrivate21handleSpecularChangedERK8QVariant
namespace Qt3DExtras {
using namespace Qt3DRender;
inline void QPhongAlphaMaterialPrivate::handleSpecularChanged(const QVariant &var)
{
    Q_Q(QPhongAlphaMaterial);
    emit q->specularChanged(var.value<QColor>());
}
}  // namespace Qt3DExtras

//  from ../qt3d/src/extras/defaults/qphongalphamaterial.cpp, line 185, as _ZN10Qt3DExtras26QPhongAlphaMaterialPrivate22handleShininessChangedERK8QVariant
namespace Qt3DExtras {
using namespace Qt3DRender;
inline void QPhongAlphaMaterialPrivate::handleShininessChanged(const QVariant &var)
{
    Q_Q(QPhongAlphaMaterial);
    emit q->shininessChanged(var.toFloat());
}
}  // namespace Qt3DExtras
//  -----------------------------------------------------------------------

//  A Qt3DExtras::QPhongAlphaMaterialPrivate that Python can take functions over in. Every Qt3DExtras::QPhongAlphaMaterialPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQt3DExtras_QPhongAlphaMaterialPrivateCall0)(const void *, Qt3DCore::QScene *, int *);
typedef void (*CuteQt3DExtras_QPhongAlphaMaterialPrivateCall1)(const void *, int *);
class CuteQt3DExtras_QPhongAlphaMaterialPrivate : public Qt3DExtras::QPhongAlphaMaterialPrivate {
public:
  using Qt3DExtras::QPhongAlphaMaterialPrivate::QPhongAlphaMaterialPrivate;
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
      CuteQt3DExtras_QPhongAlphaMaterialPrivateCall0 call = reinterpret_cast<CuteQt3DExtras_QPhongAlphaMaterialPrivateCall0>(taken[0]);
      call(this, scene, &handled);
      if (handled) return;
    }
    Qt3DCore::QNodePrivate::setScene(scene);
  }

  //  void Qt3DCore::QNodePrivate::update()
  void update() override {
    if (taken[1]) {
      int handled = 0;
      CuteQt3DExtras_QPhongAlphaMaterialPrivateCall1 call = reinterpret_cast<CuteQt3DExtras_QPhongAlphaMaterialPrivateCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    Qt3DCore::QNodePrivate::update();
  }
};

//  Qt3DExtras::QPhongAlphaMaterialPrivate::QPhongAlphaMaterialPrivate()
extern "C" Q_DECL_EXPORT
Qt3DExtras::QPhongAlphaMaterialPrivate *ritual_ZN10Qt3DExtras26QPhongAlphaMaterialPrivateC1Ev() {
  return new CuteQt3DExtras_QPhongAlphaMaterialPrivate();
}

//  void Qt3DExtras::QPhongAlphaMaterialPrivate::init()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras26QPhongAlphaMaterialPrivate4initEv(
    Qt3DExtras::QPhongAlphaMaterialPrivate *self) {
  self->init();
}

//  void Qt3DExtras::QPhongAlphaMaterialPrivate::handleAmbientChanged(const
//      QVariant &var)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras26QPhongAlphaMaterialPrivate20handleAmbientChangedERK8QVariant(
    Qt3DExtras::QPhongAlphaMaterialPrivate *self,
    const QVariant *var) {
  self->handleAmbientChanged(*var);
}

//  void Qt3DExtras::QPhongAlphaMaterialPrivate::handleDiffuseChanged(const
//      QVariant &var)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras26QPhongAlphaMaterialPrivate20handleDiffuseChangedERK8QVariant(
    Qt3DExtras::QPhongAlphaMaterialPrivate *self,
    const QVariant *var) {
  self->handleDiffuseChanged(*var);
}

//  void Qt3DExtras::QPhongAlphaMaterialPrivate::handleSpecularChanged(const
//      QVariant &var)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras26QPhongAlphaMaterialPrivate21handleSpecularChangedERK8QVariant(
    Qt3DExtras::QPhongAlphaMaterialPrivate *self,
    const QVariant *var) {
  self->handleSpecularChanged(*var);
}

//  void Qt3DExtras::QPhongAlphaMaterialPrivate::handleShininessChanged(const
//      QVariant &var)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras26QPhongAlphaMaterialPrivate22handleShininessChangedERK8QVariant(
    Qt3DExtras::QPhongAlphaMaterialPrivate *self,
    const QVariant *var) {
  self->handleShininessChanged(*var);
}

//  QPhongAlphaMaterial *Qt3DExtras::QPhongAlphaMaterialPrivate::q_func()
extern "C" Q_DECL_EXPORT
Qt3DExtras::QPhongAlphaMaterial *ritual_ZN10Qt3DExtras26QPhongAlphaMaterialPrivate6q_funcEv(
    Qt3DExtras::QPhongAlphaMaterialPrivate *self) {
  return self->q_func();
}

//  const QPhongAlphaMaterial
//      *Qt3DExtras::QPhongAlphaMaterialPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const Qt3DExtras::QPhongAlphaMaterial *ritual_ZNK10Qt3DExtras26QPhongAlphaMaterialPrivate6q_funcEv(
    const Qt3DExtras::QPhongAlphaMaterialPrivate *self) {
  return self->q_func();
}

//  a Python function taken by a CuteQt3DExtras_QPhongAlphaMaterialPrivate,
//      for the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DExtras_QPhongAlphaMaterialPrivate(
    Qt3DExtras::QPhongAlphaMaterialPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DExtras_QPhongAlphaMaterialPrivate *>(self)->take(key, call);
}
