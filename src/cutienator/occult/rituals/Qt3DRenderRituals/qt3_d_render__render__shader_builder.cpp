//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/6.12.0/Qt3DRender/private/shaderbuilder_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <Qt3DRender/6.12.0/Qt3DRender/private/qt3drender_global_p.h>
#include <Qt3DRender/Qt3DRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DRender/6.12.0/Qt3DRender/private/shaderbuilder_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <Qt3DCore/qnodeid.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DRender/6.12.0/Qt3DRender/private/qgraphicsapifilter_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qurl.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qlist.h>
#include <cstring>
#include <vector>

//  A Qt3DRender::Render::ShaderBuilder that Python can take functions over in. Every Qt3DRender::Render::ShaderBuilder
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQt3DRender_Render_ShaderBuilderCall0)(const void *, const Qt3DCore::QNode *, bool, int *);
class CuteQt3DRender_Render_ShaderBuilder : public Qt3DRender::Render::ShaderBuilder {
public:
  using Qt3DRender::Render::ShaderBuilder::ShaderBuilder;
  void *taken[1] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN8Qt3DCore12QBackendNode16syncFromFrontEndEPKNS_5QNodeEb")) {
      taken[0] = call;
      return true;
    }
    return false;
  }

  //  void Qt3DRender::Render::ShaderBuilder::syncFromFrontEnd(const
  //      Qt3DCore::QNode *frontEnd, bool firstTime)
  void syncFromFrontEnd(
      const Qt3DCore::QNode *frontEnd,
      bool firstTime) override {
    if (taken[0]) {
      int handled = 0;
      CuteQt3DRender_Render_ShaderBuilderCall0 call = reinterpret_cast<CuteQt3DRender_Render_ShaderBuilderCall0>(taken[0]);
      call(this, frontEnd, firstTime, &handled);
      if (handled) return;
    }
    Qt3DRender::Render::ShaderBuilder::syncFromFrontEnd(frontEnd, firstTime);
  }
};

//  QString Qt3DRender::Render::ShaderBuilder::getPrototypesFile()
extern "C" Q_DECL_EXPORT
QString *ritual_ZN10Qt3DRender6Render13ShaderBuilder17getPrototypesFileEv() {
  return new QString(Qt3DRender::Render::ShaderBuilder::getPrototypesFile());
}

//  void Qt3DRender::Render::ShaderBuilder::setPrototypesFile(const QString
//      &file)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render13ShaderBuilder17setPrototypesFileERK7QString(
    const QString *file) {
  Qt3DRender::Render::ShaderBuilder::setPrototypesFile(*file);
}

//  QStringList Qt3DRender::Render::ShaderBuilder::getPrototypeNames()
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZN10Qt3DRender6Render13ShaderBuilder17getPrototypeNamesEv() {
  return new QList<QString>(
      Qt3DRender::Render::ShaderBuilder::getPrototypeNames());
}

//  Qt3DRender::Render::ShaderBuilder::ShaderBuilder()
extern "C" Q_DECL_EXPORT
Qt3DRender::Render::ShaderBuilder *ritual_ZN10Qt3DRender6Render13ShaderBuilderC1Ev() {
  return new CuteQt3DRender_Render_ShaderBuilder();
}

//  Qt3DRender::Render::ShaderBuilder::~ShaderBuilder()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render13ShaderBuilderD1Ev(
    Qt3DRender::Render::ShaderBuilder *self) {
  delete self;
}

//  void Qt3DRender::Render::ShaderBuilder::cleanup()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render13ShaderBuilder7cleanupEv(
    Qt3DRender::Render::ShaderBuilder *self) {
  self->cleanup();
}

//  Qt3DCore::QNodeId Qt3DRender::Render::ShaderBuilder::shaderProgramId()
//      const
extern "C" Q_DECL_EXPORT
Qt3DCore::QNodeId *ritual_ZNK10Qt3DRender6Render13ShaderBuilder15shaderProgramIdEv(
    const Qt3DRender::Render::ShaderBuilder *self) {
  return new Qt3DCore::QNodeId(self->shaderProgramId());
}

//  QStringList Qt3DRender::Render::ShaderBuilder::enabledLayers() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK10Qt3DRender6Render13ShaderBuilder13enabledLayersEv(
    const Qt3DRender::Render::ShaderBuilder *self) {
  return new QList<QString>(self->enabledLayers());
}

//  GraphicsApiFilterData Qt3DRender::Render::ShaderBuilder::graphicsApi()
//      const
extern "C" Q_DECL_EXPORT
Qt3DRender::GraphicsApiFilterData *ritual_ZNK10Qt3DRender6Render13ShaderBuilder11graphicsApiEv(
    const Qt3DRender::Render::ShaderBuilder *self) {
  return new Qt3DRender::GraphicsApiFilterData(self->graphicsApi());
}

//  void Qt3DRender::Render::ShaderBuilder::setGraphicsApi(const
//      GraphicsApiFilterData &graphicsApi)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render13ShaderBuilder14setGraphicsApiERKNS_21GraphicsApiFilterDataE(
    Qt3DRender::Render::ShaderBuilder *self,
    const Qt3DRender::GraphicsApiFilterData *graphicsApi) {
  self->setGraphicsApi(*graphicsApi);
}

