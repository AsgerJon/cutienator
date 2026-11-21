//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qevent.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qevent.h>
#include <QtCore/qstring.h>

//  QWhatsThisClickedEvent *QWhatsThisClickedEvent::clone() const
extern "C" Q_DECL_EXPORT
QWhatsThisClickedEvent *ritual_ZNK22QWhatsThisClickedEvent5cloneEv(
    const QWhatsThisClickedEvent *self) {
  return self->clone();
}

//  QWhatsThisClickedEvent::~QWhatsThisClickedEvent()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QWhatsThisClickedEventD1Ev(QWhatsThisClickedEvent *self) {
  delete self;
}

//  QWhatsThisClickedEvent::QWhatsThisClickedEvent(const QString &href)
extern "C" Q_DECL_EXPORT
QWhatsThisClickedEvent *ritual_ZN22QWhatsThisClickedEventC1ERK7QString(
    const QString *href) {
  return new QWhatsThisClickedEvent(*href);
}

//  QString QWhatsThisClickedEvent::href() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK22QWhatsThisClickedEvent4hrefEv(
    const QWhatsThisClickedEvent *self) {
  return new QString(self->href());
}
