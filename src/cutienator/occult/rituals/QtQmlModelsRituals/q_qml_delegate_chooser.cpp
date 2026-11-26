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
#include <QtQml/QQmlListProperty>

//  const QMetaObject *QQmlDelegateChooser::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK19QQmlDelegateChooser10metaObjectEv(
    const QQmlDelegateChooser *self) {
  return self->metaObject();
}

//  void *QQmlDelegateChooser::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN19QQmlDelegateChooser11qt_metacastEPKc(
    QQmlDelegateChooser *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQmlDelegateChooser::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN19QQmlDelegateChooser11qt_metacallEN11QMetaObject4CallEiPPv(
    QQmlDelegateChooser *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
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

//  QQmlListProperty<QQmlDelegateChoice> QQmlDelegateChooser::choices()
extern "C" Q_DECL_EXPORT
QQmlListProperty<QQmlDelegateChoice> *ritual_ZN19QQmlDelegateChooser7choicesEv(
    QQmlDelegateChooser *self) {
  return new QQmlListProperty<QQmlDelegateChoice>(self->choices());
}

//  void
//      QQmlDelegateChooser::choices_append(QQmlListProperty<QQmlDelegateChoi
//      ce> *a0, QQmlDelegateChoice *a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlDelegateChooser14choices_appendEP16QQmlListPropertyI18QQmlDelegateChoiceEPS1_(
    QQmlListProperty<QQmlDelegateChoice> *a0,
    QQmlDelegateChoice *a1) {
  QQmlDelegateChooser::choices_append(a0, a1);
}

//  qsizetype
//      QQmlDelegateChooser::choices_count(QQmlListProperty<QQmlDelegateChoic
//      e> *a0)
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZN19QQmlDelegateChooser13choices_countEP16QQmlListPropertyI18QQmlDelegateChoiceE(
    QQmlListProperty<QQmlDelegateChoice> *a0) {
  return QQmlDelegateChooser::choices_count(a0);
}

//  QQmlDelegateChoice
//      *QQmlDelegateChooser::choices_at(QQmlListProperty<QQmlDelegateChoice>
//      *a0, qsizetype a1)
extern "C" Q_DECL_EXPORT
QQmlDelegateChoice *ritual_ZN19QQmlDelegateChooser10choices_atEP16QQmlListPropertyI18QQmlDelegateChoiceEx(
    QQmlListProperty<QQmlDelegateChoice> *a0,
    qsizetype a1) {
  return QQmlDelegateChooser::choices_at(a0, a1);
}

//  void
//      QQmlDelegateChooser::choices_clear(QQmlListProperty<QQmlDelegateChoic
//      e> *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlDelegateChooser13choices_clearEP16QQmlListPropertyI18QQmlDelegateChoiceE(
    QQmlListProperty<QQmlDelegateChoice> *a0) {
  QQmlDelegateChooser::choices_clear(a0);
}

//  void
//      QQmlDelegateChooser::choices_replace(QQmlListProperty<QQmlDelegateCho
//      ice> *a0, qsizetype a1, QQmlDelegateChoice *a2)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlDelegateChooser15choices_replaceEP16QQmlListPropertyI18QQmlDelegateChoiceExPS1_(
    QQmlListProperty<QQmlDelegateChoice> *a0,
    qsizetype a1,
    QQmlDelegateChoice *a2) {
  QQmlDelegateChooser::choices_replace(a0, a1, a2);
}

//  void QQmlDelegateChooser::choices_removeLast(QQmlListProperty<QQmlDelegat
//      eChoice> *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlDelegateChooser18choices_removeLastEP16QQmlListPropertyI18QQmlDelegateChoiceE(
    QQmlListProperty<QQmlDelegateChoice> *a0) {
  QQmlDelegateChooser::choices_removeLast(a0);
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

//  void QQmlDelegateChooser::roleChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlDelegateChooser11roleChangedEv(
    QQmlDelegateChooser *self) {
  self->roleChanged();
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

//  a QQmlListProperty<QQmlDelegateChoice> a ritual of QQmlDelegateChooser
//      gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QQmlDelegateChooser__QQmlListProperty_QQmlDelegateChoice(
    QQmlListProperty<QQmlDelegateChoice> *self) {
  delete self;
}

#endif  // QT_CONFIG(qml_delegate_model)
#endif  // QT_CONFIG(qml_delegate_model)
