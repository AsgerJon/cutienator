//  Written by dev_tooling.RitualGenerator from the records of QtQuickControl
//  s2Impl/6.12.0/QtQuickControls2Impl/private/qquicktumblerview_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuickControls2Impl/qtquickcontrols2implexports.h>
#include <QtQuickControls2Impl/6.12.0/QtQuickControls2Impl/private/qtquickcontrols2implglobal_p.h>
#if QT_CONFIG(quick_listview) && QT_CONFIG(quick_pathview)
#include <QtQuickControls2Impl/6.12.0/QtQuickControls2Impl/private/qtquickcontrols2implglobal_p.h>
#include <QtQuickControls2Impl/QtQuickControls2Impl>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickControls2Impl/6.12.0/QtQuickControls2Impl/private/qquicktumblerview_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qvariant.h>
#include <QtCore/qrect.h>
#include <QtQuick/QtQuick>
#include <QtQuick/qquickitem.h>

//  Only a class built on QQuickTumblerView may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuickTumblerView : QQuickTumblerView {
  using QQuickTumblerView::geometryChange;
  using QQuickTumblerView::componentComplete;
  using QQuickTumblerView::itemChange;
};

//  const QMetaObject *QQuickTumblerView::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK17QQuickTumblerView10metaObjectEv(
    const QQuickTumblerView *self) {
  return self->metaObject();
}

//  void *QQuickTumblerView::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN17QQuickTumblerView11qt_metacastEPKc(
    QQuickTumblerView *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickTumblerView::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN17QQuickTumblerView11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickTumblerView *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuickTumblerView::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN17QQuickTumblerView2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickTumblerView::tr(s, c, n));
}

//  QQuickTumblerView::QQuickTumblerView(QQuickItem *parent)
extern "C" Q_DECL_EXPORT
QQuickTumblerView *ritual_ZN17QQuickTumblerViewC1EP10QQuickItem(
    QQuickItem *parent) {
  return new QQuickTumblerView(parent);
}

//  QVariant QQuickTumblerView::model() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK17QQuickTumblerView5modelEv(
    const QQuickTumblerView *self) {
  return new QVariant(self->model());
}

//  void QQuickTumblerView::setModel(const QVariant &model)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickTumblerView8setModelERK8QVariant(
    QQuickTumblerView *self,
    const QVariant *model) {
  self->setModel(*model);
}

//  QQmlComponent *QQuickTumblerView::delegate() const
extern "C" Q_DECL_EXPORT
QQmlComponent *ritual_ZNK17QQuickTumblerView8delegateEv(
    const QQuickTumblerView *self) {
  return self->delegate();
}

//  void QQuickTumblerView::setDelegate(QQmlComponent *delegate)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickTumblerView11setDelegateEP13QQmlComponent(
    QQuickTumblerView *self,
    QQmlComponent *delegate) {
  self->setDelegate(delegate);
}

//  QQuickPath *QQuickTumblerView::path() const
extern "C" Q_DECL_EXPORT
QQuickPath *ritual_ZNK17QQuickTumblerView4pathEv(
    const QQuickTumblerView *self) {
  return self->path();
}

//  void QQuickTumblerView::setPath(QQuickPath *path)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickTumblerView7setPathEP10QQuickPath(
    QQuickTumblerView *self,
    QQuickPath *path) {
  self->setPath(path);
}

//  void QQuickTumblerView::modelChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickTumblerView12modelChangedEv(QQuickTumblerView *self) {
  self->modelChanged();
}

//  void QQuickTumblerView::delegateChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickTumblerView15delegateChangedEv(
    QQuickTumblerView *self) {
  self->delegateChanged();
}

//  void QQuickTumblerView::pathChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickTumblerView11pathChangedEv(QQuickTumblerView *self) {
  self->pathChanged();
}

//  void QQuickTumblerView::geometryChange(const QRectF &newGeometry, const
//      QRectF &oldGeometry)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickTumblerView14geometryChangeERK6QRectFS2_(
    QQuickTumblerView *self,
    const QRectF *newGeometry,
    const QRectF *oldGeometry) {
  self->geometryChange(*newGeometry, *oldGeometry);
}

//  void QQuickTumblerView::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickTumblerView17componentCompleteEv(
    QQuickTumblerView *self) {
  self->componentComplete();
}

//  void QQuickTumblerView::itemChange(ItemChange change, const
//      ItemChangeData &data)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickTumblerView10itemChangeEN10QQuickItem10ItemChangeERKNS0_14ItemChangeDataE(
    QQuickTumblerView *self,
    QQuickItem::ItemChange change,
    const QQuickItem::ItemChangeData *data) {
  self->itemChange(change, *data);
}

//  QQuickItem *QQuickTumblerView::view()
extern "C" Q_DECL_EXPORT
QQuickItem *ritual_ZN17QQuickTumblerView4viewEv(QQuickTumblerView *self) {
  return self->view();
}

//  void QQuickTumblerView::createView()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickTumblerView10createViewEv(QQuickTumblerView *self) {
  self->createView();
}

//  void QQuickTumblerView::updateFlickDeceleration()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickTumblerView23updateFlickDecelerationEv(
    QQuickTumblerView *self) {
  self->updateFlickDeceleration();
}

//  void QQuickTumblerView::updateView()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickTumblerView10updateViewEv(QQuickTumblerView *self) {
  self->updateView();
}

//  void QQuickTumblerView::updateModel()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickTumblerView11updateModelEv(QQuickTumblerView *self) {
  self->updateModel();
}

//  void QQuickTumblerView::geometryChange(const QRectF &newGeometry, const
//      QRectF &oldGeometry)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QQuickTumblerView14geometryChangeERK6QRectFS2_(
    QQuickTumblerView *self,
    const QRectF *newGeometry,
    const QRectF *oldGeometry) {
  static_cast<OwnQQuickTumblerView *>(self)->OwnQQuickTumblerView::geometryChange(
      *newGeometry,
      *oldGeometry);
}

//  void QQuickTumblerView::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QQuickTumblerView17componentCompleteEv(
    QQuickTumblerView *self) {
  static_cast<OwnQQuickTumblerView *>(self)->OwnQQuickTumblerView::componentComplete();
}

//  void QQuickTumblerView::itemChange(ItemChange change, const
//      ItemChangeData &data)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QQuickTumblerView10itemChangeEN10QQuickItem10ItemChangeERKNS0_14ItemChangeDataE(
    QQuickTumblerView *self,
    QQuickItem::ItemChange change,
    const QQuickItem::ItemChangeData *data) {
  static_cast<OwnQQuickTumblerView *>(self)->OwnQQuickTumblerView::itemChange(
      change,
      *data);
}

#endif  // QT_CONFIG(quick_listview) && QT_CONFIG(quick_pathview)
