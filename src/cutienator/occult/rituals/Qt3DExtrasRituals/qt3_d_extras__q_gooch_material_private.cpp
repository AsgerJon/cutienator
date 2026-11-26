//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DExtras/6.12.0/Qt3DExtras/private/qgoochmaterial_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <Qt3DExtras/Qt3DExtras>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DExtras/6.12.0/Qt3DExtras/private/qgoochmaterial_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qvariant.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DExtras/qgoochmaterial.h>
#include <Qt3DExtras/private/qgoochmaterial_p.h>
#include <Qt3DRender/qfilterkey.h>
#include <Qt3DRender/qeffect.h>
#include <Qt3DRender/qgraphicsapifilter.h>
#include <Qt3DRender/qparameter.h>
#include <Qt3DRender/qrenderpass.h>
#include <Qt3DRender/qtechnique.h>
#include <QtCore/qurl.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qt3d/src/extras/defaults/qgoochmaterial.cpp, line 19, as _ZN10Qt3DExtras21QGoochMaterialPrivateC1Ev
namespace Qt3DExtras {
inline QGoochMaterialPrivate::QGoochMaterialPrivate()
    : QMaterialPrivate()
    , m_effect(new Qt3DRender::QEffect)
    , m_diffuseParameter(new Qt3DRender::QParameter(QStringLiteral("kd"), QColor::fromRgbF(0.0f, 0.0f, 0.0f)))
    , m_specularParameter(new Qt3DRender::QParameter(QStringLiteral("ks"), QColor::fromRgbF(0.0f, 0.0f, 0.0f)))
    , m_coolParameter(new Qt3DRender::QParameter(QStringLiteral("kblue"), QColor::fromRgbF(0.0f, 0.0f, 0.4f)))
    , m_warmParameter(new Qt3DRender::QParameter(QStringLiteral("kyellow"), QColor::fromRgbF(0.4f, 0.4f, 0.0f)))
    , m_alphaParameter(new Qt3DRender::QParameter(QStringLiteral("alpha"), 0.25f))
    , m_betaParameter(new Qt3DRender::QParameter(QStringLiteral("beta"), 0.5f))
    , m_shininessParameter(new Qt3DRender::QParameter(QStringLiteral("shininess"), 100.0f))
    , m_gl3Technique(new Qt3DRender::QTechnique)
    , m_gl2Technique(new Qt3DRender::QTechnique)
    , m_es2Technique(new Qt3DRender::QTechnique)
    , m_rhiTechnique(new Qt3DRender::QTechnique)
    , m_gl3RenderPass(new Qt3DRender::QRenderPass)
    , m_gl2RenderPass(new Qt3DRender::QRenderPass)
    , m_es2RenderPass(new Qt3DRender::QRenderPass)
    , m_rhiRenderPass(new Qt3DRender::QRenderPass)
    , m_gl3Shader(new Qt3DRender::QShaderProgram)
    , m_gl2ES2Shader(new Qt3DRender::QShaderProgram)
    , m_rhiShader(new Qt3DRender::QShaderProgram)
    , m_filterKey(new Qt3DRender::QFilterKey)
{
}
}  // namespace Qt3DExtras

