//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickstate_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickstate_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qvariant.h>
#include <QtQml/QtQml>
#include <QtQml/qqmlproperty.h>
#include <QtCore/qlist.h>

//  QQuickStateAction::QQuickStateAction()
extern "C" Q_DECL_EXPORT
QQuickStateAction *ritual_ZN17QQuickStateActionC1Ev() {
  return new QQuickStateAction();
}

//  QQuickStateAction::QQuickStateAction(QObject *a0, const QString &a1,
//      const QVariant &a2)
extern "C" Q_DECL_EXPORT
QQuickStateAction *ritual_ZN17QQuickStateActionC1EP7QObjectRK7QStringRK8QVariant(
    QObject *a0,
    const QString *a1,
    const QVariant *a2) {
  return new QQuickStateAction(a0, *a1, *a2);
}

//  QQuickStateAction::QQuickStateAction(QObject *a0, const QQmlProperty
//      &property, const QString &a2, const QVariant &a3)
extern "C" Q_DECL_EXPORT
QQuickStateAction *ritual_ZN17QQuickStateActionC1EP7QObjectRK12QQmlPropertyRK7QStringRK8QVariant(
    QObject *a0,
    const QQmlProperty *property,
    const QString *a2,
    const QVariant *a3) {
  return new QQuickStateAction(a0, *property, *a2, *a3);
}

//  void QQuickStateAction::deleteFromBinding()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickStateAction17deleteFromBindingEv(
    QQuickStateAction *self) {
  self->deleteFromBinding();
}

//  QQuickStateAction::~QQuickStateAction()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickStateActionD1Ev(QQuickStateAction *self) {
  delete self;
}

//  QList<QQuickStateAction>::QList()
extern "C" Q_DECL_EXPORT
QList<QQuickStateAction> *ritual_list_make_QQuickStateAction() {
  return new QList<QQuickStateAction>();
}

//  void QList<QQuickStateAction>::append(const QQuickStateAction &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QQuickStateAction(
    QList<QQuickStateAction> *self,
    const QQuickStateAction *element) {
  self->append(*element);
}

//  qsizetype QList<QQuickStateAction>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QQuickStateAction(
    const QList<QQuickStateAction> *self) {
  return self->size();
}

//  const QQuickStateAction &QList<QQuickStateAction>::at(qsizetype i) const
extern "C" Q_DECL_EXPORT
QQuickStateAction *ritual_list_at_QQuickStateAction(
    const QList<QQuickStateAction> *self,
    long long index) {
  return new QQuickStateAction(self->at(index));
}

//  QList<QQuickStateAction>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QQuickStateAction(QList<QQuickStateAction> *self) {
  delete self;
}
