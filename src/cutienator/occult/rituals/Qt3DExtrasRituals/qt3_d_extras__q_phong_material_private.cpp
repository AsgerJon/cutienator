//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DExtras/6.12.0/Qt3DExtras/private/qphongmaterial_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <Qt3DExtras/Qt3DExtras>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DExtras/6.12.0/Qt3DExtras/private/qphongmaterial_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qvariant.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DExtras/qphongmaterial.h>
#include <Qt3DExtras/private/qphongmaterial_p.h>
#include <Qt3DRender/qfilterkey.h>
#include <Qt3DRender/qmaterial.h>
#include <Qt3DRender/qeffect.h>
#include <Qt3DRender/qtechnique.h>
#include <Qt3DRender/qshaderprogram.h>
#include <Qt3DRender/qshaderprogrambuilder.h>
#include <Qt3DRender/qparameter.h>
#include <Qt3DRender/qrenderpass.h>
#include <Qt3DRender/qgraphicsapifilter.h>
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

//  from ../qt3d/src/extras/defaults/qphongmaterial.cpp, line 27, as _ZN10Qt3DExtras21QPhongMaterialPrivateC1Ev
namespace Qt3DExtras {
using namespace Qt3DRender;
inline QPhongMaterialPrivate::QPhongMaterialPrivate()
    : QMaterialPrivate()
    , m_phongEffect(new QEffect())
    , m_ambientParameter(new QParameter(QStringLiteral("ka"), QColor::fromRgbF(0.05f, 0.05f, 0.05f, 1.0f)))
    , m_diffuseParameter(new QParameter(QStringLiteral("kd"), QColor::fromRgbF(0.7f, 0.7f, 0.7f, 1.0f)))
    , m_specularParameter(new QParameter(QStringLiteral("ks"), QColor::fromRgbF(0.01f, 0.01f, 0.01f, 1.0f)))
    , m_shininessParameter(new QParameter(QStringLiteral("shininess"), 150.0f))
    , m_phongGL3Technique(new QTechnique())
    , m_phongGL2Technique(new QTechnique())
    , m_phongES2Technique(new QTechnique())
    , m_phongRHITechnique(new QTechnique())
    , m_phongGL3RenderPass(new QRenderPass())
    , m_phongGL2RenderPass(new QRenderPass())
    , m_phongES2RenderPass(new QRenderPass())
    , m_phongRHIRenderPass(new QRenderPass())
    , m_phongGL3Shader(new QShaderProgram())
    , m_phongGL3ShaderBuilder(new QShaderProgramBuilder())
    , m_phongGL2ES2Shader(new QShaderProgram())
    , m_phongGL2ES2ShaderBuilder(new QShaderProgramBuilder())
    , m_phongRHIShader(new QShaderProgram())
    , m_phongRHIShaderBuilder(new QShaderProgramBuilder())
    , m_filterKey(new QFilterKey)
{
}
}  // namespace Qt3DExtras

