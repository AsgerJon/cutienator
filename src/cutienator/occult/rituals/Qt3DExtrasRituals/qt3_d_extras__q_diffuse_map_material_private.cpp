//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DExtras/6.12.0/Qt3DExtras/private/qdiffusemapmaterial_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <Qt3DExtras/Qt3DExtras>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DExtras/6.12.0/Qt3DExtras/private/qdiffusemapmaterial_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qvariant.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DExtras/qdiffusemapmaterial.h>
#include <Qt3DExtras/private/qdiffusemapmaterial_p.h>
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

//  from ../qt3d/src/extras/defaults/qdiffusemapmaterial.cpp, line 27, as _ZN10Qt3DExtras26QDiffuseMapMaterialPrivateC1Ev
namespace Qt3DExtras {
using namespace Qt3DRender;
inline QDiffuseMapMaterialPrivate::QDiffuseMapMaterialPrivate()
    : QMaterialPrivate()
    , m_diffuseMapEffect(new QEffect())
    , m_diffuseTexture(new QTexture2D())
    , m_ambientParameter(new QParameter(QStringLiteral("ka"), QColor::fromRgbF(0.05f, 0.05f, 0.05f, 1.0f)))
    , m_diffuseParameter(new QParameter(QStringLiteral("diffuseTexture"), m_diffuseTexture))
    , m_specularParameter(new QParameter(QStringLiteral("ks"), QColor::fromRgbF(0.01f, 0.01f, 0.01f, 1.0f)))
    , m_shininessParameter(new QParameter(QStringLiteral("shininess"), 150.0f))
    , m_textureScaleParameter(new QParameter(QStringLiteral("texCoordScale"), 1.0f))
    , m_diffuseMapGL3Technique(new QTechnique())
    , m_diffuseMapGL2Technique(new QTechnique())
    , m_diffuseMapES2Technique(new QTechnique())
    , m_diffuseMapRHITechnique(new QTechnique())
    , m_diffuseMapGL3RenderPass(new QRenderPass())
    , m_diffuseMapGL2RenderPass(new QRenderPass())
    , m_diffuseMapES2RenderPass(new QRenderPass())
    , m_diffuseMapRHIRenderPass(new QRenderPass())
    , m_diffuseMapGL3Shader(new QShaderProgram())
    , m_diffuseMapGL3ShaderBuilder(new QShaderProgramBuilder())
    , m_diffuseMapGL2ES2Shader(new QShaderProgram())
    , m_diffuseMapGL2ES2ShaderBuilder(new QShaderProgramBuilder())
    , m_diffuseMapRHIShader(new QShaderProgram())
    , m_diffuseMapRHIShaderBuilder(new QShaderProgramBuilder())
    , m_filterKey(new QFilterKey)
{
    m_diffuseTexture->setMagnificationFilter(QAbstractTexture::Linear);
    m_diffuseTexture->setMinificationFilter(QAbstractTexture::LinearMipMapLinear);
    m_diffuseTexture->setWrapMode(QTextureWrapMode(QTextureWrapMode::Repeat));
    m_diffuseTexture->setGenerateMipMaps(true);
    m_diffuseTexture->setMaximumAnisotropy(16.0f);
}
}  // namespace Qt3DExtras

