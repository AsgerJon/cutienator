//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickdroparea_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQuick/qtquickglobal.h>
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#if QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickdroparea_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qvariant.h>
#include <QtCore/qurl.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qlist.h>

//  const QMetaObject *QQuickDragEvent::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK15QQuickDragEvent10metaObjectEv(
    const QQuickDragEvent *self) {
  return self->metaObject();
}

//  void *QQuickDragEvent::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN15QQuickDragEvent11qt_metacastEPKc(
    QQuickDragEvent *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickDragEvent::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN15QQuickDragEvent11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickDragEvent *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuickDragEvent::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN15QQuickDragEvent2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickDragEvent::tr(s, c, n));
}

//  void QQuickDragEvent::qt_qmlMarker_uncreatable()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickDragEvent24qt_qmlMarker_uncreatableEv(
    QQuickDragEvent *self) {
  self->qt_qmlMarker_uncreatable();
}

//  QQuickDragEvent::QQuickDragEvent(QQuickDropAreaPrivate *d, QDropEvent
//      *event)
extern "C" Q_DECL_EXPORT
QQuickDragEvent *ritual_ZN15QQuickDragEventC1EP21QQuickDropAreaPrivateP10QDropEvent(
    QQuickDropAreaPrivate *d,
    QDropEvent *event) {
  return new QQuickDragEvent(d, event);
}

//  qreal QQuickDragEvent::x() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK15QQuickDragEvent1xEv(const QQuickDragEvent *self) {
  return self->x();
}

//  qreal QQuickDragEvent::y() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK15QQuickDragEvent1yEv(const QQuickDragEvent *self) {
  return self->y();
}

//  QObject *QQuickDragEvent::source() const
extern "C" Q_DECL_EXPORT
QObject *ritual_ZNK15QQuickDragEvent6sourceEv(const QQuickDragEvent *self) {
  return self->source();
}

//  Qt::DropActions QQuickDragEvent::supportedActions() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK15QQuickDragEvent16supportedActionsEv(
    const QQuickDragEvent *self) {
  return static_cast<int>(self->supportedActions().toInt());
}

//  Qt::DropActions QQuickDragEvent::proposedAction() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK15QQuickDragEvent14proposedActionEv(
    const QQuickDragEvent *self) {
  return static_cast<int>(self->proposedAction().toInt());
}

//  Qt::DropAction QQuickDragEvent::action() const
extern "C" Q_DECL_EXPORT
Qt::DropAction ritual_ZNK15QQuickDragEvent6actionEv(
    const QQuickDragEvent *self) {
  return self->action();
}

//  void QQuickDragEvent::setAction(Qt::DropAction action)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickDragEvent9setActionEN2Qt10DropActionE(
    QQuickDragEvent *self,
    Qt::DropAction action) {
  self->setAction(action);
}

//  void QQuickDragEvent::resetAction()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickDragEvent11resetActionEv(QQuickDragEvent *self) {
  self->resetAction();
}

//  QStringList QQuickDragEvent::keys() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK15QQuickDragEvent4keysEv(
    const QQuickDragEvent *self) {
  return new QList<QString>(self->keys());
}

//  bool QQuickDragEvent::accepted() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QQuickDragEvent8acceptedEv(const QQuickDragEvent *self) {
  return self->accepted();
}

//  void QQuickDragEvent::setAccepted(bool accepted)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickDragEvent11setAcceptedEb(
    QQuickDragEvent *self,
    bool accepted) {
  self->setAccepted(accepted);
}

//  bool QQuickDragEvent::hasColor() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QQuickDragEvent8hasColorEv(const QQuickDragEvent *self) {
  return self->hasColor();
}

//  bool QQuickDragEvent::hasHtml() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QQuickDragEvent7hasHtmlEv(const QQuickDragEvent *self) {
  return self->hasHtml();
}

//  bool QQuickDragEvent::hasText() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QQuickDragEvent7hasTextEv(const QQuickDragEvent *self) {
  return self->hasText();
}

//  bool QQuickDragEvent::hasUrls() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QQuickDragEvent7hasUrlsEv(const QQuickDragEvent *self) {
  return self->hasUrls();
}

//  QVariant QQuickDragEvent::colorData() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK15QQuickDragEvent9colorDataEv(
    const QQuickDragEvent *self) {
  return new QVariant(self->colorData());
}

//  QString QQuickDragEvent::html() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK15QQuickDragEvent4htmlEv(const QQuickDragEvent *self) {
  return new QString(self->html());
}

//  QString QQuickDragEvent::text() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK15QQuickDragEvent4textEv(const QQuickDragEvent *self) {
  return new QString(self->text());
}

//  QList<QUrl> QQuickDragEvent::urls() const
extern "C" Q_DECL_EXPORT
QList<QUrl> *ritual_ZNK15QQuickDragEvent4urlsEv(
    const QQuickDragEvent *self) {
  return new QList<QUrl>(self->urls());
}

//  QStringList QQuickDragEvent::formats() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK15QQuickDragEvent7formatsEv(
    const QQuickDragEvent *self) {
  return new QList<QString>(self->formats());
}

//  QString QQuickDragEvent::getDataAsString(const QString &format) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK15QQuickDragEvent15getDataAsStringERK7QString(
    const QQuickDragEvent *self,
    const QString *format) {
  return new QString(self->getDataAsString(*format));
}

//  QByteArray QQuickDragEvent::getDataAsArrayBuffer(const QString &format)
//      const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK15QQuickDragEvent20getDataAsArrayBufferERK7QString(
    const QQuickDragEvent *self,
    const QString *format) {
  return new QByteArray(self->getDataAsArrayBuffer(*format));
}

//  void QQuickDragEvent::acceptProposedAction()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickDragEvent20acceptProposedActionEv(
    QQuickDragEvent *self) {
  self->acceptProposedAction();
}

//  void QQuickDragEvent::accept()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickDragEvent6acceptEv(QQuickDragEvent *self) {
  self->accept();
}

//  void QQuickDragEvent::accept(Qt::DropAction action)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickDragEvent6acceptEN2Qt10DropActionE(
    QQuickDragEvent *self,
    Qt::DropAction action) {
  self->accept(action);
}

#endif  // QT_CONFIG(quick_draganddrop)
#endif  // QT_CONFIG(quick_draganddrop)
