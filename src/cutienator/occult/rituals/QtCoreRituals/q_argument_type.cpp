//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qmetaobject_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qmetaobject_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetatype.h>
#include <QtCore/qbytearrayview.h>

//  QArgumentType::QArgumentType()
extern "C" Q_DECL_EXPORT
QArgumentType *ritual_ZN13QArgumentTypeC1Ev() {
  return new QArgumentType();
}

//  QArgumentType::QArgumentType(QMetaType metaType)
extern "C" Q_DECL_EXPORT
QArgumentType *ritual_ZN13QArgumentTypeC1E9QMetaType(
    const QMetaType *metaType) {
  return new QArgumentType(*metaType);
}

//  QMetaType QArgumentType::metaType() const
extern "C" Q_DECL_EXPORT
QMetaType *ritual_ZNK13QArgumentType8metaTypeEv(const QArgumentType *self) {
  return new QMetaType(self->metaType());
}

//  QByteArrayView QArgumentType::name() const
extern "C" Q_DECL_EXPORT
QByteArrayView *ritual_ZNK13QArgumentType4nameEv(const QArgumentType *self) {
  return new QByteArrayView(self->name());
}

//  bool operator==(const QArgumentType &lhs, const QArgumentType &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK13QArgumentTypeS1_(
    const QArgumentType *lhs,
    const QArgumentType *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const QArgumentType &lhs, const QArgumentType &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK13QArgumentTypeS1_(
    const QArgumentType *lhs,
    const QArgumentType *rhs) {
  return operator!=(*lhs, *rhs);
}

//  QArgumentType::~QArgumentType()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QArgumentTypeD1Ev(QArgumentType *self) {
  delete self;
}
