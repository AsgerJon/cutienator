//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/6.12.0/Qt3DRender/private/loadscenejob_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <Qt3DRender/6.12.0/Qt3DRender/private/qt3drender_global_p.h>
#include <Qt3DRender/Qt3DRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DRender/6.12.0/Qt3DRender/private/loadscenejob_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qurl.h>
#include <Qt3DCore/qnodeid.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qstring.h>
#include <QtCore/qlist.h>
#include <QtCore/QList>

//  Qt3DRender::Render::LoadSceneJob::LoadSceneJob(const QUrl &source,
//      Qt3DCore::QNodeId sceneComponent)
extern "C" Q_DECL_EXPORT
Qt3DRender::Render::LoadSceneJob *ritual_ZN10Qt3DRender6Render12LoadSceneJobC1ERK4QUrlN8Qt3DCore7QNodeIdE(
    const QUrl *source,
    const Qt3DCore::QNodeId *sceneComponent) {
  return new Qt3DRender::Render::LoadSceneJob(*source, *sceneComponent);
}

//  void Qt3DRender::Render::LoadSceneJob::setData(const QByteArray &data)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render12LoadSceneJob7setDataERK10QByteArray(
    Qt3DRender::Render::LoadSceneJob *self,
    const QByteArray *data) {
  self->setData(*data);
}

//  void Qt3DRender::Render::LoadSceneJob::setNodeManagers(NodeManagers
//      *managers)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render12LoadSceneJob15setNodeManagersEPNS0_12NodeManagersE(
    Qt3DRender::Render::LoadSceneJob *self,
    Qt3DRender::Render::NodeManagers *managers) {
  self->setNodeManagers(managers);
}

//  void Qt3DRender::Render::LoadSceneJob::setSceneImporters(const
//      QList<QSceneImporter *> sceneImporters)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render12LoadSceneJob17setSceneImportersE5QListIPNS_14QSceneImporterEE(
    Qt3DRender::Render::LoadSceneJob *self,
    const QList<Qt3DRender::QSceneImporter *> *sceneImporters) {
  self->setSceneImporters(*sceneImporters);
}

//  NodeManagers *Qt3DRender::Render::LoadSceneJob::nodeManagers() const
extern "C" Q_DECL_EXPORT
Qt3DRender::Render::NodeManagers *ritual_ZNK10Qt3DRender6Render12LoadSceneJob12nodeManagersEv(
    const Qt3DRender::Render::LoadSceneJob *self) {
  return self->nodeManagers();
}

//  QList<QSceneImporter *>
//      Qt3DRender::Render::LoadSceneJob::sceneImporters() const
extern "C" Q_DECL_EXPORT
QList<Qt3DRender::QSceneImporter *> *ritual_ZNK10Qt3DRender6Render12LoadSceneJob14sceneImportersEv(
    const Qt3DRender::Render::LoadSceneJob *self) {
  return new QList<Qt3DRender::QSceneImporter *>(self->sceneImporters());
}

//  QUrl Qt3DRender::Render::LoadSceneJob::source() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK10Qt3DRender6Render12LoadSceneJob6sourceEv(
    const Qt3DRender::Render::LoadSceneJob *self) {
  return new QUrl(self->source());
}

//  Qt3DCore::QNodeId Qt3DRender::Render::LoadSceneJob::sceneComponentId()
//      const
extern "C" Q_DECL_EXPORT
Qt3DCore::QNodeId *ritual_ZNK10Qt3DRender6Render12LoadSceneJob16sceneComponentIdEv(
    const Qt3DRender::Render::LoadSceneJob *self) {
  return new Qt3DCore::QNodeId(self->sceneComponentId());
}

//  void Qt3DRender::Render::LoadSceneJob::run()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render12LoadSceneJob3runEv(
    Qt3DRender::Render::LoadSceneJob *self) {
  self->run();
}

//  Qt3DCore::QEntity
//      *Qt3DRender::Render::LoadSceneJob::tryLoadScene(QSceneLoader::Status
//      &finalStatus, const QStringList &extensions, const std::function<void
//      (QSceneImporter *)> &importerSetupFunc)
extern "C" Q_DECL_EXPORT
Qt3DCore::QEntity *ritual_ZN10Qt3DRender6Render12LoadSceneJob12tryLoadSceneERNS_12QSceneLoader6StatusERK5QListI7QStringERKSt8functionIFvPNS_14QSceneImporterEEE(
    Qt3DRender::Render::LoadSceneJob *self,
    Qt3DRender::QSceneLoader::Status *finalStatus,
    const QList<QString> *extensions,
    const std::function<void (Qt3DRender::QSceneImporter *)> *importerSetupFunc) {
  return self->tryLoadScene(*finalStatus, *extensions, *importerSetupFunc);
}

//  LoadSceneJobPrivate *Qt3DRender::Render::LoadSceneJob::d_func()
extern "C" Q_DECL_EXPORT
Qt3DRender::Render::LoadSceneJobPrivate *ritual_ZN10Qt3DRender6Render12LoadSceneJob6d_funcEv(
    Qt3DRender::Render::LoadSceneJob *self) {
  return self->d_func();
}

//  const LoadSceneJobPrivate *Qt3DRender::Render::LoadSceneJob::d_func()
//      const
extern "C" Q_DECL_EXPORT
const Qt3DRender::Render::LoadSceneJobPrivate *ritual_ZNK10Qt3DRender6Render12LoadSceneJob6d_funcEv(
    const Qt3DRender::Render::LoadSceneJob *self) {
  return self->d_func();
}

//  void Qt3DRender::Render::LoadSceneJob::run()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10Qt3DRender6Render12LoadSceneJob3runEv(
    Qt3DRender::Render::LoadSceneJob *self) {
  self->Qt3DRender::Render::LoadSceneJob::run();
}

//  a QList<Qt3DRender::QSceneImporter *> a ritual of
//      Qt3DRender::Render::LoadSceneJob gave
extern "C" Q_DECL_EXPORT
void ritual_drop_Qt3DRender_Render_LoadSceneJob__QList_Qt3DRender_QSceneImporter(
    QList<Qt3DRender::QSceneImporter *> *self) {
  delete self;
}
