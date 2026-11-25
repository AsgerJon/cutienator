//  Written by hand on 2026-11-25 from
//  QtCore/6.12.0/QtCore/private/qwineventnotifier_p.h, Qt 6.12.0, as the
//  Qt of Windows installs it. Kept as it is when the generator runs
//  again. Qt's library offers nothing of this class, so only what its
//  header writes out is called, and its virtual destructor through the
//  object. Not written: the constructors and 'waitCallback'.
#include <QtCore/qglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if defined(Q_OS_WIN)
#include <QtCore/6.12.0/QtCore/private/qwineventnotifier_p.h>

//  QWinEventNotifier *QWinEventNotifierPrivate::q_func()
extern "C" Q_DECL_EXPORT
QWinEventNotifier *ritual_ZN24QWinEventNotifierPrivate6q_funcEv(
    QWinEventNotifierPrivate *self) {
  return self->q_func();
}

//  const QWinEventNotifier *QWinEventNotifierPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QWinEventNotifier *ritual_ZNK24QWinEventNotifierPrivate6q_funcEv(
    const QWinEventNotifierPrivate *self) {
  return self->q_func();
}

//  QWinEventNotifierPrivate::~QWinEventNotifierPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QWinEventNotifierPrivateD1Ev(QWinEventNotifierPrivate *self) {
  delete self;
}

#endif  // defined(Q_OS_WIN)
