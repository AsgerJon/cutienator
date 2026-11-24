//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qevent.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#if !defined(QT_NO_INPUTMETHOD)
#include <QtGui/qevent.h>
#include <QtCore/qvariant.h>

//  QInputMethodEvent::Attribute::Attribute(AttributeType typ, int s, int l,
//      QVariant val)
extern "C" Q_DECL_EXPORT
QInputMethodEvent::Attribute *ritual_ZN17QInputMethodEvent9AttributeC1ENS_13AttributeTypeEii8QVariant(
    QInputMethodEvent::AttributeType typ,
    int s,
    int l,
    const QVariant *val) {
  return new QInputMethodEvent::Attribute(typ, s, l, *val);
}

//  QInputMethodEvent::Attribute::Attribute(AttributeType typ, int s, int l)
extern "C" Q_DECL_EXPORT
QInputMethodEvent::Attribute *ritual_ZN17QInputMethodEvent9AttributeC1ENS_13AttributeTypeEii(
    QInputMethodEvent::AttributeType typ,
    int s,
    int l) {
  return new QInputMethodEvent::Attribute(typ, s, l);
}

//  QInputMethodEvent::Attribute::~Attribute()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QInputMethodEvent9AttributeD1Ev(
    QInputMethodEvent::Attribute *self) {
  delete self;
}

#endif  // !defined(QT_NO_INPUTMETHOD)
