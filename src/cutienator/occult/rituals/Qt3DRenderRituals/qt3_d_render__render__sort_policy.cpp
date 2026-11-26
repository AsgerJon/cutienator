//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/6.12.0/Qt3DRender/private/sortpolicy_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <Qt3DRender/6.12.0/Qt3DRender/private/qt3drender_global_p.h>
#include <Qt3DRender/Qt3DRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DRender/6.12.0/Qt3DRender/private/sortpolicy_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/QList>

//  Qt3DRender::Render::SortPolicy::SortPolicy()
extern "C" Q_DECL_EXPORT
Qt3DRender::Render::SortPolicy *ritual_ZN10Qt3DRender6Render10SortPolicyC1Ev() {
  return new Qt3DRender::Render::SortPolicy();
}

//  void Qt3DRender::Render::SortPolicy::syncFromFrontEnd(const
//      Qt3DCore::QNode *frontEnd, bool firstTime)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render10SortPolicy16syncFromFrontEndEPKN8Qt3DCore5QNodeEb(
    Qt3DRender::Render::SortPolicy *self,
    const Qt3DCore::QNode *frontEnd,
    bool firstTime) {
  self->syncFromFrontEnd(frontEnd, firstTime);
}

//  QList<Qt3DRender::QSortPolicy::SortType>
//      Qt3DRender::Render::SortPolicy::sortTypes() const
extern "C" Q_DECL_EXPORT
QList<Qt3DRender::QSortPolicy::SortType> *ritual_ZNK10Qt3DRender6Render10SortPolicy9sortTypesEv(
    const Qt3DRender::Render::SortPolicy *self) {
  return new QList<Qt3DRender::QSortPolicy::SortType>(self->sortTypes());
}

//  void Qt3DRender::Render::SortPolicy::syncFromFrontEnd(const
//      Qt3DCore::QNode *frontEnd, bool firstTime)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10Qt3DRender6Render10SortPolicy16syncFromFrontEndEPKN8Qt3DCore5QNodeEb(
    Qt3DRender::Render::SortPolicy *self,
    const Qt3DCore::QNode *frontEnd,
    bool firstTime) {
  self->Qt3DRender::Render::SortPolicy::syncFromFrontEnd(
      frontEnd,
      firstTime);
}

//  a QList<Qt3DRender::QSortPolicy::SortType> a ritual of
//      Qt3DRender::Render::SortPolicy gave
extern "C" Q_DECL_EXPORT
void ritual_drop_Qt3DRender_Render_SortPolicy__QList_Qt3DRender_QSortPolicy_SortType(
    QList<Qt3DRender::QSortPolicy::SortType> *self) {
  delete self;
}
