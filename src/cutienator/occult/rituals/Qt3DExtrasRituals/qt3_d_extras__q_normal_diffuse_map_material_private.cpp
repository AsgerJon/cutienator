//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DExtras/6.12.0/Qt3DExtras/private/qnormaldiffusemapmaterial_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <Qt3DExtras/Qt3DExtras>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DExtras/6.12.0/Qt3DExtras/private/qnormaldiffusemapmaterial_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qvariant.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DExtras/qnormaldiffusemapmaterial.h>
#include <Qt3DExtras/private/qnormaldiffusemapmaterial_p.h>
#include <Qt3DRender/qfilterkey.h>
#include <Qt3DRender/qeffect.h>
#include <Qt3DRender/qtexture.h>
#include <Qt3DRender/qtechnique.h>
#include <Qt3DRender/qparameter.h>
#include <Qt3DRender/qshaderprogram.h>
#include <Qt3DRender/qshaderprogrambuilder.h>
#include <Qt3DRender/qrenderpass.h>
#include <Qt3DRender/qgraphicsapifilter.h>
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

//  from ../qt3d/src/extras/defaults/qnormaldiffusemapmaterial.cpp, line 66, as _ZN10Qt3DExtras32QNormalDiffuseMapMaterialPrivate4initEv
namespace Qt3DExtras {
using namespace Qt3DRender;
inline void QNormalDiffuseMapMaterialPrivate::init()
{
    Q_Q(QNormalDiffuseMapMaterial);

    connect(m_ambientParameter, &Qt3DRender::QParameter::valueChanged,
            this, &QNormalDiffuseMapMaterialPrivate::handleAmbientChanged);
    connect(m_diffuseParameter, &Qt3DRender::QParameter::valueChanged,
            this, &QNormalDiffuseMapMaterialPrivate::handleDiffuseChanged);
    connect(m_normalParameter, &Qt3DRender::QParameter::valueChanged,
            this, &QNormalDiffuseMapMaterialPrivate::handleNormalChanged);
    connect(m_specularParameter, &Qt3DRender::QParameter::valueChanged,
            this, &QNormalDiffuseMapMaterialPrivate::handleSpecularChanged);
    connect(m_shininessParameter, &Qt3DRender::QParameter::valueChanged,
            this, &QNormalDiffuseMapMaterialPrivate::handleShininessChanged);
    connect(m_textureScaleParameter, &Qt3DRender::QParameter::valueChanged,
            this, &QNormalDiffuseMapMaterialPrivate::handleTextureScaleChanged);

    m_normalDiffuseGL3Shader->setVertexShaderCode(QShaderProgram::loadSource(QUrl(QStringLiteral("qrc:/shaders/gl3/default.vert"))));
    m_normalDiffuseGL3ShaderBuilder->setParent(q);
    m_normalDiffuseGL3ShaderBuilder->setShaderProgram(m_normalDiffuseGL3Shader);
    m_normalDiffuseGL3ShaderBuilder->setFragmentShaderGraph(QUrl(QStringLiteral("qrc:/shaders/graphs/phong.frag.json")));
    m_normalDiffuseGL3ShaderBuilder->setEnabledLayers({QStringLiteral("diffuseTexture"),
                                                       QStringLiteral("specular"),
                                                       QStringLiteral("normalTexture")});

    m_normalDiffuseGL2ES2Shader->setVertexShaderCode(QShaderProgram::loadSource(QUrl(QStringLiteral("qrc:/shaders/es2/default.vert"))));
    m_normalDiffuseGL2ES2ShaderBuilder->setParent(q);
    m_normalDiffuseGL2ES2ShaderBuilder->setShaderProgram(m_normalDiffuseGL2ES2Shader);
    m_normalDiffuseGL2ES2ShaderBuilder->setFragmentShaderGraph(QUrl(QStringLiteral("qrc:/shaders/graphs/phong.frag.json")));
    m_normalDiffuseGL2ES2ShaderBuilder->setEnabledLayers({QStringLiteral("diffuseTexture"),
                                                          QStringLiteral("specular"),
                                                          QStringLiteral("normalTexture")});

    m_normalDiffuseRHIShader->setVertexShaderCode(QShaderProgram::loadSource(QUrl(QStringLiteral("qrc:/shaders/rhi/default_pos_norm_tex_tan.vert"))));
    m_normalDiffuseRHIShaderBuilder->setParent(q);
    m_normalDiffuseRHIShaderBuilder->setShaderProgram(m_normalDiffuseRHIShader);
    m_normalDiffuseRHIShaderBuilder->setFragmentShaderGraph(QUrl(QStringLiteral("qrc:/shaders/graphs/phong.frag.json")));
    m_normalDiffuseRHIShaderBuilder->setEnabledLayers({QStringLiteral("diffuseTexture"),
                                                       QStringLiteral("specular"),
                                                       QStringLiteral("normalTexture")});

    m_normalDiffuseGL3Technique->graphicsApiFilter()->setApi(QGraphicsApiFilter::OpenGL);
    m_normalDiffuseGL3Technique->graphicsApiFilter()->setMajorVersion(3);
    m_normalDiffuseGL3Technique->graphicsApiFilter()->setMinorVersion(1);
    m_normalDiffuseGL3Technique->graphicsApiFilter()->setProfile(QGraphicsApiFilter::CoreProfile);

    m_normalDiffuseGL2Technique->graphicsApiFilter()->setApi(QGraphicsApiFilter::OpenGL);
    m_normalDiffuseGL2Technique->graphicsApiFilter()->setMajorVersion(2);
    m_normalDiffuseGL2Technique->graphicsApiFilter()->setMinorVersion(0);
    m_normalDiffuseGL2Technique->graphicsApiFilter()->setProfile(QGraphicsApiFilter::NoProfile);

    m_normalDiffuseES2Technique->graphicsApiFilter()->setApi(QGraphicsApiFilter::OpenGLES);
    m_normalDiffuseES2Technique->graphicsApiFilter()->setMajorVersion(2);
    m_normalDiffuseES2Technique->graphicsApiFilter()->setMinorVersion(0);
    m_normalDiffuseES2Technique->graphicsApiFilter()->setProfile(QGraphicsApiFilter::NoProfile);

    m_normalDiffuseRHITechnique->graphicsApiFilter()->setApi(QGraphicsApiFilter::RHI);
    m_normalDiffuseRHITechnique->graphicsApiFilter()->setMajorVersion(1);
    m_normalDiffuseRHITechnique->graphicsApiFilter()->setMinorVersion(0);

    m_filterKey->setParent(q);
    m_filterKey->setName(QStringLiteral("renderingStyle"));
    m_filterKey->setValue(QStringLiteral("forward"));

    m_normalDiffuseGL3Technique->addFilterKey(m_filterKey);
    m_normalDiffuseGL2Technique->addFilterKey(m_filterKey);
    m_normalDiffuseES2Technique->addFilterKey(m_filterKey);
    m_normalDiffuseRHITechnique->addFilterKey(m_filterKey);

    m_normalDiffuseGL3RenderPass->setShaderProgram(m_normalDiffuseGL3Shader);
    m_normalDiffuseGL2RenderPass->setShaderProgram(m_normalDiffuseGL2ES2Shader);
    m_normalDiffuseES2RenderPass->setShaderProgram(m_normalDiffuseGL2ES2Shader);
    m_normalDiffuseRHIRenderPass->setShaderProgram(m_normalDiffuseRHIShader);

    m_normalDiffuseGL3Technique->addRenderPass(m_normalDiffuseGL3RenderPass);
    m_normalDiffuseGL2Technique->addRenderPass(m_normalDiffuseGL2RenderPass);
    m_normalDiffuseES2Technique->addRenderPass(m_normalDiffuseES2RenderPass);
    m_normalDiffuseRHITechnique->addRenderPass(m_normalDiffuseRHIRenderPass);

    m_normalDiffuseEffect->addTechnique(m_normalDiffuseGL3Technique);
    m_normalDiffuseEffect->addTechnique(m_normalDiffuseGL2Technique);
    m_normalDiffuseEffect->addTechnique(m_normalDiffuseES2Technique);
    m_normalDiffuseEffect->addTechnique(m_normalDiffuseRHITechnique);

    m_normalDiffuseEffect->addParameter(m_ambientParameter);
    m_normalDiffuseEffect->addParameter(m_diffuseParameter);
    m_normalDiffuseEffect->addParameter(m_normalParameter);
    m_normalDiffuseEffect->addParameter(m_specularParameter);
    m_normalDiffuseEffect->addParameter(m_shininessParameter);
    m_normalDiffuseEffect->addParameter(m_textureScaleParameter);

    q->setEffect(m_normalDiffuseEffect);
}
}  // namespace Qt3DExtras

