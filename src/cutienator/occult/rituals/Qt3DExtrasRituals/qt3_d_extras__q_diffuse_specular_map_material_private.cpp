//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DExtras/6.12.0/Qt3DExtras/private/qdiffusespecularmapmaterial_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <Qt3DExtras/Qt3DExtras>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DExtras/6.12.0/Qt3DExtras/private/qdiffusespecularmapmaterial_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qvariant.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DExtras/qdiffusespecularmapmaterial.h>
#include <Qt3DExtras/private/qdiffusespecularmapmaterial_p.h>
#include <Qt3DRender/qfilterkey.h>
#include <Qt3DRender/qmaterial.h>
#include <Qt3DRender/qeffect.h>
#include <Qt3DRender/qtexture.h>
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
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qt3d/src/extras/defaults/qdiffusespecularmapmaterial.cpp, line 27, as _ZN10Qt3DExtras34QDiffuseSpecularMapMaterialPrivateC1Ev
namespace Qt3DExtras {
using namespace Qt3DRender;
inline QDiffuseSpecularMapMaterialPrivate::QDiffuseSpecularMapMaterialPrivate()
    : QMaterialPrivate()
    , m_diffuseSpecularMapEffect(new QEffect())
    , m_diffuseTexture(new QTexture2D())
    , m_specularTexture(new QTexture2D())
    , m_ambientParameter(new QParameter(QStringLiteral("ka"), QColor::fromRgbF(0.05f, 0.05f, 0.05f, 1.0f)))
    , m_diffuseParameter(new QParameter(QStringLiteral("diffuseTexture"), m_diffuseTexture))
    , m_specularParameter(new QParameter(QStringLiteral("specularTexture"), m_specularTexture))
    , m_shininessParameter(new QParameter(QStringLiteral("shininess"), 150.0f))
    , m_textureScaleParameter(new QParameter(QStringLiteral("texCoordScale"), 1.0f))
    , m_diffuseSpecularMapGL3Technique(new QTechnique())
    , m_diffuseSpecularMapGL2Technique(new QTechnique())
    , m_diffuseSpecularMapES2Technique(new QTechnique())
    , m_diffuseSpecularMapRHITechnique(new QTechnique())
    , m_diffuseSpecularMapGL3RenderPass(new QRenderPass())
    , m_diffuseSpecularMapGL2RenderPass(new QRenderPass())
    , m_diffuseSpecularMapES2RenderPass(new QRenderPass())
    , m_diffuseSpecularMapRHIRenderPass(new QRenderPass())
    , m_diffuseSpecularMapGL3Shader(new QShaderProgram())
    , m_diffuseSpecularMapGL3ShaderBuilder(new QShaderProgramBuilder())
    , m_diffuseSpecularMapGL2ES2Shader(new QShaderProgram())
    , m_diffuseSpecularMapGL2ES2ShaderBuilder(new QShaderProgramBuilder())
    , m_diffuseSpecularMapRHIShader(new QShaderProgram())
    , m_diffuseSpecularMapRHIShaderBuilder(new QShaderProgramBuilder())
    , m_filterKey(new QFilterKey)
{
    m_diffuseTexture->setMagnificationFilter(QAbstractTexture::Linear);
    m_diffuseTexture->setMinificationFilter(QAbstractTexture::LinearMipMapLinear);
    m_diffuseTexture->setWrapMode(QTextureWrapMode(QTextureWrapMode::Repeat));
    m_diffuseTexture->setGenerateMipMaps(true);
    m_diffuseTexture->setMaximumAnisotropy(16.0f);

    m_specularTexture->setMagnificationFilter(QAbstractTexture::Linear);
    m_specularTexture->setMinificationFilter(QAbstractTexture::LinearMipMapLinear);
    m_specularTexture->setWrapMode(QTextureWrapMode(QTextureWrapMode::Repeat));
    m_specularTexture->setGenerateMipMaps(true);
    m_specularTexture->setMaximumAnisotropy(16.0f);
}
}  // namespace Qt3DExtras

