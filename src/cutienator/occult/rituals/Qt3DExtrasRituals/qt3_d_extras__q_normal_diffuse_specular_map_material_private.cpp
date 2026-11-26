//  Written by dev_tooling.RitualGenerator from the records of Qt3DExtras/6.1
//  2.0/Qt3DExtras/private/qnormaldiffusespecularmapmaterial_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <Qt3DExtras/Qt3DExtras>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DExtras/6.12.0/Qt3DExtras/private/qnormaldiffusespecularmapmaterial_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qvariant.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DExtras/qnormaldiffusespecularmapmaterial.h>
#include <Qt3DExtras/private/qnormaldiffusespecularmapmaterial_p.h>
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

//  from ../qt3d/src/extras/defaults/qnormaldiffusespecularmapmaterial.cpp, line 27, as _ZN10Qt3DExtras40QNormalDiffuseSpecularMapMaterialPrivateC1Ev
namespace Qt3DExtras {
using namespace Qt3DRender;
inline QNormalDiffuseSpecularMapMaterialPrivate::QNormalDiffuseSpecularMapMaterialPrivate()
    : QMaterialPrivate()
    , m_normalDiffuseSpecularEffect(new QEffect())
    , m_diffuseTexture(new QTexture2D())
    , m_normalTexture(new QTexture2D())
    , m_specularTexture(new QTexture2D())
    , m_ambientParameter(new QParameter(QStringLiteral("ka"), QColor::fromRgbF(0.05f, 0.05f, 0.05f, 1.0f)))
    , m_diffuseParameter(new QParameter(QStringLiteral("diffuseTexture"), m_diffuseTexture))
    , m_normalParameter(new QParameter(QStringLiteral("normalTexture"), m_normalTexture))
    , m_specularParameter(new QParameter(QStringLiteral("specularTexture"), m_specularTexture))
    , m_shininessParameter(new QParameter(QStringLiteral("shininess"), 150.0f))
    , m_textureScaleParameter(new QParameter(QStringLiteral("texCoordScale"), 1.0f))
    , m_normalDiffuseSpecularGL3Technique(new QTechnique())
    , m_normalDiffuseSpecularGL2Technique(new QTechnique())
    , m_normalDiffuseSpecularES2Technique(new QTechnique())
    , m_normalDiffuseSpecularRHITechnique(new QTechnique())
    , m_normalDiffuseSpecularGL3RenderPass(new QRenderPass())
    , m_normalDiffuseSpecularGL2RenderPass(new QRenderPass())
    , m_normalDiffuseSpecularES2RenderPass(new QRenderPass())
    , m_normalDiffuseSpecularRHIRenderPass(new QRenderPass())
    , m_normalDiffuseSpecularGL3Shader(new QShaderProgram())
    , m_normalDiffuseSpecularGL3ShaderBuilder(new QShaderProgramBuilder())
    , m_normalDiffuseSpecularGL2ES2Shader(new QShaderProgram())
    , m_normalDiffuseSpecularGL2ES2ShaderBuilder(new QShaderProgramBuilder())
    , m_normalDiffuseSpecularRHIShader(new QShaderProgram())
    , m_normalDiffuseSpecularRHIShaderBuilder(new QShaderProgramBuilder())
    , m_filterKey(new QFilterKey)
{
    m_diffuseTexture->setMagnificationFilter(QAbstractTexture::Linear);
    m_diffuseTexture->setMinificationFilter(QAbstractTexture::LinearMipMapLinear);
    m_diffuseTexture->setWrapMode(QTextureWrapMode(QTextureWrapMode::Repeat));
    m_diffuseTexture->setGenerateMipMaps(true);
    m_diffuseTexture->setMaximumAnisotropy(16.0f);

    m_normalTexture->setMagnificationFilter(QAbstractTexture::Linear);
    m_normalTexture->setMinificationFilter(QAbstractTexture::LinearMipMapLinear);
    m_normalTexture->setWrapMode(QTextureWrapMode(QTextureWrapMode::Repeat));
    m_normalTexture->setGenerateMipMaps(true);
    m_normalTexture->setMaximumAnisotropy(16.0f);

    m_specularTexture->setMagnificationFilter(QAbstractTexture::Linear);
    m_specularTexture->setMinificationFilter(QAbstractTexture::LinearMipMapLinear);
    m_specularTexture->setWrapMode(QTextureWrapMode(QTextureWrapMode::Repeat));
    m_specularTexture->setGenerateMipMaps(true);
    m_specularTexture->setMaximumAnisotropy(16.0f);
}
}  // namespace Qt3DExtras

