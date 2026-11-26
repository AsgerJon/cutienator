//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DExtras/6.12.0/Qt3DExtras/private/qmorphphongmaterial_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <Qt3DExtras/Qt3DExtras>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DExtras/6.12.0/Qt3DExtras/private/qmorphphongmaterial_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qvariant.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DExtras/qmorphphongmaterial.h>
#include <Qt3DExtras/private/qmorphphongmaterial_p.h>
#include <Qt3DRender/qfilterkey.h>
#include <Qt3DRender/qmaterial.h>
#include <Qt3DRender/qeffect.h>
#include <Qt3DRender/qtechnique.h>
#include <Qt3DRender/qshaderprogram.h>
#include <Qt3DRender/qparameter.h>
#include <Qt3DRender/qrenderpass.h>
#include <Qt3DRender/qgraphicsapifilter.h>
#include <Qt3DRender/qshaderprogrambuilder.h>
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

//  from ../qt3d/src/extras/defaults/qmorphphongmaterial.cpp, line 25, as _ZN10Qt3DExtras26QMorphPhongMaterialPrivateC1Ev
namespace Qt3DExtras {
using namespace Qt3DRender;
inline QMorphPhongMaterialPrivate::QMorphPhongMaterialPrivate()
    : QMaterialPrivate()
    , m_phongEffect(new QEffect())
    , m_ambientParameter(new QParameter(QStringLiteral("ka"), QColor::fromRgbF(0.05f, 0.05f, 0.05f, 1.0f)))
    , m_diffuseParameter(new QParameter(QStringLiteral("kd"), QColor::fromRgbF(0.7f, 0.7f, 0.7f, 1.0f)))
    , m_specularParameter(new QParameter(QStringLiteral("ks"), QColor::fromRgbF(0.01f, 0.01f, 0.01f, 1.0f)))
    , m_shininessParameter(new QParameter(QStringLiteral("shininess"), 150.0f))
    , m_interpolatorParameter(new QParameter(QStringLiteral("interpolator"), 0.0f))
    , m_phongGL3Technique(new QTechnique())
    , m_phongGL2Technique(new QTechnique())
    , m_phongES2Technique(new QTechnique())
    , m_phongRHITechnique(new QTechnique())
    , m_phongGL3RenderPass(new QRenderPass())
    , m_phongGL2RenderPass(new QRenderPass())
    , m_phongES2RenderPass(new QRenderPass())
    , m_phongRHIRenderPass(new QRenderPass())
    , m_phongGL3Shader(new QShaderProgram())
    , m_phongGL2ES2Shader(new QShaderProgram())
    , m_phongRHIShader(new QShaderProgram())
    , m_phongGL3ShaderBuilder(new QShaderProgramBuilder())
    , m_phongGL2ES2ShaderBuilder(new QShaderProgramBuilder())
    , m_phongRHIShaderBuilder(new QShaderProgramBuilder())
    , m_filterKey(new QFilterKey)
{
}
}  // namespace Qt3DExtras

