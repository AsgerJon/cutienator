//  Written by dev_tooling.RitualGenerator from the records of
//  QtQmlModels/6.12.0/QtQmlModels/private/qqmldelegatecomponent_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQmlModels/qtqmlmodelsglobal.h>
#include <QtQmlModels/6.12.0/QtQmlModels/private/qtqmlmodelsglobal_p.h>
#if QT_CONFIG(qml_delegate_model)
#include <QtQmlModels/6.12.0/QtQmlModels/private/qtqmlmodelsglobal_p.h>
#include <QtQmlModels/QtQmlModels>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQmlModels/6.12.0/QtQmlModels/private/qqmldelegatecomponent_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qvariant.h>

//  const QMetaObject *QQmlDelegateChoice::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK18QQmlDelegateChoice10metaObjectEv(
    const QQmlDelegateChoice *self) {
  return self->metaObject();
}

//  QString QQmlDelegateChoice::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN18QQmlDelegateChoice2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQmlDelegateChoice::tr(s, c, n));
}

//  QVariant QQmlDelegateChoice::roleValue() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK18QQmlDelegateChoice9roleValueEv(
    const QQmlDelegateChoice *self) {
  return new QVariant(self->roleValue());
}

//  void QQmlDelegateChoice::setRoleValue(const QVariant &roleValue)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQmlDelegateChoice12setRoleValueERK8QVariant(
    QQmlDelegateChoice *self,
    const QVariant *roleValue) {
  self->setRoleValue(*roleValue);
}

//  int QQmlDelegateChoice::row() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK18QQmlDelegateChoice3rowEv(const QQmlDelegateChoice *self) {
  return self->row();
}

//  void QQmlDelegateChoice::setRow(int r)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQmlDelegateChoice6setRowEi(
    QQmlDelegateChoice *self,
    int r) {
  self->setRow(r);
}

//  int QQmlDelegateChoice::column() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK18QQmlDelegateChoice6columnEv(const QQmlDelegateChoice *self) {
  return self->column();
}

//  void QQmlDelegateChoice::setColumn(int c)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQmlDelegateChoice9setColumnEi(
    QQmlDelegateChoice *self,
    int c) {
  self->setColumn(c);
}

//  QQmlComponent *QQmlDelegateChoice::delegate() const
extern "C" Q_DECL_EXPORT
QQmlComponent *ritual_ZNK18QQmlDelegateChoice8delegateEv(
    const QQmlDelegateChoice *self) {
  return self->delegate();
}

//  void QQmlDelegateChoice::setDelegate(QQmlComponent *delegate)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQmlDelegateChoice11setDelegateEP13QQmlComponent(
    QQmlDelegateChoice *self,
    QQmlComponent *delegate) {
  self->setDelegate(delegate);
}

//  bool QQmlDelegateChoice::match(int row, int column, const QVariant
//      &value) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QQmlDelegateChoice5matchEiiRK8QVariant(
    const QQmlDelegateChoice *self,
    int row,
    int column,
    const QVariant *value) {
  return self->match(row, column, *value);
}

//  bool QQmlDelegateChoice::match(int row, int column, const QVariant
//      &value) const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK18QQmlDelegateChoice5matchEiiRK8QVariant(
    const QQmlDelegateChoice *self,
    int row,
    int column,
    const QVariant *value) {
  return self->QQmlDelegateChoice::match(row, column, *value);
}

#endif  // QT_CONFIG(qml_delegate_model)
