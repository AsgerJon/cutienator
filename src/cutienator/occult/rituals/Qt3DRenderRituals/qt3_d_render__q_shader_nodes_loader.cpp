//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/6.12.0/Qt3DRender/private/qshadernodesloader_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <Qt3DRender/6.12.0/Qt3DRender/private/qt3drender_global_p.h>
#include <Qt3DRender/Qt3DRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DRender/6.12.0/Qt3DRender/private/qshadernodesloader_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qjsonobject.h>
#include <QtCore/QHash>
#include <QtCore/QString>

//  Qt3DRender::QShaderNodesLoader::QShaderNodesLoader()
extern "C" Q_DECL_EXPORT
Qt3DRender::QShaderNodesLoader *ritual_ZN10Qt3DRender18QShaderNodesLoaderC1Ev() {
  return new Qt3DRender::QShaderNodesLoader();
}

//  Status Qt3DRender::QShaderNodesLoader::status() const
extern "C" Q_DECL_EXPORT
Qt3DRender::QShaderNodesLoader::Status ritual_ZNK10Qt3DRender18QShaderNodesLoader6statusEv(
    const Qt3DRender::QShaderNodesLoader *self) {
  return self->status();
}

//  QHash<QString, QShaderNode> Qt3DRender::QShaderNodesLoader::nodes() const
extern "C" Q_DECL_EXPORT
QHash<QString, Qt3DRender::QShaderNode> *ritual_ZNK10Qt3DRender18QShaderNodesLoader5nodesEv(
    const Qt3DRender::QShaderNodesLoader *self) {
  return new QHash<QString, Qt3DRender::QShaderNode>(self->nodes());
}

//  QIODevice *Qt3DRender::QShaderNodesLoader::device() const
extern "C" Q_DECL_EXPORT
QIODevice *ritual_ZNK10Qt3DRender18QShaderNodesLoader6deviceEv(
    const Qt3DRender::QShaderNodesLoader *self) {
  return self->device();
}

//  void Qt3DRender::QShaderNodesLoader::setDevice(QIODevice *device)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender18QShaderNodesLoader9setDeviceEP9QIODevice(
    Qt3DRender::QShaderNodesLoader *self,
    QIODevice *device) {
  self->setDevice(device);
}

//  void Qt3DRender::QShaderNodesLoader::load()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender18QShaderNodesLoader4loadEv(
    Qt3DRender::QShaderNodesLoader *self) {
  self->load();
}

//  void Qt3DRender::QShaderNodesLoader::load(const QJsonObject
//      &prototypesObject)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender18QShaderNodesLoader4loadERK11QJsonObject(
    Qt3DRender::QShaderNodesLoader *self,
    const QJsonObject *prototypesObject) {
  self->load(*prototypesObject);
}

//  Qt3DRender::QShaderNodesLoader::~QShaderNodesLoader()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender18QShaderNodesLoaderD1Ev(
    Qt3DRender::QShaderNodesLoader *self) {
  delete self;
}

//  a QHash<QString, Qt3DRender::QShaderNode> a ritual of
//      Qt3DRender::QShaderNodesLoader gave
extern "C" Q_DECL_EXPORT
void ritual_drop_Qt3DRender_QShaderNodesLoader__QHash_QString_Qt3DRender_QShaderNode(
    QHash<QString, Qt3DRender::QShaderNode> *self) {
  delete self;
}