//  from ../qt3d/src/extras/defaults/qmorphphongmaterial.cpp, line 51, as _ZN10Qt3DExtras26QMorphPhongMaterialPrivate4initEv
namespace Qt3DExtras {
using namespace Qt3DRender;
inline void QMorphPhongMaterialPrivate::init()
{
    Q_Q(QMorphPhongMaterial);

    connect(m_ambientParameter, &Qt3DRender::QParameter::valueChanged,
            this, &QMorphPhongMaterialPrivate::handleAmbientChanged);
    connect(m_diffuseParameter, &Qt3DRender::QParameter::valueChanged,
            this, &QMorphPhongMaterialPrivate::handleDiffuseChanged);
    connect(m_specularParameter, &Qt3DRender::QParameter::valueChanged,
            this, &QMorphPhongMaterialPrivate::handleSpecularChanged);
    connect(m_shininessParameter, &Qt3DRender::QParameter::valueChanged,
            this, &QMorphPhongMaterialPrivate::handleShininessChanged);
    connect(m_interpolatorParameter, &Qt3DRender::QParameter::valueChanged,
            this, &QMorphPhongMaterialPrivate::handleInterpolatorChanged);

    m_phongGL3Shader->setVertexShaderCode(QShaderProgram::loadSource(QUrl(QStringLiteral("qrc:/shaders/gl3/morphphong.vert"))));
    m_phongGL3ShaderBuilder->setParent(q);
    m_phongGL3ShaderBuilder->setShaderProgram(m_phongGL3Shader);
    m_phongGL3ShaderBuilder->setFragmentShaderGraph(QUrl(QStringLiteral("qrc:/shaders/graphs/phong.frag.json")));
    m_phongGL3ShaderBuilder->setEnabledLayers({QStringLiteral("diffuse"),
                                               QStringLiteral("specular"),
                                               QStringLiteral("normal")});

    m_phongGL2ES2Shader->setVertexShaderCode(QShaderProgram::loadSource(QUrl(QStringLiteral("qrc:/shaders/es2/morphphong.vert"))));
    m_phongGL2ES2ShaderBuilder->setParent(q);
    m_phongGL2ES2ShaderBuilder->setShaderProgram(m_phongGL2ES2Shader);
    m_phongGL2ES2ShaderBuilder->setFragmentShaderGraph(QUrl(QStringLiteral("qrc:/shaders/graphs/phong.frag.json")));
    m_phongGL2ES2ShaderBuilder->setEnabledLayers({QStringLiteral("diffuse"),
                                                  QStringLiteral("specular"),
                                                  QStringLiteral("normal")});

    m_phongRHIShader->setVertexShaderCode(QShaderProgram::loadSource(QUrl(QStringLiteral("qrc:/shaders/rhi/morphphong.vert"))));
    m_phongRHIShaderBuilder->setParent(q);
    m_phongRHIShaderBuilder->setShaderProgram(m_phongRHIShader);
    m_phongRHIShaderBuilder->setFragmentShaderGraph(QUrl(QStringLiteral("qrc:/shaders/graphs/phong.frag.json")));
    m_phongRHIShaderBuilder->setEnabledLayers({QStringLiteral("diffuse"),
                                               QStringLiteral("specular"),
                                               QStringLiteral("normal")});

    m_phongGL3Technique->graphicsApiFilter()->setApi(QGraphicsApiFilter::OpenGL);
    m_phongGL3Technique->graphicsApiFilter()->setMajorVersion(3);
    m_phongGL3Technique->graphicsApiFilter()->setMinorVersion(1);
    m_phongGL3Technique->graphicsApiFilter()->setProfile(QGraphicsApiFilter::CoreProfile);

    m_phongGL2Technique->graphicsApiFilter()->setApi(QGraphicsApiFilter::OpenGL);
    m_phongGL2Technique->graphicsApiFilter()->setMajorVersion(2);
    m_phongGL2Technique->graphicsApiFilter()->setMinorVersion(0);
    m_phongGL2Technique->graphicsApiFilter()->setProfile(QGraphicsApiFilter::NoProfile);

    m_phongES2Technique->graphicsApiFilter()->setApi(QGraphicsApiFilter::OpenGLES);
    m_phongES2Technique->graphicsApiFilter()->setMajorVersion(2);
    m_phongES2Technique->graphicsApiFilter()->setMinorVersion(0);
    m_phongES2Technique->graphicsApiFilter()->setProfile(QGraphicsApiFilter::NoProfile);

    m_phongRHITechnique->graphicsApiFilter()->setApi(QGraphicsApiFilter::RHI);
    m_phongRHITechnique->graphicsApiFilter()->setMajorVersion(1);
    m_phongRHITechnique->graphicsApiFilter()->setMinorVersion(0);

    m_phongGL3RenderPass->setShaderProgram(m_phongGL3Shader);
    m_phongGL2RenderPass->setShaderProgram(m_phongGL2ES2Shader);
    m_phongES2RenderPass->setShaderProgram(m_phongGL2ES2Shader);
    m_phongRHIRenderPass->setShaderProgram(m_phongRHIShader);

    m_phongGL3Technique->addRenderPass(m_phongGL3RenderPass);
    m_phongGL2Technique->addRenderPass(m_phongGL2RenderPass);
    m_phongES2Technique->addRenderPass(m_phongES2RenderPass);
    m_phongRHITechnique->addRenderPass(m_phongRHIRenderPass);

    m_filterKey->setParent(q);
    m_filterKey->setName(QStringLiteral("renderingStyle"));
    m_filterKey->setValue(QStringLiteral("forward"));

    m_phongGL3Technique->addFilterKey(m_filterKey);
    m_phongGL2Technique->addFilterKey(m_filterKey);
    m_phongES2Technique->addFilterKey(m_filterKey);
    m_phongRHITechnique->addFilterKey(m_filterKey);

    m_phongEffect->addTechnique(m_phongGL3Technique);
    m_phongEffect->addTechnique(m_phongGL2Technique);
    m_phongEffect->addTechnique(m_phongES2Technique);
    m_phongEffect->addTechnique(m_phongRHITechnique);

    m_phongEffect->addParameter(m_ambientParameter);
    m_phongEffect->addParameter(m_diffuseParameter);
    m_phongEffect->addParameter(m_specularParameter);
    m_phongEffect->addParameter(m_shininessParameter);
    m_phongEffect->addParameter(m_interpolatorParameter);

    q->setEffect(m_phongEffect);
}
}  // namespace Qt3DExtras

