//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/qquickitemgrabresult.h, Qt 6.12.0. Changes made here are lost.
#include <QtQuick/QtQuick>
#include <QtQuick/qquickitemgrabresult.h>
#include <QtCore/qstring.h>
#include <QtGui/qimage.h>
#include <QtCore/qurl.h>

//  Only a class built on QQuickItemGrabResult may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuickItemGrabResult : QQuickItemGrabResult {
  using QQuickItemGrabResult::event;
};

//  const QMetaObject *QQuickItemGrabResult::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK20QQuickItemGrabResult10metaObjectEv(
    const QQuickItemGrabResult *self) {
  return self->metaObject();
}

//  QString QQuickItemGrabResult::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN20QQuickItemGrabResult2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickItemGrabResult::tr(s, c, n));
}

//  void QQuickItemGrabResult::qt_qmlMarker_anonymous()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickItemGrabResult22qt_qmlMarker_anonymousEv(
    QQuickItemGrabResult *self) {
  self->qt_qmlMarker_anonymous();
}

//  QImage QQuickItemGrabResult::image() const
extern "C" Q_DECL_EXPORT
QImage *ritual_ZNK20QQuickItemGrabResult5imageEv(
    const QQuickItemGrabResult *self) {
  return new QImage(self->image());
}

//  QUrl QQuickItemGrabResult::url() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK20QQuickItemGrabResult3urlEv(
    const QQuickItemGrabResult *self) {
  return new QUrl(self->url());
}

//  bool QQuickItemGrabResult::saveToFile(const QString &fileName) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QQuickItemGrabResult10saveToFileERK7QString(
    const QQuickItemGrabResult *self,
    const QString *fileName) {
  return self->saveToFile(*fileName);
}

//  bool QQuickItemGrabResult::saveToFile(const QUrl &fileName) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QQuickItemGrabResult10saveToFileERK4QUrl(
    const QQuickItemGrabResult *self,
    const QUrl *fileName) {
  return self->saveToFile(*fileName);
}

//  bool QQuickItemGrabResult::event(QEvent *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN20QQuickItemGrabResult5eventEP6QEvent(
    QQuickItemGrabResult *self,
    QEvent *a0) {
  return self->event(a0);
}

//  void QQuickItemGrabResult::setup()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickItemGrabResult5setupEv(QQuickItemGrabResult *self) {
  self->setup();
}

//  void QQuickItemGrabResult::render()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickItemGrabResult6renderEv(QQuickItemGrabResult *self) {
  self->render();
}

//  QQuickItemGrabResult::QQuickItemGrabResult(QObject *parent)
extern "C" Q_DECL_EXPORT
QQuickItemGrabResult *ritual_ZN20QQuickItemGrabResultC1EP7QObject(
    QObject *parent) {
  return new QQuickItemGrabResult(parent);
}

//  bool QQuickItemGrabResult::event(QEvent *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN20QQuickItemGrabResult5eventEP6QEvent(
    QQuickItemGrabResult *self,
    QEvent *a0) {
  return static_cast<OwnQQuickItemGrabResult *>(self)->OwnQQuickItemGrabResult::event(
      a0);
}