//  from ../qt3d/src/extras/defaults/qnormaldiffusemapmaterial.cpp, line 160, as _ZN10Qt3DExtras32QNormalDiffuseMapMaterialPrivate20handleAmbientChangedERK8QVariant
namespace Qt3DExtras {
using namespace Qt3DRender;
inline void QNormalDiffuseMapMaterialPrivate::handleAmbientChanged(const QVariant &var)
{
    Q_Q(QNormalDiffuseMapMaterial);
    emit q->ambientChanged(var.value<QColor>());
}
}  // namespace Qt3DExtras

//  from ../qt3d/src/extras/defaults/qnormaldiffusemapmaterial.cpp, line 166, as _ZN10Qt3DExtras32QNormalDiffuseMapMaterialPrivate20handleDiffuseChangedERK8QVariant
namespace Qt3DExtras {
using namespace Qt3DRender;
inline void QNormalDiffuseMapMaterialPrivate::handleDiffuseChanged(const QVariant &var)
{
    Q_Q(QNormalDiffuseMapMaterial);
    emit q->diffuseChanged(var.value<QAbstractTexture *>());
}
}  // namespace Qt3DExtras

//  from ../qt3d/src/extras/defaults/qnormaldiffusemapmaterial.cpp, line 172, as _ZN10Qt3DExtras32QNormalDiffuseMapMaterialPrivate19handleNormalChangedERK8QVariant
namespace Qt3DExtras {
using namespace Qt3DRender;
inline void QNormalDiffuseMapMaterialPrivate::handleNormalChanged(const QVariant &var)
{
    Q_Q(QNormalDiffuseMapMaterial);
    emit q->normalChanged(var.value<QAbstractTexture *>());
}
}  // namespace Qt3DExtras

