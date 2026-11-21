//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qaccessibleobject.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qaccessibleobject.h>
#include <QtCore/qrect.h>
#include <QtCore/qstring.h>

//  bool QAccessibleObject::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QAccessibleObject7isValidEv(const QAccessibleObject *self) {
  return self->isValid();
}

//  QObject *QAccessibleObject::object() const
extern "C" Q_DECL_EXPORT
QObject *ritual_ZNK17QAccessibleObject6objectEv(
    const QAccessibleObject *self) {
  return self->object();
}

//  QRect QAccessibleObject::rect() const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK17QAccessibleObject4rectEv(const QAccessibleObject *self) {
  return new QRect(self->rect());
}

//  void QAccessibleObject::setText(QAccessible::Text t, const QString &text)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QAccessibleObject7setTextEN11QAccessible4TextERK7QString(
    QAccessibleObject *self,
    QAccessible::Text t,
    const QString *text) {
  self->setText(t, *text);
}

//  QAccessibleInterface *QAccessibleObject::childAt(int x, int y) const
extern "C" Q_DECL_EXPORT
QAccessibleInterface *ritual_ZNK17QAccessibleObject7childAtEii(
    const QAccessibleObject *self,
    int x,
    int y) {
  return self->childAt(x, y);
}