//  QUrl
//      Qt3DRender::Render::ShaderBuilder::shaderGraph(QShaderProgram::Shader
//      Type type) const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK10Qt3DRender6Render13ShaderBuilder11shaderGraphENS_14QShaderProgram10ShaderTypeE(
    const Qt3DRender::Render::ShaderBuilder *self,
    Qt3DRender::QShaderProgram::ShaderType type) {
  return new QUrl(self->shaderGraph(type));
}

//  void Qt3DRender::Render::ShaderBuilder::setShaderGraph(QShaderProgram::Sh
//      aderType type, const QUrl &url)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render13ShaderBuilder14setShaderGraphENS_14QShaderProgram10ShaderTypeERK4QUrl(
    Qt3DRender::Render::ShaderBuilder *self,
    Qt3DRender::QShaderProgram::ShaderType type,
    const QUrl *url) {
  self->setShaderGraph(type, *url);
}

//  QByteArray
//      Qt3DRender::Render::ShaderBuilder::shaderCode(QShaderProgram::ShaderT
//      ype type) const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK10Qt3DRender6Render13ShaderBuilder10shaderCodeENS_14QShaderProgram10ShaderTypeE(
    const Qt3DRender::Render::ShaderBuilder *self,
    Qt3DRender::QShaderProgram::ShaderType type) {
  return new QByteArray(self->shaderCode(type));
}

//  bool Qt3DRender::Render::ShaderBuilder::isShaderCodeDirty(QShaderProgram:
//      :ShaderType type) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10Qt3DRender6Render13ShaderBuilder17isShaderCodeDirtyENS_14QShaderProgram10ShaderTypeE(
    const Qt3DRender::Render::ShaderBuilder *self,
    Qt3DRender::QShaderProgram::ShaderType type) {
  return self->isShaderCodeDirty(type);
}

//  void Qt3DRender::Render::ShaderBuilder::generateCode(QShaderProgram::Shad
//      erType type)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render13ShaderBuilder12generateCodeENS_14QShaderProgram10ShaderTypeE(
    Qt3DRender::Render::ShaderBuilder *self,
    Qt3DRender::QShaderProgram::ShaderType type) {
  self->generateCode(type);
}

//  void Qt3DRender::Render::ShaderBuilder::syncFromFrontEnd(const
//      Qt3DCore::QNode *frontEnd, bool firstTime)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render13ShaderBuilder16syncFromFrontEndEPKN8Qt3DCore5QNodeEb(
    Qt3DRender::Render::ShaderBuilder *self,
    const Qt3DCore::QNode *frontEnd,
    bool firstTime) {
  self->syncFromFrontEnd(frontEnd, firstTime);
}

//  std::vector<ShaderBuilderUpdate>
//      Qt3DRender::Render::ShaderBuilder::takePendingUpdates()
extern "C" Q_DECL_EXPORT
std::vector<Qt3DRender::Render::ShaderBuilderUpdate> *ritual_ZN10Qt3DRender6Render13ShaderBuilder18takePendingUpdatesEv(
    Qt3DRender::Render::ShaderBuilder *self) {
  return new std::vector<Qt3DRender::Render::ShaderBuilderUpdate>(
      self->takePendingUpdates());
}

//  QByteArray Qt3DRender::Render::ShaderBuilder::hashKeyForShaderGraph(QShad
//      erProgram::ShaderType type) const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK10Qt3DRender6Render13ShaderBuilder21hashKeyForShaderGraphENS_14QShaderProgram10ShaderTypeE(
    const Qt3DRender::Render::ShaderBuilder *self,
    Qt3DRender::QShaderProgram::ShaderType type) {
  return new QByteArray(self->hashKeyForShaderGraph(type));
}

//  void Qt3DRender::Render::ShaderBuilder::setEnabledLayers(const
//      QStringList &layers)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render13ShaderBuilder16setEnabledLayersERK5QListI7QStringE(
    Qt3DRender::Render::ShaderBuilder *self,
    const QList<QString> *layers) {
  self->setEnabledLayers(*layers);
}

//  a Python function taken by a CuteQt3DRender_Render_ShaderBuilder, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DRender_Render_ShaderBuilder(
    Qt3DRender::Render::ShaderBuilder *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DRender_Render_ShaderBuilder *>(self)->take(key, call);
}

//  void Qt3DRender::Render::ShaderBuilder::syncFromFrontEnd(const
//      Qt3DCore::QNode *frontEnd, bool firstTime)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10Qt3DRender6Render13ShaderBuilder16syncFromFrontEndEPKN8Qt3DCore5QNodeEb(
    Qt3DRender::Render::ShaderBuilder *self,
    const Qt3DCore::QNode *frontEnd,
    bool firstTime) {
  self->Qt3DRender::Render::ShaderBuilder::syncFromFrontEnd(
      frontEnd,
      firstTime);
}

//  a std::vector<Qt3DRender::Render::ShaderBuilderUpdate> a ritual of
//      Qt3DRender::Render::ShaderBuilder gave
extern "C" Q_DECL_EXPORT
void ritual_drop_Qt3DRender_Render_ShaderBuilder__std_vector_Qt3DRender_Render_ShaderBuilderUpdate(
    std::vector<Qt3DRender::Render::ShaderBuilderUpdate> *self) {
  delete self;
}