//  from ../qt3d/src/extras/defaults/qdiffusespecularmapmaterial.cpp, line 66, as _ZN10Qt3DExtras34QDiffuseSpecularMapMaterialPrivate4initEv
namespace Qt3DExtras {
using namespace Qt3DRender;
inline void QDiffuseSpecularMapMaterialPrivate::init()
{
    Q_Q(QDiffuseSpecularMapMaterial);

    connect(m_ambientParameter, &Qt3DRender::QParameter::valueChanged,
            this, &QDiffuseSpecularMapMaterialPrivate::handleAmbientChanged);
    connect(m_diffuseParameter, &Qt3DRender::QParameter::valueChanged,
            this, &QDiffuseSpecularMapMaterialPrivate::handleDiffuseChanged);
    connect(m_specularParameter, &Qt3DRender::QParameter::valueChanged,
            this, &QDiffuseSpecularMapMaterialPrivate::handleSpecularChanged);
    connect(m_shininessParameter, &Qt3DRender::QParameter::valueChanged,
            this, &QDiffuseSpecularMapMaterialPrivate::handleShininessChanged);
    connect(m_textureScaleParameter, &Qt3DRender::QParameter::valueChanged,
            this, &QDiffuseSpecularMapMaterialPrivate::handleTextureScaleChanged);

    m_diffuseSpecularMapGL3Shader->setVertexShaderCode(QShaderProgram::loadSource(QUrl(QStringLiteral("qrc:/shaders/gl3/default.vert"))));
    m_diffuseSpecularMapGL3ShaderBuilder->setParent(q);
    m_diffuseSpecularMapGL3ShaderBuilder->setShaderProgram(m_diffuseSpecularMapGL3Shader);
    m_diffuseSpecularMapGL3ShaderBuilder->setFragmentShaderGraph(QUrl(QStringLiteral("qrc:/shaders/graphs/phong.frag.json")));
    m_diffuseSpecularMapGL3ShaderBuilder->setEnabledLayers({QStringLiteral("diffuseTexture"),
                                                            QStringLiteral("specularTexture"),
                                                            QStringLiteral("normal")});

    m_diffuseSpecularMapGL2ES2Shader->setVertexShaderCode(QShaderProgram::loadSource(QUrl(QStringLiteral("qrc:/shaders/es2/default.vert"))));
    m_diffuseSpecularMapGL2ES2ShaderBuilder->setParent(q);
    m_diffuseSpecularMapGL2ES2ShaderBuilder->setShaderProgram(m_diffuseSpecularMapGL2ES2Shader);
    m_diffuseSpecularMapGL2ES2ShaderBuilder->setFragmentShaderGraph(QUrl(QStringLiteral("qrc:/shaders/graphs/phong.frag.json")));
    m_diffuseSpecularMapGL2ES2ShaderBuilder->setEnabledLayers({QStringLiteral("diffuseTexture"),
                                                               QStringLiteral("specularTexture"),
                                                               QStringLiteral("normal")});

    m_diffuseSpecularMapRHIShader->setVertexShaderCode(QShaderProgram::loadSource(QUrl(QStringLiteral("qrc:/shaders/rhi/default_pos_norm_tex.vert"))));
    m_diffuseSpecularMapRHIShaderBuilder->setParent(q);
    m_diffuseSpecularMapRHIShaderBuilder->setShaderProgram(m_diffuseSpecularMapRHIShader);
    m_diffuseSpecularMapRHIShaderBuilder->setFragmentShaderGraph(QUrl(QStringLiteral("qrc:/shaders/graphs/phong.frag.json")));
    m_diffuseSpecularMapRHIShaderBuilder->setEnabledLayers({QStringLiteral("diffuseTexture"),
                                                            QStringLiteral("specularTexture"),
                                                            QStringLiteral("normal")});

    m_diffuseSpecularMapGL3Technique->graphicsApiFilter()->setApi(QGraphicsApiFilter::OpenGL);
    m_diffuseSpecularMapGL3Technique->graphicsApiFilter()->setMajorVersion(3);
    m_diffuseSpecularMapGL3Technique->graphicsApiFilter()->setMinorVersion(1);
    m_diffuseSpecularMapGL3Technique->graphicsApiFilter()->setProfile(QGraphicsApiFilter::CoreProfile);

    m_diffuseSpecularMapGL2Technique->graphicsApiFilter()->setApi(QGraphicsApiFilter::OpenGL);
    m_diffuseSpecularMapGL2Technique->graphicsApiFilter()->setMajorVersion(2);
    m_diffuseSpecularMapGL2Technique->graphicsApiFilter()->setMinorVersion(0);
    m_diffuseSpecularMapGL2Technique->graphicsApiFilter()->setProfile(QGraphicsApiFilter::NoProfile);

    m_diffuseSpecularMapES2Technique->graphicsApiFilter()->setApi(QGraphicsApiFilter::OpenGLES);
    m_diffuseSpecularMapES2Technique->graphicsApiFilter()->setMajorVersion(2);
    m_diffuseSpecularMapES2Technique->graphicsApiFilter()->setMinorVersion(0);
    m_diffuseSpecularMapES2Technique->graphicsApiFilter()->setProfile(QGraphicsApiFilter::NoProfile);

    m_diffuseSpecularMapRHITechnique->graphicsApiFilter()->setApi(QGraphicsApiFilter::RHI);
    m_diffuseSpecularMapRHITechnique->graphicsApiFilter()->setMajorVersion(1);
    m_diffuseSpecularMapRHITechnique->graphicsApiFilter()->setMinorVersion(0);

    m_filterKey->setParent(q);
    m_filterKey->setName(QStringLiteral("renderingStyle"));
    m_filterKey->setValue(QStringLiteral("forward"));

    m_diffuseSpecularMapGL3Technique->addFilterKey(m_filterKey);
    m_diffuseSpecularMapGL2Technique->addFilterKey(m_filterKey);
    m_diffuseSpecularMapES2Technique->addFilterKey(m_filterKey);
    m_diffuseSpecularMapRHITechnique->addFilterKey(m_filterKey);

    m_diffuseSpecularMapGL3RenderPass->setShaderProgram(m_diffuseSpecularMapGL3Shader);
    m_diffuseSpecularMapGL2RenderPass->setShaderProgram(m_diffuseSpecularMapGL2ES2Shader);
    m_diffuseSpecularMapES2RenderPass->setShaderProgram(m_diffuseSpecularMapGL2ES2Shader);
    m_diffuseSpecularMapRHIRenderPass->setShaderProgram(m_diffuseSpecularMapRHIShader);

    m_diffuseSpecularMapGL3Technique->addRenderPass(m_diffuseSpecularMapGL3RenderPass);
    m_diffuseSpecularMapGL2Technique->addRenderPass(m_diffuseSpecularMapGL2RenderPass);
    m_diffuseSpecularMapES2Technique->addRenderPass(m_diffuseSpecularMapES2RenderPass);
    m_diffuseSpecularMapRHITechnique->addRenderPass(m_diffuseSpecularMapRHIRenderPass);

    m_diffuseSpecularMapEffect->addTechnique(m_diffuseSpecularMapGL3Technique);
    m_diffuseSpecularMapEffect->addTechnique(m_diffuseSpecularMapGL2Technique);
    m_diffuseSpecularMapEffect->addTechnique(m_diffuseSpecularMapES2Technique);
    m_diffuseSpecularMapEffect->addTechnique(m_diffuseSpecularMapRHITechnique);

    m_diffuseSpecularMapEffect->addParameter(m_ambientParameter);
    m_diffuseSpecularMapEffect->addParameter(m_diffuseParameter);
    m_diffuseSpecularMapEffect->addParameter(m_specularParameter);
    m_diffuseSpecularMapEffect->addParameter(m_shininessParameter);
    m_diffuseSpecularMapEffect->addParameter(m_textureScaleParameter);

    q->setEffect(m_diffuseSpecularMapEffect);
}
}  // namespace Qt3DExtras