//  from ../qt3d/src/extras/defaults/qnormaldiffusespecularmapmaterial.cpp, line 74, as _ZN10Qt3DExtras40QNormalDiffuseSpecularMapMaterialPrivate4initEv
namespace Qt3DExtras {
using namespace Qt3DRender;
inline void QNormalDiffuseSpecularMapMaterialPrivate::init()
{
    Q_Q(QNormalDiffuseSpecularMapMaterial);

    connect(m_ambientParameter, &Qt3DRender::QParameter::valueChanged,
            this, &QNormalDiffuseSpecularMapMaterialPrivate::handleAmbientChanged);
    connect(m_diffuseParameter, &Qt3DRender::QParameter::valueChanged,
            this, &QNormalDiffuseSpecularMapMaterialPrivate::handleDiffuseChanged);
    connect(m_normalParameter, &Qt3DRender::QParameter::valueChanged,
            this, &QNormalDiffuseSpecularMapMaterialPrivate::handleNormalChanged);
    connect(m_specularParameter, &Qt3DRender::QParameter::valueChanged,
            this, &QNormalDiffuseSpecularMapMaterialPrivate::handleSpecularChanged);
    connect(m_shininessParameter, &Qt3DRender::QParameter::valueChanged,
            this, &QNormalDiffuseSpecularMapMaterialPrivate::handleShininessChanged);
    connect(m_textureScaleParameter, &Qt3DRender::QParameter::valueChanged,
            this, &QNormalDiffuseSpecularMapMaterialPrivate::handleTextureScaleChanged);

    m_normalDiffuseSpecularGL3Shader->setVertexShaderCode(QShaderProgram::loadSource(QUrl(QStringLiteral("qrc:/shaders/gl3/default.vert"))));
    m_normalDiffuseSpecularGL3ShaderBuilder->setParent(q);
    m_normalDiffuseSpecularGL3ShaderBuilder->setShaderProgram(m_normalDiffuseSpecularGL3Shader);
    m_normalDiffuseSpecularGL3ShaderBuilder->setFragmentShaderGraph(QUrl(QStringLiteral("qrc:/shaders/graphs/phong.frag.json")));
    m_normalDiffuseSpecularGL3ShaderBuilder->setEnabledLayers({QStringLiteral("diffuseTexture"),
                                                               QStringLiteral("specularTexture"),
                                                               QStringLiteral("normalTexture")});

    m_normalDiffuseSpecularGL2ES2Shader->setVertexShaderCode(QShaderProgram::loadSource(QUrl(QStringLiteral("qrc:/shaders/es2/default.vert"))));
    m_normalDiffuseSpecularGL2ES2ShaderBuilder->setParent(q);
    m_normalDiffuseSpecularGL2ES2ShaderBuilder->setShaderProgram(m_normalDiffuseSpecularGL2ES2Shader);
    m_normalDiffuseSpecularGL2ES2ShaderBuilder->setFragmentShaderGraph(QUrl(QStringLiteral("qrc:/shaders/graphs/phong.frag.json")));
    m_normalDiffuseSpecularGL2ES2ShaderBuilder->setEnabledLayers({QStringLiteral("diffuseTexture"),
                                                                  QStringLiteral("specularTexture"),
                                                                  QStringLiteral("normalTexture")});

    m_normalDiffuseSpecularRHIShader->setVertexShaderCode(QShaderProgram::loadSource(QUrl(QStringLiteral("qrc:/shaders/rhi/default_pos_norm_tex_tan.vert"))));
    m_normalDiffuseSpecularRHIShaderBuilder->setParent(q);
    m_normalDiffuseSpecularRHIShaderBuilder->setShaderProgram(m_normalDiffuseSpecularRHIShader);
    m_normalDiffuseSpecularRHIShaderBuilder->setFragmentShaderGraph(QUrl(QStringLiteral("qrc:/shaders/graphs/phong.frag.json")));
    m_normalDiffuseSpecularRHIShaderBuilder->setEnabledLayers({QStringLiteral("diffuseTexture"),
                                                               QStringLiteral("specularTexture"),
                                                               QStringLiteral("normalTexture")});

    m_normalDiffuseSpecularGL3Technique->graphicsApiFilter()->setApi(QGraphicsApiFilter::OpenGL);
    m_normalDiffuseSpecularGL3Technique->graphicsApiFilter()->setMajorVersion(3);
    m_normalDiffuseSpecularGL3Technique->graphicsApiFilter()->setMinorVersion(1);
    m_normalDiffuseSpecularGL3Technique->graphicsApiFilter()->setProfile(QGraphicsApiFilter::CoreProfile);

    m_normalDiffuseSpecularGL2Technique->graphicsApiFilter()->setApi(QGraphicsApiFilter::OpenGL);
    m_normalDiffuseSpecularGL2Technique->graphicsApiFilter()->setMajorVersion(2);
    m_normalDiffuseSpecularGL2Technique->graphicsApiFilter()->setMinorVersion(0);
    m_normalDiffuseSpecularGL2Technique->graphicsApiFilter()->setProfile(QGraphicsApiFilter::NoProfile);

    m_normalDiffuseSpecularES2Technique->graphicsApiFilter()->setApi(QGraphicsApiFilter::OpenGLES);
    m_normalDiffuseSpecularES2Technique->graphicsApiFilter()->setMajorVersion(2);
    m_normalDiffuseSpecularES2Technique->graphicsApiFilter()->setMinorVersion(0);
    m_normalDiffuseSpecularES2Technique->graphicsApiFilter()->setProfile(QGraphicsApiFilter::NoProfile);

    m_normalDiffuseSpecularRHITechnique->graphicsApiFilter()->setApi(QGraphicsApiFilter::RHI);
    m_normalDiffuseSpecularRHITechnique->graphicsApiFilter()->setMajorVersion(1);
    m_normalDiffuseSpecularRHITechnique->graphicsApiFilter()->setMinorVersion(0);

    m_filterKey->setParent(q);
    m_filterKey->setName(QStringLiteral("renderingStyle"));
    m_filterKey->setValue(QStringLiteral("forward"));

    m_normalDiffuseSpecularGL3Technique->addFilterKey(m_filterKey);
    m_normalDiffuseSpecularGL2Technique->addFilterKey(m_filterKey);
    m_normalDiffuseSpecularES2Technique->addFilterKey(m_filterKey);
    m_normalDiffuseSpecularRHITechnique->addFilterKey(m_filterKey);

    m_normalDiffuseSpecularGL3RenderPass->setShaderProgram(m_normalDiffuseSpecularGL3Shader);
    m_normalDiffuseSpecularGL2RenderPass->setShaderProgram(m_normalDiffuseSpecularGL2ES2Shader);
    m_normalDiffuseSpecularES2RenderPass->setShaderProgram(m_normalDiffuseSpecularGL2ES2Shader);
    m_normalDiffuseSpecularRHIRenderPass->setShaderProgram(m_normalDiffuseSpecularRHIShader);

    m_normalDiffuseSpecularGL3Technique->addRenderPass(m_normalDiffuseSpecularGL3RenderPass);
    m_normalDiffuseSpecularGL2Technique->addRenderPass(m_normalDiffuseSpecularGL2RenderPass);
    m_normalDiffuseSpecularES2Technique->addRenderPass(m_normalDiffuseSpecularES2RenderPass);
    m_normalDiffuseSpecularRHITechnique->addRenderPass(m_normalDiffuseSpecularRHIRenderPass);

    m_normalDiffuseSpecularEffect->addTechnique(m_normalDiffuseSpecularGL3Technique);
    m_normalDiffuseSpecularEffect->addTechnique(m_normalDiffuseSpecularGL2Technique);
    m_normalDiffuseSpecularEffect->addTechnique(m_normalDiffuseSpecularES2Technique);
    m_normalDiffuseSpecularEffect->addTechnique(m_normalDiffuseSpecularRHITechnique);

    m_normalDiffuseSpecularEffect->addParameter(m_ambientParameter);
    m_normalDiffuseSpecularEffect->addParameter(m_diffuseParameter);
    m_normalDiffuseSpecularEffect->addParameter(m_normalParameter);
    m_normalDiffuseSpecularEffect->addParameter(m_specularParameter);
    m_normalDiffuseSpecularEffect->addParameter(m_shininessParameter);
    m_normalDiffuseSpecularEffect->addParameter(m_textureScaleParameter);

    q->setEffect(m_normalDiffuseSpecularEffect);
}
}  // namespace Qt3DExtras