//  from ../qt3d/src/extras/defaults/qphongmaterial.cpp, line 52, as _ZN10Qt3DExtras21QPhongMaterialPrivate4initEv
namespace Qt3DExtras {
using namespace Qt3DRender;
inline void QPhongMaterialPrivate::init()
{
    Q_Q(QPhongMaterial);

    connect(m_ambientParameter, &Qt3DRender::QParameter::valueChanged,
            this, &QPhongMaterialPrivate::handleAmbientChanged);
    connect(m_diffuseParameter, &Qt3DRender::QParameter::valueChanged,
            this, &QPhongMaterialPrivate::handleDiffuseChanged);
    connect(m_specularParameter, &Qt3DRender::QParameter::valueChanged,
            this, &QPhongMaterialPrivate::handleSpecularChanged);
    connect(m_shininessParameter, &Qt3DRender::QParameter::valueChanged,
            this, &QPhongMaterialPrivate::handleShininessChanged);

    m_phongGL3Shader->setVertexShaderCode(QShaderProgram::loadSource(QUrl(QStringLiteral("qrc:/shaders/gl3/default.vert"))));
    m_phongGL3ShaderBuilder->setParent(q);
    m_phongGL3ShaderBuilder->setShaderProgram(m_phongGL3Shader);
    m_phongGL3ShaderBuilder->setFragmentShaderGraph(QUrl(QStringLiteral("qrc:/shaders/graphs/phong.frag.json")));
    m_phongGL3ShaderBuilder->setEnabledLayers({QStringLiteral("diffuse"),
                                               QStringLiteral("specular"),
                                               QStringLiteral("normal")});

    m_phongGL2ES2Shader->setVertexShaderCode(QShaderProgram::loadSource(QUrl(QStringLiteral("qrc:/shaders/es2/default.vert"))));
    m_phongGL2ES2ShaderBuilder->setParent(q);
    m_phongGL2ES2ShaderBuilder->setShaderProgram(m_phongGL2ES2Shader);
    m_phongGL2ES2ShaderBuilder->setFragmentShaderGraph(QUrl(QStringLiteral("qrc:/shaders/graphs/phong.frag.json")));
    m_phongGL2ES2ShaderBuilder->setEnabledLayers({QStringLiteral("diffuse"),
                                                  QStringLiteral("specular"),
                                                  QStringLiteral("normal")});

    m_phongRHIShader->setVertexShaderCode(QShaderProgram::loadSource(QUrl(QStringLiteral("qrc:/shaders/rhi/default_pos_norm.vert"))));
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

    q->setEffect(m_phongEffect);
}
}  // namespace Qt3DExtras

//  from ../qt3d/src/extras/defaults/qphongmaterial.cpp, line 140, as _ZN10Qt3DExtras21QPhongMaterialPrivate20handleAmbientChangedERK8QVariant
namespace Qt3DExtras {
using namespace Qt3DRender;
inline void QPhongMaterialPrivate::handleAmbientChanged(const QVariant &var)
{
    Q_Q(QPhongMaterial);
    emit q->ambientChanged(var.value<QColor>());
}
}  // namespace Qt3DExtras

//  from ../qt3d/src/extras/defaults/qphongmaterial.cpp, line 146, as _ZN10Qt3DExtras21QPhongMaterialPrivate20handleDiffuseChangedERK8QVariant
namespace Qt3DExtras {
using namespace Qt3DRender;
inline void QPhongMaterialPrivate::handleDiffuseChanged(const QVariant &var)
{
    Q_Q(QPhongMaterial);
    emit q->diffuseChanged(var.value<QColor>());
}
}  // namespace Qt3DExtras

//  from ../qt3d/src/extras/defaults/qphongmaterial.cpp, line 152, as _ZN10Qt3DExtras21QPhongMaterialPrivate21handleSpecularChangedERK8QVariant
namespace Qt3DExtras {
using namespace Qt3DRender;
inline void QPhongMaterialPrivate::handleSpecularChanged(const QVariant &var)
{
    Q_Q(QPhongMaterial);
    emit q->specularChanged(var.value<QColor>());
}
}  // namespace Qt3DExtras

//  from ../qt3d/src/extras/defaults/qphongmaterial.cpp, line 158, as _ZN10Qt3DExtras21QPhongMaterialPrivate22handleShininessChangedERK8QVariant
namespace Qt3DExtras {
using namespace Qt3DRender;
inline void QPhongMaterialPrivate::handleShininessChanged(const QVariant &var)
{
    Q_Q(QPhongMaterial);
    emit q->shininessChanged(var.toFloat());
}
}  // namespace Qt3DExtras
//  -----------------------------------------------------------------------

