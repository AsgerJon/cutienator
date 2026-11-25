//  Written by hand on 2026-11-25 from
//  QtCore/6.12.0/QtCore/private/qcore_mac_p.h, Qt 6.12.0, as the Qt of
//  macOS installs it. Kept as it is when the generator runs again.
//  Not written: the constructor taking a 'QMacKeyValueObserver &&',
//  'operator=' and 'swap'.
#include <QtCore/qglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if defined(Q_OS_DARWIN)
#include <QtCore/6.12.0/QtCore/private/qcore_mac_p.h>

//  QMacKeyValueObserver::QMacKeyValueObserver()
extern "C" Q_DECL_EXPORT
QMacKeyValueObserver *ritual_ZN20QMacKeyValueObserverC1Ev() {
  return new QMacKeyValueObserver();
}

//  QMacKeyValueObserver::QMacKeyValueObserver(const QMacKeyValueObserver
//      &other)
extern "C" Q_DECL_EXPORT
QMacKeyValueObserver *ritual_ZN20QMacKeyValueObserverC1ERKS_(
    const QMacKeyValueObserver *other) {
  return new QMacKeyValueObserver(*other);
}

//  QMacKeyValueObserver::~QMacKeyValueObserver()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QMacKeyValueObserverD1Ev(QMacKeyValueObserver *self) {
  delete self;
}

//  void QMacKeyValueObserver::removeObserver()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QMacKeyValueObserver14removeObserverEv(
    QMacKeyValueObserver *self) {
  self->removeObserver();
}

#endif  // defined(Q_OS_DARWIN)
