//  Written by dev_tooling.RitualGenerator from the records of Qt3DQuickExtra
//  s/6.12.0/Qt3DQuickExtras/private/quick3dlevelofdetailloader_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <Qt3DQuickExtras/6.12.0/Qt3DQuickExtras/private/qt3dquickextras_global_p.h>
#include <Qt3DQuickExtras/Qt3DQuickExtras>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DQuickExtras/6.12.0/Qt3DQuickExtras/private/quick3dlevelofdetailloader_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qvariant.h>
#include <Qt3DRender/qlevelofdetailboundingsphere.h>
#include <QtGui/qvectornd.h>
#include <QtCore/qurl.h>
#include <QtCore/qlist.h>
#include <QtCore/QList>

//  const QMetaObject
//      *Qt3DExtras::Extras::Quick::Quick3DLevelOfDetailLoader::metaObject()
//      const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK10Qt3DExtras6Extras5Quick26Quick3DLevelOfDetailLoader10metaObjectEv(
    const Qt3DExtras::Extras::Quick::Quick3DLevelOfDetailLoader *self) {
  return self->metaObject();
}

//  void
//      *Qt3DExtras::Extras::Quick::Quick3DLevelOfDetailLoader::qt_metacast(c
//      onst char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN10Qt3DExtras6Extras5Quick26Quick3DLevelOfDetailLoader11qt_metacastEPKc(
    Qt3DExtras::Extras::Quick::Quick3DLevelOfDetailLoader *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int Qt3DExtras::Extras::Quick::Quick3DLevelOfDetailLoader::qt_metacall(QM
//      etaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN10Qt3DExtras6Extras5Quick26Quick3DLevelOfDetailLoader11qt_metacallEN11QMetaObject4CallEiPPv(
    Qt3DExtras::Extras::Quick::Quick3DLevelOfDetailLoader *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString Qt3DExtras::Extras::Quick::Quick3DLevelOfDetailLoader::tr(const
//      char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN10Qt3DExtras6Extras5Quick26Quick3DLevelOfDetailLoader2trEPKcS4_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(
      Qt3DExtras::Extras::Quick::Quick3DLevelOfDetailLoader::tr(
          s,
          c,
          n));
}

//  Qt3DExtras::Extras::Quick::Quick3DLevelOfDetailLoader::Quick3DLevelOfDeta
//      ilLoader(QNode *parent)
extern "C" Q_DECL_EXPORT
Qt3DExtras::Extras::Quick::Quick3DLevelOfDetailLoader *ritual_ZN10Qt3DExtras6Extras5Quick26Quick3DLevelOfDetailLoaderC1EPN8Qt3DCore5QNodeE(
    Qt3DCore::QNode *parent) {
  return new Qt3DExtras::Extras::Quick::Quick3DLevelOfDetailLoader(parent);
}

//  QVariantList
//      Qt3DExtras::Extras::Quick::Quick3DLevelOfDetailLoader::sources()
//      const
extern "C" Q_DECL_EXPORT
QList<QVariant> *ritual_ZNK10Qt3DExtras6Extras5Quick26Quick3DLevelOfDetailLoader7sourcesEv(
    const Qt3DExtras::Extras::Quick::Quick3DLevelOfDetailLoader *self) {
  return new QList<QVariant>(self->sources());
}

//  void
//      Qt3DExtras::Extras::Quick::Quick3DLevelOfDetailLoader::setSources(con
//      st QVariantList &sources)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras6Extras5Quick26Quick3DLevelOfDetailLoader10setSourcesERK5QListI8QVariantE(
    Qt3DExtras::Extras::Quick::Quick3DLevelOfDetailLoader *self,
    const QList<QVariant> *sources) {
  self->setSources(*sources);
}

//  Qt3DRender::QCamera
//      *Qt3DExtras::Extras::Quick::Quick3DLevelOfDetailLoader::camera()
//      const
extern "C" Q_DECL_EXPORT
Qt3DRender::QCamera *ritual_ZNK10Qt3DExtras6Extras5Quick26Quick3DLevelOfDetailLoader6cameraEv(
    const Qt3DExtras::Extras::Quick::Quick3DLevelOfDetailLoader *self) {
  return self->camera();
}

//  void Qt3DExtras::Extras::Quick::Quick3DLevelOfDetailLoader::setCamera(Qt3
//      DRender::QCamera *camera)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras6Extras5Quick26Quick3DLevelOfDetailLoader9setCameraEPN10Qt3DRender7QCameraE(
    Qt3DExtras::Extras::Quick::Quick3DLevelOfDetailLoader *self,
    Qt3DRender::QCamera *camera) {
  self->setCamera(camera);
}

//  int Qt3DExtras::Extras::Quick::Quick3DLevelOfDetailLoader::currentIndex()
//      const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10Qt3DExtras6Extras5Quick26Quick3DLevelOfDetailLoader12currentIndexEv(
    const Qt3DExtras::Extras::Quick::Quick3DLevelOfDetailLoader *self) {
  return self->currentIndex();
}

