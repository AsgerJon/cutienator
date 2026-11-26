//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/6.12.0/Qt3DRender/private/qgraphicsapifilter_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <Qt3DRender/6.12.0/Qt3DRender/private/qt3drender_global_p.h>
#include <Qt3DRender/Qt3DRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DRender/6.12.0/Qt3DRender/private/qgraphicsapifilter_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>

//  Qt3DRender::GraphicsApiFilterData::GraphicsApiFilterData()
extern "C" Q_DECL_EXPORT
Qt3DRender::GraphicsApiFilterData *ritual_ZN10Qt3DRender21GraphicsApiFilterDataC1Ev() {
  return new Qt3DRender::GraphicsApiFilterData();
}

//  QString Qt3DRender::GraphicsApiFilterData::toString() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK10Qt3DRender21GraphicsApiFilterData8toStringEv(
    const Qt3DRender::GraphicsApiFilterData *self) {
  return new QString(self->toString());
}

//  bool Qt3DRender::GraphicsApiFilterData::operator==(const
//      GraphicsApiFilterData &other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10Qt3DRender21GraphicsApiFilterDataeqERKS0_(
    const Qt3DRender::GraphicsApiFilterData *self,
    const Qt3DRender::GraphicsApiFilterData *other) {
  return self->operator==(*other);
}

//  bool Qt3DRender::GraphicsApiFilterData::operator!=(const
//      GraphicsApiFilterData &other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10Qt3DRender21GraphicsApiFilterDataneERKS0_(
    const Qt3DRender::GraphicsApiFilterData *self,
    const Qt3DRender::GraphicsApiFilterData *other) {
  return self->operator!=(*other);
}

//  bool Qt3DRender::GraphicsApiFilterData::operator<(const
//      GraphicsApiFilterData &other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10Qt3DRender21GraphicsApiFilterDataltERKS0_(
    const Qt3DRender::GraphicsApiFilterData *self,
    const Qt3DRender::GraphicsApiFilterData *other) {
  return self->operator<(*other);
}

//  Qt3DRender::GraphicsApiFilterData::~GraphicsApiFilterData()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender21GraphicsApiFilterDataD1Ev(
    Qt3DRender::GraphicsApiFilterData *self) {
  delete self;
}
