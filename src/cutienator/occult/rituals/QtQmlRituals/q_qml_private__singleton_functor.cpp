//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/qqmlprivate.h, Qt 6.12.0. Changes made here are lost.
#include <QtQml/qtqmlglobal.h>
#if QT_DEPRECATED_SINCE(6, 3)
#include <QtQml/QtQml>
#include <QtQml/qqmlprivate.h>

//  QObject *QQmlPrivate::SingletonFunctor::operator()(QQmlEngine *a0,
//      QJSEngine *a1)
extern "C" Q_DECL_EXPORT
QObject *ritual_ZN11QQmlPrivate16SingletonFunctorclEP10QQmlEngineP9QJSEngine(
    QQmlPrivate::SingletonFunctor *self,
    QQmlEngine *a0,
    QJSEngine *a1) {
  return self->operator()(a0, a1);
}

//  QQmlPrivate::SingletonFunctor::~SingletonFunctor()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQmlPrivate16SingletonFunctorD1Ev(
    QQmlPrivate::SingletonFunctor *self) {
  delete self;
}

#endif  // QT_DEPRECATED_SINCE(6, 3)
