//  Written by dev_tooling.RitualGenerator from the records of
//  QtWebChannel/6.12.0/QtWebChannel/private/qwebchannel_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtWebChannel/qwebchannel.h>
#include <QtWebChannel/QtWebChannel>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWebChannel/6.12.0/QtWebChannel/private/qwebchannel_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QWebChannel *QWebChannelPrivate::q_func()
extern "C" Q_DECL_EXPORT
QWebChannel *ritual_ZN18QWebChannelPrivate6q_funcEv(
    QWebChannelPrivate *self) {
  return self->q_func();
}

//  const QWebChannel *QWebChannelPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QWebChannel *ritual_ZNK18QWebChannelPrivate6q_funcEv(
    const QWebChannelPrivate *self) {
  return self->q_func();
}

//  void QWebChannelPrivate::init()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QWebChannelPrivate4initEv(QWebChannelPrivate *self) {
  self->init();
}

//  void QWebChannelPrivate::_q_transportDestroyed(QObject *object)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QWebChannelPrivate21_q_transportDestroyedEP7QObject(
    QWebChannelPrivate *self,
    QObject *object) {
  self->_q_transportDestroyed(object);
}
