//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qaccessible.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qaccessible.h>
#include <QtCore/qstring.h>

//  QAccessibleAnnouncementEvent::QAccessibleAnnouncementEvent(QObject
//      *object, const QString &message)
extern "C" Q_DECL_EXPORT
QAccessibleAnnouncementEvent *ritual_ZN28QAccessibleAnnouncementEventC1EP7QObjectRK7QString(
    QObject *object,
    const QString *message) {
  return new QAccessibleAnnouncementEvent(object, *message);
}

//  QAccessibleAnnouncementEvent::QAccessibleAnnouncementEvent(QAccessibleInt
//      erface *iface, const QString &message)
extern "C" Q_DECL_EXPORT
QAccessibleAnnouncementEvent *ritual_ZN28QAccessibleAnnouncementEventC1EP20QAccessibleInterfaceRK7QString(
    QAccessibleInterface *iface,
    const QString *message) {
  return new QAccessibleAnnouncementEvent(iface, *message);
}

//  QAccessibleAnnouncementEvent::~QAccessibleAnnouncementEvent()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QAccessibleAnnouncementEventD1Ev(
    QAccessibleAnnouncementEvent *self) {
  delete self;
}

//  QString QAccessibleAnnouncementEvent::message() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK28QAccessibleAnnouncementEvent7messageEv(
    const QAccessibleAnnouncementEvent *self) {
  return new QString(self->message());
}

//  QAccessible::AnnouncementPoliteness
//      QAccessibleAnnouncementEvent::politeness() const
extern "C" Q_DECL_EXPORT
QAccessible::AnnouncementPoliteness ritual_ZNK28QAccessibleAnnouncementEvent10politenessEv(
    const QAccessibleAnnouncementEvent *self) {
  return self->politeness();
}

//  void QAccessibleAnnouncementEvent::setPoliteness(QAccessible::Announcemen
//      tPoliteness politeness)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QAccessibleAnnouncementEvent13setPolitenessEN11QAccessible22AnnouncementPolitenessE(
    QAccessibleAnnouncementEvent *self,
    QAccessible::AnnouncementPoliteness politeness) {
  self->setPoliteness(politeness);
}
