//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/qqmldebug.h, Qt 6.12.0. Changes made here are lost.
#include <QtQml/qtqmlglobal.h>
#if QT_CONFIG(qml_debug)
#include <QtQml/QtQml>
#include <QtQml/qqmldebug.h>

//  ::QQmlTriviallyDestructibleDebuggingEnabler::QQmlTriviallyDestructibleDeb
//      uggingEnabler(bool printWarning)
extern "C" Q_DECL_EXPORT
::QQmlTriviallyDestructibleDebuggingEnabler *ritual_ZN12_GLOBAL__N_141QQmlTriviallyDestructibleDebuggingEnablerC1Eb(
    bool printWarning) {
  return new ::QQmlTriviallyDestructibleDebuggingEnabler(printWarning);
}

//  ::QQmlTriviallyDestructibleDebuggingEnabler::~QQmlTriviallyDestructibleDe
//      buggingEnabler()
extern "C" Q_DECL_EXPORT
void ritual_ZN041QQmlTriviallyDestructibleDebuggingEnablerD1Ev(
    ::QQmlTriviallyDestructibleDebuggingEnabler *self) {
  delete self;
}

#endif  // QT_CONFIG(qml_debug)
