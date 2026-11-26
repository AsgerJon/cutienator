//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qqmlpropertybindingbase_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmlpropertybindingbase_p.h>
#include <QtQml/6.12.0/QtQml/private/qqmlpropertyindex_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetatype.h>

//  BindingKind QQmlPropertyBindingBase::bindingKind() const
extern "C" Q_DECL_EXPORT
QQmlPropertyBindingBase::BindingKind ritual_ZNK23QQmlPropertyBindingBase11bindingKindEv(
    const QQmlPropertyBindingBase *self) {
  return self->bindingKind();
}

//  bool QQmlPropertyBindingBase::isUndefined() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK23QQmlPropertyBindingBase11isUndefinedEv(
    const QQmlPropertyBindingBase *self) {
  return self->isUndefined();
}

//  QQmlPropertyBindingBase::QQmlPropertyBindingBase(QObject *target,
//      QQmlPropertyIndex targetIndex, QMetaType targetMetaType, const
//      QtPrivate::BindingFunctionVTable *vtable, BindingKind bindingKind,
//      HasBoundFunction hasBoundFunction)
extern "C" Q_DECL_EXPORT
QQmlPropertyBindingBase *ritual_ZN23QQmlPropertyBindingBaseC1EP7QObject17QQmlPropertyIndex9QMetaTypePKN9QtPrivate21BindingFunctionVTableENS_11BindingKindENS_16HasBoundFunctionE(
    QObject *target,
    const QQmlPropertyIndex *targetIndex,
    const QMetaType *targetMetaType,
    const QtPrivate::BindingFunctionVTable *vtable,
    QQmlPropertyBindingBase::BindingKind bindingKind,
    QQmlPropertyBindingBase::HasBoundFunction hasBoundFunction) {
  return new QQmlPropertyBindingBase(
      target,
      *targetIndex,
      *targetMetaType,
      vtable,
      bindingKind,
      hasBoundFunction);
}

//  QObject *QQmlPropertyBindingBase::target() const
extern "C" Q_DECL_EXPORT
QObject *ritual_ZNK23QQmlPropertyBindingBase6targetEv(
    const QQmlPropertyBindingBase *self) {
  return self->target();
}

//  QQmlPropertyIndex QQmlPropertyBindingBase::targetIndex() const
extern "C" Q_DECL_EXPORT
QQmlPropertyIndex *ritual_ZNK23QQmlPropertyBindingBase11targetIndexEv(
    const QQmlPropertyBindingBase *self) {
  return new QQmlPropertyIndex(self->targetIndex());
}

//  bool QQmlPropertyBindingBase::hasBoundFunction() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK23QQmlPropertyBindingBase16hasBoundFunctionEv(
    const QQmlPropertyBindingBase *self) {
  return self->hasBoundFunction();
}

//  void QQmlPropertyBindingBase::setIsUndefined(bool isUndefined)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQmlPropertyBindingBase14setIsUndefinedEb(
    QQmlPropertyBindingBase *self,
    bool isUndefined) {
  self->setIsUndefined(isUndefined);
}

//  size_t QQmlPropertyBindingBase::kindOffset()
extern "C" Q_DECL_EXPORT
size_t ritual_ZN23QQmlPropertyBindingBase10kindOffsetEv() {
  return QQmlPropertyBindingBase::kindOffset();
}

//  TargetData *QQmlPropertyBindingBase::targetData()
extern "C" Q_DECL_EXPORT
QQmlPropertyBindingBase::TargetData *ritual_ZN23QQmlPropertyBindingBase10targetDataEv(
    QQmlPropertyBindingBase *self) {
  return self->targetData();
}

//  const TargetData *QQmlPropertyBindingBase::targetData() const
extern "C" Q_DECL_EXPORT
const QQmlPropertyBindingBase::TargetData *ritual_ZNK23QQmlPropertyBindingBase10targetDataEv(
    const QQmlPropertyBindingBase *self) {
  return self->targetData();
}
