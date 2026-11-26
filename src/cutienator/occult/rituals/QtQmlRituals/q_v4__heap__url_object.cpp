//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4urlobject_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4urlobject_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qurl.h>

//  void QV4::Heap::UrlObject::markObjects(Heap::Base *b, MarkStack *stack)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV44Heap9UrlObject11markObjectsEPNS0_4BaseEPNS_9MarkStackE(
    QV4::Heap::Base *b,
    QV4::MarkStack *stack) {
  QV4::Heap::UrlObject::markObjects(b, stack);
}

//  void QV4::Heap::UrlObject::init()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV44Heap9UrlObject4initEv(QV4::Heap::UrlObject *self) {
  self->init();
}

//  void QV4::Heap::UrlObject::init(const QUrl &url)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV44Heap9UrlObject4initERK4QUrl(
    QV4::Heap::UrlObject *self,
    const QUrl *url) {
  self->init(*url);
}

//  void QV4::Heap::UrlObject::destroy()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV44Heap9UrlObject7destroyEv(QV4::Heap::UrlObject *self) {
  self->destroy();
}

//  QUrl QV4::Heap::UrlObject::url() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK3QV44Heap9UrlObject3urlEv(const QV4::Heap::UrlObject *self) {
  return new QUrl(self->url());
}

//  void QV4::Heap::UrlObject::setUrl(QUrl &&url)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV44Heap9UrlObject6setUrlEO4QUrl(
    QV4::Heap::UrlObject *self,
    QUrl *url) {
  self->setUrl(std::move(*url));
}

//  QV4::Heap::UrlObject as the QV4::Heap::UrlObjectData it is built on
extern "C" Q_DECL_EXPORT
QV4::Heap::UrlObjectData *ritual_cast_QV4_Heap_UrlObject_QV4_Heap_UrlObjectData(
    QV4::Heap::UrlObject *self) {
  return static_cast<QV4::Heap::UrlObjectData *>(self);
}
