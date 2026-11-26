//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DExtras/6.12.0/Qt3DExtras/private/qmetalroughmaterial_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <Qt3DExtras/Qt3DExtras>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DExtras/6.12.0/Qt3DExtras/private/qmetalroughmaterial_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qvariant.h>
#include <QtCore/qstring.h>
#include <QtCore/qlist.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DExtras/qmetalroughmaterial.h>
#include <Qt3DExtras/private/qmetalroughmaterial_p.h>
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

//  from ../qt3d/src/extras/defaults/qmetalroughmaterial.cpp, line 26, as _ZN10Qt3DExtras26QMetalRoughMaterialPrivateC1Ev
namespace Qt3DExtras {
using namespace Qt3DRender;
inline QMetalRoughMaterialPrivate::QMetalRoughMaterialPrivate()
    : QMaterialPrivate()
    , m_baseColorParameter(new QParameter(QStringLiteral("baseColor"), QColor::fromString("grey")))
    , m_metalnessParameter(new QParameter(QStringLiteral("metalness"), 0.0f))
    , m_roughnessParameter(new QParameter(QStringLiteral("roughness"), 0.0f))
    , m_baseColorMapParameter(new QParameter(QStringLiteral("baseColorMap"), QVariant()))
    , m_metalnessMapParameter(new QParameter(QStringLiteral("metalnessMap"), QVariant()))
    , m_roughnessMapParameter(new QParameter(QStringLiteral("roughnessMap"), QVariant()))
    , m_ambientOcclusionMapParameter(new QParameter(QStringLiteral("ambientOcclusionMap"), QVariant()))
    , m_normalMapParameter(new QParameter(QStringLiteral("normalMap"), QVariant()))
    , m_textureScaleParameter(new QParameter(QStringLiteral("texCoordScale"), 1.0f))
    , m_metalRoughEffect(new QEffect())
    , m_metalRoughGL3Technique(new QTechnique())
    , m_metalRoughGL3RenderPass(new QRenderPass())
    , m_metalRoughGL3Shader(new QShaderProgram())
    , m_metalRoughGL3ShaderBuilder(new QShaderProgramBuilder())
    , m_metalRoughES3Technique(new QTechnique())
    , m_metalRoughES3RenderPass(new QRenderPass())
    , m_metalRoughES3Shader(new QShaderProgram())
    , m_metalRoughES3ShaderBuilder(new QShaderProgramBuilder())
    , m_metalRoughRHITechnique(new QTechnique())
    , m_metalRoughRHIRenderPass(new QRenderPass())
    , m_metalRoughRHIShader(new QShaderProgram())
    , m_metalRoughRHIShaderBuilder(new QShaderProgramBuilder())
    , m_filterKey(new QFilterKey)
{
}
}  // namespace Qt3DExtras

