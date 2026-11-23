//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qinputcontrol_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtGui/QtGui>
#include <QtGui/6.12.0/QtGui/private/qinputcontrol_p.h>
#include <QtCore/qstring.h>
#include <QtCore/qvariant.h>

//  const QMetaObject *QInputControl::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK13QInputControl10metaObjectEv(
    const QInputControl *self) {
  return self->metaObject();
}

//  QString QInputControl::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN13QInputControl2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QInputControl::tr(s, c, n));
}

//  QInputControl::QInputControl(Type type, QObject *parent)
extern "C" Q_DECL_EXPORT
QInputControl *ritual_ZN13QInputControlC1ENS_4TypeEP7QObject(
    QInputControl::Type type,
    QObject *parent) {
  return new QInputControl(type, parent);
}

//  bool QInputControl::isAcceptableInput(const QKeyEvent *event) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QInputControl17isAcceptableInputEPK9QKeyEvent(
    const QInputControl *self,
    const QKeyEvent *event) {
  return self->isAcceptableInput(event);
}

//  bool QInputControl::isCommonTextEditShortcut(const QKeyEvent *ke)
extern "C" Q_DECL_EXPORT
bool ritual_ZN13QInputControl24isCommonTextEditShortcutEPK9QKeyEvent(
    const QKeyEvent *ke) {
  return QInputControl::isCommonTextEditShortcut(ke);
}

//  QVariant QInputControl::selectionWrapper(QMimeData *mimeData)
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZN13QInputControl16selectionWrapperEP9QMimeData(
    QMimeData *mimeData) {
  return new QVariant(QInputControl::selectionWrapper(mimeData));
}

//  QMimeData *QInputControl::mimeDataForInputEvent(QInputMethodEvent *event)
extern "C" Q_DECL_EXPORT
QMimeData *ritual_ZN13QInputControl21mimeDataForInputEventEP17QInputMethodEvent(
    QInputMethodEvent *event) {
  return QInputControl::mimeDataForInputEvent(event);
}