//  from ../qt3d/src/extras/defaults/qnormaldiffusespecularmapmaterial.cpp, line 168, as _ZN10Qt3DExtras40QNormalDiffuseSpecularMapMaterialPrivate20handleAmbientChangedERK8QVariant
namespace Qt3DExtras {
using namespace Qt3DRender;
inline void QNormalDiffuseSpecularMapMaterialPrivate::handleAmbientChanged(const QVariant &var)
{
    Q_Q(QNormalDiffuseSpecularMapMaterial);
    emit q->ambientChanged(var.value<QColor>());
}
}  // namespace Qt3DExtras

//  from ../qt3d/src/extras/defaults/qnormaldiffusespecularmapmaterial.cpp, line 174, as _ZN10Qt3DExtras40QNormalDiffuseSpecularMapMaterialPrivate20handleDiffuseChangedERK8QVariant
namespace Qt3DExtras {
using namespace Qt3DRender;
inline void QNormalDiffuseSpecularMapMaterialPrivate::handleDiffuseChanged(const QVariant &var)
{
    Q_Q(QNormalDiffuseSpecularMapMaterial);
    emit q->diffuseChanged(var.value<QAbstractTexture *>());
}
}  // namespace Qt3DExtras

//  from ../qt3d/src/extras/defaults/qnormaldiffusespecularmapmaterial.cpp, line 180, as _ZN10Qt3DExtras40QNormalDiffuseSpecularMapMaterialPrivate19handleNormalChangedERK8QVariant
namespace Qt3DExtras {
using namespace Qt3DRender;
inline void QNormalDiffuseSpecularMapMaterialPrivate::handleNormalChanged(const QVariant &var)
{
    Q_Q(QNormalDiffuseSpecularMapMaterial);
    emit q->normalChanged(var.value<QAbstractTexture *>());
}
}  // namespace Qt3DExtras