//  from ../qt3d/src/extras/defaults/qmetalroughmaterial.cpp, line 54, as _ZN10Qt3DExtras26QMetalRoughMaterialPrivate4initEv
namespace Qt3DExtras {
using namespace Qt3DRender;
inline void QMetalRoughMaterialPrivate::init()
{
    Q_Q(QMetalRoughMaterial);

    QObject::connect(m_baseColorParameter, &Qt3DRender::QParameter::valueChanged,
                     q, &QMetalRoughMaterial::baseColorChanged);
    QObject::connect(m_metalnessParameter, &Qt3DRender::QParameter::valueChanged,
                     q, &QMetalRoughMaterial::metalnessChanged);
    QObject::connect(m_roughnessParameter, &Qt3DRender::QParameter::valueChanged,
                     q, &QMetalRoughMaterial::roughnessChanged);
    QObject::connect(m_ambientOcclusionMapParameter, &Qt3DRender::QParameter::valueChanged,
                     q, &QMetalRoughMaterial::roughnessChanged);
    QObject::connect(m_normalMapParameter, &Qt3DRender::QParameter::valueChanged,
                     q, &QMetalRoughMaterial::normalChanged);
    connect(m_textureScaleParameter, &Qt3DRender::QParameter::valueChanged,
            this, &QMetalRoughMaterialPrivate::handleTextureScaleChanged);

    m_metalRoughGL3Shader->setVertexShaderCode(QShaderProgram::loadSource(QUrl(QStringLiteral("qrc:/shaders/gl3/default.vert"))));
    m_metalRoughGL3ShaderBuilder->setParent(q);
    m_metalRoughGL3ShaderBuilder->setShaderProgram(m_metalRoughGL3Shader);
    m_metalRoughGL3ShaderBuilder->setFragmentShaderGraph(QUrl(QStringLiteral("qrc:/shaders/graphs/metalrough.frag.json")));
    m_metalRoughGL3ShaderBuilder->setEnabledLayers({QStringLiteral("baseColor"),
                                                    QStringLiteral("metalness"),
                                                    QStringLiteral("roughness"),
                                                    QStringLiteral("ambientOcclusion"),
                                                    QStringLiteral("normal")});

    m_metalRoughES3Shader->setVertexShaderCode(QShaderProgram::loadSource(QUrl(QStringLiteral("qrc:/shaders/es3/default.vert"))));
    m_metalRoughES3ShaderBuilder->setParent(q);
    m_metalRoughES3ShaderBuilder->setShaderProgram(m_metalRoughES3Shader);
    m_metalRoughES3ShaderBuilder->setFragmentShaderGraph(QUrl(QStringLiteral("qrc:/shaders/graphs/metalrough.frag.json")));
    m_metalRoughES3ShaderBuilder->setEnabledLayers({QStringLiteral("baseColor"),
                                                    QStringLiteral("metalness"),
                                                    QStringLiteral("roughness"),
                                                    QStringLiteral("ambientOcclusion"),
                                                    QStringLiteral("normal")});

    m_metalRoughRHIShader->setVertexShaderCode(QShaderProgram::loadSource(QUrl(QStringLiteral("qrc:/shaders/rhi/default_pos_norm.vert"))));
    m_metalRoughRHIShaderBuilder->setParent(q);
    m_metalRoughRHIShaderBuilder->setShaderProgram(m_metalRoughRHIShader);
    m_metalRoughRHIShaderBuilder->setFragmentShaderGraph(QUrl(QStringLiteral("qrc:/shaders/graphs/metalrough.frag.json")));
    m_metalRoughRHIShaderBuilder->setEnabledLayers({QStringLiteral("baseColor"),
                                                    QStringLiteral("metalness"),
                                                    QStringLiteral("roughness"),
                                                    QStringLiteral("ambientOcclusion"),
                                                    QStringLiteral("normal")});

    m_metalRoughGL3Technique->graphicsApiFilter()->setApi(QGraphicsApiFilter::OpenGL);
    m_metalRoughGL3Technique->graphicsApiFilter()->setMajorVersion(3);
    m_metalRoughGL3Technique->graphicsApiFilter()->setMinorVersion(1);
    m_metalRoughGL3Technique->graphicsApiFilter()->setProfile(QGraphicsApiFilter::CoreProfile);

    m_metalRoughES3Technique->graphicsApiFilter()->setApi(QGraphicsApiFilter::OpenGLES);
    m_metalRoughES3Technique->graphicsApiFilter()->setMajorVersion(3);
    m_metalRoughES3Technique->graphicsApiFilter()->setMinorVersion(0);

    m_metalRoughRHITechnique->graphicsApiFilter()->setApi(QGraphicsApiFilter::RHI);
    m_metalRoughRHITechnique->graphicsApiFilter()->setMajorVersion(1);
    m_metalRoughRHITechnique->graphicsApiFilter()->setMinorVersion(0);

    m_filterKey->setParent(q);
    m_filterKey->setName(QStringLiteral("renderingStyle"));
    m_filterKey->setValue(QStringLiteral("forward"));

    m_metalRoughGL3Technique->addFilterKey(m_filterKey);
    m_metalRoughGL3RenderPass->setShaderProgram(m_metalRoughGL3Shader);
    m_metalRoughGL3Technique->addRenderPass(m_metalRoughGL3RenderPass);
    m_metalRoughEffect->addTechnique(m_metalRoughGL3Technique);

    m_metalRoughES3Technique->addFilterKey(m_filterKey);
    m_metalRoughES3RenderPass->setShaderProgram(m_metalRoughES3Shader);
    m_metalRoughES3Technique->addRenderPass(m_metalRoughES3RenderPass);
    m_metalRoughEffect->addTechnique(m_metalRoughES3Technique);

    m_metalRoughRHITechnique->addFilterKey(m_filterKey);
    m_metalRoughRHIRenderPass->setShaderProgram(m_metalRoughRHIShader);
    m_metalRoughRHITechnique->addRenderPass(m_metalRoughRHIRenderPass);
    m_metalRoughEffect->addTechnique(m_metalRoughRHITechnique);

    // Given parameters a parent
    m_baseColorMapParameter->setParent(m_metalRoughEffect);
    m_metalnessMapParameter->setParent(m_metalRoughEffect);
    m_roughnessMapParameter->setParent(m_metalRoughEffect);

    m_metalRoughEffect->addParameter(m_baseColorParameter);
    m_metalRoughEffect->addParameter(m_metalnessParameter);
    m_metalRoughEffect->addParameter(m_roughnessParameter);
    m_metalRoughEffect->addParameter(m_textureScaleParameter);

    q->setEffect(m_metalRoughEffect);
}
}  // namespace Qt3DExtras