//  void Qt3DExtras::Extras::Quick::Quick3DLevelOfDetailLoader::setCurrentInd
//      ex(int currentIndex)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras6Extras5Quick26Quick3DLevelOfDetailLoader15setCurrentIndexEi(
    Qt3DExtras::Extras::Quick::Quick3DLevelOfDetailLoader *self,
    int currentIndex) {
  self->setCurrentIndex(currentIndex);
}

//  Qt3DRender::QLevelOfDetail::ThresholdType
//      Qt3DExtras::Extras::Quick::Quick3DLevelOfDetailLoader::thresholdType(
//      ) const
extern "C" Q_DECL_EXPORT
Qt3DRender::QLevelOfDetail::ThresholdType ritual_ZNK10Qt3DExtras6Extras5Quick26Quick3DLevelOfDetailLoader13thresholdTypeEv(
    const Qt3DExtras::Extras::Quick::Quick3DLevelOfDetailLoader *self) {
  return self->thresholdType();
}

//  void Qt3DExtras::Extras::Quick::Quick3DLevelOfDetailLoader::setThresholdT
//      ype(Qt3DRender::QLevelOfDetail::ThresholdType thresholdType)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras6Extras5Quick26Quick3DLevelOfDetailLoader16setThresholdTypeEN10Qt3DRender14QLevelOfDetail13ThresholdTypeE(
    Qt3DExtras::Extras::Quick::Quick3DLevelOfDetailLoader *self,
    Qt3DRender::QLevelOfDetail::ThresholdType thresholdType) {
  self->setThresholdType(thresholdType);
}

//  QList<qreal>
//      Qt3DExtras::Extras::Quick::Quick3DLevelOfDetailLoader::thresholds()
//      const
extern "C" Q_DECL_EXPORT
QList<qreal> *ritual_ZNK10Qt3DExtras6Extras5Quick26Quick3DLevelOfDetailLoader10thresholdsEv(
    const Qt3DExtras::Extras::Quick::Quick3DLevelOfDetailLoader *self) {
  return new QList<qreal>(self->thresholds());
}

//  void Qt3DExtras::Extras::Quick::Quick3DLevelOfDetailLoader::setThresholds
//      (const QList<qreal> &thresholds)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras6Extras5Quick26Quick3DLevelOfDetailLoader13setThresholdsERK5QListIdE(
    Qt3DExtras::Extras::Quick::Quick3DLevelOfDetailLoader *self,
    const QList<qreal> *thresholds) {
  self->setThresholds(*thresholds);
}

//  Qt3DRender::QLevelOfDetailBoundingSphere
//      Qt3DExtras::Extras::Quick::Quick3DLevelOfDetailLoader::volumeOverride
//      () const
extern "C" Q_DECL_EXPORT
Qt3DRender::QLevelOfDetailBoundingSphere *ritual_ZNK10Qt3DExtras6Extras5Quick26Quick3DLevelOfDetailLoader14volumeOverrideEv(
    const Qt3DExtras::Extras::Quick::Quick3DLevelOfDetailLoader *self) {
  return new Qt3DRender::QLevelOfDetailBoundingSphere(
      self->volumeOverride());
}

//  void Qt3DExtras::Extras::Quick::Quick3DLevelOfDetailLoader::setVolumeOver
//      ride(const Qt3DRender::QLevelOfDetailBoundingSphere &volumeOverride)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras6Extras5Quick26Quick3DLevelOfDetailLoader17setVolumeOverrideERKN10Qt3DRender28QLevelOfDetailBoundingSphereE(
    Qt3DExtras::Extras::Quick::Quick3DLevelOfDetailLoader *self,
    const Qt3DRender::QLevelOfDetailBoundingSphere *volumeOverride) {
  self->setVolumeOverride(*volumeOverride);
}

//  Qt3DRender::QLevelOfDetailBoundingSphere Qt3DExtras::Extras::Quick::Quick
//      3DLevelOfDetailLoader::createBoundingSphere(const QVector3D &center,
//      float radius)
extern "C" Q_DECL_EXPORT
Qt3DRender::QLevelOfDetailBoundingSphere *ritual_ZN10Qt3DExtras6Extras5Quick26Quick3DLevelOfDetailLoader20createBoundingSphereERK9QVector3Df(
    Qt3DExtras::Extras::Quick::Quick3DLevelOfDetailLoader *self,
    const QVector3D *center,
    float radius) {
  return new Qt3DRender::QLevelOfDetailBoundingSphere(
      self->createBoundingSphere(
          *center,
          radius));
}

//  QObject *Qt3DExtras::Extras::Quick::Quick3DLevelOfDetailLoader::entity()
//      const
extern "C" Q_DECL_EXPORT
QObject *ritual_ZNK10Qt3DExtras6Extras5Quick26Quick3DLevelOfDetailLoader6entityEv(
    const Qt3DExtras::Extras::Quick::Quick3DLevelOfDetailLoader *self) {
  return self->entity();
}

