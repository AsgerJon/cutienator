//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qaccessible.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qaccessible.h>
#include <QtCore/qstring.h>
#include <cstring>

//  A QAccessibleAnnouncementEvent that Python can take functions over in. Every QAccessibleAnnouncementEvent
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQAccessibleAnnouncementEventCall0)(const void *, int *);
class CuteQAccessibleAnnouncementEvent : public QAccessibleAnnouncementEvent {
public:
  using QAccessibleAnnouncementEvent::QAccessibleAnnouncementEvent;
  void *taken[1] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK16QAccessibleEvent19accessibleInterfaceEv")) {
      taken[0] = call;
      return true;
    }
    return false;
  }

  //  QAccessibleInterface *QAccessibleEvent::accessibleInterface() const
  QAccessibleInterface *accessibleInterface() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQAccessibleAnnouncementEventCall0 call = reinterpret_cast<CuteQAccessibleAnnouncementEventCall0>(taken[0]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QAccessibleInterface *>(given);
    }
    return QAccessibleEvent::accessibleInterface();
  }
};

//  QAccessibleAnnouncementEvent::QAccessibleAnnouncementEvent(QObject
//      *object, const QString &message)
extern "C" Q_DECL_EXPORT
QAccessibleAnnouncementEvent *ritual_ZN28QAccessibleAnnouncementEventC1EP7QObjectRK7QString(
    QObject *object,
    const QString *message) {
  return new CuteQAccessibleAnnouncementEvent(object, *message);
}

//  QAccessibleAnnouncementEvent::QAccessibleAnnouncementEvent(QAccessibleInt
//      erface *iface, const QString &message)
extern "C" Q_DECL_EXPORT
QAccessibleAnnouncementEvent *ritual_ZN28QAccessibleAnnouncementEventC1EP20QAccessibleInterfaceRK7QString(
    QAccessibleInterface *iface,
    const QString *message) {
  return new CuteQAccessibleAnnouncementEvent(iface, *message);
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

//  a Python function taken by a CuteQAccessibleAnnouncementEvent, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QAccessibleAnnouncementEvent(
    QAccessibleAnnouncementEvent *self,
    const char *key,
    void *call) {
  return static_cast<CuteQAccessibleAnnouncementEvent *>(self)->take(key, call);
}