//  from ../qt3d/src/extras/defaults/qdiffusespecularmapmaterial.cpp, line 157, as _ZN10Qt3DExtras34QDiffuseSpecularMapMaterialPrivate20handleAmbientChangedERK8QVariant
namespace Qt3DExtras {
using namespace Qt3DRender;
inline void QDiffuseSpecularMapMaterialPrivate::handleAmbientChanged(const QVariant &var)
{
    Q_Q(QDiffuseSpecularMapMaterial);
    emit q->ambientChanged(var.value<QColor>());
}
}  // namespace Qt3DExtras

//  from ../qt3d/src/extras/defaults/qdiffusespecularmapmaterial.cpp, line 163, as _ZN10Qt3DExtras34QDiffuseSpecularMapMaterialPrivate20handleDiffuseChangedERK8QVariant
namespace Qt3DExtras {
using namespace Qt3DRender;
inline void QDiffuseSpecularMapMaterialPrivate::handleDiffuseChanged(const QVariant &var)
{
    Q_Q(QDiffuseSpecularMapMaterial);
    emit q->diffuseChanged(var.value<QAbstractTexture *>());
}
}  // namespace Qt3DExtras

//  from ../qt3d/src/extras/defaults/qdiffusespecularmapmaterial.cpp, line 169, as _ZN10Qt3DExtras34QDiffuseSpecularMapMaterialPrivate21handleSpecularChangedERK8QVariant
namespace Qt3DExtras {
using namespace Qt3DRender;
inline void QDiffuseSpecularMapMaterialPrivate::handleSpecularChanged(const QVariant &var)
{
    Q_Q(QDiffuseSpecularMapMaterial);
    emit q->specularChanged(var.value<QAbstractTexture *>());
}
}  // namespace Qt3DExtras

