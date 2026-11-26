//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qqmlpropertybinding_p.h, Qt 6.12.0. Edited by
//  hand on 2026-11-25: added by hand, instances of templates of the class:
//  10. Kept as it is when the generator runs again.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmlpropertybinding_p.h>
#include <QtQml/6.12.0/QtQml/private/qqmlpropertyindex_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qproperty.h>
#include <QtCore/qmetatype.h>
#include <QtCore/qstring.h>
#include <QtQml/qqmlscriptstring.h>

//  std::size_t QQmlPropertyBinding::jsExpressionOffsetLength()
extern "C" Q_DECL_EXPORT
std::size_t ritual_ZN19QQmlPropertyBinding24jsExpressionOffsetLengthEv() {
  return QQmlPropertyBinding::jsExpressionOffsetLength();
}

//  QQmlPropertyBindingJS *QQmlPropertyBinding::jsExpression()
extern "C" Q_DECL_EXPORT
QQmlPropertyBindingJS *ritual_ZN19QQmlPropertyBinding12jsExpressionEv(
    QQmlPropertyBinding *self) {
  return self->jsExpression();
}

//  const QQmlPropertyBindingJS *QQmlPropertyBinding::jsExpression() const
extern "C" Q_DECL_EXPORT
const QQmlPropertyBindingJS *ritual_ZNK19QQmlPropertyBinding12jsExpressionEv(
    const QQmlPropertyBinding *self) {
  return self->jsExpression();
}

//  QUntypedPropertyBinding QQmlPropertyBinding::create(const
//      QQmlPropertyData *pd, QV4::Function *function, QObject *obj, const
//      QQmlRefPointer<QQmlContextData> &ctxt, QV4::ExecutionContext *scope,
//      QObject *target, QQmlPropertyIndex targetIndex)
extern "C" Q_DECL_EXPORT
QUntypedPropertyBinding *ritual_ZN19QQmlPropertyBinding6createEPK16QQmlPropertyDataPN3QV48FunctionEP7QObjectRK14QQmlRefPointerI15QQmlContextDataEPNS3_16ExecutionContextES7_17QQmlPropertyIndex(
    const QQmlPropertyData *pd,
    QV4::Function *function,
    QObject *obj,
    const QQmlRefPointer<QQmlContextData> *ctxt,
    QV4::ExecutionContext *scope,
    QObject *target,
    const QQmlPropertyIndex *targetIndex) {
  return new QUntypedPropertyBinding(
      QQmlPropertyBinding::create(
          pd,
          function,
          obj,
          *ctxt,
          scope,
          target,
          *targetIndex));
}

//  QUntypedPropertyBinding QQmlPropertyBinding::create(QMetaType
//      propertyType, QV4::Function *function, QObject *obj, const
//      QQmlRefPointer<QQmlContextData> &ctxt, QV4::ExecutionContext *scope,
//      QObject *target, QQmlPropertyIndex targetIndex)
extern "C" Q_DECL_EXPORT
QUntypedPropertyBinding *ritual_ZN19QQmlPropertyBinding6createE9QMetaTypePN3QV48FunctionEP7QObjectRK14QQmlRefPointerI15QQmlContextDataEPNS1_16ExecutionContextES5_17QQmlPropertyIndex(
    const QMetaType *propertyType,
    QV4::Function *function,
    QObject *obj,
    const QQmlRefPointer<QQmlContextData> *ctxt,
    QV4::ExecutionContext *scope,
    QObject *target,
    const QQmlPropertyIndex *targetIndex) {
  return new QUntypedPropertyBinding(
      QQmlPropertyBinding::create(
          *propertyType,
          function,
          obj,
          *ctxt,
          scope,
          target,
          *targetIndex));
}

//  QUntypedPropertyBinding QQmlPropertyBinding::createFromCodeString(const
//      QQmlPropertyData *property, const QString &str, QObject *obj, const
//      QQmlRefPointer<QQmlContextData> &ctxt, const QString &url, quint16
//      lineNumber, QObject *target, QQmlPropertyIndex targetIndex)
extern "C" Q_DECL_EXPORT
QUntypedPropertyBinding *ritual_ZN19QQmlPropertyBinding20createFromCodeStringEPK16QQmlPropertyDataRK7QStringP7QObjectRK14QQmlRefPointerI15QQmlContextDataES5_tS7_17QQmlPropertyIndex(
    const QQmlPropertyData *property,
    const QString *str,
    QObject *obj,
    const QQmlRefPointer<QQmlContextData> *ctxt,
    const QString *url,
    quint16 lineNumber,
    QObject *target,
    const QQmlPropertyIndex *targetIndex) {
  return new QUntypedPropertyBinding(
      QQmlPropertyBinding::createFromCodeString(
          property,
          *str,
          obj,
          *ctxt,
          *url,
          lineNumber,
          target,
          *targetIndex));
}

