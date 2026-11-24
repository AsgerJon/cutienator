//  Written by dev_tooling.RitualGenerator from the records of
//  QtHttpServer/qhttpserverrouter.h, Qt 6.12.0. Changes made here are lost.
#include <QtHttpServer/qhttpserverrouter.h>
#include <QtCore/qmetatype.h>
#include <QtCore/qanystringview.h>
#include <QtCore/qstring.h>

//  QHttpServerRouterPrivate *QHttpServerRouter::d_func()
extern "C" Q_DECL_EXPORT
QHttpServerRouterPrivate *ritual_ZN17QHttpServerRouter6d_funcEv(
    QHttpServerRouter *self) {
  return self->d_func();
}

//  const QHttpServerRouterPrivate *QHttpServerRouter::d_func() const
extern "C" Q_DECL_EXPORT
const QHttpServerRouterPrivate *ritual_ZNK17QHttpServerRouter6d_funcEv(
    const QHttpServerRouter *self) {
  return self->d_func();
}

//  QHttpServerRouter::QHttpServerRouter(QAbstractHttpServer *server)
extern "C" Q_DECL_EXPORT
QHttpServerRouter *ritual_ZN17QHttpServerRouterC1EP19QAbstractHttpServer(
    QAbstractHttpServer *server) {
  return new QHttpServerRouter(server);
}

//  QHttpServerRouter::~QHttpServerRouter()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QHttpServerRouterD1Ev(QHttpServerRouter *self) {
  delete self;
}

//  void QHttpServerRouter::addConverter(QMetaType metaType, QAnyStringView
//      regexp)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QHttpServerRouter12addConverterE9QMetaType14QAnyStringView(
    QHttpServerRouter *self,
    const QMetaType *metaType,
    const QString *regexp) {
  self->addConverter(*metaType, QAnyStringView(*regexp));
}

//  void QHttpServerRouter::removeConverter(QMetaType metaType)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QHttpServerRouter15removeConverterE9QMetaType(
    QHttpServerRouter *self,
    const QMetaType *metaType) {
  self->removeConverter(*metaType);
}

//  void QHttpServerRouter::clearConverters()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QHttpServerRouter15clearConvertersEv(
    QHttpServerRouter *self) {
  self->clearConverters();
}
