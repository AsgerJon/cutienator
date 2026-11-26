//  Written by dev_tooling.RitualGenerator from the records of
//  QtScxmlQml/6.12.0/QtScxmlQml/private/statemachineextended_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtScxmlQml/6.12.0/QtScxmlQml/private/qscxmlqmlglobals_p.h>
#include <QtScxmlQml/QtScxmlQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtScxmlQml/6.12.0/QtScxmlQml/private/statemachineextended_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtQml/QQmlListProperty>
#include <QtCore/QObject>

//  const QMetaObject *QScxmlStateMachineExtended::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK26QScxmlStateMachineExtended10metaObjectEv(
    const QScxmlStateMachineExtended *self) {
  return self->metaObject();
}

//  void *QScxmlStateMachineExtended::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN26QScxmlStateMachineExtended11qt_metacastEPKc(
    QScxmlStateMachineExtended *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QScxmlStateMachineExtended::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN26QScxmlStateMachineExtended11qt_metacallEN11QMetaObject4CallEiPPv(
    QScxmlStateMachineExtended *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QScxmlStateMachineExtended::tr(const char *s, const char *c, int
//      n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN26QScxmlStateMachineExtended2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QScxmlStateMachineExtended::tr(s, c, n));
}

//  QScxmlStateMachineExtended::QScxmlStateMachineExtended(QObject *extendee)
extern "C" Q_DECL_EXPORT
QScxmlStateMachineExtended *ritual_ZN26QScxmlStateMachineExtendedC1EP7QObject(
    QObject *extendee) {
  return new QScxmlStateMachineExtended(extendee);
}

//  QQmlListProperty<QObject> QScxmlStateMachineExtended::children()
extern "C" Q_DECL_EXPORT
QQmlListProperty<QObject> *ritual_ZN26QScxmlStateMachineExtended8childrenEv(
    QScxmlStateMachineExtended *self) {
  return new QQmlListProperty<QObject>(self->children());
}

//  a QQmlListProperty<QObject> a ritual of QScxmlStateMachineExtended gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QScxmlStateMachineExtended__QQmlListProperty_QObject(
    QQmlListProperty<QObject> *self) {
  delete self;
}
