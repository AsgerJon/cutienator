//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/rhi/qshaderdescription.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/rhi/qshaderdescription.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qbytearray.h>
#include <QtCore/qdebug.h>

//  QShaderDescription::QShaderDescription()
extern "C" Q_DECL_EXPORT
QShaderDescription *ritual_ZN18QShaderDescriptionC1Ev() {
  return new QShaderDescription();
}

//  QShaderDescription::QShaderDescription(const QShaderDescription &other)
extern "C" Q_DECL_EXPORT
QShaderDescription *ritual_ZN18QShaderDescriptionC1ERKS_(
    const QShaderDescription *other) {
  return new QShaderDescription(*other);
}

//  QShaderDescription::~QShaderDescription()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QShaderDescriptionD1Ev(QShaderDescription *self) {
  delete self;
}

//  void QShaderDescription::detach()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QShaderDescription6detachEv(QShaderDescription *self) {
  self->detach();
}

//  bool QShaderDescription::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QShaderDescription7isValidEv(
    const QShaderDescription *self) {
  return self->isValid();
}

//  void QShaderDescription::serialize(QDataStream *stream, int version)
//      const
extern "C" Q_DECL_EXPORT
void ritual_ZNK18QShaderDescription9serializeEP11QDataStreami(
    const QShaderDescription *self,
    QDataStream *stream,
    int version) {
  self->serialize(stream, version);
}

//  QByteArray QShaderDescription::toJson() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK18QShaderDescription6toJsonEv(
    const QShaderDescription *self) {
  return new QByteArray(self->toJson());
}

//  QShaderDescription QShaderDescription::deserialize(QDataStream *stream,
//      int version)
extern "C" Q_DECL_EXPORT
QShaderDescription *ritual_ZN18QShaderDescription11deserializeEP11QDataStreami(
    QDataStream *stream,
    int version) {
  return new QShaderDescription(
      QShaderDescription::deserialize(
          stream,
          version));
}

//  uint QShaderDescription::tessellationOutputVertexCount() const
extern "C" Q_DECL_EXPORT
uint ritual_ZNK18QShaderDescription29tessellationOutputVertexCountEv(
    const QShaderDescription *self) {
  return self->tessellationOutputVertexCount();
}

//  TessellationMode QShaderDescription::tessellationMode() const
extern "C" Q_DECL_EXPORT
QShaderDescription::TessellationMode ritual_ZNK18QShaderDescription16tessellationModeEv(
    const QShaderDescription *self) {
  return self->tessellationMode();
}

//  TessellationWindingOrder QShaderDescription::tessellationWindingOrder()
//      const
extern "C" Q_DECL_EXPORT
QShaderDescription::TessellationWindingOrder ritual_ZNK18QShaderDescription24tessellationWindingOrderEv(
    const QShaderDescription *self) {
  return self->tessellationWindingOrder();
}

//  TessellationPartitioning QShaderDescription::tessellationPartitioning()
//      const
extern "C" Q_DECL_EXPORT
QShaderDescription::TessellationPartitioning ritual_ZNK18QShaderDescription24tessellationPartitioningEv(
    const QShaderDescription *self) {
  return self->tessellationPartitioning();
}

#if !defined(QT_NO_DEBUG_STREAM)
//  QDebug operator<<(QDebug a0, const QShaderDescription &a1)
extern "C" Q_DECL_EXPORT
QDebug *ritual_Zls6QDebugRK18QShaderDescription(
    const QDebug *a0,
    const QShaderDescription *a1) {
  return new QDebug(operator<<(*a0, *a1));
}
#endif  // !defined(QT_NO_DEBUG_STREAM)

//  bool operator==(const QShaderDescription &lhs, const QShaderDescription
//      &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK18QShaderDescriptionS1_(
    const QShaderDescription *lhs,
    const QShaderDescription *rhs) {
  return operator==(*lhs, *rhs);
}