//  from ../qt3d/src/extras/defaults/qmorphphongmaterial.cpp, line 142, as _ZN10Qt3DExtras26QMorphPhongMaterialPrivate20handleAmbientChangedERK8QVariant
namespace Qt3DExtras {
using namespace Qt3DRender;
inline void QMorphPhongMaterialPrivate::handleAmbientChanged(const QVariant &var)
{
    Q_Q(QMorphPhongMaterial);
    emit q->ambientChanged(var.value<QColor>());
}
}  // namespace Qt3DExtras

//  from ../qt3d/src/extras/defaults/qmorphphongmaterial.cpp, line 148, as _ZN10Qt3DExtras26QMorphPhongMaterialPrivate20handleDiffuseChangedERK8QVariant
namespace Qt3DExtras {
using namespace Qt3DRender;
inline void QMorphPhongMaterialPrivate::handleDiffuseChanged(const QVariant &var)
{
    Q_Q(QMorphPhongMaterial);
    emit q->diffuseChanged(var.value<QColor>());
}
}  // namespace Qt3DExtras

//  from ../qt3d/src/extras/defaults/qmorphphongmaterial.cpp, line 154, as _ZN10Qt3DExtras26QMorphPhongMaterialPrivate21handleSpecularChangedERK8QVariant
namespace Qt3DExtras {
using namespace Qt3DRender;
inline void QMorphPhongMaterialPrivate::handleSpecularChanged(const QVariant &var)
{
    Q_Q(QMorphPhongMaterial);
    emit q->specularChanged(var.value<QColor>());
}
}  // namespace Qt3DExtras

//  from ../qt3d/src/extras/defaults/qmorphphongmaterial.cpp, line 160, as _ZN10Qt3DExtras26QMorphPhongMaterialPrivate22handleShininessChangedERK8QVariant
namespace Qt3DExtras {
using namespace Qt3DRender;
inline void QMorphPhongMaterialPrivate::handleShininessChanged(const QVariant &var)
{
    Q_Q(QMorphPhongMaterial);
    emit q->shininessChanged(var.toFloat());
}
}  // namespace Qt3DExtras

//  from ../qt3d/src/extras/defaults/qmorphphongmaterial.cpp, line 166, as _ZN10Qt3DExtras26QMorphPhongMaterialPrivate25handleInterpolatorChangedERK8QVariant
namespace Qt3DExtras {
using namespace Qt3DRender;
inline void QMorphPhongMaterialPrivate::handleInterpolatorChanged(const QVariant &var)
{
    Q_Q(QMorphPhongMaterial);
    emit q->interpolatorChanged(var.toFloat());
}
}  // namespace Qt3DExtras
//  -----------------------------------------------------------------------

