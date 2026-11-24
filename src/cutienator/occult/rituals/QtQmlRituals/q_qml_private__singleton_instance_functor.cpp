//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/qqmlprivate.h, Qt 6.12.0. Changes made here are lost.
#include <QtQml/QtQml>
#include <QtQml/qqmlprivate.h>

//  QObject *QQmlPrivate::SingletonInstanceFunctor::operator()(QQmlEngine
//      *a0, QJSEngine *a1)
extern "C" Q_DECL_EXPORT
QObject *ritual_ZN11QQmlPrivate24SingletonInstanceFunctorclEP10QQmlEngineP9QJSEngine(
    QQmlPrivate::SingletonInstanceFunctor *self,
    QQmlEngine *a0,
    QJSEngine *a1) {
  return self->operator()(a0, a1);
}

//  QQmlPrivate::SingletonInstanceFunctor::~SingletonInstanceFunctor()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQmlPrivate24SingletonInstanceFunctorD1Ev(
    QQmlPrivate::SingletonInstanceFunctor *self) {
  delete self;
}