//  QUntypedPropertyBinding QQmlPropertyBinding::createFromScriptString(const
//      QQmlPropertyData *property, const QQmlScriptString &script, QObject
//      *obj, QQmlContext *ctxt, QObject *target, QQmlPropertyIndex
//      targetIndex)
extern "C" Q_DECL_EXPORT
QUntypedPropertyBinding *ritual_ZN19QQmlPropertyBinding22createFromScriptStringEPK16QQmlPropertyDataRK16QQmlScriptStringP7QObjectP11QQmlContextS7_17QQmlPropertyIndex(
    const QQmlPropertyData *property,
    const QQmlScriptString *script,
    QObject *obj,
    QQmlContext *ctxt,
    QObject *target,
    const QQmlPropertyIndex *targetIndex) {
  return new QUntypedPropertyBinding(
      QQmlPropertyBinding::createFromScriptString(
          property,
          *script,
          obj,
          ctxt,
          target,
          *targetIndex));
}

//  QUntypedPropertyBinding
//      QQmlPropertyBinding::createFromBoundFunction(const QQmlPropertyData
//      *pd, QV4::BoundFunction *function, QObject *obj, const
//      QQmlRefPointer<QQmlContextData> &ctxt, QV4::ExecutionContext *scope,
//      QObject *target, QQmlPropertyIndex targetIndex)
extern "C" Q_DECL_EXPORT
QUntypedPropertyBinding *ritual_ZN19QQmlPropertyBinding23createFromBoundFunctionEPK16QQmlPropertyDataPN3QV413BoundFunctionEP7QObjectRK14QQmlRefPointerI15QQmlContextDataEPNS3_16ExecutionContextES7_17QQmlPropertyIndex(
    const QQmlPropertyData *pd,
    QV4::BoundFunction *function,
    QObject *obj,
    const QQmlRefPointer<QQmlContextData> *ctxt,
    QV4::ExecutionContext *scope,
    QObject *target,
    const QQmlPropertyIndex *targetIndex) {
  return new QUntypedPropertyBinding(
      QQmlPropertyBinding::createFromBoundFunction(
          pd,
          function,
          obj,
          *ctxt,
          scope,
          target,
          *targetIndex));
}

//  bool QQmlPropertyBinding::isUndefined(const QUntypedPropertyBinding
//      &binding)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QQmlPropertyBinding11isUndefinedERK23QUntypedPropertyBinding(
    const QUntypedPropertyBinding *binding) {
  return QQmlPropertyBinding::isUndefined(*binding);
}

//  bool QQmlPropertyBinding::isUndefined(const QPropertyBindingPrivate
//      *binding)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QQmlPropertyBinding11isUndefinedEPK23QPropertyBindingPrivate(
    const QPropertyBindingPrivate *binding) {
  return QQmlPropertyBinding::isUndefined(binding);
}

//  bool QQmlPropertyBinding::hasDependencies() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QQmlPropertyBinding15hasDependenciesEv(
    const QQmlPropertyBinding *self) {
  return self->hasDependencies();
}

//  void QQmlPropertyBinding::handleUndefinedAssignment(QQmlEnginePrivate
//      *ep, void *dataPtr)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlPropertyBinding25handleUndefinedAssignmentEP17QQmlEnginePrivatePv(
    QQmlPropertyBinding *self,
    QQmlEnginePrivate *ep,
    void *dataPtr) {
  self->handleUndefinedAssignment(ep, dataPtr);
}

//  QString QQmlPropertyBinding::createBindingLoopErrorDescription()
extern "C" Q_DECL_EXPORT
QString *ritual_ZN19QQmlPropertyBinding33createBindingLoopErrorDescriptionEv(
    QQmlPropertyBinding *self) {
  return new QString(self->createBindingLoopErrorDescription());
}

//  QQmlPropertyBinding::QQmlPropertyBinding(QMetaType metaType, QObject
//      *target, QQmlPropertyIndex targetIndex, HasBoundFunction
//      hasBoundFunction)
extern "C" Q_DECL_EXPORT
QQmlPropertyBinding *ritual_ZN19QQmlPropertyBindingC1E9QMetaTypeP7QObject17QQmlPropertyIndexN23QQmlPropertyBindingBase16HasBoundFunctionE(
    const QMetaType *metaType,
    QObject *target,
    const QQmlPropertyIndex *targetIndex,
    QQmlPropertyBindingBase::HasBoundFunction hasBoundFunction) {
  return new QQmlPropertyBinding(
      *metaType,
      target,
      *targetIndex,
      hasBoundFunction);
}

//  QUntypedPropertyBinding
//      QQmlPropertyBinding::makeUntyped(QQmlPropertyBinding *binding)
extern "C" Q_DECL_EXPORT
QUntypedPropertyBinding *ritual_ZN19QQmlPropertyBinding11makeUntypedEPS_(
    QQmlPropertyBinding *binding) {
  return new QUntypedPropertyBinding(
      QQmlPropertyBinding::makeUntyped(
          binding));
}

