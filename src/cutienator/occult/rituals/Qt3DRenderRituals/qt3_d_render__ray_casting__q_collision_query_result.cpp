//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/6.12.0/Qt3DRender/private/qcollisionqueryresult_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <Qt3DRender/6.12.0/Qt3DRender/private/qt3drender_global_p.h>
#include <Qt3DRender/Qt3DRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DRender/6.12.0/Qt3DRender/private/qcollisionqueryresult_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <vector>
#include <Qt3DCore/Qt3DCore>

//  Qt3DRender::RayCasting::QCollisionQueryResult::QCollisionQueryResult()
extern "C" Q_DECL_EXPORT
Qt3DRender::RayCasting::QCollisionQueryResult *ritual_ZN10Qt3DRender10RayCasting21QCollisionQueryResultC1Ev() {
  return new Qt3DRender::RayCasting::QCollisionQueryResult();
}

//  Qt3DRender::RayCasting::QCollisionQueryResult::QCollisionQueryResult(cons
//      t QCollisionQueryResult &a0)
extern "C" Q_DECL_EXPORT
Qt3DRender::RayCasting::QCollisionQueryResult *ritual_ZN10Qt3DRender10RayCasting21QCollisionQueryResultC1ERKS1_(
    const Qt3DRender::RayCasting::QCollisionQueryResult *a0) {
  return new Qt3DRender::RayCasting::QCollisionQueryResult(*a0);
}

//  Qt3DRender::RayCasting::QCollisionQueryResult::~QCollisionQueryResult()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender10RayCasting21QCollisionQueryResultD1Ev(
    Qt3DRender::RayCasting::QCollisionQueryResult *self) {
  delete self;
}

//  QCollisionQueryResult
//      &Qt3DRender::RayCasting::QCollisionQueryResult::operator=(const
//      QCollisionQueryResult &a0)
extern "C" Q_DECL_EXPORT
Qt3DRender::RayCasting::QCollisionQueryResult *ritual_ZN10Qt3DRender10RayCasting21QCollisionQueryResultaSERKS1_(
    Qt3DRender::RayCasting::QCollisionQueryResult *self,
    const Qt3DRender::RayCasting::QCollisionQueryResult *a0) {
  return &(self->operator=(*a0));
}

#if defined(Q_COMPILER_RVALUE_REFS)
//  QCollisionQueryResult &Qt3DRender::RayCasting::QCollisionQueryResult::ope
//      rator=(QCollisionQueryResult &&other)
extern "C" Q_DECL_EXPORT
Qt3DRender::RayCasting::QCollisionQueryResult *ritual_ZN10Qt3DRender10RayCasting21QCollisionQueryResultaSEOS1_(
    Qt3DRender::RayCasting::QCollisionQueryResult *self,
    Qt3DRender::RayCasting::QCollisionQueryResult *other) {
  return &(self->operator=(std::move(*other)));
}
#endif  // defined(Q_COMPILER_RVALUE_REFS)

//  void
//      Qt3DRender::RayCasting::QCollisionQueryResult::swap(QCollisionQueryRe
//      sult &other)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender10RayCasting21QCollisionQueryResult4swapERS1_(
    Qt3DRender::RayCasting::QCollisionQueryResult *self,
    Qt3DRender::RayCasting::QCollisionQueryResult *other) {
  self->swap(*other);
}

//  QQueryHandle Qt3DRender::RayCasting::QCollisionQueryResult::handle()
//      const
extern "C" Q_DECL_EXPORT
Qt3DRender::RayCasting::QQueryHandle ritual_ZNK10Qt3DRender10RayCasting21QCollisionQueryResult6handleEv(
    const Qt3DRender::RayCasting::QCollisionQueryResult *self) {
  return self->handle();
}

//  const std::vector<Hit>
//      &Qt3DRender::RayCasting::QCollisionQueryResult::hits() const
extern "C" Q_DECL_EXPORT
const std::vector<Qt3DRender::RayCasting::QCollisionQueryResult::Hit> *ritual_ZNK10Qt3DRender10RayCasting21QCollisionQueryResult4hitsEv(
    const Qt3DRender::RayCasting::QCollisionQueryResult *self) {
  return &(self->hits());
}

//  std::vector<Qt3DCore::QNodeId>
//      Qt3DRender::RayCasting::QCollisionQueryResult::entitiesHit() const
extern "C" Q_DECL_EXPORT
std::vector<Qt3DCore::QNodeId> *ritual_ZNK10Qt3DRender10RayCasting21QCollisionQueryResult11entitiesHitEv(
    const Qt3DRender::RayCasting::QCollisionQueryResult *self) {
  return new std::vector<Qt3DCore::QNodeId>(self->entitiesHit());
}

//  Qt3DRender::RayCasting::QCollisionQueryResult::QCollisionQueryResult(QCol
//      lisionQueryResultPrivate &p)
extern "C" Q_DECL_EXPORT
Qt3DRender::RayCasting::QCollisionQueryResult *ritual_ZN10Qt3DRender10RayCasting21QCollisionQueryResultC1ERNS0_28QCollisionQueryResultPrivateE(
    Qt3DRender::RayCasting::QCollisionQueryResultPrivate *p) {
  return new Qt3DRender::RayCasting::QCollisionQueryResult(*p);
}

//  QCollisionQueryResultPrivate
//      *Qt3DRender::RayCasting::QCollisionQueryResult::d_func()
extern "C" Q_DECL_EXPORT
Qt3DRender::RayCasting::QCollisionQueryResultPrivate *ritual_ZN10Qt3DRender10RayCasting21QCollisionQueryResult6d_funcEv(
    Qt3DRender::RayCasting::QCollisionQueryResult *self) {
  return self->d_func();
}

//  const QCollisionQueryResultPrivate
//      *Qt3DRender::RayCasting::QCollisionQueryResult::d_func() const
extern "C" Q_DECL_EXPORT
const Qt3DRender::RayCasting::QCollisionQueryResultPrivate *ritual_ZNK10Qt3DRender10RayCasting21QCollisionQueryResult6d_funcEv(
    const Qt3DRender::RayCasting::QCollisionQueryResult *self) {
  return self->d_func();
}

//  a std::vector<Qt3DCore::QNodeId> a ritual of
//      Qt3DRender::RayCasting::QCollisionQueryResult gave
extern "C" Q_DECL_EXPORT
void ritual_drop_Qt3DRender_RayCasting_QCollisionQueryResult__std_vector_Qt3DCore_QNodeId(
    std::vector<Qt3DCore::QNodeId> *self) {
  delete self;
}
