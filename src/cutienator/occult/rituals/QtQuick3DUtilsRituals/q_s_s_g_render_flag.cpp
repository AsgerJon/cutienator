//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick3DUtils/6.12.0/QtQuick3DUtils/private/qssgutils_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQuick3DUtils/6.12.0/QtQuick3DUtils/private/qtquick3dutilsglobal_p.h>
#include <QtQuick3DUtils/QtQuick3DUtils>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DUtils/6.12.0/QtQuick3DUtils/private/qssgutils_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QSSGRenderFlag::QSSGRenderFlag()
extern "C" Q_DECL_EXPORT
QSSGRenderFlag *ritual_ZN14QSSGRenderFlagC1Ev() {
  return new QSSGRenderFlag();
}

//  QSSGRenderFlag::QSSGRenderFlag(quint32 v)
extern "C" Q_DECL_EXPORT
QSSGRenderFlag *ritual_ZN14QSSGRenderFlagC1Ej(quint32 v) {
  return new QSSGRenderFlag(v);
}

//  quint32 QSSGRenderFlag::value() const
extern "C" Q_DECL_EXPORT
quint32 ritual_ZNK14QSSGRenderFlag5valueEv(const QSSGRenderFlag *self) {
  return self->value();
}

//  void QSSGRenderFlag::setValue(quint32 v)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QSSGRenderFlag8setValueEj(QSSGRenderFlag *self, quint32 v) {
  self->setValue(v);
}

//  void QSSGRenderFlag::clearFlags(quint32 v)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QSSGRenderFlag10clearFlagsEj(
    QSSGRenderFlag *self,
    quint32 v) {
  self->clearFlags(v);
}

//  void QSSGRenderFlag::setFlag(quint32 v, bool on)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QSSGRenderFlag7setFlagEjb(
    QSSGRenderFlag *self,
    quint32 v,
    bool on) {
  self->setFlag(v, on);
}

//  bool QSSGRenderFlag::isSet(quint32 v) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QSSGRenderFlag5isSetEj(
    const QSSGRenderFlag *self,
    quint32 v) {
  return self->isSet(v);
}

//  bool operator==(const QSSGRenderFlag &a, const QSSGRenderFlag &b)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK14QSSGRenderFlagS1_(
    const QSSGRenderFlag *a,
    const QSSGRenderFlag *b) {
  return operator==(*a, *b);
}

//  bool operator!=(const QSSGRenderFlag &a, const QSSGRenderFlag &b)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK14QSSGRenderFlagS1_(
    const QSSGRenderFlag *a,
    const QSSGRenderFlag *b) {
  return operator!=(*a, *b);
}

//  quint32 QSSGRenderFlag::operator unsigned int() const
extern "C" Q_DECL_EXPORT
quint32 ritual_ZNK14QSSGRenderFlagcvjEv(const QSSGRenderFlag *self) {
  return self->operator quint32();
}

//  QSSGRenderFlag::~QSSGRenderFlag()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QSSGRenderFlagD1Ev(QSSGRenderFlag *self) {
  delete self;
}