//  A Qt3DExtras::QPhongMaterialPrivate that Python can take functions over in. Every Qt3DExtras::QPhongMaterialPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQt3DExtras_QPhongMaterialPrivateCall0)(const void *, Qt3DCore::QScene *, int *);
typedef void (*CuteQt3DExtras_QPhongMaterialPrivateCall1)(const void *, int *);
class CuteQt3DExtras_QPhongMaterialPrivate : public Qt3DExtras::QPhongMaterialPrivate {
public:
  using Qt3DExtras::QPhongMaterialPrivate::QPhongMaterialPrivate;
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
      CuteQt3DExtras_QPhongMaterialPrivateCall0 call = reinterpret_cast<CuteQt3DExtras_QPhongMaterialPrivateCall0>(taken[0]);
      call(this, scene, &handled);
      if (handled) return;
    }
    Qt3DCore::QNodePrivate::setScene(scene);
  }

  //  void Qt3DCore::QNodePrivate::update()
  void update() override {
    if (taken[1]) {
      int handled = 0;
      CuteQt3DExtras_QPhongMaterialPrivateCall1 call = reinterpret_cast<CuteQt3DExtras_QPhongMaterialPrivateCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    Qt3DCore::QNodePrivate::update();
  }
};

//  Qt3DExtras::QPhongMaterialPrivate::QPhongMaterialPrivate()
extern "C" Q_DECL_EXPORT
Qt3DExtras::QPhongMaterialPrivate *ritual_ZN10Qt3DExtras21QPhongMaterialPrivateC1Ev() {
  return new CuteQt3DExtras_QPhongMaterialPrivate();
}

//  void Qt3DExtras::QPhongMaterialPrivate::init()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras21QPhongMaterialPrivate4initEv(
    Qt3DExtras::QPhongMaterialPrivate *self) {
  self->init();
}

//  void Qt3DExtras::QPhongMaterialPrivate::handleAmbientChanged(const
//      QVariant &var)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras21QPhongMaterialPrivate20handleAmbientChangedERK8QVariant(
    Qt3DExtras::QPhongMaterialPrivate *self,
    const QVariant *var) {
  self->handleAmbientChanged(*var);
}

//  void Qt3DExtras::QPhongMaterialPrivate::handleDiffuseChanged(const
//      QVariant &var)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras21QPhongMaterialPrivate20handleDiffuseChangedERK8QVariant(
    Qt3DExtras::QPhongMaterialPrivate *self,
    const QVariant *var) {
  self->handleDiffuseChanged(*var);
}

//  void Qt3DExtras::QPhongMaterialPrivate::handleSpecularChanged(const
//      QVariant &var)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras21QPhongMaterialPrivate21handleSpecularChangedERK8QVariant(
    Qt3DExtras::QPhongMaterialPrivate *self,
    const QVariant *var) {
  self->handleSpecularChanged(*var);
}

//  void Qt3DExtras::QPhongMaterialPrivate::handleShininessChanged(const
//      QVariant &var)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras21QPhongMaterialPrivate22handleShininessChangedERK8QVariant(
    Qt3DExtras::QPhongMaterialPrivate *self,
    const QVariant *var) {
  self->handleShininessChanged(*var);
}

//  QPhongMaterial *Qt3DExtras::QPhongMaterialPrivate::q_func()
extern "C" Q_DECL_EXPORT
Qt3DExtras::QPhongMaterial *ritual_ZN10Qt3DExtras21QPhongMaterialPrivate6q_funcEv(
    Qt3DExtras::QPhongMaterialPrivate *self) {
  return self->q_func();
}

//  const QPhongMaterial *Qt3DExtras::QPhongMaterialPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const Qt3DExtras::QPhongMaterial *ritual_ZNK10Qt3DExtras21QPhongMaterialPrivate6q_funcEv(
    const Qt3DExtras::QPhongMaterialPrivate *self) {
  return self->q_func();
}

//  a Python function taken by a CuteQt3DExtras_QPhongMaterialPrivate, for
//      the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DExtras_QPhongMaterialPrivate(
    Qt3DExtras::QPhongMaterialPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DExtras_QPhongMaterialPrivate *>(self)->take(key, call);
}