//  from ../qt3d/src/extras/defaults/qnormaldiffusemapmaterial.cpp, line 178, as _ZN10Qt3DExtras32QNormalDiffuseMapMaterialPrivate21handleSpecularChangedERK8QVariant
namespace Qt3DExtras {
using namespace Qt3DRender;
inline void QNormalDiffuseMapMaterialPrivate::handleSpecularChanged(const QVariant &var)
{
    Q_Q(QNormalDiffuseMapMaterial);
    emit q->specularChanged(var.value<QColor>());
}
}  // namespace Qt3DExtras

//  from ../qt3d/src/extras/defaults/qnormaldiffusemapmaterial.cpp, line 184, as _ZN10Qt3DExtras32QNormalDiffuseMapMaterialPrivate22handleShininessChangedERK8QVariant
namespace Qt3DExtras {
using namespace Qt3DRender;
inline void QNormalDiffuseMapMaterialPrivate::handleShininessChanged(const QVariant &var)
{
    Q_Q(QNormalDiffuseMapMaterial);
    emit q->shininessChanged(var.toFloat());
}
}  // namespace Qt3DExtras

//  from ../qt3d/src/extras/defaults/qnormaldiffusemapmaterial.cpp, line 190, as _ZN10Qt3DExtras32QNormalDiffuseMapMaterialPrivate25handleTextureScaleChangedERK8QVariant
namespace Qt3DExtras {
using namespace Qt3DRender;
inline void QNormalDiffuseMapMaterialPrivate::handleTextureScaleChanged(const QVariant &var)
{
    Q_Q(QNormalDiffuseMapMaterial);
    emit q->textureScaleChanged(var.toFloat());
}
}  // namespace Qt3DExtras
//  -----------------------------------------------------------------------

//  A Qt3DExtras::QNormalDiffuseMapMaterialPrivate that Python can take functions over in. Every Qt3DExtras::QNormalDiffuseMapMaterialPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQt3DExtras_QNormalDiffuseMapMaterialPrivateCall0)(const void *, int *);
typedef void (*CuteQt3DExtras_QNormalDiffuseMapMaterialPrivateCall1)(const void *, Qt3DCore::QScene *, int *);
typedef void (*CuteQt3DExtras_QNormalDiffuseMapMaterialPrivateCall2)(const void *, int *);
class CuteQt3DExtras_QNormalDiffuseMapMaterialPrivate : public Qt3DExtras::QNormalDiffuseMapMaterialPrivate {
public:
  using Qt3DExtras::QNormalDiffuseMapMaterialPrivate::QNormalDiffuseMapMaterialPrivate;
  void *taken[3] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN10Qt3DExtras32QNormalDiffuseMapMaterialPrivate4initEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN8Qt3DCore12QNodePrivate8setSceneEPNS_6QSceneE")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN8Qt3DCore12QNodePrivate6updateEv")) {
      taken[2] = call;
      return true;
    }
    return false;
  }

  //  void Qt3DExtras::QNormalDiffuseMapMaterialPrivate::init()
  void init() override {
    if (taken[0]) {
      int handled = 0;
      CuteQt3DExtras_QNormalDiffuseMapMaterialPrivateCall0 call = reinterpret_cast<CuteQt3DExtras_QNormalDiffuseMapMaterialPrivateCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    Qt3DExtras::QNormalDiffuseMapMaterialPrivate::init();
  }

  //  void Qt3DCore::QNodePrivate::setScene(QScene *scene)
  void setScene(Qt3DCore::QScene *scene) override {
    if (taken[1]) {
      int handled = 0;
      CuteQt3DExtras_QNormalDiffuseMapMaterialPrivateCall1 call = reinterpret_cast<CuteQt3DExtras_QNormalDiffuseMapMaterialPrivateCall1>(taken[1]);
      call(this, scene, &handled);
      if (handled) return;
    }
    Qt3DCore::QNodePrivate::setScene(scene);
  }

  //  void Qt3DCore::QNodePrivate::update()
  void update() override {
    if (taken[2]) {
      int handled = 0;
      CuteQt3DExtras_QNormalDiffuseMapMaterialPrivateCall2 call = reinterpret_cast<CuteQt3DExtras_QNormalDiffuseMapMaterialPrivateCall2>(taken[2]);
      call(this, &handled);
      if (handled) return;
    }
    Qt3DCore::QNodePrivate::update();
  }
};