//  from ../qt3d/src/extras/defaults/qdiffusemapmaterial.cpp, line 59, as _ZN10Qt3DExtras26QDiffuseMapMaterialPrivate4initEv
namespace Qt3DExtras {
using namespace Qt3DRender;
inline void QDiffuseMapMaterialPrivate::init()
{
    Q_Q(QDiffuseMapMaterial);

    connect(m_ambientParameter, &Qt3DRender::QParameter::valueChanged,
            this, &QDiffuseMapMaterialPrivate::handleAmbientChanged);
    connect(m_diffuseParameter, &Qt3DRender::QParameter::valueChanged,
            this, &QDiffuseMapMaterialPrivate::handleDiffuseChanged);
    connect(m_specularParameter, &Qt3DRender::QParameter::valueChanged,
            this, &QDiffuseMapMaterialPrivate::handleSpecularChanged);
    connect(m_shininessParameter, &Qt3DRender::QParameter::valueChanged,
            this, &QDiffuseMapMaterialPrivate::handleShininessChanged);
    connect(m_textureScaleParameter, &Qt3DRender::QParameter::valueChanged,
            this, &QDiffuseMapMaterialPrivate::handleTextureScaleChanged);

    m_diffuseMapGL3Shader->setVertexShaderCode(QShaderProgram::loadSource(QUrl(QStringLiteral("qrc:/shaders/gl3/default.vert"))));
    m_diffuseMapGL3ShaderBuilder->setParent(q);
    m_diffuseMapGL3ShaderBuilder->setShaderProgram(m_diffuseMapGL3Shader);
    m_diffuseMapGL3ShaderBuilder->setFragmentShaderGraph(QUrl(QStringLiteral("qrc:/shaders/graphs/phong.frag.json")));
    m_diffuseMapGL3ShaderBuilder->setEnabledLayers({QStringLiteral("diffuseTexture"),
                                                    QStringLiteral("specular"),
                                                    QStringLiteral("normal")});

    m_diffuseMapGL2ES2Shader->setVertexShaderCode(QShaderProgram::loadSource(QUrl(QStringLiteral("qrc:/shaders/es2/default.vert"))));
    m_diffuseMapGL2ES2ShaderBuilder->setParent(q);
    m_diffuseMapGL2ES2ShaderBuilder->setShaderProgram(m_diffuseMapGL2ES2Shader);
    m_diffuseMapGL2ES2ShaderBuilder->setFragmentShaderGraph(QUrl(QStringLiteral("qrc:/shaders/graphs/phong.frag.json")));
    m_diffuseMapGL2ES2ShaderBuilder->setEnabledLayers({QStringLiteral("diffuseTexture"),
                                                       QStringLiteral("specular"),
                                                       QStringLiteral("normal")});

    m_diffuseMapRHIShader->setVertexShaderCode(QShaderProgram::loadSource(QUrl(QStringLiteral("qrc:/shaders/rhi/default_pos_norm_tex.vert"))));
    m_diffuseMapRHIShaderBuilder->setParent(q);
    m_diffuseMapRHIShaderBuilder->setShaderProgram(m_diffuseMapRHIShader);
    m_diffuseMapRHIShaderBuilder->setFragmentShaderGraph(QUrl(QStringLiteral("qrc:/shaders/graphs/phong.frag.json")));
    m_diffuseMapRHIShaderBuilder->setEnabledLayers({QStringLiteral("diffuseTexture"),
                                                    QStringLiteral("specular"),
                                                    QStringLiteral("normal")});

    m_diffuseMapGL3Technique->graphicsApiFilter()->setApi(QGraphicsApiFilter::OpenGL);
    m_diffuseMapGL3Technique->graphicsApiFilter()->setMajorVersion(3);
    m_diffuseMapGL3Technique->graphicsApiFilter()->setMinorVersion(1);
    m_diffuseMapGL3Technique->graphicsApiFilter()->setProfile(QGraphicsApiFilter::CoreProfile);

    m_diffuseMapGL2Technique->graphicsApiFilter()->setApi(QGraphicsApiFilter::OpenGL);
    m_diffuseMapGL2Technique->graphicsApiFilter()->setMajorVersion(2);
    m_diffuseMapGL2Technique->graphicsApiFilter()->setMinorVersion(0);
    m_diffuseMapGL2Technique->graphicsApiFilter()->setProfile(QGraphicsApiFilter::NoProfile);

    m_diffuseMapES2Technique->graphicsApiFilter()->setApi(QGraphicsApiFilter::OpenGLES);
    m_diffuseMapES2Technique->graphicsApiFilter()->setMajorVersion(2);
    m_diffuseMapES2Technique->graphicsApiFilter()->setMinorVersion(0);
    m_diffuseMapES2Technique->graphicsApiFilter()->setProfile(QGraphicsApiFilter::NoProfile);

    m_diffuseMapRHITechnique->graphicsApiFilter()->setApi(QGraphicsApiFilter::RHI);
    m_diffuseMapRHITechnique->graphicsApiFilter()->setMajorVersion(1);
    m_diffuseMapRHITechnique->graphicsApiFilter()->setMinorVersion(0);

    m_filterKey->setParent(q);
    m_filterKey->setName(QStringLiteral("renderingStyle"));
    m_filterKey->setValue(QStringLiteral("forward"));

    m_diffuseMapGL3Technique->addFilterKey(m_filterKey);
    m_diffuseMapGL2Technique->addFilterKey(m_filterKey);
    m_diffuseMapES2Technique->addFilterKey(m_filterKey);
    m_diffuseMapRHITechnique->addFilterKey(m_filterKey);

    m_diffuseMapGL3RenderPass->setShaderProgram(m_diffuseMapGL3Shader);
    m_diffuseMapGL2RenderPass->setShaderProgram(m_diffuseMapGL2ES2Shader);
    m_diffuseMapES2RenderPass->setShaderProgram(m_diffuseMapGL2ES2Shader);
    m_diffuseMapRHIRenderPass->setShaderProgram(m_diffuseMapRHIShader);

    m_diffuseMapGL3Technique->addRenderPass(m_diffuseMapGL3RenderPass);
    m_diffuseMapGL2Technique->addRenderPass(m_diffuseMapGL2RenderPass);
    m_diffuseMapES2Technique->addRenderPass(m_diffuseMapES2RenderPass);
    m_diffuseMapRHITechnique->addRenderPass(m_diffuseMapRHIRenderPass);

    m_diffuseMapEffect->addTechnique(m_diffuseMapGL3Technique);
    m_diffuseMapEffect->addTechnique(m_diffuseMapGL2Technique);
    m_diffuseMapEffect->addTechnique(m_diffuseMapES2Technique);
    m_diffuseMapEffect->addTechnique(m_diffuseMapRHITechnique);

    m_diffuseMapEffect->addParameter(m_ambientParameter);
    m_diffuseMapEffect->addParameter(m_diffuseParameter);
    m_diffuseMapEffect->addParameter(m_specularParameter);
    m_diffuseMapEffect->addParameter(m_shininessParameter);
    m_diffuseMapEffect->addParameter(m_textureScaleParameter);

    q->setEffect(m_diffuseMapEffect);
}
}  // namespace Qt3DExtras

