//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qqmlpropertybinding_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmlpropertybinding_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/qqmlscriptstring.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmlpropertyindex_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qproperty.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetatype.h>

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