//  from ../qt3d/src/extras/defaults/qdiffusespecularmapmaterial.cpp, line 175, as _ZN10Qt3DExtras34QDiffuseSpecularMapMaterialPrivate22handleShininessChangedERK8QVariant
namespace Qt3DExtras {
using namespace Qt3DRender;
inline void QDiffuseSpecularMapMaterialPrivate::handleShininessChanged(const QVariant &var)
{
    Q_Q(QDiffuseSpecularMapMaterial);
    emit q->shininessChanged(var.toFloat());
}
}  // namespace Qt3DExtras

//  from ../qt3d/src/extras/defaults/qdiffusespecularmapmaterial.cpp, line 181, as _ZN10Qt3DExtras34QDiffuseSpecularMapMaterialPrivate25handleTextureScaleChangedERK8QVariant
namespace Qt3DExtras {
using namespace Qt3DRender;
inline void QDiffuseSpecularMapMaterialPrivate::handleTextureScaleChanged(const QVariant &var)
{
    Q_Q(QDiffuseSpecularMapMaterial);
    emit q->textureScaleChanged(var.toFloat());
}
}  // namespace Qt3DExtras
//  -----------------------------------------------------------------------

//  A Qt3DExtras::QDiffuseSpecularMapMaterialPrivate that Python can take functions over in. Every Qt3DExtras::QDiffuseSpecularMapMaterialPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQt3DExtras_QDiffuseSpecularMapMaterialPrivateCall0)(const void *, Qt3DCore::QScene *, int *);
typedef void (*CuteQt3DExtras_QDiffuseSpecularMapMaterialPrivateCall1)(const void *, int *);
class CuteQt3DExtras_QDiffuseSpecularMapMaterialPrivate : public Qt3DExtras::QDiffuseSpecularMapMaterialPrivate {
public:
  using Qt3DExtras::QDiffuseSpecularMapMaterialPrivate::QDiffuseSpecularMapMaterialPrivate;
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
      CuteQt3DExtras_QDiffuseSpecularMapMaterialPrivateCall0 call = reinterpret_cast<CuteQt3DExtras_QDiffuseSpecularMapMaterialPrivateCall0>(taken[0]);
      call(this, scene, &handled);
      if (handled) return;
    }
    Qt3DCore::QNodePrivate::setScene(scene);
  }

  //  void Qt3DCore::QNodePrivate::update()
  void update() override {
    if (taken[1]) {
      int handled = 0;
      CuteQt3DExtras_QDiffuseSpecularMapMaterialPrivateCall1 call = reinterpret_cast<CuteQt3DExtras_QDiffuseSpecularMapMaterialPrivateCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    Qt3DCore::QNodePrivate::update();
  }
};

