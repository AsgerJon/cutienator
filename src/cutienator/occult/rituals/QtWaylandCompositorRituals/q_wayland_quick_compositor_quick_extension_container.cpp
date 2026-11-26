//  Written by dev_tooling.RitualGenerator from the records of QtWaylandCompo
//  sitor/6.12.0/QtWaylandCompositor/private/qwaylandcompositorquickextension
//  s_p.h, Qt 6.12.0. Changes made here are lost.
#include <QtWaylandCompositor/qtwaylandcompositorglobal.h>
#include <QtWaylandCompositor/6.12.0/QtWaylandCompositor/private/qtwaylandcompositorglobal_p.h>
#if QT_CONFIG(wayland_compositor_quick)
#include <QtWaylandCompositor/6.12.0/QtWaylandCompositor/private/qtwaylandcompositorglobal_p.h>
#include <QtWaylandCompositor/QtWaylandCompositor>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWaylandCompositor/6.12.0/QtWaylandCompositor/private/qwaylandcompositorquickextensions_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtQml/QQmlListProperty>
#include <QtCore/QObject>
#include <QtWaylandCompositor/QWaylandCompositorExtension>

//  const QMetaObject
//      *QWaylandQuickCompositorQuickExtensionContainer::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK46QWaylandQuickCompositorQuickExtensionContainer10metaObjectEv(
    const QWaylandQuickCompositorQuickExtensionContainer *self) {
  return self->metaObject();
}

//  void *QWaylandQuickCompositorQuickExtensionContainer::qt_metacast(const
//      char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN46QWaylandQuickCompositorQuickExtensionContainer11qt_metacastEPKc(
    QWaylandQuickCompositorQuickExtensionContainer *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QWaylandQuickCompositorQuickExtensionContainer::qt_metacall(QMetaObje
//      ct::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN46QWaylandQuickCompositorQuickExtensionContainer11qt_metacallEN11QMetaObject4CallEiPPv(
    QWaylandQuickCompositorQuickExtensionContainer *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QWaylandQuickCompositorQuickExtensionContainer::tr(const char *s,
//      const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN46QWaylandQuickCompositorQuickExtensionContainer2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(
      QWaylandQuickCompositorQuickExtensionContainer::tr(
          s,
          c,
          n));
}

//  QQmlListProperty<QObject>
//      QWaylandQuickCompositorQuickExtensionContainer::data()
extern "C" Q_DECL_EXPORT
QQmlListProperty<QObject> *ritual_ZN46QWaylandQuickCompositorQuickExtensionContainer4dataEv(
    QWaylandQuickCompositorQuickExtensionContainer *self) {
  return new QQmlListProperty<QObject>(self->data());
}

//  QQmlListProperty<QWaylandCompositorExtension>
//      QWaylandQuickCompositorQuickExtensionContainer::extensions()
extern "C" Q_DECL_EXPORT
QQmlListProperty<QWaylandCompositorExtension> *ritual_ZN46QWaylandQuickCompositorQuickExtensionContainer10extensionsEv(
    QWaylandQuickCompositorQuickExtensionContainer *self) {
  return new QQmlListProperty<QWaylandCompositorExtension>(
      self->extensions());
}

//  qsizetype QWaylandQuickCompositorQuickExtensionContainer::countFunction(Q
//      QmlListProperty<QWaylandCompositorExtension> *list)
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZN46QWaylandQuickCompositorQuickExtensionContainer13countFunctionEP16QQmlListPropertyI27QWaylandCompositorExtensionE(
    QQmlListProperty<QWaylandCompositorExtension> *list) {
  return QWaylandQuickCompositorQuickExtensionContainer::countFunction(list);
}

//  QWaylandCompositorExtension *QWaylandQuickCompositorQuickExtensionContain
//      er::atFunction(QQmlListProperty<QWaylandCompositorExtension> *list,
//      qsizetype index)
extern "C" Q_DECL_EXPORT
QWaylandCompositorExtension *ritual_ZN46QWaylandQuickCompositorQuickExtensionContainer10atFunctionEP16QQmlListPropertyI27QWaylandCompositorExtensionEx(
    QQmlListProperty<QWaylandCompositorExtension> *list,
    qsizetype index) {
  return QWaylandQuickCompositorQuickExtensionContainer::atFunction(
      list,
      index);
}

//  void QWaylandQuickCompositorQuickExtensionContainer::append_extension(QQm
//      lListProperty<QWaylandCompositorExtension> *list,
//      QWaylandCompositorExtension *extension)
extern "C" Q_DECL_EXPORT
void ritual_ZN46QWaylandQuickCompositorQuickExtensionContainer16append_extensionEP16QQmlListPropertyI27QWaylandCompositorExtensionEPS1_(
    QQmlListProperty<QWaylandCompositorExtension> *list,
    QWaylandCompositorExtension *extension) {
  QWaylandQuickCompositorQuickExtensionContainer::append_extension(
      list,
      extension);
}

//  void QWaylandQuickCompositorQuickExtensionContainer::clearFunction(QQmlLi
//      stProperty<QWaylandCompositorExtension> *list)
extern "C" Q_DECL_EXPORT
void ritual_ZN46QWaylandQuickCompositorQuickExtensionContainer13clearFunctionEP16QQmlListPropertyI27QWaylandCompositorExtensionE(
    QQmlListProperty<QWaylandCompositorExtension> *list) {
  QWaylandQuickCompositorQuickExtensionContainer::clearFunction(list);
}

//  a QQmlListProperty<QObject> a ritual of
//      QWaylandQuickCompositorQuickExtensionContainer gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QWaylandQuickCompositorQuickExtensionContainer__QQmlListProperty_QObject(
    QQmlListProperty<QObject> *self) {
  delete self;
}

//  a QQmlListProperty<QWaylandCompositorExtension> a ritual of
//      QWaylandQuickCompositorQuickExtensionContainer gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QWaylandQuickCompositorQuickExtensionContainer__QQmlListProperty_QWaylandCompositorExtension(
    QQmlListProperty<QWaylandCompositorExtension> *self) {
  delete self;
}

#endif  // QT_CONFIG(wayland_compositor_quick)
