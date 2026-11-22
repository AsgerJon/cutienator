//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qevent.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qevent.h>
#include <QtCore/qstring.h>

//  QStatusTipEvent *QStatusTipEvent::clone() const
extern "C" Q_DECL_EXPORT
QStatusTipEvent *ritual_ZNK15QStatusTipEvent5cloneEv(
    const QStatusTipEvent *self) {
  return self->clone();
}

//  QStatusTipEvent::~QStatusTipEvent()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QStatusTipEventD1Ev(QStatusTipEvent *self) {
  delete self;
}

//  QStatusTipEvent::QStatusTipEvent(const QString &tip)
extern "C" Q_DECL_EXPORT
QStatusTipEvent *ritual_ZN15QStatusTipEventC1ERK7QString(
    const QString *tip) {
  return new QStatusTipEvent(*tip);
}

//  QString QStatusTipEvent::tip() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK15QStatusTipEvent3tipEv(const QStatusTipEvent *self) {
  return new QString(self->tip());
}