//  from ../qt3d/src/extras/defaults/qmetalroughmaterial.cpp, line 146, as _ZN10Qt3DExtras26QMetalRoughMaterialPrivate25handleTextureScaleChangedERK8QVariant
namespace Qt3DExtras {
using namespace Qt3DRender;
inline void QMetalRoughMaterialPrivate::handleTextureScaleChanged(const QVariant &var)
{
    Q_Q(QMetalRoughMaterial);
    emit q->textureScaleChanged(var.toFloat());
}
}  // namespace Qt3DExtras

//  from ../qt3d/src/extras/defaults/qmetalroughmaterial.cpp, line 152, as _ZN10Qt3DExtras26QMetalRoughMaterialPrivate23updateLayersOnTechniqueERK5QListI7QStringE
namespace Qt3DExtras {
using namespace Qt3DRender;
inline void QMetalRoughMaterialPrivate::updateLayersOnTechnique(const QStringList &layers)
{
    m_metalRoughGL3ShaderBuilder->setEnabledLayers(layers);
    m_metalRoughES3ShaderBuilder->setEnabledLayers(layers);
    m_metalRoughRHIShaderBuilder->setEnabledLayers(layers);
    updateVertexShaderBasedOnLayers(layers);
}
}  // namespace Qt3DExtras

//  from ../qt3d/src/extras/defaults/qmetalroughmaterial.cpp, line 160, as _ZN10Qt3DExtras26QMetalRoughMaterialPrivate31updateVertexShaderBasedOnLayersERK5QListI7QStringE
namespace Qt3DExtras {
using namespace Qt3DRender;
inline void QMetalRoughMaterialPrivate::updateVertexShaderBasedOnLayers(const QStringList &layers)
{
    const QString mapsLayers[] = {
        QStringLiteral("baseColorMap"),
        QStringLiteral("metalnessMap"),
        QStringLiteral("roughnessMap"),
        QStringLiteral("ambientOcclusionMap"),
        QStringLiteral("normalMap")
    };

    const bool needsTexCoords = std::any_of(std::cbegin(mapsLayers),
                                            std::cend(mapsLayers),
                                            [&] (const QString &mapLayers) { return layers.contains(mapLayers); });
    const bool needsTangents = layers.contains(QStringLiteral("normalMap"));

    QString vertexShader = QLatin1String("default_pos_norm");

    if (needsTexCoords)
        vertexShader += QLatin1String("_tex");
    if (needsTangents)
        vertexShader += QLatin1String("_tan");

    m_metalRoughRHIShader->setVertexShaderCode(QShaderProgram::loadSource(QUrl(QLatin1String("qrc:/shaders/rhi/%1.vert").arg(vertexShader))));
}
}  // namespace Qt3DExtras
//  -----------------------------------------------------------------------

