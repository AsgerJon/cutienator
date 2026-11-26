//  Written by dev_tooling.RitualGenerator from the records of
//  QtDesigner/6.12.0/QtDesigner/private/zoomwidget_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtDesigner/QtDesigner>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDesigner/6.12.0/QtDesigner/private/zoomwidget_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/QList>

//  const QMetaObject *qdesigner_internal::ZoomMenu::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK18qdesigner_internal8ZoomMenu10metaObjectEv(
    const qdesigner_internal::ZoomMenu *self) {
  return self->metaObject();
}

//  void *qdesigner_internal::ZoomMenu::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN18qdesigner_internal8ZoomMenu11qt_metacastEPKc(
    qdesigner_internal::ZoomMenu *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int qdesigner_internal::ZoomMenu::qt_metacall(QMetaObject::Call a0, int
//      a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN18qdesigner_internal8ZoomMenu11qt_metacallEN11QMetaObject4CallEiPPv(
    qdesigner_internal::ZoomMenu *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString qdesigner_internal::ZoomMenu::tr(const char *s, const char *c,
//      int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN18qdesigner_internal8ZoomMenu2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(qdesigner_internal::ZoomMenu::tr(s, c, n));
}

//  qdesigner_internal::ZoomMenu::ZoomMenu(QObject *parent)
extern "C" Q_DECL_EXPORT
qdesigner_internal::ZoomMenu *ritual_ZN18qdesigner_internal8ZoomMenuC1EP7QObject(
    QObject *parent) {
  return new qdesigner_internal::ZoomMenu(parent);
}

//  void qdesigner_internal::ZoomMenu::addActions(QMenu *m)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal8ZoomMenu10addActionsEP5QMenu(
    qdesigner_internal::ZoomMenu *self,
    QMenu *m) {
  self->addActions(m);
}

//  int qdesigner_internal::ZoomMenu::zoom() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK18qdesigner_internal8ZoomMenu4zoomEv(
    const qdesigner_internal::ZoomMenu *self) {
  return self->zoom();
}

//  QList<int> qdesigner_internal::ZoomMenu::zoomValues()
extern "C" Q_DECL_EXPORT
QList<int> *ritual_ZN18qdesigner_internal8ZoomMenu10zoomValuesEv() {
  return new QList<int>(qdesigner_internal::ZoomMenu::zoomValues());
}

//  void qdesigner_internal::ZoomMenu::setZoom(int percent)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal8ZoomMenu7setZoomEi(
    qdesigner_internal::ZoomMenu *self,
    int percent) {
  self->setZoom(percent);
}

//  void qdesigner_internal::ZoomMenu::zoomChanged(int a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal8ZoomMenu11zoomChangedEi(
    qdesigner_internal::ZoomMenu *self,
    int a0) {
  self->zoomChanged(a0);
}

//  void qdesigner_internal::ZoomMenu::slotZoomMenu(QAction *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal8ZoomMenu12slotZoomMenuEP7QAction(
    qdesigner_internal::ZoomMenu *self,
    QAction *a0) {
  self->slotZoomMenu(a0);
}

//  int qdesigner_internal::ZoomMenu::zoomOf(const QAction *a)
extern "C" Q_DECL_EXPORT
int ritual_ZN18qdesigner_internal8ZoomMenu6zoomOfEPK7QAction(
    const QAction *a) {
  return qdesigner_internal::ZoomMenu::zoomOf(a);
}

//  a QList<int> a ritual of qdesigner_internal::ZoomMenu gave
extern "C" Q_DECL_EXPORT
void ritual_drop_qdesigner_internal_ZoomMenu__QList_int(QList<int> *self) {
  delete self;
}