//  void QQmlPropertyBinding::bindingErrorCallback(QPropertyBindingPrivate
//      *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlPropertyBinding20bindingErrorCallbackEP23QPropertyBindingPrivate(
    QPropertyBindingPrivate *a0) {
  QQmlPropertyBinding::bindingErrorCallback(a0);
}

//  static bool QQmlPropertyBinding::doEvaluate<QMetaType::QObjectStar>(
//      QMetaType metaType, QUntypedPropertyData *dataPtr, void *f)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QQmlPropertyBinding10doEvaluateILN9QMetaType4TypeE39EEEbS1_P20QUntypedPropertyDataPv(
    const QMetaType *metaType,
    QUntypedPropertyData *dataPtr,
    void *f) {
  return QQmlPropertyBinding::doEvaluate<QMetaType::QObjectStar>(
      *metaType, dataPtr, f);
}

//  static bool QQmlPropertyBinding::doEvaluate<QMetaType::Bool>(QMetaType
//      metaType, QUntypedPropertyData *dataPtr, void *f)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QQmlPropertyBinding10doEvaluateILN9QMetaType4TypeE1EEEbS1_P20QUntypedPropertyDataPv(
    const QMetaType *metaType,
    QUntypedPropertyData *dataPtr,
    void *f) {
  return QQmlPropertyBinding::doEvaluate<QMetaType::Bool>(
      *metaType, dataPtr, f);
}

//  static bool QQmlPropertyBinding::doEvaluate<QMetaType::Int>(QMetaType
//      metaType, QUntypedPropertyData *dataPtr, void *f)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QQmlPropertyBinding10doEvaluateILN9QMetaType4TypeE2EEEbS1_P20QUntypedPropertyDataPv(
    const QMetaType *metaType,
    QUntypedPropertyData *dataPtr,
    void *f) {
  return QQmlPropertyBinding::doEvaluate<QMetaType::Int>(
      *metaType, dataPtr, f);
}

//  static bool QQmlPropertyBinding::doEvaluate<QMetaType::Double>(QMetaType
//      metaType, QUntypedPropertyData *dataPtr, void *f)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QQmlPropertyBinding10doEvaluateILN9QMetaType4TypeE6EEEbS1_P20QUntypedPropertyDataPv(
    const QMetaType *metaType,
    QUntypedPropertyData *dataPtr,
    void *f) {
  return QQmlPropertyBinding::doEvaluate<QMetaType::Double>(
      *metaType, dataPtr, f);
}

//  static bool QQmlPropertyBinding::doEvaluate<QMetaType::QString>(QMetaType
//      metaType, QUntypedPropertyData *dataPtr, void *f)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QQmlPropertyBinding10doEvaluateILN9QMetaType4TypeE10EEEbS1_P20QUntypedPropertyDataPv(
    const QMetaType *metaType,
    QUntypedPropertyData *dataPtr,
    void *f) {
  return QQmlPropertyBinding::doEvaluate<QMetaType::QString>(
      *metaType, dataPtr, f);
}

//  bool QQmlPropertyBinding::evaluate<QMetaType::QObjectStar>(QMetaType
//      metaType, void *dataPtr)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QQmlPropertyBinding8evaluateILN9QMetaType4TypeE39EEEbS1_Pv(
    QQmlPropertyBinding *self,
    const QMetaType *metaType,
    void *dataPtr) {
  return self->evaluate<QMetaType::QObjectStar>(*metaType, dataPtr);
}

//  bool QQmlPropertyBinding::evaluate<QMetaType::Bool>(QMetaType metaType,
//      void *dataPtr)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QQmlPropertyBinding8evaluateILN9QMetaType4TypeE1EEEbS1_Pv(
    QQmlPropertyBinding *self,
    const QMetaType *metaType,
    void *dataPtr) {
  return self->evaluate<QMetaType::Bool>(*metaType, dataPtr);
}

//  bool QQmlPropertyBinding::evaluate<QMetaType::Int>(QMetaType metaType,
//      void *dataPtr)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QQmlPropertyBinding8evaluateILN9QMetaType4TypeE2EEEbS1_Pv(
    QQmlPropertyBinding *self,
    const QMetaType *metaType,
    void *dataPtr) {
  return self->evaluate<QMetaType::Int>(*metaType, dataPtr);
}

//  bool QQmlPropertyBinding::evaluate<QMetaType::Double>(QMetaType metaType,
//      void *dataPtr)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QQmlPropertyBinding8evaluateILN9QMetaType4TypeE6EEEbS1_Pv(
    QQmlPropertyBinding *self,
    const QMetaType *metaType,
    void *dataPtr) {
  return self->evaluate<QMetaType::Double>(*metaType, dataPtr);
}

//  bool QQmlPropertyBinding::evaluate<QMetaType::QString>(QMetaType
//      metaType, void *dataPtr)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QQmlPropertyBinding8evaluateILN9QMetaType4TypeE10EEEbS1_Pv(
    QQmlPropertyBinding *self,
    const QMetaType *metaType,
    void *dataPtr) {
  return self->evaluate<QMetaType::QString>(*metaType, dataPtr);
}
