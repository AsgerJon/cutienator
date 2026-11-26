//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DExtras/6.12.0/Qt3DExtras/private/qpervertexcolormaterial_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <Qt3DExtras/Qt3DExtras>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DExtras/6.12.0/Qt3DExtras/private/qpervertexcolormaterial_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DExtras/qpervertexcolormaterial.h>
#include <Qt3DExtras/private/qpervertexcolormaterial_p.h>
#include <Qt3DRender/qfilterkey.h>
#include <Qt3DRender/qmaterial.h>
#include <Qt3DRender/qeffect.h>
#include <Qt3DRender/qtechnique.h>
#include <Qt3DRender/qshaderprogram.h>
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

//  from ../qt3d/src/extras/defaults/qpervertexcolormaterial.cpp, line 25, as _ZN10Qt3DExtras30QPerVertexColorMaterialPrivateC1Ev
namespace Qt3DExtras {
using namespace Qt3DRender;
inline QPerVertexColorMaterialPrivate::QPerVertexColorMaterialPrivate()
    : QMaterialPrivate()
    , m_vertexEffect(new QEffect())
    , m_vertexGL3Technique(new QTechnique())
    , m_vertexGL2Technique(new QTechnique())
    , m_vertexES2Technique(new QTechnique())
    , m_vertexRHITechnique(new QTechnique())
    , m_vertexGL3RenderPass(new QRenderPass())
    , m_vertexGL2RenderPass(new QRenderPass())
    , m_vertexES2RenderPass(new QRenderPass())
    , m_vertexRHIRenderPass(new QRenderPass())
    , m_vertexGL3Shader(new QShaderProgram())
    , m_vertexGL2ES2Shader(new QShaderProgram())
    , m_vertexRHIShader(new QShaderProgram())
    , m_filterKey(new QFilterKey)
{
}
}  // namespace Qt3DExtras

//  from ../qt3d/src/extras/defaults/qpervertexcolormaterial.cpp, line 83, as _ZN10Qt3DExtras30QPerVertexColorMaterialPrivate4initEv
namespace Qt3DExtras {
using namespace Qt3DRender;
inline void QPerVertexColorMaterialPrivate::init()
{
    m_vertexGL3Shader->setVertexShaderCode(QShaderProgram::loadSource(QUrl(QStringLiteral("qrc:/shaders/gl3/pervertexcolor.vert"))));
    m_vertexGL3Shader->setFragmentShaderCode(QShaderProgram::loadSource(QUrl(QStringLiteral("qrc:/shaders/gl3/pervertexcolor.frag"))));
    m_vertexGL2ES2Shader->setVertexShaderCode(QShaderProgram::loadSource(QUrl(QStringLiteral("qrc:/shaders/es2/pervertexcolor.vert"))));
    m_vertexGL2ES2Shader->setFragmentShaderCode(QShaderProgram::loadSource(QUrl(QStringLiteral("qrc:/shaders/es2/pervertexcolor.frag"))));
    m_vertexRHIShader->setVertexShaderCode(QShaderProgram::loadSource(QUrl(QStringLiteral("qrc:/shaders/rhi/pervertexcolor.vert"))));
    m_vertexRHIShader->setFragmentShaderCode(QShaderProgram::loadSource(QUrl(QStringLiteral("qrc:/shaders/rhi/pervertexcolor.frag"))));

    m_vertexGL3Technique->graphicsApiFilter()->setApi(QGraphicsApiFilter::OpenGL);
    m_vertexGL3Technique->graphicsApiFilter()->setMajorVersion(3);
    m_vertexGL3Technique->graphicsApiFilter()->setMinorVersion(1);
    m_vertexGL3Technique->graphicsApiFilter()->setProfile(QGraphicsApiFilter::CoreProfile);

    m_vertexGL2Technique->graphicsApiFilter()->setApi(QGraphicsApiFilter::OpenGL);
    m_vertexGL2Technique->graphicsApiFilter()->setMajorVersion(2);
    m_vertexGL2Technique->graphicsApiFilter()->setMinorVersion(0);
    m_vertexGL2Technique->graphicsApiFilter()->setProfile(QGraphicsApiFilter::NoProfile);

    m_vertexES2Technique->graphicsApiFilter()->setApi(QGraphicsApiFilter::OpenGLES);
    m_vertexES2Technique->graphicsApiFilter()->setMajorVersion(2);
    m_vertexES2Technique->graphicsApiFilter()->setMinorVersion(0);
    m_vertexES2Technique->graphicsApiFilter()->setProfile(QGraphicsApiFilter::NoProfile);

    m_vertexRHITechnique->graphicsApiFilter()->setApi(QGraphicsApiFilter::RHI);
    m_vertexRHITechnique->graphicsApiFilter()->setMajorVersion(1);
    m_vertexRHITechnique->graphicsApiFilter()->setMinorVersion(0);

    Q_Q(QPerVertexColorMaterial);
    m_filterKey->setParent(q);
    m_filterKey->setName(QStringLiteral("renderingStyle"));
    m_filterKey->setValue(QStringLiteral("forward"));

    m_vertexGL3Technique->addFilterKey(m_filterKey);
    m_vertexGL2Technique->addFilterKey(m_filterKey);
    m_vertexES2Technique->addFilterKey(m_filterKey);
    m_vertexRHITechnique->addFilterKey(m_filterKey);

    m_vertexGL3RenderPass->setShaderProgram(m_vertexGL3Shader);
    m_vertexGL2RenderPass->setShaderProgram(m_vertexGL2ES2Shader);
    m_vertexES2RenderPass->setShaderProgram(m_vertexGL2ES2Shader);
    m_vertexRHIRenderPass->setShaderProgram(m_vertexRHIShader);

    m_vertexGL3Technique->addRenderPass(m_vertexGL3RenderPass);
    m_vertexGL2Technique->addRenderPass(m_vertexGL2RenderPass);
    m_vertexES2Technique->addRenderPass(m_vertexES2RenderPass);
    m_vertexRHITechnique->addRenderPass(m_vertexRHIRenderPass);

    m_vertexEffect->addTechnique(m_vertexGL3Technique);
    m_vertexEffect->addTechnique(m_vertexGL2Technique);
    m_vertexEffect->addTechnique(m_vertexES2Technique);
    m_vertexEffect->addTechnique(m_vertexRHITechnique);

    q->setEffect(m_vertexEffect);
}
}  // namespace Qt3DExtras
//  -----------------------------------------------------------------------

