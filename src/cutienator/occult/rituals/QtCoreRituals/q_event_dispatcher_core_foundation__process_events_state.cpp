//  Written by hand on 2026-11-25 from
//  QtCore/6.12.0/QtCore/private/qeventdispatcher_cf_p.h, Qt 6.12.0, as
//  the Qt of macOS installs it. Kept as it is when the generator runs
//  again.
//  Not written: 'operator='.
#include <QtCore/qglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if defined(Q_OS_DARWIN)
#include <QtCore/6.12.0/QtCore/private/qeventdispatcher_cf_p.h>

//  QEventDispatcherCoreFoundation::ProcessEventsState::ProcessEventsState(QE
//      ventLoop::ProcessEventsFlags f)
extern "C" Q_DECL_EXPORT
QEventDispatcherCoreFoundation::ProcessEventsState *ritual_ZN30QEventDispatcherCoreFoundation18ProcessEventsStateC1E6QFlagsIN10QEventLoop17ProcessEventsFlagEE(
    int f) {
  return new QEventDispatcherCoreFoundation::ProcessEventsState(
      QFlags<QEventLoop::ProcessEventsFlag>::fromInt(f));
}

//  QEventDispatcherCoreFoundation::ProcessEventsState::ProcessEventsState(co
//      nst ProcessEventsState &other)
extern "C" Q_DECL_EXPORT
QEventDispatcherCoreFoundation::ProcessEventsState *ritual_ZN30QEventDispatcherCoreFoundation18ProcessEventsStateC1ERKS0_(
    const QEventDispatcherCoreFoundation::ProcessEventsState *other) {
  return new QEventDispatcherCoreFoundation::ProcessEventsState(*other);
}

//  QEventDispatcherCoreFoundation::ProcessEventsState::~ProcessEventsState()
extern "C" Q_DECL_EXPORT
void ritual_ZN30QEventDispatcherCoreFoundation18ProcessEventsStateD1Ev(
    QEventDispatcherCoreFoundation::ProcessEventsState *self) {
  delete self;
}

#endif  // defined(Q_OS_DARWIN)