//  Qt3DExtras::QDiffuseSpecularMapMaterialPrivate::QDiffuseSpecularMapMateri
//      alPrivate()
extern "C" Q_DECL_EXPORT
Qt3DExtras::QDiffuseSpecularMapMaterialPrivate *ritual_ZN10Qt3DExtras34QDiffuseSpecularMapMaterialPrivateC1Ev() {
  return new CuteQt3DExtras_QDiffuseSpecularMapMaterialPrivate();
}

//  void Qt3DExtras::QDiffuseSpecularMapMaterialPrivate::init()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras34QDiffuseSpecularMapMaterialPrivate4initEv(
    Qt3DExtras::QDiffuseSpecularMapMaterialPrivate *self) {
  self->init();
}

//  void Qt3DExtras::QDiffuseSpecularMapMaterialPrivate::handleAmbientChanged
//      (const QVariant &var)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras34QDiffuseSpecularMapMaterialPrivate20handleAmbientChangedERK8QVariant(
    Qt3DExtras::QDiffuseSpecularMapMaterialPrivate *self,
    const QVariant *var) {
  self->handleAmbientChanged(*var);
}

//  void Qt3DExtras::QDiffuseSpecularMapMaterialPrivate::handleDiffuseChanged
//      (const QVariant &var)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras34QDiffuseSpecularMapMaterialPrivate20handleDiffuseChangedERK8QVariant(
    Qt3DExtras::QDiffuseSpecularMapMaterialPrivate *self,
    const QVariant *var) {
  self->handleDiffuseChanged(*var);
}

//  void Qt3DExtras::QDiffuseSpecularMapMaterialPrivate::handleSpecularChange
//      d(const QVariant &var)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras34QDiffuseSpecularMapMaterialPrivate21handleSpecularChangedERK8QVariant(
    Qt3DExtras::QDiffuseSpecularMapMaterialPrivate *self,
    const QVariant *var) {
  self->handleSpecularChanged(*var);
}

//  void Qt3DExtras::QDiffuseSpecularMapMaterialPrivate::handleShininessChang
//      ed(const QVariant &var)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras34QDiffuseSpecularMapMaterialPrivate22handleShininessChangedERK8QVariant(
    Qt3DExtras::QDiffuseSpecularMapMaterialPrivate *self,
    const QVariant *var) {
  self->handleShininessChanged(*var);
}

//  void Qt3DExtras::QDiffuseSpecularMapMaterialPrivate::handleTextureScaleCh
//      anged(const QVariant &var)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras34QDiffuseSpecularMapMaterialPrivate25handleTextureScaleChangedERK8QVariant(
    Qt3DExtras::QDiffuseSpecularMapMaterialPrivate *self,
    const QVariant *var) {
  self->handleTextureScaleChanged(*var);
}

//  QDiffuseSpecularMapMaterial
//      *Qt3DExtras::QDiffuseSpecularMapMaterialPrivate::q_func()
extern "C" Q_DECL_EXPORT
Qt3DExtras::QDiffuseSpecularMapMaterial *ritual_ZN10Qt3DExtras34QDiffuseSpecularMapMaterialPrivate6q_funcEv(
    Qt3DExtras::QDiffuseSpecularMapMaterialPrivate *self) {
  return self->q_func();
}

//  const QDiffuseSpecularMapMaterial
//      *Qt3DExtras::QDiffuseSpecularMapMaterialPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const Qt3DExtras::QDiffuseSpecularMapMaterial *ritual_ZNK10Qt3DExtras34QDiffuseSpecularMapMaterialPrivate6q_funcEv(
    const Qt3DExtras::QDiffuseSpecularMapMaterialPrivate *self) {
  return self->q_func();
}

//  a Python function taken by a
//      CuteQt3DExtras_QDiffuseSpecularMapMaterialPrivate, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DExtras_QDiffuseSpecularMapMaterialPrivate(
    Qt3DExtras::QDiffuseSpecularMapMaterialPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DExtras_QDiffuseSpecularMapMaterialPrivate *>(self)->take(key, call);
}