//  A Qt3DExtras::QMetalRoughMaterialPrivate that Python can take functions over in. Every Qt3DExtras::QMetalRoughMaterialPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQt3DExtras_QMetalRoughMaterialPrivateCall0)(const void *, Qt3DCore::QScene *, int *);
typedef void (*CuteQt3DExtras_QMetalRoughMaterialPrivateCall1)(const void *, int *);
class CuteQt3DExtras_QMetalRoughMaterialPrivate : public Qt3DExtras::QMetalRoughMaterialPrivate {
public:
  using Qt3DExtras::QMetalRoughMaterialPrivate::QMetalRoughMaterialPrivate;
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
      CuteQt3DExtras_QMetalRoughMaterialPrivateCall0 call = reinterpret_cast<CuteQt3DExtras_QMetalRoughMaterialPrivateCall0>(taken[0]);
      call(this, scene, &handled);
      if (handled) return;
    }
    Qt3DCore::QNodePrivate::setScene(scene);
  }

  //  void Qt3DCore::QNodePrivate::update()
  void update() override {
    if (taken[1]) {
      int handled = 0;
      CuteQt3DExtras_QMetalRoughMaterialPrivateCall1 call = reinterpret_cast<CuteQt3DExtras_QMetalRoughMaterialPrivateCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    Qt3DCore::QNodePrivate::update();
  }
};

//  Qt3DExtras::QMetalRoughMaterialPrivate::QMetalRoughMaterialPrivate()
extern "C" Q_DECL_EXPORT
Qt3DExtras::QMetalRoughMaterialPrivate *ritual_ZN10Qt3DExtras26QMetalRoughMaterialPrivateC1Ev() {
  return new CuteQt3DExtras_QMetalRoughMaterialPrivate();
}

//  void Qt3DExtras::QMetalRoughMaterialPrivate::init()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras26QMetalRoughMaterialPrivate4initEv(
    Qt3DExtras::QMetalRoughMaterialPrivate *self) {
  self->init();
}

//  void
//      Qt3DExtras::QMetalRoughMaterialPrivate::handleTextureScaleChanged(con
//      st QVariant &var)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras26QMetalRoughMaterialPrivate25handleTextureScaleChangedERK8QVariant(
    Qt3DExtras::QMetalRoughMaterialPrivate *self,
    const QVariant *var) {
  self->handleTextureScaleChanged(*var);
}

//  void
//      Qt3DExtras::QMetalRoughMaterialPrivate::updateLayersOnTechnique(const
//      QStringList &layers)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras26QMetalRoughMaterialPrivate23updateLayersOnTechniqueERK5QListI7QStringE(
    Qt3DExtras::QMetalRoughMaterialPrivate *self,
    const QList<QString> *layers) {
  self->updateLayersOnTechnique(*layers);
}

//  void Qt3DExtras::QMetalRoughMaterialPrivate::updateVertexShaderBasedOnLay
//      ers(const QStringList &layers)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras26QMetalRoughMaterialPrivate31updateVertexShaderBasedOnLayersERK5QListI7QStringE(
    Qt3DExtras::QMetalRoughMaterialPrivate *self,
    const QList<QString> *layers) {
  self->updateVertexShaderBasedOnLayers(*layers);
}

//  QMetalRoughMaterial *Qt3DExtras::QMetalRoughMaterialPrivate::q_func()
extern "C" Q_DECL_EXPORT
Qt3DExtras::QMetalRoughMaterial *ritual_ZN10Qt3DExtras26QMetalRoughMaterialPrivate6q_funcEv(
    Qt3DExtras::QMetalRoughMaterialPrivate *self) {
  return self->q_func();
}

//  const QMetalRoughMaterial
//      *Qt3DExtras::QMetalRoughMaterialPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const Qt3DExtras::QMetalRoughMaterial *ritual_ZNK10Qt3DExtras26QMetalRoughMaterialPrivate6q_funcEv(
    const Qt3DExtras::QMetalRoughMaterialPrivate *self) {
  return self->q_func();
}

//  a Python function taken by a CuteQt3DExtras_QMetalRoughMaterialPrivate,
//      for the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DExtras_QMetalRoughMaterialPrivate(
    Qt3DExtras::QMetalRoughMaterialPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DExtras_QMetalRoughMaterialPrivate *>(self)->take(key, call);
}