//  from ../qt3d/src/extras/defaults/qdiffusemapmaterial.cpp, line 150, as _ZN10Qt3DExtras26QDiffuseMapMaterialPrivate20handleAmbientChangedERK8QVariant
namespace Qt3DExtras {
using namespace Qt3DRender;
inline void QDiffuseMapMaterialPrivate::handleAmbientChanged(const QVariant &var)
{
    Q_Q(QDiffuseMapMaterial);
    emit q->ambientChanged(var.value<QColor>());
}
}  // namespace Qt3DExtras

//  from ../qt3d/src/extras/defaults/qdiffusemapmaterial.cpp, line 156, as _ZN10Qt3DExtras26QDiffuseMapMaterialPrivate20handleDiffuseChangedERK8QVariant
namespace Qt3DExtras {
using namespace Qt3DRender;
inline void QDiffuseMapMaterialPrivate::handleDiffuseChanged(const QVariant &var)
{
    Q_Q(QDiffuseMapMaterial);
    emit q->diffuseChanged(var.value<QAbstractTexture *>());
}
}  // namespace Qt3DExtras

//  from ../qt3d/src/extras/defaults/qdiffusemapmaterial.cpp, line 162, as _ZN10Qt3DExtras26QDiffuseMapMaterialPrivate21handleSpecularChangedERK8QVariant
namespace Qt3DExtras {
using namespace Qt3DRender;
inline void QDiffuseMapMaterialPrivate::handleSpecularChanged(const QVariant &var)
{
    Q_Q(QDiffuseMapMaterial);
    emit q->specularChanged(var.value<QColor>());
}
}  // namespace Qt3DExtras

//  from ../qt3d/src/extras/defaults/qdiffusemapmaterial.cpp, line 168, as _ZN10Qt3DExtras26QDiffuseMapMaterialPrivate22handleShininessChangedERK8QVariant
namespace Qt3DExtras {
using namespace Qt3DRender;
inline void QDiffuseMapMaterialPrivate::handleShininessChanged(const QVariant &var)
{
    Q_Q(QDiffuseMapMaterial);
    emit q->shininessChanged(var.toFloat());
}
}  // namespace Qt3DExtras

//  from ../qt3d/src/extras/defaults/qdiffusemapmaterial.cpp, line 174, as _ZN10Qt3DExtras26QDiffuseMapMaterialPrivate25handleTextureScaleChangedERK8QVariant
namespace Qt3DExtras {
using namespace Qt3DRender;
inline void QDiffuseMapMaterialPrivate::handleTextureScaleChanged(const QVariant &var)
{
    Q_Q(QDiffuseMapMaterial);
    emit q->textureScaleChanged(var.toFloat());
}
}  // namespace Qt3DExtras
//  -----------------------------------------------------------------------