//  void Qt3DExtras::QNormalDiffuseMapMaterialPrivate::init()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras32QNormalDiffuseMapMaterialPrivate4initEv(
    Qt3DExtras::QNormalDiffuseMapMaterialPrivate *self) {
  self->init();
}

//  void
//      Qt3DExtras::QNormalDiffuseMapMaterialPrivate::handleAmbientChanged(co
//      nst QVariant &var)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras32QNormalDiffuseMapMaterialPrivate20handleAmbientChangedERK8QVariant(
    Qt3DExtras::QNormalDiffuseMapMaterialPrivate *self,
    const QVariant *var) {
  self->handleAmbientChanged(*var);
}

//  void
//      Qt3DExtras::QNormalDiffuseMapMaterialPrivate::handleDiffuseChanged(co
//      nst QVariant &var)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras32QNormalDiffuseMapMaterialPrivate20handleDiffuseChangedERK8QVariant(
    Qt3DExtras::QNormalDiffuseMapMaterialPrivate *self,
    const QVariant *var) {
  self->handleDiffuseChanged(*var);
}

//  void
//      Qt3DExtras::QNormalDiffuseMapMaterialPrivate::handleNormalChanged(con
//      st QVariant &var)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras32QNormalDiffuseMapMaterialPrivate19handleNormalChangedERK8QVariant(
    Qt3DExtras::QNormalDiffuseMapMaterialPrivate *self,
    const QVariant *var) {
  self->handleNormalChanged(*var);
}

//  void
//      Qt3DExtras::QNormalDiffuseMapMaterialPrivate::handleSpecularChanged(c
//      onst QVariant &var)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras32QNormalDiffuseMapMaterialPrivate21handleSpecularChangedERK8QVariant(
    Qt3DExtras::QNormalDiffuseMapMaterialPrivate *self,
    const QVariant *var) {
  self->handleSpecularChanged(*var);
}

//  void Qt3DExtras::QNormalDiffuseMapMaterialPrivate::handleShininessChanged
//      (const QVariant &var)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras32QNormalDiffuseMapMaterialPrivate22handleShininessChangedERK8QVariant(
    Qt3DExtras::QNormalDiffuseMapMaterialPrivate *self,
    const QVariant *var) {
  self->handleShininessChanged(*var);
}

//  void Qt3DExtras::QNormalDiffuseMapMaterialPrivate::handleTextureScaleChan
//      ged(const QVariant &var)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras32QNormalDiffuseMapMaterialPrivate25handleTextureScaleChangedERK8QVariant(
    Qt3DExtras::QNormalDiffuseMapMaterialPrivate *self,
    const QVariant *var) {
  self->handleTextureScaleChanged(*var);
}

//  QNormalDiffuseMapMaterial
//      *Qt3DExtras::QNormalDiffuseMapMaterialPrivate::q_func()
extern "C" Q_DECL_EXPORT
Qt3DExtras::QNormalDiffuseMapMaterial *ritual_ZN10Qt3DExtras32QNormalDiffuseMapMaterialPrivate6q_funcEv(
    Qt3DExtras::QNormalDiffuseMapMaterialPrivate *self) {
  return self->q_func();
}

//  const QNormalDiffuseMapMaterial
//      *Qt3DExtras::QNormalDiffuseMapMaterialPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const Qt3DExtras::QNormalDiffuseMapMaterial *ritual_ZNK10Qt3DExtras32QNormalDiffuseMapMaterialPrivate6q_funcEv(
    const Qt3DExtras::QNormalDiffuseMapMaterialPrivate *self) {
  return self->q_func();
}

//  a Python function taken by a
//      CuteQt3DExtras_QNormalDiffuseMapMaterialPrivate, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DExtras_QNormalDiffuseMapMaterialPrivate(
    Qt3DExtras::QNormalDiffuseMapMaterialPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DExtras_QNormalDiffuseMapMaterialPrivate *>(self)->take(key, call);
}

//  void Qt3DExtras::QNormalDiffuseMapMaterialPrivate::init()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10Qt3DExtras32QNormalDiffuseMapMaterialPrivate4initEv(
    Qt3DExtras::QNormalDiffuseMapMaterialPrivate *self) {
  self->Qt3DExtras::QNormalDiffuseMapMaterialPrivate::init();
}
