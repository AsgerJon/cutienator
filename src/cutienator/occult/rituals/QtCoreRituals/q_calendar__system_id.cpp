//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qcalendar.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qcalendar.h>

//  bool QCalendar::SystemId::isInEnum() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QCalendar8SystemId8isInEnumEv(
    const QCalendar::SystemId *self) {
  return self->isInEnum();
}

//  QCalendar::SystemId::SystemId(QCalendar::System e)
extern "C" Q_DECL_EXPORT
QCalendar::SystemId *ritual_ZN9QCalendar8SystemIdC1ENS_6SystemE(
    QCalendar::System e) {
  return new QCalendar::SystemId(e);
}

//  QCalendar::SystemId::SystemId(size_t i)
extern "C" Q_DECL_EXPORT
QCalendar::SystemId *ritual_ZN9QCalendar8SystemIdC1Em(size_t i) {
  return new QCalendar::SystemId(i);
}

//  QCalendar::SystemId::SystemId()
extern "C" Q_DECL_EXPORT
QCalendar::SystemId *ritual_ZN9QCalendar8SystemIdC1Ev() {
  return new QCalendar::SystemId();
}

//  bool QCalendar::SystemId::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QCalendar8SystemId7isValidEv(
    const QCalendar::SystemId *self) {
  return self->isValid();
}

//  QCalendar::SystemId::~SystemId()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QCalendar8SystemIdD1Ev(QCalendar::SystemId *self) {
  delete self;
}
