//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DCore/6.12.0/Qt3DCore/private/sqt_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <Qt3DCore/6.12.0/Qt3DCore/private/qt3dcore_global_p.h>
#include <Qt3DCore/Qt3DCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DCore/6.12.0/Qt3DCore/private/sqt_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qmatrix4x4.h>

//  Qt3DCore::Sqt::Sqt()
extern "C" Q_DECL_EXPORT
Qt3DCore::Sqt *ritual_ZN8Qt3DCore3SqtC1Ev() {
  return new Qt3DCore::Sqt();
}

//  QMatrix4x4 Qt3DCore::Sqt::toMatrix() const
extern "C" Q_DECL_EXPORT
QMatrix4x4 *ritual_ZNK8Qt3DCore3Sqt8toMatrixEv(const Qt3DCore::Sqt *self) {
  return new QMatrix4x4(self->toMatrix());
}

//  bool Qt3DCore::Sqt::operator==(const Sqt &rhs) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK8Qt3DCore3SqteqERKS0_(
    const Qt3DCore::Sqt *self,
    const Qt3DCore::Sqt *rhs) {
  return self->operator==(*rhs);
}

//  Qt3DCore::Sqt::~Sqt()
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore3SqtD1Ev(Qt3DCore::Sqt *self) {
  delete self;
}