//  from ../qt3d/src/extras/defaults/qnormaldiffusespecularmapmaterial.cpp, line 186, as _ZN10Qt3DExtras40QNormalDiffuseSpecularMapMaterialPrivate21handleSpecularChangedERK8QVariant
namespace Qt3DExtras {
using namespace Qt3DRender;
inline void QNormalDiffuseSpecularMapMaterialPrivate::handleSpecularChanged(const QVariant &var)
{
    Q_Q(QNormalDiffuseSpecularMapMaterial);
    emit q->specularChanged(var.value<QAbstractTexture *>());
}
}  // namespace Qt3DExtras

//  from ../qt3d/src/extras/defaults/qnormaldiffusespecularmapmaterial.cpp, line 192, as _ZN10Qt3DExtras40QNormalDiffuseSpecularMapMaterialPrivate22handleShininessChangedERK8QVariant
namespace Qt3DExtras {
using namespace Qt3DRender;
inline void QNormalDiffuseSpecularMapMaterialPrivate::handleShininessChanged(const QVariant &var)
{
    Q_Q(QNormalDiffuseSpecularMapMaterial);
    emit q->shininessChanged(var.toFloat());
}
}  // namespace Qt3DExtras

//  from ../qt3d/src/extras/defaults/qnormaldiffusespecularmapmaterial.cpp, line 198, as _ZN10Qt3DExtras40QNormalDiffuseSpecularMapMaterialPrivate25handleTextureScaleChangedERK8QVariant
namespace Qt3DExtras {
using namespace Qt3DRender;
inline void QNormalDiffuseSpecularMapMaterialPrivate::handleTextureScaleChanged(const QVariant &var)
{
    Q_Q(QNormalDiffuseSpecularMapMaterial);
    emit q->textureScaleChanged(var.toFloat());
}
}  // namespace Qt3DExtras
//  -----------------------------------------------------------------------

