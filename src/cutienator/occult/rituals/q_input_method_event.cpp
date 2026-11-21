//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qevent.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qevent.h>
#include <QtCore/qstring.h>

//  QInputMethodEvent *QInputMethodEvent::clone() const
extern "C" Q_DECL_EXPORT
QInputMethodEvent *ritual_ZNK17QInputMethodEvent5cloneEv(
    const QInputMethodEvent *self) {
  return self->clone();
}

//  QInputMethodEvent::~QInputMethodEvent()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QInputMethodEventD1Ev(QInputMethodEvent *self) {
  delete self;
}

//  QInputMethodEvent::QInputMethodEvent()
extern "C" Q_DECL_EXPORT
QInputMethodEvent *ritual_ZN17QInputMethodEventC1Ev() {
  return new QInputMethodEvent();
}

//  void QInputMethodEvent::setCommitString(const QString &commitString, int
//      replaceFrom, int replaceLength)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QInputMethodEvent15setCommitStringERK7QStringii(
    QInputMethodEvent *self,
    const QString *commitString,
    int replaceFrom,
    int replaceLength) {
  self->setCommitString(*commitString, replaceFrom, replaceLength);
}

//  const QString &QInputMethodEvent::preeditString() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK17QInputMethodEvent13preeditStringEv(
    const QInputMethodEvent *self) {
  return new QString(self->preeditString());
}

//  const QString &QInputMethodEvent::commitString() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK17QInputMethodEvent12commitStringEv(
    const QInputMethodEvent *self) {
  return new QString(self->commitString());
}

//  int QInputMethodEvent::replacementStart() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QInputMethodEvent16replacementStartEv(
    const QInputMethodEvent *self) {
  return self->replacementStart();
}

//  int QInputMethodEvent::replacementLength() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QInputMethodEvent17replacementLengthEv(
    const QInputMethodEvent *self) {
  return self->replacementLength();
}