//  A Qt3DExtras::QMorphPhongMaterialPrivate that Python can take functions over in. Every Qt3DExtras::QMorphPhongMaterialPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQt3DExtras_QMorphPhongMaterialPrivateCall0)(const void *, Qt3DCore::QScene *, int *);
typedef void (*CuteQt3DExtras_QMorphPhongMaterialPrivateCall1)(const void *, int *);
class CuteQt3DExtras_QMorphPhongMaterialPrivate : public Qt3DExtras::QMorphPhongMaterialPrivate {
public:
  using Qt3DExtras::QMorphPhongMaterialPrivate::QMorphPhongMaterialPrivate;
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
      CuteQt3DExtras_QMorphPhongMaterialPrivateCall0 call = reinterpret_cast<CuteQt3DExtras_QMorphPhongMaterialPrivateCall0>(taken[0]);
      call(this, scene, &handled);
      if (handled) return;
    }
    Qt3DCore::QNodePrivate::setScene(scene);
  }

  //  void Qt3DCore::QNodePrivate::update()
  void update() override {
    if (taken[1]) {
      int handled = 0;
      CuteQt3DExtras_QMorphPhongMaterialPrivateCall1 call = reinterpret_cast<CuteQt3DExtras_QMorphPhongMaterialPrivateCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    Qt3DCore::QNodePrivate::update();
  }
};

//  Qt3DExtras::QMorphPhongMaterialPrivate::QMorphPhongMaterialPrivate()
extern "C" Q_DECL_EXPORT
Qt3DExtras::QMorphPhongMaterialPrivate *ritual_ZN10Qt3DExtras26QMorphPhongMaterialPrivateC1Ev() {
  return new CuteQt3DExtras_QMorphPhongMaterialPrivate();
}

//  void Qt3DExtras::QMorphPhongMaterialPrivate::init()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras26QMorphPhongMaterialPrivate4initEv(
    Qt3DExtras::QMorphPhongMaterialPrivate *self) {
  self->init();
}

//  void Qt3DExtras::QMorphPhongMaterialPrivate::handleAmbientChanged(const
//      QVariant &var)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras26QMorphPhongMaterialPrivate20handleAmbientChangedERK8QVariant(
    Qt3DExtras::QMorphPhongMaterialPrivate *self,
    const QVariant *var) {
  self->handleAmbientChanged(*var);
}

//  void Qt3DExtras::QMorphPhongMaterialPrivate::handleDiffuseChanged(const
//      QVariant &var)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras26QMorphPhongMaterialPrivate20handleDiffuseChangedERK8QVariant(
    Qt3DExtras::QMorphPhongMaterialPrivate *self,
    const QVariant *var) {
  self->handleDiffuseChanged(*var);
}

//  void Qt3DExtras::QMorphPhongMaterialPrivate::handleSpecularChanged(const
//      QVariant &var)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras26QMorphPhongMaterialPrivate21handleSpecularChangedERK8QVariant(
    Qt3DExtras::QMorphPhongMaterialPrivate *self,
    const QVariant *var) {
  self->handleSpecularChanged(*var);
}

//  void Qt3DExtras::QMorphPhongMaterialPrivate::handleShininessChanged(const
//      QVariant &var)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras26QMorphPhongMaterialPrivate22handleShininessChangedERK8QVariant(
    Qt3DExtras::QMorphPhongMaterialPrivate *self,
    const QVariant *var) {
  self->handleShininessChanged(*var);
}

//  void
//      Qt3DExtras::QMorphPhongMaterialPrivate::handleInterpolatorChanged(con
//      st QVariant &var)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras26QMorphPhongMaterialPrivate25handleInterpolatorChangedERK8QVariant(
    Qt3DExtras::QMorphPhongMaterialPrivate *self,
    const QVariant *var) {
  self->handleInterpolatorChanged(*var);
}

//  QMorphPhongMaterial *Qt3DExtras::QMorphPhongMaterialPrivate::q_func()
extern "C" Q_DECL_EXPORT
Qt3DExtras::QMorphPhongMaterial *ritual_ZN10Qt3DExtras26QMorphPhongMaterialPrivate6q_funcEv(
    Qt3DExtras::QMorphPhongMaterialPrivate *self) {
  return self->q_func();
}

//  const QMorphPhongMaterial
//      *Qt3DExtras::QMorphPhongMaterialPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const Qt3DExtras::QMorphPhongMaterial *ritual_ZNK10Qt3DExtras26QMorphPhongMaterialPrivate6q_funcEv(
    const Qt3DExtras::QMorphPhongMaterialPrivate *self) {
  return self->q_func();
}

//  a Python function taken by a CuteQt3DExtras_QMorphPhongMaterialPrivate,
//      for the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DExtras_QMorphPhongMaterialPrivate(
    Qt3DExtras::QMorphPhongMaterialPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DExtras_QMorphPhongMaterialPrivate *>(self)->take(key, call);
}
