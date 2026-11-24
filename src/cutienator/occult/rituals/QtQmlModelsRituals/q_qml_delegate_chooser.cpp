//  Written by dev_tooling.RitualGenerator from the records of
//  QtQmlModels/6.12.0/QtQmlModels/private/qqmldelegatecomponent_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQmlModels/qtqmlmodelsglobal.h>
#include <QtQmlModels/6.12.0/QtQmlModels/private/qtqmlmodelsglobal_p.h>
#if QT_CONFIG(qml_delegate_model)
#if QT_CONFIG(qml_delegate_model)
#include <QtQmlModels/6.12.0/QtQmlModels/private/qtqmlmodelsglobal_p.h>
#include <QtQmlModels/QtQmlModels>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQmlModels/6.12.0/QtQmlModels/private/qqmldelegatecomponent_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>

//  const QMetaObject *QQmlDelegateChooser::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK19QQmlDelegateChooser10metaObjectEv(
    const QQmlDelegateChooser *self) {
  return self->metaObject();
}

//  QString QQmlDelegateChooser::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN19QQmlDelegateChooser2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQmlDelegateChooser::tr(s, c, n));
}

//  QString QQmlDelegateChooser::role() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK19QQmlDelegateChooser4roleEv(
    const QQmlDelegateChooser *self) {
  return new QString(self->role());
}

//  void QQmlDelegateChooser::setRole(const QString &role)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlDelegateChooser7setRoleERK7QString(
    QQmlDelegateChooser *self,
    const QString *role) {
  self->setRole(*role);
}

//  QQmlComponent *QQmlDelegateChooser::delegate(QQmlAdaptorModel
//      *adaptorModel, int row, int column) const
extern "C" Q_DECL_EXPORT
QQmlComponent *ritual_ZNK19QQmlDelegateChooser8delegateEP16QQmlAdaptorModelii(
    const QQmlDelegateChooser *self,
    QQmlAdaptorModel *adaptorModel,
    int row,
    int column) {
  return self->delegate(adaptorModel, row, column);
}

//  QQmlComponent *QQmlDelegateChooser::delegate(QQmlAdaptorModel
//      *adaptorModel, int row, int column) const
extern "C" Q_DECL_EXPORT
QQmlComponent *ritual_own_ZNK19QQmlDelegateChooser8delegateEP16QQmlAdaptorModelii(
    const QQmlDelegateChooser *self,
    QQmlAdaptorModel *adaptorModel,
    int row,
    int column) {
  return self->QQmlDelegateChooser::delegate(adaptorModel, row, column);
}

#endif  // QT_CONFIG(qml_delegate_model)
#endif  // QT_CONFIG(qml_delegate_model)
