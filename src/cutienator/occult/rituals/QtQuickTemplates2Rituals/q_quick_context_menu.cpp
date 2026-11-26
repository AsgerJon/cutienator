//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickcontextmenu_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qtquicktemplates2global_p.h>
#include <QtQuickTemplates2/QtQuickTemplates2>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickcontextmenu_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qpoint.h>

//  Only a class built on QQuickContextMenu may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuickContextMenu : QQuickContextMenu {
  using QQuickContextMenu::event;
};

//  const QMetaObject *QQuickContextMenu::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK17QQuickContextMenu10metaObjectEv(
    const QQuickContextMenu *self) {
  return self->metaObject();
}

//  void *QQuickContextMenu::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN17QQuickContextMenu11qt_metacastEPKc(
    QQuickContextMenu *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickContextMenu::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN17QQuickContextMenu11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickContextMenu *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuickContextMenu::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN17QQuickContextMenu2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickContextMenu::tr(s, c, n));
}

//  void QQuickContextMenu::qt_qmlMarker_attached()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickContextMenu21qt_qmlMarker_attachedEv(
    QQuickContextMenu *self) {
  self->qt_qmlMarker_attached();
}

//  void QQuickContextMenu::qt_qmlMarker_uncreatable()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickContextMenu24qt_qmlMarker_uncreatableEv(
    QQuickContextMenu *self) {
  self->qt_qmlMarker_uncreatable();
}

//  QQuickContextMenu::QQuickContextMenu(QObject *parent)
extern "C" Q_DECL_EXPORT
QQuickContextMenu *ritual_ZN17QQuickContextMenuC1EP7QObject(
    QObject *parent) {
  return new QQuickContextMenu(parent);
}

//  QQuickContextMenu *QQuickContextMenu::qmlAttachedProperties(QObject
//      *object)
extern "C" Q_DECL_EXPORT
QQuickContextMenu *ritual_ZN17QQuickContextMenu21qmlAttachedPropertiesEP7QObject(
    QObject *object) {
  return QQuickContextMenu::qmlAttachedProperties(object);
}

//  QQuickMenu *QQuickContextMenu::menu() const
extern "C" Q_DECL_EXPORT
QQuickMenu *ritual_ZNK17QQuickContextMenu4menuEv(
    const QQuickContextMenu *self) {
  return self->menu();
}

//  void QQuickContextMenu::setMenu(QQuickMenu *menu)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickContextMenu7setMenuEP10QQuickMenu(
    QQuickContextMenu *self,
    QQuickMenu *menu) {
  self->setMenu(menu);
}

//  void QQuickContextMenu::menuChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickContextMenu11menuChangedEv(QQuickContextMenu *self) {
  self->menuChanged();
}

//  void QQuickContextMenu::requested(QPointF position)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickContextMenu9requestedE7QPointF(
    QQuickContextMenu *self,
    const QPointF *position) {
  self->requested(*position);
}

//  bool QQuickContextMenu::event(QEvent *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN17QQuickContextMenu5eventEP6QEvent(
    QQuickContextMenu *self,
    QEvent *a0) {
  return self->event(a0);
}

//  QQuickContextMenuPrivate *QQuickContextMenu::d_func()
extern "C" Q_DECL_EXPORT
QQuickContextMenuPrivate *ritual_ZN17QQuickContextMenu6d_funcEv(
    QQuickContextMenu *self) {
  return self->d_func();
}

//  const QQuickContextMenuPrivate *QQuickContextMenu::d_func() const
extern "C" Q_DECL_EXPORT
const QQuickContextMenuPrivate *ritual_ZNK17QQuickContextMenu6d_funcEv(
    const QQuickContextMenu *self) {
  return self->d_func();
}

//  void QQuickContextMenu::classBegin()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickContextMenu10classBeginEv(QQuickContextMenu *self) {
  self->classBegin();
}

//  void QQuickContextMenu::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickContextMenu17componentCompleteEv(
    QQuickContextMenu *self) {
  self->componentComplete();
}

//  QQuickContextMenu as the QQmlParserStatus it is built on
extern "C" Q_DECL_EXPORT
QQmlParserStatus *ritual_cast_QQuickContextMenu_QQmlParserStatus(
    QQuickContextMenu *self) {
  return static_cast<QQmlParserStatus *>(self);
}

//  bool QQuickContextMenu::event(QEvent *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN17QQuickContextMenu5eventEP6QEvent(
    QQuickContextMenu *self,
    QEvent *a0) {
  return static_cast<OwnQQuickContextMenu *>(self)->OwnQQuickContextMenu::event(
      a0);
}

//  void QQuickContextMenu::classBegin()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QQuickContextMenu10classBeginEv(
    QQuickContextMenu *self) {
  self->QQuickContextMenu::classBegin();
}

//  void QQuickContextMenu::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QQuickContextMenu17componentCompleteEv(
    QQuickContextMenu *self) {
  self->QQuickContextMenu::componentComplete();
}