//  from ../qt3d/src/extras/defaults/qgoochmaterial.cpp, line 44, as _ZN10Qt3DExtras21QGoochMaterialPrivate4initEv
namespace Qt3DExtras {
inline void QGoochMaterialPrivate::init()
{
    Q_Q(QGoochMaterial);

    connect(m_diffuseParameter, &Qt3DRender::QParameter::valueChanged,
            this, &QGoochMaterialPrivate::handleDiffuseChanged);
    connect(m_specularParameter, &Qt3DRender::QParameter::valueChanged,
            this, &QGoochMaterialPrivate::handleSpecularChanged);
    connect(m_coolParameter, &Qt3DRender::QParameter::valueChanged,
            this, &QGoochMaterialPrivate::handleCoolChanged);
    connect(m_warmParameter, &Qt3DRender::QParameter::valueChanged,
            this, &QGoochMaterialPrivate::handleWarmChanged);
    connect(m_alphaParameter, &Qt3DRender::QParameter::valueChanged,
            this, &QGoochMaterialPrivate::handleAlphaChanged);
    connect(m_betaParameter, &Qt3DRender::QParameter::valueChanged,
            this, &QGoochMaterialPrivate::handleBetaChanged);
    connect(m_shininessParameter, &Qt3DRender::QParameter::valueChanged,
            this, &QGoochMaterialPrivate::handleShininessChanged);

    m_gl3Shader->setVertexShaderCode(Qt3DRender::QShaderProgram::loadSource(QUrl(QStringLiteral("qrc:/shaders/gl3/gooch.vert"))));
    m_gl3Shader->setFragmentShaderCode(Qt3DRender::QShaderProgram::loadSource(QUrl(QStringLiteral("qrc:/shaders/gl3/gooch.frag"))));
    m_gl2ES2Shader->setVertexShaderCode(Qt3DRender::QShaderProgram::loadSource(QUrl(QStringLiteral("qrc:/shaders/es2/gooch.vert"))));
    m_gl2ES2Shader->setFragmentShaderCode(Qt3DRender::QShaderProgram::loadSource(QUrl(QStringLiteral("qrc:/shaders/es2/gooch.frag"))));
    m_rhiShader->setVertexShaderCode(Qt3DRender::QShaderProgram::loadSource(QUrl(QStringLiteral("qrc:/shaders/rhi/gooch.vert"))));
    m_rhiShader->setFragmentShaderCode(Qt3DRender::QShaderProgram::loadSource(QUrl(QStringLiteral("qrc:/shaders/rhi/gooch.frag"))));

    m_gl3Technique->graphicsApiFilter()->setApi(Qt3DRender::QGraphicsApiFilter::OpenGL);
    m_gl3Technique->graphicsApiFilter()->setMajorVersion(3);
    m_gl3Technique->graphicsApiFilter()->setMinorVersion(1);
    m_gl3Technique->graphicsApiFilter()->setProfile(Qt3DRender::QGraphicsApiFilter::CoreProfile);

    m_gl2Technique->graphicsApiFilter()->setApi(Qt3DRender::QGraphicsApiFilter::OpenGL);
    m_gl2Technique->graphicsApiFilter()->setMajorVersion(2);
    m_gl2Technique->graphicsApiFilter()->setMinorVersion(0);
    m_gl2Technique->graphicsApiFilter()->setProfile(Qt3DRender::QGraphicsApiFilter::NoProfile);

    m_es2Technique->graphicsApiFilter()->setApi(Qt3DRender::QGraphicsApiFilter::OpenGLES);
    m_es2Technique->graphicsApiFilter()->setMajorVersion(2);
    m_es2Technique->graphicsApiFilter()->setMinorVersion(0);
    m_es2Technique->graphicsApiFilter()->setProfile(Qt3DRender::QGraphicsApiFilter::NoProfile);

    m_rhiTechnique->graphicsApiFilter()->setApi(Qt3DRender::QGraphicsApiFilter::RHI);
    m_rhiTechnique->graphicsApiFilter()->setMajorVersion(1);
    m_rhiTechnique->graphicsApiFilter()->setMinorVersion(0);
    m_rhiTechnique->graphicsApiFilter()->setProfile(Qt3DRender::QGraphicsApiFilter::CoreProfile);

    m_filterKey->setParent(q);
    m_filterKey->setName(QStringLiteral("renderingStyle"));
    m_filterKey->setValue(QStringLiteral("forward"));

    m_gl3Technique->addFilterKey(m_filterKey);
    m_gl2Technique->addFilterKey(m_filterKey);
    m_es2Technique->addFilterKey(m_filterKey);
    m_rhiTechnique->addFilterKey(m_filterKey);

    m_gl3RenderPass->setShaderProgram(m_gl3Shader);
    m_gl2RenderPass->setShaderProgram(m_gl2ES2Shader);
    m_es2RenderPass->setShaderProgram(m_gl2ES2Shader);
    m_rhiRenderPass->setShaderProgram(m_rhiShader);

    m_gl3Technique->addRenderPass(m_gl3RenderPass);
    m_gl2Technique->addRenderPass(m_gl2RenderPass);
    m_es2Technique->addRenderPass(m_es2RenderPass);
    m_rhiTechnique->addRenderPass(m_rhiRenderPass);

    m_effect->addTechnique(m_gl3Technique);
    m_effect->addTechnique(m_gl2Technique);
    m_effect->addTechnique(m_es2Technique);
    m_effect->addTechnique(m_rhiTechnique);

    m_effect->addParameter(m_diffuseParameter);
    m_effect->addParameter(m_specularParameter);
    m_effect->addParameter(m_coolParameter);
    m_effect->addParameter(m_warmParameter);
    m_effect->addParameter(m_alphaParameter);
    m_effect->addParameter(m_betaParameter);
    m_effect->addParameter(m_shininessParameter);

    q->setEffect(m_effect);
}
}  // namespace Qt3DExtras

