//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/6.12.0/Qt3DRender/private/qshadergraphloader_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <Qt3DRender/6.12.0/Qt3DRender/private/qt3drender_global_p.h>
#include <Qt3DRender/Qt3DRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DRender/6.12.0/Qt3DRender/private/qshadergraphloader_p.h>
#include <Qt3DRender/6.12.0/Qt3DRender/private/qshadergraph_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/QHash>
#include <QtCore/QString>

//  Qt3DRender::QShaderGraphLoader::QShaderGraphLoader()
extern "C" Q_DECL_EXPORT
Qt3DRender::QShaderGraphLoader *ritual_ZN10Qt3DRender18QShaderGraphLoaderC1Ev() {
  return new Qt3DRender::QShaderGraphLoader();
}

//  Status Qt3DRender::QShaderGraphLoader::status() const
extern "C" Q_DECL_EXPORT
Qt3DRender::QShaderGraphLoader::Status ritual_ZNK10Qt3DRender18QShaderGraphLoader6statusEv(
    const Qt3DRender::QShaderGraphLoader *self) {
  return self->status();
}

//  QShaderGraph Qt3DRender::QShaderGraphLoader::graph() const
extern "C" Q_DECL_EXPORT
Qt3DRender::QShaderGraph *ritual_ZNK10Qt3DRender18QShaderGraphLoader5graphEv(
    const Qt3DRender::QShaderGraphLoader *self) {
  return new Qt3DRender::QShaderGraph(self->graph());
}

//  QIODevice *Qt3DRender::QShaderGraphLoader::device() const
extern "C" Q_DECL_EXPORT
QIODevice *ritual_ZNK10Qt3DRender18QShaderGraphLoader6deviceEv(
    const Qt3DRender::QShaderGraphLoader *self) {
  return self->device();
}

//  void Qt3DRender::QShaderGraphLoader::setDevice(QIODevice *device)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender18QShaderGraphLoader9setDeviceEP9QIODevice(
    Qt3DRender::QShaderGraphLoader *self,
    QIODevice *device) {
  self->setDevice(device);
}

//  QHash<QString, QShaderNode> Qt3DRender::QShaderGraphLoader::prototypes()
//      const
extern "C" Q_DECL_EXPORT
QHash<QString, Qt3DRender::QShaderNode> *ritual_ZNK10Qt3DRender18QShaderGraphLoader10prototypesEv(
    const Qt3DRender::QShaderGraphLoader *self) {
  return new QHash<QString, Qt3DRender::QShaderNode>(self->prototypes());
}

//  void Qt3DRender::QShaderGraphLoader::setPrototypes(const QHash<QString,
//      QShaderNode> &prototypes)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender18QShaderGraphLoader13setPrototypesERK5QHashI7QStringNS_11QShaderNodeEE(
    Qt3DRender::QShaderGraphLoader *self,
    const QHash<QString, Qt3DRender::QShaderNode> *prototypes) {
  self->setPrototypes(*prototypes);
}

//  void Qt3DRender::QShaderGraphLoader::load()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender18QShaderGraphLoader4loadEv(
    Qt3DRender::QShaderGraphLoader *self) {
  self->load();
}

//  Qt3DRender::QShaderGraphLoader::~QShaderGraphLoader()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender18QShaderGraphLoaderD1Ev(
    Qt3DRender::QShaderGraphLoader *self) {
  delete self;
}

//  a QHash<QString, Qt3DRender::QShaderNode> a ritual of
//      Qt3DRender::QShaderGraphLoader gave
extern "C" Q_DECL_EXPORT
void ritual_drop_Qt3DRender_QShaderGraphLoader__QHash_QString_Qt3DRender_QShaderNode(
    QHash<QString, Qt3DRender::QShaderNode> *self) {
  delete self;
}