//  A Qt3DExtras::QNormalDiffuseSpecularMapMaterialPrivate that Python can take functions over in. Every Qt3DExtras::QNormalDiffuseSpecularMapMaterialPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQt3DExtras_QNormalDiffuseSpecularMapMaterialPrivateCall0)(const void *, Qt3DCore::QScene *, int *);
typedef void (*CuteQt3DExtras_QNormalDiffuseSpecularMapMaterialPrivateCall1)(const void *, int *);
class CuteQt3DExtras_QNormalDiffuseSpecularMapMaterialPrivate : public Qt3DExtras::QNormalDiffuseSpecularMapMaterialPrivate {
public:
  using Qt3DExtras::QNormalDiffuseSpecularMapMaterialPrivate::QNormalDiffuseSpecularMapMaterialPrivate;
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
      CuteQt3DExtras_QNormalDiffuseSpecularMapMaterialPrivateCall0 call = reinterpret_cast<CuteQt3DExtras_QNormalDiffuseSpecularMapMaterialPrivateCall0>(taken[0]);
      call(this, scene, &handled);
      if (handled) return;
    }
    Qt3DCore::QNodePrivate::setScene(scene);
  }

  //  void Qt3DCore::QNodePrivate::update()
  void update() override {
    if (taken[1]) {
      int handled = 0;
      CuteQt3DExtras_QNormalDiffuseSpecularMapMaterialPrivateCall1 call = reinterpret_cast<CuteQt3DExtras_QNormalDiffuseSpecularMapMaterialPrivateCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    Qt3DCore::QNodePrivate::update();
  }
};

//  Qt3DExtras::QNormalDiffuseSpecularMapMaterialPrivate::QNormalDiffuseSpecu
//      larMapMaterialPrivate()
extern "C" Q_DECL_EXPORT
Qt3DExtras::QNormalDiffuseSpecularMapMaterialPrivate *ritual_ZN10Qt3DExtras40QNormalDiffuseSpecularMapMaterialPrivateC1Ev() {
  return new CuteQt3DExtras_QNormalDiffuseSpecularMapMaterialPrivate();
}

//  void Qt3DExtras::QNormalDiffuseSpecularMapMaterialPrivate::init()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras40QNormalDiffuseSpecularMapMaterialPrivate4initEv(
    Qt3DExtras::QNormalDiffuseSpecularMapMaterialPrivate *self) {
  self->init();
}