//  A Qt3DExtras::QDiffuseMapMaterialPrivate that Python can take functions over in. Every Qt3DExtras::QDiffuseMapMaterialPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQt3DExtras_QDiffuseMapMaterialPrivateCall0)(const void *, Qt3DCore::QScene *, int *);
typedef void (*CuteQt3DExtras_QDiffuseMapMaterialPrivateCall1)(const void *, int *);
class CuteQt3DExtras_QDiffuseMapMaterialPrivate : public Qt3DExtras::QDiffuseMapMaterialPrivate {
public:
  using Qt3DExtras::QDiffuseMapMaterialPrivate::QDiffuseMapMaterialPrivate;
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
      CuteQt3DExtras_QDiffuseMapMaterialPrivateCall0 call = reinterpret_cast<CuteQt3DExtras_QDiffuseMapMaterialPrivateCall0>(taken[0]);
      call(this, scene, &handled);
      if (handled) return;
    }
    Qt3DCore::QNodePrivate::setScene(scene);
  }

  //  void Qt3DCore::QNodePrivate::update()
  void update() override {
    if (taken[1]) {
      int handled = 0;
      CuteQt3DExtras_QDiffuseMapMaterialPrivateCall1 call = reinterpret_cast<CuteQt3DExtras_QDiffuseMapMaterialPrivateCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    Qt3DCore::QNodePrivate::update();
  }
};

//  Qt3DExtras::QDiffuseMapMaterialPrivate::QDiffuseMapMaterialPrivate()
extern "C" Q_DECL_EXPORT
Qt3DExtras::QDiffuseMapMaterialPrivate *ritual_ZN10Qt3DExtras26QDiffuseMapMaterialPrivateC1Ev() {
  return new CuteQt3DExtras_QDiffuseMapMaterialPrivate();
}

//  void Qt3DExtras::QDiffuseMapMaterialPrivate::init()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras26QDiffuseMapMaterialPrivate4initEv(
    Qt3DExtras::QDiffuseMapMaterialPrivate *self) {
  self->init();
}

//  void Qt3DExtras::QDiffuseMapMaterialPrivate::handleAmbientChanged(const
//      QVariant &var)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras26QDiffuseMapMaterialPrivate20handleAmbientChangedERK8QVariant(
    Qt3DExtras::QDiffuseMapMaterialPrivate *self,
    const QVariant *var) {
  self->handleAmbientChanged(*var);
}

//  void Qt3DExtras::QDiffuseMapMaterialPrivate::handleDiffuseChanged(const
//      QVariant &var)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras26QDiffuseMapMaterialPrivate20handleDiffuseChangedERK8QVariant(
    Qt3DExtras::QDiffuseMapMaterialPrivate *self,
    const QVariant *var) {
  self->handleDiffuseChanged(*var);
}

//  void Qt3DExtras::QDiffuseMapMaterialPrivate::handleSpecularChanged(const
//      QVariant &var)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras26QDiffuseMapMaterialPrivate21handleSpecularChangedERK8QVariant(
    Qt3DExtras::QDiffuseMapMaterialPrivate *self,
    const QVariant *var) {
  self->handleSpecularChanged(*var);
}

//  void Qt3DExtras::QDiffuseMapMaterialPrivate::handleShininessChanged(const
//      QVariant &var)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras26QDiffuseMapMaterialPrivate22handleShininessChangedERK8QVariant(
    Qt3DExtras::QDiffuseMapMaterialPrivate *self,
    const QVariant *var) {
  self->handleShininessChanged(*var);
}

//  void
//      Qt3DExtras::QDiffuseMapMaterialPrivate::handleTextureScaleChanged(con
//      st QVariant &var)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras26QDiffuseMapMaterialPrivate25handleTextureScaleChangedERK8QVariant(
    Qt3DExtras::QDiffuseMapMaterialPrivate *self,
    const QVariant *var) {
  self->handleTextureScaleChanged(*var);
}

//  QDiffuseMapMaterial *Qt3DExtras::QDiffuseMapMaterialPrivate::q_func()
extern "C" Q_DECL_EXPORT
Qt3DExtras::QDiffuseMapMaterial *ritual_ZN10Qt3DExtras26QDiffuseMapMaterialPrivate6q_funcEv(
    Qt3DExtras::QDiffuseMapMaterialPrivate *self) {
  return self->q_func();
}

//  const QDiffuseMapMaterial
//      *Qt3DExtras::QDiffuseMapMaterialPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const Qt3DExtras::QDiffuseMapMaterial *ritual_ZNK10Qt3DExtras26QDiffuseMapMaterialPrivate6q_funcEv(
    const Qt3DExtras::QDiffuseMapMaterialPrivate *self) {
  return self->q_func();
}

//  a Python function taken by a CuteQt3DExtras_QDiffuseMapMaterialPrivate,
//      for the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DExtras_QDiffuseMapMaterialPrivate(
    Qt3DExtras::QDiffuseMapMaterialPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DExtras_QDiffuseMapMaterialPrivate *>(self)->take(key, call);
}