//  from ../qt3d/src/extras/defaults/qgoochmaterial.cpp, line 125, as _ZN10Qt3DExtras21QGoochMaterialPrivate20handleDiffuseChangedERK8QVariant
namespace Qt3DExtras {
inline void QGoochMaterialPrivate::handleDiffuseChanged(const QVariant &var)
{
    Q_Q(QGoochMaterial);
    emit q->diffuseChanged(var.value<QColor>());
}
}  // namespace Qt3DExtras

//  from ../qt3d/src/extras/defaults/qgoochmaterial.cpp, line 131, as _ZN10Qt3DExtras21QGoochMaterialPrivate21handleSpecularChangedERK8QVariant
namespace Qt3DExtras {
inline void QGoochMaterialPrivate::handleSpecularChanged(const QVariant &var)
{
    Q_Q(QGoochMaterial);
    emit q->specularChanged(var.value<QColor>());
}
}  // namespace Qt3DExtras

//  from ../qt3d/src/extras/defaults/qgoochmaterial.cpp, line 137, as _ZN10Qt3DExtras21QGoochMaterialPrivate17handleCoolChangedERK8QVariant
namespace Qt3DExtras {
inline void QGoochMaterialPrivate::handleCoolChanged(const QVariant &var)
{
    Q_Q(QGoochMaterial);
    emit q->coolChanged(var.value<QColor>());
}
}  // namespace Qt3DExtras

//  from ../qt3d/src/extras/defaults/qgoochmaterial.cpp, line 143, as _ZN10Qt3DExtras21QGoochMaterialPrivate17handleWarmChangedERK8QVariant
namespace Qt3DExtras {
inline void QGoochMaterialPrivate::handleWarmChanged(const QVariant &var)
{
    Q_Q(QGoochMaterial);
    emit q->warmChanged(var.value<QColor>());
}
}  // namespace Qt3DExtras

//  from ../qt3d/src/extras/defaults/qgoochmaterial.cpp, line 149, as _ZN10Qt3DExtras21QGoochMaterialPrivate18handleAlphaChangedERK8QVariant
namespace Qt3DExtras {
inline void QGoochMaterialPrivate::handleAlphaChanged(const QVariant &var)
{
    Q_Q(QGoochMaterial);
    emit q->alphaChanged(var.toFloat());
}
}  // namespace Qt3DExtras

//  from ../qt3d/src/extras/defaults/qgoochmaterial.cpp, line 155, as _ZN10Qt3DExtras21QGoochMaterialPrivate17handleBetaChangedERK8QVariant
namespace Qt3DExtras {
inline void QGoochMaterialPrivate::handleBetaChanged(const QVariant &var)
{
    Q_Q(QGoochMaterial);
    emit q->betaChanged(var.toFloat());
}
}  // namespace Qt3DExtras

//  from ../qt3d/src/extras/defaults/qgoochmaterial.cpp, line 161, as _ZN10Qt3DExtras21QGoochMaterialPrivate22handleShininessChangedERK8QVariant
namespace Qt3DExtras {
inline void QGoochMaterialPrivate::handleShininessChanged(const QVariant &var)
{
    Q_Q(QGoochMaterial);
    emit q->shininessChanged(var.toFloat());
}
}  // namespace Qt3DExtras
//  -----------------------------------------------------------------------

//  A Qt3DExtras::QGoochMaterialPrivate that Python can take functions over in. Every Qt3DExtras::QGoochMaterialPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQt3DExtras_QGoochMaterialPrivateCall0)(const void *, Qt3DCore::QScene *, int *);
typedef void (*CuteQt3DExtras_QGoochMaterialPrivateCall1)(const void *, int *);
class CuteQt3DExtras_QGoochMaterialPrivate : public Qt3DExtras::QGoochMaterialPrivate {
public:
  using Qt3DExtras::QGoochMaterialPrivate::QGoochMaterialPrivate;
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
      CuteQt3DExtras_QGoochMaterialPrivateCall0 call = reinterpret_cast<CuteQt3DExtras_QGoochMaterialPrivateCall0>(taken[0]);
      call(this, scene, &handled);
      if (handled) return;
    }
    Qt3DCore::QNodePrivate::setScene(scene);
  }

  //  void Qt3DCore::QNodePrivate::update()
  void update() override {
    if (taken[1]) {
      int handled = 0;
      CuteQt3DExtras_QGoochMaterialPrivateCall1 call = reinterpret_cast<CuteQt3DExtras_QGoochMaterialPrivateCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    Qt3DCore::QNodePrivate::update();
  }
};