//  QUrl Qt3DExtras::Extras::Quick::Quick3DLevelOfDetailLoader::source()
//      const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK10Qt3DExtras6Extras5Quick26Quick3DLevelOfDetailLoader6sourceEv(
    const Qt3DExtras::Extras::Quick::Quick3DLevelOfDetailLoader *self) {
  return new QUrl(self->source());
}

//  void
//      Qt3DExtras::Extras::Quick::Quick3DLevelOfDetailLoader::sourcesChanged
//      ()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras6Extras5Quick26Quick3DLevelOfDetailLoader14sourcesChangedEv(
    Qt3DExtras::Extras::Quick::Quick3DLevelOfDetailLoader *self) {
  self->sourcesChanged();
}

//  void
//      Qt3DExtras::Extras::Quick::Quick3DLevelOfDetailLoader::cameraChanged(
//      )
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras6Extras5Quick26Quick3DLevelOfDetailLoader13cameraChangedEv(
    Qt3DExtras::Extras::Quick::Quick3DLevelOfDetailLoader *self) {
  self->cameraChanged();
}

//  void Qt3DExtras::Extras::Quick::Quick3DLevelOfDetailLoader::currentIndexC
//      hanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras6Extras5Quick26Quick3DLevelOfDetailLoader19currentIndexChangedEv(
    Qt3DExtras::Extras::Quick::Quick3DLevelOfDetailLoader *self) {
  self->currentIndexChanged();
}

//  void Qt3DExtras::Extras::Quick::Quick3DLevelOfDetailLoader::thresholdType
//      Changed()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras6Extras5Quick26Quick3DLevelOfDetailLoader20thresholdTypeChangedEv(
    Qt3DExtras::Extras::Quick::Quick3DLevelOfDetailLoader *self) {
  self->thresholdTypeChanged();
}

//  void Qt3DExtras::Extras::Quick::Quick3DLevelOfDetailLoader::thresholdsCha
//      nged()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras6Extras5Quick26Quick3DLevelOfDetailLoader17thresholdsChangedEv(
    Qt3DExtras::Extras::Quick::Quick3DLevelOfDetailLoader *self) {
  self->thresholdsChanged();
}

//  void Qt3DExtras::Extras::Quick::Quick3DLevelOfDetailLoader::volumeOverrid
//      eChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras6Extras5Quick26Quick3DLevelOfDetailLoader21volumeOverrideChangedEv(
    Qt3DExtras::Extras::Quick::Quick3DLevelOfDetailLoader *self) {
  self->volumeOverrideChanged();
}

//  void
//      Qt3DExtras::Extras::Quick::Quick3DLevelOfDetailLoader::entityChanged(
//      )
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras6Extras5Quick26Quick3DLevelOfDetailLoader13entityChangedEv(
    Qt3DExtras::Extras::Quick::Quick3DLevelOfDetailLoader *self) {
  self->entityChanged();
}

//  void
//      Qt3DExtras::Extras::Quick::Quick3DLevelOfDetailLoader::sourceChanged(
//      )
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras6Extras5Quick26Quick3DLevelOfDetailLoader13sourceChangedEv(
    Qt3DExtras::Extras::Quick::Quick3DLevelOfDetailLoader *self) {
  self->sourceChanged();
}

//  Quick3DLevelOfDetailLoaderPrivate
//      *Qt3DExtras::Extras::Quick::Quick3DLevelOfDetailLoader::d_func()
extern "C" Q_DECL_EXPORT
Qt3DExtras::Extras::Quick::Quick3DLevelOfDetailLoaderPrivate *ritual_ZN10Qt3DExtras6Extras5Quick26Quick3DLevelOfDetailLoader6d_funcEv(
    Qt3DExtras::Extras::Quick::Quick3DLevelOfDetailLoader *self) {
  return self->d_func();
}

//  const Quick3DLevelOfDetailLoaderPrivate
//      *Qt3DExtras::Extras::Quick::Quick3DLevelOfDetailLoader::d_func()
//      const
extern "C" Q_DECL_EXPORT
const Qt3DExtras::Extras::Quick::Quick3DLevelOfDetailLoaderPrivate *ritual_ZNK10Qt3DExtras6Extras5Quick26Quick3DLevelOfDetailLoader6d_funcEv(
    const Qt3DExtras::Extras::Quick::Quick3DLevelOfDetailLoader *self) {
  return self->d_func();
}

//  a QList<qreal> a ritual of
//      Qt3DExtras::Extras::Quick::Quick3DLevelOfDetailLoader gave
extern "C" Q_DECL_EXPORT
void ritual_drop_Qt3DExtras_Extras_Quick_Quick3DLevelOfDetailLoader__QList_qreal(
    QList<qreal> *self) {
  delete self;
}