//  A Qt3DExtras::QPerVertexColorMaterialPrivate that Python can take functions over in. Every Qt3DExtras::QPerVertexColorMaterialPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQt3DExtras_QPerVertexColorMaterialPrivateCall0)(const void *, Qt3DCore::QScene *, int *);
typedef void (*CuteQt3DExtras_QPerVertexColorMaterialPrivateCall1)(const void *, int *);
class CuteQt3DExtras_QPerVertexColorMaterialPrivate : public Qt3DExtras::QPerVertexColorMaterialPrivate {
public:
  using Qt3DExtras::QPerVertexColorMaterialPrivate::QPerVertexColorMaterialPrivate;
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
      CuteQt3DExtras_QPerVertexColorMaterialPrivateCall0 call = reinterpret_cast<CuteQt3DExtras_QPerVertexColorMaterialPrivateCall0>(taken[0]);
      call(this, scene, &handled);
      if (handled) return;
    }
    Qt3DCore::QNodePrivate::setScene(scene);
  }

  //  void Qt3DCore::QNodePrivate::update()
  void update() override {
    if (taken[1]) {
      int handled = 0;
      CuteQt3DExtras_QPerVertexColorMaterialPrivateCall1 call = reinterpret_cast<CuteQt3DExtras_QPerVertexColorMaterialPrivateCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    Qt3DCore::QNodePrivate::update();
  }
};

//  Qt3DExtras::QPerVertexColorMaterialPrivate::QPerVertexColorMaterialPrivat
//      e()
extern "C" Q_DECL_EXPORT
Qt3DExtras::QPerVertexColorMaterialPrivate *ritual_ZN10Qt3DExtras30QPerVertexColorMaterialPrivateC1Ev() {
  return new CuteQt3DExtras_QPerVertexColorMaterialPrivate();
}

//  void Qt3DExtras::QPerVertexColorMaterialPrivate::init()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras30QPerVertexColorMaterialPrivate4initEv(
    Qt3DExtras::QPerVertexColorMaterialPrivate *self) {
  self->init();
}

//  QPerVertexColorMaterial
//      *Qt3DExtras::QPerVertexColorMaterialPrivate::q_func()
extern "C" Q_DECL_EXPORT
Qt3DExtras::QPerVertexColorMaterial *ritual_ZN10Qt3DExtras30QPerVertexColorMaterialPrivate6q_funcEv(
    Qt3DExtras::QPerVertexColorMaterialPrivate *self) {
  return self->q_func();
}

//  const QPerVertexColorMaterial
//      *Qt3DExtras::QPerVertexColorMaterialPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const Qt3DExtras::QPerVertexColorMaterial *ritual_ZNK10Qt3DExtras30QPerVertexColorMaterialPrivate6q_funcEv(
    const Qt3DExtras::QPerVertexColorMaterialPrivate *self) {
  return self->q_func();
}

//  a Python function taken by a
//      CuteQt3DExtras_QPerVertexColorMaterialPrivate, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DExtras_QPerVertexColorMaterialPrivate(
    Qt3DExtras::QPerVertexColorMaterialPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DExtras_QPerVertexColorMaterialPrivate *>(self)->take(key, call);
}