//  Qt3DExtras::QGoochMaterialPrivate::QGoochMaterialPrivate()
extern "C" Q_DECL_EXPORT
Qt3DExtras::QGoochMaterialPrivate *ritual_ZN10Qt3DExtras21QGoochMaterialPrivateC1Ev() {
  return new CuteQt3DExtras_QGoochMaterialPrivate();
}

//  void Qt3DExtras::QGoochMaterialPrivate::init()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras21QGoochMaterialPrivate4initEv(
    Qt3DExtras::QGoochMaterialPrivate *self) {
  self->init();
}

//  void Qt3DExtras::QGoochMaterialPrivate::handleDiffuseChanged(const
//      QVariant &var)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras21QGoochMaterialPrivate20handleDiffuseChangedERK8QVariant(
    Qt3DExtras::QGoochMaterialPrivate *self,
    const QVariant *var) {
  self->handleDiffuseChanged(*var);
}

//  void Qt3DExtras::QGoochMaterialPrivate::handleSpecularChanged(const
//      QVariant &var)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras21QGoochMaterialPrivate21handleSpecularChangedERK8QVariant(
    Qt3DExtras::QGoochMaterialPrivate *self,
    const QVariant *var) {
  self->handleSpecularChanged(*var);
}

//  void Qt3DExtras::QGoochMaterialPrivate::handleCoolChanged(const QVariant
//      &var)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras21QGoochMaterialPrivate17handleCoolChangedERK8QVariant(
    Qt3DExtras::QGoochMaterialPrivate *self,
    const QVariant *var) {
  self->handleCoolChanged(*var);
}

//  void Qt3DExtras::QGoochMaterialPrivate::handleWarmChanged(const QVariant
//      &var)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras21QGoochMaterialPrivate17handleWarmChangedERK8QVariant(
    Qt3DExtras::QGoochMaterialPrivate *self,
    const QVariant *var) {
  self->handleWarmChanged(*var);
}

//  void Qt3DExtras::QGoochMaterialPrivate::handleAlphaChanged(const QVariant
//      &var)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras21QGoochMaterialPrivate18handleAlphaChangedERK8QVariant(
    Qt3DExtras::QGoochMaterialPrivate *self,
    const QVariant *var) {
  self->handleAlphaChanged(*var);
}

//  void Qt3DExtras::QGoochMaterialPrivate::handleBetaChanged(const QVariant
//      &var)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras21QGoochMaterialPrivate17handleBetaChangedERK8QVariant(
    Qt3DExtras::QGoochMaterialPrivate *self,
    const QVariant *var) {
  self->handleBetaChanged(*var);
}

//  void Qt3DExtras::QGoochMaterialPrivate::handleShininessChanged(const
//      QVariant &var)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras21QGoochMaterialPrivate22handleShininessChangedERK8QVariant(
    Qt3DExtras::QGoochMaterialPrivate *self,
    const QVariant *var) {
  self->handleShininessChanged(*var);
}

//  QGoochMaterial *Qt3DExtras::QGoochMaterialPrivate::q_func()
extern "C" Q_DECL_EXPORT
Qt3DExtras::QGoochMaterial *ritual_ZN10Qt3DExtras21QGoochMaterialPrivate6q_funcEv(
    Qt3DExtras::QGoochMaterialPrivate *self) {
  return self->q_func();
}

//  const QGoochMaterial *Qt3DExtras::QGoochMaterialPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const Qt3DExtras::QGoochMaterial *ritual_ZNK10Qt3DExtras21QGoochMaterialPrivate6q_funcEv(
    const Qt3DExtras::QGoochMaterialPrivate *self) {
  return self->q_func();
}

//  a Python function taken by a CuteQt3DExtras_QGoochMaterialPrivate, for
//      the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DExtras_QGoochMaterialPrivate(
    Qt3DExtras::QGoochMaterialPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DExtras_QGoochMaterialPrivate *>(self)->take(key, call);
}
