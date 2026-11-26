//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DCore/qnodeid.h, Qt 6.12.0. Changes made here are lost.
#include <Qt3DCore/qnodeid.h>

//  Qt3DCore::QNodeId::QNodeId(quint64 i)
extern "C" Q_DECL_EXPORT
Qt3DCore::QNodeId *ritual_ZN8Qt3DCore7QNodeIdC1Ey(quint64 i) {
  return new Qt3DCore::QNodeId(i);
}

//  Qt3DCore::QNodeId::QNodeId()
extern "C" Q_DECL_EXPORT
Qt3DCore::QNodeId *ritual_ZN8Qt3DCore7QNodeIdC1Ev() {
  return new Qt3DCore::QNodeId();
}

//  QNodeId Qt3DCore::QNodeId::createId()
extern "C" Q_DECL_EXPORT
Qt3DCore::QNodeId *ritual_ZN8Qt3DCore7QNodeId8createIdEv() {
  return new Qt3DCore::QNodeId(Qt3DCore::QNodeId::createId());
}

//  bool Qt3DCore::QNodeId::isNull() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK8Qt3DCore7QNodeId6isNullEv(const Qt3DCore::QNodeId *self) {
  return self->isNull();
}

//  bool Qt3DCore::QNodeId::operator==(QNodeId other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK8Qt3DCore7QNodeIdeqES0_(
    const Qt3DCore::QNodeId *self,
    const Qt3DCore::QNodeId *other) {
  return self->operator==(*other);
}

//  bool Qt3DCore::QNodeId::operator!=(QNodeId other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK8Qt3DCore7QNodeIdneES0_(
    const Qt3DCore::QNodeId *self,
    const Qt3DCore::QNodeId *other) {
  return self->operator!=(*other);
}

//  bool Qt3DCore::QNodeId::operator<(QNodeId other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK8Qt3DCore7QNodeIdltES0_(
    const Qt3DCore::QNodeId *self,
    const Qt3DCore::QNodeId *other) {
  return self->operator<(*other);
}

//  bool Qt3DCore::QNodeId::operator>(QNodeId other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK8Qt3DCore7QNodeIdgtES0_(
    const Qt3DCore::QNodeId *self,
    const Qt3DCore::QNodeId *other) {
  return self->operator>(*other);
}

//  quint64 Qt3DCore::QNodeId::id() const
extern "C" Q_DECL_EXPORT
quint64 ritual_ZNK8Qt3DCore7QNodeId2idEv(const Qt3DCore::QNodeId *self) {
  return self->id();
}

//  bool Qt3DCore::QNodeId::operator bool() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK8Qt3DCore7QNodeIdcvbEv(const Qt3DCore::QNodeId *self) {
  return self->operator bool();
}

//  Qt3DCore::QNodeId::~QNodeId()
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore7QNodeIdD1Ev(Qt3DCore::QNodeId *self) {
  delete self;
}
