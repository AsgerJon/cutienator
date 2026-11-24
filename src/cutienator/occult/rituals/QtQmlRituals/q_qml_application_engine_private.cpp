//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qqmlapplicationengine_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#include <QtQml/qqmlapplicationengine.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmlapplicationengine_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qurl.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qanystringview.h>
#include <QtCore/qstring.h>

//  QQmlApplicationEngine *QQmlApplicationEnginePrivate::q_func()
extern "C" Q_DECL_EXPORT
QQmlApplicationEngine *ritual_ZN28QQmlApplicationEnginePrivate6q_funcEv(
    QQmlApplicationEnginePrivate *self) {
  return self->q_func();
}

//  const QQmlApplicationEngine *QQmlApplicationEnginePrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QQmlApplicationEngine *ritual_ZNK28QQmlApplicationEnginePrivate6q_funcEv(
    const QQmlApplicationEnginePrivate *self) {
  return self->q_func();
}

//  QQmlApplicationEnginePrivate::QQmlApplicationEnginePrivate()
extern "C" Q_DECL_EXPORT
QQmlApplicationEnginePrivate *ritual_ZN28QQmlApplicationEnginePrivateC1Ev() {
  return new QQmlApplicationEnginePrivate();
}

//  QQmlApplicationEnginePrivate::~QQmlApplicationEnginePrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QQmlApplicationEnginePrivateD1Ev(
    QQmlApplicationEnginePrivate *self) {
  delete self;
}

//  void QQmlApplicationEnginePrivate::ensureInitialized()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QQmlApplicationEnginePrivate17ensureInitializedEv(
    QQmlApplicationEnginePrivate *self) {
  self->ensureInitialized();
}

//  void QQmlApplicationEnginePrivate::init()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QQmlApplicationEnginePrivate4initEv(
    QQmlApplicationEnginePrivate *self) {
  self->init();
}

//  void QQmlApplicationEnginePrivate::cleanUp()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QQmlApplicationEnginePrivate7cleanUpEv(
    QQmlApplicationEnginePrivate *self) {
  self->cleanUp();
}

//  void QQmlApplicationEnginePrivate::startLoad(const QUrl &url, const
//      QByteArray &data, bool dataFlag)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QQmlApplicationEnginePrivate9startLoadERK4QUrlRK10QByteArrayb(
    QQmlApplicationEnginePrivate *self,
    const QUrl *url,
    const QByteArray *data,
    bool dataFlag) {
  self->startLoad(*url, *data, dataFlag);
}

//  void QQmlApplicationEnginePrivate::startLoad(QAnyStringView uri,
//      QAnyStringView type)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QQmlApplicationEnginePrivate9startLoadE14QAnyStringViewS0_(
    QQmlApplicationEnginePrivate *self,
    const QString *uri,
    const QString *type) {
  self->startLoad(QAnyStringView(*uri), QAnyStringView(*type));
}

//  void QQmlApplicationEnginePrivate::_q_loadTranslations()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QQmlApplicationEnginePrivate19_q_loadTranslationsEv(
    QQmlApplicationEnginePrivate *self) {
  self->_q_loadTranslations();
}

//  void QQmlApplicationEnginePrivate::finishLoad(QQmlComponent *component)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QQmlApplicationEnginePrivate10finishLoadEP13QQmlComponent(
    QQmlApplicationEnginePrivate *self,
    QQmlComponent *component) {
  self->finishLoad(component);
}

//  void QQmlApplicationEnginePrivate::ensureLoadingFinishes(QQmlComponent
//      *component)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QQmlApplicationEnginePrivate21ensureLoadingFinishesEP13QQmlComponent(
    QQmlApplicationEnginePrivate *self,
    QQmlComponent *component) {
  self->ensureLoadingFinishes(component);
}

//  void QQmlApplicationEnginePrivate::updateTranslationDirectory(const QUrl
//      &url)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QQmlApplicationEnginePrivate26updateTranslationDirectoryERK4QUrl(
    QQmlApplicationEnginePrivate *self,
    const QUrl *url) {
  self->updateTranslationDirectory(*url);
}
