//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickdesignersupportitems_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQuick/qtquickglobal.h>
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#if QT_CONFIG(quick_designer)
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickdesignersupportitems_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qtyperevision.h>
#include <QtCore/qurl.h>

//  QObject *QQuickDesignerSupportItems::createPrimitive(const QString
//      &typeName, QTypeRevision version, QQmlContext *context)
extern "C" Q_DECL_EXPORT
QObject *ritual_ZN26QQuickDesignerSupportItems15createPrimitiveERK7QString13QTypeRevisionP11QQmlContext(
    const QString *typeName,
    const QTypeRevision *version,
    QQmlContext *context) {
  return QQuickDesignerSupportItems::createPrimitive(
      *typeName,
      *version,
      context);
}

//  QObject *QQuickDesignerSupportItems::createComponent(const QUrl
//      &componentUrl, QQmlContext *context)
extern "C" Q_DECL_EXPORT
QObject *ritual_ZN26QQuickDesignerSupportItems15createComponentERK4QUrlP11QQmlContext(
    const QUrl *componentUrl,
    QQmlContext *context) {
  return QQuickDesignerSupportItems::createComponent(*componentUrl, context);
}

//  void QQuickDesignerSupportItems::tweakObjects(QObject *object)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuickDesignerSupportItems12tweakObjectsEP7QObject(
    QObject *object) {
  QQuickDesignerSupportItems::tweakObjects(object);
}

//  bool QQuickDesignerSupportItems::objectWasDeleted(QObject *object)
extern "C" Q_DECL_EXPORT
bool ritual_ZN26QQuickDesignerSupportItems16objectWasDeletedEP7QObject(
    QObject *object) {
  return QQuickDesignerSupportItems::objectWasDeleted(object);
}

//  void QQuickDesignerSupportItems::disableNativeTextRendering(QQuickItem
//      *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuickDesignerSupportItems26disableNativeTextRenderingEP10QQuickItem(
    QQuickItem *item) {
  QQuickDesignerSupportItems::disableNativeTextRendering(item);
}

//  void QQuickDesignerSupportItems::disableTextCursor(QQuickItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuickDesignerSupportItems17disableTextCursorEP10QQuickItem(
    QQuickItem *item) {
  QQuickDesignerSupportItems::disableTextCursor(item);
}

//  void QQuickDesignerSupportItems::disableTransition(QObject *object)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuickDesignerSupportItems17disableTransitionEP7QObject(
    QObject *object) {
  QQuickDesignerSupportItems::disableTransition(object);
}

//  void QQuickDesignerSupportItems::disableBehaivour(QObject *object)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuickDesignerSupportItems16disableBehaivourEP7QObject(
    QObject *object) {
  QQuickDesignerSupportItems::disableBehaivour(object);
}

//  void QQuickDesignerSupportItems::stopUnifiedTimer()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuickDesignerSupportItems16stopUnifiedTimerEv() {
  QQuickDesignerSupportItems::stopUnifiedTimer();
}

//  void QQuickDesignerSupportItems::registerFixResourcePathsForObjectCallBac
//      k(void (*)(QObject *) callback)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuickDesignerSupportItems41registerFixResourcePathsForObjectCallBackEPFvP7QObjectE(
    void *callback) {
  QQuickDesignerSupportItems::registerFixResourcePathsForObjectCallBack(
      reinterpret_cast<void (*)(QObject *)>(callback));
}

//  QQuickDesignerSupportItems::~QQuickDesignerSupportItems()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuickDesignerSupportItemsD1Ev(
    QQuickDesignerSupportItems *self) {
  delete self;
}

#endif  // QT_CONFIG(quick_designer)