//  void Qt3DExtras::QNormalDiffuseSpecularMapMaterialPrivate::handleAmbientC
//      hanged(const QVariant &var)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras40QNormalDiffuseSpecularMapMaterialPrivate20handleAmbientChangedERK8QVariant(
    Qt3DExtras::QNormalDiffuseSpecularMapMaterialPrivate *self,
    const QVariant *var) {
  self->handleAmbientChanged(*var);
}

//  void Qt3DExtras::QNormalDiffuseSpecularMapMaterialPrivate::handleDiffuseC
//      hanged(const QVariant &var)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras40QNormalDiffuseSpecularMapMaterialPrivate20handleDiffuseChangedERK8QVariant(
    Qt3DExtras::QNormalDiffuseSpecularMapMaterialPrivate *self,
    const QVariant *var) {
  self->handleDiffuseChanged(*var);
}

//  void Qt3DExtras::QNormalDiffuseSpecularMapMaterialPrivate::handleNormalCh
//      anged(const QVariant &var)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras40QNormalDiffuseSpecularMapMaterialPrivate19handleNormalChangedERK8QVariant(
    Qt3DExtras::QNormalDiffuseSpecularMapMaterialPrivate *self,
    const QVariant *var) {
  self->handleNormalChanged(*var);
}

//  void Qt3DExtras::QNormalDiffuseSpecularMapMaterialPrivate::handleSpecular
//      Changed(const QVariant &var)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras40QNormalDiffuseSpecularMapMaterialPrivate21handleSpecularChangedERK8QVariant(
    Qt3DExtras::QNormalDiffuseSpecularMapMaterialPrivate *self,
    const QVariant *var) {
  self->handleSpecularChanged(*var);
}

//  void Qt3DExtras::QNormalDiffuseSpecularMapMaterialPrivate::handleShinines
//      sChanged(const QVariant &var)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras40QNormalDiffuseSpecularMapMaterialPrivate22handleShininessChangedERK8QVariant(
    Qt3DExtras::QNormalDiffuseSpecularMapMaterialPrivate *self,
    const QVariant *var) {
  self->handleShininessChanged(*var);
}

//  void Qt3DExtras::QNormalDiffuseSpecularMapMaterialPrivate::handleTextureS
//      caleChanged(const QVariant &var)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras40QNormalDiffuseSpecularMapMaterialPrivate25handleTextureScaleChangedERK8QVariant(
    Qt3DExtras::QNormalDiffuseSpecularMapMaterialPrivate *self,
    const QVariant *var) {
  self->handleTextureScaleChanged(*var);
}

//  QNormalDiffuseSpecularMapMaterial
//      *Qt3DExtras::QNormalDiffuseSpecularMapMaterialPrivate::q_func()
extern "C" Q_DECL_EXPORT
Qt3DExtras::QNormalDiffuseSpecularMapMaterial *ritual_ZN10Qt3DExtras40QNormalDiffuseSpecularMapMaterialPrivate6q_funcEv(
    Qt3DExtras::QNormalDiffuseSpecularMapMaterialPrivate *self) {
  return self->q_func();
}

//  const QNormalDiffuseSpecularMapMaterial
//      *Qt3DExtras::QNormalDiffuseSpecularMapMaterialPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const Qt3DExtras::QNormalDiffuseSpecularMapMaterial *ritual_ZNK10Qt3DExtras40QNormalDiffuseSpecularMapMaterialPrivate6q_funcEv(
    const Qt3DExtras::QNormalDiffuseSpecularMapMaterialPrivate *self) {
  return self->q_func();
}

//  a Python function taken by a
//      CuteQt3DExtras_QNormalDiffuseSpecularMapMaterialPrivate, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DExtras_QNormalDiffuseSpecularMapMaterialPrivate(
    Qt3DExtras::QNormalDiffuseSpecularMapMaterialPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DExtras_QNormalDiffuseSpecularMapMaterialPrivate *>(self)->take(key, call);
}
