//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qevent.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qevent.h>
#include <QtCore/qvariant.h>

//  QInputMethodQueryEvent *QInputMethodQueryEvent::clone() const
extern "C" Q_DECL_EXPORT
QInputMethodQueryEvent *ritual_ZNK22QInputMethodQueryEvent5cloneEv(
    const QInputMethodQueryEvent *self) {
  return self->clone();
}

//  QInputMethodQueryEvent::~QInputMethodQueryEvent()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QInputMethodQueryEventD1Ev(QInputMethodQueryEvent *self) {
  delete self;
}

//  QInputMethodQueryEvent::QInputMethodQueryEvent(Qt::InputMethodQueries
//      queries)
extern "C" Q_DECL_EXPORT
QInputMethodQueryEvent *ritual_ZN22QInputMethodQueryEventC1E6QFlagsIN2Qt16InputMethodQueryEE(
    int queries) {
  return new QInputMethodQueryEvent(
      QFlags<Qt::InputMethodQuery>::fromInt(queries));
}

//  Qt::InputMethodQueries QInputMethodQueryEvent::queries() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK22QInputMethodQueryEvent7queriesEv(
    const QInputMethodQueryEvent *self) {
  return static_cast<int>(self->queries().toInt());
}

//  void QInputMethodQueryEvent::setValue(Qt::InputMethodQuery query, const
//      QVariant &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QInputMethodQueryEvent8setValueEN2Qt16InputMethodQueryERK8QVariant(
    QInputMethodQueryEvent *self,
    Qt::InputMethodQuery query,
    const QVariant *value) {
  self->setValue(query, *value);
}

//  QVariant QInputMethodQueryEvent::value(Qt::InputMethodQuery query) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK22QInputMethodQueryEvent5valueEN2Qt16InputMethodQueryE(
    const QInputMethodQueryEvent *self,
    Qt::InputMethodQuery query) {
  return new QVariant(self->value(query));
}
